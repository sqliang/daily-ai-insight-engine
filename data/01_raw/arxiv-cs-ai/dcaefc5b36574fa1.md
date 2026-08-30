---
title: 'FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated
  Learning'
source: https://arxiv.org/abs/2608.20518
author:
- '[[Jiajun Wu, Zirui Wang, Jiayu Zhou, Qiang Ye, Steve Drew]]'
published: '2026-08-24'
created: '2026-08-24'
manifest_dates:
- '2026-08-24'
description: 'arXiv:2608.20518v1 Announce Type: new Abstract: In Federated Learning
  (FL), the communication topology is a runtime variable rather than a fixed design
  choice, since links and edge devices drop in and out during training. Each round,
  the server must commit three coupled decisions, namely the communication topology,
  per-client resource allocation, and the aggregation rule for combining local updates.
  Recent agentic systems have begun bringing large language models (LLM) into FL,
  but the existing line of work either operates at setup time or handles a single
  runtime dimension such as client selection. We propose FL-MAESTRO, a multi-agent
  orchestrator that makes the joint runtime FL decision directly through three specialist
  LLM agents, one per decision dimension. A coordinator combines their analyses into
  a single decision, and a non-LLM feasibility check confirms it before the round
  executes. Because the orchestrator consumes the server''s predicted-failure list,
  it withholds clients whose updates would never be aggregated, which removes the
  dominant source of wasted round energy in classical FL on volatile edge networks.
  Because client state is read as natural-text profiles, the same orchestrator extends
  to heterogeneous device classes without per-class energy models. On a non-IID CIFAR-10
  benchmark, FL-MAESTRO matches the accuracy of the strongest energy-aware baseline
  while cutting wasted round energy from over a third to near zero. Code is available
  at https://github.com/denoslab/FL-MAESTRO.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: dcaefc5b36574fa1
---

# Computer Science > Artificial Intelligence

# Title:FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning

View PDF HTML (experimental)Abstract:In Federated Learning (FL), the communication topology is a runtime variable rather than a fixed design choice, since links and edge devices drop in and out during training. Each round, the server must commit three coupled decisions, namely the communication topology, per-client resource allocation, and the aggregation rule for combining local updates. Recent agentic systems have begun bringing large language models (LLM) into FL, but the existing line of work either operates at setup time or handles a single runtime dimension such as client selection. We propose FL-MAESTRO, a multi-agent orchestrator that makes the joint runtime FL decision directly through three specialist LLM agents, one per decision dimension. A coordinator combines their analyses into a single decision, and a non-LLM feasibility check confirms it before the round executes. Because the orchestrator consumes the server's predicted-failure list, it withholds clients whose updates would never be aggregated, which removes the dominant source of wasted round energy in classical FL on volatile edge networks. Because client state is read as natural-text profiles, the same orchestrator extends to heterogeneous device classes without per-class energy models. On a non-IID CIFAR-10 benchmark, FL-MAESTRO matches the accuracy of the strongest energy-aware baseline while cutting wasted round energy from over a third to near zero. Code is available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.