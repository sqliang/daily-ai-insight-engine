"""
pipeline/extraction/base_info/extractor.py — Stage 2a: BaseInfo 单文件提取

对单个 .md 文件执行 BaseInfo 提取的完整流水线：

    read_frontmatter → determine_missing_fields → infer_source_type
    → Agent(缺失字段兜底) → merge → write_frontmatter

设计决策：
    - id/ title/ source/ published/ created 在 Stage 1 已写入 frontmatter，此处只补填
    - source_type 优先从目录名推断（零 Agent），仅兜底时调用 Agent
    - 已有字段绝不覆盖（merge 策略：existing_fm | new_fields）
"""

import logging
from pathlib import Path
from typing import Optional

from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter
from pipeline.utils.id_utils import generate_id

from ...schemas.base_info import BaseInfo
from ...core.agent import (
    AgentCallError,
    StageResult,
    call_agent_with_retry,
    parse_json_response,
)
from .prompts import get_base_info_system_prompt, build_base_info_user_prompt
from .source_type import infer_source_type

logger = logging.getLogger(__name__)

# =============================================================================
# 缺失字段检测
# =============================================================================

# BaseInfo 模型中需要提取的字段名集合
_BASE_INFO_FIELDS = set(BaseInfo.model_fields.keys())


def determine_missing_fields(existing_fm: dict) -> list[str]:
    """
    对比已有 frontmatter 与 BaseInfo schema，找出缺失的字段。

    对比逻辑：
        - 遍历 BaseInfo.model_fields 中的所有字段
        - 如果字段（或其 camelCase 别名）已存在于 existing_fm 中 → 跳过
        - 否则加入缺失列表

    特殊处理：
        - id: 通过 generate_id() 确定性生成，不在此处处理
        - sourceType (camelCase): 检查 frontmatter 中是否有 sourceType 或 source_type

    参数：
        existing_fm: 已有 frontmatter 字典

    返回：
        缺失字段名列表（使用 Python 字段名，如 source_type）
    """
    missing: list[str] = []

    for field_name in _BASE_INFO_FIELDS:
        # 跳过 id —— 由 generate_id() 确定性生成
        if field_name == "id":
            continue

        field_info = BaseInfo.model_fields[field_name]

        if field_name in existing_fm:
            continue

        alias = field_info.alias if field_info.alias else None
        if alias and alias in existing_fm:
            continue

        missing.append(field_name)

    return missing


# =============================================================================
# 空 body 日志辅助
# =============================================================================

def _log_empty_body_skip(file_path: str, fm: dict) -> None:
    """根据 extraction_status 输出有意义的跳过原因日志。"""
    status = fm.get("extraction_status", "")
    if status == "failed":
        logger.warning("正文为空（Stage 1 抓取失败），跳过 Agent 调用: %s", file_path)
    elif status == "partial":
        logger.warning("正文为空（Stage 1 仅获取摘要），跳过 Agent 调用: %s", file_path)
    else:
        logger.warning("正文为空，跳过 Agent 调用: %s", file_path)


# =============================================================================
# Agent 兜底：对工程手段无法补全的缺失字段调用 LLM 提取
# =============================================================================

async def _extract_missing_fields_via_agent(
    *,
    input_path: Path,
    output_path: Path,
    existing_fm: dict,
    body: str,
    missing_fields: list[str],
    fields_written: list[str],
    article_id: str,
    model: Optional[str] = None,
) -> StageResult:
    """
    BaseInfo 提取的最后手段：调用 Agent 补全工程手段无法解决的缺失字段。

    正常流程中所有字段应在 Stage 1 和 source_type 推断阶段完成，
    该函数仅在遇到脏数据（旧文件缺字段、config 未覆盖的边缘 case）时被调用，
    因此绝大部分文件的 token 消耗为零。

    合并时防御性过滤 field_name in missing_fields，
    确保 Agent 幻觉不会覆盖 Stage 1 的权威数据。
    """
    input_str = str(input_path)
    output_str = str(output_path)

    # =====================================================================
    # 兜底：调用 Agent 提取仍缺失的字段
    #
    # 到达这里的条件：
    #   1. 文件正文非空（空 body 在上游已 return）
    #   2. missing_fields 非空 — source_type 从目录名推断成功后，理论上其他字段
    #      （id/title/source/published/created）在 Stage 1 ingest 已写入 frontmatter，
    #      但个别脏数据仍可能缺少字段
    #   3. 缺失字段无法通过工程手段补全 — source_type 可以查 config.yaml 映射，
    #      但 title 等字段只能从原文提取
    #
    # 为什么是"兜底"而非"主流程"：
    #   - Stage 1 ingest 已将 id/title/source/published/created 写入 frontmatter
    #   - source_type 在上游通过目录名 → config.yaml 映射推断完成（零 token）
    #   - 只有脏数据才会走到这里，正常文件的 Agent 调用在此阶段完全跳过
    #
    # Agent 调用策略：
    #   - call_agent_with_retry 内置指数退避重试（最多 3 次）
    #   - 只提取 missing_fields 中列出的字段（节省 token）
    #   - 正文截断至 8000 字符（prompts.py 中控制）
    # =====================================================================
    extraction_status = existing_fm.get("extraction_status", "success")
    status_note = ""
    if extraction_status == "failed":
        status_note = "（Stage 1 抓取失败，正文质量低）"
    elif extraction_status == "partial":
        status_note = "（Stage 1 仅获取摘要，正文不完整）"
    logger.info(
        "提取 BaseInfo: %s (缺失字段: %s)%s",
        input_str, ", ".join(missing_fields), status_note,
    )

    try:
        system_prompt = get_base_info_system_prompt()
        user_prompt = build_base_info_user_prompt(
            missing_fields=missing_fields,
            body=body,
        )
        response_text = await call_agent_with_retry(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            max_turns=3,
        )
        extracted_data = parse_json_response(response_text)
    except AgentCallError as exc:
        logger.error("Agent 调用失败 %s: %s", input_str, exc.message)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=exc.message,
        )
    except ValueError as exc:
        logger.error("JSON 解析失败 %s: %s", input_str, exc)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=f"JSON 解析失败: {exc}",
        )

    # =====================================================================
    # 合并 Agent 返回的字段到 frontmatter（不覆盖已有字段）
    #
    # 为什么再次检查 field_name in missing_fields：
    #   Agent 可能返回它认为是缺失但实际上 frontmatter 已有的字段。
    #   这里做防御性过滤，确保"已有字段绝不覆盖"被严格执行，
    #   防止 Agent 幻觉产生的值覆盖 Stage 1 的权威数据。
    # =====================================================================
    if article_id:
        existing_fm["id"] = article_id
        fields_written.append("id")

    for field_name, value in extracted_data.items():
        if field_name in missing_fields:
            existing_fm[field_name] = value
            fields_written.append(field_name)

    # 标记 pipeline_stage，供下游 Stage 2b 做前置检查：
    #   Stage 2b 会读取 frontmatter 中的 pipeline_stage 字段，
    #   确认文件已通过 Stage 2a 处理后才执行 FactExtraction
    existing_fm["pipeline_stage"] = "base_info_extracted"
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
        "BaseInfo 提取完成: %s → %s (字段: %s)",
        input_str, output_str, ", ".join(fields_written),
    )
    return StageResult(
        input_path=input_str,
        output_path=output_str,
        success=True,
        fields_extracted=fields_written,
    )


# =============================================================================
# 单文件 BaseInfo 提取流水线
# =============================================================================

async def extract_base_info(
    input_path: Path,
    output_path: Path,
    *,
    model: Optional[str] = None,
    skip_existing: bool = True,
) -> StageResult:
    """
    对单个 .md 文件执行 BaseInfo 提取。

    处理流程：
        1. read_frontmatter(input_path) → (existing_fm, body)
        2. 生成 id（从 source URL 确定性计算）
        3. determine_missing_fields(existing_fm) → missing 列表
        4. 如果无缺失字段 → 直接写入（仅补充 id），标记 skipped
        5. 如果 body 为空 → 跳过 Agent 调用，仅写入 id
        6. 构建 prompt → 调用 Agent → 解析 JSON
        7. 合并 new_fields 到 existing_fm（不覆盖已有字段）
        8. write_frontmatter(output_path, merged_fm, body)

    如果 skip_existing=True 且 output_path 已存在且已有所有 BaseInfo 字段，
    则跳过整个处理（返回 StageResult(skipped=True)）。

    参数：
        input_path: 输入 .md 文件路径
        output_path: 输出 .md 文件路径
        model: LLM 模型名称
        skip_existing: 是否跳过已处理过的文件

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

    # --- 获取文章 ID ---
    article_id = existing_fm.get("id", "")
    if not article_id:
        source_url = existing_fm.get("source", "")
        article_id = generate_id(source_url) if source_url else ""
        logger.debug("旧文件缺少 id，回退生成: %s → %s", input_str, article_id)

    # --- 检查是否需要跳过 ---
    if skip_existing and output_path.exists():
        try:
            out_fm, _ = read_frontmatter(output_path)
            if out_fm.get("id") and determine_missing_fields(out_fm) == []:
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
        _log_empty_body_skip(input_str, existing_fm)
        if article_id:
            existing_fm["id"] = article_id
        try:
            write_frontmatter(output_path, existing_fm, body)
        except Exception as exc:
            return StageResult(
                input_path=input_str,
                output_path=output_str,
                success=False,
                error=f"写入文件失败: {exc}",
            )
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=True,
            fields_extracted=["id"] if article_id else [],
            skipped=True,
        )

    # --- 初始化字段写入追踪 ---
    fields_written: list[str] = []

    # --- 确定缺失字段 ---
    missing_fields = determine_missing_fields(existing_fm)

    # --- 尝试从目录名推断 source_type（零 Agent 调用） ---
    if "source_type" in missing_fields:
        inferred_type = infer_source_type(input_path)
        if inferred_type:
            existing_fm["source_type"] = inferred_type
            missing_fields.remove("source_type")
            fields_written.append("source_type")
            logger.info(
                "source_type 从目录名推断: %s → %s", input_path.parent.name, inferred_type
            )

    # 如果所有字段都已存在（只需补充 id）
    if not missing_fields:
        if article_id:
            existing_fm["id"] = article_id
        try:
            write_frontmatter(output_path, existing_fm, body)
        except Exception as exc:
            return StageResult(
                input_path=input_str,
                output_path=output_str,
                success=False,
                error=f"写入文件失败: {exc}",
            )
        logger.info("所有 BaseInfo 字段已存在: %s", input_str)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=True,
            fields_extracted=["id"] if article_id else [],
            skipped=True,
        )

    return await _extract_missing_fields_via_agent(
        input_path=input_path,
        output_path=output_path,
        existing_fm=existing_fm,
        body=body,
        missing_fields=missing_fields,
        fields_written=fields_written,
        article_id=article_id,
        model=model,
    )
