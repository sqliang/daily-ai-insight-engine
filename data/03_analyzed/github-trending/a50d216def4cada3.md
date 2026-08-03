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
tldr: Cursor 官方发布 plugins 仓库，收录 11 个面向开发者的插件，涵盖持续学习、代码审查、文档渲染、CLI 设计、并行编排等场景。每个插件有独立的
  manifest，遵循统一目录结构。
objective_summary: Cursor 在 GitHub 上发布 cursor/plugins 仓库，提供面向开发工具、框架和 SaaS 产品的官方插件集合。该仓库包含
  11 个插件，包括 continual-learning（增量记忆更新）、thermos（分支安全审查）、pr-review-canvas（PR 差异画布渲染）、docs-canvas（文档画布渲染）、cursor-sdk（TypeScript
  SDK 集成）、orchestrate（并行云代理编排）等。每个插件以独立目录存放，包含 .cursor-plugin/plugin.json 清单、skills/
  技能文件、rules/ 规则文件和 mcp.json 配置。
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
- Cursor 官方发布 plugins 仓库，集中管理面向开发者工具和 SaaS 产品的插件集合。
- 每个插件是仓库根目录下的独立子目录，包含 .cursor-plugin/plugin.json 清单文件。
- 仓库根目录的 .cursor-plugin/marketplace.json 列出所有插件的市场清单。
- 插件内部结构统一：包含 skills/（技能文件）、rules/（.mdc 规则文件）、mcp.json（MCP 服务器定义）等目录。
- 已收录 11 个插件，覆盖持续学习、团队工作流、代码审查、文档渲染、CLI 设计、SDK 集成和并行编排等领域。
- 仓库基于 MIT 协议开源发布。
extract_result: success
object_mentions:
- object_type: project
  name: cursor/plugins
  canonical_name: cursor/plugins
  url: https://github.com/cursor/plugins
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cursor 官方发布 plugins 仓库，收录面向开发工具、框架和 SaaS 产品的插件集合。
  - 每个插件是独立目录，包含 .cursor-plugin/plugin.json 清单，仓库根目录有 .cursor-plugin/marketplace.json
    市场清单。
  article_id: a50d216def4cada3
- object_type: project
  name: continual-learning
  canonical_name: cursor/plugins/continual-learning
  url: https://github.com/cursor/plugins/tree/main/continual-learning
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Continual Learning 插件提供基于转录的增量记忆更新，仅使用高信号要点更新 AGENTS.md。
  - 该插件属于 Developer Tools 类别，由 Cursor 官方维护。
  article_id: a50d216def4cada3
- object_type: product
  name: cursor-team-kit
  canonical_name: cursor/plugins/cursor-team-kit
  url: https://github.com/cursor/plugins/tree/main/cursor-team-kit
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cursor Team Kit 插件封装了 Cursor 开发者的内部团队工作流，支持 CI、代码审查、发布、本地自动化和验证。
  article_id: a50d216def4cada3
- object_type: project
  name: thermos
  canonical_name: cursor/plugins/thermos
  url: https://github.com/cursor/plugins/tree/main/thermos
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Thermos 插件提供热核级别分支审查，包括深度安全/正确性审计、严格的代码质量评分、并行子代理和可选合并就绪 PR 流程。
  article_id: a50d216def4cada3
- object_type: project
  name: create-plugin
  canonical_name: cursor/plugins/create-plugin
  url: https://github.com/cursor/plugins/tree/main/create-plugin
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Create Plugin 插件用于快速脚手架和验证新的 Cursor 插件，属于 Developer Tools 类别。
  article_id: a50d216def4cada3
- object_type: project
  name: agent-compatibility
  canonical_name: cursor/plugins/agent-compatibility
  url: https://github.com/cursor/plugins/tree/main/agent-compatibility
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Agent Compatibility 插件提供 CLI 驱动的仓库兼容性扫描，以及用于审计启动、验证和文档的 Cursor 代理。
  article_id: a50d216def4cada3
- object_type: project
  name: cli-for-agent
  canonical_name: cursor/plugins/cli-for-agent
  url: https://github.com/cursor/plugins/tree/main/cli-for-agent
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - CLI for Agents 插件提供让编码代理可靠运行的 CLI 设计模式，涵盖标志参数、帮助示例、管道、错误处理、幂等性和干运行。
  article_id: a50d216def4cada3
- object_type: project
  name: pr-review-canvas
  canonical_name: cursor/plugins/pr-review-canvas
  url: https://github.com/cursor/plugins/tree/main/pr-review-canvas
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PR Review Canvas 将 PR 差异渲染为交互式 Cursor Canvas，按重要性分组变更、分离样板代码与核心逻辑并突出显示异常代码。
  article_id: a50d216def4cada3
- object_type: project
  name: docs-canvas
  canonical_name: cursor/plugins/docs-canvas
  url: https://github.com/cursor/plugins/tree/main/docs-canvas
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Docs Canvas 将架构文档、API 参考、操作手册和代码库导览渲染为可导航的 Cursor Canvas，支持章节、目录、图表和交叉引用。
  article_id: a50d216def4cada3
- object_type: project
  name: cursor-sdk
  canonical_name: cursor/plugins/cursor-sdk
  url: https://github.com/cursor/plugins/tree/main/cursor-sdk
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cursor SDK 插件基于 @cursor/sdk TypeScript SDK 构建应用、脚本、CI 流水线和自动化，覆盖运行时选择、认证、流式处理、MCP
    和错误处理。
  article_id: a50d216def4cada3
- object_type: project
  name: orchestrate
  canonical_name: cursor/plugins/orchestrate
  url: https://github.com/cursor/plugins/tree/main/orchestrate
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Orchestrate 插件将大型任务分发到并行的 Cursor 云代理，支持规划器、工作节点、验证器和结构化交接机制。
  article_id: a50d216def4cada3
- object_type: project
  name: pstack
  canonical_name: cursor/plugins/pstack
  url: https://github.com/cursor/plugins/tree/main/pstack
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - pstack 插件由 Lauren Tan 开发，帮助编写更少但质量更高的代码，提供可安全并行化的严谨代理工作流。
  article_id: a50d216def4cada3
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
object_insights:
- object_type: project
  name: cursor/plugins
  canonical_name: cursor/plugins
  url: https://github.com/cursor/plugins
  positioning: Cursor 官方开源的插件市场仓库，统一管理面向开发者工具和 SaaS 产品的插件生态，提供标准化目录结构和安装机制。
  technical_signal: 采用统一目录结构和 plugin.json 清单机制，每个插件独立目录包含 skills/、rules/ 和 mcp.json
    等标准化组件，具备良好的可扩展性。
  adoption_signal: 发布首日收录 11 个官方插件，作为 Cursor 生态基础设施初始曝光度高，但第三方插件的实际采用情况有待观察。
  ecosystem_relevance: 作为 Cursor 编辑器生态的插件市场基础设施，直接定义开发者工具链的集成方式，对 Cursor 平台生态发展具有战略意义。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Cursor 作为 AI 编程助手的领先者之一，其官方插件市场定义了一种全新的 IDE 插件生态模式，直接影响开发者工具链的集成方式与
    AI 代理能力的边界。
  risk_notes:
  - 目前插件数量有限，生态处于早期阶段，能否吸引第三方开发者持续贡献是关键风险。
  - 插件质量标准和审核机制尚未明确，低质量插件可能影响用户体验和生态声誉。
  score: 9.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Cursor 官方发布 plugins 仓库，收录面向开发工具、框架和 SaaS 产品的插件集合。
  - 每个插件是独立目录，包含 .cursor-plugin/plugin.json 清单，仓库根目录有 .cursor-plugin/marketplace.json
    市场清单。
- object_type: project
  name: continual-learning
  canonical_name: cursor/plugins/continual-learning
  url: https://github.com/cursor/plugins/tree/main/continual-learning
  positioning: 基于转录驱动的增量记忆更新插件，自动筛选高信号要点持续维护 AGENTS.md，实现 AI 代理的持续学习机制。
  technical_signal: 采用增量转录驱动方式更新 AGENTS.md，仅提取高信号要点而非全量记录，兼顾上下文积累效率与记忆准确性。
  adoption_signal: 作为 Cursor 官方出品的基础性插件，初始曝光度高，但实际使用效果和用户长期粘性有待市场验证。
  ecosystem_relevance: 解决 AI 编程助手在长期项目中持续学习和积累上下文的核心痛点，对提升 Cursor 用户体验具有基础性价值。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 持续学习能力是 AI 编程工具从短会话走向长期项目协作的核心差异化方向，该插件以极简方式尝试解决代理记忆更新的关键难题。
  risk_notes:
  - 增量更新策略的准确性和完整性在实践中可能不足，高信号筛选标准需要持续调优。
  - 仅更新 AGENTS.md 单一文件，长期记忆的覆盖面和支持格式可能过于局限。
  score: 7.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Continual Learning 插件提供基于转录的增量记忆更新，仅使用高信号要点更新 AGENTS.md。
  - 该插件属于 Developer Tools 类别，由 Cursor 官方维护。
- object_type: product
  name: cursor-team-kit
  canonical_name: cursor/plugins/cursor-team-kit
  url: https://github.com/cursor/plugins/tree/main/cursor-team-kit
  positioning: Cursor 团队内部开发工作流的封装产品，涵盖 CI、代码审查、发布管理和本地自动化等团队级开发流程。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Cursor 进行团队协作的开发组织
  - 探索 AI 原生开发工作流的工程团队
  product_signal: 封装了 Cursor 开发者实际使用的内部工作流，覆盖 CI 流水线、代码审查、版本发布、本地自动化和验证等完整团队开发流程。
  market_signal: 作为 Cursor 自身团队实践的外化输出，初始定位非商业化开源产品，市场推广策略和目标用户画像尚未明确。
  differentiation: 直接源于 Cursor 核心团队的实际开发流程，相较于通用 CI/CD 工具对 Cursor 用户具有天然适配性和参考价值。
  watch_reason: 团队工作流是开发者工具生态中最具粘性和壁垒的部分，Cursor 将内部实践开源化可能影响团队级 AI 开发工具格局。
  risk_notes:
  - 非商业化产品，长期维护投入和版本迭代速度不确定。
  - 工作流高度绑定 Cursor 自身实践，通用性和可迁移性可能有限。
  score: 6.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Cursor Team Kit 插件封装了 Cursor 开发者的内部团队工作流，支持 CI、代码审查、发布、本地自动化和验证。
- object_type: project
  name: thermos
  canonical_name: cursor/plugins/thermos
  url: https://github.com/cursor/plugins/tree/main/thermos
  positioning: 热核级别分支审查插件，提供深度安全审计、严格代码质量评分和并行代理审查驱动的自动化代码审查机制。
  technical_signal: 采用并行子代理架构进行分支审查，包含深度安全与正确性审计、代码质量评分和可选自动化合并就绪 PR 流程，审查自动化程度高。
  adoption_signal: 作为 Cursor 官方出品的高级代码审查插件，初始关注度高，但并行代理消耗资源多，成本敏感型团队接受度可能受限。
  ecosystem_relevance: 填补 AI 编程助手在自动化深度代码审查领域的高阶需求，对增强 Cursor 在企业级安全合规场景的适用性有重要作用。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 自动化深度代码审查是 AI 编程工具企业级部署的关键能力，热核审查模式以严格的并行审计思路代表了行业的前沿探索方向。
  risk_notes:
  - 并行代理审查带来的 Token 消耗和成本较高，中小团队可能难以承受。
  - 严格评分机制可能产生过多误报，影响开发者日常使用体验。
  score: 6.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Thermos 插件提供热核级别分支审查，包括深度安全/正确性审计、严格的代码质量评分、并行子代理和可选合并就绪 PR 流程。
- object_type: project
  name: create-plugin
  canonical_name: cursor/plugins/create-plugin
  url: https://github.com/cursor/plugins/tree/main/create-plugin
  positioning: Cursor 插件快速脚手架工具，帮助开发者快速创建和验证新插件，降低生态参与门槛和开发启动成本。
  technical_signal: 提供标准化插件脚手架生成能力，自动创建 .cursor-plugin/plugin.json 清单及 skills/、rules/
    等目录结构，降低第三方开发者的入门成本。
  adoption_signal: 作为生态建设的基础设施工具，直接影响第三方插件的开发效率，是判断 Cursor 插件生态能否繁荣的前置观测指标。
  ecosystem_relevance: 对 Cursor 插件生态发展至关重要，其功能完善程度和开发体验直接决定了第三方参与者的入局意愿和开发速度。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 脚手架工具直接决定了第三方插件生态的发展速度和开发体验，是衡量 Cursor 平台化战略执行力的关键观测指标。
  risk_notes:
  - 模板和示例的完善程度决定实际开发效率，内容不足会抑制第三方参与。
  - 若脚手架工具版本迭代滞后于插件规范变化，将导致兼容性断裂。
  score: 7.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Create Plugin 插件用于快速脚手架和验证新的 Cursor 插件，属于 Developer Tools 类别。
- object_type: project
  name: agent-compatibility
  canonical_name: cursor/plugins/agent-compatibility
  url: https://github.com/cursor/plugins/tree/main/agent-compatibility
  positioning: CLI 驱动的仓库兼容性扫描工具，通过自动化审计确保 Cursor 代理在目标仓库中的启动、验证和文档一致性。
  technical_signal: 结合 CLI 扫描和 Cursor 代理审计的双重机制，自动化检查仓库启动流程、验证流程和文档与实际代码之间的差异，覆盖兼容性全链路。
  adoption_signal: 对需要在陌生代码库中可靠运行 Cursor 代理的团队有实用价值，尤其适合大型项目和遗留代码库的适配验证场景。
  ecosystem_relevance: 解决 AI 编程工具在陌生代码库中可靠运行的适配问题，对 Cursor 在复杂企业项目中落地具有支撑作用。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 代码库兼容性是 AI 编程工具从个人开发走向团队协作的关键障碍，该插件直接回应代理在陌生代码库中可靠运行的核心难题。
  risk_notes:
  - 兼容性扫描的全面性和深度受限于预设审计规则，对高度定制化代码库可能误报率较高。
  - 扫描效率与精度之间的平衡需要持续优化，过度扫描可能影响日常开发流程。
  score: 6.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Agent Compatibility 插件提供 CLI 驱动的仓库兼容性扫描，以及用于审计启动、验证和文档的 Cursor 代理。
- object_type: project
  name: cli-for-agent
  canonical_name: cursor/plugins/cli-for-agent
  url: https://github.com/cursor/plugins/tree/main/cli-for-agent
  positioning: 面向编码代理可靠性设计的 CLI 模式插件，提供标志参数、管道、错误处理和幂等性等标准化 CLI 设计规范。
  technical_signal: 系统性总结编码代理执行 CLI 的最佳实践，涵盖标志参数、帮助示例、管道机制、错误处理、幂等性和干运行等关键设计模式。
  adoption_signal: 作为设计规范类插件，适合作为其他插件的底层依赖或参考实现，采用度取决于整体插件生态的发展。
  ecosystem_relevance: 定义了 AI 代理与 CLI 交互的标准范式，对整个 Cursor 插件生态的 CLI 交互设计具有规范和指导意义。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: CLI 交互是 AI 编码代理执行任务的主要窗口，该插件的设计模式可能成为 Cursor 插件生态中 CLI 交互的事实标准。
  risk_notes:
  - 作为设计规范类工具，实际价值取决于插件开发者是否遵循其推荐模式，缺乏强制约束力。
  - 不同编程语言和运行时环境的 CLI 行为差异可能削弱模式的通用性。
  score: 5.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - CLI for Agents 插件提供让编码代理可靠运行的 CLI 设计模式，涵盖标志参数、帮助示例、管道、错误处理、幂等性和干运行。
- object_type: project
  name: pr-review-canvas
  canonical_name: cursor/plugins/pr-review-canvas
  url: https://github.com/cursor/plugins/tree/main/pr-review-canvas
  positioning: 将 PR 差异渲染为交互式 Cursor Canvas 的代码审查插件，按重要性智能分组变更以提升审查效率和理解度。
  technical_signal: 创新地将 PR 差异可视化重组，按重要性分组变更、分离样板代码与核心逻辑、突出异常代码，利用 Canvas 交互能力提升代码审查效率。
  adoption_signal: 代码审查是日常开发高频场景，Canvas 交互形式新颖直观，可能在 Cursor 用户群体中快速获得采用。
  ecosystem_relevance: 充分利用 Cursor Canvas 原生交互能力打造差异化审查体验，展示 Cursor 平台区别于传统 IDE 的独特价值。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: PR 审查画布代表了 AI 时代代码审查的新交互范式，将传统扁平 diff 视图升级为智能分组和异常高亮的沉浸式体验。
  risk_notes:
  - Canvas 交互方式需要用户适应，学习成本可能影响初始采用率。
  - 大型 PR 的 Canvas 渲染性能和交互流畅度有待实际使用验证。
  score: 7.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - PR Review Canvas 将 PR 差异渲染为交互式 Cursor Canvas，按重要性分组变更、分离样板代码与核心逻辑并突出显示异常代码。
- object_type: project
  name: docs-canvas
  canonical_name: cursor/plugins/docs-canvas
  url: https://github.com/cursor/plugins/tree/main/docs-canvas
  positioning: 将架构文档和 API 参考渲染为可导航 Cursor Canvas 的文档可视化插件，支持章节、目录和交叉引用的沉浸式阅读体验。
  technical_signal: 将静态文档转化为交互式 Canvas 导航体验，支持章节划分、目录导航、图表渲染和文档间交叉引用，提升开发者文档阅读和理解效率。
  adoption_signal: 文档阅读是开发者日常高频场景，可视化导航体验有吸引力，但实际效果依赖于文档格式的兼容性和渲染质量。
  ecosystem_relevance: 展示 Cursor Canvas 在非代码内容上的扩展能力，拓宽了插件生态的应用场景边界，具有平台能力示范价值。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 文档可视化是 AI 编程 IDE 区别于传统 IDE 的重要交互创新方向，可能重新定义开发者与项目文档的交互方式。
  risk_notes:
  - 文档格式兼容性和渲染质量决定实际实用性，对非标准格式文档的支持有待加强。
  - 与现有文档工具和知识库平台之间的竞争关系不明确，用户迁移成本较高。
  score: 6.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Docs Canvas 将架构文档、API 参考、操作手册和代码库导览渲染为可导航的 Cursor Canvas，支持章节、目录、图表和交叉引用。
- object_type: project
  name: cursor-sdk
  canonical_name: cursor/plugins/cursor-sdk
  url: https://github.com/cursor/plugins/tree/main/cursor-sdk
  positioning: 基于 @cursor/sdk TypeScript SDK 的应用开发集成插件，提供运行时选择、认证、流式处理和 MCP 协议等标准化集成模式。
  technical_signal: 深度集成 Cursor TypeScript SDK，覆盖运行时选择、认证授权、流式处理、MCP 协议和错误处理等关键集成模式，技术栈完整。
  adoption_signal: 作为 SDK 集成的基础设施插件，采用度取决于第三方开发者对 Cursor 平台扩展的整体兴趣，是生态活跃度的前置指标。
  ecosystem_relevance: 是 Cursor 平台对外开放能力的核心技术入口，直接决定了第三方插件能调用的平台能力和开发复杂度。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: SDK 集成插件是 Cursor 平台化战略的技术基石，其 API 设计和能力边界直接定义第三方插件的开发体验和生态质量。
  risk_notes:
  - TypeScript SDK 的能力边界和 API 稳定性直接影响插件生态质量，频繁变更可能导致兼容性问题。
  - 对非 TypeScript 生态的开发者友好度有限，可能限制生态参与者的多样性。
  score: 8.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Cursor SDK 插件基于 @cursor/sdk TypeScript SDK 构建应用、脚本、CI 流水线和自动化，覆盖运行时选择、认证、流式处理、MCP
    和错误处理。
- object_type: project
  name: orchestrate
  canonical_name: cursor/plugins/orchestrate
  url: https://github.com/cursor/plugins/tree/main/orchestrate
  positioning: 并行云代理任务编排插件，将大型编码任务分发到多个 Cursor 云代理并行处理，支持规划器、工作节点和验证器协作。
  technical_signal: 采用规划器-工作节点-验证器的多代理协作架构，支持大型任务的智能分发、并行执行和结构化结果交接，架构设计具有前瞻性。
  adoption_signal: 对需要处理大规模编码任务的用户有较强吸引力，但并行代理的资源消耗较高，普及速度可能受限于成本和可用性。
  ecosystem_relevance: 体现 Cursor 云代理的差异化技术能力，展示 AI 编程工具从单代理辅助到多代理自主协作的能力跃升。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 多代理并行编排是 AI 编程工具从辅助编码迈向自主软件开发的关键技术方向，Orchestrate 代表了 Cursor 在这一方向的最新探索。
  risk_notes:
  - 并行代理的资源消耗和 Token 成本较高，大规模使用时的经济性需要验证。
  - 任务拆分和子代理结果合并的可靠性直接影响产出质量，复杂场景下可能引入新错误。
  score: 8.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - Orchestrate 插件将大型任务分发到并行的 Cursor 云代理，支持规划器、工作节点、验证器和结构化交接机制。
- object_type: project
  name: pstack
  canonical_name: cursor/plugins/pstack
  url: https://github.com/cursor/plugins/tree/main/pstack
  positioning: 由知名开发者 Lauren Tan 开发的高质量编码插件，提供可安全并行化的严谨代理工作流，追求少而精的代码产出。
  technical_signal: 专注于代理工作流的严谨性和可安全并行化能力，通过严格的代理工作流约束保证代码质量，强调深度优先于速度。
  adoption_signal: 由业界知名开发者 Lauren Tan 贡献，初始关注度和信誉度较高，作为第三方插件是验证 Cursor 插件生态吸引力的重要样本。
  ecosystem_relevance: 展示了 Cursor 插件生态对独立开发者的吸引力，证明第三方参与的可能性，对生态多元化发展具有示范意义。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为首个非 Cursor 官方知名开发者贡献的插件，是衡量 Cursor 插件生态对第三方开发者吸引力的重要观测样本。
  risk_notes:
  - 第三方插件的长期维护更新存在不确定性，开发者个人精力分配可能影响版本迭代。
  - 是否会被 Cursor 官方同类功能替代是第三方插件开发者面临的通用风险。
  score: 6.0
  article_ids:
  - a50d216def4cada3
  evidence_snippets:
  - pstack 插件由 Lauren Tan 开发，帮助编写更少但质量更高的代码，提供可安全并行化的严谨代理工作流。
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