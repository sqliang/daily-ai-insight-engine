"""
tests/test_weekly_digest.py — 周报生成器单元测试

覆盖 weekly_digest 的核心规则：ISO 周解析、周窗口过滤（周一/周日边界）、
raw + extracted 去重优先级、未提取文章的英文降级链、Markdown 渲染结构。
所有用例通过 tmp_path 构造临时 data 目录，不依赖真实 pipeline 数据。
"""

from datetime import date

import pytest

from pipeline.utils.frontmatter import write_frontmatter
from weekly_digest.collector import (
    DESCRIPTION_MAX_CHARS,
    build_digest,
    collect_items,
    iso_week_of,
    parse_iso_week,
    weeks_in_range,
)
from weekly_digest.render import render_markdown
from weekly_digest.run import main, resolve_week, write_digest

# 固定一个 ISO 周做测试：2026-W41 = 2026-10-05（周一）~ 2026-10-11（周日）
WEEK = "2026-W41"
WEEK_START = date(2026, 10, 5)
WEEK_END = date(2026, 10, 11)


# ---------------------------------------------------------------------------
# 测试数据构造
# ---------------------------------------------------------------------------

def _write_article(data_dir, stage, source_name, article_id, **meta):
    """在临时 data 目录下写一篇带 frontmatter 的假文章。"""
    path = data_dir / stage / source_name / f"{article_id}.md"
    write_frontmatter(path, {"id": article_id, **meta}, "body")
    return path


# ---------------------------------------------------------------------------
# ISO 周解析
# ---------------------------------------------------------------------------

def test_parse_iso_week_returns_monday_to_sunday():
    start, end = parse_iso_week(WEEK)
    assert start == WEEK_START
    assert end == WEEK_END
    assert start.weekday() == 0
    assert end.weekday() == 6


@pytest.mark.parametrize("bad", ["2026-W1", "2026W41", "2026-10-11", "W41", "2026-W99"])
def test_parse_iso_week_rejects_invalid(bad):
    with pytest.raises(ValueError):
        parse_iso_week(bad)


def test_iso_week_of_roundtrip():
    assert iso_week_of(WEEK_START) == WEEK
    assert iso_week_of(WEEK_END) == WEEK


# ---------------------------------------------------------------------------
# 收集：窗口过滤与去重
# ---------------------------------------------------------------------------

def test_collect_filters_by_week_window(tmp_path):
    """周一/周日边界收录，窗口外排除。"""
    _write_article(tmp_path, "01_raw", "github-trending", "mon", title="Mon", created="2026-10-05")
    _write_article(tmp_path, "01_raw", "github-trending", "sun", title="Sun", created="2026-10-11")
    _write_article(tmp_path, "01_raw", "github-trending", "prev", title="Prev", created="2026-10-04")
    _write_article(tmp_path, "01_raw", "github-trending", "next", title="Next", created="2026-10-12")

    items = collect_items("github-trending", WEEK_START, WEEK_END, data_dir=tmp_path)

    assert {it.article_id for it in items} == {"mon", "sun"}


def test_collect_dedups_with_extracted_priority(tmp_path):
    """同一 ID 同时存在于 01_raw 和 02_extracted 时，extracted（有 tldr）版本胜出。"""
    common = {"title": "Demo", "source": "https://example.com", "created": "2026-10-10"}
    _write_article(tmp_path, "01_raw", "producthunt", "dup", description="raw only", **common)
    _write_article(tmp_path, "02_extracted", "producthunt", "dup", tldr="中文摘要", **common)

    items = collect_items("producthunt", WEEK_START, WEEK_END, data_dir=tmp_path)

    assert len(items) == 1
    assert items[0].summary_zh == "中文摘要"


def test_collect_fallback_for_unextracted_article(tmp_path):
    """未提取的文章：summary_zh 为 None，英文 description 保留并截断。"""
    long_desc = "word " * 200
    _write_article(
        tmp_path, "01_raw", "github-trending", "raw1",
        title="repo/x", created="2026-10-10", description=long_desc,
        manifest_dates=["2026-10-09", "2026-10-10", "2026-09-01"],
    )

    items = collect_items("github-trending", WEEK_START, WEEK_END, data_dir=tmp_path)

    assert len(items) == 1
    item = items[0]
    assert item.summary_zh is None
    assert item.description_en is not None
    assert len(item.description_en) <= DESCRIPTION_MAX_CHARS + 2  # 截断 + " …"
    # manifest_dates 只统计周窗口内的日期
    assert item.trending_days == [date(2026, 10, 9), date(2026, 10, 10)]


# ---------------------------------------------------------------------------
# 渲染
# ---------------------------------------------------------------------------

def test_render_contains_bilingual_sections(tmp_path):
    """已提取条目渲染中文摘要 + English 原文；未提取条目渲染降级标注。"""
    base = {"source": "https://example.com", "created": "2026-10-10"}
    _write_article(
        tmp_path, "02_extracted", "github-trending", "a1",
        title="owner/repo", tldr="这是中文摘要", objective_summary="详细说明",
        description="English description", manifest_dates=["2026-10-10"],
        **base,
    )
    _write_article(
        tmp_path, "01_raw", "github-trending", "a2",
        title="owner/raw", description="raw English text", **base,
    )

    digest = build_digest("github-trending", WEEK, data_dir=tmp_path, today=date(2026, 10, 11))
    md = render_markdown(digest)

    assert f"# GitHub Trending 周报 · {WEEK}（2026-10-05 ~ 2026-10-11）" in md
    assert "## 2026-10-10 · 周六（2 条）" in md
    assert "**中文摘要**：这是中文摘要" in md
    assert "**详细说明**：详细说明" in md
    assert "**English**: English description" in md
    assert "本条未提取中文摘要" in md
    assert "**上榜**：1 天（10-10）" in md
    assert digest.stats.total == 2
    assert digest.stats.extracted == 1


def test_render_producthunt_shows_published_date(tmp_path):
    """Product Hunt 条目展示发布日期，不展示上榜天数。"""
    _write_article(
        tmp_path, "02_extracted", "producthunt", "p1",
        title="Lune", source="https://www.producthunt.com/products/lune",
        created="2026-10-10", published="2026-10-10", tldr="中文",
        manifest_dates=["2026-10-10"],
    )

    digest = build_digest("producthunt", WEEK, data_dir=tmp_path, today=date(2026, 10, 11))
    md = render_markdown(digest)

    assert "**发布日期**：2026-10-10" in md
    assert "**上榜**" not in md


def test_render_empty_week(tmp_path):
    """无收录的周也产出完整文档骨架。"""
    digest = build_digest("github-trending", WEEK, data_dir=tmp_path, today=date(2026, 10, 11))
    md = render_markdown(digest)

    assert "本周共收录 0 条" in md
    assert "本周无收录条目" in md


# ---------------------------------------------------------------------------
# 跨周范围展开
# ---------------------------------------------------------------------------

def test_weeks_in_range_same_week():
    """同周内的任意区间只展开为 1 个周。"""
    assert weeks_in_range(date(2026, 10, 7), date(2026, 10, 9)) == [WEEK]
    assert weeks_in_range(WEEK_START, WEEK_END) == [WEEK]


def test_weeks_in_range_cross_month():
    """跨月区间逐周展开；触及某周任意一天即纳入该周。"""
    # 2026-10-01 属 W40，10-11 是 W41 周日 → 两周
    assert weeks_in_range(date(2026, 10, 1), date(2026, 10, 11)) == ["2026-W40", "2026-W41"]
    # 10-12 是 W42 周一，区间触及 W42 → 三周
    assert weeks_in_range(date(2026, 10, 1), date(2026, 10, 12)) == ["2026-W40", "2026-W41", "2026-W42"]


def test_weeks_in_range_cross_year():
    """跨年边界：2025-12-29 属于 2026-W01，区间展开为 2026-W01 + 2026-W02。"""
    assert weeks_in_range(date(2025, 12, 30), date(2026, 1, 5)) == ["2026-W01", "2026-W02"]


def test_weeks_in_range_rejects_reversed():
    with pytest.raises(ValueError):
        weeks_in_range(date(2026, 10, 12), date(2026, 10, 1))


# ---------------------------------------------------------------------------
# --week 别名解析
# ---------------------------------------------------------------------------

def test_resolve_week_aliases():
    """current/last 别名基于基准日期确定性解析，无需 LLM 心算周数。"""
    # 2026-10-11（周日）属于 2026-W41，上一周为 2026-W40
    sunday = date(2026, 10, 11)
    assert resolve_week(None, today=sunday) == WEEK
    assert resolve_week("current", today=sunday) == WEEK
    assert resolve_week("last", today=sunday) == "2026-W40"
    assert resolve_week("2026-W40", today=sunday) == "2026-W40"


def test_resolve_week_rejects_invalid():
    with pytest.raises(ValueError):
        resolve_week("not-a-week")


# ---------------------------------------------------------------------------
# 进行中快照标注
# ---------------------------------------------------------------------------

def test_render_marks_in_progress_snapshot(tmp_path):
    """周未结束时头部标注"进行中快照"；已结束的周不标注。"""
    _write_article(
        tmp_path, "01_raw", "github-trending", "a1",
        title="owner/repo", created="2026-10-08",
    )

    in_progress = build_digest("github-trending", WEEK, data_dir=tmp_path, today=date(2026, 10, 8))
    assert "进行中快照" in render_markdown(in_progress)

    finished = build_digest("github-trending", WEEK, data_dir=tmp_path, today=date(2026, 10, 11))
    assert "进行中快照" not in render_markdown(finished)


# ---------------------------------------------------------------------------
# 变更告知
# ---------------------------------------------------------------------------

def test_write_digest_reports_changes(tmp_path, capsys=None):
    """重复生成同一周：首次"首次生成"，第二次对比出新增与中文升级条数。"""
    data_dir = tmp_path / "data"
    out_dir = tmp_path / "out"
    _write_article(
        data_dir, "01_raw", "github-trending", "a1",
        title="owner/repo", created="2026-10-10", description="raw English",
    )

    digest_v1 = build_digest("github-trending", WEEK, data_dir=data_dir, today=WEEK_END)
    _, _, note1 = write_digest(digest_v1, out_dir)
    assert note1 == "首次生成"

    # 数据演进：a1 补跑 extract（02_extracted 出现带 tldr 的版本），新增一篇 a2
    _write_article(
        data_dir, "02_extracted", "github-trending", "a1",
        title="owner/repo", created="2026-10-10", tldr="中文摘要",
    )
    _write_article(
        data_dir, "01_raw", "github-trending", "a2",
        title="owner/new", created="2026-10-11", description="new repo",
    )

    digest_v2 = build_digest("github-trending", WEEK, data_dir=data_dir, today=WEEK_END)
    _, _, note2 = write_digest(digest_v2, out_dir)
    assert "新增 1 条" in note2
    assert "1 条升级为中文摘要" in note2

    # 第三次数据不变 → 无变更
    digest_v3 = build_digest("github-trending", WEEK, data_dir=data_dir, today=WEEK_END)
    _, _, note3 = write_digest(digest_v3, out_dir)
    assert note3 == "较上次：新增 0 条"


def test_write_digest_tolerates_broken_old_json(tmp_path):
    """旧 JSON 损坏时降级为"首次生成"，不阻塞写入。"""
    out_dir = tmp_path / "out"
    (out_dir / "github-trending").mkdir(parents=True)
    (out_dir / "github-trending" / f"{WEEK}.json").write_text("{broken", encoding="utf-8")

    digest = build_digest("github-trending", WEEK, data_dir=tmp_path / "data", today=WEEK_END)
    md_path, json_path, note = write_digest(digest, out_dir)

    assert note == "首次生成"
    assert md_path.exists() and json_path.exists()


# ---------------------------------------------------------------------------
# CLI 参数校验
# ---------------------------------------------------------------------------

def test_cli_rejects_week_with_range():
    """--week 与 --from/--to 互斥。"""
    with pytest.raises(SystemExit):
        main(["--week", WEEK, "--from", "2026-10-01", "--to", "2026-10-12"])


def test_cli_rejects_unpaired_range():
    """--from 与 --to 必须成对出现。"""
    with pytest.raises(SystemExit):
        main(["--from", "2026-10-01"])
