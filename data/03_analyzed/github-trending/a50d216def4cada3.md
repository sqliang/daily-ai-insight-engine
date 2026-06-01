---
title: cursor/plugins
source: https://github.com/cursor/plugins
author: []
published: ''
created: '2026-06-01'
description: 'Cursor plugin specification and official pluginsCursor plugins Official
  Cursor plugins for popular developer tools, frameworks, and SaaS products. Each
  plugin is a standalone directory at the repository root with its own .cursor-plugin/plugin.json
  manifest. Plugins name Plugin Author Category description (from marketplace) continual-learning
  Continual Learning Cursor Developer Tools Incremental transcript-driven memory updates
  for AGENTS.md using high-signal bullet points only. cursor-team-kit Cursor Team
  Kit Cursor Developer Tools Internal team workflows used by Cursor developers for
  CI, code review, shipping, local automation, and verification. thermos Thermos Cursor
  Developer Tools Thermo-nuclear branch review: deep security/correctness audits,
  harsh code-quality rubrics, parallel subagents, thermos orchestration, and optional
  merge-ready PR flows. create-plugin Create Plugin Cursor Developer Tools Scaffold
  and validate new Cursor plugins. agent-compatibility Agent Compatibility Cursor
  Developer Tools CLI-backed repo compatibility scans plus Cursor agents that audit
  startup, validation, and docs against reality. cli-for-agent CLI for Agents Cursor
  Developer Tools Patterns for designing CLIs that coding agents can run reliably:
  flags, help with examples, pipelines, errors, idempotency, dry-run. pr-review-canvas
  PR Review Canvas Cursor Developer Tools Render PR diffs as interactive Cursor Canvases
  organized for reviewer comprehension — groups changes by importance, separates boilerplate
  from core logic, and highlights tricky or unexpected code. docs-canvas Docs Canvas
  Cursor Developer Tools Render documentation — architecture notes, API references,
  runbooks, and codebase walkthroughs — as a navigable Cursor Canvas with sections,
  table of contents, diagrams, and cross-references. cursor-sdk Cursor SDK Cursor
  Developer Tools Build apps, scripts, CI pipelines, and automations on top of the
  Cursor TypeScript SDK (@cursor/sdk) — runtime selection, auth, streaming, MCP, error
  handling, and ready-to-extend integration patterns. orchestrate Orchestrate Cursor
  Developer Tools Fan large tasks out across parallel Cursor cloud agents with planners,
  workers, verifiers, and structured handoffs. pstack pstack Lauren Tan Developer
  Tools if you want to go fast, go deep first. pstack helps you write less, but higher
  quality code. rigorous agent workflows you can parallelize with confidence. Author
  values match each plugin’s plugin.json author.name (Cursor lists plugins@cursor.com
  in the manifest). Repository structure This is a multi-plugin marketplace repository.
  The root .cursor-plugin/marketplace.json lists all plugins, and each plugin has
  its own manifest: plugins/ ├── .cursor-plugin/ │ └── marketplace.json # Marketplace
  manifest (lists all plugins) ├── plugin-name/ │ ├── .cursor-plugin/ │ │ └── plugin.json
  # Per-plugin manifest │ ├── skills/ # Agent skills (SKILL.md with frontmatter) │
  ├── rules/ # Cursor rules (.mdc files) │ ├── mcp.json # MCP server definitions │
  ├── README.md │ ├── CHANGELOG.md │ └── LICENSE └── ... License MIT'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a50d216def4cada3
source_type: community_discussion
tldr: Cursor 发布官方插件市场仓库，收录 11 款开发工具插件
objective_summary: Cursor 在 GitHub 上发布官方插件市场仓库 cursor/plugins，包含 11 个开发工具插件，如 Continual
  Learning、PR Review Canvas、Orchestrate、pstack 等。每个插件在独立目录下通过 plugin.
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Cursor
  technologies:
  - MCP
  key_people:
  - Lauren Tan
key_logic_flow:
- Cursor 在 GitHub 上开源了官方插件市场仓库 cursor/plugins，采用 MIT 许可证。
- 该仓库收录 11 个插件，涵盖持续学习、代码审查、文档渲染、任务编排、CLI 设计模式等功能，全部归类为开发工具。
- 每个插件以独立目录存放，内部包含 plugin.json 清单、skills 目录、rules 目录、mcp.json 等配置文件。
- 根目录下通过 .cursor-plugin/marketplace.json 统一管理所有插件的注册信息。
- 插件作者除 Cursor 官方外，还有个人开发者 Lauren Tan 贡献了 pstack 插件。
- 仓库中的 cursor-sdk 插件支持基于 Cursor TypeScript SDK 构建应用，集成了 MCP、流式处理等能力。
impact_score:
  score: 6.5
  reason: Cursor 推出官方插件市场是 AI 代码编辑器行业从'产品竞争'向'平台竞争'升级的关键信号。11 款插件覆盖了持续学习记忆、PR 审查画布、并行任务编排、SDK
    集成等核心场景，尤其是 Orchestrate（并行云 agent 编排）和 Continual Learning（增量式 AGENTS.md 记忆更新）直接触及
    AI 辅助编程的工作流范式。虽然不是 ChatGPT 级别的范式转移，但此举将显著改变 AI 编码工具的竞争维度——谁能建立起更丰富的插件生态，谁就能获得更强的开发者粘性和护城河。Cursor
    正在复用 VS Code 当年的平台化策略，短期影响集中在 AI 编码工具赛道的格局重塑，评分 6.5。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 插件架构设计与 MCP 集成方式，以及能否形成类似 VS Code 的丰富生态
hype_assessment:
  level: low
  reason: 文章/仓库内容实打实，所有插件代码已开源在 GitHub 上，采用 MIT 许可证，有明确的目录结构和配置规范。没有出现'颠覆'、'革命性'等
    PR 夸大用语，每个插件都有清晰的用途描述和实际代码。信息可信度很高。
information_entropy: high
domain_disruption:
  technical_innovation: 定义了 AI 代码编辑器的标准化插件框架，核心创新在于将 MCP 协议、skills 技能文件、rules 规则系统、TypeScript
    SDK 四层能力统一封装为可复用的插件单元。特别是 Continual Learning 插件引入了跨会话的增量记忆机制（高信号要点更新 AGENTS.md），Orchestrate
    插件实现了多 agent 并行编排（planner-worker-verifier 流水线），这两者都是 AI 辅助编程领域的前沿工程实践。Docs Canvas
    和 PR Review Canvas 将 Cursor 的 Canvas 渲染能力对外开放，形成了独特的交互模式。
  business_model: Cursor 从'AI 代码编辑器产品'向'AI 编程平台'转型，通过插件市场建立开发者生态和网络效应。这本质上是'应用商店'模式在
    AI 工具领域的复刻——插件生态越丰富，用户粘性越高，切换成本越大。同时 cursor-sdk 插件允许开发者在 Cursor 之上构建应用，进一步模糊了'工具'与'平台'的边界，为未来可能的插件内购、企业级插件分发等商业模式铺路。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Cursor 发布官方插件市场是一场典型的平台化 pivot，核心逻辑在于通过插件生态构建网络效应和迁移成本壁垒。当前虽然仅有 11 个插件，但目录结构、manifest
    规范、MCP 集成、SDK 均已就位，基础设施已经搭好。从 VC 视角看，价值复利的关键假设是：Cursor 是否能成为 AI-native 开发的主流 IDE——如果成立，插件市场将成为类似
    iOS App Store 或 VS Code Extensions 的分发渠道，网络效应会随时间指数级放大。Cursor SDK 对 MCP 的原生支持意味着插件生态不局限于
    Cursor 内部，还能桥接到更广泛的 AI Agent 工具链，进一步扩大捕获的价值面。风险点在于：(1) 当前插件数量和作者多样性不足，生态启动需要临界质量；(2)
    VS Code 已有极其成熟的扩展市场，开发者是否愿意迁移或维护两套配置存在不确定性；(3) Cursor 自身基于 VS Code 架构，平台独立性尚未完全确立。综合判断：7.5
    分，属于高潜力但需持续验证的细分赛道基础设施。若 12 个月内插件数量突破 100+、出现 killer plugin，则加速度会大幅提升。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Cursor
- Lauren Tan (pstack)
- MCP 生态
- Cursor 插件开发者
competitive_casualty:
- Windsurf
- 传统无生态的 AI 代码编辑器
- 单一功能的 AI 编码工具（如仅做代码审查的独立产品）
market_opportunities:
- 开发者可围绕 Cursor 插件市场构建垂直领域的专用插件，例如特定框架（React、Next.js、FastAPI）的代码生成与审查规则包，通过插件商店或企业订阅变现
- 团队可借鉴 Cursor 插件架构（skills + rules + MCP）中的持续学习（continual-learning）与任务编排（orchestrate）模式，打造内部
  AI 编码助手标准化工作流
- Cursor SDK 插件为独立开发者提供了接入 Cursor 生态的低门槛入口，可开发跨 IDE 的 MCP 工具链，抢占 AI 编程助手插件生态的先发红利
risk_matrix:
  regulatory: MIT 开源协议约束较小，但插件若涉及第三方 API 调用或数据回传，可能面临 GDPR / 中国《个人信息保护法》下的数据合规审查
  technological: 插件市场完全绑定 Cursor 平台的演进路线，若 Cursor 底层架构（如 MCP 协议、Agent SDK）发生不兼容变更，现有插件需持续维护适配
  competitive: VS Code、JetBrains 等主流 IDE 正在加速 AI 插件生态建设，Cursor 插件市场短期内难以形成网络效应壁垒，面临生态挤压风险
  ethical: PR Review Canvas 等代码审查插件可能强化对开发者产出的自动化评估，若被企业用于量化考核，会加剧程序员绩效焦虑与就业替代隐忧
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

Official Cursor plugins for popular developer tools, frameworks, and SaaS products. Each plugin is a standalone directory at the repository root with its own `.cursor-plugin/plugin.json`

manifest.

`name` |
Plugin | Author | Category | `description` (from marketplace) |
|---|---|---|---|---|
`continual-learning` |
Continual Learning | Cursor | Developer Tools | Incremental transcript-driven memory updates for AGENTS.md using high-signal bullet points only. |
`cursor-team-kit` |
Cursor Team Kit | Cursor | Developer Tools | Internal team workflows used by Cursor developers for CI, code review, shipping, local automation, and verification. |
`thermos` |
Thermos | Cursor | Developer Tools | Thermo-nuclear branch review: deep security/correctness audits, harsh code-quality rubrics, parallel subagents, thermos orchestration, and optional merge-ready PR flows. |
`create-plugin` |
Create Plugin | Cursor | Developer Tools | Scaffold and validate new Cursor plugins. |
`agent-compatibility` |
Agent Compatibility | Cursor | Developer Tools | CLI-backed repo compatibility scans plus Cursor agents that audit startup, validation, and docs against reality. |
`cli-for-agent` |
CLI for Agents | Cursor | Developer Tools | Patterns for designing CLIs that coding agents can run reliably: flags, help with examples, pipelines, errors, idempotency, dry-run. |
`pr-review-canvas` |
PR Review Canvas | Cursor | Developer Tools | Render PR diffs as interactive Cursor Canvases organized for reviewer comprehension — groups changes by importance, separates boilerplate from core logic, and highlights tricky or unexpected code. |
`docs-canvas` |
Docs Canvas | Cursor | Developer Tools | Render documentation — architecture notes, API references, runbooks, and codebase walkthroughs — as a navigable Cursor Canvas with sections, table of contents, diagrams, and cross-references. |
`cursor-sdk` |
Cursor SDK | Cursor | Developer Tools | Build apps, scripts, CI pipelines, and automations on top of the Cursor TypeScript SDK (@cursor/sdk) — runtime selection, auth, streaming, MCP, error handling, and ready-to-extend integration patterns. |
`orchestrate` |
Orchestrate | Cursor | Developer Tools | Fan large tasks out across parallel Cursor cloud agents with planners, workers, verifiers, and structured handoffs. |
`pstack` |
pstack | Lauren Tan | Developer Tools | if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence. |

Author values match each plugin’s `plugin.json`

`author.name`

(Cursor lists `plugins@cursor.com`

in the manifest).

This is a multi-plugin marketplace repository. The root `.cursor-plugin/marketplace.json`

lists all plugins, and each plugin has its own manifest:

```
plugins/
├── .cursor-plugin/
│ └── marketplace.json # Marketplace manifest (lists all plugins)
├── plugin-name/
│ ├── .cursor-plugin/
│ │ └── plugin.json # Per-plugin manifest
│ ├── skills/ # Agent skills (SKILL.md with frontmatter)
│ ├── rules/ # Cursor rules (.mdc files)
│ ├── mcp.json # MCP server definitions
│ ├── README.md
│ ├── CHANGELOG.md
│ └── LICENSE
└── ...
```


MIT