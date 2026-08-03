---
title: 'Library Reachability in LSR-Synth: How Anti-Memorization Design Changes the
  Measurement of Symbolic Discovery'
source: https://arxiv.org/abs/2607.28684
author:
- '[[Zhan''ao Yao, Liang Yin, Zhihao Gao, Boxuan Zhang, Xiaoyu Wu, Linjing Li, Rongyan
  Wang, Tingwei Chen, Youwei Wang, Xiaolin Zhao, Jiahui Shi, Jianjun Liu]]'
published: '2026-08-03'
created: '2026-08-03'
manifest_dates:
- '2026-08-03'
description: 'arXiv:2607.28684v1 Announce Type: new Abstract: Existing benchmarks
  for scientific equation discovery are largely composed of well-known equations available
  in the public domain, making it difficult to determine whether a model is discovering
  laws from data or merely recalling answers from its training corpus. LSR-Synth mitigates
  this problem by introducing novel synthetic terms into established scientific mechanisms
  and filtering the resulting tasks for novelty, solvability, and scientific plausibility.
  This paper examines a narrower measurement question: can these tasks further distinguish
  scientific priors supplied by language models from conventional operator search
  that does not access task semantics? We construct a semantics-free baseline using
  a fixed vocabulary with publicly documented provenance, and assess the role of candidate
  coverage through semantic blinding, library weakening, and matched operator-family
  knockouts. Under the current task snapshot, search budget, and scoring protocol,
  the fixed vocabulary already covers most tasks, while language-model-generated candidates
  rarely expand the set of solvable instances. Their marginal contribution becomes
  substantial only when vocabulary coverage is selectively disrupted. Strict out-of-distribution
  evaluation lowers the absolute success rates of all methods but does not alter this
  relationship. These findings neither invalidate LSR-Synth''s controls against memorization
  of complete formulas nor imply that language-model priors are generally unhelpful.
  Rather, they support a more limited conclusion: most current tasks remain suitable
  for evaluating the fitting and recombination of previously unseen expressions, but
  are insufficient on their own to identify contributions from priors beyond a fixed
  search space.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f83fdbe042e6dcf6
source_type: academic_paper
tldr: 论文评估符号发现基准 LSR-Synth 能否区分语言模型的科学先验与常规算子搜索。结果发现固定词汇表已覆盖大部分任务，语言模型候选仅在词汇覆盖被选择性破坏时才显著扩大可解集合，说明当前任务不足以独立识别先验贡献。
objective_summary: 本文（arXiv:2607.28684）研究符号方程发现基准 LSR-Synth 的测量特性，检验其任务能否区分语言模型提供的科学先验与不访问任务语义的常规算子搜索。作者用固定词汇表构建无语义基线，通过语义盲化、词汇表削弱与匹配算子族剔除来评估候选覆盖的作用。实验表明，在当前任务快照、搜索预算与评分协议下，固定词汇表已覆盖大多数任务，语言模型生成的候选很少扩大可解实例；其边际贡献仅在词汇覆盖被选择性破坏时才变得显著。严格的分布外评估降低了所有方法的绝对成功率，但未改变这一关系。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LSR-Synth
  - Symbolic Equation Discovery
  - Operator Search
  - Large Language Models
  key_people: []
key_logic_flow:
- 现有科学方程发现基准大多由公共领域的知名方程构成，因此难以判断模型是从数据中真正发现定律，还是从训练语料中记忆答案。
- LSR-Synth 通过向既有科学机制中引入新颖合成项，并对任务进行新颖性、可解性和科学合理性过滤，来缓解对完整公式的记忆问题。
- 本文构造了使用固定词汇表且不访问任务语义的基线，并通过语义盲化、词汇表削弱和匹配算子族剔除来评估候选覆盖的作用。
- 在当前任务快照、搜索预算和评分协议下，固定词汇表已经覆盖了大部分任务，语言模型生成的候选很少扩大可解实例的集合。
- 语言模型候选的边际贡献只有在词汇覆盖被选择性破坏时才变得显著；严格的分布外评估降低了所有方法的绝对成功率，但未改变这一关系。
- 作者认为这些结果既不否定 LSR-Synth 对完整公式记忆的控制，也不意味着语言模型先验普遍无用，只说明当前任务不足以单独识别先验的贡献。
object_mentions:
- object_type: project
  name: LSR-Synth
  canonical_name: LSR-Synth
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - LSR-Synth 通过向既有科学机制中引入新颖合成项，并对任务进行新颖性、可解性和科学合理性过滤，以缓解模型从训练语料记忆完整公式的问题。
  - 论文构建了一个使用固定词汇表、不访问任务语义的无语义基线，以评估语言模型生成的候选是否扩大了可解实例的集合。
  article_id: f83fdbe042e6dcf6
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Library Reachability in LSR-Synth: How Anti-Memorization Design Changes the Measurement of Symbolic Discovery

View PDF HTML (experimental)Abstract:Existing benchmarks for scientific equation discovery are largely composed of well-known equations available in the public domain, making it difficult to determine whether a model is discovering laws from data or merely recalling answers from its training corpus. LSR-Synth mitigates this problem by introducing novel synthetic terms into established scientific mechanisms and filtering the resulting tasks for novelty, solvability, and scientific plausibility. This paper examines a narrower measurement question: can these tasks further distinguish scientific priors supplied by language models from conventional operator search that does not access task semantics? We construct a semantics-free baseline using a fixed vocabulary with publicly documented provenance, and assess the role of candidate coverage through semantic blinding, library weakening, and matched operator-family knockouts. Under the current task snapshot, search budget, and scoring protocol, the fixed vocabulary already covers most tasks, while language-model-generated candidates rarely expand the set of solvable instances. Their marginal contribution becomes substantial only when vocabulary coverage is selectively disrupted. Strict out-of-distribution evaluation lowers the absolute success rates of all methods but does not alter this relationship. These findings neither invalidate LSR-Synth's controls against memorization of complete formulas nor imply that language-model priors are generally unhelpful. Rather, they support a more limited conclusion: most current tasks remain suitable for evaluating the fitting and recombination of previously unseen expressions, but are insufficient on their own to identify contributions from priors beyond a fixed search space.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.