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
impact_score:
  score: 3.5
  reason: 该项目是一个 Claude Code 模板集合仓库，提供 100+ 预配置模板（Agents、Commands、MCPs、Settings、Hooks、Skills）的便捷
    npx 安装。它聚合了官方 Anthropic、K-Dense Inc.（139 个科学技能）及多个社区来源的模板资源，降低了 Claude Code 的上手门槛。但本质上是生态工具和资源配置的封装整合，不涉及底层技术突破或行业范式转移，影响范围限定在
    Claude Code 用户社群内，属于日常更新级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 100+ 免配置模板能否真正提升 Claude Code 开发效率及生态兼容性
hype_assessment:
  level: low
  reason: 文章以技术性描述为主，提供了具体的安装命令（含多种安装方式）、六大组件分类表及对应示例、以及各来源模板的授权归属明细。虽然包含 Beta 版网站推广和
    GitHub star 引导，但未使用'颠覆性'、'革命性'等 PR 滥用词汇，整体信息真实可验证，概念炒作成分极低。
information_entropy: high
domain_disruption:
  technical_innovation: 无。该项目是对现有 Claude Code 配置模板的收集、分类和便捷安装封装，不涉及底层技术架构或算法创新。
  business_model: 通过开源聚合模式构建 Claude Code 生态中间件，降低开发者使用门槛，间接增强 Anthropic 平台粘性。采用 MIT
    许可并保留各来源原始授权，依赖社区贡献维持增长，类似于 npx shadcn/ui 的生态打法。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 该仓库本质上是在构建 Claude Code 生态的模板分发层与工具链基础设施。长期复利价值取决于两个关键变量：(1) Claude Code
    本身的用户基数和平台生命力——如果 Anthropic 持续投入 Claude Code，模板生态会随之水涨船高，形成正向循环；(2) 该仓库能否成为事实上的模板标准入口——当前已聚合
    Anthropic 官方技能、K-Dense 的 139 个科学技能、以及社区贡献，具有先发聚合效应。但风险也很明确：MIT 开源协议意味着商业变现路径不清晰；模板本身与
    Claude Code 强耦合，若 Anthropic 官方推出类似模板市场，该仓库可能被边缘化。整体属于'细分赛道潜在基础设施，但需持续验证平台依附性和社区网络效应能否固化'的定位，评分落在
    4-7 区间的中位。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- davila7
- K-Dense Inc.
competitive_casualty:
- 碎片化 Claude Code 模板个人维护者
- Cursor
- GitHub Copilot
market_opportunities:
- 企业可借助该模板库快速搭建团队级 Claude Code 工作流，大幅降低 AI 编码助手的采纳门槛，适合 IT 咨询和内部效率团队优先探索
- 开发者可基于该模板框架创建垂直领域（如医疗、金融、法律合规）的专用技能模板，形成差异化产品并以订阅模式变现
- 该仓库的生态模式验证了 Claude Code 模板市场的可行性，类似 VS Code 扩展市场的平台化机会值得关注
risk_matrix:
  regulatory: 模板聚合涉及多来源、多许可证（MIT、CC0、Apache 2.0）的组件，混合使用时的许可证合规和归属要求需谨慎处理，存在潜在的版权纠纷风险
  technological: Claude Code 的 API 和配置格式仍处于快速迭代期，模板可能随版本更新而失效，对维护者的持续跟进能力要求较高
  competitive: AI 编码助手竞争白热化（GitHub Copilot、Cursor、Windsurf 等），Claude Code 生态仍在早期，模板生态的价值高度依赖于
    Claude Code 自身的市场渗透率
  ethical: 安全审计和代码生成类模板若被恶意使用可能放大攻击能力；模板质量参差不齐可能引入供应链安全隐患
  additional:
  - 模板的长期维护依赖社区活跃度，如果核心维护者精力转移可能导致项目停滞或模板过时
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
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