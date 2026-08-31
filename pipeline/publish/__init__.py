"""
pipeline/publish — Stage 5 发布管道

将本地 data/ 目录中站点需要的数据 upsert 到 PostgreSQL：
    - data/05_reports/daily-report-*.json|.md  → daily_reports
    - data/00_manifest/{source}_{date}.json    → manifests
    - data/04_structured/{source}.json + archive 分片 → articles

设计要点：
    - 纯机械 JSON 读取 + SQL upsert，零 LLM 调用。
    - 全部 INSERT ... ON CONFLICT DO UPDATE，天然幂等，可反复全量重发。
    - 字段映射（publishers.py 中的 map_* 纯函数）与 DB 写入分离，便于单测。
    - synthesize 成功后会自动调用本包（失败仅记 warning，不影响日报生成）。
"""
