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
pipeline_stage: ingested
id: cedf57bb6ac50ed2
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