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