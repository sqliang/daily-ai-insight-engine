# Stage 2 Extraction — 元信息与事实提取

## 模块概览

Extraction 是 Daily AI Insight Engine 流水线的 **Stage 2**，负责对 Stage 1 产出的文章正文进行两轮结构化提取：先补全元信息（BaseInfo），再从长文本中提炼高密度客观事实（FactExtraction）。

**一句话职责**：读 Markdown 文件 → 工程推断为主、Agent 兜底为辅 → 合并到 frontmatter → 原位写回。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)      →  analyze (3)  →  aggregate (4a)  →  synthesize (4b)
  URL清单        .md文件       BaseInfo + 事实提取   深度分析         聚合JSON          日报生成
```

Stage 2 内部分为两个子阶段，**阶段间串行、阶段内并行**：

```
Stage 2a (BaseInfo)                              Stage 2b (FactExtraction)
  id / title / source / published / created        tldr / objectiveSummary
  source_type（目录名推断，零 Agent）                eventType / epistemicStatus
  Agent 仅作兜底（脏数据补缺）                       entities / keyLogicFlow
                                                    Agent 为主力（从正文提取事实）
```

**核心设计理念**：能用工程手段解决的问题不调用 Agent。BaseInfo 的绝大多数字段在 Stage 1 已写入，source_type 从目录名查 config.yaml 即可推断。只有遇到脏数据时 Agent 才作为最后手段介入，因此绝大部分文件的 Agent 调用在 Stage 2a 被跳过，token 消耗为零。

## 快速开始

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--input` / `-i` | `data/01_raw/` | 输入 .md 文件或目录路径 |
| `--concurrency` / `-c` | `config.yaml` 中 `llm.rate_limit.concurrent_requests`（5） | 并发 Agent 调用数 |
| `--stage` | `all` | 只运行指定子阶段：`base_info` / `fact_extraction` / `all` |
| `--force` | `false` | 强制重新提取（忽略 `--skip-existing`） |
| `--skip-existing` | `true` | 跳过已提取的文件 |
| `--dry-run` | `false` | 只列出将处理的文件，不实际调用 LLM |
| `--model` / `-m` | `config.yaml` 中 `llm.models.extract.name` | LLM 模型名称 |
| `--verbose` / `-v` | `false` | 详细日志输出 |

### 基本用法

```bash
# 处理所有文章（两个子阶段都执行，最常用）
uv run python pipeline/run.py extract

# 只运行 Stage 2a：BaseInfo 元信息补全（source_type 目录名推断，零 Agent）
uv run python pipeline/run.py extract --stage base_info

# 只运行 Stage 2b：FactExtraction（需要 data/02_extracted/ 已有 BaseInfo 输出）
uv run python pipeline/run.py extract --stage fact_extraction

# 处理单个文件
uv run python pipeline/run.py extract --input data/01_raw/arxiv-cs-ai/098b39fb4bd5fbf2.md

# 处理某个数据源的全部文章
uv run python pipeline/run.py extract --input data/01_raw/arxiv-cs-ai/

# 单文件 + 单阶段（最精细的调试粒度）
uv run python pipeline/run.py extract -i data/01_raw/openai-blog/01.md --stage base_info
```

> **注意**：FactExtraction 的输入路径应指向 `data/02_extracted/`（Stage 2a 的输出目录），因为 `source_type` 字段由 Stage 2a 写入。

强制重新提取与调参：

```bash
# 强制重新提取所有字段（忽略 skip-existing）
uv run python pipeline/run.py extract --force

# 强制重新提取指定子阶段（如提示词更新后）
uv run python pipeline/run.py extract --force --stage fact_extraction

# 强制重新提取单文件
uv run python pipeline/run.py extract --force --input data/01_raw/arxiv-cs-ai/01.md

# 指定模型 + 单线程（对比不同模型效果）
uv run python pipeline/run.py extract --model claude-sonnet-4-6 --concurrency 1 --verbose
```

预览与调试：

```bash
# 干跑（只列出文件，不调用 LLM）
uv run python pipeline/run.py extract --dry-run

# 按源查看待处理文件数
uv run python pipeline/run.py extract --dry-run --input data/01_raw/arxiv-cs-ai/

# 详细日志（查看每个文件的处理细节和 Agent 调用耗时）
uv run python pipeline/run.py extract --verbose

# 单文件 + 详细日志（定位特定文章的提取问题）
uv run python pipeline/run.py extract --verbose --input data/01_raw/arxiv-cs-ai/01.md
```

与上下游串联：

```bash
# ingest → extract → analyze 连续执行
uv run python pipeline/run.py ingest && \
  uv run python pipeline/run.py extract && \
  uv run python pipeline/run.py analyze

# 单文件端到端调试
uv run python pipeline/run.py extract -i data/01_raw/arxiv-cs-ai/01.md && \
  uv run python pipeline/run.py analyze -i data/02_extracted/arxiv-cs-ai/01.md
```

作为 Python 模块调用：

```python
from pipeline.extraction import run_extraction
import asyncio

# 正常提取（两个子阶段），返回 {stage_name: [StageResult, ...]}
results = asyncio.run(run_extraction(concurrency=5, stages="all", force=False))

# 只运行 FactExtraction
results = asyncio.run(run_extraction(stages="fact_extraction", force=True))

# 处理单个文件
results = asyncio.run(run_extraction(
    input_path=Path("data/01_raw/arxiv-cs-ai/01.md"), stages="all",
))
```

## 模块结构

```
pipeline/extraction/
├── __init__.py                   # 包入口，导出 run_extraction / extract_base_info / extract_fact_extraction
├── cli.py                        # CLI 契约：参数声明 + register_subparser + execute
├── orchestrator.py               # 主编排：文件发现 → 阶段调度 → 结果汇总 → 自动聚合
│
├── base_info/                    # Stage 2a: BaseInfo 提取
│   ├── __init__.py               # 导出 extract_base_info / run_base_info_stage
│   ├── extractor.py              # 单文件提取流水线：确定缺失字段 → 目录名推断 → Agent 兜底
│   ├── runner.py                 # 批量并行调度：Semaphore 控制并发，asyncio.gather 容错
│   ├── source_type.py            # source_type 推断：目录名 → config.yaml 映射，零 Agent
│   └── prompts.py                # Agent 提示词（system + user），仅兜底时使用
│
└── fact_extraction/              # Stage 2b: FactExtraction 提取
    ├── __init__.py               # 导出 extract_fact_extraction / run_fact_extraction_stage
    ├── extractor.py              # 单文件提取流水线：读取 → Agent 提取 → 校验修复 → 合并写入
    ├── runner.py                 # 批量并行调度：Semaphore 控制并发，asyncio.gather 容错
    ├── validator.py              # 5 级容错校验链 + 模糊枚举映射表
    └── prompts.py                # Agent 提示词（system + user），中文输出要求
```

**依赖的核心模块**：

```
pipeline/core/
├── agent.py                     # call_agent_with_retry / parse_json_response / StageResult
├── config_loader.py             # get_llm_config / get_stage_config / resolve_data_dir
├── frontmatter_utils.py         # build_ingestion_frontmatter（Stage 1 专用）

pipeline/utils/
├── frontmatter.py               # read_frontmatter / write_frontmatter（通用 YAML frontmatter 读写）
├── id_utils.py                  # generate_id（SHA-256）
├── file_utils.py                # get_project_root / ensure_dir / list_files
├── text_utils.py                # truncate_at_natural_break（自然边界截断）
└── enum_utils.py                # fuzzy_match_enum（枚举值模糊匹配）

pipeline/schemas/
├── base_info.py                 # SourceType 枚举 + BaseInfo Pydantic 模型
└── fact_extraction.py           # EventType / EpistemicStatus / Entities / FactExtraction 模型
```

## 核心流程

### 主编排（orchestrator.py）

```
run_extraction(concurrency, stages, skip_existing, force, model)
│
├─ 1. 加载配置
│     模型 / 并发数 / 路径 均支持 CLI 参数覆盖
│
├─ 2. 文件发现（discover_files）
│     ├─ 单文件：验证 .md 后缀，直接返回
│     └─ 目录：rglob("*.md") 递归查找
│     判定 input_base_dir（用于计算输出路径的相对结构）
│
├─ 3. Dry run → 只打印文件列表，不执行
│
├─ 4. Stage 2a: BaseInfo（如果 stages ∈ {all, base_info}）
│     run_base_info_stage() → 所有文件并行，Semaphore 控制并发
│     └─ print_stage_summary()
│
├─ 5. Stage 2b: FactExtraction（如果 stages ∈ {all, fact_extraction}）
│     _check_stage_2b_prerequisites() → 验证输入文件存在
│     run_fact_extraction_stage() → 所有文件并行
│     └─ print_stage_summary()
│
└─ 6. 自动聚合：02_extracted → 04_structured
      aggregate_frontmatter()（供前端渐进增强）
```

### Stage 2a: BaseInfo 单文件流水线（base_info/extractor.py）

```
extract_base_info(input_path, output_path)
│
├─ read_frontmatter(input_path) → (existing_fm, body)
│
├─ 获取/生成 article_id
│     优先从 frontmatter 读取（Stage 1 已写入）
│     旧文件缺少 id → generate_id(source_url) 回退生成
│
├─ skip_existing 检查
│     输出文件已存在 + id 存在 + 所有 BaseInfo 字段完整 → 跳过
│
├─ 空 body 检查
│     body 为空 → 根据 extraction_status 输出原因，跳过 Agent
│
├─ determine_missing_fields(existing_fm)
│     对比 frontmatter 与 BaseInfo schema，找出缺失字段
│
├─ source_type 目录名推断（source_type.py，零 Agent 调用）
│     infer_source_type(input_path)
│     目录名 → config.yaml sources.{name}.type 映射
│     命中 → 直接写入，从 missing_fields 中移除
│
├─ 仍有缺失字段 → _extract_missing_fields_via_agent()（兜底）
│     仅在以下条件全部满足时调用：
│       1. 正文非空
│       2. source_type 推断后 missing_fields 仍非空
│       3. 缺失字段无法通过工程手段补全（如 title 只能从原文提取）
│     │
│     ├─ build_base_info_user_prompt(missing_fields, body[:8000])
│     ├─ call_agent_with_retry(max_turns=3)
│     ├─ parse_json_response(text)
│     └─ 合并：只写入 missing_fields 中的字段（防御性过滤，已有字段绝不覆盖）
│
└─ write_frontmatter(output_path, merged_fm, body)
      输出到 data/02_extracted/{source}/XX.md
      写入 pipeline_stage: "base_info_extracted"
```

### Stage 2b: FactExtraction 单文件流水线（fact_extraction/extractor.py）

```
extract_fact_extraction(input_path, output_path)
│
├─ read_frontmatter(input_path) → (existing_fm, body)
│
├─ skip_existing 检查
│     id 存在 + 所有 FactExtraction 字段完整 → 跳过
│
├─ 空 body 检查 → 跳过 Agent
│
├─ extraction_status == "failed" → 跳过（正文仅为错误信息）
│
├─ 读取 title / source（来自 Stage 2a 已写入的 frontmatter）
│
├─ 调用 Agent 提取
│     build_fact_extraction_user_prompt(title, source, body[:12000])
│     → call_agent_with_retry(max_turns=3)
│     → parse_json_response(text)
│
├─ _validate_fact_extraction(data) — 5 级容错校验（validator.py）
│     ├─ 1. Pydantic 严格校验 → 通过即返回
│     ├─ 2. 枚举值模糊匹配（infra → infrastructure_update）
│     ├─ 3. 枚举交叉互换修复（eventType ↔ epistemicStatus swap）
│     ├─ 4. 单向枚举修复 + 默认值回退
│     └─ 5. 超长文本自然边界截断（tldr ≤ 80, objectiveSummary ≤ 150）
│
├─ model_dump(mode="json") → merge 到 existing_fm
│
└─ write_frontmatter(output_path, merged_fm, body)
      Stage 2b 的输出与输入路径相同（原位更新）
      写入 pipeline_stage: "fact_extracted"
```

## 设计决策

### 两阶段分离：阶段间串行、阶段内并行

Stage 2a (BaseInfo) 和 Stage 2b (FactExtraction) **严格串行**——Stage 2a 全部完成后才开始 Stage 2b：

- **数据依赖**：Stage 2b 的 prompt 需要 `title` 和 `source`，这些字段在 Stage 2a 处理后的输出文件中才能保证完整
- **避免写冲突**：两个阶段都向同一文件的 frontmatter 写入，串行执行天然避免了并发写入同一文件的竞态条件

每个阶段内部使用 `asyncio.Semaphore` 控制并发，所有文件的 Agent 调用并行发起。

### source_type 目录名推断（零 Agent 调用）

BaseInfo 的核心任务是确定 `source_type`。对于绝大多数数据源，这个信息在 `config.yaml` 中已经明确配置（`type` 字段），而文件目录名就是 source 的 `name`（如 `arxiv-cs-ai`、`techcrunch`），与配置一一对应。

`base_info/source_type.py` 在模块加载时构建 `目录名 → source.type` 映射表，处理文件时优先从路径推断。只有推断失败（目录名在配置中找不到对应源）时才回退到 Agent。

```python
# 推断逻辑：data/01_raw/arxiv-cs-ai/01.md → arxiv-cs-ai → academic_paper
infer_source_type(Path("data/01_raw/arxiv-cs-ai/01.md"))
# → "academic_paper"
```

### BaseInfo Agent 是兜底，不是主流程

`base_info/extractor.py` 中的 `_extract_missing_fields_via_agent()` 是私有函数，仅在工程手段穷尽后作为最后手段调用：

- 正常流程中，`id`/`title`/`source`/`published`/`created` 在 Stage 1 ingest 已写入 frontmatter
- `source_type` 在上游通过目录名 → config.yaml 映射推断完成（零 token）
- 只有遇到脏数据（旧文件缺少字段、config 未覆盖的边缘 case）才会触发 Agent
- 因此绝大部分文件的 Agent 调用在此阶段被跳过

### 存量字段保护（merge 策略）

提取结果合并到 frontmatter 时，遵循 **"已有字段绝不覆盖"** 原则：

- 读取现有 frontmatter → 对比 schema 找出缺失字段 → 只提取缺失字段 → 合并写入
- 合并时再次检查 `field_name in missing_fields` 做防御性过滤，防止 Agent 幻觉覆盖 Stage 1 的权威数据
- `skip_existing` 机制进一步减少重复调用：输出文件已存在且所有字段完整 → 跳过
- 可以安全地重复运行，`--force` 可强制重新提取

### 5 级容错校验链（fact_extraction/validator.py）

LLM 输出天然不可靠。`_validate_fact_extraction()` 实现多层容错：

1. **Pydantic 严格校验** — `FactExtraction.model_validate(data)`，通过即返回
2. **枚举值模糊匹配** — Agent 可能返回 `"infrastructure"` 而非 `"infrastructure_update"`，通过 `_EVENT_TYPE_FUZZY` / `_EPISTEMIC_FUZZY` 映射表修正
3. **枚举交叉互换修复** — Agent 有时把 `eventType` 和 `epistemicStatus` 的值填反，检测到后自动 swap
4. **单向枚举修复** — 仅一个字段填错到另一个枚举域时，单向移动并回退默认值
5. **超长文本截断** — `tldr`（max 80 字符）和 `objectiveSummary`（max 150 字符）超长时，使用三级断句策略：强断句（`。！？.!?\n`）→ 弱断句（`；，,; `）→ 硬截断

### fail-per-article 策略

每个文件的提取是独立的——某个文件 Agent 调用失败、JSON 解析错误、校验失败，通过 `try/except` 捕获后报告并跳过，**不影响其他文件**。`asyncio.gather(return_exceptions=True)` 保证单个任务异常不中断整体调度。

### 正文截断控制 Token 消耗

两个子阶段对正文长度有不同的截断策略：

| 子阶段 | 截断长度 | 理由 |
|--------|----------|------|
| BaseInfo | 8000 字符 | 兜底场景下只需判断文章类型，不需要全文 |
| FactExtraction | 12000 字符 | 事实提取需要更多上下文来准确识别实体和逻辑脉络 |

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
sourceType: "academic_paper"                   # ← Stage 2a 新增（目录名推断或 Agent 兜底）
pipeline_stage: "base_info_extracted"          # ← Stage 2a 更新
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
pipeline_stage: "fact_extracted"               # ← Stage 2b 更新
---
正文内容...
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
| 目录名不匹配 config | `infer_source_type` 返回 `None`，回退到 Agent 判断 |

### Agent 调用的重试策略

- 底层使用 `call_agent_with_retry`（`pipeline/core/agent.py`）
- 默认 `max_turns=3`：失败时指数退避重试（2s → 4s → 8s，含 jitter）
- 重试仅针对网络错误和临时性失败，JSON 解析错误不重试

### 幂等性保证

- `--skip-existing`（默认启用）：输出文件已存在且字段完整 → 跳过
- 存量字段 merge 策略：已有字段绝不覆盖
- `--force` 可强制重新提取所有字段
- 可以安全地重复运行，不会产生重复或损坏的数据

## 与其他模块的关系

### 上游（输入）

| 模块 | 说明 |
|------|------|
| `pipeline/ingestion/` | Stage 1b，产出 `data/01_raw/{source}/*.md` 原始文章文件 |
| `pipeline/config.yaml` | 数据源配置（type 字段用于 source_type 推断） |
| `pipeline/schemas/base_info.py` | BaseInfo / SourceType Pydantic 模型定义 |
| `pipeline/schemas/fact_extraction.py` | FactExtraction / EventType / EpistemicStatus / Entities 模型定义 |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/analysis/` | Stage 3，读取 `data/02_extracted/` 中的文件，进行三维度深度分析（tech-architect / capital-analyst / risk-assessor） |
| `pipeline/synthesis/aggregate_frontmatter.py` | 每次 extract 完成后自动调用，将 frontmatter 聚合到 `data/04_structured/` 供前端使用 |

### 水平依赖

| 模块 | 说明 |
|------|------|
| `pipeline/core/agent.py` | `call_agent_with_retry` / `parse_json_response` / `StageResult` — Agent 调用的统一封装 |
| `pipeline/core/config_loader.py` | 配置加载（源列表、LLM 参数、路径）、`resolve_data_dir` |
| `pipeline/utils/frontmatter.py` | YAML frontmatter 的读写操作（`read_frontmatter` / `write_frontmatter`） |
| `pipeline/utils/enum_utils.py` | `fuzzy_match_enum` — 枚举值模糊匹配工具 |
| `pipeline/utils/text_utils.py` | `truncate_at_natural_break` — 自然边界截断 |
| `pipeline/utils/id_utils.py` | `generate_id` — SHA-256 文章 ID 生成 |
| `pipeline/utils/file_utils.py` | `get_project_root` / `ensure_dir` / `list_files` |

## 扩展指南

### 新增 BaseInfo 字段

1. 在 `pipeline/schemas/base_info.py` 的 `BaseInfo` 模型中添加新字段（含 `description=`）
2. 在 `base_info/prompts.py` 的 `get_base_info_system_prompt()` 中添加新字段的分类标准和示例
3. `build_base_info_user_prompt()` 动态使用 `missing_fields` 构造 prompt，通常无需修改
4. 新字段会自动被 `determine_missing_fields()` 检测为缺失，无需修改 extractor

### 新增 FactExtraction 字段

1. 在 `pipeline/schemas/fact_extraction.py` 的 `FactExtraction` 模型中添加新字段
2. 在 `fact_extraction/prompts.py` 的 `get_fact_extraction_system_prompt()` 中添加新字段的提取说明和输出格式
3. 如果新字段是枚举类型，在 `fact_extraction/validator.py` 中添加对应的模糊匹配映射表
4. 将新字段名加入 `_FACT_EXTRACTION_FIELDS` 集合（用于 skip_existing 检查）

### 新增校验修复规则

1. 在 `fact_extraction/validator.py` 的 `_validate_fact_extraction()` 函数中添加新的修复逻辑
2. 在相应的模糊映射表（`_EVENT_TYPE_FUZZY` / `_EPISTEMIC_FUZZY`）中添加新的变体映射
3. 新增修复逻辑应遵循现有 5 级容错链的优先级顺序

### 新增数据源（source_type 映射）

如果新数据源的 `type` 在 `config.yaml` 中已正确配置，`infer_source_type()` 自动生效，无需额外修改。如果目录名与 source name 不一致，需要在 `base_info/source_type.py` 的映射逻辑中添加特殊处理。
