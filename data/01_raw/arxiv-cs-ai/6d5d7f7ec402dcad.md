---
title: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
  Agent Training'
source: https://arxiv.org/abs/2607.05804
author:
- '[[Yuhang Zhou, Kai Zheng, Haoling Li, Dengyun Peng, Can Xu, Jingjing Chen]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'arXiv:2607.05804v1 Announce Type: new Abstract: On-policy distillation
  (OPD) trains a student policy by matching a stronger teacher on the student''s own
  trajectories, offering a promising framework for language agent training. However,
  its application to long-horizon agentic tasks remains insufficiently explored. We
  identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts
  often waste wall-clock resources on tail turns that provide weak and noisy KL supervision,
  and (2) trajectory-level KL objectives concentrate most of the loss on shallow tokens,
  leaving deeper decision turns under-trained once initial behaviors are aligned.
  To address these challenges, we propose TurnOPD, a turn-level budgeting strategy
  for efficient on-policy distillation of long-horizon agents. TurnOPD consists of
  two budget controllers: adaptive rollout-depth budgeting, which uses probe-based
  turn statistics to determine rollout length, and progressive turn-normalized loss
  budgeting, which gradually shifts KL weighting from token-level to turn-balanced
  supervision. Experiments on ALFWorld, WebShop, and Multi-Hop Search with task-specialized
  teacher models show that TurnOPD achieves superior validation accuracy under equal
  wall-clock training budgets and advances the accuracy--time frontier beyond vanilla
  OPD.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 6d5d7f7ec402dcad
---

# Computer Science > Artificial Intelligence

# Title:TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training

View PDFAbstract:On-policy distillation (OPD) trains a student policy by matching a stronger teacher on the student's own trajectories, offering a promising framework for language agent training. However, its application to long-horizon agentic tasks remains insufficiently explored. We identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts often waste wall-clock resources on tail turns that provide weak and noisy KL supervision, and (2) trajectory-level KL objectives concentrate most of the loss on shallow tokens, leaving deeper decision turns under-trained once initial behaviors are aligned. To address these challenges, we propose TurnOPD, a turn-level budgeting strategy for efficient on-policy distillation of long-horizon agents. TurnOPD consists of two budget controllers: adaptive rollout-depth budgeting, which uses probe-based turn statistics to determine rollout length, and progressive turn-normalized loss budgeting, which gradually shifts KL weighting from token-level to turn-balanced supervision. Experiments on ALFWorld, WebShop, and Multi-Hop Search with task-specialized teacher models show that TurnOPD achieves superior validation accuracy under equal wall-clock training budgets and advances the accuracy--time frontier beyond vanilla OPD.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.