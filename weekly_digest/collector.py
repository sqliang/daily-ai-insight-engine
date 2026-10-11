"""
weekly_digest/collector.py — 周报数据收集

扫描 data/02_extracted/{source}/ 与 data/01_raw/{source}/ 的 Markdown frontmatter，
按 ISO 周窗口过滤、按文章 ID 去重（extracted 优先），并按降级链组装 DigestItem：
中文摘要取 tldr，未提取的文章保留英文 description 原文，由渲染层做降级展示。

设计理由：直接读本地 .md 而不是 data/04_structured JSON——后者依赖 aggregate
阶段先运行，而周报脚本要求独立可跑；01/02 目录是各阶段产物的原始落盘点。
"""

import logging
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from pipeline.utils.file_utils import get_project_root
from pipeline.utils.frontmatter import read_frontmatter

from weekly_digest.models import DigestItem, DigestStats, WeeklyDigest

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

# 信源目录名 → 周报展示名；未收录的信源回退为目录名本身
SOURCE_LABELS: Dict[str, str] = {
    "github-trending": "GitHub Trending",
    "producthunt": "Product Hunt",
}

# 英文描述在周报中的最大保留字符数：过长原文（GitHub README 全文）会淹没周报，
# 截断到摘要级别，读者可点链接查看全文
DESCRIPTION_MAX_CHARS = 300

_ISO_WEEK_RE = re.compile(r"^(\d{4})-W(\d{2})$")


# ---------------------------------------------------------------------------
# ISO 周工具
# ---------------------------------------------------------------------------

def parse_iso_week(week: str) -> Tuple[date, date]:
    """
    解析 ISO 周标识为 (周一, 周日) 日期区间。

    参数：
        week: 形如 "2026-W41" 的 ISO 周标识

    返回：
        Tuple[date, date]: (week_start, week_end)，即该周的周一与周日

    异常：
        ValueError: 格式非法或周数超出范围（01~53）时抛出
    """
    m = _ISO_WEEK_RE.match(week)
    if not m:
        raise ValueError(f"非法 ISO 周标识: {week!r}，应为形如 2026-W41 的格式")
    year, week_num = int(m.group(1)), int(m.group(2))
    try:
        start = date.fromisocalendar(year, week_num, 1)
    except ValueError as e:
        raise ValueError(f"非法 ISO 周: {week!r}（{e}）") from e
    end = date.fromisocalendar(year, week_num, 7)
    return start, end


def iso_week_of(d: date) -> str:
    """返回日期所属的 ISO 周标识（如 2026-W41）。"""
    iso = d.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def weeks_in_range(from_date: date, to_date: date) -> List[str]:
    """
    将日期区间展开为有序 ISO 周标识列表。

    周报语义以完整 ISO 周为单位，日期区间只是"选周"方式：区间内每触及
    一个 ISO 周就纳入结果。从 from_date 所属周的周一开始，每次 +7 天，
    直到周一超过 to_date。跨年无需特判——isocalendar 会正确给出
    2025-12-29 属于 2026-W01 这类边界归属。

    参数：
        from_date: 区间起始日（含）
        to_date: 区间结束日（含）

    返回：
        List[str]: 升序 ISO 周标识列表，如 ["2026-W40", "2026-W41"]

    异常：
        ValueError: from_date > to_date 时抛出
    """
    if from_date > to_date:
        raise ValueError(f"区间起点晚于终点: {from_date} > {to_date}")
    weeks: List[str] = []
    # from_date 所属周的周一
    iso = from_date.isocalendar()
    monday = date.fromisocalendar(iso.year, iso.week, 1)
    while monday <= to_date:
        weeks.append(iso_week_of(monday))
        monday += timedelta(days=7)
    return weeks


# ---------------------------------------------------------------------------
# frontmatter 字段解析
# ---------------------------------------------------------------------------

def _parse_date(value: object) -> Optional[date]:
    """
    将 frontmatter 中的日期字段解析为 date。

    yaml.safe_load 会把 ISO 日期字符串解析为 date 对象，但也可能是字符串
    或空值（GitHub Trending 的 published 常为空字符串），统一在此收敛。
    """
    if isinstance(value, date):
        return value
    if isinstance(value, str) and value.strip():
        try:
            return date.fromisoformat(value.strip()[:10])
        except ValueError:
            return None
    return None


def _truncate(text: str, limit: int) -> str:
    """将文本压成单行并截断到 limit 字符，超出部分以 … 结尾。"""
    collapsed = re.sub(r"\s+", " ", text).strip()
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[:limit].rstrip() + " …"


# ---------------------------------------------------------------------------
# 收集主流程
# ---------------------------------------------------------------------------

def _iter_source_files(data_dir: Path, source: str) -> List[Path]:
    """
    按优先级返回信源的所有 Markdown 文件：extracted 优先，raw 兜底。

    去重依赖调用方按文章 ID 先入为主，因此顺序即优先级。
    """
    files: List[Path] = []
    for stage_dir in ("02_extracted", "01_raw"):
        d = data_dir / stage_dir / source
        if d.is_dir():
            files.extend(sorted(d.glob("*.md")))
    return files


def collect_items(
    source: str,
    week_start: date,
    week_end: date,
    data_dir: Optional[Path] = None,
) -> List[DigestItem]:
    """
    收集指定信源在 ISO 周窗口内的周报条目。

    参数：
        source: 信源目录名（data/02_extracted/{source}/、data/01_raw/{source}/）
        week_start: 周起始日（周一，含）
        week_end: 周结束日（周日，含）
        data_dir: data/ 目录路径，默认取项目根目录下的 data/

    返回：
        List[DigestItem]: 周窗口内的条目，按 created 倒序、同日期按标题排序
    """
    data_dir = data_dir or (get_project_root() / "data")
    seen_ids: set[str] = set()
    items: List[DigestItem] = []

    for path in _iter_source_files(data_dir, source):
        meta, _ = read_frontmatter(path)
        if not meta:
            continue

        article_id = str(meta.get("id") or path.stem)
        if article_id in seen_ids:
            continue

        created = _parse_date(meta.get("created"))
        if created is None or not (week_start <= created <= week_end):
            continue

        seen_ids.add(article_id)

        # manifest_dates 统计本周上榜天数：同一仓库可能连续多天进入 trending 清单
        trending_days = sorted(
            {
                d
                for d in (_parse_date(v) for v in (meta.get("manifest_dates") or []))
                if d is not None and week_start <= d <= week_end
            }
        )

        description = meta.get("description") or ""
        items.append(
            DigestItem(
                article_id=article_id,
                title=str(meta.get("title") or path.stem),
                url=str(meta.get("source") or ""),
                created=created,
                published=_parse_date(meta.get("published")),
                summary_zh=(meta.get("tldr") or None),
                detail_zh=(meta.get("objective_summary") or None),
                description_en=_truncate(description, DESCRIPTION_MAX_CHARS) if description else None,
                trending_days=trending_days,
            )
        )

    # 渲染层按日期分组展示，这里先排好序：日期倒序、同日期按标题字典序。
    # 利用 Python 稳定排序：先按次关键字（标题）升序，再按主关键字（日期）倒序
    items.sort(key=lambda it: it.title.lower())
    items.sort(key=lambda it: it.created, reverse=True)
    logger.info(
        "收集完成: source=%s week=%s~%s items=%d",
        source, week_start, week_end, len(items),
    )
    return items


def build_digest(
    source: str,
    iso_week: str,
    data_dir: Optional[Path] = None,
    today: Optional[date] = None,
) -> WeeklyDigest:
    """
    构建一份完整周报（收集 + 统计）。

    参数：
        source: 信源目录名
        iso_week: ISO 周标识（如 2026-W41）
        data_dir: data/ 目录路径，默认项目根目录下的 data/
        today: 生成日期，默认取当天（测试可注入固定值）

    返回：
        WeeklyDigest: 可直接交给渲染层或序列化为 JSON
    """
    week_start, week_end = parse_iso_week(iso_week)
    items = collect_items(source, week_start, week_end, data_dir)
    stats = DigestStats(
        total=len(items),
        extracted=sum(1 for it in items if it.summary_zh),
        days_covered=len({it.created for it in items}),
    )
    return WeeklyDigest(
        source=source,
        source_label=SOURCE_LABELS.get(source, source),
        iso_week=iso_week,
        week_start=week_start,
        week_end=week_end,
        generated_at=today or date.today(),
        stats=stats,
        items=items,
    )
