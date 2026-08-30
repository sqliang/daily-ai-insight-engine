---
title: 'Automata from Agent Traces: Failure and Next-Step Prediction'
source: https://arxiv.org/abs/2608.23670
author:
- '[[Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton
  Da Costa, Ilham Wicaksono, Adriano Koshiyama]]'
published: '2026-08-26'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
- '2026-08-27'
description: 'arXiv:2608.23670v1 Announce Type: new Abstract: LLM-based agents execute
  multi-step tasks, but their behavioral structure remains opaque: long unstructured
  traces resist the safety auditing and runtime monitoring that deployment requires.
  Existing approaches operate per-trace or success-only, so they miss the cross-run
  topology that links next-step and failure prediction. To recover that shared structure,
  we collapse an entire trace corpus into a single, compact finite-state machine (FSM)
  that serves as a structural substrate for the otherwise unpredictable behavior of
  LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay
  held-out data at >=0.997 fitness with near-identical topology across splits, and
  build in milliseconds. This substrate addresses both prediction goals. For next-step
  prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched
  dataset. For failure prediction, per-state behavioral features reach held-out AUROC
  up to 0.94, and an online monitor ranks failing runs above passing ones from a partial
  trace, triggering early stopping well before completion. Behavioral topology thus
  appears shaped more by the deployment harness than by the LLM, providing a model-agnostic
  structural primitive for safety auditing and runtime monitoring.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: c69affdc82d44b2a
---

# Computer Science > Artificial Intelligence

# Title:Automata from Agent Traces: Failure and Next-Step Prediction

View PDF HTML (experimental)Abstract:LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwise unpredictable behavior of LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay held-out data at >=0.997 fitness with near-identical topology across splits, and build in milliseconds. This substrate addresses both prediction goals. For next-step prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched dataset. For failure prediction, per-state behavioral features reach held-out AUROC up to 0.94, and an online monitor ranks failing runs above passing ones from a partial trace, triggering early stopping well before completion. Behavioral topology thus appears shaped more by the deployment harness than by the LLM, providing a model-agnostic structural primitive for safety auditing and runtime monitoring.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.