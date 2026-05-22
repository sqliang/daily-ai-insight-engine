"""
pipeline/ingestion/ingest — Stage 1b: 正文抓取与清洗

读取 data/00_manifest/ 中的 JSON 清单 → 并发抓取网页正文并提取为干净 Markdown →
写入 data/01_raw/{source}/{id}.md，附带标准 YAML frontmatter。

包结构：
    cli.py           — CLI 契约 (register_subparser / execute / main)
    orchestrator.py  — 主编排 (manifest 选择、状态管理、ExitStack 并行调度)
    worker.py        — 单篇文章抓取 worker（线程池 + browser 两条通道）
    truncation.py    — 正文截断规则
"""

from pipeline.ingestion.ingest.orchestrator import run_ingest
