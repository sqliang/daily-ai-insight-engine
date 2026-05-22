"""
pipeline/extraction/__init__.py — Stage 2 提取阶段包

导出：
    - run_extraction: 异步编排入口 (run_extraction.py)
    - extract_base_info: 单文件 BaseInfo 提取 (base_info_agent.py)
    - extract_fact_extraction: 单文件 FactExtraction 提取 (fact_extraction_agent.py)
"""

from .run_extraction import run_extraction
from .agent.base_info_agent import extract_base_info
from .agent.fact_extraction_agent import extract_fact_extraction

__all__ = [
    "run_extraction",
    "extract_base_info",
    "extract_fact_extraction",
]
