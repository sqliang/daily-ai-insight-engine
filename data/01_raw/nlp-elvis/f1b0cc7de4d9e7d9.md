---
title: '🤖 AI Agents Weekly: DeepSeek Harness, DeepSeek-V4-Pro, Grok Bot, GLM-5.3,
  Gemini 3.7 Flash, Muse Glimmer, Harness Evolution Papers, and More'
source: https://nlp.elvissaravia.com/p/ai-agents-weekly-deepseek-harness
author: []
published: '2026-08-15'
created: '2026-08-16'
manifest_dates:
- '2026-08-16'
- '2026-08-17'
- '2026-08-18'
- '2026-08-19'
- '2026-08-20'
- '2026-08-22'
description: DeepSeek Harness, DeepSeek-V4-Pro, Grok Bot, GLM-5.3, Gemini 3.7 Flash,
  Muse Glimmer, Harness Evolution Papers, and More
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: f1b0cc7de4d9e7d9
---

# 🤖 AI Agents Weekly: DeepSeek Harness, DeepSeek-V4-Pro, Grok Bot, GLM-5.3, Gemini 3.7 Flash, Muse Glimmer, Harness Evolution Papers, and More

### DeepSeek Harness, DeepSeek-V4-Pro, Grok Bot, GLM-5.3, Gemini 3.7 Flash, Muse Glimmer, Harness Evolution Papers, and More

In today’s issue:

DeepSeek open-sources its agent harness

DeepSeek-V4-Pro ships agent upgrades

xAI launches Grok Bot teammates

Z.ai drops GLM-5.3 for coding

Gemini 3.7 Flash halves coding cost

Meta open-sources Muse Glimmer

Grok 4.6 hits frontier at half price

Zed launches Delta for agent teams

Evo-Bench measures harness evolution

Study finds 91.8% of skills defective


And all the top AI dev news, papers, and tools.

## Top Stories

### DeepSeek Open-Sources Its Agent Harness

DeepSeek released DeepSeek Harness v0.1 as a developer preview, open-sourcing the codebase under MIT and opening it to anyone building agent harnesses.

**Everything is a plugin:**The harness is built on the Cordis meta-framework, a kernel that mounts, unmounts, and resolves dependencies for models, tools, skills, sessions, sandboxes, storage, loops, scheduling, and UI as independent plugins.**Append-only session log:**Everything the model sees is recorded, so sessions can be resumed, forked, searched, and replayed rather than reconstructed from chat history.**Four runtime modes:**Standard ships the full toolset, Code orchestrates operations through TypeScript, Minimal strips down for benchmark runs, and Creator is for building custom presets.**Install path:**Runs via`npx @deepseek-ai/dsh web`

or from source, and the repo has already cleared 93,000 stars.

### DeepSeek Launches V4-Pro

DeepSeek shipped V4-Pro-0813, a general availability release centered almost entirely on agent workloads.

**Agentic benchmarks:**87.9 on Terminal Bench 2.1, 62.7 on DeepSWE, 74.1 on Toolathlon-Verified, 83.3 on CyberGym, and 31.8 on public AutomationBench, tested through DeepSeek Harness in minimal mode.**Flexible reasoning effort:**Low, high, and max tiers across V4-Pro and V4-Flash let you dial spend per task instead of paying reasoning cost on trivial calls.**Native Responses API:**Ships OpenAI Responses API support with one-click Codex setup, and model names stay unchanged so existing integrations keep working.**Peak and off-peak pricing:**New API rates take effect August 16, with off-peak rates 50% below peak for schedulable batch and agent workloads.