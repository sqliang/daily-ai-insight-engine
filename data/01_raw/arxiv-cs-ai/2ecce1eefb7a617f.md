---
title: 'Dual-Flow Transformers: Decoupling the Primary Prefill Path from Additional
  Decode Computation'
source: https://arxiv.org/abs/2608.12385
author:
- '[[Liming Liu, Mingze Wang, Tuo Zhao]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'arXiv:2608.12385v1 Announce Type: new Abstract: As large language models
  serve more requests, cumulative inference cost is becoming increasingly important
  relative to one-time training cost. The two inference phases stress hardware differently:
  prompt prefill is parallel and typically compute-bound, whereas autoregressive decode
  is sequential and often memory-bandwidth-bound. Conventional width or depth scaling
  increases both costs together because every added layer is evaluated in both phases.
  We ask whether additional learned computation can instead be allocated to continuation
  prediction while preserving the prompt-wide primary computation and a single persistent
  key-value (KV) cache. We introduce the Dual-Flow Transformer. Its primary flow is
  a complete causal language model that processes the prompt and writes the KV cache.
  The auxiliary flow is omitted during prompt processing and activated only from the
  final prompt position onward, adding continuation-prediction computation without
  writing persistent state or influencing the primary flow. The two flows share major
  attention, MLP, and output matrices, while using separate token embeddings and lightweight
  coupling. Sharing weights and the primary cache also creates opportunities to reuse
  loaded weights and cached keys and values during grouped execution. Across matched-token
  comparisons, Dual-Flow achieves lower validation loss across architectures and data
  configurations. In MoE models, the separation makes primary and auxiliary expert
  fan-outs independent controls over prompt cost, continuation cost, and predictive
  quality. We study two regimes: increasing decode computation at fixed prefill expert
  computation, and reallocating a fixed decode expert budget between the two flows.
  These experiments expose a prefill-decode-quality trade-off and demonstrate the
  potential of phase-specific expert allocation.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 2ecce1eefb7a617f
---

# Computer Science > Artificial Intelligence

# Title:Dual-Flow Transformers: Decoupling the Primary Prefill Path from Additional Decode Computation

View PDF HTML (experimental)Abstract:As large language models serve more requests, cumulative inference cost is becoming increasingly important relative to one-time training cost. The two inference phases stress hardware differently: prompt prefill is parallel and typically compute-bound, whereas autoregressive decode is sequential and often memory-bandwidth-bound. Conventional width or depth scaling increases both costs together because every added layer is evaluated in both phases. We ask whether additional learned computation can instead be allocated to continuation prediction while preserving the prompt-wide primary computation and a single persistent key-value (KV) cache. We introduce the Dual-Flow Transformer. Its primary flow is a complete causal language model that processes the prompt and writes the KV cache. The auxiliary flow is omitted during prompt processing and activated only from the final prompt position onward, adding continuation-prediction computation without writing persistent state or influencing the primary flow. The two flows share major attention, MLP, and output matrices, while using separate token embeddings and lightweight coupling. Sharing weights and the primary cache also creates opportunities to reuse loaded weights and cached keys and values during grouped execution. Across matched-token comparisons, Dual-Flow achieves lower validation loss across architectures and data configurations. In MoE models, the separation makes primary and auxiliary expert fan-outs independent controls over prompt cost, continuation cost, and predictive quality. We study two regimes: increasing decode computation at fixed prefill expert computation, and reallocating a fixed decode expert budget between the two flows. These experiments expose a prefill-decode-quality trade-off and demonstrate the potential of phase-specific expert allocation.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.