#!/usr/bin/env python3
"""
backfill_arxiv.py — 补建指定日期的 arxiv-cs-ai scout manifest

被 pipeline_gate.py 的 repair-ingest 在发现 arxiv 当天 manifest 缺失时自动调用，
也可独立使用：

    uv run python .agents/skills/daily-report-pipeline/scripts/backfill_arxiv.py --date YYYY-MM-DD [--ingest]

## 为什么不能用现有 scout

- Scout CLI 没有 --source/--target-date，且 RSS (rss.arxiv.org/rss/cs.AI) 只含当天
  新论文，无法回溯；
- arXiv API (export.arxiv.org) 支持 submittedDate 范围查询，但限流敏感
  （2026-07-21 实战连续返回 "Rate exceeded"），且 submittedDate 是"提交日"，
  与 RSS 的"公告日"口径不同。

## 本脚本的方案（公告日口径，最贴近当天 RSS 会抓到的内容）

arXiv ID 按提交顺序连续编号，同一天公告的论文在 ID 上是连续区间。因此：

1. 读取相邻日期（前后各最多 5 天内）的 arxiv manifest，取前一天批次最大 ID 与
   后一天批次最小 ID 作为目标日期的 ID 区间 (lo, hi)；
2. 抓取 https://arxiv.org/list/cs.AI/{YYYY-MM} 月度列表页（含标题/作者，无摘要），
   筛出 ID 落在 (lo, hi) 内的论文，即为目标日期公告的批次；
3. 按 config.yaml 的关键词过滤（标题维度）+ limit 截取，生成标准 manifest；
4. --ingest 时自动执行 `run.py ingest --manifest ...` 完成正文抓取
   （ingest 会把 created 设为 manifest 的 date，日期口径正确）。

## 已知近似与边界

- 区间端点取自相邻 manifest 的"保留集合"（每天 limit 15 后的留存），边界处可能
  有个别论文日期归属偏差；但因为关键词过滤后还要截 limit，实际影响极小；
- 列表页无摘要，关键词过滤是标题维度（RSS 流程是标题+摘要，命中率近 100%，
  标题维度偏严格但更安全）；
- 若相邻 5 天内没有任何 arxiv manifest 可用于定位区间，脚本会报错退出
  （此时只能等 arXiv API 限流窗口后改用 submittedDate 口径人工补建）。
"""

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import date, datetime, timedelta, timezone
from html import unescape
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
import contextlib

with contextlib.redirect_stdout(sys.stderr):
    setup_proxy()

import urllib.request

from pipeline.core.config_loader import get_source_by_name, resolve_data_dir
from pipeline.ingestion.filters import filter_by_keywords, filter_by_limit
from pipeline.utils.id_utils import generate_id

# 月度列表页每次请求间隔（秒）。arXiv 限流敏感，宁可慢不可被封
_FETCH_INTERVAL = 10
# 列表页单页最大条目数（页面支持 show=2000）
_PAGE_SIZE = 2000
# 定位 ID 区间时，相邻 manifest 的最大搜索跨度（天）
_NEIGHBOR_SCAN_DAYS = 5


# ---------------------------------------------------------------------------
# arXiv ID 工具（ID 形如 2607.15781 = 2026年7月第15781号，按提交顺序递增）
# ---------------------------------------------------------------------------

def _id_key(arxiv_id: str) -> tuple[int, int]:
    """把 2607.15781 转成可比较的 (2607, 15781) 元组，跨月也能正确排序。"""
    ym, seq = arxiv_id.split(".")
    return int(ym), int(seq)


def _bracket_from_neighbors(target: date) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    从相邻日期的 arxiv manifest 推算目标日期的 ID 区间 (lo, hi)。

    lo = 之前最近一天批次中的最大 ID；hi = 之后最近一天批次中的最小 ID。
    目标日期公告的论文 ID 严格落在 (lo, hi) 开区间内。

    异常：
        RuntimeError: 前后 5 天内找不到可用于定位的 manifest
    """
    manifest_dir = resolve_data_dir("manifest")
    lo = hi = None

    for delta in range(1, _NEIGHBOR_SCAN_DAYS + 1):
        if lo is None:
            prev = manifest_dir / f"arxiv-cs-ai_{target - timedelta(days=delta)}.json"
            if prev.exists():
                ids = [a["url"].split("/abs/")[-1] for a in json.loads(prev.read_text())["articles"]]
                if ids:
                    lo = max(_id_key(i) for i in ids)
        if hi is None:
            nxt = manifest_dir / f"arxiv-cs-ai_{target + timedelta(days=delta)}.json"
            if nxt.exists():
                ids = [a["url"].split("/abs/")[-1] for a in json.loads(nxt.read_text())["articles"]]
                if ids:
                    hi = min(_id_key(i) for i in ids)
        if lo and hi:
            break

    if not lo or not hi:
        raise RuntimeError(
            f"前后 {_NEIGHBOR_SCAN_DAYS} 天内未找到可用的 arxiv manifest，无法定位 "
            f"{target} 的 ID 区间。请等 arXiv API 限流解除后改用 submittedDate 口径人工补建。"
        )
    if lo >= hi:
        raise RuntimeError(f"相邻 manifest 的 ID 区间异常: lo={lo} hi={hi}")
    return lo, hi


# ---------------------------------------------------------------------------
# 月度列表页抓取与解析
# ---------------------------------------------------------------------------

def _fetch_month_page(month: str, skip: int) -> str:
    """
    抓取 cs.AI 月度列表页（带重试与限流间隔）。

    参数：
        month: YYYY-MM 格式（URL 路径段）
        skip: 分页偏移（每页最多 _PAGE_SIZE 条）

    返回：
        str: 页面 HTML
    """
    url = f"https://arxiv.org/list/cs.AI/{month}?skip={skip}&show={_PAGE_SIZE}"
    req = urllib.request.Request(url, headers={"User-Agent": "daily-ai-insight-engine/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as e:
            # 限流/网络抖动时退避重试（10s → 30s → 60s）
            wait = (attempt + 1) * 30 if attempt else _FETCH_INTERVAL
            print(f"  列表页抓取失败({e})，{wait}s 后重试 ({attempt + 1}/3)...", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"月度列表页抓取失败: {url}")


# 单条论文的解析正则：abs 链接 + 标题 + 作者（列表页无摘要）
_ENTRY_RE = re.compile(
    r'href ="/abs/(\d{4}\.\d{4,5})".*?list-title mathjax\'><span class=\'descriptor\'>Title:</span>'
    r"\s*(.*?)\s*</div>\s*<div class='list-authors'>(.*?)</div>",
    re.S,
)


def _parse_entries(html: str) -> list[tuple[str, str, str]]:
    """解析列表页 HTML，返回 [(arxiv_id, title, authors), ...]（按页面顺序 = ID 升序）。"""
    entries = []
    for m in _ENTRY_RE.finditer(html):
        aid, title, authors = m.groups()
        title = unescape(re.sub(r"<[^>]+>", "", title)).strip()
        auth = unescape(re.sub(r"<[^>]+>", "", authors)).strip()
        auth = re.sub(r"^Authors?:\s*", "", auth)
        entries.append((aid, " ".join(title.split()), " ".join(auth.split())))
    return entries


def _fetch_month_entries(month: str) -> list[tuple[str, str, str]]:
    """抓完一个月份的全部列表页（分页直到取尽）。"""
    entries: list[tuple[str, str, str]] = []
    skip = 0
    while True:
        if skip > 0:
            time.sleep(_FETCH_INTERVAL)  # 分页间隔，避免触发限流
        html = _fetch_month_page(month, skip)
        page = _parse_entries(html)
        entries.extend(page)
        # 页面页脚 "Total of N entries" 用于判断是否取尽
        total_m = re.search(r"Total of (\d+) entries", html)
        total = int(total_m.group(1)) if total_m else len(entries)
        if len(entries) >= total or not page:
            break
        skip += _PAGE_SIZE
    return entries[:total] if total_m else entries


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def backfill(target: date, do_ingest: bool) -> int:
    """
    补建指定日期的 arxiv manifest，可选自动 ingest。

    返回：
        int: 0 = 成功，1 = 失败（区间无法定位 / 列表页抓取失败 / 过滤后为空）
    """
    ds = target.isoformat()
    source = get_source_by_name("arxiv-cs-ai")
    if not source:
        print("错误: config.yaml 中找不到 arxiv-cs-ai 源配置", file=sys.stderr)
        return 1

    # 1. 定位 ID 区间
    try:
        lo, hi = _bracket_from_neighbors(target)
    except RuntimeError as e:
        print(f"错误: {e}", file=sys.stderr)
        return 1
    print(f"ID 区间: ({lo[0]}.{lo[1]}, {hi[0]}.{hi[1]})")

    # 2. 抓取区间覆盖的月份列表页（月初/月末日期可能跨两个月）
    months = sorted({f"20{str(lo[0])[:2]}-{str(lo[0])[2:]}", f"20{str(hi[0])[:2]}-{str(hi[0])[2:]}"})
    entries: list[tuple[str, str, str]] = []
    for month in months:
        print(f"抓取月度列表: {month} ...")
        entries.extend(_fetch_month_entries(month))
    # 去重（跨月时相邻页可能重叠）并按 ID 排序
    seen = {}
    for e in entries:
        seen[e[0]] = e
    entries = sorted(seen.values(), key=lambda e: _id_key(e[0]))
    print(f"列表页共 {len(entries)} 条")

    # 3. 筛出目标日期批次（ID 严格落在开区间内）
    batch = [e for e in entries if lo < _id_key(e[0]) < hi]
    print(f"{ds} 批次候选: {len(batch)} 篇")
    if not batch:
        print("错误: 区间内无论文（区间定位可能有误）", file=sys.stderr)
        return 1

    # 4. 关键词过滤 + limit（复刻 config；跳过时效过滤——日期已由区间锁定）
    articles = [
        {"url": f"https://arxiv.org/abs/{aid}", "title": t, "author": a, "summary": ""}
        for aid, t, a in batch
    ]
    articles = filter_by_keywords(articles, source.get("filter", {}).get("keywords", []))
    print(f"关键词过滤后: {len(articles)} 篇")
    articles = filter_by_limit(articles, source.get("limit", 0))
    if not articles:
        print("错误: 关键词过滤后为空", file=sys.stderr)
        return 1
    print(f"limit 裁剪后: {len(articles)} 篇")

    # 5. 写 manifest（格式与 scout 输出完全一致；published 用公告日近似）
    for a in articles:
        a["id"] = generate_id(a["url"])
        a["published"] = ds
    manifest = {
        "source": "arxiv-cs-ai",
        "source_type": source.get("type", ""),
        "tier": source.get("tier", ""),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "date": ds,
        "articles": articles,
    }
    out = resolve_data_dir("manifest") / f"arxiv-cs-ai_{ds}.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 已写入 {out}（{len(articles)} 篇）")

    # 6. 可选：自动 ingest（created 会被设为 manifest 的 date，日期口径正确）
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
    parser = argparse.ArgumentParser(description="补建指定日期的 arxiv-cs-ai manifest")
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
