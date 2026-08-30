---
title: 'A look under our trunk: what''s in our compute'
source: https://waymo.com/blog/2026/08/look-under-our-trunk/
author:
- '[[ra7]]'
published: '2026-08-20'
created: '2026-08-22'
manifest_dates:
- '2026-08-20'
- '2026-08-22'
description: 'Article URL: https://waymo.com/blog/2026/08/look-under-our-trunk/ Comments
  URL: https://news.ycombinator.com/item?id=49374853 Points: 122 # Comments: 68'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0f9bc8fb2cad5d50
source_type: community_discussion
tldr: Waymo 首次公开其自动驾驶计算系统设计，推出自研 5nm ASIC，宣称单芯片提供超 1000 TOPS ML 性能，八年间算力增长 20 倍，并与
  AMD、NVIDIA、TSMC 等合作构建车载计算平台。
objective_summary: Waymo 于 2026 年 8 月发布博客文章，首次公开自动驾驶系统 Waymo Driver 的计算架构。该系统基于响应性、加固性、冗余性三大非妥协要求设计，采用
  ML 优先的异构架构，并推出自研 5nm ASIC 用于实时处理激光雷达、雷达与摄像头原始数据，单芯片 ML 性能超 1000 TOPS。Waymo 称八年间原始算力提升
  20 倍，并与 AMD、NVIDIA、TSMC 等多家厂商合作，相关方案将在 Hot Chips 大会展示。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - Waymo
  - AMD
  - Micron
  - NVIDIA
  - Samsung
  - Sandisk
  - Socionext
  - TSMC
  technologies:
  - ASIC
  - 5nm
  - ML
  - sensor fusion
  - neural networks
  - sparse convolutions
  - dense transformers
  key_people: []
key_logic_flow:
- Waymo 首次对外公开其自动驾驶计算系统的内部设计，阐述了从商业现成组件转向自研定制系统的演进路径。
- Waymo 的算力系统围绕响应性、加固性、冗余性三大非妥协要求构建，其中冗余设计使两套独立引擎在单侧故障时可无缝接管。
- Waymo 在八年内将原始算力规模提升 20 倍，并采用 ML 优先架构，将 ML 技术与 CPU、GPU 及专用加速器结合成均衡的异构系统。
- Waymo 推出自研 5nm ASIC，专用于实时处理、融合并运行原始传感器数据上的高级神经网络，单芯片提供超过 1000 TOPS 的 ML 性能。
- Waymo 与 AMD、Micron、NVIDIA、Samsung、Sandisk、Socionext、TSMC 等伙伴合作，并将在 Hot Chips 大会分享其计算方案。
object_mentions:
- object_type: product
  name: Waymo Driver
  canonical_name: Waymo Driver
  url: https://waymo.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Waymo 首次公开自动驾驶系统 Waymo Driver 的计算方案，该系统基于超过 2 亿英里全自动驾驶经验设计，负责将原始传感器数据转化为实时驾驶指令。
  article_id: 0f9bc8fb2cad5d50
- object_type: project
  name: Waymo 5nm ASIC
  canonical_name: Waymo 5nm ASIC
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Waymo 推出自研 5nm ASIC，专门用于实时处理、融合并运行原始传感器数据上的高级神经网络，单颗芯片提供超过 1000 TOPS 的 ML 性能。
  article_id: 0f9bc8fb2cad5d50
extract_result: success
impact_score:
  score: 6.5
  reason: Waymo 作为商业化最领先的 Robotaxi 运营商，首次公开车载计算架构并披露自研 5nm ASIC（单芯片宣称 1000+ TOPS），对自动驾驶车载计算领域有明确竞争信号——Waymo
    正式加入特斯拉式的算力垂直整合阵营，且合作伙伴覆盖 AMD/NVIDIA/TSMC 等头部厂商，可能动摇 NVIDIA 等商用平台在 AV 计算环节的既有地位。但该披露本质是
    Hot Chips 大会前的 PR 预热，缺少微架构、能效比、功耗、延迟等实测细节，属于渐进式基础设施更新而非范式转移，因此评分落在重要发布区间中段。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 1000 TOPS 峰值指标缺乏能效与实测数据支撑，工程界关注真实算力成色与软硬件协同设计的落地细节
hype_assessment:
  level: medium
  reason: 文章使用了『地表最强车载计算系统』『堪比数据中心』等 PR 修辞，并抛出 1000+ TOPS 峰值算力这一惯用的营销口径（文章自己也承认要『最大化
    achieved performance』，暗示峰值与实测存在差距）。但底层工程真实存在：Waymo 拥有 200 万英里全自动驾驶里程和商业运营车队，且
    Hot Chips 演讲将提供可验证的架构细节，并非纯概念炒作，故判定为存在一定包装。
information_entropy: medium
domain_disruption:
  technical_innovation: 面向原始激光雷达/雷达/摄像头数据流的 5nm 定制 ASIC，将时间维去噪、传感器融合与推理引擎集成于单芯片，同时支持稀疏卷积与稠密
    Transformer 两类异构模型；配合 ML 优先的异构计算架构，实现从像素到驾驶动作的毫秒级端到端链路，代表了从『买商用芯片堆算力』到『芯片-传感器-算法三方协同设计』的全栈优化范式。
  business_model: 算力垂直整合将降低 Waymo 单车硬件成本与每英里算力开销，减少对 NVIDIA 等商用计算平台的依赖，形成规模化的成本护城河；作为唯一规模化商业运营的
    Robotaxi 车队验证了自研芯片路径的可行性，可能促使整个 AV 行业从采购商用计算转向定制硅片，重塑车载计算供应链的议价格局。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: Waymo 将传感器、自研 ASIC 与算法三层协同设计的飞轮一旦转起来，会随 robotaxi 运营规模（2 亿英里自动驾驶里程）产生强复利效应：数据积累驱动算法迭代，算法约束驱动下一轮芯片定制，定制硬件又压低单位里程算力成本、提升安全冗余，进而加速商业化扩张。这是典型的'运营规模→技术壁垒→单位经济改善'正向循环，3-5
    年后 Waymo 大概率仍是自动驾驶领域的计算与运营双料龙头。但扣分原因有二：其一，该 ASIC 是垂直整合的私有能力而非可外溢的行业基础设施，不会像 GPU
    或 MCP 那样服务全行业，价值捕获高度绑定 Waymo 单车队扩张节奏；其二，Robotaxi 大规模商业化仍受监管与事故责任等非技术变量制约，硬件复利兑现存在时间不确定性。综合判断为细分赛道核心资产的强复利，但尚未达到通用行业基石的量级。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- Waymo
- TSMC
- AMD
- NVIDIA
- Socionext
- Micron
competitive_casualty:
- Mobileye
- Cruise
- 通用型车载计算平台厂商
- 缺乏自研芯片能力的 Robotaxi 竞争者
market_opportunities:
- 自动驾驶与机器人公司可评估借鉴 Waymo 的'自研 ASIC + 台积电/Socionext 协同'模式，针对自身场景开发高能效边缘推理芯片
- 车规级液冷散热、抗振加固与宽温域运行等高性能车载计算组件供应商可瞄准 L4 级 Robotaxi 车队扩张带来的确定性配套需求
- 关注 Hot Chips 技术细节后，AI 芯片从业者可探索传感器前处理（时域降噪、稀疏卷积加速）等专用加速器在车载与泛边缘场景的产品化机会
risk_matrix:
  regulatory: Waymo 的算力与安全声明需通过美国 NHTSA 及各州自动驾驶法规的实际安全认证检验；与台积电等先进制程合作在出口管制趋严背景下存在供应链合规审查风险
  technological: 博客宣称的 1000 TOPS 为峰值算力，实际可达性能（尤其低 batch 场景）未经独立第三方验证；NVIDIA Thor（2000
    TOPS）与 Tesla 自研芯片等替代架构迭代迅速，自研 ASIC 的架构领先性可能被通用平台快速追赶甚至超越
  competitive: Waymo 与 NVIDIA 既是合作伙伴又是潜在竞争者（NVIDIA Drive 平台同时供给其他车企），合作关系存在微妙张力；特斯拉、Zoox、Mobileye
    等均走自研/定制芯片路线，生态竞争激烈；自研芯片重资产投入使后来者难以复制
  ethical: 自动驾驶'安全'与'最强大'等营销表述需第三方实证支撑公众信任；车载传感器持续采集道路周边行人/车辆数据，存在隐私保护与数据伦理争议；Robotaxi
    规模化对出行司机岗位的长期就业冲击不容忽视
  additional:
  - 供应链集中风险：5nm 制程高度依赖台积电，地缘政治或产能波动可能冲击芯片供应
  - 人才竞争加剧：该博客兼有招聘目的，Waymo 加大算力与芯片人才招募力度，推高行业人才争夺成本
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Waymo Driver
  canonical_name: Waymo Driver
  url: https://waymo.com
  positioning: Waymo 的全自动驾驶系统，基于超过 2 亿英里全自动驾驶经验设计，负责将原始传感器数据转化为实时驾驶指令，在无人类备份下完成整个驾驶任务。
  technical_signal: Waymo Driver 的计算架构围绕响应性、加固性、冗余性三大要求设计，采用 ML 优先的异构方案，八年间原始算力提升
    20 倍。
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Waymo 无人驾驶出行服务的乘客
  - Waymo 车队运营与维护团队
  product_signal: 系统将 ML 技术配合 CPU、GPU 与专用加速器构成均衡的异构架构，并集成车辆液冷系统以在极端温度下维持峰值性能。
  market_signal: Waymo 首次公开其车载计算系统设计，与 AMD、NVIDIA、TSMC 等伙伴合作构建计算平台，并将在 Hot Chips 大会分享方案。
  differentiation: 区别于传统驾驶辅助计算，Waymo Driver 在无人类备份下独立承担完整驾驶任务，冗余设计如两套独立引擎可在单侧故障时无缝接管。
  watch_reason: Waymo 首次对外公开计算系统设计，标志着其从商用现成组件转向自研定制系统的关键演进；算力八年提升 20 倍与 ML 优先架构为自动驾驶边缘计算设定新标杆，其后续定制组件与商业部署进展值得持续跟踪。
  risk_notes:
  - 首次披露的信息仍为概览性质，具体架构与性能数据有待 Hot Chips 大会及独立验证。
  - 自研芯片与先进制程依赖长期高投入，若商业化规模不及预期，定制路线的经济性存在不确定性。
  score: 8.0
  article_ids:
  - 0f9bc8fb2cad5d50
  evidence_snippets:
  - Waymo 首次公开自动驾驶系统 Waymo Driver 的计算方案，该系统基于超过 2 亿英里全自动驾驶经验设计，负责将原始传感器数据转化为实时驾驶指令。
- object_type: project
  name: Waymo 5nm ASIC
  canonical_name: Waymo 5nm ASIC
  url: null
  positioning: Waymo 自研的 5nm 专用 ML 芯片，专用于实时处理、融合并运行原始传感器数据上的高级神经网络，单芯片提供超过 1000 TOPS
    性能。
  technical_signal: 芯片内置专用加速器可即时提取激光雷达、雷达与摄像头原始数据的关键信息，包括低光感知时域降噪，并覆盖从稀疏卷积到稠密 Transformer
    的异构模型。
  adoption_signal: 该 ASIC 作为 Waymo Driver 计算系统的前端数据处理定制组件投入车载部署，并与 AMD、NVIDIA 等伙伴的计算方案协同工作。
  ecosystem_relevance: Waymo 与 AMD、Micron、NVIDIA、Samsung、Sandisk、Socionext、TSMC 等多家伙伴协作，定制芯片与行业领先方案共同构成车载计算生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Waymo 首次披露自研 5nm ASIC 是其从商用组件转向定制硅片的标志性进展，超 1000 TOPS 的性能定位与 ML 优先设计将影响自动驾驶边缘芯片竞争格局，其
    Hot Chips 公开细节与后续定制组件值得持续跟踪。
  risk_notes:
  - Waymo 尚未公布 ASIC 的能效、制程良率与量产时间表，性能宣称仍需第三方实测验证。
  - 自研芯片高度依赖台积电等先进制程产能，供应链波动可能影响量产节奏。
  score: 8.0
  article_ids:
  - 0f9bc8fb2cad5d50
  evidence_snippets:
  - Waymo 推出自研 5nm ASIC，专门用于实时处理、融合并运行原始传感器数据上的高级神经网络，单颗芯片提供超过 1000 TOPS 的 ML 性能。
---

Compute is the brain of the Waymo Driver, translating raw sensor data into real-time driving commands. Operating demonstrably safe, physical AI on the road demands a fundamental shift towards a system engineered for deterministic, low-latency performance. Over the past decade, we have co-designed our hardware, sensors, and algorithms side-by-side to solve the unique constraints of real-world edge compute. We’re offering the first look under our trunk to share our approach to compute, our custom silicon, and how we collaborate with industry leaders to build the most capable computing system on the road.

Compute systems for autonomous driving handle highly diverse workloads. At Waymo, we are designing a state-of-the-art system that would be considered impressive for a data center, with the added complexity of an in-vehicle operating domain and real-time requirements. Unlike traditional driver-assist computing, our system handles the entire task of driving without a human backup, demanding significantly higher performance. Drawing from more than 200 million miles of fully autonomous experience, we engineer our compute around three non-negotiable requirements:

**Responsive:**To make real-time driving decisions, the autonomous system operates entirely onboard, constantly processing decisions within milliseconds. We have engineered our stack for ultra-low latency, minimizing the delay from first pixel to action. Within those critical milliseconds, advanced ML models build a high-fidelity understanding of the environment to evaluate the safest path forward. Unlocking this requires impressive raw compute power—which we’ve scaled 20x in just eight years—paired with a deeply optimized software stack to harness it efficiently.**Ruggedized:**We have engineered our compute to thrive in the physical world with remarkable endurance and reliability from the component to the system level. Our hardware operates under constant vibration, shock, and extreme temperatures. By integrating directly with the vehicle's liquid cooling system, we sustain peak performance whether navigating freezing Midwest winters or the blistering heat of Phoenix.**Redundant:**Because there is no human to take over, proactive safety and redundancy are natively built in. Our compute is designed like two independent engines. While they normally operate as one unit running full parallel workloads, if one experiences a fault, the other seamlessly takes over.

Evolving from off-the-shelf components to custom systems required rethinking our physical and architectural design. Our highly integrated system delivers immense processing power without compromising the rider experience, maximizing battery efficiency while preserving ample trunk space and running silently. We built an ML-primary architecture to run advanced neural networks at minimal latency. To manage critical non-ML tasks like orchestration, data movement, and logging while maximizing time for ML computation, we pair our ML technologies with the best CPUs, GPUs, and accelerators. The result is a balanced, heterogeneous system.

To handle the massive influx of raw data before it reaches our core ML brain, we are excited to introduce our purpose-built 5nm ASIC. While this chip is just one of several exciting custom components we’re developing, it is a specialized ML powerhouse engineered exclusively to process, fuse, and run advanced neural networks on raw sensor data in real time. Developing silicon, sensors, and algorithms side-by-side allows us to push the boundaries of sensor fidelity, bandwidth efficiency, and quantization to execute a heterogeneity of models from sparse convolutions to dense transformers.

The ASIC’s specialized accelerators instantly extract critical information from raw lidar, radar, and camera streams, including temporal denoising for superior low-light perception. This data feeds into our purpose-built inference engine to run sensor fusion ML models, enabling greater efficiency without sacrificing fidelity. While these ASICs alone deliver over 1,000 TOPS of ML performance dedicated to front-end processing and ML models, we optimize across the full stack to maximize achieved performance, especially in the low-batch regimes we often operate.

Along with our custom silicon efforts, we partner closely with industry leaders whose world-class computing solutions provide the powerful foundation needed to scale our technology efficiently. We are proud to work alongside a number of partners like AMD, Micron, NVIDIA, Samsung, Sandisk, Socionext, and TSMC to deliver the most capable autonomous computing system.

This is just a glimpse of what's to come. As we explore new use cases for the Waymo Driver and our AI stack continues to evolve, the demand for highly efficient, high-performance compute will only grow.

If you're interested in learning more about Waymo's approach to compute, join us at our talks at Hot Chips.

You can also connect with our team and help push the boundaries of what's possible by applying for a role at waymo.com/careers.