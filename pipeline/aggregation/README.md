# Stage 4a Aggregation — Frontmatter 聚合

## 模块概览

Aggregation 是 Daily AI Insight Engine 流水线的 **Stage 4a**，负责扫描所有 stage 目录（`01_raw/` + `02_extracted/` + `03_analyzed/`）中的 `.md` 文件，提取 YAML frontmatter 并按 source 聚合为 per-source JSON 和 all_articles.json。

**一句话职责**：多阶段目录扫描 → 按 `(source, article_id)` 去重（优先级 03 > 02 > 01）→ 提取 frontmatter → 热冷分离 → 写入 JSON。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)  →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
  URL清单        .md文件       事实提取         深度分析        聚合JSON           日报生成
```

**核心设计理念**：纯机械操作，零 LLM 调用，< 1 秒完成。无论哪个阶段触发聚合（extraction 完成、analysis 完成、CLI 手动、synthesize 预处理），结果始终一致——每个 source 的 JSON 包含所有文章在其最新处理阶段的完整 frontmatter。

## 与各阶段的调用关系

```
extraction/orchestrator.py  ──┐
analysis/run_analysis.py    ──┼── aggregate_frontmatter() ──▶ data/04_structured/
synthesis/cli.py (aggregate) ──┤                              ├── {source}.json          (热数据)
synthesis/cli.py (synthesize)──┘                              ├── all_articles.json      (日报输入)
                                                              └── archive/{source}/      (冷数据)
```

Aggregation 是**跨阶段的横向切面**，不属于任何一个 stage，因此独立为 `pipeline/aggregation/`。

## 快速开始

### 基本用法

```bash
# 全量聚合：扫描三目录，按优先级去重（最常用）
uv run python pipeline/run.py aggregate

# 指定输入目录（单目录扫描，兼容旧用法）
uv run python pipeline/run.py aggregate --input data/03_analyzed/

# 指定日报窗口天数和热数据窗口
uv run python pipeline/run.py aggregate --lookback-days 7 --hot-days 14

# 干跑预览
uv run python pipeline/run.py aggregate --dry-run
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--input` / `-i` | 自动扫描三目录 | 输入目录（指定时仅扫描该目录） |
| `--output` / `-o` | `data/04_structured/` | 输出目录 |
| `--lookback-days` | `config.yaml` 中 `stages.aggregate.lookback_days`（1） | `all_articles.json` 日报时间窗口（天） |
| `--hot-days` | `config.yaml` 中 `stages.aggregate.hot_days`（7） | per-source JSON 热数据窗口（天） |
| `--max-history-days` | `config.yaml` 中 `stages.aggregate.max_history_days`（365） | archive 分片最大保留天数 |
| `--dry-run` | `false` | 只列出文件，不实际输出 |

### 作为 Python 模块调用

```python
from pipeline.aggregation import aggregate_frontmatter

result = aggregate_frontmatter(
    output_dir="data/04_structured/",
    lookback_days=1,
    hot_days=7,
    dry_run=False,
)
# → {"total_articles": 81, "sources": 24, "errors": 1, "archived": 333, ...}
```

## 模块结构

```
pipeline/aggregation/
├── __init__.py                   # 包入口，导出 aggregate_frontmatter
└── aggregate_frontmatter.py      # 核心聚合逻辑：扫描 + 去重 + 热冷分离 + archive 清理
```

## 核心流程

### 多阶段扫描策略

默认不指定 `input_dir` 时，同时扫描三个目录，按优先级去重：

```
data/03_analyzed/{source}/*.md  ──┐  优先级最高（已分析）
data/02_extracted/{source}/*.md ──┤
data/01_raw/{source}/*.md       ──┘  优先级最低（仅抓取）
                                      │
                              按 (source_subdir, filename_stem) 去重
                              首次遇见胜出 → 保留最完整版本
                                      │
                                      ▼
                              提取 frontmatter → 校验 → 输出 JSON
```

### 热冷分离

```
提取的 frontmatter
    │
    ├─ created >= today - hot_days  ──▶  {source}.json          (热数据，始终加载)
    │
    └─ created < today - hot_days   ──▶  archive/{source}/       (冷数据，按需加载)
                                         {source}_{date}.json     (按 created 日期分片)
```

### 两步过滤

| 步骤 | 过滤条件 | 影响的输出 |
|------|---------|-----------|
| 热冷分流 | `created >= today - hot_days` | `{source}.json` vs `archive/{source}/` |
| 日报窗口 | `created >= today - lookback_days` | `all_articles.json`（日报输入） |

`hot_days` 控制前端数据加载速度（值越小 → per-source JSON 越小 → 加载越快）。`lookback_days` 控制日报覆盖范围（值越大 → 日报包含更多历史文章）。

## 去重逻辑

每个 `.md` 文件通过其路径标识：`(source_subdir, filename_stem)`。目录扫描顺序为 `03_analyzed` > `02_extracted` > `01_raw`，首次遇见的版本胜出。

例如：同一篇文章 `abc123.md` 同时存在于 `02_extracted/arxiv-cs-ai/` 和 `03_analyzed/arxiv-cs-ai/`，扫描时优先扫描 `03_analyzed`，因此保留已分析的版本。

## 设计决策

### 通用聚合工具，不绑定特定阶段

`aggregate_frontmatter()` 不依赖 Stage 2/3/4 的任何内部逻辑，仅依赖 `pipeline.utils`、`pipeline.schemas` 和 `pipeline.core.config_loader`。这使得它可以被 extraction、analysis、synthesis 三个阶段安全地调用，形成干净的横向依赖关系。

### 纯机械操作，零 LLM 调用

聚合过程只涉及文件系统 I/O、YAML 解析和 JSON 序列化，不消耗 token。即使 700+ 个 .md 文件，聚合也在 1 秒内完成。

### 覆盖写策略

- `{source}.json` 每次 aggregate 覆盖写（文章可能被后续阶段更新，需重新聚合 frontmatter）
- archive 分片每次 aggregate 覆盖写（同样原因）
- `all_articles.json` 每次 aggregate 覆盖写（日报输入始终反映最新状态）
- 过期 archive 分片（超过 `max_history_days`）自动清理

### Pydantic 校验非阻塞

aggregate 对 frontmatter 进行 Pydantic 校验（`DailyAIInsight` 模型），但校验失败仅记录警告，文章仍正常输出到 JSON。这确保旧数据或格式不完美的数据不会丢失。

## 与其他模块的关系

### 上游（输入）

| 数据 | 路径 | 说明 |
|------|------|------|
| 原始文章 | `data/01_raw/{source}/*.md` | Stage 1b 产出，含基础元信息 |
| 已提取文章 | `data/02_extracted/{source}/*.md` | Stage 2 产出，含 BaseInfo + FactExtraction |
| 已分析文章 | `data/03_analyzed/{source}/*.md` | Stage 3 产出，含三维度分析字段 |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/synthesis/run_synthesis.py` | Stage 4b，读取 `all_articles.json` 作为日报生成输入 |
| `src/lib/data/sources.ts` | Next.js 前端，读取 per-source JSON + archive 分片渲染信源详情页 |
| `src/app/dashboard/` | Next.js 前端，读取 `all_articles.json` 渲染仪表盘 KPI 和图表 |

### 水平依赖

| 模块 | 说明 |
|------|------|
| `pipeline/core/config_loader.py` | `get_stage_config` / `resolve_data_dir` — 路径解析 |
| `pipeline/utils/file_utils.py` | `ensure_dir` — 目录创建 |
| `pipeline/utils/frontmatter.py` | `read_frontmatter` — YAML frontmatter 解析 |
| `pipeline/utils/schema_utils.py` | `flat_frontmatter_to_nested` — 扁平字段 → Pydantic 嵌套模型 |
| `pipeline/schemas/daily_ai_insight.py` | `DailyAIInsight` — 数据校验 |
