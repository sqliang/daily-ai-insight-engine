---
title: PATHFinder Agent for Tailored Prenatal Care
source: https://arxiv.org/abs/2607.24768
author:
- '[[Vaibhav Balloli, Carissa Samuel, Samia Abdelnabi, Alex Peahl, Elizabeth Bondi-Kelly]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 'arXiv:2607.24768v1 Announce Type: new Abstract: Prenatal care is an
  important preventive service designed to improve outcomes for pregnant individuals.
  The American College of Obstetricians and Gynecologists (ACOG) recently introduced
  guidelines advocating tailored prenatal care, called PATH (Plan for Tailored Healthcare).
  We present PATHFinder Agent(Planner for Appropriate Tailored Healthcare), an end-to-end
  conversational agentic system that gathers patient health and social context through
  structured dialogue, curates individualized prenatal care plans aligned with PATH
  guidelines, and surfaces community resources from Michigan 211. The system features
  a four-stage workflow spanning patient intake, dynamic interaction, plan synthesis,
  and clinician oversight. We evaluate frontier large language models (LLMs) on expert-curated
  rubrics across five clinical dimensions, finding that GPT-5.2 achieves the highest
  average score (77.6\%) while identifying key gaps in antenatal testing recommendations.
  We discuss future validation through human participant studies and randomized controlled
  trials.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5ee777a2fdaeebca
source_type: academic_paper
tldr: PATHFinder Agent 是一个面向定制化产前护理的端到端对话式智能体系统，依据 ACOG 的 PATH 指南生成个性化护理计划并整合密歇根 211
  社区资源。评测显示 GPT-5.2 得分最高（77.6%），但产前检测建议仍有关键缺口，未来需临床试验验证。
objective_summary: 美国妇产科医师学会（ACOG）推出了倡导定制化产前护理的 PATH（Plan for Tailored Healthcare）指南。研究者据此构建了
  PATHFinder Agent 端到端对话式智能体系统，通过结构化对话收集孕妇的健康与社会背景信息，生成符合 PATH 指南的个性化产前护理计划，并接入密歇根
  211 的社区资源。系统采用患者问诊、动态交互、计划合成与临床医生监督四阶段工作流。研究使用专家制定的评分标准在五个临床维度上评测前沿大语言模型，GPT-5.2
  平均得分最高（77.6%），同时暴露出产前检测建议中的关键缺口；作者计划通过人类受试者研究和随机对照试验作进一步验证。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - American College of Obstetricians and Gynecologists (ACOG)
  - Michigan 211
  technologies:
  - LLM
  - GPT-5.2
  - conversational agent
  key_people: []
key_logic_flow:
- ACOG 近期发布了倡导定制化产前护理的 PATH（Plan for Tailored Healthcare）指南。
- PATHFinder Agent 是一个端到端对话式智能体系统，通过结构化对话收集患者的健康与社会背景信息。
- 系统依据 PATH 指南生成个性化产前护理计划，并整合密歇根 211 的社区资源。
- 系统采用患者问诊、动态交互、计划合成与临床医生监督四阶段工作流。
- 研究在五个临床维度上评测前沿大语言模型，GPT-5.2 平均得分最高（77.6%），同时识别出产前检测建议方面的关键缺口。
- 作者计划通过人类受试者研究和随机对照试验对系统进行进一步验证。
object_mentions:
- object_type: project
  name: PATHFinder Agent
  canonical_name: PATHFinder Agent
  url: https://arxiv.org/abs/2607.24768
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PATHFinder Agent 是一个端到端的对话式智能体系统，通过结构化对话收集患者的健康与社会背景信息。
  - 该系统依据 ACOG 的 PATH 指南生成个性化产前护理计划，并整合密歇根 211 的社区资源。
  - 系统采用患者问诊、动态交互、计划合成与临床医生监督的四阶段工作流。
  article_id: 5ee777a2fdaeebca
- object_type: model
  name: GPT-5.2
  canonical_name: GPT-5.2
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 研究在五个临床维度上评测前沿大语言模型，GPT-5.2 取得了最高平均分 77.6%。
  - 评测同时识别出当前模型在产前检测建议方面的关键缺口，说明其临床建议仍有待完善。
  article_id: 5ee777a2fdaeebca
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:PATHFinder Agent for Tailored Prenatal Care

View PDF HTML (experimental)Abstract:Prenatal care is an important preventive service designed to improve outcomes for pregnant individuals. The American College of Obstetricians and Gynecologists (ACOG) recently introduced guidelines advocating tailored prenatal care, called PATH (Plan for Tailored Healthcare). We present PATHFinder Agent(Planner for Appropriate Tailored Healthcare), an end-to-end conversational agentic system that gathers patient health and social context through structured dialogue, curates individualized prenatal care plans aligned with PATH guidelines, and surfaces community resources from Michigan 211. The system features a four-stage workflow spanning patient intake, dynamic interaction, plan synthesis, and clinician oversight. We evaluate frontier large language models (LLMs) on expert-curated rubrics across five clinical dimensions, finding that GPT-5.2 achieves the highest average score (77.6\%) while identifying key gaps in antenatal testing recommendations. We discuss future validation through human participant studies and randomized controlled trials.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.