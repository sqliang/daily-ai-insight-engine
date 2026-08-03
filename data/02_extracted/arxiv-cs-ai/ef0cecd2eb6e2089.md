---
title: 'SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative
  Verification'
source: https://arxiv.org/abs/2607.20475
author:
- '[[Pragaash Ponnusamy, Shivam Sahni, Jue Wang, Tri Dao]]'
published: '2026-07-24'
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
description: 'arXiv:2607.20475v1 Announce Type: new Abstract: Sampling in LLM inference
  comprises a combinatorial set of logit processing, token selection, and verification
  operations for speculative decoding. However, existing implementations either accelerate
  only subsets of this pipeline, rely on multiple kernel launches, or assume homogeneous
  sampling behavior across a batch, limiting support for dynamic serving workloads
  and preventing efficient CUDA Graph execution. We present $\textbf{SonicSampler}$,
  a unified suite of tile-aware Triton kernels that vertically fuses the complete
  sampling pipeline into a fixed, workload-aware execution model. Our kernels support
  dynamic per-request sampling behaviors, including grammar-constrained decoding,
  repetition, frequency and presence penalties, logit bias, temperature scaling, top-$k$
  / top-$p$ / min-$p$ filtering, and speculative verification - within a single batched
  kernel while remaining fully CUDA Graph-compatible. Central to our approach is a
  novel hierarchical two-stage top-$k$ algorithm that achieves up to $\textbf{10x
  speedup}$ over competitive baselines and exploits the low-entropy structure of LLM
  outputs to enable efficient selection over large vocabularies. Across heterogeneous
  speculative decoding workloads, SonicSampler achieves up to $\textbf{16x speedup}$
  over state-of-the-art baselines while preserving flexible batched execution.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ef0cecd2eb6e2089
source_type: academic_paper
tldr: SonicSampler 提出了一套基于 Triton 的统一 tile 感知内核套件，将 LLM 推理的完整采样流水线垂直融合为单一负载感知执行模型，支持动态逐请求采样行为和推测解码验证，在异构推测解码工作负载上最高实现
  16 倍加速。
objective_summary: 该论文提出了 SonicSampler，一套基于 Triton 的统一 tile 感知内核套件，用于 LLM 推理中的采样操作。它将包括对数概率处理、令牌选择和推测解码验证在内的完整采样流水线垂直融合到单一批处理内核中，支持动态逐请求采样行为（包括语法约束解码、重复惩罚、温度缩放和
  top-k/top-p/min-p 过滤）。SonicSampler 采用一种新颖的分层两阶段 top-k 算法，利用 LLM 输出的低熵结构实现高效的大词汇表选择，在竞争基线之上实现最高
  10 倍加速，并在异构推测解码工作负载上达到最高 16 倍加速。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Triton
  - CUDA
  - CUDA Graph
  - speculative decoding
  - top-k filtering
  - top-p filtering
  - min-p filtering
  key_people: []
key_logic_flow:
- SonicSampler 是一套基于 Triton 的统一 tile 感知内核套件，将 LLM 推理采样流水线（对数处理、令牌选择、验证）垂直融合为单一批处理内核。
- 该方案支持动态逐请求采样行为，包括语法约束解码、重复/频率/存在惩罚、对数偏差、温度缩放、top-k/top-p/min-p 过滤以及推测解码验证。
- SonicSampler 在单个内核中实现完整的采样流水线，同时保持完全 CUDA Graph 兼容性，避免了多内核启动带来的额外开销。
- 核心创新是一种分层两阶段 top-k 算法，利用 LLM 输出的低熵结构实现高效的大词汇表选择，在竞争基线之上实现最高 10 倍加速。
- 在异构推测解码工作负载上，SonicSampler 相比最先进基线实现了最高 16 倍加速，同时保持了灵活的批处理执行能力。
object_mentions:
- object_type: paper
  name: 'SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative
    Verification'
  canonical_name: SonicSampler
  url: https://arxiv.org/abs/2607.20475
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SonicSampler 是一套基于 Triton 的统一 tile 感知内核套件，将 LLM 推理的完整采样流水线垂直融合为单一批处理内核。
  - 该方案支持动态逐请求采样行为，包括语法约束解码、重复/频率/存在惩罚、温度缩放和 top-k/top-p/min-p 过滤等操作。
  - SonicSampler 采用分层两阶段 top-k 算法，在竞争基线之上实现最高 10 倍加速，在异构推测解码工作负载上达到最高 16 倍加速。
  article_id: ef0cecd2eb6e2089
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative Verification

View PDF HTML (experimental)Abstract:Sampling in LLM inference comprises a combinatorial set of logit processing, token selection, and verification operations for speculative decoding. However, existing implementations either accelerate only subsets of this pipeline, rely on multiple kernel launches, or assume homogeneous sampling behavior across a batch, limiting support for dynamic serving workloads and preventing efficient CUDA Graph execution. We present $\textbf{SonicSampler}$, a unified suite of tile-aware Triton kernels that vertically fuses the complete sampling pipeline into a fixed, workload-aware execution model. Our kernels support dynamic per-request sampling behaviors, including grammar-constrained decoding, repetition, frequency and presence penalties, logit bias, temperature scaling, top-$k$ / top-$p$ / min-$p$ filtering, and speculative verification - within a single batched kernel while remaining fully CUDA Graph-compatible. Central to our approach is a novel hierarchical two-stage top-$k$ algorithm that achieves up to $\textbf{10x speedup}$ over competitive baselines and exploits the low-entropy structure of LLM outputs to enable efficient selection over large vocabularies. Across heterogeneous speculative decoding workloads, SonicSampler achieves up to $\textbf{16x speedup}$ over state-of-the-art baselines while preserving flexible batched execution.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.