---
title: 'Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems'
source: https://arxiv.org/abs/2605.26302
author:
- '[[Jianing Zhu, Yeonju Ro, John Robertson, Kevin Wang, Junbo Li, Haris Vikalo, Aditya
  Akella, Zhangyang Wang]]'
published: '2026-05-27'
created: '2026-05-28'
description: 'arXiv:2605.26302v1 Announce Type: new Abstract: Long-lived AI agents
  are increasingly deployed as persistent operational systems, yet they are still
  evaluated like freshly initialized models. Day-one benchmarks miss a basic systems
  question: how long does an agent remain reliable after deployment? Even when model
  weights are frozen, an agent''s effective state keeps changing as it compresses
  interaction history, retrieves from a growing memory store, revises facts after
  updates, and undergoes routine maintenance. Reliability therefore becomes a lifespan
  property of the full agent harness, not only a snapshot property of the base model.
  We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan
  engineering: measuring not only whether deployed agents degrade, but what form the
  degradation takes and where repair should target. AgingBench organizes agent aging
  into four mechanisms: compression aging, interference aging, revision aging, and
  maintenance aging. To diagnose these failures, AgingBench uses temporal dependency
  graphs and paired counterfactual probes that produce diagnostic profiles for the
  write, retrieval, and utilization stages of the memory pipeline. Across 7 scenarios,
  14 models, multiple memory policies, and both runner-controlled and autonomous agents,
  over ~400 runs spanning 8 - 200 sessions show that agent aging is not one-dimensional:
  behavioral tests can remain clean while factual precision decays; derived-state
  tracking can collapse sharply within a single model; and the same wrong answer can
  require different repairs depending on what the diagnostic profile points to. These
  results suggest that reliable agent deployment requires lifespan evaluation, mechanism-level
  diagnosis, and stage-targeted repair, not only stronger day-one models.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 27fbaeab8c07a7da
source_type: academic_paper
tldr: 该论文提出 AgingBench，一个用于评估已部署 AI 代理长期可靠性的纵向基准，识别了压缩老化、干扰老化、修订老化和维护老化四种机制，并通过约 400
  次实验发现代理老化是多维的，需要全生命周期评估而非仅依赖初始模型性能。
objective_summary: 研究者在一篇 arXiv 论文中提出了 AgingBench，这是一个用于衡量已部署 AI 代理长期可靠性的纵向基准，而非仅评估初始化时的模型性能。该基准将代理老化分为压缩老化、干扰老化、修订老化和维护老化四种机制，并使用时间依赖图和配对反事实探针诊断记忆管道的写入、检索和利用阶段故障。在
  7 个场景、14 个模型、多种记忆策略下进行的约 400 次实验表明，行为测试可能保持正常而事实精度已下降，不同老化模式需要不同的针对性修复。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - AgingBench
  - Agent Lifespan Engineering
  - Temporal Dependency Graphs
  - Counterfactual Probes
  key_people: []
key_logic_flow:
- 该论文指出长期部署的 AI 代理在模型权重冻结后，其有效状态仍会因交互历史压缩、记忆库增长、事实修订和日常维护而持续变化。
- 论文提出了 AgingBench 纵向可靠性基准，将代理老化机制分为压缩老化、干扰老化、修订老化和维护老化四类。
- AgingBench 使用时间依赖图和配对反事实探针来诊断记忆管道的写入、检索和利用阶段的具体故障并生成诊断画像。
- 在 7 个场景、14 个模型、多种记忆策略下进行的约 400 次实验覆盖了 8 到 200 个会话周期，横跨 runner 控制和自主代理两种类型。
- 实验表明代理老化并非一维：行为测试可能仍然正常而事实精度已经下降，衍生状态追踪可能在单个模型内急剧崩溃。
- 可靠的代理部署需要全生命周期评估、机制级别的诊断和分阶段针对性修复，而非仅依赖于更强的初始模型。
extract_result: success
object_mentions:
- object_type: project
  name: AgingBench
  canonical_name: AgingBench
  url: https://arxiv.org/abs/2605.26302
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文介绍了 AgingBench，一个用于代理生命周期工程的纵向可靠性基准，不仅衡量退化程度还诊断退化形式。
  - AgingBench 将代理老化组织为四种机制：压缩老化、干扰老化、修订老化和维护老化。
  - 在 7 个场景、14 个模型和多种记忆策略下的约 400 次实验说明代理老化是多维的，需要机制级别诊断和针对性修复。
  article_id: 27fbaeab8c07a7da
impact_score:
  score: 6.5
  reason: 该论文提出了一个被行业系统性忽视的关键问题——AI Agent 部署后的持续退化现象，并贡献了 AgingBench 基准和四种老化机制的分类框架。从技术架构视角看，它将
    Agent 可靠性从'初始化快照评测'重构为'全生命周期工程'，这对正在大规模部署 Agent 的企业（如客服、自动化运维、AI 编程助手）具有直接的方法论指导价值。但它本质上仍是一篇学术论文而非可落地的产品或基础设施，短期内不会引发行业范式转移，因此评分落在重要但非革命性的区间。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 行为测试保持清洁而事实精度已衰退——现有 Agent 评测体系可能存在系统性盲区，部署后的 Agent 到底有多不可靠？
hype_assessment:
  level: low
  reason: 论文采用标准的学术研究范式，提出了可复现的基准（AgingBench）、明确的实验设计（7 场景 × 14 模型 × ~400 次运行）和可量化的诊断方法（时序依赖图
    + 反事实探针），未使用'颠覆''革命性'等 PR 词汇，结论审慎且附带消融分析，属于实打实的学术干货。
information_entropy: high
domain_disruption:
  technical_innovation: 将 Agent 老化归纳为四种可诊断的机制（压缩老化、干扰老化、修订老化、维护老化），并引入时序依赖图和配对反事实探针，对记忆管道的写入、检索、利用三个阶段生成诊断画像——这是首次将
    Agent 可靠性问题从'模型能力'解耦为'系统生命周期'的工程框架，而非仅仅提出更强的初始模型。
  business_model: 该研究暗示了一个新兴市场方向——Agent 生命周期可观测性平台。类似于 Datadog 对微服务的监控，未来可能需要专门的 Agent
    健康度持续监测工具，在行为退化发生之前预警并提供阶段定向修复建议。这可能催生面向企业 Agent 部署的'AgentOps'或'Agent Reliability
    as a Service'类产品。
engineering_complexity: prototype
compound_value:
  score: 7.5
  reason: 该研究开创性地定义了'Agent 生命周期工程'这一全新问题域，而非仅仅提出另一个基准。其核心洞察——即使模型权重冻结，Agent 的有效状态仍会因记忆压缩、事实修订、交互历史积累而持续退化——触及了
    Agent 从 Demo 走向生产部署的根本障碍。四种老化机制（压缩/干扰/修订/维护）的框架和时序依赖图+反事实探针的诊断方法论，有望成为 Agent 可靠性工程的标准词汇和工具范式。随着
    Agent 部署规模在未来 2-3 年指数增长，'Agent 老化检测与修复'将从学术概念演变为生产刚需，早期布局该方向的基础设施公司可积累显著的诊断数据和修复策略飞轮。扣分在于：当前仅为学术基准论文，尚无产品化路径和商业验证，复利效应的启动取决于工业界采纳速度。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- LangChain/LangSmith
- Arize AI
- Weights & Biases
- Anthropic
- OpenAI
- Agent 可观测性平台
- 记忆基础设施供应商（Mem0、Pinecone、Chroma）
competitive_casualty:
- 仅依赖一次性评测的 Agent 评测创业公司
- 未考虑老化问题的传统 RPA 厂商
- 缺乏持续可靠性监控的轻量级 Agent 框架
market_opportunities:
- 可基于 AgingBench 的四种老化机制（压缩老化、干扰老化、修订老化、维护老化）开发 Agent 生命周期监控与诊断 SaaS 工具，面向已将 AI Agent
  部署到生产环境的企业提供纵向可靠性评分和阶段定向修复建议
- 针对记忆管道（写入、检索、利用）三个阶段的诊断画像方法，可封装为开源测试框架或 MLOps 平台的 Agent 可靠性插件，填补当前 CI/CD 流程中缺少 Agent
  持续健康检查的空白
- AI 工程师和架构师可将 Agent 生命周期工程作为新的技能方向，掌握时序依赖图、反事实探针等诊断方法，成为企业 Agent 运维（AgentOps）岗位的核心竞争力
risk_matrix:
  regulatory: 欧盟 AI Act 等法规对高风险 AI 系统的可靠性有持续性要求，Agent 部署后随时间退化可能导致合规风险，尤其在金融、医疗等受监管行业，Agent
    老化引发的错误决策可能触发法律责任
  technological: 当前主流 Agent 评测体系（如 SWE-bench、GAIA）均基于一次性快照测试，无法检测部署后的渐进式退化，依赖这些基准选型的
    Agent 可能在线上出现未被预见的故障，形成系统性技术债
  competitive: 率先建立 Agent 生命周期评测能力的平台（如 LangSmith、Arize、Weights & Biases）可能通过内置 AgingBench
    类功能形成差异化壁垒，后来者将面临生态锁定风险
  ethical: Agent 在长期运行中因记忆压缩和干扰老化产生的隐性偏见放大和事实扭曲，可能在用户无感知的情况下造成歧视性决策或错误信息传播，且行为测试无法触发告警
  additional:
  - 运维成本风险：Agent 老化问题意味着部署后的 Agent 系统需要持续的诊断和修复投入，企业可能低估 Agent 全生命周期的总拥有成本（TCO），导致预算超支或项目被迫终止
confidence:
  impact: medium
  compound: high
  hype: low
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: AgingBench
  canonical_name: AgingBench
  url: https://arxiv.org/abs/2605.26302
  positioning: AgingBench 是针对已部署AI代理的纵向可靠性基准，通过四种老化机制分类和记忆管道诊断，衡量退化形式并指导针对性修复。
  technical_signal: 提出了压缩老化、干扰老化、修订老化和维护老化四种机制分类，并使用时间依赖图和配对反事实探针诊断记忆管道故障。
  adoption_signal: 在7个场景、14个模型、多种记忆策略下完成约400次实验，覆盖runner控制和自主代理两种类型，横跨8到200个会话周期。
  ecosystem_relevance: 填补了AI代理从原型到生产部署过程中长期可靠性评估的工具空白，与记忆系统、代理框架和运维监控形成互补生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 长期部署的AI代理面临运行时可靠性退化问题，但业界缺乏系统化评测工具；AgingBench提出的四种老化机制和诊断方法为代理运维提供了可操作的分析框架，随着代理从演示走向生产部署，其价值将持续增长。
  risk_notes:
  - 该基准目前仅以论文形式存在，尚未提供开源实现或公开数据集，可复现性待验证。
  - 约400次实验的覆盖范围在统计泛化能力上仍有局限，需要更大规模的跨任务验证。
  - 代理老化的根本原因是否仅限于论文分类的四种机制，在实践中可能存在更多未识别老化模式。
  score: 8.0
  article_ids:
  - 27fbaeab8c07a7da
  evidence_snippets:
  - 论文介绍了 AgingBench，一个用于代理生命周期工程的纵向可靠性基准，不仅衡量退化程度还诊断退化形式。
  - AgingBench 将代理老化组织为四种机制：压缩老化、干扰老化、修订老化和维护老化。
  - 在 7 个场景、14 个模型和多种记忆策略下的约 400 次实验说明代理老化是多维的，需要机制级别诊断和针对性修复。
---

# Computer Science > Artificial Intelligence

# Title:Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems

View PDF HTML (experimental)Abstract:Long-lived AI agents are increasingly deployed as persistent operational systems, yet they are still evaluated like freshly initialized models. Day-one benchmarks miss a basic systems question: how long does an agent remain reliable after deployment? Even when model weights are frozen, an agent's effective state keeps changing as it compresses interaction history, retrieves from a growing memory store, revises facts after updates, and undergoes routine maintenance. Reliability therefore becomes a lifespan property of the full agent harness, not only a snapshot property of the base model. We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan engineering: measuring not only whether deployed agents degrade, but what form the degradation takes and where repair should target. AgingBench organizes agent aging into four mechanisms: compression aging, interference aging, revision aging, and maintenance aging. To diagnose these failures, AgingBench uses temporal dependency graphs and paired counterfactual probes that produce diagnostic profiles for the write, retrieval, and utilization stages of the memory pipeline. Across 7 scenarios, 14 models, multiple memory policies, and both runner-controlled and autonomous agents, over ~400 runs spanning 8 - 200 sessions show that agent aging is not one-dimensional: behavioral tests can remain clean while factual precision decays; derived-state tracking can collapse sharply within a single model; and the same wrong answer can require different repairs depending on what the diagnostic profile points to. These results suggest that reliable agent deployment requires lifespan evaluation, mechanism-level diagnosis, and stage-targeted repair, not only stronger day-one models.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.