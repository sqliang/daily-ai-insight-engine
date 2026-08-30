---
title: 'Serving Masked Diffusion LLMs: Characterization and Design Principles from
  Real Hardware'
source: https://arxiv.org/abs/2608.23807
author:
- '[[Farhana Amin, Sabiha Afroz, Mona Moghadampanah, Dimitrios S. Nikolopoulos]]'
published: '2026-08-26'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
- '2026-08-27'
description: 'arXiv:2608.23807v1 Announce Type: new Abstract: Masked diffusion language
  models (dLLMs) can in principle generate text faster than autoregressive (AR) models,
  since they denoise many tokens at once. Recent systems have begun building serving
  infrastructure for dLLMs, but none first measure how these models behave under real,
  concurrent serving load. Serving systems built without this grounding risk carrying
  over assumptions from AR serving that may not hold for dLLMs. We characterize dLLM
  serving to close this gap, using LLaDA-8B-Instruct with a D2F (Discrete Diffusion
  Forcing) LoRA adapter on a single NVIDIA H200 GPU, evaluated on GSM8K and HumanEval.
  We report three findings. First, request difficulty, the number of denoising steps
  a request needs, is discrete rather than continuous: requests fall into 11 fixed
  step-count levels (178 + 29k), and no signal we test predicts the level before generation
  starts (best R2 = 0.150). Second, benchmarks with short generation budgets below
  320 tokens understate serving variance, since requests are cut off before the latency
  spread appears. Third, only 24% of single-request wall-clock time is GPU computation;
  the rest is CPU-side dispatch overhead. Batching mainly helps by amortizing this
  overhead: sharing one forward pass per denoising step improves throughput by 16.0x
  at batch size 16 over a per-request-dispatch baseline. We also argue structurally
  that output quality should not degrade with batch size, stating three assumptions
  this rests on; we measure 74 to 76% GSM8K accuracy at single-request scale. Finally,
  we derive a batch-timeout rule for fixed-fill synchronized batching under Poisson
  arrivals. Together, these results show that serving diffusion language models needs
  parallelism at the level of each denoising step, which differs from AR serving in
  how admission and eviction interact with an already shared forward pass.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: fede902dc6ec2be1
---

# Computer Science > Artificial Intelligence

# Title:Serving Masked Diffusion LLMs: Characterization and Design Principles from Real Hardware

View PDF HTML (experimental)Abstract:Masked diffusion language models (dLLMs) can in principle generate text faster than autoregressive (AR) models, since they denoise many tokens at once. Recent systems have begun building serving infrastructure for dLLMs, but none first measure how these models behave under real, concurrent serving load. Serving systems built without this grounding risk carrying over assumptions from AR serving that may not hold for dLLMs. We characterize dLLM serving to close this gap, using LLaDA-8B-Instruct with a D2F (Discrete Diffusion Forcing) LoRA adapter on a single NVIDIA H200 GPU, evaluated on GSM8K and HumanEval. We report three findings. First, request difficulty, the number of denoising steps a request needs, is discrete rather than continuous: requests fall into 11 fixed step-count levels (178 + 29k), and no signal we test predicts the level before generation starts (best R2 = 0.150). Second, benchmarks with short generation budgets below 320 tokens understate serving variance, since requests are cut off before the latency spread appears. Third, only 24% of single-request wall-clock time is GPU computation; the rest is CPU-side dispatch overhead. Batching mainly helps by amortizing this overhead: sharing one forward pass per denoising step improves throughput by 16.0x at batch size 16 over a per-request-dispatch baseline. We also argue structurally that output quality should not degrade with batch size, stating three assumptions this rests on; we measure 74 to 76% GSM8K accuracy at single-request scale. Finally, we derive a batch-timeout rule for fixed-fill synchronized batching under Poisson arrivals. Together, these results show that serving diffusion language models needs parallelism at the level of each denoising step, which differs from AR serving in how admission and eviction interact with an already shared forward pass.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.