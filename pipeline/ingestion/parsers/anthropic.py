"""
Anthropic 新闻页面解析器

Anthropic 官网无 RSS feed，通过解析 sitemap.xml 获取全部页面 URL，
筛选 /news/ 路径的文章，按 lastmod 日期排序取最新。
标题从 URL slug 推导 (e.g. claude-opus-4-7 -> Claude Opus 4.7)。
"""

import re
import xml.etree.ElementTree as ET
from typing import List

from pipeline.core.web_utils import fetch_url
from pipeline.ingestion.html_utils import slug_to_title


def parse_anthropic(source: dict) -> List[dict]:
    url = source.get("url", "https://www.anthropic.com/sitemap.xml")
    html = fetch_url(url)
    if not html:
        return []

    try:
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
        if "/news/" not in href:
            continue

        date_str = lastmod.text if lastmod is not None and lastmod.text else ""
        slug = href.rstrip("/").split("/")[-1]
        title = slug_to_title(slug)

        articles.append({
            "url": href,
            "title": title,
            "published": date_str[:10] if date_str else "",
            "summary": "",
        })

    articles.sort(key=lambda a: a.get("published", ""), reverse=True)
    return articles
