---
title: 'Hotter Than a Hot Tub: The 45°C Breakthrough to Cool AI’s Biggest Machines'
source: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
author:
- '[[Josh Parker]]'
published: '2026-06-22'
created: '2026-06-22'
description: Hot tubs sit at about 38 to 40 degrees Celsius, warm enough that most
  people can only soak for about 15 minutes. NVIDIA’s newest AI servers can run their
  cooling liquid even hotter — up to 45 degrees Celsius, or 113 degrees Fahrenheit.
  That higher temperature limit is precisely what makes them more energy efficient.
  [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: da0ee3bbeda7b90d
source_type: tech_blog
tldr: NVIDIA Rubin 实现 100% 全液冷无风扇设计，冷却液温度达 45°C
objective_summary: NVIDIA 发布 Rubin 代 AI 基础设施，首次实现 100% 全液冷无风扇封闭循环冷却。DSX 参考设计采用 45°C
  冷却液和干式冷却器，将冷却用水量降至接近零，每 50 兆瓦设施年节省超 400 万美元冷却成本。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  technologies:
  - liquid cooling
  - DSX AI factory reference design
  key_people:
  - Ali Heydari
key_logic_flow:
- NVIDIA Rubin 代 AI 基础设施是全球首个实现 100% 液体冷却的系统，所有芯片和网络组件均通过封闭循环液冷冷却，无需任何风扇。
- 冷却液运行温度可达 45°C（113°F），比传统冷却温度更高，从而实现了更高的能源效率。
- NVIDIA DSX AI 工厂参考设计采用干式冷却器闭循环系统，几乎消除了数据中心的用水量，传统冷却塔每兆瓦每年约消耗 260 万加仑水。
- 传统数据中心冷却占电力消耗高达 40%，每提高冷却液温度 1°C 可降低约 4% 的冷却能耗。
- 一个 50 兆瓦的超大规模数据中心通过转向液冷基础设施，每年可在冷却相关能源和水成本上节省超过 400 万美元。
extract_result: success
---

Hot tubs sit at about 38 to 40 degrees Celsius, warm enough that most people can only soak for about 15 minutes. NVIDIA’s newest AI servers can run their cooling liquid even hotter — up to 45 degrees Celsius, or 113 degrees Fahrenheit. That higher temperature limit is precisely what makes them more energy efficient.

The Rubin generation of NVIDIA AI infrastructure is the world’s first to achieve 100% liquid cooling — every chip, every networking component, cooled entirely by liquid in a closed loop with no fans anywhere in the system. This liquid cooling methodology is outlined in the NVIDIA DSX AI factory reference design, a guide that outlines best practices to design, build and operate the entire AI factory infrastructure stack.

Although each generation offers significantly more computing power for each watt, full liquid-cooled AI compute infrastructure enables data centers to dramatically reduce cooling energy consumption — making a meaningful difference to overall data center energy use at hyperscale.

“The NVIDIA DSX reference design for AI factories has zero water consumption — we have eliminated massive amounts of power usage and pretty much all water usage,” said Ali Heydari, director of data center cooling and infrastructure at NVIDIA. “With dry-cooler-based designs, it’s a closed-loop system with no evaporative water cooling — outside of maybe 1% of the year when we might need chillers in some climates.”

Historically, cooling alone has accounted for up to 40% of a data center’s electricity consumption, making it one of the most significant areas where efficiency improvements can drive down both operational expenses and energy demands.

Industry estimates suggest that raising chiller plant temperatures by just one degree can cut cooling energy costs by about 4%. At scale, those savings add up quickly. A 50-megawatt hyperscale facility can save over $4 million annually in cooling-related energy and water costs by moving to liquid-cooled infrastructure.

In favorable climates, NVIDIA’s 45-degree liquid-cooling architecture can enable chiller-less operation with dry coolers, reducing facility cooling water consumption from roughly 2.6 million gallons per megawatt per year for conventional cooling-tower-based systems to near zero — up to a 100% reduction in water use.

The reason: traditional air-cooled data centers depend on large volumes of cooled air to remove heat from IT equipment, often requiring energy-intensive cooling infrastructure during hot weather. With NVIDIA’s 45-degree liquid cooling, heat is captured directly at the chip and transported through liquid loops operating at much higher temperatures, allowing outdoor dry coolers to reject heat efficiently for much of the year while significantly reducing mechanical cooling requirements and facility water consumption.