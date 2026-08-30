---
title: 'Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release
  for Long-Horizon Agents'
source: https://arxiv.org/abs/2608.12476
author:
- '[[Guodong Xu]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'arXiv:2608.12476v1 Announce Type: new Abstract: Long-term agent memory
  is usually treated as select--store--retrieve, but retrieval does not decide whether
  contradictory, superseded, retracted, deleted, or stale records may support an outgoing
  claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition
  model with source-bound admission, derived lifecycle state, current public barriers,
  and fail-closed structured release. Five executable clauses cover ledger integrity,
  source binding, conflict isolation, non-revival after retraction or deletion, and
  exact claim closure over a fresh view at one verified head. On a prespecified hash-frozen
  3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of
  three intentionally simple complete policies matches 1,800/3,600 and makes unmatched
  releases on 50% of violation cases. A separate sealed end-to-end service evaluation
  exercises real ingestion and release across eight query families. In its publicly
  disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400
  for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no
  regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over
  Chinese- and English-command arms, with generation-date pinning and no post-freeze
  reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent
  finite model explores 331,776 semantic and 1,990,656 query states without a full-contract
  counterexample, and a 100,000-trace three-engine differential yields zero mismatches.
  These are bounded contract and implementation results, not open-world model accuracy
  or evidence of world truth. Governed answers in the sealed service evaluation are
  deterministic service outputs; the 7B result is the ungoverned comparison, not a
  claim that a language model itself became perfectly accurate.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3e5bbba96a6cde57
source_type: academic_paper
tldr: 论文提出 Governed Persistent Memory（GPM），一种可审计的双时态状态转换模型，为长时程智能体实现源绑定、生命周期状态与失败关闭的持久记忆管理。在
  3600 例基准与密封服务评测中，受管通道正确率显著优于未受管的本地 Qwen2.5-7B，作者强调这是有界合约与实现结果。
objective_summary: 论文提出 GPM，一种可审计的双时态状态转换模型，用于解决长时程智能体在检索时无法判定冲突、过期、撤回或删除记录是否支撑输出声明的问题，核心包括源绑定准入、派生生命周期状态与失败关闭的结构化释放。GPM
  定义五个可执行条款，并在哈希冻结的 3600 例 GPM-ReleaseBench 上匹配全部完整结果。在密封端到端服务评测 V3 分支中，受管通道在 2400/2400
  集群上正确，未受管的本地 Qwen2.5-7B 仅 600/2400，且修复全部 1800 个基线失败无回归；V5 重新密封的中英文分支再次各取得 2400/2400。作者明确这些是有界合约与实现结果，而非开放世界模型准确率或世界真实性证据。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Alibaba
  technologies:
  - GPM
  - Qwen2.5-7B
  - bitemporal state-transition model
  key_people: []
key_logic_flow:
- GPM 将长时程智能体记忆从简单的选择—存储—检索扩展为可审计的双时态状态转换模型，引入源绑定准入、派生生命周期状态、当前公开壁垒和失败关闭的结构化释放。
- GPM 定义五个可执行条款，覆盖账本完整性、源绑定、冲突隔离、撤回或删除后禁止复活，以及在单一验证头部的新鲜视图上实现精确声明闭合。
- 在哈希冻结的 3600 例 GPM-ReleaseBench 上，GPM 匹配所有完整结果，而最强的三种简单策略中最好者仅匹配 1800/3600，并在 50%
  的违规案例上做出不匹配释放。
- 密封端到端服务评测覆盖八个查询家族，V3 分支中受管通道在 2400/2400 集群上正确，未受管的本地 Qwen2.5-7B 仅 600/2400，且修复全部
  1800 个基线失败且无回归。
- V5 重新密封涵盖中英文指令分支，采用生成日期固定且不做冻结后归约修正，两个分支均再次取得 2400/2400。
- 与生产代码无关的有限模型探索 331776 个语义状态和 1990656 个查询状态而无完整合约反例，10 万条轨迹的三引擎差分测试零失配；作者明确这些结果是有界合约与实现结果而非世界真实性证据。
object_mentions:
- object_type: model
  name: Governed Persistent Memory
  canonical_name: Governed Persistent Memory (GPM)
  url: https://arxiv.org/abs/2608.12476
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 GPM，一种可审计的双时态状态转换模型，为长时程智能体提供源绑定准入、派生生命周期状态和失败关闭的结构化释放。
  - GPM 定义五个可执行条款，覆盖账本完整性、源绑定、冲突隔离、撤回或删除后禁止复活，以及精确声明闭合。
  article_id: 3e5bbba96a6cde57
- object_type: dataset
  name: GPM-ReleaseBench
  canonical_name: GPM-ReleaseBench
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在预置哈希冻结的 3600 例 GPM-ReleaseBench 上，GPM 匹配所有完整结果，而最强的简单策略只匹配 1800/3600。
  - 该基准对比受管 GPM 与简单策略，结果显示简单策略在 50% 的违规案例上产生不匹配释放，而 GPM 匹配全部完整结果。
  article_id: 3e5bbba96a6cde57
- object_type: model
  name: Qwen2.5-7B
  canonical_name: Qwen2.5-7B
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在密封服务评测 V3 分支中，未受管的本地 Qwen2.5-7B 在 2400 个集群中仅正确 600 个，作为受管通道的对照基线。
  - 作者强调 V3 分支中的 7B 结果是未受管对照，而非声称语言模型本身达到了完全准确。
  article_id: 3e5bbba96a6cde57
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents

View PDF HTML (experimental)Abstract:Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release. Five executable clauses cover ledger integrity, source binding, conflict isolation, non-revival after retraction or deletion, and exact claim closure over a fresh view at one verified head.

On a prespecified hash-frozen 3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of three intentionally simple complete policies matches 1,800/3,600 and makes unmatched releases on 50% of violation cases. A separate sealed end-to-end service evaluation exercises real ingestion and release across eight query families. In its publicly disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400 for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over Chinese- and English-command arms, with generation-date pinning and no post-freeze reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent finite model explores 331,776 semantic and 1,990,656 query states without a full-contract counterexample, and a 100,000-trace three-engine differential yields zero mismatches.

These are bounded contract and implementation results, not open-world model accuracy or evidence of world truth. Governed answers in the sealed service evaluation are deterministic service outputs; the 7B result is the ungoverned comparison, not a claim that a language model itself became perfectly accurate.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.