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
pipeline_stage: ingested
id: e1eaa68bad5a6ab6
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