---
title: holaboss-ai/holaOS
source: https://github.com/holaboss-ai/holaOS
author: []
published: ''
created: '2026-08-14'
manifest_dates:
- '2026-08-14'
- '2026-08-15'
description: 'Open-source All in One AI agent workspace. Run any agent — Claude Code,
  Codex — across your tools (100+ integrations + MCP), apps, browser, and files, with
  shared memory. Built-in models or BYOK. The Computer for You and Your Agent Run
  any agent — Claude Code, Codex, or holaOS — in one local-first workspace, over your
  tools, your files, and one shared memory. Frontier models built in, or bring your
  own keys. Website · Docs · Sign in · Quick Start ⭐ If holaOS is useful, a star helps
  more builders find it. ✨ What makes it different 🔀 Run any agent, one workspace
  Claude Code, Codex, and the built-in holaOS agent — side by side, no switching.
  Whichever you run, it shares the same memory, tools, skills, and apps. Use the best
  agent for the job without rebuilding your setup every time. No lock-in — bring the
  agent you already trust. Shared everything — one context, one set of tools, one
  workspace. Consistent results — the same skills and integrations, whatever''s driving.
  🧠 One memory, every agent Context, preferences, and project history live in a single
  shared memory — stored locally, as plain files you can read and edit. Switch agents,
  close the app, come back next week: it already knows where you left off. Never start
  from zero — durable memory across sessions and agents. Local-first & yours — on
  your machine, visible and editable, not locked in someone else''s cloud. Actually
  recallable — structured and embedded, so the right context returns when it''s needed.
  💸 Models your way — built in, or bring your own One account, every model — no keys,
  no setup, no switching between providers. The latest frontier models are built in:
  cost-efficient Kimi K3 and GLM 5.2 for everyday volume, plus top-tier GPT 5.6, Claude
  Opus 5, and Fable 5 for the hard problems. Prefer your own provider? Bring your
  own keys for OpenAI, Anthropic, or any OpenAI- or Anthropic-compatible endpoint
  — those run on your account, not your holaOS plan. Zero-setup default — one account,
  every SOTA model, no API keys to manage. BYOK when you want it — your keys, your
  providers, your rates. Right model per task — pick per job, per agent. 🪟 HolaApps
  — apps and agent, side by side Install apps from the in-workspace marketplace and
  they open as real, interactive surfaces right beside your agent. Watch it work inside
  the app, step in whenever you want, and the result lands in place — not a wall of
  chat text, but the actual app, driven by the agent, next to the agent. Real surfaces,
  not chat — every app is a live UI (Notion, a browser, your own app), not a transcript.
  Side-by-side by design — app and agent share the screen, so you always see what''s
  happening and can take over. One click to install — browse the in-workspace marketplace
  and open any app instantly. Bring your own — point a HolaApp at any URL and MCP
  server; it lives on your machine, yours to open and drive. 🧩 Skills, Integrations
  & MCP — teach it once, reuse everywhere Integrations — connect Gmail, Notion, Slack,
  GitHub, Linear and 50+ more with one-click OAuth. Agents read and act across your
  tools, no glue code — and every agent inherits the same connections. MCP — plug
  in any Model Context Protocol server to give your agents new tools. Bring your own,
  or install community MCP servers in one click. Skills — package a workflow once;
  any agent runs it on demand. Combos — bundle skills and integrations into a single
  one-click install. 🛠️ Your entire workstation, agent-operable 🌐 A real browser,
  driven by agents — signed-in browsers your agents drive to browse, click, and extract
  — under your control. 🎨 Frontier generation built in — the latest image, video,
  and audio models inside every agent. Storyboard a video, design a poster, voice
  a script — one prompt. 📄 Real deliverables — reports, spreadsheets, and slides saved
  as real .xlsx, .pptx, and .docx files you can send, not text stuck in a chat. 💬
  Reach it from anywhere you chat — Feishu, WeChat, Slack, Telegram. Send a task from
  any thread; the result comes back to the same thread. ⏰ Automation — run on a schedule
  or a trigger. Digests, monitors, and reports finish and file themselves. 🚀 Run it
  your way 🖥️ Desktop app Download and go. Nothing to set up — frontier models built
  in, free to start. 🔓 Open source Self-host it. Modified Apache 2.0, bring your own
  keys, run it entirely on your machine. 🏢 Enterprise SSO with per-role permissions
  for every agent, skill, and app. Connect internal systems without exposing them.
  Audit logs on every action. On-prem or your own cloud. Table of Contents Quick Start
  Manual Install OSS Release Notes Quick Start One-Line Install For a fresh-machine
  bootstrap on macOS, Linux, or WSL, use the repository installer: curl -fsSL https://raw.githubusercontent.com/holaboss-ai/holaOS/refs/heads/main/scripts/install.sh
  | bash -s -- --launch You can also follow the manual path if you want to control
  each setup step. Star the Repository If holaOS is useful or interesting, a GitHub
  Star would be greatly appreciated. Manual Install You likely will not need this
  section because One-Line Install runs the same setup. Use Manual Install when you
  want to inspect or control each step. If you use the manual path, verify the usual
  prerequisites first: git --version node --version npm --version One-Line Agent Setup
  If you use Codex, Claude Code, Cursor, Windsurf, or another coding agent, you can
  hand it the setup instructions in one sentence: Run the holaOS install script from
  https://raw.githubusercontent.com/holaboss-ai/holaOS/refs/heads/main/scripts/install.sh.
  It should install git and Node.js 24.14.1/npm if they are missing, clone or update
  the repo into ~/holaboss-ai unless I specify another --dir, run desktop:install,
  create apps/desktop/.env from apps/desktop/.env.example if needed, run desktop:prepare-runtime:local
  and desktop:typecheck, and only run desktop:dev if I ask for --launch. If Electron
  cannot open, stop after verification and tell me the next manual step. That handoff
  keeps the installation flow self-contained while leaving the detailed bootstrap
  steps in the repo-local INSTALL.md runbook. This is the baseline installation flow
  for local desktop development. Install the desktop dependencies from the repository
  root: npm run desktop:install Create your local environment file: cp apps/desktop/.env.example
  apps/desktop/.env If you are following the repo exactly, keep the file close to
  the template and only change the values that your provider or machine needs. The
  canonical path is apps/desktop/.env. Existing legacy desktop/.env files are still
  accepted for now, but new setups should use apps/desktop/.env. Prepare the local
  runtime bundle: npm run desktop:prepare-runtime:local If you want a quick validation
  pass before launching Electron, run: npm run desktop:typecheck Start the desktop
  app in development mode: npm run desktop:dev The predev hook will validate the environment,
  rebuild native modules, and make sure a staged runtime bundle exists. If you want
  to stage the runtime before opening the desktop app, there are two common paths:
  Build from local runtime: npm run desktop:prepare-runtime:local Fetch the latest
  published runtime: npm run desktop:prepare-runtime Use the local path when you are
  actively changing runtime code. Use the published bundle when you want to verify
  the desktop against a known release artifact. Use One-Line Install when you want
  the fastest path to a working local desktop environment. Use Manual Install when
  you need to inspect or control each setup step yourself. OSS Release Notes License:
  modified Apache 2.0 with additional commercial-distribution and branding conditions.
  See LICENSE. Security issues: report privately to admin@holaboss.ai. See SECURITY.md.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4a0bba59f2decb48
source_type: community_discussion
tldr: holaOS 是 holaboss-ai 开源的本地优先智能体工作空间，可在同一桌面运行 Claude Code、Codex 与内置 holaOS agent，并共享记忆、工具、技能与应用；内置多款前沿模型，也支持自带
  API key。
objective_summary: holaboss-ai 在 GitHub 发布 holaOS，定位为面向用户及 AI agent 的本地优先桌面工作空间。它允许用户在统一工作区中并行运行
  Claude Code、Codex 与内置 holaOS agent，并共享本地文件化的记忆、工具、技能和应用市场。系统默认接入 Kimi K3、GLM 5.2、GPT
  5.6、Claude Opus 5、Fable 5 等前沿模型，也支持用户绑定 OpenAI、Anthropic 或兼容端点的自有 API key。项目提供一键安装脚本、桌面应用、开源自托管版和企业版（含
  SSO、审计、权限），并支持 OAuth 集成、MCP 服务器和技能自动化。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - holaboss-ai
  - OpenAI
  - Anthropic
  technologies:
  - MCP
  - OAuth
  - Claude Code
  - Codex
  key_people: []
key_logic_flow:
- holaboss-ai 推出 holaOS，作为本地优先的 agent 工作空间，试图解决多 agent 切换与上下文割裂的问题。
- 同一工作区可同时运行 Claude Code、Codex 与内置 holaOS agent，三者共享本地文件化的记忆、工具、技能与应用。
- 默认内置 Kimi K3、GLM 5.2、GPT 5.6、Claude Opus 5、Fable 5 等模型，并支持用户绑定自有 API key。
- 通过 OAuth 集成 50 余项服务、MCP 服务器扩展工具、技能与组合打包，实现跨 agent 的自动化工作流。
- 提供桌面应用、开源自托管版本与企业版，并支持 macOS、Linux 与 WSL 的一键安装脚本。
object_mentions:
- object_type: project
  name: holaboss-ai/holaOS
  canonical_name: holaOS
  url: https://github.com/holaboss-ai/holaOS
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - holaOS 将自己定位为面向用户及其 agent 的计算机，可在本地优先的工作空间中运行任意 agent。
  - README 指出，Claude Code、Codex 与内置 holaOS agent 可在同一工作区并排运行，无需切换。
  - 项目采用 Modified Apache 2.0 许可，提供桌面应用、开源自托管版及企业版三种形态。
  article_id: 4a0bba59f2decb48
- object_type: product
  name: holaOS Desktop
  canonical_name: holaOS Desktop
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - README 在功能表格中列出 Desktop app，宣称下载即可使用，内置前沿模型且免费开始。
  - 桌面应用支持 macOS、Linux 与 WSL，并提供一键安装脚本以完成新机器初始配置。
  article_id: 4a0bba59f2decb48
- object_type: product
  name: HolaApp
  canonical_name: HolaApp
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 用户可以指向任意 URL 和 MCP 服务器来创建 HolaApp，使其作为本地可打开和驱动的交互式应用运行。
  - HolaApp 被描述为可在工作区 marketplace 中安装并打开的实时 UI，而非单纯的聊天记录。
  article_id: 4a0bba59f2decb48
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - README 将 Claude Code 列为可在 holaOS 工作区中运行的外部 agent，与 Codex 及内置 holaOS agent 共享记忆、工具、技能和应用。
  article_id: 4a0bba59f2decb48
- object_type: product
  name: Codex
  canonical_name: OpenAI Codex
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - README 将 Codex 列为可在 holaOS 工作区中运行的外部 agent，与 Claude Code 及内置 holaOS agent 共享记忆、工具、技能和应用。
  article_id: 4a0bba59f2decb48
extract_result: success
impact_score:
  score: 6.2
  reason: holaOS 试图把 Claude Code、Codex 与自研 agent 装进同一个本地优先工作区，并通过本地文件化共享记忆、MCP、OAuth
    与技能市场打通多 agent 上下文与工具链。这种'agent 集成层/本地 OS'思路切中了当前开发者频繁切换 agent、上下文割裂的痛点，开源+企业双轨也具备扩散潜力。但它本质上是一个集成与体验层，核心竞争力取决于多
    agent 协同稳定性、记忆一致性、安全模型与生态落地，尚未构成类似 Transformer 或 ChatGPT 的范式转移。综合判断：重要产品发布，足以搅动局部工具竞争格局，但还不能称为行业拐点。评分
    6.2。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: README 中'一统多 agent、共享记忆、内置全前沿模型、50+ OAuth'等宏大宣称能否在本地安全、API 密钥管理、agent
    冲突与记忆一致性上真正落地
hype_assessment:
  level: medium
  reason: 标题自称'The Computer for You and Your Agent'，文案充斥'no lock-in'、'frontier models
    built in'、'real surfaces, not chat'、'one account, every model'等营销性词汇，且把尚未被社区充分验证的多
    agent 共享记忆、企业级审计等包装成成熟能力。项目确实开源并有安装脚本，但功能广度与体验深度之间存在明显包装水分，故判定为中等炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 技术突破不在于新模型，而在于构建了一个本地优先的'agent 外壳/操作系统'：通过统一的工作区把多个第三方 coding
    agent（Claude Code、Codex）与内置 agent 并置，并以本地文件作为共享记忆、MCP/OAuth 作为工具总线、技能/组合作为可复用工作流，试图把
    agent 从'聊天窗口'升级为可协同、可持久、可扩展的桌面环境。
  business_model: 采用开源社区版（Modified Apache 2.0）+ 免费桌面应用（内置模型按 holaOS 账号计费）+ 企业版（SSO、审计、权限、私有化部署）的三层模式。它可能削弱单一模型厂商对开发者工作流的锁定，把模型/provider
    变成可替换后端；同时通过应用市场和技能组合形成平台佣金/订阅生态，对 Cursor、Windsurf、Claude Code 等垂直 agent IDE 构成替代压力。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: holaOS 试图在本地桌面层构建'Agent 工作空间'这一新中间层，解决多 agent 切换与上下文割裂的痛点，长期来看若形成用户习惯与技能/应用市场生态，具备成为细分基础设施的复利价值。然而其当前形态更偏向于
    Claude Code / Codex 等头部 agent 的聚合外壳与共享记忆层，核心壁垒尚未验证：一是重度依赖 Anthropic、OpenAI 等上游
    agent 的能力与 API 策略，存在被平台方'原生集成'替代的风险；二是开源 + BYOK 模式虽利于获客，但商业变现路径（企业版授权、托管服务）需要大规模用户基数支撑；三是桌面端体验、稳定性与跨应用集成深度仍是早期工程挑战。因此判定为有潜力的中间件方向，但
    3-5 年后能否成为行业基石高度依赖生态采纳与产品执行力，目前处于'需持续验证'区间。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- holaboss-ai
- Anthropic
- OpenAI
- Kimi
- Zhipu AI
competitive_casualty:
- 单一 agent 工具厂商
- 闭源 AI 编程助手
- 传统 RPA 厂商
- 云端独占式 agent 平台
- 缺乏上下文记忆的 AI Wrapper 应用
market_opportunities:
- 开发者与 ISV 可围绕 holaOS 构建垂直领域的 MCP 服务器、技能包（Skills）和 HolaApp，切入其应用市场生态
- 企业服务公司可基于 holaOS 的开源自托管版本，提供私有化部署、SSO 集成、审计合规与内部工具对接的行业解决方案
- 个人开发者可关注本地优先 agent 工作空间的 UX 设计范式，学习其共享记忆、多 agent 协作与 BYOK 模式的产品化经验
risk_matrix:
  regulatory: 产品聚合多地区模型（Kimi、GLM、GPT、Claude 等）并通过 OAuth 连接 Gmail、Slack、微信等应用，可能涉及跨境数据流动、个人信息处理与第三方接口合规问题；企业版若部署在受监管行业，需关注数据本地化、审计留存与访问控制要求。
  technological: 技术替代风险较高：Claude Code、Codex、Cursor、Windsurf 等主流工具均在快速迭代，OpenAI 或 Anthropic
    可能推出官方统一客户端；项目本身依赖第三方模型 API，模型可用性与价格波动会直接影响产品体验。
  competitive: 竞争格局风险显著，agent workspace 赛道已有众多强劲玩家（OpenAI Codex、Anthropic Claude Code、Cursor、GitHub
    Copilot、各类 AI IDE），holaOS 作为新进入者需在生态、性能、安全和企业信任上建立差异化。
  ethical: agent 可驱动真实浏览器、读写本地文件、访问聊天应用并生成多媒体内容，存在越权操作、敏感信息泄露、自动化滥用及生成内容被误用的伦理与社会影响风险；共享记忆机制也可能放大偏见或错误上下文的传播。
  additional:
  - 许可证风险：项目采用 Modified Apache 2.0，需仔细审阅修改条款对企业使用和二次分派的限制
  - 开源项目早期成熟度风险：一键安装脚本、Electron 桌面应用与自托管部署的稳定性尚需社区验证
  - 多 agent 共享同一记忆与工具上下文，可能引入状态污染、权限混淆和难以追踪的连锁错误
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: holaboss-ai/holaOS
  canonical_name: holaOS
  url: https://github.com/holaboss-ai/holaOS
  positioning: holaOS 是 holaboss-ai 开源的本地优先智能体工作空间，旨在让用户在同一桌面运行并管理多个 AI agent。
  technical_signal: 项目采用本地文件化共享记忆架构，支持 MCP 服务器扩展与 OAuth 集成 50 余项服务。
  adoption_signal: 项目提供一键安装脚本与桌面应用，支持 macOS、Linux 与 WSL，降低本地部署门槛。
  ecosystem_relevance: 项目同时兼容 Claude Code、Codex 等主流 agent，并内置多款前沿模型，具备成为 agent 操作系统的潜力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该项目切中多 agent 协作与上下文割裂的痛点，以本地优先和统一工作空间为卖点，若能在企业版安全合规与社区生态上持续发力，有望成为
    agent 基础设施层的重要玩家。
  risk_notes:
  - 新开源项目，长期维护与社区活跃度仍需观察。
  - 企业版 SSO、审计等功能的实际落地效果尚待验证。
  score: 8.0
  article_ids:
  - 4a0bba59f2decb48
  evidence_snippets:
  - holaOS 将自己定位为面向用户及其 agent 的计算机，可在本地优先的工作空间中运行任意 agent。
  - README 指出，Claude Code、Codex 与内置 holaOS agent 可在同一工作区并排运行，无需切换。
  - 项目采用 Modified Apache 2.0 许可，提供桌面应用、开源自托管版及企业版三种形态。
- object_type: product
  name: holaOS Desktop
  canonical_name: holaOS Desktop
  url: null
  positioning: holaOS 的桌面客户端产品，主打下载即用、内置前沿模型、免费开始的本地 agent 工作空间体验。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要本地运行多 agent 的开发者
  - 希望统一管理 AI 工具的普通用户
  - 寻求本地优先方案的企业团队
  product_signal: 桌面应用支持 macOS、Linux 与 WSL 一键安装，内置 Kimi K3、GLM 5.2 等前沿模型，无需 API key
    即可上手。
  market_signal: 产品以“免费开始 + 自带 API key”双模式切入个人与企业市场，覆盖本地自托管与企业版需求。
  differentiation: 与单一 agent 工具不同，桌面版将多个外部与内置 agent 整合到同一工作区并共享记忆和工具。
  watch_reason: 作为 holaOS 项目最直接的产品形态，桌面版降低了普通用户体验多 agent 工作流的门槛，其下载转化、模型调用成本与付费转化路径值得持续关注。
  risk_notes:
  - 桌面客户端的稳定性与跨平台一致性仍需观察。
  - 内置模型成本与免费策略的可持续性存在不确定性。
  score: 7.0
  article_ids:
  - 4a0bba59f2decb48
  evidence_snippets:
  - README 在功能表格中列出 Desktop app，宣称下载即可使用，内置前沿模型且免费开始。
  - 桌面应用支持 macOS、Linux 与 WSL，并提供一键安装脚本以完成新机器初始配置。
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  positioning: Anthropic 推出的终端原生 AI 编程 agent，在 holaOS 中被集成为可并排运行的外部 agent 之一。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 软件开发者
  - 需要代码辅助的技术团队
  product_signal: Claude Code 可在 holaOS 工作区与 Codex 及内置 agent 共享记忆、工具、技能和应用。
  market_signal: 作为 holaOS 重点支持的外部 agent，说明其在开发者市场具备较高认知度和采用基础。
  differentiation: 相对于通用 agent，Claude Code 更专注于代码生成与开发任务，适合在工程工作流中复用。
  watch_reason: holaOS 选择集成 Claude Code 反映出其在开发者群体中的影响力，未来 holaOS 对 Claude Code 的功能封装深度将影响用户切换成本。
  risk_notes:
  - Claude Code 本身并非 holaOS 可控产品，功能更新可能影响集成体验。
  - 在 holaOS 中的运行效果取决于官方 CLI 的兼容性。
  score: 6.0
  article_ids:
  - 4a0bba59f2decb48
  evidence_snippets:
  - README 将 Claude Code 列为可在 holaOS 工作区中运行的外部 agent，与 Codex 及内置 holaOS agent 共享记忆、工具、技能和应用。
- object_type: product
  name: Codex
  canonical_name: OpenAI Codex
  url: null
  positioning: OpenAI 推出的云端 AI 编程 agent，在 holaOS 中作为可与内置 agent 并排运行的外部 agent 被引用。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 软件开发者
  - 希望利用云端模型进行编程辅助的团队
  product_signal: Codex 可在 holaOS 统一工作区内与 Claude Code、内置 agent 共享记忆、工具、技能和应用。
  market_signal: Codex 与 Claude Code 并列被 holaOS 集成，显示 OpenAI 编程 agent 在开发者生态中的竞争力。
  differentiation: 作为云端 agent，Codex 可补充本地 agent 的计算与模型能力，满足复杂工程任务需求。
  watch_reason: Codex 与 Claude Code 同时被 holaOS 纳入，体现项目对多 agent 生态开放性的定位，其云端特性与本地优先架构的协同效果值得观察。
  risk_notes:
  - Codex 的云服务可用性与定价策略会直接影响 holaOS 用户体验。
  - OpenAI 产品迭代节奏可能带来集成兼容风险。
  score: 6.0
  article_ids:
  - 4a0bba59f2decb48
  evidence_snippets:
  - README 将 Codex 列为可在 holaOS 工作区中运行的外部 agent，与 Claude Code 及内置 holaOS agent 共享记忆、工具、技能和应用。
---

**The Computer for You and Your Agent**

Run *any* agent — Claude Code, Codex, or holaOS — in one local-first workspace, over your
tools, your files, and one shared memory. Frontier models built in, or
bring your own keys.

Website · Docs · Sign in · Quick Start

**⭐ If holaOS is useful, a star helps more builders find it.**

Claude Code, Codex, and the built-in holaOS agent — side by side, no switching. Whichever you run, it shares the same memory, tools, skills, and apps. Use the best agent for the job without rebuilding your setup every time.

**No lock-in**— bring the agent you already trust.**Shared everything**— one context, one set of tools, one workspace.**Consistent results**— the same skills and integrations, whatever's driving.

Context, preferences, and project history live in a single shared memory — stored **locally, as plain files you can read and edit.** Switch agents, close the app, come back next week: it already knows where you left off.

**Never start from zero**— durable memory across sessions*and*agents.**Local-first & yours**— on your machine, visible and editable, not locked in someone else's cloud.**Actually recallable**— structured and embedded, so the right context returns when it's needed.

One account, every model — no keys, no setup, no switching between providers. The latest frontier models are **built in**: cost-efficient **Kimi K3** and **GLM 5.2** for everyday volume, plus top-tier **GPT 5.6**, **Claude Opus 5**, and **Fable 5** for the hard problems. Prefer your own provider? **Bring your own keys** for OpenAI, Anthropic, or any OpenAI- or Anthropic-compatible endpoint — those run on *your* account, not your holaOS plan.

**Zero-setup default**— one account, every SOTA model, no API keys to manage.**BYOK when you want it**— your keys, your providers, your rates.**Right model per task**— pick per job, per agent.

Install apps from the in-workspace marketplace and they open as **real, interactive surfaces right beside your agent.** Watch it work inside the app, step in whenever you want, and the result lands in place — not a wall of chat text, but the actual app, driven by the agent, next to the agent.

**Real surfaces, not chat**— every app is a live UI (Notion, a browser, your own app), not a transcript.**Side-by-side by design**— app and agent share the screen, so you always see what's happening and can take over.**One click to install**— browse the in-workspace marketplace and open any app instantly.**Bring your own**— point a HolaApp at any URL and MCP server; it lives on your machine, yours to open and drive.

**Integrations**— connect Gmail, Notion, Slack, GitHub, Linear and 50+ more with one-click OAuth. Agents read and act across your tools, no glue code — and every agent inherits the same connections.**MCP**— plug in any Model Context Protocol server to give your agents new tools. Bring your own, or install community MCP servers in one click.**Skills**— package a workflow once; any agent runs it on demand.**Combos**— bundle skills and integrations into a single one-click install.

**🌐 A real browser, driven by agents**— signed-in browsers your agents drive to browse, click, and extract — under your control.**🎨 Frontier generation built in**— the latest image, video, and audio models inside every agent. Storyboard a video, design a poster, voice a script — one prompt.**📄 Real deliverables**— reports, spreadsheets, and slides saved as real`.xlsx`

,`.pptx`

, and`.docx`

files you can send, not text stuck in a chat.**💬 Reach it from anywhere you chat**— Feishu, WeChat, Slack, Telegram. Send a task from any thread; the result comes back to the same thread.**⏰ Automation**— run on a schedule or a trigger. Digests, monitors, and reports finish and file themselves.

🖥️ Desktop app |
Download and go. Nothing to set up — frontier models built in, free to start. |
🔓 Open source |
Self-host it. Modified Apache 2.0, bring your own keys, run it entirely on your machine. |
🏢 Enterprise |
SSO with per-role permissions for every agent, skill, and app. Connect internal systems without exposing them. Audit logs on every action. On-prem or your own cloud. |

For a fresh-machine bootstrap on macOS, Linux, or WSL, use the repository installer:

`curl -fsSL https://raw.githubusercontent.com/holaboss-ai/holaOS/refs/heads/main/scripts/install.sh | bash -s -- --launch`

You can also follow the manual path if you want to control each setup step.

**If holaOS is useful or interesting, a GitHub Star would be greatly appreciated.**

You likely will not need this section because One-Line Install runs the same setup. Use Manual Install when you want to inspect or control each step. If you use the manual path, verify the usual prerequisites first:

```
git --version
node --version
npm --version
```

If you use Codex, Claude Code, Cursor, Windsurf, or another coding agent, you can hand it the setup instructions in one sentence:

```
Run the holaOS install script from https://raw.githubusercontent.com/holaboss-ai/holaOS/refs/heads/main/scripts/install.sh. It should install git and Node.js 24.14.1/npm if they are missing, clone or update the repo into ~/holaboss-ai unless I specify another --dir, run desktop:install, create apps/desktop/.env from apps/desktop/.env.example if needed, run desktop:prepare-runtime:local and desktop:typecheck, and only run desktop:dev if I ask for --launch. If Electron cannot open, stop after verification and tell me the next manual step.
```


That handoff keeps the installation flow self-contained while leaving the detailed bootstrap steps in the repo-local INSTALL.md runbook.

This is the baseline installation flow for local desktop development.

- Install the desktop dependencies from the repository root:

`npm run desktop:install`

- Create your local environment file:

`cp apps/desktop/.env.example apps/desktop/.env`

If you are following the repo exactly, keep the file close to the template and only change the values that your provider or machine needs.
The canonical path is `apps/desktop/.env`

. Existing legacy `desktop/.env`

files are still accepted for now, but new setups should use `apps/desktop/.env`

.

- Prepare the local runtime bundle:

`npm run desktop:prepare-runtime:local`

- If you want a quick validation pass before launching Electron, run:

`npm run desktop:typecheck`

- Start the desktop app in development mode:

`npm run desktop:dev`

The `predev`

hook will validate the environment, rebuild native modules, and make sure a staged runtime bundle exists.

If you want to stage the runtime before opening the desktop app, there are two common paths:

Build from local runtime:

`npm run desktop:prepare-runtime:local`

Fetch the latest published runtime:

`npm run desktop:prepare-runtime`

Use the local path when you are actively changing runtime code. Use the published bundle when you want to verify the desktop against a known release artifact.

Use `One-Line Install`

when you want the fastest path to a working local desktop environment. Use `Manual Install`

when you need to inspect or control each setup step yourself.

- License: modified Apache 2.0 with additional commercial-distribution and branding conditions. See LICENSE.
- Security issues: report privately to
`admin@holaboss.ai`

. See SECURITY.md.