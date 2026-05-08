#!/usr/bin/env python3
"""
pipeline/run.py — Daily AI Insight Engine 管道入口

初始化阶段自动完成：
1. 加载 .env 环境变量（通过 python-dotenv）
2. 加载 config/proxy.json 并注入代理环境变量

子命令：
    python pipeline/run.py backfill-ids  为已有文件补充 article.id
    python pipeline/run.py extract        Stage 2: 元信息与事实提取
    (将来可扩展 scout、ingest 等子命令)
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 项目路径定位
# ---------------------------------------------------------------------------
# run.py 位于 pipeline/ 子目录下，项目根目录在上一级
_PROJECT_ROOT = Path(__file__).parent.parent

# 将项目根目录加入 sys.path，使 pipeline 可被作为模块导入
# 这样无论从哪个目录运行 python pipeline/run.py 都能正确导入 pipeline.xxx 模块
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
    print("⚠️  python-dotenv 未安装，无法加载 .env (pip install python-dotenv)", file=sys.stderr)


# ---------------------------------------------------------------------------
# 2. 代理初始化（在 .env 加载之后，任何网络请求之前）
# ---------------------------------------------------------------------------
# 从 config/proxy.json 读取代理配置并注入到 os.environ
# 后续 curl / subprocess / requests / httpx 等自动走代理
_PROXY_CONFIG_PATH = Path(__file__).parent / "config" / "proxy.json"


def _load_proxy_config() -> dict:
    """从 proxy.json 读取代理配置，文件不存在或格式错误时返回空字典"""
    if not _PROXY_CONFIG_PATH.exists():
        return {}

    try:
        with open(_PROXY_CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "proxy" in data:
            return data["proxy"]
        if isinstance(data, dict) and ("http" in data or "https" in data):
            return data

        return {}
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️  代理配置文件解析失败: {e}", file=sys.stderr)
        return {}


def setup_proxy() -> None:
    """从 proxy.json 加载代理配置并注入到环境变量"""
    proxy = _load_proxy_config()

    if not proxy:
        print("⚠️  未找到代理配置，将尝试直连网络", file=sys.stderr)
        return

    if "http" in proxy:
        os.environ["http_proxy"] = proxy["http"]
        os.environ["HTTP_PROXY"] = proxy["http"]

    if "https" in proxy:
        os.environ["https_proxy"] = proxy["https"]
        os.environ["HTTPS_PROXY"] = proxy["https"]

    if "all" in proxy:
        os.environ["all_proxy"] = proxy["all"]
        os.environ["ALL_PROXY"] = proxy["all"]

    display = proxy.get("https") or proxy.get("http") or proxy.get("all", "")
    print(f"✅ 代理已配置: {display}")


setup_proxy()

# ---------------------------------------------------------------------------
# 业务代码入口
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Daily AI Insight Engine — 四阶段 AI 资讯处理流水线",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python pipeline/run.py aggregate                  聚合 frontmatter (Stage 4a)
  python pipeline/run.py synthesize                 日报合成 (Stage 4b)
  python pipeline/run.py synthesize --dry-run       显示 prompt 预估
  python pipeline/run.py extract                    处理所有文件 (Stage 2)
  python pipeline/run.py analyze                    深度分析所有文件 (Stage 3)
  python pipeline/run.py analyze --stage qualitative 只运行定性研判
  python pipeline/run.py analyze --concurrency 2    限制并发文件数
        """,
    )
    subparsers = parser.add_subparsers(dest="command", help="流水线阶段")

    # ------- backfill-ids 子命令 -------
    # 为 data/01_raw/ 下已有的 .md 文件补充 article.id (SHA-256 of source URL)
    # 这些文件在 ingest 阶段尚未引入 id 概念，需要通过此命令批量回填
    backfill_parser = subparsers.add_parser(
        "backfill-ids",
        help="为已有 .md 文件补充 article.id",
        description="遍历 data/01_raw/ 下的 Markdown 文件，根据 source URL 生成 SHA-256 id 并写入 frontmatter",
    )
    backfill_parser.add_argument(
        "--input", "-i",
        type=str,
        default=None,
        help="输入 .md 文件或目录路径 (默认: data/01_raw/)",
    )
    backfill_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只列出将处理的文件，不实际写入",
    )

    # ------- extract 子命令 -------
    extract_parser = subparsers.add_parser(
        "extract",
        help="Stage 2: 元信息与事实提取",
        description="从 data/01_raw/ 读取 Markdown 文件，提取 BaseInfo 和 FactExtraction，写入 data/02_extracted/",
    )
    extract_parser.add_argument(
        "--input", "-i",
        type=str,
        default=None,
        help="输入 .md 文件或目录路径 (默认: data/01_raw/)",
    )
    extract_parser.add_argument(
        "--concurrency", "-c",
        type=int,
        default=None,
        help="并发 Agent 调用数 (默认: 从 config.yaml 读取，5)",
    )
    extract_parser.add_argument(
        "--stage",
        choices=["base_info", "fact_extraction", "all"],
        default="all",
        help="只运行指定子阶段 (默认: all)",
    )
    extract_parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="跳过已提取的文件 (默认: 启用)",
    )
    extract_parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新提取所有字段 (忽略 skip-existing)",
    )
    extract_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只列出将处理的文件，不实际调用 LLM",
    )
    extract_parser.add_argument(
        "--model", "-m",
        type=str,
        default=None,
        help="LLM 模型名称 (默认: 从 config.yaml 读取)",
    )
    extract_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="显示详细日志",
    )

    # ------- analyze 子命令 -------
    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Stage 3: 深度分析（定性研判 + 价值评估 + 前瞻预测）",
        description="从 data/02_extracted/ 读取 Markdown 文件，执行 3 维度深度分析，写入 data/03_analyzed/",
    )
    analyze_parser.add_argument(
        "--input", "-i",
        type=str,
        default=None,
        help="输入 .md 文件或目录路径 (默认: data/02_extracted/)",
    )
    analyze_parser.add_argument(
        "--concurrency", "-c",
        type=int,
        default=None,
        help="并发文件处理数 (默认: 从 config.yaml 读取，3)",
    )
    analyze_parser.add_argument(
        "--stage",
        choices=["qualitative", "value", "foresight", "all"],
        default="all",
        help="只运行指定评估维度 (默认: all)",
    )
    analyze_parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="跳过已分析的文件 (默认: 启用)",
    )
    analyze_parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新分析 (忽略 skip-existing)",
    )
    analyze_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只列出将处理的文件，不实际调用 LLM",
    )
    analyze_parser.add_argument(
        "--model", "-m",
        type=str,
        default=None,
        help="LLM 模型名称 (默认: 从 config.yaml 读取)",
    )
    analyze_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="显示详细日志",
    )

    # ------- aggregate 子命令 (Stage 4a) -------
    aggregate_parser = subparsers.add_parser(
        "aggregate",
        help="Stage 4a: 提取 Frontmatter 并聚合为结构化 JSON",
        description="递归扫描 data/03_analyzed/ 下所有 .md 文件，提取 YAML frontmatter，按数据源分组输出 JSON",
    )
    aggregate_parser.add_argument(
        "--input", "-i", type=str, default=None,
        help="输入目录 (默认: data/03_analyzed/)",
    )
    aggregate_parser.add_argument(
        "--output", "-o", type=str, default=None,
        help="输出目录 (默认: data/04_structured/)",
    )
    aggregate_parser.add_argument(
        "--dry-run", action="store_true",
        help="仅列出文件，不实际写入",
    )

    # ------- synthesize 子命令 (Stage 4b) -------
    synthesize_parser = subparsers.add_parser(
        "synthesize",
        help="Stage 4b: Editor-in-Chief 日报合成",
        description="读取聚合后的结构化 JSON，调用 Claude Opus 生成完整日报（JSON + Markdown）",
    )
    synthesize_parser.add_argument(
        "--input", "-i", type=str, default=None,
        help="all_articles.json 路径 (默认: data/04_structured/all_articles.json)",
    )
    synthesize_parser.add_argument(
        "--output", "-o", type=str, default=None,
        help="输出目录 (默认: data/05_reports/)",
    )
    synthesize_parser.add_argument(
        "--model", "-m", type=str, default=None,
        help="LLM 模型名称 (默认: claude-opus-4-7)",
    )
    synthesize_parser.add_argument(
        "--max-detail", type=int, default=30,
        help="完整展示的文章数 (默认: 30)",
    )
    synthesize_parser.add_argument(
        "--dry-run", action="store_true",
        help="仅显示 prompt 预估，不调用 LLM",
    )
    synthesize_parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="显示详细日志",
    )

    args = parser.parse_args()

    # 如果没有任何子命令，打印帮助
    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # 分发到对应子命令
    if args.command == "backfill-ids":
        from pipeline.core.id_utils import generate_id
        from pipeline.core.frontmatter_utils import read_frontmatter, write_frontmatter
        from pipeline.core.file_utils import get_project_root

        # 解析输入路径
        if args.input:
            input_path = Path(args.input)
            if not input_path.is_absolute():
                input_path = _PROJECT_ROOT / input_path
        else:
            input_path = _PROJECT_ROOT / "data" / "01_raw"

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

        if errors:
            sys.exit(1)
        sys.exit(0)

    elif args.command == "aggregate":
        from pipeline.synthesis.aggregate_frontmatter import main as aggregate_main

        aggregate_argv = []
        if args.input:
            aggregate_argv.extend(["--input", args.input])
        if args.output:
            aggregate_argv.extend(["--output", args.output])
        if args.dry_run:
            aggregate_argv.append("--dry-run")

        sys.exit(aggregate_main(aggregate_argv))

    elif args.command == "synthesize":
        from pipeline.synthesis.run_synthesis import main as synthesize_main

        synthesize_argv = []
        if args.input:
            synthesize_argv.extend(["--input", args.input])
        if args.output:
            synthesize_argv.extend(["--output", args.output])
        if args.model:
            synthesize_argv.extend(["--model", args.model])
        if args.max_detail != 30:
            synthesize_argv.extend(["--max-detail", str(args.max_detail)])
        if args.dry_run:
            synthesize_argv.append("--dry-run")
        if args.verbose:
            synthesize_argv.append("--verbose")

        sys.exit(synthesize_main(synthesize_argv))

    elif args.command == "extract":
        # 导入并执行 extraction 模块
        from pipeline.extraction.run_extraction import main as extract_main

        # 将 argparse namespace 转换为 argv 列表传递给 extract_main
        extract_argv = []
        if args.input:
            extract_argv.extend(["--input", args.input])
        if args.concurrency is not None:
            extract_argv.extend(["--concurrency", str(args.concurrency)])
        if args.stage != "all":
            extract_argv.extend(["--stage", args.stage])
        if args.force:
            extract_argv.append("--force")
        if args.dry_run:
            extract_argv.append("--dry-run")
        if args.model:
            extract_argv.extend(["--model", args.model])
        if args.verbose:
            extract_argv.append("--verbose")
        # skip-existing 默认 True，只有在 force 时才需要禁用
        if args.force:
            pass  # --force 暗示不跳过
        else:
            extract_argv.append("--skip-existing")

        sys.exit(extract_main(extract_argv))

    elif args.command == "analyze":
        from pipeline.analysis.run_analysis import main as analyze_main

        analyze_argv = []
        if args.input:
            analyze_argv.extend(["--input", args.input])
        if args.concurrency is not None:
            analyze_argv.extend(["--concurrency", str(args.concurrency)])
        if args.stage != "all":
            analyze_argv.extend(["--stage", args.stage])
        if args.force:
            analyze_argv.append("--force")
        if args.dry_run:
            analyze_argv.append("--dry-run")
        if args.model:
            analyze_argv.extend(["--model", args.model])
        if args.verbose:
            analyze_argv.append("--verbose")
        if not args.force:
            analyze_argv.append("--skip-existing")

        sys.exit(analyze_main(analyze_argv))
