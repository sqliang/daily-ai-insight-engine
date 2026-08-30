---
title: Google Discover is getting an AI chatbot-tuned feed
source: https://www.theverge.com/tech/983088/google-discover-ai-chatbot-feed
author:
- '[[Emma Roth]]'
published: '2026-08-20'
created: '2026-08-21'
manifest_dates:
- '2026-08-21'
description: Google will soon allow you to customize your Discover feed by describing
  what you want to see. The new feature, rolling out to the Google app in the "coming
  days," will use AI to automatically tweak your feed and "remember" your preferences
  for future visits. You'll find the option within the three-dot menu on your [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bdb698ec663c3ddc
source_type: news_media
tldr: Google 即将在 Google app 中推出基于 AI 聊天的 Discover 信息流定制功能，用户可通过描述偏好让 AI 调整并记住设置。同时更新了
  Google News 音频简报个性化与 Preferred Sources 快捷按钮。
objective_summary: Google 宣布将在数天内向 Google app 用户推出 Discover 信息流的 AI 定制功能。用户通过三点菜单进入聊天式界面描述想看的内容，AI
  会自动调整并记住偏好，可点击“刷新你的信息流”使改动生效。此外 Google 还宣布为 Android 版 Google News 提供每日音频简报的个性化能力，并允许发布商在网站上放置可交互的
  Preferred Sources 按钮，让读者无需离开页面即可添加偏好媒体。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Google
  - YouTube
  - Instagram
  - Bluesky
  - X
  technologies:
  - AI
  - AI Overviews
  - AI Mode
  key_people: []
key_logic_flow:
- Google 将在数天内向 Google app 推出基于 AI 的 Discover 信息流定制功能，用户可以直接描述想看的内容。
- 用户在 Discover 的三点菜单中找到该选项，进入聊天式界面描述偏好，AI 会确认选择并列出将要优先展示的内容类型。
- 如果 AI 理解有偏差，用户可以补充更多信息，然后点击“刷新你的信息流”让改动立即生效。
- 该功能与 YouTube、Instagram、Bluesky、X 等社交应用此前加入的 AI 信息流定制方式类似。
- Google 同时宣布为 Android 版 Google News 应用新增每日音频简报的个性化功能。
- Google 更新了 Preferred Sources 功能，发布商可在网站上放置交互按钮，让读者一键将媒体加入偏好列表，适用于 Top stories、AI
  Overviews 与 AI Mode 板块。
object_mentions:
- object_type: product
  name: Google Discover
  canonical_name: Google Discover
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Google 即将允许用户通过在聊天式界面描述想看的内容，来定制 Discover 信息流。
  - 用户可以在三点菜单中找到该选项，AI 会自动调整信息流并记住偏好用于后续访问。
  article_id: bdb698ec663c3ddc
- object_type: product
  name: Google News
  canonical_name: Google News
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Google 还宣布为 Android 版 Google News 应用新增每日音频简报的个性化功能。
  article_id: bdb698ec663c3ddc
- object_type: product
  name: Preferred Sources
  canonical_name: Preferred Sources
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Google 更新了 Preferred Sources 功能，发布商可在网站上放置交互按钮，让读者无需离开页面即可添加偏好媒体。
  - 该功能适用于搜索的 Top stories、AI Overviews 和 AI Mode 板块，帮助用户看到更多喜爱的媒体内容。
  article_id: bdb698ec663c3ddc
extract_result: success
impact_score:
  score: 4.5
  reason: 这是 Google 将对话式 AI 能力下沉到核心消费产品 Discover 信息流的功能迭代，属于应用层落地而非范式转移。类似聊天式信息流定制已在
    YouTube、Instagram、Bluesky、X 等平台出现，Google 属于跟进者而非开创者；短期内不改变竞争格局，但凭借 Discover 的亿级用户规模与搜索数据底座，会对个性化内容分发的体验和效率产生可感知影响，故评为中等偏下分。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: AI 偏好记忆对信息流排序算法的实际影响，以及发布商 Preferred Sources 按钮能否真正改变内容分发权重
hype_assessment:
  level: low
  reason: 文章基于 Google 官方演示与功能说明，描述的是具体、数天内即将上线的产品功能，未出现"颠覆""革命性"等 PR 滥用词汇；功能本质是将已有的聊天式偏好设置模式迁移到
    Discover，宣传口径与实际能力基本一致，水分较低。
information_entropy: medium
domain_disruption:
  technical_innovation: 本质是 LLM 驱动的用户偏好理解与信息流重排序：通过聊天式界面采集偏好、记忆设置并支持"刷新信息流"即时生效，将自然语言偏好注入
    Discover 推荐管线。技术上属于现有大模型能力的工程化应用集成，而非新的模型架构或检索范式突破，创新点在交互范式而非底层技术。
  business_model: 强化 Google 搜索与 Discover 生态的广告变现与用户停留时长；Preferred Sources 按钮让发布商可在自己网站上一键引导读者加入偏好列表，形成站外到站内的流量闭环，可能改变媒体获取忠实读者的方式，并影响
    AI Overviews/AI Mode 等板块的内容分发权重分配。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 这是 Google 在存量产品（Discover 信息流）上叠加 AI 聊天定制能力，本质是应用层功能迭代，未创造新市场或新基础设施。但从资本视角看，它强化了
    Google 的内容分发数据飞轮：用户用自然语言描述偏好 → AI 调优信息流 → 停留时长与使用频率提升 → 更多广告库存与模型训练信号，具备跨时间复利。叠加
    Preferred Sources 按钮，Google 把'读者—发布商'双边关系进一步收拢到自家分发体系内，护城河价值真实。但该价值高度绑定 Google
    生态内部，3-5 年后大概率只是 Google 整体护城河的一环而非独立行业基石，且该范式已被 YouTube/Instagram/X 等同步跟进，差异化优势有限，因此复利强度中等偏上而非顶尖。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- Google
- Gemini
- 大型新闻出版机构
- Google 广告主
competitive_casualty:
- 独立新闻聚合应用（Flipboard/Feedly 等）
- 小型长尾发布商
- 无同等数据规模的个性化推荐平台
market_opportunities:
- 面向内容平台的创业者可将"对话式信息流定制"抽象为可复用的个性化 UX 组件，为中小型内容 App 提供 AI 偏好管理 SDK，降低普通用户理解与调校算法的门槛
- 媒体与发布商应尽快在站内集成 Google 新推出的 Preferred Sources 交互按钮，并研发配套的"一键添加偏好媒体"工具组件，抢占 AI Overviews
  与 AI Mode 中的品牌曝光与流量分配红利
- 关注 AI 信息流生态的从业者可布局跨平台 AI 偏好管理助手，帮助用户在 Google/YouTube/Instagram/X 等之间统一同步内容偏好，或为创作者提供内容在各
  AI 信息流中可见度的监测与分析工具
risk_matrix:
  regulatory: AI 信息流个性化高度依赖用户浏览历史与行为画像，面临 GDPR 与欧盟《数字服务法》对推荐系统透明度和画像处理的审查压力；Google
    需就 AI"记忆"偏好功能的数据使用方式、存储边界与可解释性作出充分披露，否则存在隐私合规诉讼风险
  technological: 对话式偏好定制可能仅是过渡性交互形态，文章自承 AI 理解易出现偏差、需用户二次纠正，若体验不佳可能被更隐式的行为学习所替代；且该功能为增量改进，技术护城河有限，极易被其他平台复制
  competitive: Google Discover 在 AI 信息流定制上明显晚于 YouTube、Instagram、Bluesky、X 等社交平台，属于追赶型布局，若落地体验不及预期，将加速年轻用户向新兴
    AI 聚合阅读器和短视频算法转移
  ethical: 按用户偏好深度定制新闻信息流会加剧信息茧房与回声室效应，可能放大观点极化；AI 对内容优先级的判定若隐含偏见，将系统性抬高或压低特定声音，进而影响公共信息环境的多元性
  additional:
  - 发布商对 Google 算法的依赖进一步加深：Preferred Sources 按钮使媒体流量分配更受 Google 推荐逻辑摆布，形成平台锁定效应
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: Google Discover
  canonical_name: Google Discover
  url: https://www.google.com/discover
  positioning: Google 面向移动端的信息流推荐产品，基于用户在搜索与谷歌应用中的活动推荐文章；AI 定制功能将允许用户用自然语言描述偏好，使个性化进一步深化。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Google app 用户
  - 希望用自然语言掌控信息流内容的移动端读者
  product_signal: 新增聊天式 AI 定制界面，用户通过描述偏好即可调整信息流，AI 会确认内容类型并记住设置，点击“刷新你的信息流”即可生效。
  market_signal: 该功能与 YouTube、Instagram、Bluesky、X 等社交应用的 AI 信息流定制方式类似，反映行业向生成式个性化推荐方向趋同。
  differentiation: 依托搜索历史与谷歌应用生态数据，Discover 的 AI 定制拥有更丰富的用户意图信号，且直接内置于现有高流量信息流产品中。
  watch_reason: Google Discover 拥有庞大的移动端用户基数，AI 聊天式信息流定制若顺利落地，可能成为生成式 AI 重塑信息消费入口的标杆案例，其实际采用率与内容生态影响值得持续跟踪。
  risk_notes:
  - AI 定制可能强化信息茧房效应，用户只看到符合既有偏好的内容，长期或损害信息多样性并引发信任争议。
  - 该功能仅面向 Google app 陆续推出，实际覆盖范围、语言支持与推荐透明度尚待验证。
  score: 7.0
  article_ids:
  - bdb698ec663c3ddc
  evidence_snippets:
  - Google 即将允许用户通过在聊天式界面描述想看的内容，来定制 Discover 信息流。
  - 用户可以在三点菜单中找到该选项，AI 会自动调整信息流并记住偏好用于后续访问。
- object_type: product
  name: Google News
  canonical_name: Google News
  url: https://news.google.com
  positioning: Google 面向 Android 用户的新闻聚合应用，汇聚多源资讯并推出每日音频简报，通过个性化能力提升场景化信息消费体验。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Android 版 Google News 用户
  - 偏好通过音频获取新闻的移动端用户
  product_signal: 新增每日音频简报的个性化功能，用户可按偏好定制音频新闻内容，扩展语音与通勤等场景的资讯获取方式。
  market_signal: 音频简报个性化显示 Google 在移动资讯分发中加码语音场景，是新闻产品向多元消费形态延伸的市场动作。
  differentiation: null
  watch_reason: Google News 音频简报个性化是新闻产品向语音场景延伸的信号，作为 Google 新闻生态的组成部分，其进展可反映公司对资讯分发多元化的投入方向与节奏。
  risk_notes:
  - 音频简报个性化目前仅面向 Android 版应用，iOS 与桌面端覆盖情况未明确，功能落地范围有限。
  score: 4.0
  article_ids:
  - bdb698ec663c3ddc
  evidence_snippets:
  - Google 还宣布为 Android 版 Google News 应用新增每日音频简报的个性化功能。
- object_type: product
  name: Preferred Sources
  canonical_name: Preferred Sources
  url: null
  positioning: Google 搜索生态中的媒体偏好功能，帮助用户看到更多喜爱媒体的内容，并通过网页内交互按钮让发布商直接沉淀偏好读者。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 搜索用户与新闻读者
  - 希望被优先推荐给读者的发布商与媒体机构
  product_signal: 更新后发布商可在网站放置交互式 Preferred Sources 按钮，读者点击即可添加偏好媒体，无需离开页面，覆盖 Top
    stories、AI Overviews 与 AI Mode 板块。
  market_signal: Google 将媒体偏好选择入口下沉到发布商网站，属于搜索生态与内容生态双向强化的分发策略，直接影响 AI 搜索时代的媒体流量分配。
  differentiation: 相比传统订阅或关注机制，该功能把偏好添加入口搬到发布商站点，并在 AI Overviews 与 AI Mode 等生成式搜索场景中生效，形成从内容到推荐的闭环。
  watch_reason: Preferred Sources 直接切入 AI 搜索时代的媒体流量分配，其按钮机制能否成为发布商获取忠实读者的标准入口，关系到生成式搜索下内容生态的利益分配，值得持续跟踪。
  risk_notes:
  - 机制依赖发布商主动部署交互按钮，中小型媒体可能因接入意愿或技术成本导致覆盖有限。
  - 该功能在 AI Overviews 与 AI Mode 中的推荐权重与透明度尚未披露，实际效果有待验证。
  score: 5.0
  article_ids:
  - bdb698ec663c3ddc
  evidence_snippets:
  - Google 更新了 Preferred Sources 功能，发布商可在网站上放置交互按钮，让读者无需离开页面即可添加偏好媒体。
  - 该功能适用于搜索的 Top stories、AI Overviews 和 AI Mode 板块，帮助用户看到更多喜爱的媒体内容。
---

Google will soon allow you to customize your Discover feed by describing what you want to see. The new feature, rolling out to the Google app in the “coming days,” will use AI to automatically tweak your feed and “remember” your preferences for future visits.

# Google Discover is getting an AI chatbot-tuned feed

You’ll soon be able to describe what you want to see in your Google Discover feed.

You’ll soon be able to describe what you want to see in your Google Discover feed.

You’ll find the option within the three-dot menu on your Discover feed. As shown in a video shared by Google, tapping the feature will open a chatbot-style interface, where you’ll be able to describe your preferences. The chatbot will confirm your choices and lay out the types of content it will prioritize, but you’ll also have the option to add more information if it doesn’t get it quite right. From there, you can hit “Refresh your feed” for the changes to take effect.

This might make it easier to control what you see in your Discover feed, which serves up recommended articles based on your activity across Google’s search engine and apps. Aside from Google Discover, several social media apps have added ways to customize your feeds with AI, including YouTube, Instagram, Bluesky, and X.

Google announced a couple of other changes as well, including the ability to personalize daily audio briefings in the Google News app on Android.

There’s also an update to Preferred Sources, a feature that lets you see more of your favorite outlets across Search’s “top stories” section, AI Overviews, and AI Mode. With the change, publishers can place an interactive “Preferred Sources” button on their sites, which readers can select to quickly add it to their list without navigating away from the webpage.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.