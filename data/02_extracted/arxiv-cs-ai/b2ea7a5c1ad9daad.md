---
title: 'BrainBench: Benchmarking Large Language Models for Comprehensive EEG Understanding'
source: https://arxiv.org/abs/2608.04156
author:
- '[[Yangxuan Zhou, Sha Zhao, Yuning Chen, Chen Wu, Jiquan Wang, Shijian Li, Gang
  Pan]]'
published: '2026-08-06'
created: '2026-08-06'
manifest_dates:
- '2026-08-06'
description: 'arXiv:2608.04156v1 Announce Type: new Abstract: Electroencephalography
  (EEG) analysis extends beyond assigning predefined labels to recordings; it requires
  workflows connecting natural-language instructions, signal processing, quantitative
  evidence, and scientific interpretation. We term this capability \emph{comprehensive
  EEG understanding}. Existing evaluations, however, primarily target isolated decoding
  tasks or system-specific demonstrations, leaving the competence of large language
  models (LLMs) insufficiently quantified. We introduce \benchmarkname{}, a unified
  benchmark for comprehensive, instruction-conditioned EEG understanding. It comprises
  four subsets---Foundational Analysis, Sleep Assessment, Neurocognitive Assessment,
  and Physiological Integration---covering 17 datasets, \numcases{} tasks, and over
  \numinstances{} real-data instances. Given an instruction and EEG recordings with
  optional physiological signals, a system must perform the analysis and produce a
  scientifically grounded report and, when required, artifacts. Outputs are assessed
  through numerical, categorical, set, sequence, semantic, and artifact validation.
  We evaluate \nummodels{} representative LLMs across more than 100K executions under
  two paradigms: autonomous code execution with CodeAct and structured agentic analysis
  with BrainAgent. Results vary substantially across models, subsets, difficulty levels,
  and execution paradigms, showing that EEG competence depends on the model and its
  operationalization. \benchmarkname{} provides a reproducible testbed for advancing
  LLM-based EEG understanding. The code and benchmark will be released soon, with
  evaluation results continuously updated.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b2ea7a5c1ad9daad
source_type: academic_paper
tldr: BrainBench 是 arXiv 上发布的一个综合脑电图（EEG）理解基准，包含基础分析、睡眠评估、神经认知评估和生理整合四个子集，覆盖 17 个数据集和大量真实实例。研究者在超过
  10 万次执行中评估了多种大语言模型，结果显示不同模型、子集与执行范式下的 EEG 能力差异显著。
objective_summary: 这篇 arXiv 论文提出了 BrainBench，一个面向全面、指令条件下的 EEG 理解能力的统一基准。该基准包含基础分析、睡眠评估、神经认知评估与生理整合四个子集，覆盖
  17 个数据集。系统需依据指令与 EEG 记录生成科学报告，输出通过数值、类别、集合、序列、语义和产物六种方式验证。研究者在 CodeAct 自主代码执行与 BrainAgent
  结构化智能体分析两种范式下进行了超过 10 万次执行，结果显示 EEG 能力高度依赖模型及其操作化方式。论文称代码与基准将很快发布，评测结果会持续更新。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - EEG
  - CodeAct
  - BrainAgent
  - BrainBench
  key_people: []
key_logic_flow:
- 论文认为 EEG 分析不能停留在给记录贴预定义标签，而需要连接自然语言指令、信号处理、定量证据与科学解释的完整工作流，并将这一能力称为全面 EEG 理解。
- 现有评测主要针对孤立的解码任务或系统特定演示，导致大语言模型在 EEG 上的能力未被充分量化。
- BrainBench 包含基础分析、睡眠评估、神经认知评估和生理整合四个子集，覆盖 17 个数据集和大量真实数据实例。
- 系统需根据指令与 EEG 记录生成科学报告及所需产物，输出通过数值、类别、集合、序列、语义和产物六种方式验证。
- 研究者在 CodeAct 自主代码执行与 BrainAgent 结构化智能体分析两种范式下评估了多个代表性大语言模型，总执行次数超过 10 万次。
- 结果显示不同模型、子集、难度层级和执行范式下表现差异显著，BrainBench 为推进基于大语言模型的 EEG 理解提供了可复现的测试平台。
object_mentions:
- object_type: project
  name: BrainBench
  canonical_name: BrainBench
  url: https://arxiv.org/abs/2608.04156
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - BrainBench 是论文提出的统一基准，用于全面、指令条件下的 EEG 理解评测，包含四个子集并覆盖 17 个数据集。
  - 论文在超过 10 万次执行中评估了多个代表性大语言模型，结果显示模型在不同子集、难度和范式下表现差异显著。
  article_id: b2ea7a5c1ad9daad
- object_type: project
  name: BrainAgent
  canonical_name: BrainAgent
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 论文将 BrainAgent 作为结构化智能体分析范式，与 CodeAct 自主代码执行范式并列用于评测大语言模型的 EEG 理解能力。
  article_id: b2ea7a5c1ad9daad
- object_type: project
  name: CodeAct
  canonical_name: CodeAct
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 论文在两种范式下评估大语言模型，其中 CodeAct 代表自主代码执行范式，用于执行 EEG 分析任务。
  article_id: b2ea7a5c1ad9daad
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:BrainBench: Benchmarking Large Language Models for Comprehensive EEG Understanding

View PDF HTML (experimental)Abstract:Electroencephalography (EEG) analysis extends beyond assigning predefined labels to recordings; it requires workflows connecting natural-language instructions, signal processing, quantitative evidence, and scientific interpretation. We term this capability \emph{comprehensive EEG understanding}. Existing evaluations, however, primarily target isolated decoding tasks or system-specific demonstrations, leaving the competence of large language models (LLMs) insufficiently quantified. We introduce \benchmarkname{}, a unified benchmark for comprehensive, instruction-conditioned EEG understanding. It comprises four subsets---Foundational Analysis, Sleep Assessment, Neurocognitive Assessment, and Physiological Integration---covering 17 datasets, \numcases{} tasks, and over \numinstances{} real-data instances. Given an instruction and EEG recordings with optional physiological signals, a system must perform the analysis and produce a scientifically grounded report and, when required, artifacts. Outputs are assessed through numerical, categorical, set, sequence, semantic, and artifact validation. We evaluate \nummodels{} representative LLMs across more than 100K executions under two paradigms: autonomous code execution with CodeAct and structured agentic analysis with BrainAgent. Results vary substantially across models, subsets, difficulty levels, and execution paradigms, showing that EEG competence depends on the model and its operationalization. \benchmarkname{} provides a reproducible testbed for advancing LLM-based EEG understanding. The code and benchmark will be released soon, with evaluation results continuously updated.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.