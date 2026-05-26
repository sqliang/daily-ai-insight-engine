"""pipeline/synthesis — Stage 4b: 日报合成与报告生成"""

from ..aggregation import aggregate_frontmatter
from .run_synthesis import synthesize_report
from .report_generator import generate_markdown

__all__ = ["aggregate_frontmatter", "synthesize_report", "generate_markdown"]
