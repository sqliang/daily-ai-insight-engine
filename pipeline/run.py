#!/usr/bin/env python3
"""
pipeline/run.py — Daily AI Insight Engine 管道入口

初始化阶段自动完成：
1. 加载 .env 环境变量（通过 python-dotenv）
2. 加载 config/proxy.json 并注入代理环境变量

子命令（日常五步，aggregate 在 extract/analyze 后自动执行）：
    uv run python pipeline/run.py scout              Stage 1a: 生成 URL 清单
    uv run python pipeline/run.py ingest             Stage 1b: 正文抓取与清洗
    uv run python pipeline/run.py extract            Stage 2: 元信息与事实提取 (自动 aggregate)
    uv run python pipeline/run.py analyze            Stage 3: 深度分析 (自动 aggregate)
    uv run python pipeline/run.py aggregate          Stage 4a: Frontmatter 聚合 (独立运行，用于配置变更)
    uv run python pipeline/run.py synthesize         Stage 4b: 日报合成 (成功后自动 publish)
    uv run python pipeline/run.py publish            Stage 5: 发布站点数据到 PostgreSQL

修复子命令（自动发现并修复失败文章）：
    uv run python pipeline/run.py repair             Stage 1c: 自动修复 ingest 失败的文章
    uv run python pipeline/run.py extract-repair     Stage 2c: 自动修复 extract 失败的文章
"""

import argparse
import logging
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 项目路径定位
# ---------------------------------------------------------------------------
# run.py 位于 pipeline/ 子目录下，项目根目录在上一级
_PROJECT_ROOT = Path(__file__).parent.parent

# 将项目根目录加入 sys.path，使 pipeline 可被作为模块导入
# 这样无论从哪个目录运行 uv run python pipeline/run.py 都能正确导入 pipeline.xxx 模块
_sys_path_root = str(_PROJECT_ROOT)
if _sys_path_root not in sys.path:
    sys.path.insert(0, _sys_path_root)

# ---------------------------------------------------------------------------
# 1. 加载 .env 环境变量（最早执行）
# ---------------------------------------------------------------------------
# 将 .env 文件中的配置注入到 os.environ，后续代码可通过 os.environ 读取
# 相当于 Node.js 中的 import 'dotenv/config'
try:
    from dotenv import load_dotenv

    _env_path = _PROJECT_ROOT / ".env"
    if _env_path.exists():
        load_dotenv(_env_path)
        print("✅ .env 已加载")
    else:
        print("⚠️  未找到 .env 文件，将使用系统环境变量", file=sys.stderr)
except ImportError:
    print("⚠️  python-dotenv 未安装，无法加载 .env (uv pip install python-dotenv)", file=sys.stderr)


# ---------------------------------------------------------------------------
# 2. 代理初始化（在 .env 加载之后，任何网络请求之前）
# ---------------------------------------------------------------------------
from pipeline.core.proxy_utils import setup_proxy as _setup_proxy

_setup_proxy()

# ---------------------------------------------------------------------------
# schedule-status 子命令 — 查看定时任务最近运行状态
# ---------------------------------------------------------------------------
# 不单独创建 CLI 模块文件，因为逻辑很简单：读 JSON → 格式化输出（约 30 行）。
# ---------------------------------------------------------------------------


def _execute_schedule_status(args) -> int:
    """
    读取 data/scheduled/last_run.json 并以人类可读格式输出定时任务状态。

    参数：
        args: 未使用（保持与其他 execute 函数签名一致）

    返回：
        int: 0 成功读取，1 状态文件不存在
    """
    import json
    from datetime import datetime, time

    status_path = _PROJECT_ROOT / "data" / "scheduled" / "last_run.json"

    if not status_path.exists():
        print("⚠️  尚未运行过定时任务（没有历史状态记录）")
        print(f"   期待的状态文件: {status_path}")
        print()
        print("   请先手动执行一次测试：")
        print(f"     ./pipeline/scheduled/daily_fetch.sh")
        print()
        print("   或安装定时任务后等待每天 17:30 自动执行：")
        print(f"     ./pipeline/scheduled/setup.sh")
        return 1

    with open(status_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    timestamp = data.get("timestamp", "未知")
    status = data.get("status", "未知")
    scout = data.get("scout", {})
    ingest = data.get("ingest", {})
    log_files = data.get("log_files", {})

    # 状态映射为可读 emoji
    status_display = {
        "success": "✅ 成功",
        "partial": "⚠️ 部分失败",
        "failed": "❌ 失败",
    }.get(status, f"❓ {status}")

    print()
    print("=" * 50)
    print("  定时任务最近运行状态")
    print("=" * 50)
    print(f"  运行时间: {timestamp}")
    print(f"  状态:     {status_display}")
    print()
    print("  Scout 阶段:")
    print(f"    扫描数据源: {scout.get('sources_scanned', 0)} 个")
    print(f"    发现文章:   {scout.get('articles_found', 0)} 篇")

    failed_sources = scout.get("failed_sources", [])
    if failed_sources:
        print(f"    失败源:     {', '.join(failed_sources)}")
    else:
        print(f"    失败源:     无")

    scout_errors = scout.get("errors", [])
    if scout_errors:
        print(f"    错误信息:")
        for e in scout_errors:
            print(f"      - {e}")

    print()
    print("  Ingest 阶段:")
    print(f"    总计:   {ingest.get('total', 0)} 篇")
    print(f"    成功:   {ingest.get('success', 0)} 篇")
    print(f"    部分:   {ingest.get('partial', 0)} 篇")
    print(f"    失败:   {ingest.get('failed', 0)} 篇")
    print(f"    跳过:   {ingest.get('skipped', 0)} 篇（历史去重）")

    ingest_errors = ingest.get("errors", [])
    if ingest_errors:
        print(f"    错误信息:")
        for e in ingest_errors:
            print(f"      - {e}")

    repair = data.get("repair", {})
    if repair:
        print()
        print("  Repair 阶段:")
        print(f"    发现:   {repair.get('total', 0)} 篇")
        print(f"    修复:   {repair.get('repaired', 0)} 篇")
        if repair.get("still_failed", 0) > 0:
            print(f"    仍失败: {repair.get('still_failed', 0)} 篇")

    extract_repair = data.get("extract_repair", {})
    if extract_repair:
        print()
        print("  Extract-Repair 阶段:")
        print(f"    发现:   {extract_repair.get('total', 0)} 篇")
        print(f"    修复:   {extract_repair.get('repaired', 0)} 篇")
        if extract_repair.get("still_failed", 0) > 0:
            print(f"    仍失败: {extract_repair.get('still_failed', 0)} 篇")

    print()
    print("  日志文件:")
    if log_files.get("scout"):
        print(f"    scout:  {log_files['scout']}")
    if log_files.get("ingest"):
        print(f"    ingest: {log_files['ingest']}")
    if log_files.get("repair"):
        print(f"    repair: {log_files['repair']}")
    if log_files.get("extract_repair"):
        print(f"    extract-repair: {log_files['extract_repair']}")

    # 计算下一次执行时间（每天 17:30）
    now = datetime.now()
    next_run = now.replace(hour=17, minute=30, second=0, microsecond=0)
    if now >= next_run:
        # 今天的 17:30 已过，下一次是明天
        from datetime import timedelta
        next_run = next_run + timedelta(days=1)
    print()
    print(f"  下一次执行: {next_run.strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)
    print()

    return 0


def _execute_repair(args) -> int:
    """
    执行 repair 阶段：扫描今天 failed/partial 的文章并用 browser 重试修复。
    """
    from pipeline.ingestion.repair import repair_failed_articles

    result = repair_failed_articles()
    print(f"\n=== 修复完成 ===")
    print(f"  发现: {result['total']} 篇")
    print(f"  修复: {result['repaired']} 篇")
    print(f"  仍失败: {result['still_failed']} 篇")
    if result["repaired_files"]:
        print(f"  已修复文件:")
        for f in result["repaired_files"]:
            print(f"    - {f}")
    return 0


def _register_repair(subparsers):
    """注册 repair 子命令：自动修复 ingest 失败的文章。"""
    parser = subparsers.add_parser(
        "repair",
        help="Stage 1c: 自动修复 ingest 失败的文章",
        description="扫描 data/01_raw/ 中今天 extraction_status=failed/partial 的文章，用 browser 重试抓取",
    )
    parser.set_defaults(func=_execute_repair)


def _execute_extract_repair(args) -> int:
    """
    执行 extract-repair 阶段：扫描今天 extract_result=failed 的文章并重试修复。
    """
    from datetime import date
    from pipeline.extraction.repair import repair_failed_extractions

    target_date = None
    if hasattr(args, "target_date") and args.target_date:
        target_date = date.fromisoformat(args.target_date)

    result = repair_failed_extractions(target_date=target_date)
    print(f"\n=== Extract-Repair 完成 ===")
    print(f"  发现: {result['total']} 篇")
    print(f"  修复: {result['repaired']} 篇")
    print(f"  仍失败: {result['still_failed']} 篇")
    if result["repaired_files"]:
        print(f"  已修复文件:")
        for f in result["repaired_files"]:
            print(f"    - {f}")
    return 0


def _register_extract_repair(subparsers):
    """注册 extract-repair 子命令：自动修复 extract 失败的文章。"""
    parser = subparsers.add_parser(
        "extract-repair",
        help="Stage 2c: 自动修复 extract 失败的文章",
        description="扫描 data/02_extracted/ 中今天 extract_result=failed 的文章，重新执行 LLM 提取",
    )
    parser.add_argument(
        "--target-date", "-d", type=str, default=None,
        help="只修复指定日期的文章 (格式: YYYY-MM-DD，默认: 今天)",
    )
    parser.set_defaults(func=_execute_extract_repair)


def _register_schedule_status(subparsers):
    """注册 schedule-status 子命令：查看定时任务最近运行状态。"""
    parser = subparsers.add_parser(
        "schedule-status",
        help="查看定时任务最近运行状态",
        description="读取 data/scheduled/last_run.json，以人类可读格式展示最近一次 scout + ingest 的执行结果。",
    )
    parser.set_defaults(func=_execute_schedule_status)


# ---------------------------------------------------------------------------
# 子命令注册与派发
# ---------------------------------------------------------------------------
# 每个子命令通过其模块的 register_subparser 自行注册参数并设置 execute 回调。
# run.py 只负责组装和派发，不感知任何子命令的具体参数或执行逻辑。
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Daily AI Insight Engine — AI 资讯处理流水线",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
日常五步（aggregate 在 extract/analyze 后自动执行）:
  uv run python pipeline/run.py scout                       Stage 1a: URL 清单生成
  uv run python pipeline/run.py ingest                      Stage 1b: 正文抓取
  uv run python pipeline/run.py extract                     Stage 2: 事实提取 → 自动 aggregate
  uv run python pipeline/run.py analyze                     Stage 3: 深度分析 → 自动 aggregate
  uv run python pipeline/run.py synthesize                  Stage 4b: 日报合成

独立 aggregate（配置变更时使用）:
  uv run python pipeline/run.py aggregate                   Stage 4a: 聚合 frontmatter
  uv run python pipeline/run.py aggregate --lookback-days 7  修改日报窗口
  uv run python pipeline/run.py aggregate --hot-days 14      修改热数据窗口
  uv run python pipeline/run.py aggregate --target-date 2026-06-10  精确日期回溯
  uv run python pipeline/run.py synthesize --dry-run        Stage 4b: 显示 prompt 预估
  uv run python pipeline/run.py synthesize --target-date 2026-06-10  回溯历史日报

发布到 PostgreSQL（synthesize 成功后自动执行）:
  uv run python pipeline/run.py publish                     Stage 5: 发布站点数据（热数据）
  uv run python pipeline/run.py publish --force             全量历史 backfill（含 archive 冷数据）
  uv run python pipeline/run.py publish --target-date 2026-06-10  只发指定日期
        """,
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="详细日志输出（终端显示 DEBUG 级别，日志文件始终记录 DEBUG）",
    )
    subparsers = parser.add_subparsers(dest="command", help="流水线阶段")

    # 各模块注册自己的子命令（参数定义 + 执行回调）
    from pipeline.ingestion.scout.cli import register_subparser as _reg_scout
    from pipeline.ingestion.ingest.cli import register_subparser as _reg_ingest
    from pipeline.ingestion.backfill_ids.cli import register_subparser as _reg_backfill
    from pipeline.extraction.cli import register_subparser as _reg_extract
    from pipeline.analysis.cli import register_subparser as _reg_analyze
    from pipeline.synthesis.cli import register_aggregate_subparser as _reg_aggregate
    from pipeline.synthesis.cli import register_synthesize_subparser as _reg_synthesize
    from pipeline.publish.cli import register_subparser as _reg_publish

    _reg_scout(subparsers)
    _reg_ingest(subparsers)
    _reg_backfill(subparsers)
    _reg_extract(subparsers)
    _reg_analyze(subparsers)
    _reg_aggregate(subparsers)
    _reg_synthesize(subparsers)
    _reg_publish(subparsers)
    _register_repair(subparsers)  # 自动修复 ingest 失败的文章
    _register_extract_repair(subparsers)  # 自动修复 extract 失败的文章
    _register_schedule_status(subparsers)  # 定时任务状态查询（在 run.py 内定义）

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # --- 统一日志初始化 ---
    # 在 dispatch 前一次性配置日志系统，后续各模块的 logger = logging.getLogger(__name__)
    # 无需改动即可自动获得终端 + 文件双输出
    from pipeline.core.logging_config import init_logging

    init_logging(stage=args.command, verbose=args.verbose)

    # --- 未捕获异常兜底 ---
    # Python 默认的 traceback 输出绕过 logging 体系，直接写 stderr。
    # 安装 sys.excepthook 确保未捕获异常也被写入日志文件，便于事后回溯。
    _original_excepthook = sys.excepthook

    def _logging_excepthook(exc_type, exc_value, exc_tb):
        import traceback
        tb_str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        logging.getLogger("pipeline").critical(
            "未捕获异常: %s\n%s", exc_value, tb_str.rstrip()
        )
        _original_excepthook(exc_type, exc_value, exc_tb)

    sys.excepthook = _logging_excepthook

    # 每个 register_subparser 通过 set_defaults(func=execute) 设置了执行回调
    sys.exit(args.func(args))
