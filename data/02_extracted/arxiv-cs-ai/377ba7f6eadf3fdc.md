---
title: 'Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment
  of Financial Literacy in Serious Games'
source: https://arxiv.org/abs/2606.25358
author:
- '[[Gabriel Santos, Rita Julia, Marcelo Nascimento]]'
published: '2026-06-25'
created: '2026-06-25'
description: 'arXiv:2606.25358v1 Announce Type: new Abstract: Assessing financial
  literacy during gameplay without disrupting the learning experience remains a key
  challenge in serious games for education. We present the Agentic BKT pipeline, a
  multi-agent large language model architecture for stealth assessment of financial
  competencies from open-ended gameplay events. The pipeline processes events from
  a 2D platformer serious game aligned with the OECD/INFE financial literacy framework
  through four phases: (1) the game captures every player decision as a structured
  event log; (2) an LLM event classifier labels each action on a four-point rubric
  validated against three domain experts (Fleiss kappa = 0.624, substantial agreement);
  (3) four domain-specific agents specializing in risk mitigation, investing, spending,
  and credit management perform session-level reasoning over behavioral trajectories,
  feeding per-competency Bayesian Knowledge Tracing that estimates mastery within
  each domain; and (4) an expert judge agent synthesizes the domain-level estimates
  into an overall mastery score. Evaluated with 193 K-12 participants across 264 game
  sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated
  with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p <
  0.0001) while showing no correlation with pre-test scores, providing both convergent
  and discriminant validity. The multi-agent approach approximately triples the predictive
  validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating
  that domain decomposition and session-level reasoning play a central role in capturing
  the multidimensional nature of financial literacy from gameplay'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 377ba7f6eadf3fdc
source_type: academic_paper
tldr: 多智能体LLM架构Agentic BKT通过游戏行为隐式评估金融素养，预测效度是单LLM基线的3倍
objective_summary: 研究者提出Agentic BKT管道，基于多智能体LLM架构从严肃游戏行为中隐式评估金融能力。系统通过4阶段流程处理游戏日志：事件捕获、LLM分类、4个领域智能体推理（风险/投资/支出/信用）及专家综合。193名K-12学生实验显示掌握度估计与学习增益显著相关(r=0.276,
  p=0.
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Bayesian Knowledge Tracing
  - BKT
  - Agentic BKT
  - Multi-Agent System
  key_people: []
key_logic_flow:
- 论文提出Agentic BKT管道，一种基于多智能体LLM的架构，用于从严肃游戏行为中隐式评估金融素养，与OECD/INFE金融素养框架对齐。
- 系统包含4个阶段：游戏事件日志捕获、LLM事件分类（基于四点评分表，与三位专家一致性达Fleiss kappa=0.624）、4个领域智能体（风险缓解、投资、支出、信用管理）进行会话级推理并执行贝叶斯知识追踪、专家评审智能体综合得出总体掌握度分数。
- 评估基于193名K-12学生在264场游戏会话中的数据，掌握度估计与学习增益显著相关（r=0.276, p=0.0001），与后测成绩显著相关（r=0.333,
  p<0.0001），且与前测成绩无相关性，验证了收敛效度和判别效度。
- 多智能体方法的预测效度（r=0.276，显著）约为单LLM基线（r=0.095，不显著）的3倍，表明领域分解和会话级推理在捕捉金融素养多维特性中发挥核心作用。
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games

View PDF HTML (experimental)Abstract:Assessing financial literacy during gameplay without disrupting the learning experience remains a key challenge in serious games for education. We present the Agentic BKT pipeline, a multi-agent large language model architecture for stealth assessment of financial competencies from open-ended gameplay events. The pipeline processes events from a 2D platformer serious game aligned with the OECD/INFE financial literacy framework through four phases: (1) the game captures every player decision as a structured event log; (2) an LLM event classifier labels each action on a four-point rubric validated against three domain experts (Fleiss kappa = 0.624, substantial agreement); (3) four domain-specific agents specializing in risk mitigation, investing, spending, and credit management perform session-level reasoning over behavioral trajectories, feeding per-competency Bayesian Knowledge Tracing that estimates mastery within each domain; and (4) an expert judge agent synthesizes the domain-level estimates into an overall mastery score. Evaluated with 193 K-12 participants across 264 game sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p < 0.0001) while showing no correlation with pre-test scores, providing both convergent and discriminant validity. The multi-agent approach approximately triples the predictive validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating that domain decomposition and session-level reasoning play a central role in capturing the multidimensional nature of financial literacy from gameplay

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.