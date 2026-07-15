---
title: 'Akashic: A Low-Overhead LLM Inference Service with MemAttention'
source: https://arxiv.org/abs/2607.05708
author:
- '[[Yang Liu, Zhaokai Luo, Huayi Jin, Ruozhou He, Chenchen Hong, Zhiyong Wang, Yifei
  Liu, Yunfei Gu, Chentao Wu, Junhao Hu]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'arXiv:2607.05708v1 Announce Type: new Abstract: Recent LLM-based agent
  systems continuously accumulate context across multi-turn interactions, tool invocations,
  and cross-session workflows. Replaying the full history for every request quickly
  becomes impractical: long contexts increase prefill cost, may exceed context limits,
  and often bury task-relevant evidence in irrelevant content, degrading both serving
  efficiency and output quality. We propose Akashic, a low-overhead memory system
  built around MemAttention, which organizes context into bounded chunks and models
  semantic relationships across chunks, preserving cross-chunk evidence without repeatedly
  rewriting the full history. Akashic further applies hardware-software co-designed
  memory placement to co-locate likely co-retrieved chunks, reducing retrieval fragmentation
  and I/O overhead. Across four representative workloads and three model sizes, Akashic
  improves task accuracy by up to 10.2 points, throughput by up to 1.21x, and sustainable
  request rate by up to 1.88x over strong prior memory baselines.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 17a9ddeb56fced8a
manifest_dates:
- '2026-07-08'
source_type: academic_paper
tldr: Akashic 通过 MemAttention 将上下文分块并建模语义关联，提升 LLM 推理效率。
objective_summary: 针对 LLM agent 系统多轮交互中全量历史回放导致的预填充开销大、上下文超限等问题，研究者提出 Akashic，一种基于
  MemAttention 的低开销记忆系统。MemAttention 将上下文组织为有界分块并建模跨块语义关系，配合软硬件协同的内存放置策略，减少检索碎片和 I/O
  开销。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - MemAttention
  - LLM
  key_people: []
key_logic_flow:
- LLM agent 系统在多轮交互、工具调用和跨会话工作流中持续累积上下文，全量回放历史导致预填充成本高、可能超限、无关内容淹没有效证据。
- Akashic 的核心组件 MemAttention 将上下文组织为有界分块，并对跨分块的语义关系进行建模，无需重复写入完整历史即可保留跨块证据。
- Akashic 应用软硬件协同设计的记忆放置策略，将可能同时检索的分块就近放置，减少检索碎片和 I/O 开销。
- 在四种代表性工作负载和三种模型规模上，Akashic 相比强基线方法在任务准确率上提升最高 10.2 个百分点。
- 吞吐量最高提升 1.21 倍，可持续请求率最高提升 1.88 倍。
specialized_tags:
  paper:
    paperTitle: 'Akashic: A Low-Overhead LLM Inference Service with MemAttention'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Systems
    methodType: LLM-based
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Akashic: A Low-Overhead LLM Inference Service with MemAttention

View PDF HTML (experimental)Abstract:Recent LLM-based agent systems continuously accumulate context across multi-turn interactions, tool invocations, and cross-session workflows. Replaying the full history for every request quickly becomes impractical: long contexts increase prefill cost, may exceed context limits, and often bury task-relevant evidence in irrelevant content, degrading both serving efficiency and output quality. We propose Akashic, a low-overhead memory system built around MemAttention, which organizes context into bounded chunks and models semantic relationships across chunks, preserving cross-chunk evidence without repeatedly rewriting the full history. Akashic further applies hardware-software co-designed memory placement to co-locate likely co-retrieved chunks, reducing retrieval fragmentation and I/O overhead. Across four representative workloads and three model sizes, Akashic improves task accuracy by up to 10.2 points, throughput by up to 1.21x, and sustainable request rate by up to 1.88x over strong prior memory baselines.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.