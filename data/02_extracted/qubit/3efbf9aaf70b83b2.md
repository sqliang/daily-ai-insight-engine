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