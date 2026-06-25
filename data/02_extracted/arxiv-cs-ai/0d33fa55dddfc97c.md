---
title: Hidden Anchors in Multi-Agent LLM Deliberation
source: https://arxiv.org/abs/2606.19494
author:
- '[[Apurba Pokharel, Ram Dantu]]'
published: '2026-06-19'
created: '2026-06-19'
description: 'arXiv:2606.19494v1 Announce Type: new Abstract: Multi-agent LLM deliberation,
  where agents exchange and revise answers over several rounds, is increasingly used
  to improve reasoning and accuracy, yet how and why it works is rarely modelled.
  Such deliberation mirrors how humans reach decisions. As social animals we are pulled
  both by the group, the herd effect that classical opinion-dynamics models such as
  DeGroot and Friedkin--Johnsen capture, and by our own internal belief, which they
  do not. We model multi-agent deliberation as a closed-loop dynamical system in which
  each agent carries a hidden internal belief, its anchor, that continually pulls
  its opinion regardless of its neighbours. We show this anchor can be recovered from
  the deliberation alone, and that it explains a behaviour classical consensus rules
  forbid: an agent''s confidence in the correct answer can climb past where any agent
  started, escaping the space (convexhull) formed by the initial beliefs. Checking
  whether the recovered anchor also predicts held-out runs (generalizes) gives a simple
  test for when a model is truly driven bysuch an anchor. Across three open-weight
  model families this is a spectrum, not all-or-nothing. All anchors'' influence are
  about equally strongly, but they differ in where the anchor sits, and only when
  it sits far from the initial opinions does deliberation escape the hull and need
  the full closed-loop model.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0d33fa55dddfc97c
source_type: academic_paper
tldr: 论文提出隐藏锚点模型解释多智能体LLM协商机制，证明智能体内部信念可超出初始意见空间。
objective_summary: 该论文将多智能体LLM协商建模为闭环动力系统，每个智能体存在隐藏的内部信念（锚点）持续牵引其观点。实验表明锚点可从协商对话中恢复，并解释了智能体置信度可超越所有初始信念凸包范围这一反常现象。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Multi-Agent LLM
  - DeGroot model
  - Friedkin-Johnsen model
  key_people: []
key_logic_flow:
- 多智能体LLM协商被建模为闭环动力系统，每个智能体携带隐藏的内部信念（锚点）持续牵引其观点。
- 该模型借鉴经典意见动力学模型（DeGroot和Friedkin-Johnsen），同时引入内部信念作为独立于邻居意见的牵引力。
- 研究证明锚点可以从协商过程中恢复出来，且恢复的锚点可预测未参与的协商回合。
- 锚点解释了一种传统共识规则禁止的行为：智能体对正确答案的置信度可以超越所有初始信念形成的凸包范围。
- 在三个开放权重模型家族上的实验表明，锚点影响强度相近，但锚点位置各异。
- 仅当锚点位置远离初始意见时，协商才会突破凸包范围，此时必须使用完整闭环模型进行描述。
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Hidden Anchors in Multi-Agent LLM Deliberation

View PDF HTML (experimental)Abstract:Multi-agent LLM deliberation, where agents exchange and revise answers over several rounds, is increasingly used to improve reasoning and accuracy, yet how and why it works is rarely modelled. Such deliberation mirrors how humans reach decisions. As social animals we are pulled both by the group, the herd effect that classical opinion-dynamics models such as DeGroot and Friedkin--Johnsen capture, and by our own internal belief, which they do not. We model multi-agent deliberation as a closed-loop dynamical system in which each agent carries a hidden internal belief, its anchor, that continually pulls its opinion regardless of its neighbours. We show this anchor can be recovered from the deliberation alone, and that it explains a behaviour classical consensus rules forbid: an agent's confidence in the correct answer can climb past where any agent started, escaping the space (convexhull) formed by the initial beliefs. Checking whether the recovered anchor also predicts held-out runs (generalizes) gives a simple test for when a model is truly driven bysuch an anchor. Across three open-weight model families this is a spectrum, not all-or-nothing. All anchors' influence are about equally strongly, but they differ in where the anchor sits, and only when it sits far from the initial opinions does deliberation escape the hull and need the full closed-loop model.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.