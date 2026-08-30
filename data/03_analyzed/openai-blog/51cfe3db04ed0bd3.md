---
title: The full stack behind abundant intelligence
source: https://openai.com/index/the-full-stack-behind-abundant-intelligence
author: []
published: Tue, 25 Aug 2026 07:05:00 GMT
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
- '2026-08-27'
- '2026-08-28'
description: OpenAI CFO Sarah Friar explains how advances across chips, compute, models,
  and products compound to deliver more useful intelligence at greater scale and lower
  cost.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 51cfe3db04ed0bd3
source_type: tech_blog
tldr: OpenAI 公布了首款自研推理芯片 Jalapeño 的首批实测性能：在 InferenceX 公共基准上以 GPT-OSS 120B 测试，其每千瓦峰值吞吐量更高、token
  延迟更低，并强调算力战略是一体化系统。
objective_summary: OpenAI 通过官方博客公布了其算力战略及首款自研推理芯片 Jalapeño 的实测性能结果。在 InferenceX 公共基准上使用
  GPT-OSS 120B 测试，Jalapeño 实现了比对比的商用系统更高的每千瓦峰值吞吐量和更低的 token 延迟，并在 DeepSeek R1 和 Kimi
  K2 上表现同样出色。OpenAI 将算力视为覆盖数据中心、芯片、前沿模型、开发者平台与产品的单一集成系统，目前其供应商组合包括微软、NVIDIA、AWS、AMD、Broadcom、Cerebras、CoreWeave、Oracle、SB
  Energy 与 SoftBank。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - OpenAI
  - Microsoft
  - NVIDIA
  - AWS
  - AMD
  - Broadcom
  - Cerebras
  - CoreWeave
  - Oracle
  - SB Energy
  - SoftBank
  technologies:
  - Jalapeño
  - GPT-OSS 120B
  - InferenceX
  - DeepSeek R1
  - Kimi K2
  key_people: []
key_logic_flow:
- OpenAI 将算力战略视为一个一体化系统，涵盖数据中心与芯片、前沿模型、开发者平台、消费与企业产品以及 AI 原生设备，各层之间相互增强。
- OpenAI 公布了首款自研推理芯片 Jalapeño 的首批实测性能结果，并称未来世代芯片已在研发中。
- 在 InferenceX 公共基准上使用 GPT-OSS 120B 测试，Jalapeño 比对比的商用系统实现了更高的每千瓦峰值吞吐量和更低的 token 延迟。
- Jalapeño 在 DeepSeek R1 和 Kimi K2 上的表现同样强劲，说明其收益可延伸至不同模型家族。
- OpenAI 的目标是保持帕累托前沿，为不同负载匹配最优系统，其供应商组合包括微软、NVIDIA、AWS、AMD、Broadcom、Cerebras、CoreWeave、Oracle、SB
  Energy 与 SoftBank。
object_mentions:
- object_type: product
  name: Jalapeño
  canonical_name: OpenAI Jalapeño
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 公布了首款自研推理芯片 Jalapeño 的首批实测性能结果，并称未来世代芯片已在研发中。
  - 在 InferenceX 公共基准上使用 GPT-OSS 120B 测试，Jalapeño 实现了更高的每千瓦峰值吞吐量和更低的 token 延迟。
  article_id: 51cfe3db04ed0bd3
- object_type: project
  name: InferenceX
  canonical_name: InferenceX
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - InferenceX 是一个公共基准，Jalapeño 在该基准上使用 GPT-OSS 120B 进行推理性能测试。
  article_id: 51cfe3db04ed0bd3
- object_type: model
  name: GPT-OSS 120B
  canonical_name: GPT-OSS 120B
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - InferenceX 基准使用 GPT-OSS 120B 作为测试模型来评估 Jalapeño 的峰值吞吐量和 token 延迟。
  article_id: 51cfe3db04ed0bd3
- object_type: model
  name: DeepSeek R1
  canonical_name: DeepSeek R1
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Jalapeño 在 DeepSeek R1 上也表现强劲，说明其性能优势可延伸至不同模型家族。
  article_id: 51cfe3db04ed0bd3
- object_type: model
  name: Kimi K2
  canonical_name: Kimi K2
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Jalapeño 在 Kimi K2 上同样表现良好，进一步验证了其跨模型家族的通用性能增益。
  article_id: 51cfe3db04ed0bd3
extract_result: success
impact_score:
  score: 7.5
  reason: 评分依据：OpenAI 作为前沿模型龙头发布首款自研推理芯片 Jalapeño 的实测数据，标志着其从纯模型/API 公司向垂直整合算力厂商转型的关键落子。此举直接冲击推理成本结构与对
    NVIDIA 等硬件供应商的议价格局，并为'模型厂商自研芯片'这一趋势（对标 Google TPU、AWS Inferentia、Meta MTIA）再添重量级案例，属于改变局部竞争格局的重要事件。但数据为官方自报口径、对比的商用系统型号与测试条件未完全披露，且仅覆盖推理而非训练场景，短期冲击力未达
    ChatGPT 级别的范式转移程度，故给 7.5 分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 自报基准是否存在水分，以及自研芯片能否真正转化为 API 降价与更低推理延迟
hype_assessment:
  level: medium
  reason: 判定依据：文章为官方 PR 口径，存在'一体化系统''帕累托前沿'等宏大叙事包装；'更高的每千瓦峰值吞吐量'与'更低的 token 延迟'属于自报成绩，对比基准
    InSferenceX 的商用系统清单及测试配置细节未完整披露，存在一定自选参照物的空间。但芯片确实已流片并跑出实测数据、未来世代在研，并非纯概念炒作，包装程度中等。
information_entropy: medium
domain_disruption:
  technical_innovation: 首次实现'模型+serving 软件+芯片+内存+网络'一体化协同设计的推理闭环，以每千瓦峰值吞吐量为核心能效指标，通过软硬件联合优化在推理吞吐、延迟与能耗上取得自报优势，并将收益验证延伸至
    DeepSeek R1、Kimi K2 等异族模型，证明其增益不依赖单一模型架构。
  business_model: 垂直整合战略下探：自研推理芯片显著压低推理边际成本，为 API 降价与规模化 serving 提供经济性基础，同时增强对 NVIDIA、Microsoft
    等关键供应商的议价权，避免单一算力源锁定。其'帕累托前沿'策略（保留微软、AWS、AMD、Broadcom、Cerebras、CoreWeave、Oracle
    等多元供应组合）本质上是把算力采购从依赖关系重构为可替换的商品化市场。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 算力是 AI 公司的最大成本项与规模化瓶颈，控制推理成本即控制定价权。该事件的复利逻辑链为：芯片与模型/推理软件协同设计 → 每千瓦峰值吞吐提升
    + token 延迟下降 → 单 token 推理成本下降 → 支撑更低定价与更大规模使用 → 更多使用产生更多学习信号 → 模型能力增强 → 需求进一步放大，形成自我强化的飞轮。以
    3-5 年维度看，agent 普及将推动推理量呈数量级增长，届时谁能把推理成本压到最低谁就掌握生态入口，自研芯片有望成为 OpenAI 长期基础设施底座，具备极强复利效应。但需保持审慎：当前数据来自
    OpenAI 自设的 InferenceX 基准，存在样本选择与 PR 成分；从工程样片到大规模量产、良率爬坡、软件生态成熟仍需多代迭代（Google TPU
    亦经历多代才成气候）。属'高确定性方向的早期验证'阶段，故给 8 分而非更高。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Broadcom
- TSMC
competitive_casualty:
- NVIDIA
- 小型 AI 实验室
- 第三方推理芯片厂商（Groq、Cerebras 等）
market_opportunities:
- 鉴于 OpenAI 强调'按负载匹配最优系统'的多供应商异构战略，第三方可切入芯片中立(agnostic)的推理调度与成本优化中间件赛道，帮助云厂商和企业客户在英伟达、AMD
  与自研芯片之间动态路由负载、优化单位 token 成本。
- InferenceX 这类公共推理基准的走红表明独立的 AI 硬件能效评测基础设施存在市场空白，创业团队可提供可复现、经第三方审计的推理性能与每千瓦吞吐量评测服务，为算力采购决策提供可信依据。
- Jalapeño 将'每千瓦吞吐量'确立为核心竞争指标，指向 AI 数据中心能效优化（液冷、内存带宽、网络互联、模型服务软件栈）与绿色算力咨询服务的结构化机会，适合服务正在扩张
  AI 基础设施的云厂商与大型企业。
risk_matrix:
  regulatory: 自研芯片涉及先进制程代工与出口管制合规风险；OpenAI 将模型、芯片与数据中心垂直整合，可能引发反垄断与供应商公平竞争审查，监管机构或对其供应链排他性安排与市场支配力展开调查。
  technological: 实测数据来自 OpenAI 自家基准与自家模型（GPT-OSS 120B），属于自我宣称且未经第三方独立验证，存在样本选择偏差；自研芯片生态（编译器、算子库、互联）成熟度不足，且英伟达下一代平台、谷歌
    TPU、亚马逊 Trainium 等竞品可能快速反超，使当前优势被抹平。
  competitive: OpenAI 既是英伟达、微软、博通等供应商的大客户又正变为潜在竞争者，可能引发定价、产能优先权与技术授权层面的供应链博弈；同时谷歌、亚马逊、Meta
    均已布局自研芯片，OpenAI 入场时间不早，差异化空间有限。
  ethical: 能效提升可能诱发杰文斯式回弹——推理成本下降将刺激更多 AI 负载，总体能耗与数据中心扩张不减反增，加剧能源与水资源压力；'abundant
    intelligence' 叙事也隐含更广泛的就业替代与自动化冲击风险。
  additional:
  - 先进制程产能地理高度集中（如台积电），地缘政治紧张可能中断芯片供应链；客户与供应商身份重叠带来信息保密与利益冲突风险。
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: Jalapeño
  canonical_name: OpenAI Jalapeño
  url: null
  positioning: OpenAI 首款自研推理芯片，专为 OpenAI 自身推理工作负载设计，是算力一体化系统中连接数据中心、前沿模型与产品的关键硬件层。
  technical_signal: Jalapeño 在 GPT-OSS 120B 测试中实现更高每千瓦峰值吞吐量与更低 token 延迟，性能收益可延伸至 DeepSeek
    R1 与 Kimi K2 等不同模型家族。
  adoption_signal: OpenAI 已将其作为自研推理算力底座投入使用，与微软、NVIDIA 等外部加速器并存，形成第一方芯片路径。
  ecosystem_relevance: 作为 OpenAI 算力一体化系统的一层，与数据中心、前沿模型、开发者平台与产品相互增强，反哺更优产品体验。
  target_users:
  - OpenAI 自身推理服务与模型部署团队
  - 使用 OpenAI API 与产品的开发者及企业用户
  product_signal: 首款自研推理芯片已有实测性能数据，未来世代芯片已在研发中，标志 OpenAI 在硬件层建立第一方能力。
  market_signal: 在推理算力竞争加剧的背景下，OpenAI 借自研芯片降低对单一供应商依赖，供应商组合已扩展至微软、NVIDIA、AWS、AMD、Broadcom
    等。
  differentiation: 与对比的商用系统相比，Jalapeño 在每千瓦峰值吞吐量与 token 延迟上更优，并通过模型、软件、芯片与网络协同开发获得系统级优势。
  watch_reason: OpenAI 自研芯片是算力自主战略的关键里程碑，首批实测性能与未来世代进展将直接影响其推理成本、规模化能力及对供应商的议价空间，值得持续跟踪。
  risk_notes:
  - 实测数据来自 OpenAI 自选基准与模型，对比系统选择与测试口径可能影响结果公允性。
  - 自研芯片规模化量产与良率爬坡存在不确定性，实际部署成本与商用加速器相比仍待验证。
  - OpenAI 依赖第三方供应商的格局短期内不会改变，自研芯片能否形成实质性成本优势尚需更多数据。
  score: 9.0
  article_ids:
  - 51cfe3db04ed0bd3
  evidence_snippets:
  - OpenAI 公布了首款自研推理芯片 Jalapeño 的首批实测性能结果，并称未来世代芯片已在研发中。
  - 在 InferenceX 公共基准上使用 GPT-OSS 120B 测试，Jalapeño 实现了更高的每千瓦峰值吞吐量和更低的 token 延迟。
- object_type: project
  name: InferenceX
  canonical_name: InferenceX
  url: null
  positioning: InferenceX 是一个用于推理性能对比的公共基准，以 GPT-OSS 120B 等模型衡量芯片系统的每千瓦峰值吞吐量与 token
    延迟。
  technical_signal: InferenceX 以 GPT-OSS 120B 为测试负载，为推理芯片提供标准化性能对比基准，可覆盖不同模型家族的扩展测试。
  adoption_signal: OpenAI 选择 InferenceX 作为首款自研芯片的性能发布基准，表明该基准开始被头部 AI 厂商采信。
  ecosystem_relevance: 作为公共基准，InferenceX 有望成为推理芯片与商用加速器横向对比的参考标尺，推动算力性能披露更透明。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: InferenceX 若成为推理芯片性能对比的公共标准，将影响整个算力市场对能效与延迟的评价方式，值得跟踪其覆盖模型与参与厂商的扩展。
  risk_notes:
  - InferenceX 目前信息有限，基准测试口径、模型覆盖范围与治理机制尚未充分披露，跨系统可比性存疑。
  - 该基准目前主要由 OpenAI 单方面引用，独立性与行业公信力仍需更多采用方验证。
  score: 5.0
  article_ids:
  - 51cfe3db04ed0bd3
  evidence_snippets:
  - InferenceX 是一个公共基准，Jalapeño 在该基准上使用 GPT-OSS 120B 进行推理性能测试。
---

Progress in AI compounds fastest when the entire system improves together. That is how I think about OpenAI’s compute strategy: one integrated system spanning data centers and chips, frontier models, our developer platform, consumer and enterprise products, and AI-native devices, with each layer strengthening the next.

Better software makes hardware more productive. Hardware designed for our workloads improves speed and efficiency. More capable models unlock better products, which generate more demand, usage, and learning. Those signals flow back through the system and help us improve it again.

Today, we shared the first measured performance results from Jalapeño, OpenAI’s first custom inference chip. On InferenceX, a public benchmark using GPT‑OSS 120B, Jalapeño delivered more peak throughput per kilowatt and lower token latency than the commercial systems in the comparison. It also performed strongly on DeepSeek R1 and Kimi K2, showing that its gains extend across model families.

Jalapeño gives us greater control over how our models run and over the economics of serving them. By developing the model, serving software, chip, memory, and network together, we can improve throughput, latency, energy efficiency, and cost as one system. It creates a credible first-party path alongside the accelerators we use from other partners, expanding our ability to match each workload to the strongest system at the right economics. We now have working first-party silicon with measured results, and future generations are already underway.

Different workloads place different demands on the system. Frontier training, high-volume inference, and always-on agents have different requirements across chips, software, networks, power, and latency.

Our goal is to stay on the Pareto frontier: continually seeking the strongest mix of capability, speed, reliability, efficiency, and cost for each workload. Different chips and providers lead on different dimensions, and the frontier keeps moving.

Our portfolio gives us the range to meet those needs. Microsoft’s compute and NVIDIA’s chips have been foundational to OpenAI’s growth. Today, our portfolio also includes AWS, AMD, Broadcom, Cerebras, CoreWeave, Oracle, SB Energy and SoftBank. Each brings different strengths across cloud infrastructure, accelerated computing, low-latency inference, data-center development, and energy delivery.