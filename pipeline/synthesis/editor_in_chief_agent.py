"""
pipeline/synthesis/editor_in_chief_agent.py — Stage 4b: Editor-in-Chief LLM Agent

功能：
    - 读取 data/04_structured/all_articles.json
    - 构造 system + user prompts
    - 调用 call_agent_with_retry() 生成日报 JSON
    - 解析、校验、返回日报 dict

专题洞察（Specialized Briefs）：
    除通用日报（topEvents / trendInsights / riskSignals 等）外，主编 Agent 还负责生成
    三类垂直专题简报：
        - 项目洞察（projectInsights）：基于 Stage 2 specialized_tags.github 与
          Stage 3 github_assessment 识别的开源项目/技术方案，跨天去重、提炼价值与风险。
        - 论文洞察（paperHighlights / paperInsights）：基于 Stage 2 specialized_tags.paper
          与 Stage 3 paper_assessment 识别的学术论文，解读研究问题与方法创新。
        - 产品洞察（productInsights）：基于 Stage 2 specialized_tags.product 与
          Stage 3 product_assessment 识别的产品动态，分析定位与商业信号。
    专题候选在 _build_prompts() 中按 source_dir 与 specialized_tags 双重筛选并注入 user
    prompt；生成的 specializedBrief 在 _enrich_specialized_sources() 中补齐来源、规整文本，
    确保前端可稳定追溯原文。

设计原则：
    - 单次 LLM 调用，处理全部 200+ 篇文章的合成
    - user prompt 包含预计算的统计摘要 + Top-N 完整 frontmatter + 剩余文章标题
    - system prompt 定义角色、输出 schema 和 9 条质控规则
    - 专题洞察与综合日报共用一次 LLM 调用，但由独立 schema 约束，避免彼此干扰
"""

import asyncio
import json
import logging
import os
from datetime import date, timedelta
from pathlib import Path
from typing import Optional

from pydantic import ValidationError

from ..core.agent import call_agent_with_retry, parse_json_response
from pipeline.utils.file_utils import read_json, ensure_dir
from ..core.config_loader import resolve_data_dir, get_llm_config
from .prompts.system_prompt import EDITOR_IN_CHIEF_SYSTEM_PROMPT
from .prompts.user_prompt import build_user_prompt
from ..schemas.daily_report import validate_daily_report

logger = logging.getLogger(__name__)

# 默认配置（与 config.yaml llm.synthesize 对齐；env 中 ANTHROPIC_MODEL 可作为兜底）
DEFAULT_SYNTHESIS_MODEL = "claude-opus-4-7"
DEFAULT_MAX_DETAIL = 30
DEFAULT_MAX_TOKENS = 16384


def _resolve_default_synthesis_model() -> str:
    """
    解析 synthesize 阶段的默认模型名称。

    优先级：
        1. config.yaml llm.synthesize.name
        2. 环境变量 ANTHROPIC_MODEL
        3. 硬编码兜底 DEFAULT_SYNTHESIS_MODEL

    设计理由：
        保持与 extract / analyze 阶段一致的配置语义，避免 synthesis 阶段
        硬编码模型名而忽略用户在 .env / config.yaml 中的配置。
    """
    config_model = get_llm_config("synthesize").get("name")
    if config_model:
        return config_model

    env_model = os.environ.get("ANTHROPIC_MODEL")
    if env_model:
        return env_model

    return DEFAULT_SYNTHESIS_MODEL


def _extract_github_articles(articles: list[dict]) -> list[dict]:
    """
    从 all_articles.json 的文章列表中提取项目洞察候选文章。

    当前以 source_dir == "github-trending" 为主，同时保留 specialized_tags.github
    作为对象级特征。候选文章将在 prompt 中交给主编 Agent，与昨日 projectInsights
    做跨天去重后生成最终项目洞察。

    参数：
        articles: all_articles.json 中的 articles 列表

    返回：
        source_dir == "github-trending" 的文章列表
    """
    return [a for a in articles if a.get("source_dir") == "github-trending"]


def _extract_product_articles(articles: list[dict]) -> list[dict]:
    """
    从 all_articles.json 的文章列表中提取产品洞察候选文章。

    当前以 source_dir 属于 producthunt / whytryai 为主。这些文章在 Stage 2 已被标注
    specialized_tags.product，Stage 3 生成 product_assessment；prompt 中把候选对象
    注入主编 Agent，与昨日 productInsights 做跨天去重后生成最终产品洞察。

    参数：
        articles: all_articles.json 中的 articles 列表

    返回：
        source_dir == "producthunt" 或 "whytryai" 的文章列表
    """
    return [
        a for a in articles
        if a.get("source_dir") in ("producthunt", "whytryai")
    ]


def _load_yesterday_github_keys(target_date: Optional[str]) -> set[str]:
    """
    读取昨日日报归档，获取已展示的 GitHub 项目去重键集合。

    当前使用 topProjects 中的 project_name 作为去重键（日报中未保存 project_url）。
    若昨日日报不存在或解析失败，返回空集合。

    参数：
        target_date: 目标报告日期（YYYY-MM-DD），None 时使用今天

    返回：
        昨日已展示的 GitHub 项目名集合
    """
    try:
        if target_date:
            yesterday = date.fromisoformat(target_date) - timedelta(days=1)
        else:
            yesterday = date.today() - timedelta(days=1)
    except (ValueError, TypeError):
        return set()

    yesterday_str = yesterday.isoformat()
    reports_dir = resolve_data_dir("reports")
    report_path = reports_dir / f"daily-report-{yesterday_str}.json"

    if not report_path.exists():
        return set()

    try:
        data = read_json(report_path) or {}
        gh = (data.get("specializedBrief") or {}).get("githubHighlights")
        if not gh:
            return set()
        return set(gh.get("topProjects", []))
    except Exception as exc:
        logger.warning("读取昨日日报失败 %s: %s", report_path, exc)
        return set()


def _dedup_github_articles(
    github_articles: list[dict],
    yesterday_keys: set[str],
) -> list[dict]:
    """
    对 GitHub 文章做跨天去重：剔除昨日已展示的项目。

    去重键优先级：
        1. specialized_tags.github.project_url（如果存在）
        2. specialized_tags.github.project_name / 文章 title
    同时检查 project_name 是否在昨日 topProjects 列表中。

    参数：
        github_articles: 当日 GitHub 文章候选列表
        yesterday_keys: 昨日已展示项目名集合

    返回：
        去重后的当日 GitHub 文章列表
    """
    result: list[dict] = []
    seen: set[str] = set()

    for a in github_articles:
        gh = {}
        specialized_tags = a.get("specialized_tags")
        if isinstance(specialized_tags, dict):
            gh = specialized_tags.get("github", {}) or {}

        project_url = gh.get("project_url") or gh.get("projectUrl", "")
        project_name = gh.get("project_name") or gh.get("projectName") or a.get("title", "")

        # 优先用 project_url 作为去重键，无 URL 时退回到 project_name
        key = project_url if project_url else project_name
        if not key:
            continue

        # 同时用 project_name 匹配昨日 topProjects（兼容无 URL 场景）
        if project_name in yesterday_keys or key in yesterday_keys:
            continue

        if key in seen:
            continue

        seen.add(key)
        result.append(a)

    return result


def _load_yesterday_product_keys(target_date: Optional[str]) -> set[str]:
    """
    读取昨日日报归档，获取已展示的产品去重键集合。

    当前使用 productHighlights.notableProducts 中的 product_name 作为去重键。
    若昨日日报不存在或解析失败，返回空集合。

    参数：
        target_date: 目标报告日期（YYYY-MM-DD），None 时使用今天

    返回：
        昨日已展示的产品名集合
    """
    try:
        if target_date:
            yesterday = date.fromisoformat(target_date) - timedelta(days=1)
        else:
            yesterday = date.today() - timedelta(days=1)
    except (ValueError, TypeError):
        return set()

    yesterday_str = yesterday.isoformat()
    reports_dir = resolve_data_dir("reports")
    report_path = reports_dir / f"daily-report-{yesterday_str}.json"

    if not report_path.exists():
        return set()

    try:
        data = read_json(report_path) or {}
        ph = (data.get("specializedBrief") or {}).get("productHighlights")
        if not ph:
            return set()
        return set(ph.get("notableProducts", []))
    except Exception as exc:
        logger.warning("读取昨日日报失败 %s: %s", report_path, exc)
        return set()


def _dedup_product_articles(
    product_articles: list[dict],
    yesterday_keys: set[str],
) -> list[dict]:
    """
    对产品文章做跨天去重：剔除昨日已展示的产品。

    去重键优先级：
        1. specialized_tags.product.product_url（如果存在）
        2. specialized_tags.product.product_name / 文章 title
    同时检查 product_name 是否在昨日 notableProducts 列表中。

    参数：
        product_articles: 当日产品文章候选列表
        yesterday_keys: 昨日已展示产品名集合

    返回：
        去重后的当日产品文章列表
    """
    result: list[dict] = []
    seen: set[str] = set()

    for a in product_articles:
        product = {}
        specialized_tags = a.get("specialized_tags")
        if isinstance(specialized_tags, dict):
            product = specialized_tags.get("product", {}) or {}

        product_url = product.get("product_url") or product.get("productUrl", "")
        product_name = product.get("product_name") or product.get("productName") or a.get("title", "")

        # 优先用 product_url 作为去重键，无 URL 时退回到 product_name
        key = product_url if product_url else product_name
        if not key:
            continue

        # 同时用 product_name 匹配昨日 notableProducts（兼容无 URL 场景）
        if product_name in yesterday_keys or key in yesterday_keys:
            continue

        if key in seen:
            continue

        seen.add(key)
        result.append(a)

    return result


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


_SPECIALIZED_TEXT_MAX_CHARS: dict[str, int] = {
    "keyJudgment": 220,
    "watchSignals": 90,
    "oneLine": 90,
    "whyItMatters": 220,
    "signals": 90,
    "risks": 90,
    "evidenceSnippets": 140,
}


def _normalize_specialized_sentence(value: str, max_chars: int) -> str:
    """
    规整专题洞察最终报告中的展示句子。

    参数：
        value: 主编 Agent 输出的文本字段
        max_chars: 该字段允许的最大展示长度

    返回：
        适合前端展示的完整句子

    设计理由：
        Stage 4 负责最终报告表达，LLM 偶发会输出半句话或缺少句末标点。
        这里做最后一层确定性兜底：清理空白、限制长度、补齐句末标点。
    """
    from pipeline.utils.text_utils import truncate_at_natural_break

    sentence = " ".join(value.strip().split())
    if not sentence:
        return ""

    if len(sentence) > max_chars:
        sentence = truncate_at_natural_break(sentence, max_chars)
        if len(sentence) > max_chars:
            sentence = sentence[:max_chars].rstrip("，,、；;：:")

    if sentence[-1] not in "。！？.!?」』”’）)]":
        sentence = f"{sentence}。"

    return sentence


def _normalize_specialized_string_list(value: object, max_chars: int, limit: int | None = None) -> list[str]:
    """
    规整专题洞察字符串数组。

    参数：
        value: 可能为字符串或字符串数组的原始值
        max_chars: 单条最大字符数
        limit: 最多保留条数

    返回：
        规整后的字符串数组
    """
    if isinstance(value, str):
        raw_values = [value]
    elif isinstance(value, list):
        raw_values = value
    else:
        raw_values = []

    normalized: list[str] = []
    for item in raw_values:
        if not isinstance(item, str):
            continue
        cleaned = _normalize_specialized_sentence(item, max_chars)
        if cleaned and cleaned not in normalized:
            normalized.append(cleaned)

    return normalized[:limit] if limit else normalized


def _normalize_specialized_item_text(item: dict) -> None:
    """
    规整单个专题对象的展示文本字段。

    参数：
        item: projectInsights/productInsights 中的对象条目
    """
    for field_name in ("oneLine", "whyItMatters"):
        value = item.get(field_name)
        if isinstance(value, str):
            item[field_name] = _normalize_specialized_sentence(
                value,
                _SPECIALIZED_TEXT_MAX_CHARS[field_name],
            )

    item["signals"] = _normalize_specialized_string_list(
        item.get("signals"),
        _SPECIALIZED_TEXT_MAX_CHARS["signals"],
    )
    item["risks"] = _normalize_specialized_string_list(
        item.get("risks"),
        _SPECIALIZED_TEXT_MAX_CHARS["risks"],
    )
    item["evidenceSnippets"] = _normalize_specialized_string_list(
        item.get("evidenceSnippets") or item.get("evidence_snippets"),
        _SPECIALIZED_TEXT_MAX_CHARS["evidenceSnippets"],
        limit=3,
    )
    item.pop("evidence_snippets", None)


def _enrich_specialized_sources(report: dict) -> None:
    """
    从 articleIds 补齐专题洞察 items 的 sources，并剔除无有效来源对象。

    设计理由：
        LLM 负责判断和归纳，但来源解析应由 pipeline 做确定性处理。这样即使模型只返回
        articleIds，前端仍能稳定展示标题、信源和原文 URL。专题对象必须能追溯到至少
        一篇文章；补不到来源的条目会被丢弃，避免前端展示无引用洞察。
    """
    all_articles_path = resolve_data_dir("synthesize_structured") / "all_articles.json"
    if not all_articles_path.exists():
        logger.warning("无法解析专题 sources: all_articles.json 不存在")
        return

    data = read_json(all_articles_path)
    if not data:
        return

    id_map: dict[str, dict] = {}
    for article in data.get("articles", []):
        aid = article.get("id", "")
        if not aid:
            continue
        id_map[aid] = {
            "articleId": aid,
            "title": article.get("title", ""),
            "sourceDir": article.get("source_dir", ""),
            "url": article.get("source", ""),
        }

    specialized = report.get("specializedBrief")
    if not isinstance(specialized, dict):
        return

    enriched_count = 0
    dropped_count = 0
    for section_key in ("projectInsights", "productInsights"):
        section = specialized.get(section_key)
        if not isinstance(section, dict):
            continue
        key_judgment = section.get("keyJudgment") or section.get("key_judgment")
        if isinstance(key_judgment, str):
            section["keyJudgment"] = _normalize_specialized_sentence(
                key_judgment,
                _SPECIALIZED_TEXT_MAX_CHARS["keyJudgment"],
            )
            section.pop("key_judgment", None)
        section["watchSignals"] = _normalize_specialized_string_list(
            section.get("watchSignals") or section.get("watch_signals"),
            _SPECIALIZED_TEXT_MAX_CHARS["watchSignals"],
        )
        section.pop("watch_signals", None)

        items = section.get("items") or []
        if not isinstance(items, list):
            continue

        valid_items: list[dict] = []
        coverage: set[str] = set()
        for item in items:
            if not isinstance(item, dict):
                dropped_count += 1
                continue
            raw_article_ids = item.get("articleIds") or item.get("article_ids") or []
            article_ids = [
                aid.strip()
                for aid in raw_article_ids
                if isinstance(aid, str) and aid.strip()
            ] if isinstance(raw_article_ids, list) else []

            if not article_ids:
                dropped_count += 1
                continue

            sources = []
            seen: set[str] = set()
            for aid in article_ids:
                source = id_map.get(aid)
                if not source:
                    continue
                dedup_key = source.get("url") or source.get("articleId")
                if dedup_key in seen:
                    continue
                seen.add(dedup_key)
                sources.append(source)
                if source.get("sourceDir"):
                    coverage.add(source["sourceDir"])

            if not sources:
                dropped_count += 1
                continue

            item["articleIds"] = article_ids
            item.pop("article_ids", None)
            item["sources"] = sources
            _normalize_specialized_item_text(item)
            valid_items.append(item)
            enriched_count += 1

        section["items"] = valid_items
        section["sourceCoverage"] = sorted(coverage)

    logger.info(
        "专题 sources 已解析: 保留 %d 个对象条目, 丢弃 %d 个无来源条目",
        enriched_count,
        dropped_count,
    )


def _build_prompts(
    all_articles_path: Path,
    max_detail: int = DEFAULT_MAX_DETAIL,
    target_date: Optional[str] = None,
) -> tuple[str, str]:
    """
    读取 all_articles.json 并构造 system + user prompts。

    专题洞察预处理：
        在把文章交给主编 Agent 前，先按 source_dir 与 specialized_tags 拆出项目 / 产品
        两类洞察候选，并与昨日日报做跨天去重（避免同一项目/产品连续多日重复出现）。去重后
        的候选文章作为独立上下文注入 user prompt，让 Agent 在生成综合日报的同时，输出
        specializedBrief 块。论文洞察目前由 Agent 基于 arxiv-cs-ai 及
        specialized_tags.paper 文章归纳。

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

    # 项目洞察候选文章提取 + 跨天去重
    github_articles = _extract_github_articles(articles)
    yesterday_github_keys = _load_yesterday_github_keys(target_date)
    deduped_github = _dedup_github_articles(github_articles, yesterday_github_keys)
    logger.info(
        "项目洞察去重 — 原始: %d, 昨日已展示: %d, 剩余: %d",
        len(github_articles),
        len(yesterday_github_keys),
        len(deduped_github),
    )

    # 产品洞察候选文章提取 + 跨天去重
    product_articles = _extract_product_articles(articles)
    yesterday_product_keys = _load_yesterday_product_keys(target_date)
    deduped_product = _dedup_product_articles(product_articles, yesterday_product_keys)
    logger.info(
        "产品洞察去重 — 原始: %d, 昨日已展示: %d, 剩余: %d",
        len(product_articles),
        len(yesterday_product_keys),
        len(deduped_product),
    )

    logger.info(
        "构建 prompt — 总文章: %d, 项目: %d, 产品: %d, 详细展示: %d, target_date=%s",
        len(articles),
        len(deduped_github),
        len(deduped_product),
        max_detail,
        target_date,
    )
    user_prompt = build_user_prompt(
        articles,
        max_detail=max_detail,
        target_date=target_date,
        github_articles=deduped_github,
        product_articles=deduped_product,
    )
    return EDITOR_IN_CHIEF_SYSTEM_PROMPT, user_prompt


async def run_editor_in_chief(
    all_articles_path: Path,
    *,
    model: Optional[str] = None,
    max_detail: int = DEFAULT_MAX_DETAIL,
    max_tokens: Optional[int] = None,
    target_date: Optional[str] = None,
) -> dict:
    """
    执行 Editor-in-Chief 合成。

    流程：
        1. 读取 all_articles.json 并构造 prompts（含专题洞察预处理）
        2. 调用 Claude Opus Agent（带重试）
        3. 从响应中解析 JSON
        4. 校验 JSON 结构完整性
        5. 为中英文混排文本应用 CJK-Latin 间距规范化
        6. 为 Top 事件和专题洞察条目补齐 evidenceSources / sources（确定性解析）
        7. 若指定 target_date，覆盖报告日期字段
        8. 返回日报 dict

    参数：
        all_articles_path: all_articles.json 文件路径
        model: LLM 模型名称（默认从 config.yaml / ANTHROPIC_MODEL 环境变量读取）
        max_detail: user prompt 中完整展示的文章数
        max_tokens: Agent 输出 token 上限。None 时从 config.yaml llm.models.synthesize.max_tokens
            解析（兜底 DEFAULT_MAX_TOKENS），再经 CLAUDE_CODE_MAX_OUTPUT_TOKENS 透传给 CLI
        target_date: 目标报告日期（YYYY-MM-DD），None 时由 LLM 自主决定

    返回：
        日报 dict（符合 dailyReportSchema 结构，含 specializedBrief）
    """
    model = model or _resolve_default_synthesis_model()

    # 解析输出 token 上限：显式传参 > config.yaml llm.models.synthesize.max_tokens > 兜底。
    # 此前该值从未透传到 LLM 调用（死代码），大日报会被 CLI 默认输出上限截断
    if max_tokens is None:
        max_tokens = get_llm_config("synthesize").get("max_tokens") or DEFAULT_MAX_TOKENS

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
        max_tokens=max_tokens,
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
    _enrich_specialized_sources(report)

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
    max_tokens: Optional[int] = None,
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
