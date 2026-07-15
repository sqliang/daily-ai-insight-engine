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
pipeline_stage: ingested
id: bcb8be308ae51c0d
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