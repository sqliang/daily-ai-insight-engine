---
title: 45°C cooling design cuts data center water use to near zero
source: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
author:
- '[[nitin_flanker]]'
published: '2026-06-24'
created: '2026-06-25'
description: 'Article URL: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
  Comments URL: https://news.ycombinator.com/item?id=48660178 Points: 328 # Comments:
  219'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: da0ee3bbeda7b90d
source_type: community_discussion
tldr: NVIDIA 发布 Rubin 代 AI 基础设施，实现 100% 全液冷无风扇设计，冷却液温度可达 45°C，通过干冷器闭环系统将数据中心水耗降至接近零，并显著降低冷却能耗。
objective_summary: NVIDIA 在官方博客中介绍了其 Rubin 代 AI 基础设施，采用全球首个 100% 全液冷设计，以 45°C 冷却液温度和干冷器实现闭环循环，几乎完全消除蒸发水耗。据
  NVIDIA 估算，一个 50 兆瓦的超大规模数据中心每年可节省超过 400 万美元的冷却相关能源和水成本。该设计基于 NVIDIA DSX AI 工厂参考架构，在大部分气候条件下无需开启机械冷冻机。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - Schneider Electric
  technologies:
  - Liquid Cooling
  - DSX
  - Rubin
  key_people:
  - Ali Heydari
  - Richard Whitmore
key_logic_flow:
- NVIDIA Rubin 代 AI 基础设施是全球首个实现 100% 全液冷设计的平台，所有芯片和网络组件均由闭环液体冷却，且系统内不设任何风扇。
- 冷却液温度可达 45°C，配合干冷器可在大部分气候条件下实现无冷冻机运行，将设施冷却水耗从传统冷却塔系统的每兆瓦每年约 260 万加仑降至接近零。
- 传统数据中心冷却能耗占整体用电量高达 40%，而液冷架构通过提高冷却液温度显著降低能耗，一个 50 兆瓦设施每年可节省超过 400 万美元的冷却相关成本。
- 冷却液采用 75% 水与 25% 丙二醇的混合液，通过直接贴合处理器的冷板捕获热量，再经封闭循环回路输送至室外干冷器散热。
- 全液冷设计使 Rubin 服务器前面板完全封闭无穿孔，机架密度大幅提升，原本需要 6 个机架单元的系统如今仅需 2 个。
- 液冷架构还支持废热回收，可将 AI 工厂的余热重新利用于附近商业或住宅建筑的供暖。
extract_result: success
object_mentions:
- object_type: product
  name: NVIDIA Rubin
  canonical_name: NVIDIA Rubin AI Infrastructure
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA Rubin 代 AI 基础设施是全球首个实现 100% 全液冷设计的计算平台，所有芯片和网络组件均采用闭环液体冷却且不设任何风扇。
  - Rubin 架构的冷却液温度可达 45°C，使服务器前面板实现完全封闭无穿孔设计，机架密度相比传统风冷服务器大幅提升。
  article_id: da0ee3bbeda7b90d
- object_type: project
  name: NVIDIA DSX AI Factory Reference Design
  canonical_name: NVIDIA DSX AI Factory Reference Design
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA DSX AI 工厂参考设计概述了设计、建造和运营整个 AI 工厂基础设施栈的最佳实践。
  - 该参考设计实现了接近零的水消耗，通过基于干冷器的闭环系统消除了蒸发水冷，全年约 99% 的时间无需开启冷冻机。
  article_id: da0ee3bbeda7b90d
- object_type: company
  name: Motivair
  canonical_name: Motivair
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Motivair 是 Schneider Electric 旗下的先进冷却部门，与 NVIDIA 的产品路线图已保持近十年的紧密合作。
  - Motivair 总裁 Richard Whitmore 指出，当每芯片功耗突破风冷可行阈值后，液冷成为数据中心基础设施的必选方案。
  article_id: da0ee3bbeda7b90d
impact_score:
  score: 6.5
  reason: 评分依据：这是一项重要的数据中心基础设施升级，45°C液冷闭环设计使多数气候条件下无需制冷机组，水耗降至接近零，50MW设施年省超400万美元冷却成本。其行业影响力在于：1）首次实现100%全液冷无风扇设计，芯片功率密度突破空气冷却阈值后液冷已成必然，NVIDIA此举加速了整个产业链的液冷转型；2）冷却液温度提升至45°C是量变到质变的临界点，直接解锁干冷器方案，这是工程实现上的重要突破；3）对AI模型训练/推理成本的影响是间接的——降低数据中心OPEX可能最终传导至算力定价，但不会像模型架构创新那样直接改变AI能力边界。综合来看属于重要的基础设施演进，但并非范式转移级别的变革。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 液冷基础设施对AI推理/训练成本和GPU服务可用性的间接影响
hype_assessment:
  level: medium
  reason: 判定依据：文章来自NVIDIA官方博客，属于企业PR陈述。存在一定包装痕迹——'世界首个100%全液冷''revolutionary'等表述带有营销色彩；虽然提供了具体技术参数（45°C冷却液温度、75/25丙二醇/水混合比）和量化收益数据（年省超400万美元、水耗降100%），但这些数字来自NVIDIA自身测算，缺乏独立第三方验证；文中提及'most
    climates'可实现无制冷机组运行，但未详细说明地理气候限制条件及那'1%需要制冷机组的年份'的具体分布。综合来看，技术方向真实且有价值，但声称的收益幅度和覆盖范围需独立验证。
information_entropy: medium
domain_disruption:
  technical_innovation: 45°C冷却液闭环设计使数据中心在多数气候条件下无需制冷机组，干冷器方案将年水耗从约260万加仑/兆瓦降至接近零，同时完全取消风扇。核心突破在于冷却液温度提升至45°C后仍能保证芯片在验证工作温度范围内满性能运行，入口45°C/出口约55°C的温升表明冷板吸热效率高，这打破了'数据中心必须像冷库一样'的传统行业认知，属于热管理工程学的实质性进步。
  business_model: 降低超大规模数据中心冷却OPEX约40%，50MW设施年省超400万美元，将加速液冷供应链生态成熟（Motivair/Schneider
    Electric已深度参与）。但从商业战略角度看，这也是NVIDIA对其AI硬件平台的一项差异化护城河设计——DSX参考架构促使云服务商采用NVIDIA全栈方案部署Rubin平台，增强了生态锁定效应；同时冷却成本降低可能间接影响AI云服务定价竞争格局。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: NVIDIA 通过 Rubin 平台实现了 100% 全液冷闭环，冷却液温度提升至 45°C，使数据中心水耗接近零、冷却能耗大幅下降。从 VC
    视角看，这不仅是工程优化，更是 NVIDIA 强化平台锁定和生态壁垒的关键动作：(1) DSX 参考设计成为行业标准后，云厂商和 IDC 运营商的冷却基础设施投资将深度绑定
    NVIDIA 路线图，形成物理层面的转换成本；(2) 水耗归零和 45°C 运行温度使 AI 工厂可在水资源匮乏地区部署，打开了新的地理市场空间；(3) 冷却能耗占传统数据中心高达
    40%，每提升 1°C 降低约 4% 能耗，50MW 设施年省超 400 万美元——这些节省在 AI 算力指数级扩张的背景下会持续累积复利。但与软件层网络效应不同，液冷技术本质上属于物理工程范畴，竞争对手（AMD/Intel
    及其生态伙伴）有追赶空间，因此长期复利效应虽有但非绝对护城河。评分 7.5：属于细分赛道的强基础设施级创新，复利效应显著但非不可逾越。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- NVIDIA
- Motivair (Schneider Electric)
- AWS
- Microsoft Azure
- Google Cloud
- Equinix
competitive_casualty:
- AMD
- Intel
- 传统空气冷却基础设施厂商 (Vertiv, STULZ)
- 冷却塔供应商 (Baltimore Aircoil, Evapco)
- 水冷空调系统集成商
market_opportunities:
- 数据中心液冷改造服务市场将迎来爆发式增长，现有风冷数据中心需要大规模改造为液冷架构，提供评估、设计、施工一站式服务的集成商将获得先发优势
- 液冷供应链上游（冷板、CDU、干冷器、冷却液泵、监控系统）存在明确的国产替代和垂直整合机会，尤其适配NVIDIA DSX参考架构的标准化组件供应商将受益于生态锁定效应
- 数据中心选址咨询服务将因45°C液冷方案降低对气候和地理位置的依赖而打开新市场，可帮助企业在传统不适宜建数据中心的区域（如温暖气候、缺水地区）进行选址和可行性研究
risk_matrix:
  regulatory: 丙二醇冷却液（75%水+25%丙二醇）在部分司法管辖区可能面临存储、泄漏报告和废弃处置方面的环保法规约束；数据中心的PUE和WUE能效标准正在趋严（如EU能效指令修订），现有合规框架对液冷新范式的适配存在滞后风险
  technological: NVIDIA的45°C液冷方案是深度耦合其芯片架构的专有设计，长期可能造成供应商锁定；随着AI芯片功耗密度持续攀升（超过当前液冷阈值），未来可能需要向浸没式或两相液冷演进，当前投资存在路径依赖和技术代际更替风险
  competitive: NVIDIA通过DSX参考架构从芯片层向上游基础设施设计延伸，与Schneider Electric/Motivair形成生态联盟，可能挤压传统数据中心基础设施供应商（如Vertiv、CoolIT）的市场空间和议价能力
  ethical: 液冷大幅降低数据中心水耗是显著的环保效益，但更高效的冷却降低了AI算力扩张的环境门槛，可能加速能源消耗和电子废弃物问题的恶化；算力集中化趋势（超大设施、少数供应商）存在AI资源分配不平等的社会风险
  additional:
  - 电网负荷集中化风险：冷却效率提升使同等电力可驱动更多计算芯片，单个设施的功率密度和峰值用电可能急剧上升，对区域电网的稳定性和冗余设计构成新挑战
  - 供应链单点故障风险：Motivair作为核心冷却合作伙伴承担关键技术角色，其产能瓶颈、地域政治风险或技术质量事故可能影响整个NVIDIA Rubin生态的交付节奏
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: NVIDIA Rubin
  canonical_name: NVIDIA Rubin AI Infrastructure
  url: null
  positioning: NVIDIA 面向 Rubin 代 AI 基础设施打造的全球首个 100% 全液冷计算平台，所有芯片和网络组件均采用闭环液体冷却且不设任何风扇。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 云服务提供商
  - 超大规模数据中心运营商
  - AI 工厂建设方
  product_signal: 冷却液温度可达 45°C，配合干冷器可在大部分气候条件下实现无冷冻机运行，将数据中心水耗从每年每兆瓦约 260 万加仑降至接近零。
  market_signal: 一个 50 兆瓦超大规模数据中心每年可节省超过 400 万美元的冷却相关能源和水成本，传统冷却能耗占数据中心总用电量高达 40%。
  differentiation: 全球首个实现 100% 全液冷且无风扇的 AI 基础设施，服务器前面板完全封闭无穿孔，机架密度相比传统风冷服务器提升三倍，原本六个机架单元的系统如今仅需两个。
  watch_reason: NVIDIA Rubin 通过 45°C 全液冷架构实现几乎零水耗和显著节能，正推动整个数据中心行业从风冷向液冷加速转型，其大规模部署过程中与冷却生态伙伴的协同效应值得持续跟踪。
  risk_notes:
  - 45°C 液冷方案在炎热气候条件下每年仍有约 1% 的时间需要依赖机械冷冻机辅助散热，无法完全脱离传统制冷设备。
  - 全液冷改造需要数据中心运营商进行大规模基础设施投资，现有风冷数据中心无法低成本迁移至该架构。
  score: 9.0
  article_ids:
  - da0ee3bbeda7b90d
  evidence_snippets:
  - NVIDIA Rubin 代 AI 基础设施是全球首个实现 100% 全液冷设计的计算平台，所有芯片和网络组件均采用闭环液体冷却且不设任何风扇。
  - Rubin 架构的冷却液温度可达 45°C，使服务器前面板实现完全封闭无穿孔设计，机架密度相比传统风冷服务器大幅提升。
- object_type: project
  name: NVIDIA DSX AI Factory Reference Design
  canonical_name: NVIDIA DSX AI Factory Reference Design
  url: null
  positioning: NVIDIA 推出的 AI 工厂参考设计，涵盖设计、建造和运营 AI 工厂基础设施栈的最佳实践，实现基于干冷器闭环系统的接近零水耗全液冷架构。
  technical_signal: 采用干冷器闭环系统消除蒸发水冷，全年约 99% 的时间无需开启冷冻机，冷却液为 75% 水与 25% 丙二醇的混合液，通过直接贴合处理器的冷板捕获热量。
  adoption_signal: 作为 Rubin 平台的配套参考设计，推动云服务商和数据中心运营商加速向全液冷基础设施方案转型。
  ecosystem_relevance: 与 Motivair（Schneider Electric 先进冷却部门）等领先冷却生态伙伴有近十年的协同开发历史，共同推进液冷技术在
    AI 工厂中的产业化大规模部署。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 NVIDIA AI 工厂的标准参考架构，DSX 设计定义了行业从风冷向液冷转型的技术路径和最佳实践，对超大规模数据中心建设和冷却方案选型具有重要指导意义。
  risk_notes:
  - 参考设计在炎热气候地区每年仍有约 1% 的时间需要机械冷冻机补冷，不能完全脱离传统制冷设备。
  - 全液冷方案需要数据中心运营商进行大规模基础设施改造和投资，对现有风冷数据中心的迁移成本较高。
  score: 8.0
  article_ids:
  - da0ee3bbeda7b90d
  evidence_snippets:
  - NVIDIA DSX AI 工厂参考设计概述了设计、建造和运营整个 AI 工厂基础设施栈的最佳实践，是指导全液冷 AI 工厂建设的标准参考架构。
  - 该参考设计实现了接近零的水消耗，通过基于干冷器的闭环系统消除了蒸发水冷，全年约 99% 的时间无需开启冷冻机。
---

Hot tubs sit at about 38 to 40 degrees Celsius, warm enough that most people can only soak for about 15 minutes. NVIDIA’s newest AI servers can run their cooling liquid even hotter — up to 45 degrees Celsius, or 113 degrees Fahrenheit. That higher temperature limit is precisely what makes them more energy efficient.

The Rubin generation of NVIDIA AI infrastructure is the world’s first to achieve 100% liquid cooling — every chip, every networking component, cooled entirely by liquid in a closed loop with no fans anywhere in the system. This liquid cooling methodology is outlined in the NVIDIA DSX AI factory reference design, a guide that outlines best practices to design, build and operate the entire AI factory infrastructure stack.

Although each generation offers significantly more computing power for each watt, full liquid-cooled AI compute infrastructure enables data centers to dramatically reduce cooling energy consumption — making a meaningful difference to overall data center energy use at hyperscale.

“The NVIDIA DSX reference design for AI factories has zero water consumption — we have eliminated massive amounts of power usage and pretty much all water usage,” said Ali Heydari, director of data center cooling and infrastructure at NVIDIA. “With dry-cooler-based designs, it’s a closed-loop system with no evaporative water cooling — outside of maybe 1% of the year when we might need chillers in some climates.”

Historically, cooling alone has accounted for up to 40% of a data center’s electricity consumption, making it one of the most significant areas where efficiency improvements can drive down both operational expenses and energy demands.

Industry estimates suggest that raising chiller plant temperatures by just one degree can cut cooling energy costs by about 4%. At scale, those savings add up quickly. A 50-megawatt hyperscale facility can save over $4 million annually in cooling-related energy and water costs by moving to liquid-cooled infrastructure.

In favorable climates, NVIDIA’s 45-degree liquid-cooling architecture can enable chiller-less operation with dry coolers, reducing facility cooling water consumption from roughly 2.6 million gallons per megawatt per year for conventional cooling-tower-based systems to near zero — up to a 100% reduction in water use.

The reason: traditional air-cooled data centers depend on large volumes of cooled air to remove heat from IT equipment, often requiring energy-intensive cooling infrastructure during hot weather. With NVIDIA’s 45-degree liquid cooling, heat is captured directly at the chip and transported through liquid loops operating at much higher temperatures, allowing outdoor dry coolers to reject heat efficiently for much of the year while significantly reducing mechanical cooling requirements and facility water consumption.

The data center ambient temperature is flexible — warm summer air is fine — because nothing in the server depends on cool air. The liquid does all the work — and the same liquid can be recirculated in a closed loop so no new water is consumed to cool the chips.


**A New Standard for the Industry**

Because the NVIDIA Rubin platform integrates 100% liquid-cooled infrastructure, every cloud provider and data center operator building for it is making the transition.

The ecosystem is keeping pace. Motivair, the advanced cooling division of Schneider Electric, has worked alongside NVIDIA’s product roadmap for nearly a decade — and Richard Whitmore, its president and CEO, says the relationship only intensified as power densities crossed the threshold where air cooling was no longer a viable option.

“Once the watts per chip crossed a certain level, liquid cooling became mandatory,” said Whitmore.

**Too Hot to Cool AI Infrastructure Is Hotter Than You’d Think**

There’s a long-standing misconception in the industry that a cold data center is an efficient one. Decades ago, if a data center didn’t feel like a walk-in freezer, people would assume something was wrong.

In reality, chips can sustain far warmer environments than that instinct suggests. Silicon processors generate enormous internal heat — the coolant entering a fully liquid-cooled chip at 45 degrees Celsius exits at roughly 55 degrees, having absorbed that heat load across the chip surface. Yet performance doesn’t degrade.

The processors continue to operate at full performance because liquid-cooled cold plates keep device temperatures within validated operating limits, even with coolant entering the rack at 45 degrees Celsius.

**No Fans, No Cold Aisles — A Fundamentally Different Machine**

Walk into a traditional data center and notice two things: the noise — cooling fans contribute to total noise levels at or above 85 decibels, loud enough to require ear protection — and the physical choreography of hot aisles and cold aisles, carefully managed to push cooled air across components.

The Rubin architecture changes the picture.

Coolant — 75% water and 25% propylene glycol — flows through cold plates that sit directly on processors, pulling heat out at the source. Running that coolant at up to 45 degrees Celsius means that in many climates, the facility loop can reject heat without turning on mechanical chillers and noisy fans.

That unlocks something beyond energy savings: the possibility of eliminating water consumption entirely.

In the right geography — somewhere with reliably cool outdoor air — a liquid-cooled data center can reject its heat through coolant distribution units that capture heat directly at the source and transport it to outdoor dry coolers, essentially large radiator coils positioned outside the building.

The loop is filled once and runs closed for the life of the facility. And it takes dramatically less space in the AI factory compared to traditional air-cooling infrastructure.

“In the right geographic location, with the right system design, you don’t need any refrigeration equipment,” Whitmore said. “You can just put big radiator coils outside and use the air temperature for all your cooling. It’s incredibly efficient.”

The geography caveat matters. A data center in the Scottish Highlands and one in Phoenix, Arizona, face very different realities. But even in warmer climates, the shift toward 45-degrees-Celsius coolant moves operators significantly closer to that chiller-less ideal — where chillers may turn on just a few days a year when the outside air temperature demands it.

Another key benefit of this new model for AI factories is the potential for waste heat recovery, where residual heat from AI factory operations can be repurposed to heat commercial or residential buildings nearby.

**The Engineering Problem Nobody Had Solved**

Previous liquid-cooled servers were hybrid: GPUs and CPUs got cold plates, but the rest of the system stayed air-cooled, with finned heat sinks designed to shed heat into moving air. In a fully liquid-cooled server, the cooling for these components needed to be completely redesigned to use liquid.

NVIDIA’s thermal engineering team reworked how those components handle heat, designing cooling loops that simplify how liquid is routed to multiple high-power chips on the board using a single inlet and outlet, resulting in a cleaner tray-level cooling architecture.

One visible outcome: Rubin servers have clean, sealed front panels where air-cooled servers have perforated bezels. Another: fully liquid cooled servers enable higher rack density than air-cooled servers, so a system that previously occupied six rack units now fits in two — more compute, less space, less noise.

AI workloads are not getting lighter. The compute demand driving data center construction is growing faster than almost any other category of infrastructure investment.

Without efficiency improvements in how that compute is cooled, the energy cost of running AI at scale would grow in lockstep with the hardware. Liquid cooling at up to 45 degrees Celsius — hotter than a hot tub, cooler for the planet — is one of the most important tools the industry has to close that gap.

*Learn more about **liquid cooling**, the **NVIDIA DSX** platform for AI factories and NVIDIA’s approach to **energy-efficient AI infrastructure.*