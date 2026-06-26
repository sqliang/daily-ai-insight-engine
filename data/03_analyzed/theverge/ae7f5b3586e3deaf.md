---
title: Google is finally opening the Play Store to outside payments
source: https://www.theverge.com/policy/956296/google-play-app-store-alternative-billing-fee-antitrust
author:
- '[[Richard Lawler]]'
published: '2026-06-24'
created: '2026-06-25'
description: While the court still hasn't signed off on the massive settlement resolving
  Epic's antitrust lawsuit against Google for having a monopoly over Android's app
  store with Google Play, the tech giant says it will start rolling out changes to
  the way it handles billing for developers worldwide. As announced in March, the
  flat 30 percent [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ae7f5b3586e3deaf
source_type: news_media
tldr: 谷歌宣布开放Play Store外部支付，逐步取消30%固定抽成
objective_summary: 谷歌在Epic反垄断诉讼和解背景下，宣布将逐步推出Play Store计费变更。固定30%抽成被分层费用取代，费率取决于用户首次安装时间、开发者收入及是否使用谷歌计费系统。年收入超百万美元的应用新购抽成降至20%，订阅降至10%。部分地区2026年9月生效，全球最晚2027年9月完成。
event_type: policy_and_safety
epistemic_status: pr_statement
entities:
  companies:
  - Google
  - Epic
  technologies: []
  key_people: []
key_logic_flow:
- 谷歌宣布将逐步取消Play Store固定30%抽成制度，改用分层费用结构，这是Epic反垄断诉讼和解后的调整。
- 新费率取决于三个因素：用户首次安装时间（新老用户区分）、开发者年收入水平、是否使用Google Play计费系统。
- 年收入超百万美元的应用：使用外部支付时新购抽成20%，订阅抽成10%。
- 谷歌推出Games Level Up和Apps Experience计划，跨平台运行且满足性能基准的优质应用可享更低抽成。
- 部分地区政策变更于2026年9月底生效，2027年9月30日后推广至全球范围。
extract_result: success
impact_score:
  score: 5.5
  reason: 该事件是Epic反垄断诉讼和解的直接产物，标志着移动应用分发领域标志性的'30%苹果税/谷歌税'开始松动。对AI行业而言，大量AI工具类应用（聊天助手、图像生成、生产力工具）依赖移动端分发，分层费率降低直接改变AI创业公司的获客成本结构。但另一方面，该政策是被动调整而非主动创新，费率仍保留20%/10%的分层抽成，且全球落地需至2027年才完成，短期冲击力有限。不属于范式转移级别，但足以改变局部竞争格局——尤其是对依赖应用内购的AI应用开发者。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 分层费率体系的实际成本和合规复杂度，以及外部支付接入是否真正降低开发者负担
hype_assessment:
  level: medium
  reason: 标题使用'finally opening'和'30%抽成正在消失'等表述具有一定叙事包装色彩。30%抽成并非完全消失，而是被更复杂的分层费用替代（20%/10%+外部支付附加费），且Games
    Level Up等计划仅适用于满足特定门槛的优质应用。实际变革力度低于标题暗示的'彻底开放'，存在一定过度包装。
information_entropy: high
domain_disruption:
  technical_innovation: 无
  business_model: 从固定30%抽成转向基于用户首次安装时间、开发者收入水平、是否使用谷歌计费系统的分层费率结构，并允许外部支付和网站直连。这重塑了移动应用分发的商业模式，降低了大型开发者的渠道成本，但对中小开发者实际利好有限。对AI应用生态而言，移动端分发成本下降可能加速AI原生应用的C端渗透。
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 事件本质是反垄断诉讼和解下的被动政策调整，而非主动构建技术壁垒或网络效应。开放外部支付和降低抽成确实降低了AI应用（尤其是移动端AI Agent、AI游戏等）的分发成本，开发者能留存更多收入用于再投资。但这种改善是一次性结构性的，没有叠加增强效应——开发者省下的抽成费用并不会随时间指数级增长，也不会形成数据或用户锁定。长期看，若谷歌后续通过新条款（如Apps
    Experience/Games Level Up）重新建立对优质AI应用的筛选控制权，可能创造新的平台依赖，但目前尚未形成明显的复利引擎。因此评分为4.5，属于细分赛道基础设施的潜力区间，但需持续观察谷歌是否会将API访问、AI模型托管等能力与费率挂钩。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Epic Games
- Spotify
- Netflix
- 中型AI应用开发者
- 替代支付服务商（如Braintree、Stripe）
competitive_casualty:
- Apple App Store（反垄断压力加剧）
- Google Play Store收入
- 小型支付中间商（被大支付商替代）
market_opportunities:
- 第三方支付服务商可抓住Google Play开放外部支付的窗口期，推出针对移动应用内购的替代计费解决方案，争夺每年数十亿美元的交易手续费市场
- 年收入超百万美元的应用开发者应主动评估迁移至外部支付系统的成本收益，通过20%抽成（vs 30%）和10%订阅抽成获得显著利润提升
- 可围绕Google Play新费率结构（首次安装时间、年收入档位、计费系统选择三因素模型）开发费率优化SaaS工具，帮助开发者自动计算最优支付路径
risk_matrix:
  regulatory: 法院尚未正式签署Epic和解协议，存在判决被驳回或附加条件的可能性；全球各司法管辖区（欧盟DMA、英国、印度）可能进一步施压要求更彻底变革，政策落地节奏存在不确定性
  technological: 无
  competitive: Apple App Store尚未同步降低30%抽成比例，谷歌此举将加剧跨平台开发者的不公平感，可能倒逼Apple跟进并引发新一轮价格战；同时谷歌的'Apps
    Experience'优质应用折扣计划可能导致头部应用享受更低费率而中小开发者被边缘化
  ethical: 外部支付系统可能引入新的数据隐私隐患——第三方支付平台的数据保护标准参差不齐，用户支付信息可能在多个实体间流转，增加数据泄露面；另需关注外部支付对儿童应用内购的家长管控机制可能弱化
  additional:
  - 开发者需投入工程资源适配多套支付系统（Google Play计费 + 外部支付 + 网页直连），增加技术维护成本和用户体验碎片化风险
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
---

While the court still hasn’t signed off on the massive settlement resolving Epic’s antitrust lawsuit against Google for having a monopoly over Android’s app store with Google Play, the tech giant says it will start rolling out changes to the way it handles billing for developers worldwide. As announced in March, the flat 30 percent billing fee is being replaced by “lower, decoupled fees” that partially decouple the billing and the app store.

# Google is finally opening the Play Store to outside payments

The 30 percent app store rate is going away, and now you might pay developers directly for Android apps.

The 30 percent app store rate is going away, and now you might pay developers directly for Android apps.

How much of a cut Google will take from transactions now depends on whether it’s for a user whose first install came before or after the new structure, how much a developer has earned, and whether or not the developer uses Google Play’s billing system with its 5 percent additional fee, instead of an alternative system or linking to their own website.

For apps that make over a million dollars annually, that will be 20 percent for new in-app purchases and 10 percent for subscriptions. However Google has also announced Games Level Up and Apps Experience programs for “exceptional” and “premium ” experiences that meet its guidelines by working across platforms (like tablets, smart TVs, or Android Auto), meeting benchmarks for memory usage and crash rates, and supporting features it recommends (like cloud saves or phishing-resistant sign-ins) to qualify for a lower rate on both new and existing installs.

Other program changes will go into effect in some areas at the end of September, at the end of the year, before rolling out to the rest of the world after September 30th, 2027.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.