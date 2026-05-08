#!/usr/bin/env python3
"""
Markdown Frontmatter Engine — CLI 入口

职责边界（单一入口原则）：
  - 只做参数解析与命令分发，不含任何业务逻辑
  - 所有业务逻辑委托给子模块（frontmatter / schema_ops / file_ops / env_config）
  - 子模块保持独立可导入，外部脚本可直接 from scripts import scan_notes ...

新增字段时：只需在 schema/ 下新建 .md 文件，本文件无需任何改动。

Usage:
    python3 scripts/batch_ops.py scan <directory> [--json]
    python3 scripts/batch_ops.py read <file_path>
    python3 scripts/batch_ops.py write <file_path> [--json <json>] [--fields X,Y]
    python3 scripts/batch_ops.py write-multi <dir> <json_path> [--fields X,Y]
    python3 scripts/batch_ops.py schema <schema_dir> [--list] [--fields X,Y]
    python3 scripts/batch_ops.py env-fields <skill_root>

字段过滤（--fields）：
    指定要处理的字段子集，系统会验证字段名是否在 schema 目录中注册。
    不支持的字段会警告并被忽略，不指定时自动从 .env 读取 SCHEMA_FIELDS 配置
    （从 --schema-dir 路径反推 skill_root），无配置时处理全量字段。
"""

# ── 子模块导入 ────────────────────────────────────────────────────────────────
# 导入策略（同时支持两种运行方式）：
#   1. python -m scripts.batch_ops  （作为包内模块运行，推荐）
#   2. python scripts/batch_ops.py  （直接运行）
#
# 直接运行时 Python 不自动将 skill 根目录加入 sys.path，导致找不到 scripts 包。
# 通过 __file__ 推算出 skill 根目录，追加到 sys.path，保证导入正常。
import os
import sys

if __name__ == "__main__":
    # batch_ops.py 位于 scripts/batch_ops.py，其父目录的父目录即 skill 根目录
    _skill_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _skill_root not in sys.path:
        sys.path.insert(0, _skill_root)

# 导入子模块（scripts/ 已加入 sys.path 后可被找到）
from scripts import (
    scan_notes,
    read_note,
    write_frontmatter,
    write_multi_from_json,
    scan_schema,
    get_field_order,
    load_env_fields,
)

import argparse
import json
from typing import List, Optional


# ============================================================================
# 辅助：CLI 级别的字段过滤验证
# ============================================================================
# 这只是 CLI 层的输入验证，真正传给 AI 的字段限制通过 write/write-multi 的
# 行为体现：只将用户在 --fields 中指定的字段写入，其他字段忽略。
# 若用户指定的字段不在 schema 中注册，会打印警告后自动忽略。


def _resolve_requested_fields(
    fields_arg: Optional[str],
    schema_dir: Optional[str],
) -> Optional[List[str]]:
    """
    解析 --fields 参数，返回经过验证的字段名列表。

    规则：
      - 未指定 --fields 且未在 .env 中配置 → 返回 None（全量）
      - 未指定 --fields 但 .env 中有 SCHEMA_FIELDS → 使用 .env 配置
      - 指定了但 schema_dir 未提供 → 返回指定字段（不验证）
      - 指定了且 schema_dir 有效 → 验证字段是否在 schema 中注册，
        不存在的字段打印警告后从列表中移除

    Returns:
        None       → 全量模式
        []         → 无有效字段（已打印错误）
        list[str]  → 已验证的字段名列表
    """
    if fields_arg:
        requested = [f.strip() for f in fields_arg.split(",") if f.strip()]
    else:
        # --fields 未指定：从 .env 自动读取（从 schema_dir 反推 skill_root）
        if schema_dir:
            skill_root = os.path.dirname(os.path.abspath(schema_dir.rstrip("/\\")))
            env_fields = load_env_fields(skill_root)
            if env_fields is not None:
                requested = sorted(env_fields)
            else:
                return None  # .env 无配置，走全量
        else:
            return None  # 无 --fields 且无 schema_dir，走全量

    if not requested:
        print("警告: --fields 参数为空，将处理全量字段", file=sys.stderr)
        return None

    if not schema_dir:
        return requested

    schema_entries = scan_schema(schema_dir)
    available = {e["name"] for e in schema_entries}

    unknown = sorted(set(requested) - available)
    if unknown:
        print(
            f"警告: 以下字段不在 schema 目录中，将被忽略: {', '.join(unknown)}",
            file=sys.stderr,
        )

    valid = [f for f in requested if f in available]
    if not valid:
        print("错误: 没有找到任何有效的字段", file=sys.stderr)
        return []

    return valid


# ============================================================================
# 命令处理器
# ============================================================================


def _handle_scan(args: argparse.Namespace) -> None:
    """scan 命令：扫描目录下所有 .md 文件"""
    files = scan_notes(args.directory)
    if args.json:
        print(json.dumps(files, ensure_ascii=False, indent=2))
    else:
        print(f"找到 {len(files)} 个文件:")
        for f in files:
            marker = "[FM]" if f["has_frontmatter"] else "[  ]"
            print(f"  {marker} {f['path']}")


def _handle_read(args: argparse.Namespace) -> None:
    """read 命令：读取单文件 frontmatter + 正文预览"""
    result = read_note(args.file_path)
    print(f"文件: {result['path']}")
    print(f"\nFrontmatter: {json.dumps(result['frontmatter'], ensure_ascii=False, indent=2)}")
    print(f"\n正文（前 20 行）:")
    lines = result["body"].split("\n")[:20]
    print("\n".join(lines))


def _handle_write(args: argparse.Namespace) -> None:
    """write 命令：写入单文件 frontmatter"""
    # ── 解析字段输入 ─────────────────────────────────────────────────────────
    if args.json_value:
        try:
            fields = json.loads(args.json_value)
            if not isinstance(fields, dict):
                print("错误: --json 值必须是一个 JSON 对象", file=sys.stderr)
                sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"错误: JSON 解析失败: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.field and args.value:
        fields = {args.field: args.value}
    else:
        print("错误: 请提供 --json 参数或 (field value) 位置参数", file=sys.stderr)
        sys.exit(1)

    # ── 字段过滤验证 ─────────────────────────────────────────────────────────
    requested = _resolve_requested_fields(args.fields, args.schema_dir)
    if requested is not None and requested == []:
        return  # 错误已打印

    # 只写入用户在 --fields 中指定的字段（忽略其他字段）
    if requested is not None:
        fields = {k: v for k, v in fields.items() if k in requested}

    # ── 字段顺序 ─────────────────────────────────────────────────────────────
    field_order = None
    if args.schema_dir:
        try:
            field_order = get_field_order(args.schema_dir)
            if requested is not None:
                field_order = [f for f in field_order if f in requested]
        except SystemExit:
            field_order = None

    success = write_frontmatter(args.file_path, fields, field_order)
    if success:
        print(f"已写入: {args.file_path}")


def _handle_write_multi(args: argparse.Namespace) -> None:
    """write-multi 命令：从 JSON 批量写入多个文件"""
    requested = _resolve_requested_fields(args.fields, args.schema_dir)
    if requested is not None and requested == []:
        return

    field_order = None
    if args.schema_dir:
        try:
            field_order = get_field_order(args.schema_dir)
            if requested is not None:
                field_order = [f for f in field_order if f in requested]
        except SystemExit:
            field_order = None

    result = write_multi_from_json(args.directory, args.json_path, field_order)
    print(f"处理完成: {result['total']} 个文件")
    for r in result["results"]:
        print(f"  [{r['status']}] {r['path']}")

    failed = [r for r in result["results"] if r["status"] != "ok"]
    if failed:
        sys.exit(1)


def _handle_schema(args: argparse.Namespace) -> None:
    """schema 命令：扫描并列出字段定义"""
    fields = scan_schema(args.schema_dir)

    if args.list:
        for f in fields:
            p = f["priority"] if f["priority"] != float("inf") else "∞"
            print(f"  [{p}] {f['name']}")
        return

    if args.fields:
        requested = {name.strip() for name in args.fields.split(",") if name.strip()}
        available = {f["name"] for f in fields}
        unknown = requested - available
        if unknown:
            print(
                f"警告: 以下字段不在 schema 目录中: {', '.join(sorted(unknown))}",
                file=sys.stderr,
            )
        filtered = [f for f in fields if f["name"] in requested]
        if not filtered:
            print("错误: 没有找到任何匹配的字段", file=sys.stderr)
            sys.exit(1)
        print(f"找到 {len(filtered)} 个匹配字段:")
        for f in filtered:
            p = f["priority"] if f["priority"] != float("inf") else "∞"
            print(f"  [{p}] {f['name']}: {f['path']}")
        return

    print(f"找到 {len(fields)} 个字段:")
    for f in fields:
        p = f["priority"] if f["priority"] != float("inf") else "∞"
        print(f"  [{p}] {f['name']}: {f['path']}")


def _handle_env_fields(args: argparse.Namespace) -> None:
    """env-fields 命令：读取 .env 中的 SCHEMA_FIELDS 配置"""
    fields = load_env_fields(args.skill_root)
    if fields is None:
        print("(全量)")
    else:
        print(",".join(sorted(fields)))


# ============================================================================
# 主入口：参数解析 + 命令分发
# ============================================================================


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Markdown frontmatter 文件读写工具（模块化版本）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # scan
    p = sub.add_parser("scan", help="扫描目录下的 .md 文件")
    p.add_argument("directory")
    p.add_argument(
        "--json", action="store_true",
        help="输出机器可读的 JSON 格式（推荐用于 AI 解析）",
    )

    # read
    sub.add_parser("read", help="读取笔记内容和 frontmatter").add_argument("file_path")

    # write
    w = sub.add_parser("write", help="写入 frontmatter（支持单字段或多字段 JSON）")
    w.add_argument("file_path")
    w.add_argument(
        "--json", dest="json_value", action="store", default=None,
        help='JSON 对象，如 \'{"title": "xxx", "domain": "Tech"}\'',
    )
    w.add_argument("field", nargs="?", default=None)
    w.add_argument("value", nargs="?", default=None)
    w.add_argument(
        "--schema-dir", dest="schema_dir", default=None,
        help="schema 目录路径（用于确定字段输出顺序）",
    )
    w.add_argument(
        "--fields", dest="fields", default=None,
        help="逗号分隔的字段名，只处理这些字段，如: --fields title,tags,domain",
    )

    # write-multi
    m = sub.add_parser("write-multi", help="批量写入（从 JSON 文件）")
    m.add_argument("directory")
    m.add_argument("json_path")
    m.add_argument(
        "--schema-dir", dest="schema_dir", default=None,
        help="schema 目录路径（用于确定字段输出顺序）",
    )
    m.add_argument(
        "--fields", dest="fields", default=None,
        help="逗号分隔的字段名，只处理这些字段，如: --fields title,tags",
    )

    # schema
    s = sub.add_parser("schema", help="扫描 schema 目录获取字段定义")
    s.add_argument("schema_dir")
    s.add_argument(
        "--list", action="store_true",
        help="轻量枚举，只输出 [优先级] 字段名，不读文件内容",
    )
    s.add_argument(
        "--fields", dest="fields", default=None,
        help="逗号分隔的字段名，只返回匹配的条目",
    )

    # env-fields
    sub.add_parser("env-fields", help="读取 .env 中的 SCHEMA_FIELDS 配置").add_argument(
        "skill_root", help="skill 根目录路径",
    )

    args = parser.parse_args()

    handlers = {
        "scan": _handle_scan,
        "read": _handle_read,
        "write": _handle_write,
        "write-multi": _handle_write_multi,
        "schema": _handle_schema,
        "env-fields": _handle_env_fields,
    }
    handlers[args.command](args)


if __name__ == "__main__":
    main()
