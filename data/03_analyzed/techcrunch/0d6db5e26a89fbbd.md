---
title: Google’s Gemini has a branding problem, and so does the rest of AI
source: https://techcrunch.com/2026/08/26/googles-gemini-has-a-branding-problem-and-so-does-the-rest-of-ai/
author:
- '[[Sarah Perez]]'
published: '2026-08-26'
created: '2026-08-27'
manifest_dates:
- '2026-08-27'
description: Consumer AI apps need to stop making users learn their product architecture.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0d6db5e26a89fbbd
source_type: news_media
tldr: 谷歌新版 Gemini 应用将聊天、Spark、Daily Brief 等功能分别品牌化，造成界面混乱。文章批评 AI 行业普遍把内部交互模式直接暴露给消费者，例如
  Claude 的 Cowork、ChatGPT 的 Work，用户被迫记住各种模式名称。
objective_summary: 谷歌周三发布新版 Gemini Live 语音功能，称用户无需猜测任务该用 Spark、Daily Brief 还是收件箱搜索。但文章批评谷歌将聊天、Spark
  与 Daily Brief 三个功能分别品牌化，令消费体验杂乱。Daily Brief 从 Gmail 等应用提取数据提供日程更新，却无法区分紧急信息与无关提示；Spark
  是可代用户执行操作的 AI 代理，被不必要地包装成独立品牌。文章进一步指出 Anthropic 的 Claude 与 OpenAI 的 ChatGPT 同样要求用户在聊天和代理模式间手动切换。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - Anthropic
  - OpenAI
  technologies:
  - Gemini Live
  - AI agent
  key_people: []
key_logic_flow:
- 谷歌周三发布新版 Gemini Live 语音功能，承诺用户无需猜测任务该用 Spark、Daily Brief 还是快速收件箱搜索，但文章认为其给每个功能单独品牌化反而削弱了这一承诺。
- Gemini 应用内设有聊天、Spark 和 Daily Brief 三个独立功能，各有图标与导航入口，导致消费体验杂乱，也反映出 Gemini 仍缺乏杀手级功能。
- Daily Brief 作为 AI 日程功能，从 Gmail 和日历等 Google 应用中提取数据提供主动个性化更新，却无法区分紧急信息与无关提示，还会重提用户此前的搜索记录，令人不适。
- Spark 是可代表用户执行操作的 AI 代理，被认为是 Gemini 应用较有用的功能之一，但被包装成独立品牌，普通用户无需关心自己处在应用的哪一侧。
- 问题不限于 Gemini：Anthropic 的 Claude 要求用户在聊天与 Cowork 模式之间选择，且直到本周两种模式还不共享对话记忆。
- 文章认为 AI 行业普遍将内部架构直接暴露给消费者，ChatGPT 也要求用户手动切换 Chat 与 Work，消费者被迫学习本质上是交互模式的品牌名称。
object_mentions:
- object_type: product
  name: Gemini
  canonical_name: Gemini
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌在周三公告中表示，新版 Gemini 应用可通过语音命令处理多种任务，但文章批评其将聊天、Spark 与 Daily Brief 分别品牌化，反而令消费体验杂乱。
  article_id: 0d6db5e26a89fbbd
- object_type: product
  name: Gemini Live
  canonical_name: Gemini Live
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 谷歌周三发布了新的 Gemini Live 语音功能，并承诺用户无需猜测某个任务究竟该使用 Spark、Daily Brief 还是快速收件箱搜索。
  article_id: 0d6db5e26a89fbbd
- object_type: product
  name: Spark
  canonical_name: Gemini Spark
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Spark 是 Gemini 应用内可代表用户执行操作的 AI 代理，被认为是较有用的功能之一，但文章认为它被包装成独立品牌并无必要。
  article_id: 0d6db5e26a89fbbd
- object_type: product
  name: Daily Brief
  canonical_name: Gemini Daily Brief
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Daily Brief 是 Gemini 的 AI 日程功能，会从 Gmail 和日历等 Google 应用中提取数据提供主动个性化更新，但无法区分紧急信息与无关提示，还会重提用户此前的搜索记录。
  article_id: 0d6db5e26a89fbbd
- object_type: product
  name: Claude
  canonical_name: Claude
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章指出 Anthropic 的 Claude 应用要求用户选择是聊天还是在 Cowork 模式下协作，直到本周这两种模式还不共享过去的对话记忆。
  article_id: 0d6db5e26a89fbbd
- object_type: product
  name: Cowork
  canonical_name: Claude Cowork
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Cowork 是 Claude 应用内与聊天模式并列的协作模式，截至本周两种模式仍不共享对话历史，文章认为这种设计让 AI 交互显得不自然。
  article_id: 0d6db5e26a89fbbd
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章对比称 ChatGPT 同样要求用户在 Chat 与 Work 两种模式之间切换，消费者被迫学习本质上是交互模式的品牌名称。
  article_id: 0d6db5e26a89fbbd
- object_type: product
  name: Work
  canonical_name: ChatGPT Work
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - ChatGPT 的 Work 模式与 Chat 模式需要用户手动切换，文章认为这种工程化设计把内部架构直接暴露给了消费者。
  article_id: 0d6db5e26a89fbbd
extract_result: success
impact_score:
  score: 4.0
  reason: 该事件本质是一篇针对 AI 应用 UX/品牌化的批判性评论，附带 Google Gemini Live 语音更新、Daily Brief/Spark
    品牌拆分、Claude 本周统一聊天与 Cowork 记忆等增量产品信息。行业意义在于首次集中揭示'聊天/代理/主动推荐'多模式界面正成为头部 AI 应用（Gemini、Claude、ChatGPT）的普遍形态，且各自独立品牌化加剧用户认知负担，对
    AI 产品设计方向有警示价值。但文章不涉及范式转移或重大竞争格局改变，属于产品体验层面的渐进讨论，未达到重要产品发布的冲击级别，故评分为中等偏低的 4 分。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: AI 应用将聊天、代理（Spark/Cowork/Work）等内部交互模式直接暴露给消费者，用户被迫记忆模式品牌名
hype_assessment:
  level: low
  reason: 全文是反炒作的产品批评，而非产品宣传稿：明确指出 Google 将 Spark/Daily Brief 独立品牌化是'工程师思维'，并批评每日简报会重提用户隐私搜索记录令人不适。文中无'颠覆'、'革命性'等
    PR 滥用词汇，反而用 'creepy'、'clutters' 等负面词描述体验，属于务实的行业反思，炒作指数低。
information_entropy: medium
domain_disruption:
  technical_innovation: 无本质技术突破。文章揭示的核心工程问题是：AI 应用把聊天、agent 执行（Spark/Cowork）与主动推荐（Daily
    Brief）拆分为独立模块，且记忆上下文尚未统一——Claude 的聊天与 Cowork 两种模式直到本周才共享对话记忆，反映出 agent 架构在会话状态与记忆管理上仍存在工程缝隙，且被直接暴露到产品层。
  business_model: 厂商正将 agent 能力拆分为独立品牌（Spark/Cowork/Work），试图为代理功能建立差异化产品线乃至未来独立定价入口；但碎片化品牌显著抬高用户认知成本，可能阻碍
    agent 功能从'技术亮点'走向'大众规模化'的商业化转化。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 该事件表面是谷歌的品牌混乱批评，本质上是 AI 消费层交互范式的一次'清算时刻'：谷歌、Anthropic、OpenAI 三家巨头同时把内部架构（聊天/代理/主动推送）直接暴露给用户，说明整个行业仍停留在'工程思维产品化'阶段，杀手级场景尚未跑通。从资本视角看，这恰恰验证了'统一智能入口'是下一轮必争之地——谁能把模式切换、代理编排、主动推送抽象为无感体验，让用户'一句话直达结果'，谁就能把
    AI 从工具集合升级为日常基础设施，进而靠习惯性使用沉淀数据飞轮和高留存，迁移成本极高，复利属性明确。但当前三家均未证明这一范式可落地：Daily Brief
    因回捞搜索记录产生隐私不适感，Claude 的 Cowork 直到本周才与聊天共享记忆，产品化成熟度不足，故给 7 分而非更高。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Anthropic
- Google
competitive_casualty:
- Google 的独立子品牌（Spark、Daily Brief）
- 交互模式割裂的 AI 原生应用创业公司
market_opportunities:
- 开发者可构建将聊天、AI 代理、日程简报等能力统一封装为单一对话界面的 AI 产品框架或中间件，帮助 AI 公司避免将内部架构直接暴露给消费者
- 创业者可瞄准隐私敏感型 AI 助手赛道，通过本地化处理、最小化数据收集和严格的数据使用边界，解决 Daily Brief 式主动重提用户搜索记录带来的不适感与信任问题
- AI 产品团队可将'交互模式统一'纳入设计评审标准，率先消除产品内的模式切换与碎片化品牌，将简洁直观的用户体验作为差异化竞争点
risk_matrix:
  regulatory: AI 助手从 Gmail、日历等个人数据中提取信息并主动推送、重提用户搜索记录，可能触及 GDPR/CCPA 等隐私法规对数据最小化与目的限制的要求，引发隐私监管审查
  technological: 多模式割裂架构（如 Claude 聊天与 Cowork 此前不共享记忆、Gemini 各功能独立）积累技术债，可能被统一交互层的产品架构迭代所取代
  competitive: Google、Anthropic、OpenAI 正竞相解决同一 UX 问题，率先完成统一交互体验的厂商将抢占消费者心智，未跟进者面临用户流失与品牌认知劣势
  ethical: AI 主动重提用户历史搜索与浏览数据造成'被监控'的不适感，存在隐私侵犯与信任侵蚀风险；AI 代理代表用户自主执行操作还涉及授权边界与误操作责任问题
  additional:
  - 品牌稀释：过度细分功能品牌使消费者难以形成对产品的整体认知，削弱品牌资产与口碑传播
  - 用户学习成本上升：消费者被迫记忆交互模式品牌名，抬高使用门槛，阻碍 AI 产品向主流大众用户渗透
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: Gemini
  canonical_name: Gemini
  url: null
  positioning: Gemini 是谷歌面向消费者的多模态 AI 助手应用，覆盖聊天、日程简报与代理操作等场景，试图以语音命令统一处理多种任务。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 面向普通消费者的多模态 AI 助手用户
  product_signal: 新版 Gemini 应用可经语音命令处理多种任务，但聊天、Spark 与 Daily Brief 各有独立品牌与导航入口，界面显得杂乱。
  market_signal: 文章认为 Gemini 仍缺乏杀手级功能，多个独立品牌化的功能反而削弱了统一语音助手的消费吸引力。
  differentiation: 相较 Claude 与 ChatGPT 的模式切换，Gemini 以三个独立功能品牌化的方式组织体验，杂乱感更为突出。
  watch_reason: Gemini 的品牌化策略暴露了主流 AI 助手在交互模式统一上的困境。其能否收敛功能入口、找到杀手级应用，将直接影响谷歌在消费级
    AI 市场的竞争力与用户留存。
  risk_notes:
  - 多功能各自品牌化导致界面混乱，反映出 Gemini 仍在寻找杀手级功能，存在产品定位风险。
  - 将内部工程团队划分直接暴露给消费者，可能增加普通用户的学习与使用成本。
  score: 8.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - 谷歌在周三公告中表示，新版 Gemini 应用可通过语音命令处理多种任务，但文章批评其将聊天、Spark 与 Daily Brief 分别品牌化，反而令消费体验杂乱。
- object_type: product
  name: Gemini Live
  canonical_name: Gemini Live
  url: null
  positioning: Gemini Live 是谷歌新发布的语音交互功能，允许用户通过语音命令处理多类任务，并承诺自动判断任务归属。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 偏好语音交互的 Gemini 用户
  - 希望以自然语言完成多任务处理的消费者
  product_signal: Gemini Live 主打语音驱动多任务处理，但其消除功能选择负担的承诺与各功能独立品牌化的现状自相矛盾。
  market_signal: 此次发布是谷歌统一语音助手体验的关键动作，但其品牌化策略削弱了这一承诺的市场说服力。
  differentiation: Gemini Live 试图以语音为统一入口，降低用户对 Spark、Daily Brief 与收件箱搜索等内部模式的感知。
  watch_reason: Gemini Live 代表了谷歌试图用语音统一分散功能入口的战略方向，其能否真正兑现无需猜测任务归属的承诺，是衡量 Gemini
    消费体验演进的重要观察点。
  risk_notes:
  - 语音入口的承诺与实际多品牌化现状冲突，存在承诺落空而引发失望的风险。
  score: 6.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - 谷歌周三发布了新的 Gemini Live 语音功能，并承诺用户无需猜测某个任务究竟该使用 Spark、Daily Brief 还是快速收件箱搜索。
- object_type: product
  name: Spark
  canonical_name: Gemini Spark
  url: null
  positioning: Spark 是 Gemini 应用内可代表用户执行操作的 AI 代理，被谷歌包装为独立品牌，文章认为这是较有用却被过度品牌化的功能。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要在对话中直接触发代理执行任务的 Gemini 用户
  product_signal: Spark 作为可代用户执行操作的 AI 代理，被视为 Gemini 应用较有用的功能之一，但被不必要地包装成独立品牌。
  market_signal: 文章认为主流用户无需关心任务发生在应用的哪一侧，Spark 独立品牌化增加了消费级产品的认知负担。
  differentiation: Spark 与 Daily Brief 形成对照——前者功能有用但品牌化多余，后者品牌合理却体验不佳。
  watch_reason: Spark 代表了 Gemini 在代理执行方向上的实质能力。其能否从独立品牌收敛为底层能力、由 AI 自动触发，是判断谷歌代理产品走向统一体验的关键信号。
  risk_notes:
  - 独立品牌化可能让普通用户对何时该用 Spark 产生困惑，抑制代理功能使用率。
  score: 7.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - Spark 是 Gemini 应用内可代表用户执行操作的 AI 代理，被认为是较有用的功能之一，但文章认为它被包装成独立品牌并无必要。
- object_type: product
  name: Daily Brief
  canonical_name: Gemini Daily Brief
  url: null
  positioning: Daily Brief 是 Gemini 的 AI 日程功能，从 Gmail 与日历等 Google 应用提取数据，向用户提供主动、个性化的日程更新。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 希望获得主动日程更新的 Gemini 用户
  product_signal: Daily Brief 提供主动个性化更新，但无法区分紧急信息与无关提示，还会重提用户历史搜索，被文章批评为工程师思维而非用户体验。
  market_signal: 文章认为 Daily Brief 体现了 AI 工程师而非普通用户会欣赏的设计，主动打扰式体验可能损害谷歌产品的用户信任。
  differentiation: Daily Brief 与 Spark 相反——作为独立品牌尚可理解，但其价值主张与落地体验存在明显落差。
  watch_reason: Daily Brief 是谷歌将 Gmail、日历等跨应用数据转化为主动日程服务的代表性尝试，其信息优先级判断与隐私敏感度将直接决定该功能能否被主流用户接受，也关系到谷歌在主动式
    AI 服务上的口碑。
  risk_notes:
  - 无法区分紧急信息与无关提示，可能让主动更新变成干扰而非价值。
  - 重提用户此前搜索记录的行为被评价为令人不适，存在隐私信任风险。
  score: 7.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - Daily Brief 是 Gemini 的 AI 日程功能，会从 Gmail 和日历等 Google 应用中提取数据提供主动个性化更新，但无法区分紧急信息与无关提示，还会重提用户此前的搜索记录。
- object_type: product
  name: Claude
  canonical_name: Claude
  url: null
  positioning: Claude 是 Anthropic 的 AI 助手产品，在应用内同时提供聊天与 Cowork 协作两种模式，供用户按需切换使用。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 在聊天与协作代理模式之间切换的 Claude 用户
  product_signal: Claude 应用要求用户在聊天与 Cowork 模式间手动选择，两种模式过去不共享对话记忆，交互仍显割裂。
  market_signal: 文章将 Claude 与 Gemini、ChatGPT 并列为把内部交互模式直接暴露给消费者的典型，反映行业普遍问题。
  differentiation: Claude 的聊天与 Cowork 双模式设计与 ChatGPT 的 Chat/Work、Gemini 的多功能品牌化相似，均把工程架构暴露给终端用户。
  watch_reason: Claude 的聊天与 Cowork 模式长期不共享对话记忆，代表交互体验仍未完全统一。其能否降低模式切换的认知负担并打通记忆，是观察
    Anthropic 消费级易用性的重要信号。
  risk_notes:
  - 手动切换聊天与 Cowork 模式可能增加用户学习成本，影响协作功能采用。
  score: 6.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - 文章指出 Anthropic 的 Claude 应用要求用户选择是聊天还是在 Cowork 模式下协作，直到本周这两种模式还不共享过去的对话记忆。
- object_type: product
  name: Cowork
  canonical_name: Claude Cowork
  url: null
  positioning: Cowork 是 Claude 应用内与聊天模式并列的协作模式，供用户与 AI 协同完成任务的独立交互界面。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要在协作模式下完成复杂任务的 Claude 用户
  product_signal: Cowork 作为协作模式与聊天并列，用户需主动选择进入，且两种模式过去不共享对话历史，交互完整性仍显不足。
  market_signal: 文章认为 Cowork 这类模式化设计把内部架构暴露给消费者，让 AI 交互显得不自然。
  differentiation: Cowork 与 ChatGPT 的 Work 均为代理能力的独立交互表面，但 Cowork 需额外关注与聊天模式的记忆打通问题。
  watch_reason: Cowork 是 Anthropic 将代理协作能力产品化的关键入口，其与聊天模式的记忆打通及交互统一程度，将直接决定 Claude
    在代理工作流场景的可用性与用户采用，也是观察其消费级易用性的重要窗口。
  risk_notes:
  - 作为独立协作模式存在认知负担，用户可能不清楚何时该切换到 Cowork。
  score: 5.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - Cowork 是 Claude 应用内与聊天模式并列的协作模式，截至本周两种模式仍不共享对话历史，文章认为这种设计让 AI 交互显得不自然。
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: null
  positioning: ChatGPT 是 OpenAI 的 AI 助手产品，在应用内同时提供 Chat 与 Work 两种模式，需用户手动切换使用。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要在 Chat 与 Work 模式间切换的 ChatGPT 用户
  product_signal: ChatGPT 要求用户在 Chat 与 Work 模式之间手动切换，文章认为这是把内部架构直接暴露给消费者的典型设计。
  market_signal: 文章将 ChatGPT 与 Claude、Gemini 并列批评，反映主流 AI 助手在交互模式统一上的普遍共性。
  differentiation: ChatGPT 与 Claude 一样将代理能力拆成独立模式，但品牌命名为 Chat 与 Work，与 Gemini 的多功能品牌化形成对照。
  watch_reason: ChatGPT 的 Chat 与 Work 双模式设计代表了 OpenAI 对消费级代理交互的取舍，其是否走向模式融合、降低用户选择负担，是观察主流
    AI 助手易用性演进与代理普及的重要参照。
  risk_notes:
  - 手动切换模式迫使消费者学习交互模式品牌名，增加使用门槛。
  score: 6.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - 文章对比称 ChatGPT 同样要求用户在 Chat 与 Work 两种模式之间切换，消费者被迫学习本质上是交互模式的品牌名称。
- object_type: product
  name: Work
  canonical_name: ChatGPT Work
  url: null
  positioning: Work 是 ChatGPT 应用内与 Chat 并列的独立模式，面向需要代理执行任务的用户，需手动切换进入。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要使用代理模式执行任务的 ChatGPT 用户
  product_signal: Work 与 Chat 模式需用户手动切换，文章批评这种工程化设计把内部架构直接暴露给了消费者。
  market_signal: Work 模式是 ChatGPT 将代理能力产品化的体现，但其与 Chat 的分隔被批评为让 AI 交互不自然。
  differentiation: Work 与 Claude 的 Cowork 类似，均为代理能力的独立交互表面，但品牌命名与模式边界各有不同。
  watch_reason: Work 模式是观察 OpenAI 如何在消费级产品中融合聊天与代理能力的关键窗口，其交互设计走向将反映行业对模式统一问题的普遍答案，也影响代理功能在普通用户中的普及节奏。
  risk_notes:
  - 独立 Work 模式可能增加用户的模式选择负担，影响代理功能普及。
  score: 5.0
  article_ids:
  - 0d6db5e26a89fbbd
  evidence_snippets:
  - ChatGPT 的 Work 模式与 Chat 模式需要用户手动切换，文章认为这种工程化设计把内部架构直接暴露给了消费者。
---

Google gets something right in its Wednesday announcement about new Gemini Live voice features when it says, “You shouldn’t have to guess whether a task requires Spark, a Daily Brief, or a quick inbox search.” Google means that as a promise — that the updated Gemini app can handle a variety of tasks via voice commands. But there’s a ridiculousness here: Google has given every Gemini AI feature under the sun its own branding, which undercuts that very message.

In the Gemini app, users can switch between chat, Spark, and Daily Brief — three separate features, each with its own icon and place in the app’s navigation. This clutters up what could otherwise be a more straightforward consumer experience, and it suggests that Gemini is still struggling to find a killer feature.

Take Daily Brief, for example. The feature comes across as something an AI engineer, not an everyday user, would think is clever. It’s essentially an AI-enabled agenda that offers “proactive, personalized updates” using data pulled from Google’s apps, like Gmail and Calendar. In practice, though, the Brief can’t tell the difference between information that’s urgent or actionable and unsolicited nudges to follow up on other things — like prompting you to continue research you started in the chatbot, or worse, resurfacing your prior Google searches.

That second part doesn’t feel useful; it feels creepy. So what if I had been researching college scholarships or animal rescues on Google? That doesn’t mean I want an AI tapping me on the shoulder about them later.

Spark has the opposite problem. It’s one of the more useful aspects of Gemini’s app — an AI agent that can take action on your behalf — but Google has packaged it as its own stand-alone brand, which it doesn’t need to be. Sure, internally, Google engineers may want to be on the Spark team, and that’s fine — but a mainstream AI app user definitely does not need to think about which “side” of the AI app they need to be in for a given task. They should just be able to type their request, and the AI figures out how to handle it, spinning up an agent if the task calls for one.

In fairness, the problem isn’t limited to Gemini. The AI industry at large seems to expose its internal architecture directly to consumers rather than hiding it behind a simpler interface.

Today, people have to think about whether they want to “chat” with Anthropic’s Claude or “Cowork” with its help. (Until this week, those two modes inside the Claude app didn’t even share a memory of past conversations.) ChatGPT is the same, requiring you to swap between “Chat” and “Work.” This is the kind of engineering-minded design that makes engaging with AI feel unnatural. Consumers are being asked to learn the brand names for what are essentially interaction modes or surfaces, powered by a company’s AI model.