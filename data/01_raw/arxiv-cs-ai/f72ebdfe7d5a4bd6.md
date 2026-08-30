---
title: 'Large Language Models Can Follow Instructions, But Not Many at Once: Phase
  Transitions in Compositional Constraint Satisfaction'
source: https://arxiv.org/abs/2608.12426
author:
- '[[Mariya I. Vasileva]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'arXiv:2608.12426v1 Announce Type: new Abstract: Large language models
  are increasingly deployed in settings that require simultaneous adherence to multiple
  explicit constraints - reasoning structure, safety boundaries, output schemas. Individual
  constraints are handled proficiently, but the compositional regime, where many must
  hold jointly, remains poorly characterized: how rapidly does performance degrade,
  what governs the degradation, and can the collapse be mitigated? We introduce Constraint
  Saturation Evaluation (CSE), a procedurally generated benchmark that systematically
  varies the number of simultaneous constraints (k), with every constraint scored
  by a deterministic, rule-based verifier and zero LLM-judge involvement: 15 models,
  36 constraint types, 369,753 checks at k=1-12. Three findings emerge. First, per-constraint
  pass rate decays gradually and predictably, while the chance of satisfying all k
  constraints collapses - a model passing individual constraints at ~41% at k=8 succeeds
  on all eight just 5.7% of the time. Second, constraints do not degrade equally:
  structural constraints lose 2x more baseline capability per added constraint than
  lexical ones, ordered by a comprehension-maintenance gap that separates constraints
  requiring sustained tracking from binary decisions immune to composition. Third,
  failures are nearly independent, which is what makes the accumulation multiplicative;
  the residual coupling that does exist tracks shared output features rather than
  pairwise interference - a wrong sentence count fails every constraint that reads
  it. Reliable instruction following breaks down beyond 5-6 simultaneous constraints:
  probe-level success falls below 50% at 7 constraints for the strongest model, and
  at 3 or fewer for 12 of 15.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: f72ebdfe7d5a4bd6
---

# Computer Science > Artificial Intelligence

# Title:Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction

View PDF HTML (experimental)Abstract:Large language models are increasingly deployed in settings that require simultaneous adherence to multiple explicit constraints - reasoning structure, safety boundaries, output schemas. Individual constraints are handled proficiently, but the compositional regime, where many must hold jointly, remains poorly characterized: how rapidly does performance degrade, what governs the degradation, and can the collapse be mitigated? We introduce Constraint Saturation Evaluation (CSE), a procedurally generated benchmark that systematically varies the number of simultaneous constraints (k), with every constraint scored by a deterministic, rule-based verifier and zero LLM-judge involvement: 15 models, 36 constraint types, 369,753 checks at k=1-12. Three findings emerge. First, per-constraint pass rate decays gradually and predictably, while the chance of satisfying all k constraints collapses - a model passing individual constraints at ~41% at k=8 succeeds on all eight just 5.7% of the time. Second, constraints do not degrade equally: structural constraints lose 2x more baseline capability per added constraint than lexical ones, ordered by a comprehension-maintenance gap that separates constraints requiring sustained tracking from binary decisions immune to composition. Third, failures are nearly independent, which is what makes the accumulation multiplicative; the residual coupling that does exist tracks shared output features rather than pairwise interference - a wrong sentence count fails every constraint that reads it. Reliable instruction following breaks down beyond 5-6 simultaneous constraints: probe-level success falls below 50% at 7 constraints for the strongest model, and at 3 or fewer for 12 of 15.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.