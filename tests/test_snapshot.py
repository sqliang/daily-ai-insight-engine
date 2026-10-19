"""
tests/test_snapshot.py — 站点数据快照本地生成契约测试

用临时目录构造迷你 data/，验证日报与热文章原样拷贝、manifest 按源合并降序、
index.json 来源清单与日报日期，以及无日期副本、all_articles 和 archive 的排除语义。
不涉及网络或真实 git push。
"""

import json
from datetime import datetime
from pathlib import Path

from pipeline.publish.snapshot import generate_snapshot


# ---------------------------------------------------------------------------
# 测试数据构造
# ---------------------------------------------------------------------------

def _write_json(path: Path, payload) -> None:
    """以 UTF-8 写入测试 JSON，并自动创建父目录。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _make_mini_data(root: Path) -> Path:
    """构造覆盖三类快照输入及排除项的迷你 data 目录。"""
    data_root = root / "data"

    _write_json(data_root / "05_reports" / "daily-report-2026-10-09.json", {"date": "2026-10-09"})
    (data_root / "05_reports" / "daily-report-2026-10-09.md").write_text("# 10 月 9 日\n", encoding="utf-8")
    _write_json(data_root / "05_reports" / "daily-report-2026-10-10.json", {"date": "2026-10-10"})
    _write_json(data_root / "05_reports" / "daily-report.json", {"date": "latest"})
    (data_root / "05_reports" / "daily-report.md").write_text("# 最新无日期副本\n", encoding="utf-8")

    _write_json(data_root / "04_structured" / "arxiv-cs-ai.json", [{"id": "paper"}])
    _write_json(data_root / "04_structured" / "36kr.json", [{"id": "news"}])
    _write_json(data_root / "04_structured" / "all_articles.json", [{"id": "excluded"}])
    _write_json(
        data_root / "04_structured" / "archive" / "arxiv-cs-ai" / "arxiv-cs-ai_2026-10-01.json",
        [{"id": "cold"}],
    )

    for manifest_date, marker in [
        ("2026-10-08", "oldest"),
        ("2026-10-10", "newest"),
        ("2026-10-09", "middle"),
    ]:
        _write_json(
            data_root / "00_manifest" / f"arxiv-cs-ai_{manifest_date}.json",
            {"source": "arxiv-cs-ai", "date": manifest_date, "articles": [marker]},
        )
    _write_json(
        data_root / "00_manifest" / "bensbites_2026-10-07.json",
        {"source": "bensbites", "date": "2026-10-07", "articles": []},
    )
    _write_json(data_root / "00_manifest" / "notes.json", {"ignored": True})

    return data_root


# ---------------------------------------------------------------------------
# 快照结构与 index 契约
# ---------------------------------------------------------------------------

def test_generate_snapshot_builds_contract_and_cleans_output(tmp_path):
    """快照只含契约文件，index 使用实际输入日期与两路 source 并集。"""
    data_root = _make_mini_data(tmp_path)
    snapshot_root = data_root / "snapshot"
    snapshot_root.mkdir()
    (snapshot_root / "stale.txt").write_text("stale", encoding="utf-8")

    stats = generate_snapshot(data_root)

    files = sorted(
        str(path.relative_to(snapshot_root))
        for path in snapshot_root.rglob("*")
        if path.is_file()
    )
    assert files == [
        "articles/36kr.json",
        "articles/arxiv-cs-ai.json",
        "index.json",
        "manifests/arxiv-cs-ai.json",
        "manifests/bensbites.json",
        "reports/daily-report-2026-10-09.json",
        "reports/daily-report-2026-10-09.md",
        "reports/daily-report-2026-10-10.json",
    ]
    assert not (snapshot_root / "stale.txt").exists()
    assert not (snapshot_root / "reports" / "daily-report.json").exists()
    assert not (snapshot_root / "reports" / "daily-report.md").exists()
    assert not (snapshot_root / "articles" / "all_articles.json").exists()
    assert not (snapshot_root / "articles" / "archive").exists()

    index = json.loads((snapshot_root / "index.json").read_text(encoding="utf-8"))
    assert set(index) == {"generated_at", "report_dates", "sources"}
    assert datetime.fromisoformat(index["generated_at"])
    assert index["report_dates"] == ["2026-10-10", "2026-10-09"]
    assert index["sources"] == ["36kr", "arxiv-cs-ai", "bensbites"]

    assert (snapshot_root / "articles" / "arxiv-cs-ai.json").read_bytes() == (
        data_root / "04_structured" / "arxiv-cs-ai.json"
    ).read_bytes()
    assert (snapshot_root / "reports" / "daily-report-2026-10-09.md").read_bytes() == (
        data_root / "05_reports" / "daily-report-2026-10-09.md"
    ).read_bytes()

    assert stats["files"] == len(files)
    assert stats["counts"] == {"reports": 3, "articles": 2, "manifests": 2}
    assert stats["total_bytes"] == sum(
        path.stat().st_size for path in snapshot_root.rglob("*") if path.is_file()
    )


def test_generate_snapshot_merges_manifests_in_descending_date_order(tmp_path):
    """同一源的 manifest 对象合入一个数组，首元素必须是文件名日期最新者。"""
    data_root = _make_mini_data(tmp_path)

    generate_snapshot(data_root)

    snapshot_root = data_root / "snapshot"
    arxiv_manifests = json.loads(
        (snapshot_root / "manifests" / "arxiv-cs-ai.json").read_text(encoding="utf-8")
    )
    assert [item["date"] for item in arxiv_manifests] == [
        "2026-10-10",
        "2026-10-09",
        "2026-10-08",
    ]
    assert [item["articles"][0] for item in arxiv_manifests] == ["newest", "middle", "oldest"]

    bensbites_manifests = json.loads(
        (snapshot_root / "manifests" / "bensbites.json").read_text(encoding="utf-8")
    )
    assert bensbites_manifests == [
        {"source": "bensbites", "date": "2026-10-07", "articles": []}
    ]
