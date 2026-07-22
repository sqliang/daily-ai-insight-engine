---
title: koala73/worldmonitor
source: https://github.com/koala73/worldmonitor
author: []
published: ''
created: '2026-06-20'
description: 'Real-time global intelligence dashboard. AI-powered news aggregation,
  geopolitical monitoring, and infrastructure tracking in a unified situational awareness
  interfaceWorld Monitor Real-time global intelligence dashboard — AI-powered news
  aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational
  awareness interface. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Documentation
  &nbsp;·&nbsp; Releases &nbsp;·&nbsp; Contributing What It Does 500+ curated news
  feeds across 15 categories, AI-synthesized into briefs Dual map engine — 3D globe
  (globe.gl) and WebGL flat map (deck.gl) with 56 map layer types Cross-stream correlation
  — military, economic, disaster, and escalation signal convergence Country Instability
  Index (CII) — server-authoritative CII v8 stress scoring for 31 Tier-1 countries
  Finance radar — 29 stock exchanges, commodities, crypto, and 7-signal market composite
  Local AI — run everything with Ollama, no API keys required 6 site variants from
  a single codebase (world, tech, finance, commodity, happy, energy) Native desktop
  app (Tauri 2) for macOS, Windows, and Linux 24 languages with native-language feeds
  and RTL support For the full feature list, architecture, data sources, and algorithms,
  see the documentation. Support Status All site variants and desktop binaries are
  built from a single codebase and ship from the same release process. The table below
  clarifies maintenance status so you know which surfaces are safe to depend on. Surface
  Status Notes worldmonitor.app, tech., finance., commodity., happy., energy. Stable
  Public deployments built from this repo, actively maintained Desktop binaries (Windows
  / macOS Apple Silicon / macOS Intel / Linux AppImage) Stable One Tauri binary that
  switches variants in-app; current CI release targets are full and tech Issues filed
  against any of the above are triaged from the same backlog — see the issues board
  for currently-open work. Quick Start git clone https://github.com/koala73/worldmonitor.git
  cd worldmonitor npm install npm run dev Open localhost:3000. The app runs with no
  environment variables. Feature-specific data sources may require credentials — for
  example, the flight-price command (fly LON DXB) needs TRAVELPAYOUTS_API_TOKEN to
  return live quotes; without it the command shows a "credentials required" message
  rather than synthetic data. See .env.example for the full list. For variant-specific
  development: npm run dev:tech # tech.worldmonitor.app npm run dev:finance # finance.worldmonitor.app
  npm run dev:commodity # commodity.worldmonitor.app npm run dev:happy # happy.worldmonitor.app
  npm run dev:energy # energy.worldmonitor.app See the self-hosting guide for deployment
  options (Vercel, Docker, static). Tech Stack Category Technologies Frontend Vanilla
  TypeScript, Vite, globe.gl + Three.js, deck.gl + MapLibre GL Desktop Tauri 2 (Rust)
  with Node.js sidecar AI/ML Ollama / Groq / OpenRouter, Transformers.js (browser-side)
  API Contracts Protocol Buffers (276 protos, 34 services), sebuf HTTP annotations
  Deployment Vercel Edge Functions (60+), Railway relay, Tauri, PWA Caching Redis
  (Upstash), 3-tier cache, CDN, service worker Full stack details in the architecture
  docs. Flight Data Flight data provided gracefully by Wingbits, the most advanced
  ADS-B flight data solution. Data Sources WorldMonitor aggregates 65+ external providers
  and APIs across geopolitics, finance, energy, climate, aviation, cyber, military,
  infrastructure, and news intelligence — surfaced through 500+ curated feeds and
  tracked by a freshness monitor covering 35 source groups. See the full data sources
  catalog for providers, feed tiers, and collection methods. Contributing Contributions
  welcome! See CONTRIBUTING.md for guidelines. npm run typecheck # Type checking npm
  run build:full # Production build License AGPL-3.0-only for the source code. Commercial
  use is permitted under the AGPL when you comply with its copyleft and source-availability
  terms. Use Case Allowed? Personal / research / educational Yes, under AGPL-3.0-only
  Self-hosted instance Yes, under AGPL-3.0-only Fork and modify Yes, share source
  under AGPL-3.0-only when required Commercial use / SaaS Yes, under AGPL-3.0-only
  when you comply with AGPL obligations Private-source proprietary use or official
  branding rights Separate commercial or trademark permission needed See LICENSE for
  the full code license and docs/license.mdx for a plain-language summary. Commercial
  licensing is available as an alternative option for teams that need non-AGPL terms.
  Copyright (C) 2024-2026 Elie Habib. All rights reserved. Author Elie Habib — GitHub
  Contributors Security Acknowledgments We thank the following researchers for responsibly
  disclosing security issues: Cody Richard — Disclosed three security findings covering
  IPC command exposure, renderer-to-sidecar trust boundary analysis, and fetch patch
  credential injection architecture (2026) See our Security Policy for responsible
  disclosure guidelines. worldmonitor.app &nbsp;·&nbsp; docs.worldmonitor.app &nbsp;·&nbsp;
  finance.worldmonitor.app &nbsp;·&nbsp; commodity.worldmonitor.app Star History'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5fce3c914fe93bcc
source_type: community_discussion
tldr: WorldMonitor 是一个开源实时全球情报仪表盘，聚合 500+ 新闻源、双地图引擎（3D 地球和 WebGL 平面地图）、国家不稳定指数（CII）和金融雷达，支持本地
  AI 运行、6 种站点变体和桌面客户端，基于 AGPL-3.0 协议开源。
objective_summary: Elie Habib 开发的开源项目 WorldMonitor 于 2024-2026 年间持续维护，提供了一个统一态势感知界面。该项目聚合超过
  65 个外部服务提供商和 API，覆盖地缘政治、金融、能源、气候、军事等 15 个类别的 500+ 精选新闻源。系统通过 AI 将新闻综合为简报，并配备 3D
  地球（globe.gl）和 WebGL 地图（deck.gl）双引擎及 56 种地图图层。项目还包含针对 31 个 Tier-1 国家的服务器端 CII v8
  压力评分、覆盖 29 个证券交易所的金融雷达以及 7 信号市场复合指标。该代码库可在 Vercel、Docker 或静态托管上部署，并提供 Tauri 2 桌面客户端支持
  macOS、Windows 和 Linux。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - koala73
  - Ollama
  - Groq
  - OpenRouter
  - Upstash
  - Wingbits
  - Vercel
  technologies:
  - globe.gl
  - Three.js
  - deck.gl
  - MapLibre GL
  - Tauri 2
  - Transformers.js
  - Protocol Buffers
  - Redis
  - AGPL-3.0
  key_people:
  - Elie Habib
  - Cody Richard
key_logic_flow:
- WorldMonitor 是一个开源的实时全球情报仪表盘项目，提供统一态势感知界面。
- 系统聚合 65+ 外部数据提供商和 API，通过 500+ 精选新闻源覆盖地缘政治、金融、军事等 15 个类别。
- 项目配备双地图引擎（3D 地球 globe.gl 和 WebGL 平面地图 deck.gl），支持 56 种地图图层类型。
- 内置针对 31 个 Tier-1 国家的服务器端国家不稳定指数（CII v8）压力评分系统。
- 金融雷达覆盖 29 个证券交易所、大宗商品和加密货币，并包含 7 信号市场复合指标。
- 代码库支持 6 种站点变体和 Tauri 2 桌面客户端，采用 AGPL-3.0 协议开源且允许商业使用。
extract_result: success
object_mentions:
- object_type: project
  name: koala73/worldmonitor
  canonical_name: koala73/worldmonitor
  url: https://github.com/koala73/worldmonitor
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - WorldMonitor 是一个开源实时全球情报仪表盘，聚合 500+ 新闻源并进行 AI 综合生成简报。
  - 该项目包含双地图引擎（3D 地球 globe.gl 和 WebGL 平面地图 deck.gl）和 56 种地图图层类型。
  - 项目采用 AGPL-3.0 协议开源，允许个人、研究和商业使用，但需遵守 AGPL 条款。
  article_id: 5fce3c914fe93bcc
- object_type: product
  name: worldmonitor.app
  canonical_name: WorldMonitor Web App
  url: https://worldmonitor.app
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - worldmonitor.app 是该项目的主站点变体，另包括 tech、finance、commodity、happy 和 energy 共 6 种变体。
  - 所有站点变体和桌面二进制文件从同一代码库构建并通过同一发布流程发布。
  - worldmonitor.app 等公共部署处于稳定状态，由该仓库积极维护。
  article_id: 5fce3c914fe93bcc
- object_type: product
  name: WorldMonitor Desktop
  canonical_name: WorldMonitor Desktop
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - WorldMonitor 提供基于 Tauri 2 的原生桌面客户端，支持 macOS、Windows 和 Linux 平台。
  - 桌面二进制文件（Windows、macOS Apple Silicon、macOS Intel、Linux AppImage）处于稳定状态。
  - 一个 Tauri 二进制文件可在应用内切换不同站点变体，当前 CI 发布目标为 full 和 tech 变体。
  article_id: 5fce3c914fe93bcc
---

**Real-time global intelligence dashboard** — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface.

**Documentation** ·
**Releases** ·
**Contributing**

**500+ curated news feeds**across 15 categories, AI-synthesized into briefs**Dual map engine**— 3D globe (globe.gl) and WebGL flat map (deck.gl) with 56 map layer types**Cross-stream correlation**— military, economic, disaster, and escalation signal convergence**Country Instability Index (CII)**— server-authoritative CII v8 stress scoring for 31 Tier-1 countries**Finance radar**— 29 stock exchanges, commodities, crypto, and 7-signal market composite**Local AI**— run everything with Ollama, no API keys required**6 site variants**from a single codebase (world, tech, finance, commodity, happy, energy)**Native desktop app**(Tauri 2) for macOS, Windows, and Linux**24 languages**with native-language feeds and RTL support

For the full feature list, architecture, data sources, and algorithms, see the **documentation**.

All site variants and desktop binaries are built from a single codebase and ship from the same release process. The table below clarifies maintenance status so you know which surfaces are safe to depend on.

| Surface | Status | Notes |
|---|---|---|
`worldmonitor.app` , `tech.` , `finance.` , `commodity.` , `happy.` , `energy.` |
Stable | Public deployments built from this repo, actively maintained |
| Desktop binaries (Windows / macOS Apple Silicon / macOS Intel / Linux AppImage) | Stable | One Tauri binary that switches variants in-app; current CI release targets are `full` and `tech` |

Issues filed against any of the above are triaged from the same backlog — see the issues board for currently-open work.

```
git clone https://github.com/koala73/worldmonitor.git
cd worldmonitor
npm install
npm run dev
```

Open localhost:3000. The app runs with no environment variables.

Feature-specific data sources may require credentials — for example, the flight-price command (`fly LON DXB`

) needs `TRAVELPAYOUTS_API_TOKEN`

to return live quotes; without it the command shows a "credentials required" message rather than synthetic data. See `.env.example`

for the full list.

For variant-specific development:

```
npm run dev:tech # tech.worldmonitor.app
npm run dev:finance # finance.worldmonitor.app
npm run dev:commodity # commodity.worldmonitor.app
npm run dev:happy # happy.worldmonitor.app
npm run dev:energy # energy.worldmonitor.app
```

See the **self-hosting guide** for deployment options (Vercel, Docker, static).

| Category | Technologies |
|---|---|
Frontend |
Vanilla TypeScript, Vite, globe.gl + Three.js, deck.gl + MapLibre GL |
Desktop |
Tauri 2 (Rust) with Node.js sidecar |
AI/ML |
Ollama / Groq / OpenRouter, Transformers.js (browser-side) |
API Contracts |
Protocol Buffers (276 protos, 34 services), sebuf HTTP annotations |
Deployment |
Vercel Edge Functions (60+), Railway relay, Tauri, PWA |
Caching |
Redis (Upstash), 3-tier cache, CDN, service worker |

Full stack details in the **architecture docs**.

Flight data provided gracefully by Wingbits, the most advanced ADS-B flight data solution.

WorldMonitor aggregates 65+ external providers and APIs across geopolitics, finance, energy, climate, aviation, cyber, military, infrastructure, and news intelligence — surfaced through 500+ curated feeds and tracked by a freshness monitor covering 35 source groups. See the full data sources catalog for providers, feed tiers, and collection methods.

Contributions welcome! See CONTRIBUTING.md for guidelines.

```
npm run typecheck # Type checking
npm run build:full # Production build
```

**AGPL-3.0-only** for the source code. Commercial use is permitted under the AGPL when you comply with its copyleft and source-availability terms.

| Use Case | Allowed? |
|---|---|
| Personal / research / educational | Yes, under AGPL-3.0-only |
| Self-hosted instance | Yes, under AGPL-3.0-only |
| Fork and modify | Yes, share source under AGPL-3.0-only when required |
| Commercial use / SaaS | Yes, under AGPL-3.0-only when you comply with AGPL obligations |
| Private-source proprietary use or official branding rights | Separate commercial or trademark permission needed |

See LICENSE for the full code license and docs/license.mdx for a plain-language summary. Commercial licensing is available as an alternative option for teams that need non-AGPL terms.

Copyright (C) 2024-2026 Elie Habib. All rights reserved.

**Elie Habib** — GitHub

We thank the following researchers for responsibly disclosing security issues:

**Cody Richard**— Disclosed three security findings covering IPC command exposure, renderer-to-sidecar trust boundary analysis, and fetch patch credential injection architecture (2026)

See our Security Policy for responsible disclosure guidelines.

worldmonitor.app · docs.worldmonitor.app · finance.worldmonitor.app · commodity.worldmonitor.app