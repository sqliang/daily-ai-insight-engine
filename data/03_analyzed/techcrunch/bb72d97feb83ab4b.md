---
title: Binance now lets AI agents trade, but keeping them in check is largely up to
  users
source: https://techcrunch.com/2026/08/20/binance-now-lets-ai-agents-trade-but-keeping-them-in-check-is-largely-up-to-users/
author:
- '[[Jagmeet Singh]]'
published: '2026-08-20'
created: '2026-08-20'
manifest_dates:
- '2026-08-20'
description: Binance's Agent OS works with tools including ChatGPT, Claude Code, and
  Cursor.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bb72d97feb83ab4b
source_type: news_media
tldr: 币安周四推出 Agent OS 平台，让 AI 代理接入其金融基础设施代表用户分析市场并执行交易，兼容 ChatGPT、Codex、Claude Code、Cursor
  及 MCP。风控主要依赖用户，通过默认禁提款的子账户限制代理权限与资金规模。
objective_summary: 币安（全球最大加密货币交易所，注册用户超 3 亿）于 2026 年 8 月 20 日推出 Agent OS 平台，允许开发者将
  AI 应用与代理连接到其金融基础设施，代表用户分析市场并执行交易。平台整合了币安现有 API、Binance Wallet Agentic Hub、x402 交易验证、Binance
  Skill Hub，并新增对 MCP 的支持，兼容 ChatGPT、Codex、Claude Code 和 Cursor。币安通过可配置的专用子账户（默认禁止提款）将访问控制权交给用户，用户可决定代理每笔订单需审批或自主执行，转入子账户的资金即构成交易上限。币安表示无法查看代理交易的推理过程，现有子账户
  API 的安全、风控与反洗钱政策在 Agent OS 上线时同样适用。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Binance
  - OpenAI
  - Anthropic
  technologies:
  - MCP
  - x402
  - AI Agent
  key_people:
  - Jeff Li
key_logic_flow:
- 币安于周四推出 Agent OS 平台，允许开发者将 AI 应用与代理接入其金融基础设施，实现代表用户分析市场和执行交易。
- 该平台整合了币安现有 API、Binance Wallet Agentic Hub、x402 交易验证、Binance Skill Hub，并新增对 Model
  Context Protocol（MCP）的支持。
- Agent OS 兼容 OpenAI 的 ChatGPT 和 Codex、Anthropic 的 Claude Code 以及 Cursor，用户可授权这些代理访问市场数据、查看账户信息并执行交易。
- 币安将风控责任主要交给用户，通过专用子账户对代理进行访问控制，子账户默认禁止提款以形成资金保护沙箱。
- 用户可选择代理每笔订单需审批或配置权限后自主执行，币安不设单独的亏损上限，转入子账户的金额即为实际限制。
- 币安无法查看代理交易的推理过程，只能监控交易结果，对错误信息或操纵的影响可见性有限，子账户是对抗提示注入攻击的主要防线。
object_mentions:
- object_type: product
  name: Agent OS
  canonical_name: Binance Agent OS
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 币安于本周四推出名为 Agent OS 的平台，允许开发者将 AI 应用和代理连接到币安的金融基础设施，让 AI 代理代表用户分析市场并执行交易。
  - Agent OS 将访问控制放在账户级别，用户通过专用子账户为代理配置现货或期货交易权限，默认阻止从子账户提款。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Binance Wallet Agentic Hub
  canonical_name: Binance Wallet Agentic Hub
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent OS 整合了币安现有的 Binance Wallet Agentic Hub 工具，作为连接 AI 代理与币安金融基础设施的组成部分。
  article_id: bb72d97feb83ab4b
- object_type: project
  name: Binance x402
  canonical_name: Binance x402
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent OS 纳入币安 x402 交易验证与支付促进器 API，为 AI 代理的交易执行提供验证能力。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Binance Skill Hub
  canonical_name: Binance Skill Hub
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent OS 整合了币安 Skill Hub，使开发者能够将技能接入到代理的金融操作流程中。
  article_id: bb72d97feb83ab4b
- object_type: project
  name: MCP
  canonical_name: Model Context Protocol (MCP)
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 新增了对 Model Context Protocol（MCP）的支持，并可与 ChatGPT、Codex、Claude Code 和 Cursor
    等工具配合使用。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Codex
  canonical_name: OpenAI Codex
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 OpenAI 的 Codex，用户可授权该代理访问市场数据、查看账户信息并执行交易。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 Anthropic 的 Claude Code，让用户授权代理在币安平台进行市场分析与交易操作。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Cursor
  canonical_name: Cursor
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 Cursor 工具，用户可授权该代理访问市场数据、查看账户信息并执行交易。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 OpenAI 的 ChatGPT，用户可授权该代理访问市场数据、查看账户信息并执行交易。
  article_id: bb72d97feb83ab4b
extract_result: success
impact_score:
  score: 7.2
  reason: 评分依据：币安作为全球最大加密货币交易所（3 亿+注册用户）正式推出 Agent OS，让自主 AI 代理接入真实金融执行链路代表用户交易，是
    AI Agent 从对话/编码场景向'真金白银'场景迈出的标志性一步。短期会显著拉高加密交易赛道对 agentic 能力的军备竞赛，并倒逼 Coinbase
    等对手加速跟进；同时它对 MCP 的原生支持使其天然嵌入 ChatGPT/Claude Code/Cursor 等主流工具生态，开发者接入门槛低。但该事件本质是应用层能力整合（现有
    API + MCP + x402 + 子账户沙箱的编排），并未引入新的底层技术范式；且风控责任大幅下放给用户、对提示注入与错误信息影响的可见性有限，削弱了短期冲击的烈度，属'重要产品发布、改变局部竞争格局'档位。综合评分
    7.2。
sentiment: mixed
developer_sentiment:
  tone: excited
  primary_focus: MCP 支持让开发者能用 Claude Code/Cursor 等熟悉工具构建交易代理，但子账户资金隔离、无独立亏损上限与提示注入防护边界仍是关注焦点
hype_assessment:
  level: medium
  reason: 评分依据：文章报道本身冷静克制，如实披露了'币安无法查看代理推理过程''风控主要靠用户''子账户是对抗提示注入的主要防线'等短板，未见'颠覆''革命'等
    PR 滥用词汇，可信度较高。但事件本身带有一定包装——'Agent OS'这一操作系统式命名有夸大成分，'让自主 AI 直接管理真实资金'的表述也刻意拔高了叙事张力；实际产品本质仍是既有
    API 与权限沙箱的组合集成，而非全新范式。因此判定为中等水分。
information_entropy: high
domain_disruption:
  technical_innovation: 通过 MCP 协议将 AI 代理统一接入交易所金融基础设施，结合 x402 交易验证与基于子账户的权限沙箱（默认禁止提款），形成'代理可执行交易但资金不可流出'的架构；其本质是给自主代理套上可编程、细粒度的资金围栏，同时兼容
    ChatGPT/Codex/Claude Code/Cursor 等主流工具链，把代理交易从自定义 API 整合降维成标准协议接入。
  business_model: 币安正从'交易平台'向'AI 代理基础设施提供商'延伸：每次代理自主交易都产生手续费，子账户机制天然限定风险敞口从而可规模化推广；未来可能出现第三方交易代理编排与风控
    SaaS（安全审核、策略评估、合规保险等中间层），推动加密交易走向'代理即服务'模式，并倒逼竞品交易所跟进代理接入能力。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 作为 VC 评估，我分三层看复利潜力：(1) 分发与流动性——币安 3 亿注册用户 + 全球最大加密现货/衍生品流动性池，是 AI 代理执行真实资金操作最现成的落地场景，Agent
    交易一旦形成使用习惯，交易频次与手续费收入将随代理渗透率非线性增长；(2) 协议卡位——新增 MCP 支持并接入 x402 交易验证，使币安同时成为『代理→金融』的标准连接层与支付验证层，二者都随整个
    AI Agent 生态扩张而持续增值，具备基础设施属性；(3) 生态锁定——Skill Hub 与子账户 API 一旦吸引开发者沉淀，迁移成本将形成网络效应，这是典型的复利来源。但扣分项同样明确：风控责任主要下放给用户，币安对代理推理过程无可见性，提示注入等安全缺陷可能触发监管收紧与信任危机；且价值高度绑定单一中心化交易所，受合规与同业竞争不确定性影响大。综合判断：有潜力成为『加密
    Agent 交易』细分赛道的基础设施，但安全模型与合规路径仍需持续验证，故给 7 分而非 8 分以上的『行业基石』级别。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Binance
- Anthropic
- OpenAI
- Cursor (Anysphere)
competitive_casualty:
- 未跟进 Agent 原生接入的加密交易所
- 传统智能投顾与量化策略 SaaS
- 信号跟单与人工理财顾问服务
market_opportunities:
- 针对 AI 代理接入真实资金管理的场景，创业者可开发代理行为审计与风险监控中间件，填补交易所无法查看代理推理过程、只能监控交易结果这一空白
- 币安'专用子账户 + 默认禁提款 + 转账金额即交易上限'的沙箱模式可作为行业参考范式，建议在自有金融产品或企业代理平台中复制'资金边界即风险边界'的设计
- 围绕 AI 交易代理的提示注入防护、权限校验与安全评测服务存在明确市场缺口，可面向交易所、经纪商与量化团队提供针对性的安全工具与合规评估方案
risk_matrix:
  regulatory: AI 代理自主执行交易涉及 KYC/AML、投资者保护与交易责任归属的监管空白，欧盟 MiCA 与 AI Act 对金融领域高风险 AI
    的合规要求可能收紧；币安本身在多国面临监管压力，Agent OS 上线可能进一步引发监管质询。
  technological: 代理推理完全发生在币安系统之外，提示注入攻击与错误信息操纵难以被监测；MCP 协议、工具调用权限校验及子账户 API 隔离机制的安全性和可靠性仍需真实资金场景的实战检验。
  competitive: Coinbase、OKX 等头部交易所及 DeFi 协议可能快速跟进同类 AI 代理交易服务，引发费率与生态竞争；OpenAI、Anthropic
    等模型厂商也可能向上游切入金融代理执行层，挤压中间环节价值。
  ethical: 自主交易代理可能放大散户的非理性交易与亏损风险，用户对 AI 能力的过度信任易造成财务损失；代理被操纵或故障时责任主要归于用户，存在公平性与消费者保护问题；代理基于相似数据源的趋同决策可能扰动市场。
  additional:
  - 多个 AI 代理基于相似数据源与模型可能产生交易行为趋同，形成市场层面的系统性关联风险，放大异常波动
  - 代理错误交易或提示注入导致用户损失时的责任界定与保险保障仍属空白，平台责任豁免条款可能使用户维权困难
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: Agent OS
  canonical_name: Binance Agent OS
  url: null
  positioning: 币安推出的连接 AI 代理与其金融基础设施的平台，允许代理代表用户分析市场并执行交易，通过子账户实现账户级访问控制与资金保护。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 应用与代理开发者
  - 加密货币交易者
  - 币安注册用户
  product_signal: 平台整合币安 API、Wallet Agentic Hub、x402 验证与 Skill Hub，并新增对 MCP 的支持，兼容
    ChatGPT、Codex、Claude Code 与 Cursor。
  market_signal: 币安作为全球最大加密货币交易所、注册用户超 3 亿，正式将自主 AI 代理引入真实资金管理场景，标志交易所级 AI 代理交易赛道开启。
  differentiation: 与聊天式 AI 不同，Agent OS 允许代理自主执行真实交易，并以默认禁提款的子账户沙箱取代交易所单方风控，把权限粒度交给用户。
  watch_reason: 币安将自主 AI 代理直接接入真实资金交易，是头部交易所对 Agentic AI 商业化的重要试探；其 MCP 支持与对 ChatGPT、Codex、Claude
    Code 的兼容预示 AI 代理交易基础设施的标准化方向。但风控主要依赖用户自行配置子账户，提示注入与错误决策的可见性有限，值得持续跟踪其安全实践与监管反馈。
  risk_notes:
  - 币安无法查看代理交易的推理过程，对错误信息或操纵影响可见性有限。
  - 风控责任主要落在用户身上，子账户默认禁提款是对抗提示注入攻击的主要防线。
  - 币安不设单独亏损上限，转入子账户的金额即为实际限制，存在资金损失风险。
  score: 9.0
  article_ids:
  - bb72d97feb83ab4b
  evidence_snippets:
  - 币安于本周四推出名为 Agent OS 的平台，允许开发者将 AI 应用和代理连接到币安的金融基础设施，让 AI 代理代表用户分析市场并执行交易。
  - Agent OS 将访问控制放在账户级别，用户通过专用子账户为代理配置现货或期货交易权限，默认阻止从子账户提款。
- object_type: product
  name: Binance Wallet Agentic Hub
  canonical_name: Binance Wallet Agentic Hub
  url: null
  positioning: 币安推出的用于连接 AI 代理与币安金融基础设施的组件工具，是 Agent OS 平台整合的既有能力之一。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 应用与代理开发者
  product_signal: 作为 Agent OS 平台的既有组件，负责打通 AI 代理与币安钱包相关金融能力，被纳入新平台的统一代理连接体系。
  market_signal: null
  differentiation: null
  watch_reason: 作为 Agent OS 整合的既有钱包代理组件，其演进反映币安如何将分散的代理工具收敛为统一金融代理平台，对判断交易所 Agent
    基础设施方向有参考价值。
  risk_notes:
  - 该组件作为 Agent OS 整合的一部分，独立能力与安全边界尚不清晰，需进一步观察。
  score: 4.0
  article_ids:
  - bb72d97feb83ab4b
  evidence_snippets:
  - Agent OS 整合了币安现有的 Binance Wallet Agentic Hub 工具，作为连接 AI 代理与币安金融基础设施的组成部分。
- object_type: project
  name: Binance x402
  canonical_name: Binance x402
  url: null
  positioning: 币安纳入 Agent OS 的交易验证与支付促进 API，为 AI 代理执行交易提供基于 x402 标准的验证与支付通道。
  technical_signal: x402 作为面向 AI 代理的交易验证与支付促进 API，被币安整合进 Agent OS，用于代理交易执行环节的验证与资金促进。
  adoption_signal: 币安将 x402 纳入全球最大交易所的 Agent OS 平台，标志该标准在头部交易所获得真实落地场景。
  ecosystem_relevance: x402 的整合使 Agent OS 能连接更广泛的代理支付生态，为 AI 代理自主交易提供标准化验证与支付基础设施。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: x402 是面向 AI 代理交易与支付的标准协议，被全球最大交易所币安整合进 Agent OS，标志其从概念走向真实资金场景；其验证与支付模式能否成为代理经济的基础设施值得持续跟踪。
  risk_notes:
  - 关于 x402 的具体实现细节与安全边界，报道披露有限，需关注其验证机制在真实资金场景中的可靠性。
  score: 5.0
  article_ids:
  - bb72d97feb83ab4b
  evidence_snippets:
  - Agent OS 纳入币安 x402 交易验证与支付促进器 API，为 AI 代理的交易执行提供验证能力。
- object_type: product
  name: Binance Skill Hub
  canonical_name: Binance Skill Hub
  url: null
  positioning: 币安提供的技能接入中枢，使开发者能将金融操作技能接入 AI 代理的工作流程，是 Agent OS 平台的组成部分。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 应用与代理开发者
  product_signal: Skill Hub 允许开发者将技能接入代理金融操作流程，配合 Agent OS 形成技能编排与交易执行一体化的代理开发链路。
  market_signal: null
  differentiation: null
  watch_reason: Skill Hub 是 Agent OS 中连接开发者技能与代理金融操作的关键层，其开放程度与技能生态将影响币安代理平台的扩展能力，值得观察后续演进。
  risk_notes:
  - 关于 Skill Hub 的技能接入范围、审核机制与安全限制，报道信息有限，需持续补充。
  score: 4.0
  article_ids:
  - bb72d97feb83ab4b
  evidence_snippets:
  - Agent OS 整合了币安 Skill Hub，使开发者能够将技能接入到代理的金融操作流程中。
---

Binance, the world’s largest crypto exchange with more than 300 million registered users, on Thursday launched a platform that lets AI agents analyze markets and execute trades on users’ behalf, bringing autonomous AI directly into the business of managing real money.

Called Agent OS, the platform lets developers connect AI applications and agents to Binance’s financial infrastructure. It brings the exchange’s existing tools and services such as Binance APIs, Binance Wallet Agentic Hub, Binance x402 transaction verification and payment facilitator API, and Binance Skill Hub, along with newly introduced support for its Model Context Protocol (MCP). The platform also works with tools including OpenAI’s ChatGPT and Codex, Anthropic’s Claude Code, and Cursor, allowing users to authorize agents to access market data, view account information, and execute trades.

However, as the AI race moves away from chatbots that answer questions to agents capable of taking action, Binance is putting much of the responsibility for keeping them in check on users, who ultimately have to decide what agents can access and trade and set limits on what they can do.

“Instead of total freedom, we put the power in users’ hands to give them the granular access control of what they can do through the agent,” said Jeff Li, vice president of product at Binance, in an interview. “We put [the control] at the account level to protect the users’ funds.”

Binance does that primarily through dedicated “sub-accounts”, which users can assign to agents and configure for specific activities, such as spot or futures trading. Withdrawals from those sub-accounts are blocked by default, Li told TechCrunch, creating a sandbox around an agent’s activity.

Users can also choose whether an AI agent must seek approval for every order or can execute trades autonomously once its permissions are configured, a Binance representative said. Binance does not impose a separate cap on how much an AI agent can trade or lose, so the amount a user transfers into the sub-account effectively serves as the limit.

Asked whether Binance can see what leads an agent to make a particular trade, Li said the reasoning happens outside its systems, either on the user’s computer or within their chosen AI application. “We really cannot see the reasoning of what the user’s action is,” he said.

That means Binance can monitor an agent’s resulting trading activity, but has limited visibility into whether a decision was influenced by faulty information or manipulation.

Li again pointed to the sub-account as the main line of defense when asked what would happen if an agent were manipulated through a prompt-injection attack or otherwise compromised. Binance also said its existing security, risk-control, and anti-money-laundering policies for subaccount APIs apply to Agent OS at launch.