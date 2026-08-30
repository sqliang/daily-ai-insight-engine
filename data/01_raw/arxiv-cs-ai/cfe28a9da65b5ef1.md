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
pipeline_stage: ingested
id: cfe28a9da65b5ef1
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