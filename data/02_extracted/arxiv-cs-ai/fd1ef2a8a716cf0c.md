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
tldr: 该论文研究了图结构作为大语言模型内部推理支架的作用，而非仅仅作为外部知识源。实验发现，将图结构扁平化为文本后其效益大幅下降，而视觉图引导即使在去除直接答案提示后仍然有效，表明图应当作为组织推理的可视化支架来研究。
objective_summary: 这篇 arXiv 论文（2606.02673）研究了图结构在大语言模型推理中的新角色。研究者将教师提供的推理轨迹重写为思维导图，用于指导学生模型完成多跳问答任务。实验揭示了一个模态差距：图结构被扁平化为文本后，去除直接答案提示时其效益大幅下降；而视觉图引导在同样的抽象引导设置下仍然保持有效性，这种优势在监督微调和基于
  KL 散度的蒸馏后依然存在。
event_type: application_landing
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Multi-hop QA
  - Knowledge Distillation
  key_people: []
key_logic_flow:
- 论文提出图结构对大语言模型的价值不仅在于提供外部知识，还在于组织推理过程。
- 研究者受到人类使用思维导图组织分支与汇聚思维的启发，探索图作为内部推理辅助手段的可能性。
- 在多跳问答任务上，教师提供的推理轨迹被改写为图思维导图，用于指导学生模型。
- 实验发现，图结构被扁平化为文本后，去除直接答案提示时其效益显著降低，推理效率和回答质量均大幅下降。
- 视觉图引导在去除直接答案线索后仍然保持有效性，且该优势在监督微调和基于 KL 散度的蒸馏后依然存在。
- 论文主张图不仅应作为大语言模型的外部知识结构，还应作为组织推理的可视化支架进行研究。
extract_result: success
object_mentions:
- object_type: paper
  name: Visual Graph Scaffolds for Structural Reasoning in Large Language Models
  canonical_name: Visual Graph Scaffolds for Structural Reasoning in Large Language
    Models
  url: https://arxiv.org/abs/2606.02673
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文研究了图结构作为大语言模型内部推理支架的作用，实验发现视觉图引导比扁平化文本图更有效。
  - 论文基于多跳问答任务，将教师推理轨迹重写为图思维导图来指导学生模型进行结构化推理。
  - 实验揭示了模态差距：视觉图引导在去除直接答案提示后仍然保持有效性，而文本图则效益大幅下降。
  article_id: fd1ef2a8a716cf0c
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