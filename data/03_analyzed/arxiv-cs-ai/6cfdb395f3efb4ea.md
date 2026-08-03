---
title: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures
source: https://arxiv.org/abs/2607.28802
author:
- '[[Harsh Raj, Vipul Gupta, Anas Mahmoud, Razvan-Gabriel Dumitru, Darvin Yi, Aakash
  Sabharwal, Yunzhong He]]'
published: '2026-08-03'
created: '2026-08-03'
manifest_dates:
- '2026-08-03'
description: 'arXiv:2607.28802v1 Announce Type: new Abstract: Existing evaluations
  often reduce agent failures to system-level outcomes, obscuring where the fault
  originated and which intervention would improve the agent system. This creates a
  repair-assignment problem: the same visible failure may call for model post-training,
  harness engineering, environment redesign, or benchmark repair depending on its
  source. Because agent behavior emerges from interactions among models, harnesses,
  users, tools, memory, and environments, outcome-level labels are often insufficient
  for improvement. Most failure taxonomies do little to resolve this problem because
  they are benchmark-specific and lack a shared structure. We introduce an interaction-centric
  taxonomy that localizes failures to the interactions in which they originate and
  identifies the responsible component. It organizes 41 failure modes by assigning
  each to an edge between two components and a fault side indicating where the repair
  belongs. This makes the taxonomy actionable: model-side failures identify targets
  for post-training, harness-side failures point to scaffolding and tool-integration
  fixes, and environment or grader failures reveal evaluation conditions requiring
  redesign. The schema applies across agent architectures, from coding assistants
  to long-horizon personal assistants and multi-agent systems. We ground the taxonomy
  in worked examples from public benchmarks, model system cards, published reports,
  and logged agent trajectories, and evaluate its reproducibility using independent
  reasoning agents as judges. Across four frontier models, the strongest judge reaches
  Cohen''s $\kappa=0.76$ against human category labels, suggesting that the categories
  capture shared structure rather than annotator-specific preferences.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6cfdb395f3efb4ea
source_type: academic_paper
tldr: 本文提出一种以交互为中心的智能体失败分类体系，将41种失败模式定位到组件间交互边与故障归属侧，区分模型侧、框架侧与评测侧修复责任。在四个前沿模型上，最强评判者对人工标签的
  Cohen's κ 达 0.76。
objective_summary: 一篇 arXiv 预印本论文提出以交互为中心的智能体失败分类体系，旨在解决现有评测只报告系统级结果、掩盖故障来源、导致修复分配困难的普遍问题。该体系将41种失败模式分配到模型、框架、用户、工具、记忆与环境等组件之间的交互边，并标明责任侧，使模型侧失败对应后训练目标、框架侧对应脚手架与工具集成修复、评测侧对应环境重设计。研究者用公开基准、模型系统卡片、已发表报告与智能体轨迹日志验证该分类，并用独立推理智能体作为评判者评估可复现性，在四个前沿模型上最强评判者的
  Cohen's κ 达 0.76。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - AI Agent
  - LLM
  - Multi-Agent Systems
  key_people: []
key_logic_flow:
- 现有评测常把智能体失败简化为系统级结果，掩盖故障来源，导致同一可见失败可能对应模型后训练、框架工程、环境重设计或基准修复等不同干预。
- 作者提出以交互为中心的失败分类体系，将41种失败模式分别指派到两个组件之间的交互边，并标注责任侧以定位需要修复的对象。
- 该分类具有可操作性：模型侧失败对应后训练目标，框架侧失败对应脚手架与工具集成修复，环境或评分器失败对应评测条件重设计。
- 该体系可跨智能体架构迁移，覆盖编码助手、长时程个人助手和多智能体系统。
- 研究者从公开基准、模型系统卡片、已发表报告和记录的智能体轨迹中取得实例来支撑该分类体系。
- 可复现性评估使用独立推理智能体作为评判者，在四个前沿模型上最强评判者对人工类别标签的 Cohen's κ 达到 0.76。
object_mentions:
- object_type: paper
  name: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures
  canonical_name: Model or Harness? An Interaction-Centric Taxonomy for Localizing
    Agent Failures
  url: https://arxiv.org/abs/2607.28802
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者提出一种以交互为中心的失败分类体系，将41种失败模式分配到组件之间的交互边上，并标明故障归属一侧，从而定位责任组件。
  - 该体系具有可操作性：模型侧失败指向后训练目标，框架侧失败指向脚手架与工具集成修复，环境或评分器失败指向评测条件重设计。
  - 在四个前沿模型上，最强评判者对人工类别标签达到 Cohen's κ=0.76，表明这些类别捕捉的是共享结构而非标注者特定偏好。
  article_id: 6cfdb395f3efb4ea
extract_result: success
impact_score:
  score: 5.5
  reason: 该论文直击智能体工程中'模型还是框架背锅'的修复分配痛点，提供了41种失败模式的结构化分类体系（组件间交互边+责任侧二维标注），并用独立推理智能体作为评判者完成可复现性验证（Cohen's
    κ=0.76），对智能体评测、调试和修复责任分配具有方法论价值，属于该领域少见的系统化尝试。但它是概念框架类贡献而非技术范式突破，不直接改变产品竞争格局，也不会带来算力或成本结构变化，短期影响力主要停留在学术圈与开发者工具层，故评分落在中位区间。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 41种失败模式的分类体系能否在真实智能体调试中低成本落地、是否具备跨框架通用性
hype_assessment:
  level: low
  reason: 文中未出现'颠覆''革命性'等PR化措辞，作者用公开基准、模型系统卡片、已发表报告和真实智能体轨迹做实例锚定，并以独立推理智能体做可复现性评估（κ=0.76），属于严谨学术论证而非概念炒作。κ值虽非极高但作者如实报告，未夸大评判者一致性，整体水分很低。
information_entropy: high
domain_disruption:
  technical_innovation: 首次将智能体失败从'系统级结果'分解为'组件间交互边+责任侧'的二维结构化分类，使失败定位与修复责任分配（模型后训练/框架脚手架与工具集成/评测环境与评分器重设计）可操作化，并以推理智能体评判验证跨架构迁移性，是评测方法论层面的实质创新。
  business_model: 该分类体系可作为智能体可观测性、失败诊断与调试工具链的底层标注标准，可能催生面向 agent 开发的归因分析类产品（如失败责任面板、修复建议生成），降低企业排查多组件交互故障的成本，但本身不直接重塑既有商业模式。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 该论文解决的是 Agent 生态中真实且日益尖锐的'修复归属'问题：同一失败可能源于模型后训练、框架脚手架、环境设计或评测基准，现有系统级指标无法区分。若该交互中心分类体系被可观测性与评测工具链采纳，有潜力成为
    Agent 调试/评测细分赛道的事实标准层——这类语义层一旦沉淀，复利效应明显。但当前仅为 arXiv 理论性预印本，无商业实体与产品化路径，且分类法落地高度依赖工具厂商、评测平台与前沿实验室的采纳意愿，需持续验证，故落在'细分基础设施候选'区间而非确定性基石。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- LangChain (LangSmith)
- Arize AI
- Braintrust
- METR
- Anthropic
- OpenAI
competitive_casualty:
- 纯基准分数导向的 Agent 评测厂商
- 黑盒 RAG/Agent 可观测性工具
- 缺乏故障归因能力的传统 QA 测试平台
market_opportunities:
- 智能体可观测性与故障诊断工具创业者可将该交互式失败分类体系内置到 Trace 与调试产品中，帮助开发者把 Agent 故障精准定位到模型、框架、工具或环境侧，填补当前评估只报系统级结果的空白
- Agent 评测与质量保障平台可借鉴该分类体系构建标准化失败归因标签，提升跨团队、跨框架的评测结果可比性，形成差异化竞争力并沉淀为付费能力
- 模型后训练团队可基于模型侧失败模式定向挖掘训练数据与对齐目标，把失败定位结果转化为 RLHF/RLAIF 数据飞轮，降低无效干预成本
risk_matrix:
  regulatory: 无直接监管风险；但若该分类体系被用于高风险 Agent 部署的合规归因（如 AI Act 透明度与可靠性要求），需确保归因结论可审计、可追溯
  technological: 该体系为理论框架预印本，Agent 架构（长时程记忆、多智能体）快速演进可能导致分类边界过时；LLM 评判者 Cohen's κ=0.76
    并非完美一致性，自动标注存在类别偏好与偏差放大风险
  competitive: LangChain、OpenAI、Anthropic 等平台可能推出各自专有的失败归因与观测标准，使该学术分类难以成为事实标准，商业化落地前可能被生态内原生方案挤压
  ethical: 使用 LLM 评判者自动打标签可能放大模型固有偏见；基于'归属侧'的归因可能被厂商用于推卸责任（将模型缺陷归因于环境或评测方）；分析记录轨迹日志涉及隐私与数据投毒风险
  additional:
  - 分类体系缺乏标准化组织背书，若多套并行标准并存将增加采用成本
  - 作为预印本尚未经过完整同行评审，结论稳健性与跨领域泛化性有待进一步验证
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures

View PDF HTML (experimental)Abstract:Existing evaluations often reduce agent failures to system-level outcomes, obscuring where the fault originated and which intervention would improve the agent system. This creates a repair-assignment problem: the same visible failure may call for model post-training, harness engineering, environment redesign, or benchmark repair depending on its source. Because agent behavior emerges from interactions among models, harnesses, users, tools, memory, and environments, outcome-level labels are often insufficient for improvement. Most failure taxonomies do little to resolve this problem because they are benchmark-specific and lack a shared structure. We introduce an interaction-centric taxonomy that localizes failures to the interactions in which they originate and identifies the responsible component. It organizes 41 failure modes by assigning each to an edge between two components and a fault side indicating where the repair belongs. This makes the taxonomy actionable: model-side failures identify targets for post-training, harness-side failures point to scaffolding and tool-integration fixes, and environment or grader failures reveal evaluation conditions requiring redesign. The schema applies across agent architectures, from coding assistants to long-horizon personal assistants and multi-agent systems. We ground the taxonomy in worked examples from public benchmarks, model system cards, published reports, and logged agent trajectories, and evaluate its reproducibility using independent reasoning agents as judges. Across four frontier models, the strongest judge reaches Cohen's $\kappa=0.76$ against human category labels, suggesting that the categories capture shared structure rather than annotator-specific preferences.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.