"""
pipeline/analysis/deep_analysis_agent.py — Stage 3: 深度分析 Agent

功能：
    - 针对单篇文章，并行调用 3 个独立 Agent 完成 QualitativeAssessment、
      ValueAssessment、ForesightAndActionability 三个维度的深度研判
    - 每个维度有独立的 Pydantic 校验 + 模糊枚举匹配回退
    - analyze_one_file(): 单文件处理——读取、3 路并行 Agent 调用、合并、写入
    - run_deep_analysis_stage(): 批量并行调度入口

设计决策：
    - 三个评估维度完全独立（不同 system prompt、不同输出字段），
      通过 asyncio.gather 在单文件内并行执行
    - 部分成功策略：2/3 评估通过时仍写入成功的部分，失败维度下次重试
    - 跳过检查按评估维度粒度进行（per-assessment skip），节省 token
    - 所有 Stage 2 提取结果（tldr、entities、keyLogicFlow 等）作为上下文传入
"""

import asyncio
import logging
from pathlib import Path
from typing import Optional

from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter
from ..core.agent import (
    StageResult,
    call_agent_with_retry,
    parse_json_response,
)
from ..schemas.deep_analysis import (
    QualitativeAssessment,
    ValueAssessment,
    ForesightAndActionability,
)
from .prompts import (
    get_qualitative_system_prompt,
    build_qualitative_user_prompt,
    get_value_system_prompt,
    build_value_user_prompt,
    get_foresight_system_prompt,
    build_foresight_user_prompt,
)
from .validators import validate_qualitative, validate_value, validate_foresight

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)

# =============================================================================
# 每个评估维度的 Pydantic 字段名集合（用于 skip_existing 检查）
# =============================================================================

_QUALITATIVE_FIELDS: set[str] = set(QualitativeAssessment.model_fields.keys())
_VALUE_FIELDS: set[str] = set(ValueAssessment.model_fields.keys())
_FORESIGHT_FIELDS: set[str] = set(ForesightAndActionability.model_fields.keys())

# 三个维度的字段名 → 显示标签
_ASSESSMENT_LABELS: dict[str, str] = {
    "qualitative": "定性研判",
    "value": "价值评估",
    "foresight": "前瞻预测",
}

# 每个维度对应的字段集合（用于跳过检查）
_ASSESSMENT_FIELD_SETS: dict[str, set[str]] = {
    "qualitative": _QUALITATIVE_FIELDS,
    "value": _VALUE_FIELDS,
    "foresight": _FORESIGHT_FIELDS,
}



# =============================================================================
# 单文件处理

async def analyze_one_file(
    input_path: Path,
    output_path: Path,
    *,
    model: Optional[str] = None,
    skip_existing: bool = True,
    stages: str = "all",
) -> StageResult:
    """
    对单个 .md 文件执行深度分析（3 个评估维度并行）。

    处理流程：
        1. read_frontmatter(input_path) → (existing_fm, body)
        2. 提取 Stage 2 上下文（title, source, tldr, entities 等）
        3. skip_existing 检查：按评估维度粒度判断哪些维度需要运行
        4. body 为空 → 跳过
        5. 通过 asyncio.gather 并行调用 3 个 Agent（仅运行需要的维度）
        6. 合并成功维度结果到 existing_fm
        7. write_frontmatter(output_path, merged_fm, body)

    参数：
        input_path: 输入 .md 文件路径（来自 data/02_extracted/）
        output_path: 输出 .md 文件路径（data/03_analyzed/ 下，保持子目录结构）
        model: LLM 模型名称
        skip_existing: 是否跳过已有分析结果的文件
        stages: 要运行的评估维度 ("all" | "qualitative" | "value" | "foresight")

    返回：
        StageResult 记录分析结果
    """
    input_str = str(input_path)
    output_str = str(output_path)

    # --- 读取 frontmatter ---
    try:
        existing_fm, body = read_frontmatter(input_path)
    except Exception as exc:
        logger.error("读取文件失败 %s: %s", input_str, exc)
        return StageResult(
            input_path=input_str, output_path=output_str,
            success=False, error=f"读取文件失败: {exc}",
        )

    # 如果输出文件已存在，合并已有的 Stage 3 字段，避免重新分析时覆盖
    if output_path.exists():
        try:
            out_fm, _ = read_frontmatter(output_path)
            _all_stage3_fields = _QUALITATIVE_FIELDS | _VALUE_FIELDS | _FORESIGHT_FIELDS
            for key, value in out_fm.items():
                if key in _all_stage3_fields:
                    existing_fm[key] = value
        except Exception:
            pass

    # --- 空 body 处理 ---
    if not body.strip():
        logger.warning("正文为空，跳过深度分析: %s", input_str)
        return StageResult(
            input_path=input_str, output_path=output_str,
            success=True, fields_extracted=[], skipped=True,
        )

    # --- 确定需要运行的评估维度 ---
    to_run: list[str] = []
    if stages == "all":
        candidate = ["qualitative", "value", "foresight"]
    else:
        candidate = [stages]

    if skip_existing and output_path.exists():
        try:
            out_fm, _ = read_frontmatter(output_path)
            if out_fm.get("id"):
                for dim in candidate:
                    field_set = _ASSESSMENT_FIELD_SETS[dim]
                    if not field_set.issubset(set(out_fm.keys())):
                        to_run.append(dim)
            else:
                to_run = list(candidate)
        except Exception:
            to_run = list(candidate)
    else:
        to_run = list(candidate)

    if not to_run:
        logger.info("跳过（id=%s 已分析）: %s", existing_fm.get("id"), input_str)
        return StageResult(
            input_path=input_str, output_path=output_str,
            success=True, fields_extracted=[], skipped=True,
        )

    logger.info("深度分析: %s (维度: %s)", input_str, ", ".join(to_run))

    # --- 提取 Stage 2 上下文 ---
    title = existing_fm.get("title", "")
    source = existing_fm.get("source", "")
    source_type = existing_fm.get("source_type", "")
    tldr = existing_fm.get("tldr", "")
    objective_summary = existing_fm.get("objective_summary", "")
    event_type = existing_fm.get("event_type", "")
    epistemic_status = existing_fm.get("epistemic_status", "")
    entities = existing_fm.get("entities", {})
    key_logic_flow = existing_fm.get("key_logic_flow", [])

    # --- 并行调用 Agent ---
    all_fields_written: list[str] = []
    has_error = False
    error_messages: list[str] = []

    # 每个维度的配置：(维度名, system_prompt_getter, user_prompt_builder, validate_fn, 显示标签)
    _dimension_configs = [
        ("qualitative", get_qualitative_system_prompt, build_qualitative_user_prompt, validate_qualitative),
        ("value", get_value_system_prompt, build_value_user_prompt, validate_value),
        ("foresight", get_foresight_system_prompt, build_foresight_user_prompt, validate_foresight),
    ]

    async def _run_assessment(
        dim_name: str,
        get_sys_prompt,
        build_usr_prompt,
        validate_fn,
    ) -> tuple[str, dict]:
        """通用的单维度 Agent 调用 + 校验流水线。"""
        sys_prompt = get_sys_prompt()
        usr_prompt = build_usr_prompt(
            title=title, source=source, source_type=source_type,
            tldr=tldr, objective_summary=objective_summary,
            event_type=event_type, epistemic_status=epistemic_status,
            entities=entities, key_logic_flow=key_logic_flow, body=body,
        )
        response = await call_agent_with_retry(
            prompt=usr_prompt, system_prompt=sys_prompt, model=model, max_turns=3,
        )
        data = parse_json_response(response)
        validated = validate_fn(data)
        return (dim_name, validated.model_dump(mode="json", by_alias=False))

    # 构建任务列表（仅运行需要的维度）
    tasks = [
        _run_assessment(dim, get_sys, build_usr, vfn)
        for dim, get_sys, build_usr, vfn in _dimension_configs
        if dim in to_run
    ]

    # 并行执行所有需要的评估
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Exception):
            has_error = True
            msg = f"Agent 调用/校验异常: {result}"
            error_messages.append(msg)
            logger.error("%s: %s", input_str, msg)
        elif isinstance(result, tuple) and len(result) == 2:
            dim_name, dim_data = result
            # 合并到 frontmatter
            for field_name, value in dim_data.items():
                existing_fm[field_name] = value
                all_fields_written.append(field_name)
            logger.info("  %s 完成: %s", _ASSESSMENT_LABELS.get(dim_name, dim_name), input_str)

    # --- 写入输出文件（即使部分成功也写入） ---
    if all_fields_written:
        try:
            write_frontmatter(output_path, existing_fm, body)
        except Exception as exc:
            logger.error("写入输出文件失败 %s: %s", output_str, exc)
            return StageResult(
                input_path=input_str, output_path=output_str,
                success=False, error=f"写入文件失败: {exc}",
            )

    logger.info(
        "深度分析完成: %s → %s (字段: %s)",
        input_str, output_str, ", ".join(all_fields_written) if all_fields_written else "无",
    )
    return StageResult(
        input_path=input_str,
        output_path=output_str,
        success=not has_error or len(all_fields_written) > 0,
        fields_extracted=all_fields_written,
        error="; ".join(error_messages) if error_messages else "",
    )


# =============================================================================
# 批量并行调度
# =============================================================================

async def run_deep_analysis_stage(
    file_paths: list[Path],
    output_base_dir: Path,
    input_base_dir: Path,
    semaphore: asyncio.Semaphore,
    *,
    model: Optional[str] = None,
    skip_existing: bool = True,
    stages: str = "all",
) -> list[StageResult]:
    """
    为一批文件并行执行深度分析。

    并行控制：
        - 外层：asyncio.Semaphore 限制同时处理的文件数
        - 内层：asyncio.gather 在单个文件内并行调用 3 个 Agent

    参数：
        file_paths: 待处理的 .md 文件路径列表
        output_base_dir: 输出根目录（data/03_analyzed/）
        input_base_dir: 输入根目录（data/02_extracted/）
        semaphore: 并发控制信号量
        model: LLM 模型名称
        skip_existing: 是否跳过已处理的文件
        stages: 要运行的评估维度 ("all" | "qualitative" | "value" | "foresight")

    返回：
        StageResult 列表
    """

    async def process_one(input_path: Path) -> StageResult:
        """处理单个文件，在 semaphore 保护下调用 Agent。"""
        rel_path = input_path.relative_to(input_base_dir)
        output_path = output_base_dir / rel_path

        async with semaphore:
            return await analyze_one_file(
                input_path=input_path,
                output_path=output_path,
                model=model,
                skip_existing=skip_existing,
                stages=stages,
            )

    tasks = [process_one(p) for p in file_paths]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # 将意外异常转为 StageResult
    wrapped: list[StageResult] = []
    for i, result in enumerate(results):
        if isinstance(result, StageResult):
            wrapped.append(result)
        elif isinstance(result, BaseException):
            wrapped.append(StageResult(
                input_path=str(file_paths[i]), output_path="",
                success=False, error=f"未处理的异常: {result}",
            ))
        else:
            wrapped.append(StageResult(
                input_path=str(file_paths[i]), output_path="",
                success=False, error=f"未知返回类型: {type(result)}",
            ))

    return wrapped
