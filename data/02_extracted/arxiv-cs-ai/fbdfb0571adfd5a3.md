---
title: 'VBFDD-Agent for Electric Vehicle Battery Fault Detection and Diagnosis: Descriptive
  Text Modeling of Battery Digital Signals'
source: https://arxiv.org/abs/2605.20742
author:
- '[[Joey Chan, Zhen Chen, Ershun Pan]]'
published: '2026-05-22'
created: '2026-05-22'
description: 'arXiv:2605.20742v1 Announce Type: new Abstract: With the rapid proliferation
  of electric vehicles, the safety and reliability of lithium-ion batteries have become
  critical concerns. Effective anomaly detection is essential for ensuring safe battery
  operation. However, as battery systems and operating scenarios become increasingly
  complex, battery fault diagnosis and maintenance require stronger cross-domain adaptability
  and human-AI collaboration. Traditional fault detection and diagnosis methods are
  usually designed for specific scenarios and predefined workflows, making them less
  effective in complex real-world applications. To address the scarcity of open-source
  battery fault report corpora and the lack of unified maintenance knowledge representation,
  this study proposes a descriptive text modeling approach for battery signal reports.
  Monitoring signals, statistical features, anomaly records, and state assessment
  results are transformed into structured and readable natural language descriptions,
  forming a language corpus for battery health diagnosis and maintenance. Based on
  this corpus, we propose VBFDD-Agent, a vehicle battery fault detection and diagnosis
  agent for automotive-grade battery systems. VBFDD-Agent integrates descriptive battery-state
  texts, historical case retrieval, local maintenance manuals, and large language
  model reasoning to generate structured diagnostic results and maintenance recommendations.
  Experiments show that the proposed framework can accurately perform anomaly monitoring
  based on descriptive textual representations and provide flexible, efficient, and
  actionable maintenance suggestions. Expert evaluation further confirms the practical
  value of the generated recommendations. Overall, VBFDD-Agent extends traditional
  battery diagnosis from label prediction to interpretable and maintenance-oriented
  decision support.'
tags:
- clippings
extraction_status: success
id: fbdfb0571adfd5a3
source_type: academic_paper
tldr: 提出VBFDD-Agent，将电池信号转化为自然语言描述并结合LLM推理，实现电动车电池故障检测与可解释维修决策支持
objective_summary: 一篇arXiv论文提出VBFDD-Agent框架，将电动汽车锂离子电池的监测信号、统计特征和异常记录转化为结构化自然语言描述，形成诊断语料库，再结合历史案例检索、维修手册与大语言模型推理，生成结构化诊断结果和维修建议。实验与专家评估验证了其准确性和实用价值。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - VBFDD-Agent
  - LLM
  - Descriptive Text Modeling
  - Lithium-ion Battery
  - Battery Digital Signals
  key_people: []
key_logic_flow:
- 电动汽车锂离子电池系统日趋复杂，传统故障检测方法针对特定场景设计，缺乏跨领域适应性和人机协作能力，且缺少开源的电池故障报告语料库和统一的维修知识表示
- 提出描述性文本建模方法，将电池监测信号、统计特征、异常记录和状态评估结果转化为结构化可读的自然语言描述，构建电池健康诊断与维修语料库
- 基于该语料库构建VBFDD-Agent，整合描述性电池状态文本、历史案例检索、本地维修手册和大语言模型推理四个模块
- 实验表明VBFDD-Agent能准确进行基于描述性文本表示的异常监测，并提供灵活、高效、可操作的维修建议
- 专家评估证实了生成维修建议的实用价值，该方法将传统电池诊断从标签预测扩展到可解释的、面向维修的决策支持
pipeline_stage: fact_extracted
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:VBFDD-Agent for Electric Vehicle Battery Fault Detection and Diagnosis: Descriptive Text Modeling of Battery Digital Signals

View PDF HTML (experimental)Abstract:With the rapid proliferation of electric vehicles, the safety and reliability of lithium-ion batteries have become critical concerns. Effective anomaly detection is essential for ensuring safe battery operation. However, as battery systems and operating scenarios become increasingly complex, battery fault diagnosis and maintenance require stronger cross-domain adaptability and human-AI collaboration. Traditional fault detection and diagnosis methods are usually designed for specific scenarios and predefined workflows, making them less effective in complex real-world applications.

To address the scarcity of open-source battery fault report corpora and the lack of unified maintenance knowledge representation, this study proposes a descriptive text modeling approach for battery signal reports. Monitoring signals, statistical features, anomaly records, and state assessment results are transformed into structured and readable natural language descriptions, forming a language corpus for battery health diagnosis and maintenance.

Based on this corpus, we propose VBFDD-Agent, a vehicle battery fault detection and diagnosis agent for automotive-grade battery systems. VBFDD-Agent integrates descriptive battery-state texts, historical case retrieval, local maintenance manuals, and large language model reasoning to generate structured diagnostic results and maintenance recommendations. Experiments show that the proposed framework can accurately perform anomaly monitoring based on descriptive textual representations and provide flexible, efficient, and actionable maintenance suggestions. Expert evaluation further confirms the practical value of the generated recommendations. Overall, VBFDD-Agent extends traditional battery diagnosis from label prediction to interpretable and maintenance-oriented decision support.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.