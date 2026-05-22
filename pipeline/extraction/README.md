# Stage 2 Extraction — 元信息与事实提取

## 模块概览

Extraction 是 Daily AI Insight Engine 流水线的 **Stage 2**，负责对 Stage 1 产出的文章正文进行两轮 LLM 驱动的结构化提取：先判断信源类型（BaseInfo），再从长文本中提炼高密度客观事实（FactExtraction）。

**一句话职责**：读 Markdown 文件 → 调用 Claude Agent 提取结构化字段 → 合并到 frontmatter → 原位写回。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)      →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
  URL清单        .md文件       BaseInfo + 事实提取   深度分析         聚合JSON          日报生成
```

Stage 2 内部分为两个子阶段，**阶段间串行、阶段内并行**：

```
Stage 2a (BaseInfo)          Stage 2b (FactExtraction)
   source_type 分类            tldr / objectiveSummary
                               eventType / epistemicStatus
                               entities / keyLogicFlow
```

## 快速开始

### 基本用法

```bash
# 处理所有 data/01_raw/ 下的文件（两个子阶段都执行）
uv run python pipeline/run.py extract

# 只运行 BaseInfo
uv run python pipeline/run.py extract --stage base_info

# 只运行 FactExtraction（需要 data/02_extracted/ 已有 BaseInfo 输出）
uv run python pipeline/run.py extract --stage fact_extraction

# 强制重新提取（忽略 skip-existing）
uv run python pipeline/run.py extract --force

# 干跑（列出文件，不调用 LLM）
uv run python pipeline/run.py extract --dry-run
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--input` / `-i` | `data/01_raw/` | 输入 .md 文件或目录路径 |
| `--concurrency` / `-c` | `config.yaml` 中 `llm.rate_limit.concurrent_requests`（默认 5） | 并发 Agent 调用数 |
| `--stage` | `all` | 只运行指定子阶段：`base_info` / `fact_extraction` / `all` |
| `--force` | `false` | 强制重新提取（忽略 `--skip-existing`） |
| `--skip-existing` | `true` | 跳过已提取的文件 |
| `--dry-run` | `false` | 只列出将处理的文件，不实际调用 LLM |
| `--model` / `-m` | `config.yaml` 中 `llm.models.extract.name` | LLM 模型名称 |
| `--verbose` / `-v` | `false` | 详细日志输出 |

### 作为 Python 模块调用

```python
from pipeline.extraction import run_extraction
import asyncio

results = asyncio.run(run_extraction(
    concurrency=5,
    stages="all",
    force=False,
))
# → {"base_info": [StageResult, ...], "fact_extraction": [StageResult, ...]}
```

## 设计思路

### 两阶段分离：阶段间串行、阶段内并行

Stage 2a (BaseInfo) 和 Stage 2b (FactExtraction) **严格串行**执行——Stage 2a 全部完成后才开始 Stage 2b。原因：

- **数据依赖**：Stage 2b 的 prompt 需要从 frontmatter 读取 `title` 和 `source`，而这些字段在 Stage 2a 处理后的输出文件中才能保证存在
- **避免写冲突**：两个阶段都向同一文件的 frontmatter 写入，串行执行天然避免了并发写入同一文件的竞态条件

每个阶段内部使用 `asyncio.Semaphore` 控制并发，所有文件的 Agent 调用并行发起，充分利用 API 配额。

### source_type 目录名推断（零 Agent 调用）

BaseInfo 的核心任务是判断 `source_type`。对于绝大多数数据源，这个信息在 `config.yaml` 中已经明确配置（`type` 字段），而文件目录名就是 source 的 `name`（如 `arxiv-cs-ai`、`techcrunch`），与配置一一对应。

系统在模块加载时构建 `目录名 → source.type` 映射表，处理文件时优先从路径推断，只有推断失败（如文件目录名在配置中找不到对应源）时才调用 Agent。这消除了绝大多数情况下的 Agent 调用开销。

```python
# 推断逻辑：data/01_raw/arxiv-cs-ai/01.md → arxiv-cs-ai → academic_paper
_SOURCE_TYPE_FROM_DIR = {"arxiv-cs-ai": "academic_paper", "techcrunch": "news_media", ...}
```

### 存量字段保护（merge 策略）

提取结果合并到 frontmatter 时，遵循 **"已有字段绝不覆盖"** 原则：

- 读取现有 frontmatter → 对比 schema 找出缺失字段 → 只提取缺失字段 → 合并写入
- 这意味着可以安全地重复运行，不会覆盖人工修正过的字段
- `skip_existing` 机制进一步减少重复 LLM 调用：输出文件已存在且所有字段完整 → 跳过

### 5 级容错校验链（FactExtraction）

LLM 输出天然不可靠。FactExtraction 的校验函数实现了多层容错：

1. **Pydantic 严格校验** — `FactExtraction.model_validate(data)`，通过即返回
2. **枚举值模糊匹配** — Agent 可能返回 `"infrastructure"` 而非 `"infrastructure_update"`，通过模糊映射表修正（如 `infra → infrastructure_update`、`funding → capital_movement`）
3. **枚举交叉互换修复** — Agent 有时会把 `eventType` 和 `epistemicStatus` 的值填反（如 eventType=`"theoretical_claim"` 同时 epistemicStatus=`"infrastructure_update"`），系统检测到后自动 swap
4. **单向枚举修复** — 仅一个字段填错到另一个枚举域时（如 eventType 被填成 epistemicStatus 值，但 epistemicStatus 本身合法），单向移动并回退默认值
5. **超长文本截断** — `tldr`（max 80 字符）和 `objectiveSummary`（max 150 字符）超长时，使用三级断句策略截断：强断句（`。！？.!?\n`）→ 弱断句（`；，,; `）→ 硬截断

### fail-per-article 策略

每个文件的提取是独立的——某个文件 Agent 调用失败、JSON 解析错误、校验失败，通过 `try/except` 捕获后报告并跳过，**不影响其他文件**。`asyncio.gather(return_exceptions=True)` 保证单个任务异常不中断整体调度。

### 正文截断控制 Token 消耗

两个子阶段对正文长度有不同的截断策略：

| 子阶段 | 截断长度 | 理由 |
|--------|----------|------|
| BaseInfo | 8000 字符 | 信源类型判断只需要看文章的整体风格和结构 |
| FactExtraction | 12000 字符 | 事实提取需要更多上下文来准确识别实体和逻辑脉络 |

## 模块结构

```
pipeline/extraction/
├── __init__.py               # 包入口，导出 run_extraction / extract_base_info / extract_fact_extraction
├── cli.py                    # CLI 契约：参数声明 + register_subparser + execute
├── run_extraction.py         # 主编排：文件发现 → 阶段调度 → 结果汇总
├── base_info_agent.py        # Stage 2a：BaseInfo 提取（单文件 + 批量并行）
├── fact_extraction_agent.py  # Stage 2b：FactExtraction 提取（单文件 + 批量并行）
└── prompts.py                # Agent 提示词模板（system + user，中英文混合）
```

**依赖的核心模块**：

```
pipeline/core/
├── agent.py                 # call_agent_with_retry / parse_json_response / StageResult
├── frontmatter_utils.py     # read_frontmatter / write_frontmatter
├── file_utils.py            # resolve_data_dir / get_project_root / ensure_dir
├── config_loader.py         # get_llm_config / get_stage_config / get_sources
├── id_utils.py              # generate_id（SHA-256）
├── text_utils.py            # truncate_at_natural_break（自然边界截断）
└── enum_utils.py            # fuzzy_match_enum（枚举值模糊匹配）

pipeline/schemas/
├── base_info.py             # SourceType 枚举 + BaseInfo Pydantic 模型
└── fact_extraction.py       # EventType / EpistemicStatus / Entities / FactExtraction 模型
```

## 核心流程

```
run_extraction(concurrency, stages, skip_existing, force, model)
│
├─ 1. 加载配置
│     llm_config ← get_llm_config("extract")
│     stage_config ← get_stage_config("extract")
│     模型 / 并发数 / 路径 均支持 CLI 覆盖
│
├─ 2. 文件发现
│     discover_files(input_path)
│     ├─ 单文件模式：验证 .md 后缀，直接返回
│     └─ 目录模式：rglob("*.md") 递归查找
│     判定 input_base_dir（用于计算输出路径的相对结构）
│
├─ 3. Dry run 检查 → 只打印文件列表，不执行
│
├─ 4. 创建 asyncio.Semaphore(concurrency)
│
├─ 5. Stage 2a: BaseInfo（如果 stages ∈ {all, base_info}）
│     │
│     │  run_base_info_stage(file_paths, ...)
│     │  为每个文件创建协程，在 semaphore 保护下并发执行：
│     │
│     │  extract_base_info(input_path, output_path, ...)
│     │  │
│     │  ├─ 5a. read_frontmatter(input_path) → (existing_fm, body)
│     │  │
│     │  ├─ 5b. 获取/生成 article_id
│     │  │     优先从 frontmatter 读取（00_manifest/ingest 阶段已写入）
│     │  │     旧文件缺少 id → generate_id(source_url) 回退生成
│     │  │
│     │  ├─ 5c. skip_existing 检查
│     │  │     输出文件已存在 + id 存在 + 所有 BaseInfo 字段完整 → 跳过
│     │  │
│     │  ├─ 5d. 空 body 检查 → 读 extraction_status 输出原因，跳过 Agent 调用
│     │  │
│     │  ├─ 5e. determine_missing_fields(existing_fm)
│     │  │     对比 frontmatter 与 BaseInfo schema，找出缺失字段
│     │  │
│     │  ├─ 5f. source_type 目录名推断（零 Agent 调用）
│     │  │     _infer_source_type_from_dir(input_path)
│     │  │     命中 → 直接写入，从 missing_fields 中移除
│     │  │
│     │  ├─ 5g. 仍存在缺失字段 → 调用 Agent 提取
│     │  │     build_base_info_user_prompt(missing_fields, body[:8000])
│     │  │     → call_agent_with_retry(max_turns=3)
│     │  │     → parse_json_response(text)
│     │  │
│     │  ├─ 5h. merge: 只写入 missing_fields 中的字段，已有字段不覆盖
│     │  │
│     │  └─ 5i. write_frontmatter(output_path, merged_fm, body)
│     │         输出到 data/02_extracted/{source}/XX.md
│     │
│     └─ print_stage_summary("2a (BaseInfo)", results_2a)
│
├─ 6. Stage 2b: FactExtraction（如果 stages ∈ {all, fact_extraction}）
│     │
│     │  输入 = Stage 2a 成功的输出文件（或已有的 data/02_extracted/ 文件）
│     │
│     │  run_fact_extraction_stage(file_paths, ...)
│     │  为每个文件创建协程，在 semaphore 保护下并发执行：
│     │
│     │  extract_fact_extraction(input_path, output_path, ...)
│     │  │
│     │  ├─ 6a. read_frontmatter(input_path) → (existing_fm, body)
│     │  │
│     │  ├─ 6b. skip_existing 检查
│     │  │     id 存在 + 所有 FactExtraction 字段完整 → 跳过
│     │  │
│     │  ├─ 6c. 空 body 检查 → 读 extraction_status 输出原因，跳过 Agent 调用
│     │  │
│     │  ├─ 6d. extraction_status == "failed" → 跳过（正文仅为错误信息）
│     │  │
│     │  ├─ 6e. 读取 title / source（来自 Stage 2a 已写入的 frontmatter）
│     │  │
│     │  ├─ 6f. 调用 Agent 提取
│     │  │     build_fact_extraction_user_prompt(title, source, body[:12000])
│     │  │     → call_agent_with_retry(max_turns=3)
│     │  │     → parse_json_response(text)
│     │  │
│     │  ├─ 6g. _validate_fact_extraction(data) — 5 级容错校验
│     │  │     ├─ Pydantic 严格校验
│     │  │     ├─ 枚举值模糊匹配（infra → infrastructure_update）
│     │  │     ├─ 枚举交叉互换修复（eventType ↔ epistemicStatus swap）
│     │  │     ├─ 单向枚举修复 + 默认值回退
│     │  │     └─ 超长文本自然边界截断
│     │  │
│     │  ├─ 6h. model_dump(mode="json") + merge 到 existing_fm + 写入 pipeline_stage
│     │  │
│     │  └─ 6i. write_frontmatter(output_path, merged_fm, body)
│     │         Stage 2b 的输出与输入路径相同（原位更新）
│     │
│     └─ print_stage_summary("2b (FactExtraction)", results_2b)
│
└─ 7. 返回 {"base_info": [...], "fact_extraction": [...]}
```

## 数据流

### 输入

| 数据 | 路径 | 说明 |
|------|------|------|
| 原始文章 | `data/01_raw/{source}/*.md` | Stage 1b 产出，含 title / source / published 等 frontmatter + Markdown 正文 |
| 源配置 | `pipeline/config.yaml` | 用于构建 `目录名 → source_type` 映射表 |

### 输出

| 数据 | 路径 | 格式 | 说明 |
|------|------|------|------|
| 提取后文章 | `data/02_extracted/{source}/*.md` | Markdown + 丰富后的 YAML frontmatter | 包含 BaseInfo + FactExtraction 全部字段，供 Stage 3 analyze 消费 |

### Frontmatter 字段演进

Stage 2 处理前后的 frontmatter 变化：

**输入**（Stage 1b 产出）：

```yaml
id: "098b39fb4bd5fbf2"
title: "Interference-Aware Multi-Task Unlearning"
source: "https://arxiv.org/abs/2605.19042"
published: "2026-05-20"
created: "2026-05-21T08:30:00Z"
extraction_status: "success"       # Stage 1 正文抓取质量（success/partial/failed）
pipeline_stage: "ingested"         # 标记已完成 Stage 1
---
正文内容...
```

**Stage 2a 后**（新增 source_type + 更新 pipeline_stage）：

```yaml
# ... Stage 1 字段保持不变 ...
sourceType: "academic_paper"       # ← Stage 2a 新增（或从目录名推断）
pipeline_stage: "base_info_extracted"  # ← Stage 2a 更新
---
正文内容...
```

**Stage 2b 后**（新增 6 个 FactExtraction 字段 + 更新 pipeline_stage）：

```yaml
# ... Stage 1 + Stage 2a 字段保持不变 ...
tldr: "提出干扰感知的多任务遗忘方法，在移除特定知识的同时保持模型整体性能"
objectiveSummary: "研究者提出一种新的机器遗忘学习方法..."
eventType: "framework_tools"
epistemicStatus: "verified_fact"
entities:
  companies: []
  technologies: ["Machine Unlearning", "Multi-Task Learning"]
  keyPeople: ["Ying-Hua Huang"]
keyLogicFlow:
  - "传统遗忘学习方法在单任务上有效，但在多任务场景下会产生任务间干扰"
  - "提出 Interference-Aware 方法识别任务间梯度冲突..."
pipeline_stage: "fact_extracted"     # ← Stage 2b 更新
---
正文内容...
```

## 配置说明

### config.yaml 相关字段

```yaml
# LLM 配置（影响 Agent 调用）
llm:
  models:
    extract:
      name: claude-sonnet-4-6    # 默认模型（可被 CLI --model 覆盖）
  rate_limit:
    concurrent_requests: 5       # 默认并发数（可被 CLI --concurrency 覆盖）

# Stage 配置
stages:
  extract:
    input_dir: data/01_raw/      # 默认输入目录

# 数据源定义（用于构建 source_type 映射表）
sources:
  arxiv-cs-ai:
    type: academic_paper          # 对应 BaseInfo.source_type 枚举值
```

## 错误处理

| 场景 | 行为 |
|------|------|
| 文件读取失败 | 返回 `StageResult(success=False)`，**不影响其他文件** |
| 输出文件损坏 | `try/except` 捕获，回退到重新处理 |
| 正文为空 | 跳过 Agent 调用，根据 `extraction_status` 输出具体原因（抓取失败/仅摘要/未知） |
| Stage 1 抓取失败（`extraction_status=failed`） | Stage 2a 仍可推断 source_type；Stage 2b **直接跳过**（正文仅为错误信息，不值得调用 LLM） |
| Stage 1 仅获摘要（`extraction_status=partial`） | Stage 2a/2b 仍提取，日志标注"正文不完整" |
| Stage 2b 输入文件全部缺失 | 打印明确错误："需要 Stage 2a 的输出文件，请先运行 extract --stage base_info"，**直接退出** |
| Stage 2b 输入文件部分缺失 | 打印警告（缺失数/总数），过滤出存在的文件继续处理 |
| Agent 调用失败（3 次重试耗尽） | 返回 `StageResult(success=False)`，打印错误 |
| JSON 解析失败 | 返回 `StageResult(success=False)`（5 级 JSON 恢复 parser 也无法挽救时） |
| Pydantic 校验失败 | 依次尝试模糊匹配 → 交叉互换 → 单向修复 → 默认回退，最终仍失败才报错 |
| 单个文件未处理异常 | `asyncio.gather(return_exceptions=True)` 捕获，转为 `StageResult(success=False)` |
| 单个源目录不匹配 config | `_infer_source_type_from_dir` 返回 `None`，回退到 Agent 判断 |

### Agent 调用的重试策略

- 底层使用 `call_agent_with_retry`（`pipeline/core/agent.py`）
- 默认 `max_turns=3`：失败时指数退避重试（2s → 4s → 8s，含 jitter）
- 重试仅针对网络错误和临时性失败，JSON 解析错误不重试

### 幂等性保证

- `--skip-existing`（默认启用）：输出文件已存在且字段完整 → 跳过
- 存量字段 merge 策略：已有字段绝不覆盖
- `--force` 可强制重新提取所有字段
- 因此可以安全地重复运行，不会产生重复或损坏的数据

## 与其他模块的关系

### 上游（输入）

| 模块 | 说明 |
|------|------|
| `pipeline/ingestion/ingest` | Stage 1b，产出 `data/01_raw/{source}/*.md` 原始文章文件 |
| `pipeline/config.yaml` | 数据源配置（type 字段用于 source_type 推断） |
| `pipeline/schemas/base_info.py` | BaseInfo / SourceType Pydantic 模型定义 |
| `pipeline/schemas/fact_extraction.py` | FactExtraction / EventType / EpistemicStatus / Entities 模型定义 |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/analysis/` | Stage 3，读取 `data/02_extracted/` 中的文件，进行三维度深度分析（tech-architect / capital-analyst / risk-assessor） |

### 水平依赖（同阶段）

| 模块 | 说明 |
|------|------|
| `pipeline/core/agent.py` | `call_agent_with_retry` / `parse_json_response` / `StageResult` — Agent 调用的统一封装 |
| `pipeline/core/frontmatter_utils.py` | YAML frontmatter 的读写操作 |
| `pipeline/core/enum_utils.py` | `fuzzy_match_enum` — 枚举值模糊匹配工具 |
| `pipeline/core/text_utils.py` | `truncate_at_natural_break` — 自然边界截断 |
| `pipeline/core/config_loader.py` | 配置加载（源列表、LLM 参数、路径） |

## 扩展指南

### 新增 BaseInfo 字段

1. 在 `pipeline/schemas/base_info.py` 的 `BaseInfo` 模型中添加新字段（含 `description=`）
2. 在 `prompts.py` 的 `get_base_info_system_prompt()` 中添加新字段的分类标准和示例
3. `build_base_info_user_prompt()` 动态使用 `missing_fields` 构造 prompt，通常无需修改

### 新增 FactExtraction 字段

1. 在 `pipeline/schemas/fact_extraction.py` 的 `FactExtraction` 模型中添加新字段
2. 在 `prompts.py` 的 `get_fact_extraction_system_prompt()` 中添加新字段的提取说明和输出格式
3. 如果新字段是枚举类型，在 `fact_extraction_agent.py` 中添加对应的模糊匹配映射表
4. 将新字段名加入 `_FACT_EXTRACTION_FIELDS` 集合（用于 skip_existing 检查）

### 新增校验修复规则

1. 在 `fact_extraction_agent.py` 的 `_validate_fact_extraction()` 函数中添加新的修复逻辑
2. 在相应的模糊映射表（`_EVENT_TYPE_FUZZY` / `_EPISTEMIC_FUZZY`）中添加新的变体映射
3. 新增修复逻辑应遵循现有 5 级容错链的优先级顺序
