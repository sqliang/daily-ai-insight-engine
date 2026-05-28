"""
网络请求工具

封装 curl 子进程调用、RSS 解析和正文抽取。
所有请求自动继承 os.environ 中的代理设置 (由 proxy_utils.setup_proxy() 注入)。
RSS 使用 feedparser, 正文抽取使用 trafilatura。
"""

import logging
import re
import subprocess
from datetime import datetime, timezone
from typing import List, Optional

import feedparser

logger = logging.getLogger(__name__)


def fetch_url(url: str, timeout: int = 30) -> Optional[str]:
    """
    通过 curl 获取 URL 的原始响应文本。
    自动继承进程环境变量中的代理配置。
    返回响应 body 字符串，失败时返回 None。
    """
    try:
        result = subprocess.run(
            [
                "curl", "-s", "-L",              # -s: 静默, -L: 跟随重定向
                "--max-time", str(timeout),
                "-H", "User-Agent: DailyAIInsightEngine/1.0",
                url,
            ],
            capture_output=True, text=True,
            timeout=timeout + 5,
        )
        if result.returncode != 0:
            logger.warning("curl 返回非零状态码 url=%s code=%d stderr=%s", url, result.returncode, result.stderr.strip()[:200])
            return None
        return result.stdout
    except subprocess.TimeoutExpired:
        logger.warning("curl 请求超时 url=%s timeout=%d", url, timeout)
        return None
    except Exception as e:
        logger.warning("curl 请求异常 url=%s: %s", url, e)
        return None


def fetch_rss_items(feed_url: str, timeout: int = 30) -> List[dict]:
    """
    解析 RSS/Atom feed，返回条目列表。
    每个条目包含: url, title, published, summary, author 等字段。
    """
    try:
        feed = feedparser.parse(feed_url)
    except Exception as e:
        logger.warning("RSS 解析异常 url=%s: %s", feed_url, e)
        return []

    # feedparser 不抛网络异常，而是设 bozo 标记，静默返回空 entries
    if feed.bozo and len(feed.entries) == 0:
        logger.warning("RSS 抓取可能失败（网络/代理问题） url=%s bozo=%s", feed_url, getattr(feed, 'bozo_exception', 'unknown'))
    elif feed.bozo:
        logger.debug("RSS feed 有格式瑕疵但不影响解析 url=%s bozo=%s", feed_url, getattr(feed, 'bozo_exception', 'unknown'))

    items = []
    for entry in feed.entries:
        # 发布日期解析
        published_str = ""
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            try:
                dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
                published_str = dt.strftime("%Y-%m-%d")
            except Exception:
                published_str = entry.get("published", "")
        elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
            try:
                dt = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
                published_str = dt.strftime("%Y-%m-%d")
            except Exception:
                published_str = ""
        else:
            published_str = entry.get("published", "") or entry.get("updated", "")

        # 作者
        author = ""
        if hasattr(entry, "author_detail") and entry.author_detail:
            author = entry.author_detail.get("name", "")
        if not author:
            author = entry.get("author", "")

        items.append({
            "url": entry.get("link", ""),
            "title": _clean_text(entry.get("title", "")),
            "published": published_str,
            "summary": _clean_text(entry.get("summary", entry.get("description", ""))),
            "author": author,
        })

    return items


def extract_article_content(html: str, url: str = "") -> Optional[str]:
    """
    使用 trafilatura 从 HTML 中提取干净正文 (Markdown 格式)。
    返回提取的 Markdown 文本，失败时返回 None。
    """
    try:
        import trafilatura
        result = trafilatura.extract(
            html,
            url=url,
            output_format="markdown",
            favor_precision=True,       # 优先准确度 (宁可少取也不要广告/侧边栏)
            include_comments=False,
        )
        return result.strip() if result else None
    except Exception:
        return None


def extract_metadata(html: str, url: str = "") -> dict:
    """
    使用 trafilatura 从 HTML 中提取元数据 (标题、日期、作者等)。
    """
    try:
        import trafilatura
        metadata = trafilatura.extract_metadata(html, url=url)
        if metadata is None:
            return {}
        return {
            "title": _clean_text(metadata.title or ""),
            "author": _clean_text(metadata.author or ""),
            "date": _clean_text(metadata.date or ""),
            "description": _clean_text(metadata.description or ""),
        }
    except Exception:
        return {}


def fetch_and_extract(url: str, timeout: int = 30) -> Optional[dict]:
    """
    一站式操作: 获取 URL → 提取正文 + 元数据。
    返回 {"title", "author", "published", "description", "content"} 或 None。
    """
    html = fetch_url(url, timeout=timeout)
    if not html:
        return None

    meta = extract_metadata(html, url)
    content = extract_article_content(html, url)
    if not content:
        return None

    return {
        "title": meta.get("title", ""),
        "author": meta.get("author", ""),
        "published": meta.get("date", ""),
        "description": meta.get("description", ""),
        "content": content,
    }


# ============================================================
# 内部工具函数
# ============================================================

def _clean_text(text: str, max_length: Optional[int] = None) -> str:
    """清洗文本：去除 HTML 标签、多余空白，可选截断。"""
    if not text:
        return ""

    # 去除 HTML 标签
    text = re.sub(r"<[^>]+>", "", text)
    # 解码常见 HTML 实体
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'").replace("&apos;", "'")
    # 合并空白
    text = re.sub(r"\s+", " ", text).strip()

    if max_length and len(text) > max_length:
        text = text[:max_length] + "..."

    return text
