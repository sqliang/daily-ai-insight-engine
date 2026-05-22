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
tldr: 研究提出VBFDD-Agent，将电池数字信号转为描述性文本，结合LLM推理实现故障检测与诊断。
objective_summary: 该研究提出VBFDD-Agent框架，将电池监测信号、统计特征等转换为结构化自然语言描述，结合历史案例检索、维修手册和LLM推理，生成诊断结果与维护建议。实验表明该框架能准确进行异常监测，专家评估确认了生成建议的实用价值。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - VBFDD-Agent
  - LLM
  - lithium-ion battery
  key_people: []
key_logic_flow:
- 电动汽车锂离子电池系统日益复杂，传统故障诊断方法在跨域适应性和人机协作方面存在局限。
- 研究提出描述性文本建模方法，将电池监测信号、统计特征、异常记录和状态评估结果转换为结构化自然语言描述，形成电池健康诊断语料库。
- 基于该语料库，研究提出VBFDD-Agent框架，整合电池状态文本、历史案例检索、本地维修手册和LLM推理能力。
- VBFDD-Agent能生成结构化的诊断结果和可操作的维护建议。
- 实验证明该框架能基于描述性文本表示准确进行异常监测，并提供灵活高效的维护建议。
- 专家评估确认了生成建议的实用价值，该框架将传统电池诊断从标签预测扩展到可解释的、面向维护的决策支持。
pipeline_stage: fact_extracted
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