"""
pipeline/ingestion/backfill_ids — ID 回填工具

为 data/01_raw/ 下已有的 .md 文件补充 article.id (SHA-256 of source URL)。
适用于在引入 ID 机制前已抓取的文件。
"""

from pipeline.ingestion.backfill_ids.cli import execute, register_subparser
