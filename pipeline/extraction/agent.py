"""
pipeline/extraction/agent.py — Re-export shim (DEPRECATED)

本模块内容已迁移至 pipeline.core.agent。
从本路径导入仍然可用（向后兼容），但新代码应直接从 pipeline.core.agent 导入。
"""

from ..core.agent import (  # noqa: F401
    StageResult,
    AgentCallError,
    call_agent,
    call_agent_with_retry,
    parse_json_response,
    build_agent_options,
)
