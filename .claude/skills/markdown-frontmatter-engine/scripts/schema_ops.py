"""
Schema 扫描与字段发现模块

负责发现和解析 schema/ 目录下的字段定义文件。

约定：
  - 文件名格式：`[优先级.][字段名].md`，如 `01.title.md`、`tags.md`
  - 数字前缀决定字段输出优先级，数字越小越靠前
  - 无前缀的文件排在有前缀的文件之后，按字母顺序
  - 以 `.` 开头的文件被忽略（如 `.hidden.md`）
  - 一个 .md 文件对应一个 frontmatter 字段，文件名即字段名
"""

import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

from .types import SchemaEntry


# ============================================================================
# 文件名解析：优先级前缀提取
# ============================================================================


def parse_schema_priority(filename: str) -> Tuple[Optional[int], Optional[str]]:
    """
    从 schema 文件名中提取优先级数字和字段名。

    命名约定：
      - `01.title.md`    -> 优先级 1，字段名 "title"
      - `09.aiRelevance.md` -> 优先级 9，字段名 "aiRelevance"
      - `tags.md`        -> 无优先级（返回 None），字段名 "tags"
      - `.hidden.md`     -> 跳过（字段名为 None）

    使用 stem（不含扩展名）进行解析，避免 `.md` 扩展名干扰。

    Arguments:
        filename: schema 文件名（如 `01.title.md`）

    Returns:
        (priority, field_name)
            - priority: 数字优先级，无前缀时为 None
            - field_name: 字段名，无前缀或隐藏文件时为 None
    """
    name = Path(filename).stem

    # 隐藏文件（以 . 开头）直接跳过，不作为字段
    if name.startswith("."):
        return None, None

    # 匹配可选的数字前缀：`\d+.+`
    #   - group(1) = 数字部分
    #   - group(2) = 字段名部分
    m = re.match(r"^(\d+)\.(.+)$", name)
    if m:
        return int(m.group(1)), m.group(2)

    # 无数字前缀：优先级为 None，字段名即为整个 stem
    return None, name


# ============================================================================
# Schema 扫描：目录遍历 + 排序
# ============================================================================


def scan_schema(schema_dir: str) -> List[SchemaEntry]:
    """
    扫描 schema 目录，返回所有字段定义条目。

    扫描步骤：
      1. 遍历目录下所有 .md 文件，排除隐藏文件
      2. 从文件名解析优先级和字段名
      3. 按优先级排序（有前缀 → 无前缀 → 字母序）

    排序规则（两阶段）：
      - 阶段 1：有数字前缀的字段按优先级数字升序排列
      - 阶段 2：无前缀的字段按字母升序排列在最后

    Arguments:
        schema_dir: schema 目录的路径字符串

    Returns:
        SchemaEntry 列表，每个条目包含 name、priority、path
        priority 为 float，无前缀字段使用 float("inf") 表示无穷大

    Raises:
        SystemExit: schema_dir 目录不存在时退出

    Examples:
        目录内容：01.title.md, 03.tags.md, domain.md
        -> [
            {"name": "title",  "priority": 1,   "path": ".../01.title.md"},
            {"name": "tags",   "priority": 3,   "path": ".../03.tags.md"},
            {"name": "domain",  "priority": inf, "path": ".../domain.md"},
        ]
    """
    base_dir = Path(schema_dir).resolve()

    if not base_dir.exists():
        print(f"错误: schema 目录不存在: {base_dir}", file=sys.stderr)
        sys.exit(1)

    # 遍历所有 .md 文件，排除隐藏文件
    schema_files = [
        f for f in base_dir.glob("*.md")
        if not f.name.startswith(".")
    ]

    entries: List[SchemaEntry] = []
    for f in schema_files:
        priority, name = parse_schema_priority(f.name)
        if name is None:
            # 跳过隐藏文件（理论上已在 glob 过滤，此处为防御性检查）
            continue
        entries.append({
            "name": name,
            # 无前缀时用无穷大表示，排在最后
            "priority": priority if priority is not None else float("inf"),
            "path": str(f),
        })

    # 排序函数：
    #   - 有优先级（priority != inf）的条目：按 (False, priority, name) 排序
    #       -> (False, 1, "title") 排在 (False, 2, "tags") 前面
    #   - 无优先级（priority == inf）的条目：按 (True, name) 排序
    #       -> (True, "domain") 排在所有 (False, ...) 后面，在无优先级组内按字母序
    def sort_key(e: SchemaEntry) -> Tuple:
        p = e["priority"]
        if p == float("inf"):
            # 无前缀：字母序排在最后
            return (True, e["name"])
        return (False, p, e["name"])

    entries.sort(key=sort_key)
    return entries


def get_field_order(schema_dir: str) -> List[str]:
    """
    便捷函数：返回 schema 目录中所有字段名按优先级排序的列表。

    用于 `build_frontmatter()` 的 field_order 参数，控制输出字段顺序。

    Arguments:
        schema_dir: schema 目录路径

    Returns:
        字段名列表，如 ["title", "aliases", "tags", "domain"]
    """
    return [e["name"] for e in scan_schema(schema_dir)]
