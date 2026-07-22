---
title: 'APeB: Benchmarking Personalization Ability of Large Language Model Agents'
source: https://arxiv.org/abs/2607.03162
author:
- '[[Garry Yang, Zizhe Chen, Xinru Chen, Yongqiang Chen, Jianxiang Wang, Deyu Zou,
  Linyi Ding, Jialiang Wu, Yunzhong He, Yu Gong, James Cheng, Huaixiao Tou]]'
published: '2026-07-07'
created: '2026-07-07'
description: 'arXiv:2607.03162v1 Announce Type: new Abstract: LLM-powered agents struggle
  with personalization when users issue raw, underspecified queries. In this setting,
  agents must infer latent intent, extract preferences from noisy interaction histories,
  and select among competing alternatives. Existing benchmarks rarely test this capability,
  as they often rely on user-refined queries or simplified histories. We introduce
  personalized product search (PPS), a testbed for agentic personalization under raw
  queries and diverse histories. We construct Agent Personalized Benchmark (APeB)
  from action logs, pairing underspecified intents with rich histories and user-viewed
  candidate items. Evaluating state-of-the-art LLMs with multi-step agent workflows,
  we find that models handle explicit queries well but struggle with early-stage queries
  requiring intent and preference discovery. Rubric analysis attributes this gap mainly
  to ineffective history use. A simple history-aware query-refinement pipeline, VQRA,
  yields consistent gains, highlighting the need for dedicated history-utilization
  modules in personalized agents.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 26f0d76bfefb7a6a
manifest_dates:
- '2026-07-07'
source_type: academic_paper
tldr: APeB 是从行动日志构建的基准测试，用于评估大语言模型代理在原始不完整查询下的个性化能力。研究发现现有模型在处理需要意图发现和偏好推断的查询时表现不佳，主要原因是未能有效利用用户历史信息。
objective_summary: 研究人员针对大语言模型代理在原始不完整查询下的个性化能力不足问题，引入个性化产品搜索（PPS）作为测试平台，并从行动日志中构建了
  Agent Personalized Benchmark（APeB）。该基准将不完整意图与丰富历史记录及候选物品配对，评估了多步代理工作流下的多个前沿大语言模型。结果发现模型在显式查询上表现良好，但在早期查询中因历史信息利用不充分而效果不佳；提出的
  VQRA 查询优化管线取得了一致性性能提升。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM
  - PPS
  - VQRA
  key_people: []
key_logic_flow:
- 现有基准测试很少评估大语言模型代理在原始不完整查询下的个性化能力，代理需要推断隐式意图、从噪声交互历史中提取偏好并在竞争选项中做出选择。
- 研究引入个性化产品搜索（PPS）作为测试平台，并从行动日志构建了 Agent Personalized Benchmark（APeB），将不完整意图与丰富历史记录及用户已浏览的候选物品配对。
- 评估发现当前模型在处理显式查询时表现良好，但在需要意图发现和偏好推断的早期阶段查询中表现不佳。
- 评分分析将性能差距主要归因于代理对历史信息的低效利用，而非推理能力不足。
- 论文提出的历史感知查询优化管线 VQRA 通过简单的查询精炼方法在实验中取得了一致性的性能提升。
- 研究结果表明个性化代理需要设计专用的历史信息利用模块来提升其在原始查询场景下的表现。
specialized_tags:
  paper:
    paperTitle: 'APeB: Benchmarking Personalization Ability of Large Language Model
      Agents'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: NLP
    methodType: benchmark
extract_result: success
object_mentions:
- object_type: project
  name: APeB
  canonical_name: Agent Personalized Benchmark
  url: https://arxiv.org/abs/2607.03162
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文从行动日志中构建了 Agent Personalized Benchmark（APeB），用于评估大语言模型代理在原始查询条件下的个性化能力。
  - APeB 将不完整意图与丰富历史记录及用户已浏览候选物品配对，填补了现有基准在代理个性化评估方面的空白。
  article_id: 26f0d76bfefb7a6a
- object_type: project
  name: PPS
  canonical_name: Personalized Product Search
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 研究引入了个性化产品搜索（Personalized Product Search, PPS）作为测试平台，用于在原始查询和多样化历史记录下测试代理的个性化能力。
  article_id: 26f0d76bfefb7a6a
- object_type: project
  name: VQRA
  canonical_name: VQRA
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 论文提出的历史感知查询优化管线 VQRA 通过简单的查询精炼方法在实验中取得了一致性的性能提升。
  - VQRA 的效果表明个性化代理需要设计专用的历史信息利用模块来提升其在原始查询场景下的表现。
  article_id: 26f0d76bfefb7a6a
---

# Computer Science > Artificial Intelligence

# Title:APeB: Benchmarking Personalization Ability of Large Language Model Agents

View PDF HTML (experimental)Abstract:LLM-powered agents struggle with personalization when users issue raw, underspecified queries. In this setting, agents must infer latent intent, extract preferences from noisy interaction histories, and select among competing alternatives. Existing benchmarks rarely test this capability, as they often rely on user-refined queries or simplified histories. We introduce personalized product search (PPS), a testbed for agentic personalization under raw queries and diverse histories. We construct Agent Personalized Benchmark (APeB) from action logs, pairing underspecified intents with rich histories and user-viewed candidate items. Evaluating state-of-the-art LLMs with multi-step agent workflows, we find that models handle explicit queries well but struggle with early-stage queries requiring intent and preference discovery. Rubric analysis attributes this gap mainly to ineffective history use. A simple history-aware query-refinement pipeline, VQRA, yields consistent gains, highlighting the need for dedicated history-utilization modules in personalized agents.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.