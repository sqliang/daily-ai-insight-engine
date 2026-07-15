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
pipeline_stage: fact_extracted
id: 6d5d7f7ec402dcad
manifest_dates:
- '2026-07-08'
source_type: academic_paper
tldr: 提出 TurnOPD，一种面向长程智能体训练的高效同策略蒸馏方法，通过回合级预算控制提升训练效率。
objective_summary: 该论文提出 TurnOPD 方法，通过自适应 rollout 深度预算和渐进式回合归一化损失预算，解决长程智能体同策略蒸馏中的低效问题。在
  ALFWorld、WebShop 和 Multi-Hop Search 任务上，TurnOPD 在同等训练时间下取得了更优的验证准确率。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - TurnOPD
  - On-Policy Distillation
  - KL divergence
  - Agent Training
  key_people: []
key_logic_flow:
- TurnOPD 识别出 vanilla 同策略蒸馏的两个低效问题：完整回合 rollout 在尾部步骤浪费资源，以及回合级 KL 损失集中在浅层 token 上导致深层决策回合训练不足。
- TurnOPD 提出自适应 rollout 深度预算控制器，基于探针回合统计数据动态决定 rollout 长度，避免尾部无效计算。
- TurnOPD 提出渐进式回合归一化损失预算控制器，将 KL 权重从 token 级逐步转向回合平衡监督。
- 在 ALFWorld、WebShop 和 Multi-Hop Search 三个长程智能体任务上，TurnOPD 在相同壁钟训练预算下超越了 vanilla OPD
  的验证准确率。
specialized_tags:
  paper:
    paperTitle: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
      Agent Training'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: AI
    methodType: RL-based
extract_result: success
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