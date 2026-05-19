# CLAUDE.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

## Architecture

This is a **dual-language** project: a Python offline pipeline ingests 19 AI news sources through a 4-stage Map/Reduce process, and a Next.js 16 App Router dashboard renders the final daily report as interactive charts.

**Data flow:** `19 RSS/scrape sources → Stage 1 (scout+ingest) → Stage 2 (extract facts) → Stage 3 (3-dimension analysis × concurrency) → Stage 4a (aggregate frontmatter JSON) → Stage 4b (Editor-in-Chief synthesis) → Next.js reads JSON directly from disk`

**Key design:**
- The pipeline and frontend are **decoupled by JSON files on disk**. The Next.js server reads `data/05_reports/daily-report.json` via `node:fs` at request time — no database, no API layer. Sources page reads `pipeline/config.yaml` + `data/00_manifest/*.json` via `src/lib/data/sources.ts`.
- **Dual schema contract:** Python side uses Pydantic v2 (in `pipeline/schemas/`), TypeScript side uses Zod (in `src/lib/agent/schema.ts`). Both describe the same data shapes.
- All pipeline stages support `--skip-existing` (idempotent) and `--force` (reprocess).
- The pipeline uses `claude-agent-sdk` (Anthropic) with streaming, exponential backoff retry (3 attempts), and a 5-level JSON recovery parser for truncated LLM output.
- Agent calls have `allowed_tools=[]` — the SDK agents are pure thinkers, no file system access.

**Routing:**
- `/` — Sources page (homepage): reads config.yaml + manifest JSONs, renders tier-grouped source inventory
- `/sources` — redirects to `/`
- `/sources/[name]` — Source detail page with hero banner + sortable article list
- `/dashboard` — Daily report dashboard: reads `daily-report.json`, renders KPI/charts
- `/report` — Full markdown report (react-markdown + remark-gfm)

## Essential commands

```bash
# Frontend
pnpm dev                 # Next.js dev server (Turbopack) on port 3000
pnpm build               # Production build (standalone output)
pnpm lint                # ESLint (flat config)
pnpm typecheck           # tsc --noEmit

# Pipeline (Python — run from repo root)
python pipeline/run.py scout              # Stage 1a: generate URL manifests
python pipeline/run.py ingest             # Stage 1b: download + clean articles
python pipeline/run.py extract            # Stage 2: BaseInfo + FactExtraction via Claude
python pipeline/run.py analyze            # Stage 3: 3-dimension deep analysis
python pipeline/run.py aggregate          # Stage 4a: extract frontmatter → all_articles.json
python pipeline/run.py synthesize         # Stage 4b: Editor-in-Chief daily report generation

# Pipeline variants
python pipeline/run.py synthesize --dry-run     # Estimate token usage, no LLM call
python pipeline/run.py analyze --stage qualitative  # Run only one analysis dimension
python pipeline/run.py extract --force          # Reprocess all, ignoring skip-existing

# Validation
pnpm validate            # Zod validation of data files (scripts/validate-report.ts)
```

## Python environment

Python dependencies are managed with `uv`. Install: `cd pipeline && uv pip install -r requirements.txt`.
The `run.py` entry point auto-loads `.env` (via `python-dotenv`) and auto-configures proxy from `pipeline/config/proxy.json`.
All Python imports use `pipeline.` prefix with the repo root on `sys.path`.

## Key project structure

```
pipeline/
  run.py                    # Unified CLI (argparse subcommands)
  config.yaml               # Source config + tiers_meta + display_name/display_description for UI
  core/agent.py             # claude-agent-sdk wrapper: call, retry, JSON parse, options
  core/frontmatter_utils.py # YAML frontmatter read/write for .md files
  core/config_loader.py     # Config YAML reader with caching
  core/browser_utils.py     # Playwright lifecycle management
  core/web_utils.py         # curl + feedparser + trafilatura wrappers
  core/file_utils.py        # Atomic writes, JSON I/O, directory helpers
  core/id_utils.py          # SHA-256 article ID generation
  core/proxy_utils.py       # Proxy config injection
  core/text_utils.py        # Text cleaning utilities
  schemas/                  # Pydantic v2 models (4 schema files for 4 data blocks)
  ingestion/                # RSS scraping, HTML parsing, browser rendering (Playwright)
    parsers/                # Source-specific parsers (zhihu, tldrai, machine_heart, anthropic)
  extraction/               # BaseInfo + FactExtraction agents
  analysis/                 # 3 persona agents (tech-architect, capital-analyst, risk-assessor)
    prompts/                # System prompts for each analysis dimension
  synthesis/                # Frontmatter aggregation + Editor-in-Chief report generation
    prompts/                # System + user prompts for report synthesis

src/
  app/
    layout.tsx              # Root layout with NavBar
    page.tsx                # Sources page (homepage) — tier-grouped source inventory
    loading.tsx             # Sources page skeleton loading state
    dashboard/
      page.tsx              # Dashboard — reads daily-report.json from disk, renders KPI/charts
      loading.tsx           # Dashboard skeleton loading state
    report/
      page.tsx              # Full markdown report (react-markdown + remark-gfm)
    sources/
      page.tsx              # Redirects to /
      [name]/
        page.tsx            # Source detail page with hero + ArticleList (impact-score sort)
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
      cleaner.ts            # Text cleaning utilities
    report/
      labels.ts             # Chinese label mappings (event types, sentiments, severities)
      generate-markdown.ts  # JSON-to-Markdown fallback for /report page
  components/
    layout/
      NavBar.tsx            # Sticky frosted-glass top navigation
      PageShell.tsx         # Page container (max-w-7xl, responsive padding)
    dashboard/              # KPI cards, charts (Donut/Bar), signal lists, deep dives
    charts/                 # Recharts wrappers (DonutChart, HorizontalBarChart, RadarChart)
    sources/                # Source cards, hero, article cards, analysis sub-cards
    report/                 # Markdown renderer (react-markdown + remark-gfm)
```

## Environment variables

- `ANTHROPIC_API_KEY` — required for pipeline LLM calls
- `AI_ENGINE_USE_CLAUDE` — set to `true` to use claude-agent-sdk (default: `false`)

## Data directories (all gitignored)

- `data/00_manifest/{source}_{date}.json` — URL manifests from scout stage
- `data/01_raw/{source}/*.md` — cleaned article text with YAML frontmatter
- `data/02_extracted/{source}/*.md` — articles + extracted BaseInfo and FactExtraction
- `data/03_analyzed/{source}/*.md` — articles + 3 analysis dimensions appended
- `data/04_structured/{source}.json` + `all_articles.json` — aggregated frontmatter from all analyzed articles
- `data/05_reports/daily-report.json` + `daily-report.md` — final report (consumed by Next.js dashboard)

Each `.md` file has YAML frontmatter that accumulates fields across pipeline stages. The `id` field is a SHA-256 hash of the source URL.

## Source configuration

19 sources organized in 3 tiers (A: academic/technical, B: product/community, C: business/capital), each capped at 5 articles, total target 15. Config in `pipeline/config.yaml` defines fetch strategies (`rss`, `scrape`, `browser`), keyword filters, max age, and truncation per source. 2 A-tier sources are disabled (`meta-ai-blog`, `microsoft-ai-blog`) due to unavailable or stale feeds.

`config.yaml` also includes UI-facing metadata consumed by the Next.js frontend:
- `tiers_meta` — per-tier labels, subtitles, and rationale for the Sources page hero banner
- `display_name` / `display_description` — human-readable Chinese names and descriptions for source cards
