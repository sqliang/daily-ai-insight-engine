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
---

Progress in AI compounds fastest when the entire system improves together. That is how I think about OpenAI’s compute strategy: one integrated system spanning data centers and chips, frontier models, our developer platform, consumer and enterprise products, and AI-native devices, with each layer strengthening the next.

Better software makes hardware more productive. Hardware designed for our workloads improves speed and efficiency. More capable models unlock better products, which generate more demand, usage, and learning. Those signals flow back through the system and help us improve it again.

Today, we shared the first measured performance results from Jalapeño, OpenAI’s first custom inference chip. On InferenceX, a public benchmark using GPT‑OSS 120B, Jalapeño delivered more peak throughput per kilowatt and lower token latency than the commercial systems in the comparison. It also performed strongly on DeepSeek R1 and Kimi K2, showing that its gains extend across model families.

Jalapeño gives us greater control over how our models run and over the economics of serving them. By developing the model, serving software, chip, memory, and network together, we can improve throughput, latency, energy efficiency, and cost as one system. It creates a credible first-party path alongside the accelerators we use from other partners, expanding our ability to match each workload to the strongest system at the right economics. We now have working first-party silicon with measured results, and future generations are already underway.

Different workloads place different demands on the system. Frontier training, high-volume inference, and always-on agents have different requirements across chips, software, networks, power, and latency.

Our goal is to stay on the Pareto frontier: continually seeking the strongest mix of capability, speed, reliability, efficiency, and cost for each workload. Different chips and providers lead on different dimensions, and the frontier keeps moving.

Our portfolio gives us the range to meet those needs. Microsoft’s compute and NVIDIA’s chips have been foundational to OpenAI’s growth. Today, our portfolio also includes AWS, AMD, Broadcom, Cerebras, CoreWeave, Oracle, SB Energy and SoftBank. Each brings different strengths across cloud infrastructure, accelerated computing, low-latency inference, data-center development, and energy delivery.