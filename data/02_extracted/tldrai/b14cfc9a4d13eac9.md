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
---

Agents > Memory (Research Preview)

# Agent Memory (Research Preview)

# Agent Memory (Research Preview) :::caution Agent Memory is in **research preview** and is enabled per team for design partners. [Join the waitlist](https://www.warp.dev/oz/agent-memory#waitlist) to request access for your team. ::: Agent Memory is a persistent memory system that lives on Warp and is shared across every supported agent harness, including the built-in Warp Agent, Claude Code, Codex, and others as they're added. Agents read from and write to this memory system as they run, so durable facts, decisions, and outcomes from one conversation are available to the next — regardless of which harness, machine, or teammate triggers the work. Memory creation and retrieval are asynchronous and run in the background, so they don't consume tokens or add latency to the active task. Watch this short preview to see Agent Memory in context. <VideoEmbed url="https://www.youtube.com/watch?v=ED9g1shmiEE" title="Agent Memory" /> [Join the Agent Memory waitlist](https://www.warp.dev/oz/agent-memory#waitlist). ## Key features * **Cross-harness memory** - One memory system is shared across the Warp Agent, Claude Code, Codex, and other harnesses as they're added. Third-party harnesses are covered when they run as cloud agents. * **Both local and cloud agents** - Supports interactive local agents in Warp and background cloud agents. * **Asynchronous by design** - Memory creation runs after a conversation ends. Retrieval runs in the background during a run. Neither consumes tokens or adds latency to the active task. * **Automatic memory creation from conversations** - When a conversation ends, Warp extracts durable facts, learnings, and outcomes and writes them as memories. New knowledge merges with existing memories or supersedes them on conflict. * **Shareable stores** - Memory is organized into stores. A store can be attached to one or more agents, so the same knowledge is available wherever those agents run. To share knowledge across a team, attach a store to an agent the whole team uses. * **Auto-memory for new agents** - New agents get a dedicated, agent-owned memory store by default, so they start building long-term memory from their first run. You can turn this off when you create the agent. * **Per-agent access and instructions** - Attach stores to specific agents with read-only or read-write access. Per-store instructions tell each agent how and when to use the store. * **Traceability** - Each memory records where it came from, so teams can trace a memory back to its source. * **Auditability** - Every change to a memory is recorded so teams can inspect how a memory has changed over time. ## Where Agent Memory runs Agent Memory is part of Warp. Storage, memory creation, and retrieval all run on Warp alongside your agents. The same memory is accessible from any agent you run in Warp: * The local Warp Agent. * Cloud agents triggered from the CLI, web app, schedules, or integrations. * Third-party harnesses running as cloud agents: Claude Code, Codex, and others as they're added. (Running third-party harnesses locally isn't supported during the research preview.) Memory stays bound to its owner (a user, an agent, or a team), independent of which harness reads or writes. ## Memory stores A memory store is a collection of memories. Stores are used by attaching them to agents: a store can be attached to a single agent or to several agents that need the same knowledge. To make knowledge available across a team, attach a store to an agent the whole team uses; there's no separate step for sharing a store with individual teammates. Stores differ by who owns them: * **Personal stores** - Owned by a user. Hold memories about preferences, working notes, and individual patterns. * **Agent stores** - Owned by an agent. A new agent gets one by default as its auto-memory store (see below). * **Team stores** - Owned by a team. Hold shared knowledge like deployment runbooks, code review conventions, or on-call procedures. Attach a team store to any agent the team uses so everyone's work draws on the same knowledge. Teams can use multiple stores to keep contexts separate, and attach the same store to several agents when needed. For example, a code review agent can use a dedicated store of review patterns, while a repo-specific store of architectural decisions is attached to both the code review agent and a Sentry triage agent so both reason about the same codebase. ### Auto-memory for new agents When you create an agent in the Oz web app, **Auto-memory** is on by default. With it enabled, Warp creates a dedicated memory store owned by that agent and uses it as the agent's default long-term memory: the agent reads relevant memories before it acts and writes durable facts, decisions, and preferences for future runs. Each agent has a single auto-memory store. Auto-memory is different from automatic memory creation from conversations, described below: auto-memory i