---
title: Notion Mail shuts down amid agent takeover
source: https://techcrunch.com/2026/06/25/notion-mail-shuts-down-amid-agent-takeover/
author:
- '[[Ivan Mehta]]'
published: '2026-06-25'
created: '2026-06-26'
description: The company said it is discontinuing its email inbox in favor of its
  AI agent offering as users are increasingly handing over the reins of their email
  to the agents.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5fa761beca9ae2d5
source_type: news_media
tldr: Notion 将于 2026 年 9 月 22 日关闭邮件产品 Notion Mail，全面转向 AI Agent 方案。
objective_summary: Notion 宣布关闭其邮件产品 Notion Mail，最终运营截止日期为 2026 年 9 月 22 日。该公司称超半数用户已通过
  AI Agent 管理邮件而不再打开收件箱，因此将全面转向 AI Agent。Notion Mail 于 2024 年预览发布，2025 年 4 月正式开放，
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Notion
  - Gmail
  - Skiff
  - Superhuman
  - Fyxer
  - AgentMail
  technologies:
  - AI Agent
  - Notion AI
  key_people: []
key_logic_flow:
- Notion 宣布将于 2026 年 9 月 22 日关闭其邮件产品 Notion Mail。
- Notion 表示超过半数 Notion Mail 用户通过 AI Agent 管理邮件而从不打开收件箱，这是关停的主要原因。
- Notion 将全面转向以 AI Agent 接管收件箱的策略，现有的邮件相关 Agent 功能在 Notion Mail 关闭后继续运行。
- Notion Mail 与 Gmail 关联，用户 Gmail 邮件不受影响，但需自行导出草稿和定时邮件。
- Notion Mail 源于 2024 年对安全生产力初创公司 Skiff 的收购，2025 年 4 月正式开放，曾与 Superhuman、Fyxer 竞争。
- 新兴创业公司如 AgentMail 正沿着类似思路构建专为 AI Agent 设计的邮件服务。
extract_result: success
impact_score:
  score: 6.5
  reason: Notion 关停邮件产品转向 AI Agent 是一个重要的行业信号。这验证了'AI Agent 替代传统 UI'的叙事——超半数用户不再打开收件箱，转而由
    Agent 代为管理邮件。对 Superhuman、Fyxer 等邮件 SaaS 竞品构成竞争格局冲击，也加速了'Agent 原生'产品形态的讨论。但事件本身仍是单一公司的产品方向调整，未达范式转移级别；且
    Notion Mail 从正式上线到关停仅一年多，产品本身尚未形成大规模用户基础，行业影响有限。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 产品上线仅一年即被关停，开发者对 Notion 平台产品承诺的长期稳定性产生质疑
hype_assessment:
  level: medium
  reason: 文章引用的'超半数用户不打开收件箱'数据来自 Notion 官方 PR 声明，缺乏独立第三方验证，存在自我服务倾向。'全面转向 Agent'的表述有将产品关停包装为主动战略转型的成分。但
    Notion 邮件 Agent 功能确实将继续运行，且 AgentMail 等创业公司也在验证类似方向，说明该方向有实质进展，非纯概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 无本质技术突破——邮件自动分类、过滤、调度等功能并非 Notion 首创，已有 Superhuman、Fyxer 等产品实现。核心变化在产品策略层面而非技术架构。
  business_model: 从 UI 驱动的传统邮件 SaaS 向 Agent 驱动的服务模式转型，验证了 Agent-as-Interface 的商业可行性。这将对传统
    SaaS 的定价模式（按席位 vs 按任务）、用户交互范式（点按操作 vs 委托授权）产生深远影响。新兴创业公司 AgentMail 正在构建 Agent
    原生的邮件基础设施，进一步印证了这一商业模式趋势。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 该事件验证了'AI Agent 接管收件箱'这一范式转型的真实市场需求——超过半数 Notion Mail 用户通过 Agent 管理邮件而不打开收件箱，这一用户行为数据具有强信号意义。虽然
    Notion Mail 本身用户规模有限（2025年4月才正式开放，生命周期仅17个月），但其关停决定标志着传统邮件客户端模式在 AI Agent 时代面临根本性挑战。此举将加速资本和人才向
    Agent-native 通信基础设施方向流动，长期复利效应体现在：(1) 用户管理通信的习惯从'操作界面'转向'委托代理'，习惯一旦形成粘性极强；(2)
    Agent 处理邮件积累的用户偏好数据将成为个性化模型的护城河；(3) 对 Gmail/Outlook API 的依赖反而强化了云平台层的基础设施地位。但风险在于：该范式迁移仍处于早期验证阶段，主流企业用户对
    Agent 管理邮件的信任度和合规性尚未经过大规模检验，因此评分适度偏高而非满分。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- AgentMail
- Notion AI
- Fyxer
- Anthropic
- OpenAI
competitive_casualty:
- Superhuman
- Spark Mail
- 传统邮件客户端厂商
market_opportunities:
- 创业者可聚焦构建面向 AI Agent 的原生邮件协议与服务层，替代传统收件箱 UI，AgentMail 等先行者已验证需求存在
- 企业协作平台可效仿 Notion 策略，将邮件处理深度嵌入 AI Agent 工作流，打造'无需打开收件箱'的自动化办公体验
- 传统邮件客户端（如 Superhuman）应立即规划 AI Agent 优先的交互模式，否则面临被新一代 Agent 原生服务替代的生存危机
risk_matrix:
  regulatory: AI Agent 全权管理邮件涉及 GDPR/CCPA 等数据隐私法规合规问题，用户邮件内容被 Agent 处理需明确的同意机制和数据留存策略
  technological: 纯 Agent 方案处理邮件的准确率、上下文理解能力和误操作风险仍存不确定性，关键邮件被 Agent 误判或遗漏的风险尚未充分解决
  competitive: Google/微软等平台巨头可能将 AI Agent 邮件能力深度整合进 Gmail/Outlook，挤压独立创业公司的生存空间；Superhuman
    等老牌玩家被迫转型面临技术债务
  ethical: AI Agent 代管收件箱引发用户对个人数据的控制权丧失担忧，自动决策（如自动回复、删除邮件）可能造成社交或商业关系损害，需建立人类审核兜底机制
  additional:
  - Notion 收购 Skiff 后不足两年即关停产品，反映收购整合与产品战略反复的风险，同类并购后产品存活概率值得警惕
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
---

Productivity company Notion is shutting down its email product, Notion Mail, on September 22. The company said it is discontinuing its email inbox in favor of its AI agent offering. It noted that users were increasingly handing over the reins of their email to the agents, and not opening their inbox at all.

“As Notion agents have gotten more capable, we’ve seen more users hand off email workflows to them. Today, more than half of Notion Mail users manage emails without ever opening their inbox. So, we’re going all in on using agents to run your inbox,” the company said in a post on X.

Notion Mail is connected with Gmail, meaning all emails in the inbox will stay intact. However, users will need to export drafts and scheduled emails if they want to keep them. The company said that users can export snippets and auto-label instructions and use them elsewhere and emphasized that Notion’s email-based agents will keep working post-Notion Mail shutdown.

Notion announced its email product in preview mode in 2024 after it acquired security-centric productivity startup Skiff. The company aimed to integrate email with Notion AI with features like auto-labeling, filtering, and handling scheduling for users. The company made the product available to users in April 2025 to better compete with the likes of Superhuman and Fyxer. Newer startups like AgentMail are in step with Notion’s thesis and are trying to build an email service specifically for agents.