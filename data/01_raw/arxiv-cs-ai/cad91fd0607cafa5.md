---
title: 'RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge
  Injection'
source: https://arxiv.org/abs/2607.24771
author:
- '[[Yan Hong, Wei Li, Kedong Xiu, Jun Lan, Shuheng Zhou, Zhongcai Lyu, Huijia Zhu,
  Weiqiang Wang, Jianfu Zhang]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 'arXiv:2607.24771v1 Announce Type: new Abstract: Knowledge injection
  updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting
  full authoritative answers can cause drift in non-updated behavior. Online distillation
  mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned
  distillation provides coarse supervision: it can under-emphasize reference-supported
  rollout tokens and supervise omitted facts only indirectly. We introduce RoCo-ACE,
  a rollout-conditioned online distillation objective for knowledge injection. RoCo
  uses same-rollout reference-free/reference-conditioned likelihood contrast to reallocate
  additional distillation weight to reference-supported rollout tokens, while ACE
  adds sparse reference-side anchored correction for authoritative anchors omitted
  from the rollout without full-answer imitation. Across three knowledge-injection
  settings, six retention benchmarks, multiple baselines, and multiple base models,
  RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while
  keeping evaluated retention close to the base model.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: cad91fd0607cafa5
---

# Computer Science > Artificial Intelligence

# Title:RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection

View PDF HTML (experimental)Abstract:Knowledge injection updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting full authoritative answers can cause drift in non-updated behavior. Online distillation mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned distillation provides coarse supervision: it can under-emphasize reference-supported rollout tokens and supervise omitted facts only indirectly. We introduce RoCo-ACE, a rollout-conditioned online distillation objective for knowledge injection. RoCo uses same-rollout reference-free/reference-conditioned likelihood contrast to reallocate additional distillation weight to reference-supported rollout tokens, while ACE adds sparse reference-side anchored correction for authoritative anchors omitted from the rollout without full-answer imitation. Across three knowledge-injection settings, six retention benchmarks, multiple baselines, and multiple base models, RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while keeping evaluated retention close to the base model.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.