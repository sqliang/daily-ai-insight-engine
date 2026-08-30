---
title: DiffusionGemma Technical Report
source: https://arxiv.org/abs/2608.00146
author:
- '[[gmays]]'
published: '2026-08-20'
created: '2026-08-20'
manifest_dates:
- '2026-08-20'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ffb2d30bbc94ba4a
source_type: community_discussion
tldr: DiffusionGemma 是一个实验性开源权重语言模型，采用离散扩散机制并行迭代精炼 256 个 token 的块，绕开自回归模型的顺序解码瓶颈；在单块
  NVIDIA H100 上每秒约输出 1500 个 token，训练预算不足原模型的 10%。
objective_summary: DiffusionGemma 是基于 mixture-of-experts 架构的 Gemma 4（3.8B 激活参数、25.2B
  总参数）微调得到的实验性开源权重语言模型。其两阶段训练流程以不足原模型 10% 的 token 预算完成，第一阶段用监督微调教授双向去噪，第二阶段将强化学习与采样器蒸馏结合以同时改进生成质量和推理效率。在单块
  NVIDIA H100 GPU 上，该模型每次前向传播约生成 20 个 token、每秒约输出 1500 个 token，显著快于采用最先进投机解码的自回归模型，并保留思维模式、多模态输入和长上下文支持。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Google DeepMind
  - NVIDIA
  technologies:
  - discrete diffusion
  - mixture-of-experts
  - speculative decoding
  - reinforcement learning
  - sampler distillation
  - supervised fine-tuning
  key_people: []
key_logic_flow:
- DiffusionGemma 是一种使用离散扩散机制生成文本的实验性开源权重语言模型。
- 与逐 token 解码的自回归模型不同，它并行迭代精炼 256 个 token 的块，从而绕开顺序解码瓶颈。
- 该模型通过在 mixture-of-experts 架构的 Gemma 4 模型上微调获得，总训练 token 预算不足原模型的 10%。
- 两阶段训练中，第一阶段用监督微调学习双向去噪，第二阶段将强化学习与采样器蒸馏结合，同时改进生成质量与推理效率。
- 在完整评测套件上，模型每次前向传播约生成 20 个 token，在单块 NVIDIA H100 上每秒约输出 1500 个 token，快于采用投机解码的自回归模型。
- 模型保留思维模式、多模态输入和长上下文支持，仍可进行自回归生成且性能降级较小，指向混合扩散-自回归解码方向。
object_mentions:
- object_type: model
  name: DiffusionGemma
  canonical_name: DiffusionGemma
  url: https://arxiv.org/abs/2608.00146
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - DiffusionGemma 是实验性的开源权重语言模型，使用离散扩散在并行块中迭代精炼 256 个 token，而非逐 token 顺序解码。
  - 在单块 NVIDIA H100 GPU 上，DiffusionGemma 每秒约输出 1500 个 token，大幅快于采用最先进投机解码的自回归模型。
  article_id: ffb2d30bbc94ba4a
- object_type: model
  name: Gemma 4
  canonical_name: Gemma 4
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - DiffusionGemma 由 mixture-of-experts 架构的 Gemma 4 模型微调而来，该模型拥有 3.8B 激活参数和 25.2B
    总参数。
  article_id: ffb2d30bbc94ba4a
extract_result: success
---

# Computer Science > Computation and Language

# Title:DiffusionGemma Technical Report

View PDF HTML (experimental)Abstract:We introduce DiffusionGemma, an experimental open-weight language model that uses discrete diffusion to generate text at exceptionally high speed. Rather than decoding one token at a time, DiffusionGemma iteratively refines blocks of 256 tokens in parallel, avoiding the sequential decoding bottleneck of conventional autoregressive (AR) large language models. Instead of training from scratch, we obtain DiffusionGemma by fine-tuning the mixture-of-experts Gemma 4 model with 3.8B activated and 25.2B total parameters. Our compute-efficient two-stage training pipeline uses fewer than 10% of the starting AR model's total training token budget. The first stage uses supervised fine-tuning to teach bidirectional denoising, while the second stage combines reinforcement learning with sampler distillation to jointly improve generation quality and inference efficiency. DiffusionGemma establishes a new Pareto frontier for the trade-off between generation speed and model capability. Averaged across our full evaluation suite, it generates around 20 tokens per forward pass and achieves roughly 1,500 output tokens per second on a single NVIDIA H100 GPU, which is substantially faster than AR models even with state-of-the-art speculative decoding. DiffusionGemma also retains the starting model's support for thinking mode, multimodal inputs, and long contexts. Despite diffusion fine-tuning, it remains capable of AR generation with only minor performance degradation, suggesting a path toward hybrid diffusion-AR decoding.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.