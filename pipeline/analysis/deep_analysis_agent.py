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

from ..core.frontmatter_utils import read_frontmatter, write_frontmatter
from ..extraction.agent import (
    AgentCallError,
    StageResult,
    call_agent_with_retry,
    parse_json_response,
)
from ..schemas.deep_analysis import (
    QualitativeAssessment,
    ValueAssessment,
    ForesightAndActionability,
    Sentiment,
    DeveloperTone,
    HypeLevel,
    InformationEntropy,
    EngineeringComplexity,
    ValueCaptureLayer,
    MoatImpact,
    ConfidenceLevel,
    ActionableInsight,
)
from .prompts import (
    get_qualitative_system_prompt,
    build_qualitative_user_prompt,
    get_value_system_prompt,
    build_value_user_prompt,
    get_foresight_system_prompt,
    build_foresight_user_prompt,
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
# 模糊枚举匹配
# =============================================================================

# --- Sentiment 行业情绪 ---
_SENTIMENT_FUZZY: dict[str, str] = {
    "positive": "positive",
    "optimistic": "positive",
    "bullish": "positive",
    "good": "positive",
    "negative": "negative",
    "pessimistic": "negative",
    "bearish": "negative",
    "bad": "negative",
    "neutral": "neutral",
    "balanced": "neutral",
    "mixed": "mixed",
    "uncertain": "mixed",
    "complex": "mixed",
}

# --- DeveloperTone 开发者情绪 ---
_DEVELOPER_TONE_FUZZY: dict[str, str] = {
    "excited": "excited",
    "enthusiastic": "excited",
    "positive": "excited",
    "skeptical": "skeptical",
    "skeptic": "skeptical",
    "doubtful": "skeptical",
    "cautious": "skeptical",
    "frustrated": "frustrated",
    "angry": "frustrated",
    "disappointed": "frustrated",
    "upset": "frustrated",
    "neutral": "neutral",
    "balanced": "neutral",
    "indifferent": "neutral",
}

# --- HypeLevel 炒作指数 ---
_HYPE_LEVEL_FUZZY: dict[str, str] = {
    "low": "low",
    "minimal": "low",
    "none": "low",
    "substantive": "low",
    "medium": "medium",
    "moderate": "medium",
    "some": "medium",
    "high": "high",
    "extreme": "high",
    "overhyped": "high",
    "pump": "high",
}

# --- InformationEntropy 信息熵 ---
_ENTROPY_FUZZY: dict[str, str] = {
    "high": "high",
    "dense": "high",
    "rich": "high",
    "medium": "medium",
    "moderate": "medium",
    "average": "medium",
    "low": "low",
    "sparse": "low",
    "thin": "low",
    "repetitive": "low",
}

# --- EngineeringComplexity 工程落地复杂度 ---
_ENGINEERING_COMPLEXITY_FUZZY: dict[str, str] = {
    "conceptual": "conceptual",
    "concept": "conceptual",
    "theoretical": "conceptual",
    "theory": "conceptual",
    "paper": "conceptual",
    "research": "conceptual",
    "prototype": "prototype",
    "demo": "prototype",
    "experimental": "prototype",
    "poc": "prototype",
    "proof_of_concept": "prototype",
    "production_ready": "production_ready",
    "production": "production_ready",
    "shipping": "production_ready",
    "deployed": "production_ready",
    "live": "production_ready",
    "infrastructure": "infrastructure",
    "platform": "infrastructure",
    "foundational": "infrastructure",
    "standard": "infrastructure",
}

# --- ValueCaptureLayer 价值捕获层 ---
_VALUE_CAPTURE_FUZZY: dict[str, str] = {
    "hardware_compute": "hardware_compute",
    "hardware": "hardware_compute",
    "compute": "hardware_compute",
    "chip": "hardware_compute",
    "gpu": "hardware_compute",
    "cloud_platform": "cloud_platform",
    "cloud": "cloud_platform",
    "platform": "cloud_platform",
    "iaas": "cloud_platform",
    "foundation_model": "foundation_model",
    "model": "foundation_model",
    "llm": "foundation_model",
    "ai_model": "foundation_model",
    "agent_middleware": "agent_middleware",
    "middleware": "agent_middleware",
    "agent": "agent_middleware",
    "tool": "agent_middleware",
    "framework": "agent_middleware",
    "end_application": "end_application",
    "application": "end_application",
    "saas": "end_application",
    "product": "end_application",
}

# --- MoatImpact 护城河影响 ---
_MOAT_IMPACT_FUZZY: dict[str, str] = {
    "strengthens_monopoly": "strengthens_monopoly",
    "monopoly": "strengthens_monopoly",
    "consolidation": "strengthens_monopoly",
    "winner_takes_all": "strengthens_monopoly",
    "democratizes_access": "democratizes_access",
    "democratization": "democratizes_access",
    "open": "democratizes_access",
    "accessible": "democratizes_access",
    "creates_new_moat": "creates_new_moat",
    "new_moat": "creates_new_moat",
    "differentiation": "creates_new_moat",
    "competitive_advantage": "creates_new_moat",
    "neutral": "neutral",
    "none": "neutral",
    "unchanged": "neutral",
}

# --- ConfidenceLevel AI 研判置信度 ---
_CONFIDENCE_FUZZY: dict[str, str] = {
    "high": "high",
    "confident": "high",
    "certain": "high",
    "strong": "high",
    "medium": "medium",
    "moderate": "medium",
    "uncertain": "medium",
    "low": "low",
    "uncertain": "low",
    "speculative": "low",
    "weak": "low",
}

# --- ActionableInsight 可执行建议 ---
_ACTIONABLE_INSIGHT_FUZZY: dict[str, str] = {
    "deep_dive": "deep_dive",
    "deepdive": "deep_dive",
    "research": "deep_dive",
    "study": "deep_dive",
    "read": "deep_dive",
    "monitor": "monitor",
    "watch": "monitor",
    "track": "monitor",
    "follow": "monitor",
    "strategic_invest": "strategic_invest",
    "invest": "strategic_invest",
    "build": "strategic_invest",
    "act": "strategic_invest",
    "speculative_watch": "speculative_watch",
    "speculative": "speculative_watch",
    "maybe": "speculative_watch",
    "ignore": "ignore",
    "skip": "ignore",
    "noise": "ignore",
    "pass": "ignore",
}


def _fuzzy_match_enum(value: str, mapping: dict[str, str], enum_name: str) -> Optional[str]:
    """
    模糊匹配枚举值。匹配策略：
        1. 直接查找映射表（小写归一化）
        2. 尝试在映射表中做子串包含匹配

    参数：
        value: Agent 返回的原始值
        mapping: 模糊匹配映射表
        enum_name: 枚举类名（仅用于日志）

    返回：
        匹配到的标准枚举值，未匹配返回 None
    """
    key = value.lower().strip()

    # 直接匹配
    if key in mapping:
        return mapping[key]

    # 子串包含匹配
    for k, v in mapping.items():
        if k in key or key in k:
            logger.info("模糊匹配 %s: '%s' → '%s' (匹配键 '%s')", enum_name, value, v, k)
            return v

    return None


# =============================================================================
# 校验函数
# =============================================================================

def _validate_qualitative(data: dict) -> QualitativeAssessment:
    """
    验证并构造 QualitativeAssessment 实例。

    处理流程：
        1. 先用 Pydantic 严格校验
        2. 如果枚举值校验失败 → 尝试模糊匹配
        3. 修复嵌套模型结构错误
        4. 修复后重新校验
    """
    from pydantic import ValidationError

    # --- 预处理：修复常见的嵌套模型格式错误 ---
    repaired = dict(data)

    # impactScore: 如果是纯数字 → 包装为 {score, reason}
    if "impactScore" in repaired and isinstance(repaired["impactScore"], (int, float)):
        repaired["impactScore"] = {"score": float(repaired["impactScore"]), "reason": "AI 未提供评分依据"}
        logger.info("impactScore 自动包装: %s → {score, reason}", data["impactScore"])

    # developerSentiment: 如果是纯字符串 → 包装为 {tone, primaryFocus}
    if "developerSentiment" in repaired and isinstance(repaired["developerSentiment"], str):
        repaired["developerSentiment"] = {"tone": repaired["developerSentiment"], "primaryFocus": "未明确"}
        logger.info("developerSentiment 自动包装: str → {tone, primaryFocus}")

    # hypeAssessment: 如果是纯字符串 → 包装为 {level, reason}
    if "hypeAssessment" in repaired and isinstance(repaired["hypeAssessment"], str):
        repaired["hypeAssessment"] = {"level": repaired["hypeAssessment"], "reason": "AI 未提供判定依据"}
        logger.info("hypeAssessment 自动包装: str → {level, reason}")

    # domainDisruption: 如果是纯字符串 → 包装
    if "domainDisruption" in repaired and isinstance(repaired["domainDisruption"], str):
        repaired["domainDisruption"] = {"technicalInnovation": repaired["domainDisruption"], "businessModel": "无"}

    # --- 尝试严格校验 ---
    try:
        return QualitativeAssessment.model_validate(repaired)
    except ValidationError as pydantic_err:
        errors = pydantic_err.errors()
        logger.warning("QualitativeAssessment 严格校验失败: %s", errors)

        # --- 尝试修复枚举值 ---
        for error in errors:
            loc = error.get("loc", [])
            if not loc:
                continue

            field_path = loc[0]
            raw_value = _get_nested(repaired, loc)

            if not isinstance(raw_value, str):
                continue

            # 顶层枚举字段
            if field_path == "sentiment":
                matched = _fuzzy_match_enum(raw_value, _SENTIMENT_FUZZY, "sentiment")
                if matched:
                    repaired["sentiment"] = matched
                    logger.info("sentiment 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "informationEntropy":
                matched = _fuzzy_match_enum(raw_value, _ENTROPY_FUZZY, "informationEntropy")
                if matched:
                    repaired["informationEntropy"] = matched
                    logger.info("informationEntropy 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "engineeringComplexity":
                matched = _fuzzy_match_enum(raw_value, _ENGINEERING_COMPLEXITY_FUZZY, "engineeringComplexity")
                if matched:
                    repaired["engineeringComplexity"] = matched
                    logger.info("engineeringComplexity 修复: '%s' → '%s'", raw_value, matched)

            # 嵌套枚举字段
            elif field_path == "developerSentiment" and len(loc) > 1:
                if loc[1] == "tone":
                    matched = _fuzzy_match_enum(raw_value, _DEVELOPER_TONE_FUZZY, "developerSentiment.tone")
                    if matched and isinstance(repaired.get("developerSentiment"), dict):
                        repaired["developerSentiment"]["tone"] = matched
                        logger.info("developerSentiment.tone 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "hypeAssessment" and len(loc) > 1:
                if loc[1] == "level":
                    matched = _fuzzy_match_enum(raw_value, _HYPE_LEVEL_FUZZY, "hypeAssessment.level")
                    if matched and isinstance(repaired.get("hypeAssessment"), dict):
                        repaired["hypeAssessment"]["level"] = matched
                        logger.info("hypeAssessment.level 修复: '%s' → '%s'", raw_value, matched)

        # --- 确保嵌套字段存在 ---
        if "domainDisruption" not in repaired or not isinstance(repaired.get("domainDisruption"), dict):
            repaired["domainDisruption"] = {"technicalInnovation": "无", "businessModel": "无"}

        # --- 修复后重新校验 ---
        try:
            return QualitativeAssessment.model_validate(repaired)
        except ValidationError as second_err:
            raise ValueError(
                f"QualitativeAssessment 校验失败（模糊匹配后仍失败）: {second_err}"
            ) from second_err


def _validate_value(data: dict) -> ValueAssessment:
    """验证并构造 ValueAssessment 实例。"""
    from pydantic import ValidationError

    repaired = dict(data)

    # compoundValue: 如果是纯数字 → 包装
    if "compoundValue" in repaired and isinstance(repaired["compoundValue"], (int, float)):
        repaired["compoundValue"] = {"score": float(repaired["compoundValue"]), "reason": "AI 未提供评分依据"}
        logger.info("compoundValue 自动包装: %s → {score, reason}", data["compoundValue"])

    # --- 尝试严格校验 ---
    try:
        return ValueAssessment.model_validate(repaired)
    except ValidationError as pydantic_err:
        errors = pydantic_err.errors()
        logger.warning("ValueAssessment 严格校验失败: %s", errors)

        for error in errors:
            loc = error.get("loc", [])
            if not loc:
                continue
            raw_value = _get_nested(repaired, loc)
            if not isinstance(raw_value, str):
                continue

            field_path = loc[0]
            if field_path == "valueCaptureLayer":
                matched = _fuzzy_match_enum(raw_value, _VALUE_CAPTURE_FUZZY, "valueCaptureLayer")
                if matched:
                    repaired["valueCaptureLayer"] = matched
                    logger.info("valueCaptureLayer 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "moatImpact":
                matched = _fuzzy_match_enum(raw_value, _MOAT_IMPACT_FUZZY, "moatImpact")
                if matched:
                    repaired["moatImpact"] = matched
                    logger.info("moatImpact 修复: '%s' → '%s'", raw_value, matched)

        # --- 确保列表字段存在 ---
        if "keyBeneficiaries" not in repaired:
            repaired["keyBeneficiaries"] = []
        if "competitiveCasualty" not in repaired:
            repaired["competitiveCasualty"] = []

        try:
            return ValueAssessment.model_validate(repaired)
        except ValidationError as second_err:
            raise ValueError(
                f"ValueAssessment 校验失败（模糊匹配后仍失败）: {second_err}"
            ) from second_err


def _validate_foresight(data: dict) -> ForesightAndActionability:
    """验证并构造 ForesightAndActionability 实例。"""
    from pydantic import ValidationError

    repaired = dict(data)

    # confidence: 如果是纯字符串 → 包装为三个维度的默认值
    if "confidence" in repaired and isinstance(repaired["confidence"], str):
        val = repaired["confidence"]
        repaired["confidence"] = {"impact": val, "compound": val, "hype": val}
        logger.info("confidence 自动包装: str → {impact, compound, hype}")

    # --- 尝试严格校验 ---
    try:
        return ForesightAndActionability.model_validate(repaired)
    except ValidationError as pydantic_err:
        errors = pydantic_err.errors()
        logger.warning("ForesightAndActionability 严格校验失败: %s", errors)

        for error in errors:
            loc = error.get("loc", [])
            if not loc:
                continue
            raw_value = _get_nested(repaired, loc)
            if not isinstance(raw_value, str):
                continue

            field_path = loc[0]
            # 顶层枚举
            if field_path == "actionableInsight":
                matched = _fuzzy_match_enum(raw_value, _ACTIONABLE_INSIGHT_FUZZY, "actionableInsight")
                if matched:
                    repaired["actionableInsight"] = matched
                    logger.info("actionableInsight 修复: '%s' → '%s'", raw_value, matched)

            # 嵌套枚举 (confidence.{impact, compound, hype})
            elif field_path == "confidence" and len(loc) > 1:
                sub_field = loc[1]
                if sub_field in ("impact", "compound", "hype"):
                    matched = _fuzzy_match_enum(raw_value, _CONFIDENCE_FUZZY, f"confidence.{sub_field}")
                    if matched and isinstance(repaired.get("confidence"), dict):
                        repaired["confidence"][sub_field] = matched
                        logger.info("confidence.%s 修复: '%s' → '%s'", sub_field, raw_value, matched)

        # --- 确保必要字段存在 ---
        if "marketOpportunities" not in repaired:
            repaired["marketOpportunities"] = []
        if "riskMatrix" not in repaired or not isinstance(repaired.get("riskMatrix"), dict):
            repaired["riskMatrix"] = {
                "regulatory": "无", "technological": "无",
                "competitive": "无", "ethical": "无", "additional": [],
            }

        try:
            return ForesightAndActionability.model_validate(repaired)
        except ValidationError as second_err:
            raise ValueError(
                f"ForesightAndActionability 校验失败（模糊匹配后仍失败）: {second_err}"
            ) from second_err


def _get_nested(data: dict, loc: tuple) -> object:
    """从嵌套字典中按路径 loc 取值。如 loc=('developerSentiment','tone') → data['developerSentiment']['tone']"""
    current = data
    for key in loc:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current


# =============================================================================
# 单文件处理
# =============================================================================

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

    async def run_qualitative() -> tuple[str, dict]:
        """运行 QualitativeAssessment Agent 调用 + 校验"""
        sys_prompt = get_qualitative_system_prompt()
        usr_prompt = build_qualitative_user_prompt(
            title=title, source=source, source_type=source_type,
            tldr=tldr, objective_summary=objective_summary,
            event_type=event_type, epistemic_status=epistemic_status,
            entities=entities, key_logic_flow=key_logic_flow, body=body,
        )
        response = await call_agent_with_retry(
            prompt=usr_prompt, system_prompt=sys_prompt, model=model, max_turns=3,
        )
        data = parse_json_response(response)
        validated = _validate_qualitative(data)
        return ("qualitative", validated.model_dump(mode="json", by_alias=False))

    async def run_value() -> tuple[str, dict]:
        """运行 ValueAssessment Agent 调用 + 校验"""
        sys_prompt = get_value_system_prompt()
        usr_prompt = build_value_user_prompt(
            title=title, source=source, source_type=source_type,
            tldr=tldr, objective_summary=objective_summary,
            event_type=event_type, epistemic_status=epistemic_status,
            entities=entities, key_logic_flow=key_logic_flow, body=body,
        )
        response = await call_agent_with_retry(
            prompt=usr_prompt, system_prompt=sys_prompt, model=model, max_turns=3,
        )
        data = parse_json_response(response)
        validated = _validate_value(data)
        return ("value", validated.model_dump(mode="json", by_alias=False))

    async def run_foresight() -> tuple[str, dict]:
        """运行 ForesightAndActionability Agent 调用 + 校验"""
        sys_prompt = get_foresight_system_prompt()
        usr_prompt = build_foresight_user_prompt(
            title=title, source=source, source_type=source_type,
            tldr=tldr, objective_summary=objective_summary,
            event_type=event_type, epistemic_status=epistemic_status,
            entities=entities, key_logic_flow=key_logic_flow, body=body,
        )
        response = await call_agent_with_retry(
            prompt=usr_prompt, system_prompt=sys_prompt, model=model, max_turns=3,
        )
        data = parse_json_response(response)
        validated = _validate_foresight(data)
        return ("foresight", validated.model_dump(mode="json", by_alias=False))

    # 构建任务列表（仅运行需要的维度）
    tasks = []
    if "qualitative" in to_run:
        tasks.append(run_qualitative())
    if "value" in to_run:
        tasks.append(run_value())
    if "foresight" in to_run:
        tasks.append(run_foresight())

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
