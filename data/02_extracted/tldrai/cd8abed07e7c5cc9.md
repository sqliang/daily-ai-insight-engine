---
title: Cursor prepares to launch Origin platform for code reviews (2 minute read)
source: https://www.testingcatalog.com/cursor-prepares-to-launch-origin-platform-for-code-reviews/?utm_source=tldrai
author: []
published: ''
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cd8abed07e7c5cc9
source_type: news_media
tldr: Cursor 准备将代码审查平台 Origin 从封闭合作伙伴测试扩展为公开上线，该平台由 Graphite 团队打造，主打人类与 AI 智能体协同处理
  GitHub 拉取请求。
objective_summary: Cursor 正将其内部代号为“Cursor Review”的 Origin 平台从数周的封闭合作伙伴测试推向更广泛发布，预计最快本周上线。平台包含“Codebase”（同步管理
  GitHub 仓库）和“Review”（自动化 PR 流水线，在需要人工判断时通知开发者）两个标签页，旨在让开发者和 AI 智能体共同处理跨代码库的开放 PR。Origin
  由 Cursor 在 2025 年底收购的 Graphite 团队开发，并在 Compile 大会上首次亮相。同时，SpaceXAI 最近推出 Grok Bot
  测试版，该平台可与 Origin 对接并直接拉取仓库；SpaceX 对 Anysphere 的 600 亿美元收购预计本季度完成。
event_type: application_landing
epistemic_status: rumor_leak
entities:
  companies:
  - Cursor
  - Anysphere
  - SpaceX
  - SpaceXAI
  - GitHub
  - Graphite
  technologies:
  - Origin
  - Cursor Review
  - Grok Bot
  - Grok 4.6
  key_people: []
key_logic_flow:
- Cursor 准备将 Origin 平台从封闭合作伙伴测试扩展为更广泛的上线，网络界面字符串显示其内部名为“Cursor Review”。
- 平台包含两个标签页：Codebase 用于同步和管理从 GitHub 拉取的仓库，Review 用于构建自动化 PR 流水线。
- Review 标签页会在需要人类判断时通知开发者，使人类与智能体能够协同处理跨代码库的开放 PR。
- Origin 在 Cursor Compile 大会上发布，由 Cursor 于 2025 年底收购的 Graphite 团队开发。
- SpaceXAI 最近推出 Grok Bot 测试版，该产品将能从 Origin 直接拉取仓库并执行操作。
- SpaceX 对 Anysphere 的 600 亿美元收购预计本季度完成，Grok 4.6 曾短暂出现在 Cursor 模型列表中，显示双方路线图正在融合。
object_mentions:
- object_type: product
  name: Origin
  canonical_name: Cursor Origin
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cursor 正准备将 Origin 平台从已运行数周的封闭合作伙伴测试扩展到更广泛发布。
  - 网络界面中的字符串显示该平台将以内部名称“Cursor Review”推出，开启访问后会出现 Codebase 和 Review 两个标签页。
  - Origin 在 Cursor 的 Compile 大会上首次亮相，由 Cursor 于 2025 年底收购的 Graphite 团队构建。
  article_id: cd8abed07e7c5cc9
- object_type: product
  name: Grok Bot
  canonical_name: SpaceXAI Grok Bot
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - SpaceXAI 最近将 Grok Bot 推入测试阶段，这是一款桌面和移动应用，可为智能体提供共享云计算机以登录工具并无监督地完成任务。
  - Grok Bot 本身带有 Origin 相关引用，一旦平台上线，预计将直接从 Origin 拉取仓库并对其执行操作。
  article_id: cd8abed07e7c5cc9
- object_type: product
  name: Cursor Review
  canonical_name: Cursor Origin Review
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 网络界面中的字符串显示该平台将以内部名称“Cursor Review”推出，开启访问后会出现 Codebase 和 Review 两个标签页。
  - Review 部分更为重要：它是一个自动化的拉取请求流水线，当需要开发者判断时会通知开发者。
  article_id: cd8abed07e7c5cc9
extract_result: success
---

Cursor is preparing to open Origin beyond the closed partner beta it has been running for weeks. Strings across the Cursor web interface point to the platform shipping under the internal name "Cursor Review", with two tabs appearing once access is switched on. Codebase covers syncing and managing repositories pulled in from GitHub. Review is the more consequential half: an automated pull request pipeline that notifies developers when their judgment is needed, so humans and agents can work through open PRs across a codebase together. Signals suggest a rollout could land as early as this week, ahead of the fall window Cursor named when it announced the platform in June.

Origin was unveiled at Cursor's Compile conference and built by the Graphite team the company acquired in late 2025. The pitch is that GitHub was designed around human-paced review, one reviewer, one diff, sequential merges, while Cursor demoed 22.6 commits per second into a single repository. Teams running fleets of background agents are the obvious beneficiaries, because review rather than generation is where agentic workflows now stall. The tab structure suggests Cursor wants to land the review layer first and migrate hosting later, the lower-friction path for teams unwilling to move source control off GitHub outright.

That timing sits inside a larger consolidation. SpaceXAI recently shipped Grok Bot into beta, a desktop and mobile app that gives agents a shared cloud machine they can use to sign in to tools and finish work unattended. It carries its own Origin references, and once the platform is live, Grok Bot looks set to pull repositories directly from it and act on them. With SpaceX's $60 billion acquisition of Anysphere expected to close this quarter, and Grok 4.6 having briefly surfaced in Cursor's model list as "Cursor Grok 4.6 " before being withdrawn, the two roadmaps are folding into one.