---
title: Visual Graph Scaffolds for Structural Reasoning in Large Language Models
source: https://arxiv.org/abs/2606.02673
author:
- '[[Runlin Lei, Xiaokui Xiao, Zhewei Wei]]'
published: '2026-06-03'
created: '2026-06-04'
description: 'arXiv:2606.02673v1 Announce Type: new Abstract: Graphs have been used
  to enhance large language models (LLMs) for structured reasoning, mostly as external
  knowledge sources are provided to models at test time. In this paper, we take a
  different view: the value of graphs for LLMs lie not only in supplying information,
  but also in organizing reasoning. Inspired by how humans use graph-structured mind
  maps to organize branching and converging thoughts, we ask whether graphs can serve
  as an internal form of reasoning assistance. We study this question on multi-hop
  question answering tasks, where teacher-provided reasoning traces are rewritten
  as graph mind maps and used to guide a student model. Our experiments reveal a clear
  modality gap. When graph structures are flattened into text, their benefits become
  limited once direct answer hints are removed. Under this abstract guidance setting,
  both reasoning efficiency and answer quality degrade substantially. In contrast,
  visual graph guidance remains effective without direct answer clues, and its advantage
  persists after supervised fine-tuning and KL-based distillation. The above findings
  support the claim that graphs should be studied not only as external knowledge structures
  for LLMs, but also as visual scaffolds for organizing reasoning.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fd1ef2a8a716cf0c
source_type: academic_paper
tldr: 论文发现：视觉化图结构比文本化图结构更能有效引导LLM的多跳推理，优势在微调和蒸馏后仍保持。
objective_summary: 该论文在arXiv发表，研究图结构在LLM推理中的作用方式。作者通过多跳问答实验，将教师模型的推理轨迹转化为图思维导图来指导学生模型。实验发现，图结构被扁平化为文本后，去除直接答案提示时效果显著下降；而视觉化图引导在无答案线索时仍然有效，且在监督微调和KL蒸馏后优势持续。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Large Language Models
  - LLMs
  key_people: []
key_logic_flow:
- 论文提出新视角：图对LLM的价值不仅在于提供外部知识，还在于组织推理过程本身。
- 受人类使用思维导图组织分支和汇聚思维的启发，论文将图视为推理的内部辅助工具。
- 在多跳问答任务中，将教师提供的推理轨迹改写为图思维导图，用于指导学生模型。
- 实验发现模态鸿沟：图结构被压平为文本后，一旦去除直接答案提示，其益处大幅减弱，推理效率和答案质量均显著下降。
- 相比之下，视觉化图引导在无直接答案线索时仍然有效，且该优势在监督微调和KL蒸馏后依然保持。
- 论文主张图不仅应作为LLM的外部知识结构来研究，也应作为组织推理的视觉化支撑框架。
---

# Computer Science > Artificial Intelligence

# Title:Visual Graph Scaffolds for Structural Reasoning in Large Language Models

View PDF HTML (experimental)Abstract:Graphs have been used to enhance large language models (LLMs) for structured reasoning, mostly as external knowledge sources are provided to models at test time. In this paper, we take a different view: the value of graphs for LLMs lie not only in supplying information, but also in organizing reasoning. Inspired by how humans use graph-structured mind maps to organize branching and converging thoughts, we ask whether graphs can serve as an internal form of reasoning assistance. We study this question on multi-hop question answering tasks, where teacher-provided reasoning traces are rewritten as graph mind maps and used to guide a student model. Our experiments reveal a clear modality gap. When graph structures are flattened into text, their benefits become limited once direct answer hints are removed. Under this abstract guidance setting, both reasoning efficiency and answer quality degrade substantially. In contrast, visual graph guidance remains effective without direct answer clues, and its advantage persists after supervised fine-tuning and KL-based distillation. The above findings support the claim that graphs should be studied not only as external knowledge structures for LLMs, but also as visual scaffolds for organizing reasoning.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.