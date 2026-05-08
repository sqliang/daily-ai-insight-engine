"""
知乎发现页解析器 (Playwright 浏览器渲染)

从 https://www.zhihu.com/explore 提取热门讨论列表。
页面是 React SPA，需要 `networkidle` 等待 JS 渲染完成。
通过后续关键词过滤筛选 AI 相关内容。
"""

from typing import List


def parse_zhihu_browser(source: dict, browser_session) -> List[dict]:
    url = source.get("url", "https://www.zhihu.com/explore")

    page = browser_session.new_page()
    articles: List[dict] = []

    try:
        page.goto(url, timeout=30000, wait_until="networkidle")

        links = page.query_selector_all("a[href]")
        seen_urls = set()

        for link_el in links:
            href = link_el.get_attribute("href") or ""
            title = link_el.inner_text().strip()

            if not any(p in href for p in ("/question/", "/p/")):
                continue
            if len(title) < 5:
                continue

            if not href.startswith("http"):
                href = "https://www.zhihu.com" + href
            # 移除 query 参数
            from urllib.parse import urlparse, urlunparse
            parsed = urlparse(href)
            href = urlunparse(
                (parsed.scheme, parsed.netloc, parsed.path, parsed.params, "", "")
            )

            if href not in seen_urls:
                seen_urls.add(href)
                articles.append({
                    "url": href,
                    "title": title,
                    "published": "",
                    "summary": "",
                    "author": "",
                })
    except Exception as e:
        print(f"         [zhihu] 解析异常: {e}")
    finally:
        page.close()

    return articles
