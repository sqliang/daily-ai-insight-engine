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
tldr: .NET 团队发布了 dotnet/skills 仓库，其中包含 12 个面向编程智能体的核心技能插件，涵盖 .NET 编码、数据访问、调试、构建、包管理、升级、MAUI、AI/ML、模板引擎、测试、ASP.NET
  及 .NET 11 新特性，遵循 agentskills.io 开放标准，兼容 Copilot CLI、Claude Code、VS Code 和 Cursor。
objective_summary: 微软 .NET 团队在 GitHub 上发布 dotnet/skills 仓库，这是一套面向编程智能体的核心技能和自定义智能体集合。该仓库包含
  12 个插件（dotnet、dotnet-data、dotnet-diag、dotnet-msbuild、dotnet-nuget、dotnet-upgrade、dotnet-maui、dotnet-ai、dotnet-template-engine、dotnet-test、dotnet-aspnet、dotnet11），覆盖
  .NET 开发生态各领域。所有技能遵循 agentskills.io 开放标准，兼容 Copilot CLI、Claude Code、VS Code Copilot
  Chat（预览功能）、Cursor 以及 OpenAI Codex。.NET 团队还提供了公开仪表盘（dotnet.github.io/skills）用于追踪各插件的准确性和效率评分趋势。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Microsoft
  technologies:
  - Agent Skills
  - MCP
  - RAG
  - ML.NET
  - LLM
  - MSBuild
  - NuGet
  - Entity Framework
  - ASP.NET Core
  - .NET MAUI
  key_people: []
key_logic_flow:
- 微软 .NET 团队在 GitHub 上发布 dotnet/skills 仓库，其中包含面向编程智能体的核心技能和自定义智能体集合。
- 该仓库提供 12 个插件，涵盖 .NET 编码、数据访问（Entity Framework）、调试诊断、MSBuild 构建、NuGet 包管理、版本升级、MAUI
  开发、AI/ML 集成、模板引擎、测试执行、ASP.NET Core 以及 .NET 11 新特性等领域。
- 这些技能遵循 agentskills.io 开放标准，兼容 Copilot CLI、Claude Code、VS Code Copilot Chat、Cursor
  以及 OpenAI Codex 等多个编程智能体平台。
- .NET 团队在 dotnet.github.io/skills 上提供了公开仪表盘，用于追踪各插件的准确性和效率评分趋势。
- 用户可以通过命令行（/plugin marketplace add dotnet/skills）或 VS Code 设置（chat.plugins.marketplaces）来安装和使用这些插件。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: project
  name: dotnet/skills
  canonical_name: dotnet/skills
  url: https://github.com/dotnet/skills
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该仓库包含 .NET 团队精心策划的核心技能和自定义智能体集合，用于编程智能体场景。
  - 仓库提供 12 个插件，覆盖 .NET 编码、数据访问、调试诊断、MSBuild 构建、NuGet 包管理、版本升级、MAUI 开发、AI/ML、模板引擎、测试、ASP.NET
    Core 以及 .NET 11 新特性。
  - .NET 团队在 dotnet.github.io/skills 上提供了公开仪表盘，用于追踪各插件的准确性和效率评分趋势。
  article_id: 5cf3a28e1bfde5ac
- object_type: project
  name: dotnet-ai (Agent Skill)
  canonical_name: dotnet/skills/dotnet-ai
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - dotnet-ai 插件提供 AI 和 ML 技能，涵盖技术选型、LLM 集成、智能体工作流、RAG 管道、MCP 以及经典 ML（ML.NET）。
  - 该插件是 dotnet/skills 仓库 12 个插件之一，面向 .NET 平台的 AI 与机器学习开发。
  article_id: 5cf3a28e1bfde5ac
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