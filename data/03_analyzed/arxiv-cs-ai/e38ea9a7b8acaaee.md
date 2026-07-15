---
title: 'Aligning Clinical Needs and AI Capabilities: A Survey on LLMs for Medical
  Reasoning'
source: https://arxiv.org/abs/2607.07761
author:
- '[[Qi Peng, Jiatong Li, Sirui Huang, Yiyang Jiang, Kaisong Gong, Ronger Ding, Shijie
  Ye, Changmeng Zheng, Yi Cai, Xiaobo Yang, Jin Huang, Xiao-Yong Wei, Qing Li]]'
published: '2026-07-11'
created: '2026-07-11'
description: 'arXiv:2607.07761v1 Announce Type: new Abstract: Large language models
  (LLMs) have emerged as important tools in healthcare, showing growing potential
  for clinical reasoning and patient care. This survey examines recent progress in
  medical LLMs, focusing on reasoning applications and requirements. We present a
  dual-view approach that connects clinical practice with computational methods. On
  the clinical side, we establish a five-level competency scheme following Miller''s
  Pyramid, progressing from knowledge recall to dynamic case management. On the computational
  side, we link deductive, inductive, and abductive reasoning patterns to common medical
  goals and tasks. We also introduce a benchmark dataset spanning five levels of medical
  reasoning capability and report results on 18 state-of-the-art models, revealing
  that medical specialist models excel in diagnosis-centric tasks while general models
  lead in decision support and dialogue. We conclude by discussing current progress
  and open challenges, including data limitations, hallucination, and grounding issues,
  and outline directions toward safer, more reliable, and workflow-ready systems.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e38ea9a7b8acaaee
source_type: academic_paper
tldr: LLM医疗推理综述：提出Miller金字塔五级能力框架，评测18个模型，揭示专长差异。
objective_summary: 该综述论文从临床和计算双重视角审视LLM在医疗推理中的应用。临床侧基于Miller金字塔建立从知识回忆到动态病例管理的五级能力框架，计算侧将演绎、归纳和溯因推理模式与医疗任务关联。论文引入横跨五级医疗推理能力的基准数据集，对18个模型进行评测，发现医疗专家模型在诊断任务中占优，
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM
  key_people: []
key_logic_flow:
- 该论文采用双视角方法，临床侧基于Miller金字塔建立从知识回忆到动态病例管理的五级能力框架。
- 计算侧将演绎、归纳和溯因推理模式与常见医疗目标和任务相关联。
- 论文引入一个横跨五级医疗推理能力的基准数据集用于模型评测。
- 对18个最先进模型的评测结果显示，医疗专家模型在诊断类任务中表现优异。
- 通用模型在医疗决策支持和对话任务中表现优于医疗专用模型。
- 论文讨论了当前开放挑战，包括数据局限性、幻觉问题和接地问题，并指出向更安全可靠的工作流适配系统的方向。
specialized_tags:
  paper:
    paperTitle: 'Aligning Clinical Needs and AI Capabilities: A Survey on LLMs for
      Medical Reasoning'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: NLP
    methodType: LLM-based
extract_result: success
impact_score:
  score: 5.5
  reason: 该综述提出了Miller金字塔五级医疗推理能力框架并评测了18个模型，为医疗AI提供了结构化的能力评估体系。核心发现——医疗专精模型在诊断任务占优、通用模型在决策支持和对话中领先——对行业选型有指导意义。但作为综述论文，短期内难以直接改变产业格局或引发范式转移。评分5.5：有一定行业参考价值，但不足以构成强冲击。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 医疗专精模型与通用模型在不同临床任务中的能力对比数据
hype_assessment:
  level: low
  reason: 论文以学术综述的形式呈现，明确讨论了现有挑战（数据局限、幻觉、接地问题），没有使用'颠覆性'、'革命性'等PR词汇，方法论透明，属于扎实的学术贡献而非炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 提出基于Miller金字塔的五级医疗推理能力评估框架，将演绎、归纳、溯因推理模式与临床任务层级对应，并构建了横跨五级能力的基准评测数据集
  business_model: 无
engineering_complexity: conceptual
compound_value:
  score: 5.5
  reason: 作为综述论文，其长期复利价值较为有限但不可忽视：提出的Miller金字塔五级能力框架和跨18模型的基准评测数据集，有望成为医疗LLM评估的行业参考标准，具有持续的引用价值和框架影响力。核心发现——医疗专家模型在诊断任务中占优、通用模型在决策支持和对话中领先——对产业投资具有直接指导意义，能帮助资本判断不同医疗AI赛道应采用何种模型策略。但作为学术综述而非可商业化的产品/平台，本身不具备'越用越强'的复利飞轮效应，其价值取决于框架能否被产业界广泛采纳，存在不确定性。综合评判：有潜力成为细分领域评估基础设施，但需持续验证。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Google DeepMind
- Microsoft Research
- Hippocratic AI
- OpenAI
- Anthropic
competitive_casualty:
- 通用诊断LLM初创公司（缺乏医学领域深耕）
- 传统临床决策支持系统（CDSS）厂商
market_opportunities:
- 医疗科技公司可基于'通用模型强于决策支持对话、专用模型强于诊断'的发现，设计通用+专用模型协同工作的混合临床决策支持系统
- 创业团队可利用论文提出的五级Miller金字塔能力框架，开发面向医疗机构的分层式AI能力评估工具和认证服务
- 基于该论文的跨五级医疗推理基准数据集，可衍生出专门针对医疗场景的模型微调服务和评测排行榜产品
risk_matrix:
  regulatory: 医疗AI面临严格的监管审查（FDA、CE、NMPA），LLM的幻觉和接地问题在临床场景中可能触发医疗器械认证、临床验证和医疗事故责任等合规风险
  technological: 论文揭示通用模型在决策支持与对话任务中反超医疗专家模型，表明当前'领域微调优于通用'的技术假设可能被快速颠覆，架构偏好可能迅速变化
  competitive: 科技巨头（Google、Microsoft、OpenAI）与医疗IT传统厂商（Epic、Cerner）均加速布局医疗LLM，赛道拥挤且资源高度集中，初创企业面临巨大的生态挤压
  ethical: LLM幻觉在医疗场景可能导致误诊或错误治疗方案，造成患者伤害；不同人群的数据偏差可能加剧医疗资源分配不均；患者隐私与临床数据安全面临严峻挑战
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:Aligning Clinical Needs and AI Capabilities: A Survey on LLMs for Medical Reasoning

View PDF HTML (experimental)Abstract:Large language models (LLMs) have emerged as important tools in healthcare, showing growing potential for clinical reasoning and patient care. This survey examines recent progress in medical LLMs, focusing on reasoning applications and requirements. We present a dual-view approach that connects clinical practice with computational methods. On the clinical side, we establish a five-level competency scheme following Miller's Pyramid, progressing from knowledge recall to dynamic case management. On the computational side, we link deductive, inductive, and abductive reasoning patterns to common medical goals and tasks. We also introduce a benchmark dataset spanning five levels of medical reasoning capability and report results on 18 state-of-the-art models, revealing that medical specialist models excel in diagnosis-centric tasks while general models lead in decision support and dialogue. We conclude by discussing current progress and open challenges, including data limitations, hallucination, and grounding issues, and outline directions toward safer, more reliable, and workflow-ready systems.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.