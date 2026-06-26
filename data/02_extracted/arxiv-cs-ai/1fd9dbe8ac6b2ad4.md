---
title: 'The Clinician''s Veto: Navigating Trust, Liability, and Uncertainty in Autonomous
  AI Prescribing'
source: https://arxiv.org/abs/2606.25108
author:
- '[[Eileanor LaRocco, Sarah Tan, Adarsh Subbaswamy, Anne Andrews, Andrew Taylor,
  Cree Gaskin, Chirag Agarwal]]'
published: '2026-06-25'
created: '2026-06-25'
description: 'arXiv:2606.25108v1 Announce Type: new Abstract: Autonomous AI systems
  are transitioning from advisory to autonomous roles for medication prescriptions.
  Recent United States bill H.R. 238 and Utah''s prescription-renewal pilot both authorize
  AI to prescribe medications in an agentic capacity. While some regulatory guidelines
  suggest aggregate model performance metrics for clearance, they do not require i)
  calibrated per-prediction confidence for action-gated thresholds, ii) differentiated
  communication of uncertainty arising from model ignorance (epistemic) versus genuine
  clinical ambiguity (aleatoric), and iii) inferential transparency at the moment
  of decision that allows for liability allocation. Here, we present a regulatory
  and technical argument (tested with a survey of 136 U.S. prescribing clinicians)
  positioning these as minimum architectural requirements for safe autonomous prescribing.
  Our results suggest prescribing clinicians i) would not permit autonomous prescribing
  without a calibrated confidence-based escalation mechanism, ii) preferred a competing-options
  summary when uncertainty was aleatoric but shifted to abstention when uncertainty
  was epistemic, and iii) were only willing to accept additional liability when inferential
  transparency enabled a substantive judgment under acknowledged uncertainty. These
  findings indicate our recommended architectural features would encourage higher
  rates of clinician adoption, largely through collapsing much of what "autonomy"
  conventionally means. A system meeting these requirements would function less as
  an autonomous agent and more as a heavily supervised decision-support tool. As legislation
  and state pilots proceed, our technical argument backed by clinician perspectives
  provides opportunities for regulation to constrain the degree of autonomy ethically
  granted to AI in prescribing while aligning liability with the institutional actors
  who control system design and deployment.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 1fd9dbe8ac6b2ad4
source_type: academic_paper
tldr: 研究论证AI自主开药需校准置信度、区分不确定性类型、决策透明三大架构要求，136名医生调查支持。
objective_summary: 论文通过136名美国临床医生调查，提出AI自主开药系统需三项最小架构要求：校准的逐预测置信度阈值、认知不确定性与临床模糊性的差异化沟通、决策时刻的追溯透明度。医生要求置信度驱动的升级机制，仅在透明度满足时接受额外责任。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - Autonomous AI Prescribing
  - Confidence-based Escalation
  - Inferential Transparency
  key_people: []
key_logic_flow:
- 美国H.R. 238法案和犹他州处方续签试点已授权AI以自主代理身份开药，但现有监管指南仅要求聚合模型性能指标，缺少三项关键架构要求。
- 对136名美国临床医生的调查显示，医生不会在没有校准置信度升级机制的情况下允许自主开药系统。
- 当不确定性属于偶然型（临床固有模糊性）时，医生偏好竞争选项摘要输出模式；当属于认知型（模型无知）时，医生偏好弃权输出。
- 医生仅在决策透明度允许其在已知不确定性下做出实质判断时，才愿意接受额外责任。
- 满足这些要求的系统将更像高度受监督的决策支持工具，而非真正的自主代理。
- 研究建议监管机构利用这些发现约束AI在开药中的自主程度，并将责任分配给控制系统设计和部署的机构方。
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:The Clinician's Veto: Navigating Trust, Liability, and Uncertainty in Autonomous AI Prescribing

View PDF HTML (experimental)Abstract:Autonomous AI systems are transitioning from advisory to autonomous roles for medication prescriptions. Recent United States bill H.R. 238 and Utah's prescription-renewal pilot both authorize AI to prescribe medications in an agentic capacity. While some regulatory guidelines suggest aggregate model performance metrics for clearance, they do not require i) calibrated per-prediction confidence for action-gated thresholds, ii) differentiated communication of uncertainty arising from model ignorance (epistemic) versus genuine clinical ambiguity (aleatoric), and iii) inferential transparency at the moment of decision that allows for liability allocation. Here, we present a regulatory and technical argument (tested with a survey of 136 U.S. prescribing clinicians) positioning these as minimum architectural requirements for safe autonomous prescribing. Our results suggest prescribing clinicians i) would not permit autonomous prescribing without a calibrated confidence-based escalation mechanism, ii) preferred a competing-options summary when uncertainty was aleatoric but shifted to abstention when uncertainty was epistemic, and iii) were only willing to accept additional liability when inferential transparency enabled a substantive judgment under acknowledged uncertainty. These findings indicate our recommended architectural features would encourage higher rates of clinician adoption, largely through collapsing much of what "autonomy" conventionally means. A system meeting these requirements would function less as an autonomous agent and more as a heavily supervised decision-support tool. As legislation and state pilots proceed, our technical argument backed by clinician perspectives provides opportunities for regulation to constrain the degree of autonomy ethically granted to AI in prescribing while aligning liability with the institutional actors who control system design and deployment.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.