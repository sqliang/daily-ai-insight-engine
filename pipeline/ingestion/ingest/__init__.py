"""
pipeline/ingestion/ingest — Stage 1b: 正文抓取与清洗

读取 data/00_manifest/ 中的 JSON 清单 → 逐篇抓取网页正文并提取为干净 Markdown →
写入 data/01_raw/{source}/{id}.md，附带标准 YAML frontmatter。

包结构：
    cli.py           — CLI 契约 (register_subparser / execute / main)
    orchestrator.py  — 业务逻辑 (run_ingest + 抓取/截断/去重)
"""

from pipeline.ingestion.ingest.orchestrator import run_ingest
