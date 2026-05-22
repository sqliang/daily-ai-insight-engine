---
title: 'Learn-by-Wire Training Control Governance: Bounded Autonomous Training Under
  Stress for Stability and Efficiency'
source: https://arxiv.org/abs/2605.19008
author:
- '[[Anis Radianis]]'
published: '2026-05-20'
created: '2026-05-21'
description: 'arXiv:2605.19008v1 Announce Type: new Abstract: Modern language-model
  training is increasingly exposed to instability, degraded runs, and wasted compute,
  especially under aggressive learning-rate, scale, and runtime-stress conditions.
  This paper introduces Learn-by-Wire Guard (LBW-Guard), a bounded autonomous training-control
  governance layer that operates above AdamW. Rather than replacing the optimizer
  update rule, LBW-Guard observes training telemetry, interprets instability-sensitive
  regimes, and applies bounded control to optimizer execution while preserving fixed
  training objectives. We evaluate LBW-Guard in a Qwen2.5-centered stress-and-robustness
  suite using WikiText-103, with Qwen2.5-7B as the empirical anchor, model-size comparisons
  against Qwen2.5-3B and Qwen2.5-14B, learning-rate stress tests, gradient-clipping
  baselines, and a no-LoRA TinyLlama-1B full-parameter sanity check. In the 7B reference
  setting, LBW-Guard reduces final perplexity from 13.21 to 10.74, an 18.7% improvement,
  while reducing end-to-end time from 392.54s to 357.02s, a 1.10x speedup. Under stronger
  learning-rate stress, AdamW degrades to 1885.24 final perplexity at LR=3e-3 and
  659.76 at LR=1e-3, whereas LBW-Guard remains trainable at 11.57 and 10.33, respectively.
  Gradient-clipping baselines do not reproduce this effect. These results support
  a scoped systems conclusion that stability-sensitive LLM training can benefit from
  a governance plane above the optimizer. LBW-Guard provides evidence that bounded
  runtime control can preserve productive compute under stress while remaining distinct
  from optimizer replacement and local gradient suppression.'
tags:
- clippings
extraction_status: success
id: 8e9dc20c5ca66bfe
---

# Computer Science > Artificial Intelligence

# Title:Learn-by-Wire Training Control Governance: Bounded Autonomous Training Under Stress for Stability and Efficiency

View PDF HTML (experimental)Abstract:Modern language-model training is increasingly exposed to instability, degraded runs, and wasted compute, especially under aggressive learning-rate, scale, and runtime-stress conditions. This paper introduces Learn-by-Wire Guard (LBW-Guard), a bounded autonomous training-control governance layer that operates above AdamW. Rather than replacing the optimizer update rule, LBW-Guard observes training telemetry, interprets instability-sensitive regimes, and applies bounded control to optimizer execution while preserving fixed training objectives.

We evaluate LBW-Guard in a Qwen2.5-centered stress-and-robustness suite using WikiText-103, with Qwen2.5-7B as the empirical anchor, model-size comparisons against Qwen2.5-3B and Qwen2.5-14B, learning-rate stress tests, gradient-clipping baselines, and a no-LoRA TinyLlama-1B full-parameter sanity check. In the 7B reference setting, LBW-Guard reduces final perplexity from 13.21 to 10.74, an 18.7% improvement, while reducing end-to-end time from 392.54s to 357.02s, a 1.10x speedup. Under stronger learning-rate stress, AdamW degrades to 1885.24 final perplexity at LR=3e-3 and 659.76 at LR=1e-3, whereas LBW-Guard remains trainable at 11.57 and 10.33, respectively. Gradient-clipping baselines do not reproduce this effect.

These results support a scoped systems conclusion that stability-sensitive LLM training can benefit from a governance plane above the optimizer. LBW-Guard provides evidence that bounded runtime control can preserve productive compute under stress while remaining distinct from optimizer replacement and local gradient suppression.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.