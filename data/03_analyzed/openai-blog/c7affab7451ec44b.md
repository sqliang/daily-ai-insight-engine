---
title: Building self-improving tax agents with Codex
source: https://openai.com/index/building-self-improving-tax-agents-with-codex
author: []
published: '2026-05-27'
created: '2026-05-28'
description: See how OpenAI, Thrive, and Crete built a self-improving tax agent with
  Codex, automating filings, improving accuracy, and accelerating workflows.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c7affab7451ec44b
source_type: tech_blog
tldr: OpenAI与Thrive Holdings利用Codex为Crete会计事务所构建自进化税务代理Tax AI，试点处理7000份税表，准确率达97%。
objective_summary: 过去六个月，OpenAI派驻工程师与Thrive Holdings合作，为Crete旗下30余家会计事务所开发Tax AI系统，用于自动处理1040和1041税表。系统利用Codex的智能体能力将生产使用转化为结构化信号以驱动自主改进。在试点中处理了7000份税表，节省约三分之一准备时间，
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - OpenAI
  - Thrive Holdings
  - Crete
  technologies:
  - Codex
  - Tax AI
  key_people: []
key_logic_flow:
- Crete会计事务所的从业人员在税季高峰期间，中等至复杂税表的数据录入每份需耗时8小时，涉及数百万份底层文档、往年数据和手工提取计算，税务准备工作成为严重瓶颈。
- OpenAI与Thrive Holdings合作，将前沿部署工程师和研究员派驻至Crete网络，与一线从业人员直接协作开发Tax AI系统。
- Tax AI基于Codex的智能体能力构建，通过精心设计的评估基础设施、一线从业人员直接反馈和真实生产环境，将使用数据转化为结构化信号，实现系统的自主改进。
- 从业人员上传源文件和客户备注后，Tax AI自动创建税务引擎提交草案供审核，涵盖1040和1041类型税表的准备流程。
- 系统在试点期间处理了7000份税表，字段完成准确率从上线初期的25%（75%正确率阈值）在六周内提升至86%，90%和100%正确率阈值增长更快。
- 最终效果：节省约三分之一税务准备时间，草拟税表准确率最高达97%，吞吐量提升约50%。
impact_score:
  score: 6.0
  reason: 这是 OpenAI 首次公开披露 Codex 在垂直行业（税务会计）的大规模生产部署案例，处理了 7000 份真实税表，具有重要的标杆意义。自进化智能体架构——将生产使用数据转化为结构化改进信号，实现无需人工干预的持续优化——在工程方法论上有参考价值。但本质上仍是一个垂直行业的应用落地案例，并未发布新的模型能力或开放平台，对行业格局的影响限于示范效应而非范式转移，故评为
    6 分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 97% 准确率的测量口径是否严格，自进化循环的可复现性以及是否依赖 OpenAI 派驻工程师的深度定制
hype_assessment:
  level: medium
  reason: 文章使用了 'self-improving agents'、'autonomous improvement' 等具有营销色彩的表达，但整体叙事以具体数据支撑（7000
    份税表、从 25% 到 86% 的准确率提升曲线、节省三分之一时间），且承认了初期准确率仅 25% 的现实起点，未过度使用 '颠覆'、'革命性' 等空洞词汇。炒作程度适中，属于技术博客常见的适度包装。
information_entropy: medium
domain_disruption:
  technical_innovation: 核心技术创新在于构建了一套将生产环境使用反馈转化为结构化改进信号的闭环系统：通过精心设计的评估基础设施、一线从业者直接反馈和真实生产数据，驱动
    Codex 智能体自主迭代优化，使系统在六周内从 25% 准确率提升至 86%。这种 '部署即训练' 的工程范式将传统的人工 prompt 调优和边缘案例修复自动化，是
    AI agent 从实验室走向生产的关键工程突破。
  business_model: 对专业服务（会计、法律、咨询等）行业的 SaaS 生态有重塑潜力：将 AI agent 从一次性工具转变为持续自进化的生产力平台，改变了传统软件
    '版本发布-客户升级' 的交付模式。税务准备时间节省三分之一、吞吐量提升 50%，如果可规模化复制，将推动知识密集型服务业从按人头计费向 AI 增强的效率计费模式转型。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 核心判断：这不是一次性的应用落地案例，而是 Codex 验证了「生产数据→结构化信号→自主进化」这一自强化飞轮的可行性。评估逻辑：(1) 市场规模支撑：全球税务准备市场规模超百亿美元，且具有高复购、高粘性、高客单价的SaaS理想属性，Crete试点的7000份税表仅是冰山一角；(2)
    飞轮效应明确：准确率从25%→86%（六周内）、最终达97%，增速本身在加速——这表明每多处理一份税表，系统就变得更聪明，边际成本递减而边际价值递增，是教科书级的复利结构；(3)
    跨行业可复制性强：税务是高度标准化、强监管的专业服务行业，成功突破后，法律文书、审计、合规等相邻领域具备类似的数据结构和工作流特征，Codex 的自进化范式可直接移植；(4)
    护城河的时间维度：一旦在某个垂直行业完成飞轮启动并积累足够的生产数据，后发者追赶的难度呈指数级上升，3-5年后 Codex 极大概率仍是该领域的核心基础设施。扣分项：目前仍是单一客户/单一行业的试点，尚未证明跨客户泛化能力；税收政策的地区差异性可能限制国际化扩张速度。综合评分
    8.0，属于「极强复利效应，3-5年后大概率仍是行业基石」的上限区域。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Microsoft (Azure)
- Thrive Holdings
competitive_casualty:
- Thomson Reuters (ONESOURCE)
- Wolters Kluwer (CCH Axcess)
- Intuit (ProConnect Tax)
- 传统 RPA 税务自动化厂商
- 非 AI-native 的财税 SaaS 厂商
market_opportunities:
- 专业服务垂直AI代理赛道已验证：可借鉴Tax AI的"派驻工程师+一线从业者协作"模式，在审计、法律文书、保险理赔等场景复制自进化代理方案，重点瞄准存在大量重复文档处理且准确率可渐进提升的细分领域
- AI代理评估基础设施创业机会：Tax AI的核心壁垒在于将生产使用数据转化为结构化改进信号，可围绕AI Agent的持续评估、回归测试、生产监控构建SaaS工具链，服务企业级AI代理的运维需求
- 财税SaaS厂商应加速AI代理集成：传统税务软件（如Intuit、Drake）面临被AI原生方案替代的风险，建议关注将Codex/Claude等前沿Agent能力嵌入现有工作流的中间件机会，或开发面向中小会计事务所的轻量级AI税务助手
risk_matrix:
  regulatory: 税务代理属于高度受监管领域（IRS Circular 230、各州CPA执业法规），AI生成的税表若出现系统性错误可能引发大规模税务争议与法律责任；OpenAI未披露该系统的合规审查机制，若监管机构认定AI代理构成未经授权的税务实践，可能导致产品被叫停或面临集体诉讼
  technological: 系统依赖OpenAI Codex的闭源能力，存在供应商锁定风险；97%的准确率在税务场景下仍意味着每100份税表中最多3份存在错误，若错误集中在特定税表类型可能导致系统性偏差；自进化机制可能产生不可预测的行为漂移，长期稳定性未经充分验证
  competitive: 四大会计师事务所（Deloitte、PwC等）正积极布局AI税务工具且拥有更强的合规背书和客户关系护城河；Intuit TurboTax等现有玩家拥有数千万用户基础和监管沟通渠道，可能通过生态优势挤压第三方方案；OpenAI若直接面向终端客户可能与其合作方Thrive
    Holdings/Crete形成利益冲突
  ethical: 税务从业人员面临大规模岗位替代风险——美国约有130万税务 preparer，系统宣称节省三分之一时间且提升50%吞吐量意味着显著的人力需求缩减；客户敏感财务数据经AI系统处理存在隐私泄露和第三方数据共享的隐患；自进化系统若在训练中吸收特定人群（如低收入申报者）的偏差数据，可能导致对弱势群体的系统性不利结果
  additional:
  - 系统性风险：若数千家会计事务所采用同一AI系统，模型中的单一缺陷可能同时影响数万份税表，造成集中化的税务申报失败事件
  - 声誉连锁风险：OpenAI以API供应商身份介入终端业务流程，若发生重大事故将波及整个Codex生态的企业信任度
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
---

*How Thrive Holdings and OpenAI co-developed Tax AI for Crete accountants by fusing practitioner expertise with a Codex-driven loop*

Real-world systems behave differently in production than they do in a lab, breaking in ways that are hard to anticipate before deployment. Teams often discover those failures after launch, then spend weeks inspecting edge cases, adjusting prompts, and translating production feedback into durable product improvements. The feedback loop is manual and slow, and only improves when an engineer advances it. But today, with thoughtfully designed eval infrastructure, direct access to practitioners and real world environments, and the frontier agentic capabilities of Codex, you can build agents that self-improve.

In this post, we’ll unpack how we used Codex to build this type of agent. Over the past six months, OpenAI forward deployed engineers and researchers along with Thrive Holdings’ engineers collaborated to build Tax AI alongside and for __Crete__(opens in a new window)’s network of 30+ accounting firms to help prepare increasingly complex tax returns. Instead of relying on engineers to find and fix each failure, Tax AI uses Codex to turn production use into structured signals that fuel autonomous improvement.

Crete practitioners prepare tens of thousands of tax returns each season which requires working through millions of underlying documents. For medium- to large-complexity filings, data entry alone can take eight hours per return, often involving messy data sources, prior-year documents, and manual extraction and calculation. They pointed us to tax preparation as a significant bottleneck during the busiest stretch of tax season.

To solve this problem, Tax AI processed 7,000 tax returns across the Crete firms that participated in the pilot this tax season. The system automates much of the time-intensive process of preparing 1040 and 1041 tax returns, but even more compelling than the efficiency gains is that the system itself is measurably better than the version that was first deployed three months ago.

In Tax AI, practitioners upload source files along with any client-specific notes. Tax AI then creates a tax engine submission, ready for review. It saves practitioners about a third of their time on tax preparation, drafts returns with up to 97% accuracy, and increases throughput by about 50%, creating more room for them to spend time with clients.

We can quantify this improvement by understanding how accurately Tax AI can complete a return without needing correction later. We measure accuracy by checking what share of returns reach 75%, 90%, or 100% correct field completion. At launch, only a quarter of returns were at 75% correct field completion, but within six weeks, 86% hit that mark. The system showed even faster growth at the 90% and 100% correct field completion levels. These thresholds give us a practical view of how much practitioner follow-up different returns still require.