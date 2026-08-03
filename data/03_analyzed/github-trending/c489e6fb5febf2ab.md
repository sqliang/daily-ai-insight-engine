---
title: alibaba/open-code-review
source: https://github.com/alibaba/open-code-review
author: []
published: ''
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
- '2026-07-26'
- '2026-07-27'
- '2026-07-28'
description: 'Open-source & free — Battle-tested at Alibaba''s scale. Hybrid architecture
  code review tool: deterministic pipelines + LLM Agent, precise line-level comments,
  built-in fine-tuned ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic
  compatible. OpenCodeReview English | 简体中文 | 日本語 | 한국어 | Русский What is Open Code
  Review? Open Code Review is an AI-powered code review CLI tool. It originated as
  Alibaba Group''s internal official AI code review assistant — over the past two
  years, it has served tens of thousands of developers and identified millions of
  code defects. After thorough validation at massive scale, we incubated it into an
  open source project for the community. Simply configure a model endpoint to get
  started. It reads Git diffs, sends changed files to a configurable LLM via an agent
  with tool-use capabilities, and generates structured review comments with line-level
  precision. The agent can read full file contents, search the codebase, inspect other
  changed files for context, and produce deep reviews — not just surface-level diff
  feedback. Beyond diff review, ocr scan reviews entire files for auditing unfamiliar
  codebases or directories that have no meaningful diff. Visit the official website
  for more details. Benchmark Compared to general-purpose agents (Claude Code), Open
  Code Review achieves significantly higher Precision and F1 with the same underlying
  model, while consuming only ~1/9 of the tokens and completing reviews faster. Note
  that its Recall is lower than general-purpose agents — a deliberate trade-off favoring
  precision over noise. A real-world code review benchmark built from 50 popular open-source
  repositories, 200 real Pull Requests, and 10 programming languages — cross-validated
  by 80+ senior engineers (1,505 annotated ground-truth issues). Metric What it measures
  Why it matters F1 Harmonic mean of precision and recall Best single number for overall
  review quality Precision Proportion of reported issues that are real defects Higher
  = fewer false alarms to triage Recall Proportion of real defects that are found
  Higher = fewer issues slip through review Avg Time Wall-clock time per review Matters
  for CI pipeline latency Avg Token Total tokens consumed per review Directly impacts
  API cost Why Open Code Review? The Problem with General-Purpose Agents If you''ve
  used general-purpose agents like Claude Code with Skills for code review, you''ve
  likely encountered these pain points: Incomplete coverage — On larger changesets,
  agents tend to "cut corners," selectively reviewing only some files and missing
  others. Position drift — Reported issues frequently don''t match the actual code
  location, with line numbers or file references drifting off target. Unstable quality
  — Natural-language-driven Skills are hard to debug, and review quality fluctuates
  significantly with minor prompt variations. The root cause: a purely language-driven
  architecture lacks hard constraints on the review process. Core Design: Deterministic
  Engineering × Agent Hybrid Open Code Review''s core philosophy is to combine deterministic
  engineering with an agent, each handling what it does best. Deterministic Engineering
  — Hard Constraints For review steps that must not go wrong, engineering logic —
  not the language model — guarantees correctness: Precise file selection — Determines
  exactly which files need review and which should be filtered, ensuring no important
  change is missed. Smart file bundling — Groups related files into a single review
  unit (e.g., message_en.properties and message_zh.properties are bundled together).
  Each bundle runs as a sub-agent with isolated context — a divide-and-conquer strategy
  that stays stable on very large changesets and naturally supports concurrent review.
  Fine-grained rule matching — Matches review rules to each file''s characteristics,
  keeping the model''s attention sharply focused and eliminating information noise
  at the source. Compared to purely language-driven rule guidance, template-engine-based
  rule matching is more stable and predictable. External positioning and reflection
  modules — Independent comment-positioning and comment-reflection modules systematically
  improve both the location accuracy and content accuracy of AI feedback. Agent —
  Dynamic Decision-Making The agent''s strengths are concentrated where they matter
  most — dynamic decisions and dynamic context retrieval: Scenario-tuned prompts —
  Prompt templates deeply optimized for code review, improving effectiveness while
  reducing token consumption. Scenario-tuned toolset — Distilled from deep analysis
  of tool-call traces in large-scale production data — including call frequency distributions,
  per-tool repetition rates, and the impact of new tools on the overall call chain
  — resulting in a purpose-built toolset that is more stable and predictable for code
  review than a generic agent toolkit. How to Use Prerequisites Git >= 2.41 — Open
  Code Review relies on Git for diff generation, code search, and repository operations.
  CLI Install npm install -g @alibaba-group/open-code-review After installation, the
  ocr command is available globally. For other installation methods (install script,
  GitHub Release binary, from source), see Installation. Quick Start 1. Configure
  LLM You must configure an LLM before reviewing code, unless you use Delegation Mode.
  ocr config provider # Select a built-in provider or add a custom one ocr config
  model # Pick a model for the active provider The interactive UI guides you through
  provider selection, API key entry, and model configuration, then automatically tests
  connectivity. For CLI setup, environment variables, custom providers, and other
  advanced configuration, see Configuration. 2. Review cd your-project # Workspace
  mode — review all staged, unstaged, and untracked changes ocr review # Branch range
  — compare two refs ocr review --from main --to feature-branch # Single commit ocr
  review --commit abc123 # Resume an interrupted range or commit review ocr session
  list ocr review --from main --to feature-branch --resume <session-id> # Full-file
  scan — review whole files instead of a diff (no git history needed) ocr scan # scan
  the entire repository ocr scan --path internal/agent # scan a directory or specific
  files # Delegation mode — let your AI coding agent perform the review itself # OCR
  handles file selection and rule resolution; no LLM configuration needed ocr delegate
  preview ocr delegate rule src/main.go src/handler.go Documentation Full documentation
  lives at open-codereview.ai/docs: Quickstart — install and run your first review
  Installation — all platforms and package managers CLI Reference — every command
  and flag Review Rules — customize review rules with path filtering and targeting
  Configuration — config keys and environment variables MCP Server — extend the review
  agent with external tools Coding Agent Integrations — integrate OCR into Claude
  Code, Codex, Cursor, etc. Skill — install as a reusable agent skill Plugin — install
  as a Claude Code / Codex / Cursor plugin Delegation Mode — let your agent review
  using its own LLM CI/CD Integration — GitHub Actions, GitLab CI, GitFlic CI, and
  Gerrit integration Session Viewer — browse and replay review sessions in browser
  Telemetry — OpenTelemetry integration for observability FAQ — common questions and
  troubleshooting Contributing This project exists thanks to all the people who contribute.
  See CONTRIBUTING.md for development setup, coding guidelines, and how to submit
  pull requests. License Apache-2.0 — Copyright 2026 Alibaba'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c489e6fb5febf2ab
source_type: community_discussion
tldr: 阿里巴巴将内部使用两年的 AI 代码审查 CLI 工具 Open Code Review 正式开源，采用确定性工程与智能体混合架构，在相同模型下仅消耗约
  1/9 的 Token 即可实现更高的代码审查精确率和 F1 值。
objective_summary: 阿里巴巴集团于 2026 年将内部 AI 代码审查工具 Open Code Review 正式开源。该工具两年内已服务数万开发者并识别数百万代码缺陷。它采用确定性工程与智能体混合架构，通过读取
  Git diff、智能文件打包和规则匹配进行审查。在 50 个开源仓库、200 个真实 PR 和 10 种编程语言的基准测试中，该工具相比通用智能体实现了更高的精确率和
  F1 值，Token 消耗仅为约 1/9。用户可通过 npm 全局安装并支持工作区模式、分支对比、单提交审查和全文件扫描等多种方式。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Alibaba
  - Alibaba Group
  technologies:
  - LLM
  - AI Code Review
  - Git
  key_people: []
key_logic_flow:
- Open Code Review 是阿里巴巴集团内部孵化的 AI 代码审查 CLI 工具，已服务数万开发者并识别数百万代码缺陷，于 2026 年正式开源。
- 该工具采用确定性工程与智能体混合架构：确定性部分负责精确文件选择、智能文件打包和规则匹配，智能体负责动态决策和上下文检索。
- 在 50 个开源仓库、200 个真实 Pull Request 和 10 种编程语言的基准测试中，Open Code Review 在相同模型下实现了更高的精确率和
  F1 值，Token 消耗仅为约 1/9。
- 工具通过 npm install -g @alibaba-group/open-code-review 全局安装，支持工作区模式、分支范围对比、单提交审查、全文件扫描和委托模式等审查方式。
- 项目提供完整的文档体系，包含快速开始、安装指南、CLI 参考、审查规则配置、CI/CD 集成、MCP 服务器和编码智能体集成等内容。
object_mentions:
- object_type: project
  name: Open Code Review
  canonical_name: alibaba/open-code-review
  url: https://github.com/alibaba/open-code-review
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Open Code Review 是阿里巴巴集团内部孵化的 AI 代码审查 CLI 工具，经过两年大规模验证后于 2026 年正式开源。
  - 该工具采用确定性工程与智能体混合架构，读取 Git diff 并通过支持工具调用的智能体生成行级精度的结构化审查评论。
  - 在 50 个开源仓库、200 个真实 Pull Request 和 10 种编程语言的基准测试中，该工具在相同模型下实现了更高的精确率和 F1 值，Token
    消耗仅为约 1/9。
  article_id: c489e6fb5febf2ab
extract_result: success
impact_score:
  score: 7.0
  reason: 阿里巴巴将内部验证两年、服务数万开发者的 AI 代码审查工具正式开源，其核心价值在于提出'确定性工程 + 智能体'混合架构——用工程逻辑硬约束（精确文件选择、智能打包、规则匹配）替代纯语言驱动的软约束，这是
    AI 辅助代码审查领域一个务实的架构创新。直接在相同模型下实现 1/9 Token 消耗 + 更高精确率和 F1 值，直接挑战了'通用智能体可直接替代专用工具'的行业叙事。该工具已通过
    npm 发布、支持 CI/CD 集成和 MCP 协议，具备快速规模化采用的条件。虽然不是范式转移级别（不改变大模型训练范式或推理架构），但足以改变 AI 代码审查的工程实践标准和成本预期，短期内会在开发者工具赛道形成鲶鱼效应。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Token 消耗仅约为通用智能体的 1/9，同等模型下精度更高，代码审查成本大幅降低
hype_assessment:
  level: low
  reason: 文章有明确的基准测试描述——50 个开源仓库、200 个真实 PR、10 种编程语言、1505 条人工标注的 ground-truth 问题、80+
    资深工程师交叉验证。同时坦诚披露了 Recall 低于通用智能体的设计取舍（刻意选择高精度低噪音而非高召回），这种透明性显著降低了炒作嫌疑。没有使用'颠覆''革命性'等
    PR 高频词汇，技术细节（文件打包策略、规则模板引擎、外部定位模块）都有具体描述，整体是实打实的技术分享。
information_entropy: high
domain_disruption:
  technical_innovation: 提出确定性工程与智能体混合架构而非纯语言驱动：精确文件选择确保大变更集不遗漏、智能文件打包（如将相关语言文件捆绑）实现分治并发审查、模板引擎式规则匹配替代易漂移的
    Prompt 引导，以及独立的外部定位和反射模块解决 AI 审查常见的'位置漂移'问题。这些工程实践虽非基础理论创新，但系统性地解决了纯 Agent 方案在代码审查场景中的覆盖不全、位置漂移和质量不稳定三个核心痛点。
  business_model: 开源策略可能重塑 AI 代码审查市场格局。该工具若被广泛采用，将对 GitHub Code Review、GitLab Code
    Suggestions 等商业产品形成成本压力（1/9 Token 意味着 API 成本骤降），同时推动 CI/CD 中 AI 审查从'按次计费'向'自托管低成本'模式迁移。MCP
    服务器和编码智能体集成支持则暗示了 Alibaba 在 AI 开发生态中的平台战略——通过开源工具占领开发者心智，而非直接售卖 SaaS 订阅。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 该项目的中长期价值主要源于其架构范式的示范效应，而非工具本身。核心洞察在于'确定性工程+智能体混合架构'——这一设计被验证可在同等模型下实现约
    9 倍 Token 效率提升和更高精确率，本质上重新定义了 AI 代码审查的成本结构。由于已在阿里内部经受大规模验证（数万开发者、数百万缺陷），开源后有望快速积累社区信任与采用，形成事实上的代码审查架构基准。但受限于
    Apache 2.0 开源许可，直接商业价值捕获有限，更可能是通过开发者心智占领和生态影响力为阿里云/通义等产品间接引流。长期看，该工具具备成为 AI 代码审查基础设施的潜力，复利效应取决于其规则生态和
    MCP 集成的网络效应能否建立——如果社区贡献的审查规则库形成飞轮，则价值将持续放大。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Alibaba
- 开源开发者社区
- Anthropic
- OpenAI
competitive_casualty:
- CodeRabbit
- PullRequest
- 通用型 AI 代码审查 SaaS
- 传统静态代码分析工具（SonarQube 等）
market_opportunities:
- 企业可将该混合架构（确定性工程+智能体）模式复制到其他开发工具链场景，如自动化安全审计、合规审查、依赖分析等，大幅降低Token成本同时提升结果稳定性
- 面向金融、医疗等强监管行业的定制化代码审查规则包或合规审查SaaS服务存在商业机会，基于OCR的确定性规则引擎可满足监管对"可解释、可追溯"的要求
- 团队可基于OCR构建代码审查质量仪表盘和度量体系，将AI审查结果与开发者绩效、代码健康度指标关联，形成工程管理数据产品
risk_matrix:
  regulatory: 代码数据通过第三方LLM端点审查可能引发数据出境与知识产权泄露风险，尤其是在金融、政务等敏感行业；企业需确认自部署模型场景下的合规边界
  technological: 该工具在Recall上有意折衷以换取高Precision，意味着部分真实缺陷会被漏报，过度依赖可能导致审查盲区；依赖Git >=
    2.41版本，老旧代码库可能面临兼容性问题
  competitive: CodeRabbit、GitHub Copilot Code Review、Amazon CodeGuru、JetBrains Qubrid等竞品已在市场建立用户习惯，OCR作为后发者需要在集成体验和社区生态上加速追赶
  ethical: 代码提交至外部模型端点存在数据投毒和IP泄露风险；工具对不同编程语言的审查质量可能存在隐式偏差（基准测试仅覆盖10种语言），非主流语言用户可能获得劣质体验
  additional:
  - 工具由阿里巴巴集团主导开源，竞争对手或与阿里存在商业冲突的企业可能对将代码审查依赖于此工具有所顾虑，存在地缘政治与商业信任风险
  - 1/9 Token消耗的对比基准依赖于特定通用智能体（Claude Code），在不同模型或部署环境下该优势可能大幅缩水
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Open Code Review
  canonical_name: alibaba/open-code-review
  url: https://github.com/alibaba/open-code-review
  positioning: 阿里巴巴开源的企业级 AI 代码审查 CLI 工具，采用确定性工程与智能体混合架构，在降低 Token 消耗的同时提升审查精度。
  technical_signal: 确定性工程负责精确文件选择、智能文件打包和规则匹配，智能体负责动态决策与上下文检索，二者分离使 Token 效率提升约 9
    倍。
  adoption_signal: 项目已在阿里巴巴内部服务数万开发者并识别数百万代码缺陷，经过两年大规模实战验证后于 2026 年正式开源。
  ecosystem_relevance: 作为阿里开源生态中的开发者工具，面向 Git 工作流深度集成并支持 CI/CD 管道和 MCP 服务器，填补了企业级开源代码审查工具的空白。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: 相比通用 AI 智能体方案，通过确定性工程约束实现了更高精确率和 F1 值，Token 消耗仅为约 1/9，属于架构层面的差异化创新。
  watch_reason: Open Code Review 通过确定性工程与智能体混合架构在代码审查领域实现显著突破，Token 效率提升约 9 倍且精度更高。经阿里巴巴内部两年大规模验证，具备向更广泛开源社区和
    CI/CD 生态扩展的潜力，值得持续跟踪其社区采纳与行业影响力扩散。
  risk_notes:
  - 项目 Recall 低于通用智能体，属于有意为之的精确率优先取舍，可能在需要高召回率的审计场景中表现不足。
  - 作为新开源项目，社区贡献生态尚未成熟，长期维护活力和第三方集成扩展能力有待持续观察评估。
  - 项目对 Git 版本有 >=2.41 的硬性依赖要求，部分老旧开发环境和 CI 系统可能无法直接兼容，需要额外升级成本才能采用。
  score: 7.0
  article_ids:
  - c489e6fb5febf2ab
  evidence_snippets:
  - Open Code Review 是阿里巴巴集团内部孵化的 AI 代码审查 CLI 工具，经过两年大规模验证后于 2026 年正式开源。
  - 该工具采用确定性工程与智能体混合架构，读取 Git diff 并通过支持工具调用的智能体生成行级精度的结构化审查评论。
  - 在 50 个开源仓库、200 个真实 Pull Request 和 10 种编程语言的基准测试中，该工具在相同模型下实现了更高的精确率和 F1 值，Token
    消耗仅为约 1/9。
---

English | 简体中文 | 日本語 | 한국어 | Русский

Open Code Review is an AI-powered code review CLI tool. It originated as Alibaba Group's internal official AI code review assistant — over the past two years, it has served tens of thousands of developers and identified millions of code defects. After thorough validation at massive scale, we incubated it into an open source project for the community. Simply configure a model endpoint to get started.

It reads Git diffs, sends changed files to a configurable LLM via an agent with tool-use capabilities, and generates structured review comments with line-level precision. The agent can read full file contents, search the codebase, inspect other changed files for context, and produce deep reviews — not just surface-level diff feedback. Beyond diff review, `ocr scan`

reviews entire files for auditing unfamiliar codebases or directories that have no meaningful diff.

Visit the official website for more details.

Compared to general-purpose agents (Claude Code), Open Code Review achieves significantly higher

PrecisionandF1with the same underlying model, while consuming only~1/9 of the tokensand completing reviews faster. Note that its Recall is lower than general-purpose agents — a deliberate trade-off favoring precision over noise.

A real-world code review benchmark built from **50** popular open-source repositories, **200** real Pull Requests, and **10** programming languages — cross-validated by 80+ senior engineers (**1,505** annotated ground-truth issues).

| Metric | What it measures | Why it matters |
|---|---|---|
F1 |
Harmonic mean of precision and recall | Best single number for overall review quality |
Precision |
Proportion of reported issues that are real defects | Higher = fewer false alarms to triage |
Recall |
Proportion of real defects that are found | Higher = fewer issues slip through review |
Avg Time |
Wall-clock time per review | Matters for CI pipeline latency |
Avg Token |
Total tokens consumed per review | Directly impacts API cost |

If you've used general-purpose agents like Claude Code with Skills for code review, you've likely encountered these pain points:

**Incomplete coverage**— On larger changesets, agents tend to "cut corners," selectively reviewing only some files and missing others.**Position drift**— Reported issues frequently don't match the actual code location, with line numbers or file references drifting off target.**Unstable quality**— Natural-language-driven Skills are hard to debug, and review quality fluctuates significantly with minor prompt variations.

The root cause: a purely language-driven architecture lacks hard constraints on the review process.

Open Code Review's core philosophy is to combine deterministic engineering with an agent, each handling what it does best.

**Deterministic Engineering — Hard Constraints**

For review steps that *must not go wrong*, engineering logic — not the language model — guarantees correctness:

**Precise file selection**— Determines exactly which files need review and which should be filtered, ensuring no important change is missed.**Smart file bundling**— Groups related files into a single review unit (e.g.,`message_en.properties`

and`message_zh.properties`

are bundled together). Each bundle runs as a sub-agent with isolated context — a divide-and-conquer strategy that stays stable on very large changesets and naturally supports concurrent review.**Fine-grained rule matching**— Matches review rules to each file's characteristics, keeping the model's attention sharply focused and eliminating information noise at the source. Compared to purely language-driven rule guidance, template-engine-based rule matching is more stable and predictable.**External positioning and reflection modules**— Independent comment-positioning and comment-reflection modules systematically improve both the location accuracy and content accuracy of AI feedback.

**Agent — Dynamic Decision-Making**

The agent's strengths are concentrated where they matter most — dynamic decisions and dynamic context retrieval:

**Scenario-tuned prompts**— Prompt templates deeply optimized for code review, improving effectiveness while reducing token consumption.**Scenario-tuned toolset**— Distilled from deep analysis of tool-call traces in large-scale production data — including call frequency distributions, per-tool repetition rates, and the impact of new tools on the overall call chain — resulting in a purpose-built toolset that is more stable and predictable for code review than a generic agent toolkit.

**Git >= 2.41**— Open Code Review relies on Git for diff generation, code search, and repository operations.

`npm install -g @alibaba-group/open-code-review`

After installation, the `ocr`

command is available globally.

For other installation methods (install script, GitHub Release binary, from source), see Installation.

**1. Configure LLM**

You must configure an LLM before reviewing code, unless you use Delegation Mode.

```
ocr config provider # Select a built-in provider or add a custom one
ocr config model # Pick a model for the active provider
```

The interactive UI guides you through provider selection, API key entry, and model configuration, then automatically tests connectivity.

For CLI setup, environment variables, custom providers, and other advanced configuration, see Configuration.

**2. Review**

```
cd your-project
# Workspace mode — review all staged, unstaged, and untracked changes
ocr review
# Branch range — compare two refs
ocr review --from main --to feature-branch
# Single commit
ocr review --commit abc123
# Resume an interrupted range or commit review
ocr session list
ocr review --from main --to feature-branch --resume <session-id>
# Full-file scan — review whole files instead of a diff (no git history needed)
ocr scan # scan the entire repository
ocr scan --path internal/agent # scan a directory or specific files
# Delegation mode — let your AI coding agent perform the review itself
# OCR handles file selection and rule resolution; no LLM configuration needed
ocr delegate preview
ocr delegate rule src/main.go src/handler.go
```

Full documentation lives at **open-codereview.ai/docs**:

- Quickstart — install and run your first review
- Installation — all platforms and package managers
- CLI Reference — every command and flag
- Review Rules — customize review rules with path filtering and targeting
- Configuration — config keys and environment variables
- MCP Server — extend the review agent with external tools
- Coding Agent Integrations — integrate OCR into Claude Code, Codex, Cursor, etc.
- Skill — install as a reusable agent skill
- Plugin — install as a Claude Code / Codex / Cursor plugin
- Delegation Mode — let your agent review using its own LLM

- CI/CD Integration — GitHub Actions, GitLab CI, GitFlic CI, and Gerrit integration
- Session Viewer — browse and replay review sessions in browser
- Telemetry — OpenTelemetry integration for observability
- FAQ — common questions and troubleshooting

This project exists thanks to all the people who contribute. See CONTRIBUTING.md for development setup, coding guidelines, and how to submit pull requests.

Apache-2.0 — Copyright 2026 Alibaba