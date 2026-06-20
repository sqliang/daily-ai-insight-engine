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
tldr: Lung-R1 通过肺部知识图谱 LungKG 引导 LLM 进行肺部疾病诊断推理，在 EMR 诊断任务上达到 SOTA。
objective_summary: 研究人员构建了首个结构化肺部知识图谱 LungKG（5.9 万节点、16.4 万边），并基于此训练了 Lung-R1 模型。该模型通过
  KG 约束的推理链构建和强化学习训练，在 20 个系统的评估中，EMR 诊断得分达 4.3583，超越非 Lung-R1 基线 0.1476 分。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Knowledge Graph
  - LungKG
  - Lung-R1
  - Reinforcement Learning
  - KG-constrained reasoning
  key_people: []
key_logic_flow:
- 论文定义了肺部知识与病例级诊断推理之间的差距为「肺知识到诊断鸿沟」（Pulmonary Knowledge-to-Diagnosis Gap）。
- 研究团队构建了 LungKG，这是首个结构化肺部知识图谱，包含 59,038 个节点和 164,308 条边，覆盖 15 种实体类型和 112 种关系类型。
- 基于 LungKG，团队提出了 Lung-R1，一种通过 KG 约束的推理链构建和 KG 引导的强化学习训练的肺部 LLM 诊断模型。
- 在包含 20 个系统的评估中，Lung-R1-14B 在选择题、肺部问答和 EMR 诊断三项任务上均达到最先进水平。
- Lung-R1-14B 的 EMR 诊断得分为 4.3583，超过最强非 Lung-R1 基线 0.1476 分。
- 实验结果证明了 LungKG 引导的训练方法对基于 EMR 的肺部诊断的有效性。
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