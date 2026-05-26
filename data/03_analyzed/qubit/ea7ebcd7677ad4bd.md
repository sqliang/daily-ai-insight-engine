---
title: 腾讯混元开源全新翻译模型Hy-MT2 ，上线小程序「腾讯Hy翻译」
source: https://www.qbitai.com/2026/05/422068.html
author:
- '[[闻乐]]'
published: '2026-05-21'
created: '2026-05-22'
description: 最大提升体现在指令遵循能力上
tags:
- clippings
extraction_status: success
id: ea7ebcd7677ad4bd
source_type: news_media
tldr: 腾讯混元开源Hy-MT2翻译模型系列，支持33种语言互译，并上线「腾讯Hy翻译」小程序。
objective_summary: 2026年5月21日，腾讯混元宣布开源Hy-MT2多语言翻译模型系列（1.8B/7B/30B-A3B三个尺寸），同时上线「腾讯Hy翻译」微信小程序。Hy-MT2在FLORES-200评测中接近Gemini
  3.1 Pro水平，最大提升体现在指令遵循能力。1.8B模型通过AngelSlim 1.
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Tencent
  - Google
  - Microsoft
  - ARM
  - Qualcomm
  - Intel
  - 沐曦
  - 天数智芯
  technologies:
  - Hy-MT2
  - AngelSlim
  - FLORES-200
  - IFMT Bench
  - Sherry
  - MoE
  - 1.25-bit量化
  - 4-bit量化
  - 8-bit量化
  - FP16
  - WMT26
  key_people: []
key_logic_flow:
- 2026年5月21日，腾讯混元正式开源Hy-MT2翻译模型系列，包含1.8B（端侧轻量）、7B（均衡实力）和30B-A3B（专业效果）三个尺寸，支持33种语言互译。
- Hy-MT2在FLORES-200通用翻译评测中接近Gemini 3.1 Pro水平，7B和30B-A3B在开源模型中达到最佳效果，1.8B轻量模型超越微软等主流商业翻译API。
- 相比上一代Hy-MT1.5，Hy-MT2的最大提升在于指令遵循能力，能更准确理解用户对术语、风格和输出格式的具体要求，IFMT Bench测试集已同步开源。
- Hy-MT2采用混元自研AngelSlim极端量化方案，提供1.25-bit、2-bit、4-bit、8-bit和FP16版本，1.8B模型仅需440MB存储空间，基于Sherry框架在苹果A15上推理速度提升1.5倍。
- 「腾讯Hy翻译」微信小程序同步上线，支持语音输入、自定义翻译风格和指令，可通过提前下载端侧模型实现离线翻译。
- Hy-MT2已在GitHub、HuggingFace、ModelScope和腾讯云等平台开源，ARM、高通、Intel、沐曦、天数智芯等多个硬件平台支持部署，腾讯混元同时与WMT26合作举办翻译赛事。
pipeline_stage: fact_extracted
impact_score:
  score: 5.5
  reason: Hy-MT2 是翻译领域的重量级开源发布，技术层面有真实突破（1.25-bit极端量化、指令遵循翻译能力），且在微信小程序中直接落地可用，覆盖13亿用户入口。但翻译模型本身并非基础模型级别的范式转移，更多是改变了机器翻译赛道的竞争格局——开源模型首次在关键指标上逼近
    Gemini 3.1 Pro，同时以440MB端侧体积超越微软等商业API，对商业翻译服务构成实质性威胁。综合来看属于重要产品发布+局部竞争重塑，但尚未达到行业范式转移级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 1.25-bit极端量化实现端侧440MB部署，以及翻译指令遵循能力的代际跃升
hype_assessment:
  level: medium
  reason: 文章引用了具体评测基准（FLORES-200、IFMT Bench）和量化数据，核心结论用词相对克制（'接近'而非'超越'Gemini 3.1
    Pro），但仍存在典型的PR包装痕迹：反复强调'最佳效果'、'主流商业API'等模糊比较词汇，对1.25-bit量化的精度损失缺乏披露，且未提供与NLLB等主流开源翻译模型的直接对比数据。
information_entropy: medium
domain_disruption:
  technical_innovation: 1.25-bit极端量化方案（AngelSlim）将7B以下翻译模型压缩至440MB，基于自研Sherry框架在苹果A15上推理速度提升1.5倍，为端侧离线翻译扫清了存储和算力障碍；指令遵循翻译能力（IFMT
    Bench）填补了翻译模型理解用户风格/术语偏好的空白，从'翻译'升级为'可控翻译'。
  business_model: 开源模型+微信小程序双轨策略形成'基础能力免费开源、消费级入口聚拢用户'的典型腾讯打法。1.8B端侧模型超越微软等商业API后，直接威胁按量计费的商业翻译服务；多硬件平台（含国产芯片）适配则锁定了政企信创市场的国产化需求。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 【强制 CoT 评估】第一步：判断赛道天花板——翻译是全球最大语言AI市场之一，TAM超500亿美元，且多语言需求随全球化持续增长，赛道本身具备长期复利基础。第二步：评估技术护城河的可持续性——Hy-MT2的核心壁垒不在于翻译质量（该领域正快速商品化），而在于三点：①AngelSlim
    1.25-bit极端量化方案将1.8B模型压缩至440MB，可在手机端侧实现离线翻译，这为亿级IoT和移动设备打开了部署窗口；②指令遵循能力（IFMT Bench）解决了翻译场景中「术语一致性」「风格可控性」的真实痛点，这种能力需要高质量标注数据飞轮，开源IFMT
    Bench本身即是建立行业标准的一次布局；③微信小程序分发渠道是独特壁垒——全球没有其他翻译模型能直接触达13亿微信用户。第三步：评估复利效应——开源策略虽然放弃直接模型授权收入，但能吸引开发者生态、提升腾讯云API调用量、并通过小程序收集真实场景反馈数据反哺模型迭代，形成「开源获客→云服务变现→数据回流→模型升级」的正向飞轮。第四步：风险折价——翻译模型赛道拥挤（Google、DeepL、Meta
    NLLB等），开源模型商品化速度快，3-5年后Hy-MT2单一模型未必仍是行业基石，但腾讯在「端侧量化翻译+微信生态分发」的组合壁垒更难被复制。综合给分7.0分：有成为细分赛道基础设施的潜力，但需持续验证数据飞轮和商业化转化效率。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Tencent
- Qualcomm
- ARM
- 沐曦
- 天数智芯
- HuggingFace
competitive_casualty:
- Microsoft Translator
- DeepL
- Google Translate
- 小型翻译API初创公司
- 百度翻译
- 阿里翻译
market_opportunities:
- 端侧离线翻译应用创业机会：Hy-MT2 1.8B模型仅需440MB存储空间且支持1.25-bit极端量化，可针对出境游、商务差旅、应急通讯等无网/弱网场景开发独立翻译App或SDK，差异化竞争Google
  Translate等依赖云端的方案，尤其在隐私敏感场景（如医疗问诊翻译、法律文书初译）具备合规优势。
- 垂直行业翻译微调与私有化部署服务：基于Hy-MT2的指令遵循能力（IFMT Bench已验证），可为金融、法律、医药、游戏出海等垂直领域定制术语库翻译模型，结合30B-A3B的MoE架构提供企业级私有化部署方案，满足数据不出境的政企客户需求。
- 国产芯片+翻译模型软硬一体优化方案：Hy-MT2已获ARM、高通、Intel、沐曦、天数智芯等多平台部署支持，开发者可基于Sherry框架针对国产GPU/NPU做推理优化，形成「国产芯片+开源翻译模型」的一体化解决方案，切入信创市场和智能硬件（翻译耳机、翻译笔）供应链。
risk_matrix:
  regulatory: 多语言语料合规风险：33种语言训练数据涉及多法域数据采集规范（欧盟GDPR、中国个人信息保护法、跨境数据流动规制），若训练语料包含未经授权的版权内容或个人信息，可能面临跨国诉讼和监管处罚；另翻译内容生成涉及跨境信息传播，需关注网信办对AI生成内容的标识要求。
  technological: 极限量化的质量折损风险：1.25-bit量化虽大幅降低存储和推理成本，但在低资源语言对和专业术语翻译上可能存在精度退化，长尾场景可靠性不足；此外，WMT26赛事中可能涌现更强架构（如基于扩散模型的翻译方案），导致Hy-MT2的技术窗口期缩短。
  competitive: 巨头生态挤压风险：Google Gemini 3.1 Pro仍是翻译质量标杆且深度集成于Android/Chrome生态，微软翻译API绑定Office/Azure企业套件，腾讯Hy-MT2虽开源但商业化路径依赖微信小程序生态，在海外市场缺乏分发渠道；另字节跳动、阿里等国内大厂可能快速跟进开源翻译模型，引发价格战和人才争夺。
  ethical: 翻译偏见与深度伪造风险：33种语言中低资源语言的翻译质量不均可能加剧数字语言鸿沟，错误翻译在医疗、法律等场景可能导致严重后果；指令遵循能力虽然便利但也可能被滥用，通过风格指令批量生成具有误导性的翻译内容用于舆论操控或欺诈。
  additional:
  - 微信生态依赖风险：'腾讯Hy翻译'小程序是核心产品入口，但小程序能力和分发受微信平台规则约束，若微信调整AI应用政策或限制第三方模型接入，将直接影响产品触达和用户增长
  - 开源社区治理风险：Hy-MT2开源后若缺乏持续的社区维护和文档更新，可能重蹈部分国产开源模型'发布即沉寂'的覆辙，开发者信任一旦丧失难以挽回
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: strategic_invest
---

# 腾讯混元开源全新翻译模型Hy-MT2 ，上线小程序「腾讯Hy翻译」

最大提升体现在指令遵循能力上


5月21日，腾讯混元宣布开源全新翻译模型Hy-MT2并上线翻译小程序「腾讯Hy翻译」。Hy-MT2 是支持 33 种语言互译的多语言模型，其中7B 和 30B-A3B模型在各类翻译任务上达到了开源模型最佳效果，超越了几十倍参数量的模型，轻量级的 1.8B 模型也超越了微软等主流商业 API，且得益于 AngelSlim 1.25-bit 极端量化，仅需 440MB 存储空间，可以轻松部署在主流手机芯片上支持本地推理，相比Hy-MT1.5推理速度提升 1.5 倍。


Hy-MT2 包含 3个尺寸的模型 Hy-MT2-1.8B、Hy-MT2-7B、Hy-MT2-30B-A3B，分别侧重端侧轻量部署、均衡实力以及专业效果。

「腾讯Hy翻译」小程序基于 Hy-MT2 打造，相比其他翻译工具，不仅支持语音输入，还优化了自定义翻译风格和指令的能力，让翻译结果更符合预期，实用性更强。同时，用户不仅可以在联网环境下体验高速版的混元翻译模型，也可以通过提前下载端侧翻译模型，在无网络或者弱网络场景中使用离线翻译，解决了部分应用场景中网络条件受限的问题。

在通用翻译能力评测中，Hy-MT2系列三个模型在 FLORES-200 平均表现上已经非常接近目前行业表现最好的翻译模型 （Gemini 3.1 Pro ）。同时，Hy-MT2-7B 和 Hy-MT2-30B-A3B 的实测得分已经超过国内主要的通用大模型，在轻量级模型的横向对比中，Hy-MT2-1.8B 也整体优于头部商业翻译 API。

保持通用翻译能力的同时，Hy-MT2 进一步面向真实业务场景和专业领域翻译进行优化。

在真实场景测试集上，Hy-MT2-30B-A3B 效果已经超过 Gemini 3.1 Pro，特别在垂直领域的测试集中，Hy-MT2-30B-A3B在金融、政治、教育几个领域的翻译效果已经部分超过主流翻译模型。


相比上一版本模型，Hy-MT2的最大提升体现在指令遵循能力上，模型能够更准确地理解并执行用户关于术语、风格和输出格式等方面的具体要求。腾讯混元自建数据集 IFMT Bench 测试结果表明，Hy-MT2-7B 和 Hy-MT2-30B-A3B的翻译效果已经超越等相近尺寸开源模型，接近 Gemini 3.1 Pro。目前这一测试集也已经开源。


指令遵循能力见下面的例子，通过“个性化设定：翻译结果简洁精炼，去掉冗余表达，每句不超过15个字”，模型可以很好的遵循指令，让翻译结果更符合要求。

本次升级的 Hy-MT2 模型进一步探索极低比特量化方案，除 4-bit、8-bit 和 FP16 版本外，Hy-MT2 还基于混元自研技术提供了 1.25-bit 和 2-bit 版本，以适配不同硬件环境下的部署需求。基于混元自研 Sherry 框架实现的 1.25-bit 极低比特量化版本在苹果 A15 上的推理速度相比 Hy-MT1.5 的 4-bit 量化版本提升了 1.5 倍，进一步提升了实际可用性。


为了便于开发者使用，Hy-MT2 开源的模型已经在 Github 和 Huggingface 等开源社区上线，ARM、高通、Intel、沐曦、天数智芯等多个平台均支持部署。


总体看来，Hy-MT2 是一个面向真实应用场景的高质量、高效率、多能力多语翻译模型家族，在通用翻译、专业领域翻译、真实业务场景和翻译指令遵循任务上均表现出较强竞争力。


腾讯混元翻译模型坚持从社区和实际应用场景中搜集真实反馈，不断提升模型能力。同时，腾讯混元也希望通过开源和社区活动回馈社区，现在，腾讯混元也在与WMT26官方合作「视频字幕翻译比赛」（https://www2.statmt.org/wmt26/video-subtitle-translation.html），使用Hy-MT系列模型参与「通用机器翻译比赛」（https://www2.statmt.org/wmt26/translation-task.html）和「视频字幕翻译比赛」有机会获得混元特设奖励，诚邀邀大家参与，共同推动机器翻译前沿技术发展。


开源和体验链接，可访问：


l HuggingFace：https://huggingface.co/collections/tencent/hy-mt2

l Modelscope：https://modelscope.cn/collections/Tencent-Hunyuan/Hy-MT2

l Github：https://github.com/Tencent-Hunyuan/Hy-MT2

l 腾讯云：https://console.cloud.tencent.com/tokenhub/text

l 腾讯混元官网：https://aistudio.tencent.com/llm/zh?tabIndex=0

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*

- 菲尔兹奖得主都看懵了：OpenAI非数学模型首次自主突破80年未解数学难题
*2026-05-21* - 虾马之后又火一个！OpenHuman用20分钟了解你的一切，存成卡帕西式知识库
*2026-05-16* - Need is all you need：AI接手Coding后，程序员最值钱的能力只剩这一项?
*2026-05-15* - 别让模型烧Token了！GitHub 20k星神作：把全网变成命令行
*2026-05-16*