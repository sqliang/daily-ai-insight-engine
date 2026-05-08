"""
Step 1: URL 清单生成器 (Scout)

读取 pipeline/config.yaml → 遍历启用的数据源 → 抓取 RSS/API 获取文章列表 →
生成 JSON 清单文件到 data/00_manifest/{source_name}_{YYYYMMDD}.json。

清单文件是轻量级的"待办任务列表"，供 ingest.py 消费，也支持断点续传：
如果某天的清单已存在，默认跳过该源 (除非指定 --force)。
"""

import argparse
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# 确保项目根目录在 sys.path 中，支持从任意目录运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import re
import xml.etree.ElementTree as ET

from pipeline.core.config_loader import get_sources
from pipeline.core.file_utils import ensure_dir, get_project_root, resolve_data_dir
from pipeline.core.id_utils import generate_id
from pipeline.core.web_utils import fetch_rss_items, fetch_url


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
        articles = _apply_filters(articles, source)
        print(f"         获取 {len(articles)} 篇 (过滤后)")

        # 为每篇文章生成唯一 ID（基于 source URL 的 SHA-256 哈希），
        # 这是文章进入流水线后获得的第一个身份标识，用于后续所有阶段的去重和关联
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
        from pipeline.core.file_utils import write_json
        write_json(manifest_path, manifest_data)

        all_manifests[name] = articles

    return all_manifests


# ================================================================
# 抓取策略实现
# ================================================================

def _scout_rss(source: dict) -> List[dict]:
    """
    RSS 源抓取：调用 fetch_rss_items() 解析 feed，返回文章列表。
    """
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
        # 通用 API 抓取
        html = fetch_url(url)
        if not html:
            return []
        import json
        try:
            data = json.loads(html)
        except json.JSONDecodeError:
            return []

        # 尝试按常见路径提取文章列表
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
    """
    Hacker News Algolia API 专用抓取。
    API 返回的 hits 数组中每项的格式: {title, url, points, created_at, author, ...}
    """
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
    HTML 页面抓取：按源 name 分发到专用解析器。
    专用解析器负责从 HTML 中提取文章链接列表。
    """
    name = source.get("name", "")
    if name == "tldrai":
        return _scrape_tldrai(source)
    elif name == "anthropic-blog":
        return _scrape_anthropic(source)
    elif name == "machine-heart":
        return _scrape_machine_heart(source)
    else:
        print(f"         scrape 策略暂未为此源实现专用解析器: {name}")
        return []


# ================================================================
# 专用 HTML 解析器
# ================================================================

def _scrape_tldrai(source: dict) -> List[dict]:
    """
    TLDR AI 页面解析器。

    参考 knowledge-scout/src/parsers/tldrai.py 实现。
    TLDR AI 提供 /api/latest/ai 端点，返回最新一期新闻通讯的 HTML。
    从 "Headlines & Launches" 和 "Engineering & Research" 两个板块抓取。
    """
    url = source.get("url", "https://tldr.tech/api/latest/ai")
    html = fetch_url(url)
    if not html:
        return []

    results = []

    # 板块 1: Headlines & Launches (前 5 条)
    headlines_section = _extract_section(
        html, r'Headlines &amp; Launches</h3></header>(.*?)</section>'
    )
    if headlines_section:
        pattern = r'<a class="font-bold" href="([^"]+)"[^>]*><h3>([^<]+)</h3></a>'
        for article_url, title in re.findall(pattern, headlines_section)[:5]:
            results.append({
                "url": article_url,
                "title": _clean_html_text(title),
                "summary": "TLDR AI 每日头条",
            })

    # 板块 2: Engineering & Research (前 3 条)
    research_section = _extract_section(
        html, r'Engineering &amp; Research</h3></header>(.*?)</section>'
    )
    if research_section:
        pattern = r'<a class="font-bold" href="([^"]+)"[^>]*><h3>([^<]+)</h3></a>'
        for article_url, title in re.findall(pattern, research_section)[:3]:
            results.append({
                "url": article_url,
                "title": _clean_html_text(title),
                "summary": "AI 工程与研究",
            })

    # 降级: 如果板块提取失败, 直接匹配所有文章链接
    if not results:
        pattern = (
            r'<a class="font-bold" href="([^"]+?)"'
            r'[^>]*?target="_blank"[^>]*?>'
            r'<h3>([^<]+)</h3></a>'
        )
        for article_url, title in re.findall(pattern, html)[:10]:
            # 过滤广告和赞助内容
            if "utm_source=tldr" in article_url or "Sponsor" in title:
                continue
            results.append({
                "url": article_url,
                "title": _clean_html_text(title),
                "summary": "TLDR AI 文章",
            })

    return results


def _scrape_anthropic(source: dict) -> List[dict]:
    """
    Anthropic 新闻页面解析器。

    Anthropic 官网无 RSS feed，通过解析 sitemap.xml 获取全部页面 URL，
    筛选 /news/ 路径的文章，按 lastmod 日期排序取最新。
    标题从 URL slug 推导 (e.g. claude-opus-4-7 -> Claude Opus 4.7)。
    """
    url = source.get("url", "https://www.anthropic.com/sitemap.xml")
    html = fetch_url(url)
    if not html:
        return []

    try:
        # 移除命名空间前缀, 简化解析
        clean_xml = re.sub(r' xmlns="[^"]+"', "", html)
        root = ET.fromstring(clean_xml)
    except ET.ParseError:
        print("         sitemap XML 解析失败")
        return []

    articles = []

    for url_elem in root.findall("url"):
        loc = url_elem.find("loc")
        lastmod = url_elem.find("lastmod")
        if loc is None:
            continue

        href = loc.text or ""
        # 只取 /news/ 路径的文章
        if "/news/" not in href:
            continue

        date_str = lastmod.text if lastmod is not None and lastmod.text else ""
        # 从 URL slug 推导可读标题
        slug = href.rstrip("/").split("/")[-1]
        title = _slug_to_title(slug)

        articles.append({
            "url": href,
            "title": title,
            "published": date_str[:10] if date_str else "",
            "summary": "",
        })

    # 按 published 降序排列
    articles.sort(key=lambda a: a.get("published", ""), reverse=True)
    return articles


def _scrape_machine_heart(source: dict) -> List[dict]:
    """
    机器之心页面解析器。

    机器之心官网无 RSS，通过解析首页 HTML 提取文章链接。
    """
    url = source.get("url", "https://www.jiqizhixin.com/")
    html = fetch_url(url)
    if not html:
        return []

    # 匹配文章链接: /articles/YYYY-MM-DD-xxx
    pattern = r'<a[^>]*href="(/articles/\d{4}-\d{2}-\d{2}-\d+)"[^>]*>([^<]+)</a>'
    matches = re.findall(pattern, html)
    seen = set()
    articles = []
    for path, title in matches:
        if path in seen:
            continue
        seen.add(path)
        article_url = f"https://www.jiqizhixin.com{path}"
        articles.append({
            "url": article_url,
            "title": _clean_html_text(title),
            "published": _extract_date_from_path(path),
            "summary": "",
        })
    return articles


# ================================================================
# HTML 解析辅助函数
# ================================================================

def _extract_section(html: str, pattern: str) -> str:
    """从 HTML 中用正则提取一个板块内容。"""
    m = re.search(pattern, html, re.DOTALL)
    return m.group(1) if m else ""


def _clean_html_text(text: str) -> str:
    """清理 HTML 实体和多余空白。"""
    if not text:
        return ""
    text = text.replace("&amp;", "&").replace("&#x27;", "'")
    text = text.replace("&quot;", '"').replace("&lt;", "<").replace("&gt;", ">")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _slug_to_title(slug: str) -> str:
    """将 URL slug 转换为可读标题 (e.g. claude-opus-4-7 -> Claude Opus 4.7)。"""
    # 常见缩写保持大写
    preserve_case = {"ai", "api", "sdk", "gpu", "cpu", "llm", "rlhf", "uk", "us", "eu"}
    words = []
    for w in slug.split("-"):
        if w.lower() in preserve_case:
            words.append(w.upper() if w.islower() and len(w) <= 4 else w)
        elif w.isdigit():
            words.append(w)
        else:
            words.append(w.capitalize())
    return " ".join(words)


def _extract_date_from_path(path: str) -> str:
    """从 /articles/YYYY-MM-DD-xxx 路径中提取日期。"""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", path)
    return m.group(1) if m else ""


# ================================================================
# 过滤器
# ================================================================

def _apply_filters(articles: List[dict], source: dict) -> List[dict]:
    """按源配置的过滤规则筛选文章。"""
    cfg = source.get("filter", {})
    articles = _filter_by_keywords(articles, cfg.get("keywords", []))
    articles = _filter_by_age(articles, cfg.get("max_age_hours", 48))
    articles = _filter_by_limit(articles, source.get("limit", 0))
    return articles


def _filter_by_keywords(articles: List[dict], keywords: List[str]) -> List[dict]:
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


def _filter_by_age(articles: List[dict], max_age_hours: int) -> List[dict]:
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
        dt = _parse_datetime(pub)
        if dt is None or dt >= cutoff:
            result.append(a)
    return result


def _filter_by_limit(articles: List[dict], limit: int) -> List[dict]:
    """数量裁剪：保留前 N 条。limit=0 表示不限制。"""
    if limit > 0 and len(articles) > limit:
        return articles[:limit]
    return articles


# ================================================================
# 辅助函数
# ================================================================

def _parse_datetime(s: str) -> Optional[datetime]:
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
