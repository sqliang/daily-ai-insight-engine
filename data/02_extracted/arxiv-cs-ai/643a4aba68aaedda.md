---
title: 'Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware Agricultural
  Advisory Generation'
source: https://arxiv.org/abs/2607.00454
author:
- '[[Vedant Balasubramaniam, Geetha Charan, Manojkumar Patil, Rohit P Suresh, V Priyanka,
  Kodur Sai Vinay Sathvik, Y. Narahari]]'
published: '2026-07-02'
created: '2026-07-02'
description: 'arXiv:2607.00454v1 Announce Type: new Abstract: Agricultural advisory
  systems face a fundamental tension: static agronomic guidelines offer consistent,
  evidence-based recommendations, yet remain blind to in-season variability and dynamic
  uncertainties. Recent advisory systems powered by LLMs are liable for a different
  risk of generating recommendations that are agronomically credible but physiologically
  unconvincing. Agri-SAGE is a closed-loop framework designed to resolve the above
  two limitations by integrating retrieval-grounded multi-agent LLM reasoning with
  APSIM-based biophysical simulation, to generate and validate agronomic advisories.
  To assess this framework, we evaluate three reasoning approaches, namely Plan-and-Solve,
  Tree of Thoughts, and Reflexion, over a 10-year retrospective analysis. All three
  significantly outperform static PoP (Package-of-Practice) baselines, with Tree of
  Thoughts achieving impressive peak yields. At the same time, Reflexion achieves
  comparable agronomic outcomes at substantially lower computational cost by leveraging
  cross-seasonal episodic memory.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 643a4aba68aaedda
manifest_dates:
- '2026-07-02'
source_type: academic_paper
tldr: Agri-SAGE 是一个将检索增强的多智能体 LLM 推理与 APSIM 生物物理模拟相结合的闭环框架，用于生成并验证农业咨询建议。10年期回顾实验表明，Tree
  of Thoughts 方法达到最高产量，Reflexion 方法以更低计算成本取得可比结果。
objective_summary: arXiv 论文提出 Agri-SAGE 框架，通过融合多智能体 LLM 推理与 APSIM 生物物理模拟，解决传统静态农业指南忽略季节内变化、以及纯
  LLM 建议缺乏生理合理性的双重局限。研究在 10 年期回顾分析中评估了 Plan-and-Solve、Tree of Thoughts 和 Reflexion
  三种推理方法，结果显示所有方法均显著优于静态 Package-of-Practice 基线，其中 Tree of Thoughts 达到峰值产量，Reflexion
  借助跨季节 episodic memory 以更低计算成本取得相当效果。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Multi-Agent LLM
  - APSIM
  - RAG
  - Plan-and-Solve
  - Tree of Thoughts
  - Reflexion
  key_people: []
key_logic_flow:
- 农业咨询系统面临根本矛盾：静态指南可靠但忽视季节内变化，纯 LLM 建议则可能农学上合理但生理学上不具说服力。
- Agri-SAGE 是一个闭环框架，将检索增强的多智能体 LLM 推理与 APSIM 生物物理模拟相结合，用于生成并验证农学咨询建议。
- 研究在 10 年期回顾分析中评估了 Plan-and-Solve、Tree of Thoughts 和 Reflexion 三种推理方法的表现。
- Tree of Thoughts 方法实现了令人瞩目的峰值产量表现，在三种方法中最为突出。
- Reflexion 方法通过利用跨季节的 episodic memory，在显著降低计算成本的同时取得了与 Tree of Thoughts 相当的农学效果。
- 所有三种推理方法均显著优于传统的静态 Package-of-Practice 基线方案。
specialized_tags:
  paper:
    paperTitle: 'Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware
      Agricultural Advisory Generation'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Other
    methodType: LLM-based
extract_result: success
object_mentions:
- object_type: project
  name: Agri-SAGE
  canonical_name: Agri-SAGE
  url: https://arxiv.org/abs/2607.00454
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Agri-SAGE 是一个闭环框架，通过结合检索增强的多智能体 LLM 推理与 APSIM 生物物理模拟，来生成并验证农学咨询建议。
  - 该框架被设计用于解决静态指南忽略季节内变化和纯 LLM 建议缺乏生理合理性的双重局限。
  article_id: 643a4aba68aaedda
- object_type: project
  name: APSIM
  canonical_name: APSIM
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agri-SAGE 框架集成了 APSIM 生物物理模拟引擎，用于在生成农学建议后验证其生理合理性。
  - APSIM 作为生物物理仿真引擎，为多智能体 LLM 生成的农学建议提供模拟验证的基础。
  article_id: 643a4aba68aaedda
---

# Computer Science > Artificial Intelligence

# Title:Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware Agricultural Advisory Generation

View PDF HTML (experimental)Abstract:Agricultural advisory systems face a fundamental tension: static agronomic guidelines offer consistent, evidence-based recommendations, yet remain blind to in-season variability and dynamic uncertainties. Recent advisory systems powered by LLMs are liable for a different risk of generating recommendations that are agronomically credible but physiologically unconvincing. Agri-SAGE is a closed-loop framework designed to resolve the above two limitations by integrating retrieval-grounded multi-agent LLM reasoning with APSIM-based biophysical simulation, to generate and validate agronomic advisories. To assess this framework, we evaluate three reasoning approaches, namely Plan-and-Solve, Tree of Thoughts, and Reflexion, over a 10-year retrospective analysis. All three significantly outperform static PoP (Package-of-Practice) baselines, with Tree of Thoughts achieving impressive peak yields. At the same time, Reflexion achieves comparable agronomic outcomes at substantially lower computational cost by leveraging cross-seasonal episodic memory.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.