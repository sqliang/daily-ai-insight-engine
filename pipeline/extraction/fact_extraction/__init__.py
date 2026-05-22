"""
pipeline/extraction/fact_extraction/__init__.py — Stage 2b: FactExtraction 提取

将非结构化文章正文压缩为高密度客观事实，包括事件定性、实体识别、逻辑还原。
"""

from .extractor import extract_fact_extraction
from .runner import run_fact_extraction_stage

__all__ = ["extract_fact_extraction", "run_fact_extraction_stage"]
