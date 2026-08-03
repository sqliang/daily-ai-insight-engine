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
impact_score:
  score: 3.5
  reason: 评分依据：该论文属于医疗垂直领域的应用型智能体研究，核心贡献是把 ACOG 的 PATH 临床指南转化为可执行的四阶段端到端对话智能体工作流（问诊→动态交互→计划合成→临床监督），并用专家评分体系在五个临床维度量化评测了
    GPT-5.2 等前沿模型（最高 77.6%）。这为医疗智能体提供了一套可复制的工程编排模板与评测基准，有一定参考价值；但既无模型或算法层面的架构突破，也尚未进入人体试验与随机对照试验验证阶段，且评测本身暴露了产前检测建议的关键缺口，属于细分领域的增量贡献而非行业范式转移，短期内不改变竞争格局。综合评定
    3.5 分。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: GPT-5.2 仅 77.6% 平均得分暴露的产前检测建议可靠性缺口，以及专家评分评测体系与临床验证的严谨性
hype_assessment:
  level: low
  reason: 全文为严谨的学术表达，采用"评估"、"发现关键缺口"、"计划通过人类受试者和随机对照试验验证"等克制措辞，主动披露产前检测建议的不足，未使用"颠覆"、"革命性"等
    PR 词汇，也无商业化承诺，属于实打实的研究报道，不存在概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 工程层面的创新在于将非结构化的临床指南（ACOG PATH）落地为结构化的四阶段智能体工作流：通过结构化对话采集患者健康与社会背景，动态生成个性化护理计划并联动
    Michigan 211 社区资源，同时引入"临床医生监督"这一人机协同环节。方法论创新是构建了覆盖五个临床维度的专家评分体系，为医疗智能体质量评估提供了可量化的基准框架；本质是系统编排与评测方法的创新，而非模型架构突破。
  business_model: 潜在商业化路径是面向数字孕产健康平台的临床决策支持（CDS）服务：可嵌入电子病历系统或孕产管理 App，为医疗机构提供指南对齐的个性化护理计划生成与社区资源匹配，具备
    SaaS 订阅或按问诊计费的变现空间；但受 FDA 等临床监管、医疗责任归属与 RCT 验证周期制约，距实际商用仍有相当距离。
engineering_complexity: prototype
compound_value:
  score: 4.5
  reason: 推演路径：该研究目前处于 theoretical_claim 阶段（作者明确表示需人类受试者研究与 RCT 验证），商业化为时尚早，短期无现金流。但往中长期看，它验证了
    agentic 工作流（结构化问诊→动态交互→计划合成→临床监督）在垂直医疗场景的可落地性，这一范式若通过临床验证，可能沉淀为医疗 AI 应用的可复用模式，具有细分赛道基础设施的潜力。然而两个关键风险压制其复利上限：其一，评测显示
    GPT-5.2 得分最高，说明价值主要由基础模型层捕获，PATHFinder 本身的可替代性强；其二，产前检测建议存在关键缺口，且医疗领域强监管、长周期、高验证成本，3-5
    年内难以独立成为行业基石。综合判定为『有潜力但需持续验证』区间，故给 4.5 分。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- OpenAI
- Anthropic
- Epic
- ACOG
competitive_casualty:
- 传统非 AI 护理协调工具
- 刚性协议化 CDSS 厂商
- 小型专用医学 LLM
market_opportunities:
- 医疗垂直领域的对话式智能体正成为落地热点，创业者可基于 ACOG 等权威临床指南，构建产前护理、慢病管理等专科化的临床决策支持系统，以'指南合规'作为差异化卖点
- 将社会健康决定因素（如社区资源 211 接入）与医疗 AI 结合的'医疗+社会服务'闭环模式，是面向政府卫生部门（To-G）和医院（To-B）的可复制商业化路径
- 医疗 AI 缺乏统一的临床评测基准，围绕专家评分标准、临床试验设计与合规审计提供第三方评估与验证服务，是一个未被充分占用的配套市场
risk_matrix:
  regulatory: 产前护理涉及医疗责任与患者隐私（HIPAA），此类对话式智能体若作为临床决策支持软件使用，需面对 FDA 对医疗器械软件（SaMD）的监管路径；通用大模型（如
    GPT-5.2）直接输出临床建议的合规责任归属尚不清晰
  technological: 该研究为 arXiv 预印本且处于理论声明阶段，GPT-5.2 平均得分仅 77.6%，产前检测建议仍存在关键缺口；系统未经人体受试者研究与随机对照试验验证，存在被更专业的垂直医疗模型或通用模型快速迭代所取代的风险
  competitive: 医疗 AI 赛道巨头（Google、Microsoft、Epic 等）及通用大模型厂商可低成本复制其四阶段工作流，先发优势有限；医院自建系统与开源替代方案可能进一步挤压创业空间
  ethical: 医疗 AI 误诊风险直接威胁母婴安全；产前护理涉及种族、社会经济地位等敏感因素，训练数据偏见可能导致不公平的护理建议；患者健康数据的隐私保护与
    AI 信息误导风险均需高度警惕
  additional:
  - 临床责任划分模糊：AI 建议引发医疗事故时，医生、医院与模型厂商之间的责任界定尚不明确
  - 患者信任度与医生接受度不足可能阻碍实际临床部署，需较长的用户教育与行为改变周期
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: PATHFinder Agent
  canonical_name: PATHFinder Agent
  url: https://arxiv.org/abs/2607.24768
  positioning: 端到端对话式智能体系统，依据 ACOG PATH 指南为孕妇定制个性化产前护理计划，并整合密歇根 211 社区资源。
  technical_signal: 系统采用患者问诊、动态交互、计划合成与临床医生监督的四阶段工作流，通过结构化对话端到端生成护理计划。
  adoption_signal: 项目尚处学术研究与评测阶段，无临床实际部署记录，作者规划通过人类受试者研究和随机对照试验作进一步验证。
  ecosystem_relevance: 系统依托 ACOG PATH 临床指南与密歇根 211 社区资源网络，属于医疗大模型与社区健康服务交叉的前沿生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: PATHFinder Agent 是 LLM 智能体在临床决策支持领域的前沿探索，其评测结论（GPT-5.2 平均得分最高 77.6%）为医疗大模型能力评估提供了量化基准，且明确规划了临床试验验证路径，值得持续跟踪其技术演进与落地进展。
  risk_notes:
  - 评测显示系统在产前检测建议方面仍存在关键缺口，临床建议的可靠性尚未得到验证。
  - 项目仍处于论文研究阶段，未经人类受试者研究与随机对照试验的严格验证。
  - 医疗场景涉及患者隐私保护与临床责任归属，实际部署面临较高的监管合规门槛。
  score: 5.0
  article_ids:
  - 5ee777a2fdaeebca
  evidence_snippets:
  - PATHFinder Agent 是一个端到端的对话式智能体系统，通过结构化对话收集患者的健康与社会背景信息。
  - 该系统依据 ACOG 的 PATH 指南生成个性化产前护理计划，并整合密歇根 211 的社区资源。
  - 系统采用患者问诊、动态交互、计划合成与临床医生监督的四阶段工作流。
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