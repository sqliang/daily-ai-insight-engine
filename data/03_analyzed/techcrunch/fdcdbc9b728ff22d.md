---
title: Roblox launches an AI-powered game-creation feature in its mobile app
source: https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/
author:
- '[[Lauren Forristal]]'
published: '2026-07-16'
created: '2026-07-17'
manifest_dates:
- '2026-07-17'
description: Roblox's new "Build" feature lets users generate basic games using a
  single text prompt.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fdcdbc9b728ff22d
source_type: news_media
tldr: Roblox 发布名为 Build 的 AI 游戏创作功能，用户可通过文本提示在移动端直接生成并修改游戏，该功能将于 7 月 28 日在新西兰进行公开
  alpha 测试。
objective_summary: Roblox 于 2026 年 7 月 16 日宣布推出 Build 功能，该功能利用开源和专有 AI 模型，根据用户文本提示自动生成包含游戏机制、环境、角色和音效的完整游戏。用户可在移动端创建并修改游戏，9
  岁以上验证用户可参与 alpha 测试，16 岁以上用户可向全球发布。面对行业对 AI 低质量内容的担忧，Roblox 表示将依据玩家留存率对 AI 生成游戏进行排序。同时
  Roblox 还在开发游戏测试 AI 智能体和场景生成模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Roblox
  - Google
  - Microsoft
  - Tencent
  technologies:
  - generative AI
  - AI foundation model
  - scene-generation model
  key_people: []
key_logic_flow:
- Roblox 发布名为 Build 的 AI 游戏创作功能，用户可通过文本提示在移动端直接生成游戏。
- Build 功能结合开源和专有 AI 模型，自动完成游戏机制、环境、角色、视觉风格和音效等全部环节。
- 52% 的游戏行业专业人士认为生成式 AI 对行业产生负面影响，担忧其导致低质量和重复性游戏泛滥。
- Roblox 计划通过玩家留存率来排序 AI 生成游戏，无人游玩的游戏将不会获得推荐曝光。
- Build 功能将于 7 月 28 日在新西兰面向 9 岁以上验证用户进行公开 alpha 测试。
- Roblox 还在开发用于游戏测试的 AI 智能体和新场景生成模型，计划在未来数月内推出。
object_mentions:
- object_type: product
  name: Build
  canonical_name: Roblox Build
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Roblox 发布名为 Build 的 AI 游戏创作功能，用户可通过简单文本提示从移动设备直接设计和生成游戏。
  - Build 功能结合开源和专有 AI 模型，自动处理游戏机制、环境、角色、视觉风格和音效等全部创作环节。
  - 用户输入类似"让我们制作一个在茂密森林中的 cozy 冒险游戏"这样的提示，系统即可生成初始游戏版本。
  article_id: fdcdbc9b728ff22d
- object_type: product
  name: Roblox Connect
  canonical_name: Roblox Connect
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Roblox 在发布 Build 功能前不久宣布将停用 2023 年推出的基于虚拟形象的视频通话功能 Roblox Connect。
  article_id: fdcdbc9b728ff22d
- object_type: product
  name: AI agents for playtesting
  canonical_name: Roblox AI Playtesting Agents
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Roblox 正在开发 AI 智能体来协助创作者进行游戏测试并提供分析数据，预计在未来数月内推出。
  article_id: fdcdbc9b728ff22d
- object_type: model
  name: Roblox AI foundation model
  canonical_name: Roblox AI Foundation Model for 3D Assets
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Roblox 正在投资一个用于生成 3D 游戏资产的 AI 基础模型，作为其 AI 能力建设的一部分。
  article_id: fdcdbc9b728ff22d
- object_type: model
  name: Roblox scene-generation model
  canonical_name: Roblox Scene-Generation Model
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Roblox 正在开发新场景生成模型，可从单个文本提示生成可编辑和可玩的完整 3D 场景。
  article_id: fdcdbc9b728ff22d
extract_result: success
impact_score:
  score: 6.0
  reason: 该事件是 Roblox 平台的重要 AI 功能发布，将文本到游戏生成能力直接集成到移动端，可能显著降低游戏创作门槛，改变 Roblox UGC
    生态的竞争格局。但评估需谨慎：功能仍处于新西兰公开 alpha 测试阶段，规模有限；行业对此存在显著担忧（52% 游戏专业人士认为生成式 AI 负面影响行业）；AI
    生成游戏的质量和留存仍是未知数。Roblox 的留存率排序机制是合理的应对策略但尚未验证效果。综合来看，这是一次重要的产品级 AI 落地，会改变 Roblox
    局部竞争格局，但远未到行业范式转移的程度。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: AI 生成的低质量游戏内容泛滥风险，以及 52% 行业专业人士认为生成式 AI 对游戏行业产生负面影响
hype_assessment:
  level: medium
  reason: 文章本身措辞较为平衡，同时呈现了功能亮点和行业担忧，Roblox 的具体技术声明（结合开源与专有模型、全链路生成）也较具体。但 '通过文本提示即可生成完整游戏'
    这一叙事实质上延续了多年来 'AI 让所有人成为创作者' 的硅谷叙事传统，实际生成质量和用户体验尚未经过大规模验证。Roblox 未披露所用具体模型架构和生成成功率的基准数据，存在一定的
    PR 包装成分。
information_entropy: medium
domain_disruption:
  technical_innovation: Roblox 将文本到游戏的全链路生成能力（游戏机制、环境、角色、视觉风格、音效）集成到移动端应用中，结合开源与专有
    AI 模型，并正在开发可编辑 3D 场景生成模型和 AI 游戏测试智能体。技术上属于现有生成式 AI 技术在游戏领域的系统性应用集成，而非底层模型架构的突破性创新。
  business_model: 大幅降低游戏创作门槛，将 Roblox 的 UGC 内容供给从传统编程创作者扩展到零代码用户群体。免费+付费的分层订阅模式可能重塑平台内容供给结构，但
    AI 生成内容的低质量风险可能稀释平台整体内容价值。Roblox 计划采用玩家留存率排序机制来平衡 AI 生成内容的可见性，这一设计思路值得关注，其执行效果将直接影响
    Roblox 平台经济模型。
engineering_complexity: prototype
compound_value:
  score: 7.5
  reason: Roblox 的 Build 功能在其已有强大网络效应的 UGC 平台上叠加 AI 创作能力，形成'创作门槛降低 → 内容供给增加 → 用户停留时长增长
    → 创作者收入提升'的正向飞轮。玩家留存率排序机制是关键的护城河设计——它用数据淘汰低质量 AI 内容，避免平台沦为'AI Slop 沼泽'。结合正在开发的游戏测试
    AI 智能体和场景生成模型，Roblox 正在系统性地构建 AI-native 创作基础设施。该功能的复利效应体现在：(1) 每多一个 AI 辅助创作者，平台内容多样性
    +1，用户留存 +δ；(2) 每多一款高留存 AI 游戏，推荐系统信号更丰富，分发效率提升。但需持续验证：alpha 测试仅在新西兰进行，9-15 岁用户受限发布，AI
    生成内容的长期质量分布尚未可知。若执行到位，Roblox 将从'青少年游戏平台'向'全民游戏创作平台'跃迁，3-5 年后地位大概率更加稳固。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- Roblox
- NVIDIA
- Google Cloud
- Microsoft Azure
competitive_casualty:
- Unity
- Unreal Engine
- Rec Room
- Core Games
- 小型独立游戏开发者
- 传统游戏测试服务商
market_opportunities:
- 创业者可基于类似的多模型融合架构，开发面向垂直场景（如教育游戏、品牌营销互动）的AI游戏快速生成工具
- 围绕AI生成内容的品控与排序（如留存率驱动的推荐）可衍生出AI内容质量评估SaaS服务，为UGC平台提供内容治理方案
- AI游戏测试智能体（AI agent for playtesting）是尚未被充分商业化的蓝海方向，可切入游戏研发自动化测试赛道
risk_matrix:
  regulatory: 青少年保护风险：Roblox 核心用户群体为未成年人，AI 生成内容可能绕过现有内容审核机制，面临各国儿童在线安全法规（如 COPPA、UK
    Online Safety Act）的合规压力。此外，AI 创作内容的版权归属尚不明确，可能引发知识产权纠纷
  technological: AI 生成游戏同质化风险：依赖文本提示生成的游戏在机制和体验上可能趋于雷同，降低平台内容多样性。同时 Roblox 使用开源+专有模型的混合方案，开源模型的能力上限可能成为质量瓶颈
  competitive: 巨头入场竞争激烈：Google、Microsoft、Tencent 等均有类似 AI 游戏生成工具布局，Roblox 在移动端先发但面临生态挤压；此外
    AI 大幅降低创作门槛可能导致平台内供需失衡，原有优质创作者面临内容被海量 AI 内容淹没的风险
  ethical: 就业冲击与创作公平性：52% 的游戏行业专业人士认为生成式 AI 有负面影响，该功能可能侵蚀初级游戏开发者的就业机会；AI 生成游戏也可能加剧内容低质化和同质化，影响玩家体验和平台长期生态健康
  additional:
  - 平台依赖性风险：创作者对 Roblox 平台的绑定加深，AI 生成的游戏资产和逻辑难以迁移到其他平台
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Build
  canonical_name: Roblox Build
  url: null
  positioning: Roblox 在移动端推出的 AI 游戏创作功能，用户可通过文本提示直接生成并修改完整游戏，无需编程经验。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 9 岁以上经过年龄验证的 Roblox 用户（alpha 测试阶段）
  - 无编程经验但有游戏创作意愿的 Roblox 平台用户
  product_signal: 结合开源和专有 AI 模型，自动处理游戏机制、环境、角色、视觉风格和音效等全部创作环节。
  market_signal: 计划通过玩家留存率来排序 AI 生成游戏，无人游玩的游戏将不会获得推荐曝光。
  differentiation: 相比 Google、Microsoft、腾讯等公司的类似工具，Roblox 将 AI 生成游戏纳入了其已有的玩家留存率排序体系以控制质量。
  watch_reason: Build 是 Roblox 在 AI 驱动 UGC 创作方向上的重大战略举措，将于 2026 年 7 月 28 日在新西兰进行公开
    alpha 测试。如果成功，将极大降低游戏创作门槛，可能重塑 Roblox 平台的内容生态和竞争格局。
  risk_notes:
  - 52% 的游戏行业专业人士认为生成式 AI 对行业产生负面影响，担忧其导致低质量和重复性游戏泛滥。
  - AI 生成内容的实际玩家留存率尚未经过大规模验证，留存率排序能否有效过滤低质量内容存在不确定性。
  score: 8.0
  article_ids:
  - fdcdbc9b728ff22d
  evidence_snippets:
  - Roblox 发布名为 Build 的 AI 游戏创作功能，用户可通过简单文本提示从移动设备直接设计和生成游戏。
  - Build 功能结合开源和专有 AI 模型，自动处理游戏机制、环境、角色、视觉风格和音效等全部创作环节。
  - 用户输入类似"让我们制作一个在茂密森林中的 cozy 冒险游戏"这样的提示，系统即可生成初始游戏版本。
- object_type: product
  name: Roblox Connect
  canonical_name: Roblox Connect
  url: null
  positioning: Roblox 于 2023 年推出的基于虚拟形象的视频通话功能，已被宣布停用。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Roblox 平台用户
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Roblox Connect 的停用反映了 Roblox 在 AI 时代的产品战略调整，表明公司正将资源集中到 Build 等 AI
    创作功能上，放弃非核心社交功能。
  risk_notes: []
  score: 2.0
  article_ids:
  - fdcdbc9b728ff22d
  evidence_snippets:
  - Roblox 在发布 Build 功能前不久宣布将停用 2023 年推出的基于虚拟形象的视频通话功能 Roblox Connect。
- object_type: product
  name: AI agents for playtesting
  canonical_name: Roblox AI Playtesting Agents
  url: null
  positioning: Roblox 正在开发的用于协助游戏创作者进行自动化游戏测试并提供分析数据的 AI 智能体系统。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Roblox 平台游戏创作者
  product_signal: 可协助创作者进行游戏测试并提供分析数据，预计在未来数月内推出。
  market_signal: null
  differentiation: null
  watch_reason: 作为 Build AI 创作功能的配套工具，AI 游戏测试智能体将帮助创作者提升游戏质量，是 Roblox 完善 AI 创作工具链的重要组成部分。
  risk_notes:
  - 该功能尚在开发中，具体的推出时间和最终技术形态仍存在不确定性。
  - AI 智能体进行游戏测试的实际效果和对复杂游戏的适配能力尚未得到验证。
  score: 4.0
  article_ids:
  - fdcdbc9b728ff22d
  evidence_snippets:
  - Roblox 正在开发 AI 智能体来协助创作者进行游戏测试并提供分析数据，预计在未来数月内推出。
---

Roblox announced Thursday a new feature called “Build,” allowing users to design games from their mobile devices using AI.

The Build feature lets anyone turn simple text prompts into a basic game without any programming experience. For example, if a user types, “Let’s make a cozy adventure game set in a dense forest,” the new feature will generate an initial version of the game, which users can then modify and share with friends.

“Powered by a broad set of AI models, including both open-source and proprietary Roblox models, Build handles gameplay mechanics, environment, characters, visual style, sound, and more,” the company wrote in its blog post.

Companies like Google, Microsoft, and Tencent have built similar tools. However, AI-powered game generation has raised concerns among developers and players, with critics arguing that reducing the barriers to game development via text prompts could lead to an influx of low-quality and repetitive games. This may also increase competition on the platform, as creators are required to compete not only with other developers but also with AI-generated content that can be produced far more quickly.

These concerns are reflected in this year’s Game Developers Conference State of the Game Industry survey, which found that 52% of game industry professionals believe generative AI is having a negative impact on the industry.

To address this, Roblox plans to rank these AI-generated games based on player retention, similar to the system used for other games on the platform. If a game is not played, it won’t be featured as prominently.

“Our discovery systems are designed to highlight games with long-term retention, which doesn’t include AI slop. The quality of games on the homepage isn’t changing: If no one plays it — no one can find it. The goal across these new tools is to continue to accelerate creation across all experience levels,” the company added.

The Build feature will enter public alpha testing on July 28, available to users in New Zealand aged nine and older who have verified their age. Users aged 16 and up will have the opportunity to publish their creations to a global audience. There will be a free, basic version available along with paid options.

Beyond the Build feature, Roblox is also working on developing AI agents that will assist creators in playtesting and providing analytics. These features are anticipated to roll out in the upcoming months.

The new feature highlights Roblox’s ongoing investment in AI, including an AI foundation model for generating 3D game assets and an AI chatbot for supporting developers through the game-building process. Additionally, Roblox is developing a “new scene-generation model” capable of creating entire editable and playable 3D scenes from a single text prompt.

Additionally, the announcement comes shortly after Roblox disclosed plans to discontinue “Roblox Connect,” the avatar-based video-calling feature introduced in 2023.