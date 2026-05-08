"""
文件操作模块

负责 Markdown 笔记文件的扫描、读取和写入操作。

职责划分：
  - scan_notes   : 遍历目录，收集所有 .md 文件的摘要信息
  - read_note    : 读取单个文件的 frontmatter 和正文
  - write_frontmatter    : 向单个文件写入 frontmatter（合并模式）
  - write_multi_from_json : 从 JSON 文件批量写入多个文件

注意：本模块不包含任何 frontmatter 解析逻辑（解析逻辑在 frontmatter.py），
也不包含 schema 相关逻辑（schema 相关在 schema_ops.py）。
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

from .frontmatter import parse_frontmatter, build_frontmatter
from .types import (
    NoteInfo,
    NoteReadResult,
    WriteMultiResult,
    WriteResultItem,
)


# ============================================================================
# 扫描：遍历目录收集文件信息
# ============================================================================


def scan_notes(directory: str) -> List[NoteInfo]:
    """
    递归扫描目录下所有 Markdown 文件，返回文件摘要列表。

    扫描规则：
      - 递归遍历所有子目录（rglob）
      - 只收集 .md 文件（.mdx 等扩展名不包含）
      - 排除以 `.` 开头的隐藏文件
      - 按文件名升序排列结果

    Arguments:
        directory: 目标目录的路径字符串

    Returns:
        NoteInfo 列表，每个条目包含文件路径、文件名、是否有 frontmatter

    Raises:
        SystemExit: 目录不存在时以错误码 1 退出

    Examples:
        scan_notes("notes/") ->
        [
            {"path": "/.../notes/a.md",  "name": "a.md",  "has_frontmatter": True},
            {"path": "/.../notes/b.md",  "name": "b.md",  "has_frontmatter": False},
        ]
    """
    base_dir = Path(directory).resolve()

    if not base_dir.exists():
        print(f"错误: 目录不存在: {base_dir}", file=sys.stderr)
        sys.exit(1)

    # 递归收集 .md 文件，过滤隐藏文件
    files = [
        f for f in sorted(base_dir.rglob("*.md"))
        if not f.name.startswith(".")
    ]

    result: List[NoteInfo] = []
    for f in files:
        # 只读开头判断是否有 frontmatter，不读全文以提高速度
        content_start = f.read_bytes()[:3]
        has_fm = content_start == b"---"
        result.append({
            "path": str(f),
            "name": f.name,
            "has_frontmatter": has_fm,
        })

    return result


# ============================================================================
# 读取：解析单个文件的 frontmatter
# ============================================================================


def read_note(file_path: str) -> NoteReadResult:
    """
    读取单个 Markdown 文件，解析并返回其 frontmatter 和正文。

    Arguments:
        file_path: 目标文件的路径字符串

    Returns:
        NoteReadResult，包含文件路径、frontmatter 字典、正文内容

    Raises:
        SystemExit: 文件不存在时以错误码 1 退出
    """
    path = Path(file_path)

    if not path.exists():
        print(f"错误: 文件不存在: {path}", file=sys.stderr)
        sys.exit(1)

    content = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)

    return {
        "path": str(path),
        "frontmatter": fm,
        "body": body,
    }


# ============================================================================
# 写入：更新单个文件的 frontmatter
# ============================================================================


def write_frontmatter(
    file_path: str,
    fields: dict,
    field_order: Optional[List[str]] = None,
) -> bool:
    """
    向单个 Markdown 文件写入 frontmatter 字段。

    写入策略：
      - 先解析文件中已有的 frontmatter，保留不在本次更新范围内的历史字段
      - tags 和 aliases 使用合并模式（新值追加到历史值，去重）
      - 其他字段使用覆盖模式
      - 写回时按照 field_order 排序，扩展字段按字母顺序排在最后

    Arguments:
        file_path: 目标文件路径
        fields: 要写入的字段字典，如 {"title": "Hello", "tags": ["python"]}
        field_order: 字段输出顺序（从 schema 扫描得到），可选

    Returns:
        True: 写入成功
        False: 文件不存在（错误信息已打印到 stderr）
    """
    path = Path(file_path)

    if not path.exists():
        print(f"错误: 文件不存在: {path}", file=sys.stderr)
        return False

    # 读取文件现有内容，拆分 frontmatter 和正文
    content = path.read_text(encoding="utf-8")
    existing_fm, body = parse_frontmatter(content)

    # 组装新的 frontmatter
    # field_order 为 None 时退化为插入顺序（向后兼容旧行为）
    effective_order = field_order if field_order else list(fields.keys())
    new_fm = build_frontmatter(fields, existing_fm, effective_order)

    # 写回：frontmatter + 原正文
    new_content = new_fm + body
    path.write_text(new_content, encoding="utf-8")
    return True


# ============================================================================
# 批量写入：从 JSON 文件批量更新多个文件
# ============================================================================


def write_multi_from_json(
    directory: str,
    json_path: str,
    field_order: Optional[List[str]] = None,
) -> WriteMultiResult:
    """
    从 JSON 文件读取批量写入指令，逐个更新目录下的文件。

    JSON 格式：
        [
            {"path": "file1.md",  "title": "标题1", "tags": ["python"]},
            {"path": "sub/file2.md", "title": "标题2"}
        ]
        - path: 相对于 directory 的相对路径
        - 其他键: 要写入的 frontmatter 字段

    错误处理：
      - JSON 文件不存在 → 直接 sys.exit(1)
      - 文件路径不存在 → 标记为 "not_found"，继续处理其他文件
      - 写入失败 → 标记为 "failed"，继续处理其他文件

    Arguments:
        directory: 笔记目录的根路径
        json_path: 包含批量指令的 JSON 文件路径
        field_order: 字段输出顺序（从 schema 扫描得到），可选

    Returns:
        WriteMultiResult，包含处理总数和每条记录的详细结果
    """
    base_dir = Path(directory).resolve()
    json_file = Path(json_path)

    if not json_file.exists():
        print(f"错误: JSON 文件不存在: {json_file}", file=sys.stderr)
        sys.exit(1)

    with json_file.open(encoding="utf-8") as f:
        updates = json.load(f)

    results: List[WriteResultItem] = []
    for item in updates:
        # JSON 中的 path 是相对于 directory 的相对路径
        file_path = base_dir / item["path"]

        if not file_path.exists():
            results.append({"path": str(file_path), "status": "not_found"})
            continue

        # 从 JSON 条目中提取出 path 键，其余都是 frontmatter 字段
        fields = {k: v for k, v in item.items() if k != "path"}
        success = write_frontmatter(str(file_path), fields, field_order)
        results.append({
            "path": str(file_path),
            "status": "ok" if success else "failed",
        })

    return {"total": len(results), "results": results}
