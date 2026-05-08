"""
pipeline/analysis — Stage 3: 深度分析

对每篇文章并行运行 3 个 Agent：
    - QualitativeAssessment（技术架构师视角）
    - ValueAssessment（资本分析师视角）
    - ForesightAndActionability（风控专家视角）

入口函数：run_analysis()
"""

from .run_analysis import run_analysis

__all__ = ["run_analysis"]
