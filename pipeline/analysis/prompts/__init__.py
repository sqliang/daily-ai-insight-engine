"""
pipeline/analysis/prompts — Stage 3 Deep Analysis 提示词

目录结构：
    - qualitative_system.py: QualitativeAssessment system prompt（技术架构师）
    - value_system.py: ValueAssessment system prompt（VC 资本分析师）
    - foresight_system.py: ForesightAndActionability system prompt（风控专家）
    - user_prompts.py: 3 个 user prompt 构建器（文章数据注入 + 指令）

对外接口保持与原有 prompts.py 完全兼容。
"""

from .qualitative_system import get_qualitative_system_prompt
from .value_system import get_value_system_prompt
from .foresight_system import get_foresight_system_prompt

from .user_prompts import (
    build_qualitative_user_prompt,
    build_value_user_prompt,
    build_foresight_user_prompt,
)

__all__ = [
    "get_qualitative_system_prompt",
    "build_qualitative_user_prompt",
    "get_value_system_prompt",
    "build_value_user_prompt",
    "get_foresight_system_prompt",
    "build_foresight_user_prompt",
]
