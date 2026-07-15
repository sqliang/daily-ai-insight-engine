---
title: Meet your new Slack coworker — Claude
source: https://www.therundown.ai/p/meet-your-new-slack-coworker-claude
author:
- '[[Zach Mink]]'
published: '2026-06-24'
created: '2026-06-26'
description: 'PLUS: Build a Clippy-like desktop pet for Codex'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dbdce0f8b0fb62b6
source_type: newsletter_rss
tldr: Anthropic 推出 Claude Tag，将 AI 智能体引入 Slack 频道
objective_summary: Anthropic 于 2026 年 6 月 24 日发布 Claude Tag 功能，使 Claude AI 能在 Slack
  频道中被 @ 标记并像团队成员一样执行任务，支持异步协作、跨频道上下文学习和主动信息跟踪。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Slack
  technologies: []
  key_people: []
key_logic_flow:
- Anthropic 发布了 Claude Tag 功能，将此前仅限于 Claude Code 和 Cowork 的智能体能力引入 Slack 即时通讯平台。
- 团队成员只需在 Slack 频道中 @Claude 并描述任务，AI 会自动将任务拆解为多个阶段，使用已授权的工具和数据逐步处理并返回结果。
- Claude Tag 具备跨频道上下文学习能力，能够随时间推移积累工作知识，并仅在其有权限访问的频道范围内采取行动。
- Claude Tag 还拥有环境模式（ambient mode），可主动从相关频道获取信息，并在任务被搁置时主动跟进处理。
extract_result: success
impact_score:
  score: 7.0
  reason: 该产品发布将此前仅限于 Claude Code 和 Cowork 的智能体能力扩展到了 Slack 这一主流团队协作平台，实现了从'个人 AI
    工具'到'团队 AI 协作者'的能力跃迁。跨频道上下文学习和 ambient mode（主动信息获取与任务跟进）在架构上区别于传统的被动问答式 AI 集成（如
    Microsoft Copilot 在 Teams 中的辅助模式），为 AI 在协同工作流中的角色提供了新范式。在行业竞争层面，Anthropic 以此直接挑战
    Microsoft Copilot 在办公协作 AI 领域的先发优势，且定位更偏向自主智能体而非副驾驶。不过，该功能仍受限于 Slack 生态和已授权工具的边界，尚未构成技术路线的根本性变革。综合评定为重要产品发布，改变局部竞争格局，评分
    7.0。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Claude Tag 在 Slack 中跨频道上下文积累和 ambient mode 的实际执行可靠性，以及其支持的工具集成范围
hype_assessment:
  level: low
  reason: 文章对产品功能的描述较为客观准确，核心能力（任务拆解、工具调用、跨频道上下文、ambient mode）均有具体说明且可验证，没有使用'颠覆性'、'革命性'等
    PR 滥用词汇。Anthropic 官方发布也清晰界定了能力边界（仅在有权限的频道内行动）。属于实打实的产品干货。
information_entropy: medium
domain_disruption:
  technical_innovation: 将智能体的任务拆解-工具调用-多阶段执行能力嵌入即时通讯平台，并引入跨频道上下文学习（随时间积累工作知识）和 ambient
    mode（主动从相关频道获取信息并在任务搁置时跟进），在协作场景中实现了从'被动问答机器人'到'半自主协作者'的架构跃迁。
  business_model: 重塑了 SaaS 协作工具的 AI 集成范式——AI 不再以侧边栏插件或聊天机器人的形态存在，而是以'团队成员'身份直接参与频道对话。这可能推动
    Slack 及同类平台从'人-人协作'向'人-AI-人'三角协作模式演进，对 Microsoft Teams、Google Workspace 等竞品的 AI
    策略形成竞争压力，同时为企业 AI 产品的定价模式（按成员席位还是按 AI 任务量）带来新的思考。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: Claude Tag 的核心复利效应来自三个积累性壁垒：① 跨频道上下文学习——AI 随时间积累团队工作知识，使用越久价值越高，形成典型的数据飞轮（data
    flywheel），后期用户的迁移成本极高；② 网络效应——团队越多成员在 Slack 中 @Claude，其语境理解越完整，协作效率提升越明显，形成团队级别的锁定效应；③
    环境模式（ambient mode）的主动式任务跟进，将 AI 从被动工具变为主动协作者，改变了工作流范式。这些效应叠加使 Claude Tag 不是单一功能发布，而是
    Anthropic 在企业级 Agent 交付渠道上的基础设施级布局。主要风险在于：依赖 Slack 生态（与 Salesforce 的战略关系稳固性）、Microsoft
    Copilot for Teams 的渠道分发优势、以及企业客户对 AI Shadower 的安全合规接受度。总体看，3-5 年后在企业协作 Agent 赛道中，Claude
    Tag 有潜力成为不可替代的层级。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Slack (Salesforce)
- Enterprise teams leveraging Slack
competitive_casualty:
- Microsoft Copilot for Teams
- Google Gemini for Workspace
- Standalone internal chatbot/knowledge base tools
- Traditional RPA/BPA workflow tools
- Custom Slack bot builders and niche AI assistants
market_opportunities:
- 企业可基于 Claude Tag 构建部门级 AI 协作者，将重复性沟通与任务协调工作（如工单跟进、跨团队信息同步）自动化，显著降低团队协作摩擦成本
- SaaS 和咨询公司可围绕 Claude Tag 开发行业模板和最佳实践库（如法律合同审查、营销活动排期、工程故障响应），形成可复用的 AI 协作工作流产品
- Anthropic 的 ambient mode（主动信息采集与任务跟进）开辟了 AI 从被动响应转向主动服务的新范式，创业者可借鉴这一模式在飞书、钉钉、Teams
  等平台构建类似功能
risk_matrix:
  regulatory: Claude Tag 跨频道学习和环境模式可能触及企业数据合规红线，若 Claude 在未明确告知的情况下抓取频道历史或敏感商业信息，可能违反
    GDPR、CCPA 等数据保护法规；Slack 作为多国企业通用工具，跨国部署时面临数据本地化与跨境传输的双重合规挑战
  technological: 尽管 Claude Tag 具备异步协作能力，但其依赖 Slack 平台生态，若 Slack 变更 API 策略或推出竞争性 AI
    功能，Claude Tag 的深度集成将面临中断或弱化风险；此外，AI 在多频道上下文中推理的准确性和幻觉控制仍有待长期验证
  competitive: 微软已将 Copilot 深度集成到 Teams 中，且 OpenAI、Google 等竞争对手可能很快推出类似 Slack 集成方案，Claude
    Tag 的先发优势窗口有限；企业客户可能因已有微软生态投资而倾向于选择 Copilot 而非独立第三方 AI
  ethical: Ambient mode（环境模式）主动从频道获取信息的能力可能引发员工隐私担忧——AI 持续监听频道对话并自主跟进任务，易产生被监控的心理压力；同时，AI
    在团队协作中做出的决策若出现偏差（如错误标记任务状态），责任归属模糊，可能引发团队内部信任问题
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
---

Title: Meet your new Slack coworker — Claude

URL Source: https://www.therundown.ai/p/meet-your-new-slack-coworker-claude

Published Time: 2026-06-24T09:00:00.000Z

Markdown Content:
[![Image 1](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/f6a99b1e-73ea-4b69-a7d3-e1b636a6a7ec/hubspot-NEW.jpg)](https://offers.hubspot.com/using-chatgpt-at-work?utm_medium=email-media-newsletter&utm_source=the-rundown-ai&utm_campaign=creator&utm_content=paid&utm_term=6-24-2026)

**Good morning, AI enthusiasts.** Your Slack workspace has a new coworker — Claude.

Anthropic just debuted Claude Tag, which brings the agentic capabilities previously limited to Claude Code and Cowork into Slack channels, enabling entire teams to simply tag the AI to handle tasks ranging from engineering to marketing.

**In today’s AI rundown:**

*   Claude joins Slack as an agentic coworker

*   Meta doubles down on AI smart glasses

*   Build a Clippy-like desktop pet for Codex

*   Programming language for AI-driven biology

*   4 new AI tools, community workflows, and more

**LATEST DEVELOPMENTS**

###### ANTHROPIC

#### 🤖[**Claude joins Slack as an agentic coworker**](https://www.anthropic.com/news/introducing-claude-tag?utm_campaign=meet-your-new-slack-coworker-claude&utm_medium=referral&utm_source=www.therundown.ai)

![Image 2](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/18e13a55-7649-4e65-9f5b-db8a15874b9c/HLg4WfjWwAAIy2a.jpeg)
Image source: Anthropic

**The Rundown:**Anthropic just [launched](https://www.anthropic.com/news/introducing-claude-tag?utm_campaign=meet-your-new-slack-coworker-claude&utm_medium=referral&utm_source=www.therundown.ai) Claude Tag, a new way to make its AI assistant available inside Slack, letting teams tag it like a teammate to handle tasks asynchronously and build context across channels, codebases, and tools over time.

**The details:**

*   While Claude Code brought agentic capabilities to individuals, Claude Tag takes it to teams, with the AI handling tasks for members in a Slack channel.

*   You just have to tag @Claude with the task, and the AI will break it into stages, work through them using approved tools and data, and respond when done.

*   Claude learns over time, builds context about the work being done, and can even take action across different channels — but only where it has access.

*   It also uses an ambient mode, where Claude fetches information from relevant channels and follows up on tasks that have gone quiet and may need attention.