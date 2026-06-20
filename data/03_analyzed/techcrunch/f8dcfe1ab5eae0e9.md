---
title: Qualcomm wants to be the chip inside whatever replaces your smartphone, and
  it just announced two products toward that end
source: https://techcrunch.com/2026/06/16/qualcomm-wants-to-be-the-chip-inside-whatever-replaces-your-smartphone-and-it-just-announced-two-products-toward-that-end/
author:
- '[[Ivan Mehta]]'
published: '2026-06-16'
created: '2026-06-17'
description: Qualcomm CEO Cristiano Amon said Tuesday that the company is working
  on over 40 different AI wearable devices — including jewelry, earbuds with cameras,
  pins, and watches — a sign of how aggressively the chipmaker is betting that the
  next major computing platform won't be a phone.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f8dcfe1ab5eae0e9
source_type: news_media
tldr: 高通发布Snapdragon Reality Elite平台和START工具包，押注AI穿戴设备取代手机。
objective_summary: 6月16日，高通CEO Cristiano Amon宣布正开发超40款AI穿戴设备，并发布Snapdragon Reality
  Elite（MR眼镜平台，GPU提升60%，NPU提升160%，可运行3B参数模型达45t/s）和START（AR芯片+软件+白标方案），
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Qualcomm
  - XREAL
  - Google
  - Play for Dream
  - Inspecs
  - O'Neill
  - TitanFlex
  - Apple
  - Samsung
  - Meta
  - CNBC
  technologies:
  - Snapdragon Reality Elite
  - START
  - Scalable Turnkey AI-Ready Toolkit
  - XR
  - VST
  - OST
  - NPU
  - GPU
  - CPU
  - AI
  key_people:
  - Cristiano Amon
key_logic_flow:
- 高通CEO Cristiano Amon表示公司正在开发超过40款AI穿戴设备，涵盖珠宝、摄像头耳机、胸针和手表等形态。
- 高通发布Snapdragon Reality Elite混合现实眼镜平台，GPU性能提升60%，CPU提升30%，NPU提升160%。
- 该平台可运行30亿参数语言模型达到每秒45个token，支持4.4K每眼分辨率@90fps。
- 平台支持独立VST头显和轻量级OST眼镜两种形态，首批设备包括XREAL Project Aura和Play for Dream的产品。
- 高通发布START工具包，包含AR芯片、软件平台、配套应用和白标方案，提供三种参考设计（音频+摄像头、单目显示、双目显示）。
- Inspecs和O'Neill成为START白标方案首批合作伙伴，该平台未来将扩展至智能眼镜以外的其他设备形态。
impact_score:
  score: 6.5
  reason: 高通作为XR芯片领域的实际垄断者（Quest、Ray-Ban Meta均采用高通方案），其战略方向对行业有风向标意义。Reality Elite的GPU
    60%/NPU 160%提升是代际规格升级，45t/s端侧运行3B模型是实用化里程碑，但属于渐进改进而非突破。更具价值的是START白标方案——三种参考设计直接降低了AR眼镜OEM的入场门槛，可能复制高通QRD在安卓手机生态的成功路径。但所有产品均为未来发布，40+设备是管道声明而非可验证交付物，且三星/苹果/Meta自研芯片趋势正在侵蚀高通护城河。整体是重要但非范式转移级的行业事件。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 高通此前多代XR芯片（XR1→XR2→XR2+ Gen2）实际落地进度缓慢，开发者对Reality Elite的真实性能和START工具链成熟度持观望态度
hype_assessment:
  level: medium
  reason: 文章包含可信数据（45t/s、4.4K@90fps、具体合作伙伴XREAL/Play for Dream/Inspecs），并非空洞PR。但'40+款AI穿戴设备'是未经审计的管道宣称，GPU/NPU百分比提升是典型的芯片厂商规格话术——没有第三方基准对比，且百分比对比的基线平台未明确定义。'取代你下一台手机'叙事是高通常用的概念包装手法。
information_entropy: medium
domain_disruption:
  technical_innovation: NPU性能提升160%使3B参数模型在XR设备上达到45t/s端侧推理，对有实时性要求的AI交互场景（手势追踪、语义理解、环境感知）是实质进步。START三种参考设计（音频+摄像头、单目显示、双目显示）系统性覆盖了从音频眼镜到全功能AR的形态梯度，有望大幅降低OEM的硬件研发周期。
  business_model: START白标方案将高通从'芯片卖货'升级为'交钥匙平台+参考设计+软件栈'模式，可能催生一波白牌AR眼镜品牌浪潮，类似手机时代联发科/高通的Turnkey方案催生了深圳白牌手机生态。长期看，这种方案加速了XR硬件普及，但也可能使OEM陷入同质化和高通税锁定。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 高通正在复制其在智能手机时代的'卖铲子'策略，但这次押注的是AI穿戴设备作为下一代计算平台。Snapdragon Reality Elite的NPU提升160%、支持本地运行3B参数模型达45t/s，意味着设备可以脱离云端实现实时AI交互，这解决了穿戴设备最关键的延迟和隐私痛点。START工具包提供芯片+软件+白标方案的完整交钥匙能力，降低了下游OEM的进入门槛，这种'硬件+软件栈+参考设计'三位一体的平台策略将产生极强的网络效应和迁移成本锁定。如果AI穿戴设备确实如高通预测的那样成为手机后的下一个万亿美元市场，高通将在计算基础设施层占据无法绕过的生态位，形成类似智能手机领域的长期复利。风险在于：穿戴设备取代手机的时间线高度不确定，且Apple、Meta等巨头可能自研芯片实现垂直整合，但高通在移动端积累的OEM关系和供应链优势是难以短期复制的。因此给予8分，属于'有潜力成为下一代计算平台基础设施'的范畴。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- Qualcomm
- XREAL
- Google
- Play for Dream
- Inspecs
- O'Neill
- 中小型AI穿戴设备厂商
competitive_casualty:
- Apple
- Samsung
- Meta （Ray-Ban Meta生态受冲击）
- MediaTek
- 传统智能手机OEM厂商
market_opportunities:
- 基于高通START白标方案（含三种参考设计），中小硬件厂商和品牌商可快速推出自有品牌AI智能眼镜，大幅缩短产品研发周期和降低硬件门槛
- Snapdragon Reality Elite平台支持端侧运行3B参数语言模型达45t/s，为开发者在MR眼镜上部署本地AI代理、实时翻译、环境理解等应用提供了充足的算力基础
- AI穿戴设备作为下一代计算平台尚处于早期爆发阶段，创业者可围绕高通芯片生态开发垂直场景解决方案，如工业AR巡检辅助、医疗手术导航、教育沉浸式互动等细分市场
risk_matrix:
  regulatory: AI穿戴设备涉及持续采集视觉、音频和环境数据，多国隐私法规（GDPR、CCPA、中国个人信息保护法）对数据收集范围和用户知情同意提出严格要求，产品上市面临合规审查与跨境数据流动限制风险
  technological: 高通宣称GPU提升60%、NPU提升160%等数据需经第三方实测验证；3B参数模型45t/s在复杂MR场景（实时SLAM+AI推理）中可能算力不足；Meta、Apple等竞争对手的自研芯片方案迭代速度可能超越高通平台
  competitive: Meta Ray-Ban智能眼镜已在消费市场取得先发优势（销量超百万），Apple Vision Pro定义了高端空间计算标准，三星/Google联盟也在开发竞品，高通面临下游合作伙伴（如Meta）自研芯片替代和生态挤压的双重压力
  ethical: 全天候佩戴的摄像头和麦克风设备可能引发大规模隐私泄露与未经同意的数据采集风险，AI Agent持续感知环境可能产生偏见判断或错误信息传播，同时AI穿戴设备可能加速零售、客服等岗位的就业冲击
  additional:
  - 高通平台化战略导致整机厂商过度依赖单一芯片供应商，供应链集中度高，若高通未来调整芯片授权策略或退出某细分市场，下游厂商将面临断供风险
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
---

Qualcomm CEO Cristiano Amon said Tuesday that the company is working on over 40 different AI wearable devices — including jewelry, earbuds with cameras, pins, and watches — a sign of how aggressively the chipmaker is betting that the next major computing platform won’t be a phone.

To power that vision, Qualcomm is announcing two new offerings: a platform called Snapdragon Reality Elite for mixed-reality glasses, designed to run more powerful on-device AI, and the Scalable Turnkey AI-Ready Toolkit (START), a combination of hardware modules and a software stack for AI devices, starting with smart glasses.

Compared to its previous XR platform, the new Snapdragon Reality Elite delivers improvements of up to 60% in GPU performance, up to 30% in CPU performance, and up to 160% in NPU performance, according to the company. Percentage gains in chip specs can be hard to contextualize, but Qualcomm offers one concrete data point, saying the platform can run a 3-billion-parameter language model at 45 tokens per second — fast enough for quick, responsive AI interactions. Qualcomm says the chip will also enable better head and hand tracking, along with improved see-through capabilities.

The Snapdragon Reality Elite supports 4.4K per-eye resolution at 90 fps, a modest bump from the XR2+ Gen 2’s 4.3K per-eye resolution. (The higher the per-eye resolution and frame rate, the sharper and smoother the visual experience, which matters most for reducing the motion sickness and eye strain that’ve historically made extended headset use uncomfortable.)

Qualcomm says the platform is designed to power two types of devices: stand-alone video-see-through (VST) headsets, which layer digital content over a camera feed of the real world, and lightweight, tethered optical-see-through (OST) glasses, which blend digital imagery directly into your field of view. Among the first devices to use it: XREAL Project Aura, shown at Google I/O earlier this year, and an upcoming device from Play for Dream.

START, meanwhile, consists of an AR chip, a software platform, companion apps, and a white-label program aimed at helping hardware makers get to market faster. Through the white label program, the company is offering three reference designs: an audio + camera setup similar to Meta’s Ray-Ban smart glasses, a monocular display, and a binocular display.

Eyewear manufacturers Inspecs and O’Neill — owned by TitanFlex — will be among the first partners in the white label program. Qualcomm said START will expand beyond smart glasses to support other form factors in the future.

Amon’s comments, made to CNBC, flesh out the strategic logic behind both announcements. He argued that as companies seek to gather more real-world data from users to power their AI agents, a new wave of hardware startups building novel form factors will emerge, with major implications for established smartphone players like Apple and Samsung.