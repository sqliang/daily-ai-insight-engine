---
title: 'When Engineering Outruns Intelligence: Rethinking Instruction-Guided Navigation'
source: https://arxiv.org/abs/2507.20021
author:
- '[[Matin Aghaei, Lingfeng Zhang, Mohammad Ali Alomrani, Mahdi Biparva, Yingxue Zhang]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2507.20021v3 Announce Type: replace-cross Abstract: Recent ObjectNav
  systems credit large language models (LLMs) for sizable zero-shot gains, yet it
  remains unclear how much comes from language versus geometry. We revisit this question
  by re-evaluating an instruction-guided pipeline, InstructNav, under a detector-controlled
  setting and introducing two training-free variants that only alter the action value
  map: a geometry-only Frontier Proximity Explorer (FPE) and a lightweight Semantic-Heuristic
  Frontier (SHF) that polls the LLM with simple frontier votes. Across HM3D and MP3D,
  FPE matches or exceeds the detector-controlled instruction follower while using
  no API calls and running faster; SHF attains comparable accuracy with a smaller,
  localized language prior. These results suggest that carefully engineered frontier
  geometry accounts for much of the reported progress, and that language is most reliable
  as a light heuristic rather than an end-to-end planner. Code available at: https://github.com/matinaghaei/instructnav-scrutinized'
tags:
- clippings
id: fb3dbbd1b46e3fbf
source_type: academic_paper
tldr: 研究发现精心设计的几何前沿策略在无需大语言模型情况下即可匹配或超越指令引导导航方法
objective_summary: 研究者重新评估了InstructNav导航管线，提出两种无需训练的变体FPE（纯几何）和SHF（轻量语义启发），在HM3D和MP3D数据集上，FPE以零API调用成本且运行更快的条件下达到或超过原方法性能。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - ObjectNav
  - InstructNav
  - FPE
  - SHF
  - HM3D
  - MP3D
  key_people: []
key_logic_flow:
- 研究者对InstructNav等依赖大语言模型的ObjectNav系统进行重新评估，质疑其性能提升中有多少真正来自语言能力、多少来自几何先验。
- 提出了两种无需训练的变体：纯几何驱动的Frontier Proximity Explorer (FPE) 和轻量语义启发式Semantic-Heuristic
  Frontier (SHF)。
- 在HM3D和MP3D数据集上，FPE在无需任何API调用且运行速度更快的情况下，匹配或超越了原InstructNav的检测器控制版本。
- SHF通过仅对前沿点进行简单投票的方式调用LLM，以更小且局部的语言先验达到了与完整LLM方法相当的精度。
- 实验结果表明，精心设计的前沿几何贡献了该领域大部分已报道的性能提升，语言模型更适合作为轻量启发式组件而非端到端规划器。
---

# Computer Science > Robotics

# Title:When Engineering Outruns Intelligence: Rethinking Instruction-Guided Navigation

View PDFAbstract:Recent ObjectNav systems credit large language models (LLMs) for sizable zero-shot gains, yet it remains unclear how much comes from language versus geometry. We revisit this question by re-evaluating an instruction-guided pipeline, InstructNav, under a detector-controlled setting and introducing two training-free variants that only alter the action value map: a geometry-only Frontier Proximity Explorer (FPE) and a lightweight Semantic-Heuristic Frontier (SHF) that polls the LLM with simple frontier votes. Across HM3D and MP3D, FPE matches or exceeds the detector-controlled instruction follower while using no API calls and running faster; SHF attains comparable accuracy with a smaller, localized language prior. These results suggest that carefully engineered frontier geometry accounts for much of the reported progress, and that language is most reliable as a light heuristic rather than an end-to-end planner. Code available at: this https URL

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.