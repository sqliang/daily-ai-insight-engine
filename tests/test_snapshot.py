"""
tests/test_snapshot.py — 站点数据快照生成与本地 git 发布契约测试

用临时目录构造迷你 data/，验证日报与热文章原样拷贝、manifest 按源合并降序、
index.json 来源清单与日报日期，以及无日期副本、all_articles 和 archive 的排除语义。
push 集成测试只使用本地 bare remote，覆盖 orphan、force 替换、工作区隔离和失败清理。
"""

import json
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

import pytest

from pipeline.publish import snapshot as snapshot_module
from pipeline.publish.snapshot import generate_snapshot, push_snapshot


# ---------------------------------------------------------------------------
# 测试数据构造
# ---------------------------------------------------------------------------

def _write_json(path: Path, payload) -> None:
    """以 UTF-8 写入测试 JSON，并自动创建父目录。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _git(cwd: Path, *args: str) -> str:
    """在测试仓库执行 git 并返回去除首尾空白后的 stdout。"""
    result = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def _make_main_repo(root: Path) -> Path:
    """构造带未提交修改和未跟踪文件的主仓库，用于验证工作区隔离。"""
    root.mkdir(parents=True)
    _git(root, "init", "--initial-branch=feature/test")
    _git(root, "config", "user.name", "Snapshot Test")
    _git(root, "config", "user.email", "snapshot-test@example.com")
    (root / "tracked.txt").write_text("committed\n", encoding="utf-8")
    _git(root, "add", "tracked.txt")
    _git(root, "commit", "-m", "test: initial main workspace")
    (root / "tracked.txt").write_text("local change\n", encoding="utf-8")
    (root / "untracked.txt").write_text("keep\n", encoding="utf-8")
    return root


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


def test_generate_snapshot_copies_markdown_only_report(tmp_path):
    """Markdown-only 日报仍应拷贝，但没有 JSON 可展示，故不进入 report_dates。"""
    data_root = _make_mini_data(tmp_path)
    markdown_only = data_root / "05_reports" / "daily-report-2026-10-11.md"
    markdown_only.write_text("# 仅 Markdown 日报\n", encoding="utf-8")

    stats = generate_snapshot(data_root)

    snapshot_root = data_root / "snapshot"
    assert (snapshot_root / "reports" / markdown_only.name).read_bytes() == markdown_only.read_bytes()
    index = json.loads((snapshot_root / "index.json").read_text(encoding="utf-8"))
    assert index["report_dates"] == ["2026-10-10", "2026-10-09"]
    assert stats["counts"]["reports"] == 4


# ---------------------------------------------------------------------------
# 本地 bare remote 发布集成
# ---------------------------------------------------------------------------

def test_push_snapshot_uses_root_orphan_and_force_replaces_without_touching_main(tmp_path):
    """两次本地推送验证分支根目录、无父提交、force 替换和主工作区隔离。"""
    data_root = _make_mini_data(tmp_path / "snapshot-input")
    generate_snapshot(data_root)
    snapshot_root = data_root / "snapshot"
    main_repo = _make_main_repo(tmp_path / "main-workspace")
    remote = tmp_path / "remote.git"
    _git(tmp_path, "init", "--bare", str(remote))

    before_head = _git(main_repo, "rev-parse", "HEAD")
    before_branch = _git(main_repo, "branch", "--show-current")
    before_status = _git(main_repo, "status", "--short")

    first = push_snapshot(snapshot_root, repo_root=main_repo, remote_url=str(remote))

    assert _git(remote, "rev-parse", "data-snapshot") == first["commit"]
    assert _git(remote, "rev-list", "--parents", "-n", "1", "data-snapshot") == first["commit"]
    assert set(_git(remote, "ls-tree", "--name-only", "data-snapshot").splitlines()) == {
        "articles",
        "index.json",
        "manifests",
        "reports",
    }
    assert _git(main_repo, "rev-parse", "HEAD") == before_head
    assert _git(main_repo, "branch", "--show-current") == before_branch
    assert _git(main_repo, "status", "--short") == before_status

    second_index = json.loads((snapshot_root / "index.json").read_text(encoding="utf-8"))
    second_index["generated_at"] = "2026-10-19T10:00:00+08:00"
    (snapshot_root / "index.json").write_text(
        json.dumps(second_index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    second = push_snapshot(snapshot_root, repo_root=main_repo, remote_url=str(remote))

    assert second["commit"] != first["commit"]
    assert _git(remote, "rev-parse", "data-snapshot") == second["commit"]
    assert _git(remote, "rev-list", "--parents", "-n", "1", "data-snapshot") == second["commit"]
    assert _git(remote, "rev-list", "--count", "data-snapshot") == "1"
    remote_index = json.loads(_git(remote, "show", "data-snapshot:index.json"))
    assert remote_index["generated_at"] == "2026-10-19T10:00:00+08:00"
    assert _git(main_repo, "rev-parse", "HEAD") == before_head
    assert _git(main_repo, "branch", "--show-current") == before_branch
    assert _git(main_repo, "status", "--short") == before_status


def test_push_snapshot_invalid_remote_raises_and_cleans_temporary_directory(tmp_path, monkeypatch):
    """无效本地远端必须抛出异常，且 TemporaryDirectory 不遗留临时仓库。"""
    data_root = _make_mini_data(tmp_path / "snapshot-input")
    generate_snapshot(data_root)
    main_repo = _make_main_repo(tmp_path / "main-workspace")
    temp_parent = tmp_path / "temp"
    temp_parent.mkdir()
    real_temporary_directory = tempfile.TemporaryDirectory

    def _temporary_directory(*args, **kwargs):
        """把被测代码的临时目录限制在测试目录内，以便检查失败清理。"""
        kwargs["dir"] = temp_parent
        return real_temporary_directory(*args, **kwargs)

    monkeypatch.setattr(snapshot_module.tempfile, "TemporaryDirectory", _temporary_directory)
    invalid_remote = tmp_path / "missing" / "remote.git"

    with pytest.raises(RuntimeError, match="git push"):
        push_snapshot(
            data_root / "snapshot",
            repo_root=main_repo,
            remote_url=str(invalid_remote),
        )

    assert list(temp_parent.iterdir()) == []


def test_push_snapshot_rejects_non_snapshot_branch(tmp_path):
    """branch 防御必须拒绝 main 等任意非 data-snapshot 目标。"""
    data_root = _make_mini_data(tmp_path / "snapshot-input")
    generate_snapshot(data_root)
    main_repo = _make_main_repo(tmp_path / "main-workspace")
    remote = tmp_path / "remote.git"
    _git(tmp_path, "init", "--bare", str(remote))

    with pytest.raises(ValueError, match="data-snapshot"):
        push_snapshot(
            data_root / "snapshot",
            repo_root=main_repo,
            remote_url=str(remote),
            branch="main",
        )

    assert _git(remote, "branch", "--list") == ""
