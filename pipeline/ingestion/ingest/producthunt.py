"""
pipeline/ingestion/ingest/producthunt.py — Product Hunt 专用正文兜底

Product Hunt 产品页常被 Cloudflare / JS challenge 拦截，通用 curl +
trafilatura 链路容易写入 failed 兜底文件。本模块只服务 Stage 1b ingest：
先用浏览器化请求头/Jina Reader/Playwright 获取页面，再把产品页压缩成
下游 extract/analyze 可消费的产品信息 Markdown。
"""

from __future__ import annotations

import html
import logging
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Optional

from pipeline.core.web_utils import extract_article_content, fetch_via_jina, is_bot_challenge_html

logger = logging.getLogger(__name__)


@dataclass
class ProductHuntIngestResult:
    """Product Hunt 专用兜底的结构化结果。"""

    title: str
    description: str
    content: str


def fetch_producthunt_article(
    article: dict,
    source_config: dict,
    session: Optional["BrowserSession"] = None,
) -> Optional[ProductHuntIngestResult]:
    """
    抓取并整理 Product Hunt 产品页正文。

    参数：
        article: manifest 中的文章条目，提供 title/url/summary 等兜底字段。
        source_config: Product Hunt 源配置，用于 timeout 等抓取参数。
        session: 可选 Playwright BrowserSession。常规 worker 不传入时只尝试
            浏览器化 HTTP 和 Jina；browser retry 传入后再尝试 Playwright。

    返回：
        ProductHuntIngestResult: 正文质量达标时返回；全部兜底失败时返回 None。
    """
    url = article.get("url", "")
    if not url:
        return None

    timeout = int(source_config.get("timeout", 30))
    candidates: list[str] = []

    direct_html = _fetch_with_browser_headers(url, timeout=timeout)
    if direct_html:
        candidates.append(direct_html)

    jina_body = fetch_via_jina(url, timeout=max(timeout, 60))
    if jina_body:
        candidates.append(jina_body)

    if session is not None:
        rendered_html = session.fetch_page_html(
            url,
            timeout=timeout * 1000,
            wait_until=source_config.get("wait_until", "domcontentloaded"),
            wait_ms=source_config.get("wait_ms", 5000),
            wait_for=source_config.get("wait_for"),
            wait_for_fn=source_config.get("wait_for_fn"),
        )
        if rendered_html:
            candidates.append(rendered_html)

    for raw in candidates:
        result = extract_producthunt_content(raw, article)
        if result is not None:
            return result

    return None


def extract_producthunt_content(raw: str, article: dict) -> Optional[ProductHuntIngestResult]:
    """
    从 Product Hunt HTML/Markdown 中提取产品核心信息并生成 Markdown。

    参数：
        raw: 直接 HTML、Jina Markdown 或 Playwright HTML。
        article: manifest 条目，用于补齐 title/summary/author/published。

    返回：
        ProductHuntIngestResult: 成功提取时返回；反爬页或正文过短时返回 None。
    """
    if not raw or is_bot_challenge_html(raw):
        return None

    text = _to_readable_text(raw, article.get("url", ""))
    if not text or is_bot_challenge_html(text):
        return None

    lines = _clean_lines(text)
    if not lines:
        return None

    title = _pick_title(lines, article)
    tagline = _pick_tagline(lines, title, article)
    description = _pick_description(lines, tagline, article)
    website = _pick_website(lines)
    tags = _pick_launch_tags(lines)
    launched = _pick_matching_line(lines, ("Launched ", "Launched in "))
    upvote = _pick_matching_line(lines, ("Upvote",))
    followers = _pick_matching_line(lines, ("followers", "follower"))
    forum = _pick_forum(lines)

    body = _compose_markdown(
        title=title,
        tagline=tagline,
        description=description,
        website=website,
        tags=tags,
        launched=launched,
        upvote=upvote,
        followers=followers,
        forum=forum,
        article=article,
    )
    if len(body) < 300:
        return None

    return ProductHuntIngestResult(
        title=title or article.get("title", ""),
        description=description or tagline or article.get("summary", ""),
        content=body,
    )


def _fetch_with_browser_headers(url: str, timeout: int) -> Optional[str]:
    """使用更接近真实浏览器的请求头获取 Product Hunt 页面。"""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/130.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
        return body if body and len(body.strip()) > 200 else None
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        logger.info("Product Hunt 浏览器化请求失败 url=%s: %s", url, exc)
        return None


def _to_readable_text(raw: str, url: str) -> str:
    """将 HTML 或 Markdown 统一转换为便于行级提取的文本。"""
    if "<html" in raw[:1000].lower() or "<body" in raw[:2000].lower():
        extracted = extract_article_content(raw, url) or ""
        if extracted:
            return extracted
        raw = re.sub(r"<script\b[^<]*(?:(?!</script>)<[^<]*)*</script>", "\n", raw, flags=re.I)
        raw = re.sub(r"<style\b[^<]*(?:(?!</style>)<[^<]*)*</style>", "\n", raw, flags=re.I)
        raw = re.sub(r"<[^>]+>", "\n", raw)
    return html.unescape(raw)


def _clean_lines(text: str) -> list[str]:
    """清理 Markdown 链接、图片和多余空白，保留页面中的语义行。"""
    cleaned = re.sub(r"!\[[^\]]*]\([^)]*\)", "\n", text)
    cleaned = re.sub(r"\[([^\]]+)]\(([^)]+)\)", r"\1", cleaned)
    cleaned = re.sub(r"^[#>*\-\s]+", "", cleaned, flags=re.M)
    lines: list[str] = []
    for line in cleaned.splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if line and line not in lines:
            lines.append(line)
    return lines


def _pick_title(lines: list[str], article: dict) -> str:
    """选择产品名，优先使用 manifest 标题以避免导航栏干扰。"""
    manifest_title = article.get("title", "").strip()
    if manifest_title:
        return manifest_title
    for line in lines:
        if 2 <= len(line) <= 80 and not line.lower().startswith(("best products", "launches")):
            return line
    return ""


def _pick_tagline(lines: list[str], title: str, article: dict) -> str:
    """选择产品 tagline，过滤重复标题和导航文案。"""
    summary = _clean_summary(article.get("summary", ""))
    seen_title = False
    for line in lines:
        if title and line == title:
            seen_title = True
            continue
        if seen_title and _looks_like_product_sentence(line):
            return line
    return summary


def _pick_description(lines: list[str], tagline: str, article: dict) -> str:
    """选择较完整的产品描述，manifest summary 作为最后兜底。"""
    for line in lines:
        if line == tagline:
            continue
        if _looks_like_product_sentence(line) and len(line) >= 60:
            return line
    return _clean_summary(article.get("summary", ""))


def _pick_website(lines: list[str]) -> str:
    """提取官网行。"""
    for line in lines:
        if line.startswith("Visit website"):
            return line.replace("Visit website", "").strip() or line
        if re.search(r"\b[a-z0-9-]+\.(com|ai|io|dev|app|co)\b", line, flags=re.I):
            return line
    return ""


def _pick_launch_tags(lines: list[str]) -> list[str]:
    """提取 Launch tags 后的标签。"""
    for index, line in enumerate(lines):
        if line.startswith("Launch tags:"):
            raw = line.removeprefix("Launch tags:").strip()
            if not raw and index + 1 < len(lines):
                raw = lines[index + 1]
            return [part.strip(" •,") for part in re.split(r"[•,]", raw) if part.strip(" •,")]
    return []


def _pick_matching_line(lines: list[str], prefixes: tuple[str, ...]) -> str:
    """按前缀/关键词选择一行页面事实。"""
    lowered_prefixes = tuple(prefix.lower() for prefix in prefixes)
    for line in lines:
        low = line.lower()
        if any(low.startswith(prefix) or prefix in low for prefix in lowered_prefixes):
            return line
    return ""


def _pick_forum(lines: list[str]) -> str:
    """提取产品论坛 slug。"""
    for line in lines:
        if line.startswith("p/"):
            return line
    return ""


def _looks_like_product_sentence(line: str) -> bool:
    """判断一行是否像产品 tagline/description，而不是导航或页脚。"""
    if len(line) < 12 or len(line) > 500:
        return False
    low = line.lower()
    blocked = (
        "sign in", "subscribe", "top product categories", "trending categories",
        "top reviewed", "trending products", "copyright", "privacy", "terms",
        "launch team", "company info", "reviews", "view all",
    )
    return not any(token in low for token in blocked)


def _clean_summary(summary: str) -> str:
    """去掉 RSS summary 中 Product Hunt 固定尾巴。"""
    return summary.replace("Discussion | Link", "").replace("Discussion", "").replace("| Link", "").strip()


def _compose_markdown(
    *,
    title: str,
    tagline: str,
    description: str,
    website: str,
    tags: list[str],
    launched: str,
    upvote: str,
    followers: str,
    forum: str,
    article: dict,
) -> str:
    """把已提取字段组合成稳定 Markdown，供后续 LLM 阶段读取。"""
    parts = [
        f"# {title}",
        "",
        f"Product Hunt product page for {title}.",
    ]
    if tagline:
        parts.extend(["", f"Tagline: {tagline}"])
    if description:
        parts.extend(["", f"Description: {description}"])
    if website:
        parts.extend(["", f"Website: {website}"])
    if tags:
        parts.extend(["", f"Launch tags: {', '.join(tags)}"])
    if launched:
        parts.extend(["", f"Launch timing: {launched}"])
    if upvote:
        parts.extend(["", f"Product Hunt score: {upvote}"])
    if followers:
        parts.extend(["", f"Community signal: {followers}"])
    if forum:
        parts.extend(["", f"Forum: {forum}"])
    if article.get("author"):
        parts.extend(["", f"Maker or submitter: {article['author']}"])
    if article.get("published"):
        parts.extend(["", f"Feed published date: {article['published']}"])
    if article.get("url"):
        parts.extend(["", f"Source URL: {article['url']}"])
    parts.extend([
        "",
        "Ingestion note: this content was extracted from Product Hunt product-page metadata "
        "after anti-bot fallback handling. It intentionally focuses on the product description, "
        "launch metadata, category tags, and community signals available on the public product page.",
    ])
    return "\n".join(parts).strip()
