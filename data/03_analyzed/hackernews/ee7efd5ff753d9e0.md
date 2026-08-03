---
title: Running Kimi K3 on MI355X at Better Performance per Dollar Than B300
source: https://www.wafer.ai/blog/kimi-k3-mi355x
author:
- '[[ilreb]]'
published: '2026-08-02'
created: '2026-08-02'
manifest_dates:
- '2026-08-02'
description: 'Article URL: https://www.wafer.ai/blog/kimi-k3-mi355x Comments URL:
  https://news.ycombinator.com/item?id=49141073 Points: 126 # Comments: 35'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ee7efd5ff753d9e0
source_type: community_discussion
tldr: Wafer 发布实测基准：AMD MI355X 以 952 tok/s 的节点聚合吞吐与 118 tok/s 单流解码运行 2.8T 参数的 Kimi
  K3，性能每美元达 48 tok/s/美元，超过 B300 与 B200。工程上通过修复 sglang 的 top_k_renorm_prob 缺失和 AITER
  MLA 预填充头数对齐，实现约 2-3 倍预填充加速。
objective_summary: Wafer 在官方博客公布在 AMD MI355X（8 卡 TP8）上服务 2.8T 参数开源模型 Kimi K3 的实测基准：1024
  token 输入/400 token 输出下，节点聚合吞吐 952 tok/s、单流解码 118 tok/s，性能每美元 48 tok/s/美元。对比双节点 TP16
  的 B200 聚合吞吐 498 tok/s、单节点 B300 为 1568 tok/s，但 B300 单价约为 MI355X 的 2.4 倍。工程上，团队用 RadixArk
  Kimi-K3-DSpark 草稿模型实现投机解码，为 sglang 的 ROCm 分支补齐 top_k_renorm_prob 定义，并将 AITER MLA
  预填充内核头数从 12 零填充到 16，使 172k token 冷预填充提速约 2-3 倍。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Wafer
  - AMD
  - NVIDIA
  - RadixArk
  - Moonshot AI
  - DeepSeek
  - Zhipu AI
  technologies:
  - ROCm
  - CUDA
  - Triton
  - MLA
  - MTP
  - EAGLE
  - speculative decoding
  - KV cache
  - TP8
  - HBM
  - sglang
  - AITER
  key_people: []
key_logic_flow:
- Kimi K3 是 2.8T 参数的开源模型，权重加上 1M token 上下文的 KV 缓存需要超过 1.5TB 显存，单个 B200 节点无法容纳。
- AMD MI355X 单卡拥有 288GB 显存，平均单价约为 B300 的 2.4 折、B200 的 1.7 折，成为服务超大模型的高性价比替代方案。
- 基准测试显示 MI355X 节点聚合吞吐 952 tok/s、单流解码 118 tok/s，性能每美元 48 tok/s/美元，全面优于 B200 的 7 tok/s/美元和
  B300 的 33 tok/s/美元。
- K3 未附带任何草稿张量，投机解码依赖外部草稿模型 RadixArk Kimi-K3-DSpark；sglang 的 ROCm 分支缺少 top_k_renorm_prob
  定义导致调度器崩溃。
- 用单个 PyTorch 函数补齐 top_k_renorm_prob 定义后，单流性能提升约 2.2 倍，峰值聚合吞吐增长 18%，并稳定运行在更高并发度上。
- MI355X 上 172k token 冷预填充耗时 51 秒明显慢于 B300 的 23 秒，根因是 AITER MLA 内核因头数形状不匹配而回退到 Triton，零填充到
  16 头后预填充提速约 2-3 倍。
object_mentions:
- object_type: model
  name: Kimi K3
  canonical_name: Kimi K3
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Kimi K3 是 2.8T 参数的开源大模型，权重加 1M token 上下文的 KV 缓存需要超过 1.5TB 显存，单个 B200 节点无法容纳。
  - Kimi K3 未附带任何草稿张量（无 MTP、无 EAGLE），在 MI355X 上依赖外部投机解码路径才能达到当前吞吐。
  article_id: ee7efd5ff753d9e0
- object_type: product
  name: AMD MI355X
  canonical_name: AMD MI355X
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - AMD MI355X 单卡拥有 288GB 显存，平均单价约为 B300 的 2.4 折、B200 的 1.7 折，是服务超大模型的成本替代方案。
  - MI355X 在 1024 输入/400 输出基准下达到 952 tok/s 节点聚合吞吐和 118 tok/s 单流解码。
  article_id: ee7efd5ff753d9e0
- object_type: product
  name: NVIDIA B300
  canonical_name: NVIDIA B300
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - B300 节点在聚合吞吐上以约 1.65 倍领先 MI355X，但单价约为 MI355X 的 2.4 倍，性能每美元反而落后。
  - B300 每 GPU 拥有 288GB 显存，单价假设为 6 美元每 GPU 小时，性能每美元约 33 tok/s/美元。
  article_id: ee7efd5ff753d9e0
- object_type: product
  name: NVIDIA B200
  canonical_name: NVIDIA B200
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - B200 因 Kimi K3 无法放入单个 8×192GB 节点而需双节点 TP16 部署，跨节点 all-reduce 位于解码关键路径上。
  - B200 的 TP16 部署聚合吞吐 498 tok/s 是两块节点的总和，平均每节点仅约 249 tok/s，性能每美元仅 7 tok/s/美元。
  article_id: ee7efd5ff753d9e0
- object_type: project
  name: RadixArk Kimi-K3-DSpark
  canonical_name: RadixArk Kimi-K3-DSpark
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Kimi K3 未附带任何草稿张量，投机解码只能依赖外部块扩散草稿模型 RadixArk 的 Kimi-K3-DSpark，在 CUDA 上可直接运行。
  article_id: ee7efd5ff753d9e0
- object_type: project
  name: sglang
  canonical_name: sglang
  url: https://github.com/sgl-project/sglang
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - sglang 的接受采样校验器在稠密路径调用 top_k_renorm_prob，但 ROCm 构建未定义该符号，请求落地时触发 NameError 并带崩调度器。
  - 修复方式是直接在 sglang 的 ROCm 采样分支用排序、masked_fill 和除法实现 top-k 重归一化，无需自定义内核。
  article_id: ee7efd5ff753d9e0
- object_type: project
  name: AITER
  canonical_name: AITER
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - AITER 的 MLA 预填充内核只支持 4、8 或 16 倍数的注意力头数，K3 在 TP8 下每 rank 有 12 头，导致回退到慢速 Triton
    内核。
  - 将头数从 12 零填充到 16 后启用 AITER MLA 预填充内核，预填充速度从约 4-7k tok/s 提升到约 13k tok/s。
  article_id: ee7efd5ff753d9e0
- object_type: model
  name: DeepSeek V4-Pro
  canonical_name: DeepSeek V4-Pro
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - DeepSeek V4-Pro 拥有 1.6T 参数，文章认为其智能水平已达到接近闭源 Opus 级别，是开源模型能力爆发的代表之一。
  article_id: ee7efd5ff753d9e0
- object_type: model
  name: GLM5.2
  canonical_name: GLM5.2
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GLM5.2 拥有 753B 参数，智能水平接近 Opus，文章以它作为框架类 bug 数量的对比基准，称 MI355X 适配 K3 的 bug 比 GLM5.2
    更少。
  article_id: ee7efd5ff753d9e0
extract_result: success
impact_score:
  score: 6.2
  reason: 先看依据：这是基础设施层的实测基准，而非新模型或新范式。它首次验证了 AMD MI355X 能以 48 tok/s/美元的性能每美元服务 2.8T
    参数的 Kimi K3，显著超过 B300（33）和 B200（7），直接动摇了 NVIDIA 在超大规模开源模型推理市场的定价权，并证明了 HBM 大容量路线（288GB/卡）对万亿参数
    MoE + 长上下文场景的实用价值。但存在明显局限性：数据来自 Wafer（AMD 托管服务商）单方自测，B200 对比因跨节点 all-reduce 而偏低，$/GPU-hr
    定价假设由商家自设，且整体属于既有硬件的工程适配而非方法论突破，不足以构成范式转移。综合判定为'改变局部推理成本竞争格局'级别，评 6.2。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: ROCm 生态的差距比预期小——两个 Python 级补丁（补 top_k_renorm_prob、零填充 MLA 头数）就换来
    2-3 倍预填充加速，AMD 推理护城河是否开始松动
hype_assessment:
  level: medium
  reason: 识别营销措辞：正文使用了 'new era for open source'、'crushes the B300' 等带包装色彩的表达，且 Wafer
    本身是 AMD 托管服务商，存在立场利益。但文章也给出了可复现的基准表、具体工程修复细节，并诚实承认 B300 在原始聚合吞吐上仍领先 1.65 倍、MI355X
    冷预填充显著更慢，未系统性夸大。作为自测基准，B200 数据因跨节点通信被拉低、单价假设由商家自设，存在选择性呈现。综合判定为存在一定包装、但干货占比高，level=medium。
information_entropy: high
domain_disruption:
  technical_innovation: 验证了'以 HBM 容量为杠杆'的超大规模模型推理路径：2.8T 权重加 1M token KV 缓存需超 1.5TB
    显存，MI355X 单卡 288GB 使单节点 TP8 即可承载，而 B200 需双节点 TP16。工程上两个关键修复——用单个 PyTorch 函数补齐
    sglang ROCm 分支缺失的 top_k_renorm_prob（解锁投机解码，单流提升约 2.2 倍），以及将 AITER MLA 预填充注意力头数从
    12 零填充到 16 绕过形状不匹配（冷预填充提速 2-3 倍）——证明了 AMD 生态的多数短板是'缺失定义/形状对齐'而非'缺失内核'，AI agent
    辅助调优可加速弥合这一差距。
  business_model: 重构超大模型推理的成本结构：MI355X 单价约为 B300 的 2.4 折、B200 的 1.7 折，使 2.8T 级开源模型的单节点托管在经济上首次可行，性能每美元
    48 vs B300 的 33、B200 的 7，对 GPU 云服务定价与 NVIDIA 溢价形成直接压力，可能加速'开源大模型 + AMD 廉价算力'替代闭源
    API 的商业闭环，并推动推理服务按 tok/s/$ 计价的新竞争维度。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 该事件的核心价值不在单次基准测试，而在 AMD ROCm 推理生态的'可复制性拐点'。投资逻辑链：其一，K3 服务的瓶颈正从硬件转向软件，而 Wafer
    证明软件缺口可被低成本工程补齐（top_k_renorm_prob 单函数修复、MLA 头数 12→16 零填充），意味着 AMD 的 288GB HBM
    容量与约 2.4 折价格优势正从'纸面参数'转化为'可落地的每美元吞吐'，这是可积累的工程资产。其二，开源超大模型（K3/DeepSeek/GLM）已成趋势，1M
    context 级推理对显存容量极度敏感，MI355X 在此场景拥有 B200 无法复制的结构性优势，且此类 workload 占比会随开源模型规模扩大而复利增长。其三，每次这类工程修复都会回灌
    sglang/AITER/ROCm 社区，边际成本递减、生态厚度递增，形成飞轮。风险点：NVIDIA 可能以激进定价或更高容量 HBM（如下一代 Rubin）回应；AMD
    day-0 软件支持仍依赖第三方持续投入，基准数据尚需大规模生产环境验证。综合判断 3-5 年后 AMD 大概率仍是前沿开源模型推理的基石硬件之一，故评 8
    分。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- AMD
- Wafer
- Moonshot AI
- RadixArk
- sglang/ROCm 开源生态
competitive_casualty:
- NVIDIA
- 单一 NVIDIA 架构的重资产 GPU 云厂商
- B200 高成本推理集群持有方
market_opportunities:
- 可依托 MI355X 的高性能/美元优势，为部署 Kimi K3 等超大规模 MoE 开源模型的企业提供 AMD ROCm 平台推理优化、部署与运维托管服务，形成对
  NVIDIA 算力的低成本替代方案
- 建议关注面向开源超大模型的投机解码生态机会：K3 等模型不附带草稿张量，为外部草稿模型（如 RadixArk DSpark）与配套采样验证内核的开发留下了商业化空间
- 可在 sglang/vLLM 等推理框架的 ROCm 分支上布局 CUDA-ROCm 桥接与内核适配工程服务，针对 top_k_renorm_prob 缺失、MLA
  头数对齐等系统性缺口沉淀可复用的工具链
risk_matrix:
  regulatory: 美国对高性能 GPU 的出口管制可能影响 MI355X 等 AMD 加速卡的全球供应与定价，在中美科技博弈背景下采购与跨域部署存在合规不确定性
  technological: ROCm 软件生态成熟度不足：本文依赖 sglang 与 AITER 的单点补丁修复，框架升级后可能失效；且 MI355X 冷预填充仍明显慢于
    B300，长上下文场景的 TTFT 劣势未从根因上解决
  competitive: NVIDIA 可能通过降价、推出 Blackwell Ultra 或新一代架构迅速缩小性能/美元差距；CUDA 生态锁定效应仍强，AMD
    在日 0 支持与内核覆盖度上短期难以完全追平
  ethical: 2.8T 参数模型的大规模推理带来显著能耗与碳排放压力；且本基准由 AMD 算力服务商发布，存在利益相关方偏置，需独立第三方复测验证
  additional:
  - 性能/美元结论高度依赖定价假设（MI355X $2.50 vs B300 $6.00/GPU-hr），若 AMD 折扣或云商定价结构变化，结论可能反转
  - B200 因装不下 K3 而被迫跨节点 TP16，对比口径不完全公平，单节点性能差异需谨慎解读
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: AMD MI355X
  canonical_name: AMD MI355X
  url: null
  positioning: AMD 面向超大规模模型推理的加速卡，单卡 288GB 显存，以明显低于 B300/B200 的单价提供可比硬件规格，主打性能每美元优势。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 超大规模开源模型推理服务商
  - 对每美元吞吐敏感的高性价比算力用户
  - 需要在单节点容纳超大参数模型的算力团队
  product_signal: MI355X 在 1024/400 基准下达到 952 tok/s 节点聚合吞吐与 118 tok/s 单流解码，性能每美元达
    48 tok/s/美元。
  market_signal: 以约 B300 四折、B200 六折的每 GPU 单价切入超大模型推理市场，性能每美元超越两代 Blackwell 产品。
  differentiation: 凭借 288GB 高带宽显存与显著成本优势，成为少数能在单节点容纳 2.8T 参数模型且兼具性价比的 NVIDIA 替代方案。
  watch_reason: MI355X 首次在 2.8T 参数开源模型 Kimi K3 上展示出超越 Blackwell 的性能每美元表现，且 AMD 提供
    day-0 支持，标志非 NVIDIA 阵营在超大模型推理场景的实用化突破，值得持续跟踪其软件生态成熟度与规模化落地进展。
  risk_notes:
  - ROCm 软件栈仍缺少数关键内核定义，需社区修复 sglang 的 top_k_renorm_prob 等问题才能稳定运行。
  - 172k token 冷预填充耗时约 51 秒，仍明显慢于 B300 的 23 秒，TTFT 场景竞争力偏弱。
  - 基准数据来自 Wafer 单一团队实测，缺乏 AMD 官方披露与规模化客户验证，长期供给存在不确定性。
  score: 8.0
  article_ids:
  - ee7efd5ff753d9e0
  evidence_snippets:
  - AMD MI355X 单卡拥有 288GB 显存，平均单价约为 B300 的 2.4 折、B200 的 1.7 折，是服务超大模型的成本替代方案。
  - MI355X 在 1024 输入/400 输出基准下达到 952 tok/s 节点聚合吞吐和 118 tok/s 单流解码。
- object_type: product
  name: NVIDIA B300
  canonical_name: NVIDIA B300
  url: null
  positioning: NVIDIA 面向超大规模模型推理的旗舰加速卡，单卡 288GB 显存，以绝对吞吐领先但单价高昂，面向成本不敏感的高端推理场景。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 对绝对吞吐要求最高的前沿模型推理团队
  - 预算充足、追求极致单流解码性能的企业用户
  product_signal: B300 节点聚合吞吐 1568 tok/s、单流解码 172 tok/s，绝对性能仍领先 MI355X 约 1.65 倍。
  market_signal: 以约 6 美元每 GPU 小时的单价提供约 33 tok/s/美元性能，虽绝对吞吐领先但性能每美元被 MI355X 反超。
  differentiation: 绝对吞吐仍是同类最强，但约 2.4 倍的单价溢价使其在性能每美元维度输给 AMD MI355X。
  watch_reason: B300 作为 Blackwell 旗舰在绝对吞吐上仍保持对 MI355X 的领先，但其每美元性能被 AMD 首次反超，显示超大模型推理市场开始出现除绝对性能之外的成本竞争维度，值得跟踪
    NVIDIA 的定价与产品应对策略。
  risk_notes:
  - 高单价削弱其在大规模部署中的性价比吸引力，面临来自 MI355X 等替代方案的竞争压力。
  - 基准数据来自第三方 Wafer 实测，未获 NVIDIA 官方确认，数字存在口径差异的可能。
  score: 6.0
  article_ids:
  - ee7efd5ff753d9e0
  evidence_snippets:
  - B300 节点在聚合吞吐上以约 1.65 倍领先 MI355X，但单价约为 MI355X 的 2.4 倍，性能每美元反而落后。
  - B300 每 GPU 拥有 288GB 显存，单价假设为 6 美元每 GPU 小时，性能每美元约 33 tok/s/美元。
- object_type: product
  name: NVIDIA B200
  canonical_name: NVIDIA B200
  url: null
  positioning: NVIDIA 上一代 Blackwell 加速卡，单卡 192GB 显存，因超大模型无法单节点容纳而需双节点 TP16 部署，面向常规规模推理场景。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 常规规模模型推理与训练用户
  - 存量 Blackwell 部署的基础设施团队
  product_signal: TP16 双节点部署聚合吞吐 498 tok/s，平均每节点仅约 249 tok/s，单流解码 90 tok/s，跨节点通信拖累性能。
  market_signal: 以约 4.25 美元每 GPU 小时单价计算性能每美元仅约 7 tok/s/美元，在超大模型场景显著落后 MI355X。
  differentiation: 因显存容量不足被迫跨节点部署，解码关键路径上的跨节点 all-reduce 使其在超大模型推理场景失去竞争力。
  watch_reason: B200 的案例说明当模型规模突破单节点显存容量时，硬件架构与容量设计将直接决定推理部署效率，其对比结果印证了高容量显存方向对超大模型的重要性，值得作为架构权衡的参考样本跟踪。
  risk_notes:
  - 双节点 TP16 部署引入跨节点通信开销，解码关键路径被 all-reduce 拖慢，性能劣势明显。
  - 基准基于 Wafer 单一测试场景，B200 在常规规模模型上的表现不应据此全面否定。
  score: 5.0
  article_ids:
  - ee7efd5ff753d9e0
  evidence_snippets:
  - B200 因 Kimi K3 无法放入单个 8×192GB 节点而需双节点 TP16 部署，跨节点 all-reduce 位于解码关键路径上。
  - B200 的 TP16 部署聚合吞吐 498 tok/s 是两块节点的总和，平均每节点仅约 249 tok/s，性能每美元仅 7 tok/s/美元。
---

Over the past several months, we’ve seen an explosion in the capabilities of open source models. With DeepSeek V4-Pro and GLM5.2 reaching near-Opus levels of intelligence, open source has emerged as a real, cost-efficient alternative to the closed source models we’ve been married to.

But we have yet to see one like Kimi K3. Promising Fable/Sol levels of intelligence, Kimi K3 marks the start of a new era for open source.

But a smarter model means a **bigger** model — and these models are expanding in size just as fast as they are in capabilities. GLM5.2 has 753B parameters, DeepSeek V4-Pro 1.6T, and Kimi K3 weighs in at 2.8T (!!) parameters. That’s over 1.5TB of VRAM *before* allocating a KV cache for 1M tokens of context. Not even a B200 node (8 GPUs) can fit Kimi K3. That leaves you with limited options: serve on a node of B300s, which have 288GB of VRAM per GPU, or commit two B200 nodes (TP16) to serving Kimi.

But guess which other non-NVIDIA GPU has 288GB of VRAM? AMD’s MI355X. Can you tell we like these chips yet? At around ~2.4× cheaper per GPU on average versus a B300 and ~1.7× cheaper than a B200, the MI355X is a cost-efficient alternative to Blackwells with comparable hardware specs. The only problem with AMD is software support — slower kernels and less day-0 support on inference frameworks make serving frontier models on AMD a real engineering effort. Our claim at Wafer is that agents are improving at kernel and model optimization, closing this gap as we speak. But with AMD shipping day-0 support for Kimi K3, most of the work was already done for us.

The results are great: on a 1,024-token input / 400-token output benchmark, the MI355X reaches 952 tok/s/node and 118 tok/s single stream — over 3.8× the aggregate throughput per node and over 1.3× the single-stream decode of our TP16 B200 deployment (whose 498 tok/s is a 16-GPU, 2-node total — ~249/node). B300 nodes still win ~1.65× on aggregate throughput over the MI355X, but at 2.4× the price, the MI355X crushes the B300 on performance per dollar.

8× MI355X (TP8) |
2×8 B200 (TP16) | B300 (TP8+DCP8) | |
|---|---|---|---|
| Decode tok/s per stream | 118 tok/s |
90 tok/s | 172 tok/s |
| Peak aggregate | 952 tok/s |
498 tok/s | 1,568 tok/s |
| Peak aggregate per GPU | 119 tok/s |
31 tok/s | 196 tok/s |
| Peak aggregate per $/GPU-hr | 48 tok/s/$ |
7 tok/s/$ | 33 tok/s/$ |

*Perf/dollar at $2.50/GPU-hr for the MI355X, $6.00 for the B300, and $4.25 for the B200.*

To the B200’s defence, its numbers are somewhat deflated by the fact that it pays a cross-node all-reduce on the decode critical path (RoCE v2 at ~195 Gb/s) — it’s the only config here that spans two nodes, because Kimi K3 won’t fit weights plus a 1M-token KV pool on a single 8×192GB node. But that’s exactly the point: Kimi K3 at its size is one of the first models we’ve seen where the MI355X’s focus on HBM capacity gives it a practical, measurable edge over the B200.

## How we did it

While Kimi K3 served out of the box, there was still work to be done to get it to its current throughput number.

The main lever was speculative decode. K3 ships zero draft tensors — no MTP, no EAGLE — so the only speculative path is an external block-diffusion draft: RadixArk’s Kimi-K3-DSpark. On CUDA it just runs. On ROCm our first real request breaks the scheduler with this error:

`NameError: name 'top_k_renorm_prob' is not defined. Did you mean: 'top_p_renorm_prob'?`


sglang’s accept-sampling verifier has two ways to build the target distribution: a dense path that calls `top_k_renorm_prob`

, and a sparse fast path that routes through `torch.topk`

directly. The CUDA build imports `top_k_renorm_prob`

from `sgl_kernel`

; the ROCm build aliases only a Triton top-p kernel and leaves `top_k_renorm_prob`

undefined — there’s no top-k renorm kernel for gfx950 to alias. So the moment a request lands on the dense path, the verifier hits that `NameError`

and takes the scheduler down with it.

The fix is a single PyTorch function. Top-k renorm is a small operation: take the model’s probability vector, keep the k highest entries, zero the rest, and rescale what’s left to sum to 1. A `sort`

, a `masked_fill`

, a divide — dropped straight into sglang’s ROCm sampling branch, the same computation the CUDA build gets from `sgl_kernel`

. No custom kernel: the reflex on ROCm is to assume you need one, but here it was a missing definition, not a missing kernel.

With spec dec fixed and hardened, we gained ~2.2× performance single-stream, ~1.7× per-stream at moderate load, and +18% peak aggregate. More importantly, our peak aggregate throughput landed on much higher concurrency (c64 vs c24 no-spec).

## Prefill optimizations

Discussion around model performance tends to highlight decode tokens per second. But in many cases decode tok/s is fool’s gold — decode is over-glorified, while time-to-first-token, the number users *feel* the most, gets overlooked.

The MI355X struggles here: an identical 172k-token cold prefill took ~51s on MI355X versus ~23s on a B300. On a 1M-context model, a lot of workloads have huge prefills (sometimes cold), and having GPUs spin on prefill for minutes can render entire fleets of nodes useless.

The gap was almost entirely one kernel. K3 on ROCm was falling back to slow generic Triton attention because the fast AITER MLA prefill kernel wouldn’t load. The problem was a shape mismatch, not a missing kernel — K3 at TP8 gives 12 attention heads per rank, and AITER’s MLA path is built for 4, 8, or multiples of 16. The fix was trivially simple: zero-pad the head count 12→16, run the fast kernel, and extract the real 12 heads from the output.

The result: on the same 172k cold prefill, the AITER MLA prefill ASM runs at ~13k tok/s steady-state vs the Triton fallback’s ~4–7k, speeding up prefill by ~2–3×. It’s a TTFT lever, not an aggregate-throughput one — decode is unchanged, so it doesn’t move the numbers above; it moves the number a user waits on before the first token appears.

## Takeaways

Achieving the best performance-per-dollar ratio on the MI355X was relatively out of the box. There were some expected framework-related bugs — but fewer than GLM5.2, and this time it certainly did not require custom kernels.

SOTA on AMD is imminent. Is the CUDA moat dead?