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
tldr: Meta AI 负责人 Alexandr Wang 在内部全体会上称，正在训练的新模型 Watermelon 在 AI 基准测试上已追平 OpenAI
  的 GPT-5.5，且其训练算力比上一代 Muse Spark 高出一个数量级，但该说法来自匿名信源且未经双方公司证实。
objective_summary: Business Insider 援引两名知情人士报道称，Meta 超级智能负责人 Alexandr Wang 在内部全体会议上告诉员工，正在训练中的下一代模型
  Watermelon 在多项 AI 基准测试上已追平 OpenAI 的 GPT-5.5。Wang 表示 Watermelon 使用的训练算力比 Meta 在 2026
  年 4 月发布的 Muse Spark（内部代号 Avocado）高出一个数量级，且模型仍在训练中。报道未说明 Wang 引用的是哪些具体基准测试，Meta 拒绝置评，OpenAI
  也未回应置评请求。在 Meta 公开模型或发布可复现的基准结果之前，应将该声明视为早期信号而非已验证结论。
event_type: infrastructure_update
epistemic_status: rumor_leak
entities:
  companies:
  - Meta
  - OpenAI
  - Business Insider
  technologies: []
  key_people:
  - Alexandr Wang
key_logic_flow:
- Meta 超级智能负责人 Alexandr Wang 在内部全体会上声称，正在训练的新模型 Watermelon 在 AI 基准测试上已追平 OpenAI 的
  GPT-5.5。
- Wang 表示 Watermelon 使用的训练算力比 Meta 四月发布的 Muse Spark（内部代号 Avocado）高出一个数量级。
- 该报道源自 Business Insider 引用的两名匿名知情人士，Meta 和 OpenAI 均未确认这一说法，所引用的基准测试也未被明确披露。
- OpenAI 于 2026 年 4 月发布了 GPT-5.5，并在上月末推出了 GPT-5.6。
- Meta 在 2026 年 4 月发布的 Muse Spark（Wang 加入后的首个重大模型）在某些基准上表现良好，但整体仍落后于领先竞品。
- 在 Meta 发布公开模型卡或独立评测结果之前，该声明不应被用于模型选型或容量规划决策。
extract_result: success
object_mentions:
- object_type: model
  name: Watermelon
  canonical_name: Meta Watermelon
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - Meta 超级智能负责人 Alexandr Wang 在内部全体会上称，正在训练的新模型 Watermelon 在基准测试上已追平 OpenAI 的 GPT-5.5。
  - Wang 表示 Watermelon 使用的训练算力比 Muse Spark（内部代号 Avocado）高出一个数量级，且模型仍在训练中。
  - Business Insider 援引匿名人士报道称，Meta 尚未公布 Watermelon 的发布时间表，该声明需等待独立验证。
  article_id: 5ad8f0bc5bfec4f6
- object_type: model
  name: Muse Spark
  canonical_name: Meta Muse Spark
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Meta 于 2026 年 4 月发布了 Muse Spark（内部代号 Avocado），这是 Meta 自聘请 Alexandr Wang 以来推出的首个重大模型。
  - Muse Spark 在某些基准测试上表现良好，但整体仍落后于领先竞品，因此 Watermelon 的算力大幅提升被视为追赶策略的关键。
  article_id: 5ad8f0bc5bfec4f6
- object_type: model
  name: GPT-5.5
  canonical_name: OpenAI GPT-5.5
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 于 2026 年 4 月发布了 GPT-5.5，Wang 声称 Watermelon 已在该模型的基准测试水平上追平。
  - OpenAI 在上月末推出了 GPT-5.6，但报道未说明 Watermelon 与 GPT-5.6 的比较情况。
  article_id: 5ad8f0bc5bfec4f6
- object_type: model
  name: GPT-5.6
  canonical_name: OpenAI GPT-5.6
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 在 2026 年 4 月发布 GPT-5.5 后，于上月末进一步推出了 GPT-5.6。
  article_id: 5ad8f0bc5bfec4f6
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