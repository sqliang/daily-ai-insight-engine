---
title: davila7/claude-code-templates
source: https://github.com/davila7/claude-code-templates
author: []
published: ''
created: '2026-07-13'
description: 'CLI tool for configuring and monitoring Claude Code &nbsp;&nbsp; &nbsp;&nbsp;
  🧪 NEW: Dashboard — Explore components, manage collections, and track installations
  at www.aitmpl.com. Currently in beta — feedback welcome! Claude Code Templates (aitmpl.com)
  Ready-to-use configurations for Anthropic''s Claude Code. A comprehensive collection
  of AI agents, custom commands, settings, hooks, external integrations (MCPs), and
  project templates to enhance your development workflow. Browse & Install Components
  and Templates Browse All Templates - Interactive web interface to explore and install
  100+ agents, commands, settings, hooks, and MCPs. 🚀 Quick Installation # Install
  a complete development stack npx claude-code-templates@latest --agent development-team/frontend-developer
  --command testing/generate-tests --mcp development/github-integration --yes # Browse
  and install interactively npx claude-code-templates@latest # Install specific components
  npx claude-code-templates@latest --agent development-tools/code-reviewer --yes npx
  claude-code-templates@latest --command performance/optimize-bundle --yes npx claude-code-templates@latest
  --setting performance/mcp-timeouts --yes npx claude-code-templates@latest --hook
  git/pre-commit-validation --yes npx claude-code-templates@latest --mcp database/postgresql-integration
  --yes What You Get Component Description Examples 🤖 Agents AI specialists for specific
  domains Security auditor, React performance optimizer, database architect ⚡ Commands
  Custom slash commands /generate-tests, /optimize-bundle, /check-security 🔌 MCPs
  External service integrations GitHub, PostgreSQL, Stripe, AWS, OpenAI ⚙️ Settings
  Claude Code configurations Timeouts, memory settings, output styles 🪝 Hooks Automation
  triggers Pre-commit validation, post-completion actions 🎨 Skills Reusable capabilities
  with progressive disclosure PDF processing, Excel automation, custom workflows 🛠️
  Additional Tools Beyond the template catalog, Claude Code Templates includes powerful
  development tools: 📊 Claude Code Analytics Monitor your AI-powered development sessions
  in real-time with live state detection and performance metrics. npx claude-code-templates@latest
  --analytics 💬 Conversation Monitor Mobile-optimized interface to view Claude responses
  in real-time with secure remote access. # Local access npx claude-code-templates@latest
  --chats # Secure remote access via Cloudflare Tunnel npx claude-code-templates@latest
  --chats --tunnel 🔍 Health Check Comprehensive diagnostics to ensure your Claude
  Code installation is optimized. npx claude-code-templates@latest --health-check
  🔌 Plugin Dashboard View marketplaces, installed plugins, and manage permissions
  from a unified interface. npx claude-code-templates@latest --plugins 📖 Documentation
  📚 docs.aitmpl.com - Complete guides, examples, and API reference for all components
  and tools. Contributing We welcome contributions! Browse existing templates to see
  what''s available, then check our contributing guidelines to add your own agents,
  commands, MCPs, settings, or hooks. Please read our Code of Conduct before contributing.
  Attribution This collection includes components from multiple sources: Scientific
  Skills: K-Dense-AI/claude-scientific-skills by K-Dense Inc. - MIT License (139 scientific
  skills for biology, chemistry, medicine, and computational research) Official Anthropic:
  anthropics/skills - Official Anthropic skills (21 skills) anthropics/claude-code
  - Development guides and examples (10 skills) Community Skills & Agents: obra/superpowers
  by Jesse Obra - MIT License (14 workflow skills) alirezarezvani/claude-skills by
  Alireza Rezvani - MIT License (36 professional role skills) wshobson/agents by wshobson
  - MIT License (48 agents) NerdyChefsAI Skills - Community contribution - MIT License
  (specialized enterprise skills) Commands & Tools: awesome-claude-code by hesreallyhim
  - CC0 1.0 Universal (21 commands) awesome-claude-skills - Apache 2.0 (community
  skills) move-code-quality-skill - MIT License cocoindex-claude - Apache 2.0 Each
  of these resources retains its original license and attribution, as defined by their
  respective authors. We respect and credit all original creators for their work and
  contributions to the Claude ecosystem. 📄 License This project is licensed under
  the MIT License - see the LICENSE file for details. 🔗 Links 🌐 Browse Templates:
  aitmpl.com 📚 Documentation: docs.aitmpl.com 💬 Community: GitHub Discussions 🐛 Issues:
  GitHub Issues Stargazers over time ⭐ Found this useful? Give us a star to support
  the project!'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 25bff0b4a0ece6bc
source_type: community_discussion
tldr: davila7 发布了 Claude Code 模板集合仓库，提供 100+ 免配置的 Agents、Commands、MCPs 及 Skills 模板。
objective_summary: davila7 于 GitHub 上发布了 claude-code-templates 仓库，这是一个面向 Anthropic
  Claude Code 的 100+ 模板集合。用户可通过 npx 命令安装包括 Agents、Commands、MCPs、Settings、Hooks 和 Skills
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - davila7
  - Anthropic
  - K-Dense Inc.
  technologies:
  - MCP
  - Claude Code
  key_people:
  - Jesse Obra
  - Alireza Rezvani
  - wshobson
key_logic_flow:
- davila7 发布了 claude-code-templates，这是一个为 Anthropic Claude Code 提供免配置模板的 GitHub 开源仓库。
- 模板库涵盖六大组件类型：AI 智能体（Agents）、自定义命令（Commands）、外部集成 MCP（MCPs）、配置设置（Settings）、自动化钩子（Hooks）和可复用技能（Skills），总量超过
  100 个。
- 用户可通过 npx claude-code-templates@latest 命令以多种方式安装：交互式浏览、指定组件安装或一键安装完整开发栈。
- 项目还附带辅助开发工具：实时会话监控（analytics）、移动端聊天界面（chats，支持 Cloudflare Tunnel 远程访问）、安装健康检查（health-check）和插件管理（plugins）。
- 该仓库整合了 Anthropic 官方技能、K-Dense Inc. 的 139 个科学技能以及多个社区贡献者的模板，各自保留原始许可证和归属。
- 项目采用 MIT 许可证，提供 aitmpl.com 在线浏览界面、docs.aitmpl.com 文档站以及 GitHub Issues 和 Discussions
  社区支持。
specialized_tags:
  github:
    projectName: davila7/claude-code-templates
    projectUrl: https://github.com/davila7/claude-code-templates
    primaryLanguage: JavaScript
    licenseType: MIT
    domain: ai_ml
    crossTags:
    - developer-tools
    - cli-tool
    - open-source
    aiDetail:
      primaryCategories:
      - agent_framework
      - prompt_engineering
      - code_gen
      agentSubcategory:
      - tool_use
      - orchestration
      - coding_agent
      - general_framework
      techTags:
      - MCP
      - function-calling
      - CLI
extract_result: success
---

🧪 NEW: Dashboard— Explore components, manage collections, and track installations atwww.aitmpl.com. Currently in beta — feedback welcome!

**Ready-to-use configurations for Anthropic's Claude Code.** A comprehensive collection of AI agents, custom commands, settings, hooks, external integrations (MCPs), and project templates to enhance your development workflow.

**Browse All Templates** - Interactive web interface to explore and install 100+ agents, commands, settings, hooks, and MCPs.

```
# Install a complete development stack
npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes
# Browse and install interactively
npx claude-code-templates@latest
# Install specific components
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --command performance/optimize-bundle --yes
npx claude-code-templates@latest --setting performance/mcp-timeouts --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

| Component | Description | Examples |
|---|---|---|
🤖 Agents |
AI specialists for specific domains | Security auditor, React performance optimizer, database architect |
⚡ Commands |
Custom slash commands | `/generate-tests` , `/optimize-bundle` , `/check-security` |
🔌 MCPs |
External service integrations | GitHub, PostgreSQL, Stripe, AWS, OpenAI |
⚙️ Settings |
Claude Code configurations | Timeouts, memory settings, output styles |
🪝 Hooks |
Automation triggers | Pre-commit validation, post-completion actions |
🎨 Skills |
Reusable capabilities with progressive disclosure | PDF processing, Excel automation, custom workflows |

Beyond the template catalog, Claude Code Templates includes powerful development tools:

Monitor your AI-powered development sessions in real-time with live state detection and performance metrics.

`npx claude-code-templates@latest --analytics`

Mobile-optimized interface to view Claude responses in real-time with secure remote access.

```
# Local access
npx claude-code-templates@latest --chats
# Secure remote access via Cloudflare Tunnel
npx claude-code-templates@latest --chats --tunnel
```

Comprehensive diagnostics to ensure your Claude Code installation is optimized.

`npx claude-code-templates@latest --health-check`

View marketplaces, installed plugins, and manage permissions from a unified interface.

`npx claude-code-templates@latest --plugins`

**📚 docs.aitmpl.com** - Complete guides, examples, and API reference for all components and tools.

We welcome contributions! **Browse existing templates** to see what's available, then check our contributing guidelines to add your own agents, commands, MCPs, settings, or hooks.

**Please read our Code of Conduct before contributing.**

This collection includes components from multiple sources:

**Scientific Skills:**

**K-Dense-AI/claude-scientific-skills**by K-Dense Inc. - MIT License (139 scientific skills for biology, chemistry, medicine, and computational research)

**Official Anthropic:**

**anthropics/skills**- Official Anthropic skills (21 skills)**anthropics/claude-code**- Development guides and examples (10 skills)

**Community Skills & Agents:**

**obra/superpowers**by Jesse Obra - MIT License (14 workflow skills)**alirezarezvani/claude-skills**by Alireza Rezvani - MIT License (36 professional role skills)**wshobson/agents**by wshobson - MIT License (48 agents)**NerdyChefsAI Skills**- Community contribution - MIT License (specialized enterprise skills)

**Commands & Tools:**

**awesome-claude-code**by hesreallyhim - CC0 1.0 Universal (21 commands)**awesome-claude-skills**- Apache 2.0 (community skills)**move-code-quality-skill**- MIT License**cocoindex-claude**- Apache 2.0

Each of these resources retains its **original license and attribution**, as defined by their respective authors.
We respect and credit all original creators for their work and contributions to the Claude ecosystem.

This project is licensed under the MIT License - see the LICENSE file for details.

**🌐 Browse Templates**: aitmpl.com**📚 Documentation**: docs.aitmpl.com**💬 Community**: GitHub Discussions**🐛 Issues**: GitHub Issues

**⭐ Found this useful? Give us a star to support the project!**