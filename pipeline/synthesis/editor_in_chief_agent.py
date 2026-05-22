"""
pipeline/synthesis/editor_in_chief_agent.py — Stage 4b: Editor-in-Chief LLM Agent

功能：
    - 读取 data/04_structured/all_articles.json
    - 构造 system + user prompts
    - 调用 call_agent_with_retry() 生成日报 JSON
    - 解析、校验、返回日报 dict

设计原则：
    - 单次 Claude Opus 调用，处理全部 200+ 篇文章的合成
    - user prompt 包含预计算的统计摘要 + Top-N 完整 frontmatter + 剩余文章标题
    - system prompt 定义角色、输出 schema 和 9 条质控规则
"""

import asyncio
import json
import logging
from pathlib import Path
from typing import Optional

from ..core.agent import call_agent_with_retry, parse_json_response
from pipeline.utils.file_utils import read_json, ensure_dir
from .prompts.system_prompt import EDITOR_IN_CHIEF_SYSTEM_PROMPT
from .prompts.user_prompt import build_user_prompt
from .report_generator import validate_report

logger = logging.getLogger(__name__)

# 默认配置（与 config.yaml llm.synthesize 对齐）
DEFAULT_SYNTHESIS_MODEL = "claude-opus-4-7"
DEFAULT_MAX_DETAIL = 30
DEFAULT_MAX_TOKENS = 16384


def _build_prompts(all_articles_path: Path, max_detail: int = DEFAULT_MAX_DETAIL) -> tuple[str, str]:
    """
    读取 all_articles.json 并构造 system + user prompts。

    参数：
        all_articles_path: all_articles.json 路径
        max_detail: 包含完整 frontmatter 的文章数上限

    返回：
        (system_prompt, user_prompt)
    """
    data = read_json(all_articles_path)
    if data is None:
        raise FileNotFoundError(f"找不到 all_articles.json: {all_articles_path}")

    articles = data.get("articles", [])
    if not articles:
        raise ValueError("all_articles.json 的 articles 列表为空")

    logger.info("构建 prompt — 总文章: %d, 详细展示: %d", len(articles), max_detail)
    user_prompt = build_user_prompt(articles, max_detail=max_detail)
    return EDITOR_IN_CHIEF_SYSTEM_PROMPT, user_prompt


async def run_editor_in_chief(
    all_articles_path: Path,
    *,
    model: Optional[str] = None,
    max_detail: int = DEFAULT_MAX_DETAIL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> dict:
    """
    执行 Editor-in-Chief 合成。

    流程：
        1. 读取 all_articles.json 并构造 prompts
        2. 调用 Claude Opus Agent（带重试）
        3. 从响应中解析 JSON
        4. 校验 JSON 结构完整性
        5. 返回日报 dict

    参数：
        all_articles_path: all_articles.json 文件路径
        model: LLM 模型名称（默认 claude-opus-4-7）
        max_detail: user prompt 中完整展示的文章数
        max_tokens: Agent max_tokens

    返回：
        日报 dict（符合 dailyReportSchema 结构）
    """
    model = model or DEFAULT_SYNTHESIS_MODEL

    system_prompt, user_prompt = _build_prompts(all_articles_path, max_detail=max_detail)

    logger.info(
        "调用 Editor-in-Chief Agent (model=%s, prompt 长度: system=%d chars, user=%d chars)",
        model,
        len(system_prompt),
        len(user_prompt),
    )

    response_text = await call_agent_with_retry(
        prompt=user_prompt,
        system_prompt=system_prompt,
        model=model,
        max_turns=1,
        max_retries=3,
        initial_delay=2.0,
    )

    report = parse_json_response(response_text)

    validation = validate_report(report)
    if not validation["valid"]:
        error_list = "\n  - ".join(validation["errors"])
        logger.warning("日报 JSON 校验发现问题:\n  - %s", error_list)
    if validation.get("warnings"):
        warn_list = "\n  - ".join(validation["warnings"])
        logger.info("日报 JSON 校验提醒:\n  - %s", warn_list)

    return report


def run_editor_in_chief_sync(
    all_articles_path: Path,
    *,
    model: Optional[str] = None,
    max_detail: int = DEFAULT_MAX_DETAIL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> dict:
    """同步包装器，方便 CLI 调用。"""
    return asyncio.run(
        run_editor_in_chief(
            all_articles_path,
            model=model,
            max_detail=max_detail,
            max_tokens=max_tokens,
        )
    )
