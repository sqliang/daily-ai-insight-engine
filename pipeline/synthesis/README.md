# Stage 4b Synthesis — Editor-in-Chief 日报生成

## 模块概览

Synthesis 是 Daily AI Insight Engine 流水线的 **Stage 4b**，负责将 Stage 4a 聚合的结构化文章数据通过 Editor-in-Chief Agent 合成为一份综合性日报。

**一句话职责**：读 `all_articles.json` → Editor-in-Chief Agent 生成结构化日报 → 校验 → 写入 JSON + Markdown。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)  →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
  URL清单        .md文件       事实提取         深度分析        聚合JSON           日报生成
```

## 快速开始

### 基本用法

```bash
# 全量合成（最常用）
uv run python pipeline/run.py synthesize

# 干跑：显示 token 消耗预估值，不调用 LLM
uv run python pipeline/run.py synthesize --dry-run

# 指定模型
uv run python pipeline/run.py synthesize --model claude-opus-4-7

# 指定日报窗口（会先触发 aggregate 预处理）
uv run python pipeline/run.py synthesize --lookback-days 7

# 限制详细展示文章数
uv run python pipeline/run.py synthesize --max-detail 20
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--model` / `-m` | `config.yaml` 中 `llm.models.synthesize.name` | LLM 模型名称 |
| `--dry-run` | `false` | 显示 token 预估值，不调用 LLM |
| `--lookback-days` | `0`（不预处理） | 日报窗口天数，> 0 时先触发 aggregate 预处理 |
| `--hot-days` | `7` | 传递给 aggregate 的热数据窗口 |
| `--max-detail` | `15` | 详细展示文章数上限 |
| `--verbose` / `-v` | `false` | 详细日志输出 |

### 作为 Python 模块调用

```python
from pipeline.synthesis import synthesize_report, generate_markdown

result = synthesize_report(
    model="claude-sonnet-4-6",
    max_detail=15,
    dry_run=False,
)
# → DailyReport Pydantic 实例

markdown = generate_markdown(result)
# → str: Markdown 全文
```

## 模块结构

```
pipeline/synthesis/
├── __init__.py                   # 包入口，导出 synthesize_report / generate_markdown
├── __main__.py                   # python -m pipeline.synthesis 入口
├── cli.py                        # CLI 契约：aggregate 和 synthesize 子命令注册
├── run_synthesis.py              # 主编排：读取 all_articles.json → Editor-in-Chief → 校验 → 写入
├── editor_in_chief_agent.py      # Agent 编排：构建 prompt → 调用 LLM → 解析 JSON → 校验
├── report_generator.py           # JSON → Markdown 报告文件生成
│
└── prompts/                      # 提示词
    ├── __init__.py               # 统一导出
    ├── system_prompt.py          # Editor-in-Chief system prompt（日报格式规范）
    └── user_prompt.py            # User prompt 构建器（注入文章数据）
```

## 核心流程

```
synthesize_report()
│
├─ 1. 读取 data/04_structured/all_articles.json
│     包含 lookback_days 窗口内的所有文章 frontmatter + 统计元数据
│
├─ 2. （可选）aggregate 预处理
│     当 --lookback-days > 0 时，先调用 aggregate_frontmatter() 重新聚合
│
├─ 3. Editor-in-Chief Agent 调用
│     ├─ system prompt: 日报格式规范（reportTitle / executiveSummary / topEvents / ...）
│     ├─ user prompt: 注入文章列表 + 统计摘要
│     ├─ call_agent_with_retry(max_turns=3)
│     ├─ parse_json_response() → dict
│     └─ DailyReport Pydantic 校验
│
├─ 4. 写入报告文件
│     ├─ data/05_reports/daily-report.json         （最新版，前端读取）
│     ├─ data/05_reports/daily-report.md           （最新版 Markdown）
│     ├─ data/05_reports/daily-report-{date}.json  （归档副本）
│     └─ data/05_reports/daily-report-{date}.md    （归档副本）
│
└─ 5. 返回 DailyReport 实例
```

## 设计决策

### Editor-in-Chief 单一 Agent

不同于 Stage 2/3 的多 Agent 并行，Stage 4b 使用单一 Editor-in-Chief Agent。日报需要全局视角——Top 事件排序、跨文章信号提取、整体趋势判断——多 Agent 分治反而破坏连贯性。

### 报告双格式输出

每份报告同时输出 JSON 和 Markdown 两种格式。JSON 供前端仪表盘（`/dashboard/[date]`）结构化渲染 KPI 和图表；Markdown 供全文阅读页（`/report/[date]`）渲染长文。

### 归档副本

每次合成除更新 `daily-report.json`（最新版）外，还写入带日期的归档副本 `daily-report-{date}.json`。前端仪表盘列表页扫描所有 `daily-report-*.json` 展示历史日报卡片。

### 存量字段保护

`report_generator.py` 生成 Markdown 时，对于 JSON 转换场景（无原始 Markdown），通过 `generate_markdown()` 完成 JSON → Markdown 转换。所有 LLM 产出的字段保真传递，不进行二次加工。

## 数据流

### 输入

| 数据 | 路径 | 说明 |
|------|------|------|
| 结构化文章 | `data/04_structured/all_articles.json` | Stage 4a 产出，含日报窗口内所有文章的 frontmatter |

### 输出

| 数据 | 路径 | 说明 |
|------|------|------|
| 日报 JSON | `data/05_reports/daily-report.json` | 最新日报，前端仪表盘读取 |
| 日报 Markdown | `data/05_reports/daily-report.md` | 最新日报全文，前端 `/report/[date]` 渲染 |
| 归档 JSON | `data/05_reports/daily-report-{date}.json` | 历史日报归档，`/dashboard` 列表页扫描 |
| 归档 Markdown | `data/05_reports/daily-report-{date}.md` | 历史日报全文归档 |

## 与其他模块的关系

### 上游（输入）

| 模块 | 说明 |
|------|------|
| `pipeline/aggregation/` | Stage 4a，产出 `all_articles.json` 作为日报生成输入 |
| `pipeline/schemas/daily_report.py` | `DailyReport` 及其 7 个子模型的 Pydantic 定义 |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `src/lib/data/reports.ts` | Next.js 前端，读取日报 JSON/Markdown |
| `src/app/dashboard/` | 仪表盘页，读取 `daily-report-{date}.json` 渲染 |
| `src/app/report/[date]/` | 全文页，读取 `daily-report-{date}.md` 渲染 |

### 水平依赖

| 模块 | 说明 |
|------|------|
| `pipeline/core/agent.py` | `call_agent_with_retry` / `parse_json_response` |
| `pipeline/core/config_loader.py` | LLM 配置 + 路径解析 |
| `pipeline/utils/file_utils.py` | `read_json` / `ensure_dir` |
| `pipeline/aggregation/` | `aggregate_frontmatter`（`--lookback-days > 0` 时） |
