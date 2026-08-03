---
title: After backlash, Meta pauses plan to ‘rate limit’ its smart glasses
source: https://www.theverge.com/tech/970970/after-backlash-meta-pauses-plan-to-rate-limit-its-smart-glasses
author:
- '[[Sean Hollister]]'
published: '2026-07-24'
created: '2026-07-25'
manifest_dates:
- '2026-07-25'
- '2026-07-26'
description: Remember when Meta was planning to charge a $20 monthly subscription
  fee for the smart glasses feature that lets people hear each other more clearly
  - even though that feature runs locally on your glasses and doesn't require the
  cloud? Meta has paused those plans, spokesperson Tyler Yee confirms to The Verge.
  The company is [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c7eccabed7febc7e
source_type: news_media
tldr: Meta 在公众强烈反对后暂停了为其 Ray-Ban 智能眼镜 Conversation Focus 功能设置订阅费和速率限制的计划，该功能其实运行在设备本地、无需云端支持；但
  Meta 仍打算未来对某些高级功能收取订阅费。
objective_summary: Meta 曾计划为 Ray-Ban 智能眼镜的 Conversation Focus 功能收取每月 20 美元的订阅费并设置每月
  15 小时的使用上限，但该功能实际运行在设备本地、不依赖云端。在遭到公众强烈反对后，Meta 发言人 Tyler Yee 向 The Verge 确认暂停该订阅测试，Conversation
  Focus 将继续通过早期访问计划免费提供。不过 Meta 明确表示不会放弃对高级功能采取订阅制的长期策略。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Meta
  - Ray-Ban
  technologies:
  - Conversation Focus
  key_people:
  - Tyler Yee
key_logic_flow:
- Meta 原本计划为 Ray-Ban 智能眼镜的 Conversation Focus 功能收取每月 20 美元订阅费，并设置每月 15 小时的速率限制。
- The Verge 通过断开眼镜网络连接验证了 Conversation Focus 功能完全在设备本地运行，不依赖云端服务。
- 该订阅计划在遭到公众强烈反对后，Meta 发言人 Tyler Yee 确认已暂停该功能的订阅测试。
- Conversation Focus 将继续通过早期访问计划免费提供，Meta 表示正在探索更好的方案。
- Meta 明确表示不会放弃订阅制策略，未来部分高级功能仍将采用订阅收费模式。
- Meta 声称订阅收费的目的是补贴硬件价格，使智能眼镜能以更低价格出售给更多用户。
object_mentions:
- object_type: product
  name: Meta Ray-Ban Smart Glasses
  canonical_name: Meta Ray-Ban Smart Glasses
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Meta 原计划为其 Ray-Ban 智能眼镜的 Conversation Focus 功能收取每月 20 美元的订阅费用。
  - The Verge 断开眼镜网络连接后验证该功能依然正常工作，证明其完全在设备本地运行。
  - Meta 表示以可承受的价格销售硬件是为了让 AI 眼镜覆盖更多人，订阅费用用于补贴硬件成本。
  article_id: c7eccabed7febc7e
- object_type: product
  name: Conversation Focus
  canonical_name: Conversation Focus
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Conversation Focus 是一项让用户更清晰听到对方说话的无障碍功能，运行在眼镜本地设备上。
  - 该功能在遭遇公众反对后暂停了订阅测试，目前仍通过早期访问计划免费提供给测试用户。
  - Meta 称正在为 Conversation Focus 探索更好的方案，但未承诺取消未来的速率限制。
  article_id: c7eccabed7febc7e
extract_result: success
impact_score:
  score: 3.5
  reason: 该事件本质是Meta智能眼镜部门的一次定价策略失误与危机公关回调，而非技术突破或行业范式转移。事件揭示了AI可穿戴设备厂商在本地化功能上推行订阅制的商业模式探索，以及消费者对此类做法的抵触。短期内对竞争格局影响有限，但作为案例信号（试图对纯本地功能收费并伪装成云成本压力）值得关注。评级3.5分：属于局部商业决策失误，行业冲击力中等偏低，未改变AI眼镜赛道的竞争格局。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: Meta 试图对纯本地运行的设备端功能收费，且此前用'速率限制'话术掩盖功能无需云端支持的事实
hype_assessment:
  level: low
  reason: 本文为 The Verge 的客观新闻报道，记者通过断开眼镜联网的实地测试验证了功能本地化运行的事实，无概念炒作或 PR 包装。文章内容基于 Meta
    官方回应和可复现的技术验证，属于扎实的科技报道。
information_entropy: medium
domain_disruption:
  technical_innovation: 无。Conversation Focus 功能本身并非新技术突破，本文焦点在于该功能的运行架构（设备本地推理）与收费策略之间的矛盾，而非技术本身的创新。
  business_model: 事件揭示了 AI 可穿戴设备领域的关键商业模式矛盾：设备端本地处理的功能缺乏持续运营成本，厂商难以用'成本转嫁'逻辑支撑订阅收费；Meta
    试图通过硬件补贴+高级功能订阅的复合模式来降低设备售价并获取经常性收入，但消费者对纯本地功能收费存在天然的抵触心理。这一博弈将是未来 AI 眼镜/可穿戴设备商业化路径的重要观察案例。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: Meta 暂停 Conversation Focus 订阅测试表面上是战术让步，但实质是其在智能眼镜上推行'硬件补贴+订阅收费'模型的战略试探受挫。从资本视角看，核心信号在于
    Meta 明确表示'不会放弃订阅制'，说明该公司正将 Ray-Ban 智能眼镜定位为类似打印机/游戏主机的耗材型商业模式——低价硬件获客、高价功能持续收费。这一模型一旦跑通，将产生极强的复利效应（硬件锁定
    + 订阅 ARPU 持续提升 + 用户迁移成本高企）。然而消费者对本地功能收费的强烈抵制，以及 The Verge 拆穿该功能无需云端支持的事实，暴露出 Meta
    在定价权与用户信任之间的深层矛盾。该事件为整个可穿戴 AI 赛道提供了重要的商业模式参照系：方向正确，但执行路径仍需迭代，评分 6.5 反映了中期潜力与短期不确定性并存。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- Meta
- EssilorLuxottica (Ray-Ban)
competitive_casualty:
- 独立智能眼镜初创公司
- 纯硬件销售模式的 AR 厂商
market_opportunities:
- 智能眼镜厂商可借鉴 Meta 的硬件补贴策略，通过免费提供核心本地功能来扩大用户基础，再以高级功能订阅作为收入来源
- 对 Meta 订阅计划的公众反弹为竞争品牌创造了营销窗口，可在产品宣传中强调透明定价和本地功能免费使用以争取用户信任
- 端侧 AI 功能作为差异化卖点正在显现价值，开发者可关注面向智能眼镜的本地 AI 应用生态和功能插件市场
risk_matrix:
  regulatory: 消费者保护监管风险：为纯本地运行的功能设置订阅费可能被认定为不公平或欺骗性商业行为，若 Meta 或其他厂商采取类似策略，可能面临 FTC
    或欧盟消费者权益机构的调查
  technological: 端侧 AI 能力提升将削弱云端功能的收费理由——随着芯片和模型持续进步，更多功能可在本地运行，消费者对订阅收费的接受度会进一步降低
  competitive: Apple、Google、Samsung 等潜在竞争对手可能利用 Meta 的失误，在推出同类产品时强调本地功能免费、无使用上限，形成对
    Meta 的竞争挤压
  ethical: 为辅助类功能（如 Conversation Focus 这类提升无障碍体验的特性）设置付费墙可能引发公平性争议，特别是当该功能不依赖云端基础设施时，用户会质疑收费的合理性
  additional:
  - 消费者信任侵蚀：Meta 的订阅尝试已引发公众强烈反弹，即使暂停计划，品牌信任和在智能眼镜市场的口碑已受到损害
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: Meta Ray-Ban Smart Glasses
  canonical_name: Meta Ray-Ban Smart Glasses
  url: null
  positioning: Meta 旗下的 AI 智能眼镜产品线，集成摄像头、扬声器和 AI 助手，以平价硬件策略覆盖更多用户，并通过订阅模式为高级功能变现。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 眼镜消费者
  - 智能穿戴设备用户
  - 无障碍功能需求者
  product_signal: Conversation Focus 功能被证实完全在设备本地运行而非依赖云端，但 Meta 仍曾计划对其设置订阅费和速率限制，引发公众强烈反对。
  market_signal: Meta 暂停了 Conversation Focus 的订阅测试并继续通过早期访问计划免费提供，但明确表示不会放弃高级功能订阅制的长期策略。
  differentiation: 以平价硬件价格吸引用户，通过订阅费补贴硬件成本；但将本地运行功能收费的做法引发了用户信任危机。
  watch_reason: Meta 在硬件补贴与订阅变现之间的策略博弈代表了 AI 硬件行业的典型商业模式挑战，其决策走向将影响整个智能眼镜市场的定价范式与用户预期。
  risk_notes:
  - 对设备本地运行功能收取订阅费的尝试可能严重损害用户信任和品牌声誉。
  - Meta 未承诺放弃速率限制，未来高级功能付费策略仍存较大不确定性。
  score: 7.0
  article_ids:
  - c7eccabed7febc7e
  evidence_snippets:
  - Meta 原计划为其 Ray-Ban 智能眼镜的 Conversation Focus 功能收取每月 20 美元的订阅费用。
  - The Verge 断开眼镜网络连接后验证该功能依然正常工作，证明其完全在设备本地运行。
  - Meta 表示以可承受的价格销售硬件是为了让 AI 眼镜覆盖更多人，订阅费用用于补贴硬件成本。
- object_type: product
  name: Conversation Focus
  canonical_name: Conversation Focus
  url: null
  positioning: Meta Ray-Ban 智能眼镜上的无障碍 AI 功能，利用设备端处理让用户更清晰听到对方说话，目前通过早期访问计划免费提供。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Ray-Ban 智能眼镜用户
  - 有听觉辅助需求的用户
  - 早期测试计划参与者
  product_signal: 该功能完全在设备本地运行、不依赖云端服务，但 Meta 曾计划对其收取每月 20 美元订阅费并设置 15 小时使用上限。
  market_signal: 在遭到公众强烈反对后 Meta 暂停了收费测试并继续免费提供，但未承诺放弃未来的速率限制或订阅计划。
  differentiation: 作为运行在设备本地的无障碍 AI 功能，其技术实现不依赖云端基础设施，但 Meta 仍试图将其纳入订阅变现体系。
  watch_reason: 该功能争议暴露了 AI 硬件行业在设备本地能力与云端服务收费之间的边界模糊问题，其最终定价策略将成为衡量消费者接受度的关键标杆。
  risk_notes:
  - Meta 明确表示不会放弃订阅制策略，该功能未来仍可能被纳入收费范围。
  - 用户对本地功能收费的强烈反感可能迫使 Meta 彻底调整产品线定价逻辑。
  score: 6.0
  article_ids:
  - c7eccabed7febc7e
  evidence_snippets:
  - Conversation Focus 是一项让用户更清晰听到对方说话的无障碍功能，运行在眼镜本地设备上。
  - 该功能在遭遇公众反对后暂停了订阅测试，目前仍通过早期访问计划免费提供给测试用户。
  - Meta 称正在为 Conversation Focus 探索更好的方案，但未承诺取消未来的速率限制。
---

Remember when Meta was planning to charge a $20 monthly subscription fee for the smart glasses feature that lets people hear each other more clearly — even though that feature runs locally on your glasses and doesn’t require the cloud? Meta has paused those plans, spokesperson Tyler Yee confirms to *The Verge*.

# After backlash, Meta pauses plan to ‘rate limit’ its smart glasses

“We’re still exploring all our options for the best approach.”

“We’re still exploring all our options for the best approach.”

The company is *not* giving up on the idea of a subscription fee for certain features — that’s still moving forward. Yee confirms that “some premium features will be subscription-based over time.”

But Conversation Focus, the accessibility feature, “will remain available for free through our Early Access Program for early testers while we work on a better approach.”

Here’s one of the company’s statements to *The Verge*:


Meta’s AI glasses pack a lot of value for free, and some premium features will be subscription-based over time—and conversation focus is one we want to make sure we get right. We heard the feedback so we’re pausing its subscription test for now. Conversation focus will remain available for free through our Early Access Program for early testers while we work on a better approach.

The most ridiculous part of Meta’s original plan was the “rate limits.” Meta made it sound like it *needed* to charge a subscription for Conversation Focus because running that service had an incremental cost, to the point that even paid subscribers would only get 15 hours of Conversation Focus per month. That was easy to disprove: When I disconnected my own Meta Ray-Bans from the internet, the feature kept on working.

But Meta isn’t actually promising to abandon those “rate limits.”

I asked: “Given that Conversation Focus is on-device and Meta understands the backlash, is the thinking that it will no longer be rate-limited?”

Meta’s answer: “We don’t have any more details to share, but its subscription test is currently paused and we’re still exploring all our options for the best approach.”

Yee says that “not all” premium features will be subscription-based, though. He hints the reason Meta is charging a subscription is so it can subsidize the price of hardware, not to maintain the features themselves:

We sell hardware at accessible prices to get AI glasses into the hands of as many people as possible and they pack a lot of value for free, so some premium features will be subscription-based over time. Charging power users for expanded use of premium features is how we sustain this strategy and keep investing in breakthrough capabilities.