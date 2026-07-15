---
title: Orca (GitHub Repo)
source: https://github.com/stablyai/orca?utm_source=tldrai
author: []
published: ''
created: '2026-06-26'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aae751d1d8aace5f
source_type: news_media
tldr: Orca 是一个开源 AI 编排器，可并行运行多个 CLI 代码代理（Claude Code、Codex 等）并统一管理。
objective_summary: stablyai 发布了 Orca，一款 MIT 协议的开源 AI 编排桌面工具，支持在独立工作树中并行运行 Codex、Claude
  Code、OpenCode 等多种 CLI 代理，提供跨工作树搜索、账户切换用量追踪、富文件预览和 Computer Use 等功能，并配有
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - stablyai
  technologies:
  - Computer Use
  key_people: []
key_logic_flow:
- Orca 允许用户在独立工作树中并行运行 Codex、Claude Code、OpenCode、Pi 等多种 CLI 代理，并在一个统一界面中追踪所有代理。
- 内置跨工作树快速搜索功能，支持搜索文件、代理、命令和仓库上下文。
- 支持账户切换和 Claude/Codex 用量追踪，可查看使用情况和速率限制重置时间。
- 提供 Markdown、图片、PDF 和仓库文档的富预览功能，以及让代理操控桌面应用的 Computer Use 功能。
- 支持通知推送和未读状态标记，并提供 iOS/Android 移动端配套应用用于远程监控代理。
- Orca 采用 MIT 开源协议，可通过 Homebrew 或 GitHub Releases 获取 macOS、Windows、Linux 各平台构建版本。
extract_result: success
impact_score:
  score: 5.5
  reason: Orca 是一款面向多 CLI 代理并行编排的桌面工具，解决的是开发者同时使用多个 AI 编码代理时的工作流割裂问题。它不是基座模型或基础设施层面的突破，但'独立工作树
    + 统一管理'的模式填补了多代理协作场景下的工具空白。影响范围集中在 AI 辅助编程的用户体验层，对局部竞争格局（如 AI 编码 IDE/工具赛道）有一定重塑力，但尚未达到范式转移级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 在独立工作树中并行运行多个 CLI 代理的工作流编排能力，以及跨代理的统一追踪和管理
hype_assessment:
  level: low
  reason: 描述信息以功能列表为主，没有使用'颠覆性''革命性'等 PR 滥用词汇。功能描述具体可验证（支持代理列表、跨平台构建、移动端配套应用），且有 MIT
    开源协议和 GitHub 仓库作为信任锚点，不存在明显概念包装或过度承诺。
information_entropy: high
domain_disruption:
  technical_innovation: 基于独立工作树的并行多代理编排架构，实现了 CLI 代理的统一生命周期管理、上下文隔离和跨工作树搜索。其'代理无关性'设计（兼容任意
    CLI 代理）降低了多代理协作的技术摩擦。
  business_model: 以 MIT 开源协议免费提供桌面客户端，通过社区（Discord、微信群）运营和移动端配套应用构建生态，走开发者口碑传播路线。不依赖
    API 调用抽成，对 SaaS 商业模式冲击有限。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: Orca 占据了一个日益重要的生态位——多 CLI 代理统一编排层。随着 AI 编码代理（Claude Code、Codex、OpenCode
    等）的数量和专业化程度爆发式增长，开发者需要一个供应商无关的控制平面来管理并行工作流。Orca 的 MIT 开源协议降低了采用门槛，能快速积累用户基础和社区生态，形成网络效应（更多用户→更多代理兼容→更多用户）。其跨工作树搜索、用量追踪、移动端监控等功能也创造了切换成本。但核心风险在于：(1)
    MIT 协议限制了直接货币化能力，stablyai 需要找到可持续的商业化路径（企业版/SaaS）才能支撑 VC 回报；(2) IDE 平台（VS Code、JetBrains）和终端厂商可能原生集成类似能力，挤压独立桌面工具的生存空间；(3)
    该赛道壁垒不高，竞品（如 Goose、Auggie 等）也可快速复制。综合来看，Orca 有潜力成为多 Agent 工作流事实上的桌面入口级基础设施，但变现路径和竞争防御尚需验证。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- stablyai
- Anthropic
- OpenAI
- 所有支持 CLI 的 AI 编码代理项目
competitive_casualty:
- 单代理捆绑式 IDE 插件
- 传统 RPA 厂商
- 闭源 Agent 编排平台
market_opportunities:
- 企业可基于 Orca 构建内部多代理开发工作流平台，统一管理 Claude Code、Codex 等不同 AI 编码助手的调用、监控和用量审计，提升研发效能
- 开发者工具团队可围绕 Orca 的 MIT 开源协议，开发垂直行业插件（如合规审计日志、自动代码审查报告、企业级 SSO 集成），用增值服务建立商业化模式
- 个人开发者可利用 Orca 的并行工作树和移动端远程监控能力，在多项目管理场景中大幅减少上下文切换成本，形成高效的 AI 辅助编程工作流
risk_matrix:
  regulatory: Computer Use 功能代理操控桌面应用，可能触发数据安全合规审查（如 SOC 2、ISO 27001）；跨平台数据同步和移动端远程监控涉及不同司法管辖区的数据出境合规要求
  technological: Orca 依赖第三方 CLI 代理的稳定性和 API 兼容性，上游工具升级或策略变更可能导致集成断裂；Electron 桌面架构在运行多个并行代理时存在内存和
    CPU 资源竞争风险
  competitive: 主流 IDE（VS Code、Cursor）和全栈 AI 平台（Devin、Factory）正在将多代理能力内建到编辑器中，削弱独立编排工具的价值主张；Anthropic
    和 OpenAI 等模型厂商可能推出官方原生编排方案，挤压 Orca 的生态位
  ethical: 并行运行多个 AI 代理放大了模型输出偏见和错误级联的风险，尤其在代码生成场景下可能导致系统性缺陷难以追溯；Computer Use 自动化操控界面可能替代部分人工操作岗位，引发就业冲击争议
  additional:
  - 移动端远程监控特性可能成为企业安全审查的薄弱环节，存在通过手机应用间接泄露代码上下文或敏感项目信息的潜在风险
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
---

Español · Português · 中文 · 日本語 · 한국어

**The AI Orchestrator for 100x builders.**

Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place.

**Also in the box:**

**Quick open**— Search across worktrees, files, agents, commands, and repo context without leaving your flow.**Account switcher & usage tracking**— See Claude and Codex usage and rate-limit resets, and hot-swap accounts without re-logging in.**Rich repo previews**— Preview Markdown, images, PDFs, and repo docs in the workspace.**Computer Use**— Let agents operate desktop apps and visible UI when a workflow needs real interaction.**Notifications and unread state**— Know when an agent finishes or needs attention, then mark threads unread to come back later.**And many, many more**— we ship daily, so this list is perpetually behind. The changelog is the real feature list.

Works with **any CLI agent** — if it runs in a terminal, it runs in Orca.

` Claude Code`
` Codex`
` Grok`
` Cursor`
` GitHub Copilot`
` OpenCode`
` MiMo Code`
` Amp`
` OpenClaude`
` Antigravity`
` Pi`
` oh-my-pi`
` Hermes Agent`
` Devin`
` Goose`
` Auggie`
` Autohand Code`
` Charm`
` Cline`
` Codebuff`
` Command Code`
` Continue`
` Droid`
` Kilocode`
` Kimi`
` Kiro`
` Mistral Vibe`
` Qwen Code`
` Rovo Dev`
`+ any CLI agent`

**Download from onOrca.dev**- Or grab a build directly: macOS Apple Silicon · macOS Intel · Windows (.exe) · Linux AppImage · All builds
- Running
`orca serve`

on a headless Linux server? See the headless Linux server guide.

*Or via a package manager:*

```
# macOS (Homebrew)
brew install --cask stablyai/orca/orca
# Arch Linux (AUR) — or stably-orca-git to build from source
yay -S stably-orca-bin
```

Pair with your desktop app to monitor and steer your agents from your phone.

**iOS:**Download on the App Store or join TestFlight**Android:**Download APK 0.0.27

-
**Discord:**Join the community on**Discord**. -
**Twitter / X:**Follow**@orca_build**for updates and announcements. -
**WeChat:**Scan the QR code to join the community. If the first group is full, use the backup group. -
**Feedback & Ideas:**We ship fast. Missing something? Request a new feature. -
**Privacy:**See the privacy & telemetry docs for what anonymous usage data Orca collects and how to opt out. -
**Show Support:**Star this repo to follow along with our daily ships.

Want to contribute or run locally? See our CONTRIBUTING.md guide.

Orca is free and open source under the MIT License.