"""
机器之心文章列表解析器

支持两种抓取模式:
- parse_machine_heart: curl 获取 HTML (适用于服务端渲染)
- parse_machine_heart_browser: Playwright 浏览器渲染 (适用于 SPA)
"""

import re
from typing import List

from pipeline.core.web_utils import fetch_url
from pipeline.ingestion.html_utils import clean_html_text, extract_date_from_path


def parse_machine_heart(source: dict) -> List[dict]:
    """curl-based HTML 解析 (已废弃 — 机器之心改为 SPA 渲染)。"""
    url = source.get("url", "https://www.jiqizhixin.com/")
    html = fetch_url(url)
    if not html:
        return []

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
            "title": clean_html_text(title),
            "published": extract_date_from_path(path),
            "summary": "",
        })
    return articles


def parse_machine_heart_browser(source: dict, browser_session) -> List[dict]:
    """Playwright 浏览器渲染解析。"""
    url = source.get("url", "https://www.jiqizhixin.com/")
    wait_for = source.get("wait_for", ".article-item")

    page = browser_session.new_page()
    articles: List[dict] = []

    try:
        page.goto(url, timeout=30000, wait_until="domcontentloaded")
        try:
            page.wait_for_selector(wait_for, timeout=15000)
        except Exception:
            page.wait_for_timeout(3000)

        link_els = page.query_selector_all("a[href*='/articles/']")
        seen = set()

        for link_el in link_els:
            href = link_el.get_attribute("href") or ""
            title = link_el.inner_text().strip()

            if not href or not title:
                continue
            if "/articles/" not in href:
                continue
            if href in seen:
                continue
            seen.add(href)

            if not href.startswith("http"):
                href = "https://www.jiqizhixin.com" + href

            articles.append({
                "url": href,
                "title": title,
                "published": extract_date_from_path(href),
                "summary": "",
                "author": "",
            })
    except Exception as e:
        print(f"         [machine-heart] 解析异常: {e}")
    finally:
        page.close()

    return articles
