"""
pipeline/ingestion/scout/cli.py — Scout CLI 契约

提供 register_subparser / execute 供 pipeline/run.py 组装，
同时提供 main() 供 uv run python -m pipeline.ingestion.scout 独立调用。

设计理由：
    将 CLI 定义（参数声明）与执行逻辑分离到本模块，
    scout/__main__.py 仅保留 sys.path 设置并委托给 main()，
    run.py 通过 register_subparser 复用同一套参数定义。
"""

from pipeline.ingestion.scout.orchestrator import run_scout


# ---------------------------------------------------------------------------
# CLI 契约
# ---------------------------------------------------------------------------

def _add_arguments(parser):
    """注册 scout 子命令的命令行参数。"""
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新获取所有源 (忽略已存在的清单)",
    )


def register_subparser(subparsers):
    """向父解析器注册 scout 子命令及参数，设置 execute 为执行回调。"""
    parser = subparsers.add_parser(
        "scout",
        help="Stage 1a: 生成 URL 清单",
        description="遍历启用的数据源，按 fetch_strategy 抓取 RSS/API/Scrape/Browser，生成 manifest JSON",
    )
    _add_arguments(parser)
    parser.set_defaults(func=execute)


def execute(args) -> int:
    """
    执行 scout 阶段。

    参数：
        args: 已解析的 argparse Namespace，包含 force 字段

    返回：
        int: 始终返回 0（单个源失败通过 print 报告，不阻塞整体流程）
    """
    print("=== Stage 1 Scout: URL 清单生成 ===\n")
    manifests = run_scout(force=args.force)
    total = sum(len(v) for v in manifests.values())
    print(f"\n总计: {len(manifests)} 个源, {total} 篇文章")
    return 0


def main() -> int:
    """独立 CLI 入口：uv run python -m pipeline.ingestion.scout [--force]"""
    import argparse
    parser = argparse.ArgumentParser(description="Stage 1 Scout: 生成 URL 清单")
    _add_arguments(parser)
    args = parser.parse_args()
    return execute(args)
