"""
TLDR AI 页面解析器

参考 knowledge-scout/src/parsers/tldrai.py 实现。
TLDR AI 提供 /api/latest/ai 端点，返回最新一期新闻通讯的 HTML。
从 "Headlines & Launches" 和 "Engineering & Research" 两个板块抓取。
"""

import re
from typing import List

from pipeline.core.web_utils import fetch_url
from pipeline.ingestion.html_utils import clean_html_text, extract_section


def parse_tldrai(source: dict) -> List[dict]:
    url = source.get("url", "https://tldr.tech/api/latest/ai")
    html = fetch_url(url)
    if not html:
        return []

    results = []

    # 板块 1: Headlines & Launches (前 5 条)
    headlines_section = extract_section(
        html, r'Headlines &amp; Launches</h3></header>(.*?)</section>'
    )
    if headlines_section:
        pattern = r'<a class="font-bold" href="([^"]+)"[^>]*><h3>([^<]+)</h3></a>'
        for article_url, title in re.findall(pattern, headlines_section)[:5]:
            results.append({
                "url": article_url,
                "title": clean_html_text(title),
                "summary": "TLDR AI 每日头条",
                "published": "",
                "author": "",
            })

    # 板块 2: Engineering & Research (前 3 条)
    research_section = extract_section(
        html, r'Engineering &amp; Research</h3></header>(.*?)</section>'
    )
    if research_section:
        pattern = r'<a class="font-bold" href="([^"]+)"[^>]*><h3>([^<]+)</h3></a>'
        for article_url, title in re.findall(pattern, research_section)[:3]:
            results.append({
                "url": article_url,
                "title": clean_html_text(title),
                "summary": "AI 工程与研究",
                "published": "",
                "author": "",
            })

    # 降级: 如果板块提取失败, 直接匹配所有文章链接
    if not results:
        pattern = (
            r'<a class="font-bold" href="([^"]+?)"'
            r'[^>]*?target="_blank"[^>]*?>'
            r'<h3>([^<]+)</h3></a>'
        )
        for article_url, title in re.findall(pattern, html)[:10]:
            if "utm_source=tldr" in article_url or "Sponsor" in title:
                continue
            results.append({
                "url": article_url,
                "title": clean_html_text(title),
                "summary": "TLDR AI 文章",
                "published": "",
                "author": "",
            })

    return results
