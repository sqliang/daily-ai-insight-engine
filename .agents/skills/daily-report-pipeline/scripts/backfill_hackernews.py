#!/usr/bin/env python3
"""
backfill_hackernews.py — 补建指定日期的 hackernews scout manifest

被 pipeline_gate.py 的 repair-ingest 在发现 hackernews 当天 manifest 缺失时可调用，
也可独立使用：

    uv run python .agents/skills/daily-report-pipeline/scripts/backfill_hackernews.py --date YYYY-MM-DD [--ingest]

## 为什么不能直接用现有 scout

hackernews 源的信息源是 hnrss.org 的"当日首页" RSS（points>=100），只含当前内容，
无法回溯历史日期（2026-07-28 实战：scout 失败导致当天 HN 文章数为 0）。

## 本脚本的方案（Algolia HN API 日期范围查询）

Algolia 官方 HN API 支持按创建时间和分数过滤，可以复刻 hnrss 的口径：

    https://hn.algolia.com/api/v1/search?tags=story
        &numericFilters=created_at_i>=<当天0点UTC>,created_at_i<<次日0点UTC>,points>=100

口径说明：hnrss 的"frontpage"是当日上过首页的帖子，本方案是"当天创建且 points>=100
的帖子"——两者高度重叠但不完全等同（个别帖子可能隔天才上首页），这是回溯场景下的
最佳近似。分数阈值与 config.yaml 中 hackernews 源的配置（points>=100）保持一致。
"""

import argparse
import json
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
import contextlib

with contextlib.redirect_stdout(sys.stderr):
    setup_proxy()

from pipeline.core.config_loader import get_source_by_name, resolve_data_dir
from pipeline.utils.id_utils import generate_id

import subprocess

# 与 config.yaml 中 hackernews 源一致的分数阈值（hnrss.org/frontpage?points=100）
_MIN_POINTS = 100


def fetch_hn_stories(target: date) -> list[dict]:
    """
    通过 Algolia HN API 查询指定日期创建且 points>=100 的 HN 帖子。

    参数：
        target: 目标日期（按 UTC 日界过滤，与 HN/Algolia 的时区口径一致）

    返回：
        list[dict]: Algolia hits 原始条目列表（按分数降序）
    """
    start_ts = int(datetime(target.year, target.month, target.day, tzinfo=timezone.utc).timestamp())
    end_ts = start_ts + 86400
    query = urllib.parse.urlencode({
        "tags": "story",
        "numericFilters": f"created_at_i>={start_ts},created_at_i<{end_ts},points>={_MIN_POINTS}",
        "hitsPerPage": 100,
    })
    url = f"https://hn.algolia.com/api/v1/search?{query}"

    req = urllib.request.Request(url, headers={"User-Agent": "daily-ai-insight-engine/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                hits = data.get("hits", [])
                return sorted(hits, key=lambda h: h.get("points", 0), reverse=True)
        except Exception as e:
            wait = (attempt + 1) * 10
            print(f"  Algolia 查询失败({e})，{wait}s 后重试 ({attempt + 1}/3)...", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Algolia HN API 查询失败: {url}")


def backfill(target: date, do_ingest: bool) -> int:
    """
    补建指定日期的 hackernews manifest，可选自动 ingest。

    返回：
        int: 0 = 成功，1 = 失败（查询失败 / 结果为空 / 源配置缺失）
    """
    ds = target.isoformat()
    source = get_source_by_name("hackernews")
    if not source:
        print("错误: config.yaml 中找不到 hackernews 源配置", file=sys.stderr)
        return 1

    hits = fetch_hn_stories(target)
    print(f"Algolia 返回 {len(hits)} 篇（created={ds} 且 points>={_MIN_POINTS}）")
    if not hits:
        print("错误: 查询结果为空（日期可能过久或阈值过高）", file=sys.stderr)
        return 1

    # 转换为 scout 文章格式（与 RSS 策略输出对齐）
    # HN 帖子可能无外链（Ask HN 等自帖），此时用 HN 评论页作为 URL
    articles = []
    for h in hits:
        url = h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}"
        published = (h.get("created_at") or "")[:10]
        articles.append({
            "url": url,
            "title": h.get("title", ""),
            "published": published,
            "summary": "",
            "author": h.get("author", ""),
            "id": generate_id(url),
        })

    manifest = {
        "source": "hackernews",
        "source_type": source.get("type", ""),
        "tier": source.get("tier", ""),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "date": ds,
        "articles": articles,
    }
    out = resolve_data_dir("manifest") / f"hackernews_{ds}.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 已写入 {out}（{len(articles)} 篇）")
    for a in articles[:5]:
        print(f"  - {a['title'][:70]}")

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
    parser = argparse.ArgumentParser(description="补建指定日期的 hackernews manifest")
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
