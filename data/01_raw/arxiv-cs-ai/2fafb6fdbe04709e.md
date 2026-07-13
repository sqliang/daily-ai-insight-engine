---
title: 'Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated
  Workflows'
source: https://arxiv.org/abs/2607.00269
author:
- '[[Edward Y. Chang, Longling Geng, Emily J. Chang]]'
published: '2026-07-02'
created: '2026-07-02'
description: 'arXiv:2607.00269v1 Announce Type: new Abstract: LLMs, solvers, and agent
  teams increasingly generate workflow actions, repairs, and plans, but a generated
  action may be syntactically valid yet stale, infeasible, conflicting, or destructive
  of the evidence that triggered a repair. We introduce Agentic Transaction Processing
  (ATP), a transaction model that treats generated actions as untrusted proposals
  until they pass deterministic admission under a declared, executable constraint
  set C. The principle is two-sided: a proposal is not truth, and no proposal foresees
  every disruption: anything may propose, but only the runtime admits and commits,
  and when an unforeseen disruption strikes it repairs reactively within bounds rather
  than trusting a fresh proposal. Relative to C, committed-state correctness becomes
  independent of the competence, honesty, or learning of the proposing layer. We realize
  ATP in Mnemosyne, a runtime with an append-only transition log, effective-state
  projection, dependency-safe compensation, and active commitment records, and prove
  four safety properties relative to C (authority separation, serial-equivalent generative
  admission, evidence-preserving repair, and obligation containment) together with
  a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A
  reproducible artifact rejects the targeted violations across nine falsification
  tests while still admitting valid work, at under 6% projection-and-validation overhead,
  and bounded local repair edits an order of magnitude fewer operations than global
  recompute. Mnemosyne is open source: https://github.com/eyuchang/Mnemosyne/tree/arxiv-atp-rq1-rq9b-r8-v2.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 2fafb6fdbe04709e
---

# Computer Science > Artificial Intelligence

# Title:Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows

View PDF HTML (experimental)Abstract:LLMs, solvers, and agent teams increasingly generate workflow actions, repairs, and plans, but a generated action may be syntactically valid yet stale, infeasible, conflicting, or destructive of the evidence that triggered a repair. We introduce Agentic Transaction Processing (ATP), a transaction model that treats generated actions as untrusted proposals until they pass deterministic admission under a declared, executable constraint set C. The principle is two-sided: a proposal is not truth, and no proposal foresees every disruption: anything may propose, but only the runtime admits and commits, and when an unforeseen disruption strikes it repairs reactively within bounds rather than trusting a fresh proposal. Relative to C, committed-state correctness becomes independent of the competence, honesty, or learning of the proposing layer. We realize ATP in Mnemosyne, a runtime with an append-only transition log, effective-state projection, dependency-safe compensation, and active commitment records, and prove four safety properties relative to C (authority separation, serial-equivalent generative admission, evidence-preserving repair, and obligation containment) together with a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A reproducible artifact rejects the targeted violations across nine falsification tests while still admitting valid work, at under 6% projection-and-validation overhead, and bounded local repair edits an order of magnitude fewer operations than global recompute. Mnemosyne is open source: this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.