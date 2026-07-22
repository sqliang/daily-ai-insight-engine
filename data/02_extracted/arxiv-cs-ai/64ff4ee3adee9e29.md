---
title: 'From Signals to Structure: How Memory Architecture Drives Language Emergence
  in LLM Agents'
source: https://arxiv.org/abs/2607.00233
author:
- '[[Yashar Talebirad, Eden Redman, Ali Parsaee, Osmar R. Zaiane]]'
published: '2026-07-02'
created: '2026-07-02'
description: 'arXiv:2607.00233v1 Announce Type: new Abstract: How do two agents invent
  a shared language from scratch? In a Lewis signaling game, a sender and receiver
  must coordinate on a code using only their interaction history. We study five memory
  architectures across varying channel configurations with LLM agents and find that
  memory architecture matters more than channel capacity. Agents with a persistent
  private notebook benefit from surplus channel capacity and avoid the high-capacity
  collapse seen in stateless agents, achieving the most reliable coordination ($0.867
  \pm 0.023$ at capacity = 25). Stateless agents peak at moderate capacity and then
  degrade as the vocabulary grows beyond what a rolling context window can track The
  notebook externalizes learned conventions, freeing agents from having to re-derive
  codes each round. An information bottleneck-inspired argument predicts an optimal
  capacity equal to the number of objects. Instead, the bottleneck (capacity = 8)
  proves to be a fragility point, and surplus capacity is generally better. We show
  that channel capacity alone cannot predict coordination; memory architecture determines
  whether agents turn interaction history into stable conventions, and both dimensions
  are needed to understand how signals become language.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 64ff4ee3adee9e29
manifest_dates:
- '2026-07-02'
source_type: academic_paper
tldr: 一篇研究 LLM 智能体如何在 Lewis 信号游戏中通过交互历史自发发明共享语言的研究论文。实验表明，记忆架构比通道容量更重要，带有持久私人笔记本的智能体实现了最可靠的协调（容量为
  25 时得分为 0.867），而通道容量本身无法单独预测语言协调效果。
objective_summary: 该研究在 Lewis 信号游戏框架下，让发送者和接收者 LLM 智能体仅通过交互历史进行协调以发明共享代码。研究者测试了五种记忆架构和多种通道配置，发现记忆架构的影响远超通道容量：带有持久私人笔记本的智能体最高获得
  0.867 的协调得分，而无状态智能体在中等容量后性能反而随词汇量增长而下降。一个基于信息瓶颈的理论预测最优容量等于对象数量，但实验显示容量为 8 时是脆弱点，而过剩容量普遍更好。研究得出结论：记忆架构决定了智能体是否将交互历史转化为稳定约定，通道容量和记忆架构两者结合才能解释信号如何演变为语言。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM
  - Lewis signaling game
  key_people: []
key_logic_flow:
- 研究在 Lewis 信号游戏框架下让两个 LLM 智能体（发送者和接收者）仅通过交互历史协调出一套共享代码。
- 实验比较了五种记忆架构在不同通道容量配置下的表现，发现记忆架构对协调效果的影响大于通道容量。
- 带有持久私人笔记本的智能体在容量为 25 时达到最高协调得分 0.867，避免了无状态智能体在高容量下的性能崩溃。
- 无状态智能体在中等容量达到性能峰值后，随着词汇量超出滚动上下文窗口的追踪能力而性能下降。
- 基于信息瓶颈的理论预测最优容量等于对象数量（8），但实验显示容量 8 是脆弱点，过剩容量效果普遍更好。
- 研究表明通道容量无法单独预测语言协调效果，必须结合记忆架构才能理解信号如何演变为稳定语言。
specialized_tags:
  paper:
    paperTitle: 'From Signals to Structure: How Memory Architecture Drives Language
      Emergence in LLM Agents'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: NLP
    methodType: LLM-based
extract_result: success
object_mentions:
- object_type: paper
  name: 'From Signals to Structure: How Memory Architecture Drives Language Emergence
    in LLM Agents'
  canonical_name: From Signals to Structure
  url: https://arxiv.org/abs/2607.00233
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文在 Lewis 信号游戏框架下研究五种记忆架构对 LLM 智能体自发发明共享语言的影响。
  - 实验表明带有持久私人笔记本的智能体在容量为 25 时达到最高协调得分 0.867，而无状态智能体在中等容量后性能下降。
  article_id: 64ff4ee3adee9e29
---

# Computer Science > Artificial Intelligence

# Title:From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents

View PDF HTML (experimental)Abstract:How do two agents invent a shared language from scratch? In a Lewis signaling game, a sender and receiver must coordinate on a code using only their interaction history. We study five memory architectures across varying channel configurations with LLM agents and find that memory architecture matters more than channel capacity. Agents with a persistent private notebook benefit from surplus channel capacity and avoid the high-capacity collapse seen in stateless agents, achieving the most reliable coordination ($0.867 \pm 0.023$ at capacity = 25). Stateless agents peak at moderate capacity and then degrade as the vocabulary grows beyond what a rolling context window can track The notebook externalizes learned conventions, freeing agents from having to re-derive codes each round. An information bottleneck-inspired argument predicts an optimal capacity equal to the number of objects. Instead, the bottleneck (capacity = 8) proves to be a fragility point, and surplus capacity is generally better. We show that channel capacity alone cannot predict coordination; memory architecture determines whether agents turn interaction history into stable conventions, and both dimensions are needed to understand how signals become language.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.