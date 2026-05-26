---
title: 'Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization'
source: https://arxiv.org/abs/2605.05040
author:
- '[[Xin Yu, Liuchen Liao, Yiwen Zhang, Yingchen Yu, Lingzhou Xue, Qinzhen Guo]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.05040v1 Announce Type: cross Abstract: On-policy distillation
  is an efficient alternative to reinforcement learning, offering dense token-level
  training signals. However, its reliance on a stronger external teacher has driven
  recent work on on-policy self-distillation, where the same model serves as both
  teacher and student under different prompt contexts. Yet, existing self-distillation
  methods largely reduce learning to KL matching toward the context-augmented teacher
  model. This approach often suffers from training instability and can degrade reasoning
  performance over time. Moreover, self-distillation from the same model with prompt
  augmentation lacks the exploratory diversity provided by a genuine external teacher.
  To address these limitations, we move beyond fixed-teacher KL matching and propose
  \textbf{P}reference-\textbf{B}ased \textbf{S}elf-\textbf{D}istillation (\textbf{PBSD}),
  which revisits on-policy self-distillation through a reward-regularized perspective.
  Instead of directly matching the teacher distribution, we derive a reward-regularized
  objective whose analytic optimum is a reward-reweighted teacher distribution, yielding
  a target policy provably superior to the original teacher under this objective.
  Practically, PBSD optimizes preference gaps between teacher and student samples
  while maintaining on-policy student sampling. We support this framework with a statistical
  analysis of the induced preference-learning problem, formally establishing when
  on policy self-distillation is preferable to learning from an external teacher in
  our setting. Experiments on mathematical reasoning and tool-use benchmarks across
  multiple model scales demonstrate that PBSD consistently achieves the strongest
  average performance among comparable baselines, showing improved training stability
  over prior self-distillation baselines while preserving token efficiency.'
tags:
- clippings
id: 58f201f9fcedbf0b
source_type: academic_paper
tldr: 基于奖励正则化的偏好自蒸馏方法PBSD，超越传统KL匹配，提升训练稳定性
objective_summary: PBSD方法提出基于奖励正则化的在线自蒸馏框架，用偏好差距优化替代KL匹配，在数学推理和工具使用基准上取得最强平均性能，提升训练稳定性并保持token效率。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - PBSD
  - KL matching
  - reward regularization
  - on-policy distillation
  - self-distillation
  key_people: []
key_logic_flow:
- 现有的在线自蒸馏方法主要依赖KL匹配，存在训练不稳定和推理性能随时间退化的问题。
- PBSD提出基于奖励正则化的在线自蒸馏框架，其解析最优解是对教师分布进行奖励加权后的目标策略。
- PBSD通过优化教师样本与学生样本之间的偏好差距进行学习，同时保持在线学生采样。
- 论文从统计角度分析了偏好学习问题，正式界定了在线自蒸馏何时优于从外部教师学习。
- 在数学推理和工具使用基准测试上，PBSD在多个模型规模下均取得最强平均性能，训练稳定性优于现有自蒸馏基线方法。
impact_score:
  score: 6.0
  reason: PBSD提出了一个超越传统KL匹配的自蒸馏新框架，通过奖励正则化解决了在线自蒸馏中训练不稳定和推理性能退化两大痛点，在数学推理和工具使用基准上取得最佳平均性能。该方法有理论支撑（统计分析和解析最优解推导）和跨模型规模的实验验证。但该方法本质上是训练流程中的优化改进，属于渐进式创新，尚未达到改变行业范式的程度。评分：6.0
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 自蒸馏训练的稳定性和效率提升，以及该方法在多大程度上可以替代外部教师模型
hype_assessment:
  level: low
  reason: 论文用语克制，使用了'consistent improvements'和'strongest average performance'等具体、可验证的表述，没有出现'革命性'、'颠覆'等PR滥用词汇。提供了完整的理论分析（统计意义上界定何时自蒸馏优于外部教师）、推导过程和消融实验，属于扎实的学术贡献，不存在概念包装水分。
information_entropy: high
domain_disruption:
  technical_innovation: 提出用偏好差距优化替代传统KL匹配的自蒸馏范式，从奖励正则化角度推导了解析最优解（奖励加权后的教师分布），并理论上证明该最优策略优于原始教师策略。同时给出了偏好学习问题的统计分析，正式界定了在线自蒸馏优于外部教师学习的条件。
  business_model: 若该方法被验证可大规模推广至更多任务和模型规模，有望降低大模型训练中对强大外部教师模型的依赖，减少蒸馏所需的计算资源和标注数据成本，使自蒸馏成为更经济高效的模型优化路径。
engineering_complexity: prototype
compound_value:
  score: 4.5
  reason: PBSD 提出了一个理论扎实的在线自蒸馏框架，在数学推理和工具使用基准上表现优于 KL 匹配基线。从 VC 视角看，这项工作的长期复利价值有限：首先，它是一篇纯学术论文（theoretical_claim），无公司实体背书，离产品化距离尚远；其次，作为训练方法论，它本质上是一个'可被吸收的优化技巧'——一旦被证明有效，主流
    AI 实验室（OpenAI、Anthropic、Meta）会快速将其整合进内部训练管线，而非以独立技术形式存在，因此难以形成持续的商业复利。不过，其理论贡献（解析最优解
    + 统计依据）为自蒸馏提供了更严谨的框架，若被社区广泛采用，有潜力成为 LLM 微调/蒸馏管线中的标准组件，算得上是'细分赛道的基础设施'级别贡献。综合评分
    4.5，属于方法论层面有价值、但商业化捕获能力弱的技术创新。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- OpenAI
- Anthropic
- Meta
- Google DeepMind
- Mistral AI
competitive_casualty:
- 依赖外部教师模型的蒸馏服务提供商
- 闭源蒸馏 API 平台
market_opportunities:
- AI模型微调与对齐服务商可将PBSD方法集成到训练管线中，解决传统KL匹配训练不稳定和推理性能退化问题，提升商业化模型的竞争力
- 工具调用型AI Agent开发者可利用PBSD在工具使用基准上的突出表现，优化Agent行为策略，提升复杂任务场景下的自主决策能力
- 缺乏强外部教师模型的中小团队可借助PBSD的自蒸馏机制，在有限资源下通过在线自蒸馏持续迭代模型推理能力
risk_matrix:
  regulatory: 无
  technological: 论文为纯理论推导加有限规模的实验验证，目前未公布代码，存在复现困难或后续研究证伪其核心结论的风险
  competitive: 若PBSD被大规模验证有效，头部AI实验室可快速内化同类方法，中小团队的先发优势窗口期可能较短
  ethical: 自蒸馏方法可能继承并放大教师模型中的已有偏见，且训练稳定性的提升可能降低对模型行为异常的可观测性
  additional: []
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: speculative_watch
---

# Computer Science > Machine Learning

# Title:Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization

View PDF HTML (experimental)Abstract:On-policy distillation is an efficient alternative to reinforcement learning, offering dense token-level training signals. However, its reliance on a stronger external teacher has driven recent work on on-policy self-distillation, where the same model serves as both teacher and student under different prompt contexts. Yet, existing self-distillation methods largely reduce learning to KL matching toward the context-augmented teacher model. This approach often suffers from training instability and can degrade reasoning performance over time. Moreover, self-distillation from the same model with prompt augmentation lacks the exploratory diversity provided by a genuine external teacher. To address these limitations, we move beyond fixed-teacher KL matching and propose \textbf{P}reference-\textbf{B}ased \textbf{S}elf-\textbf{D}istillation (\textbf{PBSD}), which revisits on-policy self-distillation through a reward-regularized perspective. Instead of directly matching the teacher distribution, we derive a reward-regularized objective whose analytic optimum is a reward-reweighted teacher distribution, yielding a target policy provably superior to the original teacher under this objective. Practically, PBSD optimizes preference gaps between teacher and student samples while maintaining on-policy student sampling. We support this framework with a statistical analysis of the induced preference-learning problem, formally establishing when on policy self-distillation is preferable to learning from an external teacher in our setting. Experiments on mathematical reasoning and tool-use benchmarks across multiple model scales demonstrate that PBSD consistently achieves the strongest average performance among comparable baselines, showing improved training stability over prior self-distillation baselines while preserving token efficiency.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.