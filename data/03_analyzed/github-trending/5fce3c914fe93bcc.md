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
impact_score:
  score: 5.0
  reason: 评分依据：WorldMonitor 是一个工程实现质量极高的开源情报仪表盘项目，单代码库产出6种站点变体、双地图引擎、本地AI推理、Tauri
    2桌面端等技术整合令人印象深刻。但从AI行业冲击力来看，它本质是对现有技术（Three.js/deck.gl/MapLibre/Ollama等）的系统级整合封装，而非模型架构或训练范式的底层突破。在开源情报（OSINT）仪表盘领域，已有Hugin、Datashare、OpenCTI等竞品，WorldMonitor并未开辟全新品类。它会对开源情报可视化社区产生积极影响，但尚不足以改变AI行业的竞争格局或技术路线。因此评为5.0分，属于重要但不颠覆性的开源产品发布。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 单代码库生成6种站点变体 + Tauri 2原生桌面应用的工程架构设计
hype_assessment:
  level: low
  reason: 判定依据：项目README采用技术文档式平实叙述，未出现'颠覆式''革命性''改变世界'等PR滥用词汇。每个功能点都有具体实现说明——如'276个Protocol
    Buffers protos、34个services''Redis三层缓存''34个CII v8评估指标''60+ Vercel Edge Functions'等——数据可信且有技术细节支撑。项目明确标注AGPL-3.0许可条款，透明度高。整体属于实打实的技术干货展示，未见明显概念包装。
information_entropy: high
domain_disruption:
  technical_innovation: 单代码库多站点变体架构（world/tech/finance/commodity/happy/energy 6种变体）结合双地图引擎（globe.gl
    3D + deck.gl WebGL）、本地AI推理（Ollama/Transformers.js）和Tauri 2原生桌面端的技术整合方案，展示了现代开源情报系统的全栈工程化能力，尤其在同一代码库中同时支撑Web
    App（含PWA）、Edge Functions和桌面二进制的架构设计具有工程参考价值。
  business_model: 采用AGPL-3.0-only严格开源协议配合可选的商业授权模式，在保持开源社区信任的同时为企业用户提供合规路径。这种'开源核心+商业授权'的混合策略可能成为开源情报（OSINT）工具领域的主流变现范式，影响后续同类项目的授权选择。
engineering_complexity: production_ready
compound_value:
  score: 3.5
  reason: WorldMonitor 是技术执行力极强的开源情报仪表盘项目（双地图引擎、6站点变体、Tauri 桌面端、500+新闻源整合），但从 VC 复利视角看存在三个硬伤：(1)
    无独家数据护城河——所有新闻源和金融数据均来自公开/第三方 API，聚合层价值容易被复制；(2) AGPL-3.0 许可条款对企业商业采用构成障碍，限制了收费
    SaaS 或企业级变现路径；(3) 单一个人维护者模式，长期持续迭代和社区治理存在不确定性。项目缺乏网络效应和数据飞轮——用户越多并不会让数据质量越好。虽然当下实用价值高，但
    3-5 年后难以成为不可替代的行业基础设施。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Ollama
- Vercel
- MapLibre
- Groq
- OpenRouter
- Upstash
- Wingbits
competitive_casualty:
- Palantir
- Recorded Future
- 商业地缘政治情报 SaaS 平台
- 高价企业级新闻聚合 API
market_opportunities:
- 企业安全团队可内部部署 WorldMonitor，用于地缘政治风险监控与供应链中断预警，替代昂贵的商业情报平台
- 创业者可在 WorldMonitor 基础上开发垂直行业变体（如能源、金融科技），提供定制化的 AI 情报聚合 SaaS 服务
- 依托其本地 AI 运行能力（Ollama/Transformers.js），构建面向政府或涉密单位的私有化情报分析系统，满足数据不出域要求
risk_matrix:
  regulatory: AGPL-3.0 强传染性许可要求修改后的代码也必须开源，商业 SaaS 化使用需严格合规；聚合 500+ 新闻源可能涉及版权法和跨境数据流动（GDPR、中国数据安全法）的灰色地带
  technological: 依赖 65+ 外部 API 和第三方数据源（如 Wingbits、Upstash），任一上游变更或中断都会直接影响系统功能；浏览器端
    Transformers.js 的推理速度有限，大规模实时场景可能性能不足
  competitive: 面临 Dataminr、Recorded Future 等成熟商业情报平台的竞争，后者在数据深度、客户关系和合规体系上具有明显优势；开源替代社区（如
    Grafana 生态）也可能逐步侵蚀差异化空间
  ethical: AI 驱动的新闻聚合与跨流关联分析存在信息偏见放大和误报扩散风险；实时追踪全球基础设施与军事动向可能被用于恶意监控或攻击目标识别
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: koala73/worldmonitor
  canonical_name: koala73/worldmonitor
  url: https://github.com/koala73/worldmonitor
  positioning: 一个开源的实时全球情报仪表盘，聚合500+新闻源覆盖15个类别，配备双地图引擎、国家不稳定指数和金融雷达。
  technical_signal: 项目技术架构包含双地图引擎及56种地图图层，使用Protocol Buffers定义276个接口协议，通过Vercel Edge
    Functions实现实时数据推送，并集成Ollama实现完全本地化AI推理能力。
  adoption_signal: 项目自2024年持续维护至今，主站点worldmonitor.app及5个主题变体均已稳定公开部署，桌面客户端覆盖macOS、Windows和Linux三大平台，CI持续发布更新版本。
  ecosystem_relevance: 项目整合65+外部数据服务提供商，汇聚500+新闻源，覆盖地缘政治、金融、能源、气候、军事等15个情报类别，是开源态势感知生态中的重要聚合平台。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: WorldMonitor是少数将地缘政治情报、金融雷达和国家不稳定指数整合在统一仪表盘的开源项目，技术架构成熟且支持本地部署和桌面客户端，在开源态势感知领域具有独特价值，值得持续跟踪其功能演进和社区发展。
  risk_notes:
  - 项目采用AGPL-3.0协议开源，商业使用需履行代码开源义务，对部分企业用户构成合规门槛。
  - 项目整合65+外部数据服务，单一数据源中断或API变更可能导致部分情报模块不可用。
  - 情报数据准确性与时效性高度依赖外部源质量，部分API需付费密钥才能获取实时数据。
  score: 7.0
  article_ids:
  - 5fce3c914fe93bcc
  evidence_snippets:
  - WorldMonitor 是一个开源实时全球情报仪表盘，聚合 500+ 新闻源并进行 AI 综合生成简报。
  - 该项目包含双地图引擎（3D 地球 globe.gl 和 WebGL 平面地图 deck.gl）和 56 种地图图层类型。
  - 项目采用 AGPL-3.0 协议开源，允许个人、研究和商业使用，但需遵守 AGPL 条款。
- object_type: product
  name: worldmonitor.app
  canonical_name: WorldMonitor Web App
  url: https://worldmonitor.app
  positioning: 一款实时全球情报Web应用，聚合500+新闻源并提供双地图可视化与AI简报能力，覆盖地缘政治、金融、能源等多个专题变体。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 地缘政治分析师
  - 金融从业者
  - 情报研究人员
  - 宏观策略投资者
  - 新闻聚合应用用户
  product_signal: 主站点提供6种专题变体和24种语言支持，集成双地图引擎与56种地图图层，通过Vercel Edge Functions实现全球低延迟访问。
  market_signal: 该项目为个人开发者主导的开源项目，尚未形成商业化模式，但其6个站点变体的稳定运行表明已积累一定的用户基础。
  differentiation: 与商业情报平台相比，worldmonitor.app是完全开源且支持本地部署的替代方案，双地图引擎和CII指数是核心差异化功能。
  watch_reason: 作为一个由个人开发者维护的开源全球情报平台，worldmonitor.app的功能完整度和技术成熟度超出同类项目，其6站点变体模式和Tauri桌面客户端的架构设计值得产品团队参考。
  risk_notes:
  - 个人开发者维护的项目存在维护持续性风险，关键功能依赖的付费API可能增加部署成本。
  - 开源社区尚未形成规模，贡献者和Issue响应速度可能无法与企业产品竞争。
  - 情报类产品涉及敏感数据合规问题，不同司法管辖区对情报展示有不同法律要求。
  score: 6.0
  article_ids:
  - 5fce3c914fe93bcc
  evidence_snippets:
  - worldmonitor.app 是该项目的主站点变体，另包括 tech、finance、commodity、happy 和 energy 共 6 种变体。
  - 所有站点变体和桌面二进制文件从同一代码库构建并通过同一发布流程发布。
  - worldmonitor.app 等公共部署处于稳定状态，由该仓库积极维护。
- object_type: product
  name: WorldMonitor Desktop
  canonical_name: WorldMonitor Desktop
  url: null
  positioning: 基于Tauri 2构建的原生桌面客户端，支持macOS、Windows和Linux三大平台，可在应用内切换不同站点变体，提供与Web版一致的情报体验。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 桌面端情报分析师
  - 注重隐私的本地化用户
  - 需要离线情报监控的专业用户
  product_signal: WorldMonitor Desktop基于Tauri 2框架，一个二进制文件支持应用内切换所有站点变体，当前CI发布目标覆盖full和tech两种变体。
  market_signal: 桌面客户端处于稳定发布状态，提供Windows、macOS和Linux二进制文件，但尚未看到大规模用户采纳的数据或社区反馈。
  differentiation: 与同类开源情报仪表盘的Web-only方案不同，WorldMonitor Desktop提供原生桌面体验和本地AI推理能力，支持离线部署场景。
  watch_reason: WorldMonitor Desktop展示了Tauri 2在数据密集型情报应用中的可行性，其单二进制支持多变体切换的架构设计值得关注，跟踪该项目可了解桌面端情报产品的技术演进方向。
  risk_notes:
  - 桌面客户端当前CI仅发布full和tech两种变体，其他变体的桌面支持可能不够完善。
  - Tauri 2框架在复杂数据可视化场景下的稳定性尚需更长时间验证。
  - 个人开发者维护的桌面应用在安全更新和漏洞响应方面可能存在延迟。
  score: 5.0
  article_ids:
  - 5fce3c914fe93bcc
  evidence_snippets:
  - WorldMonitor 提供基于 Tauri 2 的原生桌面客户端，支持 macOS、Windows 和 Linux 平台。
  - 桌面二进制文件（Windows、macOS Apple Silicon、macOS Intel、Linux AppImage）处于稳定状态。
  - 一个 Tauri 二进制文件可在应用内切换不同站点变体，当前 CI 发布目标为 full 和 tech 变体。
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