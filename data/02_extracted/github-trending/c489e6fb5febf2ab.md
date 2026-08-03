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