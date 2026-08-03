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
pipeline_stage: fact_extracted
id: a1cb7e7bade0d25c
source_type: news_media
tldr: PorTAL 推出 Latent Briefing 算法，让多智能体通过 KV cache 直接通信记忆而非传递 token，在准确率不变的情况下减少
  31% 的 token 消耗，并将 320 个顺序求解压缩为 2-3 次批处理操作，速度提升 20 倍（中位耗时 1.7 秒）。
objective_summary: PorTAL 团队在技术介绍中推出 Latent Briefing，一种让多智能体直接共享相关记忆的算法。该方法跳过 token
  空间，在 KV cache 层面进行通信，利用 worker 自身的注意力模式从 orchestrator 的记忆中提取相关内容并丢弃其余部分。团队改编了 Attention
  Matching（AM）压缩框架，并用任务查询打分、跨头全局掩码和 MAD 归一化阈值使其适配推理。实测显示 token 使用量减少 31% 且准确率不变，320
  个顺序求解降为 2-3 次批处理操作，中位耗时 1.7 秒，速度提升 20 倍。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - KV cache
  - Latent Briefing
  - Attention Matching
  - RAG
  - LLM
  - MAD-normalized thresholding
  key_people: []
key_logic_flow:
- 多智能体系统在 token 空间传递上下文会导致成本暴涨和信号丢失，而 LLM 摘要慢且有损、RAG 拆分上下文破坏文档间关联、全量传递上下文昂贵且降低准确率。
- Latent Briefing 让智能体直接进行 KV cache 到 KV cache 的通信，完全跳过 token 空间，利用 worker 的注意力模式从
  orchestrator 记忆中提取相关内容并丢弃其余部分。
- 该方法改编自 Attention Matching（AM）KV cache 压缩框架，并进行三项推理就绪改造：用 worker 任务查询而非自注意力打分、跨所有头应用全局掩码以支持大规模批处理、用
  MAD 归一化阈值实现自适应压缩。
- 实测结果是 token 使用量减少 31% 且准确率保持不变，320 个顺序求解被压缩为 2-3 次批处理操作，速度提升 20 倍，中位耗时降至 1.7 秒。
object_mentions:
- object_type: project
  name: Latent Briefing
  canonical_name: Latent Briefing
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章介绍 Latent Briefing 是一种让智能体直接分享相关记忆的方法，在保持同样准确率的情况下减少了 31% 的 token 消耗。
  - Latent Briefing 跳过 token 空间，直接在 KV cache 之间通信，利用 worker 自身的注意力模式从 orchestrator
    的记忆中提取相关内容并丢弃其余部分。
  article_id: a1cb7e7bade0d25c
- object_type: project
  name: Attention Matching
  canonical_name: Attention Matching
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到团队改编了 Attention Matching（AM）的 KV cache 压缩框架，该算法通过校正项保留注意力输出来压缩 KV cache。
  article_id: a1cb7e7bade0d25c
- object_type: project
  name: PorTAL
  canonical_name: PorTAL
  url: null
  confidence: low
  article_role: primary_subject
  evidence_snippets:
  - 文章标题为 PorTAL，正文围绕其团队构建的 Latent Briefing 方法展开，但正文没有对 PorTAL 本身给出更多细节说明。
  article_id: a1cb7e7bade0d25c
extract_result: success
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