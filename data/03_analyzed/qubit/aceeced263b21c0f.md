---
title: 全球首个Agentic扩散模型来了：边行动边纠错，128K上下文追平自回归
source: https://www.qbitai.com/2026/07/461650.html
author:
- '[[鹭羽]]'
published: '2026-07-28'
created: '2026-07-28'
manifest_dates:
- '2026-07-28'
description: 扩散模型首次打通长程Agent任务
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aceeced263b21c0f
source_type: news_media
tldr: 蚂蚁集团旗下 inclusionAI 团队开源 LLaDA2.2，这是全球首个千亿参数 MoE 扩散语言模型，原生支持 128K 上下文，首次将 Levenshtein
  编辑与强化学习引入扩散模型 Agent 系统，在七大 Agent 基准上平均分 53.83，逼近顶尖自回归模型 Ling-2.6-flash 的 55.74。
objective_summary: 蚂蚁集团 inclusionAI 团队于 2026 年 7 月开源了 LLaDA2.2 模型。该模型采用千亿参数 MoE 架构，原生支持
  128K 上下文，是全球首个大规模 Agentic 扩散模型。团队通过 Levenshtein 编辑范式（支持 KEEP/SUBSTITUTE/DELETE/INSERT
  四种原子操作）、L-EBPO 强化学习方法（基于环境反馈自主决策编辑位置）以及 BlockRouting 机制（降低 MoE 推理通信开销）三项技术，使扩散模型首次具备能胜任长程
  Agent 任务的能力。在七大 Agent 基准测试中，LLaDA2.2-flash 平均得分 53.83，与顶尖自回归模型 Ling-2.6-flash 的
  55.74 差距缩小至 2 分以内，并在 τ²-Bench、PinchBench、MCP-Atlas 三项交互式任务上实现反超。BF16 平均吞吐量可达 Ling-2.6-flash
  的 1.64 倍，FP8 量化后可再提升 18.6%。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Ant Group
  - inclusionAI
  technologies:
  - Diffusion Model
  - Mixture of Experts (MoE)
  - Levenshtein Editing
  - L-EBPO
  - BlockRouting
  - Reinforcement Learning
  key_people: []
key_logic_flow:
- 蚂蚁集团旗下 inclusionAI 团队发布了 LLaDA2.2，这是全球首个千亿参数 MoE 扩散语言模型，原生支持 128K 上下文，使扩散模型首次进入智能体长程任务领域。
- LLaDA2.2 采用 Levenshtein 编辑范式，在块内支持 KEEP（保留）、SUBSTITUTE（替换）、DELETE（删除）、INSERT（插入）四种原子操作，使模型可以在生成过程中自我增删和动态修正，解决了传统扩散模型结构刚性的问题。
- 团队提出 L-EBPO 方法，将多轮交互中的 Levenshtein 编辑决策建模为强化学习问题，让模型能够根据环境反馈自主决策编辑位置并评估修正效果。
- LLaDA2.2 通过渐进式长上下文训练将上下文窗口从 8K 扩展至 128K，并引入 BlockRouting 机制在 block 层筛选固定专家池以降低 MoE
  推理的 HBM 流量和通信开销。
- 在七大 Agent 基准测试中，LLaDA2.2-flash 平均得分 53.83，与 Ling-2.6-flash 的 55.74 差距缩小到 2 分以内，并在
  τ²-Bench、PinchBench、MCP-Atlas 三项交互式任务上实现反超。
object_mentions:
- object_type: model
  name: LLaDA2.2
  canonical_name: LLaDA2.2
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 蚂蚁旗下 inclusionAI 团队陆续推出 LLaDA 系列模型，最新开源 LLaDA2.2，实现扩散模型首次进入智能体长程任务。
  - LLaDA2.2 是一款千亿参数的 MoE 扩散语言模型，原生支持 128K 上下文，也是全球首个大规模 Agentic 扩散模型。
  - 在七大 Agent 基准上，LLaDA2.2-flash 平均分为 53.83，BF16 平均吞吐量可达 Ling-2.6-flash 的 1.64 倍。
  article_id: aceeced263b21c0f
- object_type: model
  name: LLaDA2.1
  canonical_name: LLaDA2.1
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - LLaDA2.1 引入 Token-to-Token 编辑机制，可以在生成过程中判断哪些 Token 应该保留、哪些需要替换。
  - LLaDA2.1 进一步证明扩散模型边写边改的可用性，为 LLaDA2.2 的 Agent 能力奠定了基础。
  article_id: aceeced263b21c0f
- object_type: model
  name: LLaDA2.0
  canonical_name: LLaDA2.0
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - LLaDA2.0 首先解决的是规模化问题，证明扩散模型能够与 MoE 等架构结合并真正落地工程。
  - LLaDA2.0 是 LLaDA 系列从 2.0 时期规模化尝试到智能体觉醒的关键第一步。
  article_id: aceeced263b21c0f
extract_result: success
impact_score:
  score: 7.5
  reason: 评分依据：这是扩散架构首次以千亿参数规模进入长程 Agent 任务领域，在七大 Agent 基准上把与顶尖自回归模型的差距缩小到 2 分以内，并在三项交互式任务上实现反超，同时提供
    1.64 倍吞吐和 FP8 量化的效率证据，具备动摇'Agent 底座只能是自回归'这一行业默认假设的潜力，属于能改变局部竞争格局的架构级突破。但模型平均分仍落后顶尖自回归基线约
    2 分，尚未全面胜出，且来自单一研究团队的一次发布，未达到 ChatGPT 级别的范式转移冲击力，故评 7.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 非自回归架构能否在真实 Agent 负载中兑现 1.64 倍吞吐优势，并将与自回归模型的能力差距从'追平'推进到'反超'
hype_assessment:
  level: medium
  reason: 识别到'全球首个''追平自回归''一刀切'等强 PR 措辞：'追平'实为平均分仍落后约 2 分、仅三项交互任务反超，'一刀切'更是夸大。但核心三项技术（Levenshtein
    编辑、L-EBPO、BlockRouting）有清晰机制说明，SWE-bench Verified 上单开 Levenshtein 编辑即 +8.6 分的消融结果与七大基准的对比数据均可交叉验证，属实质进展伴随适度包装，故判定为中等炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 首次把 Levenshtein 编辑范式（KEEP/SUBSTITUTE/DELETE/INSERT 四种原子操作）大规模集成进扩散模型去噪过程，使模型在块内具备自我增删与动态修正能力；并以
    L-EBPO 强化学习将编辑决策与环境反馈闭环，针对性解决长程交互中的错误固化与模型崩溃问题；BlockRouting 通过块级固定专家池加 Token 级路由，把
    MoE 激活专家上限恒定化，降低 HBM 流量与通信开销，使 128K 原生上下文在非自回归架构上具备工程可行性。
  business_model: 以开源方式向自回归模型在 Agent 底座的主导地位发起挑战，蚂蚁借 inclusionAI 输出技术影响力并卡位下一代架构。若
    1.64 倍吞吐优势在真实高并发 Agent 场景兑现，将直接拉低 Agent 推理的单位算力成本，可能重塑 Agent 应用的部署形态与定价结构，并推动推理成本敏感场景（实时交互、规模化工具调用）向非自回归底座迁移。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 该事件验证了扩散模型在长程 Agent 任务上逼近自回归模型的可行性，且 BF16 吞吐量达到 Ling-2.6-flash 的 1.64 倍、FP8
    再提升 18.6%，具备根本性的推理经济性优势——这在 Agent 规模化部署时代是关键成本变量。LLaDA 系列半年三代（2.0 规模化 → 2.1 边写边改
    → 2.2 智能体觉醒），展现出持续的研究复利和清晰的架构演进路径，Levenshtein 编辑 + L-EBPO + BlockRouting 三合一也构建了较完整的技术栈。但需客观看待：当前平均分仍落后顶尖自回归模型约
    2 分，且仅在蚂蚁单一团队验证，开源生态尚未形成规模化生产应用，扩散模型能否在 3-5 年后成为 Agent 行业基石仍存在被更新架构（或自回归快速演进）反超的不确定性。故给予
    6.5 分，处于'细分赛道基础设施潜力'区间高位，需持续跟踪生产环境验证与生态采纳度。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Ant Group / inclusionAI
- 开源 AI 社区
- NVIDIA 等推理硬件厂商
- MCP/Agent 中间件生态
competitive_casualty:
- MiniMax (Ling 系列)
- OpenAI / Anthropic 等闭源自回归模型厂商
- 高溢价闭源 Agent API 提供商
market_opportunities:
- 创业者可基于开源的 LLaDA2.2 面向金融、政务等强合规行业提供本地化 Agent 部署与微调服务，利用扩散模型并行解码的高吞吐特性显著降低长程 Agent
  推理成本
- 建议关注扩散模型 Agent 推理工具链的空白机会（FP8 量化、BlockRouting 部署框架、推理加速中间件），开源模型发布后基础设施与部署工具需求将先行释放
- 可抓住 Agentic 扩散模型评测基准与可观测性工具的早期标准窗口期，新架构的纠错与执行特性需要全新的评估指标和监控方案
risk_matrix:
  regulatory: 蚂蚁作为金融科技背景机构发布的模型，在金融等受监管场景落地需满足生成式 AI 备案与数据合规要求；开源许可条款的商用边界需提前确认；出海部署可能面临欧盟
    AI Act、目标市场出口管制等合规审查
  technological: 扩散模型在 Agent 任务上仍落后顶尖自回归模型约 2 分，纠错机制能否根治错误累积与模型崩溃（Model Collapse）尚待第三方复现验证；自回归阵营（Ling、DeepSeek、Qwen
    等）的快速迭代可能使扩散路线的吞吐优势被快速追平
  competitive: 蚂蚁在开发者社区规模与生态号召力上弱于头部 AI 实验室，开源模型能否形成可持续生态存疑；自回归厂商同样在推进并行解码与投机采样优化，1.64
    倍吞吐优势难以长期维持；同类扩散语言模型及后续跟进者存在内部竞争
  ethical: Agent 自主执行增删纠错能力增强后，真实环境中的错误操作（如代码删除、数据处理、资金操作）将放大现实损害风险；模型在处理环境反馈过程中可能触及敏感数据与隐私；扩散架构在输出可控性与对齐方面的成熟度仍不足，存在误用风险
  additional:
  - 模型崩溃（Model Collapse）在扩散模型长程交互中可能持续累积，纠错本身也可能引入新错误
  - 现有 Agent 基准对扩散模型架构的公平性与适配性缺乏共识，评测结论存在被高估或低估的可能
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

# 全球首个Agentic扩散模型来了：边行动边纠错，128K上下文追平自回归

扩散模型首次打通长程Agent任务

鹭羽 发自 凹非寺

量子位 | 公众号 QbitAI


终于！Agent赛道，不再是自回归（AR）模型一家独大。

长期处于非主流位置的**扩散模型**，也开始有了一席之地。

这些年但凡叫得上名字的Agent，从ChatGPT到Claude，底层清一色因果自回归LLM。

逐Token生成慢是慢了点，但行业默认，Agent的大脑只能如此。

**蚂蚁**却不这么想。

旗下inclusionAI团队陆续推出LLaDA系列模型，最新开源**LLaDA2.2**，实现扩散模型首次进入智能体长程任务！

准确来说，这是一款千亿参数的MoE扩散语言模型，原生支持128K上下文，也是全球**首个**大规模Agentic扩散模型。

总之自回归模型能干的，它也能干，自回归模型跑得慢的痛点，它也能一刀切。

更关键的是，它第一次将Levenshtein编辑、面向环境反馈的强化学习，以及长上下文工程架构，整合进同一套扩散模型Agent系统——

模型不仅能并行生成，还能在生成过程中**自我增删**、**动态修正**。

LLaDA2.2的出现同样有迹可循，从2.0时期的规模化尝试，到2.1版本的边写边改，再到如今的智能体觉醒。

半年时间、三代模型，依次完成扩散架构从生成工具到行动架构的递进。

## 扩散模型破局自回归垄断

其实**自回归模型**能统治Agent赛道这么久，也是有几分道理在的。

多轮对话、工具调用、环境反馈处理，这些任务本身就天然要求模型具备序列因果性。

一个Token一个Token蹦，逻辑链条才不容易断。

传统扩散模型则可以同时处理一个block中的多个位置，速度是比自回归快了，但代价就是Token之间彼此**缺乏严格的序列条件约束**。

放在普通文本生成场景里，这些问题倒不算什么，顶多影响一点可读性，读者看到两句重复的话，笑一笑就算了。

**但Agent场景不一样。**

Agent的输出是要被真实执行的，再小的bug也会影响整个流程，**一步错步步错**，错误会在后续交互中被持续固化成硬约束，最终导致整体目标漂移。

所以扩散模型想在更复杂困难的Agent环境中和自回归齐平，就须得迈过这一关。

对此，蚂蚁团队看得很清楚。

**LLaDA2.0**首先解决的，就是**规模化**问题。

它证明扩散模型并不是只能停留在小参数实验阶段，也能够与MoE等架构结合，真正落地工程。

在验证路线可信的前提下，蚂蚁再顺势推舟给出**LLaDA2.1**，进一步证明扩散模型**边写边改**的可用性。

LLaDA2.1引入Token-to-Token编辑机制，可以在生成过程中判断哪些Token应该保留，哪些Token需要替换。

但到了Agent，这样的局部修改还远远不够，它需要的是根本性的结构调整，实现**边行动边纠错**。

于是**LLaDA2.2**来了。

## 如何做到？三大技术拼图集中发力

LLaDA2.2的变化集中在三个方面，每一项单点突破固然重要，蚂蚁三合一系统集成在一起才是扩散模型拿到Agent入场券的重中之重。

**让模型学会自改自生**

传统扩散模型块并行解码的最大问题是结构刚性。生成完一个block，里面的Token就被钉死了。

要是错了，只能整段重来，长了也没法删，短了更没法补。

LLaDA2.2采用**Levenshtein编辑范式**，在块内支持四种原子操作：**KEEP**（保留）、**SUBSTITUTE**（替换）、**DELETE**（删除）、**INSERT**（插入）。

然后通过LCS最长公共子序列将块内草稿与目标序列对齐，动态生成编辑标签。

翻译一下就是，模型现在能对自己的生成结果修正了。

看到冗余的内容，直接DELETE切掉，发现缺了关键信息，INSERT可以在指定位置开一个口子，后续去噪轮次往里填。

这也是业界**第一次**把Levenshtein编辑大规模集成到扩散模型的去噪过程中，效果立竿见影。

实验显示，在SWE-bench Verified上，仅开启Levenshtein编辑这一项，就带来了从35.8到44.4，整整**8.6**个百分点的绝对提升。

**让模型学会看环境反馈**

除了结构刚性问题，扩散模型还有一个更为隐蔽的坑。

长程Agent交互中，早期block的微小偏差会被后续上下文不断放大。一旦返回了错误结果，模型再用这个错误结果去规划下一步，推理路径就会越走越窄。

ICML 2026的最佳论文还专门讨论过这个问题，它有一个专门的名字：**模型崩溃**（Model Collapse）。

常规修正方法是在错误外面包一层修正指令，显然这样做治标不治本。

LLaDA2.2提出的**L-EBPO**（Levenshtein Editing Evidence Lower Bound Policy Optimization），可以把多轮交互中的Levenshtein编辑决策建模为**强化学习**问题。

模型会根据环境反馈，自主决策什么时候DELETE切除病灶、什么时候INSERT填补缺失。

如果说Levenshtein编辑范式是给了扩散模型一双手，L-EBPO就是添上了眼睛，让模型能实时看到自己的错误，知道从哪里做、做完效果如何。

**让模型支撑长程Agent任务**

解决完质量问题后，摆在扩散模型面前的还有最后一道坎——**工程应用**。

Agent任务普遍需要处理超长上下文，上下文窗口不够大，Agent就举步维艰。

LLaDA2.2通过渐进式长上下文训练，一步步把原生上下文窗口从8K、64K撑到了**128K**。

随之而来的是另一重问题：标准MoE为Token级路由，每个Token独立选择专家，总激活专家集合极大，HBM流量、通信开销暴涨，推理成本飙升。

LLaDA2.2的解法是**BlockRouting**。

先在block层面精准筛选top-C个专家形成固定专家池，再内部执行Token级top-k路由，屏蔽池外专家。

这样每块激活专家上限恒定，HBM流量与专家并行通信成本得以大幅降低。

由此，**128K原生上下文+BlockRouting机制**让Agentic扩散模型真正具备了工程部署价值。

那么效果如何呢？

且看七大Agent基准上，LLaDA 2.2-flash与顶尖自回归模型**Ling-2.6-flash**正面竞技，平均分为53.83 vs 55.74，差距缩小到2分以内。

严格来说，还没有完全跑赢，但二者已处于**相近水平**。

进一步拆开看，LLaDA 2.2在τ²-Bench、PinchBench、MCP-Atlas三项交互式任务上实现反超，说明它在偏向真实交互的Agent场景中已经开始展现竞争力。

效率方面则更干脆，在11类工作负载上，LLaDA2.2-flash的BF16平均吞吐量可达Ling-2.6-flash的1.64倍，量化至FP8后，平均吞吐量还可以额外提升**18.6%**。