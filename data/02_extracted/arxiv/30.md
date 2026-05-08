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
source_type: academic_paper
tldr: 提出基于Tabu搜索的变滞后时间序列因果发现算法
objective_summary: 论文提出一种Tabu搜索算法用于时间序列因果发现，允许每条边独立指定滞后时间，使用可分解BIC评分函数并包含滞后长度惩罚项。提供了理论保证与并行实现。仿真实验图结构恢复有竞争力，在英国COVID-19数据集上验证了短延迟为主、长延迟并存的结构特征。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Causal Bayesian Networks (CBNs)
  - Tabu search
  - BIC-based score
  key_people: []
key_logic_flow:
- 现有时间序列因果发现方法通常假设固定滞后窗口，无法针对每条边优化独立的滞后参数。
- 该论文提出一种基于Tabu搜索的结构学习算法，要求所有边满足时间顺序约束，并允许每条边独立指定滞后时间直至最大滞后值。
- 算法使用可分解的BIC评分函数，结合节点特异性有效样本量和显式的滞后长度惩罚项，鼓励简约的延迟分配。
- 作者提供了算法的有效性和局部最优性理论保证，并描述了并行实现方案以提升可扩展性。
- 仿真实验表明该方法在恢复图结构方面有竞争力，且在正确恢复邻接关系时能准确估计滞后时间。
- 在英国COVID-19政策数据集上，学习到的因果结构以短延迟为主，同时保留了相当数量的长滞后依赖关系。
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