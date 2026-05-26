"""
pipeline/aggregation/ — Stage 4a: Frontmatter 聚合

将各 stage 目录的 YAML frontmatter 提取聚合为 per-source JSON + all_articles.json，
被 extraction/analysis/synthesis 三个阶段共享调用。
"""

from .aggregate_frontmatter import aggregate_frontmatter

__all__ = ["aggregate_frontmatter"]
