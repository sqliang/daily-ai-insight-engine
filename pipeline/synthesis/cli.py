"""
pipeline/synthesis/cli.py — Stage 4 Synthesis CLI 契约

统一管理 aggregate (Stage 4a) 和 synthesize (Stage 4b) 两个子命令的 CLI 契约。
提供 register_*_subparser / execute_* 供 pipeline/run.py 组装，
同时提供 main() 供 uv run python -m pipeline.synthesis 独立调用。

设计理由：
    两个子命令共享同一个 synthesis 包，统一在 cli.py 中管理 CLI 定义，
    避免在两个业务逻辑文件中重复 argparse 声明。
"""

import logging
import sys
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)



# ===========================================================================
# Stage 4a: Aggregate
# ===========================================================================

def _add_aggregate_arguments(parser):
    """注册 aggregate 子命令的命令行参数。"""
    parser.add_argument(
        "--input", "-i", type=str, default=None,
        help="输入目录 (默认: 自动扫描 data/03_analyzed/ + data/02_extracted/ + data/01_raw/，按最完整版本去重)",
    )
    parser.add_argument(
        "--output", "-o", type=str, default=None,
        help="输出目录 (默认: data/04_structured/)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="仅列出文件，不实际写入",
    )
    parser.add_argument(
        "--lookback-days", type=int, default=None,
        help="all_articles.json 日报窗口 (天)。默认从 config.yaml 读取, 1。0 = 不限",
    )
    parser.add_argument(
        "--target-date", type=str, default=None,
        help="精确日期过滤 (YYYY-MM-DD)。仅保留 created == 指定日期的文章到 all_articles.json。"
             "与 --lookback-days 互斥。用于回溯历史日报。",
    )
    parser.add_argument(
        "--hot-days", type=int, default=None,
        help="per-source JSON 热数据窗口 (天)。默认从 config.yaml 读取, 7",
    )
    parser.add_argument(
        "--max-history-days", type=int, default=None,
        help="archive 分片最大保留天数 (天)。默认从 config.yaml 读取, 365。0 = 不限",
    )


def register_aggregate_subparser(subparsers):
    """向父解析器注册 aggregate 子命令及参数，设置 execute 为执行回调。"""
    parser = subparsers.add_parser(
        "aggregate",
        help="Stage 4a: 提取 Frontmatter 并聚合为结构化 JSON",
        description="扫描 data/01_raw/ + data/02_extracted/ + data/03_analyzed/，按 ID 去重保留最完整版本，提取 frontmatter 输出 JSON",
    )
    _add_aggregate_arguments(parser)
    parser.set_defaults(func=execute_aggregate)


def execute_aggregate(args) -> int:
    """
    执行 aggregate 阶段。

    参数：
        args: 已解析的 argparse Namespace

    返回：
        int: 0 成功, 1 失败
    """
    from datetime import date
    from ..aggregation.aggregate_frontmatter import aggregate_frontmatter

    input_dir = Path(args.input) if args.input else None
    output_dir = Path(args.output) if args.output else None

    # 解析 --target-date（与 --lookback-days 互斥）
    target_date: Optional[date] = None
    if args.target_date:
        if args.lookback_days is not None:
            print("错误: --target-date 和 --lookback-days 不能同时指定", file=sys.stderr)
            return 1
        try:
            target_date = date.fromisoformat(args.target_date)
        except ValueError:
            print(f"错误: --target-date 格式无效: {args.target_date} (期望 YYYY-MM-DD)", file=sys.stderr)
            return 1

    try:
        logger.info("Stage 4a Aggregate 开始 input=%s output=%s dry_run=%s target_date=%s",
                     input_dir, output_dir, args.dry_run, target_date)
        result = aggregate_frontmatter(
            input_dir=input_dir,
            output_dir=output_dir,
            dry_run=args.dry_run,
            lookback_days=args.lookback_days,
            hot_days=args.hot_days,
            max_history_days=args.max_history_days,
            target_date=target_date,
        )

        if args.dry_run:
            logger.info("Stage 4a Aggregate dry-run 完成")
            return 0

        print(f"\n=== 聚合完成 ===")
        print(f"  总文章数: {result['total_articles']}")
        for source, count in result["sources"].items():
            print(f"    {source}: {count}")
        if result["errors"]:
            print(f"  跳过/错误: {result['errors']}")
        logger.info("Stage 4a Aggregate 完成 articles=%d sources=%d errors=%d",
                     result["total_articles"], len(result["sources"]), result["errors"])
        return 0

    except Exception as exc:
        import traceback
        logger.error("Aggregate 阶段失败: %s", exc)
        logger.debug(traceback.format_exc())
        print(f"\n聚合失败: {exc}")
        traceback.print_exc()
        return 1


# ===========================================================================
# Stage 4b: Synthesize
# ===========================================================================

def _add_synthesize_arguments(parser):
    """注册 synthesize 子命令的命令行参数。"""
    parser.add_argument(
        "--input", "-i", type=str, default=None,
        help="all_articles.json 路径 (默认: data/04_structured/all_articles.json)",
    )
    parser.add_argument(
        "--output", "-o", type=str, default=None,
        help="输出目录 (默认: data/05_reports/)",
    )
    parser.add_argument(
        "--model", "-m", type=str, default=None,
        help="LLM 模型名称 (默认: claude-opus-4-7)",
    )
    parser.add_argument(
        "--max-detail", type=int, default=30,
        help="完整展示的文章数 (默认: 30)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="仅显示 prompt 预估，不调用 LLM",
    )
    parser.add_argument(
        "--lookback-days", type=int, default=None,
        help="先按 N 天窗口重新聚合，再合成日报 (默认: 跳过，使用已有 all_articles.json)。0 = 不限",
    )
    parser.add_argument(
        "--target-date", type=str, default=None,
        help="精确日期过滤 (YYYY-MM-DD)。先按指定日期重新聚合 all_articles.json，再合成日报。"
             "与 --lookback-days 互斥。用于回溯历史日报。",
    )


def register_synthesize_subparser(subparsers):
    """向父解析器注册 synthesize 子命令及参数，设置 execute 为执行回调。"""
    parser = subparsers.add_parser(
        "synthesize",
        help="Stage 4b: Editor-in-Chief 日报合成",
        description="读取聚合后的结构化 JSON，调用 Claude Opus 生成完整日报（JSON + Markdown）",
    )
    _add_synthesize_arguments(parser)
    parser.set_defaults(func=execute_synthesize)


def execute_synthesize(args) -> int:
    """
    执行 synthesize 阶段。

    参数：
        args: 已解析的 argparse Namespace

    返回：
        int: 0 成功, 1 失败
    """
    from datetime import date
    from .run_synthesis import synthesize_report
    from ..aggregation.aggregate_frontmatter import aggregate_frontmatter

    input_path = Path(args.input) if args.input else None
    output_dir = Path(args.output) if args.output else None

    # 解析 --target-date（与 --lookback-days 互斥）
    target_date: Optional[date] = None
    if args.target_date:
        if args.lookback_days is not None:
            print("错误: --target-date 和 --lookback-days 不能同时指定", file=sys.stderr)
            return 1
        try:
            target_date = date.fromisoformat(args.target_date)
        except ValueError:
            print(f"错误: --target-date 格式无效: {args.target_date} (期望 YYYY-MM-DD)", file=sys.stderr)
            return 1

    try:
        # 如果指定了 --target-date，先按目标日期重新聚合（精确匹配模式）
        if target_date is not None:
            logger.info("预聚合: target_date=%s", target_date)
            aggregate_frontmatter(
                input_dir=None,
                output_dir=None,
                dry_run=False,
                target_date=target_date,
            )
        # 如果指定了 --lookback-days，先重新聚合以过滤文章
        elif args.lookback_days is not None:
            logger.info("预聚合: lookback_days=%s", args.lookback_days)
            aggregate_frontmatter(
                input_dir=None,
                output_dir=None,
                dry_run=False,
                lookback_days=args.lookback_days,
            )

        logger.info("Stage 4b Synthesize 开始 model=%s max_detail=%s dry_run=%s target_date=%s",
                     args.model, args.max_detail, args.dry_run, target_date)
        synthesize_report(
            input_path=input_path,
            output_dir=output_dir,
            model=args.model,
            max_detail=args.max_detail,
            dry_run=args.dry_run,
            target_date=args.target_date,
        )
        logger.info("Stage 4b Synthesize 完成")
        return 0
    except Exception as exc:
        import traceback
        print(f"\n合成失败: {exc}")
        traceback.print_exc()
        logger.error("Stage 4b Synthesize 失败: %s", exc)
        return 1


# ===========================================================================
# 独立 CLI 入口 (uv run python -m pipeline.synthesis)
# ===========================================================================

def main(argv: Optional[list[str]] = None) -> int:
    """
    Synthesis 独立 CLI 入口：uv run python -m pipeline.synthesis <aggregate|synthesize> [...]

    通过 argparse 子命令机制自动派发到 execute_aggregate 或 execute_synthesize。
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Stage 4: Synthesis — Frontmatter 聚合 + Editor-in-Chief 日报合成",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  uv run python -m pipeline.synthesis aggregate                 Stage 4a: 聚合 frontmatter
  uv run python -m pipeline.synthesis aggregate --dry-run       Stage 4a: 仅列出文件
  uv run python -m pipeline.synthesis synthesize                Stage 4b: 日报合成
  uv run python -m pipeline.synthesis synthesize --dry-run      Stage 4b: 显示 prompt 预估
        """,
    )
    subparsers = parser.add_subparsers(dest="command", help="合成阶段")

    register_aggregate_subparser(subparsers)
    register_synthesize_subparser(subparsers)

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
