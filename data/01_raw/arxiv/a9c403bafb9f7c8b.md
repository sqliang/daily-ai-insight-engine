---
title: 'Emergent Hierarchical Structure in Large Language Models: An Information-Theoretic
  Framework for Multi-Scale Representation'
source: https://arxiv.org/abs/2505.18244
author:
- '[[Yukin Zhang, Qi Dong, Kemu Xu]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2505.18244v3 Announce Type: replace-cross Abstract: Why do language
  models from different architecture families respond so differently to the same perturbation?
  We argue that the answer is not scale, but \emph{how architecture shapes information
  compression}. Analyzing eight Transformer models (7B--70B parameters) from the Llama
  and Qwen families, we show that every model spontaneously develops discrete functional
  boundaries dividing its layers into Local, Intermediate, and Global processing segments
  -- yet boundary locations and per-segment brittleness are determined overwhelmingly
  by architecture family rather than model size or training configuration. We formalize
  this regularity as the \textbf{Multi-Scale Probabilistic Generation Theory} (MSPGT),
  which models an autoregressive Transformer as a Hierarchical Variational Information
  Bottleneck system and derives a tiered set of falsifiable predictions. Three predictions
  are strongly confirmed: all eight models exhibit two prominent phase-transition
  boundaries (P1.1); Llama boundary positions are stable across a $10{\times}$ parameter
  range ($\mathrm{CV}{=}0.067$--$0.095$) while Qwen positions vary widely ($\mathrm{CV}{=}0.465$--$0.726$),
  precisely matching our strong- and weak-dominance conditions; and cross-architecture
  local-segment brittleness spans \textbf{three orders of magnitude} ($493{\times}$
  ratio) -- a gap that architecture family alone predicts and that dwarfs any within-family
  or scale-driven variation.'
tags:
- clippings
id: a9c403bafb9f7c8b
---

# Computer Science > Computation and Language

# Title:Emergent Hierarchical Structure in Large Language Models: An Information-Theoretic Framework for Multi-Scale Representation

View PDF HTML (experimental)Abstract:Why do language models from different architecture families respond so differently to the same perturbation? We argue that the answer is not scale, but \emph{how architecture shapes information compression}. Analyzing eight Transformer models (7B--70B parameters) from the Llama and Qwen families, we show that every model spontaneously develops discrete functional boundaries dividing its layers into Local, Intermediate, and Global processing segments -- yet boundary locations and per-segment brittleness are determined overwhelmingly by architecture family rather than model size or training configuration. We formalize this regularity as the \textbf{Multi-Scale Probabilistic Generation Theory} (MSPGT), which models an autoregressive Transformer as a Hierarchical Variational Information Bottleneck system and derives a tiered set of falsifiable predictions. Three predictions are strongly confirmed: all eight models exhibit two prominent phase-transition boundaries (P1.1); Llama boundary positions are stable across a $10{\times}$ parameter range ($\mathrm{CV}{=}0.067$--$0.095$) while Qwen positions vary widely ($\mathrm{CV}{=}0.465$--$0.726$), precisely matching our strong- and weak-dominance conditions; and cross-architecture local-segment brittleness spans \textbf{three orders of magnitude} ($493{\times}$ ratio) -- a gap that architecture family alone predicts and that dwarfs any within-family or scale-driven variation.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.