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
tldr: Akashic 提出基于 MemAttention 的低开销 LLM 推理内存系统，将上下文分块并建模语义关系以避免完整历史重放，在四个工作负载上准确率提升最高
  10.2 个百分点，吞吐量提升最高 1.21 倍。
objective_summary: arXiv 论文提出 Akashic，一个围绕 MemAttention 构建的低开销 LLM 推理内存系统。MemAttention
  将上下文组织为有界块并建模跨块的语义关系，无需为每次请求重写完整历史。Akashic 还采用硬件-软件协同设计的内存放置策略，将可能同时检索的块放在邻近位置以减少
  I/O 开销。在四个代表性工作负载和三种模型尺寸上的实验表明：相比已有强基线方案，Akashic 的任务准确率提升最高 10.2 个百分点，吞吐量提升最高 1.21
  倍，可持续请求率提升最高 1.88 倍。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - MemAttention
  - LLM Inference
  - Hardware-Software Co-Design
  - Memory System
  key_people: []
key_logic_flow:
- Akashic 提出了 MemAttention 机制，将上下文组织为有界块并建模跨块的语义关系，解决了长上下文累积带来的预填充成本和上下文超限问题。
- Akashic 采用硬件-软件协同设计的内存放置策略，将可能同时检索的块部署在邻近位置，从而减少检索碎片和 I/O 开销。
- 在四个代表性工作负载（多轮交互、工具调用、跨会话工作流等）和三种模型尺寸上的评测中，Akashic 相比强基线方案任务准确率提升最高 10.2 个百分点。
- Akashic 的系统吞吐量相比基线提升最高 1.21 倍，可持续请求率提升最高 1.88 倍。
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
object_mentions:
- object_type: project
  name: Akashic
  canonical_name: Akashic
  url: https://arxiv.org/abs/2607.05708
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Akashic 是一种低开销的 LLM 推理服务内存系统，围绕 MemAttention 构建，旨在解决多轮交互和工具调用中完整历史重放导致的效率问题。
  - Akashic 在四个代表性工作负载和三种模型尺寸上相比强基线方案提高了任务准确率、吞吐量和可持续请求率。
  - Akashic 应用硬件-软件协同设计的内存放置策略来聚合可能同时检索的上下文块，减少 I/O 碎片和检索开销。
  article_id: 17a9ddeb56fced8a
- object_type: project
  name: MemAttention
  canonical_name: MemAttention
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - MemAttention 是 Akashic 的核心内存机制，将上下文组织为有界块并建模跨块之间的语义关系，保留跨块证据。
  - 通过 MemAttention，系统无需为每次请求重复重写完整历史，从而显著降低预填充成本和上下文超限风险。
  article_id: 17a9ddeb56fced8a
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