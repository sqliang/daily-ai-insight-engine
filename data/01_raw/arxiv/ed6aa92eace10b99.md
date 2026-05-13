---
title: 'RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models
  via Hybrid Direct Preference Optimization'
source: https://arxiv.org/abs/2605.04539
author:
- '[[Qiming Bao, Juho Leinonen, Paul Denny, Michael J. Witbrock]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04539v1 Announce Type: cross Abstract: Direct Preference
  Optimization (DPO), the efficient alternative to PPO-based RLHF, falls short on
  knowledge-intensive generation: standard preference signals from human annotators
  or LLM judges exhibit a systematic verbosity bias that rewards fluency over logical
  correctness. This blindspot leaves a logical alignment gap -- SFT models reach NLI
  entailment of only 0.05-0.22 despite producing fluent text. We propose RLearner-LLM
  with Hybrid-DPO: an automated preference pipeline that fuses a DeBERTa-v3 NLI signal
  with a verifier LLM score, removing human annotation while overcoming the "alignment
  tax" of single-signal optimization. Evaluated across five academic domains (Biology,
  Medicine, Law) with three base architectures (LLaMA-2-13B, Qwen3-8B, Gemma 4 E4B-it),
  RLearner-LLM yields up to 6x NLI improvement over SFT, with NLI gains in 11 of 15
  cells and consistent answer-coverage gains. On Gemma 4 E4B-it (4.5B effective params),
  Hybrid-DPO lifts NLI in four of five domains (+11.9% to +2.4x) with faster inference
  across all five, scaling down to compact base models without losing the alignment-tax
  mitigation. Our Qwen3-8B RLearner-LLM wins 95% of pairwise comparisons against its
  own SFT baseline; GPT-4o-mini in turn wins 95% against our concise output -- alongside
  the 69% win the same judge gives a verbose SFT over our DPO model, this replicates
  verbosity bias on a frontier comparator and motivates logic-aware metrics (NLI,
  ACR) over LLM-as-a-judge for knowledge-intensive generation.'
tags:
- clippings
id: ed6aa92eace10b99
---

# Computer Science > Computation and Language

# Title:RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models via Hybrid Direct Preference Optimization

View PDF HTML (experimental)Abstract:Direct Preference Optimization (DPO), the efficient alternative to PPO-based RLHF, falls short on knowledge-intensive generation: standard preference signals from human annotators or LLM judges exhibit a systematic verbosity bias that rewards fluency over logical correctness. This blindspot leaves a logical alignment gap -- SFT models reach NLI entailment of only 0.05-0.22 despite producing fluent text. We propose RLearner-LLM with Hybrid-DPO: an automated preference pipeline that fuses a DeBERTa-v3 NLI signal with a verifier LLM score, removing human annotation while overcoming the "alignment tax" of single-signal optimization. Evaluated across five academic domains (Biology, Medicine, Law) with three base architectures (LLaMA-2-13B, Qwen3-8B, Gemma 4 E4B-it), RLearner-LLM yields up to 6x NLI improvement over SFT, with NLI gains in 11 of 15 cells and consistent answer-coverage gains. On Gemma 4 E4B-it (4.5B effective params), Hybrid-DPO lifts NLI in four of five domains (+11.9% to +2.4x) with faster inference across all five, scaling down to compact base models without losing the alignment-tax mitigation. Our Qwen3-8B RLearner-LLM wins 95% of pairwise comparisons against its own SFT baseline; GPT-4o-mini in turn wins 95% against our concise output -- alongside the 69% win the same judge gives a verbose SFT over our DPO model, this replicates verbosity bias on a frontier comparator and motivates logic-aware metrics (NLI, ACR) over LLM-as-a-judge for knowledge-intensive generation.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.