---
title: 'Enhancing LLMs with Context-Specific Knowledge for Mitigating Misinformation
  in SMEs: A RAG-based Modeling and Analysis'
source: https://arxiv.org/abs/2608.00006
author:
- '[[Md. Samiul Islam, Iqbal H. Sarker, Chadni Islam, Ahmad Mohsin, Ahmed Ibrahim,
  Helge Janicke]]'
published: '2026-08-05'
created: '2026-08-05'
manifest_dates:
- '2026-08-05'
description: 'arXiv:2608.00006v1 Announce Type: new Abstract: Large Language Models
  (LLMs), a part of artificial intelligence (AI), are increasingly being adopted by
  Small and Medium Enterprises (SMEs) to enhance question-answering capabilities and
  support business decision-making processes. However, hallucinations in LLM-generated
  outputs can serve as a source of misinformation, reducing user confidence in their
  reliability and trustworthiness within SMEs. Retrieval-Augmented Generation (RAG)
  has emerged as a promising approach to address this challenge by incorporating external
  knowledge sources into the modeling process. In this paper, we present VectorRAG
  and GraphRAG modeling approaches to mitigate hallucinations and misinformation risks
  and evaluate their effectiveness in SME environments. Our experimental evaluation
  is conducted on multiple state-of-the-art LLMs, including LLaMA, Mistral, and Qwen,
  to assess performance in terms of useful response generation, risk of hallucination,
  contextual relevance, as well as human-interpretation. The results demonstrate that
  RAG-enhanced LLMs can significantly improve response quality by reducing hallucinations
  and misinformation, thereby supporting more reliable, trustworthy, and context-aware
  decision-making in SME environments.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f7dc9b12db57fb7a
source_type: academic_paper
tldr: 该 arXiv 论文提出基于检索增强生成（RAG）的 VectorRAG 与 GraphRAG 建模方法，用于缓解大语言模型在中小企业问答与决策场景中的幻觉和错误信息问题，并在
  LLaMA、Mistral、Qwen 等模型上验证其能提升响应质量。
objective_summary: 论文指出，中小企业越来越多地采用大语言模型（LLM）支持问答与商业决策，但模型幻觉可能成为错误信息来源。作者提出 VectorRAG
  与 GraphRAG 两种检索增强生成建模方法，通过引入外部知识源降低幻觉与错误信息风险。实验在 LLaMA、Mistral、Qwen 等多个主流模型上展开，从有效响应生成、幻觉风险、上下文相关性与人类可解释性等维度进行评估。结果表明，RAG
  增强的 LLM 能显著提升响应质量，从而支持更可靠、可信且具备上下文感知的中小企业决策。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Meta
  - Mistral AI
  - Alibaba
  technologies:
  - RAG
  - VectorRAG
  - GraphRAG
  - LLM
  - LLaMA
  - Mistral
  - Qwen
  key_people: []
key_logic_flow:
- 大语言模型正被中小企业越来越多地用于增强问答能力并支持商业决策，但模型幻觉可能成为错误信息来源，降低用户对其可靠性与可信度的信心。
- 检索增强生成（RAG）通过将外部知识源引入建模过程，被视为缓解这一问题的有效途径。
- 论文提出 VectorRAG 与 GraphRAG 两种建模方法，用以在中小企业环境中降低幻觉与错误信息风险，并评估其实际效果。
- 实验在 LLaMA、Mistral、Qwen 等多个先进大语言模型上进行，重点考察有效响应生成、幻觉风险、上下文相关性以及人类可解释性等指标。
- 结果表明，RAG 增强的 LLM 能显著提升响应质量并减少幻觉与错误信息，从而支持更可靠可信的上下文感知决策。
object_mentions:
- object_type: model
  name: VectorRAG
  canonical_name: VectorRAG
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 VectorRAG 建模方法，利用检索增强生成技术为中小企业环境中的大语言模型引入外部知识源，以缓解幻觉与错误信息风险。
  article_id: f7dc9b12db57fb7a
- object_type: model
  name: GraphRAG
  canonical_name: GraphRAG
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文同时提出 GraphRAG 建模方法，与 VectorRAG 一起在多个大语言模型上进行实验，评估其在中小企业中减少幻觉和错误信息的效果。
  article_id: f7dc9b12db57fb7a
- object_type: model
  name: LLaMA
  canonical_name: LLaMA
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 实验评估在 LLaMA、Mistral、Qwen 等多个先进大语言模型上进行，考察有效响应生成、幻觉风险、上下文相关性与人类可解释性等指标。
  article_id: f7dc9b12db57fb7a
- object_type: model
  name: Mistral
  canonical_name: Mistral
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 实验评估在 LLaMA、Mistral、Qwen 等多个先进大语言模型上进行，考察有效响应生成、幻觉风险、上下文相关性与人类可解释性等指标。
  article_id: f7dc9b12db57fb7a
- object_type: model
  name: Qwen
  canonical_name: Qwen
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 实验评估在 LLaMA、Mistral、Qwen 等多个先进大语言模型上进行，考察有效响应生成、幻觉风险、上下文相关性与人类可解释性等指标。
  article_id: f7dc9b12db57fb7a
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Enhancing LLMs with Context-Specific Knowledge for Mitigating Misinformation in SMEs: A RAG-based Modeling and Analysis

View PDF HTML (experimental)Abstract:Large Language Models (LLMs), a part of artificial intelligence (AI), are increasingly being adopted by Small and Medium Enterprises (SMEs) to enhance question-answering capabilities and support business decision-making processes. However, hallucinations in LLM-generated outputs can serve as a source of misinformation, reducing user confidence in their reliability and trustworthiness within SMEs. Retrieval-Augmented Generation (RAG) has emerged as a promising approach to address this challenge by incorporating external knowledge sources into the modeling process. In this paper, we present VectorRAG and GraphRAG modeling approaches to mitigate hallucinations and misinformation risks and evaluate their effectiveness in SME environments. Our experimental evaluation is conducted on multiple state-of-the-art LLMs, including LLaMA, Mistral, and Qwen, to assess performance in terms of useful response generation, risk of hallucination, contextual relevance, as well as human-interpretation. The results demonstrate that RAG-enhanced LLMs can significantly improve response quality by reducing hallucinations and misinformation, thereby supporting more reliable, trustworthy, and context-aware decision-making in SME environments.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.