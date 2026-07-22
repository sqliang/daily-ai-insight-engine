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