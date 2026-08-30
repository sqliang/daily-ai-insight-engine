---
title: 'Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents'
source: https://arxiv.org/abs/2608.13574
author:
- '[[Bo Jin, Qiang Jiao, Xin Tong]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: 'arXiv:2608.13574v1 Announce Type: new Abstract: LLM agents increasingly
  operate as execution systems that invoke tools, modify local state, use persistent
  memory, and interact with external protocols. These capabilities make agents useful,
  but they also introduce risks related to over-privileged actions, weak auditability,
  prompt injection, tool poisoning, and uncontrolled side effects. This paper presents
  Agentao, a governed local-first runtime for tool-using LLM agents. Agentao separates
  model-generated action proposals from host-authorized execution through a layered
  architecture consisting of host-facing surfaces, a host contract, a runtime core,
  a permission-mediated tool system, and supporting subsystems for memory, replay,
  plugins, skills, sub-agents, and protocol integration. We describe the motivation,
  threat model, design goals, governance model, execution pipeline, and structured
  event interface of the system. Agentao does not provide formal safety guarantees;
  rather, it demonstrates how permissions, state, protocol boundaries, and execution
  traces can be made explicit runtime abstractions for building agents that are more
  governable, inspectable, and suitable for host-controlled local environments. The
  code is publicly available at https://github.com/jin-bo/agentao.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cedf57bb6ac50ed2
source_type: academic_paper
tldr: Agentao 是一个面向工具调用型 LLM 智能体的本地优先受治理运行时。它通过分层架构将模型生成的动作提案与主机授权的执行相分离，把权限、状态、协议边界和执行轨迹作为显式运行时抽象，论文代码已公开。
objective_summary: 论文提出 Agentao，一个面向工具调用型 LLM 智能体的本地优先受治理运行时。针对智能体执行带来的过度授权、弱可审计性、提示注入、工具投毒和失控副作用等风险，系统采用分层架构将模型生成的动作提案与主机授权的执行分离。该架构包含主机表面、主机契约、运行时核心、权限中介工具系统，以及内存、回放、插件、技能、子智能体和协议集成等支撑子系统。Agentao
  不提供正式安全保证，而是将权限、状态、协议边界和执行轨迹作为显式运行时抽象，目标是构建更可治理、可检查、适合主机控制本地环境的智能体，代码已公开。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM Agents
  - Prompt Injection
  - Tool Poisoning
  key_people: []
key_logic_flow:
- 论文指出 LLM 智能体作为执行系统会调用工具、修改本地状态、使用持久内存并与外部协议交互，由此带来过度授权、弱可审计性、提示注入、工具投毒和失控副作用等风险。
- Agentao 的核心设计是将模型生成的动作提案与主机授权的执行相分离，通过分层架构实现治理与控制。
- 该分层架构由主机表面、主机契约、运行时核心、权限中介工具系统以及内存、回放、插件、技能、子智能体和协议集成等支撑子系统组成。
- Agentao 明确不提供正式的安全保证，其思路是把权限、状态、协议边界和执行轨迹做成显式运行时抽象。
- 系统目标是构建更可治理、可检查、适合主机控制本地环境的智能体，论文代码已公开提供。
object_mentions:
- object_type: project
  name: Agentao
  canonical_name: Agentao
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Agentao 是一个面向工具调用型 LLM 智能体的本地优先受治理运行时，将模型生成的动作提案与主机授权的执行分离。
  - 系统采用分层架构，包含主机表面、主机契约、运行时核心、权限中介工具系统及内存、回放、插件、技能、子智能体和协议集成等子系统。
  - Agentao 不提供正式安全保证，而是将权限、状态、协议边界和执行轨迹作为显式运行时抽象，论文代码已公开。
  article_id: cedf57bb6ac50ed2
extract_result: success
impact_score:
  score: 5.0
  reason: 首先判断定位：这是 arXiv 学术论文而非商业产品发布，属智能体安全/治理这一持续升温但尚未定型的细分领域。其次评估创新度：该论文的亮点在于把权限、状态、协议边界和执行轨迹系统化为显式运行时抽象，并采用'模型提案与主机授权执行分离'的分层架构，且代码开源，对智能体基础设施方向有参考价值。但论文明确声明不提供正式安全保证，摘要中未展示实验评估、基准对比或规模化验证，属于设计论文而非可量化的范式突破。综合判断：短期内会被智能体框架与安全社区关注和借鉴，但不会改变行业竞争格局，故评分落在中位区间。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: 治理抽象是否真能抵御提示注入与工具投毒，且论文明确缺少正式安全保证
hype_assessment:
  level: low
  reason: 检查全文措辞：摘要开篇即克制地声明'不提供正式安全保证'，通篇未出现'颠覆''革命性'等 PR 滥用词汇，威胁模型、设计目标与架构组成均为务实描述，还主动披露了自身局限，属于实打实的技术设计论文而非概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 将模型生成的动作提案与主机授权的执行解耦，构建主机表面、主机契约、运行时核心、权限中介工具系统及内存/回放/插件/技能/子智能体等支撑子系统的分层治理架构，把权限、状态、协议边界与执行轨迹提升为显式运行时抽象，为本地优先智能体的可治理、可检查执行提供了系统性参考设计，但属工程架构整合而非底层原理突破。
  business_model: 本地优先+强审计的治理模型契合企业对 AI 代理合规与安全管控的诉求，有望推动企业级私有化/本地化智能体部署的落地；但当前仅为开源原型，距离商业产品与平台生态尚远，暂无直接商业模式重塑力。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: Agent 安全治理是 LLM Agent 从 Demo 走向生产化进程中的必答题，赛道本身具备长期复利价值：随着企业级 Agent 大规模部署，最小权限授权、可审计执行轨迹、提示注入与工具投毒防护将演变为
    Agent 基础设施的默认能力，3-5 年后治理运行时大概率成为行业基座之一。但 Agentao 当前仅是单篇 arXiv 论文，处于 0→1 验证期：无商业实体背书、无生态采用证据、明确不提供正式安全保证，本质是'治理模式参考实现'而非可直接商业化的基础设施。相比已获
    Anthropic 推动并形成事实标准的 MCP 协议，Agentao 缺少巨头推手与网络效应，其复利效应高度不确定，核心观察点是能否被 LangChain/CrewAI/AutoGen
    等主流框架采纳为治理层参考，或演进为开源标准。故给 5.5 分：赛道值 8 分，项目本身需持续验证。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- LangChain
- LlamaIndex
- Microsoft Azure AI
- Anthropic
- 开源 Agent 开发者社区
competitive_casualty:
- 传统 RPA 厂商
- 无安全治理能力的简易 Agent 框架
- 闭源 Agent 安全初创公司
market_opportunities:
- 智能体安全治理正成为刚需，可基于 Agentao 的权限中介与执行轨迹抽象，开发面向企业私有化部署的 AI Agent 审计治理平台
- 本地优先的受治理运行时契合金融、医疗、政企等数据敏感行业的合规诉求，可包装为'模型建议、主机授权'的智能体执行底座并落地私有化方案
- 执行回放（replay）与结构化事件接口可产品化为 Agent 安全运营（SecOps）工具链，满足可追溯、可复现的合规审计与事故调查需求
risk_matrix:
  regulatory: 欧盟 AI Act 等监管要求智能体具备可审计性与人工授权机制，与该方向天然契合；但运行时若演变为关键基础设施，可能被纳入安全认证与责任框架，需持续关注开源许可条款与出口管制变化
  technological: 论文明确不提供正式安全保证；云厂商与模型公司自带的 Agent 沙箱、容器隔离及模型原生安全能力可能快速替代此类独立运行时，其分层架构抽象存在过时风险
  competitive: OpenAI、Anthropic、微软等头部厂商正将治理能力内建到 Agent 平台与 API，企业安全厂商也在入场，独立开源框架面临生态挤压与商业化空间收窄的双重压力
  ethical: 提示注入、工具投毒与失控副作用仍是根本性安全难题，该框架只做到'可治理'而非'保证安全'；在涉及个人数据与本地状态的场景中，授权后的自动化动作仍可能放大误判、偏见与数据滥用风险
  additional:
  - 开源项目依赖社区与作者维护，缺乏商业支撑时长期演进存在不确定性
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Agentao
  canonical_name: Agentao
  url: https://arxiv.org/abs/2608.13574
  positioning: 面向工具调用型 LLM 智能体的本地优先受治理运行时，通过分层架构分离模型动作提案与主机授权执行，构建可治理、可检查、适合主机控制本地环境的智能体执行基础设施。
  technical_signal: 采用分层架构将模型生成的动作提案与主机授权的执行分离，把权限、状态、协议边界和执行轨迹建模为显式运行时抽象，并支撑内存、回放、插件、技能与子智能体等子系统。
  adoption_signal: 论文代码已公开提供，但项目仍处于研究提出阶段，尚未见到社区实际采用或第三方框架集成的公开案例。
  ecosystem_relevance: 直接回应 LLM 智能体过度授权、弱可审计性、提示注入与工具投毒等治理热点，可作为现有智能体框架补足权限与审计能力时的参考方案。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Agentao 将权限、协议边界与执行轨迹作为显式运行时抽象，直击 LLM 智能体执行安全的核心治理痛点，其分层架构与开源代码对智能体安全方向的工程实践具有持续参考价值。
  risk_notes:
  - 论文明确不提供正式安全保证，治理模型属于工程实践层面的约束，而非经过形式化验证的安全保障。
  - 项目尚处于论文研究阶段，缺乏社区采用数据与第三方集成案例，实际成熟度与稳定性有待验证。
  - 本地优先的设计定位可能限制其在云端或多租户生产环境中的部署适用性。
  score: 7.0
  article_ids:
  - cedf57bb6ac50ed2
  evidence_snippets:
  - Agentao 是一个面向工具调用型 LLM 智能体的本地优先受治理运行时，将模型生成的动作提案与主机授权的执行分离。
  - 系统采用分层架构，包含主机表面、主机契约、运行时核心、权限中介工具系统及内存、回放、插件、技能、子智能体和协议集成等子系统。
  - Agentao 不提供正式安全保证，而是将权限、状态、协议边界和执行轨迹作为显式运行时抽象，论文代码已公开。
---

# Computer Science > Artificial Intelligence

# Title:Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents

View PDF HTML (experimental)Abstract:LLM agents increasingly operate as execution systems that invoke tools, modify local state, use persistent memory, and interact with external protocols. These capabilities make agents useful, but they also introduce risks related to over-privileged actions, weak auditability, prompt injection, tool poisoning, and uncontrolled side effects. This paper presents Agentao, a governed local-first runtime for tool-using LLM agents. Agentao separates model-generated action proposals from host-authorized execution through a layered architecture consisting of host-facing surfaces, a host contract, a runtime core, a permission-mediated tool system, and supporting subsystems for memory, replay, plugins, skills, sub-agents, and protocol integration. We describe the motivation, threat model, design goals, governance model, execution pipeline, and structured event interface of the system. Agentao does not provide formal safety guarantees; rather, it demonstrates how permissions, state, protocol boundaries, and execution traces can be made explicit runtime abstractions for building agents that are more governable, inspectable, and suitable for host-controlled local environments. The code is publicly available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.