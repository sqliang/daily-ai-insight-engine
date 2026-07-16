"""
pipeline/extraction/fact_extraction/extractor.py — Stage 2b: FactExtraction 单文件提取

对单个 .md 文件执行 FactExtraction 提取的完整流水线：

    read_frontmatter → skip check → Agent 调用 → validate → merge → write_frontmatter

设计决策：
    - 所有 FactExtraction 字段都是新字段（Stage 1 不会产生这些字段）
    - 输入来自 data/02_extracted/（已由 Stage 2a 丰富了 BaseInfo）
    - Pydantic 校验失败时由 validator 进行模糊枚举修复
    - 正文空时跳过 Agent 调用
"""

import logging
from pathlib import Path
from typing import Optional

from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter

from ...core.agent import (
    AgentCallError,
    StageResult,
    call_agent_with_retry,
    parse_json_response,
)
from ...schemas.fact_extraction import SpecializedTags
from .prompts import get_fact_extraction_system_prompt, build_fact_extraction_user_prompt
from .validator import _validate_fact_extraction, _FACT_EXTRACTION_FIELDS

logger = logging.getLogger(__name__)


# =============================================================================
# 空 body 日志辅助
# =============================================================================

def _log_empty_body_skip_fact(file_path: str, fm: dict) -> None:
    """根据 extraction_status 输出有意义的跳过原因日志。"""
    status = fm.get("extraction_status", "")
    if status == "failed":
        logger.warning("正文为空（Stage 1 抓取失败），跳过 FactExtraction: %s", file_path)
    elif status == "partial":
        logger.warning("正文为空（Stage 1 仅获取摘要），跳过 FactExtraction: %s", file_path)
    else:
        logger.warning("正文为空，跳过 FactExtraction: %s", file_path)


# =============================================================================
# 单文件 FactExtraction 提取流水线
# =============================================================================

async def extract_fact_extraction(
    input_path: Path,
    output_path: Path,
    *,
    model: Optional[str] = None,
    skip_existing: bool = True,
) -> StageResult:
    """
    对单个 .md 文件执行 FactExtraction 提取。

    处理流程：
        1. read_frontmatter(input_path) → (existing_fm, body)
        2. skip_existing 检查：输出文件已存在且包含所有 FactExtraction 字段 → 跳过
        3. body 为空 → 跳过 Agent 调用
        4. 构建 prompt（包含 title、source、body）
        5. 调用 Agent → 解析 JSON → Pydantic 校验
        6. 将 FactExtraction 字段合并到 existing_fm
        7. write_frontmatter(output_path, merged_fm, body)

    参数：
        input_path: 输入 .md 文件路径（通常来自 data/02_extracted/）
        output_path: 输出 .md 文件路径（原位更新）
        model: LLM 模型名称
        skip_existing: 是否跳过已提取的文件

    返回：
        StageResult 记录提取结果
    """
    input_str = str(input_path)
    output_str = str(output_path)

    # --- 读取 frontmatter ---
    try:
        existing_fm, body = read_frontmatter(input_path)
    except Exception as exc:
        logger.error("读取文件失败 %s: %s", input_str, exc)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=f"读取文件失败: {exc}",
        )

    # --- 检查是否需要跳过 ---
    if skip_existing and output_path.exists():
        try:
            out_fm, _ = read_frontmatter(output_path)
            if out_fm.get("id") and _FACT_EXTRACTION_FIELDS.issubset(set(out_fm.keys())):
                logger.info("跳过（id=%s 已提取）: %s", out_fm.get("id"), input_str)
                return StageResult(
                    input_path=input_str,
                    output_path=output_str,
                    success=True,
                    fields_extracted=[],
                    skipped=True,
                )
        except Exception:
            pass

    # --- 空 body 处理 ---
    if not body.strip():
        _log_empty_body_skip_fact(input_str, existing_fm)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=True,
            fields_extracted=[],
            skipped=True,
        )

    # --- extraction_status == "failed" → 跳过 Agent 调用 ---
    extraction_status = existing_fm.get("extraction_status", "success")
    if extraction_status == "failed":
        logger.warning(
            "跳过 FactExtraction（Stage 1 抓取失败，正文仅为错误信息）: %s", input_str,
        )
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=True,
            fields_extracted=[],
            skipped=True,
        )

    # --- 调用 Agent 提取 ---
    title = existing_fm.get("title", "")
    source = existing_fm.get("source", "")

    status_note = ""
    if extraction_status == "partial":
        status_note = "（Stage 1 仅获取摘要，正文不完整）"
    logger.info("提取 FactExtraction: %s%s", input_str, status_note)

    try:
        system_prompt = get_fact_extraction_system_prompt()
        user_prompt = build_fact_extraction_user_prompt(
            title=title,
            source=source,
            body=body,
        )

        response_text = await call_agent_with_retry(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            max_turns=3,
        )

        extracted_data = parse_json_response(response_text)
        fact_extraction = _validate_fact_extraction(extracted_data)

    except AgentCallError as exc:
        logger.error("Agent 调用失败 %s: %s", input_str, exc.message)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=exc.message,
        )
    except ValueError as exc:
        logger.error("解析/校验失败 %s: %s", input_str, exc)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=f"解析/校验失败: {exc}",
        )

    # --- 合并 FactExtraction 字段到 frontmatter ---
    fields_written: list[str] = []
    fe_dict = fact_extraction.model_dump(mode="json", by_alias=False)
    article_id = existing_fm.get("id")

    # Stage 2 Agent 不一定知道 frontmatter id，这里统一回填，保证后续引用可追溯。
    for mention in fe_dict.get("object_mentions", []):
        if isinstance(mention, dict) and not mention.get("article_id"):
            mention["article_id"] = article_id

    for field_name, value in fe_dict.items():
        existing_fm[field_name] = value
        fields_written.append(field_name)

    # 专题对象现在统一通过 objectMentions 表达（见 prompts.py），不再使用旧版
    # specializedTags 字段。若旧提示词或模型意外返回 specializedTags，此处忽略，
    # 以保证前端专题洞察的数据源口径一致。

    existing_fm["pipeline_stage"] = "fact_extracted"
    fields_written.append("pipeline_stage")

    # --- 写入输出文件 ---
    try:
        write_frontmatter(output_path, existing_fm, body)
    except Exception as exc:
        logger.error("写入输出文件失败 %s: %s", output_str, exc)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=f"写入文件失败: {exc}",
        )

    logger.info(
        "FactExtraction 提取完成: %s → %s (字段: %s)",
        input_str, output_str, ", ".join(fields_written),
    )
    return StageResult(
        input_path=input_str,
        output_path=output_str,
        success=True,
        fields_extracted=fields_written,
    )
