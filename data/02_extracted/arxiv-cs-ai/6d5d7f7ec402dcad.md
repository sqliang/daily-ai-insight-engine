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
tldr: TurnOPD 是一种面向长周期智能体训练的逐轮预算策略，通过自适应回滚深度预算和渐进式轮归一化损失预算解决了传统在线策略蒸馏中尾部回合浪费算力和深层决策轮训练不足的问题。
objective_summary: 该论文识别了在线策略蒸馏（OPD）在长周期智能体任务中的两个低效问题：完整轨迹回滚在尾部回合提供弱且噪声大的 KL 监督信号而浪费算力，以及轨迹级
  KL 目标将大部分损失集中在浅层 token 上导致深层决策轮训练不足。作者提出 TurnOPD，包含自适应回滚深度预算和渐进式轮归一化损失预算两个控制器，在
  ALFWorld、WebShop 和 Multi-Hop Search 三个基准上使用任务专用教师模型进行实验，验证了该方法在相同训练时间预算下取得更优的验证准确率。
event_type: application_landing
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - TurnOPD
  - On-Policy Distillation
  - ALFWorld
  - WebShop
  - Multi-Hop Search
  key_people: []
key_logic_flow:
- 在线策略蒸馏（OPD）通过让学生智能体在其自身轨迹上模仿更强的教师策略来训练学生策略，但应用于长周期智能体任务时探索尚不充分。
- 论文识别了两个关键低效问题：完整轨迹回滚在尾部回合浪费算力，以及轨迹级 KL 损失将大部分损失集中在浅层 token 上。
- TurnOPD 提出了自适应回滚深度预算控制器，利用探针式回合统计来决定每轮的回滚长度。
- TurnOPD 还提出了渐进式轮归一化损失预算控制器，逐步将 KL 权重从 token 级别转向回合平衡的监督方式。
- 在 ALFWorld、WebShop 和 Multi-Hop Search 三个长周期任务上的实验表明，TurnOPD 在相同训练时间预算下取得了超越传统 OPD
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
object_mentions:
- object_type: model
  name: TurnOPD
  canonical_name: TurnOPD
  url: https://arxiv.org/abs/2607.05804
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - TurnOPD 是一种逐轮预算策略，用于长周期智能体的高效在线策略蒸馏。
  - TurnOPD 包含两个预算控制器：自适应回滚深度预算和渐进式轮归一化损失预算。
  - 实验表明 TurnOPD 在相同训练时间预算下比传统 OPD 取得更优的验证准确率。
  article_id: 6d5d7f7ec402dcad
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