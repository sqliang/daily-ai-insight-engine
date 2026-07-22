---
title: 'Lung-R1: A Knowledge Graph-Guided LLM for Pulmonary Diagnostic Reasoning'
source: https://arxiv.org/abs/2606.11675
author:
- '[[Haoyang Zeng, Yuanxi Fu, Rongzhen Li, Yuming Yang, Xiao Sun, Jingwang Huang,
  Gujie Shao, Guohui Xiang, Quan Lu, Dongfan Ye, Xuetao Chen, Jiang Zhong, Kaiwen
  Wei, Zhi Xu]]'
published: '2026-06-11'
created: '2026-06-11'
description: 'arXiv:2606.11675v1 Announce Type: new Abstract: Diagnosing pulmonary
  diseases requires integrating heterogeneous evidence amid phenotypic variability
  and cross-disease overlap. Although large language models (LLMs) have shown progress
  on pulmonary knowledge question answering (QA) and information-processing tasks,
  reliable pulmonary diagnosis requires patient-specific, relation-aware reasoning
  over electronic medical record (EMR) evidence rather than isolated knowledge recall.
  We define this gap between pulmonary knowledge and case-level diagnostic reasoning
  as the Pulmonary Knowledge-to-Diagnosis Gap. To address it, we introduce LungKG,
  the first structured pulmonary knowledge graph for diagnostic knowledge organization
  and record-grounded reasoning. LungKG contains 59,038 nodes and 164,308 edges across
  15 entity types and 112 relation types, serving as both a reusable pulmonary knowledge
  resource and the foundation for LungKG-guided model adaptation. Built on LungKG,
  we propose Lung-R1, a LungKG-guided pulmonary LLM trained through KG-constrained
  reasoning-chain construction and KG-guided reinforcement learning. In a 20-system
  evaluation, Lung-R1-14B achieves state-of-the-art performance across Choice, Pulmonary-QA,
  and EMR Diagnosis, reaching an EMR Diagnosis score of 4.3583 and surpassing the
  strongest non-Lung-R1 baseline by 0.1476 points. These results demonstrate the value
  of LungKG-guided training for EMR-based pulmonary diagnosis.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ac1bb60ccdeadde6
source_type: academic_paper
tldr: 论文提出Lung-R1模型和LungKG知识图谱，通过知识图谱引导的强化学习方法训练大语言模型，在肺部疾病诊断推理任务上达到最先进水平，EMR诊断得分4.3583。
objective_summary: 该论文针对大语言模型在肺部疾病知识问答上表现良好但缺乏基于电子病历的病例级诊断推理能力的问题，首先构建了LungKG——首个结构化肺部知识图谱，包含59,038个节点和164,308条边，覆盖15种实体类型和112种关系类型。在此基础上提出Lung-R1模型，通过知识图谱约束的推理链构建和知识图谱引导的强化学习进行训练。在包含20个系统的评估中，Lung-R1-14B在选择题、肺部知识问答和EMR诊断三项任务上均达到最先进水平，EMR诊断得分为4.3583。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Knowledge Graph
  - Reinforcement Learning
  - EMR
  - QA
  key_people: []
key_logic_flow:
- 论文定义了"肺部知识到诊断的鸿沟"，即大语言模型在肺部知识问答上表现良好，但在基于电子病历的病例级诊断推理中仍存在不足。
- 研究人员构建了LungKG，这是首个结构化的肺部知识图谱，包含59,038个节点和164,308条边，覆盖15种实体类型和112种关系类型。
- 基于LungKG，论文提出了Lung-R1模型，通过知识图谱约束的推理链构建和知识图谱引导的强化学习进行训练。
- 在包含20个系统的评估中，Lung-R1-14B在选择题、肺部知识问答和EMR诊断三项任务上均达到最先进的性能水平。
- Lung-R1-14B的EMR诊断得分为4.3583，超过最强的非Lung-R1基线0.1476分，验证了知识图谱引导训练对基于电子病历的肺部诊断的价值。
extract_result: success
object_mentions:
- object_type: model
  name: Lung-R1
  canonical_name: Lung-R1
  url: https://arxiv.org/abs/2606.11675
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 基于LungKG，论文提出了Lung-R1模型，通过知识图谱约束的推理链构建和知识图谱引导的强化学习进行训练。
  - 在20个系统的评估中，Lung-R1-14B在选择题、肺部知识问答和EMR诊断三项任务上均达到最先进水平，EMR诊断得分为4.3583。
  article_id: ac1bb60ccdeadde6
- object_type: project
  name: LungKG
  canonical_name: LungKG
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - LungKG是首个结构化的肺部知识图谱，包含59,038个节点和164,308条边，覆盖15种实体类型和112种关系类型。
  - LungKG既是可复用的肺部知识资源，也是LungKG引导的模型适配的基础，服务于诊断知识组织和记录驱动的推理。
  article_id: ac1bb60ccdeadde6
---

# Computer Science > Artificial Intelligence

# Title:Lung-R1: A Knowledge Graph-Guided LLM for Pulmonary Diagnostic Reasoning

View PDF HTML (experimental)Abstract:Diagnosing pulmonary diseases requires integrating heterogeneous evidence amid phenotypic variability and cross-disease overlap. Although large language models (LLMs) have shown progress on pulmonary knowledge question answering (QA) and information-processing tasks, reliable pulmonary diagnosis requires patient-specific, relation-aware reasoning over electronic medical record (EMR) evidence rather than isolated knowledge recall. We define this gap between pulmonary knowledge and case-level diagnostic reasoning as the Pulmonary Knowledge-to-Diagnosis Gap. To address it, we introduce LungKG, the first structured pulmonary knowledge graph for diagnostic knowledge organization and record-grounded reasoning. LungKG contains 59,038 nodes and 164,308 edges across 15 entity types and 112 relation types, serving as both a reusable pulmonary knowledge resource and the foundation for LungKG-guided model adaptation. Built on LungKG, we propose Lung-R1, a LungKG-guided pulmonary LLM trained through KG-constrained reasoning-chain construction and KG-guided reinforcement learning. In a 20-system evaluation, Lung-R1-14B achieves state-of-the-art performance across Choice, Pulmonary-QA, and EMR Diagnosis, reaching an EMR Diagnosis score of 4.3583 and surpassing the strongest non-Lung-R1 baseline by 0.1476 points. These results demonstrate the value of LungKG-guided training for EMR-based pulmonary diagnosis.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.