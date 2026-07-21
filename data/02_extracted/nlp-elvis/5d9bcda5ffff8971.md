---
title: '🤖 AI Agents Weekly: GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7,
  Robostral Navigate, The Harness Effect, and More'
source: https://nlp.elvissaravia.com/p/ai-agents-weekly-gpt-56-family-meta
author: []
published: '2026-07-11'
created: '2026-07-14'
description: GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7, Robostral Navigate,
  The Harness Effect, and More
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5d9bcda5ffff8971
manifest_dates:
- '2026-07-14'
- '2026-07-15'
source_type: newsletter_rss
tldr: OpenAI 发布 GPT-5.6 系列模型（Sol/Terra/Luna）并推出 ChatGPT Work 智能体；Meta 发布 Muse Spark
  1.1 多模态推理模型并开放 Meta Model API。xAI、Cognition、Mistral 等公司相继发布编码模型，Google 和 Tencent
  分别开源了 Gemma 4 和 Hy3 模型。
objective_summary: 本期 AI Agents Weekly 报道了多项 AI 产品发布与更新。OpenAI 发布了 GPT-5.6 系列模型，包含旗舰版
  Sol、中端 Terra 和经济型 Luna，已在 ChatGPT、Codex 和 API 上线，同时推出了 ChatGPT Work 智能体和 GPT-Live
  语音产品。Meta Superintelligence Labs 发布了 Muse Spark 1.1 多模态推理模型，在 MCP Atlas 等智能体基准测试中取得
  SOTA 成绩，并首次向开发者开放了 Meta Model API。xAI 发布 Grok 4.5、Cognition 发布 SWE-1.7（推理速度 1000
  tok/s）、Mistral 发布 Robostral Navigate 等编码模型。Google 开源了 Gemma 4 模型，Tencent 开源了 295B
  参数的 Hy3 模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Meta
  - xAI
  - Cognition
  - Mistral
  - Google
  - Tencent
  - Nous Research
  - Microsoft
  - Ternlight
  - Databricks
  - FrontierFinance
  - Sakana AI
  - Anthropic
  technologies:
  - GPT-5.6
  - MCP
  - VLM
  key_people: []
key_logic_flow:
- OpenAI 发布了 GPT-5.6 系列模型，包含 Sol、Terra 和 Luna 三个能力层级，已在 ChatGPT、Codex 和 API 上线，Sol
  定价为输入/输出每百万 token 5/30 美元。
- Meta Superintelligence Labs 发布了 Muse Spark 1.1 多模态推理模型，支持原生工具、MCP 服务器和自定义技能，可作为主智能体规划并委派任务给并行子智能体。
- Muse Spark 1.1 在 MCP Atlas 基准上取得 88.1 的 SOTA 分数，支持 100 万 token 上下文窗口，Meta Model
  API 定价为每百万输入/输出 token 1.25/4.25 美元。
- OpenAI 推出了 ChatGPT Work 智能体产品和 GPT-Live 语音产品，进一步扩展了 AI 代理在工作和语音场景中的应用。
- xAI 发布 Grok 4.5 编码模型、Cognition 发布 SWE-1.7（推理速度 1000 tok/s）、Mistral 发布 Robostral
  Navigate，多家公司聚焦编码能力的 AI 模型。
- Google 开源了 Gemma 4 模型，Tencent 开源了 295B 参数的 Hy3 模型，Microsoft 发布了用于智能体的 Flint 框架。
extract_result: success
object_mentions:
- object_type: model
  name: GPT-5.6 family (Sol, Terra, Luna)
  canonical_name: GPT-5.6
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 开始推出 GPT-5.6 系列模型 Sol、Terra 和 Luna，覆盖 ChatGPT、Codex 和 API。
  - Sol 是旗舰型号，Terra 匹配 GPT-5.5 且成本更低，Luna 速度最快价格最低。
  - GPT-5.6 是 Codex 和 ChatGPT Work 的默认大脑，针对长时间工具使用和编码进行优化。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Muse Spark 1.1
  canonical_name: Muse Spark
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Meta Superintelligence Labs 发布了 Muse Spark 1.1 多模态推理模型，专为智能体任务设计。
  - Muse Spark 1.1 在 MCP Atlas（88.1）、JobBench（54.7）等基准测试中取得 SOTA 成绩。
  - 该模型支持 100 万 token 上下文窗口，适用于长时间多模态工作场景。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 推出了 ChatGPT Work 智能体，由 GPT-5.6 作为默认大脑驱动。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Meta Model API
  canonical_name: Meta Model API
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Meta 首次向开发者开放了 Meta Model API，目前处于公开预览阶段。
  - Meta Model API 定价为每百万输入/输出 token 1.25/4.25 美元，新账户可获 20 美元免费额度。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Grok 4.5
  canonical_name: Grok 4.5
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - xAI 发布了 Grok 4.5 模型，专注于提升编码能力。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: SWE-1.7
  canonical_name: SWE-1.7
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Cognition 发布了 SWE-1.7 模型，推理速度达到每秒 1000 个 token。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Robostral Navigate
  canonical_name: Robostral Navigate
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Mistral 发布了 Robostral Navigate 模型，作为新推出的 AI 产品之一。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: GPT-Live
  canonical_name: GPT-Live
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 推出了 GPT-Live 语音产品，扩展了 AI 语音交互能力。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Gemma 4
  canonical_name: Gemma 4
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Google 开源了 Gemma 4 模型，供开发者使用。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Hy3
  canonical_name: Hy3
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Tencent 开源了 295B 参数的 Hy3 模型。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Codex
  canonical_name: Codex
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - GPT-5.6 成为 Codex 的默认大脑，Codex 桌面应用将合并到 ChatGPT 的 Windows 和 Mac 应用中。
  article_id: 5d9bcda5ffff8971
- object_type: project
  name: Flint
  canonical_name: Flint
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Microsoft 发布了用于智能体的 Flint 框架和工具。
  article_id: 5d9bcda5ffff8971
- object_type: project
  name: Hermes Agent
  canonical_name: Hermes Agent
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Nous Research 将 Hermes Agent 部署到了云端。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Cloud Run sandboxes
  canonical_name: Cloud Run sandboxes
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Google 推出了 Cloud Run sandboxes 沙箱产品。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Ternlight
  canonical_name: Ternlight
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Ternlight 实现了在浏览器中运行嵌入向量计算的功能。
  article_id: 5d9bcda5ffff8971
---

# 🤖 AI Agents Weekly: GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7, Robostral Navigate, The Harness Effect, and More

### GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7, Robostral Navigate, The Harness Effect, and More

In today’s issue:

OpenAI ships the GPT-5.6 family

Meta releases Muse Spark 1.1

OpenAI launches ChatGPT Work agent

xAI releases Grok 4.5 for coding

Cognition ships SWE-1.7 at 1000 tok/s

Mistral drops Robostral Navigate

Harness design sets agent economics

OpenAI launches GPT-Live voice

Google open-sources Gemma 4

Tencent open-sources 295B Hy3

Google ships Cloud Run sandboxes

Nous puts Hermes Agent in the cloud

Microsoft releases Flint for agents

Ternlight runs embeddings in-browser

GPT-5.6 proves 50-year math conjecture

Databricks benchmarks coding agents

OpenAI audits SWE-Bench Pro

FrontierFinance benchmarks agent analysts

Paper turns memory into navigation

GitLost tricks GitHub’s AI agent

Anthropic finds a global workspace

Sakana replays Picbreeder with VLMs


And all the top AI dev news, papers, and tools.

## Top Stories

### OpenAI Ships the GPT-5.6 Family

OpenAI began rolling out its GPT-5.6 family, Sol, Terra, and Luna, across ChatGPT, Codex, and the API.

**Capability tiers:**The number marks the generation while Sol, Terra, and Luna are durable tiers that advance on their own cadence. Sol is the flagship for the hardest tasks, Terra matches GPT-5.5 at lower cost, and Luna is the fastest and cheapest.**Built for agents:**GPT-5.6 is the new default brain behind Codex and ChatGPT Work, tuned for long-horizon tool use and coding.**Pricing:**Sol runs 5 dollars/30 dollars per million input/output tokens, Terra 2.50 dollars/15 dollars, and Luna 1 dollar/6 dollars.**Rollout:**Live now in ChatGPT, Codex, and the API, with the Codex desktop app merging into the ChatGPT app on Windows and Mac.

### Meta Releases Muse Spark 1.1

Meta Superintelligence Labs released Muse Spark 1.1, a multimodal reasoning model built for agentic tasks, and opened the Meta Model API to developers for the first time.

**Agent orchestration:**Works with native tools, MCP servers, and custom skills, and can act as a main agent that plans and delegates work to parallel subagents.**Agentic benchmarks:**Posts SOTA scores on MCP Atlas (88.1), JobBench (54.7 vs Opus 4.8 at 48.4 and GPT-5.5 at 38.3), and Humanity’s Last Exam with tools (62.1 vs Opus 4.8 at 57.9), plus FinanceBench.**Long context:**Supports a 1M-token context window for long-horizon, multimodal work.**Open API and pricing:**Meta Model API is in public preview at 1.25 dollars/4.25 dollars per million input/output tokens, with 20 dollars in free credits for new accounts.