"""
pipeline/ingestion/backfill_ids/cli.py — ID 回填工具 CLI 契约

为 data/01_raw/ 下已有的 .md 文件补充 article.id (SHA-256 of source URL)。
这些文件在 ingest 阶段尚未引入 id 概念时生成，通过此模块批量回填。

提供 register_subparser / execute 供 run.py 组装，同时提供 main() 供独立调用。

设计理由：
    本模块较小（~130 行），execute 即为核心实现，无需额外 orchestrator 文件。
    关键在于 register_subparser 位于 cli.py，遵循与其他模块一致的包结构。
"""

import sys
from pathlib import Path

from pipeline.core.config_loader import resolve_data_dir
from pipeline.utils.file_utils import get_project_root
from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter
from pipeline.utils.id_utils import generate_id


# ---------------------------------------------------------------------------
# CLI 契约
# ---------------------------------------------------------------------------

def _add_arguments(parser):
    """注册 backfill-ids 子命令的命令行参数。"""
    parser.add_argument(
        "--input", "-i",
        type=str,
        default=None,
        help="输入 .md 文件或目录路径 (默认: data/01_raw/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只列出将处理的文件，不实际写入",
    )


def register_subparser(subparsers):
    """向父解析器注册 backfill-ids 子命令及参数。"""
    parser = subparsers.add_parser(
        "backfill-ids",
        help="为已有 .md 文件补充 article.id",
        description="遍历 data/01_raw/ 下的 Markdown 文件，根据 source URL 生成 SHA-256 id 并写入 frontmatter",
    )
    _add_arguments(parser)
    parser.set_defaults(func=execute)


def execute(args) -> int:
    """
    执行 ID 回填。

    参数：
        args: 已解析的 argparse Namespace，包含 input / dry_run 字段

    返回：
        int: 0 成功, 1 存在错误
    """
    project_root = get_project_root()

    # 解析输入路径
    if args.input:
        input_path = Path(args.input)
        if not input_path.is_absolute():
            input_path = project_root / input_path
    else:
        input_path = resolve_data_dir("raw")

    # 发现文件
    if input_path.is_file():
        files = [input_path]
    else:
        files = sorted(input_path.rglob("*.md"))

    total = len(files)
    updated = 0
    skipped = 0
    errors = 0

    print(f"\n=== ID 回填 (backfill-ids) ===")
    print(f"发现 {total} 个 .md 文件")
    if args.dry_run:
        print(">>> DRY RUN 模式，不会实际写入 <<<")

    for fp in files:
        try:
            fm, body = read_frontmatter(fp)

            # 已有 id 则跳过
            if fm.get("id"):
                skipped += 1
                continue

            source_url = fm.get("source", "")
            if not source_url:
                print(f"  [跳过] {fp}: 缺少 source URL")
                skipped += 1
                continue

            article_id = generate_id(source_url)
            if not article_id:
                errors += 1
                continue

            if not args.dry_run:
                fm["id"] = article_id
                write_frontmatter(fp, fm, body)

            updated += 1
            if total <= 20 or updated % 50 == 0:
                print(f"  [{updated}/{total}] {fp.name} → id={article_id}")

        except Exception as exc:
            errors += 1
            print(f"  [错误] {fp}: {exc}")

    print(f"\n=== 完成: 更新 {updated} 个, 跳过 {skipped} 个, 错误 {errors} 个 ===")

    return 1 if errors else 0


def main() -> int:
    """独立 CLI 入口：uv run python pipeline/backfill_ids.py [--input ...] [--dry-run]"""
    import argparse
    parser = argparse.ArgumentParser(description="ID 回填工具")
    _add_arguments(parser)
    args = parser.parse_args()
    return execute(args)


if __name__ == "__main__":
    sys.exit(main())
