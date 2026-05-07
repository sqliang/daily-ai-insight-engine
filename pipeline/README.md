# Pipeline

四阶段 AI 资讯处理流水线：获取 → 提取 → 分析 → 汇总。

## 目录结构

```
pipeline/
├── config.yaml              # 核心配置 (数据源、LLM、各阶段参数、配额)
├── config/
│   └── proxy.json           # 网络代理配置 (127.0.0.1:7890)
├── requirements.txt         # Python 依赖
├── core/                    # 可复用工具库
│   ├── config_loader.py     #   YAML 配置加载与筛选
│   ├── proxy_utils.py       #   代理注入 (环境变量)
│   ├── web_utils.py         #   HTTP/RSS/正文抽取 (curl + feedparser + trafilatura)
│   ├── file_utils.py        #   原子写入、路径解析、JSON I/O
│   └── frontmatter_utils.py #   Markdown YAML frontmatter 读写
├── schemas/                 # Pydantic 数据模型 (所有阶段共用)
│   ├── base_info.py         #   SourceType 枚举 + BaseInfo 模型
│   ├── fact_extraction.py   #   FactExtraction + Entities + EventType
│   ├── deep_analysis.py     #   Qualitative/Value/Foresight 三维评估模型
│   └── daily_ai_insight.py  #   DailyAIInsight 顶层聚合模型
├── ingestion/               # Stage 1: 数据筛选与获取 ✅
│   ├── scout.py             #   Step 1 — 生成 URL 清单 → data/00_manifest/
│   └── ingest.py            #   Step 2 — 抓取正文 → data/01_raw/{source}/*.md
├── extraction/              # Stage 2: 事实抽取 (待实现)
├── deep-analysis/           # Stage 3: 深度分析 (待实现)
└── synthesis/               # Stage 4: 汇总报告 (待实现)
```

## 快速开始

### 1. 安装依赖

需要 Python >= 3.10。

```bash
cd pipeline
pip install -r requirements.txt
```

### 2. 配置代理 (可选)

如果你需要代理访问外网，编辑 `config/proxy.json`：

```json
{
  "proxy": {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
    "all": "socks5://127.0.0.1:7890"
  }
}
```

代理自动通过环境变量注入，所有网络请求 (curl、feedparser、trafilatura) 都会继承。

### 3. 配置数据源

编辑 `config.yaml`，根据需要启用/禁用数据源 (`enabled: true/false`)。

每个源的 `fetch_strategy` 决定抓取方式：
- `rss` — RSS/Atom feed 自动抓取 (如 arxiv)
- `api` — JSON API 抓取 (如 Hacker News)
- `scrape` — HTML 页面抓取 (暂未实现通用方案)

### 4. 运行

推荐使用 `run.py` 作为统一入口，它会在业务逻辑之前自动完成初始化：

```bash
# 在项目根目录下执行
python pipeline/run.py
```

`run.py` 启动时自动执行：

1. **加载 .env** — 将项目根目录的 `.env` 注入环境变量（API Key、模型配置等）
2. **加载代理** — 读取 `config/proxy.json` 并注入 `http_proxy`/`https_proxy`，后续所有网络请求自动走代理

也可以直接运行各个阶段脚本（初始化需自行处理）：

```bash
# Step 1: 生成 URL 清单 → data/00_manifest/
python -m pipeline.ingestion.scout

# 强制重新获取 (忽略已有清单)
python -m pipeline.ingestion.scout --force

# Step 2: 抓取正文 → data/01_raw/
python -m pipeline.ingestion.ingest

# 强制重新抓取 (忽略去重记录)
python -m pipeline.ingestion.ingest --force
```

## 数据流向

```
config.yaml
    │
    ▼
scout.py  ──RSS/API 抓取──▶  data/00_manifest/{source}_{date}.json
    │                            (轻量级 URL 清单，断点续传)
    ▼
ingest.py ──正文抽取──────▶  data/01_raw/{source}/01.md
    │                            (Markdown + YAML frontmatter)
    ▼
(Stage 2-4 待实现)
```

## 测试

```bash
# 单元测试
python -m pytest pipeline/tests/ -v

# 验证配置加载
python -c "
from pipeline.core.config_loader import load_config
cfg = load_config()
print(f'{len(cfg[\"sources\"])} sources loaded')
"

# 验证 RSS 抓取
python -c "
from pipeline.core.web_utils import fetch_rss_items
items = fetch_rss_items('https://rss.arxiv.org/rss/cs.AI')
print(f'{len(items)} items from arxiv RSS')
"

# 验证 Frontmatter 读写
python -c "
from pipeline.core.frontmatter_utils import build_ingestion_frontmatter, write_frontmatter, read_frontmatter
from pathlib import Path
import tempfile, shutil
d = Path(tempfile.mkdtemp())
fm = build_ingestion_frontmatter('Test', 'https://example.com', '2026-01-01', 'Alice')
write_frontmatter(d / 'test.md', fm, 'Body text')
meta, body = read_frontmatter(d / 'test.md')
assert meta['title'] == 'Test'
shutil.rmtree(d)
print('Frontmatter OK')
"
```
