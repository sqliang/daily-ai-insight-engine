---
title: 'TriQua: Reconciling Granularity and Context in Factuality Evaluation'
source: https://arxiv.org/abs/2608.05228
author:
- '[[Jin Liu, Steffen Thoma, Achim Rettinger]]'
published: '2026-08-07'
created: '2026-08-07'
manifest_dates:
- '2026-08-07'
description: 'arXiv:2608.05228v1 Announce Type: new Abstract: The "decompose-then-verify"
  paradigm for LLM factuality evaluation faces a fundamental trade-off: atomic facts,
  i.e., one sentence conveying one unit of information, often omit essential context,
  while broader statements lack the granularity needed for precise assessment. To
  address this, we introduce TriQua, a framework that flexibly models facts based
  on their complexity. Simple claims are extracted as standard triples, while complex
  claims are represented as hyperrelational facts by attaching auxiliary contextual
  qualifiers. This adaptive structure preserves the necessary context for accurate
  retrieval and verification without sacrificing atomicity. Furthermore, TriQua''s
  verification process directly annotates concrete errors within specific triples
  and qualifiers, providing fine-grained explainability for error detection. Alongside
  the framework, we propose TriQuaScore to quantify the factuality of these structured
  fact units. Empirical evaluations show that TriQuaScore strongly aligns with human
  annotated factuality scores, TriQua achieves robust decomposition quality, and outperforms
  existing decomposition-based frameworks in evidence-based fact verification.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cfe28a9da65b5ef1
source_type: academic_paper
tldr: TriQua 论文提出一种按事实复杂度灵活建模的大模型事实性评估框架：简单声明用标准三元组表示，复杂声明用带上下文限定符的超关系事实表示，并配套 TriQuaScore
  评分指标。实验显示其与人类标注的事实性评分高度一致，且在基于证据的事实验证上优于现有分解式框架。
objective_summary: TriQua 是 arXiv 上发表的一篇学术论文，针对大语言模型事实性评估中"先分解再验证"范式面临的粒度与上下文权衡问题。该方法按事实复杂度自适应建模：简单声明被提取为标准三元组，复杂声明则表示为附加上下文限定符的超关系事实，从而在不牺牲原子性的前提下保留检索与验证所需的上下文。TriQua
  的验证过程直接在具体三元组与限定符上标注具体错误，提供细粒度的错误可解释性。实验表明 TriQuaScore 与人类标注的事实性评分高度一致，TriQua 分解质量稳健，并在基于证据的事实验证中优于现有分解式框架。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - TriQua
  - TriQuaScore
  - hyperrelational facts
  - decompose-then-verify
  - factuality evaluation
  - LLM
  key_people: []
key_logic_flow:
- TriQua 提出了面向大模型事实性评估的框架，通过按事实复杂度灵活建模来调和原子性与上下文之间的权衡。
- 简单声明被 TriQua 提取为标准三元组，复杂声明则通过附加上下文限定符表示为超关系事实。
- 这种自适应结构在不牺牲原子性的前提下，保留了精确检索与验证所需的上下文信息。
- TriQua 的验证过程直接在具体三元组和限定符上标注具体错误，为错误检测提供细粒度的可解释性。
- 论文同时提出 TriQuaScore 指标，用于量化这些结构化事实单元的事实性。
- 实验显示 TriQuaScore 与人类标注的事实性评分高度一致，且 TriQua 在基于证据的事实验证中优于现有分解式框架。
object_mentions:
- object_type: paper
  name: 'TriQua: Reconciling Granularity and Context in Factuality Evaluation'
  canonical_name: TriQua (arXiv:2608.05228)
  url: https://arxiv.org/abs/2608.05228
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - '该论文发表于 arXiv 预印本平台，标题为 TriQua: Reconciling Granularity and Context in Factuality
    Evaluation，提出一种兼顾粒度与上下文的大模型事实性评估框架。'
  - 论文指出"先分解后验证"范式在原子事实与完整上下文之间存在根本性权衡，TriQua 正是为化解这一矛盾而设计。
  article_id: cfe28a9da65b5ef1
- object_type: project
  name: TriQua
  canonical_name: TriQua
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - TriQua 是一个面向大模型事实性评估的框架，根据事实复杂度灵活建模：简单声明提取为标准三元组，复杂声明表示为附加上下文限定符的超关系事实。
  - TriQua 的验证过程直接在具体三元组和限定符上标注错误，为错误检测提供细粒度的可解释性。
  article_id: cfe28a9da65b5ef1
- object_type: project
  name: TriQuaScore
  canonical_name: TriQuaScore
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 TriQuaScore 指标，用于量化 TriQua 结构化事实单元的事实性，实验表明其与人类标注的事实性评分高度一致。
  article_id: cfe28a9da65b5ef1
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:TriQua: Reconciling Granularity and Context in Factuality Evaluation

View PDF HTML (experimental)Abstract:The "decompose-then-verify" paradigm for LLM factuality evaluation faces a fundamental trade-off: atomic facts, i.e., one sentence conveying one unit of information, often omit essential context, while broader statements lack the granularity needed for precise assessment. To address this, we introduce TriQua, a framework that flexibly models facts based on their complexity. Simple claims are extracted as standard triples, while complex claims are represented as hyperrelational facts by attaching auxiliary contextual qualifiers. This adaptive structure preserves the necessary context for accurate retrieval and verification without sacrificing atomicity. Furthermore, TriQua's verification process directly annotates concrete errors within specific triples and qualifiers, providing fine-grained explainability for error detection. Alongside the framework, we propose TriQuaScore to quantify the factuality of these structured fact units. Empirical evaluations show that TriQuaScore strongly aligns with human annotated factuality scores, TriQua achieves robust decomposition quality, and outperforms existing decomposition-based frameworks in evidence-based fact verification.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.