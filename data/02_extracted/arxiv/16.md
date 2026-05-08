---
title: A Foundation Model for Zero-Shot Logical Rule Induction
source: https://arxiv.org/abs/2605.04916
author:
- '[[Yin Jun Phua]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04916v1 Announce Type: new Abstract: Inductive Logic Programming
  (ILP) learns interpretable logical rules from data. Existing methods are transductive:
  their learned parameters are bound to specific predicates and require retraining
  for each new task. We introduce Neural Rule Inducer (NRI), a pretrained model for
  zero-shot rule induction. Rather than encoding literal identities, NRI represents
  literals using domain-agnostic statistical properties such as class-conditional
  rates, entropy, and co-occurrence, which generalize across variable identities and
  counts without retraining. The model consists of a statistical encoder and a parallel
  slot-based decoder. Parallel decoding preserves the permutation invariance of logical
  disjunction; an autoregressive decoder would instead impose an arbitrary clause
  order. Product T-norm relaxation makes rule execution differentiable, allowing end-to-end
  training on prediction accuracy alone. We evaluate NRI on rule recovery, robustness
  to label noise and spurious correlations, and zero-shot transfer to real-world benchmarks,
  and we believe this work opens up the possibility of foundation models for symbolic
  reasoning. Code and the reference checkpoint are available at https://github.com/phuayj/neural-rule-inducer.'
tags:
- clippings
id: d2b0e38ffa61cc0f
source_type: academic_paper
tldr: 提出 Neural Rule Inducer (NRI) 模型，首次实现零样本逻辑规则归纳，无需针对新任务重新训练。
objective_summary: 论文提出 Neural Rule Inducer (NRI)，一种用于零样本规则归纳的预训练模型。NRI 用统计编码器表示文字的统计属性（如类条件概率、熵、共现率），替代传统
  ILP 中绑定于具体谓词的参数；采用并行槽位解码器保持逻辑析取的置换不变性，并通过 Product T-norm
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Inductive Logic Programming (ILP)
  - Neural Rule Inducer (NRI)
  - Product T-norm
  key_people: []
key_logic_flow:
- 传统归纳逻辑编程（ILP）是转导式的，其学习参数绑定于特定谓词，每遇到新任务都需要重新训练。
- NRI 不编码文字的字面标识，而是使用域无关的统计属性（类条件概率、熵、共现率）来表示文字，这些属性在不同任务间可泛化。
- 模型由统计编码器和并行槽位解码器组成；并行解码保持了逻辑析取的置换不变性，而自回归解码器会强加任意子句顺序。
- 通过 Product T-norm 松弛使规则执行过程可微分，从而可以仅基于预测准确率进行端到端训练。
- 实验评估了 NRI 在规则恢复、对标签噪声和虚假相关性的鲁棒性，以及在真实世界基准上的零样本迁移能力。
---

# Computer Science > Artificial Intelligence

# Title:A Foundation Model for Zero-Shot Logical Rule Induction

View PDF HTML (experimental)Abstract:Inductive Logic Programming (ILP) learns interpretable logical rules from data. Existing methods are transductive: their learned parameters are bound to specific predicates and require retraining for each new task. We introduce Neural Rule Inducer (NRI), a pretrained model for zero-shot rule induction. Rather than encoding literal identities, NRI represents literals using domain-agnostic statistical properties such as class-conditional rates, entropy, and co-occurrence, which generalize across variable identities and counts without retraining. The model consists of a statistical encoder and a parallel slot-based decoder. Parallel decoding preserves the permutation invariance of logical disjunction; an autoregressive decoder would instead impose an arbitrary clause order. Product T-norm relaxation makes rule execution differentiable, allowing end-to-end training on prediction accuracy alone. We evaluate NRI on rule recovery, robustness to label noise and spurious correlations, and zero-shot transfer to real-world benchmarks, and we believe this work opens up the possibility of foundation models for symbolic reasoning. Code and the reference checkpoint are available at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.