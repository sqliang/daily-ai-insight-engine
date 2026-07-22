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
tldr: 该论文将多智能体LLM讨论建模为闭环动力系统，提出每个智能体携带隐藏的"锚点"（内部信念），该锚点可仅从讨论过程恢复，并解释了智能体置信度为何能超越初始信念的凸包范围。
objective_summary: 研究者将多智能体LLM讨论过程建模为一个闭环动力系统，每个智能体持有隐藏的内部信念锚点，该锚点持续牵引其观点而不受邻居意见影响，超越了经典共识模型（DeGroot和Friedkin-Johnsen）的解释能力。论文证明该锚点可仅从讨论过程恢复，并解释了智能体对正确答案的置信度能超过任何初始信念所在凸包范围的现象。在多个开源模型系列上的验证显示，锚点影响程度相似但位置不同，只有当锚点远离初始观点时讨论结果才会逃出凸包，此时需要完整的闭环模型来解释。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Multi-Agent Systems
  key_people: []
key_logic_flow:
- 论文将多智能体LLM讨论建模为闭环动力系统，每个智能体持有一个隐藏的内部信念锚点，该锚点持续牵引其观点而不受邻居意见影响。
- 该模型超越了经典共识模型（如DeGroot和Friedkin-Johnsen），后者只能捕捉群体效应而无法模拟个体内部信念的持续牵引。
- 研究者证明锚点可以仅从讨论过程本身恢复，无需外部知识或观测内部状态。
- 锚点模型解释了经典共识规则无法解释的现象：智能体对正确答案的置信度可以超过任何初始信念所在的凸包范围。
- 在多个开源模型系列上的验证显示，所有锚点的影响程度大致相当，但锚点位置存在差异。
- 只有当锚点远离初始观点时，讨论结果才会逃出凸包，此时需要完整的闭环模型来解释讨论过程。
extract_result: success
object_mentions:
- object_type: paper
  name: Hidden Anchors in Multi-Agent LLM Deliberation
  canonical_name: Hidden Anchors in Multi-Agent LLM Deliberation
  url: https://arxiv.org/abs/2606.19494
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文将多智能体LLM讨论建模为闭环动力系统，提出每个智能体携带一个隐藏的内部信念锚点，该锚点持续牵引其观点而不受邻居意见影响。
  - 论文证明该锚点可以仅从讨论过程本身恢复，并解释了智能体置信度为何能超越初始信念的凸包范围，这是经典共识模型无法解释的。
  - 在多个开源模型系列上的验证显示所有锚点的影响程度相似，但锚点位置不同，只有当锚点远离初始观点时讨论结果才会逃出凸包。
  article_id: 0d33fa55dddfc97c
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