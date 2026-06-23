"""
pipeline/extraction/__init__.py — Stage 2 提取阶段包

导出：
    - run_extraction: 异步编排入口 (orchestrator.py)
    - extract_base_info: 单文件 BaseInfo 提取 (base_info/extractor.py)
    - extract_fact_extraction: 单文件 FactExtraction 提取 (fact_extraction/extractor.py)
"""

from .orchestrator import run_extraction
from .base_info.extractor import extract_base_info
from .fact_extraction.extractor import extract_fact_extraction
from .repair import repair_failed_extractions

__all__ = [
    "run_extraction",
    "extract_base_info",
    "extract_fact_extraction",
    "repair_failed_extractions",
]
