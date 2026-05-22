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
source_type: academic_paper
tldr: 提出LBW-Guard，一种在AdamW之上的有界自主训练控制层，将Qwen2.5-7B困惑度从13.21降至10.74。
objective_summary: 该论文提出Learn-by-Wire Guard（LBW-Guard），一种运行在AdamW优化器之上的有界自主训练控制治理层，通过监测训练遥测数据在不稳定时施加控制。在Qwen2.5-7B和WikiText-103上的实验显示，最终困惑度从13.21降至10.74（提升18.
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LBW-Guard
  - AdamW
  - WikiText-103
  - Qwen2.5
  - TinyLlama
  key_people: []
key_logic_flow:
- LBW-Guard是一个位于AdamW优化器之上的有界自主训练控制治理层，不替换优化器，而是通过观测训练遥测数据在不稳定敏感区间施加有界控制。
- 在Qwen2.5-7B参考设置下，LBW-Guard将最终困惑度从13.21降至10.74（提升18.7%），端到端训练时间从392.54秒缩短至357.02秒（加速1.10倍）。
- 在高学习率压力测试中（LR=3e-3），AdamW退化至困惑度1885.24，而LBW-Guard保持可训练状态，困惑度仅为11.57。
- 梯度裁剪基线方法无法复现LBW-Guard的稳定性提升效果，表明其机制与局部梯度抑制不同。
- 实验覆盖了Qwen2.5-3B、Qwen2.5-7B、Qwen2.5-14B的模型规模对比以及TinyLlama-1B全参数训练验证。
pipeline_stage: fact_extracted
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