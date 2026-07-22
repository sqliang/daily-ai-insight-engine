---
title: Improving Multimodal Reasoning via Worst Dimension Optimization
source: https://arxiv.org/abs/2606.07801
author:
- '[[Haocheng Lv, Huaping Zhang, Qiuchi Li, Lei Li, Chunxiao Gao]]'
published: '2026-06-09'
created: '2026-06-09'
description: 'arXiv:2606.07801v1 Announce Type: new Abstract: Multimodal reasoning
  requires a path that retains integrity over a wide range of constraints, from visual
  grounding to logic consistency. However, the current Process Reward Models focus
  on heuristically defined rewards that equally weigh these factors, which may lead
  to the concealment of individual dimension failures by the dominating factors, without
  guaranteeing the validity of the reasoning process in general.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3b80cbc55fdbbf5c
source_type: academic_paper
tldr: 一篇 arXiv 论文指出，当前多模态推理中的流程奖励模型因平等加权视觉定位与逻辑一致性等多维约束，导致主导因素掩盖了单个维度的失败。论文提出最差维度优化方法以解决该问题。
objective_summary: 该论文发表于 arXiv（编号 2606.07801），分析了当前多模态推理中 Process Reward Models 的局限性。论文指出，这些模型使用启发式定义的奖励函数平等加权不同维度的约束，使得视觉定位或逻辑一致性等单个维度的失败可能被其他主导因素掩盖。为此，论文提出
  Worst Dimension Optimization 方法，旨在保障推理过程在各维度上的完整性。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Process Reward Models
  - Worst Dimension Optimization
  - Multimodal Reasoning
  key_people: []
key_logic_flow:
- 多模态推理需要在从视觉定位到逻辑一致性的广泛约束中保持路径完整性。
- 当前流程奖励模型依赖启发式定义的奖励函数，平等地加权所有维度的约束。
- 这种平等加权方式可能导致主导因素掩盖单个维度（如视觉定位或逻辑一致性）的失败。
- 论文提出最差维度优化方法，旨在确保推理过程在各维度上的整体有效性。
extract_result: success
object_mentions:
- object_type: paper
  name: Improving Multimodal Reasoning via Worst Dimension Optimization
  canonical_name: Improving Multimodal Reasoning via Worst Dimension Optimization
  url: https://arxiv.org/abs/2606.07801
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文分析了当前 Process Reward Models 在平等加权多维约束时导致主导因素掩盖单维度失败的问题。
  - 论文提出 Worst Dimension Optimization 方法，旨在保障多模态推理在视觉定位与逻辑一致性等各维度上的完整性。
  - 该论文发表于 arXiv，编号为 2606.07801，属于计算机科学与人工智能领域。
  article_id: 3b80cbc55fdbbf5c
---

# Computer Science > Artificial Intelligence

# Title:Improving Multimodal Reasoning via Worst Dimension Optimization

View PDF HTML (experimental)Abstract:Multimodal reasoning requires a path that retains integrity over a wide range of constraints, from visual grounding to logic consistency. However, the current Process Reward Models focus on heuristically defined rewards that equally weigh these factors, which may lead to the concealment of individual dimension failures by the dominating factors, without guaranteeing the validity of the reasoning process in general.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.