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