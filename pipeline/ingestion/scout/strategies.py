"""
pipeline/ingestion/scout/strategies.py — 抓取策略实现

本模块实现四种数据源抓取策略，由 orchestrator.run_scout() 根据 source.fetch_strategy
分发调用。各策略独立实现，不感知编排逻辑和输出格式。

策略类型：
    - rss:     Feed 订阅解析，通过 fetch_rss_items() 获取标题和链接
    - api:     JSON API 调用，包含 Hacker News Algolia 专用处理器
    - scrape:  服务端 HTTP 抓取，通过 SCRAPE_PARSERS 注册表分发到具体解析器
    - browser: Playwright 浏览器渲染，通过 BROWSER_PARSERS 注册表分发到具体解析器

添加新的抓取策略时，只需在本模块新增 `_scout_xxx()` 函数，然后在
orchestrator.run_scout() 的 dispatch 分支中增加对应 case。
"""

import json
from typing import Any, Dict, List

from pipeline.core.web_utils import fetch_rss_items, fetch_url
from pipeline.ingestion.parsers import SCRAPE_PARSERS, BROWSER_PARSERS


def _ensure_browser_session():
    """
    延迟加载 BrowserSession，避免未安装 playwright 时阻塞模块导入。

    返回：
        BrowserSession 上下文管理器实例
    """
    from pipeline.core.browser_utils import BrowserSession
    return BrowserSession()


# ---------------------------------------------------------------------------
# RSS 策略
# ---------------------------------------------------------------------------

def _scout_rss(source: dict) -> List[dict]:
    """
    RSS 源抓取：调用 fetch_rss_items() 解析 feed，提取标题、链接、发布时间等基础字段。

    参数：
        source: 数据源配置字典，需包含 url 字段

    返回：
        List[dict]: 文章基础信息列表，每篇包含 url/title/published/summary/author
    """
    url = source.get("url", "")
    if not url:
        print(f"         RSS 源缺少 url 配置")
        return []

    raw_items = fetch_rss_items(url)
    articles: List[dict] = []
    for item in raw_items:
        if not item.get("url") or not item.get("title"):
            continue
        articles.append({
            "url": item["url"],
            "title": item["title"],
            "published": item.get("published", ""),
            "summary": item.get("summary", ""),
            "author": item.get("author", ""),
        })
    return articles


# ---------------------------------------------------------------------------
# API 策略
# ---------------------------------------------------------------------------

def _scout_api(source: dict) -> List[dict]:
    """
    API 源抓取：GET JSON 接口，按 source 配置解析数据路径。

    支持的数据格式：
        - 列表格式：顶层为 JSON 数组
        - 对象格式：从 data.items / data.results 字段提取数组
        - Hacker News Algolia API：自动识别并走专用处理器

    参数：
        source: 数据源配置字典，需包含 url 字段

    返回：
        List[dict]: 文章基础信息列表
    """
    url = source.get("url", "")
    if not url:
        return []

    if "hn.algolia.com" in url:
        return _scout_hackernews(url, source)
    else:
        html = fetch_url(url)
        if not html:
            return []
        try:
            data = json.loads(html)
        except json.JSONDecodeError:
            return []

        articles: List[dict] = []
        items = data if isinstance(data, list) else data.get("items", data.get("results", []))
        for item in items:
            article_url = item.get("url") or item.get("link") or item.get("href", "")
            title = item.get("title") or item.get("name", "")
            if article_url and title:
                articles.append({
                    "url": article_url,
                    "title": title,
                    "published": item.get("published", item.get("date", item.get("created_at", ""))),
                    "summary": item.get("summary", item.get("description", "")),
                    "author": item.get("author", item.get("by", "")),
                })
        return articles


def _scout_hackernews(api_url: str, source: dict) -> List[dict]:
    """
    Hacker News Algolia API 专用抓取。

    从 search API 获取 hits，按 score_threshold（默认 100）过滤，
    保留分数字段以便后续排序。

    参数：
        api_url:  Algolia search API 完整 URL（含查询参数）
        source:   数据源配置字典，用于读取 filter.score_threshold

    返回：
        List[dict]: 过滤后的 HN 文章列表，每篇额外包含 score 字段
    """
    min_score = source.get("filter", {}).get("score_threshold", 100)
    html = fetch_url(api_url)
    if not html:
        return []

    try:
        data = json.loads(html)
    except json.JSONDecodeError:
        return []

    hits = data.get("hits", [])
    articles: List[dict] = []
    for h in hits:
        score = h.get("points", 0)
        if score < min_score:
            continue
        article_url = h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}"
        articles.append({
            "url": article_url,
            "title": h.get("title", ""),
            "published": h.get("created_at", ""),
            "summary": f"Points: {score}, Comments: {h.get('num_comments', 0)}",
            "author": h.get("author", ""),
            "score": score,
        })
    return articles


# ---------------------------------------------------------------------------
# Scrape 策略
# ---------------------------------------------------------------------------

def _scout_scrape(source: dict) -> List[dict]:
    """
    HTML 页面抓取：按源 name 从 SCRAPE_PARSERS 注册表中查找对应解析器。

    解析器接收 source 配置字典，负责 HTTP 请求和 HTML 解析，
    并返回文章链接列表。

    参数：
        source: 数据源配置字典

    返回：
        List[dict]: 解析器返回的文章列表
    """
    name = source.get("name", "")
    parser = SCRAPE_PARSERS.get(name)
    if parser is None:
        print(f"         scrape 策略暂未为此源实现解析器: {name}")
        return []
    return parser(source)


# ---------------------------------------------------------------------------
# Browser 策略
# ---------------------------------------------------------------------------

def _scout_browser(source: dict, browser_session) -> List[dict]:
    """
    浏览器抓取：按源 name 从 BROWSER_PARSERS 注册表中查找对应解析器。

    解析器接收 Playwright 已渲染页面（browser_session），负责从 DOM 提取
    文章链接列表。browser_session 由 orchestrator 预先创建并在所有源之间复用。

    参数：
        source:          数据源配置字典
        browser_session: Playwright BrowserSession 上下文管理器实例

    返回：
        List[dict]: 解析器返回的文章列表
    """
    name = source.get("name", "")
    parser = BROWSER_PARSERS.get(name)
    if parser is None:
        print(f"         browser 策略暂未为此源实现解析器: {name}")
        return []
    return parser(source, browser_session)
