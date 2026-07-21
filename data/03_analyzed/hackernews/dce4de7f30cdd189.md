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
impact_score:
  score: 7.8
  reason: 该事件展示了机器人基础模型领域的重要突破：首次在大规模（10万小时）无本体预训练数据上验证了缩放定律（scaling laws）在机器人策略模型中的有效性，且缩放增益直接迁移至真实机器人后训练性能。四项仿真基准全面SOTA，新任务适配效率（10小时达75%成功率）近乎翻倍于π0.5基线（40%）。这一两阶段训练范式（无本体预训练+真实机器人后训练）效仿LLM发展路径，可能改变机器人策略模型的研发范式。但当前仅在移动操作领域验证，且为单家公司的研究成果，尚不及ChatGPT级别的范式转移（8-10分），因此评为7.8分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 无本体UMI预训练的缩放定律是否能在更广泛的机器人形态和任务上复现
hype_assessment:
  level: low
  reason: 文章整体风格偏技术论文式严谨，提供了充分的实验数据支撑（100K小时数据量、1700+场景覆盖、四项基准SOTA对比、与π0.5的消融对比、缩放曲线可视化）。未出现'革命性''颠覆'等PR滥用词汇，仅以'breaking
    the data barrier'作为引子且后续用具体实验验证。结论均基于量化实验，无空洞宣言。
information_entropy: high
domain_disruption:
  technical_innovation: 首次在机器人策略模型上验证了大规模无本体（UMI）预训练的缩放定律——预训练阶段的验证动作误差随数据量和模型规模增长稳定下降，且这一缩放规律直接迁移至后训练阶段的真实机器人成功率。这一发现打破了'机器人领域因数据稀缺无法规模化训练'的认知瓶颈。
  business_model: 小米以Robotics-1基础模型入局机器人赛道，可能加速消费级机器人应用落地。新任务适配仅需10-40小时演示数据（75%-85%成功率），大幅降低了机器人部署的时间与人工成本，有望催生'基础模型+少量微调'的机器人SaaS服务模式，改变行业'每任务从零训练'的高成本现状。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 论证过程：首先，该论文的核心突破在于实证证明了机器人策略模型存在与LLM类似的缩放定律（scaling laws）——预训练验证误差随数据量和模型规模增长稳定下降，且该优势可直接迁移至真实机器人成功率。这意味着机器人VLA赛道可能从'算法创新竞赛'转向'数据与算力规模竞赛'，效仿大语言模型的发展路径，具备极强的长期复利效应。其次，10万小时无本体（UMI）预训练数据的规模量级远超此前行业标准（通常数千小时），大幅突破了真实机器人数据采集瓶颈这一行业关键制约因素。第三，不到10小时演示即可达75%成功率的高效适配能力，意味着下游部署成本大幅降低，加速了从实验室到商业化落地的路径。但风险因素不可忽视：小米在AI研究领域的持续投入尚未形成品牌信任背书，过往AI产品落地节奏偏慢；硬件多样性导致的实体对齐问题可能限制缩放定律的跨平台普适性；Google
    DeepMind、Tesla、Physical Intelligence等竞争对手具备同等或更强的资金和数据获取能力。综合评定7.5分——方向性正确且有实证支持的范式级突破，但距'3-5年大概率成为行业基石'的确定性尚有距离，需持续跟踪后续复现验证和产品化进展。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Xiaomi
- NVIDIA
competitive_casualty:
- Physical Intelligence
- 小型机器人VLA创业公司
market_opportunities:
- 家居服务机器人开发商可基于该模型的少样本适应能力（不到10小时数据达75%成功率）快速推出面向整理收纳、厨房清洁等垂直场景的机器人产品
- 工业与商业场景的企业可借助该模型的跨场景预训练能力，以极低的采集成本适配手机包装、打印机加粉、洗衣等重复性操作任务
- 机器人数据标注与仿真测试服务商可围绕该模型的大规模UMI自动标注流水线和四项仿真基准测试需求，提供数据采集、标注优化与评估服务
risk_matrix:
  regulatory: 家用机器人进入真实家庭环境可能触发隐私保护和数据安全法规（如家庭内部视频数据采集与存储），以及具身智能安全标准尚未完善的监管不确定性
  technological: UMI无本体预训练依赖大规模、高质量轨迹数据，若开源社区或竞争对手推出更高效的数据合成方法或更优的架构方案，可能削弱该模型的技术领先性
  competitive: 谷歌RT系列、特斯拉Optimus、Figure等全球玩家在具身智能赛道竞争激烈，小米面临生态整合能力和工业落地经验的挑战，且国内宇树、星动纪元等创业公司正在快速追赶
  ethical: 家用机器人大规模部署可能替代家政、仓储等领域的低技能劳动力岗位，同时家庭环境数据采集存在泄露用户生活习惯和隐私的风险
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
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