---
title: Time series causal discovery with variable lags
source: https://arxiv.org/abs/2605.04081
author:
- '[[Bruno Petrungaro, Anthony C. Constantinou]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04081v1 Announce Type: cross Abstract: Causal Bayesian Networks
  (CBNs) are a powerful tool for reasoning under uncertainty about complex real-world
  problems. Such problems evolve over time, responding to external shocks as they
  occur. To support decision-making, CBNs require a cause-and-effect map of the variables
  under consideration, known as the network''s structure. Learning the graphical structure
  of a causal model from data remains challenging; learning it from time-series data
  is even harder because dependencies may arise at different time lags. Existing time-series
  causal discovery methods often assume a fixed lag window and do not explicitly optimise
  edge-specific lags. We propose a Tabu-based structure learning algorithm that searches
  for a time-ordered directed structure (i.e., where every edge respects time) while
  allowing edge-specific lags up to a specified maximum lag. The approach uses a decomposable
  BIC-based score with node-specific effective sample sizes and an explicit lag-length
  penalty encouraging parsimonious delay assignments while preserving efficient local
  score updates. We provide theoretical guarantees of validity and local optimality,
  and we also describe a parallel implementation for improved scalability. In simulations,
  the method recovered graph structure competitively and estimated lags accurately
  when true adjacencies were recovered. On a real-world UK COVID-19 policy dataset,
  the learnt structure was dominated by short delays while retaining a substantial
  minority of longer-lag dependencies, consistent with delayed behavioural and epidemiological
  effects.'
tags:
- clippings
id: dfc1fcd5fb7663ea
---

# Computer Science > Machine Learning

# Title:Time series causal discovery with variable lags

View PDF HTML (experimental)Abstract:Causal Bayesian Networks (CBNs) are a powerful tool for reasoning under uncertainty about complex real-world problems. Such problems evolve over time, responding to external shocks as they occur. To support decision-making, CBNs require a cause-and-effect map of the variables under consideration, known as the network's structure. Learning the graphical structure of a causal model from data remains challenging; learning it from time-series data is even harder because dependencies may arise at different time lags. Existing time-series causal discovery methods often assume a fixed lag window and do not explicitly optimise edge-specific lags. We propose a Tabu-based structure learning algorithm that searches for a time-ordered directed structure (i.e., where every edge respects time) while allowing edge-specific lags up to a specified maximum lag. The approach uses a decomposable BIC-based score with node-specific effective sample sizes and an explicit lag-length penalty encouraging parsimonious delay assignments while preserving efficient local score updates. We provide theoretical guarantees of validity and local optimality, and we also describe a parallel implementation for improved scalability. In simulations, the method recovered graph structure competitively and estimated lags accurately when true adjacencies were recovered. On a real-world UK COVID-19 policy dataset, the learnt structure was dominated by short delays while retaining a substantial minority of longer-lag dependencies, consistent with delayed behavioural and epidemiological effects.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.