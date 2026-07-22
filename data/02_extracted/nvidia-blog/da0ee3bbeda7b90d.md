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
tldr: NVIDIA 新一代 Rubin AI 基础设施实现 100% 全液冷无风扇设计，冷却液运行温度可达 45°C。配合 DSX AI 工厂参考设计的干冷器闭路系统，大幅降低数据中心冷却能耗与水资源消耗，一座
  50MW 设施每年可节省超 400 万美元。
objective_summary: NVIDIA 发布其 Rubin 代 AI 基础设施，首次实现 100% 全液冷无风扇设计，冷却液最高运行温度达 45°C。该方案基于
  NVIDIA DSX AI 工厂参考设计，采用干冷器闭路循环系统，在大部分气候条件下无需冷水机组，实现近乎零的水资源消耗。NVIDIA 数据中心冷却与基础设施总监
  Ali Heydari 表示该设计消除了大量电能使用和几乎全部水资源消耗。传统数据中心冷却能耗占总用电量高达 40%，而新架构通过提升冷却液温度显著降低能源成本，行业估算冷冻水温度每升高
  1°C 冷却成本可降低约 4%。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  technologies:
  - DSX
  - liquid cooling
  - dry cooling
  key_people:
  - Ali Heydari
key_logic_flow:
- NVIDIA 新一代 Rubin AI 基础设施是全球首个实现 100% 全液冷无风扇设计的服务器产品线，芯片和网络组件全部由封闭循环液体冷却。
- 新系统冷却液运行温度可达 45°C（113°F），比传统系统更高，这一特性使其能效显著优于同类方案。
- NVIDIA DSX AI 工厂参考设计采用干冷器闭路循环系统，在全年绝大部分时间无需冷水机组，实现近乎零的水资源消耗。
- 传统数据中心冷却能耗占总用电量高达 40%，是运营成本和能源需求的最大来源之一。
- 行业估算表明冷冻水温度每升高 1°C，冷却能源成本可降低约 4%，一座 50MW 超大规模设施通过液冷改造每年可节省超 400 万美元。
- 液冷架构将传统冷却塔系统每兆瓦每年约 260 万加仑的耗水量降至近乎零，节水幅度近 100%。
extract_result: success
object_mentions:
- object_type: project
  name: NVIDIA DSX AI factory reference design
  canonical_name: NVIDIA DSX
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA DSX AI 工厂参考设计是一份指导 AI 工厂基础设施设计、建造和运营最佳实践的白皮书。
  - 该参考设计采用干冷器闭路系统，在全年 99% 的时间内无需冷水机组，实现零水消耗。
  article_id: da0ee3bbeda7b90d
- object_type: product
  name: NVIDIA Rubin
  canonical_name: NVIDIA Rubin
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA Rubin 代 AI 基础设施是全球首个实现 100% 全液冷的产品线，芯片和网络组件均由封闭循环液体冷却。
  - Rubin 代服务器的冷却液运行温度可达 45°C，比传统温度更高，从而显著提升能效。
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