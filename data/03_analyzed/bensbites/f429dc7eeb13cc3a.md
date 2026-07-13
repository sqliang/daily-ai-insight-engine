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
pipeline_stage: ingested
id: f429dc7eeb13cc3a
impact_score:
  score: 4.2
  reason: Claude Tag 是 Anthropic 为 Claude Code 新增的 Slack 集成功能，核心价值在于将 AI 编程助手从个人终端工具扩展为团队协作实体，支持在
    Slack 中@提及共享实例、保持对话上下文并委派任务。这降低了开发团队采用 AI 编程助手的协作摩擦，属于产品体验层面的重要改进。但该功能本质上是对现有
    AI 编码工具的工作流集成，未引入新的模型能力、训练范式或架构突破，不改变市场竞争格局或技术路线。在 Ben's Bites 这类汇总新闻中的多个条目（Gemini
    3.5 Flash computer use、OpenAI Jalapeño 芯片、Figma Config 更新）同样各具亮点，但单一体量均不足以产生行业级冲击。评分
    4.2，属于有意义的生态建设，但未触及范式转移。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: Slack 中原生调用 Claude Code 的团队协作效率提升
hype_assessment:
  level: low
  reason: Ben's Bites 原文以新闻汇总形式呈现，未使用 '颠覆'、'革命性' 等 PR 倾向用语。对 Claude Tag 的描述偏功能说明——'like
    agent across your team' 是合理的产品类比而非夸张。文章整体信息密度适中，多条新闻并列呈现，无明显的概念包装或水分。
information_entropy: medium
domain_disruption:
  technical_innovation: 无。Claude Tag 是 Claude Code 与 Slack API 的产品集成，核心是打通对话上下文保持通道，属于工程整合而非技术突破。
  business_model: 将 AI 编程助手从单人终端工具扩展为团队可共享的 Slack 实体，可能推动企业从 '个人订阅 AI 编码工具' 向 '团队级
    AI 开发协作平台' 的采购模式转变，对 Slack 生态内的 AI Agent 分发渠道有示范意义。
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
- 企业团队可将 AI 编程助手嵌入 Slack 等协作平台，形成「对话即开发」的工作流，开发者工具创业者可围绕 Slack/Teams 的 AI Agent 集成构建垂直插件生态
- 在 AI 生成 UI 时主动要求 Codex 等工具生成配图资产，可显著提升前端界面质感，产品设计师和前端开发者可将此作为低成本的 UI 优化工作流
- Notion 等平台开放外部 Agent 集成能力（如 Claude Code、Cursor、Codex），为构建跨文档、任务看板和代码库的统一 Agent 工作台提供了平台级机会
risk_matrix:
  regulatory: AI Agent 读取 Slack 等企业通讯工具中的团队消息涉及数据隐私合规问题，尤其在 GDPR、CCPA 管辖区域，企业部署需提前完成数据流审计和用户同意机制
  technological: 无
  competitive: 多巨头同时押注 Agent 协作赛道（Anthropic 的 Claude Tag、Google 的 Gemini Computer
    Use、OpenAI 的 Codex），生态碎片化可能导致企业选型成本上升，小型集成商面临被平台原生功能挤压的风险
  ethical: AI Agent 长期驻留团队聊天通道并访问上下文，可能引发员工对监控和隐私的隐忧，若未明确告知和征得同意，易造成团队信任问题
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
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