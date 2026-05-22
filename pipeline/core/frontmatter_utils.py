"""
pipeline/core/frontmatter_utils.py — Ingestion Frontmatter 构建工具

构建 Stage 1 产出的标准 YAML frontmatter，定义流水线中所有 .md 文件的元数据格式。
纯通用的 frontmatter 读写已提取至 pipeline.utils.frontmatter。
"""

import re
from datetime import date
from typing import Any, Dict


def build_ingestion_frontmatter(
    title: str,
    url: str,
    published: str = "",
    author: str = "",
    description: str = "",
    source_name: str = "",
    article_id: str = "",
    extraction_status: str = "success",
) -> Dict[str, Any]:
    """
    构建 Stage 1 产出的标准 Frontmatter 字段。
    与 data/01_raw/ 中现有 .md 文件的 frontmatter 格式对齐。

    article_id: 由 00_manifest 阶段预生成的 SHA-256 文章 ID。
                如果提供，将写入 frontmatter 作为该文章在流水线中的唯一标识。
                后续所有阶段都基于此 ID 进行去重和关联。

    extraction_status: 正文提取状态，供下游阶段和人类读者判断内容质量。
        - "success": trafilatura 成功提取正文
        - "partial": HTML 获取成功但 trafilatura 未能提取正文，body 为 manifest summary 兜底
        - "failed":  HTML 获取失败，body 为错误说明 + manifest summary

    pipeline_stage: 标记文件已完成 Stage 1 处理，供下游阶段做前置检查。
        下游 Stage 2b 会检查此字段确认 Stage 2a 已执行。
    """
    authors = []
    if author:
        # wiki-link 格式：[[Author Name]]
        authors.append(f"[[{author}]]")

    fm = {
        "title": title,
        "source": url,
        "author": authors,
        "published": _normalize_date(published),
        "created": date.today().isoformat(),
        "description": description,
        "tags": ["clippings"],
        "extraction_status": extraction_status,
        "pipeline_stage": "ingested",
    }

    # 将预生成的文章 ID 置入 frontmatter，成为该文件在流水线中的"身份证"
    if article_id:
        fm["id"] = article_id

    return fm


# ============================================================
# 内部工具
# ============================================================

def _normalize_date(date_str: str) -> str:
    """尝试将各种日期字符串规范化为 YYYY-MM-DD 格式。"""
    if not date_str:
        return ""
    # 去除时间部分，只保留日期
    m = re.match(r"(\d{4}-\d{2}-\d{2})", str(date_str))
    if m:
        return m.group(1)
    return str(date_str).strip()
