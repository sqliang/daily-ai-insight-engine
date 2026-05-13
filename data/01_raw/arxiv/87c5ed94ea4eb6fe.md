---
title: 'Joint Treatment Effect Estimation from Incomplete Healthcare Data: Temporal
  Causal Normalizing Flows with LLM-driven Evolutionary MNAR Imputation'
source: https://arxiv.org/abs/2605.05125
author:
- '[[Olivia Jullian Parra, Sara Zoccheddu, David Catalan Cerezo, Tom Forzy, Franziska
  Ulrich, William Sutcliffe, Jakob Martin Burgstaller, Oliver Senn, Patrick Owen,
  Nicola Serra]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.05125v1 Announce Type: cross Abstract: Target trial emulation
  (TTE) enables causal questions to be studied with observational data when randomized
  controlled trials (RCTs) are infeasible. Yet treatment-effect methods often address
  causal estimation, missingness, and temporal structure separately, limiting their
  robustness in electronic health records (EHRs), where time-varying confounding and
  missing-not-at-random (MNAR) biomarkers can reach 50%--80%. We propose a two-stage
  pipeline for treatment effect estimation from incomplete longitudinal EHRs. First,
  CausalFlow-T, a directed acyclic graph (DAG)-constrained normalizing flow with long
  short-term memory (LSTM)-encoded patient history, performs exact invertible counterfactual
  inference, avoiding approximation errors from variational inference and separating
  confounding through explicit causal structure. Ablations on four synthetic and one
  semi-synthetic benchmark with known counterfactuals show that DAG constraints and
  exact inference address distinct failure modes: neither compensates for the other.
  Second, because CausalFlow-T requires completed inputs, we introduce an LLM-driven
  evolutionary imputer that proposes executable imputation operators rather than individual
  entries, and evaluate it with three large language model (LLM) backends, including
  two open-source models. Across 30%--80% MNAR missingness, this imputer achieves
  the best pooled rank over biomarker and causal metrics, leading in point-wise accuracy
  and temporal extrapolation while preserving average treatment effect (ATE) recovery
  as statistical baselines degrade. On Swiss primary-care EHRs from adults with type
  2 diabetes initiating a GLP-1 receptor agonist or SGLT-2 inhibitor, the pipeline
  estimates a per-protocol weight-loss difference of -0.98 kg [95% CI -1.01, -0.96]
  favoring GLP-1 receptor agonists, consistent with randomized evidence and obtained
  from realistically incomplete real-world EHRs.'
tags:
- clippings
id: 87c5ed94ea4eb6fe
---

# Computer Science > Machine Learning

# Title:Joint Treatment Effect Estimation from Incomplete Healthcare Data: Temporal Causal Normalizing Flows with LLM-driven Evolutionary MNAR Imputation

View PDF HTML (experimental)Abstract:Target trial emulation (TTE) enables causal questions to be studied with observational data when randomized controlled trials (RCTs) are infeasible. Yet treatment-effect methods often address causal estimation, missingness, and temporal structure separately, limiting their robustness in electronic health records (EHRs), where time-varying confounding and missing-not-at-random (MNAR) biomarkers can reach 50%--80%. We propose a two-stage pipeline for treatment effect estimation from incomplete longitudinal EHRs. First, CausalFlow-T, a directed acyclic graph (DAG)-constrained normalizing flow with long short-term memory (LSTM)-encoded patient history, performs exact invertible counterfactual inference, avoiding approximation errors from variational inference and separating confounding through explicit causal structure. Ablations on four synthetic and one semi-synthetic benchmark with known counterfactuals show that DAG constraints and exact inference address distinct failure modes: neither compensates for the other. Second, because CausalFlow-T requires completed inputs, we introduce an LLM-driven evolutionary imputer that proposes executable imputation operators rather than individual entries, and evaluate it with three large language model (LLM) backends, including two open-source models. Across 30%--80% MNAR missingness, this imputer achieves the best pooled rank over biomarker and causal metrics, leading in point-wise accuracy and temporal extrapolation while preserving average treatment effect (ATE) recovery as statistical baselines degrade. On Swiss primary-care EHRs from adults with type 2 diabetes initiating a GLP-1 receptor agonist or SGLT-2 inhibitor, the pipeline estimates a per-protocol weight-loss difference of -0.98 kg [95% CI -1.01, -0.96] favoring GLP-1 receptor agonists, consistent with randomized evidence and obtained from realistically incomplete real-world EHRs.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.