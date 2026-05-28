---
title: 'Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems'
source: https://arxiv.org/abs/2605.26302
author:
- '[[Jianing Zhu, Yeonju Ro, John Robertson, Kevin Wang, Junbo Li, Haris Vikalo, Aditya
  Akella, Zhangyang Wang]]'
published: '2026-05-27'
created: '2026-05-28'
description: 'arXiv:2605.26302v1 Announce Type: new Abstract: Long-lived AI agents
  are increasingly deployed as persistent operational systems, yet they are still
  evaluated like freshly initialized models. Day-one benchmarks miss a basic systems
  question: how long does an agent remain reliable after deployment? Even when model
  weights are frozen, an agent''s effective state keeps changing as it compresses
  interaction history, retrieves from a growing memory store, revises facts after
  updates, and undergoes routine maintenance. Reliability therefore becomes a lifespan
  property of the full agent harness, not only a snapshot property of the base model.
  We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan
  engineering: measuring not only whether deployed agents degrade, but what form the
  degradation takes and where repair should target. AgingBench organizes agent aging
  into four mechanisms: compression aging, interference aging, revision aging, and
  maintenance aging. To diagnose these failures, AgingBench uses temporal dependency
  graphs and paired counterfactual probes that produce diagnostic profiles for the
  write, retrieval, and utilization stages of the memory pipeline. Across 7 scenarios,
  14 models, multiple memory policies, and both runner-controlled and autonomous agents,
  over ~400 runs spanning 8 - 200 sessions show that agent aging is not one-dimensional:
  behavioral tests can remain clean while factual precision decays; derived-state
  tracking can collapse sharply within a single model; and the same wrong answer can
  require different repairs depending on what the diagnostic profile points to. These
  results suggest that reliable agent deployment requires lifespan evaluation, mechanism-level
  diagnosis, and stage-targeted repair, not only stronger day-one models.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 27fbaeab8c07a7da
---

# Computer Science > Artificial Intelligence

# Title:Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems

View PDF HTML (experimental)Abstract:Long-lived AI agents are increasingly deployed as persistent operational systems, yet they are still evaluated like freshly initialized models. Day-one benchmarks miss a basic systems question: how long does an agent remain reliable after deployment? Even when model weights are frozen, an agent's effective state keeps changing as it compresses interaction history, retrieves from a growing memory store, revises facts after updates, and undergoes routine maintenance. Reliability therefore becomes a lifespan property of the full agent harness, not only a snapshot property of the base model. We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan engineering: measuring not only whether deployed agents degrade, but what form the degradation takes and where repair should target. AgingBench organizes agent aging into four mechanisms: compression aging, interference aging, revision aging, and maintenance aging. To diagnose these failures, AgingBench uses temporal dependency graphs and paired counterfactual probes that produce diagnostic profiles for the write, retrieval, and utilization stages of the memory pipeline. Across 7 scenarios, 14 models, multiple memory policies, and both runner-controlled and autonomous agents, over ~400 runs spanning 8 - 200 sessions show that agent aging is not one-dimensional: behavioral tests can remain clean while factual precision decays; derived-state tracking can collapse sharply within a single model; and the same wrong answer can require different repairs depending on what the diagnostic profile points to. These results suggest that reliable agent deployment requires lifespan evaluation, mechanism-level diagnosis, and stage-targeted repair, not only stronger day-one models.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.