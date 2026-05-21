"""
知乎热榜解析器 (Playwright 浏览器渲染)

从 https://www.zhihu.com/hot 提取热门讨论列表。
页面是 React SPA，需要浏览器渲染，通过后续关键词过滤筛选 AI 相关内容。

设计理由：
    - 使用 browser_session.fetch_page_html() 获取渲染后 HTML，再通过 page 查询 DOM，
      兼顾 wait_for 配置支持和灵活的 DOM 遍历
    - 通过 JS evaluate 向上遍历父元素提取相对时间（"2小时前"等），
      转换为 ISO 格式日期供后续 filter_by_age 使用
    - 滚动加载更多热榜内容，避免只抓到首屏几篇
    - /hot 页面是知乎热榜，每天更新，比 /explore 推荐页更适合日更情报
"""

import re
from datetime import datetime, timedelta, timezone
from typing import List
from urllib.parse import urlparse, urlunparse


def parse_zhihu_browser(source: dict, browser_session) -> List[dict]:
    """
    解析知乎热榜页面，提取 AI 相关问题链接及发布时间。

    流程：
        1. 导航到知乎热榜 URL
        2. 等待配置的 wait_for 选择器（默认 a[href*='/question/']）
        3. 滚动加载更多内容
        4. 提取所有问题链接，通过 JS 向上查找父级元素中的时间文本
        5. 转换相对时间为 ISO 格式

    参数：
        source: 数据源配置字典，需包含 url / wait_for 字段
        browser_session: Playwright BrowserSession 上下文管理器实例

    返回：
        List[dict]: 文章列表，每篇含 url/title/published/summary/author
    """
    url = source.get("url", "https://www.zhihu.com/hot")
    wait_for = source.get("wait_for", "a[href*='/question/']")

    page = browser_session.new_page()
    articles: List[dict] = []

    try:
        page.goto(url, timeout=30000, wait_until="domcontentloaded")
        page.wait_for_selector(wait_for, timeout=15000)

        # 滚动加载更多热榜项（知乎热榜首次渲染约 10 条，滚动后加载更多）
        for _ in range(3):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1200)

        # 提取所有问题链接
        link_elements = page.query_selector_all("a[href*='/question/']")
        seen_urls = set()

        for link_el in link_elements:
            href = link_el.get_attribute("href") or ""
            if not href:
                continue

            # 提取链接文本作为标题
            title = link_el.inner_text().strip()
            if len(title) < 5:
                continue

            # 构建完整 URL，去除 query 参数
            if not href.startswith("http"):
                href = "https://www.zhihu.com" + href
            parsed = urlparse(href)
            href = urlunparse(
                (parsed.scheme, parsed.netloc, parsed.path, parsed.params, "", "")
            )

            if href in seen_urls:
                continue
            seen_urls.add(href)

            # 尝试从父元素中提取时间信息
            published = _extract_time(link_el)

            articles.append({
                "url": href,
                "title": title,
                "published": published,
                "summary": "",
                "author": "",
            })

    except Exception as e:
        print(f"         [zhihu] 解析异常: {e}")
    finally:
        page.close()

    return articles


def _extract_time(link_el) -> str:
    """
    从链接元素的父级卡片中提取相对时间并转换为 ISO 格式。

    通过 JS evaluate 向上最多 5 层父元素查找匹配的时间文本，
    支持 "X小时前"、"X分钟前"、"X天前"、"昨天" 等格式。
    无法提取时返回空字符串（filter_by_age 对空值不做过滤）。
    """
    try:
        rel_time = link_el.evaluate("""
            el => {
                let parent = el.parentElement;
                for (let i = 0; i < 5 && parent; i++) {
                    const text = parent.textContent || '';
                    const match = text.match(/(\\d+\\s*(?:小时|分钟|天)前|昨天)/);
                    if (match) return match[1];
                    parent = parent.parentElement;
                }
                return '';
            }
        """)
        if rel_time:
            return _parse_relative_time(rel_time)
    except Exception:
        pass
    return ""


def _parse_relative_time(rel_time: str) -> str:
    """
    将中文相对时间转换为 ISO 8601 格式日期字符串。

    支持格式：
        - "N分钟前" → 当前时间 - N 分钟
        - "N小时前" → 当前时间 - N 小时
        - "N天前"   → 当前时间 - N 天
        - "昨天"    → 当前日期 - 1 天
    """
    now = datetime.now(timezone.utc)

    if "分钟" in rel_time:
        match = re.search(r'\d+', rel_time)
        mins = int(match.group()) if match else 0
        dt = now - timedelta(minutes=mins)
    elif "小时" in rel_time:
        match = re.search(r'\d+', rel_time)
        hours = int(match.group()) if match else 0
        dt = now - timedelta(hours=hours)
    elif "天" in rel_time:
        match = re.search(r'\d+', rel_time)
        days = int(match.group()) if match else 0
        dt = now - timedelta(days=days)
    elif "昨天" in rel_time:
        dt = now - timedelta(days=1)
    else:
        return ""

    return dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")
