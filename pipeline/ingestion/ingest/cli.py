"""
pipeline/ingestion/ingest/cli.py — Ingest CLI 契约

提供 register_subparser / execute 供 pipeline/run.py 组装，
同时提供 main() 供 python -m pipeline.ingestion.ingest 独立调用。

设计理由：
    将 CLI 定义（参数声明）与业务逻辑（orchestrator.py）分离。
"""

from pipeline.ingestion.ingest.orchestrator import run_ingest


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
        args: 已解析的 argparse Namespace，包含 manifest / force 字段

    返回：
        int: 始终返回 0
    """
    print("=== Stage 1 Ingest: 正文抓取与 Markdown 生成 ===\n")
    files = run_ingest(manifest_name=args.manifest, force=args.force)
    print(f"\n处理完成: {len(files)} 个文件")
    return 0


def main() -> int:
    """独立 CLI 入口：python pipeline/ingestion/ingest.py [--manifest ...] [--force]"""
    import argparse
    parser = argparse.ArgumentParser(description="Stage 1 Ingest: 正文抓取")
    _add_arguments(parser)
    args = parser.parse_args()
    return execute(args)
