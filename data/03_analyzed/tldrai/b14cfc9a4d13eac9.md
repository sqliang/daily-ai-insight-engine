---
title: Warp Agent Memory (Research Preview) (6 minute read)
source: https://docs.warp.dev/agents/agent-memory/?utm_source=tldrai
author: []
published: ''
created: '2026-08-19'
manifest_dates:
- '2026-08-19'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b14cfc9a4d13eac9
source_type: news_media
tldr: Warp 发布 Agent Memory 研究预览版，这是一套托管在 Warp 平台上的持久化记忆系统，被 Warp Agent、Claude Code、Codex
  等 agent 框架共享，异步读写、不消耗 token，按团队面向设计合作伙伴开放申请。
objective_summary: Warp 推出 Agent Memory 研究预览版，按团队为设计合作伙伴开启，需加入等待列表申请访问。该系统是托管在 Warp
  上的持久化记忆系统，内置 Warp Agent、Claude Code、Codex 等所有受支持的 agent 框架均可读写其中的持久事实、决策与结果。记忆创建与检索均在后台异步运行，不消耗
  token 也不会给当前任务增加延迟。记忆按 store 组织，分为个人、agent、团队三种所有权，新建 agent 默认开启自动记忆。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Warp
  technologies:
  - Agent Memory
  - Claude Code
  - Codex
  key_people: []
key_logic_flow:
- Warp 发布 Agent Memory 研究预览版，按团队为设计合作伙伴开启，用户需加入等待列表申请访问权限。
- Agent Memory 是托管在 Warp 上的持久化记忆系统，被内置 Warp Agent、Claude Code、Codex 等所有受支持的 agent
  框架共享读写。
- 记忆创建与检索均为异步后台运行，不消耗 token 也不会给当前任务增加延迟。
- 对话结束后 Warp 自动提取持久事实、经验与结果写入记忆，新知识会与已有记忆合并或在冲突时覆盖旧记忆。
- 记忆按 store 组织，分为个人、agent、团队三种所有权，同一 store 可挂载到多个 agent 以便团队共享知识。
- 新建 agent 默认开启自动记忆，拥有专属的 agent 记忆 store，从首次运行开始构建长期记忆。
object_mentions:
- object_type: product
  name: Warp Agent Memory
  canonical_name: Warp Agent Memory
  url: https://docs.warp.dev/agents/agent-memory/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Warp 的 Agent Memory 处于研究预览阶段，按团队为设计合作伙伴开启，用户需加入等待列表申请访问权限。
  - Agent Memory 是托管在 Warp 上的持久化记忆系统，可被 Warp Agent、Claude Code、Codex 等所有受支持的 agent
    框架共享读写。
  - 记忆创建与检索均为异步后台运行，不消耗 token 也不会给当前任务增加延迟。
  article_id: b14cfc9a4d13eac9
- object_type: product
  name: Warp Agent
  canonical_name: Warp Agent
  url: https://docs.warp.dev/agents
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 内置的 Warp Agent 运行在 Warp 中，与云 agent 共同使用 Agent Memory，是研究预览期支持读写记忆的框架之一。
  article_id: b14cfc9a4d13eac9
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Claude Code 作为第三方 agent 框架，在作为云 agent 运行时被 Agent Memory 覆盖，本地运行在研究预览期不受支持。
  article_id: b14cfc9a4d13eac9
- object_type: product
  name: Codex
  canonical_name: Codex
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Codex 与 Warp Agent、Claude Code 一同被列为 Agent Memory 支持的 agent 框架，可读写共享的持久记忆。
  article_id: b14cfc9a4d13eac9
extract_result: success
impact_score:
  score: 5.5
  reason: 该事件是 Warp 在 agent 记忆层的关键产品化布局，直击'agent 跨会话失忆'这一普遍痛点，并提出跨 harness（Warp Agent
    / Claude Code / Codex）共享记忆、store 三级所有权与异步非阻塞写入的工程方案，短期内会对 agent 记忆基础设施的局部竞争格局产生实质影响。但当前仅为
    research preview，需 waitlist 申请、仅向设计合作伙伴开放，且第三方 harness 仅支持在 Warp 云端运行、记忆数据绑定 Warp
    平台，显著限制了短期冲击力与落地范围。综合判定为一次重要的产品发布而非范式转移，故给 5.5 分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 记忆数据托管在 Warp 云端、第三方 harness 仅限云端运行的生态锁定与隐私可移植性顾虑
hype_assessment:
  level: medium
  reason: 文章自述为 research preview 且需加入等待列表，措辞相对克制，未滥用'颠覆/革命'类词汇；但'所有受支持的 agent 框架共享记忆'的表述存在包装成分——第三方框架仅在
    Warp 云端运行时才被覆盖，本地 Claude Code / Codex 不在支持范围内，实质是 Warp 平台锁定下的记忆服务，带有一定的概念包装与 PR
    放大。
information_entropy: medium
domain_disruption:
  technical_innovation: 将跨 harness 的持久化记忆抽象为平台级服务：记忆创建与检索均为异步后台运行，不消耗 token 也不为当前任务增加延迟；对话结束后自动抽取持久事实/决策/结果并做合并与冲突覆盖；store
    按个人、agent、团队三级所有权组织，可挂载到多个 agent 实现团队知识共享，并支持按 store 的读写权限与使用指令。本质是记忆层的工程产品化而非算法级突破，亮点在于
    harness 无关的共享模型与可审计、可追溯设计。
  business_model: 推动 Warp 从终端工具向 agent 基础设施平台演进，以'团队共享记忆即服务'切入协作场景，形成记忆存储、自动记忆编排与
    agent 云运行时的商业闭环；同时通过将记忆数据绑定 Warp 云端构筑生态锁定，抢占企业级 agent 协作的知识层入口，为后续团队订阅与平台溢价奠定基础。
engineering_complexity: prototype
compound_value:
  score: 7.0
  reason: 评分逻辑：(1) 记忆是 agent 基础设施中最具复利效应的层——对话结束后自动沉淀持久事实与决策，跨会话、跨 harness、跨团队复用，每一次使用都在累积数据资产与切换成本，天然形成数据飞轮效应；(2)
    异步后台读写、不消耗 token 的设计消除了记忆功能的最大采用障碍（延迟与 token 成本），相比手动维护 CLAUDE.md 或同步调用外部记忆 API
    的方案具备显著的工程体验优势；(3) 但两个约束限制其上限：其一，记忆托管在 Warp 平台，价值捕获与 Warp 终端+云 agent 生态的采用度强绑定，若
    Warp 未能成为主流 agent 运行中心，复利效应会被平台天花板钳制；其二，当前仅研究预览，大规模场景下记忆冲突合并、团队权限边界与隐私治理尚未被验证。综合判断：有潜力成为
    agent 记忆细分赛道的基础设施，但需持续验证 Warp 的采用曲线与规模化管理能力，故给 7.0 分。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Warp
- Anthropic
- OpenAI
competitive_casualty:
- Mem0
- Zep
- Letta
- 传统团队知识库工具（Confluence/Notion AI）
market_opportunities:
- Agent 持久化记忆正在成为独立的基础设施赛道，开发者可关注跨 agent 框架（Claude Code、Codex 等）共享记忆的团队知识库与上下文管理工具的创业机会
- 企业可评估将多个 agent 工具的记忆统一托管到 Warp 的可行性，以降低跨工具、跨成员的上下文切换成本，尤其适合多 agent 协作的研发团队试点
- Warp 的异步记忆写入（不消耗 token、不增加任务延迟）设计思路值得自建 agent 系统的团队借鉴，可作为低成本记忆管理架构的参考范式
risk_matrix:
  regulatory: 记忆数据托管在 Warp 云端，企业专有代码、架构决策等敏感信息可能受数据驻留、GDPR 及 AI Act 的合规约束；跨团队共享记忆的访问审计与数据主权归属需重点评估
  technological: 记忆冲突时新知识直接覆盖旧记忆，自动提取可能固化错误事实；研究预览版稳定性未经验证，且面临模型厂商原生记忆（如 OpenAI、Anthropic
    内置 memory）的架构替代风险
  competitive: OpenAI、Anthropic 等模型厂商与 Mem0、Letta 等记忆创业公司均在此赛道布局，Warp 作为终端厂商切入基础设施层，面临巨头生态挤压与价格竞争压力
  ethical: 自动从对话中提取"持久事实"可能捕获未经明确同意的个人或团队信息，存在隐私侵犯风险；错误记忆经团队共享后会被多 agent 放大传播，且记忆库易遭数据投毒
  additional:
  - 供应商锁定风险：记忆系统与 Warp 平台深度绑定，跨平台迁移成本高，企业需评估对单一供应商的长期依赖
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Warp Agent Memory
  canonical_name: Warp Agent Memory
  url: https://docs.warp.dev/agents/agent-memory/
  positioning: 托管在 Warp 平台上的跨框架持久化记忆系统，供 Warp Agent、Claude Code、Codex 等 agent 框架共享读写，实现跨会话、跨工具的长期记忆。
  technical_signal: 记忆创建与检索均为异步后台运行，不消耗 token 也不给任务增加延迟，并按个人、agent、团队三类 store 组织记忆所有权。
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Warp 及第三方编码 agent 的开发者
  - 需要在团队内共享 agent 记忆的协作团队
  product_signal: 提供自动记忆创建、可共享 store、按 agent 的读写权限与指令、记忆可追溯与可审计等能力，同时覆盖本地 agent 与云
    agent 场景。
  market_signal: 产品处于研究预览阶段，按团队面向设计合作伙伴开放，需加入等待列表申请，反映 agent 记忆层正成为平台级竞争点。
  differentiation: 区别于单框架内记忆方案，它以跨 harness 共享为核心，让 Warp Agent、Claude Code、Codex 等不同框架复用同一份持久知识。
  watch_reason: Warp 将 Agent Memory 定位为跨框架 agent 基础设施层，其异步零 token 设计与团队共享模型若被验证，可能重塑
    agent 记忆方案选型，值得持续跟踪从研究预览到正式开放的过程。
  risk_notes:
  - 产品仍处研究预览阶段，按团队开放且需等待列表申请，实际可用范围与稳定性有限。
  - 第三方框架本地运行在研究预览期不受支持，仅云 agent 运行时被记忆系统覆盖。
  score: 8.0
  article_ids:
  - b14cfc9a4d13eac9
  evidence_snippets:
  - Warp 的 Agent Memory 处于研究预览阶段，按团队为设计合作伙伴开启，用户需加入等待列表申请访问权限。
  - Agent Memory 是托管在 Warp 上的持久化记忆系统，可被 Warp Agent、Claude Code、Codex 等所有受支持的 agent
    框架共享读写。
  - 记忆创建与检索均为异步后台运行，不消耗 token 也不会给当前任务增加延迟。
- object_type: product
  name: Warp Agent
  canonical_name: Warp Agent
  url: https://docs.warp.dev/agents
  positioning: Warp 内置的终端 agent，与研究预览期的 Agent Memory 深度集成，本地与云端运行均可读写共享的持久记忆。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Warp 终端进行 AI 辅助编程的开发者
  product_signal: 作为 Warp 内置 agent，本地与云 agent 形态均可使用 Agent Memory，是研究预览期支持跨会话记忆的首批框架。
  market_signal: null
  differentiation: 相比第三方框架仅云 agent 场景可用，Warp Agent 本地与云端均能读写 Agent Memory，集成度更高。
  watch_reason: Warp Agent 是 Agent Memory 的首批落地载体，其跨会话记忆的实际体验直接决定 Warp 终端对开发者的吸引力，值得持续跟踪其功能演进与采用反馈。
  risk_notes:
  - 作为研究预览组成部分，Warp Agent 的记忆能力尚不稳定，存在功能调整或延迟开放的可能。
  score: 5.0
  article_ids:
  - b14cfc9a4d13eac9
  evidence_snippets:
  - 内置的 Warp Agent 运行在 Warp 中，与云 agent 共同使用 Agent Memory，是研究预览期支持读写记忆的框架之一。
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  positioning: Anthropic 的编程 agent，作为第三方框架在云 agent 运行时接入 Warp 的 Agent Memory，本地运行在研究预览期暂不支持。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Claude Code 且希望通过 Warp 云 agent 获得跨会话记忆的开发者
  product_signal: 作为云 agent 运行时支持读写 Warp 的 Agent Memory，可跨会话复用持久事实与决策，但本地运行暂未覆盖。
  market_signal: null
  differentiation: 被纳入 Warp 跨框架记忆生态，标志着主流编码 agent 间记忆互操作的尝试，但本地运行缺口限制体验完整性。
  watch_reason: Claude Code 作为主流编码 agent 被 Warp 记忆生态纳入，说明跨框架 agent 记忆互操作正成为方向，其接入深度与本地支持进展值得持续跟踪。
  risk_notes:
  - 研究预览期本地运行不受支持，仅云 agent 场景可获得 Agent Memory 覆盖，使用范围受限。
  score: 4.0
  article_ids:
  - b14cfc9a4d13eac9
  evidence_snippets:
  - Claude Code 作为第三方 agent 框架，在作为云 agent 运行时被 Agent Memory 覆盖，本地运行在研究预览期不受支持。
- object_type: product
  name: Codex
  canonical_name: Codex
  url: null
  positioning: OpenAI 的编码 agent，被列为 Warp Agent Memory 支持的第三方框架，作为云 agent 运行时读写共享的持久记忆。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Codex 且通过 Warp 云 agent 场景获得跨会话记忆的开发者
  product_signal: 作为云 agent 运行时接入 Agent Memory，可跨会话共享持久事实与结果，体现跨厂商 agent 记忆互操作方向。
  market_signal: null
  differentiation: 与 Warp Agent、Claude Code 并列为首批支持的 agent 框架，其接入显示记忆层正从单一工具走向跨厂商生态。
  watch_reason: Codex 与 Claude Code 同时被纳入 Warp 记忆生态，标志跨厂商 agent 记忆互操作起步，其后续接入深度与本地支持进展值得关注。
  risk_notes:
  - 研究预览期本地运行不受支持，实际记忆读写覆盖仍限于云 agent 场景，能力边界有待明确。
  score: 4.0
  article_ids:
  - b14cfc9a4d13eac9
  evidence_snippets:
  - Codex 与 Warp Agent、Claude Code 一同被列为 Agent Memory 支持的 agent 框架，可读写共享的持久记忆。
---

Agents > Memory (Research Preview)

# Agent Memory (Research Preview)

# Agent Memory (Research Preview) :::caution Agent Memory is in **research preview** and is enabled per team for design partners. [Join the waitlist](https://www.warp.dev/oz/agent-memory#waitlist) to request access for your team. ::: Agent Memory is a persistent memory system that lives on Warp and is shared across every supported agent harness, including the built-in Warp Agent, Claude Code, Codex, and others as they're added. Agents read from and write to this memory system as they run, so durable facts, decisions, and outcomes from one conversation are available to the next — regardless of which harness, machine, or teammate triggers the work. Memory creation and retrieval are asynchronous and run in the background, so they don't consume tokens or add latency to the active task. Watch this short preview to see Agent Memory in context. <VideoEmbed url="https://www.youtube.com/watch?v=ED9g1shmiEE" title="Agent Memory" /> [Join the Agent Memory waitlist](https://www.warp.dev/oz/agent-memory#waitlist). ## Key features * **Cross-harness memory** - One memory system is shared across the Warp Agent, Claude Code, Codex, and other harnesses as they're added. Third-party harnesses are covered when they run as cloud agents. * **Both local and cloud agents** - Supports interactive local agents in Warp and background cloud agents. * **Asynchronous by design** - Memory creation runs after a conversation ends. Retrieval runs in the background during a run. Neither consumes tokens or adds latency to the active task. * **Automatic memory creation from conversations** - When a conversation ends, Warp extracts durable facts, learnings, and outcomes and writes them as memories. New knowledge merges with existing memories or supersedes them on conflict. * **Shareable stores** - Memory is organized into stores. A store can be attached to one or more agents, so the same knowledge is available wherever those agents run. To share knowledge across a team, attach a store to an agent the whole team uses. * **Auto-memory for new agents** - New agents get a dedicated, agent-owned memory store by default, so they start building long-term memory from their first run. You can turn this off when you create the agent. * **Per-agent access and instructions** - Attach stores to specific agents with read-only or read-write access. Per-store instructions tell each agent how and when to use the store. * **Traceability** - Each memory records where it came from, so teams can trace a memory back to its source. * **Auditability** - Every change to a memory is recorded so teams can inspect how a memory has changed over time. ## Where Agent Memory runs Agent Memory is part of Warp. Storage, memory creation, and retrieval all run on Warp alongside your agents. The same memory is accessible from any agent you run in Warp: * The local Warp Agent. * Cloud agents triggered from the CLI, web app, schedules, or integrations. * Third-party harnesses running as cloud agents: Claude Code, Codex, and others as they're added. (Running third-party harnesses locally isn't supported during the research preview.) Memory stays bound to its owner (a user, an agent, or a team), independent of which harness reads or writes. ## Memory stores A memory store is a collection of memories. Stores are used by attaching them to agents: a store can be attached to a single agent or to several agents that need the same knowledge. To make knowledge available across a team, attach a store to an agent the whole team uses; there's no separate step for sharing a store with individual teammates. Stores differ by who owns them: * **Personal stores** - Owned by a user. Hold memories about preferences, working notes, and individual patterns. * **Agent stores** - Owned by an agent. A new agent gets one by default as its auto-memory store (see below). * **Team stores** - Owned by a team. Hold shared knowledge like deployment runbooks, code review conventions, or on-call procedures. Attach a team store to any agent the team uses so everyone's work draws on the same knowledge. Teams can use multiple stores to keep contexts separate, and attach the same store to several agents when needed. For example, a code review agent can use a dedicated store of review patterns, while a repo-specific store of architectural decisions is attached to both the code review agent and a Sentry triage agent so both reason about the same codebase. ### Auto-memory for new agents When you create an agent in the Oz web app, **Auto-memory** is on by default. With it enabled, Warp creates a dedicated memory store owned by that agent and uses it as the agent's default long-term memory: the agent reads relevant memories before it acts and writes durable facts, decisions, and preferences for future runs. Each agent has a single auto-memory store. Auto-memory is different from automatic memory creation from conversations, described below: auto-memory i