"""
文章过滤器

提供关键字匹配、时效性过滤、数量裁剪等通用过滤逻辑，
可被 ingestion 及其他 pipeline 阶段复用。

设计理由：
    短关键字（<=3 字符）如 "RAG"、"AI"、"GPT" 使用 \b 词边界匹配，
    避免子串误命中（如 "RAG" 命中 "storage", "average"）。
    长关键字保持子串匹配，因为学术术语变体多（如 "fine-tuning" vs "fine-tuned"）。
"""

import re
from datetime import datetime, timedelta, timezone
from typing import List, Optional


def apply_filters(articles: List[dict], source: dict) -> List[dict]:
    """按源配置的过滤规则依次筛选文章。"""
    cfg = source.get("filter", {})
    articles = filter_by_keywords(articles, cfg.get("keywords", []))
    articles = filter_by_age(articles, cfg.get("max_age_hours", 48))
    articles = filter_by_limit(articles, source.get("limit", 0))
    return articles


def _match_keyword(text: str, keyword: str) -> bool:
    """
    关键词匹配：短关键词用 ASCII 字母边界，长关键词用子串匹配。

    设计理由：
        Python 的 \b 将 CJK 字符视为 \w，导致 "\bAI\b" 在 "AI正在" 中不匹配。
        改用 (?<![a-zA-Z0-9]) / (?![a-zA-Z0-9]) 实现 ASCII 字母边界，
        既能在纯英文中避免 "RAG" 匹配 "storage"，也能在中英文混排中正确匹配 "AI技术"。
        长关键词（如 "fine-tuning"）本身独特，无需边界限制且支持变体匹配。
    """
    if len(keyword) <= 3:
        return bool(re.search(
            r'(?<![a-zA-Z0-9])' + re.escape(keyword) + r'(?![a-zA-Z0-9])', text
        ))
    return keyword in text


def filter_by_keywords(articles: List[dict], keywords: List[str]) -> List[dict]:
    """
    关键词过滤：标题或摘要包含任一关键词即保留。

    短关键字（<=3 字符）采用词边界匹配，避免子串误命中；
    长关键字采用子串匹配，支持术语变体。
    关键词列表为空时跳过此过滤器 (全量保留)。
    """
    if not keywords:
        return articles
    result = []
    for a in articles:
        text = (a.get("title", "") + " " + a.get("summary", "")).lower()
        if any(_match_keyword(text, kw.lower()) for kw in keywords):
            result.append(a)
    return result


def filter_by_age(articles: List[dict], max_age_hours: int) -> List[dict]:
    """
    时效性过滤：只保留过去 N 小时内的文章。
    无法解析日期的不做过滤 (保守保留)。
    """
    if max_age_hours <= 0:
        return articles
    cutoff = datetime.now(timezone.utc) - timedelta(hours=max_age_hours)
    result = []
    for a in articles:
        pub = a.get("published", "")
        dt = parse_datetime(pub)
        if dt is None:
            result.append(a)
            continue
        # 用日期比较而非 datetime 比较，避免因 fetch_rss_items 输出的
        # YYYY-MM-DD 格式（无时分秒）与 cutoff 的时分秒不对齐导致的误过滤。
        # 例如 pub=2026-06-11, cutoff=2026-06-11T09:30:00 —
        # datetime 比较下 06-11 00:00 < 06-11 09:30 会错误过滤同一天的文章。
        if dt.date() >= cutoff.date():
            result.append(a)
    return result


def filter_by_limit(articles: List[dict], limit: int) -> List[dict]:
    """数量裁剪：保留前 N 条。limit=0 表示不限制。"""
    if limit > 0 and len(articles) > limit:
        return articles[:limit]
    return articles


def parse_datetime(s: str) -> Optional[datetime]:
    """尝试多种常见格式解析日期时间字符串。"""
    if not s:
        return None
    for fmt in [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
    ]:
        try:
            dt = datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None
