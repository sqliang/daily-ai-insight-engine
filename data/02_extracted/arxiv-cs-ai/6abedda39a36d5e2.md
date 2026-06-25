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
tldr: Poker Arena：基于德州扑克的多轴评估框架，揭示LLM战略推理能力结构，发现Claude Opus 4.6筹码最高但综合轴得分仅排第五。
objective_summary: 该论文提出Poker Arena，一个无限制德州扑克比赛平台，采用三层记忆架构和九轴认知画像评估LLM战略推理。实验对7个前沿模型进行了50轮各1000手牌测试，发现传统标量排行榜会系统性误排模型真实能力。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Anthropic
  technologies:
  - Poker Arena
  - Texas Hold'em
  - LLMs
  key_people: []
key_logic_flow:
- 该论文提出了Poker Arena，一个基于无限制德州扑克的比赛平台，用于评估大语言模型的战略推理和记忆能力。
- Poker Arena采用三层记忆架构（局内记忆、会话记忆和跨会话记忆）和九轴认知画像，将战略推理分解为可解释的维度（如下注规模校准和位置意识）。
- 论文评估了7个前沿模型，进行了50轮各1000手牌的比赛，并实施了受控记忆消融实验。
- 实验发现Claude Opus 4.6赢得+15,730筹码和14次第一名，但在平均轴得分上仅排名第五（共七个模型）。
- 持久性记忆对某些模型有帮助，但对另一些模型反而有害。
- 多轴评估揭示了标量排行榜系统性误排的能力结构，跨维度一致性比单轴峰值表现更重要。
extract_result: success
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