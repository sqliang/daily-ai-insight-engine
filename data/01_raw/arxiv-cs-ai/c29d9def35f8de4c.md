---
title: No Universal Signal Predicts Sample-Level LLM Regression under Version Updates
source: https://arxiv.org/abs/2608.13607
author:
- '[[Jia Sheng, Yiwei Lu]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: 'arXiv:2608.13607v1 Announce Type: new Abstract: Frontier LLMs are updated
  frequently and typically outperform their predecessors in aggregate. But aggregate
  gains say little about individual samples: an update can still cause sample-level
  regression, where a response correct under the old model becomes incorrect under
  the new one. This paper studies how to predict such regressions from signals available
  at inference time. We compare single-model signals (confidence, logit margin, attention
  entropy) against cross-version signals (output KL divergence, likelihood drift,
  token-level KL, representation drift) under a unified added-value test that isolates
  each signal''s gain over a confidence baseline. Across six benchmarks in three task
  families (multiple-choice question answering, or MCQ; math reasoning; code generation)
  and six model update pairs, we find that (1) signal effectiveness is task-dependent:
  confidence is strongest on MCQ and simpler math, while likelihood/KL signals give
  the most frequent gains on harder math and code; (2) no signal is universally best
  across model updates either; and (3) some cross-version signals stay informative
  even when confidence fails, including without labels, which supports a proof-of-concept
  selective fallback that routes high-risk samples back to the old model. Practitioners
  can use these task-level patterns to choose which regression signal to trust for
  a given update. Code is available at https://github.com/jiashengsally/llm-regression-signals.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: c29d9def35f8de4c
---

# Computer Science > Artificial Intelligence

# Title:No Universal Signal Predicts Sample-Level LLM Regression under Version Updates

View PDF HTML (experimental)Abstract:Frontier LLMs are updated frequently and typically outperform their predecessors in aggregate. But aggregate gains say little about individual samples: an update can still cause sample-level regression, where a response correct under the old model becomes incorrect under the new one. This paper studies how to predict such regressions from signals available at inference time. We compare single-model signals (confidence, logit margin, attention entropy) against cross-version signals (output KL divergence, likelihood drift, token-level KL, representation drift) under a unified added-value test that isolates each signal's gain over a confidence baseline. Across six benchmarks in three task families (multiple-choice question answering, or MCQ; math reasoning; code generation) and six model update pairs, we find that (1) signal effectiveness is task-dependent: confidence is strongest on MCQ and simpler math, while likelihood/KL signals give the most frequent gains on harder math and code; (2) no signal is universally best across model updates either; and (3) some cross-version signals stay informative even when confidence fails, including without labels, which supports a proof-of-concept selective fallback that routes high-risk samples back to the old model. Practitioners can use these task-level patterns to choose which regression signal to trust for a given update. Code is available at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.