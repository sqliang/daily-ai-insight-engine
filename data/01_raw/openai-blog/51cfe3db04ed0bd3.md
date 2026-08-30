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
pipeline_stage: ingested
id: 51cfe3db04ed0bd3
---

Progress in AI compounds fastest when the entire system improves together. That is how I think about OpenAI’s compute strategy: one integrated system spanning data centers and chips, frontier models, our developer platform, consumer and enterprise products, and AI-native devices, with each layer strengthening the next.

Better software makes hardware more productive. Hardware designed for our workloads improves speed and efficiency. More capable models unlock better products, which generate more demand, usage, and learning. Those signals flow back through the system and help us improve it again.

Today, we shared the first measured performance results from Jalapeño, OpenAI’s first custom inference chip. On InferenceX, a public benchmark using GPT‑OSS 120B, Jalapeño delivered more peak throughput per kilowatt and lower token latency than the commercial systems in the comparison. It also performed strongly on DeepSeek R1 and Kimi K2, showing that its gains extend across model families.

Jalapeño gives us greater control over how our models run and over the economics of serving them. By developing the model, serving software, chip, memory, and network together, we can improve throughput, latency, energy efficiency, and cost as one system. It creates a credible first-party path alongside the accelerators we use from other partners, expanding our ability to match each workload to the strongest system at the right economics. We now have working first-party silicon with measured results, and future generations are already underway.

Different workloads place different demands on the system. Frontier training, high-volume inference, and always-on agents have different requirements across chips, software, networks, power, and latency.

Our goal is to stay on the Pareto frontier: continually seeking the strongest mix of capability, speed, reliability, efficiency, and cost for each workload. Different chips and providers lead on different dimensions, and the frontier keeps moving.

Our portfolio gives us the range to meet those needs. Microsoft’s compute and NVIDIA’s chips have been foundational to OpenAI’s growth. Today, our portfolio also includes AWS, AMD, Broadcom, Cerebras, CoreWeave, Oracle, SB Energy and SoftBank. Each brings different strengths across cloud infrastructure, accelerated computing, low-latency inference, data-center development, and energy delivery.