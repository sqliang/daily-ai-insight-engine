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