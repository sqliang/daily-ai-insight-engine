"""
tests/test_manifest_date_aggregation.py — 日报日期口径聚合测试

覆盖历史日报回溯中的新增文章口径：同一篇文章可能多天出现在 manifest 中，
但默认日报只按 created 选择首次进入管道的文章。manifest_dates 仅作为审计
信息，不会让旧文章重复进入新的日报。
"""

from datetime import date

from pipeline.aggregation.aggregate_frontmatter import (
    _candidate_selection_score,
    _is_report_ready,
    _matches_target_date,
)
from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
from pipeline.ingestion.ingest.orchestrator import _needs_ingest, _record_manifest_date_for_existing
from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter


def test_candidate_selection_ignores_manifest_dates_for_target_date(tmp_path):
    """manifest_dates 命中不应提高 target_date 选择分数。"""
    source_dir = tmp_path / "extracted" / "github-trending"
    source_dir.mkdir(parents=True)
    extracted = source_dir / "abc123.md"
    write_frontmatter(
        extracted,
        {
            "id": "abc123",
            "title": "Demo",
            "created": "2026-06-27",
            "manifest_dates": ["2026-06-27", "2026-06-28"],
            "tldr": "summary",
            "objective_summary": "objective",
        },
        "body",
    )

    score = _candidate_selection_score(extracted, "extracted", date(2026, 6, 28))

    assert score[0] == 0
    assert score[1] == 2


def test_target_date_requires_created_match_even_when_manifest_dates_match():
    """旧文章重复出现在当天 manifest 时，不应进入当天日报窗口。"""
    record = {
        "source_dir": "producthunt",
        "id": "p1",
        "title": "Product",
        "created": "2026-06-27",
        "manifest_dates": ["2026-06-27", "2026-06-28"],
    }

    assert not _matches_target_date(record, date(2026, 6, 28))


def test_target_date_accepts_created_match():
    """created 等于 target_date 的新增文章应进入当天日报窗口。"""
    record = {
        "source_dir": "hackernews",
        "id": "hn1",
        "title": "HN",
        "created": "2026-06-28",
        "manifest_dates": ["2026-06-28"],
    }

    assert _matches_target_date(record, date(2026, 6, 28))


def test_report_input_rejects_failed_extraction():
    """提取失败文章不应进入 all_articles.json 日报合成输入。"""
    record = {
        "source_dir": "hackernews",
        "id": "hn-failed",
        "title": "Failed",
        "created": "2026-06-28",
        "extraction_status": "success",
        "extract_result": "failed",
    }

    assert not _is_report_ready(record)


def test_report_input_requires_extracted_summary():
    """具备摘要字段的已提取文章可以进入日报合成输入。"""
    record = {
        "source_dir": "hackernews",
        "id": "hn-ready",
        "title": "Ready",
        "created": "2026-06-28",
        "extraction_status": "success",
        "tldr": "summary",
    }

    assert _is_report_ready(record)


def test_historical_new_ingest_uses_manifest_date_as_created():
    """历史 manifest 新抓文章时，created 写入 manifest 日期。"""
    fm = build_ingestion_frontmatter(
        title="New Article",
        url="https://example.com/new",
        source_name="example",
        article_id="new1",
        created="2026-06-28",
    )

    assert fm["created"] == "2026-06-28"
    assert fm["manifest_dates"] == ["2026-06-28"]


def test_existing_ingest_records_manifest_date_without_overwriting_created(tmp_path):
    """已存在文章跳过抓取时，只补记 manifest_dates，不覆盖首次入库 created。"""
    target_dir = tmp_path / "raw" / "example"
    target_dir.mkdir(parents=True)
    md_path = target_dir / "old1.md"
    write_frontmatter(
        md_path,
        {
            "id": "old1",
            "title": "Old Article",
            "source": "https://example.com/old",
            "created": "2026-06-27",
            "manifest_dates": ["2026-06-27"],
        },
        "body",
    )

    _record_manifest_date_for_existing(
        {"id": "old1", "url": "https://example.com/old"},
        target_dir,
        "2026-06-28",
    )

    fm, _ = read_frontmatter(md_path)
    assert fm["created"] == "2026-06-27"
    assert fm["manifest_dates"] == ["2026-06-27", "2026-06-28"]


def test_existing_raw_file_skips_ingest_even_when_state_misses(tmp_path):
    """state 缺记录但 raw 文件已存在时，非 force ingest 不应覆盖 created。"""

    class EmptyState:
        """模拟缺失历史记录的 ingest state。"""

        force_enabled = False

        def is_seen(self, _article_id: str) -> bool:
            """模拟 state 未命中。"""
            return False

    target_dir = tmp_path / "raw" / "example"
    target_dir.mkdir(parents=True)
    write_frontmatter(
        target_dir / "old1.md",
        {
            "id": "old1",
            "title": "Old Article",
            "source": "https://example.com/old",
            "created": "2026-06-27",
        },
        "body",
    )

    assert not _needs_ingest(
        {"id": "old1", "url": "https://example.com/old"},
        target_dir,
        EmptyState(),
    )
