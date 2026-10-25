# 架构深层设计：Aggregate 多阶段扫描与 04_structured 热冷分流

> 何时读我：改动 `pipeline/aggregation/`、`pipeline/publish/`、前端数据层（`src/lib/data/`），或排查"文章处理状态显示不对 / 文章数量对不上"类问题前必读。根文件 CLAUDE.md 只有一行式要点，本文是完整设计背景与行为契约。

## Aggregate Stage Design

### Problem it solves

The pipeline has **4 call sites** that invoke `aggregate_frontmatter()`, each triggered at different stages:

| Call site | File | When | Old behavior (broken) |
|-----------|------|------|----------------------|
| extract stage | `pipeline/extraction/orchestrator.py` | After Stage 2 completes | Only scanned `02_extracted/` |
| analyze stage | `pipeline/analysis/run_analysis.py` | After Stage 3 completes | Only scanned `03_analyzed/`, **overwriting** extract's data |
| CLI aggregate | `pipeline/synthesis/cli.py` | Manual | Defaulted to `03_analyzed/` |
| CLI synthesize | `pipeline/synthesis/cli.py` | When `--lookback-days` set | Defaulted to `03_analyzed/` |

**The problem:** analyze's aggregate call overwrites per-source JSONs with only `03_analyzed/` data, discarding articles that were extracted but not yet analyzed. This made the frontend show "scout" status for those articles instead of "extracted".

### Multi-stage scanning (the fix)

When `input_dir=None` (default), `aggregate_frontmatter()` scans all three directories:

```
data/01_raw/{source}/*.md ─┐
data/02_extracted/{source}/*.md ─┤── aggregate ──→ data/04_structured/{source}.json
data/03_analyzed/{source}/*.md ──┘                   (全量，去重保留最完整版本)
```

**Dedup:** Files are keyed by `(source_subdir, filename_stem)`. Directories are scanned in priority order (`analyzed` > `extracted` > `raw`), so the first-seen (most advanced) version wins.

**Result:** Regardless of which stage triggers aggregate, per-source JSONs always contain every article at its latest processing stage. analyze no longer "overwrites" — it enhances.

### Two output files, two purposes

| Output | Filtering | Purpose | Consumer |
|--------|-----------|---------|----------|
| `{source}.json` | No time filter, all articles | Stage 5 publish 输入（→ `articles` 表） | `pipeline/publish/publishers.py` |
| `all_articles.json` | `lookback_days` time window | Daily report input | Stage 4b synthesize (`run_synthesis.py`) |

### Frontend processing status

The frontend determines article status in `src/lib/data/status.ts:determineProcessingStatus()`:

```ts
if (article.impact_score && article.sentiment) → "analyzed"   // Stage 3 done
if (article.tldr || article.objective_summary)  → "extracted"  // Stage 2 done
else                                             → "scout"      // Stage 1 only
```

Articles in manifest but NOT in `articles` 表 get `status = "scout"` and `enriched = null` (see `src/lib/data/sources/index.ts`). Multi-stage aggregate + publish ensure articles appear in the table as soon as they complete ANY stage.

## 04_structured hot/cold split

### Problem it solves

Per-source JSONs (`{source}.json`) grew unboundedly as the pipeline accumulated articles. Every aggregate run rewrote the full file, and frontend reads took longer as file sizes increased. `arxiv-cs-ai.json` reached 2.1 MB (254 articles) after the data-1 migration.

### Directory structure

```
data/04_structured/
  {source}.json                                   ← 热数据：最近 hot_days 天
  all_articles.json                               ← 日报输入（lookback_days 窗口，不变）
  archive/
    {source}/
      {source}_{YYYY-MM-DD}.json                  ← 冷数据按 created 日期分片
```

### Hot vs cold cutoff

Articles are split by `created` date relative to today:

| 分类 | 条件 | 写入位置 | 加载时机 |
|------|------|----------|----------|
| 热数据 | `created >= today - hot_days` | `{source}.json` | 始终加载 |
| 冷数据 | `created < today - hot_days` | `archive/{source}/{source}_{date}.json` | dateRange 时按需加载 |

`hot_days` 默认 7 天，可通过 `config.yaml` (`stages.aggregate.hot_days`) 或 CLI (`--hot-days N`) 调整。

### Pipeline write behavior

1. 每次 aggregate 扫描所有 stage 目录
2. 提取文章后按 `created` 分流
3. 热数据覆盖写 `{source}.json`
4. 冷数据按日期分组，覆盖写 `archive/{source}/{source}_{date}.json`（文章可能被后续阶段更新）
5. 清理超过 `max_history_days`（默认 365）的过期分片

### 读取行为（publish + 前端）

1. Stage 5 publish（`pipeline/publish/publishers.py`）合并热数据与 archive 分片：热数据优先、冷数据按 URL 规范化去重，upsert 到 `articles` 表
2. 前端 `loadStructuredData(sourceName, dateRange?)`（`src/lib/data/sources/structured-data.ts`）直接查询 `articles` 表：`source_dir` 过滤 + 可选 `created` 范围条件——热/冷之分在 DB 查询中消失

### Config reference

```yaml
# pipeline/config.yaml
stages:
  aggregate:
    lookback_days: 1       # all_articles.json 日报窗口
    hot_days: 7            # per-source JSON 热数据窗口
    max_history_days: 365  # archive 分片最大保留天数（0 = 不限）
```

### Key files

| 文件 | 职责 |
|------|------|
| `pipeline/aggregation/aggregate_frontmatter.py` | `aggregate_frontmatter()` 热冷分流 + `_cleanup_expired_archives()` |
| `pipeline/publish/publishers.py` | 热数据 + archive 合并去重，upsert 到 `articles` 表 |
| `src/lib/data/sources/structured-data.ts` | `loadStructuredData()` 查询 `articles` 表 |
| `pipeline/synthesis/cli.py` | `--hot-days` / `--max-history-days` CLI 参数 |
