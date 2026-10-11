#!/usr/bin/env python3
"""
weekly_digest/run.py — 周报生成 CLI 入口

按 ISO 自然周汇总 data/ 下的信源文章，生成中英文对照 Markdown 周报 +
同名 JSON（WeeklyDigest 序列化，预留给未来 web 站点）到 weekly_reports/。
纯本地模板拼接，零 LLM 调用。

周报是 data/ 的纯函数：每次运行全量重生成当周文件（幂等覆盖），
重复运行不丢数据，且已补跑 extract 的文章会自动从英文降级升级为中文摘要。
写文件前会与上次生成的 JSON 对比，输出"新增/升级"变更告知。

用法：
    uv run python weekly_digest/run.py                              # 两个默认信源 × 本 ISO 周
    uv run python weekly_digest/run.py --week last                  # 上一 ISO 周
    uv run python weekly_digest/run.py --week 2026-W40              # 指定历史周
    uv run python weekly_digest/run.py --from 2026-10-01 --to 2026-10-12  # 跨周区间（逐周各生成一份）
    uv run python weekly_digest/run.py --source github-trending     # 只跑单源
    uv run python weekly_digest/run.py --output-dir /tmp/x          # 覆盖输出目录
"""

import argparse
import json
import logging
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import List, Optional

# ---------------------------------------------------------------------------
# 项目路径定位
# ---------------------------------------------------------------------------
# run.py 位于 weekly_digest/ 子目录下，项目根目录在上一级；
# 加入 sys.path 以便导入 pipeline.utils 与 weekly_digest 包（与 pipeline/run.py 同模式）
_PROJECT_ROOT = Path(__file__).parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from pipeline.utils.file_utils import atomic_write, ensure_dir  # noqa: E402

from weekly_digest.collector import (  # noqa: E402
    build_digest,
    iso_week_of,
    parse_iso_week,
    weeks_in_range,
)
from weekly_digest.models import WeeklyDigest  # noqa: E402
from weekly_digest.render import render_markdown  # noqa: E402

logger = logging.getLogger("weekly_digest")

# 默认生成周报的信源（collector 本身接受任意信源目录名，日后扩展只需加到这里）
DEFAULT_SOURCES = ["github-trending", "producthunt"]

# --week 参数的特殊别名：current（当前周，缺省）/ last（上一 ISO 周）。
# 设计理由：skill 中的 LLM 不擅长心算 ISO 周数，"上周"这个高频意图走确定性代码路径
WEEK_ALIASES = ("current", "last")


# ---------------------------------------------------------------------------
# 周参数解析
# ---------------------------------------------------------------------------

def resolve_week(week_arg: Optional[str], today: Optional[date] = None) -> str:
    """
    将 --week 参数解析为 ISO 周标识。

    参数：
        week_arg: None / "current" / "last" / "2026-W41" 形式的标识
        today: 基准日期，默认当天（测试可注入固定值）

    返回：
        str: ISO 周标识（如 2026-W41）

    异常：
        ValueError: 非法周标识时抛出（由 parse_iso_week 校验）
    """
    today = today or date.today()
    if week_arg in (None, "current"):
        return iso_week_of(today)
    if week_arg == "last":
        return iso_week_of(today - timedelta(days=7))
    parse_iso_week(week_arg)  # 提前校验格式，非法输入立即报错
    return week_arg


# ---------------------------------------------------------------------------
# 变更告知
# ---------------------------------------------------------------------------

def diff_digest(old: WeeklyDigest, new: WeeklyDigest) -> str:
    """
    对比新旧两份周报，生成一行变更说明。

    对比口径：文章 ID 集合差（新增/移除）+ 交集内 summary_zh 从缺失变
    非缺失的"升级为中文摘要"条数。
    """
    old_by_id = {it.article_id: it for it in old.items}
    new_by_id = {it.article_id: it for it in new.items}

    added = len(new_by_id.keys() - old_by_id.keys())
    removed = len(old_by_id.keys() - new_by_id.keys())
    upgraded = sum(
        1
        for aid in new_by_id.keys() & old_by_id.keys()
        if not old_by_id[aid].summary_zh and new_by_id[aid].summary_zh
    )

    parts: List[str] = []
    parts.append(f"新增 {added} 条" if added else "新增 0 条")
    if upgraded:
        parts.append(f"{upgraded} 条升级为中文摘要")
    if removed:
        parts.append(f"移除 {removed} 条")
    return "较上次：" + "，".join(parts)


# ---------------------------------------------------------------------------
# 输出
# ---------------------------------------------------------------------------

def write_digest(digest: WeeklyDigest, output_dir: Path) -> tuple[Path, Path, str]:
    """
    将周报写入输出目录：Markdown + JSON 各一份，文件名即 ISO 周标识。
    写前若同名 JSON 已存在，对比生成变更告知；JSON 损坏时降级为"首次生成"，不阻塞主流程。

    返回：
        tuple[Path, Path, str]: (md 路径, json 路径, 变更告知文本)
    """
    source_dir = ensure_dir(output_dir / digest.source)
    md_path = source_dir / f"{digest.iso_week}.md"
    json_path = source_dir / f"{digest.iso_week}.json"

    change_note = "首次生成"
    if json_path.exists():
        try:
            old = WeeklyDigest.model_validate(json.loads(json_path.read_text(encoding="utf-8")))
            change_note = diff_digest(old, digest)
        except (json.JSONDecodeError, ValueError) as e:
            logger.warning("旧 JSON 无法解析，按首次生成处理: %s (%s)", json_path, e)

    atomic_write(md_path, render_markdown(digest))
    atomic_write(json_path, digest.model_dump_json(indent=2))
    return md_path, json_path, change_note


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_day(value: str) -> date:
    """argparse type：解析 YYYY-MM-DD 日期，非法时报参数错误。"""
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"非法日期: {value!r}，应为 YYYY-MM-DD 格式")


def main(argv: Optional[List[str]] = None) -> int:
    """解析命令行参数，逐周 × 逐信源生成周报。"""
    parser = argparse.ArgumentParser(
        description="按 ISO 自然周生成信源周报（Markdown + JSON）",
    )
    # --week 与 --from/--to 互斥：单周语义与区间语义不能混用
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--week",
        default=None,
        help="ISO 周标识（如 2026-W41），或别名 current（默认）/ last（上一周）",
    )
    group.add_argument("--from", dest="from_date", type=_parse_day, default=None,
                       help="区间起始日 YYYY-MM-DD（需与 --to 成对，按 ISO 周展开逐周生成）")
    parser.add_argument("--to", dest="to_date", type=_parse_day, default=None,
                        help="区间结束日 YYYY-MM-DD（需与 --from 成对）")
    parser.add_argument(
        "--source",
        default="all",
        help="信源目录名，或 all（默认，跑全部默认信源）",
    )
    parser.add_argument(
        "--output-dir",
        default=str(_PROJECT_ROOT / "weekly_reports"),
        help="输出目录，默认项目根目录下的 weekly_reports/",
    )
    args = parser.parse_args(argv)

    if (args.from_date is None) != (args.to_date is None):
        parser.error("--from 与 --to 必须成对出现")

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    # 解析出本次要生成的 ISO 周列表：单周 1 个，区间展开为多个
    if args.from_date is not None:
        try:
            weeks = weeks_in_range(args.from_date, args.to_date)
        except ValueError as e:
            parser.error(str(e))
    else:
        try:
            weeks = [resolve_week(args.week)]
        except ValueError as e:
            parser.error(str(e))

    sources = DEFAULT_SOURCES if args.source == "all" else [args.source]
    output_dir = Path(args.output_dir)

    logger.info("生成周报: weeks=%s sources=%s", weeks, sources)
    for iso_week in weeks:
        week_start, week_end = parse_iso_week(iso_week)
        logger.info("--- %s (%s ~ %s) ---", iso_week, week_start, week_end)
        for source in sources:
            digest = build_digest(source, iso_week)
            md_path, json_path, change_note = write_digest(digest, output_dir)
            logger.info(
                "%s: 收录 %d 条（中文摘要 %d 条）→ %s",
                source, digest.stats.total, digest.stats.extracted, md_path,
            )
            print(
                f"[{source}] {iso_week}: 收录 {digest.stats.total} 条"
                f"（中文摘要 {digest.stats.extracted}）· {change_note}"
            )
            print(f"  Markdown → {md_path}")
            print(f"  JSON     → {json_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
