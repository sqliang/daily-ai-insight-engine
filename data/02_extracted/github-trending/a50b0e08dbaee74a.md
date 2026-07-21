---
title: aws/agent-toolkit-for-aws
source: https://github.com/aws/agent-toolkit-for-aws
author: []
published: ''
created: '2026-06-26'
description: 'Official, AWS-supported MCP servers, skills, and plugins to help AI
  agents build on AWSAgent Toolkit for AWS Help AI coding agents build, deploy, and
  manage applications on AWS. The Agent Toolkit for AWS gives AI coding agents the
  tools, knowledge, and guardrails they need to work with AWS services. It works with
  the coding agents developers already use — including Claude Code, Codex, Cursor,
  and Kiro. Quick start Claude Code The plugins are available on the official Anthropic
  marketplace (claude-plugins-official) which is added to your Claude Code installation
  by default. Use the following commands to install supported plugins from the toolkit:
  For aws-core that covers service selection, CDK/CloudFormation, serverless, containers,
  storage, observability, billing, SDK usage, and deployment: /plugin install aws-core@claude-plugins-official
  Tip: If you get Plugin not found, update your local marketplace index first: /plugin
  marketplace update claude-plugins-official For aws-agents that covers building AI
  agents on AWS with Amazon Bedrock and AgentCore: /plugin install aws-agents@claude-plugins-official
  For aws-data-analytics that covers data lake, analytics, and ETL workflows with
  S3 Tables, AWS Glue, and Athena: /plugin install aws-data-analytics@claude-plugins-official
  For aws-agents-for-devsecops used to investigate incidents, review code and execute
  UAT for release readiness, scan code for vulnerabilities, and run penetration tests
  with AWS DevOps Agent and AWS Security Agent. /plugin marketplace add aws/agent-toolkit-for-aws
  /plugin install aws-agents-for-devsecops /reload-plugins # Or from Claude''s official
  marketplace: /plugin install aws-agents-for-devsecops@claude-plugins-official /reload-plugins
  # Setup: /aws-agents-for-devsecops:setup Codex In your terminal: codex plugin marketplace
  add aws/agent-toolkit-for-aws Then launch Codex and run /plugins to browse and install
  the aws-core plugin. Cursor Add this repository as a team marketplace from Settings
  → Plugins → Team Marketplaces → Add Marketplace → Import from Repo, pointing it
  at aws/agent-toolkit-for-aws. Cursor indexes the plugins listed in .cursor-plugin/marketplace.json
  on import. Then open the Plugins panel and install the aws-core plugin (start here),
  or aws-agents and aws-data-analytics as needed. Each plugin bundles the AWS MCP
  Server configuration and agent skills. Kiro Add the AWS MCP Server to your Kiro
  MCP configuration (.kiro/settings/mcp.json): { "mcpServers": { "aws": { "command":
  "uvx", "args": [ "mcp-proxy-for-aws@1.6.2", "https://aws-mcp.us-east-1.api.aws/mcp",
  "--metadata", "AWS_REGION=us-west-2" ] } } } Note: It is recommended to pin to a
  specific version (e.g., @1.6.2) to ensure reproducible behavior and protect against
  supply chain risks. We recommend regularly checking PyPI for new stable versions
  and updating accordingly. Then install skills from this repository: npx skills add
  aws/agent-toolkit-for-aws/skills Prerequisites: You need uv installed. An AWS account
  with credentials configured locally is required for API calls and script execution,
  but not for documentation search or skill discovery. See the user guide for detailed
  setup instructions. Other agents See the AWS MCP Server getting started guide for
  instructions on configuring the AWS MCP Server with your agent. Then install skills
  from this repository: npx skills add aws/agent-toolkit-for-aws/skills Prerequisites:
  You need uv installed. An AWS account with credentials configured locally is required
  for API calls and script execution, but not for documentation search or skill discovery.
  See the user guide for detailed setup instructions. What''s included Plugins Plugins
  bundle the AWS MCP Server configuration and agent skills into a single install for
  your coding agent. Plugin Description aws-core Core AWS skills and MCP Server configuration.
  Covers service selection, CDK/CloudFormation, serverless, containers, storage, observability,
  billing, SDK usage, and deployment. Start here. aws-agents Skills for building AI
  agents on AWS with Amazon Bedrock and AgentCore. aws-data-analytics Skills for data
  lake, analytics, and ETL workflows with S3 Tables, AWS Glue, and Athena. aws-agents-for-devsecops
  Investigate incidents, review code and execute UAT for release readiness, scan code
  for vulnerabilities, and run penetration tests with AWS DevOps Agent and AWS Security
  Agent. Plugins are currently available for Claude Code, Codex, and Cursor. For other
  agents, configure the AWS MCP Server directly and install skills from this repository.
  Skills Agent skills are curated packages of instructions and reference materials
  that help agents complete specific AWS tasks. Skills are loaded on demand — agents
  discover and retrieve only what''s relevant to the current task. npx skills add
  aws/agent-toolkit-for-aws/skills Browse the skills/ directory to see all available
  skills. Rules files Recommended project-level configuration files that tell agents
  how to use AWS most effectively — for example, by using the AWS MCP Server, discovering
  available skills, or searching documentation before acting. See rules/ for details.
  AWS MCP Server The AWS MCP Server is a managed server that gives agents access to
  AWS through the Model Context Protocol. It provides: Full AWS API coverage — Interact
  with any of the 300+ AWS services through a single authenticated endpoint. Sandboxed
  script execution — Agents can run Python scripts in an isolated environment for
  complex multi-step operations. Real-time documentation access — Search and retrieve
  current AWS documentation, API references, and service capabilities without authentication.
  Enterprise controls — Amazon CloudWatch metrics, IAM context keys for agent-specific
  policies, and AWS CloudTrail audit logging. For details on operation, available
  tools, authentication, and supported Regions, see the AWS MCP Server documentation.
  Documentation User guide — Setup, configuration, and reference documentation. AWS
  MCP Server tools — Reference for all available MCP tools. How the Agent Toolkit
  relates to the MCP servers, skills, and plugins in AWS Labs In 2025, AWS began releasing
  MCP servers, skills, and plugins as part of AWS Labs. The Agent Toolkit for AWS
  is the successor to those tools. We recommend using the Agent Toolkit for AWS, because
  it offers key features including: IAM condition keys that distinguish between agent
  actions and human actions, so you can write policies that apply only to agents.
  For example, you can write policies that only allow read-only actions through the
  MCP server, even if the user’s underlying IAM role can take write actions). CloudWatch
  metrics and CloudTrail audit logging for every request, so you can monitor and audit
  coding agent activity. Agent skills that have undergone thorough end-to-end evaluations,
  so you can be confident that workflows will complete successfully. AWS Labs MCP
  servers, skills, and plugins will continue to work and accept contributions, and
  over time the best of AWS Labs will be transitioned to the Agent Toolkit for AWS
  to ensure that customers can access the broadest array of tooling and guidance for
  their agents. License This project is licensed under the Apache-2.0 License. See
  LICENSE for details.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a50b0e08dbaee74a
source_type: community_discussion
tldr: AWS 发布 Agent Toolkit for AWS，为 Claude Code、Codex、Cursor 和 Kiro 等 AI 编程助手提供构建、部署和管理
  AWS 应用的工具、技能与安全防护措施，包含四个核心插件和 AWS MCP Server。
objective_summary: AWS 发布了 Agent Toolkit for AWS，这是其此前 AWS Labs 项目的继任者，旨在为 AI 编程助手提供
  AWS 服务集成能力。该工具包包含 aws-core、aws-agents、aws-data-analytics 和 aws-agents-for-devsecops
  四个插件，并以 AWS MCP Server 作为核心运行时组件，提供 300 多项 AWS 服务的 API 访问、沙箱化脚本执行和实时文档搜索。用户可通过终端命令或各平台插件市场在
  Claude Code、Codex、Cursor 和 Kiro 上安装使用。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - AWS
  - Anthropic
  technologies:
  - MCP
  - CDK
  - CloudFormation
  - Amazon Bedrock
  - AgentCore
  - S3 Tables
  - AWS Glue
  - Athena
  - IAM
  - CloudWatch
  - CloudTrail
  key_people: []
key_logic_flow:
- AWS 发布了 Agent Toolkit for AWS，为 AI 编程助手提供构建、部署和管理 AWS 应用的工具、知识和防护措施。
- 该工具包包含四个核心插件：aws-core 覆盖核心 AWS 技能，aws-agents 覆盖 AI 代理构建，aws-data-analytics 覆盖数据湖和分析，aws-agents-for-devsecops
  覆盖安全与合规。
- AWS MCP Server 是工具包的运行时核心，提供 300 多项 AWS 服务的统一 API 访问、沙箱化脚本执行和实时文档搜索。
- Agent Toolkit for AWS 支持 Claude Code、Codex、Cursor 和 Kiro 四种主流 AI 编程助手，每个平台各有独立的安装和配置方式。
- Agent Toolkit for AWS 是 AWS Labs 此前 MCP 服务器和插件的继任者，新增了 IAM 条件键、CloudWatch 监控和 CloudTrail
  审计日志等企业级功能。
specialized_tags:
  github:
    projectName: aws/agent-toolkit-for-aws
    projectUrl: https://github.com/aws/agent-toolkit-for-aws
    primaryLanguage: Python
    licenseType: Apache-2.0
    domain: ai_ml
    crossTags:
    - open-source
    aiDetail:
      primaryCategories:
      - agent_framework
      - llm_infra
      agentSubcategory:
      - orchestration
      - tool_use
      techTags:
      - MCP
      - function-calling
extract_result: success
object_mentions:
- object_type: project
  name: aws/agent-toolkit-for-aws
  canonical_name: aws/agent-toolkit-for-aws
  url: https://github.com/aws/agent-toolkit-for-aws
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Agent Toolkit for AWS 为 AI 编程助手提供构建、部署和管理 AWS 应用程序所需的工具、知识和安全防护措施，支持 Claude Code
    等主流编程助手。
  - 该工具包是 AWS Labs 此前发布的 MCP 服务器、技能和插件的继任者，新增了 IAM 条件键和 CloudTrail 审计日志等企业级功能。
  article_id: a50b0e08dbaee74a
- object_type: product
  name: AWS MCP Server
  canonical_name: AWS MCP Server
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - AWS MCP Server 是一个托管服务器，通过模型上下文协议让 AI 助手与 300 多项 AWS 服务交互，提供沙箱化脚本执行和实时文档搜索功能。
  - 该服务器包含完整 AWS API 覆盖、沙箱化脚本执行、实时文档搜索以及 CloudWatch 指标和 CloudTrail 审计日志等企业级控制功能。
  article_id: a50b0e08dbaee74a
- object_type: project
  name: aws-core
  canonical_name: aws-core
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - aws-core 插件涵盖服务选择、CDK/CloudFormation、无服务器、容器、存储、可观测性、账单、SDK 使用和部署等核心 AWS 技能。
  - 用户可通过 /plugin install aws-core@claude-plugins-official 命令在 Claude Code 中安装 aws-core
    插件。
  article_id: a50b0e08dbaee74a
- object_type: project
  name: aws-agents
  canonical_name: aws-agents
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - aws-agents 插件涵盖使用 Amazon Bedrock 和 AgentCore 在 AWS 上构建 AI 代理的相关技能。
  - 用户可通过 /plugin install aws-agents@claude-plugins-official 命令在 Claude Code 中安装该插件。
  article_id: a50b0e08dbaee74a
- object_type: project
  name: aws-data-analytics
  canonical_name: aws-data-analytics
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - aws-data-analytics 插件涵盖数据湖、分析和 ETL 工作流，支持 S3 Tables、AWS Glue 和 Athena 等服务的集成。
  - 用户可通过 /plugin install aws-data-analytics@claude-plugins-official 命令在 Claude Code
    中安装该插件。
  article_id: a50b0e08dbaee74a
- object_type: project
  name: aws-agents-for-devsecops
  canonical_name: aws-agents-for-devsecops
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - aws-agents-for-devsecops 插件用于调查事件、审查代码、执行 UAT、扫描漏洞以及使用 AWS DevOps Agent 和 AWS
    Security Agent 运行渗透测试。
  - 该插件可通过 /plugin install aws-agents-for-devsecops@claude-plugins-official 命令从官方市场安装。
  article_id: a50b0e08dbaee74a
---

Help AI coding agents build, deploy, and manage applications on AWS.

The Agent Toolkit for AWS gives AI coding agents the tools, knowledge, and guardrails they need to work with AWS services. It works with the coding agents developers already use — including Claude Code, Codex, Cursor, and Kiro.

Use the Agent Toolkit directly from your terminal with the AWS CLI:

```
aws configure agent-toolkit
```


See the AWS CLI integration guide for setup, configuration, and usage instructions.

The plugins are available on the official Anthropic marketplace (`claude-plugins-official`

) which is added to your Claude Code installation by default.
Use the following commands to install supported plugins from the toolkit:

For `aws-core`

that covers service selection, CDK/CloudFormation, serverless, containers, storage, observability, billing, SDK usage, and deployment:

```
/plugin install aws-core@claude-plugins-official
```



Tip:If you get`Plugin not found`

, update your local marketplace index first:`/plugin marketplace update claude-plugins-official`


For `aws-agents`

that covers building AI agents on AWS with Amazon Bedrock and AgentCore:

```
/plugin install aws-agents@claude-plugins-official
```


For `aws-data-analytics`

that covers data lake, analytics, and ETL workflows with S3 Tables, AWS Glue, and Athena:

```
/plugin install aws-data-analytics@claude-plugins-official
```


For `aws-agents-for-devsecops`

used to investigate incidents, review code and execute UAT for release readiness, scan code for vulnerabilities, and run penetration tests with AWS DevOps Agent and AWS Security Agent.

```
/plugin marketplace add aws/agent-toolkit-for-aws
/plugin install aws-agents-for-devsecops
/reload-plugins
# Or from Claude's official marketplace:
/plugin install aws-agents-for-devsecops@claude-plugins-official
/reload-plugins
# Setup:
/aws-agents-for-devsecops:setup
```


In your terminal:

```
codex plugin marketplace add aws/agent-toolkit-for-aws
```


Then launch Codex and run `/plugins`

to browse and install the **aws-core** plugin.

Add this repository as a team marketplace from **Settings → Plugins → Team Marketplaces → Add Marketplace → Import from Repo**, pointing it at `aws/agent-toolkit-for-aws`

. Cursor indexes the plugins listed in `.cursor-plugin/marketplace.json`

on import.

Then open the **Plugins** panel and install the **aws-core** plugin (start here), or **aws-agents** and **aws-data-analytics** as needed. Each plugin bundles the AWS MCP Server configuration and agent skills.

Kiro setup has two independent parts: the AWS MCP Server (for runtime AWS API access and documentation search) and local skills (for task-specific agent guidance). They complement each other but work independently — skills don't require the MCP server, and the MCP server doesn't serve locally-installed skills.

**1. Add the AWS MCP Server** to your Kiro MCP configuration (`.kiro/settings/mcp.json`

):

```
{
"mcpServers": {
"aws": {
"command": "uvx",
"args": [
"mcp-proxy-for-aws@1.6.3",
"https://aws-mcp.us-east-1.api.aws/mcp",
"--metadata",
"AWS_REGION=us-west-2"
]
}
}
}
```


Note:It is recommended to pin to a specific version (e.g.,`@1.6.3`

) to ensure reproducible behavior and protect against supply chain risks. We recommend regularly checking PyPI for new stable versions and updating accordingly.

The MCP server gives your agent access to AWS APIs, sandboxed script execution, and real-time documentation search.

**2. Install skills** from this repository:

```
npx skills add aws/agent-toolkit-for-aws/skills
```


This installs skill files to `~/.kiro/skills/`

(global) or `.kiro/skills/`

(project-level). Each skill is a directory containing a `SKILL.md`

file and optionally a `references/`

subdirectory with additional context the agent reads from the local filesystem when needed. Kiro discovers installed skills automatically and activates them on demand when a task matches.


Prerequisites:You need uv installed. An AWS account with credentials configured locally is required for API calls and script execution, but not for documentation search or skill discovery. See the user guide for detailed setup instructions.

See the AWS MCP Server getting started guide for instructions on configuring the AWS MCP Server with your agent.

Then install skills from this repository:

```
npx skills add aws/agent-toolkit-for-aws/skills
```



Prerequisites:You need uv installed. An AWS account with credentials configured locally is required for API calls and script execution, but not for documentation search or skill discovery. See the user guide for detailed setup instructions.

Plugins bundle the AWS MCP Server configuration and agent skills into a single install for your coding agent.

| Plugin | Description |
|---|---|
| aws-core | Core AWS skills and MCP Server configuration. Covers service selection, CDK/CloudFormation, serverless, containers, storage, observability, billing, SDK usage, and deployment. Start here. |
| aws-agents | Skills for building AI agents on AWS with Amazon Bedrock and AgentCore. |
| aws-data-analytics | Skills for data lake, analytics, and ETL workflows with S3 Tables, AWS Glue, and Athena. |
| aws-agents-for-devsecops | Investigate incidents, review code and execute UAT for release readiness, scan code for vulnerabilities, and run penetration tests with AWS DevOps Agent and AWS Security Agent. |

Plugins are currently available for Claude Code, Codex, and Cursor. For other agents, configure the AWS MCP Server directly and install skills from this repository.

Agent skills are curated packages of instructions and reference materials that help agents complete specific AWS tasks. Skills are loaded on demand — agents discover and retrieve only what's relevant to the current task.

```
npx skills add aws/agent-toolkit-for-aws/skills
```


Browse the `skills/`

directory to see all available skills.

Recommended project-level configuration files that tell agents how to use AWS most effectively — for example, by using the AWS MCP Server, discovering available skills, or searching documentation before acting.

See `rules/`

for details.

The AWS MCP Server is a managed server that gives agents access to AWS through the Model Context Protocol. It provides:

**Full AWS API coverage**— Interact with any of the 300+ AWS services through a single authenticated endpoint.**Sandboxed script execution**— Agents can run Python scripts in an isolated environment for complex multi-step operations.**Real-time documentation access**— Search and retrieve current AWS documentation, API references, and service capabilities without authentication.**Enterprise controls**— Amazon CloudWatch metrics, IAM context keys for agent-specific policies, and AWS CloudTrail audit logging.

For details on operation, available tools, authentication, and supported Regions, see the AWS MCP Server documentation.

- User guide — Setup, configuration, and reference documentation.
- AWS MCP Server tools — Reference for all available MCP tools.

In 2025, AWS began releasing MCP servers, skills, and plugins as part of AWS Labs. The Agent Toolkit for AWS is the successor to those tools. We recommend using the Agent Toolkit for AWS, because it offers key features including:

- IAM condition keys that distinguish between agent actions and human actions, so you can write policies that apply only to agents. For example, you can write policies that only allow read-only actions through the MCP server, even if the user’s underlying IAM role can take write actions).
- CloudWatch metrics and CloudTrail audit logging for every request, so you can monitor and audit coding agent activity.
- Agent skills that have undergone thorough end-to-end evaluations, so you can be confident that workflows will complete successfully.

AWS Labs MCP servers, skills, and plugins will continue to work and accept contributions, and over time the best of AWS Labs will be transitioned to the Agent Toolkit for AWS to ensure that customers can access the broadest array of tooling and guidance for their agents.

This project is licensed under the Apache-2.0 License. See LICENSE for details.