# 项目结构详解（完整目录树）

> 何时读我：需要定位某个模块、页面或组件的位置时查阅。根文件 CLAUDE.md 只有顶层摘要，本文是带逐文件注释的完整目录树。

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
  publish/                  # Stage 5: data/ → PostgreSQL upsert（db.py / publishers.py / cli.py）+ 站点快照（snapshot.py）

weekly_digest/              # 周报生成器（独立包，零 LLM）：按 ISO 周汇总 data/ 信源 → weekly_reports/
  run.py                    #   CLI 入口（--week / --source / --output-dir）
  collector.py              #   扫描 02_extracted 优先 + 01_raw 补齐，周窗口过滤 + ID 去重 + 字段降级
  external.py               #   外部渠道榜单（{iso_week}-kimi.md）解析与合并：URL 命中丰富 stars/语言字段，未命中作外部补充
  render.py                 #   WeeklyDigest → 中英文对照 Markdown（含外部渠道补充区块）
  models.py                 #   DigestItem / WeeklyDigest（Pydantic v2，预留为 web 站点周报数据源）

weekly_reports/             # 周报输出（运行生成）：{source}/{iso_week}.md + .json，未 gitignore 可提交；
                            #   {source}/{iso_week}-kimi.md 为外部渠道榜单输入文件（非生成物），存在时自动合并

src/
  app/
    layout.tsx              # Root layout with NavBar
    (home)/                 # 路由组（URL 不变）：隔离骨架屏 Suspense，避免提前流式 flush 导致 notFound 状态码退化为 200
      page.tsx              # Sources page (homepage) — tier-grouped source inventory
      loading.tsx           # Sources page skeleton loading state
    dashboard/
      (list)/               # 路由组（URL 不变）：骨架屏仅作用于列表页
        page.tsx            # 日报卡片列表 — 扫描 daily-report-*.json，展示所有历史日报
        loading.tsx         # 卡片列表页骨架屏
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
    db/
      schema.ts             # Drizzle 表定义（daily_reports / manifests / articles）
      client.ts             # Drizzle 客户端（postgres.js 驱动，惰性单例）
    data/
      sources/              # config（YAML）+ manifests（DB）+ structured-data（DB）→ SourceStatus/SourceDetail
      status.ts             # Processing status types, StructuredArticle schema
      tiers.ts              # Tier colors, labels, type labels, language labels
      reports.ts            # 日报列表 + 按日期读取（listReports / getReport / getReportMarkdown，查 daily_reports 表）
      specialized.ts        # 专题洞察数据加载（loadGithubBrief / loadPaperArticles / loadProductBrief）
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
