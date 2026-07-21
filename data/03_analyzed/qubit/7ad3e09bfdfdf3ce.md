---
title: PPIO发布智能模型网关，打造面向Agent时代的智能Token工厂
source: https://www.qbitai.com/2026/07/453467.html
author:
- '[[量子位的朋友们]]'
published: '2026-07-17'
created: '2026-07-18'
manifest_dates:
- '2026-07-18'
description: 万亿Token调用量验证
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7ad3e09bfdfdf3ce
source_type: news_media
tldr: PPIO于WAIC 2026期间发布Agentic Cloud新定位与智能模型网关产品。智能模型网关通过混合模型推理（MoM）和智能调度提升Token智能密度并降低成本，其日均Token调用量已超1.2万亿。
objective_summary: 2026年7月17日，PPIO在上海WAIC期间正式发布Agentic Cloud新定位及智能模型网关产品。PPIO联合创始人兼CEO姚欣提出Agent生产力公式，认为Token智能密度和Agent
  Loop时长决定Agent性能。智能模型网关具备混合模型（MoM）和模型调度两项核心功能，可将智能水平提升20%、成本降低50%-60%。PPIO还推出Agent
  Harness框架以延长Agent运行时长，并展示了PPClaw、PPHermes等托管Agent产品。截至2026年6月，PPIO日均Token调用量超1.2万亿，较2025年同期增长超8倍。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - PPIO
  - 中国信通院
  - Anthropic
  technologies:
  - Agentic Cloud
  - MoM
  - Agent Harness
  - Token Factory
  - 沙箱
  - E2B
  key_people:
  - 姚欣
key_logic_flow:
- PPIO于2026年7月17日在WAIC期间正式发布Agentic Cloud新定位和智能模型网关产品。
- 姚欣提出Agent生产力公式：Agent生产力 = Token智能密度 × Agent Loop时长。
- 智能模型网关提供混合模型（MoM）和模型调度两大功能，通过多模型交叉验证提升推理质量，并根据任务类型智能路由到合适模型。
- 在DRACO基准测试中，PPIO通过融合Mimo-V2.5-Pro、Kimi-K2.7和GLM-5.2进行混合推理，性能接近Claude Fable5，成本仅为后者的七分之一。
- PPIO Agent沙箱冷启动时延低于200ms，支持上万个沙箱同时创建，综合使用成本较同类产品降低90%以上。
- 截至2026年6月PPIO日均Token调用量超1.2万亿，在中国独立AI云计算服务提供商中排名第一，并入选中国信通院首批企业级Token服务性能攀登基线。
object_mentions:
- object_type: product
  name: PPIO Agentic Cloud
  canonical_name: PPIO Agentic Cloud
  url: https://www.ppio.cloud
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PPIO于WAIC 2026期间正式发布全新Agentic Cloud定位，致力于为Agent打造原生适配的全栈云服务体系。
  - Agentic Cloud建立在PPIO智能Token工厂的万亿级调用量验证之上，是面向Agent产业爆发的战略升级。
  article_id: 7ad3e09bfdfdf3ce
- object_type: product
  name: PPIO 智能模型网关
  canonical_name: PPIO 智能模型网关
  url: https://www.ppio.cloud
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PPIO最新发布的智能模型网关通过给AI应用提供智能调度中心，让每次模型调用都变成一场专家会诊。
  - 智能模型网关可将智能水平提升20%，将成本降低50%-60%，兼具混合模型推理和智能调度两大功能。
  article_id: 7ad3e09bfdfdf3ce
- object_type: product
  name: PPIO Agent 沙箱
  canonical_name: PPIO Agent 沙箱
  url: https://www.ppio.cloud
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - PPIO Agent沙箱冷启动时延低于200ms，采用系统级安全隔离，支持上万个沙箱同时创建。
  - PPIO Agent沙箱综合使用成本较同类产品降低90%以上，上线一年业务规模增长超120倍。
  article_id: 7ad3e09bfdfdf3ce
- object_type: product
  name: PPClaw/PPHermes
  canonical_name: PPClaw/PPHermes
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - PPIO通过Harness手段推出的PPClaw和PPHermes等托管Agent，可以实现7x24小时长时间运行且具备自我修复能力。
  article_id: 7ad3e09bfdfdf3ce
extract_result: success
impact_score:
  score: 5.5
  reason: PPIO作为中国独立AI云服务商，日均Token调用量1.2万亿（8倍同比增长）表明其已具备实质性业务体量。MoM（混合模型推理）和智能模型网关的发布，瞄准了Agent时代多模型协同与成本优化的真实痛点，DRACO基准中声称以Claude
    Fable5七分之一成本达到接近性能是一个有吸引力的工程化叙事。但该产品主要面向中国市场，全球知名度和竞争压力有限；模型路由/网关并非全新品类（业内已有OpenAI、Anthropic等类似方案），且PR声明属性意味着部分数据缺乏独立验证。对于中国AI云基础设施赛道，这是一个改变局部竞争格局的重要发布，但并非全球范式转移。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: MoM混合推理的性能提升和成本降低能否在真实长尾场景中稳定复现
hype_assessment:
  level: medium
  reason: 文章提供了实质性数据（日均1.2万亿Token、TPS≥55/s、TTFT≤0.9s、沙箱冷启动<200ms、业务增长120倍），但大量使用'智能Token工厂'、'专家会诊'、'Agent生产力公式'等营销包装语言。与Claude
    Fable5的对比存在模糊性（Fable5可能并非已公开发布模型），'智能水平提升20%'等量化指标缺少独立第三方复现验证。整体来看，干货与水分并存，包装程度中等。
information_entropy: medium
domain_disruption:
  technical_innovation: MoM（Mixture of Models）混合模型推理架构，通过多模型交叉验证与智能任务路由实现推理质量与成本动态平衡，为'以工程手段弥补单模型短板'提供了可落地的参考范式。Agent沙箱冷启动<200ms且支持上万并行实例，在工程性能上有实质突破。
  business_model: 以'Token工厂'定位构建多模型聚合与智能调度层，充当模型提供商与应用开发者之间的成本优化中间件（Inference Optimization
    as a Service），可能推动中国AI云市场从'单模型托管'向'多模型智能路由'的商业模式转型。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: PPIO的智能模型网关抓住了Agent渗透率爆发时的核心瓶颈：Token成本与质量的工程化平衡。日均1.2万亿Token调用量、同比8倍增长是强有力的PMF验证，说明市场对这一中间层有真实且急迫的需求。核心复利逻辑来自三方面：第一，数据网络效应——处理的Token越多，调度算法对模型能力边界、成本曲线、时延特征的建模越精准，形成数据飞轮；第二，MoM多模型融合方案在DRACO基准上接近Claude
    Fable5水平但成本仅1/7，这种性价比在Agent规模化场景下有极强的粘性，客户一旦将调度策略深度嵌入生产流程，切换成本显著；第三，Agent Harness框架（沙箱+工具编排+记忆管理）延长Agent运行时长，从单点网关扩展为端到端平台，提升了横向业务覆盖。然而风险在于：阿里云、腾讯云等巨头可复制类似调度层并以生态捆绑策略反制；模型供应商（如Anthropic、OpenAI）也可能在API层直接提供多模型路由能力，挤压中间件生存空间。综合来看，PPIO在独立AI云服务商中具备先发和规模优势，长期价值取决于其能否在巨头围剿前建立足够的客户依赖和算法深度。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- PPIO
- MiniMax (Mimo)
- Moonshot AI (Kimi)
- Zhipu AI (GLM)
- 中国AI Agent应用开发者
competitive_casualty:
- 传统API网关厂商
- 高价单模型API供应商
- 未针对Agent场景优化的传统IaaS云厂商
market_opportunities:
- 创业者可利用PPIO智能模型网关的MoM（混合模型推理）架构，为金融、法律、医疗等高风险行业开发多模型交叉验证的垂直Agent应用，以更低成本实现接近顶级模型的质量水平
- 基于PPIO沙箱低于200ms冷启动和90%+成本降低的特性，可构建需要大量并行Agent实例的自动化运维、批量代码审查、大规模数据标注等长程任务场景
- AI应用开发者应深入研究PPIO的智能调度与模型路由模式，将其作为优化自身模型调用策略的参考架构——通过任务感知路由实现成本与质量的动态平衡
risk_matrix:
  regulatory: 数据出境监管风险：MoM多模型融合需将请求分发至多个第三方模型（如Kimi、GLM），若涉及跨境数据流动可能触发合规要求；企业级Token服务标准后续若收紧，可能带来额外合规成本
  technological: MoM架构依赖第三方模型API的持续可用性和接口稳定性，模型升级或接口变更可能导致调度策略需频繁适配；若未来出现性能碾压性的单一超级模型，MoM方案的相对优势可能被削弱
  competitive: 阿里云、华为云等巨头正加速布局Agent云服务，PPIO作为独立厂商面临生态挤压风险；硅基流动、Together AI等同赛道友商也在推进模型路由与推理优化，竞争日趋激烈；高端模型若持续降价将缩小PPIO的性价比优势
  ethical: 多模型交叉验证机制需将用户请求分发至多个第三方模型，增加了数据暴露面和隐私泄露风险；Agent沙箱运行环境若被恶意利用，可能产生深度伪造内容或自动化网络攻击
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: PPIO Agentic Cloud
  canonical_name: PPIO Agentic Cloud
  url: https://www.ppio.cloud
  positioning: PPIO面向Agent产业爆发的战略级云服务升级，致力于为Agent自主运行构建原生适配的全栈云服务体系。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI Agent开发团队
  - 需要高性价比模型服务的企业级用户
  - 部署和运营大规模Agent应用的平台团队
  product_signal: 智能模型网关可将智能水平提升20%、成本降低50%-60%，Agent沙箱冷启动时延低于200ms。
  market_signal: 截至2026年6月日均Token调用量超1.2万亿，在中国独立AI云计算服务提供商中排名第一。
  differentiation: 将云的第一客户从人转向Agent，为Agent自主运行原生设计全栈服务体系，区别于传统通用云计算平台。
  watch_reason: PPIO Agentic Cloud代表了云计算从服务人类到服务Agent的战略范式转变，其智能模型网关和Agent沙箱已通过日均万亿级Token调用量验证，是Agent时代基础设施的关键演进方向。
  risk_notes:
  - Agentic Cloud作为新定位面临AWS、阿里云等云计算巨头在Agent领域的激烈竞争。
  - 战略升级从Token工厂到全栈云服务体系跨度较大，执行落地节奏存在不确定性。
  score: 7.0
  article_ids:
  - 7ad3e09bfdfdf3ce
  evidence_snippets:
  - PPIO于WAIC 2026期间正式发布全新Agentic Cloud定位，致力于为Agent打造原生适配的全栈云服务体系。
  - Agentic Cloud建立在PPIO智能Token工厂的万亿级调用量验证之上，是面向Agent产业爆发的战略升级。
- object_type: product
  name: PPIO 智能模型网关
  canonical_name: PPIO 智能模型网关
  url: https://www.ppio.cloud
  positioning: 面向Agent时代的智能Token调度中心，通过混合模型推理（MoM）和智能调度为AI应用动态匹配最合适的专家模型。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI应用和Agent开发者
  - 需要混合模型推理的企业用户
  - 法律合同审查、医疗诊断等高价值场景团队
  product_signal: 在DRACO基准测试中通过融合Mimo-V2.5-Pro、Kimi-K2.7和GLM-5.2实现接近Claude Fable5的性能，成本仅为七分之一。
  market_signal: 入选中国信通院首批企业级Token服务性能攀登基线，TPS≥55个/秒、TTFT≤0.9秒、调用成功率≥99.9%。
  differentiation: 区别于仅做请求转发的API网关，以MoM多模型交叉验证实现智能优先，将模型智商稳定在头部梯队而成本降至中低梯队。
  watch_reason: 智能模型网关是PPIO Agentic Cloud最核心的差异化能力，以MoM工程化方式实现性能接近顶级模型但成本仅七分之一，代表了AI推理成本效率的新范式，值得持续跟踪其企业级落地进展。
  risk_notes:
  - 混合模型推理依赖多模型协同，若任一上游模型API质量波动将影响整体输出一致性。
  - MoM多模型融合可能增加推理延迟，在高实时性交互场景下存在性能瓶颈风险。
  score: 9.0
  article_ids:
  - 7ad3e09bfdfdf3ce
  evidence_snippets:
  - PPIO最新发布的智能模型网关通过给AI应用提供智能调度中心，让每次模型调用都变成一场专家会诊。
  - 智能模型网关可将智能水平提升20%，将成本降低50%-60%，兼具混合模型推理和智能调度两大功能。
- object_type: product
  name: PPIO Agent 沙箱
  canonical_name: PPIO Agent 沙箱
  url: https://www.ppio.cloud
  positioning: 为Agent提供安全隔离运行环境的沙箱产品，以极低冷启动时延和大规模并发创建能力支撑Agent规模化部署。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要大规模部署Agent的企业
  - 对安全隔离有严格要求的AI开发团队
  product_signal: 冷启动时延低于200ms，采用系统级安全隔离，支持上万个沙箱同时创建，综合使用成本较同类产品降低90%以上。
  market_signal: 上线一年业务规模增长超120倍，证明Agent沙箱市场需求强劲且产品化能力得到验证。
  differentiation: 采用系统级安全隔离和空闲自动暂停计费机制，综合使用成本较同类产品降低90%以上，冷启动时延低于200ms。
  watch_reason: PPIO Agent沙箱以极低冷启动时延和成本优势实现一年增长超120倍，已成为PPIO Agentic Cloud生态的核心组件，其规模化后的稳定性值得持续观察。
  risk_notes:
  - AWS、Google等云计算巨头也在积极布局Agent沙箱能力，市场竞争日趋激烈。
  - 沙箱业务规模高速增长对基础设施容量和运维能力构成持续挑战。
  score: 6.0
  article_ids:
  - 7ad3e09bfdfdf3ce
  evidence_snippets:
  - PPIO Agent沙箱冷启动时延低于200ms，采用系统级安全隔离，支持上万个沙箱同时创建。
  - PPIO Agent沙箱综合使用成本较同类产品降低90%以上，上线一年业务规模增长超120倍。
- object_type: product
  name: PPClaw/PPHermes
  canonical_name: PPClaw/PPHermes
  url: null
  positioning: PPIO基于Harness框架推出的托管Agent产品，具备7x24小时长时间运行和自我修复能力。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要7x24小时持续运行Agent的企业用户
  - 对Agent可靠性和自我修复能力有高要求的运维团队
  product_signal: 可以实现7x24小时长时间运行且具备自我修复能力，基于Harness框架集成了上下文构建、工具编排和验证循环等能力。
  market_signal: null
  differentiation: 依托PPIO Harness框架提供从沙箱到任务编排的完整Agent托管能力，集成自我修复机制实现无人值守运行。
  watch_reason: PPClaw和PPHermes作为PPIO Agentic Cloud战略的托管Agent落地案例，展示了Harness框架从沙箱到长程任务执行的完整能力闭环，但当前公开信息有限，需观察后续产品化进展。
  risk_notes:
  - 产品公开信息有限，目前仅作为Harness框架的能力展示案例，缺乏独立规模化验证数据。
  - 托管Agent市场竞争激烈，需与主流Agent平台和开源方案竞争开发者生态。
  score: 4.0
  article_ids:
  - 7ad3e09bfdfdf3ce
  evidence_snippets:
  - PPIO通过Harness手段推出的PPClaw和PPHermes等托管Agent，可以实现7x24小时长时间运行且具备自我修复能力。
---

# PPIO发布智能模型网关，打造面向Agent时代的智能Token工厂

万亿Token调用量验证

7 月 17 日，2026 世界人工智能大会（WAIC）在上海举行。PPIO 同期举办了媒体沟通会，会上正式发布全新的 Agentic Cloud 定位，以及智能模型网关新品，致力于打造面向 Agent 时代的智能 Token 工厂。

PPIO 联合创始人兼 CEO 姚欣提出了一个 Agent 时代的核心公式——**Agent 生产力 = Token 智能密度 × Agent Loop 时长**。Token 智能密度决定了 Agent 每一步决策的质量上限，Agent Loop 时长决定了 Agent 能持续运行多久、完成多复杂的任务。

围绕这一公式，PPIO Agentic Cloud 构建了两层原生产品体系：智能模型网关是 AI Agent 的智能调度中心——关键决策由混合模型把关提升质量，简单任务由模型调度自动分流到轻量模型，确保 Agent 用最低的 Token 成本、最高的智能性能把任务完成，持续推高 Token 智能密度。

Agent Harness 层融合沙箱、任务编排、Tool Use、记忆管理等于一体，延长 Agent 可持续运行的 Loop 时长以解决复杂长程任务。今年 PPIO 通过 Harness 手段推出的 PPClaw/PPHermes 等托管 Agent ，可以实现 7x24h 长时间运行，且具备自我修复能力。

“Agent 时代最重要的变化，就是云的第一客户从人变成了 Agent。”姚欣表示，“过去的云计算是为人使用软件而设计，而 Agentic Cloud 是为 Agent 自主运行而生。我们希望为 Agent 打造一套原生适配的全栈云服务体系，更高效、更稳定、更低成本地支持 Agent 的构建、部署与运行，彻底释放 Agent 的产业价值。”

自 2024 年推出模型服务以来，PPIO “Token工厂”业务规模飞速增长。截至 2026 年 6 月日均 Token 调用量超 1.2 万亿，较 2025 年同期增长超 8 倍。根据灼识咨询统计，按 2025 年及 2026 年第一季度平均每日 Token 消耗量计，PPIO 在中国独立 AI 云计算服务提供商中排名第一。

全新 Agentic Cloud 建立在 PPIO 智能 Token 工厂的万亿级调用量验证之上，是面向 Agent 产业爆发的战略升级。2025 年 PPIO 推出了 Harness 核心组件之一的沙箱，今年进一步向 Harness 平台层拓展，从单点能力升级为覆盖 Agent 全链路的云服务体系，为 Agent 长期规模化应用筑牢底座。

**智能模型网关：面向 Agent 时代的智能 Token 调度**

当前许多 AI 应用开发者存在一个真实痛点，比较依赖一个“全能型”大模型。然而，单模型可能在推理时不够深刻，在检索时记忆力不足，在生成时文采平平。

如何为 AI Agent 的每一个工作步骤，都动态匹配最合适的“专家模型”，同时还要控制成本、保证稳定？

**PPIO 最新发布的智能模型网关，就是要解决这一问题。通过给 AI 应用提供一个智能调度中心，智能模型网关让每次模型调用都变成一场“专家会诊”。**

与市面上常见的、仅做简单“请求转发”的 API 网关不同，PPIO 以智能优先，兼顾性价比。

**智能模型网关的第一个功能，是混合模型（MoM，Mixture of Models）。**在处理高价值、高风险或结果不确定的关键 Agent 步骤时，比如法律合同审查、医疗初步诊断，网关会触发“多模型融合”机制。它不是只问一个模型，而是将问题同时分发给多个擅长此道的专家模型，通过交叉验证和融合生成最终答案。这种方式极大地提升了任务完成的成功率，避免了因模型“偏科”导致的任务失败和返工。

**智能模型网关的第二个功能，是模型调度。**它会根据任务类型进行智能路由，比如简单问答用轻量模型，复杂推理用强模型，并压缩冗余上下文、复用之前的计算结果，设置预算护栏和失败回退机制。最终目标是：用最经济的成本，完成同样质量的任务。

智能模型网关不是卖最贵的“超级模型”，也不是卖最便宜的“乞丐模型”，而是用工程化手段（MoM融合），把模型的智商稳定在头部梯队，同时把价格打到了中低梯队。在 DRACO 深度研究基准测试中，PPIO 通过融合 Mimo-V2.5-Pro、Kimi-K2.7 和 GLM-5.2 进行混合模型推理，可以将性能提升至接近 Claude Fable5 的水平，而成本却仅是 Claude Fable5 的七分之一。**据综合测算，PPIO 智能模型网关可以将智能水平提升 20%，将成本降低 50%-60%。**

这一能力背后，是对 Agent 时代模型调用逻辑的重新思考。不同于人类用户偶尔提问的使用模式，智能体应用的兴起正在推动 Token 消耗呈指数级增长。Agent 的运行天然具备高频工具调用、长上下文持续交互、多模型协同等特征，对延迟、稳定性和成本敏感度远高于传统场景。未来 AI 任务的执行主体从人转向 Agent，模型的核心服务对象也必须随之重构。

PPIO 智能模型网关正是这场重构中的关键一环。它以智能调度与混合模型推理为中枢，叠加自研推理引擎与全球算力调度能力，将每一次模型调用转化为可度量、可优化、可回溯的智能 Token。这种面向任务结果优化的调度逻辑，让大模型从“用得起”走向“用得聪明”，为 Agent 时代构建起一个真正高性价比的智能 Token 工厂。

这一技术实力也已获得权威认可。今年，PPIO 入选中国信通院首批“企业级 Token 服务性能攀登基线”，在通用场景下跑出了 TPS≥55个/秒、TTFT≤0.9秒、调用成功率 ≥99.9% 的硬指标，标志着平台已具备面向企业级 AI 应用和 Agent 场景的大规模高质量服务能力。

**Agent Harness：从沙箱到长程任务执行**

Agent 不能只“想”，还要能“做”，Harness 是专门用于约束、指导、验证和纠错 Agent 执行的工程框架。Harness 框架涵盖了除大模型本身之外的所有环节：上下文构建、工具编排、验证循环、成本控制和可观测性。

Harness 工程可延长 Agent 可持续运行的 Loop 时长，从而让 Agent 真正具备“执行、反馈、迭代”的生产级能力。

沙箱是 Harness 的核心组件之一。去年，PPIO 推出了国内首款兼容 E2B 接口的 Agent 沙箱，为 Agent Harness 提供安全隔离的运行环境。

PPIO Agent 沙箱冷启动时延低于 200 ms，采用系统级安全隔离，让每个 Agent 任务运行在独立虚拟机环境；支持上万个沙箱同时创建，同时任务空闲时可自动暂停计费，**综合使用成本较同类产品降低 90% 以上**。PPIO Agent 沙箱上线一年，业务规模已**增长超 120 倍**。