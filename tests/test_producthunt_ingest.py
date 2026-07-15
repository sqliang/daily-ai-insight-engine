"""
tests/test_producthunt_ingest.py — Product Hunt ingest 兜底测试

覆盖 Stage 1b 对 Product Hunt 产品页的专用解析逻辑，确保反爬页不会被
误写成 success，同时历史 manifest 日期能保留到 frontmatter。
"""

from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
from pipeline.ingestion.ingest.producthunt import extract_producthunt_content


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
