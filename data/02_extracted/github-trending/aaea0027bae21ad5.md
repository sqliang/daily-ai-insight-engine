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