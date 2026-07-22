---
title: 'Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs'
source: https://arxiv.org/abs/2606.13815
author:
- '[[Pratham Singla, Shivank Garg, Vihan Singh]]'
published: '2026-06-15'
created: '2026-06-15'
description: 'arXiv:2606.13815v1 Announce Type: new Abstract: Strategic reasoning
  under uncertainty underpins consequential decisions in negotiation, finance, and
  policy, but prevailing game-play benchmarks collapse heterogeneous reasoning dimensions
  into a single scalar, leaving the capability structure of frontier LLMs unexamined.
  We introduce Poker Arena, a no-limit Texas Hold''em tournament platform that couples
  a three-layer memory architecture (within-hand, session, and cross-session) with
  a nine-axis cognitive profile decomposing strategic reasoning into interpretable
  dimensions such as bet-sizing calibration and positional awareness. We evaluate
  seven frontier models across 50 sessions of 1,000 hands and a controlled memory
  ablation; tournament chips and aggregate axis score order the field differently:
  Claude Opus 4.6 wins +$15,730 chips with 14 first-place finishes, yet ranks only
  fifth of seven on mean axis score, while persistent memory helps some models and
  hurts others. These findings show that multi-axis evaluation surfaces capability
  structure that scalar leaderboards systematically misrank, with cross-dimensional
  consistency outweighing peak performance on any single axis.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6abedda39a36d5e2
source_type: academic_paper
tldr: Poker Arena 是一个无限制德州扑克竞技平台，用于对 LLM 的战略推理和记忆能力进行多维度评估。该平台结合三层记忆架构与九轴认知画像，发现 Claude
  Opus 4.6 在筹码收益上领先但综合得分仅排第五，表明标量排行榜会系统性误判模型能力结构。
objective_summary: 该论文提出了 Poker Arena，一个基于无限制德州扑克的评估平台，用于剖析大语言模型的战略推理与记忆能力。该平台设计了牌局内、牌局间和跨会话三层记忆架构，以及包含下注校准、位置意识等九个维度的认知画像。研究人员对
  7 个前沿模型进行了 50 场共 1000 手牌的评估和受控记忆消融实验。结果显示 Claude Opus 4.6 赢得 +15730 筹码和 14 次第一名，但在平均轴得分上仅排第五，说明多维度评估能揭示标量排行榜系统性掩盖的能力结构。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  key_people: []
key_logic_flow:
- Poker Arena 是一个无限制德州扑克竞技平台，用于评估大语言模型的战略推理和记忆能力。
- 该平台采用三层记忆架构（牌局内、牌局间和跨会话记忆）以及九轴认知画像，将战略推理分解为可解释的维度。
- 研究人员对 7 个前沿模型进行了 50 场共计 1000 手牌的评估和受控记忆消融实验。
- Claude Opus 4.6 在筹码收益上领先，赢得 +15730 筹码和 14 次第一名，但在平均轴得分上仅排第五。
- 多维度评估揭示了标量排行榜系统性误判模型能力结构的问题，跨维度一致性比单轴峰值表现更重要。
extract_result: success
object_mentions:
- object_type: project
  name: Poker Arena
  canonical_name: Poker Arena
  url: https://arxiv.org/abs/2606.13815
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Poker Arena 是一个无限制德州扑克竞技平台，结合三层记忆架构与九轴认知画像对 LLM 的战略推理能力进行多维度评估。
  - 该平台设计了牌局内、牌局间和跨会话三层记忆架构，并将战略推理分解为下注校准、位置意识等九个可解释维度。
  article_id: 6abedda39a36d5e2
- object_type: model
  name: Claude Opus 4.6
  canonical_name: Claude Opus 4.6
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Claude Opus 4.6 在 Poker Arena 中赢得 +15730 筹码和 14 次第一名，但在平均轴得分上仅排第五。
  - 该结果表明标量排行榜会系统性误判模型能力结构，跨维度一致性比单轴峰值表现更为重要。
  article_id: 6abedda39a36d5e2
---

# Computer Science > Artificial Intelligence

# Title:Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs

View PDF HTML (experimental)Abstract:Strategic reasoning under uncertainty underpins consequential decisions in negotiation, finance, and policy, but prevailing game-play benchmarks collapse heterogeneous reasoning dimensions into a single scalar, leaving the capability structure of frontier LLMs unexamined. We introduce Poker Arena, a no-limit Texas Hold'em tournament platform that couples a three-layer memory architecture (within-hand, session, and cross-session) with a nine-axis cognitive profile decomposing strategic reasoning into interpretable dimensions such as bet-sizing calibration and positional awareness. We evaluate seven frontier models across 50 sessions of 1,000 hands and a controlled memory ablation; tournament chips and aggregate axis score order the field differently: Claude Opus 4.6 wins +$15,730 chips with 14 first-place finishes, yet ranks only fifth of seven on mean axis score, while persistent memory helps some models and hurts others. These findings show that multi-axis evaluation surfaces capability structure that scalar leaderboards systematically misrank, with cross-dimensional consistency outweighing peak performance on any single axis.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.