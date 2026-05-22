# Stage 1b Ingest — 正文抓取与清洗

## 模块概览

Ingest 是 Daily AI Insight Engine 流水线的 **Stage 1b**，负责读取 Stage 1a (scout) 生成的 JSON 清单，逐篇下载 HTML、提取 Markdown 正文、按策略截断，最终生成带 YAML frontmatter 的 .md 文件。

**一句话职责**：读清单 → 抓 HTML → trafilatura 提取正文 → 截断 → 写入 .md（含 `extraction_status` 和 `pipeline_stage` 标记）。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)  →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
  URL清单       .md 文件       元信息与事实提取   深度分析         聚合JSON        日报生成
```

## 快速开始

### 基本用法

```bash
# 处理今日所有清单文件（最常用）
uv run python pipeline/run.py ingest

# 强制重新抓取（忽略去重状态）
uv run python pipeline/run.py ingest --force

# 指定并发数
uv run python pipeline/run.py ingest --concurrency 10

# 处理指定清单文件
uv run python pipeline/run.py ingest --manifest arxiv-cs-ai_2026-05-22.json
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--manifest` / `-m` | 今日所有 `*_{today}.json` | 指定清单文件名（不含路径） |
| `--force` | `false` | 忽略去重状态，强制重新抓取所有文章 |
| `--concurrency` / `-c` | `config.yaml` 中 `stages.ingest.concurrency`（默认 5） | 线程池并发数 |

### 作为 Python 模块调用

```python
from pipeline.ingestion.ingest import run_ingest

files = run_ingest(force=False, concurrency=5)
# → [Path("data/01_raw/arxiv/098b39fb.md"), ...]
print(f"生成 {len(files)} 个 .md 文件")
```

## 设计思路

### 双通道并行调度：线程池 + 主线程 browser

24 个数据源的正文获取方式不同，分为两条处理通道：

| 通道 | 策略 | 执行方式 | 适用场景 |
|------|------|----------|----------|
| 常规通道 | `rss` / `scrape` | `ThreadPoolExecutor` 线程池并发 | curl 获取 HTML + trafilatura 提取（线程安全） |
| Browser 通道 | `browser` | 主线程串行 | Playwright 渲染 JS 页面（非线程安全） |

两条通道通过 `contextlib.ExitStack` **同时运行**——线程池提交 task 后立即开始执行，主线程同时处理 browser 文章，互不阻塞。

```python
with ExitStack() as stack:
    executor = stack.enter_context(ThreadPoolExecutor(max_workers=concurrency))
    browser_session = stack.enter_context(BrowserSession())  # 仅在有 browser 文章时

    # 提交常规文章到线程池（立即开始执行）
    for article in regular_items:
        executor.submit(ingest_article, article, ...)

    # 主线程同时处理 browser 文章
    for article in browser_items:
        ingest_browser_article(article, ..., browser_session)

    # 等待线程池完成
    for future in as_completed(futures):
        result = future.result()
```

### fail-per-article：无论成败都生成 .md 文件

每个文章的抓取有 3 种可能的结果，**全部生成 .md 文件**，通过 `extraction_status` 字段标记质量：

| 状态 | 含义 | body 内容 | 下游 Stage 2 行为 |
|------|------|-----------|-------------------|
| `success` | trafilatura 成功提取正文 | 完整 Markdown 正文（可能截断） | 正常提取 |
| `partial` | HTML 获取成功但 trafilatura 无法提取正文 | ⚠️ 警告信息 + manifest 摘要 | 仍尝试提取，日志注明"正文不完整" |
| `failed` | HTML 获取完全失败 | ⚠️ 警告信息 + manifest 摘要 | Stage 2b **跳过** Agent 调用 |

这种设计确保下游阶段始终有文件可处理，不会因部分文章抓取失败而中断整个流水线。

### 正文截断策略

成功提取正文后，按源配置的 `truncation` 规则裁剪（`truncation.py`）：

| 截断模式 | 行为 | 适用源 |
|----------|------|--------|
| `first_n_chars` | 保留前 N 个字符，在段落边界处截断 | 大多数源（默认 3000 字符） |
| `abstract_only` | 仅保留 `> Abstract` 开头的块引用段落 | arXiv 等学术论文源 |
| `none` | 不截断，保留全文 | 官方博客、短文章 |

截断使用段落边界检测（`\n\n`），避免在句子中间切断。

### 线程安全去重（IngestState）

`pipeline/core/concurrency/state.py` 中的 `IngestState` 类：

- 内存中用 `threading.Lock` 保护 `seen_hashes` 集合
- 所有 worker 完成后，主线程调用 `flush_to_disk()` 一次性持久化到 `data/state.json`
- `force=True` 时清空历史状态，所有文章重新抓取
- 自动检测并迁移旧格式 MD5 哈希（12 位 → SHA-256 16 位）
- 双重去重保障：`state.is_seen()` + 磁盘文件存在性检查（防止状态文件与磁盘不一致导致永久跳过）

### 管道阶段标记（pipeline_stage）

每篇 .md 文件的 frontmatter 中写入 `pipeline_stage: "ingested"` 标记，表明文件已完成 Stage 1 处理。下游 Stage 2b 通过检查此字段确认 Stage 2a 是否已执行，从而输出有意义的错误提示而非静默失败。

## 模块结构

```
pipeline/ingestion/ingest/
├── __init__.py          # 包入口，导出 run_ingest
├── cli.py               # CLI 契约：参数声明 + register_subparser + execute
├── orchestrator.py      # 主编排：清单选择 → 文章分类 → ExitStack 并行调度 → 统计
├── worker.py            # 单篇文章抓取 worker（ingest_article + ingest_browser_article）
└── truncation.py        # 正文截断规则（first_n_chars / abstract_only / none）
```

**依赖的核心模块**：

```
pipeline/core/
├── web_utils.py              # fetch_url (curl), extract_article_content (trafilatura), extract_metadata
├── frontmatter_utils.py      # build_ingestion_frontmatter / write_frontmatter / read_frontmatter
├── file_utils.py             # read_json, write_json, resolve_data_dir, ensure_dir
├── id_utils.py               # generate_id (SHA-256, 16位 hex)
├── config_loader.py          # get_source_by_name / get_stage_config
├── browser_utils.py          # BrowserSession (Playwright 生命周期管理)
└── concurrency/state.py      # IngestState (线程安全去重)

pipeline/ingestion/
└── filters.py                # apply_filters（scout 使用，ingest 不使用）
```

## 核心流程

```
run_ingest(manifest_name, force, concurrency)
│
├─ 1. 选择清单文件
│     manifest_name 指定 → 单个文件
│     未指定 → manifest_dir.glob(f"*_{today}.json") 今日所有清单
│     找不到 → 提示"请先运行 scout"，返回 []
│
├─ 2. 初始化 IngestState(force)
│     force=True → 清空历史状态
│     读取 data/state.json → seen_hashes 集合
│     自动检测旧格式 MD5 → 迁移
│
├─ 3. 分类文章：遍历每个清单
│     │
│     ├─ 读取 manifest JSON → source_name, articles[]
│     ├─ 查 config.yaml → fetch_strategy
│     └─ 按 strategy 分类：
│         rss/scrape → regular_items (常规通道)
│         browser    → browser_items (browser 通道)
│
├─ 4. 预扫描去重
│     _needs_ingest(article, target_dir, state)
│     ├─ state.is_seen(id) == False → 需要抓取
│     ├─ state.is_seen(id) == True 但 .md 文件不存在 → 需要抓取
│     └─ state.is_seen(id) == True 且 .md 文件存在 → 跳过
│
├─ 5. ExitStack 并行调度
│     │
│     ├─ ThreadPoolExecutor(max_workers=concurrency)
│     │   提交 regular_items → ingest_article() 并行执行
│     │
│     ├─ BrowserSession()（仅在有 browser 文章时）
│     │   主线程串行执行 ingest_browser_article()
│     │
│     └─ as_completed() 等待线程池完成
│
│     ingest_article(article, source_name, target_dir, state)
│     │
│     ├─ 5a. fetch_url(url) → html (curl 子进程，线程阻塞 I/O)
│     │
│     ├─ 5b. 根据 html 结果分三种情况：
│     │     │
│     │     ├─ html 获取成功 + trafilatura 提取到正文
│     │     │   extraction_status = "success"
│     │     │   content = apply_truncation(content, source_config)
│     │     │   body = content
│     │     │
│     │     ├─ html 获取成功 + trafilatura 无法提取正文
│     │     │   extraction_status = "partial"
│     │     │   content = article.summary  # manifest 兜底
│     │     │   body = "> ⚠️ 正文提取不完整...\n\n" + content
│     │     │
│     │     └─ html 获取失败
│     │         extraction_status = "failed"
│     │         content = article.summary  # manifest 兜底
│     │         body = "> ⚠️ 正文抓取失败...\n\n" + content
│     │
│     ├─ 5c. build_ingestion_frontmatter(...)
│     │     title, source(url), author([[wiki-link]]), published, created,
│     │     description, tags(["clippings"]), extraction_status,
│     │     pipeline_stage("ingested"), id(SHA-256)
│     │
│     ├─ 5d. write_frontmatter(target_dir/{id}.md, fm, body)
│     │
│     └─ 5e. state.mark_seen(id)  # 线程安全
│
│     ingest_browser_article(...) 同理，
│     差异仅在于 html = session.fetch_page_html(url, ...)
│
├─ 6. state.flush_to_disk()
│     所有 worker 完成后，一次性写入 data/state.json
│
└─ 7. 统计提取状态分布
    read_frontmatter 每个输出文件 → 计数 success/partial/failed
    打印: "完成: 总计 N 篇 (success: X, partial: Y, failed: Z), 跳过 K 篇"
```

## 数据流

### 输入

| 数据 | 路径 | 说明 |
|------|------|------|
| URL 清单 | `data/00_manifest/{source}_{date}.json` | Stage 1a 产出，含 articles[].url / title / summary / id 等 |
| 去重状态 | `data/state.json` | 历史已处理文章 ID 集合（`seen_hashes`） |
| 源配置 | `pipeline/config.yaml` | fetch_strategy、truncation、timeout 等 |

### 输出

| 数据 | 路径 | 格式 | 说明 |
|------|------|------|------|
| 原始文章 | `data/01_raw/{source}/{id}.md` | Markdown + YAML frontmatter | 每篇一个文件，供 Stage 2 extraction 消费 |
| 去重状态 | `data/state.json` | JSON | 更新后的已处理文章 ID 集合 |

### Frontmatter 结构

每篇 .md 文件的 YAML frontmatter 包含以下字段：

```yaml
id: "098b39fb4bd5fbf2"              # SHA-256(URL) 前 16 位 hex，流水线全局唯一标识
title: "Interference-Aware Multi-Task Unlearning"
source: "https://arxiv.org/abs/2605.19042"
author:
  - "[[Ying-Hua Huang]]"            # wiki-link 格式
published: "2026-05-20"             # 规范化为 YYYY-MM-DD
created: "2026-05-22"               # 抓取日期
description: "Machine unlearning aims to..."
tags:
  - "clippings"
extraction_status: "success"        # success | partial | failed（正文抓取质量）
pipeline_stage: "ingested"          # 标记已完成 Stage 1
---
正文内容（Markdown）
```

**字段说明**：

| 字段 | 来源 | 说明 |
|------|------|------|
| `id` | `id_utils.generate_id(url)` | SHA-256 前 16 位 hex，确定性生成，贯穿整个流水线 |
| `title` | trafilatura metadata → manifest fallback | 文章原始标题 |
| `source` | manifest URL | 原始链接，可追溯性保障 |
| `author` | trafilatura metadata → manifest fallback | `[[wiki-link]]` 格式列表 |
| `published` | trafilatura metadata → manifest fallback | 规范化为 YYYY-MM-DD |
| `created` | `date.today().isoformat()` | 抓取日期（非发布日期） |
| `description` | trafilatura metadata → manifest summary | 文章摘要 |
| `tags` | 硬编码 `["clippings"]` | 默认标签 |
| `extraction_status` | worker 判定 | `success` / `partial` / `failed` — 供下游 Stage 2 决策 |
| `pipeline_stage` | 硬编码 `"ingested"` | 供下游 Stage 2b 做前置检查 |

### 正文质量标记详解

**`extraction_status = "success"`**

正文成功提取（trafilatura 产出非空内容），body 为完整 Markdown（可能已按 truncation 规则截断）。下游 Stage 2 正常处理。

**`extraction_status = "partial"`**

HTML 获取成功但 trafilatura 无法从中提取正文（常见于 JS 渲染页面、付费墙页面）。body 开头为：

```
> **⚠️ 正文提取不完整**：HTML 获取成功但无法从中提取正文，以下为文章摘要
```

后跟 manifest 中的 summary 字段作为兜底。下游 Stage 2b 仍尝试提取但日志注明"正文不完整"。

**`extraction_status = "failed"`**

HTML 获取完全失败（网络超时、目标服务器拒绝、URL 失效）。body 开头为：

```
> **⚠️ 正文抓取失败**：无法获取页面 HTML（可能原因：网络超时、目标服务器拒绝、URL 失效）
```

或（browser 策略）：

```
> **⚠️ 正文抓取失败**：Playwright 无法渲染页面（可能原因：页面加载超时、目标站点反爬、网络故障）
```

后跟 manifest summary。下游 Stage 2b **直接跳过** Agent 调用（不值得为错误信息调用 LLM）。

## 配置说明

### config.yaml 相关字段

每个数据源中影响 ingest 行为的字段：

```yaml
sources:
  arxiv-cs-ai:
    fetch_strategy: rss           # rss | scrape | browser（影响选择 worker 通道）
    timeout: 30                   # curl / Playwright 超时秒数
    truncation:
      mode: abstract_only         # first_n_chars（默认） | abstract_only | none
      limit: 3000                 # first_n_chars 模式的截断长度
    wait_for: ".css-selector"     # 仅 browser 模式，等待元素出现
    wait_ms: 2000                 # 仅 browser 模式，额外等待毫秒数
    wait_until: "domcontentloaded" # 仅 browser 模式，Playwright 加载策略
    wait_for_fn: "() => ..."      # 仅 browser 模式，自定义等待函数

# Stage 配置
stages:
  ingest:
    concurrency: 5                # 默认线程池并发数
```

## 错误处理

| 场景 | 行为 |
|------|------|
| 清单文件不存在 | 打印提示"请先运行 scout"，返回 `[]` |
| 文章 URL 为空 | 跳过该文章，返回 `None` |
| HTML 获取失败 | `extraction_status = "failed"`，body 为警告 + manifest summary，仍生成 .md |
| trafilatura 无法提取正文 | `extraction_status = "partial"`，body 为警告 + manifest summary，仍生成 .md |
| Playwright 渲染失败 | 同 HTML 获取失败，提示语改为 Playwright 相关 |
| 单个文章异常 | `as_completed` 捕获，打印 `[异常] {title}: {exc}`，**不影响其他文章** |
| 线程池 worker 异常 | `future.result()` 抛出，`try/except` 捕获 |
| 旧格式 MD5 去重数据 | `IngestState._load_raw_state()` 自动检测 12 位哈希 → 重置为空 |

### 幂等性保证

- **去重机制**：`IngestState` 基于 SHA-256 ID 去重，同一 URL 多次运行不会重复抓取
- **双重验证**：`_needs_ingest()` 不仅检查内存状态，还检查磁盘文件存在性，防止状态文件与磁盘不一致
- **`--force`**：清空历史状态，强制重新抓取所有文章
- 文章 ID 由 URL 确定性生成（SHA-256），同一 URL 多次抓取产生相同 ID

## 与其他模块的关系

### 上游（输入）

| 模块 | 说明 |
|------|------|
| `pipeline/ingestion/scout` | Stage 1a，产出 `data/00_manifest/{source}_{date}.json` URL 清单 |
| `pipeline/config.yaml` | 数据源定义（fetch_strategy、truncation、timeout） |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/extraction/` | Stage 2，读取 `data/01_raw/{source}/*.md`，检查 `extraction_status` 和 `pipeline_stage` 做智能决策 |

### 水平依赖（同阶段）

| 模块 | 说明 |
|------|------|
| `pipeline/core/web_utils.py` | `fetch_url`（curl 子进程）、`extract_article_content`（trafilatura）、`extract_metadata` |
| `pipeline/core/frontmatter_utils.py` | `build_ingestion_frontmatter` / `write_frontmatter` |
| `pipeline/core/concurrency/state.py` | `IngestState` 线程安全去重 |
| `pipeline/core/browser_utils.py` | `BrowserSession` Playwright 生命周期管理 |
| `pipeline/ingestion/ingest/truncation.py` | `apply_truncation` 正文截断 |

## 扩展指南

### 新增数据源需关注的 ingest 配置

在 `config.yaml` 中新增数据源时，以下字段直接影响 ingest 行为：

```yaml
sources:
  new-source:
    fetch_strategy: rss       # rss → 常规通道；browser → Playwright 通道
    timeout: 30               # 网络超时
    truncation:
      mode: first_n_chars     # 正文截断模式
      limit: 5000             # 截断长度
```

### 新增截断模式

1. 在 `truncation.py` 的 `apply_truncation()` 中添加新的 `elif mode == "xxx":` 分支
2. 在 `config.yaml` 中将对应源的 `truncation.mode` 设置为新值

### 新增 worker 类型

1. 在 `worker.py` 中实现新的 worker 函数，签名遵循 `(article, source_name, target_dir, state, ...) -> Optional[Path]`
2. 在 `orchestrator.py` 中增加对应的文章分类逻辑和调度代码

### 管道阶段标记扩展

当新增 Stage 3 (analysis) 时，应在成功完成后写入 `pipeline_stage: "analyzed"`，与现有的 `"ingested"` → `"base_info_extracted"` → `"fact_extracted"` 链保持一致。
