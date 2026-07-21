---
title: Xiaomi-Robotics-1
source: https://robotics.xiaomi.com/xiaomi-robotics-1.html
author:
- '[[ilreb]]'
published: '2026-07-20'
created: '2026-07-20'
manifest_dates:
- '2026-07-20'
description: 'Article URL: https://robotics.xiaomi.com/xiaomi-robotics-1.html Comments
  URL: https://news.ycombinator.com/item?id=48974454 Points: 199 # Comments: 130'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dce4de7f30cdd189
source_type: community_discussion
tldr: 小米发布机器人基础模型 Xiaomi-Robotics-1，采用 10 万小时无本体（UMI）预训练结合真实机器人后训练，在四项仿真基准测试中达到最优，且能以不到
  10 小时数据适配新任务达到 75% 成功率。
objective_summary: 小米研究团队发布了机器人基础模型 Xiaomi-Robotics-1。该模型采用两阶段训练：首先使用 10 万小时覆盖 1700
  多种场景的无本体 UMI 轨迹数据进行预训练，再使用 7200 小时真实家庭机器人数据进行后训练以对齐实体能力与指令执行。实验显示预训练阶段验证误差随数据和模型规模增长而稳定下降，且这一缩放规律直接迁移至真实机器人性能。该模型在
  RoboCasa、RoboCasa365、VLABench 和 RoboDojo 四项仿真基准测试中均达到最优，并以平均不到 10 小时的演示即可在全新任务上达到
  75% 成功率，显著优于 π0.5 基线（40%）。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Xiaomi
  technologies:
  - VLA
  - UMI
  - VLM
  key_people:
  - Jun Guo
  - Piaopiao Jin
  - Jason Li
  - Peiyan Li
  - Yingyan Li
  - Futeng Liu
  - Wanli Peng
  - Optimus Qin
  - Yifei Su
  - Nan Sun
key_logic_flow:
- Xiaomi-Robotics-1 采用大规模无本体（UMI）预训练与少量真实机器人后训练相结合的两阶段训练范式，效仿大语言模型的训练路径。
- 预训练数据包含 10 万小时、覆盖 1700 多种场景（家庭、商业、工业、户外）的 UMI 轨迹，通过 VLM 自动标注场景状态变化描述。
- 后训练使用 7200 小时真实家庭机器人数据，沿实体对齐和指令对齐两个轴将通用动作生成能力映射到真实机器人。
- 实验表明预训练阶段验证动作误差随数据量和模型规模增长稳定下降，且这一缩放规律直接迁移到后训练阶段的真实机器人成功率。
- 在 RoboCasa、RoboCasa365、VLABench、RoboDojo 四项仿真基准测试中均达到最优，相对第二名提升 2.6% 至 58.3%。
- 该模型以平均不到 10 小时演示即可在全新任务上达到 75% 成功率，显著超越 π0.5 基线（40%）；增至不到 40 小时则提升至 85%。
object_mentions:
- object_type: model
  name: Xiaomi-Robotics-1
  canonical_name: Xiaomi-Robotics-1
  url: https://robotics.xiaomi.com/xiaomi-robotics-1.html
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Xiaomi-Robotics-1 结合大规模无本体 UMI 预训练与少量真实机器人后训练，研究机器人策略模型的缩放行为。
  - 预训练使用 10 万小时覆盖 1700 多种场景的 UMI 轨迹数据，经 VLM 自动标注后用于学习场景状态驱动的动作生成。
  - 该模型在 RoboCasa、RoboCasa365、VLABench 和 RoboDojo 四项仿真基准测试中均达到最优结果。
  article_id: dce4de7f30cdd189
- object_type: model
  name: π0.5
  canonical_name: π0.5
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在高效适配新任务实验中，Xiaomi-Robotics-1 以不到 10 小时数据达到 75% 整体成功率，几乎翻倍于 π0.5 基线的 40%。
  - 当数据量增至不到 40 小时时，Xiaomi-Robotics-1 提升至 85%，而 π0.5 基线仅为 53%。
  article_id: dce4de7f30cdd189
extract_result: success
---

**Breaking the data barrier.** Scaling robot policy models with embodiment-free pre-training.

Foundation models in language and vision keep moving the frontier by riding empirical scaling laws: capability tracks data, parameters, and compute. Robotics has missed out. Large-scale, high-quality data is hard to come by, and that scarcity, more than anything else, has capped how far policy models could scale. What robots can do under genuinely large-scale training remained largely an open question. We take a step toward answering it. Xiaomi-Robotics-1 combines large-scale embodiment-free (UMI) pre-training with a modest amount of real-robot data in a post-training stage. We study how the model behaves as it scales.

## Data

Everything Xiaomi-Robotics-1 can do starts from data. For pre-training, we use **100,000 hours** of embodiment-free (UMI) trajectories spanning more than **1,700 scenarios** (household, commercial premises, industrial sites, and outdoor spaces), covering a diverse range of tasks. We develop a scalable auto-labeling pipeline that first divides trajectories into fixed-length segments and then annotates each segment with language descriptions of scene state transitions.

For post-training, we leverage cross-embodiment datasets containing in-house robot data, filtered open-sourced robot data, and a set of high-quality UMI data. For the in-house data, we collected over **7,200 hours** of real-robot data in real homes, covering tasks like tidying a sofa, sorting a shoe cabinet, and putting away kitchenware. The UMI data are manually annotated with temporal segments and instruction prompts, which differ from the auto-labeled state-transition descriptions used in the pre-training data.

## Method

Following the training paradigm of LLMs, the training of Xiaomi-Robotics-1 consists of two stages: pre-training and post-training. The first stage learns general representations for action generation from large-scale UMI data, while the post-training stage aligns the model with real robot embodiments and instruction-following capabilities.

### Pre-training

Pre-training is about breadth: exposing the model to as much of the real world as possible. We use the embodiment-free UMI data described above, which spans a broad range of environments and tasks. At this scale, manual labeling is infeasible. Thus, we built an automatic annotation pipeline powered by a strong vision-language model. Long videos are split into fixed-length clips, and the VLM describes the state transition of grippers and interacting objects within each clip. The result is a large-scale corpus of real-world manipulation trajectories, each annotated with precise language descriptions. These allow the model to learn action generation that drives the scene toward the state transitions described by the language.

An encouraging finding is that pre-training shows a clean scaling behavior: as data and model size grow, validation action error steadily decreases.

### Post-training

Post-training aims to align the strong action-generation capabilities acquired from pre-training with real robot embodiments and natural-language instruction following along two axes. **Embodiment alignment** uses high-quality cross-embodiment real-robot data to map the general action-generation ability onto actual robots. **Instruction alignment** shifts the model from "generating actions given a description of scene state transitions" to "understanding a natural-language instruction and executing it directly."

After post-training, Xiaomi-Robotics-1 can be used out-of-the-box to perform a wide range of mobile manipulation tasks in the real world. We evaluate the post-trained model in unseen environments with unseen object instances to understand whether the scaling behaviors from pre-training can transfer to real-robot performance after post-training.

The answer is yes. As we increase the amount of pre-training data and model size, real-robot success rate rises steadily and predictably. That is, a stronger pre-trained model yields better real-robot performance. The scaling gains show no signs of saturation: the real-robot success rate after post-training keeps improving as the model consumes more data or scales up during pre-training.

## Applications

After post-training, Xiaomi-Robotics-1 can serve as a strong robot foundation model for downstream applications. We put Xiaomi-Robotics-1 to use in two complementary downstream settings. **Efficient adaptation to new tasks** specializes the model to brand-new, highly complex real-robot tasks from a few hours of data per task. **Simulation benchmarks** probe its capabilities in mainstream suites that emphasize generalization.

### Efficient Adaptation to New Tasks

Xiaomi-Robotics-1 can learn new tasks with high data efficiency. The model picks up tasks like phone packing, printer refilling, laundry loading, and box packing from just a few hours of real-robot demonstrations per task. With **an average of under 10 hours** of demonstrations per task, it already reaches a 75% overall success rate, nearly doubling the π0.5 baseline (40%) at the same budget; raising the budget to **an average of under 40 hours** lifts overall success to 85%.

| Task | <10 h/task on average | <40 h/task on average | ||
|---|---|---|---|---|
| XR-1ours | π0.5 | XR-1ours | π0.5 | |
| Phone Packing | 70 | 30 | 80 | 40 |
| Printer Refilling | 70 | 20 | 60 | 20 |
| Laundry Loading | 80 | 40 | 100 | 50 |
| Box Packing | 80 | 70 | 100 | 100 |
| Overall | 75 | 40 | 85 | 53 |

Evaluation on efficient learning of new tasks. Each cell shows success rate (%), higher is better. XR-1 = Xiaomi-Robotics-1.

### Simulation Benchmarks

We evaluate Xiaomi-Robotics-1 on four mainstream simulation benchmarks. It achieves state-of-the-art results on all four benchmarks. The table reports the average success rate and the relative gain over second place. These results show that the generalization and scaling gains of Xiaomi-Robotics-1 carry over to standard simulation evaluation.

| Benchmark | XR-1ours | 2nd Best | Rel. Gain |
|---|---|---|---|
| RoboCasa | 74.5 | 72.6 | +2.6% |
| RoboCasa365 | 57.4 | 46.6 | +23.2% |
| VLABench | 59.1 | 53.2 | +11.1% |
| RoboDojo | 13.93 | 8.80 | +58.3% |

Simulation evaluation. All benchmarks report average success rate (%). XR-1 = Xiaomi-Robotics-1; Rel. Gain = (XR-1 − 2nd best) / 2nd best. Higher is better.

## Conclusion

Xiaomi-Robotics-1 demonstrates a practical path for scaling robot foundation models: large-scale embodiment-free UMI pre-training breaks the robot data bottleneck, while real-robot and instruction alignment transfer that general capability to physical robots. Results show that the model scales neatly with data volume and model size during pre-training, and that this scaling behavior translates directly to post-training, where a stronger pre-trained model yields better out-of-the-box real-robot performance in unseen environments. The resulting foundation model adapts to new tasks from minimal data and achieves state-of-the-art performance on four challenging simulation benchmarks that emphasize generalization.

Finally, we present an uncut footage of luggage packing.

## Citation

@article{guo2026xiaomi, title={Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories}, author={Guo, Jun and Jin, Piaopiao and Li, Jason and Li, Peiyan and Li, Yingyan and Liu, Futeng and Peng, Wanli, and Qin, Optimus and Su, Yifei and Sun, Nan and others}, journal={arXiv preprint arXiv:2607.15330}, year={2026} }