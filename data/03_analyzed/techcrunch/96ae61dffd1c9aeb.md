---
title: Databricks hits $188B valuation, extending its run as AI’s favorite second
  act
source: https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/
author:
- '[[Julie Bort]]'
published: '2026-07-17'
created: '2026-07-18'
manifest_dates:
- '2026-07-18'
- '2026-07-19'
description: Databricks has remade its image into an AI company and has published
  research on the cost savings of open weight AI models for coding.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 96ae61dffd1c9aeb
source_type: news_media
tldr: Databricks 宣布新一轮融资，估值达 1880 亿美元，本轮由 Coatue 领投。这是其 18 个月来的第四次大额融资，公司成功从大数据 SaaS
  厂商转型为 AI 基础设施提供商。
objective_summary: 2026 年 7 月 17 日，Databricks 宣布由 Coatue 领投的新一轮融资，估值达 1880 亿美元。融资金额约
  30 亿美元，预计夏末完成交割。这是该公司自 2024 年 12 月以来第四次大规模融资，估值从 620 亿一路升至 1880 亿。Databricks 利用其企业数据平台基础，推出
  Lakebase、Unity、Omnigent 等 AI 产品，同时积极采用中国开源大模型（如 Z.ai 的 GLM 5.2）以降低 AI 成本。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Databricks
  - Coatue
  - Z.ai
  - Anthropic
  - OpenAI
  technologies:
  - AI agent
  - open-weight model
  - GLM 5.2
  key_people:
  - Ali Ghodsi
key_logic_flow:
- Databricks 宣布由 Coatue 领投的新一轮融资，估值达 1880 亿美元，融资金额约 30 亿美元。
- 这是 Databricks 在 18 个月内第四次大额融资：2024 年 12 月以 620 亿估值融资 100 亿，2025 年 9 月以 1000 亿估值融资
  10 亿，2026 年 2 月以 1340 亿估值融资 50 亿。
- Databricks 从 2013 年创立时的大数据 SaaS 厂商成功转型为 AI 基础设施提供商，推出 Lakebase（AI 代理数据库）、Unity（AI
  网关）和 Omnigent（多智能体管理框架）等 AI 产品。
- Databricks 是 2026 年企业采用低成本中文开源大模型趋势的代表案例，尤其推崇 Z.ai 的 GLM 5.2 模型用于代码生成。
- CEO Ali Ghodsi 公布内部测试结果，称开源模型（尤其是 GLM 5.2）在处理编程任务上已达到最高难度级别，且总成本低于 Anthropic 和 OpenAI
  的闭源模型。
object_mentions:
- object_type: product
  name: Lakebase
  canonical_name: Databricks Lakebase
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 推出了 Lakebase，这是其专为 AI 代理构建的数据库产品。
  article_id: 96ae61dffd1c9aeb
- object_type: product
  name: Unity
  canonical_name: Databricks Unity
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 推出了 Unity，这是其 AI 网关产品，用于管理和治理 AI 访问。
  article_id: 96ae61dffd1c9aeb
- object_type: product
  name: Omnigent
  canonical_name: Databricks Omnigent
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 推出了名为 Omnigent 的元编排框架，用于管理多个 AI 代理的协同工作。
  article_id: 96ae61dffd1c9aeb
- object_type: model
  name: GLM 5.2
  canonical_name: Z.ai GLM 5.2
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Databricks 积极采用 Z.ai 的 GLM 5.2 作为代码生成模型，内部测试显示其编程能力达到最高难度级别，且总成本低于 Anthropic 和
    OpenAI 的闭源模型。
  article_id: 96ae61dffd1c9aeb
extract_result: success
impact_score:
  score: 7.0
  reason: Databricks 在18个月内估值从620亿飙升至1880亿美元（3倍增长），这是一级市场对'数据平台→AI基础设施'转型路线的强力背书。其AI产品矩阵（Lakebase、Unity、Omnigent）的推出以及积极采用中国开源模型降本的策略，正在重塑企业AI基础设施的竞争格局。虽然不算ChatGPT发布级别的范式转移，但这一估值信号将直接影响后续AI数据平台创业公司的融资预期，并给Snowflake等竞品带来更大市场压力。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 1880亿估值是否真正反映技术壁垒，以及采用GLM 5.2等中国开源模型的实际工程效果
hype_assessment:
  level: medium
  reason: 估值数字真实可信（已披露多轮融资细节），但媒体包装为'AI最爱的第二幕'带有叙事驱动色彩。Databricks确实完成了从大数据SaaS到AI基础设施的形象转型，'AI's
    favorite second act'属于正常的品牌叙事升级而非虚假宣传。真正的风险在于高估值是否对应同等技术护城河——其AI产品（Lakebase/Unity/Omnigent）尚在早期推广阶段，竞争格局未定。
information_entropy: medium
domain_disruption:
  technical_innovation: Databricks 推出了面向AI Agent的数据库Lakebase、AI网关Unity和多智能体管理框架Omnigent，构成了从数据存储→AI接入→多Agent编排的完整技术栈。其核心工程创新在于将底层数据湖能力与AI推理、成本优化（如引入GLM
    5.2开源模型）深度整合，实现企业级AI基础设施的一体化交付。
  business_model: Databricks 证明了'先占据企业数据资产，再向上叠加AI能力'的路线是可行的，这为所有数据基础设施公司指明了变现路径。同时，大规模采用中国开源模型（GLM
    5.2）降低AI成本的做法，正在解构Anthropic/OpenAI的闭源定价模型，可能催生'底层数据平台+开源模型集成+管理工具'的新型企业AI采购模式。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: Databricks 同时占据企业数据锁定效应（迁移成本极高）和 AI 基础设施层（Lakebase 为 AI 代理数据库、Unity 为 AI
    网关、Omnigent 为多代理管理框架）双重护城河。18 个月内估值从 620 亿美元飙升至 1880 亿美元，体现资本市场对其'数据 + AI 代理中间件'定位的高度认可。企业一旦将核心数据资产沉淀在
    Databricks 平台，AI 时代的切换成本不会降低反会升高——数据引力是最强的复利引擎之一。风险点在于云厂商（AWS 的 SageMaker + Bedrock、GCP
    的 BigQuery + Vertex AI）的纵深竞争，以及开源模型层进一步商品化可能压缩中间件层的利润空间，但短期不影响其领先地位。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Databricks
- Z.ai
- Coatue
competitive_casualty:
- Snowflake
- OpenAI
- Anthropic
market_opportunities:
- 企业级 AI 基础设施赛道仍处高景气周期，创业者可关注为传统企业提供从数据湖到 AI 代理的端到端迁移方案，效仿 Databricks 的大数据转 AI 路径
- 开源大模型（尤其是中国开源模型）在企业代码生成等垂直场景的成本优势显著，催生模型评测、微调适配与安全审计的第三方服务机会
- 多智能体管理框架（如 Databricks 的 Omnigent）预示 AI 代理编排层将成为新的中间件价值洼地，可切入企业级 AI 网关与代理监控赛道
risk_matrix:
  regulatory: Databricks 积极采用中国开源大模型（GLM 5.2）用于企业编程任务，可能触发美国政府对敏感行业使用中国 AI 模型的出口管制与国家安全审查；同时频繁大额融资（18
    个月 4 轮）可能招致 SEC 等监管机构对估值合理性和信息披露的关注
  technological: 对中国开源模型（尤其是 GLM 5.2）的深度依赖构成单点技术风险——若中国政府限制模型出口、模型质量出现退化或地缘政治紧张升级，Databricks
    的 AI 成本优势可能迅速消失；另外开源模型能力演进速度可能被闭源对手的架构突破所超越
  competitive: Snowflake、Snowpark 等竞争对手正加速 AI 化转型，云厂商（AWS SageMaker、Azure AI、GCP Vertex
    AI）自带原生 AI 基础设施挤压独立平台生存空间；1880 亿美元估值带来极高的业绩增长预期，一旦营收增速放缓将面临估值重估压力
  ethical: 企业使用低成本中国开源模型进行代码生成可能引入未被充分审计的算法偏见或后门风险；GLM 5.2 的训练数据透明度不足，在敏感行业（金融、国防）的应用存在数据伦理隐患
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: Lakebase
  canonical_name: Databricks Lakebase
  url: null
  positioning: Databricks 最新推出的专为 AI 代理构建的企业级数据库产品，依托企业数据平台为 AI 工作负载优化存储与查询性能。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 AI 代理的企业数据团队
  - 需要 AI 工作负载数据库的企业开发者
  product_signal: 专为 AI 代理设计的数据库产品，依托 Databricks 企业数据平台积累，直接面向 AI 工作负载的存储与查询需求。
  market_signal: 随 Databricks 连续融资（估值从 620 亿升至 1880 亿美元）发布，企业 AI 基础设施市场需求增长强劲。
  differentiation: 与传统分析型数据库不同，Lakebase 直接针对 AI 代理的数据访问模式进行优化，与 Databricks 企业数据生态深度集成。
  watch_reason: Lakebase 代表了数据基础设施向 AI 原生演进的关键方向，值得跟踪其在企业 AI 代理场景中的实际采用情况和产品成熟度。
  risk_notes:
  - 面临 Snowflake 等竞品在 AI 数据库领域的激烈竞争。
  - 产品上市时间尚短，成熟度和生态支持有待市场验证。
  score: 7.0
  article_ids:
  - 96ae61dffd1c9aeb
  evidence_snippets:
  - Databricks 推出了 Lakebase，这是其专为 AI 代理构建的数据库产品，依托企业级数据平台积累为 AI 工作负载提供底层存储支持。
  - Databricks 开始陆续推出 AI 产品，包括专为 AI 代理构建的数据库 Lakebase，利用其企业数据平台基础快速进入 AI 基础设施市场。
- object_type: product
  name: Unity
  canonical_name: Databricks Unity
  url: null
  positioning: Databricks 推出的 AI 网关产品，专注于企业 AI 模型访问的管理、治理与安全合规管控，是 Databricks AI 基础设施的关键组件。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业 IT 和安全团队
  - 需要治理 AI 模型访问的合规管理人员
  product_signal: 作为 AI 网关产品，Unity 提供企业级 AI 访问治理和管理能力，填补 Databricks 在 AI 安全管控领域的产品空缺。
  market_signal: 企业对 AI 治理和安全的需求快速增长，Unity 定位在 Databricks 生态中捕获这一增量市场机会。
  differentiation: 与通用 API 网关不同，Unity 专注于 AI 模型的访问权限、合规和安全策略的集中化管理与统一治理。
  watch_reason: AI 治理是 2026 年企业关注的核心议题之一，Unity 作为 Databricks 生态内的 AI 网关产品，其市场接受度值得持续跟踪。
  risk_notes:
  - AI 网关市场竞争日趋激烈，包含传统 API 管理厂商和新兴 AI 安全公司。
  score: 6.0
  article_ids:
  - 96ae61dffd1c9aeb
  evidence_snippets:
  - Databricks 推出了 Unity，这是其 AI 网关产品，用于管理和治理企业 AI 模型访问，满足企业安全合规与访问控制的迫切需求。
  - Databricks 推出 AI 网关 Unity 作为其 AI 产品矩阵的一部分，与 Lakebase 和 Omnigent 共同构建完整的 AI 基础设施栈。
- object_type: product
  name: Omnigent
  canonical_name: Databricks Omnigent
  url: null
  positioning: Databricks 推出的元编排框架，用于管理多个 AI 代理的协同工作与编排调度，面向企业级多智能体部署场景。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 部署多个 AI 代理的企业 AI 团队
  - 需要多智能体编排的企业开发平台团队
  product_signal: 作为元编排框架，Omnigent 管理多个 AI 代理的协同工作，解决企业多智能体部署中的统一编排与治理难题。
  market_signal: 多代理编排是 2026 年 AI 基础设施热门方向，Omnigent 切入快速增长的企业级多智能体管理市场。
  differentiation: 与 LangChain 等开发者导向的编排工具不同，Omnigent 面向企业级部署，提供多 AI 代理的统一治理与协调能力。
  watch_reason: 多代理编排是企业 AI 落地从单点到体系化的关键能力，Omnigent 作为 Databricks 的解决方案，其架构设计和企业采用进展值得持续关注。
  risk_notes:
  - 面临 LangChain、CrewAI 等开源编排框架的生态竞争。
  - 元编排概念尚处于行业早期阶段，产品成熟度和标准兼容性需进一步验证。
  score: 6.0
  article_ids:
  - 96ae61dffd1c9aeb
  evidence_snippets:
  - Databricks 推出了名为 Omnigent 的元编排框架，用于管理多个 AI 代理的协同工作，解决企业多智能体部署中的协调与治理问题。
  - Databricks 的 Omnigent 被描述为一种"元编排框架"，专门用于管理多个 AI 代理的协同工作，代表企业 AI 基础设施走向体系化。
---

Databricks on Thursday announced a new round of funding that values the company at $188 billion. The round was led by Coatue.

Databricks didn’t disclose exactly how much it raised; it said the money isn’t in its hands yet and that the round will close later this summer. (Other outlets have since reported the raise is roughly $3 billion.) While it’s unusual for a company to announce before it gets the money, a VC tells TechCrunch that the deal is solid, with so many firms wanting in that the company had no reason to keep its shiny new valuation a secret.

In fact, Databricks has been on a year-and-a-half fundraising tear as it successfully transitioned its image into an AI provider and not just a yesteryear SaaS sensation. Yesteryear being back in the BC times (Before ChatGPT).

Only five months ago, in February, Databricks closed a $5 billion Series L raise at a $134 billion valuation. Five months before that, in September 2025, it raised $1 billion at a $100 billion valuation. And roughly nine months before that, in December 2024, it raised what was a record-breaking round at the time of $10 billion at a $62 billion valuation.

Databricks has raised so many rounds over the years that this latest one became the subject of memes about running out of letters of the alphabet. “Turning on alerts for when we get a Series AA,” one person posted.

But its image reconstruction has been legit. Founded in 2013, it initially grew to success back in the big data era, with software that enabled enterprises to store enormous amounts of data in the cloud, yet produce speedy analytics.

Because it already sat on troves of enterprise data, Databricks was then well-positioned to respond as companies started wanting AI with the same security and governance they expect from traditional enterprise software.

The company began rolling out one AI product after another, like Lakebase, its database built for AI agents, and Unity, its AI gateway, along with a “meta-harness” called Omnigent that manages multiple agents.

Databricks also increasingly became known as one of the big examples of enterprises adopting more affordable Chinese-based open-weight models (models whose underlying code is published for anyone to use and modify) for cost control, one of the big trends of 2026. It is a particular champion of Z.ai’s GLM 5.2 as a model for coding.

Last week Databricks CEO Ali Ghodsi shared the results of some internal benchmarking done to manage his own AI costs for his 3,000 software engineers.

The company compared AI models on the actual tasks its programmers do. Not surprisingly, in the blog post revealing the results, Databricks shared that “open models, and GLM 5.2 in particular, are now able to handle even the highest level of task difficulty” in coding, and at a total lower cost than proprietary models from Anthropic and OpenAI.