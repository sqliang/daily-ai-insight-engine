"""
GitHub Trending 双源容错解析器

github-trending 原主源为第三方 RSS 镜像（GitHubTrendingRSS 项目），该镜像不定期
rebuild（隔 1~3 天），停更日会返回空列表或与上日完全重复的榜单。由于 article_id 是
仓库 URL 的 SHA-256，重复榜单在 ingest 阶段被全部去重，导致停更日 github-trending
贡献 0 篇文章、热门仓库归属日期错乱（见 2026-08-27 / 08-28 事故复盘）。

本解析器改为双源容错：
    1. 主源：直连 https://github.com/trending（服务端渲染、实时权威，无第三方镜像延迟）
    2. 兜底：主源抓取失败时退回原 RSS 镜像
    3. 丰富：主源成功时，用 RSS 镜像的 README 摘要覆盖仓库简介，提升关键词过滤命中率

任一源失败均不影响另一源；两者都失败才返回空列表。
"""

import re
from typing import List

from pipeline.core.web_utils import fetch_rss_items, fetch_url
from pipeline.ingestion.html_utils import clean_html_text

# 原 RSS 镜像地址 — 保留作为兜底源 + 摘要丰富源（README 内容比 trending 页一行简介更利于关键词过滤）
_RSS_MIRROR_URL = "https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml"

# trending 页中非仓库的链接路径前缀（登录页、赞助位、话题聚合页等）
_NON_REPO_PREFIXES = (
    "/login",
    "/topics",
    "/collections",
    "/sponsors",
    "/features",
    "/settings",
    "/marketplace",
)


def _scrape_trending_repos() -> List[dict]:
    """
    直连 github.com/trending，解析实时热门仓库列表。

    返回：
        List[dict]: 每篇含 url/title/summary/published/author，title 为 owner/repo 格式
    """
    html = fetch_url("https://github.com/trending")
    if not html:
        return []

    # 每个热门仓库对应一个 <article class="Box-row"> 块（块内含 star 按钮、标题、简介）
    blocks = re.split(r'<article class="Box-row">', html)[1:]
    repos: List[dict] = []
    for block in blocks:
        # 仓库链接：<a ... href="/owner/repo" ...>，href 前有 data-hydro-* 属性，
        # 故不能用 <a href="..."> 直接匹配
        m = re.search(r'<a[^>]*href="(/[^/"]+/[^/"]+)"[^>]*>', block)
        if not m:
            continue
        path = m.group(1)
        if path.startswith(_NON_REPO_PREFIXES):
            continue

        # 简介：<p class="...col-9...">...</p>（仓库 About 描述）
        summary = ""
        dm = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', block, re.DOTALL)
        if dm:
            summary = clean_html_text(re.sub(r"<[^>]+>", "", dm.group(1)))

        repos.append({
            "url": "https://github.com" + path,
            "title": path.lstrip("/"),
            "summary": summary,
            "published": "",
            "author": "",
        })
    return repos


def _fetch_rss_articles() -> List[dict]:
    """
    best-effort 抓取 RSS 镜像，返回文章列表。

    镜像可能停更/失败，任何异常都降级为空列表，不影响主源抓取。
    """
    try:
        return fetch_rss_items(_RSS_MIRROR_URL)
    except Exception:
        return []


def parse_github_trending(source: dict) -> List[dict]:
    """
    双源容错抓取 github-trending 热门仓库。

    参数：
        source: 数据源配置字典（fetch_strategy 已改为 scrape，url 指向 trending 页）

    返回：
        List[dict]: 主源（trending 页）成功时返回实时榜单；失败时退回 RSS 镜像
    """
    scraped = _scrape_trending_repos()
    rss_articles = _fetch_rss_articles()

    if scraped:
        # 主源成功：用 RSS 的 README 摘要覆盖仓库简介，提升关键词过滤命中率。
        # 不引入镜像中已掉出榜单的过期仓库（它们会在 ingest 阶段被 URL 去重）。
        rss_by_url = {a["url"]: a.get("summary", "") for a in rss_articles if a.get("url")}
        for repo in scraped:
            richer = rss_by_url.get(repo["url"], "")
            if richer:
                repo["summary"] = richer
        return scraped

    # 主源失败：兜底退回 RSS 镜像（含 url/title/summary/published/author）
    return [
        {
            "url": a["url"],
            "title": a.get("title", ""),
            "summary": a.get("summary", ""),
            "published": a.get("published", ""),
            "author": a.get("author", ""),
        }
        for a in rss_articles
        if a.get("url") and a.get("title")
    ]
