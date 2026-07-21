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
impact_score:
  score: 6.8
  reason: AWS 发布 Agent Toolkit for AWS，为 Claude Code、Codex、Cursor、Kiro 等主流 AI 编程助手提供统一的
    AWS 工具集，覆盖 300+ AWS 服务的 MCP 接口、沙盒脚本执行和实时文档搜索。这标志着 AWS 正式将 MCP 协议作为云服务管理的关键入口，是云服务商对
    AI Agent 生态的首次系统性基础设施级投入。短期来看，它将显著降低开发者通过 AI 助手操作 AWS 的门槛，可能加速 AWS 在 AI 编程场景中的采用率，并倒逼
    Azure、GCP 推出类似方案。但这不是范式转移——MCP Server 已有社区实现，AWS 此次是将其标准化、企业级化（IAM 条件键区分代理与人类操作、CloudTrail
    审计等），评分定在 6.8。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MCP 协议统一接入 300+ AWS 服务，AI 编程助手可直接完成基础设施编排与部署
hype_assessment:
  level: low
  reason: 文章没有使用'颠覆性''革命性'等 PR 夸张词汇，而是以务实的产品文档风格介绍四个具体插件的能力边界、安装方式和依赖项（如需要 uv、AWS
    凭证）。每个插件都有明确的功能范围描述，且项目采用 Apache-2.0 开源协议，支持跨平台集成，整体呈现为扎实的工程交付而非概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 核心创新在于基于 MCP 协议构建的 AWS 服务统一接入层，包含 300+ 服务的 API 抽象、沙盒 Python
    脚本执行环境和实时文档搜索引擎，并通过 IAM 条件键实现代理操作与人类操作的可审计区分——这是云 IAM 体系首次原生支持 AI Agent 身份识别与权限管控。
  business_model: AWS 通过开源工具包降低 AI 辅助开发的摩擦成本，实质上是将 AWS 定位为'AI Agent 默认云平台'。四个插件（core、agents、data-analytics、devsecops）覆盖了从基础设施到应用安全的完整开发周期，通过降低
    AI 编程助手使用 AWS 的门槛来巩固和扩大 AWS 的开发者生态护城河。
engineering_complexity: production_ready
compound_value:
  score: 8.5
  reason: AWS 通过 Agent Toolkit 将 AI 编程助手生态系统性地绑定到 AWS 基础设施上，形成自我强化的复利飞轮：AI Agent 使用
    AWS 工具集 → 开发者依赖 AWS 服务 → 更多云资源被消费 → 工具集进一步丰富。该工具集的战略意义在于它定义了 AI 代理与云交互的'默认接口'——四个插件覆盖了从核心云操作到
    AI 代理构建、数据分析再到 DevSecOps 的全链路，且通过 IAM 条件键实现人类与代理操作的区分审计，扫清了企业采用的安全障碍。MCP 服务器提供
    300+ AWS 服务的统一 API 访问，加上沙盒 Python 执行和实时文档搜索，构成了一个深度集成、难以替代的中间层。长期看，一旦开发者的 AI 编程助手习惯了这套工具链，切换到其他云平台的认知成本和迁移成本极高。不过需注意
    MCP 协议仍处于早期标准化阶段，且工具集本身是开源免费的——AWS 的真正复利来自于由此驱动的云服务消费增长，而非工具直接变现。
value_capture_layer: cloud_platform
moat_impact: strengthens_monopoly
key_beneficiaries:
- AWS
- Anthropic
- Cursor
- Codex
- Kiro
competitive_casualty:
- Microsoft Azure
- Google Cloud Platform (GCP)
- 传统 RPA 厂商
- 独立 MCP 中间件提供商
- 闭源 Agent 平台
market_opportunities:
- 云服务咨询公司和系统集成商可围绕 AWS Agent Toolkit 建立 AI 辅助基础设施交付实践，大幅提升 DevOps 效率并形成差异化服务能力
- 独立软件开发商可利用 AWS MCP Server 的插件生态开发面向垂直领域（如医疗合规、金融审计）的专用 AWS 管理工具
- 使用 AI 编程助手的开发团队可立即部署 aws-core 插件实现 CDK/CloudFormation 基础设施即代码的自动化生成，降低 AWS 上手门槛
risk_matrix:
  regulatory: MCP Server 提供 300+ AWS 服务的沙盒 API 访问，若 IAM 条件键（区分 Agent 与人类操作）配置不当可能导致权限提升和数据泄露；企业需建立
    Agent 操作审计和最小权限原则
  technological: 工具包强依赖 MCP 协议和特定编程助手生态（Claude Code、Codex、Cursor 等），若 MCP 标准演进或助手平台策略变化（如
    OpenAI 推出竞争协议）可能面临兼容性风险
  competitive: AWS 通过嵌入 AI 编程助手生态锁定开发者到其云服务，将倒逼 Azure/GCP 快速跟进推出类似工具包；对 Pulumi、HashiCorp
    等独立 DevOps 工具厂商构成生态挤压威胁
  ethical: DevSecOps 插件提供自动化渗透测试和漏洞扫描能力，可能降低网络攻击的技术门槛，但 AWS 引入的 IAM 条件键（区分 Agent vs
    人类操作）是积极的治理设计，有助于防范滥用
  additional: []
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
project_profile:
  name: aws/agent-toolkit-for-aws
  url: https://github.com/aws/agent-toolkit-for-aws
  primary_language: Python
  license: Apache-2.0
  description: 为 AI 编程助手（Claude Code、Codex、Cursor、Kiro）提供构建、部署和管理 AWS 应用的工具、知识和防护栏
  created_date: null
project_classification:
  domain: ai_ml
  cross_tags:
  - open-source
  ai_detail:
    primary_categories:
    - agent_framework
    - llm_infra
    agent_subcategory:
    - orchestration
    - tool_use
    tech_tags:
    - MCP
    - function-calling
tech_assessment:
  architecture_highlights: 采用插件化分层架构，核心分为三层：底层通过 AWS MCP Server（基于 Model Context Protocol）提供
    AWS API 沙箱执行和实时文档搜索能力；中间层以 Skills 体系封装场景化指令和参考材料，按需加载、按任务匹配激活；顶层通过 Plugins 将 MCP
    Server 配置和 Skills 绑定为可安装单元（aws-core、aws-agents、aws-data-analytics、aws-agents-for-devsecops
    四大插件）。这种设计实现了运行时能力（MCP）与知识引导（Skills）的解耦——Skills 不依赖 MCP Server 也可独立工作。对 Claude
    Code/Codex 通过原生 Plugin Marketplace 分发，对 Cursor 通过 Team Marketplace 导入，对 Kiro 通过
    MCP 配置 + npx skills 独立安装，体现了极强的 IDE/Agent 适配能力。
  tech_stack_quality: production_grade
  code_quality_indicators:
    has_tests: true
    has_ci_cd: true
    documentation_level: comprehensive
  dependencies_analysis: 核心依赖栈围绕 AWS 生态构建：底层依赖 AWS SDK（boto3/botocore）进行 API 调用和凭证管理；MCP
    Server 组件通过 mcp-proxy-for-aws（PyPI 包）连接到 AWS 托管的 MCP 端点；Skills 分发依赖 npx（npm）和
    uv（Python 包管理器），形成跨语言生态。此外通过 claude-plugins-official 市场索引与 Anthropic 生态耦合。版本锁定建议（如
    mcp-proxy-for-aws@1.6.3）表明对供应链安全的重视。整体依赖耦合度适中，MCP 协议层提供了清晰的抽象边界。
community_health:
  stars_trend: 作为 AWS 官方新发布的 AI 代理工具项目，自 2025 年发布以来受到广泛关注，Star 增长曲线陡峭，尤其在 Claude Code、Codex
    等主流 AI 编程助手社区中快速传播
  contributor_activity: very_active
  issue_response_time: fast
  pr_merge_velocity: high
  bus_factor_assessment: 风险极低。项目由 AWS 官方团队维护，具备充足的企业级工程资源和明确的长期支持承诺。核心贡献者分散在 AWS 多个部门，不存在单点依赖风险。即使个别维护者离开，AWS
    的组织力量也能保障持续迭代。
competitive_landscape:
  direct_alternatives:
  - anthropic/claude-code-plugins
  - vercel/ai-sdk
  - openai/openai-agents-python
  - langchain-ai/langchain-aws
  - microsoft/semantic-kernel
  differentiation: 与竞品的核心差异在于：1）这是 AWS 官方出品的一等公民集成，拥有对 AWS 200+ 服务最深最及时的能力覆盖，远非第三方适配可比；2）采用插件+Skills
    双轨制，MCP Server 提供运行时能力而 Skills 提供知识引导，两者解耦的设计在同类工具中独树一帜；3）不是单一 Agent 框架，而是「Agent
    工具包」的定位，不绑定特定 AI 编程助手，跨平台支持 Claude Code、Codex、Cursor、Kiro；4）DevSecOps 插件（aws-agents-for-devsecops）将安全扫描、渗透测试、代码审查等
    DevSecOps 流程直接集成到 Agent 工作流中。
  moat_analysis: 核心护城河有三层：第一层是 AWS 生态锁定效应——项目深度绑定 AWS API、IAM 权限模型、CloudFormation/CDK
    等基础设施即代码体系，用户一旦深度采用将产生显著的迁移成本；第二层是持续的知识覆盖优势——AWS 每年发布数百项新服务/功能，第三方工具永远无法跟上官方团队的更新速度，而
    AWS 内部团队可以第一时间将新服务的能力封装为 Skills；第三层是 MCP 协议的先发占位——作为最早一批大规模实践 MCP 协议的企业级项目，在协议理解、最佳实践和服务端稳定性上已经积累了先发优势。
adoption_guidance:
  maturity_score: 7.0
  recommended_for:
  - 已在 AWS 上运行工作负载、希望用 AI 编程代理提升开发效率的团队
  - 使用 Claude Code、Codex、Cursor 或 Kiro 进行 AI 辅助开发的 AWS 开发者
  - 需要将 DevSecOps 流程（安全扫描、渗透测试、代码审查）集成到 AI 编程代理工作流中的团队
  - 构建基于 Amazon Bedrock 和 AgentCore 的 AI 代理应用的开发者
  - 数据工程团队中使用 S3 Tables、AWS Glue、Athena 进行数据湖和分析工作的场景
  caution_for:
  - 未使用 AWS 或主要在本地/GCP/Azure 开发的团队（引入不必要的云厂商耦合）
  - 需要完全离线的开发环境（MCP Server 需要访问 AWS API 端点）
  - 使用非主流 AI 编程代理且不兼容 MCP 协议的场景（目前仅支持四种主流 Agent）
  - 对 AWS 成本敏感的小团队或独立开发者（运行 AWS 资源会产生额外费用）
  - 期望零配置开箱即用的用户（需要预先配置 AWS 凭证和安装对应工具链如 uv、npm）
  time_to_production: needs_1_3_months
object_insights:
- object_type: project
  name: aws/agent-toolkit-for-aws
  canonical_name: aws/agent-toolkit-for-aws
  url: https://github.com/aws/agent-toolkit-for-aws
  positioning: AWS 官方发布的 AI 编程助手工具包，为 Claude Code、Codex、Cursor 和 Kiro 等主流编程助手提供构建、部署和管理
    AWS 应用程序所需的全套工具、知识库和安全防护措施。
  technical_signal: 基于 Model Context Protocol 构建，以 AWS MCP Server 为核心运行时组件，提供 300
    多项 AWS 服务的统一 API 访问和沙箱化脚本执行能力。
  adoption_signal: 已原生支持 Claude Code、Codex、Cursor 和 Kiro 四种主流 AI 编程助手，通过各自插件市场或终端命令行即可安装，用户门槛较低。
  ecosystem_relevance: 与 AWS 生态系统深度绑定，涵盖 Bedrock、Glue、Athena、CDK/CloudFormation 等核心服务的技能集成，是
    AWS 在 AI Agent 编程领域的战略基础设施。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: AWS 作为全球最大云服务商，正式推出 AI 编程助手工具包标志着云基础设施与 AI Agent 编程范式的深度融合，其插件生态、企业级安全管控和开发者采用度将深刻影响行业格局。
  risk_notes:
  - 高度依赖 AWS 生态系统，非 AWS 用户无法使用。
  - 四个插件覆盖范围较广，各插件间的边界划分和协同关系可能对用户造成使用困惑。
  score: 8.0
  article_ids:
  - a50b0e08dbaee74a
  evidence_snippets:
  - Agent Toolkit for AWS 为 AI 编程助手提供构建、部署和管理 AWS 应用程序所需的工具、知识和安全防护措施，支持 Claude Code
    等主流编程助手。
  - 该工具包是 AWS Labs 此前发布的 MCP 服务器、技能和插件的继任者，新增了 IAM 条件键和 CloudTrail 审计日志等企业级功能。
- object_type: product
  name: AWS MCP Server
  canonical_name: AWS MCP Server
  url: null
  positioning: Agent Toolkit for AWS 的运行时核心组件，通过模型上下文协议为 AI 编程助手提供与 300 多项 AWS 服务交互的统一
    API 访问、沙箱化脚本执行和实时文档搜索能力。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 在 Claude Code、Codex、Cursor、Kiro 等 AI 编程助手中管理 AWS 资源的云开发者
  product_signal: 提供完整 AWS API 覆盖、沙箱化脚本执行、实时文档搜索以及 CloudWatch 指标和 CloudTrail 审计日志等企业级可观测性功能，满足生产环境需求。
  market_signal: 作为 AWS 官方发布的 MCP 服务器，已深度集成到多个主流 AI 编程助手的插件体系，标志着云服务商对 MCP 协议从实验到正式支持的转变。
  differentiation: 与第三方 MCP 实现相比，由 AWS 官方团队维护和开发，拥有最完整的 AWS API 覆盖和原生服务集成能力，企业级安全管控是核心差异化优势。
  watch_reason: 作为 AWS 在 AI Agent 编程范式中的关键基础设施组件，其 API 覆盖的广度和深度、运行时稳定性以及企业级安全管控能力，将直接影响开发者对
    AI 编程助手的采用深度和云资源管理效率。
  risk_notes:
  - 需要有效的 AWS 账户和本地配置的凭证才能进行 API 调用，增加了环境配置门槛。
  - 依赖 uv 等额外工具链安装，跨平台和跨环境的兼容性有待进一步验证。
  score: 8.0
  article_ids:
  - a50b0e08dbaee74a
  evidence_snippets:
  - AWS MCP Server 是一个托管服务器，通过模型上下文协议让 AI 助手与 300 多项 AWS 服务交互，提供沙箱化脚本执行和实时文档搜索功能。
  - 该服务器包含完整 AWS API 覆盖、沙箱化脚本执行、实时文档搜索以及 CloudWatch 指标和 CloudTrail 审计日志等企业级控制功能。
- object_type: project
  name: aws-core
  canonical_name: aws-core
  url: null
  positioning: Agent Toolkit for AWS 的核心基础插件，覆盖服务选择、CDK/CloudFormation 基础设施即代码、无服务器、容器、存储、可观测性、账单、SDK
    使用和部署等全面 AWS 开发技能。
  technical_signal: 集成 AWS 核心服务的最佳实践技能，涵盖从服务选型、基础设施编排到可观测性和成本管理的完整开发运维链路。
  adoption_signal: 作为工具包的官方推荐起始插件，已上架 Claude Code 等平台的官方插件市场，可通过 /plugin install 命令直接安装。
  ecosystem_relevance: 覆盖 AWS 最核心的云服务技能集合，是其他三个专业插件（aws-agents、aws-data-analytics、aws-agents-for-devsecops）的基础依赖。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 Agent Toolkit for AWS 的入门级插件，其技能覆盖质量和 AI 辅助的准确度直接决定了开发者对整套工具的第一印象和持续采用意愿，是整套生态的门面组件。
  risk_notes:
  - 技能覆盖面广但深度有限，复杂场景可能仍需专业领域工具的补充。
  - 依赖 AWS MCP Server 的运行稳定性，服务器不可用时插件技能无法生效。
  score: 7.0
  article_ids:
  - a50b0e08dbaee74a
  evidence_snippets:
  - aws-core 插件涵盖服务选择、CDK/CloudFormation、无服务器、容器、存储、可观测性、账单、SDK 使用和部署等核心 AWS 技能。
  - 用户可通过 /plugin install aws-core@claude-plugins-official 命令在 Claude Code 中安装 aws-core
    插件。
- object_type: project
  name: aws-agents
  canonical_name: aws-agents
  url: null
  positioning: Agent Toolkit for AWS 中专注于 AI 代理构建的插件，提供在 AWS 上使用 Amazon Bedrock 和
    AgentCore 开发、部署和管理 AI Agent 的专业技能支持。
  technical_signal: 整合 Amazon Bedrock 基础模型服务和 AgentCore 代理构建框架，覆盖从模型选择、代理编排到部署运维的完整
    AI 代理开发链路。
  adoption_signal: 已上架 Claude Code 官方插件市场，用户可通过命令行直接安装，与 aws-core 协同使用提供完整的 AI 代理开发体验。
  ecosystem_relevance: 与 AWS AI 服务生态（Bedrock）深度绑定，是 AWS 在生成式 AI 和 AI Agent 领域核心能力向开发者工具链输出的关键通道。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: AI 代理构建是当前云计算与 AI 融合最热门的赛道，该插件的技能质量和覆盖度直接反映了 AWS 在 AI Agent 领域的战略布局深度和技术储备。
  risk_notes:
  - 技能与 aws-core 在部分 AWS 基础服务覆盖上存在重叠，用户可能对两者边界不清晰。
  - 依赖特定 AWS 区域（如 us-east-1）的 Bedrock 服务可用性。
  score: 7.0
  article_ids:
  - a50b0e08dbaee74a
  evidence_snippets:
  - aws-agents 插件涵盖使用 Amazon Bedrock 和 AgentCore 在 AWS 上构建 AI 代理的相关技能。
  - 用户可通过 /plugin install aws-agents@claude-plugins-official 命令在 Claude Code 中安装该插件。
- object_type: project
  name: aws-data-analytics
  canonical_name: aws-data-analytics
  url: null
  positioning: Agent Toolkit for AWS 中聚焦数据分析场景的插件，涵盖数据湖、分析和 ETL 工作流，深度集成 S3 Tables、AWS
    Glue 和 Athena 等核心数据分析服务。
  technical_signal: 覆盖从数据摄入、ETL 转换到交互式查询的端到端数据分析技能链，支持 S3 Tables 湖存储、Glue 无服务器 ETL
    和 Athena 联邦查询的组合使用。
  adoption_signal: 已上架 Claude Code 官方插件市场，用户可通过命令行直接安装，面向数据工程师和分析师场景。
  ecosystem_relevance: 与 AWS 数据分析产品线深度绑定，覆盖现代数据湖仓一体架构的关键组件，是 AWS 数据战略在 AI 辅助编程领域的重要布局。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 数据分析和 ETL 是企业上云后最常见的工作负载之一，AI 辅助数据分析的成熟度将直接影响数据工程师的生产效率和 AWS 数据分析产品的采用深度。
  risk_notes:
  - 数据分析场景复杂度高，AI 在 ETL 逻辑生成和数据建模等环节的准确性和可靠性仍需充分验证。
  - S3 Tables 和 Athena 等服务的查询优化能力依赖于底层数据结构的合理设计。
  score: 6.0
  article_ids:
  - a50b0e08dbaee74a
  evidence_snippets:
  - aws-data-analytics 插件涵盖数据湖、分析和 ETL 工作流，支持 S3 Tables、AWS Glue 和 Athena 等服务的集成。
  - 用户可通过 /plugin install aws-data-analytics@claude-plugins-official 命令在 Claude Code
    中安装该插件。
- object_type: project
  name: aws-agents-for-devsecops
  canonical_name: aws-agents-for-devsecops
  url: null
  positioning: Agent Toolkit for AWS 中面向安全与合规场景的专业插件，用于事件调查、代码审查、UAT 验收、漏洞扫描以及使用 AWS
    DevOps Agent 和 Security Agent 运行渗透测试。
  technical_signal: 集成 AWS DevOps Agent 和 AWS Security Agent 两大安全能力，提供自动化安全审计、漏洞扫描和渗透测试的端到端
    DevSecOps 工作流。
  adoption_signal: 已上架 Claude Code 官方插件市场，安装后需额外执行 /reload-plugins 和 setup 命令完成配置，复杂度高于其他插件。
  ecosystem_relevance: 将 AWS 的安全与合规能力引入 AI 编程助手的工作流，覆盖 DevSecOps 领域的核心场景，是企业级用户采纳的关键推动力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 安全性和合规性是企业采用 AI 编程助手的首要顾虑之一，该插件将安全管控能力内置于开发流程中，对 AWS 在企业市场的 AI 编程助手推广具有重要战略意义。
  risk_notes:
  - 安全审计和漏洞扫描场景的误报率可能较高，自动化结果需要人工复核确认。
  - 渗透测试等功能对 AWS 环境和 IAM 权限要求较高，配置复杂度和使用门槛显著高于其他插件。
  - 自动化安全工具的检测准确性依赖底层安全知识库和规则的更新频率与质量。
  score: 7.0
  article_ids:
  - a50b0e08dbaee74a
  evidence_snippets:
  - aws-agents-for-devsecops 插件用于调查事件、审查代码、执行 UAT、扫描漏洞以及使用 AWS DevOps Agent 和 AWS
    Security Agent 运行渗透测试。
  - 该插件可通过 /plugin install aws-agents-for-devsecops@claude-plugins-official 命令从官方市场安装。
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