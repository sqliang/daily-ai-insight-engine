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