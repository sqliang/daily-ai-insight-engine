---
title: Alexa Plus is getting an AI update to handle more complicated instructions
source: https://www.theverge.com/tech/970399/amazon-alexa-plus-ai-update-smart-home-devices
author:
- '[[Emma Roth]]'
published: '2026-07-23'
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
description: Amazon is launching an update to its Alexa Plus assistant that will allow
  it to connect to smart home devices in new ways. With the update, which is currently
  in preview, Alexa Plus can link up with tech from Bosch, Delta, Ecovacs, iRobot,
  Yale Home, Whirlpool, Tapo, Eufy, and others, while automatically routing requests
  to [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a6e6ed7cc55ba5af
source_type: news_media
tldr: Amazon 为 Alexa Plus 推送 AI 更新，使其能够连接 Bosch、iRobot 等更多品牌的智能家居设备，并处理多步骤的复杂指令。Amazon
  同时采用 MCP 协议吸引更多第三方服务接入，Priceline 等将在今年晚些时候上线集成。
objective_summary: Amazon 于 2026 年 7 月向 Alexa Plus 推送了一项 AI 更新，目前处于预览阶段。该更新让 Alexa
  Plus 能够以新方式连接 Bosch、Delta、Ecovacs、iRobot、Yale Home、Whirlpool、Tapo、Eufy 等品牌的智能家居设备，并自动将用户语音请求路由到正确的设备并选择合适的模式。Amazon
  基于新推出的 AI 开发者工具包实现了这些集成，并正在采用开放标准 Model Context Protocol（MCP）来降低设备制造商和第三方服务的接入门槛。Canva、Headspace、Priceline、Lyft、Cengage、Virgin
  Atlantic 等公司计划在今年晚些时候推出集成，其中 Priceline 将支持用户通过 Alexa Plus 浏览酒店并完成预订。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Amazon
  - Bosch
  - Delta
  - Ecovacs
  - iRobot
  - Yale Home
  - Whirlpool
  - Tapo
  - Eufy
  - Ticketmaster
  - OpenTable
  - Uber
  - Thumbtack
  - Expedia
  - Yelp
  - Square
  - Angi
  - Canva
  - Headspace
  - Priceline
  - Lyft
  - Cengage
  - Virgin Atlantic
  - Weekend
  - Atom Tickets
  - Fandango
  - Taskrabbit
  technologies:
  - MCP
  - Model Context Protocol
  key_people: []
key_logic_flow:
- Amazon 向 Alexa Plus 推送了 AI 更新，支持以新方式连接 Bosch、iRobot 等多家品牌的智能家居设备，并自动将用户请求路由到正确的设备。
- 该更新基于 Amazon 新推出的 AI 开发者工具包，使设备制造商能够为 Alexa Plus 开发此前不支持的特殊功能集成。
- Amazon 在 2 月正式发布了重做的 AI 助手 Alexa Plus，支持多步骤请求处理和语音创建自动化例程。
- Amazon 正在采用开放标准 Model Context Protocol（MCP），以降低第三方服务接入 Alexa Plus 的技术门槛。
- Canva、Headspace、Priceline、Lyft 等公司计划在今年晚些时候推出 Alexa Plus 集成，其中 Priceline 将支持通过 Alexa
  Plus 浏览酒店和直接预订行程。
object_mentions:
- object_type: product
  name: Alexa Plus
  canonical_name: Amazon Alexa Plus
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Amazon 为 Alexa Plus 推出了 AI 更新，使其能够连接更多品牌的智能家居设备并处理多步骤的复杂指令。
  - Alexa Plus 已支持 Ticketmaster、OpenTable、Uber、Expedia 等第三方服务，可通过语音完成预订和叫车等任务。
  - Priceline 将在今年晚些时候让用户通过 Alexa Plus 浏览酒店选项并直接完成预订，同时支持 Amazon Wallet 支付。
  article_id: a6e6ed7cc55ba5af
- object_type: project
  name: Model Context Protocol
  canonical_name: Model Context Protocol (MCP)
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Amazon 正在采用 Model Context Protocol（MCP），这是一项允许 AI 模型连接到外部系统和工具的开源标准。
  - Amazon 通过采用 MCP 协议让更多品牌能够与 Alexa Plus 交互，Canva、Headspace、Lyft 等公司将在今年晚些时候推出集成。
  article_id: a6e6ed7cc55ba5af
extract_result: success
impact_score:
  score: 3.5
  reason: Alexa Plus 的功能更新属于产品层面的渐进式改进，而非技术范式的突破。其核心变化在于扩大了设备兼容范围（Bosch、iRobot 等品牌）和指令处理能力（多步骤路由），但这些能力在
    2026 年已是主流 AI 助手的标配。真正有意义的信号是 Amazon 采用 MCP 开放协议——这为第三方服务接入提供了标准化的技术路径，但文章并未披露具体的性能数据或用户体验改善指标。综合来看，对
    Alexa 生态用户有直接价值，但对整个 AI 行业竞争格局的冲击力有限，不足以改变当前语音助手市场的力量分布。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: MCP 协议集成与第三方服务接入的实际开发复杂度
hype_assessment:
  level: medium
  reason: 文章使用'AI update'和'handle more complicated instructions'等措辞营造技术升级感，但实际内容主要是扩大设备品牌兼容列表和第三方合作预告。'AI
    更新'的包装程度超过了技术创新本身的分量——多步骤指令路由是 2026 年 AI 助手的基线能力，并非突破性进展。MCP 的采用是更值得关注的底层变化，但在报道中被简化为一段背景信息，整体存在一定程度的
    PR 包装。
information_entropy: medium
domain_disruption:
  technical_innovation: 采用 Model Context Protocol (MCP) 开放标准作为 AI 模型与外部系统/工具的连接协议，降低了第三方服务接入语音助手的集成门槛，使设备制造商能为
    Alexa Plus 开发此前不支持的独特功能。
  business_model: 通过 MCP 开放标准扩大第三方服务生态（Canva、Priceline、Lyft 等），将 Alexa Plus 从智能家居控制器扩展为语音驱动的消费服务平台（旅行预订、票务、出行），并借
    Amazon Wallet 打通支付闭环，强化平台经济的交易抽成模式。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: Alexa Plus 此次更新的核心价值在于 Amazon 对 MCP（Model Context Protocol）的采纳。从 VC 视角看，这不仅是产品迭代，更是平台战略的质变——MCP
    作为开放标准从根本上降低了第三方服务接入的技术壁垒，将 Alexa 从封闭的语音助手转向开放的 Agent 平台。这种架构选择可能产生网络效应：接入的服务越多，Alexa
    越智能→用户越依赖→吸引更多开发者。但需清醒认识两点：一是语音交互的 consumer adoption curve 历来低于资本预期，Amazon 在 Alexa
    上已投入十年仍未实现真正的杀手级场景；二是 MCP 本身是 Anthropic 主导的开放协议，Amazon 的采纳在强化自身生态的同时也在为竞争对手铺路。综合来看，长期复利潜力存在但需持续
    2-3 年验证对话式 Agent 平台是否真正能跑通 PMF。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Amazon
- Anthropic
- Bosch
- iRobot
- Priceline
- Lyft
competitive_casualty:
- Google Assistant
- Apple Siri
- Samsung SmartThings
- 中小型语音 AI 创业公司
market_opportunities:
- MCP 协议集成服务商可抓住 Amazon 背书带来的标准化机遇，为中小品牌和设备制造商提供一键接入 Alexa Plus 及后续 AI 助手的桥梁方案，形成
  SaaS 订阅或按调用计费的商业模式
- 智能家居设备厂商可借助 Amazon AI 开发者工具包快速补齐此前不支持的独特功能集成，在语音控制体验上形成差异化卖点，尤其是洗衣机、扫地机器人等复杂操作场景
- 语音电商与支付闭环赛道迎来新入局机会——Priceline 等已展示通过 Alexa Plus 完成酒店浏览到预订的全流程，旅游、票务、本地生活服务商可直接复用以
  Amazon Wallet 为基座构建语音交易能力
risk_matrix:
  regulatory: 语音助手在全天候监听场景下涉及用户隐私数据采集与存储，面临 GDPR、CCPA 及中国《个人信息保护法》等多法域合规压力；Amazon
    Wallet 接入第三方支付可能触发金融监管审查
  technological: MCP 协议仍处于早期普及阶段，若未能形成广泛行业共识或被竞争对手另立标准，Amazon 的平台壁垒可能反而被削弱；语音指令在复杂设备场景下的意图识别准确率仍是技术瓶颈
  competitive: Apple（Siri + HomeKit）、Google（Google Assistant + Matter）同步推进类似能力，且 Matter
    协议在智能家居互联互通上有先发优势；Alexa Plus 每月 19.99 美元的订阅模式在面对免费竞品时可能限制用户增长
  ethical: 语音助手持续监听可能引发家庭隐私边界争议，尤其当涉及儿童时；智能家居设备被远程攻破将带来物理安全威胁；MQTT/MCP 通道若权限控制不当可能导致第三方服务越权访问用户数据
  additional:
  - 智能家居设备品牌碎片化严重，每新增一个品牌集成都需要单独的对接工作，规模化扩展的边际成本短期内难以摊薄
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: Alexa Plus
  canonical_name: Amazon Alexa Plus
  url: null
  positioning: Amazon 推出的新一代 AI 语音助手，能够处理多步骤复杂指令、自动跨品牌路由智能家居设备请求，并集成第三方服务完成预订与支付任务，正通过
    MCP 开放协议拓展服务生态。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 智能家居用户
  - 追求语音自动化体验的消费者
  - Amazon 生态活跃用户
  product_signal: 此次 AI 更新让 Alexa Plus 能够以新方式连接 Bosch、iRobot 等多个品牌的智能家居设备，自动将用户语音请求路由到正确设备并选择合适的运行模式。
  market_signal: Priceline、Lyft、Canva、Headspace、Virgin Atlantic 等多家公司计划在今年晚些时候推出 Alexa
    Plus 集成，其中 Priceline 将支持通过 Alexa Plus 浏览酒店并直接完成预订和支付。
  differentiation: 不同于传统语音助手仅执行单步简单指令，Alexa Plus 能处理多步骤复杂请求并自动决策设备模式选择，同时通过 MCP 开放协议显著降低第三方服务集成门槛。
  watch_reason: Amazon 正通过 AI 更新和 MCP 开放协议将 Alexa Plus 从封闭语音助手转型为开放智能家居控制平台，其跨品牌设备控制能力和第三方服务生态的扩展速度将直接决定与
    Google Home、Apple HomeKit 的竞争格局，值得持续跟踪其生态建设进展。
  risk_notes:
  - Alexa Plus 的智能家居设备集成目前仍处于预览阶段，跨品牌交互的可靠性和稳定性有待大规模用户验证。
  - 第三方服务集成（如 Priceline 预订、Amazon Wallet 支付）计划于今年晚些时候上线，实际落地时间和覆盖范围存在不确定性。
  score: 7.0
  article_ids:
  - a6e6ed7cc55ba5af
  evidence_snippets:
  - Amazon 为 Alexa Plus 推出了 AI 更新，使其能够以新方式连接 Bosch、iRobot、Delta 等多个品牌的智能家居设备，并自动将用户语音请求路由到正确的设备。
  - Alexa Plus 当前已支持多家第三方服务，包括 Ticketmaster、OpenTable、Uber 和 Expedia，用户可以通过语音命令完成预订餐厅、叫车和购买门票等日常任务。
  - Priceline 将在今年晚些时候让用户通过 Alexa Plus 浏览酒店选项并直接完成预订，同时支持通过 Amazon Wallet 完成支付，无需跳转到其他应用。
- object_type: project
  name: Model Context Protocol
  canonical_name: Model Context Protocol (MCP)
  url: null
  positioning: 一项允许 AI 模型连接到外部系统和工具的开源标准协议，由 Anthropic 提出，被 Amazon 采用以降低第三方服务接入 Alexa
    Plus 的技术门槛，推动 AI 开放生态建设。
  technical_signal: MCP 作为开放标准协议为 AI 模型与外部系统之间的交互定义统一接口，Amazon 将其用于 Alexa Plus 以降低设备制造商和第三方服务的集成复杂度。
  adoption_signal: 除 Amazon 外，Canva、Headspace、Priceline、Lyft、Virgin Atlantic 等多家公司计划在今年晚些时候基于
    MCP 协议推出 Alexa Plus 集成服务，产业采用正在加速。
  ecosystem_relevance: MCP 协议作为连接 AI 模型与外部工具的通用标准，正在成为 AI 开放生态的关键基础设施组件，Amazon 在消费级
    AI 领域的采用将显著提升其行业影响力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: MCP 协议正从开发者工具标准扩展为消费级 AI 平台的接入协议，Amazon Alexa Plus 的采用标志着其从开发社区走向大规模产业落地，值得持续跟踪其能否成为
    AI 时代系统集成的通用标准。
  risk_notes:
  - MCP 协议目前仍处于早期采用阶段，不同厂商的实际集成效果和标准化程度有待验证。
  - Amazon 对 MCP 的采用可能包含定制化改造，协议的通用性和厂商中立性面临被单一厂商锁定的潜在风险。
  score: 6.0
  article_ids:
  - a6e6ed7cc55ba5af
  evidence_snippets:
  - Amazon 正在采用 Model Context Protocol（MCP），这是一项允许 AI 模型连接到外部系统和工具的开源标准，Amazon 借此协议让更多品牌与
    Alexa Plus 实现交互集成。
  - Canva、Headspace、Priceline、Lyft 和 Virgin Atlantic 等多家知名公司计划在今年晚些时候基于 MCP 协议推出 Alexa
    Plus 集成服务，从而大大拓展语音助手的功能边界。
---

Amazon is launching an update to its Alexa Plus assistant that will allow it to connect to smart home devices in new ways. With the update, which is currently in preview, Alexa Plus can link up with tech from Bosch, Delta, Ecovacs, iRobot, Yale Home, Whirlpool, Tapo, Eufy, and others, while automatically routing requests to the correct device.

# Alexa Plus is getting an AI update to handle more complicated instructions

Amazon’s upgraded AI assistant will be able to do more across a wider range of smart home devices.

Amazon’s upgraded AI assistant will be able to do more across a wider range of smart home devices.

In an example shared by Amazon, a person with a supported washing machine can say, “Alexa, my kid’s soccer jersey could use a deep clean, but the tag says cold wash only.” From there, Alexa Plus would navigate the washer’s cycle options and choose the correct setting. The new integrations are powered by Amazon’s new AI developer toolkit, which is supposed to make it easier for device makers to connect to Alexa Plus, “including those with unique capabilities that weren’t supported before.”

Amazon widely launched its revamped AI assistant in February, which can handle multi-step requests and help you create routines using your voice. It currently only performs tasks in a limited number of third-party services, such as Ticketmaster, OpenTable, Uber, Thumbtack, Expedia, Yelp, Square, and Angi.

But Amazon is trying to change this by adopting the Model Context Protocol (MCP), an open-source standard that allows AI models to connect to external systems and tools. This will give more brands the ability to interact with Alexa Plus, with Canva, Headspace, Priceline, Lyft, Cengage, Virgin Atlantic, Weekend, and other companies launching integrations later this year.

For example, Priceline will give customers the ability to browse hotel options and book a trip directly through Alexa Plus. Priceline, along with Atom Tickets, Cengage, Fandango, and Taskrabbit, will soon support payments through Amazon Wallet as well.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.