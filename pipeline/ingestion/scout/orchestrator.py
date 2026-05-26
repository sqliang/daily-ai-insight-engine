"""
pipeline/ingestion/scout/orchestrator.py — 主编排器

Stage 1a 入口函数 run_scout() 的实现。负责遍历启用数据源、按 fetch_strategy 分发
到对应策略函数、应用过滤规则、生成文章 ID、写入 JSON 清单。

设计理由：
    - 编排逻辑与策略实现分离，新增抓取策略只需在 strategies.py 添加函数并在此 dispatch
    - Browser session 在所有 browser 策略的源之间复用，避免重复启动 Chromium
    - 每个源的清单独立写入，单个源失败不影响其他源（fail-per-source 策略）
"""

import logging
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from pipeline.core.config_loader import get_sources

logger = logging.getLogger(__name__)

from pipeline.core.config_loader import resolve_data_dir
from pipeline.utils.file_utils import write_json
from pipeline.utils.id_utils import generate_id
from pipeline.ingestion.filters import apply_filters
from pipeline.ingestion.scout.strategies import (
    _ensure_browser_session,
    _scout_rss,
    _scout_api,
    _scout_scrape,
    _scout_browser,
)
from pipeline.ingestion.scout.manifest_writer import _generate_markdown_manifest


def run_scout(force: bool = False) -> Dict[str, List[dict]]:
    """
    主编排器：遍历所有启用的数据源，生成当日 URL 清单。

    流程：
        1. 读取 config.yaml 中所有 enabled 的数据源
        2. 若存在 browser 策略的源，预先创建共享 BrowserSession
        3. 按源逐个：检查已有清单 → 按策略抓取 → 过滤 → 生成 ID → 写入 JSON
        4. 生成汇总 Markdown 清单
        5. 清理 BrowserSession

    参数：
        force: True 时忽略已存在的当日清单，强制重新抓取

    返回：
        Dict[str, List[dict]]: {source_name: [articles]} 字典

    异常：
        不抛出 — 单个源抓取失败通过 print 报告后继续处理下一个源
    """
    sources = get_sources(enabled_only=True)
    today_str = date.today().isoformat()
    manifest_dir = resolve_data_dir("manifest")
    all_manifests: Dict[str, List[dict]] = {}

    logger.info("Scout 开始 sources=%d today=%s", len(sources), today_str)


    # 检测是否有 browser 策略的源，提前创建 browser session（复用 Chromium 实例）
    needs_browser = any(s.get("fetch_strategy") == "browser" for s in sources)
    browser_session = None
    if needs_browser:
        browser_session = _ensure_browser_session().__enter__()

    try:
        for source in sources:
            name = source.get("name", "")
            strategy = source.get("fetch_strategy", "rss")

            # 检查是否已有今日清单
            manifest_path = manifest_dir / f"{name}_{today_str}.json"
            if manifest_path.exists() and not force:
                print(f"  [跳过] {name} — 今日清单已存在: {manifest_path.name}")
                continue

            # 根据抓取策略分发
            print(f"  [抓取] {name} (strategy={strategy})...")
            articles: List[dict] = []

            try:
                if strategy == "rss":
                    articles = _scout_rss(source)
                elif strategy == "api":
                    articles = _scout_api(source)
                elif strategy == "scrape":
                    articles = _scout_scrape(source)
                elif strategy == "browser":
                    articles = _scout_browser(source, browser_session)
                else:
                    logger.warning("未知抓取策略 source=%s strategy=%s", name, strategy)
                    print(f"         未知抓取策略: {strategy}，跳过")
                    continue
            except Exception as e:
                logger.error("抓取失败 source=%s strategy=%s: %s", name, strategy, e)
                print(f"         ❌ 抓取失败: {e}")
                continue

            if not articles:
                print(f"         无新文章")
                continue

            # 应用过滤规则
            articles = apply_filters(articles, source)
            print(f"         获取 {len(articles)} 篇 (过滤后)")

            # 为每篇文章生成唯一 ID
            for article in articles:
                article["id"] = generate_id(article.get("url", ""))

            # 写入清单文件
            manifest_data = {
                "source": name,
                "source_type": source.get("type", ""),
                "tier": source.get("tier", ""),
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "date": today_str,
                "articles": articles,
            }
            write_json(manifest_path, manifest_data)

            all_manifests[name] = articles

        # 生成汇总 Markdown 清单
        _generate_markdown_manifest(all_manifests, manifest_dir, today_str, sources)

    finally:
        if browser_session:
            browser_session.__exit__(None, None, None)

    total = sum(len(v) for v in all_manifests.values())
    logger.info("Scout 完成 sources=%d articles=%d", len(all_manifests), total)
    return all_manifests
