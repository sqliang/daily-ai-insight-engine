---
title: 'From Signals to Structure: How Memory Architecture Drives Language Emergence
  in LLM Agents'
source: https://arxiv.org/abs/2607.00233
author:
- '[[Yashar Talebirad, Eden Redman, Ali Parsaee, Osmar R. Zaiane]]'
published: '2026-07-02'
created: '2026-07-02'
description: 'arXiv:2607.00233v1 Announce Type: new Abstract: How do two agents invent
  a shared language from scratch? In a Lewis signaling game, a sender and receiver
  must coordinate on a code using only their interaction history. We study five memory
  architectures across varying channel configurations with LLM agents and find that
  memory architecture matters more than channel capacity. Agents with a persistent
  private notebook benefit from surplus channel capacity and avoid the high-capacity
  collapse seen in stateless agents, achieving the most reliable coordination ($0.867
  \pm 0.023$ at capacity = 25). Stateless agents peak at moderate capacity and then
  degrade as the vocabulary grows beyond what a rolling context window can track The
  notebook externalizes learned conventions, freeing agents from having to re-derive
  codes each round. An information bottleneck-inspired argument predicts an optimal
  capacity equal to the number of objects. Instead, the bottleneck (capacity = 8)
  proves to be a fragility point, and surplus capacity is generally better. We show
  that channel capacity alone cannot predict coordination; memory architecture determines
  whether agents turn interaction history into stable conventions, and both dimensions
  are needed to understand how signals become language.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 64ff4ee3adee9e29
manifest_dates:
- '2026-07-02'
source_type: academic_paper
tldr: 研究发现LLM智能体在信号游戏中，记忆架构比信道容量更能决定语言能否成功涌现。
objective_summary: 研究者使用LLM智能体在Lewis信号游戏中测试五种记忆架构。拥有持久私有笔记本的智能体在信道容量为25时达到最高协调得分0.867±0.023。无状态智能体在高容量时性能崩溃。记忆架构比信道容量更能决定语言能否稳定涌现。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Lewis signaling game
  key_people: []
key_logic_flow:
- 研究者在Lewis信号游戏中，让LLM智能体担任发送者和接收者，仅通过交互历史协调出一个共享编码系统。
- 实验比较了五种记忆架构在不同信道容量下的表现，发现记忆架构比信道容量对语言涌现的影响更大。
- 拥有持久私有笔记本的智能体在信道容量为25时达到最佳协调效果（0.867±0.023），且能避免无状态智能体在高容量时出现的性能崩溃。
- 无状态智能体仅在中等信道容量时达到最佳表现，词汇量超过滚动上下文窗口追踪能力后性能下降。
- 信息瓶颈理论预测最优容量等于物体数量，但实验发现瓶颈容量（容量=8）反而是脆弱点，冗余容量普遍更优。
- 信道容量本身无法预测协调效果，必须结合记忆架构才能理解信号如何演变为稳定语言。
specialized_tags:
  paper:
    paperTitle: 'From Signals to Structure: How Memory Architecture Drives Language
      Emergence in LLM Agents'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: NLP
    methodType: LLM-based
extract_result: success
impact_score:
  score: 4.0
  reason: 该论文通过 Lewis 信号游戏实验系统比较了五种记忆架构对语言涌现的影响，结论扎实但属于渐进式学术贡献。虽然'持久私有笔记本优于无状态'这一发现对多智能体系统设计有启发意义，但短期内在工业界引发范式转变的可能性低，属于局部认知更新而非行业颠覆。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 记忆架构对LLM多智能体协调能力的影响程度
hype_assessment:
  level: low
  reason: 论文是标准的 arXiv 学术发表，标题和摘要使用'How Memory Architecture Drives Language Emergence'等描述性语言，没有'颠覆性''革命性'等
    PR 滥用词汇。结论基于定量实验结果（0.867±0.023 等具体数值），实验设计有消融研究（五种架构 × 不同信道容量），存在诚信的学术表述。
information_entropy: high
domain_disruption:
  technical_innovation: 系统揭示了记忆架构（尤其是持久私有笔记本）相比信道容量对语言涌现的支配性作用，挑战了信息瓶颈理论关于'最优容量等于物体数量'的预测——实验证明冗余容量普遍更优、瓶颈容量反而是脆弱点，为多智能体系统的记忆设计提供了新的理论依据
  business_model: 无
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 该研究揭示了持久记忆架构（私有笔记本）对LLM智能体协作语言涌现的关键作用，核心发现是'记忆架构比信道容量更能决定语言能否稳定涌现'。这对Agent系统设计有深远指导意义：当前行业过度关注上下文窗口扩展（长上下文竞赛），而该论文证明持久化外部记忆比单纯扩大信道容量更有效。长期来看，该结论可能成为Agent记忆层设计的基础理论支撑，影响RAG、Agent持久化存储等基础设施方向。但论文仍处于理论验证阶段（Lewis信号游戏），距离商业落地有较大距离，且样本量有限，复利效应需要更多实证研究支撑。评分6.5反映了其作为潜在基础设施设计原则的价值，但需持续验证。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- LangChain
- Mem0
- Anthropic
- CrewAI
- AutoGPT
competitive_casualty:
- 纯无状态Agent即服务平台
- 依赖单一长上下文窗口的Agent方案
- 未引入持久记忆层的传统RPA厂商
market_opportunities:
- 多智能体系统开发者可借鉴持久化私有笔记本（persistent notebook）的记忆架构，设计更高效的智能体协作协议，提升任务协调与信息共享的稳定性
- 企业级 AI 工作流产品可引入显式外部记忆模块（如共享知识库或智能体笔记），替代纯上下文窗口依赖，解决长时间运行任务中的信息漂移问题
- 研究者可基于该实验范式探索更多记忆架构变体（如分层记忆、混合记忆），为构建可规模化自组织语言系统的商用框架提供理论依据
risk_matrix:
  regulatory: 无
  technological: 该研究挑战了信息瓶颈理论的最优容量预测（容量=物体数量），若后续研究无法复现或发现边界条件，该结论存在被修正或推翻的可能
  competitive: 大型云厂商（如 OpenAI、Google DeepMind）可能快速将类似记忆架构集成到其多智能体产品中，挤压基于该方向创业的差异化空间
  ethical: 持久化智能体记忆可能引发数据隐私担忧——私有笔记本的底层机制若被不当扩展至用户交互场景，可能导致非预期的个人信息长期留存或滥用
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
paper_metadata:
  title: 'From Signals to Structure: How Memory Architecture Drives Language Emergence
    in LLM Agents'
  authors: []
  affiliations: []
  venue: arXiv preprint
  paper_url: https://arxiv.org/abs/2607.00233
  code_url: null
  dataset_url: null
research_problem:
  core_question: 在 Lewis 信号博弈中，不同的记忆架构如何影响 LLM 智能体之间共同语言（共享约定）的涌现？
  motivation: 理解智能体如何仅通过交互历史从头开始发明共享语言，是揭示人类语言起源和设计更高效多智能体通信机制的关键问题。以往关于涌现沟通（emergent
    communication）的研究多关注信道容量等通信约束，但较少系统性地研究智能体的记忆架构在约定固化中的作用。
  significance: fundamental
  gap_addressed: 填补了先前工作在语言涌现研究中忽略的空白：信道容量本身不足以预测协调效果，记忆架构决定了智能体能否将交互历史转化为稳定的共享约定。论文系统对比了五种记忆架构在不同信道配置下的表现，揭示了'高容量塌缩'等反直觉现象。
methodology:
  approach_summary: 该研究在 Lewis 信号博弈框架下，让发送者与接收者两个 LLM 智能体仅通过交互历史进行协调，系统比较了五种记忆架构（包括无状态基线、滚动窗口、持久私有笔记本等），并在不同信道容量（通信符号数量上限）配置下测试每种架构的协调成功率。研究发现，配备持久私有笔记本（私人记事本）的智能体能够利用额外信道容量，避免了无状态智能体在词汇量过大时出现的'高容量塌缩'，取得了最稳定的协调效果。论文还指出，传统信息瓶颈理论预测的最优容量等于物体数量的结论在
    LLM 智能体场景下并不成立，瓶颈点反而成为脆弱点。
  novelty_type: algorithmic
  key_innovations:
  - 首次系统比较了五种记忆架构在 LLM 智能体语言涌现中的表现，揭示了记忆架构比信道容量更重要的核心发现
  - 发现了无状态智能体的'高容量塌缩'现象——信道容量过大反而导致协调效果下降，而带持久记忆的智能体能有效利用多余容量
  - 对信息瓶颈理论在 LLM 智能体语言涌现中的适用性提出挑战，实验证明瓶颈容量（等于物体数量）反而成为脆弱点
  - '''私人记事本''外化学习约定的设计，使智能体无需每轮重新推导编码，为多智能体系统中约定固化提供了可扩展思路'
  inspiration_sources:
  - Lewis 信号博弈（Lewis, 1969）——语言哲学中关于约定形成的经典框架
  - 信息瓶颈理论（Tishby et al., 2000）——预测最优信道容量与任务复杂度关系
  - 涌现沟通（emergent communication）领域相关工作在参考游戏（referential game）中的实验方法
  - 外部记忆（externalized memory）与认知卸载（cognitive offloading）概念——源自认知科学
  technical_depth: moderate
experimental_rigor:
  benchmark_coverage: 采用 Lewis 信号博弈作为唯一的实验范式，通过控制信道容量（从低到高多个档次）和五种记忆架构进行系统对比实验。实验覆盖了无状态、滚动上下文窗口、持久私有笔记本等架构。评测指标为协调成功率（sender
    和 receiver 能否成功传递物体信息）。
  baseline_comparison: adequate
  ablation_quality: adequate
  reproducibility_level: partially
  claimed_improvement: 配备持久私有笔记本的智能体在信道容量为 25 时达到 0.867 ± 0.023 的协调成功率，显著优于无状态基线及其他记忆架构，且避免了高容量塌缩问题。
limitations_and_honesty:
  stated_limitations: []
  reviewer_concerns:
  - 仅使用了一种博弈范式（Lewis 信号博弈），结论是否可以推广到更复杂的通信场景缺乏验证
  - 实验仅报告了一种 LLM 模型的结果，不同模型系列（如开源模型 vs 闭源模型）的记忆行为可能存在显著差异
  - '''私人记事本''的设计在多大程度上依赖于特定模型的能力（如长上下文理解、指令遵循）尚不明确'
  - 实验规模可能较小（博弈轮次、物体数量等），统计显著性和可重复性有待进一步验证
  overclaiming_assessment: honest
  generalization_concern: 研究仅基于 Lewis 信号博弈这一个相对简化的通信场景，结论向更复杂的自然语言交互、多轮协商、大规模多智能体系统等真实场景的泛化能力尚未验证。不同记忆架构的效果可能随任务复杂度、智能体数量、通信拓扑结构的变化而发生质变。
industrial_relevance:
  applicable_domains:
  - 多智能体系统（Multi-Agent Systems）通信协议设计
  - 人机协作中的共享约定建立
  - AI 智能体工具使用与记忆系统设计
  - 去中心化智能体网络中的协调机制
  compute_requirements: commodity
  integration_readiness: needs_research
  cost_efficiency_analysis: 该方法本身不需要额外训练或微调，仅通过设计智能体的记忆架构即可提升协调效果，算力开销主要来自 LLM 推理本身。'私人记事本'架构增加了一定的存储和检索开销，但相比重新推理编码而言整体效率更高。不过，当前结果尚处于实验室验证阶段，距离可靠地集成到工业级多智能体系统还需进一步的鲁棒性测试与规模扩展研究。
related_work_context:
  closest_prior_works:
  - Lewis (1969) — Lewis 信号博弈的原始理论框架
  - Emergent communication 系列工作（Lazaridou et al., 2017; Mordatch & Abbeel, 2018）—
    通过强化学习研究智能体之间语言涌现
  - Bisk et al. (2020) 等人关于参考游戏（referential game）中通信效率的研究
  - Dagan et al. (2021) — 关于多智能体系统中的交互记忆与协作
  advancement_over_prior: 先前涌现沟通研究主要使用强化学习训练的智能体，而本工作首次在 LLM 驱动的情境化智能体（in-context
    learning）中系统研究了记忆架构对语言涌现的影响。其关键发现——记忆比信道容量更重要、高容量塌缩现象、信息瓶颈假设的失效——为理解符号通信的认知基础提供了新的实证视角，超越了传统基于参数学习的框架。
  opens_new_direction: true
  potential_follow_ups:
  - 将实验扩展到更多 LLM 系列及更复杂的通信博弈（如图形传递、概念谈判）以验证结论的泛化性
  - 探索混合记忆架构（如分层记忆、检索增强记忆）在更大规模多智能体系统中的表现
  - 研究记忆架构与通信效率之间的联合优化，探索自适应信道容量分配策略
  - 将'私人记事本'机制与工具使用结合，设计可工业落地的多智能体协调协议
---

# Computer Science > Artificial Intelligence

# Title:From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents

View PDF HTML (experimental)Abstract:How do two agents invent a shared language from scratch? In a Lewis signaling game, a sender and receiver must coordinate on a code using only their interaction history. We study five memory architectures across varying channel configurations with LLM agents and find that memory architecture matters more than channel capacity. Agents with a persistent private notebook benefit from surplus channel capacity and avoid the high-capacity collapse seen in stateless agents, achieving the most reliable coordination ($0.867 \pm 0.023$ at capacity = 25). Stateless agents peak at moderate capacity and then degrade as the vocabulary grows beyond what a rolling context window can track The notebook externalizes learned conventions, freeing agents from having to re-derive codes each round. An information bottleneck-inspired argument predicts an optimal capacity equal to the number of objects. Instead, the bottleneck (capacity = 8) proves to be a fragility point, and surplus capacity is generally better. We show that channel capacity alone cannot predict coordination; memory architecture determines whether agents turn interaction history into stable conventions, and both dimensions are needed to understand how signals become language.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.