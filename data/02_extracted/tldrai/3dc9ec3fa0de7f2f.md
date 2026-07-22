---
title: 'GeneBench-Pro: Scientific Judgment in AI Agents (9 minute read)'
source: https://openai.com/index/introducing-genebench-pro/?utm_source=tldrai
author: []
published: ''
created: '2026-07-02'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3dc9ec3fa0de7f2f
manifest_dates:
- '2026-07-02'
source_type: news_media
tldr: OpenAI 发布 GeneBench-Pro 基准测试，包含 129 个合成构造问题，用于评估 AI 智能体在计算生物学中的高阶科学判断能力，包括处理模糊性、修正假设和选择正确分析路径。
objective_summary: OpenAI 于 2026 年 7 月 21 日推出 GeneBench-Pro，这是一个面向计算生物学领域的研究级基准测试，用于衡量
  AI 智能体在模糊性下做出科学判断的能力。该基准包含 129 个合成构造的问题，覆盖基因组学、定量生物学和转化医学，要求模型探索数据、选择分析路径并进行迭代实验。其中
  82 个问题已送交外部领域专家（包括研究生、博士后、产业科学家和教授）评审以验证其真实性和答案可识别性。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  technologies:
  - GeneBench-Pro
  - GeneBench
  key_people: []
key_logic_flow:
- OpenAI 发布 GeneBench-Pro 基准测试，旨在衡量 AI 智能体在计算生物学中处理模糊性和进行高阶判断的能力。
- 该基准定义了"研究品味"为塑造分析流程的一系列判断链，包括数据能支持哪些问题、早期诊断如何改变模型或估计量、以及何时需要修正初始计划。
- GeneBench-Pro 包含 129 个问题，覆盖基因组学、定量生物学和转化医学领域，每个问题提供真实且混乱的数据集、实验上下文和面向下游决策的目标估计量。
- 为避免传统基准的失败模式，每个问题均通过合成方式构建以确保因果结构已知，通过消融研究验证错误分析路径不会产生通过结果。
- 82 个问题已送交外部领域专家评审，包括研究生、博士后、产业科学家和教授，以确保问题的真实性和分析方法的适当性。
- 专家反馈指出，这些问题对研究生而言即使有资深导师的迭代反馈也颇具挑战性，要求对数据质量和潜在陷阱进行深入反思分析。
extract_result: success
object_mentions:
- object_type: project
  name: GeneBench-Pro
  canonical_name: GeneBench-Pro
  url: https://openai.com/index/introducing-genebench-pro/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 发布 GeneBench-Pro，这是一个研究级基准测试，用于测试模型是否能处理现实计算生物学中需要大量判断的分析任务。
  - 该基准包含 129 个合成构造的问题，覆盖基因组学、定量生物学和转化医学，要求模型探索数据、选择分析路径并进行迭代实验。
  - 其中 82 个问题已送交外部领域专家（包括研究生、博士后、产业科学家和教授）评审，以验证问题的真实性和答案可识别性。
  article_id: 3dc9ec3fa0de7f2f
- object_type: project
  name: GeneBench
  canonical_name: GeneBench
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GeneBench-Pro 在原有 GeneBench 的基础上扩展，覆盖了更困难、更贴近实际的任务。
  - GeneBench 是 GeneBench-Pro 的前身基准，新基准在此基础上提升了任务难度和现实性。
  article_id: 3dc9ec3fa0de7f2f
---

# Introducing GeneBench-Pro

A research-level benchmark measuring how AI agents navigate ambiguity and make consequential judgments in computational biology.

Scientific data rarely arrive with instructions. Researchers must decide whether a pattern reflects biology or noise, whether the data can support the question being asked, and how each result should change what they do next. AI agents are increasingly capable of executing complex analyses, but real scientific research also depends not simply on recalling facts or following a predefined workflow but also on making these higher-order judgments.

Today, we’re introducing GeneBench-Pro—a challenging, research-level benchmark for testing whether models can handle the kind of judgment-heavy analysis that real-world computational biology requires. It expands on __GeneBench__(opens in a new window) to cover harder, more realistic tasks across genomics, quantitative biology, and translational medicine, capturing the complexity, iterative nature, and ambiguity of scientific research in computational biology.

To date, there have been few convincing assessments of the system-level judgment calls that make real-world computational research difficult. These include handling ambiguity, revising assumptions, choosing the correct analysis path, and knowing when a result is decision-ready. Because these skills are difficult to formalize, they are also difficult to assess rigorously, even as weaknesses in them increasingly constrain overall AI performance.

GeneBench-Pro is designed to precisely measure these higher-level capabilities. Within GeneBench-Pro, we define “research taste” as the chains of judgment calls that shape an analysis: which questions the data can support, how early diagnostics should change the model or estimand, and when an initial plan needs to be revised. Each GeneBench-Pro problem gives the model a realistic and messy dataset, brief experimental context, and a target estimand tied to a downstream decision. To answer correctly, the model must explore the data, choose an appropriate analytical approach, engage in an iterative process of experimentation, and supply a final answer.

In biology, the cost of data generation (e.g., genome sequencing) has fallen dramatically, and __some researchers now argue__(opens in a new window) that the limiting factor is no longer sample collection but downstream computation and analysis. GeneBench-Pro is built to assess progress in addressing that bottleneck, with 129 questions covering a broad range of computational biology settings and methods.

GeneBench-Pro is also designed to avoid common benchmark failures. Many long-horizon biology benchmarks construct multi-step questions around messy historical datasets, where there may be no single correct path through the analysis. An agent might choose one defensible cutoff, while another might choose a different but equally defensible option, reflecting the arbitrary choices made by the benchmark creator more than any fundamental differences in model performance. The reverse can also happen: if a problem is too numerically insensitive, an agent can make fundamental errors in an analysis and still produce a passing result.

To avoid these failure modes, each GeneBench-Pro problem is built synthetically: we know the full causal structure and directly simulate the data-generating process. That enables us to tune the complexity of each problem, ensure that reasonable differences in subjective analytical choices still produce accepted numerical results, and verify (through ablation studies) that plausible but incorrect analyses fail. We then audit problem drafts through detailed trace analyses to check for information leakage and unintended solution pathways. This gives us confidence that getting the right answer depends on choosing the correct analytic pathway and not on exploiting a shortcut or matching an arbitrary author preference.

We sent 82 of the 129 GeneBench-Pro questions to external domain experts, including graduate students, postdoctoral researchers, industry scientists, and professors. Reviewers assessed each problem’s realism, whether the target answer was identifiable, and whether the methods and estimators were appropriate. Feedback was used to improve problems.

“The problems I reviewed would have beenchallenging for a graduate studentto complete without iterated feedback from an experienced supervisor. The data contained technical and quality control issues that required thoughtful and reflective data analysis with awareness of potential pitfalls to complete successfully; they were not simply applying some off-the-shelf method to clean and well curated data.”