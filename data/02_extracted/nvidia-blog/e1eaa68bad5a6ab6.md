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
tldr: NVIDIA 推理软件栈在 Blackwell 上将 DeepSeek V4 token 成本降低 5 倍
objective_summary: NVIDIA 官方博客介绍了其推理软件栈如何通过 TensorRT-LLM、Dynamo 等框架与 Blackwell GPU
  协同设计，在一月内将 DeepSeek V4 token 成本降低 5 倍。Baseten、Cognition、Deep Infra、Together AI
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
  - Blackwell
  key_people: []
key_logic_flow:
- 企业 AI 基础设施决策标准已从芯片峰值规格转向每 token 成本（每美元、每瓦特可产出的有用 token 数量）。
- NVIDIA 推理软件栈与其 GPU、CPU、网络和系统协同设计，并依托开源生态持续提升硬件性能。
- 在 Blackwell 平台上，NVIDIA 的软件堆栈仅一个月就将 DeepSeek V4 模型的 token 成本降低了 5 倍。
- Baseten 使用 TensorRT-LLM 在 Blackwell GPU 上服务 DeepSeek V4 Pro，通过专有运行时优化实现每秒 token
  数提升高达 50%。
- Cognition 使用 NVIDIA Dynamo 推理框架管理推理 GPU，无需自建基础设施即可扩展强化学习工作负载。
- DigitalOcean 帮助 Hippocratic AI 在 Blackwell GPU 上使用 NVIDIA 推理软件，将医疗 AI 推理吞吐量提升 30%
  并保持亚秒级首次响应时间。
extract_result: success
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