"""
pipeline/extraction/cli.py — Stage 2 Extraction CLI 契约

提供 register_subparser / execute 供 pipeline/run.py 组装，
同时提供 main() 供 uv run python pipeline/extraction/cli.py 独立调用。

设计理由：
    将 CLI 定义与编排逻辑（run_extraction.py）分离到不同文件。
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Optional

from ..core.file_utils import get_project_root


# ---------------------------------------------------------------------------
# CLI 契约
# ---------------------------------------------------------------------------

def _add_arguments(parser):
    """注册 extract 子命令的命令行参数。"""
    parser.add_argument(
        "--input", "-i", type=str, default=None,
        help="输入 .md 文件或目录路径 (默认: data/01_raw/)",
    )
    parser.add_argument(
        "--concurrency", "-c", type=int, default=None,
        help="并发 Agent 调用数 (默认: 从 config.yaml 读取，5)",
    )
    parser.add_argument(
        "--stage",
        choices=["base_info", "fact_extraction", "all"],
        default="all",
        help="只运行指定子阶段 (默认: all)",
    )
    parser.add_argument(
        "--skip-existing", action="store_true", default=True,
        help="跳过已提取的文件 (默认: 启用)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="强制重新提取所有字段 (忽略 skip-existing)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="只列出将处理的文件，不实际调用 LLM",
    )
    parser.add_argument(
        "--model", "-m", type=str, default=None,
        help="LLM 模型名称 (默认: 从 config.yaml 读取)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="详细日志输出",
    )


def register_subparser(subparsers):
    """向父解析器注册 extract 子命令及参数，设置 execute 为执行回调。"""
    parser = subparsers.add_parser(
        "extract",
        help="Stage 2: 元信息与事实提取",
        description="从 data/01_raw/ 读取 Markdown 文件，提取 BaseInfo 和 FactExtraction，写入 data/02_extracted/",
    )
    _add_arguments(parser)
    parser.set_defaults(func=execute)


def execute(args) -> int:
    """
    执行 extract 阶段。

    参数：
        args: 已解析的 argparse Namespace

    返回：
        int: 0 成功, 1 失败
    """
    # 配置日志
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # 解析输入路径
    input_path: Optional[Path] = None
    if args.input:
        input_path = Path(args.input)
        if not input_path.is_absolute():
            input_path = get_project_root() / input_path

    try:
        from .run_extraction import run_extraction

        asyncio.run(
            run_extraction(
                input_path=input_path,
                concurrency=args.concurrency,
                stages=args.stage,
                skip_existing=args.skip_existing,
                force=args.force,
                dry_run=args.dry_run,
                model=args.model,
            )
        )
        return 0
    except FileNotFoundError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\n中断", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"错误: {exc}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def main(argv: Optional[list[str]] = None) -> int:
    """
    Stage 2 Extraction 独立 CLI 入口。

    参数：
        argv: 命令行参数列表（None 时使用 sys.argv[1:]）

    返回：
        0 成功, 1 失败
    """
    import argparse
    parser = argparse.ArgumentParser(description="Stage 2 Extract: 元信息与事实提取")
    _add_arguments(parser)
    args = parser.parse_args(argv)
    return execute(args)


if __name__ == "__main__":
    sys.exit(main())
