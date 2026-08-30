---
title: 'SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation'
source: https://arxiv.org/abs/2608.17426
author:
- '[[Keyu Tu, Zhuowei Chen, Mengqi Huang, Yuxin Wang, Jiahao Zhu, Zhendong Mao, Yongdong
  Zhang]]'
published: '2026-08-20'
created: '2026-08-20'
manifest_dates:
- '2026-08-20'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cbb026dedc7a0a31
source_type: academic_paper
tldr: 论文提出面向结果的视频生成任务语义任务完成（Semantic Task Completion），并构建覆盖六个领域的 SemComp-Data 数据集与基于视觉语言模型的
  SemComp-Bench 评估协议，实验表明现有视频生成模型在达成预期结果与保持语义接地上仍有挑战。
objective_summary: 该论文于 arXiv 发布（编号 2608.17426），提出语义任务完成视频生成这一面向结果的新任务，要求同时达成预期结果与语义接地。作者构建了覆盖六个领域的评估数据集
  SemComp-Data，每个实例包含参考图像、详细指令、简短指令和以结果为中心的视频片段，并通过可扩展的四阶段整理流水线将原始视频标准化。论文还提出 SemComp-Bench
  评估协议，用视觉语言模型回答结构化二值问题，分别报告结果达成分数（OA Score）与生成可靠性分数（GR Score）。在代表性视频生成模型上的实验表明，在达成预期结果的同时保持任务相关的语义接地仍然困难。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - SemComp-Bench
  - SemComp-Data
  - VLM
  - Semantic Task Completion Video Generation
  - Video Generation
  key_people: []
key_logic_flow:
- 论文提出语义任务完成视频生成这一面向结果的新任务，成功标准同时要求达成预期结果与语义接地。
- 语义接地刻画参考图像与生成结果之间在任务相关高层语义上的对应关系，评估只关注生成结果，不要求完整中间步骤序列或常规外观一致性。
- 为支持系统评估，作者构建了覆盖六个领域的评估数据集 SemComp-Data，每个实例包含参考图像、详细指令、简短指令和以结果为中心的视频片段。
- 一个可扩展的四阶段整理流水线将原始视频转换为标准化的 SemComp-Data 实例。
- 论文提出 SemComp-Bench 评估协议，使用视觉语言模型回答结构化二值问题，并报告结果达成分数（OA Score）与生成可靠性分数（GR Score）。
- 在代表性视频生成模型上的实验表明，在达成预期结果的同时保持参考图像中任务相关的语义接地仍然具有挑战性。
object_mentions:
- object_type: paper
  name: 'SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation'
  canonical_name: 'SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation'
  url: https://arxiv.org/abs/2608.17426
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文在 arXiv 上发布，提出语义任务完成视频生成这一面向结果的新任务，并配套构建了评估数据集 SemComp-Data 与评估协议 SemComp-Bench。
  article_id: cbb026dedc7a0a31
- object_type: project
  name: SemComp-Bench
  canonical_name: SemComp-Bench
  url: https://arxiv.org/abs/2608.17426
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SemComp-Bench 是论文提出的评估协议，使用视觉语言模型回答结构化二值问题，并报告结果达成分数（OA Score）与生成可靠性分数（GR Score）。
  article_id: cbb026dedc7a0a31
- object_type: dataset
  name: SemComp-Data
  canonical_name: SemComp-Data
  url: https://arxiv.org/abs/2608.17426
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SemComp-Data 是覆盖六个领域的评估数据集，每个实例包含参考图像、详细指令、简短指令以及以结果为中心的视频片段。
  article_id: cbb026dedc7a0a31
extract_result: success
---

# Computer Science > Computer Vision and Pattern Recognition

# Title:SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation

View PDF HTML (experimental)Abstract:We introduce Semantic Task Completion Video Generation, an outcome-oriented video generation task. Under this formulation, success requires both achievement of the intended outcome and semantic grounding. Semantic grounding characterizes the correspondence between the reference image and the generated outcome in terms of high-level semantics relevant to the task. Evaluation focuses on the generated outcome and requires neither the presentation of a complete sequence of intermediate task steps nor conventional appearance consistency with the reference image. To support systematic evaluation, we construct SemComp-Data, an evaluation dataset covering six domains. Each instance comprises a reference image, a detailed instruction, a brief instruction, and an outcome-centric video clip. A scalable four-stage curation pipeline converts raw videos into standardized SemComp-Data instances. We further introduce SemComp-Bench, an evaluation protocol that uses a vision-language model (VLM) to answer structured binary questions. SemComp-Bench reports the OA Score and the GR Score for Outcome Achievement and Generation Reliability, respectively. Experiments on representative video generation models show that achieving intended outcomes while maintaining task-relevant semantic grounding in reference images remains challenging.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.