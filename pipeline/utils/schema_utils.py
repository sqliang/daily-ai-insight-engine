"""
pipeline/utils/schema_utils.py — 扁平 YAML frontmatter 到 DailyAIInsight 嵌套结构的桥接

功能：
    - flat_frontmatter_to_nested(): 将扁平 YAML frontmatter dict 的字段路由到 DailyAIInsight 的 5 个子模型
    - 在模块加载时从 DailyAIInsight.model_fields 自动构建字段映射，无需手动维护

设计理由：
    YAML frontmatter 将所有阶段的字段以扁平形式存储（如 title、tldr、impactScore 都在同一层），
    而 DailyAIInsight 期望嵌套结构（base_info.title、fact_extraction.tldr、qualitative_assessment.impactScore）。
    此模块通过字段名反向查找，将每个扁平 key 路由到正确的子模型。
    非 schema 字段（如 pipeline_stage、source_dir、tags）静默忽略。
"""

from __future__ import annotations

from pipeline.schemas.daily_ai_insight import DailyAIInsight

# ---------------------------------------------------------------------------
# 模块加载时构建字段 → 父模型映射
# ---------------------------------------------------------------------------

# DailyAIInsight 的 5 个顶层字段名 → 子模型类
_SUB_MODEL_SLOTS: dict[str, type] = {}
for _field_name, _field_info in DailyAIInsight.model_fields.items():
    _SUB_MODEL_SLOTS[_field_name] = _field_info.annotation

# 每个子模型字段的 Python 名 → 父槽位名
_FIELD_TO_PARENT: dict[str, str] = {}
# 每个子模型字段的 alias → 父槽位名（兼容 camelCase 旧格式 frontmatter）
_ALIAS_TO_PARENT: dict[str, str] = {}

for _parent_key, _sub_cls in _SUB_MODEL_SLOTS.items():
    for _sub_field_name, _sub_field_info in _sub_cls.model_fields.items():
        _FIELD_TO_PARENT[_sub_field_name] = _parent_key
        _alias = _sub_field_info.alias
        if _alias and _alias != _sub_field_name:
            _ALIAS_TO_PARENT[_alias] = _parent_key


def flat_frontmatter_to_nested(fm: dict) -> dict[str, dict]:
    """
    将扁平 YAML frontmatter dict 转换为 DailyAIInsight 期望的嵌套结构。

    遍历扁平 dict 的每个 key，将其路由到对应的子模型槽位。
    非 schema 字段（如 pipeline_stage、source_dir）静默忽略。
    支持 Python 名（snake_case）和 camelCase alias 两种键名。

    参数：
        fm: 扁平 frontmatter dict（来自 YAML frontmatter）

    返回：
        嵌套 dict，键为 DailyAIInsight 的 5 个顶层字段名：
        {"base_info": {...}, "fact_extraction": {...}, "qualitative_assessment": {...},
         "value_assessment": {...}, "foresight_and_actionability": {...}}
        无数据的子模型对应空 dict
    """
    result: dict[str, dict] = {key: {} for key in _SUB_MODEL_SLOTS}

    for key, value in fm.items():
        parent = _FIELD_TO_PARENT.get(key)
        if parent is None:
            parent = _ALIAS_TO_PARENT.get(key)
        if parent is not None:
            result[parent][key] = value
        # 非 schema 字段静默忽略

    return result
