---
title: 'Back to the Future: A workbook time machine for spread sheet creation benchmarks'
source: https://arxiv.org/abs/2608.07873
author:
- '[[Mansi Uniyal, Agamdeep Singh, Ananya Singha, Priyanshu Gupta, Mukul Singh, Gust
  Verbruggen, Vu Le, Sumit Gulwani]]'
published: '2026-08-12'
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ac2b1a4ff6a65efd
source_type: academic_paper
tldr: 论文提出“工作簿时光机”自动构建电子表格生成基准，生成含 150 项任务的 wtmbench，用于评估 LLM 在 Excel 中创建公式、图表等派生对象的能力。
objective_summary: 研究人员在 arXiv 发表论文，提出 workbook time machine 流水线，可从公开工作簿语料自动生成（输入工作簿、输出工作簿、查询）三元组，覆盖公式、图表、数据透视表和条件格式四类对象。据此整理出
  wtmbench 基准，共 150 个任务，查询粒度分为三个层级。实验评估了现有电子表格操作智能体与基线，结果表明查询具体程度、智能体编排方式以及控制电子表格的接口
  API 会显著影响 LLM 在 Excel 任务上的表现。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM
  - workbook time machine
  - wtmcorpus
  - wtmbench
  - Excel
  key_people: []
key_logic_flow:
- 论文提出 workbook time machine 流水线，用于自动构建评估语言模型电子表格生成能力的基准。
- 该流水线作用于公开工作簿语料，生成 wtmcorpus 三元组集合，涵盖公式、图表、数据透视表和条件格式四种对象类型。
- 从 wtmcorpus 中筛选出 wtmbench，包含 150 个任务，并按查询具体程度分为三个层级。
- 研究者在 wtmbench 上评估现有电子表格操作智能体与基线方法。
- 实验发现，查询粒度、智能体编排策略以及控制电子表格的接口 API 是影响 LLM Excel 任务表现的关键因素。
object_mentions:
- object_type: paper
  name: 'Back to the Future: A workbook time machine for spread sheet creation benchmarks'
  canonical_name: 'Back to the Future: A workbook time machine for spreadsheet creation
    benchmarks'
  url: https://arxiv.org/abs/2608.07873
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - '标题为 Back to the Future: A workbook time machine for spread sheet creation benchmarks
    的论文发表于 arXiv，摘要介绍了工作簿时光机流水线及其生成的 wtmcorpus 与 wtmbench。'
  article_id: ac2b1a4ff6a65efd
- object_type: project
  name: workbook time machine
  canonical_name: workbook time machine
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文摘要指出，他们引入了 workbook time machine，这是一个自动构建基准的流水线，用于评估语言模型在电子表格中创建派生对象的能力。
  article_id: ac2b1a4ff6a65efd
- object_type: dataset
  name: wtmcorpus
  canonical_name: wtmcorpus
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 将该流水线应用于公开工作簿语料后，产生了 wtmcorpus，它是由（输入工作簿、输出工作簿、查询）三元组组成的集合，覆盖四种对象类型和不同复杂度。
  article_id: ac2b1a4ff6a65efd
- object_type: dataset
  name: wtmbench
  canonical_name: wtmbench
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 研究者从 wtmcorpus 中整理出 wtmbench，这是一个包含 150 个任务的评测基准，查询描述按照三个具体程度层级进行组织。
  article_id: ac2b1a4ff6a65efd
- object_type: product
  name: Microsoft Excel
  canonical_name: Microsoft Excel
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 实验评估现有电子表格操作智能体与基线后，摘要指出查询具体程度、智能体编排以及用于控制电子表格的接口 API 会显著影响 LLM 在 Excel 任务上的表现。
  article_id: ac2b1a4ff6a65efd
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Back to the Future: A workbook time machine for spread sheet creation benchmarks

View PDF HTML (experimental)Abstract:We introduce the workbook time machine, a pipeline that automatically creates benchmarks evaluating the ability of language models to create derived objects in spreadsheets (formulas, charts, pivot tables, and conditional formatting). Applied to public workbook corpora, it produces wtmcorpus--a collection of (input workbook, output workbook, query) triples spanning four artifact types and varying complexity. From this corpus we curate wtmbench, a 150-task evaluation benchmark with queries at three levels of specificity. We evaluate existing spreadsheet manipulation agents and baselines on wtmbench across artifact types, step complexity, and instruction granularity. Our evaluations show that query specificity, agent orchestration, and interface API used to control spreadsheets play a big role in LLM performance on Excel tasks.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.