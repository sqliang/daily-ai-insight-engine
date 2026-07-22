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
tldr: 该论文通过对136名美国处方临床医生的调查研究，论证了自主AI处方系统必须具备校准置信度升级机制、区分认知与随机不确定性的差异化沟通、以及推理透明性这三个最低架构要求，否则临床医生不会接受其自主处方权。
objective_summary: 该论文针对美国H.R. 238法案和犹他州处方续签试点中授权的AI自主处方场景，提出了三项最低架构要求：校准的逐预测置信度阈值、区分认知不确定性（模型无知）与随机不确定性（临床模糊性）的沟通机制、以及允许责任分配的推理透明性。论文对136名美国处方临床医生的调查显示，医生拒绝在缺乏校准置信度升级机制的情况下允许自主处方，在随机不确定性下偏好竞争选项汇总而在认知不确定性下偏好弃权，且仅在推理透明性支持实质性判断时才愿意承担额外责任。论文认为满足这些要求的系统实际上更像受监督的决策支持工具而非自主智能体。
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Autonomous AI Prescribing
  - Calibrated Confidence-Based Escalation
  - Inferential Transparency
  key_people: []
key_logic_flow:
- 美国H.R. 238法案和犹他州处方续签试点已授权AI在处方中担任代理角色，从辅助决策转向自主决策。
- 当前监管指南仅要求总体模型性能指标，未要求校准的逐预测置信度阈值、区分认知不确定性与随机不确定性的沟通机制、以及推理透明性。
- 对136名美国处方临床医生的调查表明，医生拒绝在缺乏校准置信度升级机制的情况下允许AI自主处方。
- 当不确定性属于随机类型时，医生偏好AI提供竞争选项汇总；当不确定性属于认知类型时，医生偏好AI弃权处理。
- 医生仅在推理透明性支持其在已知不确定性下做出实质性判断时，才愿意承担额外的责任分配。
- 满足这些架构要求的系统本质上不再是自主智能体，而是高度受监督的决策支持工具，这压缩了传统意义上的"自主性"内涵。
extract_result: success
object_mentions:
- object_type: paper
  name: 'The Clinician''s Veto: Navigating Trust, Liability, and Uncertainty in Autonomous
    AI Prescribing'
  canonical_name: '2606.25108'
  url: https://arxiv.org/abs/2606.25108
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出自主AI处方系统必须包含校准置信度升级机制、区分认知与随机不确定性的沟通机制、以及推理透明性作为最低架构要求。
  - 论文基于对136名美国处方临床医生的调查，论证了当前监管指南在逐预测不确定性管理方面的不足并提出了架构改进方案。
  - 论文结论指出满足这些要求的系统将更接近受监督的决策支持工具，而非传统意义上的自主AI智能体。
  article_id: 1fd9dbe8ac6b2ad4
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