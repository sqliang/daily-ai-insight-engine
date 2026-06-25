---
title: 'SPARC: A Multi-Agent System for Electrical Circuit Question Answering'
source: https://arxiv.org/abs/2606.20643
author:
- '[[Mushtari Sadia, Zhenning Yang, Umme Habiba Lamia, Nishat Shawrin, Ang Chen, Amrita
  Roy Chowdhury]]'
published: '2026-06-23'
created: '2026-06-24'
description: 'arXiv:2606.20643v1 Announce Type: new Abstract: Electrical circuit diagram
  QA tasks require complex mathematical reasoning, which remains challenging for multimodal
  LLMs. We present SPARC, a multi-agent system that answers questions over circuit
  diagrams by grounding reasoning in executable physics-based simulations. SPARC uses
  LLM agents to synthesize, execute, and analyze simulation programs, improving accuracy
  and reliability by design. It achieves 83% accuracy, with up to a 58% absolute improvement
  over baselines, while enabling systematic error diagnosis.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 63bbce2cc6ed251b
source_type: academic_paper
tldr: SPARC 是一个多智能体系统，通过可执行物理仿真进行电路图问答，准确率达83%。
objective_summary: 研究人员提出了SPARC，一个利用LLM智能体合成、执行和分析物理仿真程序来回答电路图问题的多智能体系统。在电路图问答任务上达到83%准确率，相比基线最高提升58%，并支持系统性错误诊断。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - SPARC
  - Multimodal LLM
  key_people: []
key_logic_flow:
- SPARC 是一个多智能体系统，专门用于电路图问答任务，解决多模态大语言模型在复杂数学推理上的不足。
- 该系统通过将推理过程锚定在可执行的物理仿真中，利用LLM智能体合成、执行并分析仿真程序。
- SPARC 在电路图问答任务上达到 83% 的准确率，相比基线方法最高实现 58% 的绝对提升。
- 该系统通过设计实现了系统性错误诊断能力，提升了可靠性和准确性。
extract_result: success
impact_score:
  score: 3.5
  reason: SPARC 是一个面向电路图问答这一垂直领域的多智能体系统，核心贡献在于将推理过程锚定在可执行的物理仿真中。虽然83%准确率和58%的绝对提升在学术基准上表现亮眼，但其应用场景高度局限在电路图问答这一窄域，且技术路线（LLM生成仿真代码+执行验证）并非全新范式。该工作更接近一项扎实的工程化解决方案而非行业范式转移，短期对AI行业整体格局无明显冲击力。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 仿真代码生成+执行的可靠性是否具备跨领域泛化能力
hype_assessment:
  level: low
  reason: arXiv论文，语言客观，提供了具体的准确率数字和对比基线（83% accuracy, up to 58% absolute improvement），没有出现'颠覆性''革命性'等PR滥用词汇，也没有过度夸大适用范围。属于实打实的学术成果汇报。
information_entropy: medium
domain_disruption:
  technical_innovation: 提出了将LLM多智能体协同与可执行物理仿真相结合的技术方案，通过'合成→执行→分析'的闭环让模型推理结果可被物理引擎验证，从而系统性提升数学推理任务的可靠性并支持错误诊断。这一思路对STEM领域（物理、电子、力学等）的推理问题具有参考价值。
  business_model: 无
engineering_complexity: prototype
compound_value:
  score: 4.0
  reason: SPARC 的核心价值在于提出了一种通用范式：将 LLM 多智能体推理锚定在可执行的物理仿真中，从而在需要精确数学/物理推理的领域大幅超越端到端多模态大模型。作为学术论文，它尚未商业化，且目前仅限电路图问答这一窄领域，但该范式（multi-agent
    + simulation grounding）可迁移至结构力学、流体仿真、芯片验证等更广的工程场景。长期看，若该思路被集成到商业仿真软件或 AI 平台中，可能成为细分技术栈的基石；但当前阶段距离产品化和收入验证还较远，需关注后续是否有衍生创业公司或大厂采纳。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Ansys
- Cadence Design Systems
- Synopsys
- NVIDIA
competitive_casualty:
- 端到端多模态大模型（依赖纯视觉理解处理技术图表者）
- 传统规则型电路解析工具
market_opportunities:
- 教育科技领域可基于 SPARC 的仿真锚定推理方法开发电路图自动批改与智能辅导系统，切入 STEM 教育自动化市场
- 电子设计自动化（EDA）工具厂商可借鉴该多智能体架构，构建面向电路设计与验证的 AI 辅助分析产品，提升工程师工作效率
- 该仿真锚定方法论可跨领域迁移至其他 STEM 学科（如机械制图、化学结构分析），催生垂直行业的多智能体推理工具
risk_matrix:
  regulatory: 无（纯学术研究，不涉及合规敏感数据或应用场景）
  technological: 83% 的准确率在安全关键型电路应用中仍存在较高容错风险；该方法对复杂非线性电路的泛化能力尚未验证，可能被下一代原生多模态推理模型绕过或取代
  competitive: EDA 巨头（Cadence、Synopsys）可能快速整合类似能力到已有商业工具中形成生态壁垒；同时开源社区可能出现更轻量级的替代方案挤压差异化空间
  ethical: 在安全关键场景（如电力系统、医疗设备）中过度依赖自动化电路分析可能因误判导致安全事故；自动化程度提升可能减少初级电路设计工程师的培训与就业机会
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:SPARC: A Multi-Agent System for Electrical Circuit Question Answering

View PDFAbstract:Electrical circuit diagram QA tasks require complex mathematical reasoning, which remains challenging for multimodal LLMs. We present SPARC, a multi-agent system that answers questions over circuit diagrams by grounding reasoning in executable physics-based simulations. SPARC uses LLM agents to synthesize, execute, and analyze simulation programs, improving accuracy and reliability by design. It achieves 83% accuracy, with up to a 58% absolute improvement over baselines, while enabling systematic error diagnosis.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.