---
title: Search Discipline for Long-Horizon Research Agents
source: https://arxiv.org/abs/2606.11522
author:
- '[[Adithya Srinivasan, Devesh Paragiri]]'
published: '2026-06-11'
created: '2026-06-11'
description: 'arXiv:2606.11522v1 Announce Type: new Abstract: Autoresearch agents
  now propose, evaluate, and select scientific candidates against a metric, and that
  metric is usually an aggregate reduced over a heterogeneous space of regions, slices,
  or cohorts. We show that when scientific validity lives in that disaggregated structure,
  the aggregate can rank the wrong candidate first. The headline number improves while
  the structure underneath inverts, so a decision made on the number accepts a candidate
  that quietly breaks the model. The failure is not domain-specific. It appears wherever
  a candidate''s validity is multi-dimensional but its verifier is a single reduction.
  We demonstrate the inversion on a fire-model task in the Ecosystem Demography model.
  The highest-scoring candidate and a slightly lower one are within noise of each
  other on global score, yet the top-scoring one collapses the protected boreal regions
  while the other preserves them. What separates them is the per-region behavior,
  not the headline number. This decision should not be left to the agent that produced
  the candidates. The agent optimizing the score is the last party likely to catch
  the score being wrong, and a prompt has no remaining turn once the agent has stopped.
  We move the decision to an external control loop that audits each candidate on its
  disaggregated behavior and acts after the agent has decided. It can demote a candidate
  the agent would have accepted, and it can reopen a run the agent had declared finished.
  Our contribution is the inversion finding itself, and a search-discipline protocol
  that decides on reviewable candidate-effect evidence instead of the score.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: b8fefd5fda42649d
---

# Computer Science > Artificial Intelligence

# Title:Search Discipline for Long-Horizon Research Agents

View PDF HTML (experimental)Abstract:Autoresearch agents now propose, evaluate, and select scientific candidates against a metric, and that metric is usually an aggregate reduced over a heterogeneous space of regions, slices, or cohorts. We show that when scientific validity lives in that disaggregated structure, the aggregate can rank the wrong candidate first. The headline number improves while the structure underneath inverts, so a decision made on the number accepts a candidate that quietly breaks the model. The failure is not domain-specific. It appears wherever a candidate's validity is multi-dimensional but its verifier is a single reduction.

We demonstrate the inversion on a fire-model task in the Ecosystem Demography model. The highest-scoring candidate and a slightly lower one are within noise of each other on global score, yet the top-scoring one collapses the protected boreal regions while the other preserves them. What separates them is the per-region behavior, not the headline number.

This decision should not be left to the agent that produced the candidates. The agent optimizing the score is the last party likely to catch the score being wrong, and a prompt has no remaining turn once the agent has stopped. We move the decision to an external control loop that audits each candidate on its disaggregated behavior and acts after the agent has decided. It can demote a candidate the agent would have accepted, and it can reopen a run the agent had declared finished. Our contribution is the inversion finding itself, and a search-discipline protocol that decides on reviewable candidate-effect evidence instead of the score.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.