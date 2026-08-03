---
title: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures
source: https://arxiv.org/abs/2607.28802
author:
- '[[Harsh Raj, Vipul Gupta, Anas Mahmoud, Razvan-Gabriel Dumitru, Darvin Yi, Aakash
  Sabharwal, Yunzhong He]]'
published: '2026-08-03'
created: '2026-08-03'
manifest_dates:
- '2026-08-03'
description: 'arXiv:2607.28802v1 Announce Type: new Abstract: Existing evaluations
  often reduce agent failures to system-level outcomes, obscuring where the fault
  originated and which intervention would improve the agent system. This creates a
  repair-assignment problem: the same visible failure may call for model post-training,
  harness engineering, environment redesign, or benchmark repair depending on its
  source. Because agent behavior emerges from interactions among models, harnesses,
  users, tools, memory, and environments, outcome-level labels are often insufficient
  for improvement. Most failure taxonomies do little to resolve this problem because
  they are benchmark-specific and lack a shared structure. We introduce an interaction-centric
  taxonomy that localizes failures to the interactions in which they originate and
  identifies the responsible component. It organizes 41 failure modes by assigning
  each to an edge between two components and a fault side indicating where the repair
  belongs. This makes the taxonomy actionable: model-side failures identify targets
  for post-training, harness-side failures point to scaffolding and tool-integration
  fixes, and environment or grader failures reveal evaluation conditions requiring
  redesign. The schema applies across agent architectures, from coding assistants
  to long-horizon personal assistants and multi-agent systems. We ground the taxonomy
  in worked examples from public benchmarks, model system cards, published reports,
  and logged agent trajectories, and evaluate its reproducibility using independent
  reasoning agents as judges. Across four frontier models, the strongest judge reaches
  Cohen''s $\kappa=0.76$ against human category labels, suggesting that the categories
  capture shared structure rather than annotator-specific preferences.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 6cfdb395f3efb4ea
---

# Computer Science > Artificial Intelligence

# Title:Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures

View PDF HTML (experimental)Abstract:Existing evaluations often reduce agent failures to system-level outcomes, obscuring where the fault originated and which intervention would improve the agent system. This creates a repair-assignment problem: the same visible failure may call for model post-training, harness engineering, environment redesign, or benchmark repair depending on its source. Because agent behavior emerges from interactions among models, harnesses, users, tools, memory, and environments, outcome-level labels are often insufficient for improvement. Most failure taxonomies do little to resolve this problem because they are benchmark-specific and lack a shared structure. We introduce an interaction-centric taxonomy that localizes failures to the interactions in which they originate and identifies the responsible component. It organizes 41 failure modes by assigning each to an edge between two components and a fault side indicating where the repair belongs. This makes the taxonomy actionable: model-side failures identify targets for post-training, harness-side failures point to scaffolding and tool-integration fixes, and environment or grader failures reveal evaluation conditions requiring redesign. The schema applies across agent architectures, from coding assistants to long-horizon personal assistants and multi-agent systems. We ground the taxonomy in worked examples from public benchmarks, model system cards, published reports, and logged agent trajectories, and evaluate its reproducibility using independent reasoning agents as judges. Across four frontier models, the strongest judge reaches Cohen's $\kappa=0.76$ against human category labels, suggesting that the categories capture shared structure rather than annotator-specific preferences.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.