---
title: Twitch streamers can now opt out from training Amazon’s AI
source: https://www.theverge.com/tech/979112/twitch-streamers-can-now-opt-out-from-training-amazons-ai
author:
- '[[Jay Peters]]'
published: '2026-08-12'
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
description: Twitch users can now opt out of allowing their content to be used to
  train Amazon's generative AI models. Opting out means that "your streams, VODs,
  clips, stream chats, and pictures and text on your channel" won't be used in "future
  training" of an Amazon AI model "whose purpose is to generate or synthesize text,
  [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: da3ea3dbc9d0910a
source_type: news_media
tldr: Twitch 新增隐私开关，允许用户选择不让自己的直播、回放、聊天等频道内容被用于训练 Amazon 的生成式 AI 模型，但其他 AI 辅助功能仍正常运行。
objective_summary: Twitch（隶属于 Amazon）在其设置中上线了“Training for Generative AI”开关，位于 Security
  and Privacy 标签页。用户关闭后，其直播、视频回放、剪辑、聊天、图片和文字将不会被用于未来旨在生成或合成文本、音频、图像、视频的 Amazon 生成式
  AI 模型训练；其他 AI 支持功能（如字幕、安全工具、推荐、赞助辅助）仍然有效。记者发现自己账号中该开关默认为开启，并已向 Amazon 求证默认策略。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Twitch
  - Amazon
  technologies:
  - generative AI
  - AI-supported features
  key_people: []
key_logic_flow:
- Twitch 新增“Training for Generative AI”开关，允许用户退出将其频道内容用于 Amazon 生成式 AI 模型训练。
- 退出后，直播、视频回放、剪辑、聊天、图片和文字不会被用于未来旨在生成或合成文本、音频、图像、视频的 Amazon AI 模型训练。
- 其他 AI 支持功能（如字幕、安全工具、AutoMod、观众发现推荐、实时赞助辅助）在退出后仍可继续运行。
- 在他人直播间中发送的聊天内容是否被用于训练，由该直播间主播的退出偏好决定。
- 记者发现该开关在其账号中初始为开启状态，并已向 Amazon 确认这是否为默认设置。
object_mentions:
- object_type: product
  name: Twitch “Training for Generative AI” toggle
  canonical_name: Twitch Training for Generative AI toggle
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Twitch 用户在设置的 Security and Privacy 标签下可以看到新的 Training for Generative AI 开关，用于控制是否允许频道内容训练
    Amazon 的生成式 AI 模型。
  - Twitch 支持页面说明，关闭该开关后，直播、VOD、剪辑、聊天、图片和文字不会被用于未来 Amazon 生成式 AI 模型的训练。
  article_id: da3ea3dbc9d0910a
- object_type: model
  name: Amazon generative AI content models
  canonical_name: Amazon generative AI content models
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 开关说明中称允许频道内容用于训练 Amazon 的生成式 AI 内容模型，其用途是生成或合成文本、音频、图像或视频。
  - Twitch 支持页面表示，退出训练意味着这些内容不会被用于未来 Amazon 生成式 AI 模型的训练。
  article_id: da3ea3dbc9d0910a
- object_type: product
  name: AI-supported Twitch features
  canonical_name: Twitch AI-supported features
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Amazon 的开关说明列举，AI 支持的 Twitch 功能包括促进主播增长与变现的实时赞助活动辅助、观众发现推荐以及社区安全功能 AutoMod。
  - 其他 AI 支持功能如字幕和安全工具在退出生成式 AI 训练后仍可正常运行。
  article_id: da3ea3dbc9d0910a
extract_result: success
impact_score:
  score: 5.5
  reason: 该事件并非技术突破，而是主流内容平台（Twitch/Amazon）在生成式 AI 数据治理上的重要政策调整。它确立了“创作者可选择退出内容被用于模型训练”的行业先例，对依赖
    UGC 训练 AI 的平台（YouTube、TikTok、Instagram 等）形成合规与公关压力，可能推动更多平台上线类似 opt-out 开关；但本质上属于隐私设置层面的变更，短期内不会直接改变模型能力或市场竞争格局。评分：5.5。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 开关默认开启（opt-out 而非 opt-in）以及“他人直播间聊天内容受主播偏好支配”的归属逻辑
hype_assessment:
  level: low
  reason: 文章为事实性报道，引用了 Twitch 支持页面的具体描述，包括开关位置、影响范围（stream/VOD/clips/chat 等）以及不影响的
    AI 辅助功能。没有出现“颠覆”、“革命性”等 PR 夸张词汇，判定依据为信息具体、可验证、无过度包装。水分较低。
information_entropy: medium
domain_disruption:
  technical_innovation: 无
  business_model: 重塑平台与创作者之间的数据使用契约：Twitch 将 UGC 训练数据的授权从“默认可使用”改为“默认可使用但可退出”，未来可能影响
    AI 模型训练的数据获取成本、合规策略，并促使其他大型平台引入类似的创作者同意机制。
engineering_complexity: production_ready
compound_value:
  score: 4.2
  reason: 该事件本质是平台级隐私合规开关，而非技术或商业模式创新。其对资本的长期价值主要体现在两方面：一是降低 Amazon/Twitch 因未经授权使用
    UGC 训练生成式 AI 而面临的监管与声誉风险，二是推动行业训练数据来源从“默认可用”向“明示同意/授权”转型。这意味着未来基础模型训练的数据获取成本将系统性上升，利好拥有第一手用户关系、能合法获取授权数据的大型平台；但对于依赖免费
    UGC 或灰色数据抓取的玩家则是利空。作为单一产品功能，它没有网络效应或基础设施锁定，难以形成复利增长，因此评分处于中等偏低区间。
value_capture_layer: foundation_model
moat_impact: strengthens_monopoly
key_beneficiaries:
- Amazon
- Twitch
competitive_casualty:
- 依赖未授权 UGC 训练的生成式 AI 初创公司
- 低成本网络爬虫与灰色数据经纪商
- 缺乏清晰数据溯源能力的基础模型实验室
market_opportunities:
- 面向MCN机构和独立创作者开发多平台隐私开关统一管理工具，帮助其批量审计并控制内容是否被用于生成式AI训练。
- 为出海平台和内容社区提供AI训练数据合规咨询与隐私政策落地服务，抢占欧美数据监管趋严背景下的合规市场。
- 围绕UGC/直播场景构建数据授权与溯源中间件，使平台在启用AI训练前能够按用户偏好进行细粒度授权管理。
risk_matrix:
  regulatory: 若默认开启，Twitch/Amazon可能面临GDPR、美国各州隐私法等诉讼风险；监管者可能要求生成式AI训练从opt-out转为更严格的opt-in。
  technological: 大量主播选择退出将削弱Amazon在直播、聊天、视频等多模态生成模型上的数据优势，影响模型效果与迭代速度。
  competitive: YouTube、TikTok等平台可能跟进更严格的训练数据政策，形成合规差异化竞争，进而改变创作者平台格局。
  ethical: 默认开启易被质疑侵犯用户数据自主权；观众在他人的直播间发言是否被用于训练由主播偏好决定，存在知情同意边界模糊问题。
  additional:
  - 退出训练后仍保留部分AI功能，可能让普通用户误以为已完全禁用AI处理，存在沟通与信任风险。
  - 训练数据范围收窄可能影响推荐、实时赞助辅助等功能的长期效果，进而对主播变现和社区生态产生连锁影响。
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Twitch “Training for Generative AI” toggle
  canonical_name: Twitch Training for Generative AI toggle
  url: null
  positioning: Twitch 在平台隐私设置中新增的生成式 AI 训练退出开关，允许主播控制其频道内容是否被用于 Amazon 生成式 AI 模型训练。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Twitch 主播与内容创作者
  - 关注隐私与数据使用权的 Twitch 用户
  product_signal: 开关位于 Security and Privacy 标签页，记者发现其初始为开启状态，默认策略尚待 Amazon 确认，关闭后不影响字幕和安全工具等其他
    AI 辅助功能运行。
  market_signal: 反映了大型内容平台在将创作者数据用于生成式 AI 训练时，面临的隐私合规压力与维护创作者关系之间的紧张平衡。
  differentiation: 与默认收集创作者数据的做法不同，该功能明确赋予主播对其直播、回放、剪辑、聊天等内容是否用于生成式 AI 训练的选择权。
  watch_reason: 该开关是 Amazon/Twitch 在生成式 AI 数据使用合规化方面的关键动作，其最终默认状态、退出范围的具体执行边界以及是否会扩展至
    Amazon 其他业务，都值得持续跟踪。
  risk_notes:
  - 默认开启状态尚未得到 Amazon 官方确认，可能影响用户真实选择权。
  - 退出仅覆盖生成式 AI 训练，其他 AI 用途仍按 Twitch 隐私政策执行。
  score: 7.0
  article_ids:
  - da3ea3dbc9d0910a
  evidence_snippets:
  - Twitch 用户在设置的 Security and Privacy 标签下可以看到新的 Training for Generative AI 开关，用于控制是否允许频道内容训练
    Amazon 的生成式 AI 模型。
  - Twitch 支持页面说明，关闭该开关后，直播、VOD、剪辑、聊天、图片和文字不会被用于未来 Amazon 生成式 AI 模型的训练。
- object_type: product
  name: AI-supported Twitch features
  canonical_name: Twitch AI-supported features
  url: null
  positioning: Twitch 平台中已集成、依赖 AI 但独立于生成式 AI 模型训练的功能集合，用于支持主播增长变现、观众发现与社区安全治理。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Twitch 主播
  - Twitch 观众
  - 广告主与品牌方
  product_signal: 包括促进主播增长与变现的实时赞助活动辅助、观众发现推荐、社区安全工具 AutoMod，以及字幕和安全工具等 AI 支持功能。
  market_signal: 显示 Twitch 正将 AI 能力按业务场景细分，并试图在回应数据使用争议的同时，保持平台商业化与用户体验的连续性。
  differentiation: 这些 AI 支持功能在用户退出生成式 AI 训练后仍可继续运行，体现了平台对生成式训练与其他 AI 用途的区隔化处理。
  watch_reason: 作为 Twitch AI 战略中非生成式训练的核心组成部分，这些功能关系到平台商业化、社区安全和用户体验，值得观察其与隐私开关的协同演进。
  risk_notes:
  - 功能范围较宽泛，具体算法逻辑、数据处理方式及其与生成式 AI 训练的数据边界未在报道中详细披露。
  score: 5.0
  article_ids:
  - da3ea3dbc9d0910a
  evidence_snippets:
  - Amazon 的开关说明列举，AI 支持的 Twitch 功能包括促进主播增长与变现的实时赞助活动辅助、观众发现推荐以及社区安全功能 AutoMod。
  - 其他 AI 支持功能如字幕和安全工具在退出生成式 AI 训练后仍可正常运行。
---

Twitch users can now opt out of allowing their content to be used to train Amazon’s generative AI models. Opting out means that “your streams, VODs, clips, stream chats, and pictures and text on your channel” won’t be used in “future training” of an Amazon AI model “whose purpose is to generate or synthesize text, audio, images, or video,” according to a Twitch support page.

# Twitch streamers can now opt out from training Amazon’s AI

Flip the new Twitch toggle if you don’t want your content to be used to train Amazon’s generative AI content models.

Flip the new Twitch toggle if you don’t want your content to be used to train Amazon’s generative AI content models.

Other “AI-supported” features like captions and safety tools will still function if you opt-out of generative AI training. However, if you participate in a chat on another person’s stream, “their opt-out preferences govern if that chat can be used for training,” Twitch says.

The “Training for Generative AI” toggle is present for me in Twitch’s settings under the Security and Privacy tab. It was toggled on when I found it, and I’ve asked Amazon if that’s the default.

Here’s the full text of Amazon’s description for the toggle:

Allow your channel content to train generative AI content models at Amazon. Turning this off does not opt you out of Twitch and Amazon using your channel content for other purposes described in the Twitch Privacy Notice, including using AI-supported Twitch features that benefit the community by facilitating streamer growth and monetization (such as real-time sponsorship campaign assistance), viewer discovery (such as recommendations), and community safety (such as AutoMod). Learn more


**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.

## Most Popular

- Google’s Pixel 11 series pairs a little new hardware with a lot of new software
- Xbox Elite 3 prototype pad leaks with tiny built-in screen
- How Google’s new Pixel 11 phones compare to last year’s models
- The 7 biggest announcements of Google’s Pixel 11 launch
- The Pixel Tag is Google’s answer to the AirTag