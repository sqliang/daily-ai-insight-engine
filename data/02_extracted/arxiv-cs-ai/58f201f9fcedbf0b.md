---
title: 'Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization'
source: https://arxiv.org/abs/2605.05040
author:
- '[[Xin Yu, Liuchen Liao, Yiwen Zhang, Yingchen Yu, Lingzhou Xue, Qinzhen Guo]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.05040v1 Announce Type: cross Abstract: On-policy distillation
  is an efficient alternative to reinforcement learning, offering dense token-level
  training signals. However, its reliance on a stronger external teacher has driven
  recent work on on-policy self-distillation, where the same model serves as both
  teacher and student under different prompt contexts. Yet, existing self-distillation
  methods largely reduce learning to KL matching toward the context-augmented teacher
  model. This approach often suffers from training instability and can degrade reasoning
  performance over time. Moreover, self-distillation from the same model with prompt
  augmentation lacks the exploratory diversity provided by a genuine external teacher.
  To address these limitations, we move beyond fixed-teacher KL matching and propose
  \textbf{P}reference-\textbf{B}ased \textbf{S}elf-\textbf{D}istillation (\textbf{PBSD}),
  which revisits on-policy self-distillation through a reward-regularized perspective.
  Instead of directly matching the teacher distribution, we derive a reward-regularized
  objective whose analytic optimum is a reward-reweighted teacher distribution, yielding
  a target policy provably superior to the original teacher under this objective.
  Practically, PBSD optimizes preference gaps between teacher and student samples
  while maintaining on-policy student sampling. We support this framework with a statistical
  analysis of the induced preference-learning problem, formally establishing when
  on policy self-distillation is preferable to learning from an external teacher in
  our setting. Experiments on mathematical reasoning and tool-use benchmarks across
  multiple model scales demonstrate that PBSD consistently achieves the strongest
  average performance among comparable baselines, showing improved training stability
  over prior self-distillation baselines while preserving token efficiency.'
tags:
- clippings
id: 58f201f9fcedbf0b
source_type: academic_paper
tldr: 基于奖励正则化的偏好自蒸馏方法PBSD，超越传统KL匹配，提升训练稳定性
objective_summary: PBSD方法提出基于奖励正则化的在线自蒸馏框架，用偏好差距优化替代KL匹配，在数学推理和工具使用基准上取得最强平均性能，提升训练稳定性并保持token效率。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - PBSD
  - KL matching
  - reward regularization
  - on-policy distillation
  - self-distillation
  key_people: []
key_logic_flow:
- 现有的在线自蒸馏方法主要依赖KL匹配，存在训练不稳定和推理性能随时间退化的问题。
- PBSD提出基于奖励正则化的在线自蒸馏框架，其解析最优解是对教师分布进行奖励加权后的目标策略。
- PBSD通过优化教师样本与学生样本之间的偏好差距进行学习，同时保持在线学生采样。
- 论文从统计角度分析了偏好学习问题，正式界定了在线自蒸馏何时优于从外部教师学习。
- 在数学推理和工具使用基准测试上，PBSD在多个模型规模下均取得最强平均性能，训练稳定性优于现有自蒸馏基线方法。
---

# Computer Science > Machine Learning

# Title:Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization

View PDF HTML (experimental)Abstract:On-policy distillation is an efficient alternative to reinforcement learning, offering dense token-level training signals. However, its reliance on a stronger external teacher has driven recent work on on-policy self-distillation, where the same model serves as both teacher and student under different prompt contexts. Yet, existing self-distillation methods largely reduce learning to KL matching toward the context-augmented teacher model. This approach often suffers from training instability and can degrade reasoning performance over time. Moreover, self-distillation from the same model with prompt augmentation lacks the exploratory diversity provided by a genuine external teacher. To address these limitations, we move beyond fixed-teacher KL matching and propose \textbf{P}reference-\textbf{B}ased \textbf{S}elf-\textbf{D}istillation (\textbf{PBSD}), which revisits on-policy self-distillation through a reward-regularized perspective. Instead of directly matching the teacher distribution, we derive a reward-regularized objective whose analytic optimum is a reward-reweighted teacher distribution, yielding a target policy provably superior to the original teacher under this objective. Practically, PBSD optimizes preference gaps between teacher and student samples while maintaining on-policy student sampling. We support this framework with a statistical analysis of the induced preference-learning problem, formally establishing when on policy self-distillation is preferable to learning from an external teacher in our setting. Experiments on mathematical reasoning and tool-use benchmarks across multiple model scales demonstrate that PBSD consistently achieves the strongest average performance among comparable baselines, showing improved training stability over prior self-distillation baselines while preserving token efficiency.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.