---
title: 'Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents'
source: https://arxiv.org/abs/2608.13574
author:
- '[[Bo Jin, Qiang Jiao, Xin Tong]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: 'arXiv:2608.13574v1 Announce Type: new Abstract: LLM agents increasingly
  operate as execution systems that invoke tools, modify local state, use persistent
  memory, and interact with external protocols. These capabilities make agents useful,
  but they also introduce risks related to over-privileged actions, weak auditability,
  prompt injection, tool poisoning, and uncontrolled side effects. This paper presents
  Agentao, a governed local-first runtime for tool-using LLM agents. Agentao separates
  model-generated action proposals from host-authorized execution through a layered
  architecture consisting of host-facing surfaces, a host contract, a runtime core,
  a permission-mediated tool system, and supporting subsystems for memory, replay,
  plugins, skills, sub-agents, and protocol integration. We describe the motivation,
  threat model, design goals, governance model, execution pipeline, and structured
  event interface of the system. Agentao does not provide formal safety guarantees;
  rather, it demonstrates how permissions, state, protocol boundaries, and execution
  traces can be made explicit runtime abstractions for building agents that are more
  governable, inspectable, and suitable for host-controlled local environments. The
  code is publicly available at https://github.com/jin-bo/agentao.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cedf57bb6ac50ed2
source_type: academic_paper
tldr: Agentao 是一个面向工具调用型 LLM 智能体的本地优先受治理运行时。它通过分层架构将模型生成的动作提案与主机授权的执行相分离，把权限、状态、协议边界和执行轨迹作为显式运行时抽象，论文代码已公开。
objective_summary: 论文提出 Agentao，一个面向工具调用型 LLM 智能体的本地优先受治理运行时。针对智能体执行带来的过度授权、弱可审计性、提示注入、工具投毒和失控副作用等风险，系统采用分层架构将模型生成的动作提案与主机授权的执行分离。该架构包含主机表面、主机契约、运行时核心、权限中介工具系统，以及内存、回放、插件、技能、子智能体和协议集成等支撑子系统。Agentao
  不提供正式安全保证，而是将权限、状态、协议边界和执行轨迹作为显式运行时抽象，目标是构建更可治理、可检查、适合主机控制本地环境的智能体，代码已公开。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM Agents
  - Prompt Injection
  - Tool Poisoning
  key_people: []
key_logic_flow:
- 论文指出 LLM 智能体作为执行系统会调用工具、修改本地状态、使用持久内存并与外部协议交互，由此带来过度授权、弱可审计性、提示注入、工具投毒和失控副作用等风险。
- Agentao 的核心设计是将模型生成的动作提案与主机授权的执行相分离，通过分层架构实现治理与控制。
- 该分层架构由主机表面、主机契约、运行时核心、权限中介工具系统以及内存、回放、插件、技能、子智能体和协议集成等支撑子系统组成。
- Agentao 明确不提供正式的安全保证，其思路是把权限、状态、协议边界和执行轨迹做成显式运行时抽象。
- 系统目标是构建更可治理、可检查、适合主机控制本地环境的智能体，论文代码已公开提供。
object_mentions:
- object_type: project
  name: Agentao
  canonical_name: Agentao
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Agentao 是一个面向工具调用型 LLM 智能体的本地优先受治理运行时，将模型生成的动作提案与主机授权的执行分离。
  - 系统采用分层架构，包含主机表面、主机契约、运行时核心、权限中介工具系统及内存、回放、插件、技能、子智能体和协议集成等子系统。
  - Agentao 不提供正式安全保证，而是将权限、状态、协议边界和执行轨迹作为显式运行时抽象，论文代码已公开。
  article_id: cedf57bb6ac50ed2
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents

View PDF HTML (experimental)Abstract:LLM agents increasingly operate as execution systems that invoke tools, modify local state, use persistent memory, and interact with external protocols. These capabilities make agents useful, but they also introduce risks related to over-privileged actions, weak auditability, prompt injection, tool poisoning, and uncontrolled side effects. This paper presents Agentao, a governed local-first runtime for tool-using LLM agents. Agentao separates model-generated action proposals from host-authorized execution through a layered architecture consisting of host-facing surfaces, a host contract, a runtime core, a permission-mediated tool system, and supporting subsystems for memory, replay, plugins, skills, sub-agents, and protocol integration. We describe the motivation, threat model, design goals, governance model, execution pipeline, and structured event interface of the system. Agentao does not provide formal safety guarantees; rather, it demonstrates how permissions, state, protocol boundaries, and execution traces can be made explicit runtime abstractions for building agents that are more governable, inspectable, and suitable for host-controlled local environments. The code is publicly available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.