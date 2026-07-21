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
pipeline_stage: ingested
id: 28d2e5cda847dcca
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