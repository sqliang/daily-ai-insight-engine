"""
pipeline/utils/frontmatter.py — Markdown Frontmatter 读写工具

支持读写 YAML 前置元数据 (--- 包裹的 YAML 块)。
与业务逻辑无关，可独立复用。
"""

import re
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Tuple

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


def read_created_date(filepath: Path) -> str:
    """
    读取 .md 文件 frontmatter 中的 created 字段，统一返回 YYYY-MM-DD 字符串。

    兼容 YAML 解析出的 date 对象与字符串（取前 10 字符）。
    文件不存在、无 frontmatter 或无 created 字段时返回 ""。
    """
    if not filepath.exists():
        return ""
    metadata, _ = read_frontmatter(filepath)
    created = metadata.get("created", "")
    if isinstance(created, date):
        return created.isoformat()
    return str(created)[:10]


def filter_by_created(files: List[Path], target: date) -> List[Path]:
    """
    按 frontmatter created == target 过滤文件列表（日期隔离的核心过滤器）。

    供 extract/analyze 阶段的 --target-date 参数使用，防止阶段执行误伤
    其他日期的文章（2026-07-29 事故：未隔离导致 1300+ 篇历史积压被处理）。

    设计理由：
        created 缺失或 frontmatter 无法解析的文件被**保守排除**——
        指定日期运行时，宁可漏处理（后续 check 门禁会发现），
        也不能把范围外的文件送进 LLM（成本不可逆）。
    """
    target_str = target.isoformat()
    return [fp for fp in files if read_created_date(fp) == target_str]
