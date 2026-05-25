# Stage 1a Scout — URL 清单生成

## 模块概览

Scout 是 Daily AI Insight Engine 流水线的 **Stage 1a**，负责遍历所有启用的数据源，按各自的 `fetch_strategy` 抓取文章列表（URL + 标题 + 摘要），应用过滤规则后生成标准化的 JSON 清单文件。

**一句话职责**：读 config.yaml → 按策略抓取文章列表 → 过滤 → 生成 ID → 写入 JSON 清单。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)  →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
  URL清单        .md文件       事实提取         深度分析         聚合JSON          日报生成
```

## 快速开始

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--force` | `false` | 忽略已存在的当日清单，全部重新抓取（即使清单文件已存在） |

### 基本用法

```bash
# 抓取所有已启用数据源的最新文章列表（最常用）
uv run python pipeline/run.py scout

# 强制重新抓取（忽略已存在的今日清单，全部重新获取）
uv run python pipeline/run.py scout --force
```

日常首次运行会为每个启用的数据源生成 `data/00_manifest/{source}_{today}.json`；已存在当日清单的源自动跳过（幂等）。预期输出示例：

```
=== Stage 1 Scout: URL 清单生成 ===
[arxiv-cs-ai] rss: 15 篇文章
[openai-blog] rss: 3 篇文章
...
总计: 19 个源, 87 篇文章
```

查看抓取结果：

```bash
# 列出今日生成的所有清单文件
ls data/00_manifest/*_$(date +%Y-%m-%d).json

# 查看某个源的清单内容（含文章标题、URL、SHA-256 ID）
cat data/00_manifest/arxiv-cs-ai_$(date +%Y-%m-%d).json | python -m json.tool | head -40

# 查看人类可读的 Markdown 汇总清单
cat data/00_manifest/$(date +%Y-%m-%d)-manifest-*.md
```

与下游 ingest 串联运行：

```bash
# 先 scout 生成清单，再 ingest 抓取正文
uv run python pipeline/run.py scout && uv run python pipeline/run.py ingest
```

作为 Python 模块调用：

```python
from pipeline.ingestion.scout import run_scout

# 正常抓取，返回 {source_name: [articles]} 字典
manifests = run_scout(force=False)
print(f"{len(manifests)} 个源, {sum(len(v) for v in manifests.values())} 篇文章")

# 强制重新抓取
manifests = run_scout(force=True)
```

## 设计思路

### 四种抓取策略

24 个数据源的 HTML 获取方式各不相同，通过 `fetch_strategy` 字段区分：

| 策略 | 源数量 | 获取方式 | 适用场景 |
|------|--------|----------|----------|
| `rss` | 18 个 | `feedparser` 解析 RSS/Atom feed | 博客、新闻站点（arXiv、OpenAI、HN 等） |
| `api` | 2 个 | `curl` GET JSON API 端点 | Hacker News Algolia、GitHub Trending |
| `scrape` | 2 个 | `curl` GET HTML + 专用解析器 | Anthropic sitemap、TLDR AI |
| `browser` | 2 个 | Playwright 渲染 + 专用解析器 | 知乎（需要 JS 渲染） |

每种策略在 `strategies.py` 中有对应的 `_scout_xxx()` 函数，由 `orchestrator.py` 的 dispatch 分支分发。

### 解析器注册表模式

`scrape` 和 `browser` 策略不直接包含解析逻辑，而是通过注册表查找：

```python
# pipeline/ingestion/parsers/__init__.py

SCRAPE_PARSERS = {
    "tldrai": parse_tldrai,
    "anthropic-blog": parse_anthropic,
}

BROWSER_PARSERS = {
    "zhihu": parse_zhihu_browser,
}
```

添加新解析器只需在注册表中增加一行，`strategies.py` 和 `orchestrator.py` 无需修改。

### fail-per-source 策略

每个源的抓取是独立的——某个源失败（网络超时、页面改版、解析错误）通过 `try/except` 捕获后报告并跳过，**不影响其他源**。这与 ingest 的 fail-per-article 策略一致。

### BrowserSession 复用

存在多个 browser 策略源时（目前只有知乎），`orchestrator` 在开始抓取前预先创建一个 `BrowserSession`，在所有 browser 源之间复用，而不是每处理一个源就启动和关闭一次 Chromium。

### 过滤管道

每篇文章经过三层过滤（`filters.py`）：

1. **关键词过滤** — 标题或摘要包含任一关键词才保留
2. **时效性过滤** — 只保留最近 N 小时内的文章（默认 48h）
3. **数量裁剪** — 保留前 N 条（由 `limit` 控制）

> 短关键词（≤3 字符，如 "AI"、"RAG"）使用 ASCII 字母边界匹配，避免子串误命中（如 "RAG" 命中 "storage"）。

## 模块结构

```
pipeline/ingestion/scout/
├── __init__.py          # 包入口，导出 run_scout
├── __main__.py          # uv run python -m pipeline.ingestion.scout 入口
├── cli.py               # CLI 契约：参数声明 + register_subparser + execute
├── orchestrator.py      # 主编排：遍历源 → 分发策略 → 过滤 → 生成ID → 写JSON
├── strategies.py        # 四种抓取策略实现 (rss/api/scrape/browser)
└── manifest_writer.py   # 生成人类可读的 Markdown 汇总清单
```

**依赖的核心模块**：

```
pipeline/core/
├── web_utils.py         # fetch_rss_items (feedparser), fetch_url (curl)
├── file_utils.py        # write_json, read_json, resolve_data_dir, atomic_write
├── id_utils.py          # SHA-256 文章 ID 生成
├── config_loader.py     # get_sources(enabled_only=True)
└── browser_utils.py     # BrowserSession（Playwright 生命周期管理）

pipeline/ingestion/
├── filters.py           # apply_filters (关键词/时效/数量)
└── parsers/             # 专用解析器注册表 + 实现
    ├── __init__.py      # SCRAPE_PARSERS / BROWSER_PARSERS 注册表
    ├── tldrai.py        # TLDR AI 解析器
    ├── anthropic.py     # Anthropic sitemap 解析器
    └── zhihu.py         # 知乎 browser 解析器
```

## 核心流程

```
run_scout(force=False)
│
├─ 1. get_sources(enabled_only=True)
│     从 config.yaml 读取所有 enabled: true 的数据源
│     按 config 中定义的顺序排列
│
├─ 2. 检测 browser 策略源 → 预创建 BrowserSession
│     仅在存在 browser 策略源时启动 Chromium
│     所有 browser 源复用同一个 session
│
├─ 3. 遍历每个源：
│     │
│     ├─ 3a. 跳过检查
│     │     manifest 文件已存在 且 非 --force → 跳过
│     │
│     ├─ 3b. 策略分发
│     │     rss     → _scout_rss(source)         # feedparser 解析
│     │     api     → _scout_api(source)          # curl JSON API
│     │     scrape  → _scout_scrape(source)       # curl HTML + 解析器
│     │     browser → _scout_browser(source, bs)  # Playwright + 解析器
│     │
│     ├─ 3c. apply_filters(articles, source)
│     │     关键词匹配 → 时效性检查 → 数量裁剪
│     │
│     ├─ 3d. generate_id(url) 为每篇文章生成 SHA-256 ID
│     │     确定性 16 位 hex，贯穿整个流水线
│     │
│     └─ 3e. write_json(manifest_path, manifest_data)
│           输出到 data/00_manifest/{source}_{date}.json
│
├─ 4. 生成 Markdown 汇总清单
│     _generate_markdown_manifest()
│     新抓取的文章 + 从已有 JSON 回读被跳过源的数据
│     按 Tier (A→B→C) 再按 name 排序输出
│     原子写入 data/00_manifest/{date}-manifest-第{W}周.md
│
└─ 5. 返回 {source_name: [articles]} 字典
```

## 数据流

### 输入

| 数据 | 路径 | 说明 |
|------|------|------|
| 源配置 | `pipeline/config.yaml` | 24 个源，含 url、fetch_strategy、filter、tier 等 |
| RSS/API/HTML | 外部网络 | 各数据源的实时内容 |

### 输出

| 数据 | 路径 | 格式 | 说明 |
|------|------|------|------|
| URL 清单 | `data/00_manifest/{source}_{date}.json` | JSON | 每源一个文件，供 ingest 阶段消费 |
| 汇总清单 | `data/00_manifest/{date}-manifest-第{W}周.md` | Markdown | 人类可读的全天汇总 |

### 清单 JSON 结构

```json
{
  "source": "arxiv-cs-ai",
  "source_type": "academic_paper",
  "tier": "A",
  "generated_at": "2026-05-21T08:30:00.000000+00:00",
  "date": "2026-05-21",
  "articles": [
    {
      "url": "https://arxiv.org/abs/2605.19042",
      "title": "Interference-Aware Multi-Task Unlearning",
      "published": "2026-05-20",
      "summary": "Machine unlearning aims to remove...",
      "author": "Ying-Hua Huang et al.",
      "id": "098b39fb4bd5fbf2"
    }
  ]
}
```

## 配置说明

### config.yaml 相关字段

每个数据源中影响 scout 行为的字段：

```yaml
sources:
  arxiv-cs-ai:
    enabled: true               # false 时跳过
    fetch_strategy: rss         # rss | api | scrape | browser
    url: "https://..."          # RSS feed / API 端点 / 网页 URL
    tier: A                     # A | B | C（影响汇总清单排序）
    type: academic_paper        # 源类型标签
    language: en                # en | zh
    filter:
      keywords: ["LLM", "Agent", ...]  # 关键词列表
      max_age_hours: 48                 # 时效性窗口
      score_threshold: 100              # 仅 HN Algolia API 使用
    limit: 15                    # 保留前 N 篇（0 = 不限制）
    wait_for: ".css-selector"    # 仅 browser 模式，等待元素出现
```

## 错误处理

| 场景 | 行为 |
|------|------|
| 源缺少 URL 配置 | 打印警告，返回空列表，**不影响其他源** |
| RSS feed 解析失败 | `feedparser.parse()` 返回空列表 |
| API JSON 解码失败 | 返回空列表 |
| scrape/browser 无对应解析器 | 打印提示，返回空列表 |
| 网络超时 | `fetch_url()` 返回 `None`，记录为空列表 |
| 单个源异常 | `try/except` 捕获，打印错误，**继续处理下一个源** |
| 所有源都无文章 | 正常退出，不生成汇总清单 |

### 幂等性保证

- `--force` 不传时，已存在的当日清单会被跳过（`manifest_path.exists()` 检查）
- 文章 ID 由 URL 确定性生成（SHA-256），同一 URL 多次 scout 产生的 ID 相同
- 因此可以安全地重复运行，不会产生重复数据

## 与其他模块的关系

### 上游（输入）

| 模块 | 说明 |
|------|------|
| `pipeline/config.yaml` | 数据源定义（URL、策略、过滤规则） |
| `pipeline/ingestion/parsers/` | scrape/browser 专用解析器 |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/ingestion/ingest` | Stage 1b，读取 JSON 清单，逐篇抓取正文 |

## 扩展指南

### 新增数据源

1. 在 `config.yaml` 的 `sources` 列表中添加新条目，设置 `fetch_strategy`、`url`、`filter` 等
2. 如果策略是 `rss` 或 `api`（标准 JSON API），通常无需写代码
3. 如果策略是 `scrape`：在 `parsers/` 下新增解析器，并在 `SCRAPE_PARSERS` 注册
4. 如果策略是 `browser`：在 `parsers/` 下新增解析器，并在 `BROWSER_PARSERS` 注册

### 新增抓取策略

1. 在 `strategies.py` 中添加新的 `_scout_xxx(source, [browser_session])` 函数
2. 在 `orchestrator.py` 的 dispatch 分支中增加对应的 `elif strategy == "xxx":` 分支
3. 在 `config.yaml` 中将源的 `fetch_strategy` 设置为新值

### 解析器接口约定

Scrape 解析器签名：`def parse_xxx(source: dict) -> List[dict]`

Browser 解析器签名：`def parse_xxx(source: dict, browser_session: BrowserSession) -> List[dict]`

返回的文章 dict 需包含：`url`（必需）、`title`（必需）、`published`、`summary`、`author`。
