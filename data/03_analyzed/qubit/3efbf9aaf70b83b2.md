---
title: 源神启动！一张消费级显卡跑“Opus级”Agent，Qwen3.8-27B多项榜单反超Claude
source: https://www.qbitai.com/2026/08/473669.html
author:
- '[[梦瑶]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
- '2026-08-16'
- '2026-08-17'
description: 推理能力还能自定义
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3efbf9aaf70b83b2
source_type: news_media
tldr: 阿里通义团队正式开源 Qwen3.8-27B，总参数 270 亿，官方 Benchmark 显示其在 SWE-bench Pro、QwenSWEBench
  等多项编码与 Agent 评测中反超 Claude Opus 4.6 Max；模型支持原生多模态、262K 上下文，量化后可在 24GB 显存消费级显卡本地部署。
objective_summary: 2026 年 8 月，阿里通义团队正式开源 Qwen3.8-27B 模型，总参数 270 亿。官方 Benchmark 显示其在
  SWE-bench Pro 上以 8.3 分、QwenSWEBench 上以 15.2 分反超 Anthropic 的 Claude Opus 4.6 Max，OSWorld-Verified、AndroidWorld
  等 Agent 评测也全面领先。模型原生支持多模态、262K 上下文并可扩展至 100 万 Token，内置 reasoning_effort 推理档位与 preserve_thinking
  长任务功能，量化后可在 24GB 显存消费级显卡上本地部署。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Alibaba
  - Anthropic
  technologies:
  - Qwen3.8-27B
  - Gated DeltaNet
  - reasoning_effort
  - preserve_thinking
  - SWE-bench Pro
  - QwenSWEBench
  - OSWorld-Verified
  - AndroidWorld
  - WebArena-Verified
  - CoWorkBench
  - FP8
  key_people: []
key_logic_flow:
- 阿里通义团队正式开源 Qwen3.8-27B，总参数量 270 亿，支持原生多模态、262K 原生上下文并可扩展至 100 万 Token，量化后可装入 24GB
  显存的消费级显卡。
- 官方 Benchmark 显示其在 SWE-bench Pro 上以 8.3 分、QwenSWEBench 上以 15.2 分反超 Claude Opus 4.6
  Max，Agent 评测中 CoWorkBench 也以 70.7 分超过后者的 68.2 分。
- 在多模态与电脑操作评测中，OSWorld-Verified 达到 84.3 分、AndroidWorld 达到 81.9 分，均明显高于 Claude Opus
  4.6 Max。
- 模型内置推理档位 reasoning_effort，分为 xhigh、medium、low 三档，并默认开启 preserve_thinking 以在长程 Agent
  任务中保留思考过程。
- 架构上采用 64 层设计，其中 48 层为 Gated DeltaNet 线性注意力、16 层为完整 Attention，用于降低长序列下的计算与缓存压力。
object_mentions:
- object_type: model
  name: Qwen3.8-27B
  canonical_name: Qwen3.8-27B
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 阿里通义团队正式开源 Qwen3.8-27B，总参数量 270 亿，支持原生多模态与 262K 原生上下文并可扩展至 100 万 Token。
  - 在官方 SWE-bench Pro 编程评测中，Qwen3.8-27B 以 8.3 分优势反超 Claude Opus 4.6 Max。
  - Qwen3.8-27B 内置 reasoning_effort 推理档位，支持 xhigh、medium、low 三档调节推理深度。
  article_id: 3efbf9aaf70b83b2
- object_type: model
  name: Claude Opus 4.6 Max
  canonical_name: Claude Opus 4.6 Max
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Qwen3.8-27B 在 SWE-bench Pro、QwenSWEBench 及多项 Agent 评测中均超过 Anthropic 的 Claude Opus
    4.6 Max。
  - 在电脑操作评测 OSWorld-Verified 中，Claude Opus 4.6 Max 得分为 72.7，低于 Qwen3.8-27B 的 84.3。
  article_id: 3efbf9aaf70b83b2
- object_type: project
  name: QwenSWEBench
  canonical_name: QwenSWEBench
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在更考验真实软件工程能力的 QwenSWEBench 评测中，Qwen3.8-27B 领先 Claude Opus 4.6 Max 达 15.2 分。
  article_id: 3efbf9aaf70b83b2
- object_type: model
  name: Qwen3.8-27B-FP8
  canonical_name: Qwen3.8-27B-FP8
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 有网友将 Qwen3.8-27B-FP8 部署到单张 NVIDIA GH200 上，同时跑 10 个真实请求，首批流式 Token 基本在 10ms 内返回。
  article_id: 3efbf9aaf70b83b2
extract_result: success
impact_score:
  score: 7.5
  reason: 首先，这是一款可在 24GB 显存消费级显卡本地部署的 27B 开源模型，官方榜单显示其在 SWE-bench Pro、QwenSWEBench
    等编码与 Agent 评测中反超 Claude Opus 4.6 Max，直接冲击了'Opus 级能力只能由云端闭源旗舰提供'的既有认知，改变了本地部署的性价比曲线，对闭源
    API 商业模式形成实质压力。其次，Qwen 系列在开源社区影响力极大，27B 这个'黄金尺寸'叠加原生多模态与 262K 上下文，具备快速扩散和生态沉淀的基础，短期内会引发大量部署与二次开发。但需注意三点扣分：官方
    Benchmark 为厂商自报，缺少第三方独立复现；对比基准是闭源旗舰而非同量级开源对手，口径上存在优势放大；且这属于 Qwen3.8 系列的迭代演进而非全新范式，未达到
    ChatGPT 发布级别的范式转移。综合判定 7.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 能否在消费级硬件上真实复现接近 Opus 的编码与长程 Agent 能力，而非仅停留在厂商自报榜单
hype_assessment:
  level: medium
  reason: 文章标题与正文高频使用'反超 Claude''Opus 级''消费级显卡跑旗舰'等强传播话术，存在明显的 PR 包装痕迹；核心榜单为阿里官方自报数据，且对比对象选择闭源旗舰而非同量级开源模型，缺少第三方复现佐证，属于'选择性呈现'；'消费级显卡'实际需要
    RTX 3090/4090 这类 24GB 显存旗舰卡并依赖量化部署，与大众理解的入门消费级有差距，存在一定夸张。但模型本身真实开源、架构有实质创新（Gated
    DeltaNet 线性注意力混合设计），社区已有多方实测佐证其可用性，并非空穴来风的概念炒作，故判定为中等水分。
information_entropy: high
domain_disruption:
  technical_innovation: 混合线性注意力架构创新——64 层中以 3:1 节奏循环部署 48 层 Gated DeltaNet 线性注意力与
    16 层完整 Attention，在保持全局信息交互能力的同时大幅降低长序列下的计算量与 KV Cache 压力，使 27B 模型在消费级硬件上支撑 262K
    原生上下文并可扩展至百万 Token 成为现实；配合 reasoning_effort 三档推理深度调节与默认开启的 preserve_thinking 长程决策保留机制，实现了从推理成本弹性可控到
    Agent 长任务记忆延续的系统级优化，这是小尺寸模型逼近闭源旗舰的关键工程路径。
  business_model: 对闭源 API 按 token 计费的商业模式形成直接冲击：若自报榜单经社区复现成立，大量编码、Agent 与专业工作负载可从按调用付费的闭源
    API 迁移到本地/私有化部署，压缩闭源模型在开发者工具链中的定价空间与议价能力；同时反向催生消费级推理优化（量化、FP8）与开源模型托管服务的商业化机会，推动'本地算力
    + 开源权重'成为企业对私数据场景的默认选项。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 评分逻辑：先验证复利来源是否成立。正面证据——(1) 27B 参数量在 SWE-bench Pro、QwenSWEBench、OSWorld-Verified、AndroidWorld、CoWorkBench
    等 Agent/编码/多模态评测中反超 Claude Opus 4.6 Max，且 FP8 量化后可装入 24GB 显存消费级显卡，意味着'Opus 级 Agent
    能力'首次实现零 API 成本本地运行，这是对 Agent 成本曲线的结构性下移而非单点波动；(2) 262K 原生上下文 + 可扩展百万 Token +
    原生多模态 + preserve_thinking + reasoning_effort 三档推理控制，说明它不是阉割版，而是完整的长程 Agent 底座，下游量化工具、推理引擎、Agent
    框架会围绕这一能力等级长期沉淀；(3) 对阿里而言，每次开源都强化 Qwen 生态位并拉动阿里云推理与训练需求，具备平台级复利效应。反向因素——开源模型迭代极快，Qwen
    自身约 3-6 个月即发新版本，27B 这个具体权重文件 1-2 年内就会被自家下一代替换，单体模型护城河极短，真正的复利沉淀在'开源本地 Agent 底座'这一品类而非某个权重。综合判断：该事件永久重置了本地
    Agent 的能力/成本门槛，具备成为细分赛道基础设施的潜力，但需持续验证其生态地位能否穿越下一代模型迭代，故给 7.5 而非更高。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Alibaba
- Alibaba Cloud
- NVIDIA
- Hugging Face
- Ollama
- vLLM
competitive_casualty:
- Anthropic
- OpenAI
- 闭源模型 API 服务商
market_opportunities:
- 建议创业团队基于 Qwen3.8-27B 开发本地私有化部署的编码 Agent 产品，面向数据敏感型企业与个人开发者提供不依赖 API 调用、成本更低的编程助手，抢占
  24GB 消费级显卡的本地推理市场
- 可围绕 reasoning_effort 推理档位设计按推理深度分级的智能调度产品，自动为简单问答与复杂长程 Agent 任务匹配不同推理档位，在保证效果的同时显著降低推理成本
- 关注面向该模型的量化部署工具链机会（FP8 量化、KV Cache 优化、长上下文裁剪），27B 级别开源模型的生态化部署工具将形成新的中间件创业窗口
risk_matrix:
  regulatory: 开源模型合规与跨境监管风险：Qwen 系列模型在部分国家可能面临出口管制或使用限制，且中美 AI 治理博弈可能影响阿里后续开源策略的稳定性；企业部署前需核查模型许可条款与所在地区数据合规要求
  technological: 官方 Benchmark 均为厂商自报，缺少第三方独立验证，存在榜单过拟合与评测口径偏差风险；Gated DeltaNet 线性注意力混合架构在真实超长上下文（262K+）下的稳定性尚需社区大规模复现验证
  competitive: 开源赛道迭代极快，DeepSeek、Llama、Mistral 等同级模型竞相发布，27B 的榜单优势可能被迅速追平甚至反超；Anthropic/OpenAI
    等闭源厂商也可能针对性推出新版本压缩其性价比优势
  ethical: 原生多模态能力增强深度伪造与信息操纵风险，开源权重可被随意二次分发、滥用行为难以追溯；'反超 Opus'等营销表述可能引发对单一基准的过度依赖与误判
  additional:
  - 厂商榜单存在选择性展示嫌疑（如 CI 开启前后的不对称对比），建议独立复现核心评测后再做采购与技术选型决策
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: QwenSWEBench
  canonical_name: QwenSWEBench
  url: null
  positioning: QwenSWEBench 是 Qwen 团队提出的软件工程能力评测基准，侧重考察模型在真实软件工程任务中的实战表现，用于衡量编程与 Agent
    模型的工程能力。
  technical_signal: 该基准聚焦真实软件工程场景的评测，区别于一般编程题目，能更直接反映模型在工程任务中的落地能力。
  adoption_signal: Qwen 官方将其作为核心评测榜单，用于对外展示 Qwen3.8-27B 在软件工程任务上领先 Claude Opus 4.6
    Max 15.2 分的表现。
  ecosystem_relevance: 该基准服务于 Qwen 开源模型生态，为本地可部署的小尺寸模型提供对标闭源旗舰的工程能力参照坐标。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: QwenSWEBench 作为反映真实软件工程能力的评测基准，其口径可用于追踪 Qwen 开源系列与闭源旗舰模型在编码与 Agent
    场景的差距变化，且随 Qwen3.8 系列持续发布而不断被引用，值得长期跟踪。
  risk_notes:
  - 该基准出自模型开发方 Qwen 团队自身，榜单结果可能存在评测口径偏向，缺乏第三方独立复现验证。
  - 目前仅在单篇文章中被提及，作为次要引用对象，其评测方法与样本覆盖面尚未获得广泛第三方采用证据。
  score: 5.0
  article_ids:
  - 3efbf9aaf70b83b2
  evidence_snippets:
  - 在更考验真实软件工程能力的 QwenSWEBench 评测中，Qwen3.8-27B 领先 Claude Opus 4.6 Max 达 15.2 分。
  - 在编程评测SWE-bench Pro里，Qwen3.8-27B比Claude Opus 4.6 Max高出8.3分；到了软件工程评测 QwenSWEBench，领先幅度进一步拉到15.2分。
---

# 源神启动！一张消费级显卡跑“Opus级”Agent，Qwen3.8-27B多项榜单反超Claude

推理能力还能自定义

# 梦瑶 发自 凹非寺

# 量子位 | 公众号 QbitAI

狂喜～开发者苦等已久的**Qwen3.8-27B**终于开！源！了！

270亿的总参数量，在官方Benchmark多项软件工程和Agent评测中的表现吧，多少又有点让Claude《危》了——

Agent编程评测SWE-bench Pro上，27B以8.3分的优势卷超**Claude Opus 4.6 Max**。

到了更考验真实软件工程能力的QwenSWEBench，甚至领先幅度进一步扩大到15.2分：

尺寸虽小，参数配置和模型表现配的可不孬——

**原生多模态、262K原生上下文、最高100万Token扩展，重点强化的Coding、专业工作和长程Agent能力**，也一项没落下。

好东西大家自然都想尝鲜一番！！

这不嘛，已经有一大波网友开始大roll特roll了。

下面这老哥用3.8-27B和3.6-27B分别做了个像素风宝塔效果，3.8-27B在色彩细节和主体结构明显更next level～

还有网友用Qwen3.8-27B做的俄罗斯方块——

甚至连空格键掉落时的屏幕抖动、消除行时出现的奖励倍增器效果也都是模型自己添加的：

甚至还有网友说：好啊好啊，那这意思是，差不多咱以后可以在本地跑「Opus级」模型了！？

Qwen这模型，多少还是有点说法的。。。

# 270亿参数，代码和Agent多项榜单超过Opus 4.6 Max

Qwen3.8这一代，说实话最近上新速度属实有点快。。。

而且这只27B，开发者友友们其实已经蹲挺久了。

正式开源之前社区里的《催更》就没怎么停过，也有不少人直接把它列进这一轮Qwen3.8里最值得等的开源版本。

大家之所以这么惦记，一个特别现实的原因就是——这回，自家电脑真有机会带得动了。（doge）

毕竟——总参数量就**「270亿」**。

换句话说，经过量化之后24GB显存的RTX 3090、4090这类显卡，都有机会把模型整卡装下～

尺寸下来了，上下文长度倒是一点没跟着缩水，**原生支持262K Token上下文，还可以继续扩展到100万Token。**

具体到干活场景，这一代27B重点强化的方向也很明确：

**编程、专业工作、研究以及长程Agent任务，**基本都是现在开发者最常拿模型狠狠干活的地方。

但！这里我特别想单独拎出来说一个能力——

**「原生多模态」**。

需要给友友们划个重点，Qwen3.8-27B本身就带视觉理解和解析能力。

意思就是，它除了读文字、啃代码，还能直接看图片、读PDF文档、理解图表，甚至处理视频！！！（欢呼.jpg）

尺寸够小，能往本地塞，上下文够长，能吃大工程，多模态和Agent能力又都保留了。

至于这些本事到底练到什么程度，官方榜单已经给出了一波答案。

咱们先从最适合拿来干活的两项看——**代码和Agent**。

在编程评测SWE-bench Pro里，Qwen3.8-27B比Claude Opus 4.6 Max高出8.3分；到了软件工程评测 QwenSWEBench，领先幅度进一步拉到15.2分。

Agent评测中面向计算机、金融、法律、医疗等专业长任务的CoWorkBench达到70.7分，也超过Opus 4.6 Max的68.2的成绩——

再看**多模态能力**这边，模型能力提升表现甚至更集中。

在电脑操作评测OSWorld-Verified中，Qwen3.8-27B拿到84.3分，Opus 4.6 Max是72.7。（给到Claude一个拉！）

手机操作评测AndroidWorld中，Qwen3.8-27B达到81.9分，Opus 4.6 Max是62.0，浏览器操作WebArena-Verified，则从上一代的48.8提升到了64.8——

通用多模态智能这边，也有几项维度我们可以一起看一下。

在**视觉数学问题解决能力**上，开启CI后，Qwen3.8-27B拿到94.6分，是图里这一排可见模型中的最高成绩，这类任务不只是识别图片里的字，还得把图形、公式、空间关系一起理解。

在**通用视觉推理**方面，Qwen3.8-27B开启CI后做到85.6分，相比不开CI时的65.7提升非常明显，它更偏向考模型面对普通视觉场景时，能不能从「看见东西」进一步走到「理解关系、做判断」。

这成绩也说明这代27B模型在看图、读文档和视觉推理这些任务上，模型覆盖的场景和性能表现更多更强～

好东西大家自然要一试，这不嘛，各方网友大神已经开始集体研究「这小27B模型到底该怎么跑」了。（doge）

比如下面这位友友用Qwen3.8-27B做了一个贪吃蛇游戏后，直言感觉像拥有了一个Opus级别的Agent——

还有网友直接把Qwen3.8-27B-FP8放到一张NVIDIA GH200上实测，同时跑10个真实请求，每个最高输出16K Token、上下文拉到262K。

结果首批流式Token基本都在10ms内返回，10个请求也全部正常完成，高并发和长上下文下的运行稳定性确实夯：

还有网友直言模型的多模态理解能力也非常不错。

一次性丢给它一部1935年的11分钟电影，让模型识别其中96个带时间戳的事件并逐字引用画面文字。

最终157秒完成，时间点对应到具体画面时，整部片子的误差大约只有2秒，而且是在单张GPU上跑完：

只能说，还是那个Qwen，还是不负众望啊。。。

# 从Thinking推理档位到上下文理解，27B还有这些功能

除了前面这些榜单表现，Qwen3.8-27B这次还有一个很实用的变化。

那就是模型到底要「想多久」，我们现在可以自己手动调了，因为27B里内置了个**「推理档位」**——

模型默认开启Thinking模式，同时支持reasoning_effort调节推理深度，一共分成xhigh、medium和low三档。

复杂代码、长程Agent这类任务可以把档位拉高；简单问答、摘要、轻量任务则可以降下来，优先换速度和成本。

此外Thinking本身也能直接关闭，让模型跳过推理过程直接回答，真diy私人定制了。

此外在长任务这件事上，还有一个挺实用的功能——Qwen3.8-27B默认开启了**preserve_thinking**。

简单说，就是Agent前几轮「怎么想的」可以继续留在后面的上下文里。

比如Coding Agent连续改十几个文件，做到后面时还能沿着前面的决策继续走，少一点每轮重新捋思路的重复劳动，同时也能更好利用KV Cache。

小小的身形，想把长任务稳稳扛住，底层架构也得下点功夫。

具体来说Qwen3.8-27B一共64层，其中48层采用Gated DeltaNet线性注意力，16层保留完整Attention，基本按照「三层线性注意力+一层完整Attention」的节奏循环。

**线性注意力负责降低长序列下的计算和缓存压力，完整Attention则隔几层做一次更充分的信息交互。**