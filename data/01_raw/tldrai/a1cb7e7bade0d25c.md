---
title: PorTAL (1 minute read)
source: https://threadreaderapp.com/thread/2081819550329327689.html?utm_source=tldrai
author: []
published: ''
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: a1cb7e7bade0d25c
---

Introducing Latent Briefing, a way for agents to quickly share their relevant memory directly. Result: 31% fewer tokens used, same accuracy.

Multi-agent systems are powerful, but can be wildly inefficient. They pass context as tokens, so costs explode and signal gets lost. We built an algorithm that allows agents to communicate KV cache to KV cache.

Agents need to share context, but doing it in token space has real tradeoffs:

• LLM summaries: slow (20–60s), lossy, and often miss what the next agent actually needs
• RAG: splits context into chunks, so relationships across documents get lost
• Passing full context: expensive, noisy, and often hurts accuracy

Our method skips tokens entirely. We operate on the KV cache, using the worker's own attention patterns to extract what's relevant from the orchestrator's memory and discard the rest.

We adapted the Attention Matching (AM) KV cache compaction framework. The AM algorithm compacts the KV cache (C1, β, C2) preserving attention outputs through a correction term.

We modified the algorithm to make it inference ready: 1. Score tokens using the worker's task query, not self attention 2. Global mask across all heads → enables massive batching 3. MAD-normalized thresholding for adaptive compression

Result: 320 sequential solves → 2-3 batched ops. 20x speedup to a median of 1.7 s.