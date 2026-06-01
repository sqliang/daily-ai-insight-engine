"""
OpenAI Blog 文章发现解析器 (Browser 策略)

从 OpenAI 官方 RSS feed 获取最新文章链接列表。
RSS feed 不需要浏览器渲染，但标记为 browser 策略以便 ingest 阶段
使用 Playwright 渲染正文页面（OpenAI 博客文章通过 JS 动态渲染内容）。

设计理由：
    - Scout 阶段不需要 browser_session（RSS feed 直接可读）
    - 标记为 browser 策略后，ingest 阶段自动走 ingest_browser_article()
      用 Playwright 渲染页面 → trafilatura 提取正文
    - URL 从 source["url"] 读取（config.yaml 中配置），不在代码中写死
"""

from typing import List

import feedparser

from pipeline.core.web_utils import fetch_url


def parse_openai_browser(source: dict, browser_session) -> List[dict]:
    """
    从 OpenAI RSS feed 解析文章列表，返回标准化 dict 供 manifest 写入。

    与 _scout_rss() 逻辑相同，但通过 browser parser 接口注册，
    使 ingest 阶段按 browser 策略处理（Playwright 渲染 → trafilatura 提取）。

    参数：
        source:           数据源配置字典，url 字段指向 RSS feed 地址
        browser_session:  Playwright BrowserSession 实例（本解析器不使用）

    返回：
        List[dict]: 文章列表，每篇含 url/title/published/summary/author
    """
    url = source.get("url", "")
    if not url:
        print("         [openai] RSS 源缺少 url 配置")
        return []

    # 先用 curl 获取 RSS XML（curl 走代理比 urllib 更稳定），再交给 feedparser 解析
    # urllib 通过本地 HTTPS 代理时可能遇到 SSL 证书验证问题，curl 不受此影响
    xml_content = fetch_url(url)
    if not xml_content:
        print(f"         [openai] RSS feed 获取失败: {url}")
        return []

    feed = feedparser.parse(xml_content)
    articles: List[dict] = []
    for entry in feed.entries:
        article_url = entry.get("link") or entry.get("url", "")
        title = entry.get("title", "")
        if not article_url or not title:
            continue
        articles.append({
            "url": article_url,
            "title": title,
            "published": entry.get("published", entry.get("updated", "")),
            "summary": entry.get("summary", ""),
            "author": entry.get("author", ""),
        })
    return articles
