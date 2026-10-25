# Pipeline 命令全集（CLI 变体参考）

> 何时读我：需要运行 pipeline 命令（含变体参数）、站点快照、周报或 daily-report-pipeline 门禁脚本时查阅。根文件 CLAUDE.md 只列了最常用的核心命令，本文是完整变体参考。

## Frontend

```bash
pnpm dev                 # Next.js dev server (Turbopack) on port 3000
pnpm build               # Production build (standalone output)
pnpm lint                # ESLint (flat config)
pnpm typecheck           # tsc --noEmit
```

## Pipeline 核心流程（Python — run from repo root with uv）

aggregate 在 extract 和 analyze 后自动执行；publish 在 synthesize 后自动执行：

```bash
uv run python pipeline/run.py scout              # Stage 1a: generate URL manifests
uv run python pipeline/run.py ingest             # Stage 1b: download + clean articles
uv run python pipeline/run.py extract            # Stage 2: BaseInfo + FactExtraction → auto-aggregates
uv run python pipeline/run.py analyze            # Stage 3: 3-dimension deep analysis → auto-aggregates
uv run python pipeline/run.py synthesize         # Stage 4b: Editor-in-Chief daily report generation → auto-publishes
uv run python pipeline/run.py publish            # Stage 5: upsert data/ → PostgreSQL (idempotent; hot articles + all manifests/reports)
uv run python pipeline/run.py publish --force    # Stage 5 full backfill: include archive cold-data shards
uv run python pipeline/run.py publish --target-date 2026-07-21  # Stage 5: only that date's articles/manifests/report
```

## 站点数据快照

publish 成功后默认自动生成并推送 data-snapshot；快照失败只记 warning，不影响发布结果：

```bash
uv run python pipeline/run.py publish --skip-snapshot  # 跳过本次 publish 后的自动快照
# snapshot 命令保留为手动重建/修复入口
uv run python pipeline/run.py snapshot             # 全量重建 data/snapshot/，只在本地生成
uv run python pipeline/run.py snapshot --push      # 手动 force push data-snapshot orphan 分支；快照位于分支根目录，不切换主工作区
```

## Standalone aggregate 与 Pipeline 变体

Standalone aggregate 适用场景：config 变更、调整 --lookback-days / --hot-days / --target-date、--force 重跑：

```bash
uv run python pipeline/run.py aggregate          # Stage 4a: extract frontmatter → all_articles.json

uv run python pipeline/run.py synthesize --dry-run     # Estimate token usage, no LLM call
uv run python pipeline/run.py analyze --stage qualitative  # Run only one analysis dimension
uv run python pipeline/run.py extract --force          # Reprocess all, ignoring skip-existing
uv run python pipeline/run.py extract --target-date 2026-07-21   # Date-scoped: only articles with created==2026-07-21
uv run python pipeline/run.py analyze --target-date 2026-07-21   # Same date scoping for analyze
# ⚠️ Bare extract/analyze (no --target-date / -i) processes ALL unprocessed files including
#    multi-month backlog — the CLI prints a prominent warning. Always scope large runs.
uv run python pipeline/run.py aggregate --lookback-days 0  # Standalone: include all historical articles (no time filter)
uv run python pipeline/run.py aggregate --lookback-days 7  # Standalone: re-aggregate with wider lookback window
uv run python pipeline/run.py synthesize --lookback-days 7  # Re-aggregate last 7 days before synthesis
uv run python pipeline/run.py aggregate --target-date 2026-06-10  # Exact date: only articles with created==2026-06-10
uv run python pipeline/run.py synthesize --target-date 2026-06-10  # Generate report for a specific past date
```

## Weekly digest（standalone package, zero LLM — pure local template rendering）

```bash
uv run python weekly_digest/run.py                          # github-trending + producthunt × 本 ISO 周 → weekly_reports/
uv run python weekly_digest/run.py --week last              # 上一 ISO 周（别名 current/last，避免手算周数）
uv run python weekly_digest/run.py --week 2026-W40          # 指定历史周
uv run python weekly_digest/run.py --from 2026-10-01 --to 2026-10-12  # 跨周区间：按 ISO 周展开，逐周各生成一份
uv run python weekly_digest/run.py --source github-trending # 只跑单源
# 重复运行同一周为幂等全量重生成（不丢数据，已补 extract 的文章自动升级中文摘要），
# 并输出"较上次：新增 N 条 / M 条升级为中文摘要"变更告知；周未结束时文档头标注"进行中快照"
```

外部渠道合并：若 `weekly_reports/{source}/{iso_week}-kimi.md` 外部渠道榜单存在，生成时自动合并（URL 重合丰富 stars/语言字段，未收录项目以"外部渠道补充"区块追加）。

## 指定日期日报流水线门禁脚本（daily-report-pipeline skill）

scout/ingest 由每日 17:30 定时任务完成后，从抓取完整性检查开始，按 **check → 定点 repair → 复检门禁** 的方式跑通 extract → analyze → synthesize → publish，生成指定日期的日报并发布到 PostgreSQL。所有操作严格限定 frontmatter `created == 目标日期` 的文章；repair 为单文件粒度（控制 LLM 成本）；每阶段最多 2 轮修复循环。synthesize 成功后自动 publish（失败仅 warning），流程末尾再补一条幂等 `publish --target-date` 兜底，并以 DB 行数核验作为"站点可见"的判据。跨天去重的昨日日报来源为 本地文件 → DB 兜底。

```bash
GATE=.agents/skills/daily-report-pipeline/scripts/pipeline_gate.py
uv run python $GATE check-ingest --date 2026-07-21    # 抓取完整性检查（JSON 报告，exit 0/1）
uv run python $GATE repair-ingest --date 2026-07-21   # 定点修复（浏览器重抓 + Jina/Wayback 兜底 + 劣化回滚 + arxiv manifest 自动补建）
uv run python $GATE run-extract --date 2026-07-21     # 日期隔离执行 extract（单进程 --target-date，超 200 篇预检熔断拒跑）
uv run python $GATE check-extract --date 2026-07-21   # Stage 2 后验检查
uv run python $GATE repair-extract --date 2026-07-21  # 单文件 extract --force
uv run python $GATE run-analyze --date 2026-07-21     # 日期隔离执行 analyze（同上）
uv run python $GATE check-analyze --date 2026-07-21   # Stage 3 后验检查
uv run python $GATE repair-analyze --date 2026-07-21  # 单文件 analyze --force
```

检查口径要点：正文质量启发式（反爬/HTML 泄漏/Jina 截断快照/过短，36kr 等短内容源有豁免阈值）；manifest 缺失判定已排除周末空窗（arxiv/nlp-elvis 周末无内容属正常）；extract/analyze 判定与前端 `determineProcessingStatus` 对齐。
