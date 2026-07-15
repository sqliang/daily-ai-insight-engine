---
title: Meta's Watermelon Matches GPT-5.5 Benchmarks (3 minute read)
source: https://letsdatascience.com/news/metas-watermelon-matches-gpt-55-benchmarks-76a9460e?utm_source=tldrai
author: []
published: ''
created: '2026-07-04'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5ad8f0bc5bfec4f6
manifest_dates:
- '2026-07-04'
- '2026-07-05'
source_type: news_media
tldr: Meta 内部模型 Watermelon 据称在基准测试中追上 GPT-5.5，但未经独立验证。
objective_summary: Alexandr Wang 在 Meta 内部全体会议上声称，正在训练中的 Watermelon 模型在 AI 基准测试中已追上
  OpenAI 的 GPT-5.5。该模型使用了比 Muse Spark 多一个数量级的算力。此消息源自 Business Insider 援引两名匿名知情人士，Meta
event_type: application_landing
epistemic_status: rumor_leak
entities:
  companies:
  - Meta
  - OpenAI
  - Business Insider
  technologies:
  - Watermelon
  - Muse Spark
  - GPT-5.5
  - GPT-5.6
  key_people:
  - Alexandr Wang
key_logic_flow:
- Meta 人工智能负责人 Alexandr Wang 在内部全体会议上声称，正在训练中的模型 Watermelon 在基准测试中已追上 OpenAI 的 GPT-5.5。
- Watermelon 使用了比此前模型 Muse Spark（内部代号 Avocado）多一个数量级的训练算力，表明 Meta 以算力规模为核心竞争策略。
- 该消息源自 Business Insider 援引两名匿名知情人士，Business Insider 未明确 Wang 引用了哪些具体基准测试。
- OpenAI 已于 2026 年 4 月发布 GPT-5.5，并于上月底发布 GPT-5.6。
- Meta 和 OpenAI 均未对 Business Insider 的报道作出官方回应或确认。
- 文章指出在 Meta 发布公开模型卡或可复现评估结果之前，该声称应被视为早期信号而非经过验证的事实。
extract_result: success
---

Meta's superintelligence chief **Alexandr Wang** told employees in a town hall that the company's upcoming model, codenamed **Watermelon**, has "caught up" with OpenAI's **GPT-5.5** on closely followed AI benchmarks, according to Business Insider, which cited two people familiar with the matter. Wang reportedly said Watermelon is still in training and uses "an order of magnitude more compute" than **Muse Spark** (Meta's April model, internally codenamed Avocado), which had trailed rival models despite solid benchmark scores. Business Insider notes it was not clear which benchmarks Wang cited, and neither Meta nor OpenAI has confirmed the claim. For practitioners, an internal, single-sourced benchmark claim is not equivalent to a published, reproducible evaluation and should be treated as an early signal, not a verified result, until Meta releases the model publicly.

An unconfirmed internal benchmark claim from Meta's AI leadership is a reminder that town-hall statements are not evaluation artifacts: until Meta publishes reproducible results or a model card for Watermelon, "caught up with GPT-5.5" is a single-sourced assertion, not verified parity. For practitioners tracking the frontier-model race, the more concrete signal here is the compute trajectory Wang described, not the benchmark claim itself.

According to Business Insider, **Alexandr Wang** told Meta employees in a town hall that the company's upcoming model, codenamed **Watermelon**, "has caught up" with OpenAI's **GPT-5.5** based on closely followed AI benchmarks, citing two people familiar with the matter. Business Insider reports Wang said Watermelon, the successor to Avocado (Meta's internal codename for Muse Spark), is "currently in training" and "uses an order of magnitude more compute than Avocado." OpenAI released GPT-5.5 in April and introduced GPT-5.6 late last month, per Business Insider. Meta declined to comment and OpenAI did not respond to a request for comment. Investing.com, redistributing the Business Insider report, added that it was not immediately clear which benchmarks Wang was citing.

Meta released Muse Spark in April 2026, its first major model since hiring Wang, and it performed well on some benchmarks while still falling short of leading rivals overall. Wang's description of Watermelon using "an order of magnitude more compute" than Muse Spark points to continued aggressive scaling as Meta's primary lever, consistent with the company's reported multibillion-dollar spending on chips and data centers under Zuckerberg's direct oversight of AI development.

Treat this as a leading indicator, not a procurement signal. Internal benchmark claims announced without published methodology, evaluation datasets, or third-party replication carry a real risk of optimistic framing. Wait for a public model card, an official benchmark table, or independent evaluations before factoring Watermelon into model-selection or capacity-planning decisions.

Meta has not given a release timeline for Watermelon. Watch for a public launch announcement, published benchmark results, and whether the model narrows the gap with GPT-5.5 and GPT-5.6 on independently run evaluations rather than internally cited ones.

## Key Points

- 1Meta's AI chief told staff Watermelon has matched GPT-5.5 on internal benchmarks, per a single Business Insider report citing anonymous sources.
- 2Wang described Watermelon as using far more training compute than April's Muse Spark, underscoring compute scaling as Meta's core strategy.
- 3Practitioners should wait for published benchmarks or independent evaluations before treating the parity claim as verified for deployment decisions.

## Scoring Rationale

Notable signal in the Meta-OpenAI frontier-model race given Meta's competitive stakes, but the claim rests on a single anonymous-sourced town-hall statement with no published benchmark data, and neither company confirmed specifics, so it stays provisional pending independent verification.

## Sources

Public references used for this report.

Practice with real Ad Tech data

90 SQL & Python problems · 15 industry datasets