"""
pipeline/utils/frontmatter.py — Markdown Frontmatter 读写工具

支持读写 YAML 前置元数据 (--- 包裹的 YAML 块)。
与业务逻辑无关，可独立复用。
"""

import re
from pathlib import Path
from typing import Any, Dict, Tuple

import yaml

from pipeline.utils.file_utils import ensure_dir

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
