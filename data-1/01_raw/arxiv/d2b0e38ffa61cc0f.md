---
title: A Foundation Model for Zero-Shot Logical Rule Induction
source: https://arxiv.org/abs/2605.04916
author:
- '[[Yin Jun Phua]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04916v1 Announce Type: new Abstract: Inductive Logic Programming
  (ILP) learns interpretable logical rules from data. Existing methods are transductive:
  their learned parameters are bound to specific predicates and require retraining
  for each new task. We introduce Neural Rule Inducer (NRI), a pretrained model for
  zero-shot rule induction. Rather than encoding literal identities, NRI represents
  literals using domain-agnostic statistical properties such as class-conditional
  rates, entropy, and co-occurrence, which generalize across variable identities and
  counts without retraining. The model consists of a statistical encoder and a parallel
  slot-based decoder. Parallel decoding preserves the permutation invariance of logical
  disjunction; an autoregressive decoder would instead impose an arbitrary clause
  order. Product T-norm relaxation makes rule execution differentiable, allowing end-to-end
  training on prediction accuracy alone. We evaluate NRI on rule recovery, robustness
  to label noise and spurious correlations, and zero-shot transfer to real-world benchmarks,
  and we believe this work opens up the possibility of foundation models for symbolic
  reasoning. Code and the reference checkpoint are available at https://github.com/phuayj/neural-rule-inducer.'
tags:
- clippings
id: d2b0e38ffa61cc0f
---

# Computer Science > Artificial Intelligence

# Title:A Foundation Model for Zero-Shot Logical Rule Induction

View PDF HTML (experimental)Abstract:Inductive Logic Programming (ILP) learns interpretable logical rules from data. Existing methods are transductive: their learned parameters are bound to specific predicates and require retraining for each new task. We introduce Neural Rule Inducer (NRI), a pretrained model for zero-shot rule induction. Rather than encoding literal identities, NRI represents literals using domain-agnostic statistical properties such as class-conditional rates, entropy, and co-occurrence, which generalize across variable identities and counts without retraining. The model consists of a statistical encoder and a parallel slot-based decoder. Parallel decoding preserves the permutation invariance of logical disjunction; an autoregressive decoder would instead impose an arbitrary clause order. Product T-norm relaxation makes rule execution differentiable, allowing end-to-end training on prediction accuracy alone. We evaluate NRI on rule recovery, robustness to label noise and spurious correlations, and zero-shot transfer to real-world benchmarks, and we believe this work opens up the possibility of foundation models for symbolic reasoning. Code and the reference checkpoint are available at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.