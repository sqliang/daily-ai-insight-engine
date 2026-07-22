---
title: Natural raises $30M to reinvent payments for AI agents — and take on Stripe
source: https://techcrunch.com/2026/07/20/natural-raises-30m-to-reinvent-payments-for-ai-agents-and-take-on-stripe/
author:
- '[[Marina Temkin]]'
published: '2026-07-20'
created: '2026-07-21'
manifest_dates:
- '2026-07-21'
description: The one-year-old startup aims to reinvent financial architecture for
  autonomous AI transactions.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cf3c8dfd6c45ed29
source_type: news_media
tldr: AI 代理支付基础设施初创公司 Natural 完成 3000 万美元 Series A 融资，由 Forerunner 领投，累计融资 4000 万美元。该公司构建代理编排层，让
  AI 代理能自主完成支付、收款和资金管理，直接与 Stripe 等传统支付巨头竞争。
objective_summary: Natural 是一家成立于 2025 年的支付基础设施初创公司，由 Kahlil Lalji、Eric Wang 和 Walt
  Leung 联合创立。公司于 2026 年 7 月宣布完成 3000 万美元 Series A 轮融资，由 Forerunner 的 Kirsten Green
  领投，累计融资达 4000 万美元。Natural 定位为 AI 代理的支付编排层，使 AI 代理能够自主完成支付、收款和与人类或其他代理之间的资金交易，旨在解决传统金融系统（如信用卡和
  ACH）依赖人工授权无法支持自主代理的问题。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Natural
  - Forerunner
  - Stripe
  - Ivella
  - Earnin
  - Nextdoor
  - Y Combinator
  technologies:
  - AI Agent
  key_people:
  - Kahlil Lalji
  - Eric Wang
  - Walt Leung
  - Kirsten Green
key_logic_flow:
- Natural 成立于 2025 年，由 Kahlil Lalji、Eric Wang 和 Walt Leung 联合创立，专注于为 AI 代理重建支付基础设施。
- 传统支付系统（如信用卡和 ACH）依赖人工授权进行交易，无法支持需要自主行动的 AI 代理。
- Natural 定位为代理编排层，通过集成其基础设施，企业可以让 AI 代理自主执行支付、收款以及与人类或其他代理之间的交易。
- 公司完成了 3000 万美元的 Series A 轮融资，由 Forerunner 领投，累计融资总额达到 4000 万美元。
- Kahlil Lalji 此前创办的面向夫妻的金融产品 Ivella 于 2023 年被 Earnin 收购。
- Natural 不仅帮助代理代表消费者完成支付和结账，还试图重建包括争议交易处理在内的支付基础设施。
object_mentions:
- object_type: company
  name: Natural
  canonical_name: Natural
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Natural 定位为代理编排层，使 AI 代理能够自主移动和存储资金。
  - 公司完成 3000 万美元 Series A 融资，由 Forerunner 领投，累计融资达 4000 万美元。
  - Natural 不仅帮助代理支付和结账，还试图重建包括争议交易处理在内的支付基础设施。
  article_id: cf3c8dfd6c45ed29
- object_type: company
  name: Ivella
  canonical_name: Ivella
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Kahlil Lalji 此前的创业项目 Ivella 是一个 YC 支持的面向夫妻的银行和金融产品。
  - Ivella 于 2023 年被 Earnin 收购，此后 Lalji 在 Earnin 担任了两年工程师。
  article_id: cf3c8dfd6c45ed29
- object_type: product
  name: Natural Agent Orchestration Layer
  canonical_name: Natural Agent Orchestration Layer
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - Natural 定位为代理编排层，通过集成其基础设施，企业可以让代理自主支付、收款和与人类或其他代理交易。
  article_id: cf3c8dfd6c45ed29
extract_result: success
impact_score:
  score: 6.8
  reason: 该事件属于 AI 基础设施赛道的重要融资，评分 6.8。正面：AI 代理自主支付是真实的结构性瓶颈，天然与 Stripe 等传统支付巨头存在代际差异，Forerunner
    领投说明 VC 认可赛道逻辑。制约：Natural 仅成立一年，产品尚在早期，累计 4000 万美元在支付基础设施领域并不算大额（Stripe 估值超 600
    亿），且需要说服企业客户将支付流从 Stripe 迁移到新平台——执行风险极高。短期不会改变 AI 行业格局，但为代理生态补上了关键缺失的一环。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: AI 代理能否真正脱离人类授权，自主完成支付闭环
hype_assessment:
  level: medium
  reason: 存在一定包装。'take on Stripe'是典型的挑战者叙事，媒体放大了竞争对抗。但'代理支付是最重要的结构性基础设施问题'的判断本身合理，没有使用'颠覆''革命性'等虚词，融资额和团队背景真实可信，核心痛点（传统金融
    Rails 不支持自主代理）有坚实的技术逻辑支撑。
information_entropy: medium
domain_disruption:
  technical_innovation: 为 AI 代理重构支付编排层，核心突破在于用程序化授权机制替代传统金融系统中的人工授权环节（信用卡、ACH 依赖人类签名），使代理能自主完成支付、收款和资金管理，本质上是金融系统接口从
    human-in-the-loop 向 agent-native 的范式切换。
  business_model: 从 AI 代理间交易流水中抽成的 API 计费模式，不直接面向消费者，而是作为企业 AI 系统的底层基础设施。若规模化成功，可能催生'代理经济'的支付标准层，重塑
    SaaS 生态中支付分成的权力结构（从 Stripe 主导的人类支付转向 Natural 主导的代理支付）。
engineering_complexity: prototype
compound_value:
  score: 8.0
  reason: Natural 正在构建 AI Agent 时代的原生支付轨道，这是一个极有可能产生强网络效应和切换成本的赛道。传统支付系统（信用卡、ACH）依赖人工授权，从根本上无法支持自主
    AI 代理执行支付、收款和资金管理——这是结构性瓶颈而非渐进式优化。Natural 的代理编排层一旦被企业采用，将形成双重锁定：一方面 Agent 的行为数据沉淀在
    Natural 的平台上，另一方面支付基础设施的集成成本极高（与银行、合规、争议处理深度耦合），迁移意愿会非常低。Forerunner 领投 3000 万美元
    Series A 表明顶级消费 VC 认为这是'AI 时代的 Stripe'级机会。但需注意：① 公司仅成立 1 年，产品市场契合尚未充分验证；② Stripe
    本身也在快速布局 AI 支付能力（Stripe 2025 年已有 Agent 相关 SDK），巨头反扑风险真实存在；③ 金融基础设施赛道监管门槛极高，合规成本可能侵蚀利润率。综合来看，如果
    Natural 能在 Stripe 反应之前建立足够的网络效应和集成深度，3-5 年后有望成为 AI Agent 经济体不可或缺的基础设施。评分 8.0 反映了高天花板与早期阶段的不确定性之间的权衡。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Natural
- Forerunner
- AI Agent 平台开发者
- Y Combinator
competitive_casualty:
- Stripe
- 传统支付处理器（Adyen、Square）
- 信用卡网络（Visa、Mastercard）
- ACH 依赖型银行基础设施
market_opportunities:
- 关注 AI 代理支付基础设施赛道，面向物流、电商、供应链等垂直行业开发代理自主支付与对账解决方案，抢占 Stripe 尚未覆盖的增量市场
- AI 代理自主交易量的增长将催生新型合规与争议处理工具（如代理行为审计、自动争议仲裁），可切入作为独立 SaaS 产品
- 传统支付服务商（如 Stripe、Adyen、Square）应加速推出 AI 代理感知的支付 API 和代理身份验证能力，以防御新兴公司的颠覆
risk_matrix:
  regulatory: AI 代理自主执行金融交易涉及 KYC/AML 合规、交易责任归属、资金安全等监管问题，全球金融监管框架尚未覆盖自主代理场景，存在重大合规不确定性
  technological: Natural 的产品尚处于早期阶段，大规模交易处理的可靠性、安全性和延迟表现尚未验证；Stripe 等成熟平台可能快速跟进推出竞品，新技术窗口期有限
  competitive: 直接与 Stripe 等支付巨头正面竞争，巨头拥有完善生态、海量商户基础和信任优势；Visa/Mastercard 等卡组织也可能升级网络以支持自主代理交易，挤压中间层空间
  ethical: AI 代理持有并自主支配资金可能引发未授权交易、用户隐私泄露（代理需访问支付凭证），以及算法偏差导致的歧视性金融服务等问题
  additional:
  - AI 代理间交易的欺诈检测和身份验证机制尚未成熟，容易成为新型金融犯罪的目标
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Natural Agent Orchestration Layer
  canonical_name: Natural Agent Orchestration Layer
  url: null
  positioning: 面向AI代理的支付编排层，让AI代理能够自主完成支付、收款和资金管理，与Stripe等传统支付基础设施直接竞争。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 部署AI代理并需要其自主完成支付的企业
  - 构建自主代理电商和供应链应用的开发者
  product_signal: Natural构建了AI代理的支付编排层，企业集成后AI代理可自主执行支付、收款以及争议交易处理，无需人工授权。
  market_signal: 2026年7月完成3000万美元Series A轮融资，由Forerunner领投，累计融资4000万美元，直接与Stripe竞争。
  differentiation: 与依赖人工授权的传统支付系统不同，Natural从头为AI代理重建了支付基础设施，包括自主支付和争议交易处理。
  watch_reason: Natural正在为AI代理重建支付基础设施，获Forerunner 3000万美元领投并直接挑战Stripe，是AI代理经济中关键基础设施的早期领跑者，其进展将影响自主代理的商业化落地。
  risk_notes:
  - 与Stripe等成熟支付巨头直接竞争，在渠道、合规和品牌认知方面差距显著。
  - AI代理支付市场尚处早期，监管框架和行业标准尚未建立，长期商业路径存不确定性。
  - 公司成立于2025年，团队规模和运营历史有限，产品成熟度和市场验证尚需时间。
  score: 7.0
  article_ids:
  - cf3c8dfd6c45ed29
  evidence_snippets:
  - Natural 定位为代理编排层，通过集成其基础设施，企业可以让代理自主支付、收款和与人类或其他代理交易。
  - 传统支付系统依赖人工授权进行交易，无法支持需要自主行动的AI代理，Natural为此从头重建支付基础设施。
---

AI agents are starting to execute more sophisticated tasks, such as identifying vendors that can deliver freight, comparing prices, and messaging the vendor to organizing a delivery. But when it comes to making a payment for the shipment, they still need to involve a human.

Today’s financial sector relies on financial rails, the underlying infrastructure that moves money and information between banks, businesses, and consumers. But these financial rails were built for human-initiated transactions, not autonomous AI agents. For example, traditional payment systems like credit cards and ACH rely on human authorization for transactions, which slows down agents engineered to work autonomously.

One new startup, Natural, is tackling the problem by redesigning the whole system from the ground up. And it now has $30 million in fresh capital to pursue an ambitious plan that will put it in direct competition with giants like Stripe.

About a year ago, Natural co-founder and CEO Kahlil Lalji realized that AI agents were evolving faster than existing financial architecture, which can’t support tasks like autonomously paying a vendor, collecting payments, or transacting with each other.

Lalji has a background in banking and finance, but as he prepared to launch another startup he had hoped to avoid the sector. His previous startup Ivella, a YC-backed banking and financial product for couples, was sold in 2023 to Earnin, where he worked as an engineer for two years. He told TechCrunch he had been burned by the finance sector after the Zero Interest Rate Policy era ended.

And yet, Lalji couldn’t ignore the opportunity.

“I kept on coming back to it,” he said. “It just feels obvious that agentic payments are going to be structurally the most important problem [in the] space.”

Lalji teamed up with Eric Wang, his co-founder at Ivella, and Walt Leung, a former engineering manager at Nextdoor, and founded Natural in 2025. The startup positions itself as an agent orchestration layer that enables AI agents to move and store funds. By integrating Natural’s infrastructure, companies can allow their agents to make autonomous payments, collect funds, and transact with both humans and other agents.

Natural got the attention of Kirsten Green, founder and managing partner at VC firm Forerunner. Green, whose firm focuses on consumer experiences and the future of commerce, led its $30 million Series A round in the company, bringing the company’s total funding to $40 million.

Green was attracted by Natural’s broader ambitions. The startup isn’t just focused on helping agents pay for and check out goods on behalf of consumers, it’s also trying to reinvent payment infrastructure, including how disputed transactions are handled.