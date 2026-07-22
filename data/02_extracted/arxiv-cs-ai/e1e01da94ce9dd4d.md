---
title: 'The Theory of Mind Utility: Formal Specification of a Mentalizing Mechanism'
source: https://arxiv.org/abs/2606.12721
author:
- '[[Nikolos Gurney, Stacy Marsella]]'
published: '2026-06-12'
created: '2026-06-12'
description: 'arXiv:2606.12721v1 Announce Type: new Abstract: Inferring others'' beliefs
  requires more than reading surface signals; it requires tracking who told them what,
  in what order, and how credibly. The Theory of Mind Utility (ToM-U) formalizes this
  epistemic state inference problem at the computational level of analysis, specifying
  what mentalizing computes and why without commitment to algorithmic or neural implementation.
  ToM-U achieves this by constructing Local Epistemic World Models (LEWMs) -- directed
  typed graphs that represent agents, state nodes, and the epistemic relationships
  among them -- and evaluating discrete candidate LEWMs against observed behavior
  until one achieves sufficient confidence. Five formal definitions specify the LEWM
  structure, agent node properties including ordered information access history, a
  bounded proliferation mechanism for recursive mentalizing, three inference procedures,
  and a residue function that captures the structured trace left by failed mentalizing
  attempts. ToM-U differs from Bayesian Theory of Mind and adjacent formal accounts,
  which presuppose rather than derive belief states, and from simulation theory and
  theory-theory, which lack a formal apparatus for epistemic state inference. The
  architecture generates directional, falsifiable predictions about mentalizing failure
  that follow from structural properties of the model rather than auxiliary assumptions,
  and positions ToM-U as a domain-agnostic mechanism upstream of goal inference and
  other downstream social cognitive processes.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e1e01da94ce9dd4d
source_type: academic_paper
tldr: 一篇 arXiv 论文形式化定义了"心智理论效用"(ToM-U)机制，通过构建局部认知世界模型(LEWM)来推断他人信念状态，并产生关于心智化失败的结构化预测。
objective_summary: 该论文在计算层面形式化定义了 Theory of Mind Utility (ToM-U) 机制，用于推断他人信念状态。ToM-U
  通过构建有向类型图——局部认知世界模型(LEWM)来表示智能体、状态节点及其认知关系，并评估离散候选 LEWM 与观测行为的匹配度直到达到置信阈值。论文给出了五条形式定义，涵盖
  LEWM 结构、智能体节点属性（含有序信息访问历史）、递归心智化的有界增生机制、三种推理过程以及残差函数。该框架区别于贝叶斯心智理论和模拟理论，后者预设而非推导信念状态。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Theory of Mind Utility
  - ToM-U
  - Local Epistemic World Models
  - LEWM
  - Bayesian Theory of Mind
  key_people: []
key_logic_flow:
- ToM-U 从计算层面形式化定义了心智化机制，阐明心智算计算什么以及为什么这样做，而不承诺算法或神经实现。
- 该机制通过构造局部认知世界模型(LEWM)——有向类型图来表示智能体、状态节点及其认知关系。
- 系统通过评估离散候选 LEWM 与观测到的行为之间的匹配度，直到达到足够的置信水平。
- 论文给出了五条形式定义，涵盖 LEWM 结构、智能体节点属性（含有序信息访问历史）、递归心智化的有界增生机制、三种推理过程以及残差函数。
- ToM-U 区别于贝叶斯心智理论（后者预设而非推导信念状态）以及模拟理论和理论论（后者缺乏认知状态推断的形式化工具）。
- 该架构基于模型的结构属性而非辅助假设，生成关于心智化失败的方向性和可证伪预测，并将自身定位为目标推断等下游社会认知过程的上游机制。
extract_result: success
object_mentions:
- object_type: paper
  name: 'The Theory of Mind Utility: Formal Specification of a Mentalizing Mechanism'
  canonical_name: ToM-U Paper
  url: https://arxiv.org/abs/2606.12721
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - '该论文标题为"The Theory of Mind Utility: Formal Specification of a Mentalizing Mechanism"，发布于
    arXiv，编号 2606.12721。'
  - ToM-U 通过构建局部认知世界模型(LEWM)来形式化认知状态推断问题，这是在计算层面的分析，不承诺算法或神经实现。
  article_id: e1e01da94ce9dd4d
- object_type: project
  name: Theory of Mind Utility (ToM-U)
  canonical_name: ToM-U
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - ToM-U 构造局部认知世界模型(LEWM)——有向类型图表示智能体、状态节点及其认知关系，并评估候选 LEWM 与观测行为的匹配度。
  - ToM-U 区分于贝叶斯心智理论和模拟理论，后者预设信念状态而前者从信息访问历史推导认知状态。
  article_id: e1e01da94ce9dd4d
- object_type: project
  name: Local Epistemic World Models (LEWM)
  canonical_name: LEWM
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - LEWM 是有向类型图，表示智能体、状态节点以及它们之间的认知关系，是 ToM-U 的核心表示结构。
  - 五条形式定义规定了 LEWM 的结构、智能体节点属性（含有序信息访问历史）、递归心智化增生机制和推理过程。
  article_id: e1e01da94ce9dd4d
---

# Computer Science > Artificial Intelligence

# Title:The Theory of Mind Utility: Formal Specification of a Mentalizing Mechanism

View PDF HTML (experimental)Abstract:Inferring others' beliefs requires more than reading surface signals; it requires tracking who told them what, in what order, and how credibly. The Theory of Mind Utility (ToM-U) formalizes this epistemic state inference problem at the computational level of analysis, specifying what mentalizing computes and why without commitment to algorithmic or neural implementation. ToM-U achieves this by constructing Local Epistemic World Models (LEWMs) -- directed typed graphs that represent agents, state nodes, and the epistemic relationships among them -- and evaluating discrete candidate LEWMs against observed behavior until one achieves sufficient confidence. Five formal definitions specify the LEWM structure, agent node properties including ordered information access history, a bounded proliferation mechanism for recursive mentalizing, three inference procedures, and a residue function that captures the structured trace left by failed mentalizing attempts. ToM-U differs from Bayesian Theory of Mind and adjacent formal accounts, which presuppose rather than derive belief states, and from simulation theory and theory-theory, which lack a formal apparatus for epistemic state inference. The architecture generates directional, falsifiable predictions about mentalizing failure that follow from structural properties of the model rather than auxiliary assumptions, and positions ToM-U as a domain-agnostic mechanism upstream of goal inference and other downstream social cognitive processes.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.