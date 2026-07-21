---
title: PostHog/posthog
source: https://github.com/PostHog/posthog
author: []
published: ''
created: '2026-07-17'
manifest_dates:
- '2026-07-17'
- '2026-07-18'
description: '🦔 PostHog is the leading platform for building self-driving products.
  Our developer tools – AI observability, analytics, session replay, flags, experiments,
  error tracking, logs, and more – capture all the context agents need to diagnose
  problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop,
  or the MCP. Docs - Community - Roadmap - Why PostHog? - Changelog - Bug reports
  PostHog is the open source platform for building self-driving products PostHog provides
  every tool you need to build a successful product, and captures all the context
  agents need to proactively diagnose problems, uncover opportunities, and ship fixes:
  Self-driving mode: Turn signals in your product data (errors, rage clicks, failed
  queries, and more) into researched reports and pull requests you review and merge.
  Product analytics: Autocapture or manually instrument event-based analytics to understand
  user behavior and analyze data with visualization or SQL. Web analytics: Monitor
  web traffic and user sessions with a GA-like dashboard. Easily monitor conversion,
  web vitals, and revenue. Session replays: Watch real user sessions of interactions
  with your website or mobile app to diagnose issues and understand user behavior.
  Feature flags: Safely roll out features to select users or cohorts with feature
  flags. Experiments: Test changes and measure their statistical impact on goal metrics.
  Set up experiments with no-code too. Error tracking: Track errors, get alerts, and
  resolve issues to improve your product. Logs: Ingest, search, and analyze log data
  alongside the rest of your product data. Surveys: Ask anything with our collection
  of no-code survey templates, or build custom surveys with our survey builder. Data
  warehouse: Sync data from external tools like Stripe, Hubspot, your data warehouse,
  and more. Query it alongside your product data. Data pipelines: Run custom filters
  and transformations on your incoming data. Send it to 25+ tools or any webhook in
  real time or batch export large amounts to your warehouse. AI observability: Capture
  traces, generations, latency, and cost for your LLM-powered app. Workflows: Create
  workflows that automate actions or send messages to your users. You can steer it
  all from Slack, web, desktop (PostHog Code), or your own editor via the MCP. Best
  of all, all of this is free to use with a generous monthly free tier for each tool.
  Get started by signing up for PostHog Cloud US or PostHog Cloud EU. Table of Contents
  PostHog is the open source platform for building self-driving products Table of
  Contents Getting started with PostHog PostHog Cloud (Recommended) Self-hosting the
  open-source hobby deploy (Advanced) Setting up PostHog Learning more about PostHog
  Contributing Open-source vs. paid We’re hiring! Getting started with PostHog PostHog
  Cloud (Recommended) The fastest and most reliable way to get started with PostHog
  is signing up for free to&nbsp;PostHog Cloud or PostHog Cloud EU. Your first 1 million
  events, 5k recordings, 1M flag requests, 100k exceptions, and 1500 survey responses
  are free every month, after which you pay based on usage. Self-hosting the open-source
  hobby deploy (Advanced) If you want to self-host PostHog, you can deploy a hobby
  instance in one line on Linux with Docker (recommended 4GB memory): /bin/bash -c
  "$(curl -fsSL https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby)"
  Open source deployments should scale to approximately 100k events per month, after
  which we recommend migrating to a PostHog Cloud. We do not provide customer support
  or offer guarantees for open source deployments. See our self-hosting docs, troubleshooting
  guide, and disclaimer for more info. Setting up PostHog Once you''ve got a PostHog
  instance, you can set it up by installing our JavaScript web snippet, one of our
  SDKs, or by using our API. You can also connect the MCP to bring PostHog into Claude
  Code, Cursor, or any MCP-compatible agent. We have SDKs and libraries for popular
  languages and frameworks like: Frontend Mobile Backend JavaScript React Native Python
  Next.js Android Node React iOS PHP Vue Flutter Ruby Beyond this, we have docs and
  guides for Go, .NET/C#, Django, Angular, WordPress, Webflow, and more. Once you''ve
  installed PostHog, see our product docs for more information on how to set up product
  analytics, web analytics, session replays, feature flags, experiments, error tracking,
  surveys, data warehouse, and more. Learning more about PostHog Our code isn''t the
  only thing that''s open source 😳. We also open source our company handbook which
  details our strategy, ways of working, and processes. Curious about how to make
  the most of PostHog? We wrote a guide to winning with PostHog which walks you through
  the basics of measuring activation, tracking retention, and capturing revenue. Contributing
  We ❤️ contributions big and small: Vote on features or get early access to beta
  functionality in our roadmap Open a PR (see our instructions on developing PostHog
  locally) Submit a feature request or bug report For an overview of the codebase
  structure, see monorepo layout and products. Open-source vs. paid This repo is available
  under the MIT expat license, except for the ee directory (which has its license
  here) if applicable. Need absolutely 💯% FOSS? Check out our posthog-foss repository,
  which is purged of all proprietary code and features. The pricing for our paid plan
  is completely transparent and available on our pricing page. We''re hiring! Hey!
  If you''re reading this, you''ve proven yourself as a dedicated README reader. You
  might also make a great addition to our team. We''re growing fast and would love
  for you to join us.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fbfdec28cfffc04c
source_type: community_discussion
tldr: PostHog 是一个开源的全栈产品分析平台，集产品分析、会话回放、功能开关、A/B 测试、错误追踪、AI 可观测性和自助代理模式于一体，支持自托管部署和云服务，并通过
  MCP 协议将平台能力接入 Claude Code、Cursor 等 AI 编辑器。
objective_summary: PostHog 是一个开源的全栈产品分析平台，提供了产品分析、网页分析、会话回放、功能开关、A/B 测试、错误追踪、日志管理、问卷调查、数据仓库、数据管道、AI
  可观测性和自助代理模式等十余种工具。用户可选择免费注册使用 PostHog Cloud（US 或 EU 区域），或通过 Docker 一行命令自托管部署开源版本。每月免费配额包含
  100 万事件、5000 条录制、100 万功能开关请求、10 万异常和 1500 条问卷回复，超出后按使用量付费。该平台还支持通过 MCP 协议将全部功能接入
  Claude Code、Cursor 等 AI 编程工具。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - PostHog
  technologies:
  - MCP
  key_people: []
key_logic_flow:
- PostHog 是一个开源的全栈产品分析平台，集成了产品分析、网页分析、会话回放、功能开关、A/B 测试、错误追踪、日志管理、问卷调查、数据仓库、数据管道、AI
  可观测性和自助代理模式等十余种工具。
- PostHog 提供两种使用方式：免费注册使用 PostHog Cloud（US 或 EU 区域）或通过 Docker 一行命令自托管部署开源版本。
- PostHog 支持通过 MCP 协议将全部平台功能接入 Claude Code、Cursor 等 MCP 兼容的 AI 编程工具。
- 每月免费配额包括 100 万事件、5000 条录制、100 万功能开关请求、10 万异常和 1500 条问卷回复，超出后按使用量付费。
- PostHog 提供多语言 SDK，覆盖前端（JavaScript、Next.js、React、Vue）、移动端（React Native、Android、iOS、Flutter）和后端（Python、Node、PHP、Ruby）等技术栈。
- 自托管开源版每月可处理约 10 万事件，超出此规模后官方建议迁移至 PostHog Cloud。
object_mentions:
- object_type: project
  name: PostHog/posthog
  canonical_name: PostHog/posthog
  url: https://github.com/PostHog/posthog
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PostHog 是一个开源的全栈产品分析平台，集成了产品分析、网页分析、会话回放、功能开关、A/B 测试、错误追踪、日志管理、问卷调查、数据仓库、数据管道、AI
    可观测性和自助代理模式等十余种工具。
  - 该平台每月免费配额包括 100 万事件、5000 条录制、100 万功能开关请求、10 万异常和 1500 条问卷回复，超出后按使用量付费。
  article_id: fbfdec28cfffc04c
- object_type: product
  name: PostHog Cloud
  canonical_name: PostHog Cloud
  url: https://posthog.com
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - PostHog Cloud 提供 US 和 EU 两个区域的云服务，用户可免费注册使用，每月赠送 100 万事件等免费配额。
  - 自托管开源版每月可处理约 10 万事件，超出此规模后官方建议迁移至 PostHog Cloud。
  article_id: fbfdec28cfffc04c
- object_type: product
  name: PostHog Code
  canonical_name: PostHog Code
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 用户可以通过 Slack、网页、桌面端应用 PostHog Code 或通过 MCP 协议在编辑器中操作 PostHog 的全部功能。
  article_id: fbfdec28cfffc04c
- object_type: project
  name: posthog-foss
  canonical_name: posthog-foss
  url: https://github.com/PostHog/posthog-foss
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - posthog-foss 仓库是去除了所有专有代码和功能的完全开源版本，适合需要百分之百自由开源软件的开发者。
  article_id: fbfdec28cfffc04c
extract_result: success
impact_score:
  score: 5.0
  reason: PostHog 已是开发者社区中颇具影响力的开源产品分析平台，与 Mixpanel、Amplitude 等商业产品形成直接竞争。本次事件虽然是
    GitHub README 介绍而非重大新版本发布，但其 'Self-driving mode'（将产品信号自动转化为研究报告和 PR）和 MCP 协议集成代表了
    AI 时代产品分析工具的新方向——从被动观测转向主动修复。这在一定程度上改变了产品分析赛道的竞争格局，但不足以构成行业范式转移。此外，PostHog 的平台化策略（将十余种工具整合到一个平台）和慷慨的免费配额也值得关注。综合评分
    5.0 分，属于局部竞争格局层面的重要产品动态。
sentiment: neutral
developer_sentiment:
  tone: excited
  primary_focus: 通过 MCP 协议将产品分析能力接入 Claude Code、Cursor 等 AI 编程工具，实现数据驱动自主修复
hype_assessment:
  level: low
  reason: README 内容以功能列表、定价信息和入门指引为主，虽带有一定的营销包装（如 'self-driving products'），但整体实事求是，没有滥用
    '颠覆性''革命性'等夸张词汇。产品功能真实可验证，开源代码可审计。
information_entropy: high
domain_disruption:
  technical_innovation: PostHog 通过 MCP 协议将全栈产品分析能力桥接到 AI 编程工具（Claude Code、Cursor 等），使
    AI Agent 能够直接查询产品数据、分析用户行为、追踪错误并生成修复 PR。其 'Self-driving mode' 将产品信号（错误、rage clicks、失败查询等）自动转化为研究报告和代码变更，实现了从
    '人工查看仪表盘' 到 'AI 自主诊断并修复' 的工作流范式跃迁。
  business_model: 开源核心（MIT）+ 透明定价 + 慷慨免费配额（每月 100 万事件、5000 条录制等）的模式，大幅降低了团队采用产品分析工具的门槛。对
    Mixpanel、Amplitude、FullStory 等传统闭源商业产品形成显著的替代压力，尤其是在预算敏感的初创团队和开源社区中。同时，通过 MCP
    协议将平台定位从 '数据分析工具' 扩展为 'AI 开发基础设施'，拓展了商业化空间。
engineering_complexity: production_ready
compound_value:
  score: 8.5
  reason: PostHog 正在构建产品分析领域的开源标准，其长期复利效应体现在三个层面：第一，开源策略带来极强的病毒式传播和社区采纳，每月100万事件的免费配额实质上是针对开发者的渠道漏斗，企业规模扩大后自然转化为付费客户；第二，从单一产品分析扩展为覆盖会话回放、功能开关、A/B测试、错误追踪、日志、问卷、数据仓库等十余种工具的All-in-One平台，显著提高了用户的迁移成本和生命周期价值，同时压缩了细分赛道竞品的生存空间；第三，AI自驱模式（self-driving
    mode）和MCP协议集成是关键差异化——PostHog不再只是被动分析工具，而是让AI代理主动诊断问题并生成PR修复，这使其从'观测层'升级为'行动层'，在AI原生开发范式下占据了不可替代的位置。综合来看，PostHog具备了类似GitHub之于代码托管或Datadog之于可观测性的平台级复利效应，3-5年后大概率是产品分析+AI可观测性的基础设施级存在。扣分项在于开源商业化难度、云服务定价压力以及Amplitude等竞品的反击，但这些风险被其开源生态和AI差异化部分对冲。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- PostHog
- Anthropic
- Cursor
- MCP 生态
competitive_casualty:
- Amplitude
- Mixpanel
- Hotjar
- FullStory
- LaunchDarkly
market_opportunities:
- 创业团队可借鉴 PostHog 的'自驱动模式(Self-driving mode)'与 MCP 协议结合这一范式，开发面向垂直行业（如电商、SaaS、金融科技）的
  AI 辅助产品优化工具，实现从用户行为数据洞察到代码修复的端到端闭环
- 开发者工具链团队可参考 PostHog 的全栈一体化策略，将产品分析、会话回放、功能开关、A/B 测试、错误追踪和 AI 可观测性整合为单一平台，替代 Mixpanel
  + Hotjar + Sentry + LaunchDarkly 等多工具组合，大幅降低客户的集成和运维成本
- 开源商业化项目可研究 PostHog 的'慷慨免费层 + 自托管开源 + 云服务升级'三层变现模型，通过在社区建立信任和采纳基础后，自然向高可用云服务转化付费客户
risk_matrix:
  regulatory: 会话回放(Session Replay)和自动埋点(Autocapture)功能在 GDPR、CCPA 等隐私法规下存在未经充分同意的用户数据收集合规风险；自托管版本虽将数据合规责任转移给部署方，但
    PostHog 仍可能因开源版本被用于违规追踪场景而面临品牌声誉连带风险
  technological: MCP 协议仍处于生态早期阶段，长期兼容性和标准化方向不确定；自驱动 AI agent 的决策可靠性尚未被大规模验证，自动生成 PR
    和修复方案可能引入新的生产事故风险；开源版每月约 10 万事件的规模上限限制了企业级采用，迁移至云版的门槛可能造成用户流失
  competitive: Mixpanel、Amplitude、FullStory、Sentry、LaunchDarkly 等成熟竞品在各自细分领域拥有深度品牌护城河和企业客户基础；Matomo、Plausible、Umami
    等轻量级开源分析工具在隐私优先市场形成侧翼竞争；Google Analytics 4、Microsoft Clarity 等云巨头的免费嵌入式分析能力对 PostHog
    的免费策略构成生态级挤压
  ethical: 自动埋点机制可能无意中捕获用户敏感信息（如密码字段、信用卡号、聊天内容），且用户难以感知被追踪；会话回放涉及真实用户完整操作录屏，在知情同意机制设计不完善时存在重大伦理争议；AI
    agent 自主生成并提交代码修复的权力下放机制可能被滥用或产生不可预见的连锁影响
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: PostHog/posthog
  canonical_name: PostHog/posthog
  url: https://github.com/PostHog/posthog
  positioning: 开源全栈产品分析平台，集产品分析、会话回放、A/B测试、错误追踪和AI可观测性于一体，支持自托管部署和云服务，并通过MCP协议将平台能力接入AI编辑器。
  technical_signal: 通过MCP协议将PostHog全平台能力接入Claude Code、Cursor等AI编辑器，实现从数据洞察到代码修复的自动化闭环。
  adoption_signal: 每月免费配额包含100万事件和5000条录制，覆盖前后端及移动端多语言SDK，支持Docker一行命令自托管部署，降低了开发者的采用门槛。
  ecosystem_relevance: 集成产品分析、AI可观测性、日志管理、数据管道等十余种工具，构成覆盖产品开发全周期的完整数据分析生态系统。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: PostHog以开源模式整合产品分析与AI可观测性，通过MCP协议打通AI编程工具，开创了数据驱动的自主代理式产品开发范式，值得持续关注其生态发展和商业化进展。
  risk_notes:
  - 自托管开源版每月仅约10万事件处理上限，超出需迁移至云服务，大规模自部署存在可扩展性瓶颈。
  - 作为商业开源项目，需关注开源版与商业版之间功能边界的迁移和变化。
  score: 8.0
  article_ids:
  - fbfdec28cfffc04c
  evidence_snippets:
  - PostHog 是一个开源的全栈产品分析平台，集成了产品分析、网页分析、会话回放、功能开关、A/B 测试、错误追踪、日志管理、问卷调查、数据仓库、数据管道、AI
    可观测性和自助代理模式等十余种工具。
  - 该平台每月免费配额包括 100 万事件、5000 条录制、100 万功能开关请求、10 万异常和 1500 条问卷回复，超出后按使用量付费。
- object_type: product
  name: PostHog Code
  canonical_name: PostHog Code
  url: null
  positioning: PostHog的桌面端应用程序，支持通过Slack、网页或MCP协议在AI编辑器中远程操作PostHog的全部产品分析和管理功能。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - PostHog平台用户
  - 产品与数据分析师
  product_signal: 作为PostHog的桌面客户端，提供了通过MCP协议将产品分析平台与AI编辑器深度集成，在开发环境中直接操作产品数据的能力。
  market_signal: 作为PostHog平台的多端交互入口之一，通过桌面端和MCP协议丰富了用户操作和管理产品数据的使用场景。
  differentiation: 通过MCP协议将产品分析平台能力嵌入AI编辑器，实现了数据分析与代码编写的工作流无缝融合。
  watch_reason: PostHog Code通过MCP协议将产品分析能力嵌入AI开发环境，代表了数据分析工具与AI编程工具深度融合的新方向，但其独立价值有待进一步验证。
  risk_notes:
  - 产品定位较为模糊，核心功能可能被PostHog主平台或MCP协议直接覆盖。
  - 桌面端应用的独立使用场景和价值需要更多市场验证。
  score: 5.0
  article_ids:
  - fbfdec28cfffc04c
  evidence_snippets:
  - 用户可以通过 Slack、网页、桌面端应用 PostHog Code 或通过 MCP 协议在编辑器中操作 PostHog 的全部功能。
- object_type: project
  name: posthog-foss
  canonical_name: posthog-foss
  url: https://github.com/PostHog/posthog-foss
  positioning: PostHog去除了所有专有代码和功能的完全开源版本，适合需要百分之百自由开源软件合规的开发者与团队。
  technical_signal: 完全移除专有代码，仅保留MIT许可的开源核心功能，为追求完全开源合规的团队提供纯净无专有代码的替代版本。
  adoption_signal: 面向对软件自由度有严格要求的FOSS社区，作为PostHog商业化主仓库的补充选择。
  ecosystem_relevance: 补充了PostHog的开源生态层次，满足从完全开源到商业功能全覆盖的不同粒度用户需求。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: posthog-foss作为PostHog生态中的纯FOSS独立分支，展示了开源商业化项目平衡社区开源理想与商业可持续性的实践模式。
  risk_notes:
  - 功能较为有限，缺乏PostHog的核心商业功能，更新和维护活跃度可能低于主仓库。
  - 与主仓库的功能差异和同步延迟可能导致生态碎片化风险。
  score: 4.0
  article_ids:
  - fbfdec28cfffc04c
  evidence_snippets:
  - posthog-foss 仓库是去除了所有专有代码和功能的完全开源版本，适合需要百分之百自由开源软件的开发者。
---

Docs - Community - Roadmap - Why PostHog? - Changelog - Bug reports

PostHog provides every tool you need to build a successful product, and captures all the context agents need to proactively diagnose problems, uncover opportunities, and ship fixes:

- Self-driving mode: Turn signals in your product data (errors, rage clicks, failed queries, and more) into researched reports and pull requests you review and merge.
- Product analytics: Autocapture or manually instrument event-based analytics to understand user behavior and analyze data with visualization or SQL.
- Web analytics: Monitor web traffic and user sessions with a GA-like dashboard. Easily monitor conversion, web vitals, and revenue.
- Session replays: Watch real user sessions of interactions with your website or mobile app to diagnose issues and understand user behavior.
- Feature flags: Safely roll out features to select users or cohorts with feature flags.
- Experiments: Test changes and measure their statistical impact on goal metrics. Set up experiments with no-code too.
- Error tracking: Track errors, get alerts, and resolve issues to improve your product.
- Logs: Ingest, search, and analyze log data alongside the rest of your product data.
- Surveys: Ask anything with our collection of no-code survey templates, or build custom surveys with our survey builder.
- Data warehouse: Sync data from external tools like Stripe, Hubspot, your data warehouse, and more. Query it alongside your product data.
- Data pipelines: Run custom filters and transformations on your incoming data. Send it to 25+ tools or any webhook in real time or batch export large amounts to your warehouse.
- AI observability: Capture traces, generations, latency, and cost for your LLM-powered app.
- Workflows: Create workflows that automate actions or send messages to your users.

You can steer it all from Slack, web, desktop (PostHog Code), or your own editor via the MCP.

Best of all, all of this is free to use with a generous monthly free tier for each tool. Get started by signing up for PostHog Cloud US or PostHog Cloud EU.

- PostHog is the open source platform for building self-driving products
- Table of Contents
- Getting started with PostHog
- Setting up PostHog
- Learning more about PostHog
- Contributing
- Open-source vs. paid
- We’re hiring!

The fastest and most reliable way to get started with PostHog is signing up for free to PostHog Cloud or PostHog Cloud EU. Your first 1 million events, 5k recordings, 1M flag requests, 100k exceptions, and 1500 survey responses are free every month, after which you pay based on usage.

If you want to self-host PostHog, you can deploy a hobby instance in one line on Linux with Docker (recommended 4GB memory):

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby)"`

Open source deployments should scale to approximately 100k events per month, after which we recommend migrating to a PostHog Cloud.

We *do not* provide customer support or offer guarantees for open source deployments. See our self-hosting docs, troubleshooting guide, and disclaimer for more info.

Once you've got a PostHog instance, you can set it up by installing our JavaScript web snippet, one of our SDKs, or by using our API. You can also connect the MCP to bring PostHog into Claude Code, Cursor, or any MCP-compatible agent.

We have SDKs and libraries for popular languages and frameworks like:

| Frontend | Mobile | Backend |
|---|---|---|
| JavaScript | React Native | Python |
| Next.js | Android | Node |
| React | iOS | PHP |
| Vue | Flutter | Ruby |

Beyond this, we have docs and guides for Go, .NET/C#, Django, Angular, WordPress, Webflow, and more.

Once you've installed PostHog, see our product docs for more information on how to set up product analytics, web analytics, session replays, feature flags, experiments, error tracking, surveys, data warehouse, and more.

Our code isn't the only thing that's open source 😳. We also open source our company handbook which details our strategy, ways of working, and processes.

Curious about how to make the most of PostHog? We wrote a guide to winning with PostHog which walks you through the basics of measuring activation, tracking retention, and capturing revenue.

We <3 contributions big and small:

- Vote on features or get early access to beta functionality in our roadmap
- Open a PR (see our instructions on developing PostHog locally)
- Submit a feature request or bug report

For an overview of the codebase structure, see monorepo layout and products.

This repo is available under the MIT expat license, except for the `ee`

directory (which has its license here) if applicable.

Need *absolutely 💯% FOSS*? Check out our posthog-foss repository, which is purged of all proprietary code and features.

The pricing for our paid plan is completely transparent and available on our pricing page.

Hey! If you're reading this, you've proven yourself as a dedicated README reader.

You might also make a great addition to our team. We're growing fast and would love for you to join us.