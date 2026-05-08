"""
文章过滤器

提供关键字匹配、时效性过滤、数量裁剪等通用过滤逻辑，
可被 ingestion 及其他 pipeline 阶段复用。
"""

from datetime import datetime, timedelta, timezone
from typing import List, Optional


def apply_filters(articles: List[dict], source: dict) -> List[dict]:
    """按源配置的过滤规则依次筛选文章。"""
    cfg = source.get("filter", {})
    articles = filter_by_keywords(articles, cfg.get("keywords", []))
    articles = filter_by_age(articles, cfg.get("max_age_hours", 48))
    articles = filter_by_limit(articles, source.get("limit", 0))
    return articles


def filter_by_keywords(articles: List[dict], keywords: List[str]) -> List[dict]:
    """
    关键词过滤：标题或摘要包含任一关键词即保留。
    关键词列表为空时跳过此过滤器 (全量保留)。
    """
    if not keywords:
        return articles
    result = []
    for a in articles:
        text = (a.get("title", "") + " " + a.get("summary", "")).lower()
        if any(kw.lower() in text for kw in keywords):
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
        if dt is None or dt >= cutoff:
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
