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
pipeline_stage: fact_extracted
id: fede902dc6ec2be1
source_type: academic_paper
tldr: arXiv 论文实测扩散语言模型（dLLM）在真实硬件上的服务特征，发现请求难度呈离散分布、GPU 计算仅占单请求耗时的 24%，并通过每去噪步骤共享一次前向传播在批次大小
  16 时带来 16.0 倍吞吐提升。
objective_summary: 该 arXiv 论文在单块 NVIDIA H200 GPU 上，使用 LLaDA-8B-Instruct 搭配 D2F（Discrete
  Diffusion Forcing）LoRA 适配器对扩散语言模型的服务行为进行实测，评估基准为 GSM8K 与 HumanEval。研究发现请求难度即所需去噪步数呈离散分布，请求落入
  11 个固定步数层级，且生成前无任何信号能预测该层级。单请求耗时中 GPU 计算仅占 24%，其余为 CPU 侧分发开销，共享前向传播使批次大小 16 时吞吐较逐请求分发基线提升
  16.0 倍。单请求规模下 GSM8K 准确率为 74% 至 76%，论文还推导出泊松到达下的批超时规则。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - NVIDIA
  technologies:
  - dLLM (Masked Diffusion Language Model)
  - D2F (Discrete Diffusion Forcing)
  - LoRA
  - autoregressive (AR) model
  - GSM8K
  - HumanEval
  key_people: []
key_logic_flow:
- 扩散语言模型可同时去噪多个 token，理论上生成速度快于自回归模型，但已有服务系统未在真实并发负载下实测其行为。
- 请求难度即所需去噪步数是离散而非连续的，请求落入 11 个固定步数层级，生成前无任何测试信号能预测该层级，最佳 R2 仅为 0.150。
- 生成预算低于 320 token 的基准会低估服务方差，因为请求在延迟分布显现之前就被截断。
- 单请求耗时中 GPU 计算仅占 24%，其余为 CPU 侧分发开销；批次大小 16 时共享每个去噪步骤一次前向传播，吞吐较逐请求分发基线提升 16.0 倍。
- 论文主张输出质量在理论上不应随批次增大而下降，并给出三个支撑假设，单请求规模下 GSM8K 准确率实测为 74% 至 76%。
- 论文推导出泊松到达下固定填充同步批处理的批超时规则，认为服务扩散语言模型需要在每个去噪步骤层面实现并行。
object_mentions:
- object_type: paper
  name: 'Serving Masked Diffusion LLMs: Characterization and Design Principles from
    Real Hardware'
  canonical_name: 'Serving Masked Diffusion LLMs: Characterization and Design Principles
    from Real Hardware'
  url: https://arxiv.org/abs/2608.23807
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - '该论文发表于 arXiv 人工智能分类下，标题为 Serving Masked Diffusion LLMs: Characterization and
    Design Principles from Real Hardware。'
  - 论文目的是在真实并发服务负载下刻画扩散语言模型的行为，并给出面向 dLLM 的服务系统设计原则。
  article_id: fede902dc6ec2be1
- object_type: model
  name: LLaDA-8B-Instruct
  canonical_name: LLaDA-8B-Instruct
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文在单块 NVIDIA H200 GPU 上使用 LLaDA-8B-Instruct 模型搭配 D2F LoRA 适配器进行服务端实测。
  - 该模型在 GSM8K 与 HumanEval 基准上被用于评估扩散语言模型在不同服务负载下的生成表现。
  article_id: fede902dc6ec2be1
- object_type: model
  name: D2F (Discrete Diffusion Forcing) LoRA adapter
  canonical_name: D2F (Discrete Diffusion Forcing)
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - D2F 即 Discrete Diffusion Forcing，以 LoRA 适配器形式叠加在 LLaDA-8B-Instruct 上用于扩散语言模型的服务实验。
  - 论文将其与 LLaDA-8B-Instruct 组合部署在单块 NVIDIA H200 GPU 上进行并发负载测试。
  article_id: fede902dc6ec2be1
- object_type: dataset
  name: GSM8K
  canonical_name: GSM8K
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GSM8K 是论文用于评估 dLLM 服务质量的数学推理基准，单请求规模下实测准确率为 74% 至 76%。
  - 论文通过该基准在扩散语言模型服务实验中验证输出质量与批次大小的关系。
  article_id: fede902dc6ec2be1
- object_type: dataset
  name: HumanEval
  canonical_name: HumanEval
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - HumanEval 是论文用于评估服务质量的代码生成基准，与 GSM8K 一同用于扩散语言模型的负载测试。
  - 该基准与 GSM8K 被用来衡量请求在并发服务负载下的延迟与吞吐特征。
  article_id: fede902dc6ec2be1
extract_result: success
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