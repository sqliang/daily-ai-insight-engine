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
tldr: AWS 发布 Agent Toolkit for AWS，为 AI 编码代理提供 AWS 服务的集成工具、技能和护栏。
objective_summary: AWS 发布了 Agent Toolkit for AWS，为 Claude Code、Codex、Cursor、Kiro 等
  AI 编码代理提供操作 AWS 服务的工具包。该工具包含四个插件（aws-core、aws-agents、aws-data-analytics、aws-agents-for
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - AWS
  - Anthropic
  technologies:
  - MCP
  - Amazon Bedrock
  - AgentCore
  - CDK
  - CloudFormation
  - S3 Tables
  - AWS Glue
  - Athena
  - CloudWatch
  - CloudTrail
  - IAM
  key_people: []
key_logic_flow:
- AWS 推出 Agent Toolkit for AWS，为 Claude Code、Codex、Cursor、Kiro 等 AI 编码代理提供操作和部署 AWS
  服务的工具、知识和安全护栏。
- 该工具包包含四个核心插件：aws-core（基础 AWS 操作）、aws-agents（Bedrock 和 AgentCore 构建智能体）、aws-data-analytics（数据湖与分析）、aws-agents-for-devsecops（安全审查与渗透测试）。
- 插件可通过各代理的官方插件市场安装，Claude Code 使用 /plugin install 命令，Codex 和 Cursor 通过各自的市场界面导入。
- AWS MCP Server 提供完整 AWS API 覆盖、沙盒化 Python 脚本执行环境和实时文档检索，支持 IAM 条件键实现代理与人类操作的权限隔离。
- Agent Toolkit 是 AWS Labs 此前发布的 MCP 服务器和插件的继承者，新增了 CloudWatch 指标监控、CloudTrail 审计日志和企业级访问控制功能。
- 工具包支持按需加载的 Agent Skills 技能包和项目级配置文件（rules/），代理仅在需要时加载相关技能。
extract_result: success
---

Help AI coding agents build, deploy, and manage applications on AWS.

The Agent Toolkit for AWS gives AI coding agents the tools, knowledge, and guardrails they need to work with AWS services. It works with the coding agents developers already use — including Claude Code, Codex, Cursor, and Kiro.

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

Add the AWS MCP Server to your Kiro MCP configuration (`.kiro/settings/mcp.json`

):

```
{
"mcpServers": {
"aws": {
"command": "uvx",
"args": [
"mcp-proxy-for-aws@1.6.2",
"https://aws-mcp.us-east-1.api.aws/mcp",
"--metadata", "AWS_REGION=us-west-2"
]
}
}
}
```


Note:It is recommended to pin to a specific version (e.g.,`@1.6.2`

) to ensure reproducible behavior and protect against supply chain risks. We recommend regularly checking PyPI for new stable versions and updating accordingly.

Then install skills from this repository:

```
npx skills add aws/agent-toolkit-for-aws/skills
```



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