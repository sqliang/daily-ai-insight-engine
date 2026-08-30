---
title: World models of environment, agent and joint agent-environment systems
source: https://arxiv.org/abs/2608.20401
author:
- '[[Manuel Baltieri, Filippo Torresan, Yivan Zhang, Alexander Boyd, Fernando E. Rosas]]'
published: '2026-08-24'
created: '2026-08-24'
manifest_dates:
- '2026-08-24'
description: 'arXiv:2608.20401v1 Announce Type: new Abstract: World models are a central
  component of model-based reinforcement learning. They are usually discussed in terms
  of what variables they predict, such as observations, rewards, states, latent or
  information states. We argue that there is a prior distinction: which channel they
  model. We consider three cases: the environment channel $O_{:} \mid A_{:}$, the
  agent channel $A_{:} \mid O_{:}$, and the realised joint process $(A, O)_{:}$, equivalently
  viewed as a channel with no inputs. Using computational mechanics, we define canonical
  predictive models for these three cases as $\epsilon$-transducers or $\epsilon$-machines.
  Canonical environment models recover standard predictive state representations,
  while the other two give analogous notions of canonical models for the agent and
  the joint system. We then build canonical support-restricted environment and agent
  models induced by closed-loop coupling, whose predictive equivalences range over
  continuations supported by the realised interaction. The key structural result is
  that canonical support-restricted environment states factor through the canonical
  joint causal states, and their transition structure is induced directly from the
  joint model; the agent-side construction is dual. Finally, we give a POMDP/controller
  example in which the unrestricted environment model has infinitely many states while
  the canonical support-restricted model induced by the coupling is finite. The framework
  clarifies what different world models are models of, and how coupling and support
  restriction can change their canonical predictive structure and complexity.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e845ffbc7ba2f0cd
source_type: academic_paper
tldr: 该 arXiv 论文提出世界模型研究应优先区分所建模的通道，即环境通道、智能体通道与联合过程三类，并用计算力学定义了三类情况的规范预测模型。论文进一步证明闭环耦合诱导的支持受限模型可显著降低状态复杂度，示例中从无限状态降为有限。
objective_summary: 该论文（arXiv 2608.20401）属于人工智能领域，研究基于模型的强化学习中的世界模型。作者主张在讨论世界模型预测什么变量之前，应先区分其建模的通道，将模型分为环境通道、智能体通道与实际联合过程三类。论文运用计算力学为三类情况定义规范预测模型（ε-转导器或
  ε-机器），并构建闭环耦合诱导的支持受限环境与智能体模型。核心结构结果表明支持受限环境状态可经联合因果状态分解，且论文以 POMDP/控制器示例展示无限制模型状态无限而受限模型有限。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - World Models
  - Model-Based Reinforcement Learning
  - Computational Mechanics
  - ε-transducers
  - ε-machines
  - POMDP
  - Predictive State Representations
  - Causal States
  key_people: []
key_logic_flow:
- 论文主张世界模型研究存在一个先于“预测什么变量”的区分，即“建模哪个通道”，并将世界模型分为环境通道、智能体通道与联合过程三类。
- 作者使用计算力学为三类情况定义规范预测模型，分别表示为 ε-转导器（ε-transducers）或 ε-机器（ε-machines）。
- 规范环境模型恢复了标准的预测状态表示，而另外两类为智能体与联合系统提供了对应的规范模型概念。
- 论文构建了由闭环耦合诱导的规范支持受限环境与智能体模型，其预测等价关系覆盖实际交互所支持的延续。
- 关键结构结果是规范支持受限环境状态可通过规范联合因果状态分解，其转移结构直接由联合模型诱导，智能体侧构造与之对偶。
- 论文给出 POMDP/控制器示例，其中无限制环境模型具有无限多个状态，而由耦合诱导的规范支持受限模型是有限的。
object_mentions:
- object_type: paper
  name: World models of environment, agent and joint agent-environment systems
  canonical_name: arXiv 2608.20401 World models of environment, agent and joint agent-environment
    systems
  url: https://arxiv.org/abs/2608.20401
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文定义了世界模型所建模的三种通道，即环境通道、智能体通道以及实际联合过程。
  - 论文以 POMDP/控制器示例说明无限制环境模型状态无限，而耦合诱导的支持受限模型有限。
  article_id: e845ffbc7ba2f0cd
extract_result: success
impact_score:
  score: 4.5
  reason: 评分依据：该论文提供了一个理论优雅的概念框架，主张世界模型研究应先区分所建模的通道（环境/智能体/联合过程），并用计算力学统一给出三类情况的规范预测模型定义。其核心结构结果——闭环耦合诱导的支持受限模型可将无限状态压缩为有限——对基于模型的强化学习与世界模型复杂度研究具有学术指导意义，可能推动
    PSR、ε-机器等流派的理论整合。但该工作纯属理论贡献，无实验验证、无代码实现、无产业落地路径，短期内不会改变任何行业竞争格局或产品形态，影响主要局限于学术圈与前沿研究群体。综合判定处于『有实质内容但未达重要产品级冲击』的区间，评分为
    4.5。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 关注该框架能否统一现有世界模型各流派（预测状态表示、ε-机器等）的数学基础，以及支持受限模型对实际强化学习系统状态复杂度的理论指导价值
hype_assessment:
  level: low
  reason: 判定依据：全文使用计算力学形式化定义规范预测模型，给出结构定理与 POMDP/控制器示例，定位表述克制（'澄清不同世界模型所建模的对象'），未见『颠覆』『革命性』等
    PR 滥用词汇，也无配套夸大宣传话术，属于实打实的理论干货。
information_entropy: high
domain_disruption:
  technical_innovation: 提出以『建模通道』为第一性的世界模型分类框架，用计算力学（ε-转导器/ε-机器）为环境通道、智能体通道与联合过程统一构造规范预测模型；核心结构定理证明闭环耦合诱导的支持受限环境状态可通过联合因果状态分解、转移结构由联合模型直接诱导，示例中可将无限状态压缩为有限，为理解世界模型的复杂度来源与模型选择提供了新的数学工具。
  business_model: 无。该论文为纯理论贡献，未涉及任何商业模式或产品形态；其潜在间接价值在于为世界模型的可扩展性与样本效率提供理论基础，长期或影响具身智能、机器人等依赖模型学习的领域路线选择，但不构成短期商业冲击。
engineering_complexity: conceptual
compound_value:
  score: 6.0
  reason: 分步推演：①世界模型赛道正处于资本密集期（NVIDIA Cosmos、Wayve GAIA、DeepMind Genie、World Labs
    等相继重仓投入），是世界模拟器与具身智能的底层组件，资金真实在流动；②本文核心增量在于提出'建模哪个通道'的先行区分，并用计算力学给出规范预测模型，关键结构结果是闭环耦合诱导的支持受限模型可将状态复杂度从无限降至有限——若被实证复现并工程化，将直接转化为世界模型训练/推理的算力成本优势，这是资本最看重的效率杠杆；③必须承认风险：本文为纯理论
    arXiv 论文，无代码、无基准实验、无商业实体，学术到工程的转化在 RL 领域通常需 3-5 年，且存在被更强实证方法覆盖的可能，短期无直接现金流兑现；④综合判断：处于'细分赛道基础设施候选'区间（4-7
    分），长期若成为世界模型设计的标准理论框架则复利显著，但当前需持续验证，故给 6.0 分。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- NVIDIA
- DeepMind
- Wayve
- World Labs
competitive_casualty:
- 依赖暴力算力扩展的世界模型初创公司
- 忽视通道结构的生成式世界模拟器厂商
market_opportunities:
- 基于支持受限世界模型可显著降低状态复杂度的理论洞见，可开发更紧凑、样本高效的模型强化学习算法，应用于机器人控制与具身智能等对计算资源敏感的落地场景
- 智能体通道与联合过程建模框架可为 AI Agent 的状态表征与决策架构设计提供新的理论指导，帮助构建更能区分'建模对象'的下一代 Agent 系统
- 可将该理论框架转化为世界模型的形式化评测基准，帮助从业者在不同世界模型方案之间比较真实的状态复杂度与预测结构
risk_matrix:
  regulatory: 无
  technological: 该理论依赖计算力学与 ε-转导器形式体系，尚未在主流 RL 框架（JAX、RLlib、TorchRL 等）或规模化任务上得到验证；若后续无法复现'支持受限带来复杂度骤降'的实际收益，可能停留在纯学术层面
  competitive: 世界模型赛道由 DeepMind（Genie）、Meta（JEPA）、OpenAI 等巨头主导，且存在多种竞争性形式框架；该论文若未形成代码生态或进入主流基准，其影响力与工程落地空间有限
  ethical: 世界模型若泛化用于高保真环境与交互仿真，可能间接助长深度伪造、对抗性环境或仿真欺骗等下游滥用，但本文本身暂无直接伦理风险
  additional: []
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
---

# Computer Science > Artificial Intelligence

# Title:World models of environment, agent and joint agent-environment systems

View PDFAbstract:World models are a central component of model-based reinforcement learning. They are usually discussed in terms of what variables they predict, such as observations, rewards, states, latent or information states. We argue that there is a prior distinction: which channel they model. We consider three cases: the environment channel $O_{:} \mid A_{:}$, the agent channel $A_{:} \mid O_{:}$, and the realised joint process $(A, O)_{:}$, equivalently viewed as a channel with no inputs. Using computational mechanics, we define canonical predictive models for these three cases as $\epsilon$-transducers or $\epsilon$-machines. Canonical environment models recover standard predictive state representations, while the other two give analogous notions of canonical models for the agent and the joint system. We then build canonical support-restricted environment and agent models induced by closed-loop coupling, whose predictive equivalences range over continuations supported by the realised interaction. The key structural result is that canonical support-restricted environment states factor through the canonical joint causal states, and their transition structure is induced directly from the joint model; the agent-side construction is dual. Finally, we give a POMDP/controller example in which the unrestricted environment model has infinitely many states while the canonical support-restricted model induced by the coupling is finite. The framework clarifies what different world models are models of, and how coupling and support restriction can change their canonical predictive structure and complexity.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.