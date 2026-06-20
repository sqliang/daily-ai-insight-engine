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
tldr: WorldMonitor 开源实时全球情报仪表盘，集成500+新闻源与AI分析
objective_summary: Elie Habib 开发的 WorldMonitor 是一个开源实时全球情报仪表盘，集成500+精选新闻源、双地图引擎（globe.gl
  和 deck.gl）、国家不稳定指数（CII）和金融雷达。支持本地 AI 运行、6种站点变体和 Tauri 2 桌面应用，采用 AGPL-3.0 许可。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Vercel
  - Ollama
  - Groq
  - OpenRouter
  - Upstash
  - Wingbits
  - MapLibre
  technologies:
  - globe.gl
  - Three.js
  - deck.gl
  - MapLibre GL
  - Tauri 2
  - Protocol Buffers
  - Transformers.js
  - Redis
  - Vite
  - PWA
  - WebGL
  - AGPL-3.0
  key_people:
  - Elie Habib
  - Cody Richard
key_logic_flow:
- WorldMonitor 是一个开源的实时全球情报仪表盘，提供 AI 驱动的新闻聚合、地缘政治监控和基础设施追踪功能。
- 项目集成了500+精选新闻源（覆盖15个类别）、双地图引擎（globe.gl 3D地球和 deck.gl WebGL平面地图）以及56种地图图层类型。
- 提供国家不稳定指数（CII v8，覆盖31个 Tier-1 国家）和金融雷达（29个交易所、商品、加密货币、7信号市场复合指数）等专业分析模块。
- 支持本地 AI 运行（Ollama/Transformers.js）、6种站点变体（world/tech/finance/commodity/happy/energy）和
  Tauri 2 原生桌面应用（macOS/Windows/Linux）。
- 技术栈包括 Vanilla TypeScript、Vite、Three.js、deck.gl、MapLibre GL、Tauri 2（Rust）、Protocol
  Buffers（276 protos, 34 services）和 Redis 三层缓存。
- 代码采用 AGPL-3.0-only 许可，由 Elie Habib 开发，支持 Vercel Edge Functions、Docker 和静态文件等多种部署方式。
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