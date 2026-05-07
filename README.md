# Daily AI Insight Engine

AI 舆情分析日报系统 MVP：从每日 AI 新闻中抽取结构化洞察，生成可读分析报告，并用 Next.js Dashboard 展示可视化结果。

本项目围绕笔试题的核心原则实现：**重设计、轻爬虫、巧组装**。它不把原始新闻一次性丢给大模型生成全文，而是采用“单篇结构化抽取 + 全局聚合分析”的离线 pipeline，让处理逻辑、Schema 设计和 AI 使用边界都可以被审查。

## 项目目标

- 获取并保存 10-20 条 AI 相关新闻原始数据。
- 将非结构化新闻转成可排序、可聚合、可视化的结构化数据。
- 基于结构化结果生成 AI 分析日报，包括 Top 事件、深度总结、趋势判断、风险与机会提示。
- 用前端页面展示完整日报和基础图表。

## 技术栈

- Next.js App Router、React、TypeScript
- Tailwind CSS 4
- Zod：Schema 定义与运行时校验
- `@anthropic-ai/claude-agent-sdk`：Agent 分析核心接入点
- pnpm：依赖安装与脚本运行

依赖在 `package.json` 中使用 `latest`，以满足“使用最新版依赖”的要求。当前一次安装解析出的核心版本包括 Next.js 16.2.5、React 19.2.6、Tailwind CSS 4.2.4。

## 数据源说明

MVP 使用 `data/raw/articles.json` 中的 15 条静态样例数据，覆盖英文与中文信源：

- 官方渠道：OpenAI Blog、Google DeepMind Blog、Anthropic News、NVIDIA Blog、Microsoft AI Blog、Meta AI Blog
- 科技媒体：TechCrunch、The Verge、机器之心、量子位、36氪
- 研究与社区：arXiv、Hugging Face、Product Hunt、Hacker News

选择理由：

- 官方渠道适合捕捉模型、产品、平台能力的一手发布。
- 科技媒体适合观察商业化、资本、用户信任和产业竞争。
- 研究与开发者社区适合发现技术路线、开源生态和实践阻力。
- 中英文混合能够避免只看到海外叙事或本土叙事，提升日报的行业完整度。

## 系统架构

```text
data/01_raw/articles.json
        |
        v
Cleaning: 文本清洗、HTML 去噪、长度截断
        |
        v
Map: 单篇文章结构化抽取 StructuredInsight
        |
        v
data/02_processed/structured-insights.json
        |
        v
Reduce: 基于结构化数据生成 DailyReport
        |
        v
data/04_reports/daily-report.json
        |
        v
Next.js Dashboard 静态读取与可视化展示
```

### 关键设计决策

- **读写分离**：耗时、可能失败、需要密钥的 AI pipeline 放在 `scripts/run-pipeline.ts`；前端只读取本地 JSON，避免把长任务放进 Serverless 请求链路。
- **Map-Reduce**：Map 阶段逐篇抽取，Reduce 阶段只聚合已经校验过的结构化结果，满足“不一次性丢给 AI”的限制。
- **Schema first**：`src/lib/agent/schema.ts` 同时约束 pipeline、Agent 输出、验证脚本和前端消费，减少自由文本带来的不稳定。
- **Mock fallback**：默认使用确定性 heuristic 生成示例报告；设置 `AI_ENGINE_USE_CLAUDE=true` 后可走 Claude Agent SDK，便于无 API Key 环境下评审。

## Schema 设计思路

项目定义了三层核心数据模型：

### RawArticle

字段包括 `id`、`title`、`url`、`source`、`language`、`publishedAt`、`summary`、`content`。

设计目的：保留原始数据证据链，让每条洞察都能追溯到标题、来源和发布时间，满足提交要求中的“原始数据文件”和“数据来源说明”。

### StructuredInsight

字段包括 `articleId`、`eventType`、`topicTags`、`entities`、`sentiment`、`impactScore`、`urgencyScore`、`keyFacts`、`risks`、`opportunities`。

设计目的：这不是 summary，而是把文章转成可计算特征：

- `eventType` 用于事件分类和聚类。
- `topicTags` 用于趋势归纳。
- `entities` 用于识别公司、技术、人物、产品和区域热度。
- `impactScore` 用于 Top 事件排序。
- `urgencyScore` 用于判断短期跟踪优先级。
- `sentiment`、`risks`、`opportunities` 服务舆情和决策辅助。

### DailyReport

字段包括 `date`、`dataSourceSummary`、`topEvents`、`deepDives`、`trendInsights`、`riskSignals`、`opportunitySignals`、`visualizationData`。

设计目的：让前端页面无需再次调用模型，直接消费稳定 JSON；同时把可视化数据预计算出来，保证展示层简单可靠。

## AI 使用方式

Agent 层位于 `src/lib/agent/`：

- `prompts.ts` 管理抽取和聚合 Prompt。
- `schema.ts` 定义 Zod Schema。
- `index.ts` 封装 `AIInsightEngine`，提供 `extractArticle` 和 `synthesizeReport`。
- `heuristics.ts` 提供无密钥 fallback，保证示例可复现。

默认运行不会调用外部模型。若需要启用 Claude：

```bash
cp .env.example .env
```

设置：

```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
AI_ENGINE_USE_CLAUDE=true
```

错误处理策略：

- 单篇文章抽取失败时记录错误并跳过，不中断整条 pipeline。
- 所有输出写入前都通过 Zod 校验。
- Reduce 阶段只接收结构化后的 `StructuredInsight[]`，不直接接收原始长文本。

## 目录结构

```text
data/
  raw/articles.json
  processed/structured-insights.json
  reports/daily-report.json
scripts/
  run-pipeline.ts
  validate-report.ts
src/
  app/
    page.tsx
    layout.tsx
    globals.css
  components/dashboard/
  lib/
    agent/
    data/
    report/
```

## 快速启动

安装依赖：

```bash
pnpm install
```

生成结构化结果和日报：

```bash
pnpm pipeline
```

校验数据文件：

```bash
pnpm validate
```

启动前端：

```bash
pnpm dev
```

访问：

```text
http://localhost:3000
```

## 输出结果示例

- 原始数据：`data/01_raw/articles.json`
- 单篇结构化抽取结果：`data/02_processed/structured-insights.json`
- 完整 AI 分析日报：`data/04_reports/daily-report.json`
- 可视化页面：`src/app/page.tsx`

## 验证命令

```bash
pnpm typecheck
pnpm validate
pnpm build
pnpm lint
```

## 局限性与后续优化

- 当前数据源为静态整理，后续可增加 RSS/API 抓取模块。
- 当前可视化使用轻量 CSS 图表，后续可接入 Recharts 或 ECharts 增强交互。
- 当前默认 heuristic fallback，后续可针对 Claude Agent SDK 增加更严格的 JSON repair 和重试策略。
- 可增加人工审核界面，在日报发布前调整风险级别和事件优先级。
- 可将日报读取能力封装为 MCP Server，供其他 Agent 工作流调用。
