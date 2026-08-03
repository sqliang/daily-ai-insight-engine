---
title: AMD's Helios (4 minute read)
source: https://www.cnbc.com/2026/07/20/amd-helios-microsoft-ai-nvidia.html?utm_source=tldrai
author: []
published: ''
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bedb98d5f0e81ee7
source_type: news_media
tldr: AMD 推出首款机架级 AI 系统 Helios，微软加入 Meta、OpenAI、Oracle 等客户行列。Helios 整合 AMD 自研 GPU、CPU、网络和软件，以最低每
  token 成本为目标，将于今年晚些时候开始出货。
objective_summary: 2026 年 7 月 20 日，AMD 宣布其首款机架级 AI 系统 Helios 即将出货，微软成为最新客户。Helios
  将 AMD 的 Instinct GPU、EPYC CPU、网络和软件整合为一体化系统，旨在以最低每 token 成本与 Nvidia 的 Grace Blackwell
  和 Vera Rubin 竞争。微软将在 Azure 数据中心部署 Helios 用于前沿模型推理，Meta、OpenAI、Oracle 和 Tata Consultancy
  Services 等也已承诺采用。Futurum Group 估计 Helios 单套系统成本在 500 万至 550 万美元之间，AMD 股价当日上涨超过 4%。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - AMD
  - Microsoft
  - Meta
  - OpenAI
  - Oracle
  - Tata Consultancy Services
  - SpaceX
  - Cohere
  - Nvidia
  - Futurum Group
  technologies:
  - Helios
  - Instinct GPU
  - EPYC
  - Venice
  - MI300X
  - Grace Blackwell
  - Vera Rubin
  - Maia
  key_people:
  - Forrest Norrod
  - Lisa Su
  - Satya Nadella
  - Daniel Newman
  - Jim Cramer
key_logic_flow:
- AMD 推出首款机架级 AI 系统 Helios，整合 GPU、CPU、网络和软件四大部分，旨在提供最低的每 token 成本。
- 微软宣布将采用 Helios 部署于 Azure 数据中心，用于前沿模型推理和 Azure AI 服务，同时新增两个基于 AMD Venice CPU 的计算实例，分别面向
  Agentic AI 和半导体设计。
- Meta 承诺部署高达 6 吉瓦的 AMD GPU，今年先以 1 吉瓦的 Helios 机架开局；OpenAI、Oracle 和 Tata Consultancy
  Services 也已承诺采用 Helios。
- Futurum Group 估计 Helios 单价在 500 万至 550 万美元之间，重量达 7000 磅，比 Nvidia Vera Rubin 更宽更重；Vera
  Rubin 估价为 350 万至 400 万美元。
- AMD 数据中心收入在 2026 年第一季度同比增长 57%，公司计划从 2027 年起实现数百亿美元的 AI 收入，其中大部分来自 Helios。
- Nvidia 控制着超过 95% 的数据中心 GPU 市场，AMD 仅占约 4.5%，但分析师认为 Helios 有望帮助 AMD 将份额提升至 20% 至 25%。
object_mentions:
- object_type: product
  name: AMD Helios
  canonical_name: AMD Helios
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - AMD 正在准备出货其首款专为人工智能设计的机架级系统 Helios，这是首个与 Nvidia Grace Blackwell 和 Vera Rubin 直接竞争的一体化系统。
  - 微软宣布将采用 Helios 系统部署于 Azure 数据中心，用于前沿模型推理和 Azure AI 服务，这是 Helios 获得的重要客户承诺。
  - Helios 整合了 AMD 自研的 GPU、CPU、网络和软件四大部分，AMD 表示该系统旨在提供最低的每 token 推理成本和最优总拥有成本。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Nvidia Grace Blackwell
  canonical_name: Nvidia Grace Blackwell
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Helios 是首个直接与 Nvidia 广受欢迎的 Grace Blackwell 和 Vera Rubin 机架级系统竞争的同类产品。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Nvidia Vera Rubin
  canonical_name: Nvidia Vera Rubin
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Futurum Group 估计 Nvidia 第二代机架级系统 Vera Rubin 单价在 350 万至 400 万美元之间，低于 Helios 的 500
    万至 550 万美元。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: AMD Instinct GPU
  canonical_name: AMD Instinct GPU
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - AMD 表示前十大 AI 公司中有八家在其 Instinct GPU 上运行工作负载，包括 OpenAI、Cohere 和 SpaceXAI。
  - 每个 Helios 计算托盘配备四块 Instinct GPU，由一颗 EPYC CPU 驱动，构成系统的核心算力单元。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: AMD MI300X
  canonical_name: AMD MI300X
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 微软在 2023 年率先采用了 AMD 的 MI300X GPU，该芯片是当时与 Nvidia AI 芯片直接竞争的产品。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Microsoft Azure AI
  canonical_name: Microsoft Azure AI
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 微软 CEO Satya Nadella 表示正在扩展 Azure 基础设施组合以纳入 AMD Helios，为客户提供构建下一代 AI 应用程序所需的性能和选择。
  - Helios 系统将用于支持 Azure AI 服务以及微软 AI 客户的前沿模型推理工作负载。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: AMD Venice CPU
  canonical_name: AMD Venice CPU
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 微软将新增两个基于 AMD 最新 Venice CPU 的计算实例，一个面向 Agentic AI 和数据管道，另一个面向半导体设计。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Microsoft Maia
  canonical_name: Microsoft Maia
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 微软在其数据中心内部署了自研的 Maia 芯片，与 AMD 芯片形成互补的计算资源布局。
  article_id: bedb98d5f0e81ee7
extract_result: success
---

After a decade-long comeback, chip giant Advanced Micro Devices is preparing to ship its first rack-scale system for artificial intelligence, called Helios, to a growing list of customers that now includes Microsoft.

It's the first rival to Nvidia's wildly popular Grace Blackwell and Vera Rubin systems, and is aiming to give the world's most valuable chipmaker its first real competition in years.

Microsoft announced Monday it will use the Helios system in its data centers, joining Meta, OpenAI, Oracle and others in a race to grab as much compute as possible.

AMD will begin shipping to customers, including Microsoft, later this year. Shares of AMD climbed more than 4% on Monday. Microsoft stock climbed more than 1%.

Details about financial terms or the amount of compute capacity weren't disclosed.

"We are expanding the Azure infrastructure portfolio with AMD Helios to give customers the performance, scale and choice they need to build and run the next generation of AI applications," Microsoft CEO Satya Nadella wrote in a press release.

The new Helios system will power frontier model inference for Microsoft, its AI customers and support Azure AI services. Microsoft will also add two new computing instances run on AMD's latest "Venice" central processing units, or CPUs, one for agentic AI and data pipelines, and another for semiconductor design.

It's the continuation of a longtime partnership, with AMD chips powering Microsoft's Surface PCs and Xbox gaming consoles for many years. In 2023, Microsoft was also the first to adopt AMD's MI300X graphics processing unit, or GPU, that rivaled Nvidia's AI chips. Microsoft also deploys its own Maia chips in its data centers.

Like its peers, Microsoft needs as much compute as possible, especially as it ramps up its own model development and allocates more computing capacity to research and development. In June, it announced seven models built in-house. Microsoft's AI efforts thus far have seen mixed results, from its 365 Copilot AI assistant to its GitHub Copilot coding agent. It's the worst-performing "Magnificent Seven" stock so far this year.

Microsoft is part of a growing number of big companies turning to AMD for AI acceleration. AMD says eight of the top 10 AI companies run workloads on its Instinct GPUs, including OpenAI, Cohere and Elon Musk's SpaceXAI, which is part of SpaceX.

In February, Meta* *announced it'll use up to 6 gigawatts of AMD GPUs over time, starting with 1 gigawatt deployed on Helios racks later this year. OpenAI and Oracle also made major commitments to deploy Helios this year, with India's largest IT company, Tata Consultancy Services, committing to use it as well.

CNBC got the world's first detailed look inside a Helios system, from the Texas data center lab where it's being developed and tested.

### 'Lowest cost per token'

Named for an ancient Greek god who pulls the sun across the sky with the help of four horses, Helios brings together four things AMD does in-house: GPUs, CPUs, networking and software.

"We're very focused on providing the best total cost of ownership, the lowest cost per token, all in," data center head Forrest Norrod told CNBC about AMD's first-generation system. "And our customers are telling us that we're achieving that."

In May, AMD CEO Lisa Su told CNBC's Jim Cramer that Helios has "significant benefits" over Nvidia's rack-scale systems, "when you're talking about inference and when you're talking about memory bandwidth and memory capabilities."

While AMD wouldn't comment on cost, the Futurum Group estimates Helios will cost between $5 million and $5.5 million. That's compared with Futurum estimates of $3.5 million to $4 million for Nvidia's second-generation rack-scale system, Vera Rubin.

At up to 7,000 pounds, Helios is also wider and heavier than Nvidia's Vera Rubin.

Nvidia controls more than 95% of the data center GPU market, according to the Futurum Group. AMD only holds some 4.5% of the market, but Helios could change that.

"I think there's a serious case in which AMD does great and can get to 20% and 25%. And by the way, this is hundreds of billions of dollars of revenue," said Daniel Newman, analyst and CEO of the Futurum Group.

In the first quarter of 2026, data centers made up the majority of AMD's revenue, up 57% year over year. AMD told CNBC that it plans to book tens of billions in data center AI revenue starting in 2027, the majority coming from Helios.

In data center CPU market share, Intel remains the clear leader, but AMD has steadily been gaining ground. This CPU leadership sets AMD apart from Nvidia, which launched its first server CPU in 2021 and shifted strategies to renew focus on the chips this year.

### 'A very different AMD'

Norrod called Helios "our baby," as he showed CNBC the system's core chips. Each of its 18 compute trays has four Instinct GPUs powered by a single EPYC central processing unit.