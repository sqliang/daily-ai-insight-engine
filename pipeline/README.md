# Pipeline

四阶段 AI 资讯处理流水线：获取 → 提取 → 分析 → 汇总。

## 目录结构

```
pipeline/
├── run.py                    # 统一 CLI 入口（argparse 子命令）
├── config.yaml               # 核心配置（数据源、LLM、各阶段参数）
├── config/
│   └── proxy.json            # 网络代理配置（127.0.0.1:7890）
├── requirements.txt          # Python 依赖
│
├── core/                     # 可复用工具库
│   ├── agent.py              #   claude-agent-sdk 封装（调用、重试、JSON 解析）
│   ├── config_loader.py      #   YAML 配置加载与缓存
│   ├── proxy_utils.py        #   代理注入（环境变量）
│   ├── web_utils.py          #   HTTP/RSS/正文抽取（curl + feedparser + trafilatura）
│   ├── browser_utils.py      #   Playwright 生命周期管理
│   ├── file_utils.py         #   原子写入、路径解析、JSON I/O
│   ├── id_utils.py           #   SHA-256 文章 ID 生成
│   ├── text_utils.py         #   文本清洗与截断
│   └── concurrency/
│       └── state.py          #   线程安全去重状态（IngestState）
│
├── schemas/                  # Pydantic v2 数据模型（所有阶段共用）
│   ├── base_info.py          #   SourceType 枚举 + BaseInfo 模型
│   ├── fact_extraction.py    #   FactExtraction + Entities + EventType
│   ├── deep_analysis.py      #   Qualitative / Value / Foresight 三维度评估模型
│   └── daily_ai_insight.py   #   DailyAIInsight 顶层聚合模型
│
├── utils/                    # 通用工具
│   ├── frontmatter.py        #   YAML frontmatter 读写
│   ├── enum_utils.py         #   枚举值模糊匹配
│   ├── file_utils.py         #   文件系统辅助
│   ├── id_utils.py           #   SHA-256 ID 生成
│   ├── text_utils.py         #   文本截断
│   └── schema_utils.py       #   扁平 frontmatter → 嵌套模型转换
│
├── ingestion/                # Stage 1: 数据获取 ✅
│   ├── filters.py            #   关键词/时效/数量过滤器
│   ├── scout/                #   Stage 1a — URL 清单生成 → data/00_manifest/
│   │   ├── README.md
│   │   ├── cli.py
│   │   ├── orchestrator.py
│   │   ├── strategies.py
│   │   └── manifest_writer.py
│   ├── ingest/               #   Stage 1b — 正文抓取与清洗 → data/01_raw/
│   │   ├── README.md
│   │   ├── cli.py
│   │   ├── orchestrator.py
│   │   ├── worker.py
│   │   └── truncation.py
│   ├── backfill_ids/         #   辅助工具：旧文件 ID 回填
│   └── parsers/              #   专用解析器（zhihu、anthropic、tldrai 等）
│
├── extraction/               # Stage 2: 事实提取 ✅
│   ├── README.md
│   ├── cli.py
│   ├── orchestrator.py
│   ├── base_info/            #   Stage 2a — 元信息补全（source_type 推断 + Agent 兜底）
│   │   ├── extractor.py
│   │   ├── runner.py
│   │   ├── source_type.py
│   │   └── prompts.py
│   └── fact_extraction/      #   Stage 2b — 事实提取（tldr、entities、keyLogicFlow）
│       ├── extractor.py
│       ├── runner.py
│       ├── validator.py
│       └── prompts.py
│
├── analysis/                 # Stage 3: 三维度深度分析 ✅
│   ├── README.md
│   ├── cli.py
│   ├── run_analysis.py
│   ├── deep_analysis_agent.py
│   ├── validators.py
│   ├── fuzzy_maps.py
│   └── prompts/
│
├── aggregation/              # Stage 4a: Frontmatter 聚合 ✅
│   ├── README.md
│   ├── __init__.py
│   └── aggregate_frontmatter.py  # 多阶段扫描 + 热冷分流 → data/04_structured/
│
└── synthesis/                # Stage 4b: 日报合成 ✅
    ├── README.md
    ├── cli.py
    ├── synthesize_report.py       # Editor-in-Chief 日报生成 → data/05_reports/
    ├── report_generator.py        # JSON → Markdown 报告文件生成
    └── prompts/
```

## 快速开始

### 1. 安装依赖

```bash
uv pip install -r pipeline/requirements.txt
```

### 2. 配置代理（可选）

如需代理访问外网，编辑 `pipeline/config/proxy.json`：

```json
{
  "proxy": {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
    "all": "socks5://127.0.0.1:7890"
  }
}
```

代理通过环境变量注入，所有网络请求（curl、feedparser、trafilatura）都会继承。

### 3. 配置数据源

编辑 `pipeline/config.yaml`，根据需要启用/禁用数据源（`enabled: true/false`）。

每个源的 `fetch_strategy` 决定抓取方式：

| 策略 | 说明 |
|------|------|
| `rss` | RSS/Atom feed 自动抓取（如 arXiv、OpenAI Blog） |
| `api` | JSON API 抓取（如 Hacker News Algolia） |
| `scrape` | HTML 页面抓取 + 专用解析器 |
| `browser` | Playwright 渲染 JS 页面 + 专用解析器（如 知乎） |

### 4. 运行

```bash
# 所有阶段通过统一入口运行
uv run python pipeline/run.py scout          # Stage 1a: 生成 URL 清单
uv run python pipeline/run.py ingest         # Stage 1b: 正文抓取
uv run python pipeline/run.py extract        # Stage 2: 事实提取
uv run python pipeline/run.py analyze        # Stage 3: 三维度深度分析
uv run python pipeline/run.py aggregate      # Stage 4a: Frontmatter 聚合（extract/analyze 后自动执行，通常无需手动运行）
uv run python pipeline/run.py synthesize     # Stage 4b: 日报合成
```

`run.py` 启动时自动执行：
1. **加载 .env** — 注入环境变量（API Key 等）
2. **加载代理** — 读取 `config/proxy.json` 注入代理配置

### 基本用法

```bash
# 查看所有可用子命令
uv run python pipeline/run.py --help

# 查看某个子命令的详细参数
uv run python pipeline/run.py scout --help
uv run python pipeline/run.py ingest --help
uv run python pipeline/run.py extract --help
uv run python pipeline/run.py analyze --help
uv run python pipeline/run.py synthesize --help
```

端到端完整运行（首次或全量重建）：

```bash
# 按顺序执行全部阶段（aggregate 在 extract 和 analyze 后自动执行）
uv run python pipeline/run.py scout && \
  uv run python pipeline/run.py ingest && \
  uv run python pipeline/run.py extract && \
  uv run python pipeline/run.py analyze && \
  uv run python pipeline/run.py synthesize
```

> **注意**：`extract` 和 `analyze` 完成后都会自动调用 `aggregate`（Stage 4a 聚合），无需单独运行。

日常增量运行（最常用）：

```bash
# 所有阶段默认启用 --skip-existing，已处理文章自动跳过
uv run python pipeline/run.py scout && \
  uv run python pipeline/run.py ingest && \
  uv run python pipeline/run.py extract && \
  uv run python pipeline/run.py analyze && \
  uv run python pipeline/run.py synthesize
```

单独运行某个阶段：

```bash
# 只运行日报合成（假设前面阶段都已完成）
uv run python pipeline/run.py synthesize

# 只运行深度分析的某个维度
uv run python pipeline/run.py analyze --stage qualitative

# 只处理某个数据源
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/

# 只处理单篇文章
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/098b39fb4bd5fbf2.md
```

强制重新处理：

```bash
# 每个阶段都支持 --force（忽略 skip-existing）
uv run python pipeline/run.py scout --force
uv run python pipeline/run.py ingest --force
uv run python pipeline/run.py extract --force
uv run python pipeline/run.py analyze --force
uv run python pipeline/run.py synthesize --force

# 组合使用：强制重新抓取 + 高并发
uv run python pipeline/run.py ingest --force --concurrency 10
```

预览与调试：

```bash
# 各阶段的 dry-run（列出文件但不实际处理）
uv run python pipeline/run.py extract --dry-run
uv run python pipeline/run.py analyze --dry-run
uv run python pipeline/run.py synthesize --dry-run    # 显示 token 预估值

# 详细日志输出
uv run python pipeline/run.py analyze --verbose
uv run python pipeline/run.py extract --verbose

# 指定 LLM 模型
uv run python pipeline/run.py analyze --model claude-sonnet-4-6
uv run python pipeline/run.py extract --model deepseek-v4-pro

# 调整并发数
uv run python pipeline/run.py analyze --concurrency 1     # 单文件逐篇调试
uv run python pipeline/run.py ingest --concurrency 10     # 高速抓取
```

单篇文章端到端调试：

```bash
# 从 URL 清单到日报合成，只处理一个源的一篇文章
uv run python pipeline/run.py scout
uv run python pipeline/run.py ingest -m arxiv-cs-ai_$(date +%Y-%m-%d).json

# 取第一篇文章作为测试目标
FIRST_FILE=$(ls data/01_raw/arxiv-cs-ai/*.md | head -1)
uv run python pipeline/run.py extract --input "$FIRST_FILE"

# 分析阶段的输入路径要切换到 02_extracted
uv run python pipeline/run.py analyze --input "${FIRST_FILE/01_raw/02_extracted}"
uv run python pipeline/run.py synthesize
```

## 数据流向

```
config.yaml
    │
    ▼
Stage 1a: scout  ──RSS/API/Scrape/Browser──▶  data/00_manifest/{source}_{date}.json
    │                                                  (URL 清单，断点续传)
    ▼
Stage 1b: ingest ──curl/Playwright + trafilatura──▶  data/01_raw/{source}/{id}.md
    │                                                  (Markdown + YAML frontmatter)
    ▼
Stage 2:  extract ──BaseInfo + FactExtraction──▶  data/02_extracted/{source}/{id}.md
    │                                                  (添加 sourceType / tldr / entities 等)
    ▼
Stage 3:  analyze ──3 维度 Agent 并行分析──▶  data/03_analyzed/{source}/{id}.md
    │                                                  (添加定性研判 / 价值评估 / 前瞻预测)
    ▼
Stage 4a: aggregate ──frontmatter 提取聚合──▶  data/04_structured/{source}.json
    │                                              + all_articles.json（供前端读取）
    ▼
Stage 4b: synthesize ──Editor-in-Chief 日报──▶  data/05_reports/daily-report.json
                                                   + daily-report.md（供前端 dashboard）
```

## 各阶段详细文档

| 阶段 | 文档 | 说明 |
|------|------|------|
| Stage 1a | [`ingestion/scout/README.md`](ingestion/scout/README.md) | URL 清单生成、四种抓取策略、过滤管道 |
| Stage 1b | [`ingestion/ingest/README.md`](ingestion/ingest/README.md) | 正文抓取、双通道并行调度、截断策略、去重机制 |
| Stage 2 | [`extraction/README.md`](extraction/README.md) | BaseInfo 推断 + FactExtraction、5 级容错校验、两阶段分离 |
| Stage 3 | [`analysis/README.md`](analysis/README.md) | 三维度深度分析、双层并行、模糊枚举修复、部分成功策略 |
| Stage 4a | [`aggregation/README.md`](aggregation/README.md) | Frontmatter 聚合 + 热冷分流 |
| Stage 4b | [`synthesis/README.md`](synthesis/README.md) | Editor-in-Chief 日报合成 |

## 设计原则

### 幂等性

所有阶段默认启用 `--skip-existing`，通过文章 ID（SHA-256 of URL）判定是否已处理。可以安全地重复运行，不会产生重复数据。`--force` 可强制重新处理。

### fail-per-article / fail-per-source

- **Stage 1a**：每个源的抓取独立，单个源失败不影响其他源
- **Stage 1b**：每篇文章的抓取独立，抓取失败仍生成 .md 文件（通过 `extraction_status` 标记质量）
- **Stage 2-4**：每个文件的处理独立，通过 `asyncio.gather(return_exceptions=True)` 容错

### 存量字段保护

下游阶段合并 frontmatter 时遵循"已有字段绝不覆盖"原则。Agent 只写入当前阶段负责的新字段，不会覆盖上游阶段的权威数据。

### 正文截断控制 Token 消耗

| 阶段 | 截断长度 | 理由 |
|------|----------|------|
| Stage 1b ingest | 按源配置（默认 3000） | 原始正文存储控制 |
| Stage 2a BaseInfo | 8000 字符 | 兜底场景只需判断文章类型 |
| Stage 2b FactExtraction | 12000 字符 | 事实提取需要更多上下文 |
| Stage 3 analysis | 6000 字符 | 深度分析关注结论而非细节 |

## 测试

```bash
# 单元测试
uv run python -m pytest pipeline/tests/ -v

# 验证配置加载
uv run python -c "
from pipeline.core.config_loader import load_config
cfg = load_config()
print(f'{len(cfg[\"sources\"])} sources loaded')
"

# 验证 RSS 抓取
uv run python -c "
from pipeline.core.web_utils import fetch_rss_items
items = fetch_rss_items('https://rss.arxiv.org/rss/cs.AI')
print(f'{len(items)} items from arxiv RSS')
"

# 验证 Frontmatter 读写
uv run python -c "
from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter
from pathlib import Path
import tempfile, shutil
d = Path(tempfile.mkdtemp())
fm = {'id': 'test123', 'title': 'Test', 'source': 'https://example.com'}
write_frontmatter(d / 'test.md', fm, 'Body text')
meta, body = read_frontmatter(d / 'test.md')
assert meta['title'] == 'Test'
shutil.rmtree(d)
print('Frontmatter OK')
"
```
