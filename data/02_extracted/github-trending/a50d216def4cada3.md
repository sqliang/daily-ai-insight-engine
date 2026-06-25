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
extract_result: success
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