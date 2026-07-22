---
title: How NVIDIA’s Inference Software Stack Powers the Lowest Token Cost
source: https://blogs.nvidia.com/blog/inference-software-lowest-token-cost/
author:
- '[[Amr Elmeleegy]]'
published: '2026-06-30'
created: '2026-07-01'
description: 'As organizations move from AI pilots to production AI factories, infrastructure
  decisions have shifted from peak chip specifications to cost per token: how many
  useful tokens they can deliver per dollar, per watt and within required latency
  targets. Codesigned with NVIDIA GPUs, CPUs, networking and systems, and strengthened
  by a broad open source ecosystem, NVIDIA’s [&#8230;]'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e1eaa68bad5a6ab6
manifest_dates:
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
source_type: tech_blog
tldr: NVIDIA 官方博客称其全栈推理软件与 Blackwell GPU 协同设计，一个月内将 DeepSeek V4 的令牌成本降低最多 5 倍。Baseten、Cognition、Deep
  Infra 等多家公司已通过 TensorRT-LLM 和 Dynamo 等组件在 Blackwell 上获得显著的推理性能提升。
objective_summary: NVIDIA 于官方博客发布其推理软件栈技术介绍，宣称该软件栈与 Blackwell GPU 协同设计，一个月内将 DeepSeek
  V4 模型的令牌成本降低最多 5 倍。Baseten 使用 TensorRT-LLM 在 Blackwell 上服务 DeepSeek V4 Pro，实现最高
  50% 的每秒令牌数提升；Cognition 使用 NVIDIA Dynamo 框架管理推理 GPU 以支持强化学习工作负载；Deep Infra 利用该软件栈从第一天起在
  Blackwell 上运行前沿开源模型；DigitalOcean 帮助 Hippocratic AI 将推理吞吐量提升 30%，在 1000 万次患者通话中保持亚半秒首响应时间；Together
  AI 使用 TensorRT-LLM 帮助 Cursor 加速模型到生产端点的路径。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - Baseten
  - Cognition
  - Deep Infra
  - DigitalOcean
  - Hippocratic AI
  - Together AI
  - Cursor
  technologies:
  - TensorRT-LLM
  - NVIDIA Dynamo
  - DeepSeek V4
  - Blackwell
  key_people: []
key_logic_flow:
- NVIDIA 宣称其全栈推理软件与 Blackwell GPU 协同设计，一个月内将 DeepSeek V4 模型的令牌成本降低最多 5 倍。
- Baseten 使用 NVIDIA TensorRT-LLM 开源库在 Blackwell GPU 上服务 DeepSeek V4 Pro，结合专有运行时优化实现了最高
  50% 的每秒令牌数提升。
- Cognition 使用 NVIDIA Dynamo 推理框架管理推理 GPU，为其强化学习工作负载提供了无需自建基础设施的现成扩展路径。
- Deep Infra 利用 NVIDIA 推理软件栈从第一天起就在 Blackwell 上高效运行包括 DeepSeek V4 在内的前沿开源模型。
- DigitalOcean 帮助 Hippocratic AI 在 Blackwell GPU 上优化医疗 AI 推理，吞吐量提升 30%，在 1000 万次患者通话中保持亚半秒的首响应时间。
- Together AI 使用 NVIDIA TensorRT-LLM 在 Blackwell 上帮助 Cursor 加速从模型优化到生产推理端点的全流程。
extract_result: success
object_mentions:
- object_type: project
  name: NVIDIA TensorRT-LLM
  canonical_name: TensorRT-LLM
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Baseten 使用 NVIDIA TensorRT-LLM 开源库在 Blackwell GPU 上服务 DeepSeek V4 Pro，结合专有运行时优化实现了最高
    50% 的每秒令牌数提升。
  - Together AI 使用 NVIDIA TensorRT-LLM 在 Blackwell 上帮助 Cursor 加速从模型优化到生产推理端点的路径。
  article_id: e1eaa68bad5a6ab6
- object_type: project
  name: NVIDIA Dynamo
  canonical_name: NVIDIA Dynamo
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cognition 使用 NVIDIA Dynamo 推理框架管理推理 GPU，为其强化学习工作负载提供了无需自建基础设施的现成扩展路径。
  article_id: e1eaa68bad5a6ab6
- object_type: model
  name: DeepSeek V4
  canonical_name: DeepSeek V4
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - NVIDIA 宣称其推理软件栈在 Blackwell 平台上一个月内将 DeepSeek V4 模型的令牌成本降低最多 5 倍。
  - Deep Infra 利用 NVIDIA 推理软件栈从第一天起就在 Blackwell 上高效运行包括 DeepSeek V4 在内的前沿开源模型。
  article_id: e1eaa68bad5a6ab6
- object_type: product
  name: Cursor
  canonical_name: Cursor
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Together AI 使用 NVIDIA TensorRT-LLM 在 Blackwell 上帮助 Cursor 加速从模型优化到生产端点的路径，为其实时编程体验提供支持。
  article_id: e1eaa68bad5a6ab6
---

As organizations move from AI pilots to production AI factories, infrastructure decisions have shifted from peak chip specifications to cost per token: how many useful tokens they can deliver per dollar, per watt and within required latency targets.

Codesigned with NVIDIA GPUs, CPUs, networking and systems, and strengthened by a broad open source ecosystem, NVIDIA’s full-stack inference software continuously improves hardware performance. On the NVIDIA Blackwell platform, the software stack has already reduced token costs by up to 5x on the DeepSeek V4 model in just one month.

Leading companies and inference providers are already seeing the compounding value of NVIDIA’s inference software stack on Blackwell:

- Baseten used the NVIDIA TensorRT-LLM open source library to serve DeepSeek V4 Pro on Blackwell GPUs for reasoning, coding and long-context workloads, applying proprietary runtime optimizations to deliver up to 50% more tokens per second.
- Cognition is using the NVIDIA Dynamo inference framework to manage inference GPUs, giving its team a ready-made path to scale reinforcement learning workloads without needing to build that infrastructure from scratch.
- Deep Infra uses the NVIDIA inference software stack to serve frontier open source models performantly on Blackwell from day zero, including DeepSeek V4.
- DigitalOcean helped Hippocratic AI use NVIDIA inference software on Blackwell GPUs to serve healthcare AI faster and more efficiently, increasing inference throughput by 30% while maintaining a sub-half-second time to first response across 10 million patient calls.
- Together AI used NVIDIA TensorRT-LLM on Blackwell to help Cursor accelerate the path from model optimizations to production endpoints for its real-time coding experience.

**Why Software Matters for Inference Economics**

Traditional web, search and software-as-a-service workloads were relatively predictable: A user might load a page, refresh a feed or update a business record. These requests typically followed similar software paths, reading from or writing to a database, and scaled by adding more of the same servers.

Agentic AI is different.

Agents can reason, plan, call tools, spin up specialist subagents and manage massive context across multi-turn workflows. They turn a single request into a distributed computing problem that can span hundreds of subagents, thousands of tasks and multiple large language models, running across GPUs, CPUs, DPUs and storage systems.

The software stack determines whether that complexity turns into wasted capacity or lower cost per token.

Lower cost per token comes from turning individual optimizations into system-level performance. NVIDIA’s inference software stack does this by connecting three layers: