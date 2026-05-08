---
title: Spotify's AI DJ now supports French, German, Italian and Brazilian Portuguese
source: https://techcrunch.com/2026/05/07/spotifys-ai-dj-now-supports-french-german-italian-and-brazilian-portuguese/
author:
- '[[Ivan Mehta]]'
published: 2026-05-07
created: 2026-05-07
description: Spotify's AI DJ feature now supports French, German, Italian, and Brazilian
  Portuguese.
tags:
- clippings
id: ef2c16cfdd65c7a2
source_type: news_media
tldr: Spotify AI DJ 新增法、德、意、巴西葡语四种语言支持
objective_summary: Spotify 于 2026 年 5 月 7 日宣布，AI DJ 功能新增法语、德语、意大利语和巴西葡萄牙语支持，并扩展至奥地利、巴西、法国等
  8 个新市场。此前该功能仅支持英语和西班牙语，目前已在超过 75 个国家上线。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Spotify
  technologies:
  - AI DJ
  key_people: []
key_logic_flow:
- Spotify 于 2026 年 5 月 7 日宣布 AI DJ 功能新增法语、德语、意大利语和巴西葡萄牙语四种语言支持，此前仅支持英语和西班牙语。
- 不同语言的 AI DJ 拥有不同的名称和个性：Maia、Ben、Alex 和 Dani。
- 该功能扩展至奥地利、巴西、法国、德国、意大利、葡萄牙、韩国和瑞士 8 个新市场，目前已在超过 75 个国家可用。
- 2025 年 5 月，Spotify 更新 AI DJ 功能，允许用户通过语音指令与 AI DJ 对话并更改音乐氛围或流派。
- 2025 年 10 月，Spotify 新增文本交互功能，用户可像使用 ChatGPT 或 Claude 一样向 AI DJ 发送文字指令点歌。
- Spotify 持续在应用中增加 AI 功能，包括通过描述需求即可生成自定义歌单或播客列表的提示式播放列表功能。
impact_score:
  score: 2.3
  reason: 这是 Spotify AI DJ 功能的例行语言扩展，新增四种语言和八个市场，属于产品本地化迭代而非技术突破。短期来看，对行业格局几乎无冲击力——既没有新的模型能力发布，也没有改变
    AI 音乐推荐的技术范式。对于非 Spotify 用户或竞争对手（如 Apple Music、YouTube Music）而言，这是一个可预期的功能跟进，不构成竞争壁垒的变化。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 多语言 TTS 和 NLU 的工程落地质量，以及不同语言下 AI 个性的差异化设计
hype_assessment:
  level: low
  reason: TechCrunch 的报道是事实性陈述，没有使用'颠覆'、'革命性'等 PR 滥用词汇。该功能已在 75+ 国家上线，属于已落地产品的自然扩展，不存在概念包装或过度宣传。
information_entropy: medium
domain_disruption:
  technical_innovation: 在多语言语音交互场景下，Spotify 需要针对每种语言训练或微调不同的 TTS 声音模型和 NLU 意图识别管道，并定制不同的
    AI 人格（Maia/Ben/Alex/Dani）。其本质突破有限，更多是工程上的多语言支撑能力扩展，而非底层架构创新。
  business_model: 无。该功能面向现有 Premium 用户，不改变 Spotify 的订阅商业模式，也未开辟新的变现路径。
engineering_complexity: production_ready
compound_value:
  score: 5.5
  reason: Spotify AI DJ 多语言扩展本质上是存量产品的功能增强，而非新基础设施层的建立。其复利效应体现在两个维度：一是多语言覆盖扩大了交互数据池，AI
    模型随用户使用量增长而持续优化，形成数据飞轮；二是语音/文本交互加深了用户与 Spotify 之间的粘性，用户对个性化 AI DJ 的投入（调教、歌单偏好）构成潜在迁移成本。但整体护城河偏浅——该功能并非不可复制的技术壁垒，Apple
    Music、YouTube Music 等竞品可通过授权或自建方式推出类似功能。长期来看，AI DJ 作为 Spotify 生态内的交互入口，价值上限受限于
    Spotify 自身用户基数，不具备独立平台级复利效应，因此评分 5.5。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Spotify
competitive_casualty:
- Apple Music
- Amazon Music
- 传统广播电台
market_opportunities:
- 多语言、多文化背景的 AI 语音助手/数字人 IP 定制化服务存在明确市场需求，创业者可为区域市场打造具有本土化人格的 AI 交互产品
- 音乐流媒体之外的垂直场景（如播客平台、有声书、健身应用）可借鉴 Spotify AI DJ 模式，将 LLM 交互、语音合成与个性化推荐融合，提升用户黏性
- 针对中小型音乐平台或区域性流媒体服务，提供白标化的 AI DJ 引擎集成方案，直接复制 Spotify 已验证的多语言交互体验
risk_matrix:
  regulatory: 多国市场扩展（欧盟、巴西、韩国）面临不同数据保护法规的合规压力，AI DJ 的语音交互涉及用户语音数据采集与处理，需满足 GDPR、LGPD
    等法律的严格要求；AI 生成的口播内容在不同市场可能涉及版权和内容审查风险
  technological: 语音 AI 和端侧模型技术迭代迅速，当前方案（依赖云端 LLM 和 TTS）面临被更高效的开源语音模型或端侧推理方案替代的风险；多语言口播的流畅度和自然度差异可能影响非英语市场的用户体验
  competitive: Apple Music、YouTube Music、Amazon Music 等竞品均在对 AI 个性化播放与语音交互功能加码投入，巨头在
    AI 基础模型和生态整合能力上具有显著优势，可能挤压 Spotify 的先发窗口
  ethical: AI DJ 的个性化推荐和互动可能加剧信息茧房效应，用户接触新音乐的多样性下降；AI 语音替代传统电台 DJ 和音乐节目主持人，存在就业替代隐忧
  additional:
  - 不同语言版本的 AI DJ 人格设定（Maia、Ben、Alex、Dani）若缺乏本地文化团队的深度参与，可能因文化误读引发市场抵触
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
---

Spotify said on Thursday that its interactive AI DJ feature now supports four additional languages: French, German, Italian, and Brazilian Portuguese. Until now, the feature, which you can interact with to request songs and get AI-powered spoken commentary, was only available in English and Spanish.

The company said the AI DJs have different names and personalities to suit their respective languages: Maia, Ben, Alex, and Dani.

Besides expanding support for new languages, the company is bringing the feature to Austria, Brazil, France, Germany, Italy, Portugal, South Korea and Switzerland. The AI DJ is now available in more than 75 countries.

Spotify’s initial version of the AI DJ used to just provide commentary on songs while playing tracks that users would like. But over the last few years, the company has made attempts to make the feature more interactive. In May 2025, the streaming service updated the feature to [let users chat with the AI DJ and make requests](https://techcrunch.com/2025/05/13/spotifys-ai-dj-now-lets-you-use-voice-commands-to-personalize-your-tunes/) to change the mood or genre. The company also added the ability to [prompt the AI DJ](https://techcrunch.com/2025/10/15/you-can-now-text-spotifys-ai-dj/) to play tracks, similar to how ChatGPT, Claude, or Gemini operate.

The company has been adding more AI features to the app, such as the ability to create [custom playlists of songs or podcasts](https://techcrunch.com/2026/04/07/spotifys-prompted-playlist-feature-will-now-work-for-podcasts-too/) by simply describing what they want to listen to.