---
title: dotnet/skills
source: https://github.com/dotnet/skills
author: []
published: ''
created: '2026-05-22'
description: 'Repository for skills to assist AI coding agents with .NET and C#.NET
  Agent Skills This repository contains the .NET team''s curated set of core skills
  and custom agents for coding agents. For information about the Agent Skills standard,
  see agentskills.io. 📊 Dashboard - Accuracy and efficiency scoring trends for contained
  plugins (https://dotnet.github.io/skills/) What''s Included Plugin Description dotnet
  Collection of core .NET skills for handling common .NET coding tasks. dotnet-data
  Skills for .NET data access and Entity Framework related tasks. dotnet-diag Skills
  for .NET performance investigations, debugging, and incident analysis. dotnet-msbuild
  Comprehensive MSBuild and .NET build skills: failure diagnosis, performance optimization,
  code quality, and modernization. dotnet-nuget NuGet and .NET package management:
  dependency management and modernization. dotnet-upgrade Skills for migrating and
  upgrading .NET projects across framework versions, language features, and compatibility
  targets. dotnet-maui Skills for .NET MAUI development: environment setup, diagnostics,
  and troubleshooting. dotnet-ai AI and ML skills for .NET: technology selection,
  LLM integration, agentic workflows, RAG pipelines, MCP, and classic ML with ML.NET.
  dotnet-template-engine .NET Template Engine skills: template discovery, project
  scaffolding, and template authoring. dotnet-test Skills for running, diagnosing,
  and migrating .NET tests: test execution, filtering, platform detection, and MSTest
  workflows. dotnet-aspnet ASP.NET Core web development skills including middleware,
  endpoints, real-time communication, and API patterns. dotnet11 Skills for new .NET
  11 APIs and language features. Installation 🚀 Plugins - Copilot CLI / Claude Code
  Launch Copilot CLI or Claude Code Add the marketplace:/plugin marketplace add dotnet/skills
  Install a plugin:/plugin install <plugin>@dotnet-agent-skills Restart to load the
  new plugins View available skills:/skills View available agents:/agents Update plugin
  (on demand):/plugin update <plugin>@dotnet-agent-skills VS Code / VS Code Insiders
  (Preview) Important VS Code plugin support is a preview feature and subject to change.
  You may need to enable it first. // settings.json { "chat.plugins.enabled": true,
  "chat.plugins.marketplaces": ["dotnet/skills"] } Once configured, type /plugins
  in Copilot Chat or use the @agentPlugins filter in Extensions to browse and install
  plugins from the marketplace. Cursor This repository is a Cursor plugin marketplace.
  You can discover and install published plugins directly in Cursor: Open the marketplace
  panel in Cursor Search for .NET or browse cursor.com/marketplace Install the desired
  plugins For local development or unpublished changes, import plugins from a local
  checkout: Copy or symlink your local checkout to ~/.cursor/plugins/local/dotnet-agent-skills
  Restart Cursor or run Developer: Reload Window Codex CLI Skills in this repository
  follow the agentskills.io open standard and are compatible with OpenAI Codex. Install
  individual skills using the skill-installer CLI with the GitHub URL: $ skill-installer
  install https://github.com/dotnet/skills/tree/main/plugins/<plugin>/skills/<skill-name>
  Contributing See CONTRIBUTING.md for contribution guidelines and how to add a new
  plugin. License See LICENSE for details.'
tags:
- clippings
extraction_status: success
id: 5cf3a28e1bfde5ac
source_type: community_discussion
tldr: 微软 .NET 团队发布 dotnet/skills 开源仓库，提供 12 个面向 AI 编码智能体的技能插件，兼容多平台。
objective_summary: 微软 .NET 团队在 GitHub 发布了 dotnet/skills 仓库，这是一套面向 AI 编码智能体的精选核心技能与自定义智能体集合，遵循
  agentskills.io 开放标准。仓库包含 12 个插件，覆盖 .NET 核心开发、数据访问、诊断调试、MSBuild、NuGet、项目升级、M
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Microsoft
  - dotnet
  technologies:
  - Agent Skills
  - Copilot CLI
  - Claude Code
  - Cursor
  - OpenAI Codex
  - .NET
  - Entity Framework
  - MSBuild
  - NuGet
  - MAUI
  - ML.NET
  - ASP.NET Core
  - MSTest
  - .NET 11
  key_people: []
key_logic_flow:
- 微软 .NET 团队在 GitHub 上以 dotnet/skills 名义发布了一个开源技能仓库，作为 AI 编码智能体的插件市场
- 该仓库遵循 agentskills.io 开放标准，确保技能在不同 AI 编码平台间具有互操作性
- 仓库共包含 12 个插件，分别覆盖 .NET 核心开发、数据访问（EF）、性能诊断、MSBuild 构建、NuGet 包管理、项目升级迁移、MAUI 跨平台开发、AI/ML
  集成、模板引擎、测试、ASP.NET Core 及 .NET 11 新 API 等领域
- 用户可在 Copilot CLI、Claude Code 中通过 /plugin marketplace add 命令添加市场并安装插件，也可在 VS Code
  Copilot Chat 中启用插件预览功能
- 该仓库同时也是 Cursor 插件市场，用户可在 Cursor 内直接搜索安装；对于 OpenAI Codex，可通过 skill-installer CLI
  按 GitHub URL 安装单个技能
pipeline_stage: fact_extracted
impact_score:
  score: 6.5
  reason: 微软 .NET 团队以官方身份发布遵循 agentskills.io 开放标准的技能插件仓库，标志着 AI 编码智能体从'通用对话'向'专业化技能生态'演进的关键一步。12
    个插件覆盖 .NET 全栈开发链路，且原生兼容 Copilot CLI、Claude Code、Cursor、OpenAI Codex 四大平台，具有跨生态示范效应。但当前影响面仍局限于
    .NET 开发者圈层，尚未构成全行业范式转移，故评分 6.5——属于改变局部竞争格局的重要产品发布，距行业范式转移尚有距离。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 开放标准 agentskills.io 能否真正实现跨平台技能互操作，以及插件市场的发现-安装-更新体验是否流畅
hype_assessment:
  level: low
  reason: 文章为 GitHub README 风格的技术文档，以表格陈列 12 个插件的具体能力边界，附精确的 CLI 安装命令和多平台配置示例，并公开了准确率与效率评分仪表盘。全文未出现'颠覆''革命性'等
    PR 滥用词汇，信息呈现克制、务实。
information_entropy: high
domain_disruption:
  technical_innovation: 核心突破不在于单个技能的实现，而在于 agentskills.io 开放标准层——将 AI 编码智能体的领域知识封装为可发现、可安装、可更新的标准化技能单元，实现跨
    Claude Code、Copilot CLI、Cursor、Codex 等异构平台的技能可移植性。这类似于为 AI 编码智能体构建了'插件操作系统'抽象层。
  business_model: 该仓库实质上是一个 AI 编码智能体的'技能市场'雏形。微软以 .NET 生态为切入点率先卡位，若 agentskills.io
    标准获得广泛采纳，技能分发可能成为开发者工具链的新入口——替代传统文档和 Stack Overflow 的'搜索-复制-粘贴'模式，重塑开发者工具的分发与商业化路径。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Agent Skills 开放标准若成为 AI 编码智能体时代的「技能包管理器」，将具备类似 npm/PyPI 的网络效应和长期复利积累。微软以
    .NET 技能市场为锚点率先卡位，拥有三重优势：(1) 全球最大企业开发者生态的既有网络；(2) Copilot/GitHub 的原生分发渠道；(3) 通过
    agentskills.io 开放标准占据规则定义权。一旦技能生态跨过临界质量，每个新增技能都会增强平台锁定效应，3-5 年后或成为 Agent 时代不可绕过的中间层。但当前评分上限受限于：(a)
    技能仅覆盖 .NET 领域，跨语言通用性待验证；(b) agentskills.io 能否突破微软生态成为全行业共识尚存不确定性；(c) 各 AI 编码平台深度原生集成可能削弱开放标准的必要性。若标准成功破圈至多语言生态，3
    年价值可达 9+ 分；若困于 .NET 利基市场，则回落至 4-5 分。7.5 分反映对该方向战略价值的认可与对执行风险的审慎判断。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Microsoft
- GitHub (Copilot)
- agentskills.io 标准生态
- Anthropic (Claude Code)
- Cursor
- OpenAI (Codex)
competitive_casualty:
- JetBrains AI Assistant
- 未采纳 agentskills 标准的独立 AI 编码工具
- 传统 IDE 插件生态（将被 Agent 技能范式替代）
market_opportunities:
- 开发者或创业团队可基于 agentskills.io 开放标准，为 Python、Rust、Java 等非 .NET 生态构建对应的技能插件市场和兼容层，抢占多语言
  AI 编码智能体的技能标准化红利
- 企业可参考 dotnet/skills 的模式，为内部私有代码库和定制框架开发专属技能插件，提升组织级 AI 辅助编码的一致性和合规性
- AI 编码工具厂商（或独立开发者）可围绕技能插件的质量评测、安全审计和版本治理构建 SaaS 工具链，填补技能市场"可信供应链"的空白
risk_matrix:
  regulatory: 无
  technological: agentskills.io 标准尚处早期，若未来主流 AI 编码代理采用原生的动态上下文理解（无需显式技能声明），此类技能插件架构可能快速过时；此外，微软内部优先级变化可能导致仓库维护停滞
  competitive: 微软通过 dotnet/skills 在 AI 编码代理生态中抢先建立 .NET 优先的技能标准，可能挤压 JetBrains AI
    Assistant、Google Gemini Code Assist 等竞品在 .NET 开发者群体中的渗透空间，形成生态锁定效应
  ethical: 技能插件可能包含有偏见或过时的编码模式（如不安全的数据访问范式），若缺乏有效的审核机制，AI 代理可能在不知情的情况下大规模传播不良实践；此外，恶意参与者可能通过仿冒插件进行供应链投毒
  additional:
  - 碎片化风险：若各语言生态各自建立互不兼容的技能标准（如 Python 社区另起炉灶），agentskills.io 的统一愿景可能落空，导致开发者面临多套标准的学习和维护成本
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
---

This repository contains the .NET team's curated set of core skills and custom agents for coding agents. For information about the Agent Skills standard, see agentskills.io.

**📊 Dashboard** - Accuracy and efficiency scoring trends for contained plugins (https://dotnet.github.io/skills/)

| Plugin | Description |
|---|---|
| dotnet | Collection of core .NET skills for handling common .NET coding tasks. |
| dotnet-data | Skills for .NET data access and Entity Framework related tasks. |
| dotnet-diag | Skills for .NET performance investigations, debugging, and incident analysis. |
| dotnet-msbuild | Comprehensive MSBuild and .NET build skills: failure diagnosis, performance optimization, code quality, and modernization. |
| dotnet-nuget | NuGet and .NET package management: dependency management and modernization. |
| dotnet-upgrade | Skills for migrating and upgrading .NET projects across framework versions, language features, and compatibility targets. |
| dotnet-maui | Skills for .NET MAUI development: environment setup, diagnostics, and troubleshooting. |
| dotnet-ai | AI and ML skills for .NET: technology selection, LLM integration, agentic workflows, RAG pipelines, MCP, and classic ML with ML.NET. |
| dotnet-template-engine | .NET Template Engine skills: template discovery, project scaffolding, and template authoring. |
| dotnet-test | Skills for running, diagnosing, and migrating .NET tests: test execution, filtering, platform detection, and MSTest workflows. |
| dotnet-aspnet | ASP.NET Core web development skills including middleware, endpoints, real-time communication, and API patterns. |
| dotnet11 | Skills for new .NET 11 APIs and language features. |

- Launch Copilot CLI or Claude Code
- Add the marketplace:
`/plugin marketplace add dotnet/skills`

- Install a plugin:
`/plugin install <plugin>@dotnet-agent-skills`

- Restart to load the new plugins
- View available skills:
`/skills`

- View available agents:
`/agents`

- Update plugin (on demand):
`/plugin update <plugin>@dotnet-agent-skills`


Important

VS Code plugin support is a preview feature and subject to change. You may need to enable it first.

```
// settings.json
{
"chat.plugins.enabled": true,
"chat.plugins.marketplaces": ["dotnet/skills"]
}
```

Once configured, type `/plugins`

in Copilot Chat or use the `@agentPlugins`

filter in Extensions to browse and install plugins from the marketplace.

This repository is a Cursor plugin marketplace. You can discover and install published plugins directly in Cursor:

- Open the marketplace panel in Cursor
- Search for
`.NET`

or browse cursor.com/marketplace - Install the desired plugins

For local development or unpublished changes, import plugins from a local checkout:

- Copy or symlink your local checkout to
`~/.cursor/plugins/local/dotnet-agent-skills`

- Restart Cursor or run
**Developer: Reload Window**

Skills in this repository follow the agentskills.io open standard and are compatible with OpenAI Codex.

Install individual skills using the `skill-installer`

CLI with the GitHub URL:

`$ skill-installer install https://github.com/dotnet/skills/tree/main/plugins/<plugin>/skills/<skill-name>`

See CONTRIBUTING.md for contribution guidelines and how to add a new plugin.

See LICENSE for details.