---
title: 'Dual-Flow Transformers: Decoupling the Primary Prefill Path from Additional
  Decode Computation'
source: https://arxiv.org/abs/2608.12385
author:
- '[[Liming Liu, Mingze Wang, Tuo Zhao]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'arXiv:2608.12385v1 Announce Type: new Abstract: As large language models
  serve more requests, cumulative inference cost is becoming increasingly important
  relative to one-time training cost. The two inference phases stress hardware differently:
  prompt prefill is parallel and typically compute-bound, whereas autoregressive decode
  is sequential and often memory-bandwidth-bound. Conventional width or depth scaling
  increases both costs together because every added layer is evaluated in both phases.
  We ask whether additional learned computation can instead be allocated to continuation
  prediction while preserving the prompt-wide primary computation and a single persistent
  key-value (KV) cache. We introduce the Dual-Flow Transformer. Its primary flow is
  a complete causal language model that processes the prompt and writes the KV cache.
  The auxiliary flow is omitted during prompt processing and activated only from the
  final prompt position onward, adding continuation-prediction computation without
  writing persistent state or influencing the primary flow. The two flows share major
  attention, MLP, and output matrices, while using separate token embeddings and lightweight
  coupling. Sharing weights and the primary cache also creates opportunities to reuse
  loaded weights and cached keys and values during grouped execution. Across matched-token
  comparisons, Dual-Flow achieves lower validation loss across architectures and data
  configurations. In MoE models, the separation makes primary and auxiliary expert
  fan-outs independent controls over prompt cost, continuation cost, and predictive
  quality. We study two regimes: increasing decode computation at fixed prefill expert
  computation, and reallocating a fixed decode expert budget between the two flows.
  These experiments expose a prefill-decode-quality trade-off and demonstrate the
  potential of phase-specific expert allocation.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2ecce1eefb7a617f
source_type: academic_paper
tldr: Dual-Flow Transformer 论文提出将提示预填充的主计算路径与解码阶段的额外计算解耦：辅助流程仅在提示末尾后激活。实验显示在匹配 token
  下取得更低验证损失，并支持 MoE 中按阶段独立分配专家计算。
objective_summary: 该 arXiv 预印本提出 Dual-Flow Transformer 架构，将预填充阶段的主计算与解码阶段的辅助计算解耦。主流程是一个完整的因果语言模型，负责处理提示并写入
  KV 缓存；辅助流程仅在最后提示位置后激活，不写持久状态也不影响主流程。两个流程共享注意力、MLP 与输出矩阵，但使用独立的 token 嵌入与轻量耦合。作者报告在匹配
  token 的对比中，该架构在多种架构与数据配置下取得更低验证损失，并实验了固定预填充专家计算下增加解码计算、以及在两流程间重新分配解码专家预算两种 MoE 情形。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Dual-Flow Transformer
  - MoE
  - KV cache
  key_people: []
key_logic_flow:
- 大规模语言模型服务请求增多后，累计推理成本相对于一次性训练成本的重要性正在上升。
- 提示预填充阶段并行且通常受计算限制，而自回归解码阶段串行且常受内存带宽限制，传统宽度或深度扩展会同时增加两个阶段的成本。
- Dual-Flow Transformer 的主流程是一个完整的因果语言模型，负责处理提示并写入 KV 缓存，辅助流程仅在最后提示位置起激活且不写持久状态。
- 两个流程共享注意力、MLP 与输出矩阵，同时使用独立 token 嵌入与轻量耦合，权重与主缓存共享使分组执行时可复用已加载权重和缓存的键值。
- 在匹配 token 的对比中，Dual-Flow 在多种架构与数据配置下取得更低的验证损失。
- 在 MoE 模型中主辅专家扇出成为独立控制手段，实验研究了两种解码专家预算分配情形并揭示了预填充-解码-质量权衡。
object_mentions:
- object_type: paper
  name: Dual-Flow Transformers
  canonical_name: Dual-Flow Transformers
  url: https://arxiv.org/abs/2608.12385
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出 Dual-Flow Transformer 架构，其主流程处理提示并写入 KV 缓存，辅助流程仅在最后提示位置之后激活且不写持久状态。
  - 两个流程共享主要的注意力、MLP 和输出矩阵，同时使用独立的 token 嵌入与轻量耦合，从而在匹配 token 的对比中取得更低验证损失。
  article_id: 2ecce1eefb7a617f
extract_result: success
impact_score:
  score: 6.5
  reason: 该论文切中 LLM 推理成本结构中的真实痛点——预填充与解码两阶段对算力和带宽的压力不对称，而传统宽度/深度扩展会同时抬升两个阶段的开销。提出架构级解耦方案，让
    MoE 下可按阶段独立分配专家算力，方向新颖且与当下长上下文推理成本问题高度相关，可能启发后续推理优化与模型架构设计。但作为未经同行评审的预印本，实验仅报告验证损失层面的对比，缺乏下游任务评估、真实吞吐/延迟基准以及代码与权重开源，短期行业冲击有限。综合评分依据：创新性在架构层面成立、选题贴合产业需求，但证据链停留在理论验证阶段，故给
    6.5 分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 验证损失下降能否转化为实际推理吞吐与成本收益，以及是否会开源代码和权重供复现
hype_assessment:
  level: low
  reason: 论文措辞克制，明确将结论限定在匹配 token 的验证损失对比，并坦承实验揭示的是'预填充-解码-质量权衡'而非绝对优势，未使用'颠覆''革命性'等
    PR 式词汇。但存在论文常见的以验证损失替代端到端收益的叙事方式，缺少服务级基准作为支撑。综合判断水分较低。
information_entropy: high
domain_disruption:
  technical_innovation: 提出将语言模型的预填充与解码两个推理阶段的计算路径解耦：主流程保持完整因果 LM 处理提示并写 KV 缓存，辅助流程仅在提示末尾后激活且不写持久状态，两者共享注意力/MLP/输出矩阵但使用独立
    token 嵌入。这一设计使 MoE 下主辅专家扇出成为独立的成本与质量控制手段，突破传统宽度/深度扩展同时抬升两阶段成本的结构性约束，并借助权重与主缓存共享为分组执行中的缓存复用创造机会。
  business_model: 直接触及 LLM 服务成本中占比持续上升的推理开销：若方案被后续工作验证，服务商可按'提示长度 vs 续写量'的场景特征分阶段定制计算预算，为
    API 定价分层和推理基础设施（vLLM/SGLang 等）的调度策略提供新的优化维度。但当前仅为学术构想，离可量产部署和商业模式重塑尚有距离。
engineering_complexity: prototype
compound_value:
  score: 5.0
  reason: 投资逻辑推演：1) 需求确定性——LLM 服务规模化后累计推理成本超越训练成本是确定性趋势，'预填充受计算限制、解码受内存带宽限制'的成本结构洞察已被业界反复验证（DeepSeek
    在 MoE 推理上的成本优势即为先例），该方向有真实商业价值锚点；2) 技术成熟度——本文仍为 arXiv 预印本，认识论状态为理论性主张，仅报告匹配 token
    下的验证损失改善，未给出主流 benchmark、长上下文或真实部署负载下的收益证据，亦无代码与复现承诺，距工程化落地尚有多个验证周期；3) 价值捕获路径——真正的商业化需经由推理栈（vLLM/TensorRT-LLM）或下一代
    MoE 模型实现，若被主流栈采纳可沉淀为推理优化基础设施，具备复利效应，但存在被更强替代方案覆盖的风险；4) 格局影响——若架构成立，'分阶段计算分配'将成为新的优化维度，利好
    MoE 厂商与推理基础设施，利空依赖稠密暴力扩展的厂商。综合评分 5.0：方向正确、具备成为细分赛道基础设施的潜力，但证据强度与落地距离决定其仍需持续验证。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- DeepSeek
- Mistral AI
- vLLM 开源生态
- Together AI
competitive_casualty:
- 依赖稠密模型暴力扩展的模型厂商
- 未布局分阶段推理优化的中小模型初创公司
market_opportunities:
- Dual-Flow 架构若获社区复现验证，可启发推理引擎团队开发"预填充与解码分阶段算力调度"方案，在高并发提示（prefill 密集）场景下显著降低单位推理成本
- MoE 场景下按阶段独立分配专家计算的思想，可为云服务商与大规模模型运营方提供更细粒度的推理资源规划与差异化定价（预填充/解码分档）产品化机会
- 建议持续关注该论文是否发布代码与基线数据，一旦开源可作为长上下文或高 QPS 服务场景下与投机解码、前缀缓存等方案的对比基线
risk_matrix:
  regulatory: 无（纯学术预印本，暂无直接监管或合规风险）
  technological: 论文为未经社区独立复现验证的理论主张，存在复现失败或被证伪的可能；且可能被投机解码、前缀缓存、连续批处理等既有推理优化路线吸收或替代
  competitive: 云厂商与芯片公司若率先将该思想工程化并绑定自有推理栈，可能形成新的优化壁垒；同时面临 Meta、DeepSeek 等头部模型厂同类推理优化研究的竞争挤压
  ethical: 推理效率提升可能降低大规模批量生成与滥用的门槛（如垃圾内容、深度伪造），需配套内容治理与使用约束
  additional: []
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
---

# Computer Science > Artificial Intelligence

# Title:Dual-Flow Transformers: Decoupling the Primary Prefill Path from Additional Decode Computation

View PDF HTML (experimental)Abstract:As large language models serve more requests, cumulative inference cost is becoming increasingly important relative to one-time training cost. The two inference phases stress hardware differently: prompt prefill is parallel and typically compute-bound, whereas autoregressive decode is sequential and often memory-bandwidth-bound. Conventional width or depth scaling increases both costs together because every added layer is evaluated in both phases. We ask whether additional learned computation can instead be allocated to continuation prediction while preserving the prompt-wide primary computation and a single persistent key-value (KV) cache. We introduce the Dual-Flow Transformer. Its primary flow is a complete causal language model that processes the prompt and writes the KV cache. The auxiliary flow is omitted during prompt processing and activated only from the final prompt position onward, adding continuation-prediction computation without writing persistent state or influencing the primary flow. The two flows share major attention, MLP, and output matrices, while using separate token embeddings and lightweight coupling. Sharing weights and the primary cache also creates opportunities to reuse loaded weights and cached keys and values during grouped execution. Across matched-token comparisons, Dual-Flow achieves lower validation loss across architectures and data configurations. In MoE models, the separation makes primary and auxiliary expert fan-outs independent controls over prompt cost, continuation cost, and predictive quality. We study two regimes: increasing decode computation at fixed prefill expert computation, and reallocating a fixed decode expert budget between the two flows. These experiments expose a prefill-decode-quality trade-off and demonstrate the potential of phase-specific expert allocation.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.