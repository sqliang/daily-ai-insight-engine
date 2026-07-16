# CLAUDE.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

## Architecture

This is a **dual-language** project: a Python offline pipeline ingests 26 AI information sources (23 active) through a 6-stage Map/Reduce process (5 runnable commands — aggregate auto-executes after extract and analyze), and a Next.js 16 App Router dashboard renders the final daily report as interactive charts.

**Data flow:** `26 RSS/scrape/browser sources → Stage 1a (scout URL manifests) → Stage 1b (ingest content download, with browser fallback for anti-bot pages) → Stage 2 (extract facts + source-aware specialized tags for projects/papers/products) → Stage 3 (3-dimension analysis × concurrency + project/paper/product deep analysis) → Stage 4a (aggregate frontmatter JSON + hot/cold split) → Stage 4b (Editor-in-Chief synthesis: daily report + project/paper/product specialized briefs) → Next.js reads JSON directly from disk`

**Key design:**
- The pipeline and frontend are **decoupled by JSON files on disk**. The Next.js server reads `data/05_reports/daily-report.json` via `node:fs` at request time — no database, no API layer. Sources page reads `pipeline/config.yaml` + `data/00_manifest/*.json` via `src/lib/data/sources.ts`.
- **Dual schema contract:** Python side uses Pydantic v2 (in `pipeline/schemas/`), TypeScript side uses Zod (in `src/lib/agent/schema.ts`). Both describe the same data shapes.
- All pipeline stages support `--skip-existing` (idempotent) and `--force` (reprocess).
- **Multi-stage aggregate:** Stage 4a `aggregate` scans `data/01_raw/` + `data/02_extracted/` + `data/03_analyzed/` by default, deduplicating by `(source, article_id)` with priority `03 > 02 > 01`. This ensures per-source JSONs contain every article at its latest processing stage, regardless of which pipeline stage triggered aggregate. See "Aggregate Stage Design" section below for details.
- **Hot/cold data split:** `{source}.json` stores only recent `hot_days` (default: 7) of articles for fast frontend reads. Older articles are archived as date-sharded JSON files under `archive/{source}/{source}_{date}.json`. The frontend transparently merges archive shards when a `dateRange` query parameter is active on the source detail page. See "04_structured hot/cold split" below for details.
- **Time slicing:** `all_articles.json` (daily report input) filters by `created` field with `lookback_days` (default: 1, today only). Use `--lookback-days 0` to include all history.
- **Report archival:** Stage 4b writes both `daily-report-{date}.json` (archive) and `daily-report.json` (latest copy for frontend). The `/dashboard` page scans all `daily-report-*.json` files and displays a card list. `/dashboard/[date]` shows the visualization dashboard, `/report/[date]` shows the full markdown.
- The pipeline uses `claude-agent-sdk` (Anthropic) with streaming, exponential backoff retry (3 attempts), and a 5-level JSON recovery parser for truncated LLM output.
- Agent calls have `allowed_tools=[]` — the SDK agents are pure thinkers, no file system access.
- **Specialized briefs:** Stage 4b generates three topic-specific briefs — `projectInsights` (open-source projects & technical solutions), `paperInsights`/`paperHighlights` (AI papers), and `productInsights` (AI products) — alongside the general daily report. These briefs are built on top of Stage 2 specialized tags and Stage 3 deep analysis (not raw source classification), deduplicate against yesterday's report, and produce normalized insight items with traceable `sources` and `evidenceSnippets`. They are stored in the same `daily-report.json` and consumed by `/specialized/*` pages.

**Styling:** Tailwind CSS v4.1+ is the **primary styling method**. Always prefer utility classes over CSS Modules, inline styles, or custom CSS. CSS Modules are a last resort — only when Tailwind genuinely cannot achieve the result (complex `@keyframes`, `::-webkit-scrollbar`, etc.). See `.claude/skills/tailwind-css-patterns/SKILL.md` for patterns and conventions.

**Routing:**
- `/` — Sources page (homepage): reads config.yaml + manifest JSONs, renders tier-grouped source inventory
- `/sources` — redirects to `/`
- `/sources/[name]` — Source detail page with hero banner + sortable article list
- `/dashboard` — 日报卡片列表：扫描 `data/05_reports/daily-report-*.json`，按日期降序展示所有历史日报卡片
- `/dashboard/[date]` — 指定日期的可视化仪表盘（KPI + 图表 + 事件 + 信号），含 "完整报告" 入口
- `/report` — 重定向到 `/dashboard`
- `/report/[date]` — 指定日期的 Markdown 全文（react-markdown + remark-gfm），降级为 JSON → Markdown 转换
- `/specialized/github/[date]` — 项目洞察页：基于 Stage 2/3 识别的开源项目与技术方案，经跨天去重后展示 AI 子领域分布、项目评分、适用人群与风险信号
- `/specialized/paper/[date]` — 论文洞察页：基于 Stage 2/3 识别的 AI 论文，展示研究问题、方法创新、实验严谨度与产业相关性
- `/specialized/product/[date]` — 产品洞察页：基于 Stage 2/3 识别的 AI 产品动态，展示定位、商业模式、目标用户与市场信号

## Comment conventions

All comments use **Chinese** (Simplified). Code identifiers (variable names, function names, type names) remain English. Comments explain **why** and **how** — design rationale, architectural decisions, data flow direction, and edge cases. Don't write comments that just restate what the code says.

### Python (`pipeline/`)

```python
"""
pipeline/module_name.py — 模块用途简述

说明本模块在管道中的位置（Stage N）、负责什么、被哪些模块消费。
包含：关键设计决策、数据流转方向、异常处理策略。
"""

# ---------------------------------------------------------------------------
# 逻辑分区标题
# ---------------------------------------------------------------------------

def public_function(param: str) -> dict:
    """
    函数用途。

    参数：
        param: 参数说明（含约束条件）

    返回：
        dict: 返回值说明

    异常：
        ValueError: 在什么情况下抛出

    设计理由：
        为什么这样做而不是另一种方式（如涉及非显而易见的取舍）
    """
    ...

class SomeModel(BaseModel):
    """类的用途和设计意图。"""

    field_name: str = Field(
        ...,
        description="字段含义。说明该字段的消费方和用途。",
    )
```

- **每个 `.py` 文件**开头必须有模块级 docstring
- **每个函数**（包括 `_private`）必须有 docstring
- **每个 Pydantic model 和 class** 必须有 docstring
- **每个 Pydantic Field** 必须提供 `description=` 参数
- 用 `# ---` 分隔线划分文件内的逻辑分区
- 行内注释用 `#` 仅在逻辑非显而易见时使用

### TypeScript / TSX (`src/`)

```tsx
// ============================================================================
// component-or-module.tsx — 文件用途简述
//
// 说明本文件的职责、被哪些页面/模块消费、数据流向。
// 涉及非显而易见的决策时解释设计理由。
// ============================================================================

// ---------------------------------------------------------------------------
// 逻辑分区标题
// ---------------------------------------------------------------------------

/**
 * 组件或函数的用途。
 *
 * 描述该组件的职责、使用场景、以及关键的交互行为。
 * 当 props 含义不是一目了然时，说明其作用。
 */
export function MyComponent({ items, onSelect }: Props) {
  // 非显而易见的逻辑需要行内注释说明原因
  const threshold = items.length > 10 ? 0.5 : 0.8;

  return ( ... );
}
```

- **每个 `.ts` / `.tsx` 文件**开头必须有 banner 注释块（`// ====` 分隔），说明文件职责和消费方
- **每个 export 的组件和函数**必须有 JSDoc（`/** ... */`）描述其用途
- 组件 JSDoc 需说明使用场景，props 含义不直观时需额外说明
- 用 `// ---` 分隔线划分文件内的逻辑分区
- 行内注释用 `//` 仅在逻辑非显而易见时使用（为什么取这个阈值、为什么做这个判断）

### YAML 配置文件

```yaml
# ---------------------------------------------------------------------------
# 配置区块标题 — 说明该区块控制什么功能
# ---------------------------------------------------------------------------

# 字段含义说明，尤其是值含义不直观时
key: value  # 行内注释说明该值的特殊含义或选择理由
```

- 每个逻辑区块用 `# ---` 分隔注释标注
- 每个配置项应有行内或上方注释说明含义
- 布尔开关和枚举值必须注释说明每个值的含义

## Essential commands

```bash
# Frontend
pnpm dev                 # Next.js dev server (Turbopack) on port 3000
pnpm build               # Production build (standalone output)
pnpm lint                # ESLint (flat config)
pnpm typecheck           # tsc --noEmit

# Pipeline (Python — run from repo root with uv)
# Essential 5-command workflow (aggregate auto-executes after extract & analyze):
uv run python pipeline/run.py scout              # Stage 1a: generate URL manifests
uv run python pipeline/run.py ingest             # Stage 1b: download + clean articles
uv run python pipeline/run.py extract            # Stage 2: BaseInfo + FactExtraction → auto-aggregates
uv run python pipeline/run.py analyze            # Stage 3: 3-dimension deep analysis → auto-aggregates
uv run python pipeline/run.py synthesize         # Stage 4b: Editor-in-Chief daily report generation

# Standalone aggregate (for edge cases: config changes, --lookback-days, --hot-days, --target-date, --force):
uv run python pipeline/run.py aggregate          # Stage 4a: extract frontmatter → all_articles.json

# Pipeline variants
uv run python pipeline/run.py synthesize --dry-run     # Estimate token usage, no LLM call
uv run python pipeline/run.py analyze --stage qualitative  # Run only one analysis dimension
uv run python pipeline/run.py extract --force          # Reprocess all, ignoring skip-existing
uv run python pipeline/run.py aggregate --lookback-days 0  # Standalone: include all historical articles (no time filter)
uv run python pipeline/run.py aggregate --lookback-days 7  # Standalone: re-aggregate with wider lookback window
uv run python pipeline/run.py synthesize --lookback-days 7  # Re-aggregate last 7 days before synthesis
uv run python pipeline/run.py aggregate --target-date 2026-06-10  # Exact date: only articles with created==2026-06-10
uv run python pipeline/run.py synthesize --target-date 2026-06-10  # Generate report for a specific past date
```

## Python environment

Python 依赖通过 `uv` 管理（已安装，无需重复安装）。如需重新安装：`uv pip install -r pipeline/requirements.txt`。
`run.py` 入口自动加载 `.env`（通过 `python-dotenv`）并注入 `pipeline/config/proxy.json` 的代理配置。
所有 Python 命令必须通过 `uv run python` 执行，保证使用 uv 环境中的依赖。
所有 Python 导入使用 `pipeline.` 前缀，项目根目录在 `sys.path` 上。

## Key project structure

```
pipeline/
  run.py                    # Unified CLI (argparse subcommands)
  config.yaml               # Source config + tiers_meta + display_name/display_description for UI
  core/                     # Core business components
    agent.py                #   claude-agent-sdk wrapper: call, retry, JSON parse, options
    web_utils.py            #   curl + feedparser + trafilatura wrappers
    browser_utils.py        #   Playwright lifecycle management
    config_loader.py        #   Config YAML reader with caching
    frontmatter_utils.py    #   YAML frontmatter read/write for .md files
    proxy_utils.py          #   Proxy config injection
    logging_config.py       #   Unified logging initialization
    concurrency/            #   Concurrent processing utilities
  utils/                    # Pure utilities (no business logic)
    file_utils.py           #   Atomic writes, JSON I/O, directory helpers
    id_utils.py             #   SHA-256 article ID generation
    text_utils.py           #   Text cleaning utilities
    schema_utils.py         #   Flat ↔ nested frontmatter conversion
    enum_utils.py           #   Enum helpers
    frontmatter.py          #   Frontmatter parsing
  schemas/                  # Pydantic v2 models（含 BaseInfo / FactExtraction / DeepAnalysis / DailyReport / SpecializedAnalysis）
  ingestion/                # Stage 1: RSS scraping, HTML parsing, browser rendering (Playwright)
    scout/                  #   Stage 1a: URL manifest generation
    ingest/                 #   Stage 1b: Content download + cleaning
    backfill_ids/           #   Article ID backfill utility
    parsers/                #   Source-specific parsers (zhihu, tldrai, machine_heart, anthropic)
  extraction/               # Stage 2: BaseInfo + FactExtraction agents（含 source-aware specialized tags）
  analysis/                 # Stage 3: 3 persona agents（tech-architect / capital-analyst / risk-assessor）+ project/paper/product specialized analysis
    prompts/                #   System prompts for each analysis dimension
  aggregation/              # Stage 4a: Frontmatter aggregation + hot/cold split
  synthesis/                # Stage 4b: Editor-in-Chief report generation（daily report + specialized briefs）
    prompts/                #   System + user prompts for report synthesis

src/
  app/
    layout.tsx              # Root layout with NavBar
    page.tsx                # Sources page (homepage) — tier-grouped source inventory
    loading.tsx             # Sources page skeleton loading state
    dashboard/
      page.tsx              # 日报卡片列表 — 扫描 daily-report-*.json，展示所有历史日报
      [date]/
        page.tsx            # 指定日期的可视化仪表盘（KPI + 图表 + 事件 + 信号）
    report/
      page.tsx              # 重定向到 /dashboard
      [date]/
        page.tsx            # 指定日期的 Markdown 全文（react-markdown + remark-gfm）
    sources/
      page.tsx              # Redirects to /
      [name]/
        page.tsx            # Source detail page with hero + ArticleList (impact-score sort)
    specialized/
      github/[date]/
        page.tsx            # 项目洞察页（开源项目与技术方案）
      paper/[date]/
        page.tsx            # 论文洞察页（AI 学术论文）
      product/[date]/
        page.tsx            # 产品洞察页（AI 产品动态）
  lib/
    agent/
      schema.ts             # Zod schemas — the single source of truth for TypeScript types
      prompts.ts            # LLM prompt templates
      heuristics.ts         # Analysis heuristics
      index.ts              # Barrel export
    data/
      files.ts              # Type-safe JSON read/write with Zod validation
      sources.ts            # Reads config.yaml + manifests → SourceStatus/SourceDetail
      status.ts             # Processing status types, StructuredArticle schema
      tiers.ts              # Tier colors, labels, type labels, language labels
      reports.ts            # 日报列表扫描 + 按日期读取（listReports / getReport / getReportMarkdown）
      specialized.ts        # 专题洞察数据加载（loadGithubBrief / loadPaperArticles / loadProductBrief）
      cleaner.ts            # Text cleaning utilities
    report/
      labels.ts             # Chinese label mappings (event types, sentiments, severities)
      generate-markdown.ts  # JSON-to-Markdown fallback for /report page
  components/
    layout/
      NavBar.tsx            # Sticky frosted-glass top navigation
      PageShell.tsx         # Page container (max-w-7xl, responsive padding)
    dashboard/              # DashboardContent (完整仪表盘布局) + KPI/图表/事件/信号区块
    charts/                 # Recharts wrappers (DonutChart, HorizontalBarChart, RadarChart)
    sources/                # Source cards, hero, article cards, analysis sub-cards
    reports/                # ReportCard (日报卡片，用于 /dashboard 列表页) + SpecializedReportHero + SpecializedEntries
    report/                 # MarkdownRenderer (react-markdown + remark-gfm)
```

## Environment variables

- `ANTHROPIC_API_KEY` — required for pipeline LLM calls
- `AI_ENGINE_USE_CLAUDE` — set to `true` to use claude-agent-sdk (default: `false`)

## Data directories (all gitignored)

- `data/00_manifest/{source}_{date}.json` — URL manifests from scout stage
- `data/01_raw/{source}/*.md` — cleaned article text with YAML frontmatter (after ingest)
- `data/02_extracted/{source}/*.md` — articles + extracted BaseInfo and FactExtraction (after extract)
- `data/03_analyzed/{source}/*.md` — articles + 3 analysis dimensions appended (after analyze)
- `data/04_structured/{source}.json` — per-source JSON array: recent `hot_days` (default: 7) articles at their latest processing stage. Consumed by frontend source detail page for enrichment via `loadStructuredData()`
- `data/04_structured/all_articles.json` — time-window filtered merge (controlled by `lookback_days`). Includes metadata: `aggregated_stages`, `lookback_days`, `coverage_period`, `skipped_old`, `sources`. Input to Stage 4b synthesize
- `data/04_structured/archive/{source}/{source}_{YYYY-MM-DD}.json` — cold data date shards. Contains articles older than `hot_days`, grouped by `created` date. Loaded on-demand by frontend when `dateRange` query param is active. Shards are overwritten each aggregate run (articles may have been further processed). Expired shards (older than `max_history_days`, default 365) are cleaned up automatically
- `data/05_reports/daily-report.json` + `daily-report.md` — latest report for frontend consumption，包含 `specializedBrief` 专题洞察块（`projectInsights` / `paperHighlights` / `productInsights`）。Archive copies `daily-report-{date}.json` / `.md` are written alongside

Each `.md` file has YAML frontmatter that accumulates fields across pipeline stages. Key fields: `id` (SHA-256 hash of source URL), `created` (ingestion date, set to `date.today()` at Stage 1b), `published` (original publication date), `tldr` / `objective_summary` (Stage 2 fields), `impact_score` / `sentiment` (Stage 3 fields), `specialized_tags` / `github_assessment` / `paper_assessment` / `product_assessment` (source-aware 专题标注与分析字段)。

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
| `{source}.json` | No time filter, all articles | Frontend source detail page enrichment | `src/lib/data/sources.ts:loadStructuredData()` |
| `all_articles.json` | `lookback_days` time window | Daily report input | Stage 4b synthesize (`run_synthesis.py`) |

### Frontend processing status

The frontend determines article status in `src/lib/data/status.ts:determineProcessingStatus()`:

```ts
if (article.impact_score && article.sentiment) → "analyzed"   // Stage 3 done
if (article.tldr || article.objective_summary)  → "extracted"  // Stage 2 done
else                                             → "scout"      // Stage 1 only
```

Articles in manifest but NOT in per-source JSON get `status = "scout"` and `enriched = null` (see `src/lib/data/sources.ts:408-424`). Multi-stage aggregate ensures articles appear in the JSON as soon as they complete ANY stage.

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

### Frontend read behavior

`loadStructuredData(sourceName, dateRange?)` 在 `src/lib/data/sources.ts:319`：

1. 总是先加载 `{source}.json`（热数据）
2. 如果 `dateRange` 有值且指向了热窗口之外的日期：
   - 列出 `archive/{source}/` 下所有分片
   - 按文件名中的日期筛选匹配的分片
   - 合并到结果中（URL 去重，热数据优先）
3. 如果 `archive/` 目录不存在（兼容旧 aggregate）：降级为只读热数据

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
| `src/lib/data/sources.ts` | `loadStructuredData()` 热数据 + archive 按需加载 |
| `pipeline/synthesis/cli.py` | `--hot-days` / `--max-history-days` CLI 参数 |

## Source configuration

26 sources (23 active, 3 disabled) organized in 3 tiers (A: academic/technical, B: product/community, C: business/capital), each capped at 5 articles, total target 15. Config in `pipeline/config.yaml` defines fetch strategies (`rss`, `scrape`, `browser`), keyword filters, max age, and truncation per source. 3 sources are disabled (`meta-ai-blog`, `microsoft-ai-blog`, `zhihu`) due to unavailable or stale feeds.

`config.yaml` also includes UI-facing metadata consumed by the Next.js frontend:
- `tiers_meta` — per-tier labels, subtitles, and rationale for the Sources page hero banner
- `display_name` / `display_description` — human-readable Chinese names and descriptions for source cards

## Playwright MCP debug output convention

When using Playwright MCP tools (`browser_snapshot`, `browser_take_screenshot`) during debugging or exploration, always write output files under `debug-output/`:

```
# snapshot
filename: "debug-output/producthunt-snapshot.md"

# screenshot  
filename: "debug-output/page-screenshot.png"
```

The `debug-output/` directory is gitignored. Files written to the project root will pollute the working tree.
