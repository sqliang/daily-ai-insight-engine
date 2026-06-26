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
impact_score:
  score: 5.5
  reason: 该论文针对AI自主开药这一正在立法推进中的具体场景，提出了三项最小架构要求（校准置信度阈值、不确定性类型差异化沟通、决策透明度），并附136名医生的实证调查支撑。虽然不是GPT级别的范式转移，但恰逢美国H.R.
    238法案和犹他州试点推进之时，可能直接影响监管框架和医疗AI产品的架构设计，具有中等偏上的政策影响力。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: 置信度校准和不确定性类型区分的工程实现难度，以及责任分配模型的落地可行性
hype_assessment:
  level: low
  reason: 论文使用学术论文的标准克制语气，没有出现'颠覆'、'革命'等PR用词。所有主张均有136名医生的调查数据支撑，结论谨慎——明确指出满足要求的系统'更像是高度受监督的决策支持工具而非自主代理'，属于实打实的学术贡献。
information_entropy: high
domain_disruption:
  technical_innovation: 提出了AI自主开药系统的三项最小架构设计约束：基于逐预测校准置信度的行动门控升级机制、认知不确定性（模型无知）与偶然不确定性（临床固有模糊性）的差异化输出策略、以及决策时刻的可追溯透明度设计，为医疗AI从辅助决策向自主代理转型提供了具体的工程规范蓝图。
  business_model: 核心冲击在于重新分配法律责任——论文明确主张将开药决策的责任从临床医生转移到'控制系统设计和部署的机构方'（即医院或AI供应商），可能催生以责任转移为核心卖点的医疗AI保险和合规服务新模式。
engineering_complexity: conceptual
compound_value:
  score: 4.0
  reason: 该论文从监管架构角度定义AI自主开药的最小可行性要求（校准置信度、不确定性类型区分、决策透明可追溯），并非技术突破或商业模式创新，因此直接商业价值有限。但其价值在于：1）为AI医疗监管提供了可操作的技术框架，可能影响FDA等机构未来指南，进而塑造行业合规壁垒；2）验证了AI自主处方市场正在形成（H.R.238法案+犹他州试点），但约束性框架意味着这一赛道的商业路径需要重资产投入于合规与安全基建，而非纯粹追求自主化程度。长期看，这类监管框架研究有复利效应——合规要求一旦写入法规，会成为所有参与者必须跨越的门槛，但作为一篇学术论文而非法规本身，影响力传递链条较长，变数较大。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Epic Systems
- Oracle Health
- 大型医疗IT基础设施提供商
competitive_casualty:
- 小型AI处方初创公司
- 纯自主处方平台（弱监管模式）
market_opportunities:
- 医疗AI企业可基于论文提出的三项最小架构要求（校准置信度阈值、不确定性类型区分、决策追溯透明度）开发新一代自主处方系统，满足临床医生的信任条件并获得监管先发优势
- 监管科技创业机会：为医疗机构和AI处方系统开发商提供合规审计工具，自动化验证系统是否满足置信度升级机制和透明度要求，应对即将到来的更严格监管
- 医疗AI责任险产品创新方向：保险公司可基于论文中不同透明度级别对应不同责任承担的框架，设计分层责任保险方案，覆盖从辅助决策到高度监督自主处方的各类场景
risk_matrix:
  regulatory: 美国H.R. 238法案和犹他州试点已授权AI以自主代理身份开药，但现有监管指南仅要求聚合模型性能指标，缺乏论文指出的三项关键架构要求，存在重大监管空白。论文建议监管机构利用调查结果约束AI自主程度，未来可能出台更严格的合规标准，未提前布局的企业将面临合规风险
  technological: 若处方系统未实现逐预测置信度校准和认知/偶然不确定性区分，可能在高风险场景中给出错误推荐；医生对两种不确定性类型偏好不同的输出模式（竞争选项摘要
    vs 弃权），增加了系统设计的工程复杂度
  competitive: 传统医疗服务机构与科技巨头均在布局AI处方赛道，率先满足论文所述医生信任阈值（置信度升级机制+透明度）的企业将建立合规壁垒，形成差异化竞争优势；未能达标的系统可能被医生集体拒绝采用
  ethical: AI自主开药直接涉及患者用药安全和生命健康；医生仅在透明度满足时才愿承担额外责任，可能导致责任归属真空；系统若未妥善处理数据偏见可能造成不同人群间的诊疗差异
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
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