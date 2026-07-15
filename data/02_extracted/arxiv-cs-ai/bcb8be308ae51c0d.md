---
title: Understanding Rollout Error in Graph World Models
source: https://arxiv.org/abs/2606.27780
author:
- '[[Xinyuan Song, Zekun Cai]]'
published: '2026-06-29'
created: '2026-06-29'
manifest_dates:
- '2026-06-29'
- '2026-06-30'
description: 'arXiv:2606.27780v1 Announce Type: new Abstract: World models are often
  used for planning by rolling learned dynamics forward. Many planning environments,
  however, are not vectors or images; they are graphs of agents, tools, skills, routes,
  and dependencies. In these settings, a local prediction error may stay local or
  spread through the graph, and the failure mode changes again when edges are predicted
  rather than fixed. This paper studies long-horizon rollout error in Graph World
  Models (GWMs). We formulate a unified fixed-edge and dynamic-edge GWM framework
  with action nodes for node-, edge-, and graph-level decisions. We develop graph-valued
  rollout bounds that separate topology-induced amplification from model-induced amplification,
  and we introduce a joint node-edge operator for dynamic-edge rollouts. Guided by
  the analysis, we propose Error-Aware GWM, which combines spectral regularization,
  rollout consistency, and critical-node weighting. Across synthetic topologies and
  heterogeneous agent-graph testbeds, rollout error and planning regret grow with
  horizon, dynamic-edge training is needed when structure evolves, and Error-Aware
  GWM prevents long-horizon divergence while preserving prediction accuracy. Real-world
  graph benchmarks clarify the scope of GWMs: they are most useful for dynamic graph
  rollout and agent planning, while specialized graph models remain strong on static
  or sparse prediction tasks.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bcb8be308ae51c0d
source_type: academic_paper
tldr: 研究图世界模型中预测误差的累积问题，提出拓扑感知误差边界及Error-Aware GWM训练方法
objective_summary: 该论文研究了图世界模型（GWM）在规划中的预测误差累积问题。作者Xinyuan Song和Zekun Cai为固定边和动态边GWM建立了统一的状态-动作转移框架，推导了拓扑感知误差边界，并提出了结合谱正则化、展开一致性和关键节点权重的Error-Aware
  GWM训练目标，
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Graph World Models
  - GWM
  - Error-Aware GWM
  key_people:
  - Xinyuan Song
  - Zekun Cai
key_logic_flow:
- 论文指出大多数世界模型（World Model）的展开误差分析假设向量化状态和标量误差放大，而许多规划环境天然具有图结构，需要拓扑感知的分析方法。
- 为固定边和动态边GWM建立了统一的状态-动作转移框架，并分别推导了拓扑感知的误差传播边界。
- 固定边展开中，长程节点误差可分解为拓扑因子（由图谱半径决定）和模型因子（由层谱范数决定）两个独立分量。
- 动态边展开中引入了联合节点-边误差算子，揭示了特征预测与结构预测之间的反馈放大效应，说明边缘误差会放大后续消息传递。
- 基于理论边界提出了Error-Aware GWM训练目标，融合了谱正则化、展开一致性约束和关键节点加权三种机制。
- 实验证明展开误差和规划遗憾随预测步数增长而增大，结构动态变化时必须使用动态边训练，Error-Aware GWM能提升长程稳定性且不牺牲单步精度。
specialized_tags:
  paper:
    paperTitle: Understanding Rollout Error in Graph World Models
    authors:
    - Xinyuan Song
    - Zekun Cai
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Graph
    methodType: theoretical
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Understanding Rollout Error in Graph World Models

View PDF HTML (experimental)Abstract:World models are increasingly used for planning, yet most analyses of rollout error assume vector-valued states and scalar error amplification. Many planning environments, however, are naturally graph-structured: agents, tools, skills, routes, and dependencies interact through evolving relations. In this work, we study how prediction errors accumulate in Graph World Models (GWMs). We formulate fixed-edge and dynamic-edge GWM rollouts under a unified state-action transition framework and derive topology-aware error bounds. For fixed-edge rollouts, we show that long-horizon node error separates into a topology factor, governed by the graph spectral radius, and a model factor, governed by layer spectral norms. For dynamic-edge rollouts, we introduce a joint node-edge error operator that captures feedback between feature prediction and structure prediction, revealing when edge errors amplify future message passing. Motivated by these bounds, we propose Error-Aware GWM, a training objective that combines spectral regularization, rollout consistency, and critical-node weighting. Across synthetic graph topologies and heterogeneous agent-graph testbeds, we find that rollout error and planning regret grow with horizon, that dynamic-edge training is necessary when structure evolves, and that Error-Aware GWM improves long-horizon stability without sacrificing one-step accuracy. Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.