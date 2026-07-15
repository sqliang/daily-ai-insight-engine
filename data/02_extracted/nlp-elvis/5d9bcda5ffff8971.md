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
tldr: OpenAI发布GPT-5.6系列模型，Meta发布Muse Spark 1.1多模态推理模型并开放API。
objective_summary: OpenAI于2026年7月推出GPT-5.6系列（Sol、Terra、Luna），按能力层级定价并集成至ChatGPT、Codex和API。Meta同步发布Muse
  Spark 1.1多模态推理模型，首次向开发者开放Meta Model API，在多项Agent基准测试中取得SOTA成绩。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Meta
  technologies:
  - GPT-5.6
  - Sol
  - Terra
  - Luna
  - Muse Spark 1.1
  - MCP
  - Meta Model API
  key_people: []
key_logic_flow:
- OpenAI开始推出GPT-5.6系列模型，包含Sol、Terra、Luna三个能力层级，Sol面向最困难任务，Terra匹配GPT-5.5性能成本更低，Luna最快最便宜。
- GPT-5.6系列专为智能体任务优化，定价为Sol每百万输入/输出Token 5/30美元，Terra为2.50/15美元，Luna为1/6美元，已集成至ChatGPT、Codex和API。
- Meta发布Muse Spark 1.1多模态推理模型，支持原生工具、MCP服务器和自定义技能，可作为主智能体规划并委派任务给并行子智能体。
- Muse Spark 1.1在MCP Atlas（88.1）、JobBench（54.7）和Humanity's Last Exam with tools（62.1）等基准测试中取得SOTA成绩，支持100万Token上下文窗口。
- Meta首次向开发者开放Meta Model API，处于公开预览阶段，定价为每百万输入/输出Token 1.25/4.25美元，新账户提供20美元免费额度。
extract_result: success
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