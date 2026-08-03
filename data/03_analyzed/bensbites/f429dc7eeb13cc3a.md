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
object_insights:
- object_type: product
  name: Claude Tag
  canonical_name: Claude Tag
  url: null
  positioning: Slack 工作流中@提及共享 Claude Code 实例的团队 Agent 协作工具。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Slack 的开发团队
  - 已部署 Claude Code 的组织
  product_signal: 将 Claude Code 实例以 Agent 身份引入 Slack，支持上下文保持和异步任务委托。
  market_signal: null
  differentiation: 不同于传统 Slack 机器人，共享实例可跨对话保持上下文并自主执行委派任务。
  watch_reason: Claude Tag 将 Claude Code 从个人终端工具扩展为团队协作 Agent，代表了 AI 编码助手向工作流平台化演进的重要方向。
  risk_notes:
  - 共享实例的权限隔离和安全性尚需验证。
  score: 6.0
  article_ids:
  - f429dc7eeb13cc3a
  evidence_snippets:
  - Claude Tag 允许用户在 Slack 中@提及共享的 Claude Code 实例，像 Agent 一样将其引入团队工作流。
  - 它可以保持来自 Slack 的上下文，让用户委派任务后去做其他事情。
- object_type: product
  name: Gemini 3.5 Flash
  canonical_name: Gemini 3.5 Flash
  url: null
  positioning: 新增计算机使用能力的 Google 多模态 AI 模型。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 开发者
  - 研究人员
  - 自动化工作流构建者
  product_signal: 新增计算机使用能力，可控制浏览器、移动端和桌面环境，提供开源 GitHub 仓库供本地试用。
  market_signal: null
  differentiation: 与纯对话模型不同，Gemini 3.5 Flash 可跨平台执行实际计算机操作，扩展了模型的能力边界。
  watch_reason: 计算机使用能力使 Gemini 3.5 Flash 从对话模型升级为可执行实际操作的 Agent 基座，对自动化工具生态有重大影响。
  risk_notes:
  - 跨平台控制的安全性和可靠性在实际场景中仍待验证。
  score: 7.0
  article_ids:
  - f429dc7eeb13cc3a
  evidence_snippets:
  - Gemini 3.5 Flash 新增了计算机使用能力，可以控制浏览器、移动端和桌面环境。
  - Google 提供了一个 GitHub 仓库，供用户本地或通过 Browserbase 试用该功能。
- object_type: product
  name: Jalapeño
  canonical_name: Jalapeño
  url: null
  positioning: OpenAI 与 Broadcom 合作制造的首款自研 AI 推理芯片。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - OpenAI 内部推理基础设施
  - ChatGPT 与 API 用户
  product_signal: 专为 ChatGPT、Codex、API 及未来 Agent 产品的 LLM 推理工作设计，首批自研芯片已流片。
  market_signal: 自研芯片标志着 AI 巨头向上游硬件整合的战略趋势，可能重构 AI 推理成本结构。
  differentiation: 与通用 GPU 不同，Jalapeño 针对 OpenAI 自有模型的推理场景深度定制，是 OpenAI 软硬一体战略的核心布局。
  watch_reason: 自研芯片使 OpenAI 摆脱对第三方 GPU 的依赖，对推理成本控制和产品路线图自主性具有深远的战略影响。
  risk_notes:
  - 芯片大规模部署的性能和良率尚需时间验证。
  score: 8.0
  article_ids:
  - f429dc7eeb13cc3a
  evidence_snippets:
  - OpenAI 与 Broadcom 合作制造了首款自研 AI 芯片 Jalapeño，专为 ChatGPT、Codex 和 API 的 LLM 工作设计。
  - 该芯片也面向未来的 Agent 产品，用于支撑推理场景。
- object_type: product
  name: Figma Motion
  canonical_name: Figma Motion
  url: null
  positioning: Figma Config 大会发布的动效设计专用新工具。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - UI/UX 设计师
  - 动效设计师
  product_signal: 作为 Figma Config 2026 重要发布项，Figma Motion 填补了 Figma 在动效设计领域的工具空白。
  market_signal: null
  differentiation: 与独立动效工具不同，Figma Motion 集成在 Figma 设计生态内，减少设计工具链切换成本。
  watch_reason: Figma Motion 的加入使 Figma 从静态设计工具向完整交互与动效设计平台持续演进，值得关注其与专业动效工具的竞争格局。
  risk_notes:
  - 与 After Effects 等成熟动效工具相比，功能深度尚待观察。
  score: 5.0
  article_ids:
  - f429dc7eeb13cc3a
  evidence_snippets:
  - Figma Config 大会发布了 Figma Motion，这是一个用于动效设计工作的新工具。
  - 大会还发布了将设计图层转化为代码的工具、可编辑着色器生成和 Figma Agent 第三方连接等功能。
- object_type: product
  name: Notion Developer Platform
  canonical_name: Notion Developer Platform
  url: null
  positioning: 支持运行代码工作流并集成外部 AI Agent 的 Notion 新开发者平台。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Notion 高级用户
  - 开发者团队
  - 知识工作者
  product_signal: 新增运行基于代码的工作流的能力，可集成 Claude Code、Cursor、Codex 等外部 Agent 基于共享文档协作。
  market_signal: Notion 从文档工具向开发者平台转型，与 AI 编码工具生态深度整合，可能重塑团队协作方式。
  differentiation: 与 Notion 传统无代码定位不同，新平台开放代码执行和 Agent 集成，成为 AI 时代的协作基础设施。
  watch_reason: Notion 向开发者平台转型的战略步伐值得关注，AI Agent 集成能力可能改变团队知识协作和任务管理范式。
  risk_notes:
  - 与专业开发者平台（如 GitHub）的竞争定位尚不清晰，执行成熟度有待观察。
  score: 7.0
  article_ids:
  - f429dc7eeb13cc3a
  evidence_snippets:
  - Notion 的新开发者平台增加了运行基于代码的工作流的能力。
  - 该平台可以集成 Claude Code、Cursor、Codex 等外部 Agent，使其基于共享文档和任务板协作。
- object_type: product
  name: GPT-5.5 Instant
  canonical_name: GPT-5.5 Instant
  url: null
  positioning: OpenAI 持续更新的轻量快速响应版 GPT 模型。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - ChatGPT 用户
  - API 开发者
  product_signal: 更新后对话更富趣味性，在意图理解、约束遵循和推荐能力上均有提升。
  market_signal: null
  differentiation: 定位为快速响应版模型，侧重对话体验微调和指令遵循能力的持续迭代。
  watch_reason: GPT-5.5 Instant 的持续优化反映了 OpenAI 在轻量级模型上通过微调提升用户体验的产品迭代思路。
  risk_notes:
  - 增量式更新，缺乏突破性功能亮点。
  score: 4.0
  article_ids:
  - f429dc7eeb13cc3a
  evidence_snippets:
  - GPT-5.5 Instant 获得了一次更新，使其对话更有趣，同时在意图理解、约束遵循和推荐方面表现更好。
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