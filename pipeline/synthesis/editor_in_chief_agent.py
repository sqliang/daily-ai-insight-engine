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

from pydantic import ValidationError

from ..core.agent import call_agent_with_retry, parse_json_response
from pipeline.utils.file_utils import read_json, ensure_dir
from .prompts.system_prompt import EDITOR_IN_CHIEF_SYSTEM_PROMPT
from .prompts.user_prompt import build_user_prompt
from ..schemas.daily_report import validate_daily_report

logger = logging.getLogger(__name__)

# 默认配置（与 config.yaml llm.synthesize 对齐）
DEFAULT_SYNTHESIS_MODEL = "claude-opus-4-7"
DEFAULT_MAX_DETAIL = 30
DEFAULT_MAX_TOKENS = 16384


def _apply_cjk_spacing(report: dict) -> None:
    """
    递归遍历报告 dict，对所有字符串值应用中英文间距规范化。

    处理 LLM 生成的中英文混排文本缺少 CJK-Latin 空格的问题，
    对 executiveSummary、whyItMatters、background 等所有文本字段
    自动插入规范间距。
    """
    from pipeline.utils.text_utils import insert_cjk_spacing

    def _walk(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str):
                    obj[key] = insert_cjk_spacing(value)
                elif isinstance(value, (dict, list)):
                    _walk(value)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, str):
                    obj[i] = insert_cjk_spacing(item)
                elif isinstance(item, (dict, list)):
                    _walk(item)

    _walk(report)


def _enrich_evidence_sources(report: dict) -> None:
    """
    从 all_articles.json 中解析 articleIds → URL 映射，
    为每个 topEvent 生成 evidenceSources 数组供前端渲染可点击来源链接，
    同时在 evidence 文本末尾追加内联编号标记 [1][2]...。

    all_articles.json 路径为 data/04_structured/all_articles.json。
    """
    import re
    from pipeline.core.config_loader import resolve_data_dir
    from pipeline.utils.file_utils import read_json

    # 清理 evidence 中 LLM 可能残留的内联引用文本
    _CITATION_CLEANUP_RE = re.compile(r'\s*[（(]来源[：:][^)）]*[)）]\s*')

    all_articles_path = resolve_data_dir("synthesize_structured") / "all_articles.json"
    if not all_articles_path.exists():
        logger.warning("无法解析 evidenceSources: all_articles.json 不存在")
        return

    data = read_json(all_articles_path)
    if not data:
        return

    articles = data.get("articles", [])
    # 构建 id → {source_dir, title, source(url)} 映射
    id_map: dict[str, dict] = {}
    for a in articles:
        aid = a.get("id", "")
        if aid and a.get("source"):
            id_map[aid] = {
                "source_dir": a.get("source_dir", ""),
                "title": a.get("title", ""),
                "url": a.get("source", ""),
            }

    for event in report.get("topEvents", []):
        sources = []
        seen_urls = set()
        for aid in event.get("articleIds", []):
            info = id_map.get(aid)
            if info and info["url"] not in seen_urls:
                seen_urls.add(info["url"])
                sources.append({
                    "sourceDir": info["source_dir"],
                    "title": info["title"],
                    "url": info["url"],
                })
        event["evidenceSources"] = sources

        # 构建 articleId → 全局编号的映射（基于 evidenceSources 的顺序）
        # evidenceSources 已按首次出现排序并去重
        id_to_global_num: dict[str, int] = {}
        for idx, s in enumerate(sources):
            # 反向查找：哪些 articleIds 映射到了这个 source
            for aid in event.get("articleIds", []):
                info = id_map.get(aid)
                if info and info["url"] == s["url"]:
                    id_to_global_num[aid] = idx + 1  # 1-based

        # 为每条 evidence 末尾追加精准编号标记
        evidence_article_ids = event.get("evidenceArticleIds", [])
        for j in range(len(event.get("evidence", []))):
            ev = event["evidence"][j]
            ev = _CITATION_CLEANUP_RE.sub("", ev).rstrip()

            # 获取本条 evidence 对应的 articleIds
            ev_article_ids = (
                evidence_article_ids[j]
                if j < len(evidence_article_ids) and evidence_article_ids[j]
                else []
            )

            if ev_article_ids and id_to_global_num:
                # 精准模式：只标注 LLM 指定的 article 对应的编号
                nums = []
                seen_nums = set()
                for aid in ev_article_ids:
                    n = id_to_global_num.get(aid)
                    if n is not None and n not in seen_nums:
                        seen_nums.add(n)
                        nums.append(n)
                if nums:
                    markers = "".join(f"[{n}]" for n in sorted(nums))
                    ev = f"{ev} {markers}"
            elif sources:
                # 降级：LLM 未输出 evidenceArticleIds，用计数徽章
                ev = f"{ev} [{len(sources)}来源]"

            event["evidence"][j] = ev

    logger.info(
        "evidenceSources 已解析: %d 个事件, %d 个来源",
        len(report.get("topEvents", [])),
        sum(len(e.get("evidenceSources", [])) for e in report.get("topEvents", [])),
    )


def _build_prompts(
    all_articles_path: Path,
    max_detail: int = DEFAULT_MAX_DETAIL,
    target_date: Optional[str] = None,
) -> tuple[str, str]:
    """
    读取 all_articles.json 并构造 system + user prompts。

    参数：
        all_articles_path: all_articles.json 路径
        max_detail: 包含完整 frontmatter 的文章数上限
        target_date: 目标报告日期（YYYY-MM-DD），注入 prompt 让 LLM 以此为上下文

    返回：
        (system_prompt, user_prompt)
    """
    data = read_json(all_articles_path)
    if data is None:
        raise FileNotFoundError(f"找不到 all_articles.json: {all_articles_path}")

    articles = data.get("articles", [])
    if not articles:
        raise ValueError("all_articles.json 的 articles 列表为空")

    logger.info("构建 prompt — 总文章: %d, 详细展示: %d, target_date=%s", len(articles), max_detail, target_date)
    user_prompt = build_user_prompt(articles, max_detail=max_detail, target_date=target_date)
    return EDITOR_IN_CHIEF_SYSTEM_PROMPT, user_prompt


async def run_editor_in_chief(
    all_articles_path: Path,
    *,
    model: Optional[str] = None,
    max_detail: int = DEFAULT_MAX_DETAIL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    target_date: Optional[str] = None,
) -> dict:
    """
    执行 Editor-in-Chief 合成。

    流程：
        1. 读取 all_articles.json 并构造 prompts
        2. 调用 Claude Opus Agent（带重试）
        3. 从响应中解析 JSON
        4. 校验 JSON 结构完整性
        5. 若指定 target_date，覆盖报告日期字段
        6. 返回日报 dict

    参数：
        all_articles_path: all_articles.json 文件路径
        model: LLM 模型名称（默认 claude-opus-4-7）
        max_detail: user prompt 中完整展示的文章数
        max_tokens: Agent max_tokens
        target_date: 目标报告日期（YYYY-MM-DD），None 时由 LLM 自主决定

    返回：
        日报 dict（符合 dailyReportSchema 结构）
    """
    model = model or DEFAULT_SYNTHESIS_MODEL

    system_prompt, user_prompt = _build_prompts(
        all_articles_path, max_detail=max_detail, target_date=target_date
    )

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

    try:
        validated = validate_daily_report(report)
        report = validated.model_dump(mode="json", by_alias=True)
    except ValidationError as exc:
        logger.warning("日报 JSON Pydantic 校验失败 (%d 个错误):\n  %s", len(exc.errors()), exc.errors())
        # 校验失败不阻断流程，仍返回原始 dict

    # 中英文混排间距规范化：对所有文本字段自动插入 CJK-Latin 间距
    _apply_cjk_spacing(report)

    # 来源 URL 解析：从 articleIds 查 all_articles.json 获取原文 URL
    _enrich_evidence_sources(report)

    # 若指定 target_date，覆盖 LLM 输出的日期字段，确保报告日期和文件命名一致
    if target_date:
        report["date"] = target_date
        logger.info("报告日期已覆盖为 target_date=%s", target_date)

    return report


def run_editor_in_chief_sync(
    all_articles_path: Path,
    *,
    model: Optional[str] = None,
    max_detail: int = DEFAULT_MAX_DETAIL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    target_date: Optional[str] = None,
) -> dict:
    """同步包装器，方便 CLI 调用。"""
    return asyncio.run(
        run_editor_in_chief(
            all_articles_path,
            model=model,
            max_detail=max_detail,
            max_tokens=max_tokens,
            target_date=target_date,
        )
    )
