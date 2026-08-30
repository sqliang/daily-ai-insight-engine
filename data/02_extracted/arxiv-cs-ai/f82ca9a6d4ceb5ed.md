---
title: 'Software Frameworks for Explainable AI in Time Series Classification: A Systematic
  Review'
source: https://arxiv.org/abs/2608.21449
author:
- '[[Louis Peter, Nils Gumpfer, Jana Fischer, Christin Seifert, Jennifer Hannig]]'
published: '2026-08-25'
created: '2026-08-25'
manifest_dates:
- '2026-08-25'
description: 'arXiv:2608.21449v1 Announce Type: new Abstract: Time series arise in
  a wide range of application domains and are analyzed using machine learning in decision-critical
  settings. Time series classification (TSC) is one of the most widely studied and
  relevant tasks. In this context, ensuring the transparency and trustworthiness of
  TSC models has become an important requirement, motivating the use of explainable
  artificial intelligence (XAI) methods. Despite growing interest, research on XAI
  for TSC remains fragmented, and a systematic understanding of the available software
  frameworks for explanation generation, their evaluation practices, and practical
  limitations is still lacking. Prior work largely focused on individual explanation
  methods, while cross-framework consistency, time-series-specific evaluation, and
  reproducibility have received little attention. In this survey, we analyze existing
  software frameworks for explanation generation and evaluation in TSC. We compare
  them along multiple dimensions, including supported XAI methods, evaluation metrics,
  usability, benchmarking support, and reproducibility, providing the first time-series-specific
  survey of frameworks with implementation comparisons and an analysis of frequency-domain
  support. We identify six frameworks that explicitly support time series and reveal
  common limitations: only one method supports frequency-domain explanations despite
  their relevance; only two evaluation metrics have been developed specifically for
  time series; and identical XAI methods can yield substantially different explanations
  across frameworks. Based on these findings, we discuss open challenges and outline
  directions for future research, highlighting the need for unified, time-series-specific
  XAI frameworks that enable faithful, reproducible, and time-series-aware explanations.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f82ca9a6d4ceb5ed
source_type: academic_paper
tldr: 一篇 arXiv 系统综述梳理了时间序列分类（TSC）中可解释人工智能（XAI）的软件框架，比较了六个明确支持时间序列的框架，发现仅一种方法支持频域解释、仅两种评估指标专为时间序列设计，并呼吁构建统一的
  TSC 专用 XAI 框架。
objective_summary: '该综述发表于 arXiv，题为《Software Frameworks for Explainable AI in Time
  Series Classification: A Systematic Review》。作者系统比较了现有 TSC 可解释性框架在支持的 XAI 方法、评估指标、易用性、基准支持和可复现性等维度的差异，识别出六个明确支持时间序列的框架。研究发现跨框架一致性不足，相同
  XAI 方法在不同框架下会产生差异显著的解释结果。作者据此指出开放挑战，呼吁构建统一、时间序列感知且可复现的 XAI 框架。'
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - XAI
  - TSC
  - frequency-domain analysis
  key_people: []
key_logic_flow:
- 该论文在 arXiv 上发表，是首篇针对时间序列分类场景的可解释人工智能软件框架系统综述。
- 研究者从支持的 XAI 方法、评估指标、易用性、基准支持和可复现性等多个维度对现有软件框架进行了比较。
- 论文识别出六个明确支持时间序列的框架，并揭示了它们普遍存在的共同局限。
- 研究显示仅一种框架方法支持频域解释，且只有两种评估指标是专为时间序列设计的。
- 研究发现相同的 XAI 方法在不同框架下可能产生差异显著的解释结果，跨框架一致性不足。
- 作者据此提出开放挑战，呼吁构建统一、时间序列感知且可复现的 XAI 框架以支撑后续研究。
object_mentions:
- object_type: paper
  name: 'Software Frameworks for Explainable AI in Time Series Classification: A Systematic
    Review'
  canonical_name: Software Frameworks for Explainable AI in Time Series Classification
    (arXiv:2608.21449)
  url: https://arxiv.org/abs/2608.21449
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文是首篇针对时间序列分类场景的 XAI 软件框架系统综述，比较了框架在支持方法、评估指标、易用性、基准支持与可复现性等维度的差异。
  - 论文识别出六个明确支持时间序列的框架，并指出仅一种方法支持频域解释、仅两种评估指标专为时间序列设计，且相同方法在不同框架下解释差异明显。
  article_id: f82ca9a6d4ceb5ed
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Software Frameworks for Explainable AI in Time Series Classification: A Systematic Review

View PDF HTML (experimental)Abstract:Time series arise in a wide range of application domains and are analyzed using machine learning in decision-critical settings. Time series classification (TSC) is one of the most widely studied and relevant tasks. In this context, ensuring the transparency and trustworthiness of TSC models has become an important requirement, motivating the use of explainable artificial intelligence (XAI) methods. Despite growing interest, research on XAI for TSC remains fragmented, and a systematic understanding of the available software frameworks for explanation generation, their evaluation practices, and practical limitations is still lacking. Prior work largely focused on individual explanation methods, while cross-framework consistency, time-series-specific evaluation, and reproducibility have received little attention. In this survey, we analyze existing software frameworks for explanation generation and evaluation in TSC. We compare them along multiple dimensions, including supported XAI methods, evaluation metrics, usability, benchmarking support, and reproducibility, providing the first time-series-specific survey of frameworks with implementation comparisons and an analysis of frequency-domain support. We identify six frameworks that explicitly support time series and reveal common limitations: only one method supports frequency-domain explanations despite their relevance; only two evaluation metrics have been developed specifically for time series; and identical XAI methods can yield substantially different explanations across frameworks. Based on these findings, we discuss open challenges and outline directions for future research, highlighting the need for unified, time-series-specific XAI frameworks that enable faithful, reproducible, and time-series-aware explanations.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.