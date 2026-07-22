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
tldr: 一篇 arXiv 论文提出 Agentic BKT 管道，这是一个多智能体 LLM 架构，用于在严肃游戏中通过分析玩家行为事件来无缝评估金融素养。实验证明该方法与学习增益显著相关，预测效度约为单
  LLM 基线的三倍。
objective_summary: 该论文在 arXiv 上发表，提出一种名为 Agentic BKT 的多智能体 LLM 架构，通过四阶段流程（游戏事件日志采集、LLM
  事件分类、四个领域专精智能体进行会话级贝叶斯知识追踪、专家评判智能体综合评分）对严肃游戏中的玩家金融能力进行隐形评估。基于 193 名 K-12 学生在 264
  场游戏会话中的评估显示，该方法与学习增益（r=0.276, p=0.0001）和后测成绩（r=0.333, p<0.0001）显著相关，且与前测成绩无相关，验证了聚合效度和区分效度。相比单
  LLM 基线（r=0.095，不显著），该多智能体架构的预测效度约提升三倍。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM
  - Bayesian Knowledge Tracing
  - Multi-Agent Architecture
  - Agentic BKT
  key_people: []
key_logic_flow:
- 研究团队提出 Agentic BKT 管道，一种多智能体 LLM 架构，用于在严肃游戏中对金融素养进行隐形评估，而不干扰玩家的学习体验。
- 该管道包含四个阶段：游戏采集每位玩家的结构化事件日志，LLM 事件分类器按四点评分量表标注每个动作，四个领域专精智能体分别对风险管理、投资、支出和信用管理进行会话级推理与贝叶斯知识追踪，最后专家评判智能体综合得出总体掌握度评分。
- 评估数据集来自 193 名 K-12 学生在 264 场游戏会话中产生的开放结局游戏事件，游戏内容基于 OECD/INFE 金融素养框架设计。
- 该方法与学习增益显著相关（r=0.276, p=0.0001）并与后测成绩显著相关（r=0.333, p<0.0001），验证了聚合效度。
- 该方法与前测成绩无显著相关，验证了区分效度，表明其测量的是游戏中学到的知识而非先验知识。
- 相比单 LLM 基线（r=0.095，不显著），多智能体架构的预测效度约提升三倍，证明领域分解和会话级推理对捕捉金融素养多维性的关键作用。
extract_result: success
object_mentions:
- object_type: paper
  name: 'Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment
    of Financial Literacy in Serious Games'
  canonical_name: Agentic Knowledge Tracing
  url: https://arxiv.org/abs/2606.25358
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出 Agentic BKT 管道，一种多智能体 LLM 架构，用于在严肃游戏中对金融素养进行隐形评估。
  - 实验基于 193 名 K-12 学生在 264 场游戏会话中评估，结果显示与学习增益显著相关（r=0.276, p=0.0001）。
  - 多智能体方法的预测效度约为单 LLM 基线（r=0.095，不显著）的三倍。
  article_id: 377ba7f6eadf3fdc
- object_type: project
  name: Agentic BKT Pipeline
  canonical_name: Agentic BKT Pipeline
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Agentic BKT 管道是一个多智能体 LLM 架构，包含四阶段流程用于从开放结局游戏事件中评估金融能力。
  - 该管道包含 LLM 事件分类器、四个领域专精智能体和专家评判智能体，各司其职完成推理与评估。
  - 该架构与 OECD/INFE 金融素养框架对齐，基于 2D 平台跳跃严肃游戏的事件日志运行。
  article_id: 377ba7f6eadf3fdc
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