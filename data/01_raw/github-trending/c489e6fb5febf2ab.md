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
- '2026-07-30'
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
pipeline_stage: ingested
id: c489e6fb5febf2ab
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