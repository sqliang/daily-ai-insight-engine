"""
pipeline/ingestion/ingest/producthunt.py — Product Hunt 专用正文兜底

Product Hunt 产品页常被 Cloudflare / JS challenge 拦截，通用 curl +
trafilatura 链路容易写入 failed 兜底文件。本模块只服务 Stage 1b ingest：
配置 PRODUCTHUNT_API_TOKEN 时优先走官方 GraphQL API（2026-08 起 PH 整站
开启 Cloudflare managed challenge，curl/Jina/Playwright 均被稳定拦截，
官方 API 是唯一可靠通道）；无 token 或 API 失败时保持原有兜底链路
（浏览器化请求头 → Jina Reader → Playwright），再把产品页压缩成
下游 extract/analyze 可消费的产品信息 Markdown。
"""

from __future__ import annotations

import html
import json
import logging
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Optional

from pipeline.core.web_utils import extract_article_content, fetch_via_jina, is_bot_challenge_html

logger = logging.getLogger(__name__)

# Product Hunt 官方 GraphQL API 端点（v2，公开数据只读）
_PH_GRAPHQL_URL = "https://api.producthunt.com/v2/api/graphql"

# 产品页查询字段：覆盖 extract/analyze 所需的产品定位、描述、话题与社区信号
_PH_POST_QUERY = """
query($slug: String!) {
  post(slug: $slug) {
    name
    tagline
    description
    votesCount
    commentsCount
    website
    url
    createdAt
    topics { edges { node { name } } }
    makers { name }
  }
}
"""

# 日期窗口兜底查询：/products/ slug 与 post slug 不一致时按发布日期 + 标题/slug 定位
# 带分页：窗口跨多天时帖子数可能超过单页上限
_PH_POSTS_BY_DATE_QUERY = """
query($after: DateTime!, $before: DateTime!, $cursor: String) {
  posts(postedAfter: $after, postedBefore: $before, first: 50, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        slug
        name
        tagline
        description
        votesCount
        commentsCount
        website
        url
        createdAt
        topics { edges { node { name } } }
        makers { name }
      }
    }
  }
}
"""


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

    设计理由：
        PH 整站处于 Cloudflare managed challenge 之后，HTTP/Jina/Playwright
        三条链路实测均会被拦截（仅有概率性放行）。配置了官方 API token 时
        优先走 GraphQL，结构化数据稳定且信息密度高于正文抓取。
    """
    url = article.get("url", "")
    if not url:
        return None

    timeout = int(source_config.get("timeout", 30))

    # --- 优先通道：官方 GraphQL API（需要 PRODUCTHUNT_API_TOKEN）---
    api_result = _fetch_via_graphql(url, article, timeout=timeout)
    if api_result is not None:
        return api_result

    # --- 兜底链路：浏览器化 HTTP → Jina → Playwright ---
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


# ---------------------------------------------------------------------------
# 官方 GraphQL API 通道（优先）
# ---------------------------------------------------------------------------

def _extract_post_slug(url: str) -> str:
    """
    从 Product Hunt 产品页 URL 提取 post slug。

    支持 /products/<slug> 与 /posts/<slug> 两种路径形态，容忍结尾斜杠与 query。
    无法识别时返回空串（调用方据此跳过 API 通道）。
    """
    match = re.search(r"producthunt\.com/(?:products|posts)/([\w-]+)", url)
    return match.group(1) if match else ""


def _fetch_via_graphql(
    url: str,
    article: dict,
    timeout: int,
) -> Optional[ProductHuntIngestResult]:
    """
    通过 Product Hunt 官方 GraphQL API 获取产品结构化数据并组装结果。

    参数：
        url: 产品页 URL（从中提取 post slug）
        article: manifest 条目，API 缺字段时兜底
        timeout: 请求超时秒数

    返回：
        ProductHuntIngestResult: API 命中且关键字段齐备时返回；
        未配置 token、slug 无法识别、API 报错或产品不存在时返回 None，
        由调用方继续走旧兜底链路。
    """
    token = os.environ.get("PRODUCTHUNT_API_TOKEN", "").strip()
    slug = _extract_post_slug(url)
    if not token or not slug:
        return None

    try:
        data = _graphql_request(token, _PH_POST_QUERY, {"slug": slug}, timeout)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        logger.warning("Product Hunt GraphQL 请求失败 url=%s: %s", url, exc)
        return None

    post = (data.get("data") or {}).get("post")
    if not post:
        # /products/<slug> 的 slug 是产品 Hub slug，与 post slug 不一定一致；
        # 直接用 post(slug:) 查不到时，回退为"发布日期窗口 + 标题/slug 匹配"
        logger.info("Product Hunt GraphQL 未找到 post slug=%s，尝试按日期窗口匹配", slug)
        post = _find_post_in_date_window(token, article, slug, timeout)
        if not post:
            logger.info("Product Hunt GraphQL 日期窗口匹配失败 slug=%s", slug)
            return None

    return _result_from_api_post(post, article, url)


def _graphql_request(token: str, query: str, variables: dict, timeout: int) -> dict:
    """向 Product Hunt GraphQL API 发起一次查询，返回解析后的 JSON dict。"""
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        _PH_GRAPHQL_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=max(timeout, 30)) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _find_post_in_date_window(
    token: str,
    article: dict,
    slug: str,
    timeout: int,
) -> Optional[dict]:
    """
    按发布日期窗口拉取 posts 列表，再用标题或 slug 匹配定位 post。

    设计理由：
        PH API 的 posts 查询不支持文本搜索，且 postedAfter/postedBefore 的
        实际语义是"返回 before 当天上榜的那批帖子"（实测：窗口 08-09~08-16
        返回的全部是 08-16 的帖子，after 不生效）。因此只能逐日查询：
        按 published 前后窗口内每一天各查一次，在当天批次内做匹配。
        匹配条件取并集：规范化标题相等、规范化名称与 slug 相等、post slug
        与 Hub slug 相等（覆盖 manifest 标题与 PH 正式名称不一致的情况，
        如标题 "Media Sharing" 对应产品 "argos"）。
    """
    from datetime import datetime, timedelta

    title = (article.get("title") or "").strip()
    published = (article.get("published") or "")[:10]
    if not published:
        return None
    try:
        day = datetime.strptime(published, "%Y-%m-%d")
    except ValueError:
        return None

    # 规范化：小写 + 去除非字母数字，容忍标点、空格与大小写差异
    def _norm(s: str) -> str:
        return re.sub(r"[^a-z0-9]+", "", s.lower())

    norm_title = _norm(title)
    norm_slug = _norm(slug)

    # 按可能性排序逐日探测：published 当天优先，再向前后扩展（容忍 RSS 日期偏差）
    for offset in (0, 1, -1, 2, 3, -2, 4, 5):
        ds = (day + timedelta(days=offset)).strftime("%Y-%m-%d")
        base_variables = {"after": ds + "T00:00:00Z", "before": ds + "T23:59:59Z"}

        # 当天批次可能超过单页 20 条上限，分页遍历（防御性上限 3 页）
        matches: list[dict] = []
        cursor: Optional[str] = None
        for _ in range(3):
            variables = dict(base_variables, cursor=cursor)
            try:
                data = _graphql_request(token, _PH_POSTS_BY_DATE_QUERY, variables, timeout)
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
                logger.warning("Product Hunt GraphQL 日期窗口查询失败: %s", exc)
                return None

            posts_data = (data.get("data") or {}).get("posts") or {}
            for edge in posts_data.get("edges", []):
                node = edge.get("node") or {}
                norm_name = _norm(node.get("name", ""))
                if norm_name and (
                    (norm_title and norm_name == norm_title)
                    or norm_name == norm_slug
                    or _norm(node.get("slug", "")) == norm_slug
                ):
                    matches.append(node)

            page_info = posts_data.get("pageInfo") or {}
            if not page_info.get("hasNextPage"):
                break
            cursor = page_info.get("endCursor")
            if not cursor:
                break

        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            # 同一天出现歧义多个匹配时直接判失败，避免张冠李戴
            return None

    return None


def _result_from_api_post(
    post: dict,
    article: dict,
    url: str,
) -> Optional[ProductHuntIngestResult]:
    """
    把 GraphQL post 对象组装为 ProductHuntIngestResult。

    设计理由：
        API 返回的 website 是 PH 跳转追踪链接而非真实官网，仍保留原值并标注；
        正文字段与 _compose_markdown 的输出结构保持一致，保证下游 extract 的
        提示词对两种来源的 Markdown 形状无感知。
    """
    title = (post.get("name") or article.get("title", "")).strip()
    tagline = (post.get("tagline") or "").strip()
    description = (post.get("description") or "").strip()
    if not title or not (tagline or description):
        return None

    topics = [
        edge["node"]["name"]
        for edge in (post.get("topics") or {}).get("edges", [])
        if edge.get("node", {}).get("name")
    ]
    makers = [m["name"] for m in post.get("makers") or [] if m.get("name")]

    parts = [
        f"# {title}",
        "",
        f"Product Hunt product page for {title}.",
    ]
    if tagline:
        parts.extend(["", f"Tagline: {tagline}"])
    if description:
        parts.extend(["", f"Description: {description}"])
    if post.get("website"):
        parts.extend(["", f"Website: {post['website']}"])
    if topics:
        parts.extend(["", f"Launch tags: {', '.join(topics)}"])
    if post.get("votesCount") is not None:
        parts.extend(["", f"Product Hunt score: {post['votesCount']} upvotes, {post.get('commentsCount', 0)} comments"])
    if makers:
        parts.extend(["", f"Maker or submitter: {', '.join(makers)}"])
    if post.get("createdAt"):
        parts.extend(["", f"Feed published date: {post['createdAt'][:10]}"])
    parts.extend(["", f"Source URL: {url}"])
    parts.extend([
        "",
        "Ingestion note: this content was retrieved via the official Product Hunt GraphQL API. "
        "It intentionally focuses on the product description, launch metadata, category tags, "
        "and community signals available on the public product page.",
    ])
    body = "\n".join(parts).strip()
    if len(body) < 300:
        return None

    return ProductHuntIngestResult(
        title=title,
        description=description or tagline or article.get("summary", ""),
        content=body,
    )


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
