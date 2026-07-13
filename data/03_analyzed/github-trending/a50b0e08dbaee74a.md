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
pipeline_stage: ingested
id: a50b0e08dbaee74a
impact_score:
  score: 6.5
  reason: AWS 发布 Agent Toolkit 是一项重要的平台级产品发布，它为 AI 编码代理（Claude Code、Codex、Cursor、Kiro）提供了操作
    AWS 的标准化工具链和知识库。核心价值在于：通过 MCP 协议统一了 300+ AWS 服务的交互接口，内置沙箱执行和 CloudTrail 审计日志等企业控制能力，并为每个主流
    AI 代理提供了即装即用的插件。这直接解决了 AI 编码代理操作云基础设施时缺乏结构化工具和最佳实践的痛点。虽未达到范式转移级别（8-10分），但作为首个由云厂商官方发布的
    AI 代理工具包，它改变了 AI 辅助云开发的竞争格局，迫使其他云厂商跟进类似能力。评分 6.5，属于重要的产品发布级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 如何通过插件和 MCP 配置让 AI 代理安全、高效地操作 AWS 服务
hype_assessment:
  level: low
  reason: README 内容务实，未出现 '颠覆'、'革命性' 等 PR 话术。提供了具体的插件列表（aws-core、aws-agents、aws-data-analytics、aws-agents-for-devsecops）、针对不同代理的精确安装命令、版本锁定建议（@1.6.2），以及沙箱执行、CloudTrail
    审计等实际能力说明。信息密度高，无明显概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 为 AI 编码代理提供标准化的 AWS 操作工具链和知识库，通过 MCP 协议实现 300+ AWS 服务的统一交互接口，并内置沙箱执行环境、实时文档检索和
    IAM 安全护栏。agent skills 的按需加载机制使得代理仅检索当前任务相关的内容，降低了上下文窗口消耗。
  business_model: 降低 AWS 的 AI 辅助开发门槛，可能显著推动 AWS 服务使用量增长。同时为云厂商与 AI 编码代理的深度集成树立了行业标杆，未来其他云厂商（GCP、Azure）很可能推出类似工具包，改变云服务消费方式。
engineering_complexity: production_ready
compound_value:
  score: 8.5
  reason: AWS 正在将自身塑造为 AI Agent 时代的默认云基础设施层。通过发布 MCP 原生工具包，AWS 让所有主流 AI 编码代理（Claude
    Code、Codex、Cursor、Kiro）都能原生操作其 300+ 项服务。这本质上是云计算的接口范式迁移——从人类通过控制台/CLI 管理云，转向 Agent
    通过 MCP 协议直接调用云。一旦开发者的 Agent 工作流深度绑定 AWS 工具链，迁移成本将极高，形成强大的平台锁定效应。此外，AWS 采用开放策略（支持多
    Agent），但工具包本身是 AWS 专属，不会产生跨云标准化红利。随着 Agent 驱动开发成为主流，这套工具包的采用曲线与 Agent 渗透率正相关，复利效应显著。风险点在于：其他云厂商（GCP、Azure）必然跟进，且
    Agent 生态仍处早期，标准化协议（MCP）的演进方向尚未完全确定。
value_capture_layer: cloud_platform
moat_impact: strengthens_monopoly
key_beneficiaries:
- Amazon (AWS)
- Anthropic (Claude Code)
- OpenAI (Codex)
- Cursor
- AWS 企业客户
competitive_casualty:
- Google Cloud Platform (GCP)
- Microsoft Azure
- 中小型云服务商
- 传统 DevOps 与云管理工具（如 HashiCorp Terraform 等被 Agent 原生工作流旁路）
market_opportunities:
- AWS官方Agent Toolkit的发布验证了MCP协议作为AI Agent与云基础设施交互的事实标准，创业团队可快速切入其他云平台（GCP/Azure/阿里云）的MCP适配层开发，抢占多云Agent工具链空白市场
- 企业可基于aws-agents-for-devsecops插件构建自动化的代码审计、渗透测试与事故响应流水线，将安全运营从人工驱动转为AI Agent驱动的DevSecOps模式，显著降低安全人力成本
- AWS Agent Skills的按需加载机制为AI Agent知识管理提供了新范式，可借鉴此模式为企业的内部技术栈（如K8s运维、数据库管理、监控告警等）构建私有化Agent技能包，打造企业专属的AI运维中台
risk_matrix:
  regulatory: AI Agent直接执行AWS API调用可能引发合规风险：Agent自动化操作超出预期范围造成的资源变更、数据泄露或配置错误，责任主体难以界定；企业需建立Agent行为的IAM细粒度权限管控、操作审批流和全链路CloudTrail审计日志，以满足SOC2/ISO27001等合规要求
  technological: 与AWS生态深度绑定带来显著的厂商锁定风险：Agent Toolkit高度依赖AWS MCP Server、Bedrock、CDK等专有服务，若后续出现更优秀的开源多云Agent方案，迁移成本极高；同时Agent依赖的MCP
    Server版本演进可能导致旧插件兼容性问题
  competitive: Azure和GCP将迅速跟进推出各自的云Agent工具包，AWS的先发优势窗口有限（预计3-6个月）；Cursor、Codex等IDE平台也可能自建云资源管理工具链，挤压AWS插件在Agent生态中的话语权；价格战风险——云厂商可能以免费Agent工具作为争夺开发者的钩子产品
  ethical: AI Agent获得云基础设施操作权限后，自动化错误（如误删生产数据库、错误开放安全组端口、无节制创建昂贵资源）可能导致大规模故障和经济损失，而责任归属在Agent开发者、云厂商和操作者之间模糊不清；Agent技能包中的最佳实践可能隐含偏见或过时配置，误导开发者
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: strategic_invest
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