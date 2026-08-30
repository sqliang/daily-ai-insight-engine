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