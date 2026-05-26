"""
pipeline/analysis/cli.py — Stage 3 Analysis CLI 契约

提供 register_subparser / execute 供 pipeline/run.py 组装，
同时提供 main() 供独立调用。

设计理由：
    将 CLI 定义与编排逻辑（run_analysis.py）分离到不同文件。
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)



# ---------------------------------------------------------------------------
# CLI 契约
# ---------------------------------------------------------------------------

def _add_arguments(parser):
    """注册 analyze 子命令的命令行参数。"""
    parser.add_argument(
        "--input", "-i", type=str, default=None,
        help="输入 .md 文件或目录路径 (默认: data/02_extracted/)",
    )
    parser.add_argument(
        "--concurrency", "-c", type=int, default=None,
        help="并发文件处理数 (默认: 从 config.yaml 读取，3)",
    )
    parser.add_argument(
        "--stage",
        choices=["qualitative", "value", "foresight", "all"],
        default="all",
        help="只运行指定评估维度 (默认: all)",
    )
    parser.add_argument(
        "--skip-existing", action="store_true", default=True,
        help="跳过已分析的文件 (默认: 启用)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="强制重新分析 (忽略 skip-existing)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="只列出将处理的文件，不实际调用 LLM",
    )
    parser.add_argument(
        "--model", "-m", type=str, default=None,
        help="LLM 模型名称 (默认: 从 config.yaml 读取)",
    )


def register_subparser(subparsers):
    """向父解析器注册 analyze 子命令及参数，设置 execute 为执行回调。"""
    parser = subparsers.add_parser(
        "analyze",
        help="Stage 3: 深度分析（定性研判 + 价值评估 + 前瞻预测）",
        description="从 data/02_extracted/ 读取 Markdown 文件，执行 3 维度深度分析，写入 data/03_analyzed/",
    )
    _add_arguments(parser)
    parser.set_defaults(func=execute)


def execute(args) -> int:
    """
    执行 analyze 阶段。

    参数：
        args: 已解析的 argparse Namespace

    返回：
        int: 0 成功, 1 存在失败, 130 被中断
    """
    input_path = None
    if args.input:
        input_path = Path(args.input).resolve()

    try:
        from .run_analysis import run_analysis

        results = asyncio.run(run_analysis(
            input_path=input_path,
            concurrency=args.concurrency,
            stages=args.stage,
            skip_existing=args.skip_existing and not args.force,
            force=args.force,
            dry_run=args.dry_run,
            model=args.model,
        ))

        from ..core.agent import StageResult
        failed = [r for r in results if isinstance(r, StageResult) and not r.success]
        if failed:
            return 1
        return 0

    except KeyboardInterrupt:
        logger.info("用户中断 (KeyboardInterrupt)")
        print("\n操作已取消", file=sys.stderr)
        return 130
    except Exception as exc:
        import traceback
        logger.error("Analysis 阶段失败: %s", exc)
        logger.debug(traceback.format_exc())
        print(f"\n分析失败: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1


def main(argv: Optional[list[str]] = None) -> int:
    """
    Stage 3 深度分析独立 CLI 入口。

    参数：
        argv: 命令行参数列表，None 时使用 sys.argv[1:]

    返回：
        退出码（0 成功，1 失败）
    """
    import argparse
    parser = argparse.ArgumentParser(
        description="Stage 3: 深度分析——从 data/02_extracted/ 读取，写入 data/03_analyzed/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  uv run python pipeline/run.py analyze                    处理所有文件
  uv run python pipeline/run.py analyze --input data/02_extracted/arxiv/01.md
  uv run python pipeline/run.py analyze --stage qualitative  只运行定性研判
  uv run python pipeline/run.py analyze --dry-run           列出将处理的文件
  uv run python pipeline/run.py analyze --concurrency 2     限制并发文件数
  uv run python pipeline/run.py analyze --force             强制重新分析
        """,
    )
    _add_arguments(parser)
    args = parser.parse_args(argv)
    return execute(args)


if __name__ == "__main__":
    sys.exit(main())
