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
pipeline_stage: ingested
id: 0f9bc8fb2cad5d50
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