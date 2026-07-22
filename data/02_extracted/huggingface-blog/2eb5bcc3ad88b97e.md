---
title: 'MosaicLeaks: Can your research agent keep a secret?'
source: https://huggingface.co/blog/ServiceNow/mosaicleaks
author: []
published: '2026-06-18'
created: '2026-06-19'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2eb5bcc3ad88b97e
source_type: tech_blog
tldr: ServiceNow 提出了 MosaicLeaks 任务，用于评估深度研究智能体在混合公私有信息查询时通过外部搜索泄露敏感信息的风险。实验表明仅优化任务性能会加重泄露，他们提出的隐私感知训练方法
  PA-DR 将完整信息泄露率从 34.0% 降至 9.9%。
objective_summary: ServiceNow 发布了一篇关于深度研究智能体隐私泄露风险的研究，提出了 MosaicLeaks 评估任务和 PA-DR
  训练方法。该研究将隐私泄露分为意图泄露、答案泄露和完整信息泄露三个层级，并发现仅优化任务性能会加剧泄露。PA-DR 方法将严格链成功率从 48.7% 提升至 58.7%，同时将完整信息泄露率从
  34.0% 降至 9.9%。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - ServiceNow
  technologies:
  - MosaicLeaks
  - PA-DR
  - RL
  key_people: []
key_logic_flow:
- 深度研究智能体在混合使用本地私密文档和外部工具时，其外部搜索查询可能被对手累积分析，从而推断出私密信息，这就是马赛克效应隐私风险。
- ServiceNow 提出了 MosaicLeaks 评估任务，这是一种包含交错公私有信息的多跳问答深度研究任务，以智能体的外部查询日志作为泄露通道来评估隐私泄露程度。
- 他们将泄露分为三个层级：意图泄露（对手可以推断研究目标）、答案泄露（对手可以回答私人问题）和完整信息泄露（对手可以发现并陈述私密事实）。
- 实验表明现有智能体频繁泄露私密信息，且仅针对任务性能进行训练会使隐私泄露更加严重。
- 他们提出了隐私感知深度研究训练方法 PA-DR，将严格链成功率从 48.7% 提升至 58.7%。
- PA-DR 将完整信息泄露率从 34.0% 降至 9.9%，显著增强了智能体在混合信息查询场景下的隐私保护能力。
extract_result: success
object_mentions:
- object_type: project
  name: MosaicLeaks
  canonical_name: ServiceNow MosaicLeaks
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - MosaicLeaks 提出了一种新的深度研究任务，包含交错公私有信息的多跳问题，用于评估智能体在混合查询中的隐私泄露风险。
  - MosaicLeaks 将智能体的网络查询视为泄露通道，对手仅通过累积的查询日志来推断私密的企业信息。
  article_id: 2eb5bcc3ad88b97e
- object_type: project
  name: Privacy-Aware Deep Research (PA-DR)
  canonical_name: PA-DR
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PA-DR 是一种马赛克泄露感知的强化学习训练方法，将严格链成功率从 48.7% 提升至 58.7%。
  - PA-DR 将答案泄露和完整信息泄露率从 34.0% 降至 9.9%，显著降低了智能体在深度研究任务中的隐私泄露风险。
  article_id: 2eb5bcc3ad88b97e
---

Deep research agents increasingly combine private local documents with external tools like web retrieval, creating a privacy risk: an agent's external queries may leak sensitive information. **MosaicLeaks** proposes a new deep-research task with multi-hop questions that interleave public and private information. Across the models we tested, agents frequently leaked private information, and training only for task performance made it worse. We propose a mosaic-leakage-aware RL training method, **Privacy-Aware Deep Research (PA-DR)**, which raises strict chain success (the share of chains where every hop is answered correctly) from 48.7% to 58.7% while reducing answer/full-information leakage from 34.0% to 9.9%.

A research agent at a healthcare firm is working through a routine question, and along the way it fires off a handful of ordinary-looking web searches. One references a cloud-migration milestone, one a January 2024 security disclosure, one narrows down which vendor got hit. No single query necessarily gives away the whole secret. But anyone watching the agent's outbound traffic can reassemble the fragments: MediConn had migrated 70% of its infrastructure to the cloud by January 2025, a fact that lived only in private documents. This is the mosaic effect, and it's the failure mode at the centre of MosaicLeaks.

MosaicLeaks treats those web queries as the leakage channel: the adversary never sees the private documents or the agent's reasoning, only the cumulative query log, and tries to infer private enterprise information from it.

We measure leakage in three ways, depending on what the adversary can infer from the observed queries:

| Leakage type | What the adversary sees | What counts as leakage |
|---|---|---|
Intent leakage |
Only the agent's web-query log | The adversary can infer the private research questions or goals the agent was trying to answer |
Answer leakage |
The web-query log plus a question about private information | The adversary can answer those private questions without seeing the private documents |
Full-information leakage |
Only the web-query log | The adversary can state verifiably true private claims, even without being given the questions |

These three represent increasing levels of concern. Intent leakage reveals *what the agent is investigating*. Answer leakage means the query log holds enough to answer a private question someone already has in hand. Full-information leakage is the strongest case: the observer can discover and state private facts without being told what to look for.