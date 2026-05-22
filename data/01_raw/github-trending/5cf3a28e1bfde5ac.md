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