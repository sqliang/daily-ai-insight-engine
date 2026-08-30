---
title: 'A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing'
source: https://arxiv.org/abs/2608.13573
author:
- '[[William Nixon, Jon Durbin, Florian Standhartinger, Haryadi S. Gunawi, Juncheng
  Yang]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: 'arXiv:2608.13573v1 Announce Type: new Abstract: Large Language Model
  (LLM) serving has become a critical cloud workload, and realistic traces are essential
  for motivating and benchmarking serving systems. However, existing LLM serving workload
  studies remain limited in scale and scope. They often observe short time periods
  and provide limited visibility into how users interact with models in production.
  As a result, they do not fully capture how LLM serving workloads evolve over time
  or how user-model interactions shape production traffic. In this work, we further
  the understanding of real-world LLM serving workloads through both a global characterization
  and a longitudinal study of a one-year production trace from Chutes. Unlike prior
  studies, our trace captures full production behavior across many models and users,
  including both popular and long-tail models. We analyze the workload from aggregate,
  temporal, model-level, and user-level perspectives, revealing workload evolution
  and user-model structure that are typically hidden behind aggregate views. To support
  future research, we will release the full one-year trace with the paper, enabling
  downstream studies of production behavior without relying on sampled or synthetically
  generated workloads.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6df4b4be97cf4ca6
source_type: academic_paper
tldr: 一篇 arXiv 论文对 Chutes 平台一年期 LLM serving 生产 trace 做全局特征刻画与纵向研究，从聚合、时间、模型级和用户级四个视角揭示工作负载演化，并计划随论文发布完整
  trace 数据。
objective_summary: 该论文以 Chutes 平台一年期生产 trace 为研究对象，对真实 LLM serving 工作负载进行全局特征刻画与纵向研究。该
  trace 覆盖多模型多用户的完整生产行为，包含流行模型与长尾模型。作者从聚合、时间、模型级和用户级四个视角分析工作负载的演化规律与用户-模型结构，并宣布将随论文发布完整的一年期
  trace，使下游研究无需依赖采样或合成工作负载。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies:
  - Chutes
  technologies:
  - LLM serving
  - LLM
  key_people: []
key_logic_flow:
- 现有 LLM serving 工作负载研究在规模和范围上有限，多只观察短时段，对生产环境中用户与模型的交互方式可见性不足。
- 本文基于 Chutes 平台的一年期生产 trace 进行全局特征刻画与纵向研究，突破了以往研究的尺度限制。
- 该 trace 记录了多个模型和用户的生产行为，既涵盖流行模型也包含长尾模型。
- 研究从聚合、时间、模型级和用户级四个视角分析工作负载，揭示通常被聚合视图隐藏的演化规律与用户-模型结构。
- 作者将随论文发布完整的一年期 trace，支持后续无需依赖采样或合成数据的生产行为研究。
object_mentions:
- object_type: paper
  name: 'A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing'
  canonical_name: 'A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing'
  url: https://arxiv.org/abs/2608.13573
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文对 Chutes 平台一年期生产 trace 进行全局特征刻画与纵向研究，并计划随论文发布完整的一年期 trace 数据。
  article_id: 6df4b4be97cf4ca6
- object_type: dataset
  name: Chutes one-year production trace
  canonical_name: Chutes one-year LLM serving production trace
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 该 trace 覆盖多个模型和用户的完整生产行为，包括流行模型与长尾模型，作者将随论文发布完整数据。
  article_id: 6df4b4be97cf4ca6
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing

View PDFAbstract:Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems. However, existing LLM serving workload studies remain limited in scale and scope. They often observe short time periods and provide limited visibility into how users interact with models in production. As a result, they do not fully capture how LLM serving workloads evolve over time or how user-model interactions shape production traffic.

In this work, we further the understanding of real-world LLM serving workloads through both a global characterization and a longitudinal study of a one-year production trace from Chutes. Unlike prior studies, our trace captures full production behavior across many models and users, including both popular and long-tail models. We analyze the workload from aggregate, temporal, model-level, and user-level perspectives, revealing workload evolution and user-model structure that are typically hidden behind aggregate views. To support future research, we will release the full one-year trace with the paper, enabling downstream studies of production behavior without relying on sampled or synthetically generated workloads.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.