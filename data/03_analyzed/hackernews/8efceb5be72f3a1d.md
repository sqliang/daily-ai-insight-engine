---
title: Salesforce to Acquire Fin (formerly Intercom) for $3.6B
source: https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL
author:
- '[[colesantiago]]'
published: '2026-06-15'
created: '2026-06-16'
description: 'Article URL: https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL
  Comments URL: https://news.ycombinator.com/item?id=48540126 Points: 306 # Comments:
  227'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 8efceb5be72f3a1d
source_type: community_discussion
tldr: Salesforce 以约 36 亿美元收购 Fin（原 Intercom），将其 AI 客服代理平台与自研模型 Apex 纳入 Agentforce
  生态，加速企业级自主代理在各规模客户中的部署。Fin 的 AI Agent 平均自主解决 76% 的支持工单，覆盖实时聊天、邮件、WhatsApp、短信、电话和
  Slack 等多个渠道。
objective_summary: 2026 年 6 月 15 日，Salesforce 宣布签署最终协议，以约 36 亿美元收购客户代理公司 Fin（原 Intercom）。Fin
  的核心产品是其 AI Agent，基于自研模型 Apex，可在实时聊天、邮件、WhatsApp、短信、电话和 Slack 等多个渠道端到端解决复杂客户查询，已实现平均自主解决
  76% 支持工单的成果。收购完成后，Fin 将补充 Salesforce 的 Agentforce 平台，为中小企业提供快速部署选项。该交易预计在 Salesforce
  2027 财年第四季度完成，不影响其资本回报计划。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Salesforce
  - Fin
  technologies:
  - AI Agent
  - Apex
  - Agentforce
  key_people:
  - Marc Benioff
  - Eoghan McCabe
key_logic_flow:
- Salesforce 宣布以约 36 亿美元收购 Fin（原 Intercom），交易预计在 Salesforce 2027 财年第四季度完成。
- Fin 的核心产品是其 AI Agent，基于自研模型 Apex，可在实时聊天、邮件、WhatsApp、短信、电话和 Slack 等多个渠道端到端解决复杂客户查询。
- Fin 的 AI Agent 已展示出平均自主解决 76% 支持工单的客户成果，其性能优于市面上的前沿商业模型。
- Agentforce 在 2027 财年第一季度达到 12 亿美元年经常性收入（ARR），同比增长 205%。
- Fin 的技术将补充 Agentforce 平台，为服务组织提供快速部署选项，尤其适合需要快速启动的中小企业。
- Fin 拥有超过 30,000 家企业的全球客户基础和经验丰富的 AI 技术团队，加入 Salesforce 后有望加速 AI 代理在各规模企业中的部署。
extract_result: success
object_mentions:
- object_type: product
  name: Fin AI Agent
  canonical_name: Fin AI Agent
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Fin 的核心产品是其 AI Agent，可在实时聊天、邮件、WhatsApp、短信、电话和 Slack 等多个渠道端到端解决复杂客户查询。
  - 该 AI Agent 基于自研模型 Apex，已展示出平均自主解决 76% 支持工单的客户成果，性能优于市面上的前沿商业模型。
  article_id: 8efceb5be72f3a1d
- object_type: model
  name: Apex
  canonical_name: Apex
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Fin 的 AI Agent 由公司自研的 AI 模型 Apex 驱动，该模型专为客服场景设计，已展示出行业领先的问题解决率。
  article_id: 8efceb5be72f3a1d
- object_type: product
  name: Agentforce
  canonical_name: Agentforce
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Agentforce 在 2027 财年第一季度达到 12 亿美元年经常性收入（ARR），同比增长 205%。
  - Fin 的打包产品与自研模型将补充 Agentforce 平台，为服务组织提供额外快速部署选项，尤其适合需要快速启动的中小企业。
  article_id: 8efceb5be72f3a1d
impact_score:
  score: 6.8
  reason: 这是一笔金额重大的战略收购（36亿美元），直接验证了 AI 客服 Agent 赛道的商业化可行性。Agentforce 在 Q1 FY27 达到
    12 亿美元 ARR（同比增长 205%）已证明市场高速增长，收购 Fin 是对产品矩阵的补强——尤其为中小企业提供快速部署方案。但收购本身属于行业整合而非范式突破，36
    亿美元对于 Salesforce 这样体量的 CRM 巨头属于战略性补强，不会立刻改变竞争格局。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: Fin 被 Salesforce 收购后产品的独立性与开放性，以及面向中小企业的定价策略是否会改变
hype_assessment:
  level: medium
  reason: 新闻稿存在一定 PR 包装，如 '行业领先的客户代理公司'、'定义了品类' 等营销用语。但提供了具体可验证的硬数据支撑——Fin 的 AI Agent
    实现平均 76% 的端到端自动解决率、服务超过 3 万客户、Agentforce 的 12 亿美元 ARR 等。整体水分可控，属于标准的重大收购宣传。
information_entropy: medium
domain_disruption:
  technical_innovation: Fin 自研的 Apex 模型专为客服场景优化，在工单自动解决率上超越通用前沿模型，体现了垂直领域专用模型（Vertical
    Specialist Model）对比通用基础模型的差异化技术路径——通过领域特定训练数据与任务导向的架构设计，在受限域内实现更高自动化水平。
  business_model: 收购将独立 AI 客服 SaaS 产品整合进 Salesforce 的 CRM 生态，使中小企业能以更低门槛获得开箱即用的 AI
    客服 Agent，与 Agentforce 的企业级深度定制形成互补。这加速了 AI 客服从 '大客户专属' 向 '全市场规模部署' 的商业化渗透，可能倒逼
    Zendesk、Freshdesk 等竞品加速 AI 整合。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 此次收购验证了垂直 AI Agent（客服场景）的巨大商业价值。Salesforce 以 $3.6B 将 Fin 的自研 Apex 模型（平均
    76% 自动解决率）与 Agentforce 平台（Q1 FY27 ARR $1.2B，同比增长 205%）结合，形成从大型企业到 SMB 的全覆盖 AI
    客服矩阵。Fin 的差异化在于其专为客服场景设计的 Apex 模型的性能超越了通用前沿模型，这创造了模型层面的竞争壁垒。长期来看，AI 客服是 CRM 领域确定性最强的
    AI 落地场景，Salesforce 通过此次收购获得了差异化模型能力、3 万+中小企业客户基础和一支深度 AI 工程团队，有望在 3-5 年内成为 AI
    客服基础设施的绝对主导者。但整合风险不可忽视——Salesforce 过往大型收购（Slack、Tableau、MuleSoft）的整合回报参差不齐，且 $3.6B
    的收购溢价（约 12 倍 ARR）意味着回报需要持续的严苛验证。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Salesforce
- Fin (Intercom)
- Agentforce
competitive_casualty:
- Zendesk
- Freshworks
- AI 客服初创公司
- 传统呼叫中心 BPO
market_opportunities:
- AI 客服赛道进入加速整合期，创业者可关注垂直行业（医疗、金融、教育）的定制化 AI Agent 方案，利用 Salesforce + Fin 的生态空白快速切入
- 中小企业（SMB）AI 客服快速部署方案存在巨大市场缺口，可开发基于开源模型的轻量化 AI 客服产品，主打"零代码、小时级上线"的差异化定位
- Agentforce 生态的第三方工具与集成服务机会增多，围绕 Fin 的 Apex 模型与 Salesforce 平台之间的数据管道、性能监控、合规审计等环节可孵化专业服务
risk_matrix:
  regulatory: 反垄断审查风险——Salesforce 作为 CRM 巨头收购主要竞争对手（36 亿美元规模），可能面临 FTC 或欧盟的竞争审查，延长交易完成时间或附加剥离条件
  technological: Fin 的自研 Apex 模型在基准测试中虽领先闭源前沿模型，但开源模型（如 Llama、Mistral 系列）在客服场景快速追赶，模型优势窗口期可能缩短
  competitive: Zendesk、HubSpot、Freshworks 等竞争对手可能通过并购或自建加速 AI 客服布局，引发行业性价格战和人才争夺；此外，OpenAI、Anthropic
    等通用 AI 平台也可能向下渗透客服场景
  ethical: AI Agent 实现 76% 的客服工单自动化将显著冲击全球客服岗位（数以百万计），引发就业转移和社会适应性问题；同时多渠道数据汇集加剧客户隐私和数据治理挑战
  additional:
  - 收购整合风险——Fin 与 Salesforce 的企业文化、技术栈和客户群（SMB vs Enterprise）存在差异，整合失败将影响 Agentforce
    续费率和客户满意度
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Fin AI Agent
  canonical_name: Fin AI Agent
  url: null
  positioning: Salesforce 以 36 亿美元收购的多渠道 AI 客服代理平台，基于自研模型 Apex 端到端解决客户查询，将融入 Agentforce
    生态加速企业级自主代理部署。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 中小企业（SMB）
  - 商业组织
  - 企业服务团队
  product_signal: AI Agent 已实现平均自主解决 76% 支持工单的成果，覆盖实时聊天、邮件、WhatsApp、短信、电话和 Slack 七个渠道。
  market_signal: Salesforce 以约 36 亿美元完成收购，Agentforce 同期达 12 亿美元 ARR 同比增长 205%，Fin
    拥有超 3 万家企业客户基础。
  differentiation: 基于专为客服场景构建的自研模型 Apex，性能优于前沿商业模型，并提供比 Agentforce 更快速的打包部署选项。
  watch_reason: 作为 Salesforce 以 36 亿美元高价收购的 AI 客服代理，Fin 的 76% 自主解决率代表行业标杆水平，其整合后的产品路线图将深刻影响企业级
    AI 客服市场竞争格局，值得持续跟踪。
  risk_notes:
  - 收购整合存在不确定性，Fin 与 Agentforce 的客服代理功能可能重叠，需关注产品路线图调整方向。
  - 36 亿美元的高估值能否通过后续增长兑现，取决于 Fin 客户在 Salesforce 生态中的留存率和交叉销售效果。
  score: 9.0
  article_ids:
  - 8efceb5be72f3a1d
  evidence_snippets:
  - Fin 的核心产品是其 AI Agent，可在实时聊天、邮件、WhatsApp、短信、电话和 Slack 等多个渠道端到端解决复杂客户查询。
  - 该 AI Agent 基于自研模型 Apex，已展示出平均自主解决 76% 支持工单的客户成果，性能优于市面上的前沿商业模型。
  - Agentforce 在 2027 财年第一季度达到 12 亿美元年经常性收入（ARR），同比增长 205%。
  - Salesforce 宣布以约 36 亿美元收购 Fin（原 Intercom），交易预计在 Salesforce 2027 财年第四季度完成。
---

*Acquisition will bring Fin’s customer agent platform to companies of all sizes, accelerating time-to-value and expanding Salesforce’s ability to deliver autonomous agents across the enterprise *

**SAN FRANCISCO, CA — June 15, 2026** — Salesforce (NYSE: CRM), the global leader in CRM, today announced it has signed a definitive agreement to acquire Fin, formerly Intercom, an industry-leading customer agent company. Under the terms of the agreement, Salesforce will acquire Fin for approximately $3.6 billion, subject to customary purchase price adjustments.

Fin’s core offering, its AI Agent, resolves complex customer queries end-to-end, across every channel, including live chat, email, WhatsApp, SMS, phone, and Slack. The AI Agent is powered by the company’s proprietary AI model, Apex, that is purpose-built for customer support and has demonstrated industry-leading resolution rates that outperform top commercially available frontier models.

“We’re thrilled to welcome Fin to Salesforce as we enable every company to become an agentic enterprise,” said Marc Benioff, Chair and CEO, Salesforce. “Fin brings proven agent technology, a deep commitment to customer success, and an incredible AI team that will complement Agentforce with powerful service agent capabilities. Together, we’ll help companies of every size seize this opportunity — accelerating time to value with trusted agents that deliver measurable outcomes at scale.”

“This is a major win for consumers of the world,” said Eoghan McCabe, Chief Executive Officer and Co-Founder of Fin. “Our technology has defined this category and set the new standards for what great customer service looks like today. By joining forces with Salesforce, we can deploy it far and wide at a rate far faster than we could have ever achieved on our own.”

#### Accelerating Agentic Time-to-Value Across Customer Segments

Building on the strength of Agentforce, which reached $1.2 billion in ARR in Q1 FY27, up 205% year-over-year, Fin’s packaged offerings and proprietary models will complement Agentforce’s deeply customizable platform with additional fast-to-value deployment options for service organizations.

Upon close, Salesforce and Fin will give customers more ways to deploy AI agents across their customer service operations, with fast time-to-value options especially well-suited for SMB and some commercial organizations that need to launch quickly, integrate with existing systems, and deliver measurable outcomes. Together, Salesforce and Fin will support customers at every stage of AI adoption, from rapidly deployable support agents to more tailored, enterprise-scale transformations built on trusted data, security, governance, and integration.

Fin’s AI agent technology will help organizations improve autonomous resolution, reduce cost-to-serve, and accelerate AI adoption across their service organizations. The AI Agent has already demonstrated strong customer outcomes, including examples of AI agents resolving on average 76% of support volume end-to-end. The acquisition will also bring a long-tenured technical AI team and an established global customer base of more than 30,000 companies to Salesforce.

#### Transaction Details

The transaction is expected to close in the fourth quarter of Salesforce’s fiscal year 2027, subject to the satisfaction of customary closing conditions, including the receipt of required regulatory clearances. Based on the expected timing of closing of the transaction, there is no anticipated change to Salesforce’s fiscal year 2027 financial guidance, previously announced on May 27, 2026. The transaction will not impact Salesforce’s capital return program.

#### Forward-Looking Statements

This press release contains forward-looking statements within the meaning of the Safe Harbor provisions of the Private Securities Litigation Reform Act of 1995 regarding the proposed acquisition of Fin by Salesforce that involve substantial risks, uncertainties and assumptions that could cause actual results to differ materially from those expressed or implied by such statements. Forward-looking statements in this report include, among other things, statements about the potential benefits of the proposed acquisition and its lack of impact on previously announced guidance and our capital return program, Salesforce’s plans, the financial condition, results of operations and business of Salesforce and the anticipated timing of the closing of the proposed acquisition. Risks and uncertainties include, but are not limited to: the satisfaction of closing conditions; Salesforce’s ability to successfully integrate Fin; and potential disruptions to business relationships resulting from the announcement. Additional information is detailed in Salesforce’s latest filings with the Securities and Exchange Commission, including its Annual Report on Form 10-K and Quarterly Reports on Form 10-Q. Salesforce assumes no obligation to, and does not intend to, update these forward-looking statements, except as required by law.

#### About Salesforce

Salesforce helps organizations of any size become agentic enterprises – integrating humans, agents, apps, and data on a trusted, unified platform to unlock unprecedented growth and innovation. Visit www.salesforce.com for more information.