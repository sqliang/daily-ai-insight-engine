"""
pipeline/extraction/base_info/__init__.py — Stage 2a: BaseInfo 提取

从文章 frontmatter 中提取 BaseInfo 元信息（id, title, source, source_type 等）。
source_type 优先从 config.yaml 的目录名映射推断，仅兜底时调用 Agent。
"""

from .extractor import extract_base_info
from .runner import run_base_info_stage

__all__ = ["extract_base_info", "run_base_info_stage"]
