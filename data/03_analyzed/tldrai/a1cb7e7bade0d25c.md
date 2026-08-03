---
title: PorTAL (1 minute read)
source: https://threadreaderapp.com/thread/2081819550329327689.html?utm_source=tldrai
author: []
published: ''
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a1cb7e7bade0d25c
source_type: news_media
tldr: PorTAL 推出 Latent Briefing 算法，让多智能体通过 KV cache 直接通信记忆而非传递 token，在准确率不变的情况下减少
  31% 的 token 消耗，并将 320 个顺序求解压缩为 2-3 次批处理操作，速度提升 20 倍（中位耗时 1.7 秒）。
objective_summary: PorTAL 团队在技术介绍中推出 Latent Briefing，一种让多智能体直接共享相关记忆的算法。该方法跳过 token
  空间，在 KV cache 层面进行通信，利用 worker 自身的注意力模式从 orchestrator 的记忆中提取相关内容并丢弃其余部分。团队改编了 Attention
  Matching（AM）压缩框架，并用任务查询打分、跨头全局掩码和 MAD 归一化阈值使其适配推理。实测显示 token 使用量减少 31% 且准确率不变，320
  个顺序求解降为 2-3 次批处理操作，中位耗时 1.7 秒，速度提升 20 倍。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - KV cache
  - Latent Briefing
  - Attention Matching
  - RAG
  - LLM
  - MAD-normalized thresholding
  key_people: []
key_logic_flow:
- 多智能体系统在 token 空间传递上下文会导致成本暴涨和信号丢失，而 LLM 摘要慢且有损、RAG 拆分上下文破坏文档间关联、全量传递上下文昂贵且降低准确率。
- Latent Briefing 让智能体直接进行 KV cache 到 KV cache 的通信，完全跳过 token 空间，利用 worker 的注意力模式从
  orchestrator 记忆中提取相关内容并丢弃其余部分。
- 该方法改编自 Attention Matching（AM）KV cache 压缩框架，并进行三项推理就绪改造：用 worker 任务查询而非自注意力打分、跨所有头应用全局掩码以支持大规模批处理、用
  MAD 归一化阈值实现自适应压缩。
- 实测结果是 token 使用量减少 31% 且准确率保持不变，320 个顺序求解被压缩为 2-3 次批处理操作，速度提升 20 倍，中位耗时降至 1.7 秒。
object_mentions:
- object_type: project
  name: Latent Briefing
  canonical_name: Latent Briefing
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章介绍 Latent Briefing 是一种让智能体直接分享相关记忆的方法，在保持同样准确率的情况下减少了 31% 的 token 消耗。
  - Latent Briefing 跳过 token 空间，直接在 KV cache 之间通信，利用 worker 自身的注意力模式从 orchestrator
    的记忆中提取相关内容并丢弃其余部分。
  article_id: a1cb7e7bade0d25c
- object_type: project
  name: Attention Matching
  canonical_name: Attention Matching
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到团队改编了 Attention Matching（AM）的 KV cache 压缩框架，该算法通过校正项保留注意力输出来压缩 KV cache。
  article_id: a1cb7e7bade0d25c
- object_type: project
  name: PorTAL
  canonical_name: PorTAL
  url: null
  confidence: low
  article_role: primary_subject
  evidence_snippets:
  - 文章标题为 PorTAL，正文围绕其团队构建的 Latent Briefing 方法展开，但正文没有对 PorTAL 本身给出更多细节说明。
  article_id: a1cb7e7bade0d25c
extract_result: success
impact_score:
  score: 6.0
  reason: 多智能体上下文传递的成本与延迟是当前 Agent 生态的核心痛点之一，Latent Briefing 提出跳过 token 空间、在 KV cache
    层面直连通信的思路，实测 token 消耗降低 31% 且准确率不变、延迟降低 20 倍（中位 1.7 秒），具备重塑局部 Agent 编排成本结构的潜力。但该方法目前仅为
    PorTAL 团队的自测成果，未经同行评审与独立复现，且仅验证了单一顺序求解场景，尚未达到行业范式转移级别，因此给予中等偏上评分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: KV cache 直连通信能否跨模型/跨 Agent 框架复现，以及 31% token 节省与 20 倍加速自测指标的真实性和泛化性
hype_assessment:
  level: low
  reason: 通篇未见“颠覆/革命性”等 PR 滥用词汇，给出了具体可验证的数字（31% token 节省、20 倍加速、中位 1.7 秒）、明确的方法出处（Attention
    Matching KV cache 压缩框架）和三项具体的工程改造（任务查询打分、跨头全局掩码、MAD 归一化阈值），属于实打实的技术介绍。保留意见是指标为团队自测、测试场景单一，需独立复现验证，但不足以判定为包装炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 提出多智能体在 KV cache 层面直连通信的算法范式，彻底绕开 token 空间的摘要/RAG/全量传递三条老路，利用
    worker 自身的注意力模式（任务查询打分）从 orchestrator 的 KV cache 中按需提取相关记忆并丢弃其余部分；并对 Attention
    Matching 压缩框架做了三项推理就绪改造：任务查询打分替代自注意力、跨头全局掩码支持大规模批处理、MAD 归一化阈值实现自适应压缩。这是从“转述式通信”到“按需读取记忆”的架构转变。
  business_model: 直接冲击 Agent 编排层的推理成本结构：token 消耗降 31%、延迟降 20 倍，意味着 agent-as-a-service
    的边际成本显著下降，可能推动按 token 计价的 API 定价模式向按“任务完成/记忆交互”计价迁移；同时 KV cache 管理与压缩将成为推理基础设施层的新差异化竞争点，可能催生
    KV cache 直连的专用推理服务或 Agent 通信协议。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 多智能体系统的 token 爆炸是规模化部署的真实瓶颈，而 KV cache 直连通信绕过了 token 空间，从机制上同时解决成本与信号丢失问题，属于底层效率创新。若该技术被主流编排框架采纳，有望成为
    Agent 通信的基础设施层（类似 RAG 之于知识检索的地位），具备复利效应——因为多智能体越普及，KV 级通信的边际价值越大。但扣分项明显：(1) 该方案依赖推理引擎暴露并支持
    KV cache 操作，深度耦合具体模型与版本，模型迭代可能导致兼容性断裂；(2) 团队规模小、尚未商业化，技术验证仅停留在论文级数据集；(3) 云厂商与基础模型提供商（OpenAI/Anthropic）完全可以在推理层原生实现同等能力，将其封装为
    API 服务，从而截留绝大部分价值。综合判断：有机会成为细分赛道标准件，但被巨头吸收的风险高，处于需要持续验证的 4-7 分区间。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- PorTAL
- LangChain
- CrewAI
- vLLM 生态
- Together AI
competitive_casualty:
- 基于 RAG 上下文的 Agent 中间件
- 按 token 计费的 Agent 编排平台
- 依赖 LLM 摘要传递上下文的编排方案
- 向量数据库在 Agent 上下文共享场景的应用
market_opportunities:
- 多智能体系统开发商可集成 KV cache 级记忆共享技术，显著降低 Agent 协作的 token 成本与端到端延迟，尤其在任务编排密集型场景构建差异化卖点
- 面向 Agent 的推理基础设施与网关服务商可将该压缩算法封装为托管能力，以“同精度下 token 消耗下降 31%、延迟降低 20 倍”为卖点吸引高并发多智能体客户
- 该技术可能催生“智能体记忆安全审计”工具机会：监控并治理 KV cache 层面跨 Agent 流转的敏感记忆，满足企业合规与隐私治理需求
risk_matrix:
  regulatory: 算法本身无直接监管限制，但 KV cache 跨智能体共享的记忆若含个人或敏感数据，落地金融、医疗等受监管场景时需评估其是否纳入数据合规审计与本地化要求
  technological: 依赖 Attention Matching 压缩框架且基准为团队自报，需独立复现验证；KV cache 压缩赛道竞争激烈（H2O、SnapKV、StreamingLLM
    等），更优或开源等价方案可能削弱其技术护城河
  competitive: OpenAI、Anthropic、Google 及 LangChain/AutoGen 等主流 Agent 框架可能快速内化类似能力，独立方案面临生态挤压与功能商品化风险
  ethical: 绕过 token 层直接共享 KV cache 记忆，可能引入新的隐私泄露与内容审查盲区；共享记忆可能放大系统偏见，并成为数据投毒与记忆篡改的攻击面
  additional:
  - 当前仅有团队技术介绍，未见开源代码或独立第三方复现，工程成熟度、跨模型可移植性与长尾场景可靠性待验证
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Latent Briefing
  canonical_name: Latent Briefing
  url: null
  positioning: 一种面向多智能体系统的记忆共享算法，通过 KV cache 到 KV cache 的直连通信，让智能体高效传递相关上下文而无需经过 token
    空间。
  technical_signal: 基于 Attention Matching 压缩框架改造，采用 worker 任务查询打分、跨头全局掩码与 MAD 归一化阈值，实现推理就绪的自适应
    KV cache 压缩。
  adoption_signal: 实测在准确率不变的前提下减少 31% token 消耗，将 320 个顺序求解压缩为 2-3 次批处理，中位耗时降至 1.7
    秒。
  ecosystem_relevance: 多智能体系统成本与信号丢失是通用痛点，该方法可惠及基于 LLM 的 agent 编排框架与多代理应用生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Latent Briefing 直击多智能体 token 通信的高成本与信号丢失问题，实测 20 倍提速且准确率不变，代表 KV cache
    层面的新型通信范式，值得持续跟踪其后续开源与生态落地情况。
  risk_notes:
  - 目前尚处于技术介绍阶段，缺乏公开可复现的基准评测与代码实现，实际效果待验证。
  - KV cache 层通信依赖 orchestrator 与 worker 的注意力模式对齐，在异构模型间可能难以直接复用。
  score: 8.0
  article_ids:
  - a1cb7e7bade0d25c
  evidence_snippets:
  - 文章介绍 Latent Briefing 是一种让智能体直接分享相关记忆的方法，在保持同样准确率的情况下减少了 31% 的 token 消耗。
  - Latent Briefing 跳过 token 空间，直接在 KV cache 之间通信，利用 worker 自身的注意力模式从 orchestrator
    的记忆中提取相关内容并丢弃其余部分。
- object_type: project
  name: Attention Matching
  canonical_name: Attention Matching
  url: null
  positioning: 一种通过校正项保留注意力输出的 KV cache 压缩框架，为 Latent Briefing 等推理场景提供底层压缩基础，属于记忆压缩领域的既有研究成果。
  technical_signal: AM 算法以 C1、β、C2 三参数形式压缩 KV cache，通过校正项维持注意力输出近似，Latent Briefing
    正是基于该框架做推理适配。
  adoption_signal: 文章仅将其作为被改编的底层方法提及，未见其独立采用规模或实测数据，属于间接采用信号。
  ecosystem_relevance: KV cache 压缩是长上下文与多智能体推理的关键基础设施方向，AM 框架为后续推理就绪改造提供了理论基础。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Attention Matching 作为 Latent Briefing 的底层压缩框架被引用，说明 KV cache 压缩正从离线研究走向推理场景落地，值得关注其与更多推理加速方法的结合。
  risk_notes:
  - 文章仅作为提及对象出现，缺乏独立性能数据与更广泛生态验证，观察维度有限。
  score: 5.0
  article_ids:
  - a1cb7e7bade0d25c
  evidence_snippets:
  - 文章提到团队改编了 Attention Matching（AM）的 KV cache 压缩框架，该算法通过校正项保留注意力输出来压缩 KV cache。
---

Introducing Latent Briefing, a way for agents to quickly share their relevant memory directly. Result: 31% fewer tokens used, same accuracy.

Multi-agent systems are powerful, but can be wildly inefficient. They pass context as tokens, so costs explode and signal gets lost. We built an algorithm that allows agents to communicate KV cache to KV cache.

Agents need to share context, but doing it in token space has real tradeoffs:

• LLM summaries: slow (20–60s), lossy, and often miss what the next agent actually needs
• RAG: splits context into chunks, so relationships across documents get lost
• Passing full context: expensive, noisy, and often hurts accuracy

Our method skips tokens entirely. We operate on the KV cache, using the worker's own attention patterns to extract what's relevant from the orchestrator's memory and discard the rest.

We adapted the Attention Matching (AM) KV cache compaction framework. The AM algorithm compacts the KV cache (C1, β, C2) preserving attention outputs through a correction term.

We modified the algorithm to make it inference ready: 1. Score tokens using the worker's task query, not self attention 2. Global mask across all heads → enables massive batching 3. MAD-normalized thresholding for adaptive compression

Result: 320 sequential solves → 2-3 batched ops. 20x speedup to a median of 1.7 s.