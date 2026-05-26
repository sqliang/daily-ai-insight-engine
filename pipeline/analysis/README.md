# Stage 3 Deep Analysis — 深度分析

## 模块概览

Deep Analysis 是 Daily AI Insight Engine 流水线的 **Stage 3**，负责对 Stage 2 产出的结构化事实进行三维度深度研判：从技术质量、资本格局、前瞻风险三个视角独立评估每篇文章，生成具有决策参考价值的分析结论。

**一句话职责**：读 Markdown 文件（含 Stage 2 事实）→ 3 个 Agent 并行评估 → 合并到 frontmatter → 写入 `data/03_analyzed/`。

在整个流水线中的位置：

```
scout (1a)  →  ingest (1b)  →  extract (2)       →  analyze (3)    →  aggregate (4a)  →  synthesize (4b)
  URL清单        .md文件       BaseInfo + 事实提取    深度分析            聚合JSON           日报生成
```

Stage 3 内部三个评估维度**完全独立、单文件内并行执行**：

```
                         ┌─ QualitativeAssessment (技术架构师视角)
analyze_one_file() ─────┼─ ValueAssessment (VC 资本分析师视角)
                         └─ ForesightAndActionability (风控专家视角)

每篇文章 = 1 次文件读取 + 3 路并行 Agent 调用 + 1 次文件写入
```

**核心设计理念**：三个维度解答三个不同的问题——"当下有多重要？""长期价值在哪？""有什么风险、该做什么？"——分别由不同专业视角的 Agent 独立完成，互不干扰。

## 快速开始

### 基本用法

```bash
# ===== 全量处理 =====
# 处理所有 data/02_extracted/ 下的文件（三个维度全部运行）
uv run python pipeline/run.py analyze

# ===== 按 source 子目录处理 =====
# 只处理某个数据源的文章（如 arxiv 论文）
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/

# 只处理 36氪 的文章
uv run python pipeline/run.py analyze --input data/02_extracted/36kr/

# ===== 单文件处理 =====
# 处理单篇文章（适合测试 prompt 效果或重试失败文件）
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/01.md

# ===== 按维度运行 =====
# 只运行定性研判（技术架构师视角）
uv run python pipeline/run.py analyze --stage qualitative

# 只运行价值评估（资本分析师视角）
uv run python pipeline/run.py analyze --stage value

# 只运行前瞻预测（风控专家视角）
uv run python pipeline/run.py analyze --stage foresight

# ===== 单文件 + 单维度（快速调试） =====
# 对一篇文章只跑一个维度，验证 prompt 或模型效果
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/01.md --stage qualitative

# ===== 重新处理 =====
# 强制重新分析全部文件（忽略 skip-existing）
uv run python pipeline/run.py analyze --force

# 强制重新分析某个 source 子目录
uv run python pipeline/run.py analyze --input data/02_extracted/hackernews/ --force

# 只重跑单个维度（如补齐之前跳过的 value 评估）
uv run python pipeline/run.py analyze --stage value --force

# ===== 并发与模型 =====
# 限制并发文件数（降低 API 压力）
uv run python pipeline/run.py analyze --concurrency 2

# 指定非默认模型
uv run python pipeline/run.py analyze --model claude-sonnet-4-6

# ===== 调试与预览 =====
# 干跑：列出将处理的文件，不调用 LLM
uv run python pipeline/run.py analyze --dry-run

# 干跑指定目录
uv run python pipeline/run.py analyze --input data/02_extracted/36kr/ --dry-run

# 详细日志（显示 DEBUG 级别信息）
uv run python pipeline/run.py analyze --verbose

# 单文件 + 详细日志（排查单个文件的问题）
uv run python pipeline/run.py analyze --input data/02_extracted/36kr/01.md --verbose

# ===== 推荐工作流 =====
# 1. 先干跑确认文件范围
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/ --dry-run

# 2. 确认无误后正式运行
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/

# 3. 用 verbose 排查失败文件
uv run python pipeline/run.py analyze --input data/02_extracted/arxiv-cs-ai/01.md --force --verbose
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--input` / `-i` | `data/02_extracted/` | 输入 .md 文件或目录路径 |
| `--concurrency` / `-c` | `config.yaml` 中 `stages.analyze.concurrency`（3） | 并发文件处理数 |
| `--stage` | `all` | 只运行指定维度：`qualitative` / `value` / `foresight` / `all` |
| `--force` | `false` | 强制重新分析（忽略 `--skip-existing`） |
| `--skip-existing` | `true` | 跳过已分析的文件（按维度粒度检查） |
| `--dry-run` | `false` | 只列出将处理的文件，不实际调用 LLM |
| `--model` / `-m` | `config.yaml` 中 `llm.models.analyze.name` | LLM 模型名称 |
| `--verbose` / `-v` | `false` | 详细日志输出 |

### 作为 Python 模块调用

```python
from pipeline.analysis import run_analysis
import asyncio

results = asyncio.run(run_analysis(
    concurrency=3,
    stages="all",
    force=False,
))
# → [StageResult, ...]
```

## 模块结构

```
pipeline/analysis/
├── __init__.py                   # 包入口，导出 run_analysis
├── cli.py                        # CLI 契约：参数声明 + register_subparser + execute
├── run_analysis.py               # 主编排：文件发现 → 配置加载 → 批量调度 → 汇总 → 自动聚合
├── deep_analysis_agent.py        # Agent 编排：单文件 3 路并行 + 合并写入 + 批量调度
├── validators.py                 # Pydantic 校验 + 模糊枚举修复（3 个维度各一个校验函数）
├── fuzzy_maps.py                 # 8 张模糊枚举匹配映射表（纯数据，无业务逻辑）
│
└── prompts/                      # 提示词（按维度独立）
    ├── __init__.py               # 统一导出接口
    ├── qualitative_system.py     # QualitativeAssessment system prompt（技术架构师）
    ├── value_system.py           # ValueAssessment system prompt（VC 资本分析师）
    ├── foresight_system.py       # ForesightAndActionability system prompt（风控专家）
    └── user_prompts.py           # 3 个 user prompt 构建器（注入 Stage 2 事实 + 正文）
```

**依赖的核心模块**：

```
pipeline/core/
├── agent.py                     # call_agent_with_retry / parse_json_response / StageResult
├── config_loader.py             # get_llm_config / get_stage_config / resolve_data_dir

pipeline/utils/
├── frontmatter.py               # read_frontmatter / write_frontmatter（通用 YAML frontmatter 读写）
├── file_utils.py                # ensure_dir（目录创建）
├── text_utils.py                # truncate_at_natural_break（自然边界截断）
└── enum_utils.py                # fuzzy_match_enum（枚举值模糊匹配，validators.py 使用）

pipeline/schemas/
└── deep_analysis.py             # 3 个评估模型 + 16 个枚举 + 8 个嵌套子模型

pipeline/analysis/
├── fuzzy_maps.py                # 8 张模糊枚举匹配表（Sentiment / DeveloperTone / HypeLevel /
│                                #   InformationEntropy / EngineeringComplexity /
│                                #   ValueCaptureLayer / MoatImpact / ConfidenceLevel /
│                                #   ActionableInsight）—— 纯数据模块，被 validators.py 导入
├── validators.py                # 3 个维度的 Pydantic 校验 + 模糊枚举修复函数
│                                #   validate_qualitative / validate_value / validate_foresight
│                                #   共享 _get_nested() 辅助函数，被 deep_analysis_agent.py 导入
```

## 核心流程

### 总览：两层并行模型

Stage 3 采用**两层并行**架构——外层控制文件并发，内层控制单文件的维度并发。

```
                        run_analysis()                         ← 主编排入口
                             │
              1. 加载配置: model / concurrency=3 / paths
              2. discover_files() → 326 个 .md 文件
              3. asyncio.Semaphore(3) ← 外层：同时最多 3 个文件
                             │
              4. run_deep_analysis_stage()
                             │
    ┌────────────────────────┼────────────────────────────┐
    │         外层：Semaphore(3) — 3 个文件同时在跑         │
    │                                                    │
    │  process_one(文件A)    process_one(文件B)    process_one(文件C)
    │       │                     │                     │
    │       ▼                     ▼                     ▼
    │  analyze_one_file(A)  analyze_one_file(B)  analyze_one_file(C)
    │       │                     │                     │
    │       │   ┌───────────┐     │   ┌───────────┐     │   ┌───────────┐
    │       │   │ 内层：     │     │   │ 内层：     │     │   │ 内层：     │
    │       │   │ 3 Agent   │     │   │ 3 Agent   │     │   │ 3 Agent   │
    │       │   │ 并行调用   │     │   │ 并行调用   │     │   │ 并行调用   │
    │       │   │           │     │   │           │     │   │           │
    │       │   │ qual ◀──▶ │     │   │ qual ◀──▶ │     │   │ qual ◀──▶ │
    │       │   │ value ◀──▶│     │   │ value ◀──▶│     │   │ value ◀──▶│
    │       │   │ foresight │     │   │ foresight │     │   │ foresight │
    │       │   │           │     │   │           │     │   │           │
    │       │   │ asyncio   │     │   │ asyncio   │     │   │ asyncio   │
    │       │   │ .gather() │     │   │ .gather() │     │   │ .gather() │
    │       │   └───────────┘     │   └───────────┘     │   └───────────┘
    │       │   合并 → 写入        │   合并 → 写入        │   合并 → 写入
    │       ▼                     ▼                     ▼
    │  文件A 完成             文件B 完成             文件C 完成
    │  Semaphore 释放 → D 进入  Semaphore 释放 → E 进入  Semaphore 释放 → F 进入
    │                                                    │
    └────────────────────────────────────────────────────┘
                             │
              5. aggregate_frontmatter()
                 03_analyzed → 04_structured (自动)
                             │
              6. _print_summary()  成功 / 跳过 / 失败
```

| 层级 | 并发机制 | 控制参数 | 最大并发 Agent 数 (--stage all) |
|------|---------|---------|-------------------------------|
| 外层（文件级） | `asyncio.Semaphore` | `concurrency`（默认 3） | 3 个文件同时处理 |
| 内层（维度级） | `asyncio.gather` | 固定 3 个维度 | 3 个 Agent / 文件 |
| **总计** | | | **3 × 3 = 9 个 Agent 同时运行** |

> 只运行单个维度时（如 `--stage qualitative`），每个文件仅 1 个 Agent 调用，最大并发降为 3。

### 主编排（run_analysis.py）

```
run_analysis(input_path, concurrency, stages, skip_existing, force, dry_run, model)
│
├─ 1. 加载配置
│     模型名 / 并发数 / 路径均支持 CLI 参数覆盖
│     force=True → skip_existing=False
│
├─ 2. 文件发现（discover_files）
│     基准目录统一使用 data/02_extracted/，保证输出保留 source 子目录结构
│
├─ 3. 路径计算（compute_output_base）
│     data/02_extracted/{source}/XX.md → data/03_analyzed/{source}/XX.md
│
├─ 4. Dry run → 只打印文件列表 + 对应输出路径，不执行
│
├─ 5. 创建 asyncio.Semaphore(concurrency) → 调用 run_deep_analysis_stage()
│     ├─ 外层 Semaphore 控制同时处理的文件数（默认 3）
│     ├─ 内层 asyncio.gather 单文件内并行 3 个维度
│     └─ return_exceptions=True 保证单文件异常不中断整体调度
│
├─ 6. 自动聚合：03_analyzed → 04_structured
│     aggregate_frontmatter()（纯机械操作，零 LLM 调用。与 Stage 2 保持一致）
│
└─ 7. _print_summary() 打印成功/跳过/失败统计
```

### 单文件处理流水线（deep_analysis_agent.py: analyze_one_file）

每篇文章的完整处理路径如下。输入是 `data/02_extracted/` 下一个 .md 文件（含 Stage 2 的 frontmatter + 正文），输出是 `data/03_analyzed/` 下同名文件（frontmatter 新增 Stage 3 字段）。

```
analyze_one_file(input_path, output_path, model, skip_existing, stages)
│
├─ read_frontmatter(input_path) → (existing_fm, body)
│     existing_fm 包含 Stage 2 全部字段：title / tldr / entities / keyLogicFlow ...
│     body 为文章正文（Markdown）
│
├─ 输出文件合并保护
│     如果 output_path 已存在 → 读取已有 Stage 3 字段合并到 existing_fm
│     避免重复运行时覆盖之前正确的分析结果
│
├─ 空 body 检查 → 跳过，返回 StageResult(skipped=True)
│
├─ 跳过检查（按维度粒度）
│     对比每个维度的 Pydantic 字段集合是否已存在于输出文件
│     只将字段不完整的维度加入 to_run 列表
│     to_run 为空 → 跳过，返回 StageResult(skipped=True)
│
├─ 提取 Stage 2 上下文
│     以下字段被注入 user prompt 作为"已知事实"，Agent 无需重新提取：
│       title / source / source_type
│       tldr / objective_summary          ← Stage 2b 一句话总结 + 客观摘要
│       event_type / epistemic_status     ← Stage 2b 事件类型 + 认识论状态
│       entities / key_logic_flow         ← Stage 2b 实体 + 核心逻辑脉络
│
├─ 3 路并行 Agent 调用（_run_assessment × 3）
│     通过 _dimension_configs 配置列表驱动，只运行 to_run 中的维度：
│     │
│     ├─ _run_assessment("qualitative", get_qualitative_system_prompt,
│     │                   build_qualitative_user_prompt, validate_qualitative)
│     │   ├─ 构建 system prompt："你是一位资深 AI 技术架构师..."
│     │   ├─ 构建 user prompt：文章信息 + 事实摘要 + 正文(≤6000字符)
│     │   ├─ call_agent_with_retry(max_turns=3)  → LLM 返回 JSON
│     │   ├─ parse_json_response()               → dict
│     │   └─ validate_qualitative(data)           → QualitativeAssessment
│     │         ├─ 自动包装标量字段（如 impactScore: 7.5 → {score, reason}）
│     │         ├─ Pydantic 严格校验 → 通过即返回
│     │         ├─ 校验失败 → 8 张模糊映射表逐一修正枚举值
│     │         ├─ 补全缺失字段默认值
│     │         └─ 修复后重新校验 → 仍失败则 raise
│     │
│     ├─ _run_assessment("value", get_value_system_prompt,
│     │                   build_value_user_prompt, validate_value)
│     │   └─ 同上流程 → ValueAssessment {compoundValue, valueCaptureLayer,
│     │                                   moatImpact, keyBeneficiaries, ...}
│     │
│     └─ _run_assessment("foresight", get_foresight_system_prompt,
│                         build_foresight_user_prompt, validate_foresight)
│         └─ 同上流程 → ForesightAndActionability {marketOpportunities,
│                                                   riskMatrix, actionableInsight, ...}
│
├─ 合并结果到 existing_fm
│     model_dump(mode="json", by_alias=False) → 扁平 dict → merge 到 frontmatter
│     部分成功策略：1/3 通过就写入，失败维度下次自动重试
│
├─ write_frontmatter(output_path, merged_fm, body)
│     输出到 data/03_analyzed/{source}/XX.md，子目录结构保留
│
└─ 返回 StageResult
      .success: 至少一个维度成功 or 跳过
      .fields_extracted: 实际写入的字段名列表
      .error: 失败维度的错误信息（如有）
```

**关键数据流**：每一步的输入输出对应关系：

```
输入文件: data/02_extracted/36kr/0a9e72cc64d162f9.md
  ├─ frontmatter: {title, source, tldr, entities, keyLogicFlow, ...}  ← Stage 2 写入
  └─ body:        "2026年5月21日36氪晚报汇总..."

                               │
                               ▼  analyze_one_file()
                               │
输出文件: data/03_analyzed/36kr/0a9e72cc64d162f9.md
  ├─ frontmatter: {...Stage 2 字段全保留...}
  │               + impact_score, sentiment, developer_sentiment, ...    ← qualitative
  │               + compound_value, value_capture_layer, moat_impact, ... ← value
  │               + market_opportunities, risk_matrix, actionable_insight ← foresight
  └─ body:        "2026年5月21日36氪晚报汇总..."  ← 正文原样保留
```

## 设计决策

### 三维度完全独立 + 单文件内并行

QualitativeAssessment、ValueAssessment、ForesightAndActionability 三个维度之间**没有数据依赖**：

- 每个维度有独立的 system prompt（不同角色视角）和独立的 Pydantic 输出 schema
- 在单文件内通过 `asyncio.gather` 并行执行，等待最慢的维度完成即可
- 一个维度的失败不影响其他维度（部分成功策略）

### 按维度粒度 skip_existing

不同于 Stage 2 的"整文件跳过"，Stage 3 的跳过检查按**单个评估维度**进行：

- 读取输出文件 frontmatter，检查每个维度的字段集合是否完整
- 只重新运行字段缺失的维度，已完成的维度不重复调用 LLM
- 例如：之前只跑了 `--stage qualitative`，下次跑 `--stage all` 时只会运行 value + foresight

这依赖于 `_ASSESSMENT_FIELD_SETS` 中预定义的每个维度的 Pydantic 字段名集合。

### 部分成功策略

三个维度中只要有一个成功提取到字段，就写入输出文件：

- `has_error` + `len(all_fields_written) > 0` → `success=True`（部分成功也算成功）
- 失败的维度会留下错误信息在 `error_messages` 中
- 下次运行时，失败的维度会被 `skip_existing` 检测为"字段不完整"并重新运行

### 正文截断策略

Stage 3 的正文截断比 Stage 2 更短（6000 vs 12000 字符）：

- Stage 2 已经将长文浓缩为结构化事实（tldr、entities、keyLogicFlow 等）
- Agent 主要依据这些结构化事实做出研判，正文提供补充上下文
- 截断在自然断点处（句号、段落结束），避免破坏语义完整性

### 两层并发控制

```
外层：asyncio.Semaphore(concurrency)  → 控制同时处理的文件数（默认 3）
内层：asyncio.gather(3 个 Agent)      → 单文件内 3 个维度并行

总并发 Agent 调用数 = concurrency × 3
```

### 模糊枚举匹配 + 嵌套模型修复

LLM 输出天然不可靠，`validate_qualitative()` / `validate_value()` / `validate_foresight()`（位于 `validators.py`）各有一套多层容错：

1. **嵌套模型自动包装**：LLM 可能返回 `"impactScore": 7.5`（纯数字），自动包装为 `{score: 7.5, reason: "AI 未提供评分依据"}`
2. **Pydantic 严格校验**：通过即返回
3. **枚举值模糊匹配**：LLM 返回 `"bullish"` → 自动映射为 `"positive"`，共维护 8 张模糊映射表
4. **缺失字段补全**：列表字段缺失 → `[]`；对象字段缺失 → 默认结构
5. **修复后重新校验**：全部修复后再跑一次 Pydantic，仍失败才报错

模糊匹配表涵盖 8 个枚举维度：Sentiment、DeveloperTone、HypeLevel、InformationEntropy、EngineeringComplexity、ValueCaptureLayer、MoatImpact、ConfidenceLevel、ActionableInsight。

### 输出文件合并保护

当输出文件已存在时（`output_path.exists()`），分析阶段会先读取已有输出文件的 Stage 3 字段并合并到当前 frontmatter 中：

```python
# deep_analysis_agent.py:536-544
if output_path.exists():
    out_fm, _ = read_frontmatter(output_path)
    for key, value in out_fm.items():
        if key in _all_stage3_fields:
            existing_fm[key] = value
```

这确保了：重复运行时不会覆盖已有的正确分析结果；部分维度重跑时已有维度不受影响。

### Feedback loop：分析完成后自动聚合

`run_analysis()` 完成后自动调用 `aggregate_frontmatter()`（Stage 4a），将 `data/03_analyzed/` 中的所有 frontmatter 聚合到 `data/04_structured/`：

- 纯机械操作，零 LLM 调用，< 1 秒完成
- 使前端仪表盘在分析完成后立即可用
- 与 Stage 2 extraction 的行为保持一致（extraction 完成后也会自动聚合）

## 数据流

### 输入

| 数据 | 路径 | 说明 |
|------|------|------|
| 已提取文章 | `data/02_extracted/{source}/*.md` | Stage 2 产出，含 BaseInfo + FactExtraction 全部字段 + 正文 |
| 源配置 | `pipeline/config.yaml` | 用于读取 LLM 模型名、并发数等参数 |

### 输出

| 数据 | 路径 | 格式 | 说明 |
|------|------|------|------|
| 已分析文章 | `data/03_analyzed/{source}/*.md` | Markdown + 丰富后的 YAML frontmatter | 包含 Stage 2 全部字段 + Stage 3 三个维度的分析字段，供 Stage 4a aggregate 消费 |

### Frontmatter 字段演进

**输入**（Stage 2b 产出，来自 `data/02_extracted/`）：

```yaml
id: "098b39fb4bd5fbf2"
title: "Interference-Aware Multi-Task Unlearning"
source: "https://arxiv.org/abs/2605.19042"
source_type: "academic_paper"
published: "2026-05-20"
created: "2026-05-21T08:30:00Z"
extraction_status: "success"
pipeline_stage: "fact_extracted"
tldr: "提出干扰感知的多任务遗忘方法..."
objective_summary: "研究者提出一种新的机器遗忘学习方法..."
event_type: "framework_tools"
epistemic_status: "verified_fact"
entities:
  companies: []
  technologies: ["Machine Unlearning", "Multi-Task Learning"]
  keyPeople: ["Ying-Hua Huang"]
keyLogicFlow:
  - "传统遗忘学习方法在单任务上有效，但在多任务场景下会产生任务间干扰..."
---
正文内容...
```

**Stage 3 后**（新增以下 Stage 3 字段，Stage 2 字段保持不变）：

```yaml
# ===== Stage 3: QualitativeAssessment（定性研判） =====
impact_score: {score: 6.5, reason: "论文提出的干扰感知方法有实际应用价值，但距离生产部署还有距离..."}
sentiment: "positive"
developer_sentiment: {tone: "excited", primary_focus: "多任务遗忘的工程实用性"}
hype_assessment: {level: "low", reason: "论文提供了充分的实验数据和消融研究，没有夸张宣传"}
information_entropy: "high"
domain_disruption: {technical_innovation: "提出任务间梯度冲突识别机制...", business_model: "可应用于模型合规性服务..."}
engineering_complexity: "prototype"

# ===== Stage 3: ValueAssessment（价值与格局评估） =====
compound_value: {score: 7.0, reason: "机器遗忘是 AI 合规的刚需方向，3-5 年内大概率成为模型训练的标准环节..."}
value_capture_layer: "foundation_model"
moat_impact: "creates_new_moat"
key_beneficiaries: ["Anthropic", "OpenAI", "Google DeepMind"]
competitive_casualty: ["传统数据清洗工具厂商"]

# ===== Stage 3: ForesightAndActionability（前瞻预测与行动转化） =====
market_opportunities:
  - "开发者可基于该方法构建模型合规性审计 SaaS 工具"
  - "建议关注 AI Act 合规要求对遗忘学习工具的需求拉动"
risk_matrix:
  regulatory: "AI Act 可能要求在欧盟部署的模型具备遗忘能力，合规成本增加"
  technological: "方法目前仅在小规模模型上验证，大规模模型的泛化性存疑"
  competitive: "各大模型厂商可能自行研发类似方案，形成专利壁垒"
  ethical: "无"
  additional: []
confidence: {impact: "high", compound: "medium", hype: "high"}
actionable_insight: "monitor"
---
正文内容...
```

### 字段写入规则

- 所有 Stage 3 字段以 **snake_case** 写入 frontmatter（Python 字段名）
- `model_dump(mode="json", by_alias=False)` 确保输出使用 Python 名而非 camelCase alias
- `flat_frontmatter_to_nested()`（在 aggregate 阶段）同时支持 snake_case 和 camelCase，兼容性无问题

## 错误处理

| 场景 | 行为 |
|------|------|
| 文件读取失败 | 返回 `StageResult(success=False)`，**不影响其他文件** |
| 正文为空 | 跳过 Agent 调用，返回 `StageResult(skipped=True)` |
| 所有维度均已完成（skip_existing） | 跳过，返回 `StageResult(skipped=True)` |
| 单个维度 Agent 调用失败（3 次重试耗尽） | 该维度字段不写入；其他维度正常写入；日志记录错误 |
| JSON 解析失败 | 该维度字段不写入；其他维度正常处理（5 级 JSON 恢复 parser 也无法挽救时） |
| Pydantic 校验失败（含模糊匹配后） | 该维度字段不写入；其他维度正常处理 |
| 部分维度成功 | 成功维度写入输出文件；下次运行时失败维度自动重试 |
| 输出文件写入失败 | 返回 `StageResult(success=False)` |
| 单个文件未处理异常 | `asyncio.gather(return_exceptions=True)` 捕获，转为 `StageResult(success=False)` |
| 输入目录下无 .md 文件 | 输出 "发现 0 个 .md 文件"，干净退出 |

### Agent 调用的重试策略

- 底层使用 `call_agent_with_retry`（`pipeline/core/agent.py`）
- 默认 `max_turns=3`：失败时指数退避重试（2s → 4s → 8s，含 jitter）
- 重试仅针对网络错误和临时性失败，JSON 解析错误不重试

### 幂等性保证

- `--skip-existing`（默认启用）：输出文件已存在且维度字段完整 → 跳过该维度
- 部分成功策略：失败的维度下次自动重试
- 输出文件合并保护：已有正确字段不会被覆盖
- 可以安全地重复运行，不会产生重复或损坏的数据

## 与其他模块的关系

### 上游（输入）

| 模块 | 说明 |
|------|------|
| `pipeline/extraction/` | Stage 2b，产出 `data/02_extracted/{source}/*.md`，含 BaseInfo + FactExtraction + 正文 |
| `pipeline/schemas/deep_analysis.py` | QualitativeAssessment / ValueAssessment / ForesightAndActionability 模型定义及其 16 个枚举 |
| `pipeline/schemas/fact_extraction.py` | FactExtraction 模型定义（Stage 3 从 frontmatter 中读取 entities、eventType 等字段作为上下文） |

### 下游（消费方）

| 模块 | 说明 |
|------|------|
| `pipeline/aggregation/aggregate_frontmatter.py` | Stage 4a，读取 `data/03_analyzed/` 中所有 frontmatter，按 source 分组聚合成 JSON |
| `pipeline/synthesis/` | Stage 4b，Editor-in-Chief 日报生成，使用分析字段进行 Top 5 排序和信号筛选 |
| `src/app/dashboard/` | Next.js 前端仪表盘，读取 `data/04_structured/all_articles.json` 渲染 KPI 卡片和图表 |

### 水平依赖

| 模块 | 说明 |
|------|------|
| `pipeline/core/agent.py` | `call_agent_with_retry` / `parse_json_response` / `StageResult` — Agent 调用的统一封装 |
| `pipeline/core/config_loader.py` | 配置加载（LLM 参数、路径）、`resolve_data_dir` |
| `pipeline/utils/frontmatter.py` | YAML frontmatter 的读写操作（`read_frontmatter` / `write_frontmatter`） |
| `pipeline/utils/enum_utils.py` | `fuzzy_match_enum` — 枚举值模糊匹配工具 |
| `pipeline/utils/text_utils.py` | `truncate_at_natural_break` — 自然边界截断 |
| `pipeline/utils/file_utils.py` | `ensure_dir` — 目录创建 |
| `pipeline/aggregation/aggregate_frontmatter.py` | 每次 analyze 完成后自动调用 |

## 扩展指南

### 新增分析维度

1. 在 `pipeline/schemas/deep_analysis.py` 中创建新的 Pydantic 模型（含所有嵌套子模型和枚举）
2. 在 `prompts/` 下新增 system prompt 文件（如 `new_dimension_system.py`）
3. 在 `prompts/user_prompts.py` 中新增 user prompt 构建函数
4. 在 `prompts/__init__.py` 中导出新的 prompt 函数
5. 在 `validators.py` 中新增校验函数 `validate_new_dimension(data: dict) → NewDimension`
6. 在 `deep_analysis_agent.py` 的 `_dimension_configs` 列表中追加新维度配置行
7. 在 `cli.py` 的 `--stage` choices 中添加新维度名称

### 新增评估字段（在现有维度内）

1. 在 `pipeline/schemas/deep_analysis.py` 的对应评估模型中添加新字段
2. 在对应的 `prompts/*_system.py` 的 system prompt 中添加新字段的说明和输出格式
3. 如果新字段是枚举类型，在 `fuzzy_maps.py` 中添加对应的模糊匹配映射表，并在 `validators.py` 的对应校验函数中添加枚举修复逻辑
4. 新字段会自动被 `_ASSESSMENT_FIELD_SETS` 包含（通过 `model_fields.keys()` 动态获取）

### 新增枚举值

1. 在 `pipeline/schemas/deep_analysis.py` 的对应枚举类中添加新值
2. 在对应的 `prompts/*_system.py` 的 system prompt 中更新枚举说明
3. 在 `fuzzy_maps.py` 的对应模糊匹配表中添加新值的同义词映射

### 调整并发策略

修改 `pipeline/config.yaml` 中 `stages.analyze.concurrency` 的值，或通过 `--concurrency` CLI 参数覆盖。当前默认值为 3，即同时处理 3 个文件（最多 9 个并发 Agent 调用）。
