"""
tests/test_producthunt_ingest.py — Product Hunt ingest 兜底测试

覆盖 Stage 1b 对 Product Hunt 产品页的专用解析逻辑，确保反爬页不会被
误写成 success，同时历史 manifest 日期能保留到 frontmatter。
"""

from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
from pipeline.ingestion.ingest.producthunt import (
    _extract_post_slug,
    _fetch_via_graphql,
    _result_from_api_post,
    extract_producthunt_content,
)


def test_extract_producthunt_content_from_html():
    """Product Hunt 产品页 HTML 应被整理成包含核心产品字段的 Markdown。"""
    article = {
        "url": "https://www.producthunt.com/products/cewsco",
        "title": "Cewsco",
        "summary": "All-in-one AI assistant — chat, images, voice & market data Discussion | Link",
        "author": "kal winthrop",
        "published": "2026-06-25",
    }
    html = """
    <html><body>
      <h1>Cewsco</h1>
      <h2>Do everything with Cewsco ai</h2>
      <a>Visit website</a><a>cewsco.com</a>
      <p>Cewsco is the all-in-one AI assistant at cewsco.com. Chat, generate images,
      have voice conversations, and write code — all in one app. Powered by Orion AI.
      Free to try.</p>
      <p>Launch tags: SaaS • Artificial Intelligence • Computers</p>
      <p>Launched 12d ago</p>
      <p>Upvote • 2 points</p>
      <p>2 followers</p>
      <p>p/cewsco</p>
    </body></html>
    """

    result = extract_producthunt_content(html, article)

    assert result is not None
    assert result.title == "Cewsco"
    assert result.description.startswith("Cewsco is the all-in-one AI assistant")
    assert "Launch tags: SaaS, Artificial Intelligence, Computers" in result.content
    assert "Source URL: https://www.producthunt.com/products/cewsco" in result.content
    assert len(result.content) > 300


def test_extract_producthunt_content_rejects_antibot_page():
    """反爬验证页不能被误判为有效产品正文。"""
    article = {
        "url": "https://www.producthunt.com/products/cewsco",
        "title": "Cewsco",
        "summary": "All-in-one AI assistant",
    }
    html = """
    <html><body>
      <h1>正在进行安全验证</h1>
      <p>本网站使用安全服务防护恶意自动程序。</p>
      <script>window._cf_chl_opt = {}</script>
    </body></html>
    """

    assert extract_producthunt_content(html, article) is None


def test_build_ingestion_frontmatter_uses_manifest_created_date():
    """历史 manifest 重跑时 frontmatter created 应保留 manifest 日期。"""
    fm = build_ingestion_frontmatter(
        title="Cewsco",
        url="https://www.producthunt.com/products/cewsco",
        source_name="producthunt",
        article_id="ed176ccf41297247",
        extraction_status="success",
        created="2026-06-26",
    )

    assert fm["created"] == "2026-06-26"
    assert fm["manifest_dates"] == ["2026-06-26"]


# ---------------------------------------------------------------------------
# GraphQL API 通道
# ---------------------------------------------------------------------------

def test_extract_post_slug():
    """产品页 URL 的 slug 提取应覆盖 /products/ 与 /posts/ 两种形态。"""
    assert _extract_post_slug("https://www.producthunt.com/products/gemini-3-7-flash") == "gemini-3-7-flash"
    assert _extract_post_slug("https://www.producthunt.com/posts/min-4?utm_source=x") == "min-4"
    assert _extract_post_slug("https://example.com/other") == ""


def _api_post_payload() -> dict:
    """构造一份与真实 GraphQL 响应同构的 post 对象。"""
    return {
        "name": "Gemini 3.7 Flash",
        "tagline": "Google's smartest workhorse yet for coding & agents",
        "description": "Gemini 3.7 Flash is a fast multimodal model for coding and agent workflows.",
        "votesCount": 246,
        "commentsCount": 31,
        "website": "https://www.producthunt.com/r/ABC",
        "url": "https://www.producthunt.com/posts/gemini-3-7-flash",
        "createdAt": "2026-08-13T07:01:00Z",
        "topics": {"edges": [{"node": {"name": "Artificial Intelligence"}}, {"node": {"name": "Development"}}]},
        "makers": [{"name": "Ankit Sharma"}],
    }


def test_result_from_api_post_builds_markdown():
    """API post 对象应组装成包含核心产品字段的 Markdown。"""
    result = _result_from_api_post(
        _api_post_payload(),
        article={"title": "Gemini 3.7 Flash"},
        url="https://www.producthunt.com/products/gemini-3-7-flash",
    )

    assert result is not None
    assert result.title == "Gemini 3.7 Flash"
    assert "Tagline: Google's smartest workhorse yet" in result.content
    assert "Launch tags: Artificial Intelligence, Development" in result.content
    assert "246 upvotes" in result.content
    assert "Maker or submitter: Ankit Sharma" in result.content
    assert len(result.content) > 300


def test_result_from_api_post_rejects_missing_fields():
    """缺标题或缺 tagline/description 时应判定为不可用结果。"""
    assert _result_from_api_post({"name": ""}, {}, "https://www.producthunt.com/products/x") is None
    assert _result_from_api_post({"name": "X"}, {}, "https://www.producthunt.com/products/x") is None


def test_fetch_via_graphql_requires_token_and_slug(monkeypatch):
    """未配置 token 或 URL 无法提取 slug 时直接返回 None，不发请求。"""
    monkeypatch.delenv("PRODUCTHUNT_API_TOKEN", raising=False)
    assert _fetch_via_graphql("https://www.producthunt.com/products/x", {}, timeout=5) is None

    monkeypatch.setenv("PRODUCTHUNT_API_TOKEN", "fake-token")
    assert _fetch_via_graphql("https://example.com/other", {}, timeout=5) is None


def test_find_post_in_date_window(monkeypatch):
    """slug 查不到时应按日期窗口 + 规范化标题匹配定位 post。"""
    from pipeline.ingestion.ingest import producthunt as ph

    calls = []

    def fake_request(token, query, variables, timeout):
        calls.append(variables)
        node = _api_post_payload() | {"slug": "gemini-3-7-flash"}
        return {"data": {"posts": {"edges": [{"node": node}, {"node": _api_post_payload() | {"name": "Other Tool", "slug": "other-tool"}}]}}}

    monkeypatch.setattr(ph, "_graphql_request", fake_request)
    post = ph._find_post_in_date_window(
        "fake-token",
        {"title": "Gemini 3.7 Flash", "published": "2026-08-13"},
        slug="gemini-3-7-flash",
        timeout=5,
    )

    assert post is not None and post["name"] == "Gemini 3.7 Flash"
    # 逐日探测：第一天即 published 当天，且为合法 ISO 格式
    assert calls[0]["after"] == "2026-08-13T00:00:00Z"
    assert calls[0]["before"] == "2026-08-13T23:59:59Z"


def test_find_post_in_date_window_matches_by_slug_when_title_differs(monkeypatch):
    """manifest 标题与 PH 正式名称不一致时（如 'Media Sharing' vs argos），可用 slug 匹配。"""
    from pipeline.ingestion.ingest import producthunt as ph

    def fake_request(token, query, variables, timeout):
        node = _api_post_payload() | {"name": "Argos", "slug": "argos"}
        return {"data": {"posts": {"edges": [{"node": node}]}}}

    monkeypatch.setattr(ph, "_graphql_request", fake_request)
    post = ph._find_post_in_date_window(
        "fake-token",
        {"title": "Media Sharing", "published": "2026-08-13"},
        slug="argos",
        timeout=5,
    )
    assert post is not None and post["name"] == "Argos"


def test_find_post_in_date_window_rejects_ambiguous(monkeypatch):
    """窗口内出现多个同名产品时应判定失败，避免张冠李戴。"""
    from pipeline.ingestion.ingest import producthunt as ph

    def fake_request(token, query, variables, timeout):
        dup = _api_post_payload() | {"slug": "gemini-3-7-flash"}
        return {"data": {"posts": {"edges": [{"node": dup}, {"node": dict(dup)}]}}}

    monkeypatch.setattr(ph, "_graphql_request", fake_request)
    assert ph._find_post_in_date_window(
        "fake-token",
        {"title": "Gemini 3.7 Flash", "published": "2026-08-13"},
        slug="gemini-3-7-flash",
        timeout=5,
    ) is None
