---
title: 'Monetization Gateway: Charge for any resource behind Cloudflare via x402'
source: https://blog.cloudflare.com/monetization-gateway/
author:
- '[[soheilpro]]'
published: '2026-07-01'
created: '2026-07-02'
description: 'Article URL: https://blog.cloudflare.com/monetization-gateway/ Comments
  URL: https://news.ycombinator.com/item?id=48746914 Points: 296 # Comments: 209'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cb51fdc1bab74ebe
manifest_dates:
- '2026-07-02'
source_type: community_discussion
tldr: Cloudflare 发布了 Monetization Gateway（货币化网关），允许客户对 Cloudflare 保护下的任何资产（网页、数据集、API
  或 MCP 工具）通过 x402 协议收取稳定币小额支付。该网关在边缘处理支付验证，无需买家注册账户或卖家搭建计费系统，目标是将 HTTP 请求本身变为一笔交易。
objective_summary: Cloudflare 于 2026 年 7 月 21 日宣布推出 Monetization Gateway，这是一套基于 x402
  开放协议的支付引擎，使 Cloudflare 客户能够对网页、数据集、API 和 MCP 工具等受 Cloudflare 保护的资产收取使用费。该网关提供统一的支付策略控制面，在边缘处理支付验证与执行，无需买家提前注册或卖家自建计费系统。支付通过
  OpenUSD 和 USDC 等稳定币结算，支持低至美分以下的小额交易，结算时间在秒级以内。Cloudflare 正与超过 25 家行业领导企业通过 x402
  Foundation 共同建设该开放协议。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Cloudflare
  - x402 Foundation
  technologies:
  - x402
  - Monetization Gateway
  - Web Bot Auth
  - stablecoins
  key_people: []
key_logic_flow:
- Cloudflare 宣布推出 Monetization Gateway，允许客户对受 Cloudflare 保护的任何资产（网页、数据集、API、MCP 工具）收取使用费。
- 该网关基于 x402 开放协议，通过 HTTP 402 Payment Required 状态码实现请求级支付，买家无需提前注册或持有 API 密钥。
- 支付通过 OpenUSD 和 USDC 等稳定币结算，支持低至美分以下的小额交易，结算时间在秒级以内且无拒付风险。
- Cloudflare 表示正与超过 25 家行业领导企业通过 x402 Foundation 共同建设 x402 开放协议。
- 网关提供灵活支付规则 API，支持按 REST 动词定价、按任务复杂度可变定价、仅对未认证调用者收费等策略。
- Cloudflare 认为随着 AI Agent 成为互联网主要使用者，基于使用量的按需定价将取代传统的广告和订阅模式。
extract_result: success
object_mentions:
- object_type: product
  name: Cloudflare Monetization Gateway
  canonical_name: Cloudflare Monetization Gateway
  url: https://blog.cloudflare.com/monetization-gateway/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cloudflare 宣布推出 Monetization Gateway，该引擎允许客户对受 Cloudflare 保护的任何资产（网页、数据集、API 或
    MCP 工具）收取费用。
  - 该网关提供统一的支付策略控制面，在边缘处理支付验证与执行，无需买家注册或卖家自建计费系统。
  - 网关会提供一个灵活支付规则 API，允许客户精确表达何时要求调用者付费访问其数字资源。
  article_id: cb51fdc1bab74ebe
- object_type: project
  name: x402
  canonical_name: x402
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - x402 是一个开放协议，使得通过 HTTP 进行支付成为可能，协议名称源自 HTTP 402 Payment Required 状态码。
  - Cloudflare 正与超过 25 家行业领导企业通过 x402 Foundation 共同建设 x402 开放协议。
  - x402 支付流程中买家支付后附上支付证明重复请求，验证方验证后服务器返回资源，无需重定向到结账页面。
  article_id: cb51fdc1bab74ebe
impact_score:
  score: 7.5
  reason: Cloudflare 凭借其在全球 330+ 数据中心的边缘网络优势，将支付验证直接嵌入代理层，大幅降低了内容/API 按用量收费的实施门槛。这是
    HTTP 402 状态码自 1998 年定义以来首次获得实质性的大规模基础设施支持。结合 x402 开放协议（已有 25+ 行业伙伴加入基金会）和稳定币（USDC/Open
    USD）微支付，可能从根本上改变 AI 代理时代的网络经济模型。但实际采用取决于双边市场的同步增长——内容提供方需要设置定价，AI 代理运营商需要集成支付客户端——短期
    6-12 个月内属于早期采用阶段，不会立即改变行业格局。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 如何利用 Cloudflare 边缘为 API、数据集和 MCP 工具设置按用量微支付，无需自建计费系统
hype_assessment:
  level: medium
  reason: 文章构建了'AI 代理成为互联网主导用户'的宏大叙事来铺垫产品必要性，使用了'evolving business model'、'new era'等框架性包装语言，带有一定前瞻性断言。但产品本身是真实可用的基础设施服务，x402
    协议已获 25+ 行业合作伙伴支持，Cloudflare 有实际的技术能力和网络规模支撑该产品落地，并非空泛的概念炒作。命名'Monetization Gateway'和叙事框架存在营销包装成分，但核心价值主张扎实。
information_entropy: medium
domain_disruption:
  technical_innovation: 在 CDN/反向代理层原生集成 HTTP 402 Payment Required 支付验证流程，将支付凭证作为请求准入条件，实现边缘侧秒级稳定币结算，并计划未来合并身份验证（Web
    Bot Auth）与支付验证为单一请求流水线
  business_model: 将互联网内容/API 的经济模式从广告+订阅转向无摩擦的按请求/按 Token 微支付，打破'低于一定金额收款成本高于收款价值'的历史困境，让网站、API、数据集能直接向
    AI 代理按实际用量收费，消除注册账户和 API Key 的前置摩擦
engineering_complexity: infrastructure
compound_value:
  score: 8.5
  reason: Cloudflare 利用其反向代理的中间人位置插入支付层，这是其独有的战略优势——AWS CloudFront、Akamai、Fastly 虽有边缘网络但缺了'安全+CDN+支付'三位一体的生态协同。核心逻辑：1）AI
    代理成为互联网主要用户后，按请求/按 Token 的用量付费将从可选变为必需，Monetization Gateway 解决了'无账户买家如何进行秒级微支付'这一关键瓶颈；2）支付验证在边缘完成，卖家无需自建计费系统、无需
    onboarding 买家，大幅降低 usage-based pricing 的实施门槛，这直接打开了长尾内容/API/MCP 工具的变现市场；3）双边网络效应显著——越多卖家配置支付规则，越多代理买家需要在
    Cloudflare 网络上持有支付凭证，形成锁定；4）x402 开放协议策略降低了生态协调成本，但 Cloudflare 作为最大部署者仍处于最佳价值捕获位置。风险点：稳定币监管不确定性、代理经济规模化速度可能慢于预期、AWS
    等竞品可能快速跟进。整体来看这是一个面向 AI 代理时代的基础设施级机会，具备强复利效应，但 adoption 曲线仍需验证。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Cloudflare
- Circle (USDC)
- Anthropic
- OpenAI
- x402 Foundation
competitive_casualty:
- Akamai
- Fastly
- AWS CloudFront
- Stripe/PayPal（微支付场景）
- 依靠免费抓取内容的 AI 爬虫
market_opportunities:
- MCP 工具和 API 提供商可直接利用 Monetization Gateway 实现按调用量计费，无需自建计费系统，大幅降低小微开发者和独立开发者的变现门槛
- 内容创作者和数据集所有者可为 AI 爬虫设置按页/按条收费的定价策略，将原本被无偿抓取的数据资产转化为持续收入流
- AI Agent 开发框架和浏览器可集成 x402 协议支付能力，使其 Agent 具备自主完成微支付的能力，催生 Agent 原生经济生态
risk_matrix:
  regulatory: 稳定币微支付面临多司法管辖区监管不确定性——美国各州货币传输牌照要求、欧盟 MiCA 合规成本、以及跨境支付的反洗钱（AML）义务可能限制
    Cloudflare 全球部署速度；若 x402 被认定为支付服务提供商，可能触发更严格的金融监管
  technological: x402 协议尚处于早期阶段（由 x402 Foundation 推动），生态成熟度和客户端/服务端 SDK 覆盖率不足；买家端钱包集成和稳定币流动性问题可能阻碍实际采用；若协议设计存在性能瓶颈或安全漏洞，可能影响支付验证的实时性
  competitive: Stripe、PayPal 等成熟支付平台可能快速跟进推出类似的 HTTP 级别微支付方案；AWS CloudFront + AWS
    Billing 组合可能推出竞争性产品；CDN 边缘支付这一差异点可能被竞争对手快速复制，Cloudflare 的先发优势窗口有限
  ethical: 按用量付费模式可能加剧数字鸿沟——资金充裕的 AI 公司和研究机构可无障碍访问付费内容，而小型独立开发者和学术机构可能被挤出；Agent 自主支付可能引发自动化消费失控问题（无人类审核的累计支出），需建立支出上限和审计机制
  additional:
  - 集中化风险：绑定 Cloudflare 网络意味着客户业务对单一 CDN 基础设施的依赖加深，一旦 Cloudflare 服务中断或政策变更，支付驱动的业务模型将直接受损
  - 提现与汇率风险：稳定币结算虽然秒级完成，但法币出入金通道仍依赖传统银行系统，大规模变现可能遭遇流动性瓶颈或合规审查延迟
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: Cloudflare Monetization Gateway
  canonical_name: Cloudflare Monetization Gateway
  url: https://blog.cloudflare.com/monetization-gateway/
  positioning: 基于 x402 开放协议的边缘支付引擎，让 Cloudflare 客户对受保护的网页、API、数据集和 MCP 工具收取稳定币小额使用费。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 内容创作者和网站所有者
  - API 提供方
  - 数据集拥有者
  - MCP 工具开发者
  product_signal: 在边缘处理支付验证与执行，买家和卖家均无需自建计费系统或提前注册账户。
  market_signal: 针对 AI Agent 成为互联网主要使用者的趋势，用基于使用量的按需定价取代传统广告和订阅模式。
  differentiation: 利用 Cloudflare 全球网络的代理层位置，在 HTTP 请求层面直接完成支付验证与资源交付。
  watch_reason: Cloudflare 将全球 CDN 网络转化为支付基础设施，可能重塑 AI 时代内容与数据的经济模型，值得持续跟踪其开发者采用率和实际支付场景落地。
  risk_notes:
  - 稳定币监管政策在全球范围内存在不确定性，可能影响网关的合规运营。
  - 买家和开发者对 HTTP 402 支付模式的接受度尚未得到大规模验证。
  score: 7.0
  article_ids:
  - cb51fdc1bab74ebe
  evidence_snippets:
  - Cloudflare 宣布推出 Monetization Gateway，该引擎允许客户对受 Cloudflare 保护的任何资产（网页、数据集、API 或
    MCP 工具）收取费用。
  - 该网关提供统一的支付策略控制面，在边缘处理支付验证与执行，无需买家注册或卖家自建计费系统。
  - 网关会提供一个灵活支付规则 API，允许客户精确表达何时要求调用者付费访问其数字资源。
- object_type: project
  name: x402
  canonical_name: x402
  url: null
  positioning: 基于 HTTP 402 Payment Required 状态码的开放协议，使任意 HTTP 请求可直接附带支付并完成点对点资源交付。
  technical_signal: 在 HTTP 层面设计请求-支付-验证-交付的闭环流程，无需重定向到外部结账页面或调用独立支付 API。
  adoption_signal: 超过 25 家行业领导企业正通过 x402 Foundation 共同建设该协议，Cloudflare 已基于此协议落地 Monetization
    Gateway。
  ecosystem_relevance: 为 AI Agent 经济提供原生支付基础设施，填补互联网从注意力经济向使用量经济转型中的支付协议空白。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: x402 有潜力成为 AI Agent 时代互联网支付的标准化协议，其开放的联盟治理模式和多行业参与度为广泛采用奠定了基础。
  risk_notes:
  - HTTP 402 作为新兴支付协议，缺乏经过大规模验证的生产环境案例。
  - 协议成功依赖于联盟成员的实际落地意愿和互操作性实现质量。
  score: 7.0
  article_ids:
  - cb51fdc1bab74ebe
  evidence_snippets:
  - x402 是一个开放协议，使得通过 HTTP 进行支付成为可能，协议名称源自 HTTP 402 Payment Required 状态码。
  - Cloudflare 正与超过 25 家行业领导企业通过 x402 Foundation 共同建设 x402 开放协议。
  - x402 支付流程中买家支付后附上支付证明重复请求，验证方验证后服务器返回资源，无需重定向到结账页面。
---

Today, we are announcing the Cloudflare Monetization Gateway, an engine that will give Cloudflare customers the ability to charge for any asset protected by Cloudflare: web pages, datasets, APIs, or MCP tools.

It will provide a single control plane to manage payment policies and access controls across your applications, while also protecting your origin from high payment volumes by handling payment verification and enforcement at the edge. At launch, payments will settle in stablecoins over__ x402__, the open protocol __we are building__ with a coalition of more than 25 industry leaders via the __x402 Foundation__.


### The evolving business model of the web

For 30 years, the web has run on a simple economic bargain: trading content for human attention. That attention has been monetized through advertising, subscriptions, and e-commerce. This bargain funded the Internet as we know it.

But as agents become the dominant Internet users, the model is breaking. An agent does not look at ads or need to maintain a monthly subscription to all the tools it wants to access. It reads a page or consumes a data feed once, takes what it needs, and moves on. Across the web, AI crawlers already request content anywhere from a hundred to tens of thousands of times for every visitor they __send back__.

This reality demands a new model: usage-based pricing for everything. If attention and e-commerce are moving from websites to AI harnesses and AI-written software, then agents should pay for the inputs they need — training data, inference content, developer tooling, and API usage. The natural unit of payment for software is the request, the token, or the outcome, not the seat or the month. A few examples of what that could look like:

A few cents per web search, billed per call

\$0.001 base fee plus a \$0.01 per MB charge for an upload endpoint

\$0.99 per resolved support escalation, paid only when the work succeeds


This is the same shift behind __paying creators when an answer engine uses their content__ — a fair exchange of value whenever content or a resource is used, priced on neutral rails built for the purpose. People often envision an agent buying high-priced assets like web domains, but most of what an agent pays for sits upstream of any checkout, and is priced far lower.

Some of the Internet already works this way. Cloud and APIs have been sold by the call and by the hour for years, but only to a known buyer: a user signs up, they are issued an API key, and they incur usage-based metered billing. Content mostly skipped payment and ran on advertising instead. These business models have never been able to serve unverified buyers for sub-cent transactions because __the payment rails__ cost too much and took too long to settle. Below a certain price, collecting the payment cost more than the payment was worth.

Historically, usage-based billing was difficult to implement. Businesses needed to effectively become payments companies, running their own accounting to track internal usage in a robust and auditable way. Tracking this usage required significant overhauls of backend systems. Many instead chose per-seat pricing because it is simpler and frequently more profitable.

Agents flip this dynamic. A single agent can do the work of an entire team around the clock, making a flat one-time fee disconnected from actual consumption. At the same time, an agent can make thousands of micropayments without friction, while asking a person to approve each payment would be impossibly burdensome. Usage-based price points are where agents live and where stablecoin-based micropayments shine. That's because stablecoins (such as __Open USD__ and __USDC__) allow buyers to transfer tiny sums across the Internet, incurring negligible fees and settling in less than a second. This is not feasible with other payment rails today.

Here’s where we can help. Cloudflare has spent years building usage-based accounting for our own billing systems and for our customers’ analytics. We can dramatically simplify the implementation of usage-based billing for web-based assets thanks to our position as a proxy layer between buyers and sellers. As shown below, with Cloudflare supporting usage-based billing, the evidence of payment can move into the request itself, and the payment validation and the request paths merge.

And here’s the benefit to you: the metering, the payment exchange, and the settlement move off your origin. What stays with you is what matters — your rules, your prices, and your revenue. You will not need to onboard the buyer or stand up a billing system. You will write a rule and agentic buyers will pay for what they use.


### A refresher on x402

Last year on __Content Independence Day__, we gave site owners one-click control over which AI crawlers could reach their content, and with __Pay Per Crawl__ we let them charge crawlers for it. The Monetization Gateway is the next step: instead of only charging crawlers for content, you will be able to charge any caller for any resource, from an API to data to an MCP tool call, and you will not have to build the payment machinery yourself.

x402 is an open protocol that makes it possible to pay over HTTP, named for the 402 status code it finally puts to use. The x402 exchange is simple: a client requests a payment-gated resource. Instead of serving it, the server responds with 402 Payment Required and a small payload that states the price, the accepted asset, and where to pay. The client pays and repeats the request with proof of payment attached. A facilitator verifies, and the server returns the resource. It all happens inside ordinary HTTP requests and responses, with no redirect to a checkout page and no separate payment API to call. Settlement happens peer-to-peer, so any funds that a buyer sends to a seller are directly deposited to the seller’s wallet. We are designing the Monetization Gateway to keep payment overhead low and are aiming for sub-second payment settlement.

*x402 Payment Flow: AI Agent ↔ APIServer ↔ Blockchain, Source: *__x402 Readme on GitHub__* *

Two properties make x402 a good fit for machine payments. The payment amounts can be small, down to fractions of a cent, because the protocol adds almost no overhead. And the buyer needs no account with the seller, because the payment itself is the credential. x402 is rail agnostic, but it is a natural fit for stablecoins, which can settle in under a second for a fraction of a cent with zero chargebacks.


### What the Monetization Gateway does

The Monetization Gateway will provide a flexible payment rules API that will allow you to express exactly when you want a caller to pay to access your digital resources.

Here’s how it will work. Tokens, APIs, MCP tool calls, and data already flow through that path. You will decide, as precisely as you want, which of that traffic has to pay. And you will be able to enforce your decisions by writing expressions, similar to expressions that you already write for other Cloudflare rules, in a simple, dedicated product API. The Monetization Gateway will scale with Cloudflare’s global network across 330+ cities, which means that the x402 handshake will occur in close proximity to your buyer. This will reduce request latency and protect your origin.

A few examples of planned capabilities:

Charge for specific REST verbs: Require payment on calls to a specific route, for example $0.01 for every GET or POST request to /api/premium/*.

Variable pricing: Charge variable amounts for tasks of varying complexity, for example, image generation might charge any amount up to $2, depending on the compute used.

Charge only unauthenticated callers: Intercept HTTP 401 "Unauthorized" responses from your origin and return 402 "Payment Required" instead with pricing and payment instructions.


When a request matches, the Monetization Gateway will verify payment before letting it through. You will be able to set these rules in the dashboard, or manage them as code through the Cloudflare API and Terraform, so a paid endpoint is just another part of your infrastructure config.

The Monetization Gateway will initially allow users to require buyers to pay for services and resources in stablecoins. Sellers will be able to use the stablecoins they accumulate for their own transactions or redeem the stablecoins for equivalent fiat currency in their bank account. Using the Monetization Gateway offers a way to increase the addressable market for your products. With the Gateway, agents can request your resource, be told the price, pay, and get the response. No signup, no API key, no prior relationship required. You will decide how much you need to know about that buyer, and you will have the flexibility to require agents to authenticate with __Web Bot Auth__ and apply usage-based pricing against accounts they already hold.


### Where we see this going

The Monetization Gateway will turn the request into a payment and give Cloudflare customers new revenue opportunities, but where this goes is far bigger.

An agent is software that acts autonomously on a user’s behalf, and agents are starting to act on their own. Soon they will carry wallets and buy what they need without a person in the loop: a dataset, an API call, a tool, a block of compute. Some of those resources will be free, and some will require proof of who the agent is and who it acts for, through verified agent identity. Many will require both an identity and a payment, and Cloudflare is one of the few places that will be able to settle all of it inside a single request, by verifying the agent, applying the rule, and checking the payment before the origin ever sees the call. The agent becomes the primary buyer on the Internet, and the request becomes the transaction.

There is an enormous amount of value moving across the Internet today that goes unmonetized or undermonetized, not because no one would pay for it, but because the tools to charge for it have never existed. Every useful API call, every answer, every tool invocation an agent makes has value, and almost none of it is paid for today. That is the opportunity in front of us, and it is what the Monetization Gateway will unlock.

This is what we are building toward: an agent-first Internet with Internet-scale settlement built in. Where the people who make something worth paying for get paid by the software that uses it, automatically. And where the smallest new API can reach the same buyers, on the same terms, as the largest company on the web, and the independent creator is paid by the large language models that use their work. That is the next business model of the Internet, and we are building to power it.


### Sign up for our waitlist

The Monetization Gateway waitlist is open now for Cloudflare customers. If you’re interested in monetizing your web page, dataset, API, or MCP tool with usage-based pricing, __please join our early access list__.