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
pipeline_stage: fact_extracted
id: 2ecce1eefb7a617f
source_type: academic_paper
tldr: Dual-Flow Transformer 论文提出将提示预填充的主计算路径与解码阶段的额外计算解耦：辅助流程仅在提示末尾后激活。实验显示在匹配 token
  下取得更低验证损失，并支持 MoE 中按阶段独立分配专家计算。
objective_summary: 该 arXiv 预印本提出 Dual-Flow Transformer 架构，将预填充阶段的主计算与解码阶段的辅助计算解耦。主流程是一个完整的因果语言模型，负责处理提示并写入
  KV 缓存；辅助流程仅在最后提示位置后激活，不写持久状态也不影响主流程。两个流程共享注意力、MLP 与输出矩阵，但使用独立的 token 嵌入与轻量耦合。作者报告在匹配
  token 的对比中，该架构在多种架构与数据配置下取得更低验证损失，并实验了固定预填充专家计算下增加解码计算、以及在两流程间重新分配解码专家预算两种 MoE 情形。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Dual-Flow Transformer
  - MoE
  - KV cache
  key_people: []
key_logic_flow:
- 大规模语言模型服务请求增多后，累计推理成本相对于一次性训练成本的重要性正在上升。
- 提示预填充阶段并行且通常受计算限制，而自回归解码阶段串行且常受内存带宽限制，传统宽度或深度扩展会同时增加两个阶段的成本。
- Dual-Flow Transformer 的主流程是一个完整的因果语言模型，负责处理提示并写入 KV 缓存，辅助流程仅在最后提示位置起激活且不写持久状态。
- 两个流程共享注意力、MLP 与输出矩阵，同时使用独立 token 嵌入与轻量耦合，权重与主缓存共享使分组执行时可复用已加载权重和缓存的键值。
- 在匹配 token 的对比中，Dual-Flow 在多种架构与数据配置下取得更低的验证损失。
- 在 MoE 模型中主辅专家扇出成为独立控制手段，实验研究了两种解码专家预算分配情形并揭示了预填充-解码-质量权衡。
object_mentions:
- object_type: paper
  name: Dual-Flow Transformers
  canonical_name: Dual-Flow Transformers
  url: https://arxiv.org/abs/2608.12385
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出 Dual-Flow Transformer 架构，其主流程处理提示并写入 KV 缓存，辅助流程仅在最后提示位置之后激活且不写持久状态。
  - 两个流程共享主要的注意力、MLP 和输出矩阵，同时使用独立的 token 嵌入与轻量耦合，从而在匹配 token 的对比中取得更低验证损失。
  article_id: 2ecce1eefb7a617f
extract_result: success
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