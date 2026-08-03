---
title: 老黄「开源协议」就剩一家没签，是谁啊好难猜啊
source: https://www.qbitai.com/2026/07/461341.html
author:
- '[[Jay]]'
published: '2026-07-27'
created: '2026-07-27'
manifest_dates:
- '2026-07-27'
description: Denny’s和英伟达，有一项核心业务高度重叠
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f2babacf4e97c2ed
source_type: news_media
tldr: 英伟达CEO黄仁勋发布公开信倡导开源AI模型，获70多家机构签署包括OpenAI和微软，但Anthropic拒绝签署，其员工以要求CUDA开源作为讽刺回应，事件引发对开源模型与商业利益的广泛讨论。
objective_summary: 2026年7月，英伟达CEO黄仁勋发布个人首条推文及公开信，呼吁行业支持开放权重AI模型。OpenAI、微软等70多家机构和公司签署了该开源倡议书，但Anthropic是唯一拒绝签署的主要AI公司。Anthropic技术人员Julian
  Schrittwieser以要求英伟达开源CUDA和微软开源Windows作为讽刺回应，吴恩达出面为黄仁勋辩护。分析认为开源模型普及将分散推理算力需求，可能反而强化英伟达的生态护城河。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - NVIDIA
  - OpenAI
  - Anthropic
  - Microsoft
  - Google DeepMind
  - Denny's
  technologies:
  - CUDA
  - GPU
  - Whisper
  - TPU
  - Windows
  key_people:
  - Jensen Huang
  - Sam Altman
  - Satya Nadella
  - Julian Schrittwieser
  - Andrew Ng
  - Yann LeCun
key_logic_flow:
- 黄仁勋发布个人首条推文和公开信，号召AI行业支持开放权重模型，获得70多家公司和机构签署。
- OpenAI和微软CEO纳德拉均签署了开源倡议书，但Anthropic是唯一拒绝签署的主要AI公司。
- Anthropic员工Julian Schrittwieser在X平台公开讽刺，要求英伟达开源CUDA和微软开源Windows作为条件。
- 吴恩达出面为黄仁勋辩护，指出混淆个人不开源代码与阻止他人开源的逻辑是错误的。
- 分析认为开放权重模型普及将分散推理算力需求，更多企业自行部署模型，反而强化英伟达的生态护城河。
- 美式连锁餐厅Denny's以幽默方式声援黄仁勋，借用Open一词的双关含义表达支持。
object_mentions:
- object_type: product
  name: Whisper
  canonical_name: OpenAI Whisper
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI虽然未开源旗舰大模型，但发布过Whisper和gpt-oss等小模型作为开源贡献。
  article_id: f2babacf4e97c2ed
- object_type: product
  name: Claude Fable
  canonical_name: Claude Fable
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提及在Anthropic的Claude Fable发布期间，部分用户遭遇了连续三次被封号的问题。
  article_id: f2babacf4e97c2ed
extract_result: success
impact_score:
  score: 7.0
  reason: 英伟达CEO黄仁勋以个人首条推文+公开信发起开源倡议，获得70余家机构签署，包括OpenAI和微软等关键玩家。Anthropic拒绝签署并引发公开争论，行业首次形成明确的开源vs闭源阵营分化。这不仅是PR事件，更可能影响未来AI模型的发布策略和生态格局。评分依据：属于重要行业事件，改变局部竞争格局，但距范式转移还有距离。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 英伟达要求他人开源模型，自己却坚持CUDA闭源的双标争议
hype_assessment:
  level: medium
  reason: 事件本身具有实质内容（70多家真实签署方），但存在明显的PR包装。老黄选择个人首条推文发布公开信，时机选择刻意制造话题。文章也承认这份倡议是否有实际约束力存疑——'估计一个月后就没人记得了'。'真Open·AI协议'等表述属于PR话术包装，实际更像一份立场宣言而非具约束力的协议。
information_entropy: medium
domain_disruption:
  technical_innovation: 无。本事件为行业政策倡议，不涉及技术架构或工程突破。核心讨论围绕模型开放策略而非技术本身。
  business_model: 分析指出开放权重模型普及将分散推理算力需求——更多企业自行部署而非依赖API服务商——可能反而强化英伟达的生态护城河。这一洞察重塑了对'开源vs闭源'商业模式竞争的理解，表明开源策略可能意外巩固硬件供应商的议价权。
engineering_complexity: conceptual
compound_value:
  score: 7.8
  reason: 该事件表面是开源意识形态之争，实质是英伟达从AI训练市场向推理市场扩张的长期战略布局。开放权重模型普及将带来推理算力的分散化部署——企业自行部署模型而非依赖闭源API，直接拉动GPU采购需求，且部署方无动力切割CUDA生态自研芯片。70+家机构签署形成的行业共识具有基础设施效应，短期内难以逆转。但需注意：该倡议缺乏实质约束力，开放权重模型与闭源前沿模型的质量差距仍需验证，且Anthropic为代表的闭源阵营仍掌握顶尖模型能力和大量资本。若开源生态持续进化至接近闭源水平，英伟达将在训练+推理市场形成双重垄断，复利效应极强；若开源质量始终落后，则此倡议仅为口号，价值有限。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- NVIDIA
- Meta
- Mistral AI
- AWS
competitive_casualty:
- Anthropic
- 定制AI芯片初创公司
- Google TPU
market_opportunities:
- 围绕英伟达GPU生态的开源模型推理部署服务——开放权重模型普及将分散推理算力需求，更多企业自行部署模型，催生面向自部署场景的GPU算力优化与运维服务市场
- 面向企业的开源模型私有化微调与安全合规方案——在开源阵营壮大背景下，帮助金融、医疗、政务等受监管行业安全地将开源模型落地到垂直场景，存在明确的商业变现空间
- 跨芯片平台的模型兼容中间件——闭源阵营（Anthropic/Google TPU、OpenAI自研芯片）与开源阵营（NVIDIA生态）分化加剧，开发一套屏蔽底层芯片差异的模型运行层具有战略稀缺价值
risk_matrix:
  regulatory: 开源权重模型面临跨境监管合规压力——欧盟AI Act对开源模型有特定豁免条款与限制条件，美国对华GPU出口管制可能因开源模型普及而进一步收紧，企业需持续追踪各司法管辖区的监管动态
  technological: 英伟达CUDA单点依赖风险——Anthropic员工以CUDA开源作为条件进行讽刺，折射出行业对单一GPU生态厂商过度依赖的担忧。长期看，Google
    TPU、AMD ROCm等替代方案将持续获得闭源阵营的投入，可能逐步侵蚀CUDA生态壁垒
  competitive: AI芯片生态加速两极分化——Anthropic+Google的TPU路线与OpenAI自研芯片'小辣椒'持续加码，闭源模型厂商正加速构建与英伟达切割的技术栈。开源阵营扩大虽短期利好英伟达，但长期可能催生抗衡力量
  ethical: 开源权重模型的双重用途风险——模型权重开放后更易被滥用（深度伪造、恶意内容生成、生物武器设计等），随着开源阵营扩大，社会舆论与监管机构对AI安全的关注将持续升温，可能倒逼更严厉的开源模型分发管控
  additional:
  - 开源倡议缺乏实质约束力——目前仅以签名形式推进，未涉及具体执行机制、合规标准或技术承诺，存在沦为公关活动的风险
  - 社交媒体叙事扭曲产业判断——事件在X平台获得6000万阅读量，情绪驱动成分较高，可能夸大行业共识的稳固程度
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: Whisper
  canonical_name: OpenAI Whisper
  url: null
  positioning: OpenAI推出的开源语音识别模型，是该公司的代表性开源贡献，在AI开源生态中具有重要标杆意义。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 语音识别技术开发者
  - AI开源社区开发者
  - 需要本地部署语音识别能力的企业
  product_signal: Whisper是OpenAI为数不多的开源模型之一，被文章引为OpenAI支持开源生态的实际行动案例。
  market_signal: 在开源倡议论战中，Whisper被用作对比参照，突出Anthropic完全没有开源产品的局面。
  differentiation: 相比Anthropic完全闭源的策略，Whisper代表了OpenAI在开源领域的切实贡献与行动。
  watch_reason: 作为OpenAI少数公开发布的开源模型，Whisper在持续升级的开源与闭源路线之争中具有标杆意义，其后续更新维护动态将反映OpenAI开源策略的演变方向。
  risk_notes:
  - Whisper作为较早的开源模型，OpenAI后续可能减少对其的更新维护投入力度。
  score: 3.0
  article_ids:
  - f2babacf4e97c2ed
  evidence_snippets:
  - OpenAI虽然未开源旗舰大模型，但发布过Whisper和gpt-oss等小模型作为开源贡献。在开源倡议论战中，Whisper被引为OpenAI支持开源的具体案例。
- object_type: product
  name: Claude Fable
  canonical_name: Claude Fable
  url: null
  positioning: Anthropic推出的AI对话产品，因封号问题在开源倡议论战中备受关注，被视为闭源策略的代表性产品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 追求AI安全对齐的用户
  - 企业级AI应用开发者
  - 对话AI产品用户
  product_signal: Fable发布期间出现用户被连续封号的问题，被广泛用作Anthropic闭源策略与用户体验矛盾的例证。
  market_signal: 在开源与闭源之争白热化阶段，Fable的用户体验问题被放大为Anthropic企业立场的缩影。
  differentiation: 与签署开源倡议的公司产品相比，Fable完全闭源且账号管理策略较为严格，代表安全对齐优先的路线。
  watch_reason: 作为Anthropic的核心对话产品，Fable在开源倡议论战中持续成为舆论焦点，其产品策略和安全理念代表了一条与开源阵营截然不同的AI发展路径。
  risk_notes:
  - 连续封号问题表明产品审核机制存在缺陷，可能影响用户留存和口碑传播。
  - 完全闭源策略在开源浪潮中可能面临越来越大的舆论与竞争压力。
  score: 5.0
  article_ids:
  - f2babacf4e97c2ed
  evidence_snippets:
  - 文章提及在Anthropic的Claude Fable发布期间，部分用户遭遇了连续三次被封号的问题，引发网友对Anthropic闭源策略的广泛批评。
---

# 老黄「开源协议」就剩一家没签，是谁啊好难猜啊

Denny’s和英伟达，有一项核心业务高度重叠

Jay 发自 凹非寺

量子位 | 公众号 QbitAI


您猜怎么着？

除了Anthropic外，几乎所有人都签了老黄的开源倡议书，**包括OpenAI**。

也算顺了老黄的心愿，不枉他这几天X出道奔走呼号。

如今这盘棋，大势已定。就差最后一颗棋子：**Anthropic**。

而对此，**A社一名员工**也出面，某种程度上给出了回应——

哇哦，好棒呀，啥时候CUDA和Windows也能开源捏。


太勇了啊bro，演都不演一下，直接跟开源阵营爆了。。。

打起来，打起来！（吃瓜脸）

# 真Open·AI协议

但在正式吃瓜前，咱们先从头捋捋，这所谓的「开源倡议」到底是怎么来的。

几天前，老黄发了**人生第一条推**，附带一封公开信，全力站台开源模型。

核心逻辑很简单：开放权重模型对AI生态的健康至关重要，大家应该抱团支持。

当时第一批签了大概25家公司和机构，结果热度一起来，名单迅速扩大，现在已经到了**70多家**。

声势非常恐怖。帖子一发，杨立昆、「龙虾之父」全部现身力挺。

**微软CEO纳德拉**也亲自下场公开站台：

开放权重模型对于健康的 AI 生态系统至关重要。我们正与业内其他人士共同努力，为开放权重模型制定发展路径。


可以说是彻底引爆了舆论，现在那条帖子已经六千万阅读。

**六千万。**

你知道什么概念吗，AI圈已经很久很久没有这种量级的讨论了。

不得不说，「铲子王」还是有号召力的，一手攒起了大半个AI圈。

让咱开瓶豆汁庆祝一下！（bushi）

但真正让这出戏变得有意思的，是第二个节点。

**OpenAI，也签了。**

不er，闹呢，原来OpenAI跟Open有关系？？（doge）

老实说，尽管OpenAI没有开源旗舰大模型，他们确实发布过不少小模型，比如**Whisper、gpt-oss**之类的，这一点还是值得肯定。

反观Anthropic——

一个都没有。

**还在乐此不疲地封号。。。**

Fable发布那一波，身边有朋友已经被连续封三次了，我现在也是看到Claude就PTSD。

关键是，A社如果只是自己闷头修围墙也就算了，还多次公开引导「开源模型是危险的」，甚至呼吁限制开源模型的部署。

坏事做尽啊！！

反者道之动，如今压力终于给到Anthropic。

这份开源「英雄帖」的支持者越多，网友们对A社的不满情绪就越进一步发酵。

到了这一步，所有人的目光都盯着Anthropic，想看看他们到底什么反应。

这次也确实没当小哑巴——A社的一名员工出来回应了。

Julian Schrittwieser，Anthropic的MTS（翻译过来就是技术人员）。

别看名头好像不大，我查了一下，这哥们是真有点东西。

他在Google DeepMind待了**将近十年**，AlphaGo、AlphaZero、MuZero、AlphaProof……他全都在里面。

后来还参与了**Gemini的强化学习**。

就是这么一位大哥，周末在X上连续开麦，单枪匹马怒喷老黄和微软CEO。。。

黄哥，我太兴奋了！现在我坚信开源的力量，期待CUDA和GPU driver的开源！


嚯！纳德拉大哥也发声了，迫不及待想看到Windows和MS Office开源！


一瞬间，网友的怒火被彻底点燃。

甚至连**吴恩达**都亲自下场，为黄仁勋辩护：

这是一种错误的类比。每个人都有权不公开自己的代码。真正的问题在于，有人试图阻止其他人将代码开源。


不过，A社小哥并未退缩，仍在施展「阴阳大法」——

看到有人断定我一定是想禁止公开权重模型，真是好笑…..

我一直觉得开源模型非常有用好吗！但有趣的是，一些历史上极度反对开源的公司，现在突然都赞成开源

。


# Anthropic，全美最不吃压力之人👍。

# 这很重要吗？

到这里，你可能觉得，这不就是一个很简单的故事吗，老黄振臂一呼，全行业组成「正义联盟」，只有A社一个顽固分子在负隅顽抗还嘴臭（bushi）。

但说真的，我仔细想了想，A社的反应，并非全无道理。

开源倡议当然是好事，但关键在于——**老黄，你是真的支持「开源」吗？**

先补充一个背景：

前沿闭源模型正在加速推理芯片「去英伟达化」。

OpenAI在搞自己的芯片，内部代号「小辣椒」；Anthropic和谷歌在用TPU。

大家都想摆脱对英伟达的依赖。

但如果「开源」阵营掌握了技术话语权，这个叙事可能会彻底扭转。

开放权重模型普及后，更多企业、初创公司和机构会自行部署和运行AI模型，而非只依赖封闭API服务商。

这自然直接拉动推理算力需求。

更关键的是，这些都不是模型厂商，自然没有单独搞芯片端到端的动力，也不会有和英伟达生态切割的想法。

简单来说就是，**开源模型越多，部署越分散，英伟达的护城河越坚固**。

不过话说回来，讨论这一切的前提，还得看这份开源倡议到底有没有实际的约束力。

如果都是喊喊口号，就没必要浪费口舌在这吵来吵去了。。。

为什么大家都觉得签这个东西很重要？

估计一个月后就没人记得了吧。。。


# One More Thing

不过也无所谓了。

因为一个真正Open、并且势必将永远拥护Open协议的玩家，正在出现。

**美式连锁餐厅**Denny’s，跨行空降声援黄仁勋，表示他们和英伟达一样，坚信Open（不打烊）的重要性。

（可以理解为美国版「永和大王」，全天供应早餐/简餐、分量大、价格亲民）

好样的Denny’s，一直Open下去！

而Denny’s的「官宣」加盟，或许比老黄开源协议上那七十多家签名方，都要更加重磅。

因为有网友进一步挖掘，发现了一个令人细思极恐的细节——

Denny’s和英伟达，有一项核心业务高度重叠：

卖Chips（薯条/芯片）。

（doge）

参考链接：

[1]https://x.com/Mononofu/status/2080937562739531837

[2]https://x.com/beffjezos/status/2080858083472146656?s=20

[3]https://x.com/dennysdiner/status/2081069889931112816?s=46&t=iTysI4vQLQqCNJjSmBODPw


*版权所有，未经授权不得以任何形式转载及使用，违者必究。*