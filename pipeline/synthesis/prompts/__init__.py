"""pipeline/synthesis/prompts — Stage 4b 提示词"""

from .system_prompt import EDITOR_IN_CHIEF_SYSTEM_PROMPT
from .user_prompt import build_user_prompt

__all__ = ["EDITOR_IN_CHIEF_SYSTEM_PROMPT", "build_user_prompt"]
