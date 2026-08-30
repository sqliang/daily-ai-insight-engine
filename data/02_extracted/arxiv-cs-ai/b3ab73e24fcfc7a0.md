---
title: Ontology-Grounded Project Memory for Coding Agents
source: https://arxiv.org/abs/2608.13662
author:
- '[[James Adam]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: 'arXiv:2608.13662v1 Announce Type: new Abstract: Coding agents have become
  the primary means of generating new code in many software projects, and the resulting
  velocity of changes makes keeping track of the reasons behind those changes challenging.
  This paper introduces MOOSEDev, a system designed to give coding agents structured,
  ontology-grounded project memory. The system captures architectural decisions, lessons,
  constraints, and rationales in a knowledge graph exposed to agents via a Model Context
  Protocol (MCP) interface. Records carry lifecycle status, provenance, and supersession
  links, queryable via MOOSE, a proprietary neurosymbolic engine that treats the symbolic
  layer as the primary reasoning substrate. We compared MOOSEDev against a production
  vector-memory tool on a neutral public corpus of 835 typed records. MOOSEDev returned
  the expected answer set essentially in full (0.98-1.00) on supersession, set-completeness,
  and negation questions, whereas the baseline''s top-k retrieval surfaced between
  6% and 27%. Conversely, relevance recall and token cost were largely equivalent
  between the two systems. We also describe a temporal commit-history bootstrap of
  our own codebase, a pre-registered live trial, and lessons learned.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b3ab73e24fcfc7a0
source_type: academic_paper
tldr: 本文介绍 MOOSEDev，一个为编码智能体提供结构化、基于本体（ontology）的项目记忆系统，将架构决策、经验教训等记录存入知识图谱并通过 MCP
  接口暴露。在 835 条记录基准上，其在取代、集合完整性与否定问题上的答案召回率远超向量记忆基线。
objective_summary: 本文为一篇 arXiv 论文，提出 MOOSEDev，一个为编码智能体提供结构化、基于本体的项目记忆系统。该系统将架构决策、经验教训、约束与设计理由捕获到知识图谱中，通过
  Model Context Protocol（MCP）接口暴露，并借助将符号层作为主要推理基底的专有神经符号引擎 MOOSE 查询记录。作者在包含 835 条类型化记录的公共语料上对比
  MOOSEDev 与生产级向量记忆工具，结果显示前者在取代、集合完整性与否定问题上几乎完整返回期望答案集（0.98-1.00），而基线 top-k 检索仅返回
  6%-27%，相关性与 token 成本两者大致相当。论文还报告了基于提交历史的时序引导、预注册在线试验及经验教训。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - MCP
  - knowledge graph
  - neurosymbolic engine
  - ontology
  - vector memory retrieval
  key_people: []
key_logic_flow:
- MOOSEDev 是一个为编码智能体提供结构化、基于本体（ontology）的项目记忆的系统。
- 该系统将架构决策、经验教训、约束与设计理由捕获到知识图谱中，并通过 MCP 接口暴露给智能体。
- 记录携带生命周期状态、来源与取代链接，可通过将符号层作为主要推理基底的专有神经符号引擎 MOOSE 查询。
- 在 835 条类型化记录的公共语料上，MOOSEDev 在取代、集合完整性与否定问题上几乎完整返回期望答案集（0.98-1.00），而基线 top-k 检索仅返回
  6% 至 27%。
- 在相关性召回与 token 成本方面，MOOSEDev 与生产级向量记忆工具大致相当。
- 论文还描述了基于提交历史的时序引导方法、预注册的在线试验以及经验教训。
object_mentions:
- object_type: project
  name: MOOSEDev
  canonical_name: MOOSEDev
  url: https://arxiv.org/abs/2608.13662
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 本文介绍 MOOSEDev，一个旨在为编码智能体提供结构化、基于本体（ontology）的项目记忆的系统。
  - MOOSEDev 将架构决策、经验教训、约束与设计理由捕获到知识图谱中，并通过 MCP 接口暴露给智能体。
  article_id: b3ab73e24fcfc7a0
- object_type: project
  name: MOOSE
  canonical_name: MOOSE
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 记录携带生命周期状态、来源与取代链接，可通过 MOOSE 这一将符号层作为主要推理基底的专有神经符号引擎查询。
  article_id: b3ab73e24fcfc7a0
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Ontology-Grounded Project Memory for Coding Agents

View PDF HTML (experimental)Abstract:Coding agents have become the primary means of generating new code in many software projects, and the resulting velocity of changes makes keeping track of the reasons behind those changes challenging. This paper introduces MOOSEDev, a system designed to give coding agents structured, ontology-grounded project memory. The system captures architectural decisions, lessons, constraints, and rationales in a knowledge graph exposed to agents via a Model Context Protocol (MCP) interface. Records carry lifecycle status, provenance, and supersession links, queryable via MOOSE, a proprietary neurosymbolic engine that treats the symbolic layer as the primary reasoning substrate. We compared MOOSEDev against a production vector-memory tool on a neutral public corpus of 835 typed records. MOOSEDev returned the expected answer set essentially in full (0.98-1.00) on supersession, set-completeness, and negation questions, whereas the baseline's top-k retrieval surfaced between 6% and 27%. Conversely, relevance recall and token cost were largely equivalent between the two systems. We also describe a temporal commit-history bootstrap of our own codebase, a pre-registered live trial, and lessons learned.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.