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
tldr: APeB 是评估LLM代理个性化能力的基准测试框架
objective_summary: 研究人员提出了 APeB（Agent Personalized Benchmark），基于个性化产品搜索场景，用于评估大语言模型代理在用户原始不明确查询下的个性化能力。实验发现主流LLM处理明确查询表现良好，但在需要意图和偏好发现的早期查询阶段表现不佳，主要原因是未能有效利用历史交互信息。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - APeB
  - VQRA
  key_people: []
key_logic_flow:
- 现有基准测试很少评估LLM代理在用户原始不明确查询下的个性化能力，通常依赖用户精炼后的查询或简化历史
- APeB基准基于个性化产品搜索构建，包含不明确意图、丰富交互历史和候选项目数据，用于测试代理的意图推断和偏好提取能力
- 评估发现主流LLM在处理明确查询时表现良好，但在需推断潜在意图和发现偏好的早期阶段查询上表现不佳
- Rubric归因分析表明模型表现差距主要源于未能有效利用用户交互历史信息
- 提出的VQRA（历史感知查询精炼管线）通过显式利用历史信息，在个性化任务上获得了一致性的性能提升
- 该研究揭示了专用历史利用模块对个性化代理系统的必要性
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