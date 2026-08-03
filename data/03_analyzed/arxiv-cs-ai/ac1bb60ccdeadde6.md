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
impact_score:
  score: 3.5
  reason: 该论文属于垂直领域（肺部诊断）的学术贡献，构建了首个结构化肺部知识图谱 LungKG 并集成 KG 引导的强化学习训练。EMR 诊断得分提升 0.1476（约
    3.4%），属于增量改进而非范式突破。KG 引导 LLM 推理的方法在学术上有价值，但对整个 AI 行业的短期冲击有限，主要影响医学 NLP 子领域。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 知识图谱引导的医学 LLM 推理方法能否推广到其他疾病领域，以及 3.4% 的增量提升是否具有临床实际意义
hype_assessment:
  level: low
  reason: 论文叙述克制，没有使用颠覆性、革命性等 PR 包装词汇。明确定义了问题范畴（Pulmonary Knowledge-to-Diagnosis Gap），清晰报告了数据集规模（5.9
    万节点、16.4 万边）和具体指标（4.3583 分，超越基线 0.1476），增量幅度较小反而增加了可信度。
information_entropy: high
domain_disruption:
  technical_innovation: 首次构建了结构化肺部知识图谱 LungKG（59,038 节点、164,308 边、15 种实体类型、112 种关系类型），并将其与
    KG 约束的推理链构建和 KG 引导的强化学习相结合，为 EMR 数据驱动的医学诊断推理提供了一种可复用的范式。
  business_model: 无直接影响。尚处于学术验证阶段，若后续产品化可能演化为临床辅助诊断 SaaS 或嵌入 HIS/EMR 系统，但距商业化路径较远。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: Lung-R1 验证了知识图谱引导 LLM 推理在医学诊断场景的有效性，方法论具有跨专科复制潜力（可推广至心血管、肿瘤等领域），且 LungKG
    作为首个结构化肺部知识图谱有成为行业标准基础设施的潜质。但从 VC 视角看：1）当前仅为单一学术论文成果，未关联任何商业化实体或产品路线图；2）医疗 AI
    落地需克服临床验证、FDA/NMPA 监管审批、EMR 数据互通等长周期障碍；3）跨领域复制需要每个专科重新构建高质量 KG，边际复制成本高，平台效应有限。综合判断属于'有潜力但需持续验证'区间（4-7
    分中段），投资信号偏早期警示性，建议跟踪该团队的后续技术转化动向和跨领域扩展进展。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Epic Systems
- Oracle Health
- Google DeepMind
- Microsoft Cloud for Healthcare
competitive_casualty:
- 通用LLM医疗诊断方案
- 传统规则式临床决策支持系统（CDSS）
- 缺乏领域知识图谱的AI健康助手
market_opportunities:
- 可将 LungKG 知识图谱构建方法论迁移至其他临床科室（如心血管、神经内科），开发专科级疾病诊断辅助工具
- 基于 KG 约束推理链 + 强化学习的训练范式可推广至医药研发领域的文献分析与临床决策支持，形成垂直行业解决方案
- 医院信息系统（HIS/EMR）厂商可探索将外部领域知识图谱嵌入现有系统的产品化路径，提升诊断推荐能力
risk_matrix:
  regulatory: 医疗AI诊断模型面临严格的监管审批门槛（FDA/NMPA/CE MDR），临床验证周期长，且EMR数据跨境传输可能涉及数据主权与合规问题
  technological: LungKG 的维护与更新成本较高，覆盖范围可能不全面；模型在真实临床环境中的泛化能力尚未验证；EMR数据质量高度依赖医院信息化水平，跨机构迁移存在不确定性
  competitive: 科技巨头（Google DeepMind、微软）和头部医疗AI初创公司均在布局专科诊断AI，拥有更强的数据积累、渠道资源与品牌信任度，Lung-R1作为学术成果面临商业化壁垒
  ethical: 基于EMR的训练数据存在患者隐私泄露风险；模型诊断建议可能在特定人群（种族、年龄、性别）上产生系统性偏差；临床医师过度依赖AI输出可能导致误诊责任归属争议
  additional: []
confidence:
  impact: low
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: LungKG
  canonical_name: LungKG
  url: null
  positioning: 首个结构化肺部知识图谱，包含59,038个节点和164,308条边，覆盖15种实体类型和112种关系类型，服务于肺部诊断知识组织和记录驱动的推理。
  technical_signal: 通过知识图谱约束的推理链构建和知识图谱引导的强化学习训练大语言模型，在EMR诊断任务上达到4.3583分，超越最强基线0.1476分。
  adoption_signal: null
  ecosystem_relevance: 为肺部疾病诊断这一垂直医疗领域提供了首个结构化知识图谱资源，可与大语言模型训练流程整合，促进医学诊断推理方向的研究。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该项目首次将结构化肺部知识图谱与大语言模型强化学习训练相结合，验证了知识图谱引导训练对基于电子病历的肺部诊断的有效性，有望推动医疗AI诊断推理方向的范式创新。
  risk_notes:
  - 知识图谱的覆盖范围仅限于肺部疾病领域，迁移至其他医学领域需要大量的人工标注和领域适配工作。
  - 评估仅涉及20个系统的对比实验，真实临床环境下的诊断可靠性和泛化能力仍有待进一步验证。
  score: 6.0
  article_ids:
  - ac1bb60ccdeadde6
  evidence_snippets:
  - LungKG是首个结构化的肺部知识图谱，包含59,038个节点和164,308条边，覆盖15种实体类型和112种关系类型。
  - LungKG既是可复用的肺部知识资源，也是LungKG引导的模型适配的基础，服务于诊断知识组织和记录驱动的推理。
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