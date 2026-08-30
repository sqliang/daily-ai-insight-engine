---
title: 'Hate Speech Classification In Roman Urdu: A Comparative Study On Parameter
  Efficient Fine-Tuning And Prompt Engineering'
source: https://arxiv.org/abs/2608.21408
author:
- '[[Toneema Zubair]]'
published: '2026-08-25'
created: '2026-08-25'
manifest_dates:
- '2026-08-25'
description: 'arXiv:2608.21408v1 Announce Type: new Abstract: Due to the widespread
  accessibility of the internet and social media, toxic and hateful con-tent has grown
  exponentially, causing significant distress and negative societal impacts. Ro-man
  Urdu, a low-resource language used in Pakistan and among Urdu-speaking communities
  worldwide, presents additional challenges because of its informal grammar, inconsistent
  sen-tence structures, and multiple variations in word spellings. This research aims
  to identify the most effective techniques for hate speech classification in such
  low-resource settings with limited data. To address this, the study investigates
  and compares the latest approaches, in-cluding prompt tuning, parameter-efficient
  fine-tuning (PEFT) using LoRA, and prompt en-gineering, under various experimental
  configurations. To achieve this objective, four exper-iments were designed. The
  first experiment involved direct inferencing with LLMs without any fine-tuning,
  to evaluate how well these models understand Roman Urdu in a zero-shot setting,
  especially given limited data. The second experiment utilized parameter-efficient
  fine-tuning (PEFT) with LoRA, which updates only a small subset of parameters, thereby
  reducing computational cost. The third experiment explored prompt tuning with both
  mixed and manually crafted prompts, using very small sets of training examples relative
  to the entire dataset, making it computationally efficient as well. Finally, the
  fourth experiment applied prompt engineering through zero-shot and few-shot learning,
  relying solely on care-fully designed instruction prompts for classification without
  further training.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: efae21be59ab69d3
source_type: academic_paper
tldr: 该论文研究罗马乌尔都语这一低资源语言的仇恨言论分类，设计了四个实验对比零样本推理、LoRA 参数高效微调、提示调优与提示工程等方法，旨在数据有限条件下找出最有效的分类技术。论文以
  arXiv 预印本形式发布，编号为 2608.21408。
objective_summary: 研究者针对巴基斯坦及全球乌尔都语社区使用的罗马乌尔都语开展仇恨言论分类研究，该语言因非正式语法、不一致句式和拼写多变而处理难度高。研究设计了四个实验：大语言模型零样本直接推理、基于
  LoRA 的参数高效微调、混合与手工提示的提示调优、以及零样本和少样本的提示工程。各实验均围绕在低资源、数据有限的条件下比较不同技术的分类效果与计算成本，论文以
  arXiv 预印本形式发布。
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LoRA
  - PEFT
  - Prompt Tuning
  - Prompt Engineering
  - LLM
  key_people: []
key_logic_flow:
- 研究背景是互联网与社交媒体上恶意和仇恨内容激增，罗马乌尔都语因非正式语法、不一致句式及拼写多变而构成额外处理挑战。
- 研究目标是在低资源、数据有限的条件下，找出罗马乌尔都语仇恨言论分类最有效的技术。
- 实验一使用大语言模型直接推理，不做任何微调，以零样本方式评估模型对罗马乌尔都语的理解能力。
- 实验二采用基于 LoRA 的参数高效微调，仅更新一小部分参数，从而降低计算成本。
- 实验三进行提示调优，使用混合与手工设计的提示，并采用相对于全量数据集很小的训练示例集。
- 实验四应用零样本与少样本学习的提示工程，仅依靠精心设计的指令提示完成分类，不进行额外训练。
object_mentions:
- object_type: paper
  name: 'Hate Speech Classification In Roman Urdu: A Comparative Study On Parameter
    Efficient Fine-Tuning And Prompt Engineering'
  canonical_name: Hate Speech Classification in Roman Urdu
  url: https://arxiv.org/abs/2608.21408
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文研究罗马乌尔都语这一低资源语言的仇恨言论分类，核心目标是识别数据有限场景下最有效的分类技术。
  - 论文设计了四个实验，系统对比零样本直接推理、基于 LoRA 的参数高效微调、提示调优以及零样本和少样本提示工程。
  article_id: efae21be59ab69d3
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Hate Speech Classification In Roman Urdu: A Comparative Study On Parameter Efficient Fine-Tuning And Prompt Engineering

View PDFAbstract:Due to the widespread accessibility of the internet and social media, toxic and hateful con-tent has grown exponentially, causing significant distress and negative societal impacts. Ro-man Urdu, a low-resource language used in Pakistan and among Urdu-speaking communities worldwide, presents additional challenges because of its informal grammar, inconsistent sen-tence structures, and multiple variations in word spellings. This research aims to identify the most effective techniques for hate speech classification in such low-resource settings with limited data. To address this, the study investigates and compares the latest approaches, in-cluding prompt tuning, parameter-efficient fine-tuning (PEFT) using LoRA, and prompt en-gineering, under various experimental configurations. To achieve this objective, four exper-iments were designed. The first experiment involved direct inferencing with LLMs without any fine-tuning, to evaluate how well these models understand Roman Urdu in a zero-shot setting, especially given limited data. The second experiment utilized parameter-efficient fine-tuning (PEFT) with LoRA, which updates only a small subset of parameters, thereby reducing computational cost. The third experiment explored prompt tuning with both mixed and manually crafted prompts, using very small sets of training examples relative to the entire dataset, making it computationally efficient as well. Finally, the fourth experiment applied prompt engineering through zero-shot and few-shot learning, relying solely on care-fully designed instruction prompts for classification without further training.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.