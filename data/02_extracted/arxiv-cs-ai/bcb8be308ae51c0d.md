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
tldr: 该论文研究了图世界模型（GWM）在规划任务中的 rollout 误差累积问题，提出了固定边和动态边场景下的拓扑感知误差界，并设计了 Error-Aware
  GWM 训练方法来提升长程稳定性。
objective_summary: 该论文将 rollout 误差分析从向量值状态扩展到图结构环境，在统一的状态-动作转移框架下推导了固定边和动态边 GWM 的拓扑感知误差界。固定边场景中，长程节点误差分解为图谱半径决定的拓扑因子和层谱范数决定的模型因子；动态边场景中引入联合节点-边误差算子刻画特征预测与结构预测的相互反馈。基于误差界分析，论文提出了结合谱正则化、rollout
  一致性和关键节点加权的 Error-Aware GWM 训练目标。在合成图拓扑和异构智能体-图测试床上的实验结果显示，Error-Aware GWM 在不牺牲单步准确率的前提下提升了长程稳定性。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Graph World Models (GWM)
  - Error-Aware GWM
  key_people: []
key_logic_flow:
- 该论文将图世界模型（GWM）的 rollout 误差分析从向量值状态扩展到图结构环境，并建立了统一的状态-动作转移分析框架。
- 对于固定边 rollout，推导出长程节点误差可分解为拓扑因子（由图谱半径决定）和模型因子（由层谱范数决定）两部分。
- 对于动态边 rollout，论文引入联合节点-边误差算子，捕获特征预测与结构预测之间的反馈循环，揭示了边误差会放大未来消息传递的条件。
- 基于误差界分析，论文提出 Error-Aware GWM 训练目标，该目标同时使用谱正则化、rollout 一致性和关键节点加权三个组成部分。
- 在合成图拓扑和异构智能体-图测试床上的实验表明，rollout 误差和规划遗憾度随着预测步数增加而增长，且动态边训练在结构演化场景中是必要的。
- Error-Aware GWM 方法在不牺牲单步预测准确率的前提下，有效提升了长程自回归规划的稳定性。
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
object_mentions:
- object_type: paper
  name: Understanding Rollout Error in Graph World Models
  canonical_name: Understanding Rollout Error in Graph World Models
  url: https://arxiv.org/abs/2606.27780
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文研究了图世界模型（GWM）在规划任务中的 rollout 误差累积问题，并提出了拓扑感知误差界。
  - 论文提出了 Error-Aware GWM 训练目标，结合了谱正则化、rollout 一致性和关键节点加权以提升长程稳定性。
  - 实验在合成图拓扑和异构智能体-图测试床上验证了 Error-Aware GWM 在长程稳定性上的改进效果。
  article_id: bcb8be308ae51c0d
- object_type: model
  name: Error-Aware GWM
  canonical_name: Error-Aware GWM
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Error-Aware GWM 是一种结合谱正则化、rollout 一致性和关键节点加权的训练目标。
  - 实验表明 Error-Aware GWM 在不牺牲单步准确率的前提下提升了长程规划稳定性。
  article_id: bcb8be308ae51c0d
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