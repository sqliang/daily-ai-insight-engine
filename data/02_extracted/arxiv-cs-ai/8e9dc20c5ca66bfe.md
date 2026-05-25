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
tldr: LBW-Guard在AdamW之上实现有界自主训练控制，Qwen2.5-7B困惑度降18.7%且提速1.10倍，高学习率下保持可训练性。
objective_summary: 2026年，一篇arXiv论文提出LBW-Guard（Learn-by-Wire Guard），一种位于AdamW优化器之上的有界自主训练控制治理层。该层观测训练遥测数据、识别不稳定区域并施加有界控制，不替换优化器更新规则。在Qwen2.5系列模型（3B/7B/14B）和TinyLlama-1B上使
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LBW-Guard
  - AdamW
  - LoRA
  - Gradient Clipping
  - WikiText-103
  - Qwen2.5-7B
  - Qwen2.5-3B
  - Qwen2.5-14B
  - TinyLlama-1B
  key_people: []
key_logic_flow:
- 现代语言模型训练在高学习率、大规模和运行压力条件下，面临日益加剧的不稳定性、运行退化和算力浪费问题
- LBW-Guard被设计为AdamW优化器之上的一个有界自主训练控制治理层，通过观测训练遥测数据、识别不稳定敏感区域并施加有界控制来工作，而非替换优化器更新规则
- 在Qwen2.5-7B基准设置中，LBW-Guard将最终困惑度从13.21降至10.74（降低18.7%），同时将端到端训练时间从392.54秒缩短至357.02秒，实现1.10倍加速
- 在更强的学习率压力下（LR=3e-3），AdamW的最终困惑度退化至1885.24，LR=1e-3时退化至659.76，而LBW-Guard分别保持在11.57和10.33的可训练水平
- 梯度裁剪基线方法无法复现LBW-Guard的效果，证明其机制不同于简单的局部梯度抑制
- 作者得出有限系统结论：稳定性敏感的LLM训练可以从优化器之上的治理平面中受益，有界运行时控制可在压力下保持有效算力利用
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