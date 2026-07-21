---
title: karakeep-app/karakeep
source: https://github.com/karakeep-app/karakeep
author: []
published: ''
created: '2026-07-07'
description: 'A self-hostable bookmark-everything app (links, notes and images) with
  AI-based automatic tagging and full text search Karakeep (previously Hoarder) is
  a self-hostable bookmark-everything app with a touch of AI for the data hoarders
  out there. Features 🔗 Bookmark links, take simple notes and store images and pdfs.
  ⬇️ Automatic fetching for link titles, descriptions and images. 📋 Sort your bookmarks
  into lists. 👥 Collaborate with others on the same list. 🔎 Full text search of all
  the content stored. ✨ LLM-based automatic tagging and summarization. With supports
  for local models using ollama! 🤖 LLM Agents (e.g. OpenClaw, Hermes) friendly with
  powerful CLI, and official skills. ⚙️ Rule-based engine for customized management.
  🎆 OCR for extracting text from images. 🔖 Chrome plugin, Firefox addon, and Safari
  extension for quick bookmarking. 📱 An iOS app, and an Android app. 📰 Auto hoarding
  from RSS feeds. 🔌 REST API and multiple clients. 🌐 Multi-language support. 🖍️ Mark
  and store highlights from your hoarded content. 🗄️ Full page archival (using monolith)
  to protect against link rot. ▶️ Auto video archiving using yt-dlp. ☑️ Bulk actions
  support. 🔐 SSO support. 🌙 Dark mode support. 💾 Self-hosting first. ⬇️ Bookmark importers
  from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager. 🔄 Automatic sync
  with browser bookmarks via floccus. [Planned] Offline reading on mobile, semantic
  search across bookmarks, ... ⚠️ This app is under heavy development. Documentation
  Installation Configuration Screenshots Security Considerations Development Demo
  You can access the demo at https://try.karakeep.app. Login with the following creds:
  email: demo@karakeep.app password: demodemo The demo is seeded with some content,
  but it''s in read-only mode to prevent abuse. About the name The name Karakeep is
  inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used
  to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized
  but often hold personal value or hidden usefulness. It evokes the image of a messy
  drawer or forgotten box, full of stuff you can''t quite throw away—because somehow,
  it matters (or more likely, because you''re a hoarder!). Stack NextJS for the web
  app. Using app router. Drizzle for the database and its migrations. NextAuth for
  authentication. tRPC for client->server communication. Puppeteer for crawling the
  bookmarks. OpenAI because AI is so hot right now. Meilisearch for the full content
  search. Why did I build it? I browse reddit, twitter and hackernews a lot from my
  phone. I frequently find interesting stuff (articles, tools, etc) that I''d like
  to bookmark and read later when I''m in front of a laptop. Typical read-it-later
  apps usecase. Initially, I was using Pocket for that. Then I got into self-hosting
  and I wanted to self-host this usecase. I used memos for those quick notes and I
  loved it but it was lacking some features that I found important for that usecase
  such as link previews and automatic tagging (more on that in the next section).
  I''m a systems engineer in my day job (and have been for the past 7 years). I didn''t
  want to get too detached from the web development world. I decided to build this
  app as a way to keep my hand dirty with web development, and at the same time, build
  something that I care about and use every day. Alternatives memos: I love memos.
  I have it running on my home server and it''s one of my most used self-hosted apps.
  It doesn''t, however, archive or preview the links shared in it. It''s just that
  I dump a lot of links there and I''d have loved if I''d be able to figure which
  link is that by just looking at my timeline. Also, given the variety of things I
  dump there, I''d have loved if it does some sort of automatic tagging for what I
  save there. This is exactly the usecase that I''m trying to tackle with Karakeep.
  mymind: Mymind is the closest alternative to this project and from where I drew
  a lot of inspirations. It''s a commercial product though. raindrop: A polished open
  source bookmark manager that supports links, images and files. It''s not self-hostable
  though. Bookmark managers (mostly focused on bookmarking links): Pocket (Dead):
  Pocket is what hooked me into the whole idea of read-it-later apps. I used it a
  lot. However, I recently got into home-labbing and became obsessed with the idea
  of running my services in my home server. Karakeep is meant to be a self-hosting
  first app. Mozilla recently announced that it''s shutting down pocket. Linkwarden:
  An open-source self-hostable bookmark manager that I ran for a bit in my homelab.
  It''s focused mostly on links and supports collaborative collections. Wallabag:
  Wallabag is a well-established open source read-it-later app written in php. Shiori:
  Shiori is meant to be an open source pocket clone written in Go. Translations Karakeep
  uses Weblate for managing translations. If you want to help translate Karakeep,
  you can do so here. Karakeep Cloud ☁️ If you''re not comfortable with self-hosting,
  you can use our managed Karakeep cloud at cloud.karakeep.app. Cloud subscriptions
  support the development of Karakeep. Support If you''re enjoying using Karakeep,
  drop a ⭐️ on the repo! Community Channels Join us on Discord. Follow us on Twitter:
  @karakeep_app. License Karakeep is licensed under AGPL-3.0 and owned by Localhost
  Labs Ltd. Star History'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aaea0027bae21ad5
manifest_dates:
- '2026-07-07'
source_type: community_discussion
tldr: Karakeep（原 Hoarder）是一款基于 AGPL-3.0 开源的自托管收藏管理应用，支持链接书签、笔记、图片和 PDF 存储，集成 LLM 自动标签与摘要功能，并提供多平台客户端和浏览器插件。
objective_summary: Localhost Labs Ltd 开发的 Karakeep（原 Hoarder）是一款自托管优先的"收藏一切"应用，于 2026
  年 7 月在 GitHub 上公开维护。它支持书签链接、笔记、图片和 PDF 存储，利用 LLM（含 ollama 本地模型）实现自动标签与摘要，提供 Chrome、Firefox、Safari
  浏览器插件及 iOS、Android 移动端。项目使用 NextJS、Drizzle、tRPC、Puppeteer、Meilisearch 等技术栈构建，并提供了托管云服务
  cloud.karakeep.app 供不愿自托管的用户使用。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Localhost Labs Ltd
  technologies:
  - NextJS
  - Drizzle
  - NextAuth
  - tRPC
  - Puppeteer
  - OpenAI
  - Meilisearch
  - OCR
  - LLM
  - REST API
  - SSO
  - RSS
  - yt-dlp
  - ollama
  - AGPL-3.0
  key_people: []
key_logic_flow:
- Karakeep 是一款自托管优先的"收藏一切"应用，支持链接书签、笔记、图片和 PDF 存储。
- 它利用 LLM 实现自动标签和摘要，并支持通过 ollama 使用本地模型运行。
- 该项目提供 Chrome、Firefox、Safari 浏览器插件以及 iOS 和 Android 移动端应用。
- Karakeep 支持 RSS 自动收藏、全文搜索、OCR 图片文字提取、全页面归档和视频自动归档功能。
- 项目使用 NextJS、Drizzle、NextAuth、tRPC、Puppeteer 和 Meilisearch 等技术栈构建。
- Karakeep 由 Localhost Labs Ltd 所有并采用 AGPL-3.0 开源协议，同时提供托管云服务 cloud.karakeep.app。
specialized_tags:
  github:
    projectName: karakeep-app/karakeep
    projectUrl: https://github.com/karakeep-app/karakeep
    primaryLanguage: TypeScript
    licenseType: AGPL-3.0
    domain: other
    crossTags:
    - self-hosted
    - open-source
    - read-it-later
extract_result: success
object_mentions:
- object_type: project
  name: karakeep-app/karakeep
  canonical_name: karakeep-app/karakeep
  url: https://github.com/karakeep-app/karakeep
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Karakeep（原 Hoarder）是一款自托管优先的"收藏一切"应用，支持链接书签、笔记、图片和 PDF 存储。
  - 该项目利用 LLM 实现自动标签和摘要，并支持通过 ollama 使用本地模型。
  - Karakeep 由 Localhost Labs Ltd 所有，采用 AGPL-3.0 开源协议发布。
  article_id: aaea0027bae21ad5
- object_type: product
  name: Karakeep Cloud
  canonical_name: Karakeep Cloud
  url: https://cloud.karakeep.app
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 如果用户不习惯自托管，可以使用 Karakeep 托管云服务 cloud.karakeep.app。
  - 云订阅收入用于支持 Karakeep 的持续开发。
  article_id: aaea0027bae21ad5
- object_type: product
  name: Chrome plugin
  canonical_name: Karakeep Chrome Extension
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 提供 Chrome 浏览器插件用于快速书签收藏。
  article_id: aaea0027bae21ad5
- object_type: product
  name: Firefox addon
  canonical_name: Karakeep Firefox Addon
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 提供 Firefox 浏览器插件用于快速书签收藏。
  article_id: aaea0027bae21ad5
- object_type: product
  name: Safari extension
  canonical_name: Karakeep Safari Extension
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 提供 Safari 浏览器插件用于快速书签收藏。
  article_id: aaea0027bae21ad5
- object_type: product
  name: iOS app
  canonical_name: Karakeep iOS App
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 提供了 iOS 移动端应用。
  article_id: aaea0027bae21ad5
- object_type: product
  name: Android app
  canonical_name: Karakeep Android App
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 提供了 Android 移动端应用。
  article_id: aaea0027bae21ad5
- object_type: project
  name: memos
  canonical_name: usememos/memos
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者表示他喜欢 memos 并在家庭服务器上运行，但 memos 不支持链接归档或预览。
  - 作者从 memos 的使用体验中获得了构建 Karakeep 的灵感。
  article_id: aaea0027bae21ad5
- object_type: product
  name: Pocket
  canonical_name: Pocket
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Pocket 是让作者接触阅读后存应用理念的产品，但 Mozilla 最近宣布关闭 Pocket。
  - 作者最初使用 Pocket 来收藏和稍后阅读感兴趣的内容。
  article_id: aaea0027bae21ad5
- object_type: project
  name: Linkwarden
  canonical_name: linkwarden/linkwarden
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Linkwarden 是一款开源可自托管的书签管理器，作者曾在家庭实验室中运行过。
  - 它主要关注链接管理并支持协作收藏。
  article_id: aaea0027bae21ad5
- object_type: project
  name: ollama
  canonical_name: ollama/ollama
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 支持通过 ollama 使用本地模型进行 LLM 自动标签和摘要。
  article_id: aaea0027bae21ad5
- object_type: project
  name: floccus
  canonical_name: floccusaddon/floccus
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 支持通过 floccus 与浏览器书签自动同步。
  article_id: aaea0027bae21ad5
- object_type: project
  name: Weblate
  canonical_name: Weblate
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 使用 Weblate 管理多语言翻译，社区可通过 Weblate 参与翻译工作。
  article_id: aaea0027bae21ad5
- object_type: project
  name: monolith
  canonical_name: Y2Z/monolith
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 使用 monolith 进行全页面归档以防范链接失效。
  article_id: aaea0027bae21ad5
- object_type: project
  name: yt-dlp
  canonical_name: yt-dlp/yt-dlp
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - Karakeep 使用 yt-dlp 实现视频自动归档。
  article_id: aaea0027bae21ad5
impact_score:
  score: 2.5
  reason: Karakeep 是一款成熟的自托管书签管理应用，AI 自动标签和 OCR 功能在同类开源项目中较为突出，但整体属于功能性迭代而非行业级突破。项目已在
    GitHub 上积累了一定社区关注度，对自托管生态有局部影响，但对 AI 行业整体格局无实质性冲击。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 自托管优先 + 本地 LLM（ollama）自动标签，替代 Pocket 的隐私友好方案
hype_assessment:
  level: low
  reason: 项目介绍务实，功能清单具体可验证，未使用'颠覆'、'革命性'等 PR 话术。项目定位清晰——自托管的 Pocket 替代品，功能边界诚实。
information_entropy: medium
domain_disruption:
  technical_innovation: 将本地 LLM（ollama）集成到自托管书签管理流程中实现自动标签与摘要，结合 OCR 图片文字提取和 Meilisearch
    全文搜索，为个人知识管理场景提供了端到端的 AI 增强方案。技术架构上采用 NextJS App Router + tRPC + Drizzle 的全栈模式，工程选型现代但无本质突破。
  business_model: AGPL-3.0 开源许可 + 托管云服务（cloud.karakeep.app）的双轨商业模式，延续了开源项目常见的开放核心模式。对
    SaaS 生态的重塑力有限，但为自托管社区提供了一个可运营的参考模型。
engineering_complexity: production_ready
compound_value:
  score: 3.5
  reason: Karakeep 是一款实用但投资价值有限的自我托管书签管理工具。核心逻辑：1) 市场天花板低——书签管理（read-it-later）赛道规模有限，且存在
    Pocket（已关闭）、Raindrop.io、Wallabag 等大量同类竞品，差异化不足；2) AGPL-3.0 许可叠加自托管优先定位，天然限制商业化空间，可寻址市场远小于
    SaaS 类产品；3) 缺少网络效应与数据网络效应——用户数据存于各自服务器，无法形成跨用户的飞轮增长；4) 技术壁垒浅——AI 标签和摘要已成为行业标配，基于
    ollama 本地模型虽是加分项但非独占优势，易被复制；5) 创始人动机为个人工具+保持 Web 开发手感，非 VC 级创业意图，缺乏规模化扩张的激励。综上，该工具对个人用户有实用价值，但作为投资标的缺乏长期复合回报潜力，评分
    3.5。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- ollama
- Meilisearch
- Localhost Labs Ltd
competitive_casualty:
- Raindrop.io
- Pocket
- 商业书签管理 SaaS
market_opportunities:
- 自托管 AI 工具需求持续攀升，企业可基于 Karakeep 搭建内部知识管理系统，利用本地 LLM（ollama）实现敏感数据的自动分类与全文检索，降低数据外泄风险
- Mozilla 宣布关闭 Pocket 后市场出现真空期，创业者可参考 Karakeep 模式推出面向隐私敏感用户的商业化托管服务（如 cloud.karakeep.app），通过订阅制变现
- Karakeep 的 LLM Agent 友好 CLI 和 REST API 为自动化工作流提供了实用工具接入点，开发者可将其集成到 AI Agent 中实现网页内容的自动归档与知识化沉淀
risk_matrix:
  regulatory: AGPL-3.0 许可证要求衍生作品必须开源，商业 SaaS 部署需谨慎处理合规边界；OCR 与全文归档功能可能涉及版权内容的复制与存储，在部分司法管辖区存在侵权风险
  technological: 技术栈重度依赖多个第三方服务（Meilisearch、Puppeteer、yt-dlp、OpenAI/ollama），任一上游变更、API
    价格调整或弃用都可能影响整体功能稳定性
  competitive: 书签管理赛道参与者众多（Linkwarden、Wallabag、Shiori、Raindrop 等成熟项目），且 Notion、Obsidian
    等知识管理平台也在内嵌类似收藏能力，生态挤压风险显著
  ethical: AI 自动标签可能继承底层模型的偏见；全文归档与视频存档功能可能被用于未经授权的内容复制和传播，引发数据伦理争议
  additional:
  - 项目曾更名（Hoarder → Karakeep），品牌稳定性存在不确定性；项目发展高度依赖 Localhost Labs Ltd 的持续维护投入
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: karakeep-app/karakeep
  canonical_name: karakeep-app/karakeep
  url: https://github.com/karakeep-app/karakeep
  positioning: 自托管优先的"收藏一切"应用，支持链接、笔记、图片和 PDF 存储，集成 LLM 自动标签与摘要，并提供多平台客户端与浏览器插件。
  technical_signal: 基于 NextJS、Drizzle、tRPC、Puppeteer 和 Meilisearch 等技术栈构建，支持 LLM 自动标签摘要、OCR
    图片文字提取、全文搜索和全页面归档功能。
  adoption_signal: 项目在 GitHub 公开维护并获社区星标，提供托管云服务 cloud.karakeep.app，已建立 Discord 社区和
    Twitter 官方账号，覆盖 iOS 和 Android 用户。
  ecosystem_relevance: 填补 Pocket 关停后的自托管收藏管理空白，支持从 Chrome、Pocket、Linkwarden、Omnivore
    等平台导入数据，兼容 floccus 书签同步。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Karakeep 结合 LLM 能力的自托管收藏管理定位，在 Pocket 关停释放市场需求和自托管生态壮大的背景下，有望成为该领域的关键基础设施，值得持续跟踪其用户增长和功能演进方向。
  risk_notes:
  - 与 mymind、Raindrop 等商业产品及 Linkwarden 等开源项目竞争，需持续建立差异化优势。
  - 自托管模式对非技术用户的门槛较高，可能限制其用户规模的天花板。
  score: 7.0
  article_ids:
  - aaea0027bae21ad5
  evidence_snippets:
  - Karakeep（原 Hoarder）是一款自托管优先的"收藏一切"应用，支持链接书签、笔记、图片和 PDF 存储。该项目利用 LLM 实现自动标签和摘要，并支持通过
    ollama 使用本地模型。
  - Karakeep 由 Localhost Labs Ltd 所有，采用 AGPL-3.0 开源协议发布。项目提供 Chrome、Firefox、Safari
    浏览器插件以及 iOS 和 Android 移动端应用，并支持 RSS 自动收藏和全页面归档功能。
- object_type: project
  name: memos
  canonical_name: usememos/memos
  url: null
  positioning: 轻量级自托管笔记应用，支持快速记录和时间线展示，适合家庭服务器部署的个人笔记与信息快存需求。
  technical_signal: 提供简洁的笔记和时间线管理功能，但不支持链接归档、预览和自动标签分类，功能定位偏向轻量记录而非收藏管理。
  adoption_signal: 作者将其列为家庭服务器上最常用的自托管应用之一，在自托管社区中拥有较高的采用度和用户口碑。
  ecosystem_relevance: 作为 Karakeep 的直接灵感来源，其缺少链接归档和自动标签的功能缺口直接推动了收藏管理工具的细分发展。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: memos 作为自托管笔记领域的代表性项目，其缺少链接归档和自动标签的功能边界直接催生了 Karakeep 等更垂直的收藏管理工具，值得持续关注两者的生态协同演进方向。
  risk_notes:
  - 在链接密集型使用场景中功能受限，可能被 Karakeep 等更具垂直能力的工具分流用户。
  score: 3.0
  article_ids:
  - aaea0027bae21ad5
  evidence_snippets:
  - 作者表示他喜欢 memos 并在家庭服务器上运行，但 memos 不支持链接归档或预览。
  - 作者从 memos 的使用体验中获得了构建 Karakeep 的灵感，希望在笔记场景中实现链接预览和自动标签功能。
- object_type: product
  name: Pocket
  canonical_name: Pocket
  url: null
  positioning: 经典的"稍后阅读"应用，帮助用户保存网页内容供后续阅读，是该产品品类的开创者和普及者。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 内容收藏用户
  - 稍后阅读需求用户
  - 网页书签管理用户
  product_signal: Mozilla 宣布关停 Pocket，该经典"稍后阅读"产品即将停止服务，标志着该集中式服务进入生命周期终点。
  market_signal: Pocket 的关停释放了大量用户迁移需求，为自托管和开源的收藏管理工具创造了显著的市场窗口。
  differentiation: 作为最早普及"稍后阅读"理念的产品，Pocket 以简洁体验著称，但其关停凸显了集中式服务在用户信任和可持续性上的局限。
  watch_reason: Pocket 被 Mozilla 关停释放了大量用户的迁移需求，为自托管和开源替代品创造了历史性增长窗口，值得持续追踪用户流向和收藏管理新品类形成路径。
  risk_notes:
  - 关停过程中的用户数据导出体验将直接影响替代品的获客效率和用户信任重建。
  score: 5.0
  article_ids:
  - aaea0027bae21ad5
  evidence_snippets:
  - Pocket 是让作者接触阅读后存应用理念的产品，但 Mozilla 最近宣布关闭 Pocket。作者最初使用 Pocket 来收藏和稍后阅读感兴趣的内容。
  - 作者最初使用 Pocket 来收藏和稍后阅读感兴趣的内容，但随后转向了自托管的替代方案，体现了从集中式服务向自托管迁移的趋势。
- object_type: project
  name: Linkwarden
  canonical_name: linkwarden/linkwarden
  url: null
  positioning: 开源可自托管的书签管理器，专注于链接管理和协作收藏，是自托管书签管理领域的代表性项目。
  technical_signal: 主要关注链接管理并支持协作收藏，采用开源可自托管架构，但功能范围聚焦于链接而非多类型内容存储与管理。
  adoption_signal: 作者曾在家庭实验室中运行过该项目，说明其在自托管社区中已有一定认知度和采用基础。
  ecosystem_relevance: 作为开源书签管理领域与 Karakeep 直接竞争的项目，两者功能定位的差异反映了自托管收藏管理生态的细分方向。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Linkwarden 作为开源自托管书签管理的既有项目，与 Karakeep 的竞争关系使其成为评估收藏管理生态演进的重要参照，值得持续关注其功能迭代和社区增长。
  risk_notes:
  - 功能范围较窄（主要关注链接管理），可能在 Karakeep 等多类型内容管理工具的竞争下流失用户。
  score: 3.0
  article_ids:
  - aaea0027bae21ad5
  evidence_snippets:
  - Linkwarden 是一款开源可自托管的书签管理器，作者曾在家庭实验室中运行过。
  - 它主要关注链接管理并支持协作收藏，但功能范围聚焦于链接，在归档和自动标签方面不及 Karakeep 全面。
---

Karakeep (previously Hoarder) is a self-hostable bookmark-everything app with a touch of AI for the data hoarders out there.

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 👥 Collaborate with others on the same list.
- 🔎 Full text search of all the content stored.
- ✨ LLM-based automatic tagging and summarization. With supports for local models using ollama!
- 🤖 LLM Agents (e.g. OpenClaw, Hermes) friendly with powerful CLI, and official skills.
- ⚙️ Rule-based engine for customized management.
- 🎆 OCR for extracting text from images.
- 🔖 Chrome plugin, Firefox addon, and Safari extension for quick bookmarking.
- 📱 An iOS app, and an Android app.
- 📰 Auto hoarding from RSS feeds.
- 🔌 REST API and multiple clients.
- 🌐 Multi-language support.
- 🖍️ Mark and store highlights from your hoarded content.
- 🗄️ Full page archival (using monolith) to protect against link rot.
▶️ Auto video archiving using yt-dlp.- ☑️ Bulk actions support.
- 🔐 SSO support.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
- 🔄 Automatic sync with browser bookmarks via floccus.
- [Planned] Offline reading on mobile, semantic search across bookmarks, ...

You can access the demo at https://try.karakeep.app. Login with the following creds:

```
email: demo@karakeep.app
password: demodemo
```


The demo is seeded with some content, but it's in read-only mode to prevent abuse.

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).

- NextJS for the web app. Using app router.
- Drizzle for the database and its migrations.
- NextAuth for authentication.
- tRPC for client->server communication.
- Puppeteer for crawling the bookmarks.
- OpenAI because AI is so hot right now.
- Meilisearch for the full content search.

I browse reddit, twitter and hackernews a lot from my phone. I frequently find interesting stuff (articles, tools, etc) that I'd like to bookmark and read later when I'm in front of a laptop. Typical read-it-later apps usecase. Initially, I was using Pocket for that. Then I got into self-hosting and I wanted to self-host this usecase. I used memos for those quick notes and I loved it but it was lacking some features that I found important for that usecase such as link previews and automatic tagging (more on that in the next section).

I'm a systems engineer in my day job (and have been for the past 7 years). I didn't want to get too detached from the web development world. I decided to build this app as a way to keep my hand dirty with web development, and at the same time, build something that I care about and use every day.

- memos: I love memos. I have it running on my home server and it's one of my most used self-hosted apps. It doesn't, however, archive or preview the links shared in it. It's just that I dump a lot of links there and I'd have loved if I'd be able to figure which link is that by just looking at my timeline. Also, given the variety of things I dump there, I'd have loved if it does some sort of automatic tagging for what I save there. This is exactly the usecase that I'm trying to tackle with Karakeep.
- mymind: Mymind is the closest alternative to this project and from where I drew a lot of inspirations. It's a commercial product though.
- raindrop: A polished open source bookmark manager that supports links, images and files. It's not self-hostable though.
- Bookmark managers (mostly focused on bookmarking links):
- Pocket (Dead): Pocket is what hooked me into the whole idea of read-it-later apps. I used it a lot. However, I recently got into home-labbing and became obsessed with the idea of running my services in my home server. Karakeep is meant to be a self-hosting first app. Mozilla recently announced that it's shutting down pocket.
- Linkwarden: An open-source self-hostable bookmark manager that I ran for a bit in my homelab. It's focused mostly on links and supports collaborative collections.
- Wallabag: Wallabag is a well-established open source read-it-later app written in php.
- Shiori: Shiori is meant to be an open source pocket clone written in Go.


Karakeep uses Weblate for managing translations. If you want to help translate Karakeep, you can do so here.

If you're not comfortable with self-hosting, you can use our managed Karakeep cloud at cloud.karakeep.app. Cloud subscriptions support the development of Karakeep.

If you're enjoying using Karakeep, drop a ⭐️ on the repo!

- Join us on Discord.
- Follow us on Twitter: @karakeep_app.

Karakeep is licensed under AGPL-3.0 and owned by Localhost Labs Ltd.