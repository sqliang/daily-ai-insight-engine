"""pipeline/synthesis — Stage 4: 综合洞察与报告生成"""

from .aggregate_frontmatter import aggregate_frontmatter
from .run_synthesis import synthesize_report
from .report_generator import validate_report, generate_markdown

__all__ = ["aggregate_frontmatter", "synthesize_report", "validate_report", "generate_markdown"]
