---
title: 'AICoFe: Implementation and Deployment of an AI-Based Collaborative Feedback
  System for Higher Education'
source: https://arxiv.org/abs/2605.04740
author:
- '[[Alvaro Becerra, Alejandra Palma, Ruth Cobos]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04740v1 Announce Type: cross Abstract: Effective peer feedback
  is essential for developing critical reflection in higher education, yet its impact
  is often limited by the inconsistent quality of student-generated comments. This
  paper presents the implementation and deployment of AICoFe (AI-based Collaborative
  Feedback), a system designed to bridge this gap through a human-centered AI approach.
  We describe a modular architecture that orchestrates a multi-LLM pipeline, utilizing
  GPT-4.1-mini, Gemini 2.5 Flash, and Llama 3.1, to synthesize quantitative rubric
  data and qualitative observations into coherent, actionable feedback. Key to the
  system is a "teacher-in-the-loop" mediation workflow, where educators use specialized
  Learning Analytics dashboards to curate and refine AI-generated drafts before delivery.
  Furthermore, we detail the underlying data infrastructure, which employs a hybrid
  SQL and MongoDB strategy to ensure traceability and manage semi-structured feedback
  versions.'
tags:
- clippings
id: 9ec8f37ddbdbfa2f
source_type: academic_paper
tldr: 论文提出并部署了AICoFe系统，通过多LLM流水线和教师介入工作流提升高等教育同伴反馈质量。
objective_summary: 研究人员提出AICoFe系统，采用GPT-4.1-mini、Gemini 2.5 Flash和Llama 3.1构成的多LLM流水线，将定量评分与定性观察综合为反馈草稿，经教师通过分析仪表盘审核后交付，数据层采用SQL与MongoDB混合架构。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Google
  - Meta
  technologies:
  - GPT-4.1-mini
  - Gemini 2.5 Flash
  - Llama 3.1
  - multi-LLM pipeline
  - Learning Analytics dashboard
  - teacher-in-the-loop
  key_people: []
key_logic_flow:
- 论文提出AICoFe系统，采用人类中心AI方法解决高等教育中同伴反馈质量不一致的问题。
- 系统通过编排多LLM流水线（GPT-4.1-mini、Gemini 2.5 Flash、Llama 3.1），将定量评分数据和定性观察综合为连贯可操作的反馈。
- 系统设计了'教师介入'（teacher-in-the-loop）工作流，教师通过专业学习分析仪表盘筛选和优化AI生成的反馈草稿。
- 数据基础设施采用混合SQL和MongoDB策略，确保可追溯性并管理半结构化的反馈版本。
- 该系统已在真实高等教育环境中完成实施和部署。
---

# Computer Science > Human-Computer Interaction

# Title:AICoFe: Implementation and Deployment of an AI-Based Collaborative Feedback System for Higher Education

View PDF HTML (experimental)Abstract:Effective peer feedback is essential for developing critical reflection in higher education, yet its impact is often limited by the inconsistent quality of student-generated comments. This paper presents the implementation and deployment of AICoFe (AI-based Collaborative Feedback), a system designed to bridge this gap through a human-centered AI approach. We describe a modular architecture that orchestrates a multi-LLM pipeline, utilizing GPT-4.1-mini, Gemini 2.5 Flash, and Llama 3.1, to synthesize quantitative rubric data and qualitative observations into coherent, actionable feedback. Key to the system is a "teacher-in-the-loop" mediation workflow, where educators use specialized Learning Analytics dashboards to curate and refine AI-generated drafts before delivery. Furthermore, we detail the underlying data infrastructure, which employs a hybrid SQL and MongoDB strategy to ensure traceability and manage semi-structured feedback versions.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.