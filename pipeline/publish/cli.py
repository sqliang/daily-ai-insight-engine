"""
pipeline/publish/cli.py — Stage 5 Publish CLI 契约

提供 register_subparser(subparsers) 供 pipeline/run.py 组装派发，
子命令 publish：把 data/ 目录中站点需要的数据 upsert 到 PostgreSQL。

用法：
    uv run python pipeline/run.py publish                     # 热数据文章 + 全部 manifest/日报
    uv run python pipeline/run.py publish --force             # 全量历史 backfill（含 archive 冷数据）
    uv run python pipeline/run.py publish --target-date 2026-08-29  # 只发指定日期
"""

import logging
import sys
from typing import Optional

logger = logging.getLogger(__name__)


def register_subparser(subparsers):
    """向父解析器注册 publish 子命令及参数，设置 execute 为执行回调。"""
    parser = subparsers.add_parser(
        "publish",
        help="Stage 5: 发布站点数据到 PostgreSQL",
        description="将 data/ 下的日报、manifest、结构化文章 upsert 到 PostgreSQL（幂等，可重复执行）",
    )
    parser.add_argument(
        "--target-date", type=str, default=None,
        help="只发布指定日期 (YYYY-MM-DD)：该 created 日期的文章 + 该日期的 manifest/日报",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="全量历史 backfill：文章扫描包含 archive 冷数据分片。"
             "默认行为已是 upsert 幂等，--force 的主要语义是覆盖冷数据",
    )
    parser.set_defaults(func=execute_publish)


def execute_publish(args) -> int:
    """
    执行 publish 阶段。

    参数：
        args: 已解析的 argparse Namespace

    返回：
        int: 0 成功, 1 失败
    """
    from datetime import date

    from .publishers import publish_all

    # 校验 --target-date 格式，尽早失败而非扫完文件后才发现
    target_date: Optional[str] = None
    if args.target_date:
        try:
            date.fromisoformat(args.target_date)
        except ValueError:
            print(f"错误: --target-date 格式无效: {args.target_date} (期望 YYYY-MM-DD)", file=sys.stderr)
            return 1
        target_date = args.target_date

    # 指定日期时历史文章可能落在 archive 冷数据中，必须一并扫描
    include_archive = args.force or target_date is not None

    try:
        logger.info("Stage 5 Publish 开始 target_date=%s force=%s", target_date, args.force)
        stats = publish_all(target_date=target_date, include_archive=include_archive)

        print("\n=== 发布完成 ===")
        print(f"  日报 (daily_reports): {stats['reports']}")
        print(f"  清单 (manifests):     {stats['manifests']}")
        print(f"  文章 (articles):      {stats['articles']}")
        return 0

    except Exception as exc:
        import traceback
        logger.error("Publish 阶段失败: %s", exc)
        logger.debug(traceback.format_exc())
        print(f"\n发布失败: {exc}")
        traceback.print_exc()
        return 1
