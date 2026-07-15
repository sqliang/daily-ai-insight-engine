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
tldr: Karakeep 是一款自托管书签管理应用，支持 AI 自动标签与全文搜索。
objective_summary: Karakeep（原 Hoarder）由 Localhost Labs Ltd 开发并采用 AGPL-3.0 许可，是一款自托管的收藏一切应用。支持链接、笔记、图片、PDF
  收藏，提供 LLM 自动标签与摘要、OCR 文字提取、RSS 自动抓取和多平台客户端。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Localhost Labs Ltd
  technologies:
  - LLM
  - OCR
  - Drizzle
  - tRPC
  - Puppeteer
  - Meilisearch
  - OpenAI
  - yt-dlp
  - NextAuth
  key_people: []
key_logic_flow:
- Karakeep（原 Hoarder）是一款自托管的书签管理应用，支持链接、笔记、图片和 PDF 等多种内容的收藏与管理。
- 该应用集成 LLM 驱动的自动标签与摘要功能，支持通过 ollama 使用本地模型，并提供了 OCR 图片文字提取和全文页面归档能力。
- 项目基于 NextJS App Router、Drizzle、NextAuth、tRPC、Puppeteer 和 Meilisearch 等技术栈构建，采用 AGPL-3.0
  开源许可证。
- Karakeep 提供多平台客户端支持，包括 Chrome、Firefox、Safari 浏览器扩展以及 iOS 和 Android 原生应用。
- 该项目受 memos 和 mymind 等产品启发，定位为自托管的 Pocket 替代方案，由 Localhost Labs Ltd 拥有和维护。
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