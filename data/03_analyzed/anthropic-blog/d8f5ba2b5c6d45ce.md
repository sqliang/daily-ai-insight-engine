---
title: Accelerating Scientific Research
source: https://www.anthropic.com/news/accelerating-scientific-research
author: []
published: '2026-08-27'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
- '2026-08-29'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d8f5ba2b5c6d45ce
source_type: tech_blog
tldr: Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，并通过 AI for Science 项目支持全球科研人员，其
  Opus 4.5 在科学类基准上显著提升。文章还介绍了斯坦福大学基于 Claude 的通用生物医学智能体 Biomni，它能整合数百种工具并覆盖超过 25 个生物学子领域。
objective_summary: Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，这是一套连接器和技能套件，旨在让
  Claude 成为更好的科研协作工具。Anthropic 持续投入提升 Claude 的科研能力，Opus 4.5 在图表解读、计算生物学和蛋白质理解基准上显著改进，并通过
  AI for Science 项目向全球高影响力科研项目提供免费 API 额度。研究人员基于 Claude 构建的自定义系统覆盖实验规划、数据分析和项目压缩等科研全流程。斯坦福大学开发的
  Biomni 智能体平台将数百种生物医学工具整合为单一系统，支持自然语言请求，能在超过 25 个生物学子领域形成假设、设计实验方案并执行分析。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Stanford University
  technologies:
  - Claude
  - Claude for Life Sciences
  - Opus 4.5
  key_people: []
key_logic_flow:
- Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，这是一套连接器和技能套件，旨在让 Claude 成为更好的科研协作伙伴。
- Anthropic 持续投入将 Claude 打造为最具科研能力的模型，Opus 4.5 在图表解读、计算生物学和蛋白质理解基准上展现出显著改进。
- Anthropic 通过 AI for Science 项目为全球从事高影响力科研项目的研究人员提供免费 API 额度，并据此理解科学家使用 AI 的方式。
- 研究人员开发的自定义系统让 Claude 覆盖科研全流程，包括判断该做哪些实验、把通常耗时数月的项目压缩到数小时、在海量数据中发现人类容易忽视的模式。
- 斯坦福大学推出 Biomni 通用生物医学智能体平台，将数百种数据库、软件包和实验方案整合为单一系统，由 Claude 驱动的智能体自动导航。
- Biomni 支持研究者用自然语言提出请求并自动选择合适资源，能形成假设、设计实验协议，并在超过 25 个生物学子领域执行分析。
object_mentions:
- object_type: product
  name: Claude for Life Sciences
  canonical_name: Claude for Life Sciences
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，这是一套连接器和技能套件，旨在让 Claude 成为更好的科研协作伙伴。
  article_id: d8f5ba2b5c6d45ce
- object_type: product
  name: Biomni
  canonical_name: Biomni
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Biomni 是斯坦福大学开发的通用生物医学智能体平台，将数百种工具、软件包和数据集整合为单一系统，由 Claude 驱动的智能体自动导航。
  article_id: d8f5ba2b5c6d45ce
- object_type: project
  name: AI for Science program
  canonical_name: Anthropic AI for Science
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 通过 AI for Science 项目向全球从事高影响力科研项目的领先研究人员提供免费 API 额度。
  article_id: d8f5ba2b5c6d45ce
- object_type: model
  name: Opus 4.5
  canonical_name: Claude Opus 4.5
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Anthropic 表示 Opus 4.5 在图表解读、计算生物学和蛋白质理解基准上展现出显著改进，体现了其对科研能力的持续投入。
  article_id: d8f5ba2b5c6d45ce
extract_result: success
impact_score:
  score: 5.5
  reason: 评分依据：这是一篇 Anthropic 官方 PR 文章，属于应用落地类新闻而非模型架构突破。其实际信息点包括：Claude for Life
    Sciences 连接器/技能套件、Opus 4.5 在图表解读/计算生物学/蛋白质理解基准上的自报提升、AI for Science 免费 API 资助计划，以及斯坦福
    Biomni 智能体平台。其中 Biomni 将数百种生物医学工具整合进单一智能体、覆盖 25+ 子领域并支持自然语言驱动，对科研工具生态有较强的示范效应和竞争格局扰动；但整体仍是生态卡位与场景落地，未触及模型能力或训练范式的本质跃迁，短期不构成行业范式转移，因此给
    5.5 分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: Opus 4.5 科学基准提升为厂商自报数据、缺乏第三方复现，以及 Biomni 整合数百工具后的真实可靠性与可扩展性
hype_assessment:
  level: medium
  reason: 判定依据：文章使用了'最具科研能力的模型''重塑科研工作方式''消除瓶颈'等典型的 PR 拔高措辞，且 Opus 4.5 的基准提升属于厂商自证、缺少独立评测数据，存在一定包装成分。但另一方面，Claude
    for Life Sciences 与 AI for Science 计划均有实质性产品与资源投入，Biomni 也有可验证的具体能力描述（数百工具、25+
    子领域），并非纯概念炒作或空头支票，故判定为 medium。
information_entropy: medium
domain_disruption:
  technical_innovation: 底层依托 Opus 4.5 在多模态图表解读与蛋白质理解上的能力增强，Biomni 展示了'自然语言驱动 + 海量工具编排'的通用生物医学智能体范式：把碎片化的数百个数据库、软件包与实验协议封装为单一导航系统，跨
    25 个以上子领域完成假设生成、实验方案设计与分析执行，属于应用/工程层创新，而非模型架构层面的本质突破。
  business_model: Anthropic 通过 AI for Science 免费 API 额度扶持高影响力科研项目，以'科研场景前置绑定'抢占科学家心智与早期工具链依赖，是典型的云厂商生态打法；Claude
    for Life Sciences 以连接器和 Skills 形式切入，意图在 AI for Science 商业化尚未定型的窗口期完成卡位，未来可向科研机构订阅、企业级合规方案等方向变现。
engineering_complexity: prototype
compound_value:
  score: 7.2
  reason: Anthropic 押注 AI for Science 具备较强复利逻辑：科研工作流一旦嵌入 Claude 生态，将形成'模型能力提升→更多高质量科研产出→科研使用数据反哺模型'的数据飞轮，且科学发现本身的长期影响力极高。斯坦福
    Biomni 展示的科学智能体通用性（覆盖 25+ 子领域、整合数百种工具）表明这一基础设施正在成型，3-5 年后 AI 原生科研大概率是主流范式。但当前信息仅为
    pr_statement，真实科研产出（如诺奖级发现）尚未验证，免费 API 换取留存与付费转化的商业模式也未证实，且面临 DeepMind、OpenAI
    等强竞争，故落在'细分赛道基础设施潜力股'的高端而非确定性基石区间。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Stanford University
- Biomni
competitive_casualty:
- 传统生命科学软件厂商（LIMS/ELN）
- 非 AI 原生的生物信息学工具链
- 外包生物信息学分析服务商
market_opportunities:
- 创业者可基于 Claude for Life Sciences 的连接器与技能生态，面向基因组学、蛋白质工程等垂直子领域开发科研智能体，复用 Biomni 的"工具整合+自然语言导航"架构模式
- 生物医药企业与 CRO 可部署 Biomni 类通用生物医学智能体，将数百种数据库与实验方案整合为单一系统，压缩实验规划与数据分析周期，显著降低研发成本
- 参照 AI for Science 以免费 API 额度切入高影响力科研项目的获客模式，科研场景可作为 AI 公司获取高价值专业用户并沉淀垂直领域数据资产的战略入口
risk_matrix:
  regulatory: 生命科学 AI 面临双重用途管控、生物安全审查与医疗研究工具监管（如 FDA），Anthropic 强化科研能力可能进一步触发出口管制与合规审查关注
  technological: 科学基准上的领先易被开源模型或竞争对手快速追平；Biomni 类 Agent 在复杂实验流程中的可靠性与结果可复现性尚未充分验证，存在隐蔽偏差与工具集成失败风险
  competitive: Google DeepMind（AlphaFold 等）、OpenAI、微软均在重兵布局科学发现与生物医药 AI，科研工具生态可能被头部平台锁定，垂直玩家面临巨头碾压与价格战
  ethical: AI 自动形成假设与执行分析可能放大数据中的既有偏差，产生不可靠的科研结论；在合成生物学等场景存在双重用途与生物安全伦理风险；自动化压缩研究流程可能冲击科研辅助人员就业结构
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Claude for Life Sciences
  canonical_name: Claude for Life Sciences
  url: null
  positioning: Anthropic 推出的生命科学领域连接器与技能套件，旨在让 Claude 成为更专业的科研协作伙伴，覆盖实验规划与数据分析等科研环节。
  technical_signal: 产品底座基于 Opus 4.5，其在图表解读、计算生物学和蛋白质理解基准上展现出显著改进。
  adoption_signal: 文章显示科研人员已基于 Claude 构建覆盖实验规划与数据分析等科研全流程的自定义系统，验证了该套件的采用方向。
  ecosystem_relevance: 该套件与 AI for Science 项目及 Biomni 等研究系统形成生态协同，共同构建 Anthropic 科研生态。
  target_users:
  - 生命科学领域研究人员
  - 生物医学与计算生物学团队
  product_signal: 该套件将连接器与技能整合进 Claude 工作流，使科研人员能用自然语言驱动实验规划、数据分析和项目压缩等任务。
  market_signal: Anthropic 通过免费 API 额度支持科研人员并换取使用反馈，正加速渗透生命科学这一高价值垂直市场。
  differentiation: 与通用 AI 助手相比，它专注科研全流程协作，能处理需要深度专业知识且此前难以规模化扩展的科研任务。
  watch_reason: Claude for Life Sciences 是 Anthropic 从通用模型向垂直科研场景产品化延伸的标志，其连接器与技能套件模式能否沉淀为可复用的科研工作流，将决定
    Anthropic 在生命科学市场的长期竞争位势，值得持续跟踪。
  risk_notes:
  - 生命科学场景对结果准确性与可解释性要求极高，模型幻觉可能制约其在实验决策等关键环节的落地。
  - 目前采用主要依赖免费额度驱动，尚未披露商业化定价，长期收入模式仍存在不确定性。
  score: 8.0
  article_ids:
  - d8f5ba2b5c6d45ce
  evidence_snippets:
  - Anthropic 于 2025 年 10 月推出 Claude for Life Sciences，这是一套连接器和技能套件，旨在让 Claude 成为更好的科研协作伙伴。
- object_type: product
  name: Biomni
  canonical_name: Biomni
  url: null
  positioning: 斯坦福大学开发的通用生物医学智能体平台，将数百种数据库、软件包和实验方案整合为单一系统，由 Claude 驱动智能体自动导航。
  technical_signal: 作为 Agentic AI 在生物医学领域的前沿应用，Biomni 由 Claude 驱动智能体自动导航数百种工具资源。
  adoption_signal: null
  ecosystem_relevance: Biomni 深度绑定 Claude 生态，其落地效果将直接影响 Anthropic 在学术科研领域的渗透与口碑。
  target_users:
  - 生物医学研究人员
  - 生命科学实验室与科研机构
  product_signal: 支持研究者用自然语言提出请求并自动选择合适资源，能形成假设、设计实验协议并在超过 25 个生物学子领域执行分析。
  market_signal: Biomni 瞄准科研工具碎片化这一长期痛点，若能验证有效，有望成为生物医学研究的基础设施级平台。
  differentiation: 与单点科研工具不同，Biomni 以单一智能体系统整合数百种资源，显著降低研究者跨平台选择与学习成本。
  watch_reason: Biomni 是文章中最具代表性的 Claude 科研应用案例，其通用生物医学智能体架构直击科研工具碎片化痛点，若验证有效可能重塑生物医学研究的基础设施形态，值得持续跟踪。
  risk_notes:
  - Biomni 由斯坦福大学主导研发，尚处研究阶段，其规模化部署与长期维护的可持续性有待观察。
  - 跨超 25 个子领域的自动化分析仍面临数据质量与生物复杂性的挑战，输出可靠性需进一步验证。
  score: 7.0
  article_ids:
  - d8f5ba2b5c6d45ce
  evidence_snippets:
  - Biomni 是斯坦福大学开发的通用生物医学智能体平台，将数百种工具、软件包和数据集整合为单一系统，由 Claude 驱动的智能体自动导航。
- object_type: project
  name: AI for Science program
  canonical_name: Anthropic AI for Science
  url: null
  positioning: Anthropic 面向全球高影响力科研项目的资助计划，通过提供免费 API 额度支持领先研究人员并获取真实使用反馈。
  technical_signal: 该计划为 Anthropic 提供科学家真实使用 AI 的方式洞察，直接反哺 Opus 4.5 等模型科研能力的迭代方向。
  adoption_signal: 计划已覆盖全球领先科研人员，催生出覆盖实验规划、数据分析与项目压缩等科研全流程的自定义系统。
  ecosystem_relevance: 该计划连接学术界与产业界，帮助 Anthropic 建立科研生态影响力并挖掘高价值科研合作机会。
  target_users:
  - 从事高影响力科研项目的全球领先研究人员
  product_signal: null
  market_signal: 该项目是 Anthropic 科研垂直市场布局的关键抓手，以免费额度换取生态入口与使用数据。
  differentiation: 与纯商业销售策略不同，该计划以公益资助形式建立科研信任，形成差异化的生态壁垒。
  watch_reason: AI for Science 是 Anthropic 科研战略的生态枢纽，其覆盖规模与产出的科研合作成果将决定 Claude 在学术界的渗透深度，值得跟踪其扩展节奏与典型案例。
  risk_notes:
  - 免费 API 额度模式依赖 Anthropic 持续投入，预算调整可能导致计划规模缩减或支持范围收窄。
  - 文章未披露计划的具体规模与量化成果，作为参考提及对象其实际影响力的证据仍较有限。
  score: 5.0
  article_ids:
  - d8f5ba2b5c6d45ce
  evidence_snippets:
  - Anthropic 通过 AI for Science 项目向全球从事高影响力科研项目的领先研究人员提供免费 API 额度。
---

# How scientists are using Claude to accelerate research and discovery

Last October we launched Claude for Life Sciences—a suite of connectors and skills that made Claude a better scientific collaborator. Since then, we've invested heavily in making Claude the most capable model for scientific work, with Opus 4.5 showing significant improvements in figure interpretation, computational biology, and protein understanding benchmarks. These advances, informed by our partnerships with researchers in academia and industry, reflect our commitment to understanding exactly how scientists are using AI to accelerate progress.

We’ve also been working closely with scientists through our AI for Science program, which provides free API credits to leading researchers working on high-impact scientific projects around the world.

These researchers have developed custom systems that use Claude in ways that go far beyond tasks like literature reviews or coding assistance. In the labs we spoke to, Claude is a collaborator that works across all stages of the research process: making it easier and more cost-effective to understand which experiments to run, using a variety of tools to help compress projects that normally take months into hours, and finding patterns in massive datasets that humans might overlook. In many cases it’s eliminating bottlenecks, handling tasks that require deep knowledge and have previously been impossible to scale; in some it’s enabling entirely different research approaches than researchers have traditionally been able to take.

In other words, Claude is beginning to reshape how these scientists work—and point them towards novel scientific insights and discoveries.

## Biomni: a general-purpose biomedical agent with access to hundreds of tools and databases

One bottleneck in biological research is the fragmentation of tools: there are hundreds of databases, software packages, and protocols available, and researchers spend substantial time selecting from and mastering various platforms. That’s time that, in a perfect world, would be spent on running experiments, interpreting data, or pursuing new projects.

Biomni, an agentic AI platform from Stanford University, collects hundreds of tools, packages, and data-sets into a single system through which a Claude-powered agent can navigate. Researchers give it requests in plain English; Biomni automatically selects the appropriate resources. It can form hypotheses, design experimental protocols, and perform analyses across more than 25 biological subfields.