"""
Markdown Frontmatter 读写工具

支持读写 YAML 前置元数据 (--- 包裹的 YAML 块)，用于所有流水线阶段操作 .md 文件。
"""

import re
from datetime import date
from pathlib import Path
from typing import Any, Dict, Tuple

import yaml


# 匹配 YAML frontmatter 块: 开头的 --- ... ---
_FRONTMATTER_RE = re.compile(
    r"^---\s*\n(.*?)\n---\s*\n?(.*)",
    re.DOTALL,
)


def read_frontmatter(filepath: Path) -> Tuple[Dict[str, Any], str]:
    """
    读取 .md 文件，返回 (frontmatter 字典, 正文内容)。
    文件不存在或没有 frontmatter 时返回 ({}, "")。
    """
    if not filepath.exists():
        return {}, ""

    content = filepath.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(content)
    if not m:
        return {}, content

    try:
        metadata = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        metadata = {}

    body = m.group(2)
    return metadata, body


def write_frontmatter(filepath: Path, metadata: Dict[str, Any], body: str) -> None:
    """
    写入带 YAML frontmatter 的 .md 文件。
    确保目录存在。
    """
    from .file_utils import ensure_dir

    ensure_dir(filepath.parent)

    # 确保 tags 始终为列表格式
    if "tags" in metadata and isinstance(metadata["tags"], list):
        pass  # 列表格式直接序列化即可

    fm_yaml = yaml.dump(
        metadata,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).strip()

    md_content = f"---\n{fm_yaml}\n---\n\n{body}"
    filepath.write_text(md_content, encoding="utf-8")


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
