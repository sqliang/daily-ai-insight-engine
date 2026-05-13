---
title: 'Emergent Hierarchical Structure in Large Language Models: An Information-Theoretic
  Framework for Multi-Scale Representation'
source: https://arxiv.org/abs/2505.18244
author:
- '[[Yukin Zhang, Qi Dong, Kemu Xu]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2505.18244v3 Announce Type: replace-cross Abstract: Why do language
  models from different architecture families respond so differently to the same perturbation?
  We argue that the answer is not scale, but \emph{how architecture shapes information
  compression}. Analyzing eight Transformer models (7B--70B parameters) from the Llama
  and Qwen families, we show that every model spontaneously develops discrete functional
  boundaries dividing its layers into Local, Intermediate, and Global processing segments
  -- yet boundary locations and per-segment brittleness are determined overwhelmingly
  by architecture family rather than model size or training configuration. We formalize
  this regularity as the \textbf{Multi-Scale Probabilistic Generation Theory} (MSPGT),
  which models an autoregressive Transformer as a Hierarchical Variational Information
  Bottleneck system and derives a tiered set of falsifiable predictions. Three predictions
  are strongly confirmed: all eight models exhibit two prominent phase-transition
  boundaries (P1.1); Llama boundary positions are stable across a $10{\times}$ parameter
  range ($\mathrm{CV}{=}0.067$--$0.095$) while Qwen positions vary widely ($\mathrm{CV}{=}0.465$--$0.726$),
  precisely matching our strong- and weak-dominance conditions; and cross-architecture
  local-segment brittleness spans \textbf{three orders of magnitude} ($493{\times}$
  ratio) -- a gap that architecture family alone predicts and that dwarfs any within-family
  or scale-driven variation.'
tags:
- clippings
id: a9c403bafb9f7c8b
source_type: academic_paper
tldr: 研究发现LLM架构族（而非模型规模）决定层级功能边界位置与脆性，差距达三个数量级。
objective_summary: 该研究分析了Llama和Qwen两个家族的8个Transformer模型（7B-70B参数），发现每个模型自发形成离散的功能层级边界（局部/中间/全局处理段），且边界位置和脆性由架构族主导，跨架构脆性差异达493倍。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Transformer
  - MSPGT
  - Hierarchical Variational Information Bottleneck
  key_people: []
key_logic_flow:
- 论文提出多尺度概率生成理论（MSPGT），将自回归Transformer建模为层级变分信息瓶颈系统，并推导出可证伪的层级预测。
- 分析了Llama和Qwen两个架构家族的8个模型（7B-70B参数），发现所有模型均自发形成离散的功能层级边界，将层划分为局部、中间和全局处理三段。
- 验证了三个预测中的第一个：所有8个模型均展现出两个显著的相变边界。
- 验证了第二个预测：Llama家族边界位置在10倍参数范围内高度稳定，而Qwen家族位置变化较大，符合强弱支配条件。
- 验证了第三个预测：跨架构的局部段脆性差异达493倍（三个数量级），该差距仅由架构族决定，远超同族或规模引起的差异。
- 结论认为架构如何塑造信息压缩比模型规模更关键地决定了模型对扰动的响应差异。
---

# Computer Science > Computation and Language

# Title:Emergent Hierarchical Structure in Large Language Models: An Information-Theoretic Framework for Multi-Scale Representation

View PDF HTML (experimental)Abstract:Why do language models from different architecture families respond so differently to the same perturbation? We argue that the answer is not scale, but \emph{how architecture shapes information compression}. Analyzing eight Transformer models (7B--70B parameters) from the Llama and Qwen families, we show that every model spontaneously develops discrete functional boundaries dividing its layers into Local, Intermediate, and Global processing segments -- yet boundary locations and per-segment brittleness are determined overwhelmingly by architecture family rather than model size or training configuration. We formalize this regularity as the \textbf{Multi-Scale Probabilistic Generation Theory} (MSPGT), which models an autoregressive Transformer as a Hierarchical Variational Information Bottleneck system and derives a tiered set of falsifiable predictions. Three predictions are strongly confirmed: all eight models exhibit two prominent phase-transition boundaries (P1.1); Llama boundary positions are stable across a $10{\times}$ parameter range ($\mathrm{CV}{=}0.067$--$0.095$) while Qwen positions vary widely ($\mathrm{CV}{=}0.465$--$0.726$), precisely matching our strong- and weak-dominance conditions; and cross-architecture local-segment brittleness spans \textbf{three orders of magnitude} ($493{\times}$ ratio) -- a gap that architecture family alone predicts and that dwarfs any within-family or scale-driven variation.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.