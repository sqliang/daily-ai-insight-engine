"""
tests/test_stage_target_date.py — extract/analyze 阶段 --target-date 日期隔离测试

背景（2026-07-29 事故）：阶段执行未做日期隔离时，skip-existing 会把数月历史
积压一并送进 LLM（extract 519 篇、analyze 1381 篇，目标日期仅占 16 篇），
烧穿 API 余额。这里验证 filter_by_created 的过滤语义，确保日期隔离可靠。
"""

from datetime import date
from pathlib import Path

from pipeline.utils.frontmatter import filter_by_created, read_created_date, write_frontmatter


def _make_md(tmp_path: Path, name: str, created: str) -> Path:
    """构造带指定 created 的测试 .md 文件。"""
    fp = tmp_path / name
    write_frontmatter(fp, {"title": name, "created": created}, "正文内容")
    return fp


def test_read_created_date_formats(tmp_path):
    """created 的多种写法都应被统一为 YYYY-MM-DD。"""
    fp_quoted = _make_md(tmp_path, "a.md", "2026-07-21")
    assert read_created_date(fp_quoted) == "2026-07-21"

    # 无 created 字段 → 空串
    fp_none = tmp_path / "b.md"
    write_frontmatter(fp_none, {"title": "b"}, "正文")
    assert read_created_date(fp_none) == ""

    # 文件不存在 → 空串（不抛异常）
    assert read_created_date(tmp_path / "missing.md") == ""


def test_filter_by_created_keeps_only_target_date(tmp_path):
    """过滤后只保留 created == target 的文件，范围外与无日期的全部排除。"""
    target = date(2026, 7, 21)
    in_scope = [
        _make_md(tmp_path, "in1.md", "2026-07-21"),
        _make_md(tmp_path, "in2.md", "2026-07-21"),
    ]
    out_of_scope = [
        _make_md(tmp_path, "out1.md", "2026-07-20"),
        _make_md(tmp_path, "out2.md", "2026-07-22"),
        _make_md(tmp_path, "out3.md", "2026-05-07"),
    ]
    no_date = tmp_path / "nodate.md"
    write_frontmatter(no_date, {"title": "nodate"}, "正文")

    result = filter_by_created(in_scope + out_of_scope + [no_date], target)

    # 范围内的全部保留，范围外和无日期的全部排除（保守排除原则：
    # 宁可漏处理让 check 门禁发现，也不能把范围外文件送进 LLM）
    assert sorted(p.name for p in result) == ["in1.md", "in2.md"]


def test_filter_by_created_empty_result(tmp_path):
    """没有匹配日期时返回空列表（调用方应视为"当天无待处理"而非处理全量）。"""
    files = [_make_md(tmp_path, "x.md", "2026-07-20")]
    assert filter_by_created(files, date(2026, 7, 21)) == []
