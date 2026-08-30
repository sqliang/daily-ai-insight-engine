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