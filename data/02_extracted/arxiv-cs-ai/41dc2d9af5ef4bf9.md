---
title: 'SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema
  Induction and Fusion from Text'
source: https://arxiv.org/abs/2607.21610
author:
- '[[Miaobo Hu, Xiaobo Guo, Shuhao Hu, Bokun Wang, Rui Chen, Xin Wang, Daren Zha,
  Jun Xiao]]'
published: '2026-07-27'
created: '2026-07-27'
manifest_dates:
- '2026-07-27'
description: 'arXiv:2607.21610v1 Announce Type: new Abstract: Schema graphs are an
  upstream bottleneck of schema-grounded information extraction and knowledge graph
  construction, yet most extraction systems assume the schema is already available.
  We introduce SCOPE (Schema Construction and Ontology-induction Pipeline Evaluation),
  a train-text-only benchmark for corpus-to-schema induction and optional schema fusion
  from raw text, built from 24 public information extraction sources (15 RE and 9
  EE) normalized into evaluation-only gold schema graphs; its core event-extraction
  target covers event types and within-event argument roles, with inter-event links
  reported separately. We present SCION (Schema Construction and Induction with Ontology
  Normalization), an auditable reference pipeline rather than a new extraction architecture;
  it constructs candidate spaces from train text and restricts naming, merging, filtering,
  validation, and conservative fusion to candidate-linked evidence under strict JSON
  contracts. On the SCOPE core suite, SCION-lite attains the highest F1 among released
  source-schema references, Text2Onto-style, LLM-only, and matched extract-then-aggregate
  baselines under Literal, Fuzzy, Continuous, and Graph schema-graph metrics, while
  the compact open-model SCION-RL variant reduces reliance on proprietary LLM schema
  engineers. These results are reported against normalized typed-edge targets rather
  than as claims that induced schemas surpass human ontology design; the release includes
  evidence-linked outputs, parse/fallback logs, candidate retention/merging logs,
  run manifests, code, and benchmark packages at https://github.com/wandugu/paper_scion.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 41dc2d9af5ef4bf9
source_type: academic_paper
tldr: 该论文提出了SCOPE基准和SCION可审计管线，用于从原始文本中进行模式归纳与融合。SCOPE基于24个公开信息抽取源构建了评估标准模式图，SCION则是一个通过严格JSON合约进行候选空间构建与命名的可审计参考管线。实验表明SCION-lite在多项指标上超越现有基线，SCION-RL变体可减少对专有大语言模型的依赖。
objective_summary: arXiv论文（2026年7月）提出了SCOPE基准（模式构建与本体归纳管道评估）和SCION管线（模式构建与本体归一化归纳）。SCOPE包含24个公开信息抽取源（15个关系抽取和9个事件抽取），归一化为仅用于评估的标准模式图。SCION是一个可审计的参考管线，通过候选空间构建、命名、合并、过滤、验证和保守融合等步骤，在严格JSON合约下运作。实验显示SCION-lite在字面、模糊、连续和图模式图指标上均取得最高F1分数，SCION-RL变体使用紧凑的开源模型降低了对专有LLM的依赖。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - SCOPE
  - SCION
  - SCION-lite
  - SCION-RL
  - Text2Onto
  key_people: []
key_logic_flow:
- 论文指出模式图是模式驱动信息抽取和知识图谱构建的上游瓶颈，但大多数抽取系统假设模式已预先可用。
- SCOPE基准从24个公开信息抽取源（15个关系抽取和9个事件抽取）构建了仅用于评估的标准模式图，覆盖事件类型、事件内参数角色和事件间链接。
- SCION管线通过从训练文本构建候选空间，并在严格的JSON合约下进行命名、合并、过滤、验证和保守融合等操作。
- SCION-lite在字面匹配、模糊匹配、连续匹配和图模式图四种指标上均取得最高F1分数，超越了Text2Onto风格、仅LLM、以及抽取后聚合等基线方法。
- SCION-RL变体使用紧凑的开源模型取代专有LLM作为模式工程师，降低了对专有大语言模型的依赖。
- 论文发布了包含证据链接的输出、解析/回退日志、候选保留/合并日志、运行清单、代码和基准测试包。
object_mentions:
- object_type: project
  name: SCOPE
  canonical_name: SCOPE Benchmark
  url: https://arxiv.org/abs/2607.21610
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SCOPE是一个训练文本仅用基准，用于语料库到模式的归纳和可选模式融合，从24个公开信息抽取源构建。
  - 其核心事件抽取目标覆盖事件类型和事件内参数角色，事件间链接单独报告。
  article_id: 41dc2d9af5ef4bf9
- object_type: project
  name: SCION
  canonical_name: SCION Pipeline
  url: https://arxiv.org/abs/2607.21610
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SCION是一个可审计参考管线而非新的抽取架构，在严格JSON合约下构建候选空间并进行命名、合并、过滤、验证和保守融合。
  - SCION-lite在SCOPE核心套件上取得最高F1分数，超越多种基线方法。
  - SCION-RL变体使用紧凑开源模型减少对专有LLM模式工程师的依赖。
  article_id: 41dc2d9af5ef4bf9
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema Induction and Fusion from Text

View PDFAbstract:Schema graphs are an upstream bottleneck of schema-grounded information extraction and knowledge graph construction, yet most extraction systems assume the schema is already available. We introduce SCOPE (Schema Construction and Ontology-induction Pipeline Evaluation), a train-text-only benchmark for corpus-to-schema induction and optional schema fusion from raw text, built from 24 public information extraction sources (15 RE and 9 EE) normalized into evaluation-only gold schema graphs; its core event-extraction target covers event types and within-event argument roles, with inter-event links reported separately. We present SCION (Schema Construction and Induction with Ontology Normalization), an auditable reference pipeline rather than a new extraction architecture; it constructs candidate spaces from train text and restricts naming, merging, filtering, validation, and conservative fusion to candidate-linked evidence under strict JSON contracts. On the SCOPE core suite, SCION-lite attains the highest F1 among released source-schema references, Text2Onto-style, LLM-only, and matched extract-then-aggregate baselines under Literal, Fuzzy, Continuous, and Graph schema-graph metrics, while the compact open-model SCION-RL variant reduces reliance on proprietary LLM schema engineers. These results are reported against normalized typed-edge targets rather than as claims that induced schemas surpass human ontology design; the release includes evidence-linked outputs, parse/fallback logs, candidate retention/merging logs, run manifests, code, and benchmark packages at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.