"""
HTML / 文本解析辅助函数

提供 HTML 实体清理、正则板块提取、URL slug 转标题等工具函数，
被各专用解析器复用。
"""

import re


def extract_section(html: str, pattern: str) -> str:
    """从 HTML 中用正则提取一个板块内容。"""
    m = re.search(pattern, html, re.DOTALL)
    return m.group(1) if m else ""


def clean_html_text(text: str) -> str:
    """清理 HTML 实体和多余空白。"""
    if not text:
        return ""
    text = text.replace("&amp;", "&").replace("&#x27;", "'")
    text = text.replace("&quot;", '"').replace("&lt;", "<").replace("&gt;", ">")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def slug_to_title(slug: str) -> str:
    """将 URL slug 转换为可读标题 (e.g. claude-opus-4-7 -> Claude Opus 4.7)。"""
    preserve_case = {"ai", "api", "sdk", "gpu", "cpu", "llm", "rlhf", "uk", "us", "eu"}
    words = []
    for w in slug.split("-"):
        if w.lower() in preserve_case:
            words.append(w.upper() if w.islower() and len(w) <= 4 else w)
        elif w.isdigit():
            words.append(w)
        else:
            words.append(w.capitalize())
    return " ".join(words)


def extract_date_from_path(path: str) -> str:
    """从 /articles/YYYY-MM-DD-xxx 路径中提取日期。"""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", path)
    return m.group(1) if m else ""
