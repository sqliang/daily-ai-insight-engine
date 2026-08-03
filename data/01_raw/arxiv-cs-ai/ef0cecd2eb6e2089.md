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
pipeline_stage: ingested
id: ef0cecd2eb6e2089
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