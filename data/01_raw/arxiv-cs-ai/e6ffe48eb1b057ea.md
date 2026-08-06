---
title: Memory Reward Inflation in Self-Improving LLM Agents
source: https://arxiv.org/abs/2608.00017
author:
- '[[Mohammad Asadolahi, Amir Amini, Samira Talebi, Amirfarhad Farhadi, Azadeh Zamanifar]]'
published: '2026-08-05'
created: '2026-08-05'
manifest_dates:
- '2026-08-05'
description: 'arXiv:2608.00017v1 Announce Type: new Abstract: Self-improving LLM agents
  increasingly learn from experience without updating any weights. Each episode is
  stored in an external memory, scored, and retrieved for similar future tasks to
  shape later behavior. Viewed through a reward lens, the stored score is a proxy
  reward for an implicit, non-parametric policy. Each retrieved episode then becomes
  a policy-improvement step whose reliability hinges on how that score is produced.
  In deployment, ground-truth labels are unavailable, so the stored reward is at best
  an LLM assessment. This substitution creates a failure mode, the *Echo Gap*, across
  the memory-based self-improving agents and model families studied. Incorrect episodes
  receive inflated rewards; thus, the agent preferentially reuses the very mistakes
  it has most confident in. Because the error compounds through memory rather than
  averaging out and the confirming judge''s errors remain correlated with the original
  self-grading bias, so it cannot identify which memories are overvalued. The missing
  property is formalized as the *Error-Independence Assumption* (EIA), which we prove
  is a *necessary* condition for correcting the inflation, not merely a description
  of a good verifier: a usable signal must track truth *and* decorrelate its error
  from the memory bias, and the recoverable payoff is a closed-form function of exactly
  those two quantities. We further show the inflation compounds not only when retrieval
  ranks by the stored score but also under plain similarity retrieval which is the
  regime the deployed agent uses. Finally, the answer-free de-inflation algorithm
  LUCID delivers a consistent end-to-end gain on the BIRD text-to-SQL benchmark. It
  raises execution accuracy to $56.9\%$, above both a Memento-style self-graded agent
  ($54.0\%$, a $+2.9$-point mean gain across seeds) and a memory-less agent of identical
  architecture ($52.4\%$).'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: e6ffe48eb1b057ea
---

# Computer Science > Artificial Intelligence

# Title:Memory Reward Inflation in Self-Improving LLM Agents

View PDF HTML (experimental)Abstract:Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored reward is at best an LLM assessment. This substitution creates a failure mode, the *Echo Gap*, across the memory-based self-improving agents and model families studied. Incorrect episodes receive inflated rewards; thus, the agent preferentially reuses the very mistakes it has most confident in. Because the error compounds through memory rather than averaging out and the confirming judge's errors remain correlated with the original self-grading bias, so it cannot identify which memories are overvalued. The missing property is formalized as the *Error-Independence Assumption* (EIA), which we prove is a *necessary* condition for correcting the inflation, not merely a description of a good verifier: a usable signal must track truth *and* decorrelate its error from the memory bias, and the recoverable payoff is a closed-form function of exactly those two quantities. We further show the inflation compounds not only when retrieval ranks by the stored score but also under plain similarity retrieval which is the regime the deployed agent uses. Finally, the answer-free de-inflation algorithm LUCID delivers a consistent end-to-end gain on the BIRD text-to-SQL benchmark. It raises execution accuracy to $56.9\%$, above both a Memento-style self-graded agent ($54.0\%$, a $+2.9$-point mean gain across seeds) and a memory-less agent of identical architecture ($52.4\%$).

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.