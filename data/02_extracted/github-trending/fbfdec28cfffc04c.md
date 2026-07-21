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