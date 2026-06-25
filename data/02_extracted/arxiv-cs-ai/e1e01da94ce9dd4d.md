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
tldr: 提出 Theory of Mind Utility (ToM-U) 形式化框架，通过局部认知世界模型推断他人的信念状态。
objective_summary: 该论文在计算层面形式化了心智化（mentalizing）机制，提出 ToM-U 框架，通过构建局部认知世界模型（LEWM）——一种表示智能体、状态节点及其认知关系的有向类型图——来推断他人的认知状态，并定义了五种形式化规范。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - ToM-U
  - LEWM
  - Bayesian Theory of Mind
  key_people: []
key_logic_flow:
- ToM-U 在计算层面形式化了心智化机制，不涉及具体的算法或神经实现。
- ToM-U 通过构建局部认知世界模型（LEWM）——有向类型图——来表示智能体、状态节点及其认知关系。
- 模型包含五种形式化定义：LEWM 结构、智能体节点属性（含有序信息访问历史）、递归心智化的有界扩展机制、三种推理过程、以及心智化失败的结构化残差痕迹。
- ToM-U 与贝叶斯心智理论不同，后者预设而非推导信念状态。
- ToM-U 与模拟理论和理论-理论不同，后者缺乏认知状态推理的形式化工具。
- 该框架声称能产生基于模型结构性质的方向性、可证伪的心智化失败预测，并定位为目标推理等下游社会认知过程的上游机制。
extract_result: success
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