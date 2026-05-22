"""
pipeline/extraction/agent/base_info_agent.py — Stage 2a: 基础元信息提取

功能：
    - generate_id(): 已在 pipeline.core.id_utils 中统一实现，此处不再重复
    - determine_missing_fields(): 对比已有 frontmatter 与 BaseInfo schema，找出缺失字段
    - _infer_source_type_from_dir(): 从文件路径的父目录名反推 config.yaml 中的 source_type
    - extract_base_info(): 单文件处理——读取、判断、调用 Agent、合并、写入
    - run_base_info_stage(): 批量并行调度入口

设计决策：
    - id 字段在 00_manifest/ingest 阶段已写入，此处只读取不做重新生成
    - source_type 优先从目录名推断（如 arxiv → academic_paper），零成本消除 Agent 调用
    - 仅在前两种方式都无法确定 source_type 时才调用 Agent 判断
    - 已有字段绝不覆盖（merge 策略：existing_fm | new_fields）
"""

import logging
import sys
from pathlib import Path
from typing import Optional

import asyncio

from ...core.frontmatter_utils import read_frontmatter, write_frontmatter
from ...core.id_utils import generate_id
from ...schemas.base_info import BaseInfo
from ...core.agent import (
    AgentCallError,
    StageResult,
    call_agent_with_retry,
    parse_json_response,
)
from .prompts.base_info import get_base_info_system_prompt, build_base_info_user_prompt

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)


# =============================================================================
# 缺失字段检测
# =============================================================================

# BaseInfo 模型中需要提取的字段名集合
# 从 schemas/base_info.py 的 BaseInfo 模型中获取
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

        # 获取该字段的 Pydantic FieldInfo，检查是否有 alias
        field_info = BaseInfo.model_fields[field_name]

        # 检查 Python 字段名是否已存在（key 存在即为已有，值为 None/空字符串也算已处理）
        if field_name in existing_fm:
            continue

        # 检查 camelCase 别名是否已存在
        alias = field_info.alias if field_info.alias else None
        if alias and alias in existing_fm:
            continue

        # 字段缺失
        missing.append(field_name)

    return missing


# =============================================================================
# source_type 推断（目录名 → config.yaml source.type，零 Agent 调用）
# =============================================================================

# 在模块加载时构建目录名 → source_type 的映射表
# 如：data/01_raw/arxiv/ → academic_paper
_SOURCE_TYPE_FROM_DIR: dict[str, str] = {}


def _build_source_type_map() -> None:
    """
    从 config.yaml 的数据源配置中提取 name → source.type 映射。

    以文件所在目录名（即 source name）为索引，反查配置中对应数据源的
    type 字段（与 BaseInfo.source_type 枚举值一致）。

    此映射允许 BaseInfo 提取阶段完全跳过 Agent 调用：
    所有 source_type 都可以从文件路径的父目录名推断，零成本、零延迟。
    """
    from ...core.config_loader import get_sources

    for src in get_sources(enabled_only=False):
        name = src.get("name", "")
        src_type = src.get("type", "")
        if name and src_type:
            _SOURCE_TYPE_FROM_DIR[name] = src_type


# 模块加载时构建一次，后续所有调用复用
_build_source_type_map()


def _infer_source_type_from_dir(file_path: Path) -> Optional[str]:
    """
    从文件路径的父目录名推断 source_type。

    查找逻辑：
        1. 取文件所在父目录名（如 data/01_raw/arxiv/01.md → arxiv）
        2. 在 _SOURCE_TYPE_FROM_DIR 映射表中查找
        3. 返回标准枚举值（如 academic_paper）或 None

    参数：
        file_path: 输入 .md 文件路径

    返回：
        标准 source_type 枚举值字符串，无法推断时返回 None
    """
    parent_dir = file_path.parent.name
    return _SOURCE_TYPE_FROM_DIR.get(parent_dir)


# =============================================================================
# 空 body 日志辅助
# =============================================================================

def _log_empty_body_skip(file_path: str, fm: dict) -> None:
    """
    根据 extraction_status 输出有意义的跳过原因日志。

    参数：
        file_path: 文件路径（用于日志）
        fm: frontmatter 字典
    """
    status = fm.get("extraction_status", "")
    if status == "failed":
        logger.warning("正文为空（Stage 1 抓取失败），跳过 Agent 调用: %s", file_path)
    elif status == "partial":
        logger.warning("正文为空（Stage 1 仅获取摘要），跳过 Agent 调用: %s", file_path)
    else:
        logger.warning("正文为空，跳过 Agent 调用: %s", file_path)


# =============================================================================
# 单文件处理
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
    # 优先从 frontmatter 读取（00_manifest/ingest 阶段已写入），
    # 仅在旧文件缺少 id 时回退到动态生成
    article_id = existing_fm.get("id", "")
    if not article_id:
        source_url = existing_fm.get("source", "")
        article_id = generate_id(source_url) if source_url else ""
        logger.debug("旧文件缺少 id，回退生成: %s → %s", input_str, article_id)

    # --- 检查是否需要跳过 ---
    # id 存在 + 所有字段完整 = 已由本阶段处理过
    if skip_existing and output_path.exists():
        try:
            out_fm, _ = read_frontmatter(output_path)
            # 以 id 存在为前提（文件确实被流水线处理过），再检查字段完整性
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
            pass  # 输出文件损坏，继续处理

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
    # 对于绝大多数数据源，source_type 在 config.yaml 中已有明确配置，
    # 而文件目录名就是 source name（如 arxiv-cs-ai、techcrunch），
    # 因此可以直接推断，无需浪费 Agent 调用
    if "source_type" in missing_fields:
        inferred_type = _infer_source_type_from_dir(input_path)
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

    # --- 调用 Agent 提取缺失字段 ---
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
        # 构建提示词
        system_prompt = get_base_info_system_prompt()
        user_prompt = build_base_info_user_prompt(
            missing_fields=missing_fields,
            body=body,
        )

        # 调用 Agent（带重试）
        response_text = await call_agent_with_retry(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            max_turns=3,
        )

        # 解析 JSON
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

    # --- 合并提取结果 ---
    # 关键：只有 existing_fm 中不存在的字段才写入，已有字段绝不覆盖

    # 写入 id（从 frontmatter 读取或回退生成）
    if article_id:
        existing_fm["id"] = article_id
        fields_written.append("id")

    # 合并 Agent 提取的字段
    for field_name, value in extracted_data.items():
        # 只写入缺失字段，已有字段不覆盖
        if field_name in missing_fields:
            existing_fm[field_name] = value
            fields_written.append(field_name)

    # 标记管道阶段（供下游阶段做前置检查）
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
        input_str,
        output_str,
        ", ".join(fields_written),
    )
    return StageResult(
        input_path=input_str,
        output_path=output_str,
        success=True,
        fields_extracted=fields_written,
    )


# =============================================================================
# 批量并行调度
# =============================================================================

async def run_base_info_stage(
    file_paths: list[Path],
    output_base_dir: Path,
    input_base_dir: Path,
    semaphore: asyncio.Semaphore,
    *,
    model: Optional[str] = None,
    skip_existing: bool = True,
) -> list[StageResult]:
    """
    为一批文件并行执行 BaseInfo 提取。

    并行控制：
        - 使用 asyncio.Semaphore 限制并发 Agent 调用数量
        - 每个文件通过 semaphore 获得许可后才执行 Agent 调用
        - asyncio.gather(return_exceptions=True) 保证单个文件失败不影响其他

    输出路径规则：
        output_path = output_base_dir / (input_path 相对 input_base_dir 的子路径)
        例如: data/01_raw/arxiv/01.md → data/02_extracted/arxiv/01.md

    参数：
        file_paths: 待处理的 .md 文件路径列表
        output_base_dir: 输出根目录（如 data/02_extracted/）
        input_base_dir: 输入根目录（如 data/01_raw/）
        semaphore: 并发控制信号量
        model: LLM 模型名称
        skip_existing: 是否跳过已处理的文件

    返回：
        StageResult 列表（与 file_paths 顺序一致）
    """

    async def process_one(input_path: Path) -> StageResult:
        """处理单个文件，在 semaphore 保护下调用 Agent。"""
        # 计算输出路径：保持子目录结构
        rel_path = input_path.relative_to(input_base_dir)
        output_path = output_base_dir / rel_path

        # semaphore 控制并发数
        async with semaphore:
            return await extract_base_info(
                input_path=input_path,
                output_path=output_path,
                model=model,
                skip_existing=skip_existing,
            )

    # 创建所有并发任务
    tasks = [process_one(p) for p in file_paths]

    # return_exceptions=True: 单个文件异常不中断其他文件的处理
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # 将意外异常转为 StageResult
    wrapped: list[StageResult] = []
    for i, result in enumerate(results):
        if isinstance(result, StageResult):
            wrapped.append(result)
        elif isinstance(result, BaseException):
            wrapped.append(
                StageResult(
                    input_path=str(file_paths[i]),
                    output_path="",
                    success=False,
                    error=f"未处理的异常: {result}",
                )
            )
        else:
            wrapped.append(
                StageResult(
                    input_path=str(file_paths[i]),
                    output_path="",
                    success=False,
                    error=f"未知返回类型: {type(result)}",
                )
            )

    return wrapped
