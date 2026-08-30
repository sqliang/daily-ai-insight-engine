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
pipeline_stage: ingested
id: a50d216def4cada3
manifest_dates:
- '2026-06-01'
- '2026-08-15'
- '2026-08-16'
- '2026-08-21'
- '2026-08-22'
- '2026-08-23'
- '2026-08-29'
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