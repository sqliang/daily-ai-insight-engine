#!/usr/bin/env python3
"""
backfill_substack.py — 补建指定日期 Substack 系数据源的 scout manifest

被 pipeline_gate.py 的 repair-ingest 在发现 Substack 系源当天 manifest 缺失时可调用，
也可独立使用：

    uv run python .agents/skills/daily-report-pipeline/scripts/backfill_substack.py --source bensbites --date YYYY-MM-DD [--ingest]

## 适用范围

Substack 平台的源（bensbites / therundown / theneuron / importai / oneusefulthing 等）。
判断依据：config.yaml 中源 url 的域名支持 /api/v1/archive 接口即可。

## 为什么不能直接用现有 scout

这些源的 RSS 只含最新若干篇，无法按历史日期回溯（2026-07-30 实战：
scout 失败导致 bensbites 当天的《1 Billion ChatGPT users》缺失）。

## 本脚本的方案（Substack archive API）

Substack 提供公开的分页存档接口：

    https://<域名>/api/v1/archive?sort=new&search=&offset=0&limit=15

按发布时间倒序返回文章元数据（含 canonical URL、标题、发布日期、摘要、作者）。
脚本翻页查找目标日期的文章，按 scout manifest 格式写出，再可选自动 ingest。

口径说明：post_date 为 UTC 时间，与 RSS 的 published 口径一致；只取 post_date 当天
的文章，不做关键词过滤（这些源在 config.yaml 中本身无关键词配置）。
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

# 单次翻页大小（archive API 上限约 50）
_PAGE_SIZE = 15
# 最多翻页数（防止目标日期很早时无限翻页；15 篇/页 × 20 页 ≈ 覆盖数月）
_MAX_PAGES = 20


def _fetch_archive_page(base_url: str, offset: int) -> list[dict]:
    """
    抓取一页 Substack archive（带重试）。

    参数：
        base_url: 源的站点根 URL（如 https://www.bensbites.com）
        offset: 分页偏移

    返回：
        list[dict]: 文章元数据列表（空列表表示已到末页）
    """
    query = urllib.parse.urlencode({"sort": "new", "search": "", "offset": offset, "limit": _PAGE_SIZE})
    url = f"{base_url.rstrip('/')}/api/v1/archive?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "daily-ai-insight-engine/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            wait = (attempt + 1) * 10
            print(f"  archive 抓取失败({e})，{wait}s 后重试 ({attempt + 1}/3)...", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Substack archive API 抓取失败: {url}")


def find_posts_on_date(base_url: str, target: date) -> list[dict]:
    """
    翻页查找目标日期（UTC）发布的文章。

    archive 按发布时间倒序排列：遇到比目标日期更早的文章即可停止翻页。
    """
    ds = target.isoformat()
    posts = []
    for page in range(_MAX_PAGES):
        entries = _fetch_archive_page(base_url, offset=page * _PAGE_SIZE)
        if not entries:
            break
        for e in entries:
            post_date = (e.get("post_date") or "")[:10]
            if post_date == ds:
                posts.append(e)
            elif post_date < ds:
                # 已经翻到过目标日期之前，后续不可能再有目标日期的文章
                return posts
        if page > 0:
            time.sleep(3)  # 翻页间隔，礼貌限速
    return posts


def backfill(source_name: str, target: date, do_ingest: bool) -> int:
    """
    补建指定 Substack 源在目标日期的 manifest，可选自动 ingest。

    返回：
        int: 0 = 成功（含"当天本无新文章"），1 = 失败
    """
    ds = target.isoformat()
    source = get_source_by_name(source_name)
    if not source:
        print(f"错误: config.yaml 中找不到 {source_name} 源配置", file=sys.stderr)
        return 1
    base_url = source.get("url", "")
    # config 中 url 可能是 RSS 路径（如 /feed），取其站点根
    parsed = urllib.parse.urlparse(base_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    posts = find_posts_on_date(base_url, target)
    print(f"{source_name}: {ds} 当天 archive 中找到 {len(posts)} 篇")

    if not posts:
        # 当天本无新文章是正常情况（稀疏源），不算失败
        print("该源当天无新文章，无需补建 manifest")
        return 0

    articles = []
    for p in posts:
        url = p.get("canonical_url") or p.get("url", "")
        if not url:
            continue
        articles.append({
            "url": url,
            "title": p.get("title", ""),
            "published": (p.get("post_date") or "")[:10],
            "summary": p.get("description") or p.get("subtitle") or "",
            "author": (p.get("publishedBylines") or [{}])[0].get("name", ""),
            "id": generate_id(url),
        })

    manifest = {
        "source": source_name,
        "source_type": source.get("type", ""),
        "tier": source.get("tier", ""),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "date": ds,
        "articles": articles,
    }
    out = resolve_data_dir("manifest") / f"{source_name}_{ds}.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 已写入 {out}（{len(articles)} 篇）")
    for a in articles:
        print(f"  - {a['published']} {a['title'][:70]}")

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
    parser = argparse.ArgumentParser(description="补建 Substack 系源指定日期的 manifest")
    parser.add_argument("--source", "-s", required=True, help="数据源名（须为 config.yaml 中 Substack 平台的源）")
    parser.add_argument("--date", "-d", required=True, help="目标日期 YYYY-MM-DD")
    parser.add_argument("--ingest", action="store_true", help="补建后自动执行 ingest")
    args = parser.parse_args()
    try:
        target = date.fromisoformat(args.date)
    except ValueError:
        print(f"错误: --date 格式无效: {args.date}", file=sys.stderr)
        sys.exit(2)
    sys.exit(backfill(args.source, target, args.ingest))


if __name__ == "__main__":
    main()
