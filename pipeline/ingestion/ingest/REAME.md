# Stage 1b Ingest — 正文抓取与清洗

## 模块概览

Ingest 是 Daily AI Insight Engine 流水线的 **Stage 1b**，负责将 Stage 1a (scout) 产出的文章 URL 清单逐个下载、提取正文、清洗并输出为带有 YAML frontmatter 的标准 Markdown 文件。

**一句话职责**：读 URL 清单 → 下载 HTML → 提取 Markdown 正文 → 截断清洗 → 写入 .md 文件。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)  →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
   URL清单        .md文件       事实提取         深度分析         聚合JSON          日报生成
```

## 快速开始

### 基本用法

```bash
# 处理今天 scout 产出的所有清单（最常用）
uv run python pipeline/run.py ingest

# 指定某个清单文件
uv run python pipeline/run.py ingest --manifest arxiv-cs-ai_2026-05-21.json

# 强制重新抓取（忽略去重状态）
uv run python pipeline/run.py ingest --force

# 指定并发线程数（默认 5）
uv run python pipeline/run.py ingest --concurrency 8
```

### 参数说明

| 参数 | 简写 | 默认值 | 说明 |
|------|------|--------|------|
| `--manifest` | `-m` | 无 (处理今日全部) | 指定清单文件名，不含路径 |
| `--force` | — | `false` | 忽略去重状态，强制重新抓取 |
| `--concurrency` | `-c` | config → 5 | 线程池并发数 |

并发数解析优先级：**CLI 参数 > config.yaml (`stages.ingest.concurrency`) > 默认值 5**。

### 作为 Python 模块调用

```python
from pipeline.ingestion.ingest import run_ingest

files = run_ingest(
    manifest_name="arxiv-cs-ai_2026-05-21.json",  # None = 今日全部
    force=False,
    concurrency=5,
)
print(f"生成了 {len(files)} 个文件")
```

## 设计思路

### 为什么用 ThreadPoolExecutor 而非 asyncio？

Ingest 的 I/O 是阻塞式的：
- HTTP 抓取通过 `subprocess.run(["curl", ...])`（子进程调用）
- 正文提取通过 `trafilatura.extract()`（同步库）

这些调用无法 await，放在 asyncio 事件循环中会阻塞整个 loop。虽然可以用 `run_in_executor` 包装，但会增加代码复杂度却无实际收益。

Stage 2/3 用 asyncio 是因为它们调用 `claude-agent-sdk`（async-native）。Ingest 的场景不同，线程池是更合适的选择。

> 核心并发模块 `pipeline/core/concurrency/runner.py` 同时提供了 ThreadPool 和 asyncio 两种模式的 `TaskRunner`，供后续其他阶段复用。

### 双通道设计：常规 vs Browser

19 个数据源中使用两种 HTML 获取方式：

| 策略 | 源数量 | 获取方式 | 线程安全？ |
|------|--------|----------|------------|
| `rss` / `scrape` | 18 个 | `curl` 子进程 | ✅ 子进程天然隔离 |
| `browser` | 1 个（知乎） | Playwright 同步 API | ❌ BrowserSession 不可跨线程共享 |

对于 browser 策略，采用**双通道并行**模型：
- **通道 1（线程池）**：常规文章通过 `ThreadPoolExecutor` 并发抓取
- **通道 2（主线程）**：browser 文章在主线程串行处理，复用单个 `BrowserSession`

两个通道通过 `ExitStack` 同时管理，**并行运行**，共享同一个线程安全的 `IngestState`。

### 去重策略

文章 ID 由 `SHA-256(source_url)` 的前 16 位 hex 字符生成，确定性、幂等。去重状态存储在 `data/state/ingest_state.json`，通过 `threading.Lock` 保护内存中的 set，所有 worker 完成后一次性 flush 到磁盘。

预扫描去重采用双重验证：既检查 `state.json` 记录，也验证磁盘上 `.md` 文件是否确实存在。仅靠 state 记录会在文件被误删时永久跳过文章。

**为什么不逐篇写状态文件？** 逐篇写意味着磁盘 I/O 成为瓶颈，且需要文件锁保护。内存 set + 一次性 flush 的方案更简单，代价是中途崩溃会丢失本次 run 的进度（但幂等 ID + 文件存在性验证保证重跑不会产生重复数据）。

## 模块结构

```
pipeline/ingestion/ingest/
├── __init__.py          # 包入口，导出 run_ingest
├── __main__.py          # uv run python -m pipeline.ingestion.ingest 入口
├── cli.py               # CLI 契约：参数声明 + 注册子命令
├── orchestrator.py      # 主编排：选清单 → 分类 → ExitStack 并行调度 → flush
├── worker.py            # 单篇文章抓取 worker（两种通道）
└── truncation.py        # 正文截断规则
```

**依赖的核心模块**：

```
pipeline/core/
├── concurrency/
│   ├── state.py         # 线程安全 IngestState（去重状态管理）
│   └── runner.py        # 通用 TaskRunner（ThreadPool + asyncio 双模式）
├── web_utils.py         # fetch_url (curl), extract_article_content (trafilatura)
├── frontmatter_utils.py # 构建与写入 YAML frontmatter
├── id_utils.py          # SHA-256 文章 ID 生成
├── config_loader.py     # YAML 配置读取与缓存
├── file_utils.py        # JSON 读写 + 目录工具
└── browser_utils.py     # BrowserSession（Playwright 生命周期管理）
```

## 核心流程

```
run_ingest(manifest_name, force, concurrency)
│
├─ 1. 选择清单文件
│     指定 --manifest → 单个文件
│     未指定 → glob data/00_manifest/*_{today}.json（全部今日清单）
│
├─ 2. IngestState(force=force)
│     读取 data/state/ingest_state.json → 加载已处理 ID 集合
│     force=True → 清空集合，重新开始
│     自动检测旧格式 MD5 哈希（12位），迁移为 SHA-256（16位）
│
├─ 3. 遍历清单，按 fetch_strategy 分类文章
│     browser_articles  = []     # fetch_strategy == "browser"（仅知乎）
│     regular_articles  = []     # fetch_strategy == "rss" | "scrape"
│     同时解析 source_config → target_dir，创建目录
│
├─ 4. 预扫描去重
│     遍历两类文章列表，调 state.is_seen() 过滤已处理文章
│     → 减少无用任务提交，提前报 "所有文章已处理"
│
├─ 5. ExitStack 并行调度
│     ┌─ ExitStack ───────────────────────────────────────┐
│     │                                                    │
│     │  ThreadPoolExecutor(max_workers=concurrency)       │
│     │  ├─ executor.submit(ingest_article, ...) × N       │
│     │  │  每个 worker: curl → trafilatura → truncation  │
│     │  │              → write .md → state.mark_seen()   │
│     │  └─ 与 BrowserSession 并行运行                      │
│     │                                                    │
│     │  BrowserSession()  [仅在 browser_items 非空时]      │
│     │  ├─ ingest_browser_article(...) × M (主线程串行)    │
│     │  │  每个: Playwright → trafilatura → truncation   │
│     │  │        → write .md → state.mark_seen()         │
│     │  └─ 与线程池共享 IngestState（Lock 保护）           │
│     │                                                    │
│     │  等待 as_completed(futures) → 收集结果              │
│     └────────────────────────────────────────────────────┘│
│
├─ 6. state.flush_to_disk()
│     将内存中的 seen_hashes 集合写入 state.json
│     记录 last_ingest 时间戳
│
└─ 7. 输出统计 + 返回文件路径列表
```

### 时间线示意（Browser + 线程池并行）

```
ThreadPool (curl)   │████████████████████████████████████████│  ← N 篇常规文章
Main (browser)      │  ████████ (知乎 5篇)  │                  ← M 篇 browser 文章
                    └── 并行执行 ───────────┘
```

### 单篇文章 Worker 流程

```
ingest_article(article, source_name, target_dir, state)
│
├─ article_id = article["id"] or SHA-256(article["url"])
│  （去重判断由 orchestrator 的 _needs_ingest() 统一处理，
│    worker 不再自行检查 is_seen）
│
├─ fetch_url(url, timeout)          # curl -s -L --max-time N
│   │
│   ├─ 成功 ─┐
│   │        ├─ extract_metadata(html, url)      # trafilatura 元数据
│   │        ├─ extract_article_content(html)    # trafilatura 正文 (Markdown)
│   │        │   │
│   │        │   ├─ content 非空 → extraction_status = "success"
│   │        │   │                apply_truncation(content, cfg)
│   │        │   │
│   │        │   └─ content 为空 → extraction_status = "partial"
│   │        │                     body = manifest summary + 提示语
│   │        │
│   │        └─ 继续到写文件步骤
│   │
│   └─ 失败 → extraction_status = "failed"
│              body = 错误说明 + manifest summary
│              meta 为空，用 manifest 元数据兜底
│              → 继续到写文件步骤（不 return None）
│
├─ build_ingestion_frontmatter(..., extraction_status=...)  # 含提取状态
├─ write_frontmatter(path, fm, body)  # 写入 .md 文件
├─ state.mark_seen(article_id)        # 标记已处理
└─ 返回 Path
```

## 数据流

### 输入

| 数据 | 路径 | 格式 | 说明 |
|------|------|------|------|
| URL 清单 | `data/00_manifest/{source}_{date}.json` | JSON | scout 阶段产出，含 `articles[]` 数组 |
| 源配置 | `pipeline/config.yaml` | YAML | fetch_strategy、timeout、truncation、target_dir 等 |
| 去重状态 | `data/state/ingest_state.json` | JSON | `{"seen_hashes": [...], "last_ingest": "..."}` |

### 输出

| 数据 | 路径 | 格式 | 说明 |
|------|------|------|------|
| 文章文件 | `data/01_raw/{target_dir}/{article_id}.md` | Markdown | YAML frontmatter + Markdown 正文 |
| 去重状态 | `data/state/ingest_state.json` | JSON | 更新后的去重列表 |

### 输出文件 Frontmatter 字段

```yaml
---
title: "文章标题"
source: "https://original.url/article"
author:
  - "[[Author Name]]"
published: "2026-05-20"
created: "2026-05-21"
description: "文章摘要或描述"
tags:
  - clippings
id: "098b39fb4bd5fbf2"   # SHA-256(url) 前 16 位，流水线全局唯一 ID
extraction_status: success  # 正文提取状态：success | partial | failed
---
```

**extraction_status 字段说明：**

| 值 | 含义 | 触发条件 |
|------|------|------|
| `success` | 正文提取成功 | HTML 获取成功 + trafilatura 提取出正文 |
| `partial` | 部分提取 | HTML 获取成功但 trafilatura 未能提取正文，body 为 manifest summary 兜底 + 提示语 |
| `failed` | 抓取失败 | HTML 获取失败（网络超时 / 服务端拒绝 / URL 失效），body 为错误说明 + manifest summary |

下游阶段可依据 `extraction_status` 判断内容质量，跳过或降级处理 `failed` 和 `partial` 文章。

## 配置说明

### config.yaml 相关字段

每个数据源配置影响 ingest 行为的字段：

```yaml
sources:
  arxiv-cs-ai:
    fetch_strategy: rss          # rss | scrape | browser
    timeout: 30                  # curl/Playwright 超时秒数（默认 30）
    target_dir: arxiv            # 输出子目录名（默认与 source name 相同）
    truncation:
      mode: abstract_only        # first_n_chars | abstract_only | none
      limit: 3000                # 仅 first_n_chars 模式生效
    wait_for: ".css-selector"     # 仅 browser 模式，等待元素出现
```

全局 ingest 配置：

```yaml
stages:
  ingest:
    concurrency: 5               # 线程池并发数（CLI 参数可覆盖）
    time_window_hours: 48        # 时效性窗口
    max_articles_per_source: 5   # 每源最大文章数
```

### 截断模式详解

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| `first_n_chars` | 保留前 N 个字符，在段落边界截断 | 博客、新闻（保留开头核心内容） |
| `abstract_only` | 仅保留 `> Abstract` 开头的 blockquote 段落 | arXiv 学术论文（摘要即核心） |
| `none` | 不截断，保留全文 | Hacker News 短摘要、GitHub Trending |

## 并发模型

### 线程安全保证

| 共享资源 | 保护方式 | 竞争情况 |
|----------|----------|----------|
| `IngestState._seen_ids` | `threading.Lock` | 低 — 仅 add/contains，锁持有时间微秒级 |
| `config_loader._config_cache` | GIL — 启动后只读 | 无 |
| `write_frontmatter()` → 文件写入 | 文件名基于唯一 ID | 无 — 两篇不同文章不可能写同一个文件 |
| `os.environ`（代理配置） | GIL — 启动时设置，运行时只读 | 无 |
| `BrowserSession` | 仅主线程访问 | 无 — worker 线程不碰 Playwright |

### 并发度选择建议

- **1-2**：保守，接近串行速度，适合调试
- **5**（默认）：平衡选择，网络 I/O 与 CPU（trafilatura）重叠良好
- **8-10**：激进，网络带宽充足时可尝试，注意 curl 子进程数量

## 错误处理与恢复

### 鲁棒性保证

**每篇 manifest 中的文章都会生成对应的 `.md` 文件**，无论抓取是否成功：

- HTML 获取成功 + trafilatura 提取正文 → `extraction_status: success`，body 为 Markdown 正文
- HTML 获取成功但 trafilatura 无法提取 → `extraction_status: partial`，body 为 manifest summary + 提示语
- HTML 获取失败（超时/拒绝/失效） → `extraction_status: failed`，body 为错误说明 + manifest summary

### 文件存在性验证

预扫描去重时会同时检查 `state.json` 记录和磁盘上的 `.md` 文件。即使 state 认为已处理，若对应 `.md` 文件被误删，也会自动重新抓取。这防止了 state 与磁盘不一致导致的永久跳过。

### 中途崩溃（Ctrl+C / 进程被杀）

- `ExitStack` 自动清理 `ThreadPoolExecutor`（取消 pending futures）和 `BrowserSession`
- `flush_to_disk()` **未被调用** → `state.json` 保持上次成功 run 的状态
- 已写入的 `.md` 文件保留在磁盘上
- **恢复方式**：重新运行 `ingest`（不带 `--force`），文件存在性验证会正确处理：已有文件的跳过，缺失文件的补抓

### 旧格式迁移

- 自动检测 `state.json` 中的旧格式 MD5 哈希（12 位 hex），检测到时自动重置去重列表并打印提示

## 与其他模块的关系

### 上游（输入）

| 模块 | 说明 |
|------|------|
| `pipeline/ingestion/scout` | Stage 1a，产出 URL 清单 JSON（`data/00_manifest/`） |
| `pipeline/config.yaml` | 数据源配置（fetch_strategy、truncation 等） |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/extraction` | Stage 2，读取 `data/01_raw/` 中的 .md 文件，提取 BaseInfo 和结构化事实 |

### 同层（复用）

| 模块 | 说明 |
|------|------|
| `pipeline/core/concurrency/state.py` | `IngestState` 可被其他需要去重的阶段复用 |
| `pipeline/core/concurrency/runner.py` | `TaskRunner` 可被 scout 等其他阶段用于并发调度 |

## 扩展指南

### 新增 fetch_strategy

1. 在 `worker.py` 中添加新的 worker 函数（参考 `ingest_browser_article` 的模式）
2. 在 `orchestrator.py` 的分类步骤中增加新的识别逻辑
3. 在 `config.yaml` 中将源的 `fetch_strategy` 设置为新值

### 新增截断模式

1. 在 `truncation.py` 的 `apply_truncation()` 中添加新分支
2. 在 `config.yaml` 中将源的 `truncation.mode` 设置为新值
3. 确保新模式有合理的 fallback（如 `abstract_only` 模式在无 abstract 时 fallback 到 `body[:3000]`）
