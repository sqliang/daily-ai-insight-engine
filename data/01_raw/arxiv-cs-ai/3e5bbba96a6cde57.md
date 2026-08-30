---
title: 'Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release
  for Long-Horizon Agents'
source: https://arxiv.org/abs/2608.12476
author:
- '[[Guodong Xu]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'arXiv:2608.12476v1 Announce Type: new Abstract: Long-term agent memory
  is usually treated as select--store--retrieve, but retrieval does not decide whether
  contradictory, superseded, retracted, deleted, or stale records may support an outgoing
  claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition
  model with source-bound admission, derived lifecycle state, current public barriers,
  and fail-closed structured release. Five executable clauses cover ledger integrity,
  source binding, conflict isolation, non-revival after retraction or deletion, and
  exact claim closure over a fresh view at one verified head. On a prespecified hash-frozen
  3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of
  three intentionally simple complete policies matches 1,800/3,600 and makes unmatched
  releases on 50% of violation cases. A separate sealed end-to-end service evaluation
  exercises real ingestion and release across eight query families. In its publicly
  disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400
  for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no
  regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over
  Chinese- and English-command arms, with generation-date pinning and no post-freeze
  reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent
  finite model explores 331,776 semantic and 1,990,656 query states without a full-contract
  counterexample, and a 100,000-trace three-engine differential yields zero mismatches.
  These are bounded contract and implementation results, not open-world model accuracy
  or evidence of world truth. Governed answers in the sealed service evaluation are
  deterministic service outputs; the 7B result is the ungoverned comparison, not a
  claim that a language model itself became perfectly accurate.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 3e5bbba96a6cde57
---

# Computer Science > Artificial Intelligence

# Title:Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents

View PDF HTML (experimental)Abstract:Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release. Five executable clauses cover ledger integrity, source binding, conflict isolation, non-revival after retraction or deletion, and exact claim closure over a fresh view at one verified head.

On a prespecified hash-frozen 3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of three intentionally simple complete policies matches 1,800/3,600 and makes unmatched releases on 50% of violation cases. A separate sealed end-to-end service evaluation exercises real ingestion and release across eight query families. In its publicly disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400 for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over Chinese- and English-command arms, with generation-date pinning and no post-freeze reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent finite model explores 331,776 semantic and 1,990,656 query states without a full-contract counterexample, and a 100,000-trace three-engine differential yields zero mismatches.

These are bounded contract and implementation results, not open-world model accuracy or evidence of world truth. Governed answers in the sealed service evaluation are deterministic service outputs; the 7B result is the ungoverned comparison, not a claim that a language model itself became perfectly accurate.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.