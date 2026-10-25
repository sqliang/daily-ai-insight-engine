# CLAUDE.md

This file provides guidance to AI coding agents (Claude Code, Codex, Kimi Code, Cursor, Copilot, etc.) when working with code in this repository. `AGENTS.md` is a symlink to this file.

## 详细文档索引（按需加载，不要预读）

| 任务场景 | 文档 |
|---|---|
| 写/改代码前（注释规范完整示例） | `docs/agent/comment-conventions.md` |
| 运行 pipeline / 周报 / 门禁脚本（全部 CLI 变体） | `docs/agent/pipeline-commands.md` |
| 改动 aggregate / publish / 前端数据层（深层设计契约） | `docs/agent/architecture-deep-dive.md` |
| 定位模块、页面、组件位置（完整目录树） | `docs/agent/project-structure.md` |
| 设计背景与演进 | `docs/0_整体设计说明.md` ～ `docs/7_本地数据库连接与维护指南.md` |

维护约定：修改任一份 `docs/agent/` 文档时，检查本文件对应摘要是否需要同步。

## Architecture

This is a **dual-language** project: a Python offline pipeline ingests 26 AI information sources (23 active) through a 6-stage Map/Reduce process (6 runnable commands — aggregate auto-executes after extract and analyze, publish auto-executes after synthesize), and a Next.js 16 App Router dashboard renders the final daily report as interactive charts.

**Data flow:** `26 RSS/scrape/browser sources → Stage 1a (scout URL manifests) → Stage 1b (ingest content download, with browser fallback for anti-bot pages) → Stage 2 (extract facts + source-aware specialized tags) → Stage 3 (3-dimension analysis × concurrency + specialized deep analysis) → Stage 4a (aggregate frontmatter JSON + hot/cold split) → Stage 4b (Editor-in-Chief synthesis: daily report + specialized briefs) → Stage 5 (publish: upsert data/ → PostgreSQL, idempotent, no LLM calls) → Next.js reads from PostgreSQL via Drizzle`

**Key design:**
- Pipeline and frontend are **decoupled by PostgreSQL** (`daily_reports` / `manifests` / `articles` 三表，schema 见 `src/lib/db/schema.ts`) — no API layer; local `data/` is pipeline working storage, no longer read by the site (DB 抛错时回退 `data/snapshot/`)。Local dev: Docker Compose PostgreSQL (port 5433); production: Neon (`DATABASE_URL`)。
- **Dual schema contract:** Python Pydantic v2 (`pipeline/schemas/`) ↔ TypeScript Zod (`src/lib/agent/schema.ts`)，描述同一数据形状。
- All pipeline stages support `--skip-existing` (idempotent) and `--force` (reprocess)。
- Aggregate 默认扫描 01/02/03 三个 stage 目录去重（03>02>01 优先级）；`{source}.json` 只存近 `hot_days`(7) 天热数据，冷数据按日期分片到 `archive/`。设计细节见 `docs/agent/architecture-deep-dive.md`。
- LLM 调用走 `claude-agent-sdk`：`allowed_tools=[]`（纯思考，无文件访问）且 `mcp_servers={}` + `strict_mcp_config=True`（防止 SDK 加载用户级插件弹出浏览器）。浏览器只允许出现在 ingest 阶段（`BrowserSession`），LLM 阶段永不触碰。
- **Specialized briefs:** Stage 4b 在日报外生成 `projectInsights` / `paperHighlights` / `productInsights` 专题洞察，存于同一 `daily-report.json`，由 `/specialized/*` 页面消费。

**Styling:** Tailwind CSS v4.1+ is the **primary styling method**. Always prefer utility classes; CSS Modules 仅在 Tailwind 无法实现时兜底（复杂 `@keyframes`、`::-webkit-scrollbar` 等）。模式见 `.claude/skills/tailwind-css-patterns/SKILL.md`。

**Routing:** `/` Sources 首页 · `/sources/[name]` 信源详情 · `/dashboard` 日报卡片列表 · `/dashboard/[date]` 可视化仪表盘 · `/report/[date]` Markdown 全文 · `/specialized/{github,paper,product}/[date]` 专题洞察页（`/sources`、`/report` 重定向到对应首页）。

## Comment conventions

All comments use **Chinese** (Simplified)；代码标识符保持英文。注释解释 **why/how**，不复述代码本身。完整示例见 `docs/agent/comment-conventions.md`（写代码前必读），核心规则：

- 每个 `.py` 文件开头有模块级 docstring；每个函数（含 `_private`）、每个 Pydantic model/class 有 docstring；每个 Pydantic Field 必须带 `description=`
- 每个 `.ts`/`.tsx` 文件开头有 banner 注释块（`// ====`）；每个 export 的组件/函数有 JSDoc
- 用 `# ---` / `// ---` 分隔线划分文件内逻辑分区；行内注释仅在逻辑非显而易见时使用

## Essential commands

```bash
# Frontend
pnpm dev / pnpm build / pnpm lint / pnpm typecheck

# Pipeline 核心流程（repo 根目录，uv 运行；aggregate/publish 自动串联）
uv run python pipeline/run.py scout        # Stage 1a
uv run python pipeline/run.py ingest       # Stage 1b
uv run python pipeline/run.py extract      # Stage 2 → auto-aggregates
uv run python pipeline/run.py analyze      # Stage 3 → auto-aggregates
uv run python pipeline/run.py synthesize   # Stage 4b → auto-publishes
uv run python pipeline/run.py publish      # Stage 5: data/ → PostgreSQL（幂等）

# Weekly digest（独立包，零 LLM）
uv run python weekly_digest/run.py         # 本 ISO 周；--week last / 2026-W40 / --from --to / --source
```

⚠️ 裸跑 extract/analyze（不带 `--target-date`）会处理全部未处理积压——大批次务必限定范围。全部变体（`--force` / `--target-date` / snapshot / 门禁脚本等）见 `docs/agent/pipeline-commands.md`。

## Skills（项目级，.agents/skills/ 与 .claude/skills/ 双镜像）

- **weekly-digest**：自然语言生成 GitHub Trending / Product Hunt 周报；skill 只做意图解析，逻辑在 `weekly_digest/` Python 层。若 `weekly_reports/{source}/{iso_week}-kimi.md` 外部榜单存在，生成时自动合并。
- **daily-report-pipeline**：指定日期跑通 check → repair → extract → analyze → synthesize → publish 门禁流程，严格限定 `created == 目标日期`，门禁脚本见 `docs/agent/pipeline-commands.md`。

⚠️ `.agents/skills/` 与 `.claude/skills/` 是镜像副本，**修改任一份后必须同步另一份**。

## Python environment

Python 依赖通过 `uv` 管理（如需重装：`uv pip install -r pipeline/requirements.txt`）。`run.py` 入口自动加载 `.env` 并注入 `pipeline/config/proxy.json` 代理配置。所有 Python 命令必须通过 `uv run python` 执行；导入使用 `pipeline.` 前缀，项目根目录在 `sys.path` 上。

## Environment variables

- `ANTHROPIC_API_KEY` — required for pipeline LLM calls
- `AI_ENGINE_USE_CLAUDE` — set to `true` to use claude-agent-sdk (default: `false`)
- `PRODUCTHUNT_API_TOKEN` — optional; Product Hunt GraphQL API token（设置后绕过 Cloudflare 挑战走官方 API）
- `JINA_API_KEY` — optional; Jina Reader API key（匿名 r.jina.ai 常被 401/402 拒绝，不可用时应答链回退 Wayback Machine）
- `DATABASE_URL` — required for Stage 5 `publish` (e.g. `postgresql://postgres:postgres@localhost:5433/ai_insight`)；表由 drizzle migrations 管理，pipeline 只写
- `DATA_SNAPSHOT_BASE_URL` — optional; 前端快照回退远程基址，默认 `https://raw.githubusercontent.com/sqliang/daily-ai-insight-engine/data-snapshot/`；本地 `data/snapshot/` 始终优先

## Data directories (all gitignored)

> `data/` 是 pipeline 本地工作存储（含文章正文）；站点读 PostgreSQL，仅 DB 抛错时回退 `data/snapshot/`。

- `data/00_manifest/{source}_{date}.json` — scout URL manifests → publish → `manifests` 表
- `data/01_raw|02_extracted|03_analyzed/{source}/*.md` — 各 stage 的文章正文 + 累积 YAML frontmatter
- `data/04_structured/{source}.json` — 近 `hot_days`(7) 天热数据（最新处理阶段）；`archive/{source}/{source}_{date}.json` 冷数据分片；`all_articles.json` 日报输入（`lookback_days` 窗口）
- `data/05_reports/daily-report[-{date}].json/.md` — 日报输出（含专题洞察块）→ publish → `daily_reports` 表
- `data/snapshot/` — 站点离线快照；publish 成功后自动重建推送（`--skip-snapshot` 可关）

Frontmatter 关键字段：`id`（源 URL 的 SHA-256）、`created`（抓取日期）、`published`、`tldr`/`objective_summary`（Stage 2）、`impact_score`/`sentiment`（Stage 3）、`specialized_tags`/`*_assessment`（专题标注与分析）。

## Source configuration

26 sources (23 active, 3 disabled: `meta-ai-blog` / `microsoft-ai-blog` / `zhihu`) 分 3 tiers（A 学术/技术，B 产品/社区，C 商业/资本），每源上限 5 篇。`pipeline/config.yaml` 定义抓取策略（`rss`/`scrape`/`browser`）、关键词过滤、max age，以及 UI 元数据（`tiers_meta`、`display_name`、`display_description`）。

## Playwright MCP debug output convention

Playwright MCP 工具（`browser_snapshot`、`browser_take_screenshot`）的输出文件一律写到 `debug-output/`（已 gitignore），例如 `debug-output/producthunt-snapshot.md`；写到项目根目录会污染工作区。
