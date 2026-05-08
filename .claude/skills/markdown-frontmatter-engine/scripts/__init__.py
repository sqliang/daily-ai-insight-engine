# scripts/__init__.py
"""
Markdown Frontmatter Engine — 脚本包初始化

提供向后兼容的模块级导入，使得外部代码可以直接从 scripts 包导入：
    from scripts import scan_notes, read_note, ...
而不必知道内部模块的具体划分。

新增子模块后，在此文件中添加对应的 re-export 即可保持导入路径不变。
"""

from .types import (
    NoteInfo,
    NoteReadResult,
    SchemaEntry,
    WriteResultItem,
    WriteMultiResult,
)

from .frontmatter import parse_frontmatter, build_frontmatter
from .schema_ops import scan_schema, get_field_order, parse_schema_priority
from .env_config import load_env_fields
from .file_ops import scan_notes, read_note, write_frontmatter, write_multi_from_json

__all__ = [
    # 类型
    "NoteInfo",
    "NoteReadResult",
    "SchemaEntry",
    "WriteResultItem",
    "WriteMultiResult",
    # frontmatter
    "parse_frontmatter",
    "build_frontmatter",
    # schema
    "scan_schema",
    "get_field_order",
    "parse_schema_priority",
    # env
    "load_env_fields",
    # file_ops
    "scan_notes",
    "read_note",
    "write_frontmatter",
    "write_multi_from_json",
]
