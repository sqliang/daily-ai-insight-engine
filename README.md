# Daily AI Insight Engine

> 四阶段离线 AI 资讯处理流水线 × Next.js 可视化日报看板

Daily AI Insight Engine 从 19 个中英文信源自动采集每日 AI 资讯，经采集→事实提取→深度分析→综合合成四阶段处理，生成包含 Top 事件、深度研判、趋势判断、风险与机会信号的完整日报，并通过 Next.js 仪表盘进行交互式可视化。

---

## 架构一览

```
19 个信源 (arXiv/OpenAI/HN/TechCrunch/知乎...)
        │
        ▼
┌──────────────────────────────────────┐
│  Stage 1: 数据采集 (Scout + Ingest)   │  → data/01_raw/{source}/*.md
│  Stage 2: 事实提取 (BaseInfo + Fact)  │  → data/02_extracted/{source}/*.md
│  Stage 3: 深度分析 (3 维度 × 并发)    │  → data/03_analyzed/{source}/*.md
│  Stage 4a: Frontmatter JSON 聚合      │  → data/04_structured/all_articles.json
│  Stage 4b: Editor-in-Chief 日报合成   │  → data/05_reports/daily-report.json
└──────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────┐
│  Next.js 16 · Recharts · Tailwind     │
│  服务端 readFile → Zod 校验 → 渲染     │
└──────────────────────────────────────┘
```

---

## 快速开始

### 环境要求

- Python 3.11+ + `uv`（Python 依赖管理）
- Node.js 20+ + `pnpm`
- Claude API Key（需设置为环境变量 `ANTHROPIC_API_KEY`）

### 安装

```bash
# 1. 克隆仓库
git clone <repo-url> && cd daily-ai-insight-engine

# 2. 安装 Python 依赖
cd pipeline && uv pip install -r requirements.txt && cd ..

# 3. 安装前端依赖
pnpm install

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env：填入 ANTHROPIC_API_KEY
```

### 运行流水线

```bash
# 完整四阶段运行
python pipeline/run.py scout          # Stage 1a: 生成 URL 清单
python pipeline/run.py ingest         # Stage 1b: 下载清洗正文
python pipeline/run.py extract        # Stage 2: 事实提取
python pipeline/run.py analyze        # Stage 3: 深度分析
python pipeline/run.py aggregate      # Stage 4a: Frontmatter 聚合
python pipeline/run.py synthesize     # Stage 4b: 日报合成
```

支持断点续传 —— 所有阶段默认 `--skip-existing`，已处理的文件自动跳过。重新处理可加 `--force`。

### 启动前端看板

```bash
pnpm dev
# 打开 http://localhost:3000 查看数据源全景（首页）
# 打开 http://localhost:3000/dashboard 查看日报看板
# 打开 http://localhost:3000/report 查看完整报告
```

---

## 项目结构

```
daily-ai-insight-engine/
├── pipeline/                          # Python 离线流水线
│   ├── run.py                         #   统一 CLI 入口
│   ├── config.yaml                    #   19 信源 + LLM 参数 + 配额 + UI 展示元数据
│   ├── core/                          #   共享工具库 (Agent/文件/浏览器/Web/ID/代理)
│   ├── schemas/                       #   Pydantic 数据模型 (4 个 Schema 文件)
│   ├── ingestion/                     #   Stage 1: 信源采集
│   │   └── parsers/                   #   专用解析器 (zhihu/tldrai/machine_heart/anthropic)
│   ├── extraction/                    #   Stage 2: 事实提取
│   ├── analysis/                      #   Stage 3: 多维深度分析
│   │   └── prompts/                   #   三维度 System Prompt
│   └── synthesis/                     #   Stage 4: 聚合 + Editor-in-Chief 合成
│       └── prompts/                   #   System + User Prompt
│
├── src/                               # Next.js 前端
│   ├── app/                           #   App Router 页面
│   │   ├── layout.tsx                 #   根布局 (NavBar)
│   │   ├── page.tsx                   #   数据源全景 (首页, 读取 config.yaml)
│   │   ├── loading.tsx                #   首页骨架屏
│   │   ├── dashboard/
│   │   │   └── page.tsx               #   日报看板 (读取 daily-report.json)
│   │   ├── report/
│   │   │   └── page.tsx               #   完整报告 (Markdown 渲染)
│   │   └── sources/
│   │       ├── page.tsx               #   重定向到 /
│   │       ├── loading.tsx            #   数据源页骨架屏
│   │       └── [name]/
│   │           └── page.tsx           #   数据源详情页
│   ├── components/                    #   React 组件
│   │   ├── layout/                    #   导航栏 + 页面容器
│   │   ├── dashboard/                 #   看板组件 (KPI/图表/信号/深度研判/趋势)
│   │   ├── charts/                    #   图表组件 (Donut/Bar/Radar)
│   │   ├── sources/                   #   数据源组件 (Hero/Grid/Card/ArticleList 等 15 个)
│   │   └── report/                    #   Markdown 渲染器
│   └── lib/                           #   工具库
│       ├── agent/                     #   Zod Schema + Agent 引擎 + 启发式规则
│       ├── data/                      #   文件 I/O + 数据源加载 + 状态管理 + Tier 标签
│       └── report/                    #   标签映射 + Markdown 动态生成
│
├── data/                              # 数据产物 (gitignored)
│   ├── 00_manifest/                   #   URL 清单
│   ├── 01_raw/                        #   清洗后的纯文本
│   ├── 02_extracted/                  #   事实提取层
│   ├── 03_analyzed/                   #   深度分析层
│   ├── 04_structured/                 #   Frontmatter JSON 聚合 (per-source + all_articles)
│   └── 05_reports/                    #   最终日报 (daily-report.json + .md)
│
├── docs/                              # 设计文档
│   ├── 0_整体设计说明.md               #   架构总览
│   ├── 1_数据源筛选与获取设计说明.md     #   Stage 1 详细设计
│   ├── 2_Schema设计说明.md             #   Schema 契约设计
│   ├── 3_核心流程设计说明.md           #   Stage 4 核心流程设计
│   ├── 4-system-requirement.md        #   系统需求文档
│   └── 5_UI设计说明.md                #   前端 UI 设计说明
│
├── rename-to-ids.py                   # 辅助脚本: 按 article ID 重命名文件
```

---

## 黄金三角信源体系

| Tier | 定位 | 信源 | 数量 |
|------|------|------|------|
| **A** | 学术 / 技术前沿 | arXiv CS.AI, OpenAI Blog, Google/DeepMind, Anthropic, NVIDIA, HuggingFace (2 个已禁用) | 6 (4 活跃) |
| **B** | 产品 / 开发者情绪 | Hacker News, Product Hunt, GitHub Trending, Ben's Bites, 知乎 | 5 |
| **C** | 商业 / 资本动向 | TechCrunch, The Verge, KDnuggets, TLDR AI, 机器之心, 量子位, 36氪 | 8 |

每 Tier 配额上限 5 篇，总目标 15 篇，超出按 impact_score 淘汰。支持 RSS / API / HTML 抓取 / 浏览器渲染四种抓取策略。

---

## 数据 Schema

每篇文章经流水线处理后累积 32+ 个结构化字段，分属 5 个评估维度：

| Block | 维度 | 核心字段 | 产出阶段 |
|-------|------|----------|----------|
| 0 | BaseInfo | `id`, `source_type`, `published`, `created` | Stage 2 |
| 1 | FactExtraction | `event_type`, `entities`, `key_logic_flow`, `impact_score` | Stage 2 |
| 2 | QualitativeAssessment | `sentiment`, `developer_sentiment`, `hype_assessment`, `information_entropy` | Stage 3 |
| 3 | ValueAssessment | `compound_value`, `value_capture_layer`, `moat_impact` | Stage 3 |
| 4 | ForesightAndActionability | `risk_matrix`, `market_opportunities`, `actionable_insight` | Stage 3 |

双端 Schema 契约：Python 侧 Pydantic（权威数据源），TypeScript 侧 Zod（前端消费）。

---

## 日报输出

### JSON 报告 (`data/05_reports/daily-report.json`)

```json
{
  "date": "2026-05-08",
  "generatedAt": "2026-05-08T12:00:00Z",
  "reportTitle": "2026-05-08 AI 行业情报日报",
  "executiveSummary": "...",
  "topEvents": [5],
  "deepDives": [3],
  "trendInsights": [4],
  "riskSignals": [5-7],
  "opportunitySignals": [5-7],
  "visualizationData": {
    "eventTypeDistribution": [...],
    "sentimentDistribution": [...],
    "impactRanking": [10],
    "entityFrequency": [20]
  }
}
```

### 看板截图

![看板截图](./dashboard.png)

![数据源页全貌](./sources-page-full.png)

看板包含：
- 执行摘要 + KPI 指标卡片（样本量/信源数/语言覆盖）
- 事件类型 × 情绪分布双 Donut 饼图
- Top 5 事件详情卡片（含影响力评分 + 支撑证据）
- 影响力排名 + 高频实体双栏柱状图
- 4 维度趋势判断（技术/应用/政策/资本）
- 3 篇深度研判（背景/影响/后续关注）
- 风险信号 + 机会信号列表（含严重程度标签）

数据源页包含：
- 深色渐变 Hero Banner（三角顶点卡片 + 统计概览 + 筛选策略）
- 三级分层 Grid（Tier A/B/C 独立区域，彩色竖条标识）
- 信源详情卡片（标签/描述/关键词/文章计数）
- 点击卡片进入详情页，查看该源全部文章

---

## 技术栈

| 层 | 技术 |
|----|------|
| 流水线语言 | Python 3.11+ (asyncio) |
| LLM 调用 | `claude-agent-sdk` (Anthropic) — Sonnet (extract) / Opus (analyze, synthesize) |
| 数据校验 | Pydantic v2 (Python) + Zod (TypeScript) |
| 前端框架 | Next.js 16 App Router + Turbopack |
| 图表 | Recharts + CSS 自定义 |
| 样式 | Tailwind CSS 4 (深色主题, glass morphism) |
| 抓取 | feedparser, trafilatura, readability-lxml, Playwright |
| 包管理 | pnpm (前端), uv (Python) |

---

## 运行命令速查

| 命令 | 用途 |
|------|------|
| `python pipeline/run.py scout` | Stage 1a: 生成 URL 清单 |
| `python pipeline/run.py ingest` | Stage 1b: 下载清洗正文 |
| `python pipeline/run.py extract` | Stage 2: 事实提取 |
| `python pipeline/run.py analyze` | Stage 3: 深度分析 |
| `python pipeline/run.py aggregate` | Stage 4a: Frontmatter 聚合 |
| `python pipeline/run.py synthesize` | Stage 4b: 日报合成 |
| `python pipeline/run.py synthesize --dry-run` | 预估 token 消耗，不调用 LLM |
| `python pipeline/run.py analyze --stage qualitative` | 仅运行单一分析维度 |
| `pnpm dev` | 启动 Next.js 开发服务器 |
| `pnpm validate` | Zod 校验数据文件完整性 |

---

## 设计文档

| 文档 | 内容 |
|------|------|
| [整体设计说明](./docs/0_整体设计说明.md) | 架构总览、数据目录结构、技术栈、信源体系 |
| [数据源筛选与获取设计说明](./docs/1_数据源筛选与获取设计说明.md) | Stage 1 详细设计：Scout/Ingest 流程、四种抓取策略、过滤管线 |
| [Schema 设计说明](./docs/2_Schema设计说明.md) | Pydantic/Zod 双端 Schema 契约、12 种枚举类型、5 Block 架构 |
| [核心流程设计说明](./docs/3_核心流程设计说明.md) | Stage 4 详细设计：Prompt 工程、JSON 解析、数据结构桥接 |
| [系统需求文档](./docs/4-system-requirement.md) | 原始系统需求规格说明 |
| [UI 设计说明](./docs/5_UI设计说明.md) | 前端组件架构、数据流、设计系统、响应式布局 |

---

## 许可证

MIT
