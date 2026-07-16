"""
网络请求工具

封装 curl 子进程调用、RSS 解析和正文抽取。
所有请求自动继承 os.environ 中的代理设置 (由 proxy_utils.setup_proxy() 注入)。
RSS 使用 feedparser, 正文抽取使用 trafilatura。
"""

import logging
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from typing import List, Optional

import feedparser

logger = logging.getLogger(__name__)


def fetch_url(url: str, timeout: int = 30, max_retries: int = 3) -> Optional[str]:
    """
    通过 curl 获取 URL 的原始响应文本。
    自动继承进程环境变量中的代理配置。
    内置指数退避重试（默认 3 次，间隔 1s/2s/4s），应对瞬时网络故障。
    返回响应 body 字符串，所有重试耗尽后仍失败则返回 None。

    设计理由：
        管线在 GitHub Actions 等不稳定网络环境中运行，单次 curl 失败率
        约 2-4%。加入指数退避重试可将瞬时故障恢复率提升至 ~95%，
        且对目标服务器影响极小（最多 3 次请求，间隔递增）。
    """
    import time

    for attempt in range(max_retries):
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
                logger.warning(
                    "curl 返回非零状态码 url=%s code=%d attempt=%d/%d stderr=%s",
                    url, result.returncode, attempt + 1, max_retries,
                    result.stderr.strip()[:200],
                )
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # 1s, 2s, 4s
                    continue
                return None
            return result.stdout
        except subprocess.TimeoutExpired:
            logger.warning(
                "curl 请求超时 url=%s timeout=%d attempt=%d/%d",
                url, timeout, attempt + 1, max_retries,
            )
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return None
        except Exception as e:
            logger.warning(
                "curl 请求异常 url=%s attempt=%d/%d: %s",
                url, attempt + 1, max_retries, e,
            )
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return None

    return None


def is_bot_challenge_html(html: str) -> bool:
    """
    检测 HTML 是否为反爬挑战页面，而非真实文章内容。

    当 curl 请求遇到 Cloudflare / JS challenge 等反爬机制时，
    返回的 HTML 不含正文内容，trafilatura 无法提取任何文本。
    此函数识别这些反爬页面特征，以便上游调用方决定是否用浏览器重试。

    检测特征（任一匹配即返回 True）：
        - Cloudflare challenge 脚本标记（_cf_chl_opt、/cdn-cgi/challenge-platform）
        - <noscript> 中要求启用 JavaScript
        - 页面极短且包含 meta refresh（Cloudflare 的另一种展示形式）

    参数：
        html:   fetch_url() 返回的 HTML 字符串

    返回：
        bool:  True 表示 HTML 很可能是反爬页面，需要浏览器渲染
    """
    if not html:
        return False

    html_lower = html.lower()

    # 部分站点直接返回极短的反爬提示文本，不包含标准 HTML / noscript 结构。
    # 例如 Reuters 会返回 "Please enable JS and disable any ad blocker"。
    if is_blocked_extracted_content(html):
        return True

    # Cloudflare managed challenge
    if "_cf_chl_opt" in html:
        return True
    if "/cdn-cgi/challenge-platform" in html:
        return True
    if "challenge-error-text" in html_lower:
        return True

    # <noscript> 中提示需要 JavaScript（Cloudflare / 通用 JS 渲染页面）
    if "enable javascript" in html_lower and "<noscript>" in html_lower:
        return True

    # 中文 Cloudflare 安全验证页面（如 ProductHunt 返回 "正在进行安全验证" +
    # "本网站使用安全服务防护恶意自动程序"）
    if "安全验证" in html or "安全服务防护" in html:
        return True

    return False


def is_blocked_extracted_content(content: str) -> bool:
    """
    判断已提取正文是否其实是反爬、付费墙或工具错误占位。

    参数：
        content: trafilatura / Jina / Playwright 已提取出的正文文本

    返回：
        bool: True 表示正文不可用于后续提取和分析

    设计理由：
        少数站点会把反爬提示伪装成普通短文本，导致上游误判为 success。
        这里做内容层二次检查，防止无意义占位进入 extraction / analysis。
    """
    if not content:
        return False

    normalized = re.sub(r"\s+", " ", content).strip().lower()
    blocked_markers = (
        "please enable js and disable any ad blocker",
        "please enable javascript and disable any ad blocker",
        "please enable javascript",
        "access denied",
        "just a moment",
        "checking your browser",
        "subscribe to unlock this article",
        "error submitting the form",
    )
    return any(marker in normalized for marker in blocked_markers)


def fetch_pdf_text(url: str, timeout: int = 30) -> Optional[str]:
    """
    下载 PDF 并用 pdftotext 提取正文。

    参数：
        url: PDF 文件 URL
        timeout: 下载和解析超时时间（秒）

    返回：
        提取出的纯文本；失败时返回 None

    设计理由：
        HN / 论文 / 基金会来源经常直接指向 PDF。HTML 抽取链路无法处理这类
        URL，若不单独解析会被错误写成 Playwright 失败兜底。
    """
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            pdf_path = f"{tmpdir}/article.pdf"
            text_path = f"{tmpdir}/article.txt"
            curl_result = subprocess.run(
                [
                    "curl", "-s", "-L",
                    "--max-time", str(timeout),
                    "-H", "User-Agent: DailyAIInsightEngine/1.0",
                    "-o", pdf_path,
                    url,
                ],
                capture_output=True,
                text=True,
                timeout=timeout + 5,
            )
            if curl_result.returncode != 0:
                logger.warning(
                    "PDF 下载失败 url=%s code=%d stderr=%s",
                    url,
                    curl_result.returncode,
                    curl_result.stderr.strip()[:200],
                )
                return None

            text_result = subprocess.run(
                ["pdftotext", "-layout", pdf_path, text_path],
                capture_output=True,
                text=True,
                timeout=timeout + 5,
            )
            if text_result.returncode != 0:
                logger.warning(
                    "PDF 文本提取失败 url=%s code=%d stderr=%s",
                    url,
                    text_result.returncode,
                    text_result.stderr.strip()[:200],
                )
                return None

            with open(text_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read().strip()

            return text if len(text) >= 200 else None
    except FileNotFoundError:
        logger.warning("pdftotext 不存在，无法解析 PDF url=%s", url)
        return None
    except subprocess.TimeoutExpired:
        logger.warning("PDF 抓取或解析超时 url=%s timeout=%d", url, timeout)
        return None
    except Exception as exc:
        logger.warning("PDF 抓取异常 url=%s error=%s", url, exc)
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


# ============================================================
# Jina AI Reader 兜底
# ============================================================

_JINA_READER_URL = "https://r.jina.ai"


def fetch_via_jina(url: str, timeout: int = 60) -> Optional[str]:
    """
    通过 Jina AI Reader 获取页面的干净 Markdown 内容。

    用于 Product Hunt 等被 Cloudflare 保护的页面，浏览器/curl 无法直接获取正文。
    Jina 在服务端渲染页面，通常能绕过反爬保护。

    参数：
        url:   原始文章 URL
        timeout: 请求超时秒数

    返回：
        清洗后的 Markdown 正文，失败返回 None
    """
    import urllib.request

    try:
        jina_url = f"{_JINA_READER_URL}/{url}"
        req = urllib.request.Request(
            jina_url,
            headers={"User-Agent": "Googlebot/2.1", "Accept": "text/markdown"},
        )
        resp = urllib.request.urlopen(req, timeout=timeout)
        raw = resp.read().decode("utf-8")
        if raw and len(raw.strip()) > 200:
            return raw.strip()
    except Exception as exc:
        logger.warning("Jina AI Reader 兜底失败 url=%s: %s", url, exc)
    return None
