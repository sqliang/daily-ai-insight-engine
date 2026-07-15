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
tldr: 研究发现LLM智能体在信号游戏中，记忆架构比信道容量更能决定语言能否成功涌现。
objective_summary: 研究者使用LLM智能体在Lewis信号游戏中测试五种记忆架构。拥有持久私有笔记本的智能体在信道容量为25时达到最高协调得分0.867±0.023。无状态智能体在高容量时性能崩溃。记忆架构比信道容量更能决定语言能否稳定涌现。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Lewis signaling game
  key_people: []
key_logic_flow:
- 研究者在Lewis信号游戏中，让LLM智能体担任发送者和接收者，仅通过交互历史协调出一个共享编码系统。
- 实验比较了五种记忆架构在不同信道容量下的表现，发现记忆架构比信道容量对语言涌现的影响更大。
- 拥有持久私有笔记本的智能体在信道容量为25时达到最佳协调效果（0.867±0.023），且能避免无状态智能体在高容量时出现的性能崩溃。
- 无状态智能体仅在中等信道容量时达到最佳表现，词汇量超过滚动上下文窗口追踪能力后性能下降。
- 信息瓶颈理论预测最优容量等于物体数量，但实验发现瓶颈容量（容量=8）反而是脆弱点，冗余容量普遍更优。
- 信道容量本身无法预测协调效果，必须结合记忆架构才能理解信号如何演变为稳定语言。
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