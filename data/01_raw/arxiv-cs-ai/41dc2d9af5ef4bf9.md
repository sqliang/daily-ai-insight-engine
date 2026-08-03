---
title: 'SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema
  Induction and Fusion from Text'
source: https://arxiv.org/abs/2607.21610
author:
- '[[Miaobo Hu, Xiaobo Guo, Shuhao Hu, Bokun Wang, Rui Chen, Xin Wang, Daren Zha,
  Jun Xiao]]'
published: '2026-07-27'
created: '2026-07-27'
manifest_dates:
- '2026-07-27'
description: 'arXiv:2607.21610v1 Announce Type: new Abstract: Schema graphs are an
  upstream bottleneck of schema-grounded information extraction and knowledge graph
  construction, yet most extraction systems assume the schema is already available.
  We introduce SCOPE (Schema Construction and Ontology-induction Pipeline Evaluation),
  a train-text-only benchmark for corpus-to-schema induction and optional schema fusion
  from raw text, built from 24 public information extraction sources (15 RE and 9
  EE) normalized into evaluation-only gold schema graphs; its core event-extraction
  target covers event types and within-event argument roles, with inter-event links
  reported separately. We present SCION (Schema Construction and Induction with Ontology
  Normalization), an auditable reference pipeline rather than a new extraction architecture;
  it constructs candidate spaces from train text and restricts naming, merging, filtering,
  validation, and conservative fusion to candidate-linked evidence under strict JSON
  contracts. On the SCOPE core suite, SCION-lite attains the highest F1 among released
  source-schema references, Text2Onto-style, LLM-only, and matched extract-then-aggregate
  baselines under Literal, Fuzzy, Continuous, and Graph schema-graph metrics, while
  the compact open-model SCION-RL variant reduces reliance on proprietary LLM schema
  engineers. These results are reported against normalized typed-edge targets rather
  than as claims that induced schemas surpass human ontology design; the release includes
  evidence-linked outputs, parse/fallback logs, candidate retention/merging logs,
  run manifests, code, and benchmark packages at https://github.com/wandugu/paper_scion.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 41dc2d9af5ef4bf9
---

# Computer Science > Artificial Intelligence

# Title:SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema Induction and Fusion from Text

View PDFAbstract:Schema graphs are an upstream bottleneck of schema-grounded information extraction and knowledge graph construction, yet most extraction systems assume the schema is already available. We introduce SCOPE (Schema Construction and Ontology-induction Pipeline Evaluation), a train-text-only benchmark for corpus-to-schema induction and optional schema fusion from raw text, built from 24 public information extraction sources (15 RE and 9 EE) normalized into evaluation-only gold schema graphs; its core event-extraction target covers event types and within-event argument roles, with inter-event links reported separately. We present SCION (Schema Construction and Induction with Ontology Normalization), an auditable reference pipeline rather than a new extraction architecture; it constructs candidate spaces from train text and restricts naming, merging, filtering, validation, and conservative fusion to candidate-linked evidence under strict JSON contracts. On the SCOPE core suite, SCION-lite attains the highest F1 among released source-schema references, Text2Onto-style, LLM-only, and matched extract-then-aggregate baselines under Literal, Fuzzy, Continuous, and Graph schema-graph metrics, while the compact open-model SCION-RL variant reduces reliance on proprietary LLM schema engineers. These results are reported against normalized typed-edge targets rather than as claims that induced schemas surpass human ontology design; the release includes evidence-linked outputs, parse/fallback logs, candidate retention/merging logs, run manifests, code, and benchmark packages at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.