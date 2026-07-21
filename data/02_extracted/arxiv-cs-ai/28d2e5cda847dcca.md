---
title: 'AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors,
  and Adaptive Recovery'
source: https://arxiv.org/abs/2607.15367
author:
- '[[Raunak B Sinha]]'
published: '2026-07-20'
created: '2026-07-20'
manifest_dates:
- '2026-07-20'
description: 'arXiv:2607.15367v1 Announce Type: new Abstract: Desktop voice assistants
  are still dominated by cloud pipelines that ship raw audio off the machine and expose
  a fixed set of skills. We describe AnovaX, a small local-first assistant that runs
  entirely on the user''s computer and treats the desktop itself as its action surface.
  A single Python process wires together a wake-word gate, a speech pipeline, an LLM
  planner (Gemini) that emits a JSON plan of tool calls, a whitelist-and-denylist
  safety layer, a multi-agent orchestrator that translates each plan into typed child
  agents on a bounded thread pool, and an adaptive recovery loop that takes over whenever
  a core step fails. Every tool corresponds to a specialized agent class (AppAgent,
  TypingAgent, BrowserAgent and six others) with its own timeout, retry policy, and
  shared-resource locks. A recursive MetaAgent lets the planner delegate a sub-goal
  back to itself, capped at two levels of nesting. The recovery loop uses a compact
  ReAct-style prompt and hides Gemini''s latency behind speculative execution of read-only
  tools. A companion Flask server exposes a phone-friendly remote over the local WiFi,
  mirrors every agent lifecycle event to the phone in real time, and streams the laptop''s
  screen back over MJPEG so the user can watch remote commands land as they run. The
  point of the project is less to compete with Siri or Alexa than to show that a legible,
  few-thousand-line assistant is enough to open apps, type into them, run searches,
  coordinate concurrent actions, recover from single-step failures, and be driven
  entirely from a phone in another room -- without the LLM ever touching the keyboard.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 28d2e5cda847dcca
source_type: academic_paper
tldr: AnovaX 是一个完全本地运行的多代理桌面语音助手系统，利用 Gemini LLM 进行任务规划，通过类型化子代理执行工具调用，并配备自适应恢复机制，无需将音频数据发送到云端。
objective_summary: 该论文提出了 AnovaX，一个完全在用户本地计算机上运行的桌面语音助手系统。系统通过单 Python 进程集成了唤醒词门控、语音流水线、Gemini
  LLM 规划器和多代理编排器，将每个 JSON 格式的计划翻译为带类型、带超时和重试策略的子代理任务。系统还包含自适应恢复循环和两级的递归 MetaAgent，并配套提供
  Flask 远程控制服务器，可通过手机在本地 WiFi 内实时操控电脑。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Google
  technologies:
  - LLM
  - Multi-Agent
  - ReAct
  - JSON
  - MJPEG
  - REST
  key_people: []
key_logic_flow:
- AnovaX 是一个本地优先的桌面语音助手系统，所有处理完全在用户计算机上完成，不将原始音频发送到云端。
- 系统使用 Gemini 作为 LLM 规划器，生成 JSON 格式的工具调用计划，并通过白名单和黑名单安全层进行过滤。
- 多代理编排器将每个计划转换为带类型的子代理实例，运行在有限线程池上，每个代理有独立的超时和重试策略。
- 系统包含一个自适应恢复循环，该循环使用精简的 ReAct 风格提示，并在核心步骤失败时接管控制。
- 一个递归的 MetaAgent 允许规划器将子目标再次委托给自身，最多支持两级嵌套深度。
- 配套的 Flask 服务器通过本地 WiFi 提供手机远程控制界面，通过 MJPEG 流实时回传笔记本电脑屏幕。
object_mentions:
- object_type: project
  name: AnovaX
  canonical_name: AnovaX
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - AnovaX 是一个完全运行在用户计算机本地的桌面语音助手，将桌面本身作为操作界面。
  - 系统通过单 Python 进程整合了唤醒词门控、语音流水线、LLM 规划器和多代理编排器。
  - 每个工具对应一个专门的代理类，包括 AppAgent、TypingAgent、BrowserAgent 等八种类型。
  article_id: 28d2e5cda847dcca
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors, and Adaptive Recovery

View PDF HTML (experimental)Abstract:Desktop voice assistants are still dominated by cloud pipelines that ship raw audio off the machine and expose a fixed set of skills. We describe AnovaX, a small local-first assistant that runs entirely on the user's computer and treats the desktop itself as its action surface. A single Python process wires together a wake-word gate, a speech pipeline, an LLM planner (Gemini) that emits a JSON plan of tool calls, a whitelist-and-denylist safety layer, a multi-agent orchestrator that translates each plan into typed child agents on a bounded thread pool, and an adaptive recovery loop that takes over whenever a core step fails. Every tool corresponds to a specialized agent class (AppAgent, TypingAgent, BrowserAgent and six others) with its own timeout, retry policy, and shared-resource locks. A recursive MetaAgent lets the planner delegate a sub-goal back to itself, capped at two levels of nesting. The recovery loop uses a compact ReAct-style prompt and hides Gemini's latency behind speculative execution of read-only tools. A companion Flask server exposes a phone-friendly remote over the local WiFi, mirrors every agent lifecycle event to the phone in real time, and streams the laptop's screen back over MJPEG so the user can watch remote commands land as they run. The point of the project is less to compete with Siri or Alexa than to show that a legible, few-thousand-line assistant is enough to open apps, type into them, run searches, coordinate concurrent actions, recover from single-step failures, and be driven entirely from a phone in another room -- without the LLM ever touching the keyboard.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.