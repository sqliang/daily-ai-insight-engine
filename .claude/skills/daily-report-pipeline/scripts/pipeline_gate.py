#!/usr/bin/env python3
"""
pipeline_gate.py — 指定日期日报流水线的"检查→定点修复"门禁脚本

被 .agents/skills/daily-report-pipeline/SKILL.md 编排调用，负责各阶段的后验检查与
定点修复。设计目标：
1. 日期隔离 —— 所有检查/修复只作用于 frontmatter `created == --date` 的文章，
   严禁触碰其他日期的数据。
2. 成本控制 —— repair 全部是单文件粒度（LLM 调用只针对问题文章），不重跑全天。
3. 只读检查 —— check-* 子命令不写任何文件，只输出 JSON 报告；
   exit 0 = 通过，exit 1 = 存在问题。

用法（必须在项目根目录下执行）：
    uv run python .agents/skills/daily-report-pipeline/scripts/pipeline_gate.py <command> --date YYYY-MM-DD

命令：
    check-ingest     检查 Stage 1 抓取完整性（manifest 覆盖 + 状态 + 正文质量启发式）
    repair-ingest    定点修复抓取问题（浏览器重抓 + Jina 兜底 + 劣化回滚）
    run-extract      日期隔离地执行 Stage 2（单进程 --target-date + 预检熔断）
    check-extract    检查 Stage 2 提取结果（缺失文件 / extract_result / 关键字段 / 过期）
    repair-extract   对问题文章单独重跑 extract（LLM 调用，单文件粒度）
    run-analyze      日期隔离地执行 Stage 3（单进程 --target-date + 预检熔断）
    check-analyze    检查 Stage 3 分析结果（缺失文件 / impact_score / sentiment / 过期）
    repair-analyze   对问题文章单独重跑 analyze（LLM 调用，单文件粒度）
"""

import argparse
import json
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# 环境初始化（复刻 pipeline/run.py：项目根目录上 sys.path + .env + 代理）
# ---------------------------------------------------------------------------
# 脚本位于 .agents/skills/daily-report-pipeline/scripts/ 下，向上 4 级是项目根
_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_ROOT))

from dotenv import load_dotenv

load_dotenv(_ROOT / ".env")

from pipeline.core.proxy_utils import setup_proxy

# setup_proxy 会向 stdout 打印代理信息；为保证 check-* 的 stdout 只有 JSON 报告
# （agent/脚本会解析 stdout），把初始化阶段的打印重定向到 stderr
import contextlib

with contextlib.redirect_stdout(sys.stderr):
    setup_proxy()

from pipeline.core.config_loader import get_sources, resolve_data_dir
from pipeline.core.web_utils import fetch_via_jina, is_bot_challenge_html
from pipeline.ingestion.repair import repair_failed_articles
from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

# 正文低于该字符数视为"过短可疑"。取 200 而非更大的值：
# 36kr 快讯、TLDR 条目等本身就短（正文 300~800 字符属正常），
# 只有 < 200 才大概率是抓取失败残留（占位快照、空壳页面等）
MIN_BODY_CHARS = 200

# Jina Reader 缓存快照的标记文本，出现即说明拿到的是缓存残页而非全文
_JINA_SNAPSHOT_MARK = "Warning: This is a cached snapshot"

# 短内容源的"过短"豁免阈值（字符）。这些源的文章本身就是短条目，
# 用通用 200 字符阈值会每天误报（2026-07-21 实测 36kr 快讯正文仅 107~186 字符）
_SHORT_SOURCE_MIN_CHARS = {
    "36kr": 50,          # 快讯快电，一句话新闻
    "tldrai": 80,        # TLDR 风格的 1-minute read 条目
    "producthunt": 80,   # 产品 tagline + 简介
}


# ---------------------------------------------------------------------------
# 通用工具
# ---------------------------------------------------------------------------

def _parse_date(s: str) -> date:
    """解析 YYYY-MM-DD 参数，非法格式直接报错退出。"""
    try:
        return date.fromisoformat(s)
    except ValueError:
        print(f"错误: --date 格式无效: {s} (期望 YYYY-MM-DD)", file=sys.stderr)
        sys.exit(2)


def _created_str(fm: dict) -> str:
    """从 frontmatter 取 created 并统一为 YYYY-MM-DD 字符串（兼容 date 对象）。"""
    created = fm.get("created", "")
    if isinstance(created, date):
        return created.isoformat()
    return str(created)[:10]


def _iter_date_files(base_dir: Path, target: date):
    """
    遍历 base_dir 下所有 .md，产出 (path, frontmatter, body) —— 仅 created==target 的文件。

    日期隔离的核心：所有阶段检查都通过这个函数过滤，保证只处理指定日期的文章。
    frontmatter 解析失败的文件跳过（不产生误判）。
    """
    if not base_dir.exists():
        return
    for fp in sorted(base_dir.rglob("*.md")):
        if not fp.is_file() or fp.parent == base_dir:
            continue
        try:
            fm, body = read_frontmatter(fp)
        except Exception:
            continue
        if _created_str(fm) == target.isoformat():
            yield fp, fm, body


def _emit(report: dict, has_issues: bool):
    """统一输出 JSON 报告并按结果设置退出码（0=通过，1=有问题）。"""
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(1 if has_issues else 0)


# 错误页特征：Jina/浏览器可能把 404 等错误页当成"正文"返回
# （2026-07-29 实战：TLDR 文章源 URL 死链，Jina 返回 Google Cloud 的 404 页，
# 修复脚本险些把错误页当正文接受）
_ERROR_PAGE_MARKS = (
    "Target URL returned error 404",
    "404  |  Page Not Found",
    "404 | Page Not Found",
    "Page Not Found",
)


def _is_error_page(text: str) -> bool:
    """检测正文是否为 404 等错误页内容（而非真正的文章正文）。"""
    head = text[:500]  # 错误页特征通常出现在开头标题区
    return any(mark in head for mark in _ERROR_PAGE_MARKS)


def _body_problems(body: str, source: str = "") -> list[str]:
    """
    正文质量启发式检查，返回问题原因列表（空列表 = 正文健康）。

    背景：extraction_status=success 不代表正文真的完整——Jina 兜底可能写入
    截断的缓存快照、浏览器"部分修复"可能写入 HTML 源码（2026-07-21 实战均出现过），
    所以必须对 success 文件也做内容级检查。

    参数：
        body: 文章正文
        source: 数据源名（文件所在子目录名），用于短内容源的阈值豁免
    """
    problems = []
    text = body.strip()
    if is_bot_challenge_html(text):
        problems.append("anti_bot")
    if text.startswith(("<!DOCTYPE", "<html")):
        problems.append("html_dump")
    if _JINA_SNAPSHOT_MARK in text:
        problems.append("jina_cached_snapshot")
    if _is_error_page(text):
        problems.append("error_page")
    # 短内容源用豁免阈值：36kr 快讯正文 100~200 字符属正常（实测），
    # tldrai/producthunt 同理是短条目源；这些源只在正文几乎为空时才报警
    min_chars = _SHORT_SOURCE_MIN_CHARS.get(source, MIN_BODY_CHARS)
    if len(text) < min_chars:
        problems.append(f"too_short({len(text)})")
    return problems


def _run_cli(args: list[str], timeout: int = 1800) -> tuple[int, str]:
    """
    调用项目 CLI（pipeline/run.py），返回 (returncode, 输出摘要)。

    修复动作统一走现有 CLI 而不是直接调内部函数，保证行为与日常流水线完全一致
    （包括 extract/analyze 后的自动 aggregate）。

    timeout 默认 1800s 面向单文件 repair；run_stage 全天执行需显式传更大的值
    （实测 60+ 篇 × 3 分析维度会超过 30 分钟，2026-08-14 曾因超时中断）。
    """
    cmd = ["uv", "run", "python", "pipeline/run.py"] + args
    proc = subprocess.run(cmd, cwd=_ROOT, capture_output=True, text=True, timeout=timeout)
    tail = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode, "\n".join(tail[-5:])


# ---------------------------------------------------------------------------
# Stage 1: ingest 检查与修复
# ---------------------------------------------------------------------------

def _missing_manifests(target: date) -> list[str]:
    """
    找出当天"异常缺失" manifest 的活跃源。

    判定启发式（避免把周期性空窗误报为 scout 失败）：
    - 周末（周六/周日）不标记任何缺失——arxiv、nlp-elvis 等源周末本就无内容
      （实测 2026-07-25/26 周末这两源无 manifest 属正常）；
    - 工作日缺失时，要求前一天有该源 manifest，且（后一天也有，或后一天还没到/
      未运行）才标记——单点 scout 失败（如 2026-07-21 arxiv SSL 错误）前后天都有，
      能被准确捕获；连续多天缺失（多为源停更）不会被误报。
    """
    if target.weekday() >= 5:  # 5=周六, 6=周日
        return []
    manifest_dir = resolve_data_dir("manifest")
    prev_ds = (target - timedelta(days=1)).isoformat()
    next_ds = (target + timedelta(days=1)).isoformat()
    # 后一天是否已有任何 manifest（没有说明后一天还没到或定时任务未跑）
    next_day_has_any = any(manifest_dir.glob(f"*_{next_ds}.json"))

    missing = []
    for src in get_sources(enabled_only=True):
        name = src["name"]
        if (manifest_dir / f"{name}_{target.isoformat()}.json").exists():
            continue
        prev_has = (manifest_dir / f"{name}_{prev_ds}.json").exists()
        next_has = (manifest_dir / f"{name}_{next_ds}.json").exists()
        if prev_has and (next_has or not next_day_has_any):
            missing.append(name)
    return missing


def check_ingest(target: date):
    """
    检查指定日期的抓取完整性。

    三类问题：
    1. missing_manifests —— 活跃源当天异常缺 manifest（判定见 _missing_manifests）
    2. failed —— extraction_status 为 failed/partial
    3. suspicious —— status=success 但正文有质量问题（反爬/ HTML 泄漏/截断快照/过短）
    """
    ds = target.isoformat()
    raw_dir = resolve_data_dir("raw")

    missing_manifests = _missing_manifests(target)

    failed, suspicious = [], []
    for fp, fm, body in _iter_date_files(raw_dir, target):
        rel = str(fp.relative_to(raw_dir))
        status = fm.get("extraction_status", "")
        if status in ("failed", "partial"):
            failed.append({"file": rel, "status": status, "title": fm.get("title", "")})
            continue
        problems = _body_problems(body, source=fp.parent.name)
        if problems:
            suspicious.append({"file": rel, "reasons": problems, "title": fm.get("title", "")})

    _emit(
        {
            "stage": "ingest",
            "date": ds,
            "missing_manifests": missing_manifests,
            "failed": failed,
            "suspicious": suspicious,
        },
        has_issues=bool(missing_manifests or failed or suspicious),
    )


def _is_degraded(old_body: str, new_body: str) -> bool:
    """
    判断修复后的新正文是否反而劣化。

    两种劣化模式（均来自实战）：
    - 新正文变成 HTML 源码（浏览器"部分修复"写入原始 HTML）
    - 新正文长度不到旧正文的一半（如 7.8KB 的 HN 评论摘录被 368 字符的致谢名单覆盖）
    """
    new_text = new_body.strip()
    if new_text.startswith(("<!DOCTYPE", "<html")):
        return True
    return len(new_text) < len(old_body.strip()) * 0.5


def repair_ingest(target: date):
    """
    定点修复指定日期的抓取问题。

    流程（只处理检查出的问题文件，不影响健康文章）：
    1. 内存备份旧正文（用于劣化回滚），把问题文件状态重置为 failed
    2. 调 repair_failed_articles(target_date) 走浏览器重抓（该函数内部按 created 过滤）
    3. 仍失败的逐个用 Jina Reader 新鲜抓取兜底
    4. 劣化回滚：新正文比旧的更差时恢复旧正文（状态标回 success 之外的 partial 以留痕）
    5. 缺 manifest 的源：arxiv-cs-ai 自动调 backfill_arxiv.py 补建并 ingest；
       其他源无法自动补救，在报告中列出由人工决策
    """
    ds = target.isoformat()
    raw_dir = resolve_data_dir("raw")

    # --- 收集问题文件（与 check_ingest 同一套判定，保证 repair 覆盖 check 的报告面）---
    missing_manifests = _missing_manifests(target)
    problem_files: list[Path] = []
    for fp, fm, body in _iter_date_files(raw_dir, target):
        if fm.get("extraction_status", "") in ("failed", "partial") or _body_problems(body, source=fp.parent.name):
            problem_files.append(fp)

    # --- 缺 manifest 补救 ---
    backfilled = []
    for name in missing_manifests:
        if name == "arxiv-cs-ai":
            backfill = Path(__file__).parent / "backfill_arxiv.py"
            proc = subprocess.run(
                ["uv", "run", "python", str(backfill), "--date", ds, "--ingest"],
                cwd=_ROOT, capture_output=True, text=True, timeout=3600,
            )
            ok = proc.returncode == 0
            backfilled.append({"source": name, "success": ok})
            if not ok:
                print(proc.stdout[-2000:], file=sys.stderr)
                print(proc.stderr[-2000:], file=sys.stderr)
        else:
            backfilled.append({"source": name, "success": False, "note": "无自动补救方案，需人工处理"})

    if not problem_files:
        _emit({"stage": "repair-ingest", "date": ds, "backfill": backfilled,
               "repaired": [], "still_failed": [], "rolled_back": []},
              has_issues=any(not b["success"] for b in backfilled))

    # --- 1. 备份旧正文与旧状态 + 重置状态（repair_failed_articles 只扫 failed/partial）---
    old_bodies: dict[Path, str] = {}
    old_statuses: dict[Path, str] = {}
    for fp in problem_files:
        fm, body = read_frontmatter(fp)
        old_bodies[fp] = body
        old_statuses[fp] = fm.get("extraction_status", "failed")
        fm["extraction_status"] = "failed"
        write_frontmatter(fp, fm, body)

    # --- 2. 浏览器重抓（复用现有 repair 实现，含反爬检测）---
    repair_failed_articles(target_date=target)

    # --- 3+4. Jina 兜底 + 劣化回滚 ---
    repaired, still_failed, rolled_back = [], [], []
    for fp in problem_files:
        old_body = old_bodies[fp]
        rel = str(fp.relative_to(raw_dir))

        fm, _ = read_frontmatter(fp)
        if fm.get("extraction_status") != "success":
            # 浏览器仍被拦/失败 → Jina 新鲜抓取兜底
            # 三重把关：反爬页、错误页（404 等）、劣化内容都不接受
            content = fetch_via_jina(fm.get("source", ""), timeout=90)
            if (content and not is_bot_challenge_html(content)
                    and not _is_error_page(content)
                    and not _is_degraded(old_body, content)):
                fm["extraction_status"] = "success"
                write_frontmatter(fp, fm, content)

        # 重新读取最终状态再判定（Jina 可能已改写文件）
        fm, body = read_frontmatter(fp)
        if fm.get("extraction_status") == "success" and not _is_degraded(old_body, body):
            repaired.append(rel)
        elif _is_degraded(old_body, body):
            # 修复反而劣化 → 回滚旧正文与旧状态。
            # 覆盖两种劣化：success 但内容更差；"部分修复"把 HTML 源码写进正文
            # （旧逻辑的漏洞：后者 status=partial 落在 still_failed 分支，垃圾正文被留在盘上）
            fm["extraction_status"] = old_statuses[fp]
            write_frontmatter(fp, fm, old_body)
            rolled_back.append(rel)
        else:
            still_failed.append(rel)

    _emit(
        {
            "stage": "repair-ingest",
            "date": ds,
            "backfill": backfilled,
            "repaired": repaired,
            "rolled_back": rolled_back,
            "still_failed": still_failed,
        },
        has_issues=bool(still_failed) or any(not b["success"] for b in backfilled),
    )


# ---------------------------------------------------------------------------
# Stage 2/3: extract / analyze 检查与修复（同一模式，参数化复用）
# ---------------------------------------------------------------------------
# 判定逻辑与前端 determineProcessingStatus 对齐：
#   extracted = 有 tldr 或 objective_summary；analyzed = 有 impact_score 且 sentiment
# 每个阶段同时检查"上游文件在下游没有对应输出"（阶段根本没跑到该文件）。
# ---------------------------------------------------------------------------

_STAGE_CFG = {
    "extract": {
        "upstream": "raw",          # 输入目录（data/01_raw/）
        "downstream": "extracted",  # 输出目录（data/02_extracted/）
        "cli": "extract",
    },
    "analyze": {
        "upstream": "extracted",    # 输入目录（data/02_extracted/）
        "downstream": "analyzed",   # 输出目录（data/03_analyzed/）
        "cli": "analyze",
    },
}


def _stage_problems(stage: str, target: date) -> list[dict]:
    """
    收集某阶段指定日期的问题文章列表。

    问题定义：
    - missing_output —— 上游有文件但下游没有对应输出（阶段漏跑）
    - stale_output —— 上游文件的修改时间晚于下游输出（典型场景：ingest repair
      更新了正文，但 extract/analyze 结果还基于旧的截断内容，必须重跑）
    - extract 阶段额外判：extract_result==failed，或 tldr/objective_summary 均缺失
    - analyze 阶段额外判：impact_score 或 sentiment 缺失
    """
    cfg = _STAGE_CFG[stage]
    up_dir = resolve_data_dir(cfg["upstream"])
    down_dir = resolve_data_dir(cfg["downstream"])
    problems = []

    for fp, fm, _body in _iter_date_files(up_dir, target):
        rel = fp.relative_to(up_dir)
        out_fp = down_dir / rel
        entry = {"file": str(rel), "title": fm.get("title", "")}
        if not out_fp.exists():
            problems.append({**entry, "reason": "missing_output"})
            continue
        # 过期检测：下游正文与上游正文不一致 → 结果基于旧内容，需重跑。
        # 为什么不用 mtime 对比：后续日期的 ingest 会给老文章补记 manifest_dates
        # （只动 frontmatter 不动正文），mtime 对比会把这些元数据更新误判为过期
        # （实测 07-21 有 17 篇此类误报，正文对比后仅剩真正被 repair 改过的 1 篇）
        try:
            out_fm, out_body = read_frontmatter(out_fp)
        except Exception:
            problems.append({**entry, "reason": "output_unreadable"})
            continue
        if out_body != _body:
            problems.append({**entry, "reason": "stale_output"})
            continue
        if stage == "extract":
            if out_fm.get("extract_result") == "failed":
                problems.append({**entry, "reason": "extract_result=failed"})
            elif not (out_fm.get("tldr") or out_fm.get("objective_summary")):
                problems.append({**entry, "reason": "missing_tldr_and_summary"})
        else:
            if not (out_fm.get("impact_score") and out_fm.get("sentiment")):
                problems.append({**entry, "reason": "missing_impact_score_or_sentiment"})
    return problems


def check_stage(stage: str, target: date):
    """check-extract / check-analyze 的统一实现（只读，JSON 报告）。"""
    problems = _stage_problems(stage, target)
    _emit({"stage": f"check-{stage}", "date": target.isoformat(), "problems": problems},
          has_issues=bool(problems))


def run_stage(stage: str, target: date, max_files: int = 100, allow_large: bool = False):
    """
    run-extract / run-analyze：日期隔离的阶段执行（单进程 + 预检熔断）。

    两道保险（2026-07-29 事故后设计，详见 SKILL.md 设计约束章节）：
    1. 阶段执行统一走 pipeline CLI 的 `--target-date`（日期隔离做在 pipeline
       源码里，单进程单进程跑完只 aggregate 一次，不再逐文件起 90 个子进程）；
    2. 执行前预检：范围内文件数与待处理文件数（= check 口径的问题数）任一
       超过 max_files 即拒绝执行——即使日期过滤逻辑未来出 bug，大批量
       LLM 操作也会被物理拦下。确需大批量时显式传 --allow-large。
    """
    cfg = _STAGE_CFG[stage]
    up_dir = resolve_data_dir(cfg["upstream"])
    ds = target.isoformat()

    # --- 预检：统计范围与工作量（纯本地 frontmatter 扫描，无 LLM 调用）---
    in_scope = sum(1 for _ in _iter_date_files(up_dir, target))
    pending = len(_stage_problems(stage, target))

    if not allow_large and (in_scope > max_files or pending > max_files):
        _emit(
            {
                "stage": f"run-{stage}",
                "date": ds,
                "aborted": True,
                "reason": f"预检熔断: 范围内 {in_scope} 篇 / 待处理 {pending} 篇，"
                          f"超过阈值 {max_files}。确认无误后加 --allow-large 重试",
                "in_scope": in_scope,
                "pending": pending,
            },
            has_issues=True,
        )

    # --- 单进程执行（pipeline CLI 内部完成日期过滤 + skip-existing + 一次 aggregate）---
    # 超时给 4 小时：analyze 是 3 维度 × 篇数的 LLM 调用，60+ 篇远超默认 1800s；
    # skip-existing 保证中断后重跑只处理剩余文件，重复执行成本低
    code, tail = _run_cli([cfg["cli"], "--target-date", ds], timeout=4 * 3600)

    _emit(
        {
            "stage": f"run-{stage}",
            "date": ds,
            "in_scope": in_scope,
            "pending_before": pending,
            "cli_exit": code,
            "cli_tail": tail,
        },
        has_issues=(code != 0),
    )


def repair_stage(stage: str, target: date):
    """
    repair-extract / repair-analyze 的统一实现。

    对每篇问题文章单独调用 `run.py <stage> -i <上游文件> --force`：
    - 单文件粒度，LLM 成本只花在问题文章上
    - --force 忽略 skip-existing，强制重跑
    - CLI 内部会自动 aggregate（多阶段扫描，安全，不会覆盖其他日期数据）
    """
    cfg = _STAGE_CFG[stage]
    up_dir = resolve_data_dir(cfg["upstream"])
    problems = _stage_problems(stage, target)

    repaired, still_failed = [], []
    for p in problems:
        input_fp = up_dir / p["file"]
        code, tail = _run_cli([cfg["cli"], "-i", str(input_fp.relative_to(_ROOT)), "--force"])
        # 修复后重新判定该文件（只查这一个文件，不重扫全天）
        remaining = [x for x in _stage_problems(stage, target) if x["file"] == p["file"]]
        if code == 0 and not remaining:
            repaired.append(p["file"])
        else:
            still_failed.append({**p, "cli_tail": tail})

    _emit({"stage": f"repair-{stage}", "date": target.isoformat(),
           "repaired": repaired, "still_failed": still_failed},
          has_issues=bool(still_failed))


# ---------------------------------------------------------------------------
# 入口
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="指定日期日报流水线门禁：检查与定点修复")
    parser.add_argument(
        "command",
        choices=["check-ingest", "repair-ingest", "run-extract", "check-extract",
                 "repair-extract", "run-analyze", "check-analyze", "repair-analyze"],
    )
    parser.add_argument("--date", "-d", required=True, help="目标日期 YYYY-MM-DD")
    parser.add_argument(
        "--max-files", type=int, default=100,
        help="run-* 预检熔断阈值：范围内或待处理文件数超过该值即拒绝执行 (默认 100)",
    )
    parser.add_argument(
        "--allow-large", action="store_true",
        help="确认要执行大批量操作时绕过预检熔断（需显式声明）",
    )
    args = parser.parse_args()
    target = _parse_date(args.date)

    if args.command == "check-ingest":
        check_ingest(target)
    elif args.command == "repair-ingest":
        repair_ingest(target)
    elif args.command == "run-extract":
        run_stage("extract", target, max_files=args.max_files, allow_large=args.allow_large)
    elif args.command == "check-extract":
        check_stage("extract", target)
    elif args.command == "repair-extract":
        repair_stage("extract", target)
    elif args.command == "run-analyze":
        run_stage("analyze", target, max_files=args.max_files, allow_large=args.allow_large)
    elif args.command == "check-analyze":
        check_stage("analyze", target)
    elif args.command == "repair-analyze":
        repair_stage("analyze", target)


if __name__ == "__main__":
    main()
