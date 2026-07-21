---
title: Pebble Mega Update – July 2026
source: https://repebble.com/blog/pebble-mega-update-july-2026
author:
- '[[crazysaem]]'
published: '2026-07-17'
created: '2026-07-17'
manifest_dates:
- '2026-07-17'
description: 'Article URL: https://repebble.com/blog/pebble-mega-update-july-2026
  Comments URL: https://news.ycombinator.com/item?id=48943174 Points: 112 # Comments:
  32'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ebb9acccbaac08b9
source_type: community_discussion
tldr: Pebble 团队在2026年7月更新中宣布 Pebble Time 2 已生产超过23000只并完成80%预订单发货；PebbleOS 电池续航大幅提升，Pebble
  2 Duo 中位续航从17天增至30天以上；Pebble Round 2 即将量产；Index 01 功能已在移动应用中上线；硬件问题提供免费更换。
objective_summary: rePebble（Core Devices）于2026年7月14日发布 Pebble 项目重大更新。Pebble Time 2
  智能手表已生产超过23000只，完成80%预订单发货，剩余订单预计7月底前完成。PebbleOS 通过功耗优化将 Pebble 2 Duo 中位电池续航从17天提升至30天以上。软件团队与
  Moddable 合作发布 SDK 更新，引入触屏、扬声器、RGB 背光 API 和 Alloy 原生 JS 框架。社区已为新产品创建2120个应用和表盘。Index
  01 功能在移动应用中上线，支持多平台同步和 MCP 集成。硬件方面报告了高功耗、触控故障、玻璃裂纹和按钮问题，公司已为330只 PT2 提供免费更换且不限保修期。Pebble
  Round 2 正在进行量产前环境测试。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Core Devices
  - Moddable
  technologies:
  - PebbleOS
  - PPoGATT
  - ASK
  - BLE
  - FFI
  - MCP
  key_people:
  - Gerard
  - Claudio
  - Trevor
  - Colin
  - Nicholas Jitkoff
key_logic_flow:
- Pebble Time 2 已生产超过23000只手表，完成80%以上预订单发货，剩余黑色和红色版预计7月31日前发出，灰色和蓝色版7月28日前发出。
- PebbleOS 软件团队将 Pebble 2 Duo 的中位电池续航从17天提升至超过30天，Pebble Time 2 当前中位续航约为21天。
- 与 Moddable 团队合作发布了 Pebble SDK 更新，新增触屏 API、扬声器 API、RGB 背光 API、Alloy 原生 JS 应用框架以及
  FFI（C 代码与 JS 互调）功能。
- 社区开发者已为 Pebble Time 2 和 Pebble Round 2 创建了2120个应用和表盘。
- Index 01 全部核心功能已在 Pebble 移动应用中上线，支持与 iOS Reminders、Obsidian、Google Tasks、日历、MCP
  和 Webhook 同步，并提供端到端加密和开源代码。
- 硬件方面报告了高功耗、触控面板故障、玻璃裂纹（51例）和按钮问题（32例）等主要质量缺陷，公司为330只 PT2 免费更换且不限保修期。
object_mentions:
- object_type: product
  name: Pebble Time 2
  canonical_name: Pebble Time 2
  url: https://repebble.com/watch
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 自2026年3月底开始量产以来，Pebble 已生产超过23000只 Pebble Time 2 手表，完成80%以上预订单发货。
  - Pebble Time 2 黑色和红色版预计2026年7月31日前发货，灰色和蓝色版预计7月28日前发货。
  - 截至更新时，公司已为330只 PT2 提供免费更换，累计用户使用时长达到1782万小时。
  article_id: ebb9acccbaac08b9
- object_type: product
  name: Pebble Round 2
  canonical_name: Pebble Round 2
  url: https://repebble.com/watch
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 2026年7月初，Pebble 向注册测试的用户寄送了更多 Pebble Round 2 手表以进行 Beta 版软件测试。
  - 因不锈钢底壳的 CNC 加工外观缺陷，Round 2 未能在5月启动量产，工厂已接收新版底壳。
  - 团队计划自2026年7月14日起开始量产 Pebble Round 2 手表，同时正在进行跌落等环境测试。
  article_id: ebb9acccbaac08b9
- object_type: project
  name: PebbleOS
  canonical_name: PebbleOS
  url: https://github.com/pebble
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PebbleOS 通过功耗优化将 Pebble 2 Duo 的中位电池续航从17天提升至超过30天。
  - 团队对 PebbleOS 和移动应用进行了数百项稳定性改进，跟踪修复计步不准、加速度计失灵和触屏失灵三个主要软件问题。
  - 软件路线图包括发送短信应用、查找手机、全新天气应用、所见即所得表盘编辑器和反向 PPoGATT 迁移等。
  article_id: ebb9acccbaac08b9
- object_type: product
  name: Index 01
  canonical_name: Index 01
  url: https://index.repebble.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Index 01 的全部核心功能已在 Pebble 移动应用中上线，用户可在设置中启用 Index 信息流。
  - Index 01 支持与 iOS Reminders、Obsidian、Google Tasks、日历、MCP 和 Webhook 同步，并提供可选的端到端加密。
  - 团队还构建了 Web 应用 index.rePebble.com，用户可在任何位置访问 Index 信息。
  article_id: ebb9acccbaac08b9
- object_type: product
  name: Pebble mobile app
  canonical_name: Pebble mobile app
  url: https://repebble.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Index 01 的全部核心功能已集成在 Pebble 移动应用中，用户可通过设置中的开关启用 Index 信息流。
  - 团队对 Pebble 移动应用进行了数百项稳定性改进，持续根据用户反馈修复问题。
  - 移动应用正逐步推进反向 PPoGATT 迁移，以启用 iOS AccessorySetupKit 和欧盟地区的通知回复功能。
  article_id: ebb9acccbaac08b9
- object_type: project
  name: coredevices/mobileapp
  canonical_name: coredevices/mobileapp
  url: https://github.com/coredevices/mobileapp
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Pebble 移动应用的全部代码已在 github.com/coredevices/mobileapp 上开源。
  - 该开源仓库包含 Index 01 功能、Pebble 手表通信等完整的移动端实现。
  article_id: ebb9acccbaac08b9
- object_type: project
  name: Alloy
  canonical_name: Alloy
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Alloy 是 Pebble SDK 中新增的原生 JS 应用框架，允许在 Pebble 手表上运行纯 JavaScript 应用。
  - Alloy 支持 FFI 功能，允许在 JavaScript 应用中直接调用 C 代码，类似于 Android NDK 的工作方式。
  article_id: ebb9acccbaac08b9
- object_type: project
  name: XSBUG
  canonical_name: XSBUG
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - XSBUG 是 Pebble SDK 中新增的 JavaScript 调试器，通过 pebble build --debug 命令启动。
  - 启用调试构建后，PBL_DEBUG 宏被定义并自动启动 XSBUG 调试器用于 JS 应用调试。
  article_id: ebb9acccbaac08b9
- object_type: project
  name: Chronology II
  canonical_name: Chronology II
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Chronology II 是由 Nicholas Jitkoff 开发的 Pebble 表盘，被作者列为当前最喜爱的表盘。
  article_id: ebb9acccbaac08b9
extract_result: success
impact_score:
  score: 3.5
  reason: 该更新主要面向 Pebble 智能手表社区，虽涉及电池续航大幅优化、SDK 更新、Index 01 AI 功能的移动端上线等多项实质性进展，但整体属于特定硬件生态的迭代而非改变
    AI 行业格局的事件。Pebble 作为怀旧型智能手表品牌，其回归对主流 AI/穿戴赛道竞争格局影响有限。Index 01 的 MCP 集成和开源移动端算是一个亮点，但尚未形成规模效应。综合评估，对
    AI 行业冲击力处于低水平。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: SDK 新增触屏、扬声器、RGB 背光 API 和 Alloy 原生 JS 框架，以及 FFI 实现 C/JS 互调
hype_assessment:
  level: low
  reason: 文章风格极其务实，几乎没有 PR 包装。团队明确给出了生产数据（23000+只、80%订单完成、具体发货日期）、续航提升的中位数值（17天→30天+）以及硬件缺陷统计（51例玻璃裂纹、32例按钮问题），并主动承认问题提供免费更换。这种透明度与数据化表述表明不是炒作。
information_entropy: high
domain_disruption:
  technical_innovation: PebbleOS 功耗深度优化将 2 Duo 中位续航从 17 天提升至 30 天以上；反向 PPoGATT 重构以支持
    iOS ASK 和通知回复功能，是蓝牙协议栈层面的系统性改进。
  business_model: Core Devices 采用 DTC（Direct-to-Consumer）预售模式，通过社区驱动开发降低 R&D 成本，同时以开源移动端应用和
    Index 01 AI 笔记功能构建生态锁定。但 Pebble 整体仍是小众复古硬件，未改变智能穿戴主流商业模式。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: Pebble 的长期复利价值建立在三个差异化支柱上：1) 开源软硬件生态的社区网络效应——SDK 开放、Alloy 框架、FFI 互调能力已吸引社区创建2120个应用/表盘，这种开发者投资会随时间形成迁移成本壁垒；2)
    电池续航统治力（中位30天+ vs Apple Watch 的1-2天）在可穿戴市场是真实且可感知的护城河，对特定用户群（户外、极客、续航焦虑者）有强吸引力；3)
    Index 01 的 MCP 集成将 Pebble 定位为 AI Agent 时代的 wrist-worn interface，这是区别于传统手表的代际优势。但规模仅23000台、供应链天花板明显、且智能手表作为品类被
    Apple Watch + 手机取代的风险仍在，6分反映其在细分赛道有扎实护城河潜质，但离主流市场仍缺跨越鸿沟的催化剂。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Core Devices
- Moddable
- Anthropic (MCP 生态受益)
- Pebble 社区开发者
competitive_casualty:
- 传统长续航智能手表厂商（Garmin 等）
- 其他 AI 可穿戴创业公司
- 闭源智能手表平台
market_opportunities:
- Pebble SDK 新增触屏、扬声器、RGB 背光 API 和 Alloy 原生 JS 框架，为开发者创造了打造差异化智能手表应用和表盘的机会，可聚焦于低功耗健康辅助、工具类应用等细分场景
- Index 01 的语音录制与 AI 转录功能结合 MCP 和 Webhook 集成，为可穿戴 AI 配件开创了新品类，创业者可围绕语音笔记→知识管理的工作流自动化构建
  SaaS 服务
- Pebble 社区已有 2120 款应用/表盘且仍在快速增长，开发者可面向 Pebble Time 2 和 Pebble Round 2 受众提供付费主题与专业工具应用，利用小团队低成本优势抢占生态位
risk_matrix:
  regulatory: Index 01 语音录制与转录功能涉及用户隐私与数据跨境合规，尤其在 GDPR 下需明确数据存储与处理边界；Notification
    Forwarding 功能标注 'EU only' 暗示受欧盟数字市场法规制，iOS 平台接口限制（PPoGATT 反向工程）可能进一步面临应用商店审核风险
  technological: PebbleOS 依赖 iOS/Android 平台 BLE 协议栈，苹果 AccessorySetupKit 切换需全量固件升级，存在平台策略变更导致的兼容性中断风险；e-ink
    低功耗显示方案可能被新兴的 MicroLED 或更低功耗彩色屏幕技术替代
  competitive: Apple Watch、Garmin、Google Pixel Watch 等主流产品在健康传感、应用生态和品牌认知上具有压倒性优势，Pebble
    的差异化（长续航、开源、复古设计）护城河较浅，巨头一旦推出类似定位产品将直接挤压生存空间
  ethical: Index 01 持续语音录制在未明确征得对方同意的场景下可能引发隐私争议；51 例玻璃裂纹报告虽已免费更换，但硬件质量缺陷若持续出现将影响用户信任并带来产品安全声誉风险
  additional:
  - 核心软件团队仅 4 人，供应链与客服团队共 3 人，极小的组织规模在面对需求激增或硬件质量危机时抗压能力有限
  - 硬件组件（定制屏幕、电池等）供应链集中，若 Pebble Round 2 量产或 PT2 补货期间遭遇供应链中断将直接影响交付能力
  - 社区驱动模式的双刃剑：核心功能（如 HRV、SP02、麦克风 API）依赖外部贡献者，关键特性进度不可控
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: Pebble Time 2
  canonical_name: Pebble Time 2
  url: https://repebble.com/watch
  positioning: Pebble Time 2 是 rePebble 推出的新一代智能手表，采用电子墨水屏与物理按键设计，主打超长续航和开源社区生态。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Pebble 老用户及极客爱好者
  - 追求超长续航的智能手表用户
  - 开源硬件与社区生态参与者
  product_signal: 已生产超过23000只手表，完成80%预订单发货，累计用户使用时长达到1782万小时。
  market_signal: 预订单覆盖93个国家，黑色和红色版预计2026年7月31日前发货，即将进入现货销售状态。
  differentiation: 在主流智能手表追求彩色触屏和丰富应用的潮流下，PT2以电子墨水屏、数周续航和开源生态形成差异化竞争力。
  watch_reason: Pebble Time 2 是 Pebble 品牌复活后首款量产产品，已累计生产超23000只并覆盖93个国家，其量产交付能力和用户增长趋势是衡量
    Pebble 复活计划成功与否的核心指标。
  risk_notes:
  - 已报告高功耗、触控故障、玻璃裂纹（51例）和按钮问题（32例）等硬件质量缺陷，质量控制有待加强。
  - 公司为330只 PT2 提供免费更换且不限保修期，售后成本可能对利润空间造成持续压力。
  score: 8.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - 自2026年3月底开始量产以来，Pebble 已生产超过23000只 Pebble Time 2 手表，完成80%以上预订单发货。
  - Pebble Time 2 黑色和红色版预计2026年7月31日前发货，灰色和蓝色版预计7月28日前发货。
  - 截至更新时，公司已为330只 PT2 提供免费更换，累计用户使用时长达到1782万小时。
- object_type: product
  name: Pebble Round 2
  canonical_name: Pebble Round 2
  url: https://repebble.com/watch
  positioning: Pebble Round 2 是 rePebble 推出的圆形表盘智能手表，延续 Pebble 经典的圆屏设计和电子墨水屏技术。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Pebble 经典圆屏爱好者
  - 开源硬件极客
  - 追求差异化设计的手表用户
  product_signal: 计划于2026年7月14日起启动量产，已向 Beta 测试用户寄送测试手表，但量产曾因底壳缺陷推迟。
  market_signal: 目前处于 Beta 软件测试阶段，已完成测试用户招募，量产时间表仍存在不确定性。
  differentiation: 在方形智能手表主导的市场中，以独特的圆形电子墨水屏设计和开源生态形成差异化定位。
  watch_reason: Pebble Round 2 以圆形电子墨水屏设计拓展 Pebble 产品线，其量产进展和首批用户反馈将验证 rePebble 的产品线扩展能力和供应链管理水平。
  risk_notes:
  - 不锈钢底壳 CNC 加工外观缺陷导致量产推迟超过两个月，供应链质量控制能力有待验证。
  - 正在进行跌落等环境测试，量产时间表和质量稳定性仍存在不确定性。
  - 作为第二款产品，用户需求和市场接受度尚未经过大规模验证。
  score: 7.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - 2026年7月初，Pebble 向注册测试的用户寄送了更多 Pebble Round 2 手表以进行 Beta 版软件测试。
  - 因不锈钢底壳的 CNC 加工外观缺陷，Round 2 未能在5月启动量产，工厂已接收新版底壳。
  - 团队计划自2026年7月14日起开始量产 Pebble Round 2 手表，同时正在进行跌落等环境测试。
- object_type: project
  name: PebbleOS
  canonical_name: PebbleOS
  url: https://github.com/pebble
  positioning: PebbleOS 是 rePebble 维护的开源智能手表操作系统，基于原 Pebble 固件持续优化功耗与功能，支持全系新款 Pebble
    手表。
  technical_signal: 通过功耗优化将 Pebble 2 Duo 中位电池续航从17天提升至超过30天，Pebble Time 2 中位续航约21天且仍有改进空间。
  adoption_signal: 社区开发者已为 Pebble Time 2 和 Pebble Round 2 创建了2120个应用和表盘，生态活跃度持续提升。
  ecosystem_relevance: 与 Moddable 团队合作发布 SDK 更新，引入触屏 API、扬声器 API、RGB 背光 API 和 Alloy
    JS 框架，大幅降低开发门槛。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: PebbleOS 是整个 Pebble 硬件生态的核心软件基石，其功耗优化成果（续航翻倍至30天以上）、SDK 迭代速度和社区贡献活跃度直接决定了
    Pebble 平台的长期竞争力和用户体验。
  risk_notes:
  - 核心软件团队仅四人，人力有限可能制约路线图推进速度和问题响应能力。
  - iOS 端反向 PPoGATT 迁移技术复杂度高，需要升级所有在用手表的恢复固件，工程周期长。
  score: 9.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - PebbleOS 通过功耗优化将 Pebble 2 Duo 的中位电池续航从17天提升至超过30天。
  - 团队对 PebbleOS 和移动应用进行了数百项稳定性改进，跟踪修复计步不准、加速度计失灵和触屏失灵三个主要软件问题。
  - 软件路线图包括发送短信应用、查找手机、全新天气应用、所见即所得表盘编辑器和反向 PPoGATT 迁移等。
- object_type: product
  name: Index 01
  canonical_name: Index 01
  url: https://index.repebble.com
  positioning: Index 01 是 Pebble 生态系统中的个人信息管理功能，支持多平台同步和端到端加密，深度集成在 Pebble 移动应用中。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Pebble 智能手表用户
  - 注重隐私的个人信息管理用户
  - 跨平台同步需求用户
  product_signal: 全部核心功能已在 Pebble 移动应用中上线，用户可通过设置中的开关启用 Index 信息流并体验完整功能。
  market_signal: 已提供 Web 应用 index.rePebble.com 支持跨平台访问，但功能仍处于初版阶段。
  differentiation: 将个人信息流（备忘录、任务、日历）与智能手表深度集成，以开源代码和端到端加密形成隐私差异化优势。
  watch_reason: Index 01 是 Pebble 从硬件向软件服务延伸的关键产品，其多平台同步、MCP 集成和端到端加密的设计思路反映了 Pebble
    平台的差异化战略方向和生态扩展能力。
  risk_notes:
  - 功能尚处于初版阶段，成熟度和用户体验有待更大规模的市场验证。
  - 与 iOS Reminders、Obsidian 等第三方服务的集成稳定性依赖外部 API 变化。
  score: 6.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - Index 01 的全部核心功能已在 Pebble 移动应用中上线，用户可在设置中启用 Index 信息流。
  - Index 01 支持与 iOS Reminders、Obsidian、Google Tasks、日历、MCP 和 Webhook 同步，并提供可选的端到端加密。
  - 团队还构建了 Web 应用 index.rePebble.com，用户可在任何位置访问 Index 信息。
- object_type: product
  name: Pebble mobile app
  canonical_name: Pebble mobile app
  url: https://repebble.com
  positioning: Pebble 移动应用是 Pebble 智能手表的配套手机客户端，负责设备连接、通知管理和 Index 信息流展示，覆盖 iOS 和
    Android 平台。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Pebble 智能手表用户
  - iOS 和 Android 双平台用户
  product_signal: 已集成 Index 01 全部核心功能，正在推进反向 PPoGATT 迁移以启用 iOS AccessorySetupKit 和欧盟通知回复功能。
  market_signal: 社区贡献了 Apple HealthKit 和 Google health 同步等新功能，应用稳定性经过数百项改进持续优化。
  differentiation: 以开源移动应用代码和活跃社区贡献模式，区别于传统智能手表厂商的封闭式配套应用。
  watch_reason: Pebble 移动应用是连接手表与用户数字生活的核心枢纽，Index 01 集成和反向 PPoGATT 迁移两项关键更新将决定用户体验的完整度和平台可用性。
  risk_notes:
  - 反向 PPoGATT 迁移需要升级所有在用手表的恢复固件，工程量大且周期长。
  - 核心软件团队仅四人，移动应用迭代速度和问题响应可能受限于人力资源。
  score: 6.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - Index 01 的全部核心功能已集成在 Pebble 移动应用中，用户可通过设置中的开关启用 Index 信息流。
  - 团队对 Pebble 移动应用进行了数百项稳定性改进，持续根据用户反馈修复问题。
  - 移动应用正逐步推进反向 PPoGATT 迁移，以启用 iOS AccessorySetupKit 和欧盟地区的通知回复功能。
- object_type: project
  name: Alloy
  canonical_name: Alloy
  url: null
  positioning: Alloy 是 Pebble SDK 中原生 JavaScript 应用框架，允许开发者用纯 JS 编写手表应用，并通过 FFI 接口直接调用
    C 代码。
  technical_signal: 支持 FFI 功能，允许在 JavaScript 应用中直接调用 C 代码，工作方式类似于 Android NDK 的混合编程模式。
  adoption_signal: null
  ecosystem_relevance: 大幅降低了 Pebble 应用开发门槛，使 Web 开发者无需嵌入式经验即可参与 Pebble 生态建设，扩大了潜在开发者群体。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Alloy 框架是 Pebble 生态开发者工具链的重要创新，其"纯 JS 写应用加 FFI 调 C 代码"的设计可能大幅降低开发门槛，是观察
    Pebble 生态能否吸引 Web 开发者参与的关键信号。
  risk_notes:
  - 作为新生框架，Alloy 的稳定性和兼容性尚需社区开发者验证。
  - JavaScript 在嵌入式设备上的性能表现可能成为复杂应用运行的瓶颈。
  score: 5.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - Alloy 是 Pebble SDK 中新增的原生 JS 应用框架，允许在 Pebble 手表上运行纯 JavaScript 应用。
  - Alloy 支持 FFI 功能，允许在 JavaScript 应用中直接调用 C 代码，类似于 Android NDK 的工作方式。
- object_type: project
  name: XSBUG
  canonical_name: XSBUG
  url: null
  positioning: XSBUG 是 Pebble SDK 中集成的 JavaScript 调试器，通过 pebble build --debug 命令启动，为
    Pebble 应用开发提供调试能力。
  technical_signal: 在调试构建中自动定义 PBL_DEBUG 宏并启动 XSBUG 调试器，为 Pebble JS 应用提供完整的调试支持。
  adoption_signal: null
  ecosystem_relevance: 完善了 Pebble 开发者工具链，降低应用调试难度，对吸引社区开发者具有积极意义。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: XSBUG 作为 Pebble SDK 的开发调试工具，完善了开发者体验链条，其功能完备程度将直接影响社区应用的开发效率与整体质量。
  risk_notes:
  - 作为新发布的调试工具，XSBUG 的实际功能和稳定性尚待社区开发者反馈验证。
  score: 3.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - XSBUG 是 Pebble SDK 中新增的 JavaScript 调试器，通过 pebble build --debug 命令启动。
  - 启用调试构建后，PBL_DEBUG 宏被定义并自动启动 XSBUG 调试器用于 JS 应用调试。
- object_type: project
  name: Chronology II
  canonical_name: Chronology II
  url: null
  positioning: Chronology II 是由 Nicholas Jitkoff 开发的 Pebble 表盘，作为社区创意案例展示了 Pebble
    表盘生态的丰富性。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: 作为社区开发的表盘作品，反映了 Pebble 生态中开发者的创意活力和社区参与度。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Chronology II 作为社区开发的表盘案例，反映了 Pebble 生态中开发者的创意活力，但其作为单一表盘项目的独立跟踪价值相对有限，更多是生态活跃度的缩影。
  risk_notes:
  - 作为社区个人项目，Chronology II 的长期维护和与新版 PebbleOS 的兼容性存在不确定性。
  score: 2.0
  article_ids:
  - ebb9acccbaac08b9
  evidence_snippets:
  - Chronology II 是由 Nicholas Jitkoff 开发的 Pebble 表盘，被作者列为当前最喜爱的表盘。
---

TL:DR;

- Pebble Time 2 Shipping Status
- Pebble Software Updates
- PT2 - Issues You’ve Reported
- Pebble Round 2 Production Update
- Index 01 Production Update


Since we started mass production in late March, we’ve built over 23,000 Pebble Time 2 watches. We’re over 80% of the way through fulfilling all the pre-orders we’ve received! But that means there are still some ultra patient folks who haven’t received their watches yet. If you’ve placed an pre-order for PT2 and haven’t received it yet (including Batch 6 - August), here’s when we expect to ship your watch out:

- Pebble Time 2 - Black → July 31
- Pebble Time 2 - Red → July 31
- Pebble Time 2 - Grey → July 28
- Pebble Time 2 - Blue → July 28

Coincidentally, this means that we’ll be ‘in-stock’ with no wait very soon! If you’ve been holding off placing an order because you didn’t want to wait, now is the time to jump on it. This won’t last forever - first-come first serve. As soon as the current inventory is sold out, we’ll be back in pre-order mode waiting for the next shipment.

Order today on rePebble.com/watch.

Major props to our three person customer support and logistics team! Claudio, Trevor and Colin have answered thousands of your questions and helped ship watches safely onto your wrist in 93 countries. Have a question? Please check out our Help site first. If that doesn’t have an answer, please email us at [email protected].

Want an extra Pebble charger? shop.repebble.com now carries accessories - full selection of straps coming soon.

Over the last 6 months, the core four person Pebble software team built and shipped a metric ton of new Pebble open source software! Our improvements were centered around these areas:

**Battery life**

We’ve (well, mostly Gerard 🙂) worked extraordinarily hard over the last few months, optimizing and reducing power consumption in PebbleOS. As predicted, we boosted the median battery life of Pebble 2 Duo from 17 days (last summer) to over 30 days. Pebble Time 2 median is currently around 21 days - more improvements in the works here too! The biggest consumers of power are backlight, watchfaces with a lot of animations and health tracking. If you want to ‘hypermile’ your Pebble, try switching to a low-animation watchface and the new *Battery Saver* backlight mode (Settings → Display → Backlight).

**Apps and SDK**

**T**ogether with the Moddable team, we’ve published several Pebble SDK updates introducing new features like:

- Touch Screen API (Calculator on your wrist anyone?)
- Speaker API (useful for tuning your guitar, or feeding your Tamagotchi)
- RGB Backlight API (try it in this wild little app Chinese Toy Phone)
- Apps can now determine how they were quick launched (ie by single press, long press)
- Alloy (native JS apps)
- FFI - run C code within Alloy JS apps (similar to Android NDK) and js debugger
- A bunch of new JS APIs
`pebble build --debug`

now defines PBL_DEBUG and launches XSBUG, a powerful JS debugger


Developers in the Pebble community have created 2,120 apps and watchfaces for Pebble Time 2 and Pebble Round 2 already!

**Index 01**

The first version of all Index 01 functionality is up and running inside the Pebble mobile app. Don’t have an Index 01 yet? You can check out how it works and try the software interface in the Pebble app, just go to Settings → General → Enable Index feed.

All the main features are in, including syncing to iOS Reminders, Obsidian, Google Tasks, Calendar, Android music control, MCPs and sending recordings or transcriptions to your own server or app via Webhook. Optional encryption (you own the keys) protects optional cloud backup. And of course, it’s all open source (github.com/coredevices/mobileapp). We even built a little webapp that you can use to access your Index information from anywhere → index.rePebble.com. Watch the podcast or read the blog post to learn more.

**Stability**

Thanks to helpful bug reports from y’all, we’ve made hundreds of small improvements to PebbleOS and the Pebble mobile app. Please keep it coming!

I’ll dive into one specific (and ultra technical) topic - reverse PPoGATT (Pebble Protocol over GATT). Quick history: during the first Pebble era, we configured the Pebble mobile app to expose a PPoGATT service, as means to work around the lack of IPC between iOS apps. This setup is the opposite of how Bluetooth accessories normally connect to phones and caused a number of weird problems! Also this setup blocks us from using iOS AccessorySetupKit (ASK), which is a prerequisite for us to implement the new Notification Forwarding feature (EU only) that will finally enable you to reply to notifications. Enabling ASK is going to be tough - our iOS app must either use ASK or not, meaning that we need to upgrade the recovery firmware on all Pebble watches in the field to reverse PPoGATT before we can switch ASK on. Anyways, we have the first piece of the puzzle in place (Pebble Round 2’s recovery firmware already has the upgrade). This saga will take a while.

**Community Contributions**

Thank you to the dozens of developers from the broader Pebble community who have contributed huge improvements to PebbleOS and the mobile app, including Apple HealthKit and Google health sync, improved light sensor algorithms, notification filtering, many new language packs, and so many bug fixes. It’s so fun and very energizing to see so many talented hackers push PRs! See the full list and thank you devs! Some exciting new community built features are on the horizon: HRV, SP02, exposing HRM via BLE, mic API, multiple BLE clients and more

**Software Roadmap**

We keep improving Pebble software primarily because *we* are Pebble users. We love using the products we make and continually want to make them better! Here’s some of the things we’re excited to work on next:

- Send text app (Android only)
- Find my phone
- Beautiful new weather app for PT2 and PR2 (created by grim, a winner of the Spring Developer Contest)
- Tweaking PebbleOS UI for Round 2
- Improving the Pebble mobile app UI
- WYSIWYG watchface editor - spiritual successor to Pebble Canvas
- Continue transition to fully reverse PPoGATT role to enable ASK and (eventually) replies to notifications for iOS users (in EU)
- See below for index roadmap

Thank you all for reporting any bugs or issues you’ve spotted! We test each watch at the factory before it’s shipped out, and we test each software release internally and with a growing team of beta testers (want to join? Sign up at rePebble.com/account). But these tests are not infallible and we will make mistakes. We appreciate your reports as they help us get more information to help us fix problems!

**Software Issues**

We’re tracking three big software issues with PebbleOS, and a multitude of smaller problems. While we are actively working on fixing these with a future software , we don’t have an ETA on when these will be fixed.

- Step and sleep tracking metrics are not accurate for some people
- Accelerometer sometimes stops working
- Touch screen sometimes stops working or registers touches in wrong location

It would be tough to list here the long-tail of software issues we’ve had reported. But please note that while we don’t reply to everyone, we do read every single report and look for patterns and clues that help us fix many issues with each software update (see the changelog for PebbleOS and Pebble mobile app).

**Hardware Issues**

You’ve all demonstrated incredible patience waiting for your PT2 to ship. You’re excited to try the first brand new Pebble in the last 10 years. That’s why we understand how painful and difficult it could be if you unbox your brand new watch and discover manufacturing flaw, or use it for a few weeks and find the battery is dying too quickly or accidentally crack the glass. It sucks!

We feel your pain, even more than you can possibly imagine. That’s why everyone who has reported a hardware issue to our support team has received a free replacement (with free worldwide shipping) regardless of whether their device is under warranty or not.

To date, we’ve replaced 330 PT2s (out of 17.82 million hours of usage from 19,000+ watches in the field).

Mass producing a consumer electronic product is labour intensive. Making stuff is still a very human-centric process. We make mistakes. A worker may not assemble a part correctly. A test may be accidentally skipped. The test result could be read incorrectly. Procedures can be put in place to minimize mistakes, but the cost will rise. As with all of hardware product development - it’s a tradeoff 🤷.

The most frequent hardware issue we’re seeing is very high power consumption (less than ~3 day battery life). We’ve taken apart some units and found a variety of issues. To combat this, we’ve implemented more stringent power consumption testing on the assembly line. If you encounter this issue (regardless of your warranty eligibility), please send us a bug report in the Pebble app and we can help you out!

Next most frequent are problems with the touch panel. At first, we thought this could be a hardware problem and replaced around 70 watches. After reviewing the units with our factory, we now believe this could be a software bug. We’re working to fix these issues with a software update - if we can’t, we’ll replace the affected watches (regardless of your warranty eligibility).

Next up is the front glass cracking. We’ve had 51 reports so far, and we’ve sent a free replacement to each person affected. If your glass has cracked, send us a video (preferably, picture is ok) in a bug report in the Pebble app. During the lead up to mass production, we performed extensive environmental testing - including drop testing, tumble testing, button press, strap stretch and bend, thermal cycling and many other tests. All test results showed normal durability compared to similar smartwatches. But if your watch glass cracks, do you care what the factory test results were? Or that this has happened to just 0.25% of all PT2s - or once every 30+ years of usage? Of course not - your watch just broke. That’s why we will continue replacing reasonable reports of glass cracking for free as long as we can. At some point, we will shift to offering a replacement at a highly discounted amount. We are also looking into sourcing extra LCM modules (the entire front assembly - glass, touch panel, display, metal top cover and backlight) and making them available for folks who choose to fix their watch themselves.

The final big category of hardware issue are reports of button problems (32 so far). In some cases, a small interior clip is improperly assembled, causing the button to pop off. We’ve addressed this issue with changes to the production line process and hope that it becomes much less frequent as watches assembled after the change start making their way out into the world. If you encounter this issue (regardless of your warranty eligibility), please send us a bug report in the Pebble app and we can help you out!

Then we’ve had a long tail of smaller issues that I’m moderately embarrassed by, like a report of the watch missing screws on the bottom, or the front falling off. I guess these things do happen!


*My current favourite watchface -* *Chronology II* *by Nicholas Jitkoff*

I posted a mini-update on Pebble Round 2 in June - we weren’t able to start mass production in May because of a cosmetic problem with the stainless steel bottom case (an extra indentation made by the CNC milling machine). Since then the factory has received a new version of the bottom case and things are looking much better! In parallel, we’ve been running extensive environmental testing (including drop testing).

At the beginning of July, we shipped out more Pebble Round 2 watches to lucky folks who signed up for the beta test. Thanks for your help finding and testing fixes for bugs in PebbleOS!

Our plan (as of today July 14 - subject to change) is to start mass producing Round 2 watches during last week of July. We’ll start ramping up production slowly and carefully. Roughly 14,000 people have pre-ordered Round 2. It will take us about 2 months to build all pre-ordered watches. We expect to finish shipping out all pre-ordered Round 2 watches by the end of September.

If you preordered Round 2 on rePebble.com/watch, we’ll send you an email roughly 2 weeks before your watch is ready to ship asking you to confirm your address, add optional accessories to your order and pay any additional taxes due. If you haven’t already selected your watch colour, please do so on orders.rePebble.com.

Each Round 2 pre-order includes a silicone watch strap and charger. We’ve also created beautiful custom leather straps for PR2 ($20-30), including brown or black soft leather straps that feel very similar to the straps we made for the original Pebble Time Round.


Since our last update, we expanded our beta test and learned a lot from the hundreds of willing test subjects. Thank you for your service and bug reports!

Index 01 is now officially in mass production! We’ve assembled several thousand rings so far, and have gradually begun shipping them out. Schedule has slipped slightly from our last estimate (early August), we’re now aiming to ship out nearly all pre-orders by the end of August, except for a few unlucky size/color variants that will ship in September.

We’ve received reports from testers that Index 01 may feel every so slightly smaller than the ring sizers. Please take the time now to recheck your ring size with the ring sizer kit. If the ring sizer feels tight on your finger, is hard to get on/off, or if you cannot easily clench your hand with the sizer on, **please change your size to the next larger size.** When in doubt, order a larger size. You can always adjust a larger Index 01 to feel smaller with a foam adhesive or clip but you can’t make it larger!

If you preordered Index 01 on rePebble.com/index, we’ll send you an email roughly 2 weeks before your ring is ready to ship asking you to confirm your address and pay any additional taxes due. If you haven’t already selected your Index 01 size and colour, please do so on orders.rePebble.com.

Index 01 has changed my life. There’s no way I could go back to a world without external memory for my brain. And this is just the beginning, Index 01 software is improving every single day. I excited to hear what you think of it!