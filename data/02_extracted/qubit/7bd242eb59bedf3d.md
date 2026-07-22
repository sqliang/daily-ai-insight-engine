---
title: 不同模型厂同一家Agentic Infra，AGI时代的地基终于浮出水面
source: https://www.qbitai.com/2026/07/455805.html
author:
- '[[克雷西]]'
published: '2026-07-20'
created: '2026-07-21'
manifest_dates:
- '2026-07-21'
description: 大模型时代的共同选择
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7bd242eb59bedf3d
source_type: news_media
tldr: 无问芯穹成为Kimi、智谱、MiniMax、阶跃星辰四家国产头部大模型公司的共同AI Infra合作伙伴，其Agentic MaaS平台日均Token调用量半年增长40倍。公司发布跨集群异构PD分离架构和智算集群运维智能体系统等核心技术，已部署触及37000P算力并覆盖16种主流芯片。
objective_summary: 无问芯穹在2026年WAIC上宣布与MiniMax签署战略合作，并邀请阶跃星辰发表主旨演讲，此前已为Kimi和智谱提供AI Infra服务，成为四家不同国产大模型公司的共同选择。该公司发布跨集群异构PD分离架构，实测首Token延迟降低51.5%、单Token成本降低37.5%，同时推出智算集群运维智能体系统实现故障自愈。截至2026年7月，其Agentic
  MaaS平台日均Token调用量较去年12月增长40倍，已部署37000P算力并覆盖16种主流芯片。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - 无问芯穹
  - MiniMax
  - 阶跃星辰
  - 智谱
  - Kimi
  - 上海移动
  - 观猹
  technologies:
  - Agentic Infra
  - Agentic MaaS
  - PD分离
  - PDD架构
  - KV Cache
  - Radix Cache
  - 跨集群强化学习
  - Token工厂
  key_people:
  - 张鹏
  - 杨植麟
key_logic_flow:
- 无问芯穹已与四家国产头部大模型公司（Kimi、智谱、MiniMax、阶跃星辰）达成深度合作，成为多家不同模型厂商共同选择的AI Infra基础设施供应商。
- 2026年推理需求超过训练成为AI算力消耗主战场，中国日均Token调用量突破140万亿，但算力供给仍呈线性增长，形成供需缺口。
- 无问芯穹发布跨集群异构PD分离架构，将Prefill和Decode拆解部署，首创PDD三级链路（P、RelayDecode、MainDecode）解决广域网传输延迟问题。
- 无问芯穹推出智算集群运维智能体系统，实现7×24小时全天候值守和故障自愈，运维人效提升5倍以上、关键故障处理效率提升6倍。
- 无问芯穹构建"前店后厂一中心"体系：算力集散中心（Agentic Infra平台，37000P算力、16种芯片）、Token工厂（Agentic MaaS平台）和AI生产力商店（行业解决方案）。
- 无问芯穹实现了跨集群强化学习连续一周0中断稳定运行，并计划将跨域计算资源支撑规模拓展至十万卡以上。
object_mentions:
- object_type: product
  name: Agentic Infra 自主式基础设施平台
  canonical_name: 无问芯穹 Agentic Infra
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 一中心指的是「算力集散中心」，即Agentic Infra自主式基础设施平台，核心目标是实现智能资源规模最大化。
  - 这个集散中心已部署触达37000P算力，覆盖接入16种主流芯片。
  - 无问芯穹实现了跨集群强化学习连续一周0中断稳定运行，并计划拓展至十万卡以上规模。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: Agentic MaaS 大模型服务平台
  canonical_name: 无问芯穹 Agentic MaaS
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 后厂也就是「Token工厂」，即Agentic MaaS大模型服务平台，核心思路是「在规模之上向效率要产能」。
  - 截至7月，无问芯穹Agentic MaaS平台的日均Token调用量，较去年12月涨了40倍。
  article_id: 7bd242eb59bedf3d
- object_type: project
  name: 跨集群异构PD分离架构
  canonical_name: 跨集群异构PD分离架构
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 无问芯穹在今年WAIC官宣了一项自研的硬技术——跨集群异构PD分离，把Prefill和Decode拆开部署让不同芯片干各自最擅长的事。
  - 无问芯穹首创PDD架构，把传统PD链路拆成P、RelayDecode、MainDecode三级，解决了广域网传输延迟问题。
  - 实测该架构在首Token延迟降低51.5%的同时，单Token成本可降低37.5%。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: 智算集群运维智能体系统
  canonical_name: 智算集群运维智能体系统
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 无问芯穹这次发布了「智算集群运维智能体系统」，能够端到端地解决实际生产场景中的运维难题。
  - 该系统实现7×24小时全天候值守，运维人效提升5倍以上，关键故障处理效率提升6倍。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: 天问模型服务门户
  canonical_name: 天问
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 无问芯穹与上海移动联合打造了「天问」模型服务门户，作为面向企业用户的模型服务入口。
  article_id: 7bd242eb59bedf3d
- object_type: product
  name: TokenDance
  canonical_name: TokenDance
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 无问芯穹联合观猹做了一个面向开发者的「TokenDance」，对标OpenRouter。
  article_id: 7bd242eb59bedf3d
extract_result: success
---

# 不同模型厂同一家Agentic Infra，AGI时代的地基终于浮出水面

大模型时代的共同选择

##### 克雷西 发自 上海

量子位 | 公众号 QbitAI

先说一件有意思的事。

就在今天的WAIC论坛上，MiniMax和阶跃星辰，同时出现在了一家AI Infra公司的论坛现场，前者参加战略合作签约，后者发布主旨演讲。

苗头其实更早就出现了。4个月前的中关村论坛上，智谱张鹏和Kimi杨植麟就曾与这家公司联合创始人兼CEO同框，参与圆桌论坛，并被现场点名该公司已为Kimi、智谱提供服务。

四家国产头部基模公司，先后跟同一家AI Infra达成了深度合作。开句玩笑话——集齐四家，就可以召唤神龙了。

这家AI Infra公司，正是**无问芯穹**。

这个身位有点像「电池领域的宁德时代」——造车的人可以「兄弟登山，各自努力」，但电池这一层，绕不开就是绕不开。无问芯穹想做的，就是**大模型时代的共同选择**。

问题也因此变得更有趣了：

他们到底看中了这家公司什么？

答案要从两头找。

**需求端**，2026年推理开始反超训练，成为AI算力消耗的主战场，推理成本两年降了280倍，企业的AI总支出却没降反升，中国日均Token调用量已经突破140万亿，一年涨了四成，需求呈指数级往上冲。

**供给端**却完全是另一副面孔。物理算力的扩产逻辑还是线性的，多修几个机房、多买几张卡，缺口却在三五年内都填不平。

一边指数增长，一边线性爬坡，中间那道口子，就是无问芯穹想站进去的位置。

更难的是，模型部署得好不好，外人很难判断。

一个请求发下去，模型正常回复了，但输出的精度可能已经悄悄掉了三成，这种问题常规监控查不出来。

等到用户在业务里察觉到不对劲，模型的招牌已经砸了。

这道看不见的门槛，才会真正决定哪家供应商能留在牌桌上。

## 为什么国产大模型优选无问芯穹？

Token经济全面爆发以来，推理需求正在加速，算力缺口也在持续扩大。

但MaaS这门生意的门槛，比外界想象的高得多。

Kimi、智谱、MiniMax、阶跃星辰为什么都点了头，自然有他们自己的算盘，但本质上是同时把三件事押了上去——

**比如：模型效果会不会打折，成本烧不烧得起，出了问题稳不稳得住。**

先说**效果**。

前面提到的那种隐蔽滑坡，是这个行业最让人头疼的地方。

有第三方供应商部署模型后，精度比原厂掉了30%，客户自己甚至察觉不到，直到业务指标开始下滑才回头排查。

无问芯穹在这件事上的做法，是定了一套准入测试标准。

这套标准，会从工具调用的一致性，到推理模式的精度对齐，逐项进行核验，每一个新模型上架前都要过这道关。

结果是，客户无论走无问芯穹还是原厂API，体验几乎感觉不到差别。

再来是**成本**。

无问芯穹在今年WAIC官宣了一项自研的硬技术——跨集群异构PD分离。

大模型推理里的Prefill和Decode是两个负载完全不同的阶段，硬件需求也不一样，拆开部署能让不同类型的芯片各自干最擅长的事。

但拆到不同机房后，会撞上一个新问题。

PD分离之后，需要在异构芯片之间用广域网以太网传输KV Cache，面临着带宽低、延迟高的情况，等于两个接力选手各自都跑得很出色，但在交棒的时候，却掉了链子。

为此，无问芯穹首先把Decode实例设计的Radix Cache技术，创新性地迁移到了这套跨集群架构里，让传输的数据量直接降低一个数量级。

接着，他们又首创了PDD架构，把传统的PD链路拆成P、RelayDecode、MainDecode三级。

遇到传输延迟高的请求，RelayDecode先顶上去把Token吐给用户，用户完全感觉不到这段实际长达数十秒的延迟，等数据传完，再无缝切给MainDecode接手。

实测显示，该架构在首Token延迟（TTFT）降低51.5%的同时，单Token成本可降低37.5%。

最后是**稳定性**。

集群规模一大，故障往往藏得很深。

大模型推理背后要管理数十上百个集群，扛住全国每天上T规模的流量分发，服务器一旦宕机，靠人盯着屏幕根本来不及反应。

无问芯穹这次发布了“智算集群运维智能体系统”，能够端到端地解决实际生产场景中的运维难题，7×24小时全天候值守，让智算集群的运维从“人找问题”转变为“问题找人”，和“问题自己解决”，实现了运维人效提升5倍以上，关键故障处理效率提升6倍。

## 前店后厂一中心，构建系统竞争力

三件事都解决了，仅仅只是构成了Token工厂这一层的地基。

无问芯穹真正要交出去的答卷，是把算力、Token、生产力串成一个完整的系统，对应它自己提出的那个公式——

**AI生产力 = 智能资源规模 × Token转化效率 × AI生产力转化效率。**

一中心，指的是**「算力集散中心」**，即Agentic Infra自主式基础设施平台。

国产芯片生态天然碎片化，无问芯穹把散落各处的算力资源统一汇聚、弹性调度、按需利用，为模型与应用层筑牢充足、稳定、可扩展的算力底座。核心目标非常明确：实现智能资源规模最大化。

这个集散中心已部署触达**37000P算力**，覆盖接入**16种主流芯片**。

跨集群强化学习的挑战，同样是在这一层被啃下来的。无问芯穹认为，在Post-training的Scaling Law持续发展的当下，强化学习成为解锁智能的关键。

其算力需求的硬件种类更加复杂，规模量级也更加庞大，基于异构和超大算力规模的双重刚需，跨集群强化学习因此成为智能规模化及持续进化的新锚点，这也是无问芯穹Agentic Infra自主式基础设施平台重点布局与攻克的核心场景。

无问芯穹把网络、平台、框架三层的优化贯穿到底，成功实现了跨域强化学习训练连续一周0中断稳定运行，让大规模跨域强化学习不仅可以“跑得通”，还能“跑得快、跑得稳”。

未来，无问芯穹还将针对并行策略、通信融合、智能算子、极致容错等核心技术持续深耕，将跨域计算资源的支撑规模，持续拓展至十万卡级以上。

后厂，也就是**「Token工厂」**，即Agentic MaaS大模型服务平台。

这是前面讲的效果、成本、稳定性三重优势真正兑现的地方，核心思路是“在规模之上向效率要产能”，也是一整套从网关、路由到底层推理实例的完整服务技术栈，“层层可优化、处处有增量”。

在这个「工厂」里，除了上文提到的新技术“跨集群异构PD分离架构”，无问芯穹还和多家头部大模型公司深度合作，在真实业务场景里持续打磨推理效率和服务稳定性，业务规模又反过来推动技术迭代得更快。

公司官宣：截至7月，无问芯穹Agentic MaaS平台的日均Token调用量，较去年12月涨了40倍。

它还与上海移动联合打造了“天问”模型服务门户，联合观猹做了一个面向开发者的「TokenDance」，对标OpenRouter。

前店，是把攒下的能力覆盖千行百业的**「AI生产力商店」**，即Agentic Infra行业解决方案。

这套解决方案已覆盖文娱游戏、医疗健康、法律终端、能源电力等多个行业领域，把技术势能全面转化为各行业能用、好用、可复用的落地价值。