---
title: 'Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated
  Workflows'
source: https://arxiv.org/abs/2607.00269
author:
- '[[Edward Y. Chang, Longling Geng, Emily J. Chang]]'
published: '2026-07-02'
created: '2026-07-02'
description: 'arXiv:2607.00269v1 Announce Type: new Abstract: LLMs, solvers, and agent
  teams increasingly generate workflow actions, repairs, and plans, but a generated
  action may be syntactically valid yet stale, infeasible, conflicting, or destructive
  of the evidence that triggered a repair. We introduce Agentic Transaction Processing
  (ATP), a transaction model that treats generated actions as untrusted proposals
  until they pass deterministic admission under a declared, executable constraint
  set C. The principle is two-sided: a proposal is not truth, and no proposal foresees
  every disruption: anything may propose, but only the runtime admits and commits,
  and when an unforeseen disruption strikes it repairs reactively within bounds rather
  than trusting a fresh proposal. Relative to C, committed-state correctness becomes
  independent of the competence, honesty, or learning of the proposing layer. We realize
  ATP in Mnemosyne, a runtime with an append-only transition log, effective-state
  projection, dependency-safe compensation, and active commitment records, and prove
  four safety properties relative to C (authority separation, serial-equivalent generative
  admission, evidence-preserving repair, and obligation containment) together with
  a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A
  reproducible artifact rejects the targeted violations across nine falsification
  tests while still admitting valid work, at under 6% projection-and-validation overhead,
  and bounded local repair edits an order of magnitude fewer operations than global
  recompute. Mnemosyne is open source: https://github.com/eyuchang/Mnemosyne/tree/arxiv-atp-rq1-rq9b-r8-v2.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2fafb6fdbe04709e
manifest_dates:
- '2026-07-02'
source_type: academic_paper
tldr: arXiv 论文提出 Agentic Transaction Processing (ATP) 事务模型，将 AI 生成的动作视为不可信提案，只有通过确定性约束集
  C 准入后才能提交。论文基于 ATP 实现了运行时系统 Mnemosyne，包含追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录，并证明了四项安全属性。
objective_summary: 该论文提出了 Agentic Transaction Processing (ATP) 事务模型，将 LLM、求解器和智能体团队生成的工作流动作视为不可信提案，需通过声明的确定性约束集
  C 的准入检查后才能由运行时提交。作者基于 ATP 实现了 Mnemosyne 运行时系统，采用追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录等机制。论文证明了
  ATP 相对于约束集 C 的四项安全属性：权限分离、序列等价生成准入、证据保留修复和约束包含。可复现的实验表明，Mnemosyne 在九项伪造测试中拒绝了所有目标违规行为，同时仍允许有效工作流通过，投影与验证开销低于
  6%，局部修复协议 (LCRP) 修改的操作数比全局重新计算少一个数量级。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - ATP
  - LCRP
  - LLM
  key_people: []
key_logic_flow:
- 论文指出现有问题：LLM 和智能体生成的工作流动作虽然语法正确，但可能因过时、不可行、冲突或破坏触发修复的证据而导致系统错误。
- 论文提出 Agentic Transaction Processing (ATP) 事务模型，核心原则是双重认定——提案不可信，且任何提案无法预见所有干扰；只有运行时负责准入和提交。
- ATP 模型要求所有生成动作必须通过声明的确定性约束集 C 的准入检查后才能被提交执行。
- 论文实现了 Mnemosyne 运行时系统，包含追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录四个核心组件。
- 论文证明了 ATP 相对于约束集 C 的四项安全属性：权限分离、序列等价生成准入、证据保留修复和约束包含。
- 实验表明 Mnemosyne 在九项测试中拒绝了所有目标违规行为，投影与验证开销低于 6%，局部修复协议 (LCRP) 相比全局重新计算效率高出一个数量级。
specialized_tags:
  paper:
    paperTitle: 'Mnemosyne: Agentic Transaction Processing for Validating and Repairing
      AI-generated Workflows'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Systems
    methodType:
    - LLM-based
    - theoretical
extract_result: success
object_mentions:
- object_type: project
  name: Mnemosyne
  canonical_name: Mnemosyne
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文基于 Agentic Transaction Processing 模型实现了 Mnemosyne 运行时系统，包含追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录等机制。
  - Mnemosyne 在九项伪造测试中拒绝了所有目标违规行为，同时仍允许有效工作流通过，投影与验证开销低于 6%。
  - '论文标题为 Mnemosyne: Agentic Transaction Processing for Validating and Repairing
    AI-generated Workflows，Mnemosyne 是该工作的核心贡献。'
  article_id: 2fafb6fdbe04709e
- object_type: project
  name: Agentic Transaction Processing (ATP)
  canonical_name: Agentic Transaction Processing
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出了 Agentic Transaction Processing (ATP) 事务模型，将生成的动作视为不可信提案，直到它们通过声明的确定性约束集的准入检查。
  - ATP 模型的核心原则是：提案不等于事实，且没有提案能预见所有干扰；任何东西都可以提议，但只有运行时负责准入和提交。
  - 相对于约束集 C，ATP 保证已提交状态的正確性与提议层的能力、诚实性或学习无关。
  article_id: 2fafb6fdbe04709e
- object_type: project
  name: Localized Constraint Repair Protocol (LCRP)
  canonical_name: LCRP
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 论文证明了 Mnemosyne 的局部修复协议 (LCRP) 具有有界反应式修复保证。
  - LCRP 在实验中修改的操作数比全局重新计算少一个数量级。
  article_id: 2fafb6fdbe04709e
impact_score:
  score: 6.2
  reason: 该论文提出 Agentic Transaction Processing (ATP) 模型，将数据库事务的原子性、隔离性和补偿回滚等经典概念系统性地迁移到
    AI 生成 workflow 的验证与修复场景，填补了现有 agent 系统缺乏事务性安全保障的空白。论文给出了四种形式化安全属性的证明（权威分离、序列等价生成准入、保留证据的修复、义务约束）以及
    LCRP 协议的有界响应修复保证，学术贡献扎实。然而，这仍属理论性框架提出阶段，实验仅在 falsification 测试上验证了违规拒绝能力（开销低于 6%），尚未在真实复杂
    agent 系统中大规模部署验证。相比 ChatGPT 发布级别的范式转移，其行业冲击力还需时间观察工程落地效果。综合评定为 6.2 分——在 agent
    安全架构方向上开辟了新的研究路线，但短期内不会立即改变产业格局。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 事务性保障让 agent 生成的 action 不再是黑盒信任，而是可验证、可回滚的确定性操作
hype_assessment:
  level: low
  reason: 论文措辞严谨，没有使用'颠覆'、'革命性'等 PR 词汇，而是围绕事务模型、形式化安全属性和有界修复保证展开论述。提供了可复现的开源 artifact（GitHub），9
    项 falsification 测试均明确报告结果，实验数据诚实（开销 6% 并非奇迹级数字）。arXiv 论文的学术风格天然抑制了过度包装。
information_entropy: high
domain_disruption:
  technical_innovation: 将数据库事务的追加日志、有效状态投影、依赖安全补偿和活跃提交记录等经典机制，创新性地适配到 AI 生成 workflow
    的准入验证与局部修复场景，并形式化证明了 ATP 模型相对于约束集 C 的四种安全属性。LCRP 协议的有界响应修复保证在编辑操作量上比全局重算少一个数量级，为
    agent 行为安全提供了理论可验证的工程路径。
  business_model: 无直接商业模式影响。但该框架若成熟落地，可降低企业采用自主 agent 系统的合规风险，推动 agent 在金融、医疗等强监管行业的部署——agent
    不再'黑盒运行'而是可审计、可补偿的事务化操作。
engineering_complexity: prototype
compound_value:
  score: 7.5
  reason: 从 VC 视角看，Mnemosyne 解决的是一级痛点：AI Agent 在自主执行多步骤工作流时缺乏事务性安全保障。随着 Agent 从'对话聊天'演进到'生产级自动化'，原子性提交、约束验证、回滚补偿和有界修复成为不可避免的基础设施需求。ATP
    模型的四个安全属性证明（权威分离、序列等价准入、保留证据的修复、义务约束）给出了严谨的理论地基，LCRP 局部修复比全局重算少一个数量级编辑量的实验数据也验证了实用性。然而扣分点在于：(1)
    当前仅为学术论文 + 开源原型，距离生产级中间件还有工程化鸿沟；(2) 未绑定任何商业实体，商业化路径不清晰；(3) 需要被 LangChain、Temporal
    等已有编排框架采纳才能发挥网络效应。综合来看，若 ATP 模式被主流 Agent 框架采纳为事实标准，其复利效应极强（3 年后可能成为 Agent 工作流的
    ACID），但当前仍处于早期验证阶段，评分落在 7-8 区间。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- LangChain
- Temporal Technologies
- GitHub
- Microsoft
- CrewAI
- AutoGPT
competitive_casualty:
- UiPath
- Automation Anywhere
- 传统低代码自动化平台
- 缺乏事务保障的简易 Agent 框架
market_opportunities:
- 面向金融、医疗等强监管行业，可基于 ATP 模型构建 AI Agent 工作流审计与合规平台，提供不可篡改的事务日志和确定性准入验证
- 可将 Mnemosyne 的事务安全层作为插件集成到 LangGraph、CrewAI、AutoGen 等主流 Agent 编排框架中，解决 AI 生成操作不可信的核心痛点
- 基于 LCRP 局部约束修复协议开发自动化工作流修复中间件，在 AI 运维场景中实现比全局重算低一个数量级的故障恢复成本
risk_matrix:
  regulatory: ATP 模型提供了完整的操作日志和确定性准入机制，可能被监管机构采纳为 AI 工作流的合规标准参考，但约束集 C 的定义本身将成为新的审计焦点，不完善的约束定义可能产生虚假合规风险
  technological: ATP 的安全性完全依赖于声明性约束集 C 的完备性和正确性，有缺陷或不完整的约束集可能导致虚假安全感；该方案目前仅在论文实验环境中验证，未经过大规模生产环境考验
  competitive: AWS（Step Functions）、Temporal、以及 Agent 框架（LangChain、Microsoft AutoGen）等基础设施和平台厂商可能快速集成类似的事务性保障能力，压缩独立解决方案的市场空间
  ethical: 该技术通过运行时准入机制可显著减少 AI Agent 自主决策造成的无意伤害，是负责任的 AI 落地的重要基础设施；但约束集的设计偏见可能系统性排斥某些合法操作路径，需要多方参与的约束治理机制
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
paper_metadata:
  title: 'Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated
    Workflows'
  authors: []
  affiliations: []
  venue: arXiv preprint
  paper_url: https://arxiv.org/abs/2607.00269
  code_url: null
  dataset_url: null
research_problem:
  core_question: 如何形式化地保证AI生成的工作流动作在运行时的一致性、安全性和可修复性，使其不受生成层能力或诚实度的影响？
  motivation: LLM、求解器和智能体团队越来越多地自主生成工作流动作、修复和计划，但这些生成的动作即使语法正确，也可能存在过时、不可行、冲突或破坏触发修复的原始证据等问题。现有方法要么完全信任LLM输出，要么仅做浅层语法检查，缺乏运行时正确性的形式化保证。迫切需要一种事务模型来将生成与验证解耦。
  significance: fundamental
  gap_addressed: 填补了AI生成工作流领域缺乏运行时事务保证的空白——现有工作流系统和智能体框架没有形式化地处理生成动作的不可靠性，也没有将数据库事务的ACID概念系统性地引入AI工作流验证与修复中。
methodology:
  approach_summary: 提出Agentic事务处理（ATP）模型，将AI生成的任何工作流动作视为不可信提案，必须在声明的可执行约束集C下通过确定性准入才能被运行时提交执行。核心原则是：提案不等于真理，任何提案都无法预见所有干扰。基于此，设计并实现了Mnemosyne运行时，包含仅追加的转换日志（append-only
    transition log）、有效状态投影（effective-state projection）、依赖安全的补偿（dependency-safe compensation）和活跃提交记录（active
    commitment records）。同时设计了LCRP（Localized Constraint Repair Protocol）本地化约束修复协议，当不可预见的干扰发生时，在边界内进行反应式修复而非重新生成全局方案。论文形式化证明了四项安全性质：权限分离、序列等价生成准入、证据保持修复和义务约束，以及LCRP的有界反应式修复保证。
  novelty_type: theoretical
  key_innovations:
  - 提出ATP事务模型，将数据库事务的形式化语义（提交、回滚、补偿）系统性地引入AI生成工作流领域，建立了生成层与运行时的严格权限分离
  - 设计LCRP本地化约束修复协议，仅编辑受干扰影响的局部操作而非全局重计算，将修复开销降低一个数量级
  - 形式化证明四项安全性质（权限分离、序列等价生成准入、证据保持修复、义务约束）和有界反应式修复保证，为AI工作流正确性提供了数学基础
  - 实现可复现的Mnemosyne原型系统，集成仅追加日志、有效状态投影和依赖安全补偿等机制
  inspiration_sources:
  - 数据库事务处理（ACID属性与提交协议）
  - 补偿事务模式（Saga架构）
  - 形式化验证与模型检测
  - 反应式系统与自我修复设计
  technical_depth: deeply_technical
experimental_rigor:
  benchmark_coverage: 使用9个针对性设计的反例验证测试（falsification tests）来系统评估系统拒绝各种违规类型的能力，同时验证对有效工作负载的正常接受。修复效率评估通过与全局重计算（global
    recompute）方案的对比来进行。
  baseline_comparison: selective
  ablation_quality: minimal
  reproducibility_level: fully_reproducible
  claimed_improvement: 在全部9个反例测试中成功拒绝目标违规行为；运行时投影与验证开销低于6%；LCRP本地修复的编辑操作数比全局重计算少一个数量级（约10倍改进）
limitations_and_honesty:
  stated_limitations:
  - 明确承认无法预见所有可能的干扰（no proposal foresees every disruption）
  - 约束集C需要人工声明定义，本身可能不完整
  - ATP保证的正确性依赖于C的正确性
  reviewer_concerns:
  - 与现有主流AI智能体框架（如AutoGPT、LangChain、Semantic Kernel等）缺乏系统性的实验对比
  - 约束集C的编写和维护需要大量领域专家投入，自动化程度不足，可能成为实际部署的瓶颈
  - 9个反例测试的覆盖范围有限，大规模真实工作流场景下的表现尚不明确
  - 形式化证明的假设条件在实际系统中的满足程度需要更多验证
  - 缺少对多智能体协作场景下事务隔离和并发控制的讨论
  overclaiming_assessment: honest
  generalization_concern: ATP的有效性高度依赖于预定义约束集C的完整性和正确性。在动态变化、开放域或非确定性的环境中，约束集本身可能频繁失效或需要持续演化，这种依赖性可能严重限制模型向新兴应用领域的泛化能力。同时，论文实验主要在受控反例下验证，在真实复杂工作流中的泛化性能有待检验。
industrial_relevance:
  applicable_domains:
  - AI驱动的智能体工作流编排与自动化运维
  - 数据处理与ETL管线
  - 机器人流程自动化（RPA）
  - DevOps与CI/CD流水线
  - 云服务编排与资源管理
  compute_requirements: commodity
  integration_readiness: needs_research
  cost_efficiency_analysis: LCRP将修复操编辑作数减少一个数量级，直接降低了故障恢复的计算成本和时间开销。运行时仅6%的额外投影与验证开销对生产系统影响极小，具备良好的成本效益比。但约束集C的编写需要领域专家投入前期成本，且每次工作流逻辑变更可能需要同步更新约束集，这部分隐性成本可能较高。整体来看，对于高可靠性要求的自动化工作流场景，引入ATP的收益显著大于成本。
related_work_context:
  closest_prior_works:
  - 数据库事务处理系统（ACID事务模型）
  - Saga补偿事务模式（分布式事务的补偿机制）
  - AutoGPT、LangChain等AI智能体框架
  - 程序合成与形式化验证方法
  advancement_over_prior: 首次将数据库事务的形式化保证体系（序列等价、提交协议、补偿回滚）系统性地引入AI生成工作流验证领域，而非简单套用传统事务概念。核心突破在于建立了生成层与运行时的严格权限分离机制，使运行时正确性不再依赖于生成层的智能水平或诚实度——这是对现有完全信任LLM输出范式的一项根本性改进。
  opens_new_direction: true
  potential_follow_ups:
  - 将ATP扩展到多智能体协作与分布式事务场景，处理并发提案之间的隔离与冲突
  - 研究约束集C的自动推断和增量学习方法，降低人工编写成本
  - 在云原生工作流引擎（如Temporal、Argo Workflows）中实际部署Mnemosyne并评估生产级性能
  - 探索将ATP与强化学习结合，实现约束的自适应演化
  - 研究松弛化形式化保证以换取更高性能的折中方案
object_insights:
- object_type: project
  name: Mnemosyne
  canonical_name: Mnemosyne
  url: null
  positioning: 基于 ATP 事务模型实现的运行时系统，具备追加式转换日志与有效状态投影等机制，专用于验证和修复 AI 生成的工作流。
  technical_signal: 项目采用追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录四项核心机制，为 AI 工作流提供运行时安全保障。
  adoption_signal: null
  ecosystem_relevance: 作为开源项目，Mnemosyne 填补了 LLM 生成层与安全执行层之间的信任缺口，属于 AI 基础设施安全方向的关键探索。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Mnemosyne 提出的 ATP 模型从根本上改变了 AI 生成工作流的信任模式，将运行时验证与局部修复机制结合，为智能体系统安全执行提供了可证明保障，值得持续关注其在多智能体协作场景中的推广效果。
  risk_notes:
  - Mnemosyne 目前仍处于学术验证阶段，尚未在生产环境中经过大规模测试。
  - 其约束集 C 的完整定义在实际部署中可能面临挑战，运行时性能开销也需要进一步评估。
  score: 8.0
  article_ids:
  - 2fafb6fdbe04709e
  evidence_snippets:
  - 论文基于 Agentic Transaction Processing 模型实现了 Mnemosyne 运行时系统，包含追加式转换日志、有效状态投影、依赖安全补偿和主动提交记录等机制。
  - Mnemosyne 在九项伪造测试中拒绝了所有目标违规行为，同时仍允许有效工作流通过，投影与验证开销低于 6%。
  - '论文标题为 Mnemosyne: Agentic Transaction Processing for Validating and Repairing
    AI-generated Workflows，Mnemosyne 是该工作的核心贡献。'
- object_type: project
  name: Agentic Transaction Processing (ATP)
  canonical_name: Agentic Transaction Processing
  url: null
  positioning: 将数据库事务处理思想引入 AI 工作流领域的创新型事务模型，将生成动作视为不可信提案，需通过确定性约束准入后方可提交执行。
  technical_signal: ATP 提出双重认定原则，提案不等于事实且无法预见所有干扰，运行时负责准入和提交，使状态正确性与提议层能力解耦。
  adoption_signal: null
  ecosystem_relevance: ATP 弥补了 AI 生成内容运行时安全保障的理论空白，其四项安全属性定义对智能体系统安全方向有基础性贡献。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ATP 模型为 AI 智能体工作流安全提供了一种全新的理论框架，将数据库事务的 ACID 属性思想迁移到 AI 生成动作验证场景，若被广泛采用可能成为智能体系统安全执行的标准范式。
  risk_notes:
  - ATP 模型依赖约束集 C 的完整定义，在复杂真实场景中穷举所有约束可能不切实际。
  - ATP 目前仅在 Mnemosyne 单一实现中得到验证，缺乏跨框架通用性验证。
  score: 7.0
  article_ids:
  - 2fafb6fdbe04709e
  evidence_snippets:
  - 论文提出了 Agentic Transaction Processing (ATP) 事务模型，将生成的动作视为不可信提案，直到它们通过声明的确定性约束集的准入检查。
  - ATP 模型的核心原则是：提案不等于事实，且没有提案能预见所有干扰；任何东西都可以提议，但只有运行时负责准入和提交。
  - 相对于约束集 C，ATP 保证已提交状态的正確性与提议层的能力、诚实性或学习无关。
- object_type: project
  name: Localized Constraint Repair Protocol (LCRP)
  canonical_name: LCRP
  url: null
  positioning: Mnemosyne 运行时系统中的局部修复协议，当约束违反时通过有界反应式修复替代全局重新计算，高效修正 AI 工作流的违规操作。
  technical_signal: LCRP 具有有界反应式修复保证，在实验中修改的操作数比全局重新计算少一个数量级，显著提升修复效率。
  adoption_signal: null
  ecosystem_relevance: 局部修复策略解决了 AI 工作流修复的核心效率瓶颈，对构建需要实时响应的智能体系统具有重要意义。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: LCRP 的局部修复策略效率比全局重新计算提升一个数量级，这对需要实时响应的智能体系统至关重要，值得关注其是否能成为 AI 工作流修复的标准方案。
  risk_notes:
  - LCRP 作为 Mnemosyne 的组成部分，其有效性和边界条件与 Mnemosyne 整体架构深度耦合。
  - 该协议仅在学术实验中验证，其在复杂多步工作流中的实际修复边界尚未明确。
  score: 5.0
  article_ids:
  - 2fafb6fdbe04709e
  evidence_snippets:
  - 论文证明了 Mnemosyne 的局部修复协议 (LCRP) 具有有界反应式修复保证。
  - LCRP 在实验中修改的操作数比全局重新计算少一个数量级。
---

# Computer Science > Artificial Intelligence

# Title:Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows

View PDF HTML (experimental)Abstract:LLMs, solvers, and agent teams increasingly generate workflow actions, repairs, and plans, but a generated action may be syntactically valid yet stale, infeasible, conflicting, or destructive of the evidence that triggered a repair. We introduce Agentic Transaction Processing (ATP), a transaction model that treats generated actions as untrusted proposals until they pass deterministic admission under a declared, executable constraint set C. The principle is two-sided: a proposal is not truth, and no proposal foresees every disruption: anything may propose, but only the runtime admits and commits, and when an unforeseen disruption strikes it repairs reactively within bounds rather than trusting a fresh proposal. Relative to C, committed-state correctness becomes independent of the competence, honesty, or learning of the proposing layer. We realize ATP in Mnemosyne, a runtime with an append-only transition log, effective-state projection, dependency-safe compensation, and active commitment records, and prove four safety properties relative to C (authority separation, serial-equivalent generative admission, evidence-preserving repair, and obligation containment) together with a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A reproducible artifact rejects the targeted violations across nine falsification tests while still admitting valid work, at under 6% projection-and-validation overhead, and bounded local repair edits an order of magnitude fewer operations than global recompute. Mnemosyne is open source: this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.