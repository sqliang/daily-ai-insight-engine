---
title: Choose Boring Technology (2015)
source: https://mcfunley.com/choose-boring-technology
author:
- '[[tosh]]'
published: '2026-08-13'
created: '2026-08-14'
manifest_dates:
- '2026-08-14'
description: 'Article URL: https://mcfunley.com/choose-boring-technology Comments
  URL: https://news.ycombinator.com/item?id=49289512 Points: 338 # Comments: 176'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f9c2faed5b010c6e
source_type: community_discussion
tldr: 前 Etsy 工程师 Dan McKinley 提出「选择无聊技术」的工程选型原则：公司应把有限创新代币花在核心业务上，优先选用成熟、故障模式已知的技术栈，并在引入新技术前通过全局成本评估与组织共识流程加以约束。
objective_summary: Dan McKinley 在 2015 年发表博客文章，结合自身在 Etsy 的经历以及前主管 Kellan 的技术决策影响，系统阐述「选择无聊技术」的选型哲学。文章将公司可承受的技术创新量类比为固定数量的「创新代币」，主张用成熟技术解决多数问题，只有在现有栈确实无法经济地解决问题时才引入新技术，并强调任何新技术引入都应经过组织层面的公开讨论、迁移承诺和成本评估。文中以
  Etsy 早期因堆砌 Python 中间层导致数年无法交付、以及用 PHP/MySQL/Memcached/Gearman 构建 activity feeds
  并随平台自然扩展 20 倍的案例，说明克制选型对长期运营可靠性的价值。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Etsy
  technologies:
  - MySQL
  - Postgres
  - PHP
  - Python
  - Memcached
  - Squid
  - Cron
  - NodeJS
  - MongoDB
  - Ruby
  - Scala
  - Redis
  - Gearman
  - Solr
  - Java
  key_people:
  - Dan McKinley
  - Kellan
  - Don Rumsfeld
  - Socrates
key_logic_flow:
- 作者以 Kellan 在 Etsy 的技术决策为起点，提出「拥抱无聊」的选型原则，认为工程师应将有限注意力集中在公司业务使命而非工具创新上。
- 文章引入「创新代币」概念，指出每个公司在成熟前大约只有三枚可消耗的创新代币，选择 NodeJS、MongoDB、自研数据库等新潮技术都会消耗这些珍贵资源。
- 作者区分了「已知未知」与「未知未知」，强调成熟技术的优势不仅在于能力已知，更在于故障模式和运维边界已被充分理解。
- 文章批评「为每个任务选最佳工具」的局部优化思维，认为真正要优化的是公司整体运营成本、认知负载和长期可靠性。
- 作者提出引入新技术的约束流程：先在现有栈内求解、书面记录旧栈的不可行之处、明确迁移旧功能的承诺与时间表，并组织全公司可见的讨论。
- Etsy 的案例从正反两方面印证了观点：早期为 Python 程序员强造中间层导致数年无法交付，而 activity feeds 基于 PHP/MySQL/Memcached/Gearman
  却在无人专门维护时随平台自然扩展 20 倍。
object_mentions:
- object_type: product
  name: MySQL
  canonical_name: MySQL
  url: https://www.mysql.com/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者将 MySQL 列为「无聊但足够好」的技术范例，认为其能力与失败模式已被充分理解。
  - 文章指出成熟技术如 MySQL、Postgres、PHP、Python 的共有特征是 boring and good，适合作为默认选型。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Postgres
  canonical_name: PostgreSQL
  url: https://www.postgresql.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Postgres 被作者归入「无聊但良好」的技术清单，作为推荐默认选择的关系型数据库之一。
  - 作者用 Postgres 与 MySQL 并列，说明 boring 不等于 bad，而是代表运维经验丰富、风险可控。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: PHP
  canonical_name: PHP
  url: https://www.php.net/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - PHP 被文章列为 boring 技术的代表，作者认为它能力已知、失败模式已知。
  - Etsy 曾努力将大部分系统统一迁移到 PHP，并基于 PHP/MySQL/Memcached/Gearman 构建 activity feeds。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Python
  canonical_name: Python
  url: https://www.python.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Python 被列入无聊但可接受的技术清单，说明其成熟度足以作为默认工具。
  - Etsy 早期案例显示，公司招聘了一批 Python 程序员后为他们强造了一个无意义的中间层，导致长期技术债。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Memcached
  canonical_name: Memcached
  url: https://memcached.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Memcached 被列为 boring 技术的典型代表，适合作为默认缓存方案。
  - Etsy 使用 PHP/MySQL/Memcached/Gearman 技术栈实现 activity feeds，并在数年间随平台自然扩展 20 倍。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Redis
  canonical_name: Redis
  url: https://redis.io/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Redis 被用作反例，说明如果用新潮技术实现 activity feeds 可能会更简单，但也会增加未知风险。
  - 文章强调，即使 Redis 可能让 activity feeds 更易实现，Etsy 仍选择基于现有栈构建，以获得长期可维护性。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Gearman
  canonical_name: Gearman
  url: http://gearman.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Gearman 被描述为 PHP 的作业服务器，是 Etsy 统一技术栈的一部分。
  - Etsy 基于 PHP/MySQL/Memcached/Gearman 构建 activity feeds，证明有限技术栈可以支撑复杂功能。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Solr
  canonical_name: Apache Solr
  url: https://solr.apache.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Solr 是文章中少数被明确认定为必须引入的新技术案例，因为用原始 PHP 实现带分面的全文搜索并不现实。
  - 作者用 Solr 说明其立场并非绝对化：当现有栈确实无法经济地解决问题时，引入新技术是合理的。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: NodeJS
  canonical_name: Node.js
  url: https://nodejs.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者用 NodeJS 作为消耗创新代币的例子，说明选择它会占用公司有限的技术冒险预算。
  - 文章认为，除非公司是 JavaScript 咨询公司，否则把创新代币花在 NodeJS 这类工具上会增加失败或延迟的风险。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: MongoDB
  canonical_name: MongoDB
  url: https://www.mongodb.com/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - MongoDB 被作为消耗一枚创新代币的典型例子，说明新潮数据库的未知风险较高。
  - 作者指出，除非公司是数据库公司，否则把创新资源投入在底层数据存储技术上并不明智。
  article_id: f9c2faed5b010c6e
- object_type: project
  name: Etsy activity feeds
  canonical_name: Etsy Activity Feeds
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 作者以 Etsy 的 activity feeds 功能为例，说明基于 PHP/MySQL/Memcached/Gearman 的保守实现能够在数年间随平台自然扩展
    20 倍。
  - 该项目在上线后数年无人专门维护，但因使用共享平台而稳定运行，体现了克制技术选型的长期收益。
  article_id: f9c2faed5b010c6e
extract_result: success
impact_score:
  score: 3.0
  reason: 该文是2015年发表的经典工程博客，并非当下新产品、论文或融资事件；其'创新代币'与'无聊技术优先'的选型哲学已在工程界广泛传播并被内化。当前更多属于理念回顾与社区讨论，对AI基础设施选型仍有长期参考价值，但短期行业冲击力有限。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: 如何在AI工程栈选型中平衡追新冲动与长期运维可靠性，避免将有限创新资源消耗在非核心工具上
hype_assessment:
  level: low
  reason: 文章立场恰恰是反炒作：明确反对'为每个任务选最佳工具'的局部优化，用Etsy正反案例和'创新代币'模型支撑论点，通篇未使用'颠覆''革命性'等PR词汇，而是在解构技术选型中的认知负载与运维成本，干货浓度高。
information_entropy: high
domain_disruption:
  technical_innovation: 提出'创新代币'框架与'无聊技术优先'的工程选型方法论，强调成熟技术的已知故障模式、全局成本优化以及引入新技术前的组织共识与迁移承诺
  business_model: 促使企业将有限工程资源集中于核心业务价值创造，通过减少技术栈碎片化和认知负载来降低长期运维成本与可靠性风险
engineering_complexity: conceptual
compound_value:
  score: 7.5
  reason: 该文并非一次性产品发布，而是一个已被反复验证的工程技术选型框架。其核心论点——“创新代币有限，应把冒险集中在核心业务而非基础设施”——在 AI
    资本效率愈发重要的当下更具解释力：AI 创业公司若把有限资源耗费在自研编排框架、追新数据库或过度复杂的 Agent 中间件上，会显著压缩模型与产品的迭代空间。2015
    年发表至今仍是工程决策与投资人尽调中的高频引用文本，具备长期思想复利。但它毕竟是一篇方法论文章，本身不形成网络效应、数据飞轮或锁定能力，因此无法给到基础设施级别的
    8–10 分；其复利主要体现在降低资本浪费、提高执行确定性的“负向收益”上。
value_capture_layer: cloud_platform
moat_impact: strengthens_monopoly
key_beneficiaries:
- AWS
- Microsoft Azure
- Google Cloud
- PostgreSQL
- Datadog
- Confluent
- Redis
competitive_casualty:
- 过度工程化的 AI Agent 中间件初创公司
- 未经验证的向量数据库新贵
- 追逐技术潮流的非核心创新团队
- 最佳工具局部优化型 SaaS 厂商
market_opportunities:
- 为企业提供基于'创新代币'理念的技术栈审计与选型咨询服务，帮助其在核心业务创新与运维风险之间取得平衡。
- 开发技术选型决策支持工具或内部平台工程产品，量化评估新技术引入的全局成本、已知故障模式与迁移承诺。
- 围绕成熟技术栈的自动化运维、可观测性与降本增效方案仍存在稳定市场需求，尤其是帮助组织降低认知负载的服务。
risk_matrix:
  regulatory: 无
  technological: 过度追逐新潮技术会导致未知故障模式放大、运维复杂度激增与人才稀缺；但若僵化执行'无聊技术'原则，也可能错失架构升级窗口，形成长期技术债务。
  competitive: 竞争对手借助更先进技术栈实现效率或体验跃迁时，保守选型可能导致产品迭代速度落后，尤其在 AI 等快速演进领域。
  ethical: 无
  additional:
  - 组织惯性导致拒绝合理创新
  - ' boring 技术栈可能降低对顶尖工程师的吸引力'
  - 创新代币分配不当造成核心业务能力投入不足
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: MySQL
  canonical_name: MySQL
  url: https://www.mysql.com/
  positioning: 关系型数据库老将，在文中被当作「无聊但足够好」的默认技术范例。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要稳定关系型数据库的企业后端团队
  - 追求运维风险可控的中小工程团队
  product_signal: 成熟的关系型数据库，能力与失败模式已被充分理解。
  market_signal: 被作者列为 boring and good 的代表，是企业默认选型的安全牌。
  differentiation: 与 Postgres 并列， boring 不等于落后，而是代表运维风险可控。
  watch_reason: 文章将 MySQL 作为克制技术冒险的标杆，对当前 AI 工程团队在控制基础设施复杂度、降低未知风险方面仍有直接参考价值。
  risk_notes:
  - 在高并发写入或复杂查询场景下仍需针对性调优与架构设计。
  score: 6.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - 作者将 MySQL 列为「无聊但足够好」的技术范例，认为其能力与失败模式已被充分理解。
  - 文章指出成熟技术如 MySQL、Postgres、PHP、Python 的共有特征是 boring and good，适合作为默认选型。
- object_type: product
  name: Postgres
  canonical_name: PostgreSQL
  url: https://www.postgresql.org/
  positioning: 开源关系型数据库，被作者归入 boring 技术的推荐默认选项。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要开源关系型数据库的 SaaS 团队
  - 重视数据完整性与扩展性的平台工程团队
  product_signal: 功能成熟、社区生态完善，适合作为默认持久化方案。
  market_signal: 与 MySQL 并列出现，代表经过生产验证的可靠选型。
  differentiation: 用与 MySQL 并列的方式说明 boring 也可以是功能强大且风险可控的选择。
  watch_reason: 文章以 Postgres 为例说明成熟数据库仍是多数业务的理性默认，对技术栈收敛与降低长期运维成本均有参考意义。
  risk_notes:
  - 引入新扩展或主版本升级时仍需评估运维与迁移成本。
  score: 6.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - Postgres 被作者归入「无聊但良好」的技术清单，作为推荐默认选择的关系型数据库之一。
  - 作者用 Postgres 与 MySQL 并列，说明 boring 不等于 bad，而是代表运维经验丰富、风险可控。
- object_type: product
  name: PHP
  canonical_name: PHP
  url: https://www.php.net/
  positioning: Web 脚本语言，在文中被列为 boring 技术的代表之一。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 统一后端技术栈的 Web 平台团队
  - 已有 PHP 生态投入的中小公司
  product_signal: 能力边界和失败模式已知，适合作为统一后端技术栈。
  market_signal: Etsy 曾努力将系统统一迁移到 PHP，并用其实现核心功能。
  differentiation: 与 Python 形成对照，说明统一栈比迁就程序员偏好更重要。
  watch_reason: PHP 作为「克制技术栈扩张」论点中的关键语言案例，对平台型团队统一后端选型、降低认知负载具有警示价值。
  risk_notes:
  - 生态更新节奏与现代工程实践支持度因团队而异。
  score: 6.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - PHP 被文章列为 boring 技术的代表，作者认为它能力已知、失败模式已知。
  - Etsy 曾努力将大部分系统统一迁移到 PHP，并基于 PHP/MySQL/Memcached/Gearman 构建 activity feeds。
- object_type: product
  name: Python
  canonical_name: Python
  url: https://www.python.org/
  positioning: 通用编程语言，在文中既被当作无聊技术，也被用于反例说明。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 通用后端与数据工程团队
  - 需避免为迁就偏好而强造中间层的组织
  product_signal: 成熟度高，但文章警告不应为了迁就程序员而强造中间层。
  market_signal: Etsy 早期因招聘 Python 程序员而引入不必要的中间层，造成长期交付困难。
  differentiation: 与 PHP 的对比揭示了「人因驱动选型」的风险。
  watch_reason: 文章用 Python 说明即使语言本身成熟，错误的使用动机仍会带来技术债，对 AI 团队避免人驱选型有警示意义。
  risk_notes:
  - 多语言共存会增加认知负载与跨栈运维复杂度。
  score: 6.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - Python 被列入无聊但可接受的技术清单，说明其成熟度足以作为默认工具。
  - Etsy 早期案例显示，公司招聘了一批 Python 程序员后为他们强造了一个无意义的中间层，导致长期技术债。
- object_type: product
  name: Memcached
  canonical_name: Memcached
  url: https://memcached.org/
  positioning: 分布式内存缓存系统，被作者视为 boring 缓存方案的典范。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要简单缓存层的 Web 服务团队
  - 已使用 PHP/MySQL 技术栈的平台
  product_signal: 简单可靠的键值缓存，是共享平台能力的一部分。
  market_signal: Etsy 用它与 PHP/MySQL/Gearman 构建 activity feeds 并随平台扩展 20 倍。
  differentiation: 作为保守栈中的缓存层，证明了有限技术组合能支撑复杂功能。
  watch_reason: Memcached 是「用现有栈解决复杂问题」成功案例的核心组件，对 AI 工程团队选择缓存默认选型、控制复杂度具有参考价值。
  risk_notes:
  - 纯内存缓存无法保证持久化，大规模集群需处理一致性问题。
  score: 7.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - Memcached 被列为 boring 技术的典型代表，适合作为默认缓存方案。
  - Etsy 使用 PHP/MySQL/Memcached/Gearman 技术栈实现 activity feeds，并在数年间随平台自然扩展 20 倍。
- object_type: product
  name: Redis
  canonical_name: Redis
  url: https://redis.io/
  positioning: 内存数据结构存储，在文中作为新潮缓存/数据存储的反例出现。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要内存数据结构存储的团队
  - 正在评估缓存与持久化选型的架构师
  product_signal: 文章暗示 Redis 可能让 activity feeds 更易实现，但会带来未知风险。
  market_signal: 被用来对比说明企业不应把有限创新代币消耗在可替代的基础设施上。
  differentiation: 与 Memcached 的对照体现了「够用即可」vs「更先进但风险更高」的取舍。
  watch_reason: 文章用 Redis 反思「为每个任务选最佳工具」的局部优化思维，提醒 AI 团队在基础设施选型上优先控制全局成本。
  risk_notes:
  - 新特性与运维边界若未充分理解，容易积累未知故障点。
  score: 6.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - Redis 被用作反例，说明如果用新潮技术实现 activity feeds 可能会更简单，但也会增加未知风险。
  - 文章强调，即使 Redis 可能让 activity feeds 更易实现，Etsy 仍选择基于现有栈构建，以获得长期可维护性。
- object_type: product
  name: Gearman
  canonical_name: Gearman
  url: http://gearman.org/
  positioning: PHP 作业调度服务器，Etsy 统一技术栈中的任务队列组件。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - PHP 生态下的异步任务处理团队
  - 构建保守技术栈的平台工程师
  product_signal: 作为任务队列与 PHP 生态集成，支撑后台作业处理。
  market_signal: 与 PHP/MySQL/Memcached 一起构成 Etsy activity feeds 的稳定基础。
  differentiation: 在保守栈中承担异步任务，证明现有工具组合足以扩展复杂功能。
  watch_reason: Gearman 是文章中「有限技术栈自然扩展 20 倍」的关键支撑组件，对 AI 平台在任务队列选型上保持克制具有参考价值。
  risk_notes:
  - 项目活跃度与社区规模相较现代消息队列偏弱，新选型需谨慎。
  score: 7.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - Gearman 被描述为 PHP 的作业服务器，是 Etsy 统一技术栈的一部分。
  - Etsy 基于 PHP/MySQL/Memcached/Gearman 构建 activity feeds，证明有限技术栈可以支撑复杂功能。
- object_type: product
  name: Solr
  canonical_name: Apache Solr
  url: https://solr.apache.org/
  positioning: 开源搜索平台，文中少数被明确认可的「必须引入的新技术」案例。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要全文搜索与分面能力的 Web 产品
  - 已论证现有栈无法满足搜索需求的团队
  product_signal: 提供带分面的全文搜索能力，弥补了 PHP 原生方案的不足。
  market_signal: 被作者用来证明当现有栈确实无法经济解决问题时，引入新技术是合理的。
  differentiation: 与 NodeJS/MongoDB 等潮流技术形成对比，是「有充分理由才引入」的正面例子。
  watch_reason: Solr 展示了如何在克制选型框架下理性引入新技术，对 AI 产品在搜索等专门场景中论证引入成本具有参考意义。
  risk_notes:
  - 搜索集群的运维与调优成本较高，引入前需充分论证收益。
  score: 7.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - Solr 是文章中少数被明确认定为必须引入的新技术案例，因为用原始 PHP 实现带分面的全文搜索并不现实。
  - 作者用 Solr 说明其立场并非绝对化：当现有栈确实无法经济地解决问题时，引入新技术是合理的。
- object_type: product
  name: NodeJS
  canonical_name: Node.js
  url: https://nodejs.org/
  positioning: JavaScript 运行时，在文中作为消耗「创新代币」的典型案例。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - JavaScript 全栈开发团队
  - 正在评估是否引入 Node.js 的组织
  product_signal: 作者认为它可能让网站开发更现代，但会占用有限的技术冒险预算。
  market_signal: 被直接点名作为 2015 年前后企业热衷但不必要的潮流选型。
  differentiation: 与 boring 技术栈对比，代表高未知风险与组织注意力分散。
  watch_reason: 文章以 Node.js 为例提醒非核心技术公司不要把创新资源浪费在基础设施时尚上，对 AI 创业团队控制技术冒险有参考价值。
  risk_notes:
  - 若组织缺乏 Node.js 专长，容易在调试与运维上付出额外成本。
  score: 6.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - 作者用 NodeJS 作为消耗创新代币的例子，说明选择它会占用公司有限的技术冒险预算。
  - 文章认为，除非公司是 JavaScript 咨询公司，否则把创新代币花在 NodeJS 这类工具上会增加失败或延迟的风险。
- object_type: product
  name: MongoDB
  canonical_name: MongoDB
  url: https://www.mongodb.com/
  positioning: 文档型 NoSQL 数据库，文中作为消耗创新代币的新潮数据库代表。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要文档型数据库的应用团队
  - 正在评估 NoSQL 选型的数据架构师
  product_signal: 作者指出选择它意味着承担数据存储层的未知风险。
  market_signal: 被用作警示案例，说明非数据库公司不应把创新资源投入底层数据存储。
  differentiation: 与 MySQL/Postgres 形成 boring vs shiny 的鲜明对比。
  watch_reason: 文章用 MongoDB 反思数据存储选型的全局成本，对 AI 数据平台在持久化方案选择上保持克制仍有启发。
  risk_notes:
  - 数据模型与一致性语义若未充分理解，可能导致数据层不稳定。
  score: 6.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - MongoDB 被作为消耗一枚创新代币的典型例子，说明新潮数据库的未知风险较高。
  - 作者指出，除非公司是数据库公司，否则把创新资源投入在底层数据存储技术上并不明智。
- object_type: project
  name: Etsy activity feeds
  canonical_name: Etsy Activity Feeds
  url: null
  positioning: Etsy 的 activity feeds 功能实现，是文章论证克制选型的核心案例。
  technical_signal: 基于 PHP/MySQL/Memcached/Gearman 的保守技术栈实现复杂 feeds 功能。
  adoption_signal: 上线后数年无人专门维护，却因共享平台自然扩展 20 倍。
  ecosystem_relevance: 证明在统一平台能力内求解，可显著降低长期运营成本。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该案例是「选择无聊技术」最具说服力的正面证据，对平台工程与长期可靠性决策有持续参考价值，尤其适合 AI 基础设施团队借鉴。
  risk_notes:
  - 案例依赖 Etsy 特定组织文化与平台成熟度，直接复制需谨慎。
  score: 9.0
  article_ids:
  - f9c2faed5b010c6e
  evidence_snippets:
  - 作者以 Etsy 的 activity feeds 功能为例，说明基于 PHP/MySQL/Memcached/Gearman 的保守实现能够在数年间随平台自然扩展
    20 倍。
  - 该项目在上线后数年无人专门维护，但因使用共享平台而稳定运行，体现了克制技术选型的长期收益。
---

Probably the single best thing to happen to me in my career was having had Kellan placed in charge of me. I stuck around long enough to see Kellan’s technical decisionmaking start to bear fruit. I learned a great deal *from* this, but I also learned a great deal as a *result* of this. I would not have been free to become the engineer that wrote Data Driven Products Now! if Kellan had not been there to so thoroughly stick the landing on technology choices.

In the year since leaving Etsy, I’ve resurrected my ability to care about technology. And my thoughts have crystallized to the point where I can write them down coherently. What follows is a distillation of the Kellan gestalt, which will hopefully serve to horrify him only slightly.

##### Embrace Boredom.

Let’s say every company gets about three innovation tokens. You can spend these however you want, but the supply is fixed for a long while. You might get a few more *after* you achieve a certain level of stability and maturity, but the general tendency is to overestimate the contents of your wallet. Clearly this model is approximate, but I think it helps.

If you choose to write your website in NodeJS, you just spent one of your innovation tokens. If you choose to use MongoDB, you just spent one of your innovation tokens. If you choose to use service discovery tech that’s existed for a year or less, you just spent one of your innovation tokens. If you choose to write your own database, oh god, you’re in trouble.

Any of those choices might be sensible if you’re a javascript consultancy, or a database company. But you’re probably not. You’re probably working for a company that is at least ostensibly rethinking global commerce or reinventing payments on the web or pursuing some other suitably epic mission. In that context, devoting any of your limited attention to innovating ssh is an excellent way to fail. Or at best, delay success [1].

What counts as boring? That’s a little tricky. “Boring” should not be conflated with “bad.” There is technology out there that is both boring and bad [2]. You should not use any of that. But there are many choices of technology that are boring and good, or at least good enough. MySQL is boring. Postgres is boring. PHP is boring. Python is boring. Memcached is boring. Squid is boring. Cron is boring.

The nice thing about boringness (so constrained) is that the capabilities of these things are well understood. But more importantly, their failure modes are well understood. Anyone who knows me well will understand that it’s only with a overwhelming sense of malaise that I now invoke the spectre of Don Rumsfeld, but I must.

When choosing technology, you have both known unknowns and unknown unknowns [3].

- A known unknown is something like:
*we don’t know what happens when this database hits 100% CPU.* - An unknown unknown is something like:
*geez it didn’t even occur to us that writing stats would cause GC pauses.*

Both sets are typically non-empty, even for tech that’s existed for decades. But for shiny new technology the magnitude of unknown unknowns is significantly larger, and this is important.

##### Optimize Globally.

I unapologetically think a bias in favor of boring technology is a good thing, but it’s not the only factor that needs to be considered. Technology choices don’t happen in isolation. They have a scope that touches your entire team, organization, and the system that emerges from the sum total of your choices.

Adding technology to your company comes with a cost. As an abstract statement this is obvious: if we’re already using Ruby, adding Python to the mix doesn’t feel sensible because the resulting complexity would outweigh Python’s marginal utility. But somehow when we’re talking about Python and Scala or MySQL and Redis people lose their minds, discard all constraints, and start raving about using the best tool for the job.

Your function in a nutshell is to map business problems onto a solution space that involves choices of software. If the choices of software were truly without baggage, you could indeed pick a whole mess of locally-the-best tools for your assortment of problems.

But of course, the baggage exists. We call the baggage “operations” and to a lesser extent “cognitive overhead.” You have to monitor the thing. You have to figure out unit tests. You need to know the first thing about it to hack on it. You need an init script. I could go on for days here, and all of this adds up fast.

The problem with “best tool for the job” thinking is that it takes a myopic view of the words “best” and “job.” Your job is keeping the company in business, god damn it. And the “best” tool is the one that occupies the “least worst” position for as many of your problems as possible.

It is basically always the case that the long-term costs of keeping a system working reliably vastly exceed any inconveniences you encounter while building it. Mature and productive developers understand this.

##### Choose New Technology, Sometimes.

Taking this reasoning to its *reductio ad absurdum* would mean picking Java, and then trying to implement a website without using anything else at all. And that would be crazy. You need some means to add things to your toolbox.

An important first step is to acknowledge that this is a process, and a conversation. New tech eventually has company-wide effects, so adding tech is a decision that requires company-wide visibility. Your organizational specifics may force the conversation, or they may facilitate developers adding new databases and queues without talking to anyone. One way or another you have to set cultural expectations that **this is something we all talk about**.

One of the most worthwhile exercises I recommend here is to **consider how you would solve your immediate problem without adding anything new**. First, posing this question should detect the situation where the “problem” is that someone really wants to use the technology. If that is the case, you should immediately abort.

It can be amazing how far a small set of technology choices can go. The answer to this question in practice is almost never “we can’t do it,” it’s usually just somewhere on the spectrum of “well, we could do it, but it would be too hard” [4]. If you think you can’t accomplish your goals with what you’ve got now, you are probably just not thinking creatively enough.

It’s helpful to **write down exactly what it is about the current stack that makes solving the problem prohibitively expensive and difficult.** This is related to the previous exercise, but it’s subtly different.

New technology choices might be purely additive (for example: “we don’t have caching yet, so let’s add memcached”). But they might also overlap or replace things you are already using. If that’s the case, you should **set clear expectations about migrating old functionality to the new system.** The policy should typically be “we’re committed to migrating,” with a proposed timeline. The intention of this step is to keep wreckage at manageable levels, and to avoid proliferating locally-optimal solutions.

This process is not daunting, and it’s not much of a hassle. It’s a handful of questions to fill out as homework, followed by a meeting to talk about it. I think that if a new technology (or a new service to be created on your infrastructure) can pass through this gauntlet unscathed, adding it is fine.

##### Just Ship.

Polyglot programming is sold with the promise that letting developers choose their own tools with complete freedom will make them more effective at solving problems. This is a naive definition of the problems at best, and motivated reasoning at worst. The weight of day-to-day operational toil this creates crushes you to death.

Mindful choice of technology gives engineering minds real freedom: the freedom to contemplate bigger questions. Technology for its own sake is snake oil.

*Update, July 27th 2015: I wrote a talk based on this article. You can see it here.*

- Etsy in its early years suffered from this pretty badly. We hired a bunch of Python programmers and decided that we needed to find something for them to do in Python, and the only thing that came to mind was creating a pointless middle layer that required years of effort to amputate. Meanwhile, the 90th percentile search latency was about two minutes. Etsy didn't fail, but it went several years without shipping anything at all. So it took longer to succeed than it needed to.
- We often casually refer to the boring/bad intersection of doom as “enterprise software,” but that terminology may be imprecise.
- In saying this Rumsfeld was either intentionally or unintentionally alluding to the Socratic Paradox. Socrates was by all accounts a thoughtful individual in a number of ways that Rumsfeld is not.
-
A good example of this from my experience is Etsy’s activity feeds. When we built this feature, we were working pretty hard to consolidate most of Etsy onto PHP, MySQL, Memcached, and Gearman (a PHP job server). It was much more complicated to implement the feature on that stack than it might have been with something like Redis (or maybe not). But it is absolutely possible to build activity feeds on that stack.

An amazing thing happened with that project: our attention turned elsewhere for several years. During that time, activity feeds scaled up 20x while

*nobody was watching it at all.*We made no changes whatsoever specifically targeted at activity feeds, but everything worked out fine as usage exploded because we were using a shared platform. This is the long-term benefit of restraint in technology choices in a nutshell.This isn’t an absolutist position--while activity feeds stored in memcached was judged to be practical, implementing full text search with faceting in raw PHP wasn't. So Etsy used Solr.