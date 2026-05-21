"""
pipeline/ingestion/scout — Stage 1a: URL 清单生成器

读取 pipeline/config.yaml → 遍历启用的数据源 → 抓取 RSS/API 获取文章列表 →
生成 JSON 清单文件到 data/00_manifest/{source_name}_{YYYYMMDD}.json。

清单文件是轻量级的"待办任务列表"，供 ingest.py 消费，也支持断点续传：
如果某天的清单已存在，默认跳过该源（除非指定 --force）。

包结构：
    orchestrator.py   — 主编排器 run_scout()
    strategies.py     — 抓取策略实现 (_scout_rss / _scout_api / _scout_scrape / _scout_browser)
    manifest_writer.py — Markdown 汇总清单生成
"""

from pipeline.ingestion.scout.orchestrator import run_scout
