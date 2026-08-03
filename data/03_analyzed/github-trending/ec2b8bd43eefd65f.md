---
title: NousResearch/hermes-agent
source: https://github.com/NousResearch/hermes-agent
author: []
published: ''
created: '2026-06-08'
description: 'The agent that grows with you Hermes Agent ☤ The self-improving AI agent
  built by Nous Research. It''s the only agent with a built-in learning loop — it
  creates skills from experience, improves them during use, nudges itself to persist
  knowledge, searches its own past conversations, and builds a deepening model of
  who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure
  that costs nearly nothing when idle. It''s not tied to your laptop — talk to it
  from Telegram while it works on a cloud VM. Use any model you want — Nous Portal,
  OpenRouter (200+ models), NovitaAI (AI-native cloud for Model API, Agent Sandbox,
  and GPU Cloud), NVIDIA NIM (Nemotron), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax,
  Hugging Face, OpenAI, or your own endpoint. Switch with hermes model — no code changes,
  no lock-in. A real terminal interface Full TUI with multiline editing, slash-command
  autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.
  Lives where you do Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from
  a single gateway process. Voice memo transcription, cross-platform conversation
  continuity. A closed learning loop Agent-curated memory with periodic nudges. Autonomous
  skill creation after complex tasks. Skills self-improve during use. FTS5 session
  search with LLM summarization for cross-session recall. Honcho dialectic user modeling.
  Compatible with the agentskills.io open standard. Scheduled automations Built-in
  cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly
  audits — all in natural language, running unattended. Delegates and parallelizes
  Spawn isolated subagents for parallel workstreams. Write Python scripts that call
  tools via RPC, collapsing multi-step pipelines into zero-context-cost turns. Runs
  anywhere, not just your laptop Six terminal backends — local, Docker, SSH, Singularity,
  Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent''s
  environment hibernates when idle and wakes on demand, costing nearly nothing between
  sessions. Run it on a $5 VPS or a GPU cluster. Research-ready Batch trajectory generation,
  trajectory compression for training the next generation of tool-calling models.
  Quick Install Linux, macOS, WSL2, Termux curl -fsSL https://hermes-agent.nousresearch.com/install.sh
  | bash Windows (native, PowerShell) Heads up: Native Windows runs Hermes without
  WSL — CLI, gateway, TUI, and tools all work natively. If you''d rather use WSL2,
  the Linux/macOS one-liner above works there too. Found a bug? Please file issues.
  Run this in PowerShell: iex (irm https://hermes-agent.nousresearch.com/install.ps1)
  The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, and
  a portable Git Bash (MinGit, unpacked to %LOCALAPPDATA%\hermes\git — no admin required,
  completely isolated from any system Git install). Hermes uses this bundled Git Bash
  to run shell commands. If you already have Git installed, the installer detects
  it and uses that instead. Otherwise a ~45MB MinGit download is all you need — it
  won''t touch or interfere with any system Git. Android / Termux: The tested manual
  path is documented in the Termux guide. On Termux, Hermes installs a curated .[termux]
  extra because the full .[all] extra currently pulls Android-incompatible voice dependencies.
  Windows: Native Windows is fully supported — the PowerShell one-liner above installs
  everything. If you''d rather use WSL2, the Linux command works there too. Native
  Windows install lives under %LOCALAPPDATA%\hermes; WSL2 installs under ~/.hermes
  as on Linux. The only Hermes feature that currently needs WSL2 specifically is the
  browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway
  both run natively). After installation: source ~/.bashrc # reload shell (or: source
  ~/.zshrc) hermes # start chatting! Getting Started hermes # Interactive CLI — start
  a conversation hermes model # Choose your LLM provider and model hermes tools #
  Configure which tools are enabled hermes config set # Set individual config values
  hermes gateway # Start the messaging gateway (Telegram, Discord, etc.) hermes setup
  # Run the full setup wizard (configures everything at once) hermes claw migrate
  # Migrate from OpenClaw (if coming from OpenClaw) hermes update # Update to the
  latest version hermes doctor # Diagnose any issues 📖 Full documentation → Skip the
  API-key collection — Nous Portal Hermes works with whatever provider you want —
  that''s not changing. But if you''d rather not collect five separate API keys for
  the model, web search, image generation, TTS, and a cloud browser, Nous Portal covers
  all of them under one subscription: 300+ models — pick any of them with /model <name>
  Tool Gateway — web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI),
  cloud browser (Browser Use), all routed through your sub. No extra accounts. One
  command from a fresh install: hermes setup --portal That logs you in via OAuth,
  sets Nous as your provider, and turns on the Tool Gateway. Check what''s wired up
  any time with hermes portal info. Full details on the Tool Gateway docs page. You
  can still bring your own keys per-tool whenever you want — the gateway is per-backend,
  not all-or-nothing. CLI vs Messaging Quick Reference Hermes has two entry points:
  start the terminal UI with hermes, or run the gateway and talk to it from Telegram,
  Discord, Slack, WhatsApp, Signal, or Email. Once you''re in a conversation, many
  slash commands are shared across both interfaces. Action CLI Messaging platforms
  Start chatting hermes Run hermes gateway setup + hermes gateway start, then send
  the bot a message Start fresh conversation /new or /reset /new or /reset Change
  model /model [provider:model] /model [provider:model] Set a personality /personality
  [name] /personality [name] Retry or undo the last turn /retry, /undo /retry, /undo
  Compress context / check usage /compress, /usage, /insights [--days N] /compress,
  /usage, /insights [days] Browse skills /skills or /<skill-name> /<skill-name> Interrupt
  current work Ctrl+C or send a new message /stop or send a new message Platform-specific
  status /platforms /status, /sethome For the full command lists, see the CLI guide
  and the Messaging Gateway guide. Documentation All documentation lives at hermes-agent.nousresearch.com/docs:
  Section What''s Covered Quickstart Install → setup → first conversation in 2 minutes
  CLI Usage Commands, keybindings, personalities, sessions Configuration Config file,
  providers, models, all options Messaging Gateway Telegram, Discord, Slack, WhatsApp,
  Signal, Home Assistant Security Command approval, DM pairing, container isolation
  Tools & Toolsets 40+ tools, toolset system, terminal backends Skills System Procedural
  memory, Skills Hub, creating skills Memory Persistent memory, user profiles, best
  practices MCP Integration Connect any MCP server for extended capabilities Cron
  Scheduling Scheduled tasks with platform delivery Context Files Project context
  that shapes every conversation Architecture Project structure, agent loop, key classes
  Contributing Development setup, PR process, code style CLI Reference All commands
  and flags Environment Variables Complete env var reference Migrating from OpenClaw
  If you''re coming from OpenClaw, Hermes can automatically import your settings,
  memories, skills, and API keys. During first-time setup: The setup wizard (hermes
  setup) automatically detects ~/.openclaw and offers to migrate before configuration
  begins. Anytime after install: hermes claw migrate # Interactive migration (full
  preset) hermes claw migrate --dry-run # Preview what would be migrated hermes claw
  migrate --preset user-data # Migrate without secrets hermes claw migrate --overwrite
  # Overwrite existing conflicts What gets imported: SOUL.md — persona file Memories
  — MEMORY.md and USER.md entries Skills — user-created skills → ~/.hermes/skills/openclaw-imports/
  Command allowlist — approval patterns Messaging settings — platform configs, allowed
  users, working directory API keys — allowlisted secrets (Telegram, OpenRouter, OpenAI,
  Anthropic, ElevenLabs) TTS assets — workspace audio files Workspace instructions
  — AGENTS.md (with --workspace-target) See hermes claw migrate --help for all options,
  or use the openclaw-migration skill for an interactive agent-guided migration with
  dry-run previews. Contributing We welcome contributions! See the Contributing Guide
  for development setup, code style, and PR process. Quick start for contributors
  — clone and go with setup-hermes.sh: git clone https://github.com/NousResearch/hermes-agent.git
  cd hermes-agent ./setup-hermes.sh # installs uv, creates venv, installs .[all],
  symlinks ~/.local/bin/hermes ./hermes # auto-detects the venv, no need to `source`
  first Manual path (equivalent to the above): curl -LsSf https://astral.sh/uv/install.sh
  | sh uv venv .venv --python 3.11 source .venv/bin/activate uv pip install -e ".[all,dev]"
  scripts/run_tests.sh Community 💬 Discord 📚 Skills Hub 🐛 Issues 🔌 computer-use-linux
  — Linux desktop-control MCP server for Hermes and other MCP hosts, with AT-SPI accessibility
  trees, Wayland/X11 input, screenshots, and compositor window targeting. 🔌 HermesClaw
  — Community WeChat bridge: Run Hermes Agent and OpenClaw on the same WeChat account.
  License MIT — see LICENSE. Built by Nous Research.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ec2b8bd43eefd65f
source_type: community_discussion
tldr: Nous Research 发布了开源 AI 代理 Hermes Agent，具备内置自我改进学习循环、跨平台消息网关和多模型支持，可在低至 5 美元的
  VPS 或云服务器上运行。
objective_summary: Nous Research 发布了开源 AI 代理项目 Hermes Agent，该代理具有内置的闭环学习系统，能够从经验中自主创建技能、在对话过程中自我改进、通过周期性提醒持久化知识，并在跨会话场景下构建用户画像建模。Hermes
  Agent 支持超过 300 种模型，可通过 Nous Portal、OpenRouter、OpenAI、Hugging Face、NVIDIA 等提供商切换，同时支持六种终端后端（本地、Docker、SSH、Singularity、Modal
  和 Daytona）以及 Telegram、Discord、Slack、WhatsApp、Signal 和 CLI 等多个消息平台。项目还提供了从 OpenClaw
  的自动迁移工具、内置 cron 调度器、子代理并行处理以及 MCP 集成等高级能力。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Nous Research
  - OpenAI
  - NVIDIA
  - Hugging Face
  - Xiaomi
  - MiniMax
  - NovitaAI
  technologies:
  - MCP
  - FTS5
  - RPC
  - OAuth
  key_people: []
key_logic_flow:
- Nous Research 发布了开源 AI 代理项目 Hermes Agent，其核心特性是内置闭环学习系统，使代理能够从对话经验中自主创建技能并在使用过程中不断自我改进。
- Hermes Agent 提供本地、Docker、SSH、Singularity、Modal 和 Daytona 共六种终端后端，可在低至 5 美元的 VPS
  到 GPU 集群上灵活部署，并结合 Modal 或 Daytona 的服务器无状态持久化能力以降低成本。
- 通过单一网关服务，Hermes Agent 同时连接 Telegram、Discord、Slack、WhatsApp、Signal 和 CLI 等多个平台，支持语音转录和跨平台对话连续性。
- 用户可通过 /model 命令在超过 300 种模型间自由切换，支持的提供商包括 OpenAI、NVIDIA、Hugging Face、Xiaomi 和 MiniMax
  等，无需修改代码。
- Hermes Agent 提供了从 OpenClaw 的自动迁移工具，可导入设置、记忆、技能和 API 密钥，并支持全量迁移、预览模式和覆盖模式等多种选项。
- 该代理内置 cron 调度器用于无人值守的自动化任务，并支持隔离子代理进行并行处理，可将多步流水线压缩为零上下文开销的单轮调用。
extract_result: success
object_mentions:
- object_type: project
  name: NousResearch/hermes-agent
  canonical_name: hermes-agent
  url: https://github.com/NousResearch/hermes-agent
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Nous Research 发布了开源 AI 代理项目 Hermes Agent，其最大特点是内置闭环学习系统，使代理能够从对话经验中自主创建技能并在使用过程中不断自我改进与优化。
  - Hermes Agent 提供了本地、Docker、SSH、Singularity、Modal 和 Daytona 共六种终端后端选择，可在低至 5 美元的
    VPS 或 GPU 集群上灵活部署运行。
  - 该项目提供从 OpenClaw 的自动迁移工具、内置 cron 调度器、子代理并行处理以及 MCP 集成等高级功能。
  article_id: ec2b8bd43eefd65f
- object_type: product
  name: Nous Portal
  canonical_name: Nous Portal
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Nous Portal 是 Nous Research 提供的订阅服务，涵盖 300 多种模型选择和一个统一的工具网关。
  - 通过 hermes setup --portal 命令可一键完成 OAuth 登录并配置 Nous Portal 为模型和工具提供商。
  - 工具网关将网页搜索、图像生成、语音合成和云浏览器等能力全部路由到用户订阅中，无需额外账户和 API 密钥。
  article_id: ec2b8bd43eefd65f
- object_type: project
  name: OpenClaw
  canonical_name: OpenClaw
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Hermes Agent 提供 hermes claw migrate 命令，可从 OpenClaw 自动导入记忆、技能、设置和 API 密钥。
  - OpenClaw 迁移支持全量迁移、预览模式、仅用户数据迁移和覆盖模式等多种选项以满足不同需求。
  article_id: ec2b8bd43eefd65f
- object_type: project
  name: computer-use-linux
  canonical_name: computer-use-linux
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - computer-use-linux 是 Nous Research 提供的 Linux 桌面控制 MCP 服务器，支持 Hermes Agent 和其他
    MCP 主机。
  - 该工具支持 AT-SPI 无障碍树解析、Wayland 和 X11 输入模拟、屏幕截图以及合成器窗口定位等桌面控制能力。
  article_id: ec2b8bd43eefd65f
- object_type: project
  name: HermesClaw
  canonical_name: HermesClaw
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - HermesClaw 是社区开发维护的微信桥接项目，可在同一微信账号上同时运行 Hermes Agent 和 OpenClaw。
  article_id: ec2b8bd43eefd65f
- object_type: project
  name: agentskills.io
  canonical_name: agentskills.io
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Hermes Agent 兼容 agentskills.io 开放标准，该标准定义了 AI 代理技能的可互操作格式。
  article_id: ec2b8bd43eefd65f
impact_score:
  score: 6.8
  reason: Hermes Agent 是开源智能体领域的一个重要发布，其核心差异化在于内置学习循环——自主创建技能、跨会话记忆和用户画像建模。这些能力组合在开源生态中尚属首次，可能改变开发者构建持久化
    AI 代理的方式。但影响有限：1）学习循环的有效性需要社区验证，目前仍偏研究性质；2）单个 agent 框架不足以构成行业范式转移，类似概念在 AutoGPT、CrewAI
    等项目中已有探索；3）整体架构更接近功能丰富的工程集成，而非底层技术突破。综合判定为重要产品发布级别（6-7 分段），将改变开源代理框架的竞争格局，但不构成
    ChatGPT 式的行业地震。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 自主技能创建和学习循环是否真能摆脱人工编排，实现自我进化的 AI 代理
hype_assessment:
  level: medium
  reason: 文章使用了 'the only agent with a built-in learning loop'、'self-improving' 等强势
    PR 词汇，这是典型的差异化营销话术。实际技术分析：学习循环（自主技能创建+跨会话记忆）确实新颖且代码已开源，但 'the only' 的排他性声称经不起推敲（AutoGPT
    的记忆系统、LangChain 的 agent 循环等已有类似概念）。项目提供了充分的安装文档、架构细节和部署选项，干货充足，但 '革命性自我进化' 的包装痕迹明显，水分中等。
information_entropy: high
domain_disruption:
  technical_innovation: 提出了闭环学习循环的技术架构，核心创新在于将自主技能创建（从复杂任务轨迹中提取可复用技能）、跨会话记忆（FTS5 向量搜索
    + LLM 摘要）、Honcho 辩证用户建模三者深度耦合，形成一个持续自我改进的环路。此外，多平台单一网关进程（Telegram/Discord/Slack
    等共享同一 agent 实例）和子代理并行化（RPC 调用折叠多步管线为零上下文开销）在工程实现上也有独到之处。
  business_model: 采用 MIT 开源核心 + Nous Portal 付费订阅（工具网关：搜索、图像生成、TTS、云浏览器等一站式服务）的双层商业模式。这种
    '开源获客 + 云服务变现' 模式可能冲击闭源代理即服务市场（如 OpenAI 的 GPTs），让中小团队能以极低成本（$5 VPS）部署具备类似能力的代理。同时
    agentskills.io 开放标准兼容性有助于构建技能生态，形成网络效应。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: Hermes Agent 的核心创新在于闭环学习循环——自主创建技能、跨会话记忆、用户画像建模——这些能力具有明显的复利效应：使用越多，代理越了解用户和任务，数据累积带来的切换成本越高。MIT
    开源许可降低了采用门槛，但也意味着核心技术无法独占，任何人都可 fork 复用。300+ 模型支持和多平台网关（Telegram/Discord/Slack
    等）消除了平台锁定风险，极低运行成本（$5 VPS / 无服务器休眠计费）大幅降低了用户获取门槛。但代理框架赛道极为拥挤（OpenAI Agents SDK、LangChain、CrewAI、AutoGPT
    等），Nous Research 作为研究机构的工程化和商业化能力待验证。综合判断：有潜力成为 Agent 基础设施关键组件，但开放式许可和竞争格局限制了价值捕获上界。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Nous Research
- Modal
- Daytona
- OpenRouter
- NovitaAI
competitive_casualty:
- 闭源 Agent 框架
- 传统 RPA 厂商
- 单平台 Agent 工具
market_opportunities:
- 企业可将 Hermes Agent 部署为内部自进化 AI 助手，利用其跨平台网关（Slack/Telegram/Discord）和长期记忆能力，在 DevOps
  运维、日报生成和知识管理场景中实现无人值守的持续优化
- 个人开发者可基于其 agentskills.io 兼容标准构建垂直技能包（如代码审计、SEO 分析、合规检查），通过开放技能市场变现，形成新的 AI Agent
  插件经济生态
- 云服务商（如 Modal、Daytona）可推出 Hermes Agent 托管服务，结合其无服务器持久化特性（空闲休眠、按需唤醒），为企业客户提供零运维成本的
  AI Agent 基础设施方案
risk_matrix:
  regulatory: 具备自主技能创建和跨会话用户画像建模能力的开源代理，在 EU AI Act 下可能被归类为高风险 AI 系统；跨平台语音转录功能在 GDPR
    和各国隐私法下存在未明确告知同意的合规风险；自主技能自我改进机制可能引发 AI 安全审查与责任界定难题
  technological: 自我改进循环的实际效果尚未经过第三方实证验证，可能存在边际收益递减问题；依赖 300+ 第三方模型提供商和多个外部 API（Firecrawl、FAL、Browser
    Use），单点故障风险较高；同类框架（AutoGPT、CrewAI、LangGraph）持续迭代可能导致差异化优势缩小
  competitive: OpenAI、Anthropic 和 Google 正在其平台中构建原生 Agent 能力，可能挤压开源替代方案的生态空间；微软 Copilot、字节跳动
    Coze 等商业产品已在 Agent 编排和跨平台集成上投入重兵，形成先发用户黏性
  ethical: 跨会话记忆和 Honcho 用户建模可能导致长期隐私侵蚀，用户难以追踪和控制代理已积累的个人信息；自主技能创建缺乏人工审核机制，存在生成有害或偏见技能的潜在风险；语音备忘录转录功能若未经明确知情同意，可能违反数据最小化原则
  additional:
  - 虽声称 MIT 开源，但全功能体验依赖 Nous Portal 订阅（单一供应商锁定），存在"开源引流、闭源变现"的隐性风险
  - 单一网关进程架构存在单点崩溃风险，长时间运行后内存泄漏或进程级故障可能导致跨平台服务中断
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: NousResearch/hermes-agent
  canonical_name: hermes-agent
  url: https://github.com/NousResearch/hermes-agent
  positioning: Nous Research 开发的开源 AI 代理项目，核心特色是内置闭环学习系统，使代理能从经验中自主创建技能并在使用中持续自我改进。
  technical_signal: 内置闭环学习系统使代理能够从对话经验中自主创建技能，通过周期性提醒持久化知识，并支持 FTS5 跨会话搜索与 LLM 摘要召回。
  adoption_signal: 支持六种终端后端和低至 5 美元的 VPS 部署，同时提供 Telegram、Discord、Slack、WhatsApp、Signal
    和 CLI 跨平台消息网关服务。
  ecosystem_relevance: 支持超过 300 种模型，可通过 Nous Portal、OpenRouter、OpenAI、Hugging Face、NVIDIA
    等提供商灵活切换，并兼容 agentskills.io 开放标准与 MCP 集成。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Hermes Agent 的闭环自我改进机制在开源 AI 代理领域具有独特性，能从经验中创建技能并跨会话建模用户画像。支持低至 5
    美元 VPS 到 GPU 集群的灵活部署，显著降低了 AI 代理的实际使用门槛与持续运营成本。
  risk_notes:
  - 与 LangChain、CrewAI 等已有开源 AI 代理框架存在直接竞争，其闭环学习机制的差异化优势在实际复杂场景中尚需大规模验证。
  - 项目依赖多个第三方模型提供商和基础设施服务，长期运营的稳定性对提供商生态有较强依赖。
  score: 8.0
  article_ids:
  - ec2b8bd43eefd65f
  evidence_snippets:
  - Nous Research 发布了开源 AI 代理项目 Hermes Agent，其最大特点是内置闭环学习系统，使代理能够从对话经验中自主创建技能并在使用过程中不断自我改进与优化。
  - Hermes Agent 提供了本地、Docker、SSH、Singularity、Modal 和 Daytona 共六种终端后端选择，可在低至 5 美元的
    VPS 或 GPU 集群上灵活部署运行。
  - 该项目提供从 OpenClaw 的自动迁移工具、内置 cron 调度器、子代理并行处理以及 MCP 集成等高级功能。
- object_type: project
  name: OpenClaw
  canonical_name: OpenClaw
  url: null
  positioning: 与 Hermes Agent 存在数据迁移兼容关系的开源 AI 代理项目，用户可通过迁移工具导入记忆、技能、设置和 API 密钥等核心数据。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: OpenClaw 作为被 Hermes Agent 提供自动迁移工具的开源 AI 代理项目，其记忆和技能数据格式可能影响 Hermes
    用户的迁移体验，值得关注其与 Hermes 生态的整合进展。
  risk_notes:
  - 文章仅提及 Hermes Agent 对 OpenClaw 的迁移兼容性，未提供 OpenClaw 项目自身的技术细节、活跃度及社区规模信息，评估维度有限。
  score: 3.0
  article_ids:
  - ec2b8bd43eefd65f
  evidence_snippets:
  - Hermes Agent 提供 hermes claw migrate 命令，可从 OpenClaw 自动导入记忆、技能、设置和 API 密钥。
  - OpenClaw 迁移支持全量迁移、预览模式、仅用户数据迁移和覆盖模式等多种选项以满足不同需求。
---

**The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — Nous Portal, OpenRouter (200+ models), NovitaAI (AI-native cloud for Model API, Agent Sandbox, and GPU Cloud), NVIDIA NIM (Nemotron), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, or your own endpoint. Switch with `hermes model`

— no code changes, no lock-in.

A real terminal interface | Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output. |
Lives where you do | Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity. |
A closed learning loop | Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling. Compatible with the agentskills.io open standard. |
Scheduled automations | Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended. |
Delegates and parallelizes | Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns. |
Runs anywhere, not just your laptop | Six terminal backends — local, Docker, SSH, Singularity, Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster. |
Research-ready | Batch trajectory generation, trajectory compression for training the next generation of tool-calling models. |

`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`


Heads up:Native Windows runs Hermes without WSL — CLI, gateway, TUI, and tools all work natively. If you'd rather use WSL2, the Linux/macOS one-liner above works there too. Found a bug? Please file issues.

Run this in PowerShell:

`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`

The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, **and a portable Git Bash** (MinGit, unpacked to `%LOCALAPPDATA%\hermes\git`

— no admin required, completely isolated from any system Git install). Hermes uses this bundled Git Bash to run shell commands.

If you already have Git installed, the installer detects it and uses that instead. Otherwise a ~45MB MinGit download is all you need — it won't touch or interfere with any system Git.


Android / Termux:The tested manual path is documented in the Termux guide. On Termux, Hermes installs a curated`.[termux]`

extra because the full`.[all]`

extra currently pulls Android-incompatible voice dependencies.

Windows:Native Windows is fully supported — the PowerShell one-liner above installs everything. If you'd rather use WSL2, the Linux command works there too. Native Windows install lives under`%LOCALAPPDATA%\hermes`

; WSL2 installs under`~/.hermes`

as on Linux. The only Hermes feature that currently needs WSL2 specifically is the browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway both run natively).

After installation:

```
source ~/.bashrc # reload shell (or: source ~/.zshrc)
hermes # start chatting!
```

```
hermes # Interactive CLI — start a conversation
hermes model # Choose your LLM provider and model
hermes tools # Configure which tools are enabled
hermes config set # Set individual config values
hermes gateway # Start the messaging gateway (Telegram, Discord, etc.)
hermes setup # Run the full setup wizard (configures everything at once)
hermes claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes update # Update to the latest version
hermes doctor # Diagnose any issues
```

Hermes works with whatever provider you want — that's not changing. But if you'd rather not collect five separate API keys for the model, web search, image generation, TTS, and a cloud browser, **Nous Portal** covers all of them under one subscription:

**300+ models**— pick any of them with`/model <name>`

**Tool Gateway**— web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI), cloud browser (Browser Use), all routed through your sub. No extra accounts.

One command from a fresh install:

`hermes setup --portal`

That logs you in via OAuth, sets Nous as your provider, and turns on the Tool Gateway. Check what's wired up any time with `hermes portal info`

. Full details on the Tool Gateway docs page.

You can still bring your own keys per-tool whenever you want — the gateway is per-backend, not all-or-nothing.

Hermes has two entry points: start the terminal UI with `hermes`

, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action | CLI | Messaging platforms |
|---|---|---|
| Start chatting | `hermes` |
Run `hermes gateway setup` + `hermes gateway start` , then send the bot a message |
| Start fresh conversation | `/new` or `/reset` |
`/new` or `/reset` |
| Change model | `/model [provider:model]` |
`/model [provider:model]` |
| Set a personality | `/personality [name]` |
`/personality [name]` |
| Retry or undo the last turn | `/retry` , `/undo` |
`/retry` , `/undo` |
| Compress context / check usage | `/compress` , `/usage` , `/insights [--days N]` |
`/compress` , `/usage` , `/insights [days]` |
| Browse skills | `/skills` or `/<skill-name>` |
`/<skill-name>` |
| Interrupt current work | `Ctrl+C` or send a new message |
`/stop` or send a new message |
| Platform-specific status | `/platforms` |
`/status` , `/sethome` |

For the full command lists, see the CLI guide and the Messaging Gateway guide.

All documentation lives at **hermes-agent.nousresearch.com/docs**:

| Section | What's Covered |
|---|---|
| Quickstart | Install → setup → first conversation in 2 minutes |
| CLI Usage | Commands, keybindings, personalities, sessions |
| Configuration | Config file, providers, models, all options |
| Messaging Gateway | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| Security | Command approval, DM pairing, container isolation |
| Tools & Toolsets | 40+ tools, toolset system, terminal backends |
| Skills System | Procedural memory, Skills Hub, creating skills |
| Memory | Persistent memory, user profiles, best practices |
| MCP Integration | Connect any MCP server for extended capabilities |
| Cron Scheduling | Scheduled tasks with platform delivery |
| Context Files | Project context that shapes every conversation |
| Architecture | Project structure, agent loop, key classes |
| Contributing | Development setup, PR process, code style |
| CLI Reference | All commands and flags |
| Environment Variables | Complete env var reference |

If you're coming from OpenClaw, Hermes can automatically import your settings, memories, skills, and API keys.

**During first-time setup:** The setup wizard (`hermes setup`

) automatically detects `~/.openclaw`

and offers to migrate before configuration begins.

**Anytime after install:**

```
hermes claw migrate # Interactive migration (full preset)
hermes claw migrate --dry-run # Preview what would be migrated
hermes claw migrate --preset user-data # Migrate without secrets
hermes claw migrate --overwrite # Overwrite existing conflicts
```

What gets imported:

**SOUL.md**— persona file**Memories**— MEMORY.md and USER.md entries**Skills**— user-created skills →`~/.hermes/skills/openclaw-imports/`

**Command allowlist**— approval patterns**Messaging settings**— platform configs, allowed users, working directory**API keys**— allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)**TTS assets**— workspace audio files**Workspace instructions**— AGENTS.md (with`--workspace-target`

)

See `hermes claw migrate --help`

for all options, or use the `openclaw-migration`

skill for an interactive agent-guided migration with dry-run previews.

We welcome contributions! See the Contributing Guide for development setup, code style, and PR process.

Quick start for contributors — clone and go with `setup-hermes.sh`

:

```
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
./setup-hermes.sh # installs uv, creates venv, installs .[all], symlinks ~/.local/bin/hermes
./hermes # auto-detects the venv, no need to `source` first
```

Manual path (equivalent to the above):

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

- 💬 Discord
- 📚 Skills Hub
- 🐛 Issues
- 🔌 computer-use-linux — Linux desktop-control MCP server for Hermes and other MCP hosts, with AT-SPI accessibility trees, Wayland/X11 input, screenshots, and compositor window targeting.
- 🔌 HermesClaw — Community WeChat bridge: Run Hermes Agent and OpenClaw on the same WeChat account.

MIT — see LICENSE.

Built by Nous Research.