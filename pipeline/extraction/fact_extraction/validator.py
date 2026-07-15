"""
pipeline/extraction/fact_extraction/validator.py — Stage 2b: Pydantic 校验 + 模糊枚举修复

处理 Agent 返回的非标准枚举值，包括：
    - 模糊枚举匹配（如 "infrastructure" → "infrastructure_update"）
    - 交叉互换检测（eventType 和 epistemicStatus 值互换）
    - 单向字段修复（Agent 将值填入错误字段）
    - 文本截断（tldr/objectiveSummary 超长时断句截断）
"""

import logging

from pipeline.utils.text_utils import truncate_at_natural_break
from pipeline.utils.enum_utils import fuzzy_match_enum
from ...schemas.fact_extraction import (
    FactExtraction,
    EventType,
    EpistemicStatus,
)

logger = logging.getLogger(__name__)

# =============================================================================
# 所有 FactExtraction 字段名（用于 skip_existing 检查）
# =============================================================================

_FACT_EXTRACTION_FIELDS: set[str] = set(FactExtraction.model_fields.keys())


# =============================================================================
# 模糊枚举匹配映射表
# =============================================================================

_EVENT_TYPE_FUZZY: dict[str, str] = {
    "infrastructure": "infrastructure_update",
    "infra": "infrastructure_update",
    "infra_update": "infrastructure_update",
    "hardware": "infrastructure_update",
    "framework": "framework_tools",
    "tools": "framework_tools",
    "tool": "framework_tools",
    "oss": "framework_tools",
    "open_source": "framework_tools",
    "capital": "capital_movement",
    "funding": "capital_movement",
    "investment": "capital_movement",
    "acquisition": "capital_movement",
    "ipo": "capital_movement",
    "application": "application_landing",
    "product": "application_landing",
    "launch": "application_landing",
    "deployment": "application_landing",
    "policy": "policy_and_safety",
    "regulation": "policy_and_safety",
    "safety": "policy_and_safety",
    "security": "policy_and_safety",
    "governance": "policy_and_safety",
}

_EPISTEMIC_FUZZY: dict[str, str] = {
    "fact": "verified_fact",
    "verified": "verified_fact",
    "confirmed": "verified_fact",
    "pr": "pr_statement",
    "announcement": "pr_statement",
    "press_release": "pr_statement",
    "marketing": "pr_statement",
    "claim": "theoretical_claim",
    "theory": "theoretical_claim",
    "hypothesis": "theoretical_claim",
    "research": "theoretical_claim",
    "rumor": "rumor_leak",
    "leak": "rumor_leak",
    "unconfirmed": "rumor_leak",
    "speculation": "rumor_leak",
}


# =============================================================================
# 校验 + 修复
# =============================================================================

def _truncate_string_field(
    repaired: dict,
    original: dict,
    field_names: tuple[str, ...],
    max_len: int,
) -> None:
    """
    对可能使用别名或 snake_case 的文本字段做长度兜底。

    参数：
        repaired: 待修复的 Agent 返回字典
        original: 原始 Agent 返回字典，用于日志记录原始长度
        field_names: 同一语义字段的可接受键名列表
        max_len: Pydantic schema 允许的最大字符数

    设计理由：
        Pydantic 允许 objectiveSummary/objective_summary 双写法，但 Agent 偶尔会返回
        snake_case。截断逻辑必须覆盖两种键名，否则历史文章重跑会被同一个长度错误反复阻塞。
    """
    for field_name in field_names:
        value = repaired.get(field_name)
        if not isinstance(value, str) or len(value) <= max_len:
            continue

        truncated = truncate_at_natural_break(value, max_len)
        if len(truncated) > max_len:
            truncated = truncated[:max_len].strip()

        repaired[field_name] = truncated
        logger.info(
            "%s 截断: %d → %d 字符",
            field_name,
            len(original.get(field_name, "")),
            len(repaired[field_name]),
        )

def _validate_fact_extraction(data: dict) -> FactExtraction:
    """
    验证并构造 FactExtraction 实例。

    处理流程：
        1. 先用 Pydantic 严格校验
        2. 如果枚举值校验失败 → 尝试模糊匹配
        3. 检测 enum 交叉互换（eventType ↔ epistemicStatus）
        4. 单向字段修复
        5. 确保 entities / keyLogicFlow 存在
        6. 截断超长文本字段
        7. 修复后重新校验

    参数：
        data: Agent 返回的原始 JSON 字典

    返回：
        验证通过的 FactExtraction 实例

    异常：
        ValueError: 模糊匹配也失败时抛出
    """
    from pydantic import ValidationError

    # --- 尝试严格校验 ---
    try:
        return FactExtraction.model_validate(data)
    except ValidationError as pydantic_err:
        errors = pydantic_err.errors()
        logger.warning("FactExtraction 严格校验失败: %s", errors)

        # --- 尝试修复枚举值 ---
        repaired = dict(data)
        _already_swapped = False

        for error in errors:
            loc = error.get("loc", [])
            if not loc:
                continue

            field_name = loc[0]
            raw_value = data.get(field_name)

            if field_name in ("eventType", "event_type") and isinstance(raw_value, str):
                matched = fuzzy_match_enum(raw_value, _EVENT_TYPE_FUZZY, "eventType")
                if matched:
                    repaired[field_name] = matched
                    logger.info("eventType 修复: '%s' → '%s'", raw_value, matched)

            if field_name in ("epistemicStatus", "epistemic_status") and isinstance(raw_value, str):
                matched = fuzzy_match_enum(raw_value, _EPISTEMIC_FUZZY, "epistemicStatus")
                if matched:
                    repaired[field_name] = matched
                    logger.info("epistemicStatus 修复: '%s' → '%s'", raw_value, matched)

        # --- 检测 enum 交叉互换 ---
        if not _already_swapped:
            evt_raw = repaired.get("eventType") or repaired.get("event_type")
            eps_raw = repaired.get("epistemicStatus") or repaired.get("epistemic_status")

            if isinstance(evt_raw, str) and isinstance(eps_raw, str):
                evt_is_eps = (
                    evt_raw in _EPISTEMIC_FUZZY
                    or fuzzy_match_enum(evt_raw, _EPISTEMIC_FUZZY, "eventType→epistemicStatus") is not None
                    or evt_raw in EpistemicStatus.__members__
                )
                eps_is_evt = (
                    eps_raw in _EVENT_TYPE_FUZZY
                    or fuzzy_match_enum(eps_raw, _EVENT_TYPE_FUZZY, "epistemicStatus→eventType") is not None
                    or eps_raw in EventType.__members__
                )

                if evt_is_eps and eps_is_evt:
                    evt_matched = (
                        fuzzy_match_enum(eps_raw, _EVENT_TYPE_FUZZY, "epistemicStatus→eventType")
                        or eps_raw
                    )
                    eps_matched = (
                        fuzzy_match_enum(evt_raw, _EPISTEMIC_FUZZY, "eventType→epistemicStatus")
                        or evt_raw
                    )
                    evt_key = "eventType" if "eventType" in repaired else "event_type"
                    eps_key = "epistemicStatus" if "epistemicStatus" in repaired else "epistemic_status"
                    repaired[evt_key] = evt_matched
                    repaired[eps_key] = eps_matched
                    _already_swapped = True
                    logger.info(
                        "检测到 enum 交叉互换: eventType('%s') ↔ epistemicStatus('%s') → 已交换",
                        evt_raw, eps_raw,
                    )

        # --- 单向 enum 修复 ---
        if not _already_swapped:
            evt_key = "eventType" if "eventType" in repaired else "event_type"
            eps_key = "epistemicStatus" if "epistemicStatus" in repaired else "epistemic_status"

            evt_val = repaired.get(evt_key)
            eps_val = repaired.get(eps_key)

            if isinstance(evt_val, str) and isinstance(eps_val, str):
                evt_as_eps = fuzzy_match_enum(evt_val, _EPISTEMIC_FUZZY, "eventType→epistemicStatus")
                evt_as_evt = fuzzy_match_enum(evt_val, _EVENT_TYPE_FUZZY, "eventType")
                evt_is_valid_event = (
                    evt_as_evt is not None
                    or evt_val in EventType.__members__
                )
                eps_as_eps = fuzzy_match_enum(eps_val, _EPISTEMIC_FUZZY, "epistemicStatus")
                eps_is_valid_eps = (
                    eps_as_eps is not None
                    or eps_val in EpistemicStatus.__members__
                )

                if evt_as_eps is not None and not evt_is_valid_event:
                    repaired[eps_key] = evt_as_eps
                    repaired[evt_key] = "framework_tools"
                    logger.info(
                        "单向修复 eventType: '%s' → epistemicStatus, eventType 回退为 framework_tools",
                        evt_val,
                    )
                elif eps_as_eps is None and not eps_is_valid_eps:
                    eps_as_evt = fuzzy_match_enum(eps_val, _EVENT_TYPE_FUZZY, "epistemicStatus→eventType")
                    if eps_as_evt is not None:
                        repaired[evt_key] = eps_as_evt
                        repaired[eps_key] = "verified_fact"
                        logger.info(
                            "单向修复 epistemicStatus: '%s' → eventType, epistemicStatus 回退为 verified_fact",
                            eps_val,
                        )

        # --- 确保 entities 字段存在 ---
        if "entities" not in repaired or not isinstance(repaired.get("entities"), dict):
            repaired["entities"] = {"companies": [], "technologies": [], "keyPeople": []}

        # --- 确保 keyLogicFlow 存在 ---
        if "keyLogicFlow" not in repaired:
            repaired["keyLogicFlow"] = []

        # --- 截断超长文本字段 ---
        _truncate_string_field(repaired, data, ("tldr",), 250)
        _truncate_string_field(repaired, data, ("objectiveSummary", "objective_summary"), 500)

        # --- 修复后重新校验 ---
        try:
            return FactExtraction.model_validate(repaired)
        except ValidationError as second_err:
            raise ValueError(
                f"FactExtraction 校验失败（模糊匹配后仍失败）: {second_err}"
            ) from second_err
