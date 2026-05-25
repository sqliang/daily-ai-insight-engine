"""
pipeline/analysis/validators.py — Stage 3 深度分析校验函数

为 QualitativeAssessment、ValueAssessment、ForesightAndActionability 三个维度
各提供一个 Pydantic 校验 + 模糊枚举修复的组合函数。

校验流程（三个维度共用）：
    1. 预处理：将 LLM 可能返回的标量值自动包装为嵌套模型格式
    2. Pydantic 严格校验 → 通过即返回
    3. 校验失败 → 对每个错误的枚举字段尝试模糊匹配修正
    4. 补全缺失的列表/对象字段的默认值
    5. 修复后重新校验 → 仍失败则抛出 ValueError
"""

import logging
from typing import Any

from pydantic import ValidationError

from pipeline.utils.enum_utils import fuzzy_match_enum
from ..schemas.deep_analysis import (
    QualitativeAssessment,
    ValueAssessment,
    ForesightAndActionability,
)
from .fuzzy_maps import (
    SENTIMENT_FUZZY,
    DEVELOPER_TONE_FUZZY,
    HYPE_LEVEL_FUZZY,
    ENTROPY_FUZZY,
    ENGINEERING_COMPLEXITY_FUZZY,
    VALUE_CAPTURE_FUZZY,
    MOAT_IMPACT_FUZZY,
    CONFIDENCE_FUZZY,
    ACTIONABLE_INSIGHT_FUZZY,
)

logger = logging.getLogger(__name__)


# =============================================================================
# 辅助函数
# =============================================================================


def _get_nested(data: dict, loc: tuple) -> Any:
    """
    从嵌套字典中按路径 loc 取值。

    例：loc=('developerSentiment','tone') → data['developerSentiment']['tone']
    任一级 key 不存在或非 dict 时返回 None。
    """
    current = data
    for key in loc:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current


# =============================================================================
# QualitativeAssessment 校验
# =============================================================================


def validate_qualitative(data: dict) -> QualitativeAssessment:
    """
    验证并构造 QualitativeAssessment 实例。

    处理流程：
        1. 自动包装标量嵌套字段（impactScore / developerSentiment / hypeAssessment / domainDisruption）
        2. Pydantic 严格校验
        3. 校验失败 → 模糊匹配修正 sentiment / informationEntropy / engineeringComplexity 及嵌套枚举
        4. 确保 domainDisruption 存在
        5. 修复后重新校验

    参数：
        data: LLM 返回的原始 dict

    返回：
        QualitativeAssessment 实例

    异常：
        ValueError: 模糊匹配后仍无法通过 Pydantic 校验
    """
    repaired = dict(data)

    # --- 预处理：修复常见的嵌套模型格式错误 ---

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
                matched = fuzzy_match_enum(raw_value, SENTIMENT_FUZZY, "sentiment")
                if matched:
                    repaired["sentiment"] = matched
                    logger.info("sentiment 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "informationEntropy":
                matched = fuzzy_match_enum(raw_value, ENTROPY_FUZZY, "informationEntropy")
                if matched:
                    repaired["informationEntropy"] = matched
                    logger.info("informationEntropy 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "engineeringComplexity":
                matched = fuzzy_match_enum(raw_value, ENGINEERING_COMPLEXITY_FUZZY, "engineeringComplexity")
                if matched:
                    repaired["engineeringComplexity"] = matched
                    logger.info("engineeringComplexity 修复: '%s' → '%s'", raw_value, matched)

            # 嵌套枚举字段
            elif field_path == "developerSentiment" and len(loc) > 1:
                if loc[1] == "tone":
                    matched = fuzzy_match_enum(raw_value, DEVELOPER_TONE_FUZZY, "developerSentiment.tone")
                    if matched and isinstance(repaired.get("developerSentiment"), dict):
                        repaired["developerSentiment"]["tone"] = matched
                        logger.info("developerSentiment.tone 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "hypeAssessment" and len(loc) > 1:
                if loc[1] == "level":
                    matched = fuzzy_match_enum(raw_value, HYPE_LEVEL_FUZZY, "hypeAssessment.level")
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


# =============================================================================
# ValueAssessment 校验
# =============================================================================


def validate_value(data: dict) -> ValueAssessment:
    """
    验证并构造 ValueAssessment 实例。

    处理流程：
        1. 自动包装标量 compoundValue → {score, reason}
        2. Pydantic 严格校验
        3. 校验失败 → 模糊匹配修正 valueCaptureLayer / moatImpact
        4. 确保列表字段 keyBeneficiaries / competitiveCasualty 存在
        5. 修复后重新校验

    参数：
        data: LLM 返回的原始 dict

    返回：
        ValueAssessment 实例

    异常：
        ValueError: 模糊匹配后仍无法通过 Pydantic 校验
    """
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
                matched = fuzzy_match_enum(raw_value, VALUE_CAPTURE_FUZZY, "valueCaptureLayer")
                if matched:
                    repaired["valueCaptureLayer"] = matched
                    logger.info("valueCaptureLayer 修复: '%s' → '%s'", raw_value, matched)

            elif field_path == "moatImpact":
                matched = fuzzy_match_enum(raw_value, MOAT_IMPACT_FUZZY, "moatImpact")
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


# =============================================================================
# ForesightAndActionability 校验
# =============================================================================


def validate_foresight(data: dict) -> ForesightAndActionability:
    """
    验证并构造 ForesightAndActionability 实例。

    处理流程：
        1. 自动包装标量 confidence → {impact, compound, hype}
        2. Pydantic 严格校验
        3. 校验失败 → 模糊匹配修正 actionableInsight / confidence.{impact, compound, hype}
        4. 确保 marketOpportunities / riskMatrix 存在
        5. 修复后重新校验

    参数：
        data: LLM 返回的原始 dict

    返回：
        ForesightAndActionability 实例

    异常：
        ValueError: 模糊匹配后仍无法通过 Pydantic 校验
    """
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
                matched = fuzzy_match_enum(raw_value, ACTIONABLE_INSIGHT_FUZZY, "actionableInsight")
                if matched:
                    repaired["actionableInsight"] = matched
                    logger.info("actionableInsight 修复: '%s' → '%s'", raw_value, matched)

            # 嵌套枚举 (confidence.{impact, compound, hype})
            elif field_path == "confidence" and len(loc) > 1:
                sub_field = loc[1]
                if sub_field in ("impact", "compound", "hype"):
                    matched = fuzzy_match_enum(raw_value, CONFIDENCE_FUZZY, f"confidence.{sub_field}")
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
