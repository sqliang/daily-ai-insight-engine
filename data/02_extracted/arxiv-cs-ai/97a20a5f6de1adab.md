---
title: 'Position: Evaluation Scores Are Perishable Knowledge Claims'
source: https://arxiv.org/abs/2607.26191
author:
- '[[Sankalp Gilda, Shlok Gilda]]'
published: '2026-07-31'
created: '2026-07-31'
manifest_dates:
- '2026-07-31'
description: 'arXiv:2607.26191v1 Announce Type: new Abstract: Evaluation methodologies
  for language models increasingly combine multiple signals, from automated metrics
  and LLM-as-judge ratings to human assessments and benchmark suite results. When
  these signals are aggregated via averaging, evaluation confidence can then substantially
  exceed the reliability of the weakest signal: a phenomenon we call trust inflation
  in evaluation. We argue that evaluation scores should be treated as epistemic claims
  with three properties: formality (human evaluation provides stronger evidence than
  an automated metric), scope (a benchmark result applies to the tested distribution,
  not universally), and validity windows (benchmark results expire as contamination
  accumulates and distributions shift). Several converging research traditions (chain-of-thought
  analysis, possibilistic logic, and algebraic theory) establish weakest-link aggregation
  as the conservative endpoint of a parameterized operator family controlled by a
  single pessimism parameter. Drawing on those traditions, and on concrete lessons
  from building an evaluation harness for agentic AI, we propose that evaluation results
  carry explicit metadata (formality tier, scope declaration, and expiration date)
  to make their epistemic status transparent. We illustrate the cost of mean aggregation
  on the public HELM leaderboard: across 54 frontier models on ten scenarios, the
  top-five models ranked by mean score and by weakest-link are completely disjoint.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 97a20a5f6de1adab
source_type: academic_paper
tldr: 本文是 arXiv 位置论文，主张将大模型评估分数视为具有形式性、作用范围与有效期三种属性的认知主张，指出多种信号取均值聚合会造成"信任膨胀"。论文提出以最弱环节聚合作为保守聚合端点，并建议评估结果携带显式元数据。在
  HELM 排行榜上，54 个模型按均值与最弱环节排序的前五名完全不重叠。
objective_summary: 这篇 arXiv 位置论文（编号 2607.26191）讨论了语言模型评估中自动指标、LLM-as-judge 评分、人类评估与基准测试等信号被取均值聚合后产生的信任膨胀问题。作者主张评估分数应被视为具有形式性、作用范围和有效期三种属性的认知主张，并借鉴思维链分析、可能逻辑与代数理论确立最弱环节聚合为保守聚合端点。论文建议评估结果携带形式性等级、范围声明与过期日期等显式元数据以公开其认识论状态。论文以公共
  HELM 排行榜为反例验证观点：54 个前沿模型在十个场景下按均值与最弱环节排序的前五名完全不相交。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM-as-judge
  - HELM
  - chain-of-thought analysis
  - possibilistic logic
  key_people: []
key_logic_flow:
- 论文指出语言模型评估方法日益整合自动指标、LLM-as-judge 评分、人类评估和基准测试等多种信号。
- 当这些信号通过取平均值聚合时，评估置信度可能大幅超过最弱信号的真实可靠性，作者称之为评估中的信任膨胀。
- 作者主张评估分数应被视为具有形式性、作用范围和有效期三种属性的认知主张。
- 思维链分析、可能逻辑与代数理论等研究传统共同确立最弱环节聚合为受单一悲观参数控制的算子族保守端点。
- 论文提议评估结果应携带形式性等级、范围声明和过期日期等显式元数据，以透明化其认识论状态。
- 公共 HELM 排行榜数据显示，54 个前沿模型在十个场景下按均值与最弱环节排序的前五名完全不相交。
object_mentions:
- object_type: paper
  name: 'Position: Evaluation Scores Are Perishable Knowledge Claims'
  canonical_name: 'Position: Evaluation Scores Are Perishable Knowledge Claims'
  url: https://arxiv.org/abs/2607.26191
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - '文章标题为《Position: Evaluation Scores Are Perishable Knowledge Claims》，来源为 arXiv
    预印本平台，编号 2607.26191，属于计算机科学领域的人工智能方向。'
  article_id: 97a20a5f6de1adab
- object_type: project
  name: HELM
  canonical_name: HELM
  url: https://crfm.stanford.edu/helm/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 论文以公共 HELM 排行榜为例说明均值聚合的代价：54 个前沿模型在十个场景下按均值与最弱环节排序的前五名完全不相交。
  article_id: 97a20a5f6de1adab
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Position: Evaluation Scores Are Perishable Knowledge Claims

View PDF HTML (experimental)Abstract:Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results. When these signals are aggregated via averaging, evaluation confidence can then substantially exceed the reliability of the weakest signal: a phenomenon we call trust inflation in evaluation. We argue that evaluation scores should be treated as epistemic claims with three properties: formality (human evaluation provides stronger evidence than an automated metric), scope (a benchmark result applies to the tested distribution, not universally), and validity windows (benchmark results expire as contamination accumulates and distributions shift). Several converging research traditions (chain-of-thought analysis, possibilistic logic, and algebraic theory) establish weakest-link aggregation as the conservative endpoint of a parameterized operator family controlled by a single pessimism parameter. Drawing on those traditions, and on concrete lessons from building an evaluation harness for agentic AI, we propose that evaluation results carry explicit metadata (formality tier, scope declaration, and expiration date) to make their epistemic status transparent. We illustrate the cost of mean aggregation on the public HELM leaderboard: across 54 frontier models on ten scenarios, the top-five models ranked by mean score and by weakest-link are completely disjoint.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.