---
title: 'SEAGym: An Evaluation Environment for Self-Evolving LLM Agents'
source: https://arxiv.org/abs/2606.17546
author:
- '[[Congjie Zheng, Chuanyi Xue, Bin Liang, Jun Yang, Changshui Zhang]]'
published: '2026-06-17'
created: '2026-06-17'
description: 'arXiv:2606.17546v1 Announce Type: new Abstract: Self-evolving LLM-based
  agents improve mainly by changing their agent harness: the structured execution
  layer around a base model, including prompts, memory, tools, middleware, runtime
  state, and the model-tool interaction loop. Existing evaluations often reduce this
  process to isolated task scores or a single sequential curve, obscuring whether
  an update produces reusable improvement, overfits recent tasks, increases cost,
  or harms older behavior. We introduce SEAGym, an evaluation environment for measuring
  agent harness updates across training, validation, test, replay, and cost records.
  SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources
  with train batches, frozen update-validation, held-out ID and OOD transfer views,
  replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym
  on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch
  protocol. The results show that these evaluation views provide complementary signals
  about the evolution process: frequent updates may fail to improve held-out performance,
  useful intermediate snapshots may collapse later, and source diversity and model
  backend can affect harness reliability.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 195d89ae5bcccbcb
---

# Computer Science > Artificial Intelligence

# Title:SEAGym: An Evaluation Environment for Self-Evolving LLM Agents

View PDF HTML (experimental)Abstract:Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.