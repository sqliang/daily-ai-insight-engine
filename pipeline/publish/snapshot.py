"""
pipeline/publish/snapshot.py — Stage 5 站点数据快照生成与 GitHub 分支发布

数据流：
    data/05_reports → data/snapshot/reports（带日期日报）
    data/04_structured 顶层 JSON → data/snapshot/articles（热文章）
    data/00_manifest → data/snapshot/manifests（按源合并、按日期降序）
    实际快照内容 → data/snapshot/index.json（日期与来源索引）

快照供前端在 PostgreSQL 不可用时回退读取；--push 将快照放到 data-snapshot
orphan 分支的仓库根目录，使本地文件与 raw.githubusercontent.com 共享同一契约。
发布全程使用临时目录，绝不在主工作区 checkout 或改写分支；force push 仅用于
让该独立分支始终保存最新一份全量快照，不影响主代码分支。
"""

import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional


SNAPSHOT_BRANCH = "data-snapshot"
SNAPSHOT_REMOTE = "git@github.com:sqliang/daily-ai-insight-engine.git"
_REPORT_NAME_RE = re.compile(r"^daily-report-(?P<date>\d{4}-\d{2}-\d{2})\.json$")
_REPORT_MARKDOWN_NAME_RE = re.compile(r"^daily-report-(?P<date>\d{4}-\d{2}-\d{2})\.md$")
_MANIFEST_NAME_RE = re.compile(r"^(?P<source>.+)_(?P<date>\d{4}-\d{2}-\d{2})\.json$")


# ---------------------------------------------------------------------------
# 本地快照生成
# ---------------------------------------------------------------------------

def generate_snapshot(data_root: Path) -> dict:
    """
    清空并全量重建 data_root/snapshot，返回文件与体量统计。

    参数：
        data_root: pipeline 本地数据目录，通常为主仓库的 data/。

    返回：
        dict: snapshot_dir、files（含 index.json）、counts（各子目录文件数）
              和 total_bytes（快照全部文件总字节数）。

    异常：
        ValueError: 符合命名契约的 manifest 不是 JSON 对象时抛出，避免发布残缺数据。
        OSError: 文件清理、读取或写入失败时抛出。

    设计理由：
        日报与文章直接按字节拷贝，避免 JSON 重序列化改变前端收到的内容；
        manifest 则必须重组成单源数组，让前端一次请求即可按日期回退查询。
    """
    data_root = Path(data_root)
    snapshot_root = data_root / "snapshot"
    if snapshot_root.exists():
        shutil.rmtree(snapshot_root)

    reports_output = snapshot_root / "reports"
    articles_output = snapshot_root / "articles"
    manifests_output = snapshot_root / "manifests"
    for output_dir in (reports_output, articles_output, manifests_output):
        output_dir.mkdir(parents=True, exist_ok=True)

    report_dates = set()
    report_files = 0
    reports_input = data_root / "05_reports"
    for report_path in sorted(reports_input.glob("daily-report-*.json")):
        match = _REPORT_NAME_RE.fullmatch(report_path.name)
        if not report_path.is_file() or match is None:
            continue
        shutil.copy2(report_path, reports_output / report_path.name)
        report_files += 1
        report_dates.add(match.group("date"))

    # report_dates 与 DB daily_reports 口径一致，只由 JSON 日报收集；
    # Markdown-only 文件仍独立拷贝，供全文回退，但不用于日报卡片列表。
    for markdown_path in sorted(reports_input.glob("daily-report-*.md")):
        match = _REPORT_MARKDOWN_NAME_RE.fullmatch(markdown_path.name)
        if not markdown_path.is_file() or match is None:
            continue
        shutil.copy2(markdown_path, reports_output / markdown_path.name)
        report_files += 1

    article_sources = set()
    article_files = 0
    structured_input = data_root / "04_structured"
    for article_path in sorted(structured_input.glob("*.json")):
        if not article_path.is_file() or article_path.name == "all_articles.json":
            continue
        shutil.copy2(article_path, articles_output / article_path.name)
        article_sources.add(article_path.stem)
        article_files += 1

    manifest_groups = {}
    manifests_input = data_root / "00_manifest"
    for manifest_path in sorted(manifests_input.glob("*.json")):
        match = _MANIFEST_NAME_RE.fullmatch(manifest_path.name)
        if not manifest_path.is_file() or match is None:
            continue
        with manifest_path.open("r", encoding="utf-8") as file:
            manifest = json.load(file)
        if not isinstance(manifest, dict):
            raise ValueError(f"manifest 必须是 JSON 对象: {manifest_path}")
        source = match.group("source")
        manifest_groups.setdefault(source, []).append((match.group("date"), manifest))

    for source in sorted(manifest_groups):
        dated_manifests = sorted(
            manifest_groups[source], key=lambda item: item[0], reverse=True
        )
        output_path = manifests_output / f"{source}.json"
        with output_path.open("w", encoding="utf-8") as file:
            json.dump(
                [manifest for _, manifest in dated_manifests],
                file,
                ensure_ascii=False,
                indent=2,
            )
            file.write("\n")

    sources = sorted(article_sources | set(manifest_groups))
    index = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "report_dates": sorted(report_dates, reverse=True),
        "sources": sources,
    }
    index_path = snapshot_root / "index.json"
    with index_path.open("w", encoding="utf-8") as file:
        json.dump(index, file, ensure_ascii=False, indent=2)
        file.write("\n")

    snapshot_files = [path for path in snapshot_root.rglob("*") if path.is_file()]
    return {
        "snapshot_dir": str(snapshot_root),
        "files": len(snapshot_files),
        "counts": {
            "reports": report_files,
            "articles": article_files,
            "manifests": len(manifest_groups),
        },
        "total_bytes": sum(path.stat().st_size for path in snapshot_files),
    }


# ---------------------------------------------------------------------------
# 独立 orphan 分支发布
# ---------------------------------------------------------------------------

def _run_git(args, cwd: Path, check: bool = True):
    """在指定目录执行 git；失败时保留 stderr 上下文，便于 CLI 直接报告原因。"""
    result = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}"
        raise RuntimeError(f"git {' '.join(args)} 失败: {detail}")
    return result


def _git_config_or_default(repo_root: Path, key: str, default: str) -> str:
    """读取主仓库可见的 git config；未配置时使用快照提交专用默认值。"""
    result = _run_git(["config", key], cwd=repo_root, check=False)
    return result.stdout.strip() or default


def push_snapshot(
    snapshot_root: Path,
    repo_root: Optional[Path] = None,
    remote_url: str = SNAPSHOT_REMOTE,
    branch: str = SNAPSHOT_BRANCH,
) -> dict:
    """
    在临时目录将快照提交为无父提交，并 force push 到独立数据分支。

    参数：
        snapshot_root: generate_snapshot 生成的快照目录，内容映射到分支根目录。
        repo_root: 用于读取 git 作者信息的主仓库路径；默认按当前文件定位。
        remote_url: 快照推送目标，默认使用任务约定的 GitHub SSH 地址。
        branch: 独立快照分支名，仅允许 data-snapshot。

    返回：
        dict: 推送 branch、remote 与快照 commit hash。

    异常：
        ValueError: branch 不是 data-snapshot 时抛出，阻止误 force push 代码分支。
        FileNotFoundError: 快照目录或 index.json 不存在时抛出。
        RuntimeError: 任一 git 初始化、提交或推送步骤失败时抛出。

    设计理由：
        临时仓库的首个提交天然没有父提交，配合 --orphan 明确分支语义；
        TemporaryDirectory 在成功或失败后都会清理，不让发布过程污染主工作区。
    """
    if branch != SNAPSHOT_BRANCH:
        raise ValueError(f"快照推送只允许 {SNAPSHOT_BRANCH} 分支，收到: {branch}")

    snapshot_root = Path(snapshot_root)
    if not snapshot_root.is_dir() or not (snapshot_root / "index.json").is_file():
        raise FileNotFoundError(f"快照目录不完整，缺少 index.json: {snapshot_root}")

    main_repo = Path(repo_root) if repo_root is not None else Path(__file__).resolve().parents[2]
    user_name = _git_config_or_default(main_repo, "user.name", "Daily AI Insight Bot")
    user_email = _git_config_or_default(
        main_repo,
        "user.email",
        "daily-ai-insight-bot@users.noreply.github.com",
    )

    with tempfile.TemporaryDirectory(prefix="site-data-snapshot-") as temp_dir:
        temp_repo = Path(temp_dir) / "repo"
        shutil.copytree(snapshot_root, temp_repo)
        _run_git(["init"], cwd=temp_repo)
        _run_git(["checkout", "--orphan", branch], cwd=temp_repo)
        _run_git(["config", "user.name", user_name], cwd=temp_repo)
        _run_git(["config", "user.email", user_email], cwd=temp_repo)
        _run_git(["add", "--all"], cwd=temp_repo)
        _run_git(["commit", "-m", "chore(data): update site data snapshot"], cwd=temp_repo)
        commit = _run_git(["rev-parse", "HEAD"], cwd=temp_repo).stdout.strip()
        _run_git(["remote", "add", "origin", remote_url], cwd=temp_repo)
        _run_git(["push", "--force", "origin", branch], cwd=temp_repo)

    return {"branch": branch, "remote": remote_url, "commit": commit}
