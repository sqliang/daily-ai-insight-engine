"""
pipeline/analysis/deep_analysis_agent.py — Stage 3: 深度分析 Agent

功能：
    - 针对单篇文章，并行调用 3 个独立 Agent 完成 QualitativeAssessment、
      ValueAssessment、ForesightAndActionability 三个维度的深度研判
    - 仅运行三类主分析维度；专题分析 Agent 保留代码但暂时不自动触发
    - 每个维度有独立的 Pydantic 校验 + 模糊枚举匹配回退
    - analyze_one_file(): 单文件处理——读取、N 路并行 Agent 调用、合并、写入
    - run_deep_analysis_stage(): 批量并行调度入口

设计决策：
    - 三个基础评估维度完全独立（不同 system prompt、不同输出字段），
      通过 asyncio.gather 在单文件内并行执行
    - 专题分析维度曾通过 source_match 机制自动追加，目前暂时停用
    - 部分成功策略：N 个评估中部分通过时仍写入成功的部分，失败维度下次重试
    - 跳过检查按评估维度粒度进行（per-assessment skip），节省 token
    - 所有 Stage 2 提取结果（tldr、entities、keyLogicFlow 等）作为上下文传入
"""

import asyncio
import json
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
from ..schemas.specialized_analysis import (
    GitHubProjectAnalysis,
    ObjectInsightBundle,
    PaperAnalysis,
    ProductAnalysis,
)

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
_OBJECT_INSIGHT_FIELDS: set[str] = {"object_insights"}

# 专题分析字段集合。
#
# 这些字段在 Stage 3 深度分析阶段仍会被写入文章 frontmatter（如 github_assessment、
# paper_assessment、product_assessment），供 Stage 4b 合成时参考。同时，在重新分析
# 或部分维度重跑时，需要把这些字段与通用评估字段一起保留，避免覆盖已有专题分析结果。
_GITHUB_PROJECT_FIELDS: set[str] = set(GitHubProjectAnalysis.model_fields.keys())

_PAPER_FIELDS: set[str] = set(PaperAnalysis.model_fields.keys())

_PRODUCT_FIELDS: set[str] = set(ProductAnalysis.model_fields.keys())

# 三个维度的字段名 → 显示标签
_ASSESSMENT_LABELS: dict[str, str] = {
    "qualitative": "定性研判",
    "value": "价值评估",
    "foresight": "前瞻预测",
    "object": "对象洞察",
}

# 每个维度对应的字段集合（用于跳过检查）
_ASSESSMENT_FIELD_SETS: dict[str, set[str]] = {
    "qualitative": _QUALITATIVE_FIELDS,
    "value": _VALUE_FIELDS,
    "foresight": _FORESIGHT_FIELDS,
    "object": _OBJECT_INSIGHT_FIELDS,
}


def _object_insight_system_prompt() -> str:
    """返回项目/产品统一对象洞察 Agent 的系统提示词。"""
    return """你是 Daily AI Insight Engine 的专题洞察分析师，负责把文章中识别出的项目和产品转化为可跟踪的对象洞察。

## 任务
基于文章事实、Stage 2 objectMentions 和已有三维分析上下文，输出 objectInsights。

## 输出要求
- 只分析 objectType 为 project 或 product 的对象。
- 只分析 confidence 为 high/medium 且 articleRole 不是 ecosystem_context 的对象。
- 每个对象都必须保留 articleIds 和 evidenceSnippets，不能输出没有来源证据的对象。
- evidenceSnippets 必须优先原样保留 Stage 2 objectMentions 中的证据句；每条目标长度 40-140 个中文字符，必须是完整句子或完整分句，保留句末标点，不要压缩成短标签，也不要在逗号、顿号或半句处截断。
- 所有人类可读字段使用中文。
- positioning: 30-90 个中文字符，完整说明对象定位并以句末标点结束。
- technicalSignal/adoptionSignal/ecosystemRelevance/productSignal/marketSignal/differentiation: 每项 25-90 个中文字符，必须表达完整事实或判断并以句末标点结束；没有依据时返回 null。
- watchReason: 60-160 个中文字符，必须是完整判断并以句末标点结束。
- riskNotes: 每条 25-90 个中文字符，必须是完整风险表述并以句末标点结束。
- score 为 1-10，表示专题关注优先级。

## 输出格式
只返回 JSON：
{
  "objectInsights": [
    {
      "objectType": "project",
      "name": "对象名称",
      "canonicalName": "归一化名称",
      "url": "https://example.com",
      "positioning": "对象定位",
      "technicalSignal": "项目技术信号，产品对象可为 null",
      "adoptionSignal": "项目采用信号，产品对象可为 null",
      "ecosystemRelevance": "项目生态相关性，产品对象可为 null",
      "targetUsers": ["产品目标用户，项目对象可为空数组"],
      "productSignal": "产品能力信号，项目对象可为 null",
      "marketSignal": "市场信号，项目对象可为 null",
      "differentiation": "差异化判断，项目对象可为 null",
      "watchReason": "为什么值得持续跟踪",
      "riskNotes": ["风险或不确定性"],
      "score": 7,
      "articleIds": ["article-id"],
      "evidenceSnippets": ["证据片段"]
    }
  ]
}
"""


def _eligible_object_mentions(object_mentions: list) -> list[dict]:
    """筛选适合进入 Stage 3 对象洞察的项目/产品 mention。"""
    eligible: list[dict] = []
    for mention in object_mentions:
        if not isinstance(mention, dict):
            continue
        object_type = mention.get("object_type") or mention.get("objectType")
        confidence = mention.get("confidence")
        role = mention.get("article_role") or mention.get("articleRole")
        evidence = mention.get("evidence_snippets") or mention.get("evidenceSnippets") or []
        if object_type not in ("project", "product"):
            continue
        if confidence not in ("high", "medium"):
            continue
        if role == "ecosystem_context":
            continue
        if not evidence:
            continue
        eligible.append(mention)
    return eligible


def _build_object_insight_user_prompt(
    *,
    article_id: str,
    title: str,
    source: str,
    tldr: str,
    objective_summary: str,
    key_logic_flow: list,
    object_mentions: list[dict],
    body: str,
) -> str:
    """构造对象洞察 Agent 的用户提示词。"""
    return f"""## 文章信息
ID：{article_id}
标题：{title}
来源：{source}

## Stage 2 摘要
TLDR：{tldr}
客观摘要：{objective_summary}
关键逻辑：
{json.dumps(key_logic_flow, ensure_ascii=False, indent=2)}

## 待分析对象
{json.dumps(object_mentions, ensure_ascii=False, indent=2)}

## 文章正文
{body[:6000]}

## 指令
请为待分析对象生成 objectInsights。必须保留 articleIds=[文章 ID] 和对应 evidenceSnippets。
evidenceSnippets 优先复制“待分析对象”中的原证据；如需改写，必须保持 40-140 个中文字符左右、事实完整、句末有标点，不能输出半句话。
"""



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
    对单个 .md 文件执行深度分析（3 个基础评估维度并行）。

    处理流程：
        1. read_frontmatter(input_path) → (existing_fm, body)
        2. 提取 Stage 2 上下文（title, source, tldr, entities 等）
        3. skip_existing 检查：按评估维度粒度判断哪些维度需要运行
        4. 专题分析维度暂时停用，仅运行三类主分析维度
        5. body 为空 → 跳过
        6. 通过 asyncio.gather 并行调用 N 个 Agent（仅运行需要的维度）
        7. 合并成功维度结果到 existing_fm
        8. write_frontmatter(output_path, merged_fm, body)

    参数：
        input_path: 输入 .md 文件路径（来自 data/02_extracted/）
        output_path: 输出 .md 文件路径（data/03_analyzed/ 下，保持子目录结构）
        model: LLM 模型名称
        skip_existing: 是否跳过已有分析结果的文件
        stages: 要运行的基础评估维度 ("all" | "qualitative" | "value" | "foresight")。

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
            _all_stage3_fields = _QUALITATIVE_FIELDS | _VALUE_FIELDS | _FORESIGHT_FIELDS | _OBJECT_INSIGHT_FIELDS | _GITHUB_PROJECT_FIELDS | _PAPER_FIELDS | _PRODUCT_FIELDS
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
    object_mentions = existing_fm.get("object_mentions") or existing_fm.get("objectMentions") or []
    eligible_mentions = _eligible_object_mentions(object_mentions if isinstance(object_mentions, list) else [])
    if stages == "all" and eligible_mentions and "object" not in to_run:
        if not (skip_existing and output_path.exists() and "object_insights" in existing_fm):
            to_run.append("object")
    if stages == "object" and not eligible_mentions:
        to_run = []

    # --- 并行调用 Agent ---
    all_fields_written: list[str] = []
    has_error = False
    error_messages: list[str] = []

    if not to_run:
        logger.info("跳过（id=%s 已分析）: %s", existing_fm.get("id"), input_str)
        return StageResult(
            input_path=input_str, output_path=output_str,
            success=True, fields_extracted=[], skipped=True,
        )

    logger.info("深度分析: %s (维度: %s)", input_str, ", ".join(to_run))

    # 每个维度的配置：(维度名, system_prompt_getter, user_prompt_builder, validate_fn)
    _dimension_configs = [
        ("qualitative", get_qualitative_system_prompt, build_qualitative_user_prompt, validate_qualitative),
        ("value", get_value_system_prompt, build_value_user_prompt, validate_value),
        ("foresight", get_foresight_system_prompt, build_foresight_user_prompt, validate_foresight),
    ]

    _all_configs = {item[0]: item for item in _dimension_configs}

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

    async def _run_object_insight() -> tuple[str, dict]:
        """运行统一对象洞察 Agent。"""
        usr_prompt = _build_object_insight_user_prompt(
            article_id=existing_fm.get("id", ""),
            title=title,
            source=source,
            tldr=tldr,
            objective_summary=objective_summary,
            key_logic_flow=key_logic_flow,
            object_mentions=eligible_mentions,
            body=body,
        )
        response = await call_agent_with_retry(
            prompt=usr_prompt,
            system_prompt=_object_insight_system_prompt(),
            model=model,
            max_turns=3,
        )
        data = parse_json_response(response)
        validated = ObjectInsightBundle.model_validate(data)
        return ("object", validated.model_dump(mode="json", by_alias=False))

    # 构建任务列表（仅运行需要的主分析维度）
    tasks = [
        _run_assessment(dim, get_sys, build_usr, vfn)
        for dim, get_sys, build_usr, vfn in [
            _all_configs[dim] for dim in to_run if dim in _all_configs
        ]
    ]
    if "object" in to_run and eligible_mentions:
        tasks.append(_run_object_insight())
    if not tasks:
        logger.info("跳过（无可分析对象）: %s", input_str)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=True,
            fields_extracted=[],
            skipped=True,
        )

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
        - 内层：asyncio.gather 在单个文件内并行调用 N 个主分析 Agent

    参数：
        file_paths: 待处理的 .md 文件路径列表
        output_base_dir: 输出根目录（data/03_analyzed/）
        input_base_dir: 输入根目录（data/02_extracted/）
        semaphore: 并发控制信号量
        model: LLM 模型名称
        skip_existing: 是否跳过已处理的文件
        stages: 要运行的基础评估维度 ("all" | "qualitative" | "value" | "foresight")。

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
