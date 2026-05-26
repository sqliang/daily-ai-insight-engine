# Stage 1 Ingestion — 数据获取

## 模块概览

Ingestion 是 Daily AI Insight Engine 流水线的 **Stage 1**，负责从 19 个中英文 AI 数据源获取文章列表并抓取正文内容。

**一句话职责**：读 config.yaml → 按策略抓取文章列表 → 过滤 → 生成 ID → 下载正文 → 清洗 → 写入 .md。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)  →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
  URL清单        .md文件       事实提取         深度分析        聚合JSON           日报生成
```

## 子阶段

| 子阶段 | 目录 | 文档 | 职责 |
|--------|------|------|------|
| Stage 1a — Scout | [`scout/`](scout/) | [scout/README.md](scout/README.md) | URL 清单生成：四种抓取策略、过滤管道、断点续传 |
| Stage 1b — Ingest | [`ingest/`](ingest/) | [ingest/README.md](ingest/README.md) | 正文抓取：双通道并行调度、正文清洗、截断策略、去重机制 |

## 模块结构

```
pipeline/ingestion/
├── __init__.py                   # 包入口
├── filters.py                    # 关键词/时效/数量过滤器（scout + ingest 共用）
├── html_utils.py                 # HTML 清洗与正文抽取辅助
│
├── scout/                        # Stage 1a — URL 清单生成
│   ├── README.md
│   ├── cli.py                    #  CLI 契约
│   ├── orchestrator.py           #  主编排：遍历数据源 → 策略执行 → 过滤 → 写入 JSON
│   ├── strategies.py             #  四种抓取策略：rss / api / scrape / browser
│   └── manifest_writer.py        #  JSON 清单写入 + 增量更新
│
├── ingest/                       # Stage 1b — 正文抓取
│   ├── README.md
│   ├── cli.py                    #  CLI 契约
│   ├── orchestrator.py           #  主编排：清单读取 → 双通道并行 → 写入 .md
│   ├── worker.py                 #  单篇文章抓取：curl / Playwright → trafilatura → 清洗
│   └── truncation.py             #  正文截断策略
│
├── backfill_ids/                 # 辅助工具：旧文件 ID 回填
│   ├── cli.py
│   └── __main__.py
│
└── parsers/                      # 专用解析器（按数据源定制）
    ├── anthropic.py              #  Anthropic sitemap 解析
    ├── machine_heart.py          #  机器之心 HTML 解析
    ├── openai.py                 #  OpenAI RSS 解析
    ├── tldrai.py                 #  TLDR AI HTML 解析
    └── zhihu.py                  #  知乎浏览器渲染 + 解析
```

## 核心流程

```
config.yaml
    │  19 个数据源, 3 个 tier (A/B/C)
    │  fetch_strategy: rss | api | scrape | browser
    ▼
Stage 1a: scout ─────────────────────────────────────────▶ data/00_manifest/{source}_{date}.json
    │  遍历数据源 → 按策略抓取文章列表 → 关键词过滤 → 生成 SHA-256 ID
    │  每个源最多 5 篇，每天一份清单
    ▼
Stage 1b: ingest ─────────────────────────────────────────▶ data/01_raw/{source}/{id}.md
    │  读取清单 → 双通道并行调度 → curl/Playwright 抓取正文
    │  → trafilatura 清洗 → 截断 → YAML frontmatter + Markdown 正文
    │  每篇文章一个 .md 文件，含基础元信息 (id / title / source / published / created)
```

## 设计决策

### 四种抓取策略

| 策略 | 适用场景 | 实现方式 |
|------|---------|---------|
| `rss` | 有标准 RSS/Atom feed 的源 | `feedparser` 解析 + 关键词过滤 |
| `api` | 提供 JSON API 的源 | `curl` + JSON 解析（如 Hacker News Algolia） |
| `scrape` | 无 feed 但有可预测 HTML 结构的源 | `curl` + 专用解析器 |
| `browser` | JS 渲染页面（如 知乎） | Playwright 渲染 + 专用解析器 |

### 断点续传与幂等性

- **Scout**：每天一份 URL 清单，默认跳过已存在的当日清单（`--force` 覆盖）
- **Ingest**：通过 SHA-256 ID 去重，`state.json` 记录已抓取的 seen_hashes，`--skip-existing` 跳过已抓取文章
- 两次运行之间的增量处理天然安全——新文章追加，已有文章跳过

### 正文截断控制成本

每个源可配置独立的 `max_chars` 截断长度（默认 3000 字符）。截断后的正文存储为 .md 正文，原始长度记录在 frontmatter 的 `original_length` 字段中。截断点选择自然句子边界，避免截断在词中间。

### 专用解析器

对于结构特殊的源（如 Anthropic sitemap、机器之心、知乎），通过 `parsers/` 中的专用模块处理。这些解析器处理特定源的 HTML 结构、日期格式、标题提取等细节，保证提取质量。

## 与其他模块的关系

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/extraction/` | Stage 2，读取 `data/01_raw/` 中的 .md 文件进行 BaseInfo + FactExtraction |
| `pipeline/aggregation/` | Stage 4a，扫描 `data/01_raw/` 聚合 frontmatter 到 JSON |

### 水平依赖

| 模块 | 说明 |
|------|------|
| `pipeline/core/web_utils.py` | `fetch_url` / `fetch_rss_items` — HTTP/RSS 抓取 |
| `pipeline/core/browser_utils.py` | Playwright 生命周期管理 |
| `pipeline/core/config_loader.py` | `get_sources` / `resolve_data_dir` — 配置加载 |
| `pipeline/core/concurrency/state.py` | `IngestState` — 线程安全去重状态 |
| `pipeline/utils/file_utils.py` | `ensure_dir` / `read_json` / `write_json` |
| `pipeline/utils/id_utils.py` | `generate_id` — SHA-256 ID 生成 |
