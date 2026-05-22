"""
pipeline/utils/enum_utils.py — 枚举值模糊匹配工具

共享的模糊枚举匹配逻辑，被 extraction (fact_extraction_agent) 和
analysis (deep_analysis_agent) 共用，处理 Agent LLM 返回的非标准枚举值。
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


def fuzzy_match_enum(value: str, mapping: dict[str, str], enum_name: str) -> Optional[str]:
    """
    模糊匹配枚举值。

    匹配策略：
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

    # 子串包含匹配：检查 key 是否包含映射键或被映射键包含
    for k, v in mapping.items():
        if k in key or key in k:
            logger.info("模糊匹配 %s: '%s' → '%s' (匹配键 '%s')", enum_name, value, v, k)
            return v

    return None
