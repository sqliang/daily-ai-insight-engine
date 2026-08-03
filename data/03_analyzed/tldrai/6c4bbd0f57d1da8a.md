---
title: Updated Claude Voice Mode (9 minute read)
source: https://www.engadget.com/2221938/claude-voice-mode-just-got-smarter/?utm_source=tldrai
author: []
published: ''
created: '2026-07-25'
manifest_dates:
- '2026-07-25'
- '2026-07-26'
- '2026-07-27'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6c4bbd0f57d1da8a
source_type: news_media
tldr: Anthropic 更新了 Claude 语音模式，使它能调用 Sonnet 和 Opus 等更强大的模型处理复杂请求，并可连接 Gmail 和 Slack
  等外部应用获取上下文。新语音模式以测试版形式向所有桌面端、移动端和网页端用户逐步推出。
objective_summary: Anthropic 于今日发布 Claude 语音模式更新，将此前仅使用 Haiku 模型的语音查询路由策略升级为支持 Sonnet
  和 Opus 模型，并默认使用用户上次文本聊天所用的模型。更新后的语音模式可以连接 Gmail 和 Slack 等已授权外部应用以获取上下文信息。Anthropic
  正在向所有桌面端、移动端和网页端用户逐步推出该测试版，免费用户仍仅限使用 Haiku 模型。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Engadget
  - OpenAI
  technologies:
  - Claude Voice Mode
  - Haiku
  - Sonnet
  - Opus
  - GPT-Live
  key_people: []
key_logic_flow:
- Anthropic 此前为降低延迟，Claude 语音模式仅使用最小的 Haiku 模型，导致复杂请求处理能力受限。
- Anthropic 今日发布语音模式更新，使其能够调用 Sonnet 和 Opus 模型，并默认使用用户上次文本聊天所用的模型。
- 用户可以通过模型选择器在 Haiku、Sonnet 和 Opus 之间实时切换，语音模式会自动选取相应模型的最快版本以保证对话流畅。
- 更新后的语音模式可以连接 Gmail 和 Slack 等已授权外部应用以获取上下文信息，但需用户事先授予权限。
- Claude 语音模式采用轮流对话架构，与 OpenAI 的 GPT-Live 全双工系统不同，无法同时处理语音输入和输出。
- Claude 语音模式无法自动检测语言切换，用户需口头告知或手动在设置中选择目标语言；同时新增对印尼语等更多语言的支持。
object_mentions:
- object_type: product
  name: Claude Voice Mode
  canonical_name: Claude Voice Mode
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 今日更新 Claude 语音模式，使其能够调用 Sonnet 和 Opus 等更强大的模型处理复杂请求，此前仅使用 Haiku 模型。
  - 更新后的语音模式可以连接 Gmail 和 Slack 等已授权外部应用以获取上下文信息，但需要用户授予权限。
  - Anthropic 正在向所有桌面端、移动端和网页端用户逐步推出新的语音模式测试版，免费用户仅限使用 Haiku 模型。
  article_id: 6c4bbd0f57d1da8a
- object_type: product
  name: GPT-Live
  canonical_name: GPT-Live
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 与 OpenAI 的 GPT-Live 系统不同，Claude 语音模式采用轮流对话架构，无法同时处理语音输入和生成输出。
  article_id: 6c4bbd0f57d1da8a
extract_result: success
impact_score:
  score: 5.5
  reason: 从技术架构角度看，此次更新本质上是将语音模式的查询路由从固定使用 Haiku 模型升级为支持动态选择 Sonnet/Opus，并默认沿用用户上次文本聊天的模型。这解决了此前语音模式'只能问简单问题'的核心痛点，显著提升了复杂请求的处理质量。同时接入
    Gmail/Slack 等外部应用上下文，使语音助手从'独立问答工具'进化为'有上下文感知能力的助手'。但需注意两个硬伤：1）采用轮流对话架构而非全双工，与
    GPT-Live 存在代际体验差距；2）无法自动检测语言切换，多语场景体验割裂。整体而言，这是一个重要的产品补强，让 Claude 语音模式从'能用'变为'好用'，但并非范式级突破，短期内主要影响消费者
    AI 助手市场的竞争格局。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 语音模式的模型路由架构改进与全双工技术差距
hype_assessment:
  level: low
  reason: 文章本身没有使用 '颠覆性'、'革命性' 等 PR 滥用词汇，Anthropic 的官方回应也保持了克制，明确承认了轮流对话架构和语言检测等现有限制。文章既列举了改进点（模型路由、应用集成），也如实说明了局限性（非全双工、无自动语言切换），属于相对客观的产品更新报道，没有过度包装。
information_entropy: high
domain_disruption:
  technical_innovation: 将语音查询从固定使用最小模型 Haiku 升级为智能路由至 Sonnet/Opus 的架构，默认沿用用户上次文本聊天模型并支持对话中实时切换，且自动选取最快模型版本保证对话流畅性。这是一个务实的工程优化——用更聪明的路由策略替代'一刀切'的低延迟方案，在延迟与智能之间取得了更好的平衡。
  business_model: 通过提升语音交互质量增强 Claude 在消费级 AI 助手市场的竞争力，缩小与 OpenAI GPT-Live 的功能差距；同时借助
    Gmail/Slack 等应用集成构建生态粘性，推动用户从'免费试用'向'付费订阅'转化，是 Anthropic 在 consumer AI 领域的竞争策略升级。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 语音作为 AI 交互模态具有长期复利效应——随着 AI 助手从聊天界面转向更自然的交互方式，语音入口将沉淀为用户习惯和切换成本。此次更新的核心价值在于将语音模式从'轻量问答玩具'升级为'智能化的工作助手'：引入
    Sonnet/Opus 模型意味着复杂任务（代码调试、深度分析、多步推理）现在可通过语音完成，Gmail/Slack 集成则将语音交互延伸到用户已有的工作流中，形成'语音
    + 工具调用'的双重粘性。然而，扣分项在于：1) 仍采用轮替架构（turn-based），与 GPT-Live 的全双工实时对话相比体验有代差，OpenAI
    的先发优势在语音交互自然度上仍明显；2) 免费用户锁死在 Haiku 上，说明 Anthropic 尚未将语音作为独立获客手段，而是作为付费增值功能；3)
    语言切换需手动告知而非自动检测，说明多语言语音体验仍在打磨中。综合来看，这次更新提升了 Claude 语音模式的基线竞争力，但尚未构成颠覆性复利壁垒，需观察下半年更多的语音投资成果。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Google (Gmail 集成)
- Salesforce (Slack 集成)
competitive_casualty:
- OpenAI (GPT-Live 差异化缩小)
- 独立语音 AI 助手 (ElevenLabs 等)
- Cortana/Siri 等传统语音助手
market_opportunities:
- 企业协同场景可基于Claude语音模式+Gmail/Slack集成开发语音驱动的自动化工作流，例如语音指令查邮件、读Slack消息后直接生成回复草稿
- 多语言语音AI助理在东南亚市场（尤其是印尼语）存在差异化落地机会，开发者可优先针对该区域构建本地化语音交互应用
- 轮询对话架构的延迟控制方案（模型路由与最快版本自动切换）可作为技术参考，启发语音中间件创业方向
risk_matrix:
  regulatory: 语音数据采集结合Gmail/Slack等个人/企业应用授权访问，可能触发GDPR及各国数据隐私法规的合规审查，需要关注Anthropic的数据处理和授权机制
  technological: 轮询对话架构在实时性和自然度上不及OpenAI GPT-Live的全双工系统，若用户对对话流畅度要求提升，此技术路线可能面临体验劣势
  competitive: OpenAI GPT-Live已实现全双工语音交互，Google Gemini也在语音领域持续投入，Claude语音模式在体验和功能完整性上面临巨头挤压风险
  ethical: 语音模式连接外部应用（Gmail/Slack）获取上下文，增加用户数据被模型不当访问或泄露的伦理风险；免费用户仅限Haiku模型可能加剧AI服务数字鸿沟
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Claude Voice Mode
  canonical_name: Claude Voice Mode
  url: null
  positioning: Anthropic 推出的 Claude 语音对话功能，支持调用 Sonnet 和 Opus 等更强模型处理复杂请求，并可连接 Gmail
    和 Slack 等已授权外部应用获取上下文信息。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Claude 付费订阅用户（可使用 Sonnet 和 Opus 模型获得完整语音体验）
  - 需要语音交互的桌面端、移动端及网页端用户
  - 免费用户（仅限 Haiku 模型且单次连接）
  product_signal: 用户可通过模型选择器在 Haiku、Sonnet 和 Opus 之间实时切换，语音模式自动选取相应模型的最快版本以保持对话流畅。
  market_signal: Anthropic 以测试版逐步向所有桌面端、移动端和网页端用户推出新语音模式，免费用户仍仅限使用 Haiku 模型。
  differentiation: 采用轮流对话架构而非全双工模式，与 OpenAI 的 GPT-Live 形成设计差异化；同时无法自动检测语言切换需用户手动操作。
  watch_reason: Claude 语音模式本次升级解决了此前仅使用 Haiku 模型导致的复杂请求处理能力受限问题，并引入 Gmail 和 Slack
    等外部应用连接能力，使其从基础功能向实用工具进化，值得持续关注 Anthropic 在语音交互领域的后续布局。
  risk_notes:
  - 免费用户仅限使用 Haiku 模型且仅支持单次连接，语音交互体验受限。
  - 轮流对话架构而非全双工模式，交互自然度与 GPT-Live 相比仍有差距。
  - 无法自动检测语言切换，用户需口头告知或手动设置，多语言场景下使用不便。
  score: 7.0
  article_ids:
  - 6c4bbd0f57d1da8a
  evidence_snippets:
  - Anthropic 今日更新 Claude 语音模式，使其能够调用 Sonnet 和 Opus 等更强大的模型处理复杂请求，此前仅使用 Haiku 模型。
  - 更新后的语音模式可以连接 Gmail 和 Slack 等已授权外部应用以获取上下文信息，但需要用户授予权限。
  - Anthropic 正在向所有桌面端、移动端和网页端用户逐步推出新的语音模式测试版，免费用户仅限使用 Haiku 模型。
---

# Claude's voice mode just got smarter

And you can connect it to apps like Gmail and Slack.

Since last year, Anthropic has offered a voice mode through Claude, allowing you to speak to its chatbot instead of writing out your prompts. If I had to guess, most people probably don't know Claude has voice input. However, for those that have used it, the consensus has been that it could use work. One issue is that before today Anthropic routed voice mode queries through Haiku, its smallest model, to reduce latency. That meant voice mode worked well enough for simple questions, but could struggle with more complicated requests. Today, Anthropic is releasing an update to address that complaint.

Now when you use voice mode, it can turn to the company's Sonnet and Opus models for help. Provided you pay for Claude access, the tool will default to the last system you used for text chat. You can also switch between Haiku, Sonnet or Opus mid-conversation through the model picker. "Voice mode uses the fastest version of whichever model you've selected, so the conversation runs smoothly," Anthropic notes. Additionally, voice mode can now pull context from connected apps such as Gmail and Slack, as long as you grant Claude permission to do so.

An Anthropic spokesperson told Engadget voice mode uses a turn-based architecture, so all interactions will see Claude listen to you, pause to think and then respond. It's not fully duplex like OpenAI's new GPT-Live system, which can simultaneously process speech and generate an output. In practice, that should make talking to Claude feel less natural than ChatGPT. Another limitation of Claude's voice mode is that it can't automatically detect the language you're speaking in if you decide to switch languages mid-conversation. You need to either tell it out loud you're about to switch or select the language you're about to speak in from the voice settings menu. However, Anthropic has added support for additional languages, including Indonesian.

"This release is focused on intelligence and tool access," Anthropic told Engadget. "We're continuing to invest in voice and we'll have more to share later this year."

Anthropic is rolling out the new voice mode in beta to all users across its desktop and mobile apps, as well as web client. If you're using Claude through a free account, Anthropic will limit you to a single connection and your prompts will all go through Haiku, though you can speak to Claude in all of the languages voice mode now supports.