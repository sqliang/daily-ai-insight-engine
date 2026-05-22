#!/usr/bin/env python3
"""
pipeline/run.py — Daily AI Insight Engine 管道入口

初始化阶段自动完成：
1. 加载 .env 环境变量（通过 python-dotenv）
2. 加载 config/proxy.json 并注入代理环境变量

子命令：
    uv run python pipeline/run.py scout          Stage 1a: 生成 URL 清单
    uv run python pipeline/run.py ingest         Stage 1b: 正文抓取与清洗
    uv run python pipeline/run.py extract        Stage 2: 元信息与事实提取
    uv run python pipeline/run.py analyze        Stage 3: 深度分析
    uv run python pipeline/run.py aggregate      Stage 4a: Frontmatter 聚合
    uv run python pipeline/run.py synthesize     Stage 4b: 日报合成
"""

import argparse
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
# 子命令注册与派发
# ---------------------------------------------------------------------------
# 每个子命令通过其模块的 register_subparser 自行注册参数并设置 execute 回调。
# run.py 只负责组装和派发，不感知任何子命令的具体参数或执行逻辑。
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Daily AI Insight Engine — 四阶段 AI 资讯处理流水线",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  uv run python pipeline/run.py scout                       Stage 1a: URL 清单生成
  uv run python pipeline/run.py ingest                      Stage 1b: 正文抓取
  uv run python pipeline/run.py extract                     Stage 2: 事实提取
  uv run python pipeline/run.py analyze                     Stage 3: 深度分析
  uv run python pipeline/run.py aggregate                   Stage 4a: 聚合 frontmatter
  uv run python pipeline/run.py synthesize                  Stage 4b: 日报合成
  uv run python pipeline/run.py synthesize --dry-run        Stage 4b: 显示 prompt 预估
        """,
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

    _reg_scout(subparsers)
    _reg_ingest(subparsers)
    _reg_backfill(subparsers)
    _reg_extract(subparsers)
    _reg_analyze(subparsers)
    _reg_aggregate(subparsers)
    _reg_synthesize(subparsers)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # 每个 register_subparser 通过 set_defaults(func=execute) 设置了执行回调
    sys.exit(args.func(args))
