---
title: Memory in Video World Models (6 minute read)
source: https://research.nvidia.com/labs/sil/projects/WorldTrace/?utm_source=tldrai
author: []
published: ''
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c17ed40cfaca9eb6
source_type: news_media
tldr: NVIDIA研究团队提出WorldTrace框架，通过固定分布内槽位位置解决自回归视频世界模型中KV缓存超出训练窗口后不可寻址的问题，无需重训练即可提升长程生成一致性与场景回忆能力。
objective_summary: NVIDIA研究团队在ICML 2026 F2S Workshop上发表最佳论文《Addressable Memory for
  Video World Models》。研究发现自回归视频世界模型在生成长度超过训练上下文窗口时，由于时间RoPE偏移超出训练范围，KV缓存中的历史记忆即使物理存在也会变得不可寻址。为此提出训练无关的WorldTrace框架，为两层KV缓存的摘要槽按槽位排名分配固定分布内位置，并先将键对齐到规范相位再平均、再重旋转到目标槽位，从而保持压缩记忆可寻址。基于该可寻址缓存，WorldTrace-Field通过旋转不变历史聚合提升长程rollout的时间一致性，WorldTrace-Landmark则保存逐字场景痕迹以实现长程情景回忆，二者在LoopMem基准的ABA路径等指标上显著优于滑动窗口基线。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - NVIDIA
  technologies:
  - WorldTrace
  - WorldTrace-Field
  - WorldTrace-Landmark
  - KV Cache
  - RoPE
  - Position-Aligned CLIP
  - TempSSIM
  - LoopMem
  key_people:
  - Xindi Wu
  - Sven Elflein
  - James Lucas
  - Olga Russakovsky
  - Laura Leal-Taixé
  - Despoina Paschalidou
  - Jonathan Lorraine
  - Aljoša Ošep
key_logic_flow:
- 自回归视频世界模型使用KV缓存存储视觉记忆，但生成长度超过训练上下文窗口时视觉持久性会崩溃。
- 超出训练范围的时间RoPE偏移是根因：缓存中的过去观测即使仍然存在，对注意力查询也变得不可寻址。
- 在RoPE旋转空间直接对键进行朴素平均会混合不兼容相位，导致信号抵消。
- WorldTrace采用两层KV缓存结构，为摘要槽按槽位排名分配固定的分布内位置，使其位置独立于展开长度。
- 键先对齐到规范相位再平均，然后重新旋转到摘要槽位位置，从而避免相位抵消并保持平均注意力logits。
- WorldTrace-Field面向时间一致性，用于更平滑的长程rollout；WorldTrace-Landmark保存逐字场景痕迹，用于长程情景回忆。
- 在LoopMem基准测试中，WT-Landmark在长ABA路径上的PAC从0.627提升至0.825，WT-Field在24倍horizon上TempSSIM提升15.5%。
object_mentions:
- object_type: project
  name: WorldTrace
  canonical_name: WorldTrace
  url: https://research.nvidia.com/labs/sil/projects/WorldTrace/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章标题指向NVIDIA研究实验室的WorldTrace项目页面，并在正文中将WorldTrace描述为解决视频世界模型记忆可寻址性的训练无关框架。
  - WorldTrace通过为两层KV缓存的摘要槽分配固定分布内位置，保持压缩记忆在任意生成长度下可寻址。
  article_id: c17ed40cfaca9eb6
- object_type: paper
  name: Addressable Memory for Video World Models
  canonical_name: Addressable Memory for Video World Models
  url: https://arxiv.org/abs/2608.07408
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章末尾的BibTeX条目显示论文标题为《Addressable Memory for Video World Models》，作者来自NVIDIA等机构，发表于ICML
    2026 F2S Workshop并获得最佳论文。
  - 论文arXiv编号为2608.07408，主要类别为cs.CV，并标注为Oral presentation。
  article_id: c17ed40cfaca9eb6
- object_type: model
  name: WorldTrace-Field
  canonical_name: WorldTrace-Field
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - WorldTrace-Field基于可寻址缓存，通过旋转不变的历史聚合来提升长程rollout的时间一致性。
  - 在24倍horizon下，WT-Field相比滑动窗口将TempSSIM提升15.5%，同时降低了Local Scene Drift。
  article_id: c17ed40cfaca9eb6
- object_type: model
  name: WorldTrace-Landmark
  canonical_name: WorldTrace-Landmark
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - WorldTrace-Landmark检测场景进入帧并将其逐字存入摘要槽，冻结插入以避免bfloat16漂移，目标是长程情景回忆。
  - 在LoopMem基准的长ABA路径上，WT-Landmark的PAC得分达到0.825，而滑动窗口基线仅为0.627。
  article_id: c17ed40cfaca9eb6
- object_type: dataset
  name: LoopMem
  canonical_name: LoopMem
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - LoopMem被用作 episodic recall 的测试基准，通过让模型返回先前访问的场景并用Position-Aligned CLIP评分来评估记忆能力。
  - 该基准覆盖了不同拓扑结构、路径长度、相机朝向以及多次重访设置。
  article_id: c17ed40cfaca9eb6
extract_result: success
impact_score:
  score: 6.8
  reason: 该工作针对自回归视频世界模型在长程生成时记忆不可寻址这一核心瓶颈，提出了无需重训练即可即插即用的 KV 缓存地址化方案。ICML 2026 Workshop
    最佳论文与 NVIDIA 研究背景增加了可信度，定量指标（LoopMem PAC 0.627→0.825、24× horizon TempSSIM +15.5%）显示明确的性能跃升。然而其影响仍主要停留在研究社区和潜在的开源/闭源世界模型推理优化层面，尚未进入生产级平台或引发行业格局重构，因此给予
    6.8 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 训练无关即可解决长程 KV 缓存地址性的工程技巧与可复现性
hype_assessment:
  level: medium
  reason: 文章存在一定程度的包装：使用“Best Paper”、“without retraining”、“visual persistence collapses”等具有传播力的表述，并突出
    NVIDIA 背书。但核心论点有具体机制（slot-rank positions、canonical-key averaging）和量化基准支撑，未出现“颠覆视频生成”之类的过度夸张，因此判定为中等炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 提出两层 KV 缓存结构，将摘要槽的位置按槽位排名固定于训练分布内，使长程缓存记忆始终可寻址；并通过规范相位对齐-平均-重旋转的键写入策略，避免
    RoPE 相位抵消，支持旋转不变的历史聚合与逐字场景痕迹保存。
  business_model: 可作为 NVIDIA Cosmos 等世界模型推理栈的即插即用优化模块，降低长视频/长程仿真推理成本，潜在应用于游戏、机器人仿真、交互式视频生成等需要持久视觉记忆的
    B 端与创作者场景。
engineering_complexity: prototype
compound_value:
  score: 7.5
  reason: WorldTrace 切中了自回归视频世界模型在长程生成时的核心瓶颈——KV 缓存中的历史记忆因 RoPE 偏移超出训练分布而变得不可寻址。通过训练无关的固定分布内槽位位置与规范相位对齐，它在不重新训练模型的情况下显著提升了时间一致性和场景回忆能力。若自回归视频世界模型成为交互式世界、机器人物理仿真或生成式游戏引擎的主流技术路线，addressable
    memory 将成为底层推理栈的关键原语，具备长期复利价值。但当前仍停留在学术框架/论文阶段，能否被主流模型（如 Sora、Genie 等）集成、是否会被扩散或状态空间模型路线取代，尚需验证，因此未给
    8 分以上。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- NVIDIA
- NVIDIA Omniverse
- OpenAI
- Google DeepMind
- Runway
- Luma AI
competitive_casualty:
- 依赖滑动窗口记忆的视频生成方案
- 长上下文能力弱的闭源视频模型
- 缺乏长程推理算力储备的小型视频生成初创
- 以'更长上下文'为核心卖点的专有中间件
market_opportunities:
- 创业者可基于WorldTrace的可寻址KV缓存思路，为自回归视频世界模型开发长程记忆增强中间件或推理优化服务，切入游戏、具身智能与自动驾驶仿真等对时序一致性要求高的场景
- 建议关注视频生成基础设施赛道中KV缓存压缩、长上下文推理与旋转位置编码相关的工程化机会，为大模型推理厂商提供训练无关的内存扩展方案
- 产品经理可将WorldTrace-Field与WorldTrace-Landmark两类能力分别映射到'长镜头平滑生成'与'场景回忆/重访'功能，探索虚拟拍摄、交互式世界构建等新形态应用
risk_matrix:
  regulatory: 无
  technological: 存在被原生长上下文架构或线性注意力/状态空间模型替代的风险；若未来训练窗口显著扩大或出现无需KV缓存的新架构，WorldTrace这类补丁式方案价值可能下降
  competitive: NVIDIA可能将该技术快速集成至Omniverse、 Cosmos等产品线，同时OpenAI、Google等巨头在长视频模型方向亦有布局，独立第三方工具面临生态挤压与价格战风险
  ethical: 视频世界模型长程记忆能力的增强可能降低深度伪造与虚拟场景操纵的门槛，需关注生成内容溯源与滥用风险
  additional:
  - 该论文为workshop最佳论文，虽然指标显著，但尚未经过大规模真实场景与产品化验证
  - Canonical-key对齐与重旋转的实现细节较复杂，工程落地中可能面临数值稳定性与推理延迟挑战
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: WorldTrace
  canonical_name: WorldTrace
  url: https://research.nvidia.com/labs/sil/projects/WorldTrace/
  positioning: NVIDIA 提出的训练无关框架，通过固定分布内槽位位置让视频世界模型的压缩 KV 缓存记忆在任意生成长度下保持可寻址。
  technical_signal: 识别时间 RoPE 偏移超出训练范围是记忆不可寻址的根因，采用固定分布内槽位位置与规范键写入保持可寻址性。
  adoption_signal: 刚获 ICML 2026 F2S Workshop 最佳论文，目前仍属学术前沿成果，工业落地与开源采用尚需观察。
  ecosystem_relevance: 针对自回归视频世界模型长程生成一致性与场景回忆瓶颈，对交互式世界模型与具身智能仿真具有底层价值。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: WorldTrace 在不重训练的前提下修复了 KV 缓存在超出训练窗口后不可寻址的根本问题，使长程 rollout 的时间一致性与逐字场景回忆能力同步提升，是视频世界模型落地长序列生成的关键基础设施。
  risk_notes:
  - 目前仅在 LoopMem 等合成基准验证，真实开放世界泛化能力仍待检验。
  - 摘要槽数量与键旋转操作引入的额外计算和存储开销，在大规模部署时尚需工程验证。
  score: 8.0
  article_ids:
  - c17ed40cfaca9eb6
  evidence_snippets:
  - 文章标题指向 NVIDIA 研究实验室的 WorldTrace 项目页面，并在正文中将 WorldTrace 描述为解决视频世界模型记忆可寻址性的训练无关框架。
  - WorldTrace 通过为两层 KV 缓存的摘要槽分配固定分布内位置，保持压缩记忆在任意生成长度下可寻址。
---

### 1. Addressability

Temporal RoPE offsets exceed the training range, so cached memories become **unreadable even when they are physically present**. Past the trained window, attention queries see phases the model never learned to address.

ICML 2026 F2S Workshop, Best Paper

**TL;DR.** WorldTrace keeps compressed memory addressable with fixed in-distribution slot positions, then uses canonical-key writers for two goals: **WorldTrace-Field** for smoother long rollouts and **WorldTrace-Landmark** for recalling previously visited scenes, all without retraining the generator.

We study visual persistence in autoregressive video world models, where Key–Value (KV) caches store growing visual memory but become hard to retrieve from beyond the training horizon. We identify out-of-distribution temporal RoPE offsets as the root cause: past observations may remain cached, yet become unaddressable to attention. WorldTrace is a training-free framework that keeps compressed memory addressable by assigning each slot a fixed, in-distribution position relative to the current frame. Built on this addressable cache, **WorldTrace-Field** improves coherent long rollouts with rotation-invariant history aggregation, while **WorldTrace-Landmark** preserves verbatim scene traces for long-range recall.

Autoregressive video world models promise interactive worlds, but **visual persistence** collapses once generation exceeds the training horizon.

Can an autoregressive video world model reliably remember where it has been, at any generation length?

Two coupled bottlenecks arise once generation crosses the training context window:

Temporal RoPE offsets exceed the training range, so cached memories become **unreadable even when they are physically present**. Past the trained window, attention queries see phases the model never learned to address.

Naive key averaging in RoPE-rotated space mixes incompatible phases. The resulting phase cancellation destroys the signal that compressed summaries are supposed to carry.

A two-tier KV cache: a verbatim recent window plus $N_s$ summary slots, with **positions assigned by slot rank** alone (independent of horizon) so every summary stays in-distribution at any generation length. Two complementary writers fill the slots:

Virtual position for summary slot $s$:

$q$ is the current query position, $L_{\mathrm{train}}$ is the training context length, and $F$ is the number of frames per autoregressive block. Slot positions depend on rank, not rollout length.

Keys are first aligned into a shared canonical phase, averaged, then re-rotated to the summary slot position. This avoids phase cancellation and preserves mean attention logits. WT-Field targets temporal coherence under compression; *not* a recall mechanism.

Scene-entry frames are detected from the canonical-key signal, stored verbatim into summary slots, and frozen on insertion to avoid bfloat16 drift from repeated unrotate→rerotate shifts. WT-Landmark keeps slot-rank positions unchanged and targets episodic recall over long rollouts.

LoopMem tests episodic recall by asking the model to return to previously visited scenes and scoring the regenerated view with Position-Aligned CLIP (PAC). Across topology, path length, camera orientation, and multi-revisit settings, WT-Landmark consistently improves over sliding-window recall: 0.825 vs. 0.627 PAC on the long ABA path, 0.864 vs. 0.723 on standard ABA, and 0.941 vs. 0.892 on ABABA. The hardest $360^\circ$ pan shows the smallest gain (0.577 vs. 0.559), making the limitation visible rather than hidden by the aggregate.

Vary the number of intermediate waypoints before returning to the starting scene.

Increase the number of generated chunks per leg to stretch context distance.

Stress recall under camera-orientation changes, including wide pans.

Revisit the same place multiple times to test repeated episodic recall.

Holding the content operator fixed (canonical averaging) and varying only the position assignment, slot-rank positions lead Block-Rel by **+5.9% TempSSIM** at 8× horizon and **+2.8%** at 16×. At 24× (N=48), WT-Field improves +15.5% TempSSIM over sliding-window while also lowering Local Scene Drift, where every $N$-dependent position formula degrades non-monotonically.

```
@inproceedings{wu2026worldtrace,
title={Addressable Memory for Video World Models},
author={Xindi Wu and Sven Elflein and James Lucas and Olga Russakovsky and Laura Leal-Taix\'{e} and Despoina Paschalidou and Jonathan Lorraine and Aljo\v{s}a O\v{s}ep},
booktitle={ICML 2026 Workshop: From Frames to Stories (F2S)},
note={Oral presentation},
year={2026},
eprint={2608.07408},
archivePrefix={arXiv},
primaryClass={cs.CV},
url={https://arxiv.org/abs/2608.07408},
}
```