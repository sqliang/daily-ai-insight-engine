---
title: Claude Code in Slack
source: https://www.bensbites.com/p/claude-code-in-slack
author: []
published: '2026-06-25'
created: '2026-06-26'
description: a tip to get better UI from Codex
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f429dc7eeb13cc3a
source_type: community_discussion
tldr: 本期 Ben's Bites 介绍了 Claude Tag（在 Slack 中召唤 Claude Code 的协作功能）、Gemini 3.5 Flash
  新增计算机使用能力、OpenAI 与 Broadcom 合作自研芯片 Jalapeño、Figma Config 发布多项新工具、Notion 新开发者平台支持集成外部
  AI Agent 等多项 AI 动态。
objective_summary: 2026 年 7 月 21 日，Ben's Bites 汇总了近期 AI 行业动态，核心包括：Anthropic 推出 Claude
  Tag 功能，允许用户在 Slack 中像 Agent 一样调用共享 Claude Code 实例并保持上下文；Google 发布 Gemini 3.5 Flash
  并开放计算机使用能力；OpenAI 与 Broadcom 合作制造首款自研 AI 芯片 Jalapeño，专为 ChatGPT、Codex 和 API 设计；Figma
  Config 大会发布代码生成、Figma Motion 动效工具和 Agent 第三方连接等更新；Notion 新开发者平台支持运行代码工作流并集成 Claude
  Code、Cursor、Codex 等外部 Agent。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Google
  - OpenAI
  - Broadcom
  - Figma
  - Notion
  - DeepMind
  - AssemblyAI
  - Modal
  - Perplexity
  - Genspark
  - Harvey
  - Rippling
  - Runpod
  - Exa
  technologies:
  - Claude Code
  - Claude Tag
  - Gemini 3.5 Flash
  - GPT-5.5 Instant
  - Image Gen
  - Jalapeño
  key_people:
  - Keshav
  - Ben Kus
  - John Jumper
key_logic_flow:
- Keshav 分享了一个使用 Codex 的 Image Gen 技能自动生成 UI 图片的技巧，认为这样能让网页 UI 不再单调。
- Claude Tag 允许用户在 Slack 中@提及共享的 Claude Code 实例，将其作为团队 Agent，保持上下文并委派任务。
- Google 发布的 Gemini 3.5 Flash 新增计算机使用能力，可控制浏览器、移动端和桌面环境，并提供 GitHub 仓库供本地或通过 Browserbase
  试用。
- OpenAI 与 Broadcom 合作制造了首款自研 AI 芯片 Jalapeño，专为 ChatGPT、Codex、API 及未来 Agent 产品的 LLM
  推理工作设计。
- Notion 新开发者平台支持运行基于代码的工作流，并能集成 Claude Code、Cursor、Codex 等外部 Agent，使其基于共享文档和任务板工作。
- Figma Config 大会发布了多项更新，包括将设计图层转化为代码的新工具、Figma Motion 动效设计工具、可编辑着色器生成以及 Figma Agent
  第三方连接等功能。
extract_result: success
object_mentions:
- object_type: product
  name: Claude Tag
  canonical_name: Claude Tag
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - Claude Tag 允许用户在 Slack 中@提及共享的 Claude Code 实例，像 Agent 一样将其引入团队工作流。
  - 它可以保持来自 Slack 的上下文，让用户委派任务后去做其他事情。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Gemini 3.5 Flash
  canonical_name: Gemini 3.5 Flash
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - Gemini 3.5 Flash 新增了计算机使用能力，可以控制浏览器、移动端和桌面环境。
  - Google 提供了一个 GitHub 仓库，供用户本地或通过 Browserbase 试用该功能。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Jalapeño
  canonical_name: Jalapeño
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 与 Broadcom 合作制造了首款自研 AI 芯片 Jalapeño，专为 ChatGPT、Codex 和 API 的 LLM 工作设计。
  - 该芯片也面向未来的 Agent 产品，用于支撑推理场景。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Figma Motion
  canonical_name: Figma Motion
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Figma Config 大会发布了 Figma Motion，这是一个用于动效设计工作的新工具。
  - 大会还发布了将设计图层转化为代码的工具、可编辑着色器生成和 Figma Agent 第三方连接等功能。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Notion Developer Platform
  canonical_name: Notion Developer Platform
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - Notion 的新开发者平台增加了运行基于代码的工作流的能力。
  - 该平台可以集成 Claude Code、Cursor、Codex 等外部 Agent，使其基于共享文档和任务板协作。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: GPT-5.5 Instant
  canonical_name: GPT-5.5 Instant
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GPT-5.5 Instant 获得了一次更新，使其对话更有趣，同时在意图理解、约束遵循和推荐方面表现更好。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Exa Connect
  canonical_name: Exa Connect
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Exa Connect 是面向 Web Agent 的产品，可查询 ZoomInfo、Crunchbase、Similarweb 等数据源。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Perplexity Computer for Counsel
  canonical_name: Perplexity Computer for Counsel
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Perplexity Computer for Counsel 是一款面向法律场景的产品，提供法律研究、文档和案件管理工具。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: AssemblyAI Universal-3.5 Pro Realtime
  canonical_name: AssemblyAI Universal-3.5 Pro Realtime
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - AssemblyAI Universal-3.5 Pro Realtime 是一款语音转文本产品，能够利用 Agent 在通话端提供的上下文信息。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Modal Auto Endpoints
  canonical_name: Modal Auto Endpoints
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Modal Auto Endpoints 允许用户用一条命令在生产环境中运行开源模型。
  article_id: f429dc7eeb13cc3a
- object_type: project
  name: Executor
  canonical_name: Executor
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Executor 是一个开源网关，用于将 Agent 连接到各类服务。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Aside
  canonical_name: Aside
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Aside 是一款 AI 浏览器，具有垂直标签页、本地加密数据存储以及 Claude 和 ChatGPT 支持。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Genspark Design
  canonical_name: Genspark Design
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Genspark Design 可以生成 UI 原型、视频、HTML 动画和代码。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Hubble
  canonical_name: Hubble
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Hubble 是一款面向用户和 Agent 的 Markdown 记事本，支持实时 HTML 预览。
  article_id: f429dc7eeb13cc3a
- object_type: company
  name: Engram
  canonical_name: Engram
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Engram 是一个新的实验室，希望训练一个能从用户工作中学习并每天更新的个人模型。
  article_id: f429dc7eeb13cc3a
- object_type: project
  name: Emil's design skills repo
  canonical_name: Emil's design skills repo
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 该仓库包含了设计工程相关的技能集，拥有超过 10 万次安装。
  article_id: f429dc7eeb13cc3a
- object_type: product
  name: Harvey Labs
  canonical_name: Harvey Labs
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Harvey Labs 提供了法律领域的基础模型、开放式评估以及由律所拥有的人工智能能力。
  article_id: f429dc7eeb13cc3a
---

# Claude Code in Slack

### a tip to get better UI from Codex

Hey folks,

Keshav here.

About a week ago, I watched Codex automatically generate images with the Image Gen skill while making an app. It used them as real assets in the UI.

Since then, I’ve started explicitly asking it to create images whenever I’m building web UIs. The results are noticeably better: pages look less bland, and because Claude Code can’t generate images, the output feels different from the usual AI-generated UI.

Give it a try.

*Ben’s Bites is brought to you by Rippling*

Spinning up agents is easy.

Letting them access your company data safelyisn’t. Join Box CTO Ben Kus onJune 30for a live webinar on the guardrails, eval process, and onboarding guide your agents need — including thediagnostic tool Rippling’s own AI team uses— save your spot.

#### Headlines

**Claude Tag**lets you mention a shared instance of Claude Code like agent across your team in Slack. Tag it into work, let it keep context from Slack, and delegate tasks while you do something else.**Gemini 3.5 Flash has computer use**now. It can control the browser, mobile and desktop environments, and Google has a GitHub repo to try it locally or through Browserbase.**New from Figma Config**- turn design layers into code, new tool (Figma Motion) for motion design work, generate editable shaders, vibe coding for plugins, third-party connections for Figma Agent and more.**Notion’s new developer platform**is adding the ability to run code-based workflows and the ability to integrate external agents like Claude Code, Cursor, Codex, etc., so that they can work from shared docs and task boards.**OpenAI built its first AI chip**, Jalapeño, with Broadcom. It is made for the LLM work behind ChatGPT, Codex, the API and future agent products.**Build & ship at the Runpod Flash Hack Day!**Join Runpod on June 30 at the SF Builder’s Collective for an in-person hackathon. Remote-friendly. Learn how to use Runpod Flash to turn Python functions into auto-scaling, serverless GPU endpoints without Docker. Demos, prizes & mentorship. Register here.*

#### My feed

GPT-5.5 Instant got an update that makes it more fun to talk to, better at intent, constraints and recommendations.

Exa Connect - web agents to query ZoomInfo, Crunchbase, Similarweb and more.

Perplexity Computer for Counsel - legal research, docs and matter tools in Computer.

AssemblyAI Universal-3.5 Pro Realtime - speech-to-text uses the agent’s side of the call as context.

Modal Auto Endpoints - run open models in production with one command.

Executor - open-source gateway for connecting agents to services.

Aside - AI browser with vertical tabs, local encrypted data and Claude/ChatGPT support.

Genspark Design - generate UI prototypes, videos, HTML animations and code.

Hubble - Markdown notepad for you and agents, with live HTML previews.

John Jumper, AlphaFold lead, is leaving DeepMind for Anthropic.

Engram - a new lab that hopes to train a personal model that learns from your work and updates roughly every day.

Emil’s design skills repo - design engineering skills with 100k+ installs.

Harvey Labs - legal foundation models, open evals and firm-owned intelligence.

Codex workflow tip - have your agent write workflow papercuts to /tmp while it runs.


#### Afters

Read about me and Ben’s Bites

📷 thumbnail via @keshavatearth



* sponsors who make this newsletter possible :)

Wanna partner with us for the next quarter?

Email us at shanice@bensbites.com or k@bensbites.com