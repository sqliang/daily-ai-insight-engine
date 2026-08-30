#!/usr/bin/env python3
"""
backfill_github_trending.py — 补建指定日期的 github-trending scout manifest

被 pipeline_gate.py 的 repair-ingest 在发现 github-trending 当天 manifest 缺失时可调用，
也可独立使用：

    uv run python .agents/skills/daily-report-pipeline/scripts/backfill_github_trending.py --date YYYY-MM-DD [--ingest]

## 为什么不能直接用现有 scout

github-trending 原主源是第三方 RSS 镜像（GitHubTrendingRSS），不定期 rebuild（隔 1~3 天）。
停更日返回空或与上日完全重复的榜单，导致当天 manifest 缺失或 0 新文章（2026-08-27/08-28
事故复盘）。github.com/trending 是实时页面，本身无法回溯历史日期。

## 本脚本的方案（Wayback Machine 快照回溯）

web.archive.org 会不定期归档 github.com/trending 页面。通过 CDX API 查指定日期的
全部快照，选最接近当日 scout 时间（09:30 UTC，即定时任务 17:30 北京时间）的那份，
解析快照 HTML 中的热门仓库列表，复刻 scout 的产物（manifest + 关键词过滤）。

口径说明（如实告知用户）：
  1. 快照是「某时刻的 trending 榜单」，与 scout 定时任务应抓取的时点存在小幅偏差。
     本脚本合并当日全部快照的仓库并集，以逼近当天「出现过的完整榜单」，避免单份
     快照因时点偏差漏掉当天独有的仓库。
  2. trending 榜单多日稳定，多数仓库在相邻日期已被 ingest（URL 去重），回溯通常只能
     补到「首次进入榜单」的少量仓库——这是历史补账的固有近似，无法还原完整榜单。
"""

import argparse
import contextlib
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# 环境初始化（脚本位于 .agents/skills/daily-report-pipeline/scripts/，向上 4 级为根）
# ---------------------------------------------------------------------------
_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_ROOT))

from dotenv import load_dotenv

load_dotenv(_ROOT / ".env")

from pipeline.core.proxy_utils import setup_proxy

# 初始化打印重定向到 stderr，保持 stdout 输出干净（便于调用方解析）
with contextlib.redirect_stdout(sys.stderr):
    setup_proxy()

from pipeline.core.config_loader import get_source_by_name, resolve_data_dir
from pipeline.ingestion.filters import apply_filters
from pipeline.utils.id_utils import generate_id

# 与 config.yaml 中 github-trending 源一致的抓取目标（直连 trending 页）
_TRENDING_URL = "https://github.com/trending"

# trending 页中非仓库的链接路径前缀（登录页、赞助位、话题聚合页等）
_NON_REPO_PREFIXES = (
    "features", "security", "solutions", "resources", "enterprise",
    "open-source", "sponsors", "trending", "collections", "topics",
    "login", "settings", "marketplace", "apps", "about", "pricing", "events",
)

# 请求间隔（避免触发 archive.org 限流）
_REQUEST_INTERVAL = 5


def _http_get_json(url: str) -> dict:
    """
    GET 请求并解析 JSON，带 UA 头与 3 次指数退避重试。

    异常：
        RuntimeError: 3 次重试均失败
    """
    req = urllib.request.Request(url, headers={"User-Agent": "daily-ai-insight-engine/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            wait = (attempt + 1) * 10
            print(f"  GET 失败({exc})，{wait}s 后重试 ({attempt + 1}/3)...", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"GET 失败: {url}")


def _query_snapshot_timestamps(target: date) -> list[str]:
    """
    通过 Wayback CDX API 查询指定日期的 github.com/trending 全部快照时间戳。

    参数：
        target: 目标日期（本地日界）

    返回：
        list[str]: 快照时间戳列表（YYYYMMDDHHMMSS，按时间升序）
    """
    day = target.strftime("%Y%m%d")
    params = urllib.parse.urlencode({
        "url": "github.com/trending",
        "from": f"{day}000000",
        "to": f"{day}235959",
        "output": "json",
        "filter": "statuscode:200",
    })
    url = f"http://web.archive.org/cdx/search/cdx?{params}"
    rows = _http_get_json(url)
    # CDX 返回 [["urlkey","timestamp",...], ...]，首行是表头
    timestamps = [r[1] for r in rows[1:]]
    return sorted(timestamps)


def _fetch_snapshot_html(timestamp: str) -> str:
    """
    fetch 指定时间戳的快照 HTML（follow redirect，带重试）。

    参数：
        timestamp: 快照时间戳（YYYYMMDDHHMMSS）

    返回：
        str: 快照 HTML 全文
    """
    url = f"http://web.archive.org/web/{timestamp}/{_TRENDING_URL}"
    req = urllib.request.Request(url, headers={"User-Agent": "daily-ai-insight-engine/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                return resp.read().decode("utf-8", errors="ignore")
        except Exception as exc:
            wait = (attempt + 1) * 10
            print(f"  fetch 快照失败({exc})，{wait}s 后重试 ({attempt + 1}/3)...", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"fetch 快照失败: {url}")


def _extract_repos(html: str) -> list[dict]:
    """
    解析快照 HTML，提取热门仓库列表。

    每个仓库对应一个 <article class="Box-row"> 块；标题链接在块内 <h2> 中，
    简介在 <p class="...col-9..."> 中。Wayback 会把链接改写为
    /web/{ts}/https://github.com/{owner}/{repo}，用 github.com/{owner}/{repo}
    子串匹配即可兼容两种形式。

    返回：
        list[dict]: 每篇含 url/title/summary/published/author，title 为 owner/repo 格式
    """
    blocks = re.split(r'<article class="Box-row">', html)[1:]
    repos: list[dict] = []
    for block in blocks:
        # 标题链接：<h2 ...><a href="...">
        h2m = re.search(r'<h2[^>]*>.*?<a[^>]*href="([^"]+)"', block, re.DOTALL)
        if not h2m:
            continue
        mm = re.search(r'github\.com/([^/"]+)/([^/"?]+)', h2m.group(1))
        if not mm:
            continue
        owner, repo = mm.group(1), mm.group(2)
        if owner in _NON_REPO_PREFIXES:
            continue

        # 简介：<p class="...col-9...">...</p>（仓库 About 描述）
        summary = ""
        dm = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', block, re.DOTALL)
        if dm:
            summary = re.sub(r"<[^>]+>", "", dm.group(1)).strip()

        repos.append({
            "url": f"https://github.com/{owner}/{repo}",
            "title": f"{owner}/{repo}",
            "summary": summary,
            "published": "",
            "author": "",
        })
    return repos


def _merge_repos(timestamps: list[str]) -> list[dict]:
    """
    合并指定日期全部快照的仓库并集。

    每份快照只反映 trending 榜单一时刻的快照，全天多份快照的并集能逼近当天
    「出现过的完整榜单」，避免单份快照因时点偏差漏掉当天独有的仓库。

    返回：
        list[dict]: 按 url 去重后的仓库列表，summary 取多份快照中最长的
    """
    merged: dict[str, dict] = {}
    for i, ts in enumerate(timestamps):
        if i > 0:
            time.sleep(_REQUEST_INTERVAL)  # 避免连续请求 archive.org
        html = _fetch_snapshot_html(ts)
        repos = _extract_repos(html)
        for repo in repos:
            url = repo["url"]
            if url not in merged:
                merged[url] = repo
            elif len(repo.get("summary", "")) > len(merged[url].get("summary", "")):
                merged[url]["summary"] = repo["summary"]
        print(f"  快照 {ts[8:10]}:{ts[10:12]}:{ts[12:14]} UTC: {len(repos)} 个，累计并集 {len(merged)} 个")
    return list(merged.values())


def backfill(target: date, do_ingest: bool) -> int:
    """
    补建指定日期的 github-trending manifest，可选自动 ingest。

    返回：
        int: 0 = 成功，1 = 失败（无快照 / 结果为空 / 源配置缺失）
    """
    ds = target.isoformat()
    source = get_source_by_name("github-trending")
    if not source:
        print("错误: config.yaml 中找不到 github-trending 源配置", file=sys.stderr)
        return 1

    timestamps = _query_snapshot_timestamps(target)
    print(f"Wayback 快照数: {len(timestamps)}")
    if not timestamps:
        print("错误: Wayback Machine 无该日期的 github.com/trending 快照", file=sys.stderr)
        return 1

    repos = _merge_repos(timestamps)
    print(f"全天并集仓库: {len(repos)} 个")

    # 复刻 scout 的过滤口径（关键词 + 时效 + 数量裁剪）
    filtered = apply_filters(repos, source)
    print(f"过滤后（关键词命中）: {len(filtered)} 个")
    for a in filtered:
        print(f"  - {a['title']}  |  {a['summary'][:60]}")

    if not filtered:
        print("警告: 过滤后无仓库（可能当天榜单无 AI 相关项目）", file=sys.stderr)
        # 仍写 manifest（空文章），与 scout「无新文章不写 manifest」不同——这里
        # 用户显式补建，保留空清单以消除 missing_manifests 告警
        articles = []
    else:
        articles = [
            {
                "url": a["url"],
                "title": a["title"],
                "published": a.get("published", ""),
                "summary": a.get("summary", ""),
                "author": a.get("author", ""),
                "id": generate_id(a["url"]),
            }
            for a in filtered
        ]

    manifest = {
        "source": "github-trending",
        "source_type": source.get("type", ""),
        "tier": source.get("tier", ""),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "date": ds,
        "articles": articles,
    }
    out = resolve_data_dir("manifest") / f"github-trending_{ds}.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 已写入 {out}（{len(articles)} 篇）")

    if do_ingest:
        print("执行 ingest ...")
        proc = subprocess.run(
            ["uv", "run", "python", "pipeline/run.py", "ingest", "--manifest", out.name],
            cwd=_ROOT,
        )
        if proc.returncode != 0:
            print("错误: ingest 失败", file=sys.stderr)
            return 1
        print("✅ ingest 完成")
    return 0


def main():
    parser = argparse.ArgumentParser(description="补建指定日期的 github-trending manifest（Wayback 回溯）")
    parser.add_argument("--date", "-d", required=True, help="目标日期 YYYY-MM-DD")
    parser.add_argument("--ingest", action="store_true", help="补建后自动执行 ingest")
    args = parser.parse_args()
    try:
        target = date.fromisoformat(args.date)
    except ValueError:
        print(f"错误: --date 格式无效: {args.date}", file=sys.stderr)
        sys.exit(2)
    sys.exit(backfill(target, args.ingest))


if __name__ == "__main__":
    main()
