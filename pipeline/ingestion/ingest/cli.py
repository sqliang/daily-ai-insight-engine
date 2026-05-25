"""
pipeline/ingestion/ingest/cli.py — Ingest CLI 契约

提供 register_subparser / execute 供 pipeline/run.py 组装，
同时提供 main() 供 uv run python -m pipeline.ingestion.ingest 独立调用。

设计理由：
    将 CLI 定义（参数声明）与业务逻辑（orchestrator.py）分离。
"""

import logging

from pipeline.ingestion.ingest.orchestrator import run_ingest

logger = logging.getLogger(__name__)



# ---------------------------------------------------------------------------
# CLI 契约
# ---------------------------------------------------------------------------

def _add_arguments(parser):
    """注册 ingest 子命令的命令行参数。"""
    parser.add_argument(
        "--manifest", "-m",
        type=str,
        default=None,
        help="指定清单文件名 (不含路径，默认处理最新清单)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新抓取，忽略去重状态",
    )
    parser.add_argument(
        "--concurrency", "-c",
        type=int,
        default=None,
        help="并发抓取线程数 (默认: 从 config.yaml 读取，否则 5)",
    )


def register_subparser(subparsers):
    """向父解析器注册 ingest 子命令及参数，设置 execute 为执行回调。"""
    parser = subparsers.add_parser(
        "ingest",
        help="Stage 1b: 正文抓取与清洗",
        description="读取 manifest 清单，逐篇下载 HTML、提取 Markdown 正文、截断处理、写入 .md 文件",
    )
    _add_arguments(parser)
    parser.set_defaults(func=execute)


def execute(args) -> int:
    """
    执行 ingest 阶段。

    参数：
        args: 已解析的 argparse Namespace，包含 manifest / force / concurrency 字段

    返回：
        int: 始终返回 0
    """
    # 解析并发数：CLI 参数 > config.yaml > 默认 5
    concurrency = args.concurrency
    if concurrency is None:
        from pipeline.core.config_loader import get_stage_config
        stage_config = get_stage_config("ingest")
        concurrency = stage_config.get("concurrency", 5)
    concurrency = max(1, concurrency)

    logger.info("Stage 1 Ingest 开始 manifest=%s force=%s concurrency=%d",
                args.manifest, args.force, concurrency)
    print(f"=== Stage 1 Ingest: 正文抓取与 Markdown 生成 (并发: {concurrency}) ===\n")
    files = run_ingest(
        manifest_name=args.manifest,
        force=args.force,
        concurrency=concurrency,
    )
    print(f"\n处理完成: {len(files)} 个文件")
    logger.info("Stage 1 Ingest 完成 files=%d", len(files))
    return 0


def main() -> int:
    """独立 CLI 入口：uv run python pipeline/ingestion/ingest.py [--manifest ...] [--force] [--concurrency ...]"""
    import argparse
    parser = argparse.ArgumentParser(description="Stage 1 Ingest: 正文抓取")
    _add_arguments(parser)
    args = parser.parse_args()
    return execute(args)
