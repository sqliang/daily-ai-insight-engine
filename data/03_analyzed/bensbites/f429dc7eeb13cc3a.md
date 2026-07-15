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
tldr: Claude Tag 让 Claude Code 可在 Slack 中被 @ 提及并协作
objective_summary: Ben's Bites 日报汇总多项 AI 新闻：Anthropic 发布 Claude Tag 功能使 Claude Code
  集成到 Slack 协作；Google 为 Gemini 3.5 Flash 增加计算机使用能力；Figma Config 发布多项新工具；Notion 推出支持外部
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Google
  - Figma
  - Notion
  - OpenAI
  - Broadcom
  - DeepMind
  - Runpod
  - AssemblyAI
  - Rippling
  technologies:
  - Claude Code
  - Claude Tag
  - Gemini 3.5 Flash
  - GPT-5.5 Instant
  - Jalapeño
  - Computer Use
  key_people:
  - Keshav
  - John Jumper
  - Ben Kus
key_logic_flow:
- Claude Tag 是 Anthropic 推出的新功能，允许用户在 Slack 中 @ 提及共享的 Claude Code 实例，使其保持对话上下文并委派任务
- Google 为 Gemini 3.5 Flash 增加了计算机使用能力，可控制浏览器、移动和桌面环境
- OpenAI 与 Broadcom 合作制造了其首款 AI 芯片 Jalapeño，专为 ChatGPT、Codex、API 及未来代理产品设计
- Figma Config 大会上发布了从设计图层生成代码、Figma Motion 动效工具、可编辑着色器以及 Figma Agent 第三方连接等新功能
- Notion 新开发者平台支持运行基于代码的工作流，并可集成 Claude Code、Cursor、Codex 等外部 AI 代理
- AlphaFold 负责人 John Jumper 离开 DeepMind 加入 Anthropic
extract_result: success
impact_score:
  score: 6.0
  reason: Claude Tag 将 AI 编程助手从单人 CLI 工具扩展为团队协作成员，直接嵌入 Slack 这一企业通讯中枢，降低了上下文切换成本。该功能实现了对话上下文的跨平台持久化共享和任务委派，是
    AI Agent 协作形态的重要产品化尝试。但本质上是集成层创新，未改变底层模型能力或训练范式，行业影响范围限定在已使用 Claude Code 和 Slack
    的团队中，不具备出圈效应或范式转移性质。综合评估为中等偏上冲击力，可影响局部竞争格局（特别是 AI 编程工具的团队协作赛道）。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Slack 中直接 @ 调用 Claude Code 并保持对话上下文的能力，减少工具切换摩擦
hype_assessment:
  level: low
  reason: 报道出自 Ben's Bites 的每日新闻摘要，文体本身属于事实性信息汇总。描述用语克制（如 'lets you mention a shared
    instance'、'tag it into work'），未出现'颠覆''革命性'等 PR 夸大类词汇，各条新闻均平实介绍功能细节，无明显炒作包装痕迹。
information_entropy: medium
domain_disruption:
  technical_innovation: 将 AI 编程代理通过 Slack 集成实现多轮对话上下文的跨平台持久化共享和团队级任务委派，打通了 CLI 编程助手与企业即时通讯之间的协作壁垒，属于交互范式层面的创新
  business_model: 推动 AI 编程工具从个人开发者自选工具向团队级标准化协作平台演进，可能重塑企业 AI 开发工具的采购决策模式——从按席位订阅转向按团队协作能力定价
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: Claude Code 的 Slack 集成（Claude Tag）将 AI 编程代理从单人工具升级为团队协作基础设施，具备中等复利效应。核心逻辑：(1)
    团队在 Slack 中共享 Claude Code 实例，对话上下文和任务历史在渠道中积累，产生团队级别的数据护城河和切换成本；(2) Slack 作为企业通讯的核心枢纽，Claude
    Code 嵌入其中可获得高频使用和自然分发，形成'越用越好用'的正反馈循环；(3) @提及交互模式降低了 AI 代理的使用门槛，让非技术团队成员也能自然参与协作。但风险在于：(a)
    依赖 Slack 平台生态，受其 API 策略变化影响；(b) 竞争对手（如 OpenAI Codex Agent、GitHub Copilot）同样可以构建类似
    Slack 集成，差异化窗口有限；(c) 该功能本身不改变模型层的竞争格局，核心价值仍锚定在 Claude 模型能力上。综合来看，这是一个重要的产品化方向和生态卡位，但需持续观察采用率和粘性才能确认其基础设施级地位。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Slack (Salesforce)
competitive_casualty:
- OpenAI Codex Agent
- GitHub Copilot Chat
- Cursor
market_opportunities:
- 企业可将 Claude Tag 集成到内部 Slack 工作流中，构建 AI 驱动的任务委派和上下文保持系统，降低团队协作中的信息摩擦
- Notion 新开发者平台支持外部 AI 代理接入，创业团队可开发连接 Claude Code/Cursor/Codex 的中间件，打通文档、任务看板与 AI
  协作的闭环
- OpenAI 自研芯片 Jalapeño 的量产将降低 API 推理成本，应用层开发者应关注后续定价调整窗口，提前规划高吞吐量 AI 产品的商业化路径
risk_matrix:
  regulatory: AI 代理接入 Slack 等企业通讯工具将触发数据隐私合规审查，特别是在 GDPR 和 EU AI Act 框架下，企业需重新评估 AI
    对内部通信数据的访问权限与留存策略
  technological: Claude Tag 深度绑定 Slack 生态，若 Slack 在企业协作市场的份额被 Notion、Teams 等蚕食，该功能的技术杠杆将随之衰减；Google
    Computer Use 能力的加入使浏览器/桌面自动化赛道出现双巨头并立格局，技术路线收敛风险上升
  competitive: Google 为 Gemini 3.5 Flash 增加计算机使用能力，与 Claude 的 Computer Use 形成正面竞争；OpenAI
    自研芯片将降低模型推理成本，可能引发新一轮 API 价格战，挤压中小 AI Infra 公司的生存空间
  ethical: Claude Tag 在 Slack 中保持上下文并委派任务意味着 AI 可访问团队内部对话历史，存在员工隐私泄露和监控扩大的伦理争议；计算机使用能力增强了深度伪造、自动钓鱼等攻击向量
  additional:
  - AI 顶级人才向单一公司集中——AlphaFold 负责人离开 DeepMind 加入 Anthropic，加剧了 AI 基础研究的人才虹吸效应，长期可能削弱学术机构和竞争对手的创新能力
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
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