---
title: Podcasting platform Riverside enters the newsletter publishing game
source: https://techcrunch.com/2026/06/30/podcasting-platform-riverside-enters-the-newsletter-publishing-game/
author:
- '[[Ivan Mehta]]'
published: '2026-06-30'
created: '2026-07-01'
description: Users will be able use AI to create newsletters based on their recordings.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fd93a14ef0eaaad2
manifest_dates:
- '2026-07-01'
source_type: news_media
tldr: Riverside 推出 AI 新闻通讯功能，可将录音自动转为新闻信
objective_summary: Riverside 在 2026 年 6 月为其录制工具推出 AI 新闻通讯功能，用户可将现有播客和视频录音自动转为新闻信并从应用内直接发送。同时推出了多摄像头录制、远程嘉宾、AI
  剪辑、社交内容生成和 AI 视频增强等更新。该公司累计融资超 6000 万美元。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Riverside
  - Mailchimp
  - Substack
  - Beehiiv
  - Ghost
  - Mastodon
  - TechCrunch
  technologies:
  - AI
  key_people:
  - Nadav Keyson
key_logic_flow:
- Riverside 为其视频和播客录制工具新增新闻通讯功能，用户可通过 AI 将现有录音自动转为新闻信并从应用内直接发送。
- Riverside 联合创始人兼 CEO Nadav Keyson 表示，该功能旨在帮助用户利用已有的口语内容生成新闻信，而非直接与 Mailchimp、Substack、Beehiiv
  等平台竞争。
- Riverside 还更新了录制套件，支持多摄像头录制和添加远程嘉宾。
- 新 AI 功能包括录音完成后自动生成剪辑初稿、为社交媒体平台创建钩子和内容，以及基于对话视频播客训练的 AI 视频增强功能（改善光线、深度和清晰度）。
- Riverside 累计融资超过 6000 万美元。与此同时，Substack 于 3 月推出内置录音工作室，Beehiiv 于 4 月涉足播客，Mastodon
  于 6 月宣布允许用户将帖子发布为新闻信。
extract_result: success
impact_score:
  score: 3.5
  reason: Riverside 为播客录制工具新增 AI 新闻通讯转换功能，属于产品层面的功能迭代，而非技术范式突破。该功能的核心价值在于降低播客创作者的内容复用门槛（语音→文字），但AI语音转文字和内容摘要本身已是成熟技术，缺乏独到的技术创新点。短期来看，这是播客/SaaS
    工具赛道的一次常规功能扩展，不会对行业格局产生显著冲击。Substack 和 Beehiiv 此前已双向渗透，Riverside 的入局只是验证了跨品类融合趋势，并未改变局部竞争态势。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: AI 从录音自动生成新闻信的质量是否足够好，以及多摄像头录制和远程嘉宾功能的实际可用性
hype_assessment:
  level: low
  reason: 文章没有使用 '颠覆'、'革命性' 等夸张 PR 词汇。Riverside CEO 明确表示不直接与 Substack/Beehiiv 竞争，而是定位为现有用户的增值功能，表述克制务实。AI
    增强、自动剪辑等功能描述也较为具体（训练于对话视频播客、改善光线深度清晰度），没有过度包装。
information_entropy: medium
domain_disruption:
  technical_innovation: 无本质技术突破。AI 驱动的语音转新闻通讯功能基于成熟的 ASR 和 NLG 技术组合，AI 视频增强（改善光线、深度、清晰度）训练于对话视频播客领域数据有一定工程价值，但属于渐进式优化而非架构级创新。
  business_model: Riverside 通过内置新闻通讯功能延长用户留存周期、提升单用户 ARPU，反映了 SaaS 工具从单一垂直工具向 '内容创作全链路平台'
    演进的趋势。但与 Substack/Beehiiv 的相互渗透本质上是对存量创作者的争夺，并未创造新的商业模式。
engineering_complexity: production_ready
compound_value:
  score: 6.8
  reason: Riverside 通过 AI 新闻通讯转换功能拓展了内容创作工作流，核心价值在于将口语内容自动转化为文字形态，提升了已有录制资产的复用效率。但该功能本身技术门槛不高，Mailchimp/Substack/Beehiiv
    等平台也可反向集成 AI 转录。真正具有复利效应的是其基于对话视频播客训练的 AI 视频增强模型——随着平台上录制内容增多，训练数据持续积累，形成数据飞轮效应，模型质量会随时间提升并成为差异化壁垒。叠加多机位录制、远程嘉宾、AI
    剪辑等功能，Riverside 正从单一录制工具向内容创作 OS 演进，用户切换成本逐步升高。然而，该赛道正处于平台功能趋同阶段（Substack 加录音、Beehiiv
    加播客），竞争格局未定，长期复利效应需持续观察用户留存和 AI 模型的代际差距。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Riverside
- 内容创作者与独立播客主
- AI 视频增强技术栈供应商
competitive_casualty:
- Substack
- Beehiiv
- Mailchimp
- 单一功能 AI 内容重制工具（如通用转录转文字 SaaS）
market_opportunities:
- 创业团队可开发跨平台内容自动适配工具，实现播客/视频内容一键转化为文字新闻信、社交帖文等多格式发布，抓住创作者多平台分发的刚需痛点
- 内容创作者可借助 Riverside 等平台的 AI 功能，建立'一次录制、多端分发'的高效内容生产流程，大幅降低文字内容创作门槛，提升内容产出效率
- 面向企业客户的定制化 AI 内容重制服务存在机会，帮助品牌方将线上研讨会、播客访谈等口语内容批量转化为高质量的邮件新闻信和社媒内容
risk_matrix:
  regulatory: AI 生成内容的披露义务日益严格，多国监管部门可能要求明确标注 AI 辅助生成的新闻信内容；邮件营销相关的 CAN-SPAM 和 GDPR
    合规责任由发送方承担，Riverside 作为平台方需建立完善的合规保障机制
  technological: AI 语音转文字和内容生成的质量仍有限制，对于专业深度内容的准确性和风格一致性可能无法满足高要求用户；大语言模型能力的快速迭代可能使
    Riverside 当前的 AI 功能在 6-12 个月内被通用模型的能力所覆盖，形成技术替代风险
  competitive: Substack、Beehiiv、Mastodon 等平台正双向渗透（Substack 推出录音室、Beehiiv 涉足播客），Riverside
    面临来自成熟内容平台的生态挤压；其融资规模（6000 万美元）与 Mailchimp（被 Intuit 以 120 亿美元收购）、Substack（估值超
    6.5 亿美元）等竞品相比存在数量级差距，资源竞争处于劣势
  ethical: AI 将口语内容自动转为文字新闻信时可能丢失语境、语气和细微表达，产生内容曲解或断章取义的风险；播客嘉宾的内容被自动转化为新闻信并分发的知情同意问题可能引发隐私争议
  additional:
  - 平台依赖关系风险：Riverside 作为中间层工具，其 AI 新闻信功能高度依赖底层 LLM 服务商的 API 可用性和定价策略，存在成本不可控和被上游厂商挤压的风险
  - 用户粘性风险：新闻信订阅者实际上归属于发送者而非 Riverside 平台，用户若迁移到其他录制工具或新闻信平台，Riverside 缺乏锁定效应
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

Video and podcast recording tool maker Riverside is giving its users a new way to reach their audiences: newsletters.

Riverside isn’t aiming to directly take on established newsletter platforms like Mailchimp, Substack, Beehiiv, or Ghost, however. Instead, recognizing that its userbase already generates a lot of content, the company is giving the users of its recording tools an AI tool to turn their existing videos and podcasts into newsletters, and send them directly from within its app. Users can also create and send newsletters from scratch without using the AI conversion feature.

“Substack and Beehiiv start you at a blank page. But our creators and business customers are already producing rich, information-dense spoken content on Riverside. For most people, speaking is easier and more natural than writing from scratch, and the ideas are already there, in the conversation. So instead of asking them to start over in a separate tool, we help them turn a recording they’ve already made into newsletter-ready content with far less effort,” Riverside’s co-founder and CEO Nadav Keyson told TechCrunch.

The company is also updating its recording suite to support multi-camera recording setups. It’s also giving users the ability to add remote guests to recordings.

The update brings new AI features as well. Users can use AI to draft a first cut of a recording as soon as it’s finished, and the assistant can also create hooks and content for various social media platforms. The company is also adding an AI video enhancement feature, trained on conversational video podcasts, that it says can improve lighting, depth, and sharpness of recordings.

Riverside, which has raised over $60 million in funding, joins a host of platforms that have been trying to enter alternative publishing avenues to either diversify or expand their revenue streams. For instance, Substack in March launched a built-in recording studio that competes directly with Riverside, and in April, newsletter platform Beehiiv ventured into podcasting as well. In June, social network Mastodon said that it will allow users to publish their posts as newsletters.