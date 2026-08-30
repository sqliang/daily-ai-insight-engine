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
pipeline_stage: fact_extracted
id: f1b0cc7de4d9e7d9
source_type: newsletter_rss
tldr: DeepSeek 以 MIT 许可证开源智能体框架 DeepSeek Harness v0.1，并发布主打智能体工作负载的 V4-Pro-0813 正式版；本期周刊还涵盖
  Grok Bot、GLM-5.3、Gemini 3.7 Flash、Muse Glimmer 等多项发布。
objective_summary: DeepSeek 发布 DeepSeek Harness v0.1 开发者预览版，基于 Cordis 元框架将模型、工具、会话等作为独立插件挂载，提供四种运行时模式与可恢复的追加式会话日志。同时
  DeepSeek 推出 V4-Pro-0813 正式版，专注智能体工作负载，在 Terminal Bench 2.1 等智能体基准上表现突出，并支持 OpenAI
  Responses API 与分档推理力度。新 API 价格自 8 月 16 日生效，非高峰时段费率比高峰时段低 50%。此外 xAI、Z.ai、Meta、Zed
  等多家公司也在本周发布各自的新产品。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - DeepSeek
  - xAI
  - Z.ai
  - Meta
  - Zed
  technologies:
  - Cordis meta-framework
  - OpenAI Responses API
  - Terminal Bench
  - DeepSWE
  - Toolathlon
  - CyberGym
  - AutomationBench
  - TypeScript
  key_people: []
key_logic_flow:
- DeepSeek 开源了其智能体框架 DeepSeek Harness v0.1，采用 MIT 许可证，面向所有构建智能体 harness 的开发者开放。
- DeepSeek Harness 基于 Cordis 元框架构建，将模型、工具、技能、会话、沙箱、存储、循环、调度和 UI 作为独立插件进行挂载、卸载与依赖解析。
- DeepSeek Harness 采用追加式会话日志，模型看到的所有内容都会被记录，会话可以恢复、分叉、搜索和重放。
- DeepSeek 发布 V4-Pro-0813 正式版，重点面向智能体工作负载，在 Terminal Bench 2.1 上取得 87.9 分，在 DeepSWE
  上取得 62.7 分。
- V4-Pro 与 V4-Flash 提供低、高、最大三档推理力度调节，并原生支持 OpenAI Responses API 与一键 Codex 配置，模型名称保持不变。
- 新 API 价格自 8 月 16 日生效，非高峰时段费率比高峰时段低 50%，适用于可调度的批处理和智能体工作负载。
object_mentions:
- object_type: project
  name: DeepSeek Harness
  canonical_name: DeepSeek Harness
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - DeepSeek 以 MIT 许可证开源了智能体框架 DeepSeek Harness v0.1，面向所有构建智能体 harness 的开发者开放，仓库已超过
    9.3 万星。
  - 该框架基于 Cordis 元框架构建，将模型、工具、技能、会话、沙箱、存储、循环、调度和 UI 作为独立插件进行挂载与依赖解析。
  - 框架提供标准、代码、极简和创建者四种运行时模式，并可通过 npx @deepseek-ai/dsh web 命令或从源码安装运行。
  article_id: f1b0cc7de4d9e7d9
- object_type: model
  name: DeepSeek-V4-Pro-0813
  canonical_name: DeepSeek V4-Pro
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - DeepSeek 发布 V4-Pro-0813 正式版，作为几乎完全面向智能体工作负载的通用可用版本，通过 DeepSeek Harness 极简模式完成基准测试。
  - V4-Pro 在 Terminal Bench 2.1 上取得 87.9 分，在 DeepSWE 上取得 62.7 分，在 Toolathlon-Verified
    上取得 74.1 分。
  - V4-Pro 原生支持 OpenAI Responses API 与一键 Codex 配置，且模型名称保持不变，现有集成可继续工作。
  article_id: f1b0cc7de4d9e7d9
- object_type: project
  name: Cordis meta-framework
  canonical_name: Cordis
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - DeepSeek Harness 建立在 Cordis 元框架之上，该内核为模型、工具、技能、会话、沙箱、存储等组件提供挂载、卸载与依赖解析能力。
  article_id: f1b0cc7de4d9e7d9
- object_type: model
  name: DeepSeek-V4-Flash
  canonical_name: DeepSeek V4-Flash
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - V4-Pro 与 V4-Flash 都提供低、高、最大三档推理力度调节，开发者可以按任务控制推理成本而无需为简单调用支付过高费用。
  article_id: f1b0cc7de4d9e7d9
- object_type: product
  name: Grok Bot
  canonical_name: Grok Bot
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - xAI 推出 Grok Bot 团队协作者，该消息仅在本期周刊的今日要闻标题中列出，文章未提供更多细节。
  article_id: f1b0cc7de4d9e7d9
- object_type: model
  name: GLM-5.3
  canonical_name: GLM-5.3
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Z.ai 发布了面向编码场景的 GLM-5.3，该消息仅在本期周刊的今日要闻标题中提及，未提供具体细节。
  article_id: f1b0cc7de4d9e7d9
- object_type: model
  name: Gemini 3.7 Flash
  canonical_name: Gemini 3.7 Flash
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Gemini 3.7 Flash 将编码成本减半，该消息仅在本期周刊的今日要闻标题中提及，未提供具体细节。
  article_id: f1b0cc7de4d9e7d9
- object_type: model
  name: Muse Glimmer
  canonical_name: Muse Glimmer
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Meta 开源了 Muse Glimmer，该消息仅在本期周刊的今日要闻标题中提及，未提供更多细节。
  article_id: f1b0cc7de4d9e7d9
- object_type: model
  name: Grok 4.6
  canonical_name: Grok 4.6
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Grok 4.6 以半价达到前沿水平，该消息仅在本期周刊的今日要闻标题中提及，未提供更多细节。
  article_id: f1b0cc7de4d9e7d9
- object_type: product
  name: Zed Delta
  canonical_name: Zed Delta
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Zed 推出了面向智能体团队的 Delta，该消息仅在本期周刊的今日要闻标题中提及，未提供更多细节。
  article_id: f1b0cc7de4d9e7d9
- object_type: project
  name: Evo-Bench
  canonical_name: Evo-Bench
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Evo-Bench 用于衡量智能体 harness 的演进，该消息仅在本期周刊的今日要闻标题中提及，未提供更多细节。
  article_id: f1b0cc7de4d9e7d9
extract_result: success
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