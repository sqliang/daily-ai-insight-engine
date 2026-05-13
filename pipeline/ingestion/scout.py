"""
Step 1: URL 清单生成器 (Scout)

读取 pipeline/config.yaml → 遍历启用的数据源 → 抓取 RSS/API 获取文章列表 →
生成 JSON 清单文件到 data/00_manifest/{source_name}_{YYYYMMDD}.json。

清单文件是轻量级的"待办任务列表"，供 ingest.py 消费，也支持断点续传：
如果某天的清单已存在，默认跳过该源 (除非指定 --force)。
"""

import argparse
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# 确保项目根目录在 sys.path 中，支持从任意目录运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pipeline.core.config_loader import get_sources
from pipeline.core.file_utils import resolve_data_dir, write_json, read_json, atomic_write, list_files
from pipeline.core.id_utils import generate_id
from pipeline.core.web_utils import fetch_rss_items, fetch_url

from pipeline.ingestion.filters import apply_filters
from pipeline.ingestion.parsers import SCRAPE_PARSERS, BROWSER_PARSERS

SOURCE_TYPE_LABEL: Dict[str, str] = {
    "academic_paper": "学术论文",
    "tech_blog": "技术博客",
    "news_media": "科技媒体",
    "community_discussion": "社区讨论",
}


def _ensure_browser_session():
    """延迟加载 BrowserSession，避免未安装 playwright 时阻塞模块导入。"""
    from pipeline.core.browser_utils import BrowserSession
    return BrowserSession()


# ================================================================
# 主编排器
# ================================================================

def run_scout(force: bool = False) -> Dict[str, List[dict]]:
    """
    主入口：遍历所有启用的源，生成清单文件。
    返回 {source_name: [articles]} 字典。
    force=True 时忽略已存在的清单，强制重新获取。
    """
    sources = get_sources(enabled_only=True)
    today_str = date.today().isoformat()
    manifest_dir = resolve_data_dir("manifest")
    all_manifests: Dict[str, List[dict]] = {}

    # 检测是否有 browser 策略的源，提前创建 browser session (复用 Chromium 实例)
    needs_browser = any(s.get("fetch_strategy") == "browser" for s in sources)
    browser_session = None
    if needs_browser:
        browser_session = _ensure_browser_session().__enter__()

    try:
        for source in sources:
            name = source.get("name", "")
            strategy = source.get("fetch_strategy", "rss")

            # 检查是否已有今日清单
            manifest_path = manifest_dir / f"{name}_{today_str}.json"
            if manifest_path.exists() and not force:
                print(f"  [跳过] {name} — 今日清单已存在: {manifest_path.name}")
                continue

            # 根据抓取策略分发
            print(f"  [抓取] {name} (strategy={strategy})...")
            articles: List[dict] = []

            try:
                if strategy == "rss":
                    articles = _scout_rss(source)
                elif strategy == "api":
                    articles = _scout_api(source)
                elif strategy == "scrape":
                    articles = _scout_scrape(source)
                elif strategy == "browser":
                    articles = _scout_browser(source, browser_session)
                else:
                    print(f"         未知抓取策略: {strategy}，跳过")
                    continue
            except Exception as e:
                print(f"         ❌ 抓取失败: {e}")
                continue

            if not articles:
                print(f"         无新文章")
                continue

            # 应用过滤规则
            articles = apply_filters(articles, source)
            print(f"         获取 {len(articles)} 篇 (过滤后)")

            # 为每篇文章生成唯一 ID
            for article in articles:
                article["id"] = generate_id(article.get("url", ""))

            # 写入清单文件
            manifest_data = {
                "source": name,
                "source_type": source.get("type", ""),
                "tier": source.get("tier", ""),
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "date": today_str,
                "articles": articles,
            }
            write_json(manifest_path, manifest_data)

            all_manifests[name] = articles

        # 生成汇总 Markdown 清单
        _generate_markdown_manifest(all_manifests, manifest_dir, today_str, sources)

    finally:
        if browser_session:
            browser_session.__exit__(None, None, None)

    return all_manifests


# ================================================================
# 抓取策略实现
# ================================================================

def _scout_rss(source: dict) -> List[dict]:
    """RSS 源抓取：调用 fetch_rss_items() 解析 feed。"""
    url = source.get("url", "")
    if not url:
        print(f"         RSS 源缺少 url 配置")
        return []

    raw_items = fetch_rss_items(url)
    articles = []
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


def _scout_api(source: dict) -> List[dict]:
    """
    API 源抓取：GET JSON 接口，按 source 配置解析数据路径。
    目前支持 Hacker News Algolia API。
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
        import json
        try:
            data = json.loads(html)
        except json.JSONDecodeError:
            return []

        articles = []
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
    """Hacker News Algolia API 专用抓取。"""
    min_score = source.get("filter", {}).get("score_threshold", 100)
    html = fetch_url(api_url)
    if not html:
        return []

    import json
    try:
        data = json.loads(html)
    except json.JSONDecodeError:
        return []

    hits = data.get("hits", [])
    articles = []
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


def _scout_scrape(source: dict) -> List[dict]:
    """
    HTML 页面抓取：按源 name 从解析器注册表中查找对应解析器。
    解析器负责从 HTML 中提取文章链接列表。
    """
    name = source.get("name", "")
    parser = SCRAPE_PARSERS.get(name)
    if parser is None:
        print(f"         scrape 策略暂未为此源实现解析器: {name}")
        return []
    return parser(source)


def _scout_browser(source: dict, browser_session) -> List[dict]:
    """
    浏览器抓取：按源 name 从解析器注册表中查找对应解析器。
    解析器接收 Playwright 已渲染页面，负责从 DOM 提取文章链接列表。
    """
    name = source.get("name", "")
    parser = BROWSER_PARSERS.get(name)
    if parser is None:
        print(f"         browser 策略暂未为此源实现解析器: {name}")
        return []
    return parser(source, browser_session)


# ================================================================
# Markdown 汇总清单生成
# ================================================================

def _generate_markdown_manifest(
    all_manifests: Dict[str, List[dict]],
    manifest_dir: Path,
    today_str: str,
    sources: List[dict],
) -> None:
    """
    生成汇总 Markdown 文件到 data/00_manifest/。
    合并刚抓取的文章 + 从已存在的 JSON 清单中读取被跳过的源。
    """
    merged: Dict[str, dict] = {}

    for source in sources:
        name = source.get("name", "")
        if name in all_manifests and all_manifests[name]:
            # 本次 run 新抓取的
            merged[name] = {
                "articles": all_manifests[name],
                "source_type": source.get("type", ""),
                "tier": source.get("tier", ""),
                "language": source.get("language", "en"),
            }
        else:
            # 源被跳过 — 尝试从已有 JSON 清单读回
            manifest_path = manifest_dir / f"{name}_{today_str}.json"
            data = read_json(manifest_path)
            if data and data.get("articles"):
                merged[name] = {
                    "articles": data["articles"],
                    "source_type": data.get("source_type", source.get("type", "")),
                    "tier": data.get("tier", source.get("tier", "")),
                    "language": source.get("language", "en"),
                }
            else:
                print(f"  [Markdown] ⚠ {name} — 无清单数据，跳过")

    if not merged:
        print("  [Markdown] ⚠ 没有任何源有文章数据，跳过生成")
        return

    # 按 Tier (A→B→C) 再按 name 排序
    tier_order = {"A": 0, "B": 1, "C": 2}
    sorted_names = sorted(merged.keys(), key=lambda n: (tier_order.get(merged[n]["tier"], 99), n))

    total_sources = len(sorted_names)
    total_articles = sum(len(merged[n]["articles"]) for n in sorted_names)
    iso_week = datetime.now().isocalendar()[1]
    generated_at = datetime.now(timezone.utc).isoformat()

    # Build markdown
    lines: List[str] = []
    lines.append("---")
    lines.append(f'date: "{today_str}"')
    lines.append(f"week: {iso_week}")
    lines.append(f"total_sources: {total_sources}")
    lines.append(f"total_articles: {total_articles}")
    lines.append(f'generated_at: "{generated_at}"')
    lines.append("---")
    lines.append("")
    lines.append("# Daily AI Insight — 数据源清单")
    lines.append("")
    lines.append(
        f"**日期**: {today_str} | **第 {iso_week} 周** | "
        f"**{total_sources}** 个源, **{total_articles}** 篇文章"
    )
    lines.append("")

    for name in sorted_names:
        info = merged[name]
        articles: list = info["articles"]
        src_type = info["source_type"]
        tier = info["tier"]
        lang = info["language"]
        src_type_cn = SOURCE_TYPE_LABEL.get(src_type, src_type)
        lang_display = "中文" if lang == "zh" else "EN"
        count = len(articles)

        lines.append("---")
        lines.append("")
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"> Tier {tier} · {src_type_cn} · {lang_display} · {count} 篇")
        lines.append("")

        for article in articles:
            title = article.get("title", "无标题").strip() or "无标题"
            url = article.get("url", "")
            published = article.get("published", "")
            author = article.get("author", "")
            summary = article.get("summary", "").strip()

            # 文章标题行 (带链接)
            if url:
                lines.append(f"- **[{title}]({url})**")
            else:
                lines.append(f"- **{title}**")

            # 元信息行
            meta_parts: List[str] = []
            if published:
                meta_parts.append(f"发布: {published}")
            if author:
                meta_parts.append(f"作者: {author}")
            if meta_parts:
                lines.append(f"  - {' | '.join(meta_parts)}")

            # 摘要行
            if summary:
                lines.append(f"  - 摘要: {summary}")
            lines.append("")

    md_content = "\n".join(lines)
    filename = f"{today_str}-manifest-第{iso_week}周.md"
    filepath = manifest_dir / filename
    atomic_write(filepath, md_content)
    print(f"  [Markdown] ✅ 已生成汇总清单: {filename}")


# ================================================================
# CLI 入口
# ================================================================

def main():
    parser = argparse.ArgumentParser(description="Stage 1 Scout: 生成 URL 清单")
    parser.add_argument("--force", action="store_true", help="强制重新获取所有源")
    args = parser.parse_args()

    print("=== Stage 1 Scout: URL 清单生成 ===\n")
    manifests = run_scout(force=args.force)

    total = sum(len(v) for v in manifests.values())
    print(f"\n总计: {len(manifests)} 个源, {total} 篇文章")


if __name__ == "__main__":
    main()
