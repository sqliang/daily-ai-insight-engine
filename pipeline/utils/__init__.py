"""
pipeline/utils/ — 纯通用工具库

本包提供与业务无关的纯工具函数，可独立于流水线任何模块复用。
"""

from pipeline.utils.file_utils import (
    atomic_write,
    ensure_dir,
    get_next_sequence_number,
    get_project_root,
    list_files,
    read_json,
    write_json,
)
from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter
from pipeline.utils.id_utils import ID_LENGTH, generate_id
from pipeline.utils.text_utils import truncate_at_natural_break
from pipeline.utils.enum_utils import fuzzy_match_enum

__all__ = [
    # file_utils
    "get_project_root",
    "ensure_dir",
    "atomic_write",
    "read_json",
    "write_json",
    "list_files",
    "get_next_sequence_number",
    # id_utils
    "generate_id",
    "ID_LENGTH",
    # text_utils
    "truncate_at_natural_break",
    # enum_utils
    "fuzzy_match_enum",
    # frontmatter
    "read_frontmatter",
    "write_frontmatter",
]
