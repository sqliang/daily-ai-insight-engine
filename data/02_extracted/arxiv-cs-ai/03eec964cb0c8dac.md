---
title: 'When the Judge Should Not Decide: Evidence-Locked, Non-Compensatory Selection
  Bounds LLM-Judge Failure in Reasoning Pipelines'
source: https://arxiv.org/abs/2608.07813
author:
- '[[Yiyao Zhang, Diksha Goel, Hussain Ahmad, Shixun Huang, Jun Shen]]'
published: '2026-08-12'
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 03eec964cb0c8dac
source_type: academic_paper
tldr: 该研究指出推理管道中 LLM judge 的决策规则比其准确率更能决定最终输出质量，并提出 Evidence-Locked Derive-Gate-Repair（EL-DGR）非补偿性选择规则，在
  GSM8K 和 HotpotQA 上相比首个候选 GRPO 结果分别提升约 2.8 个百分点和 2.00 EM，同时有效限制错误 judge 的破坏范围。
objective_summary: 论文在四个 GRPO 策略生成的冻结候选池上，评估 DeepSeek-R1-7B 作为无约束标量 judge 的表现，发现其在
  500 道 GSM8K 题上仅比答案级多数投票高 1.0 个百分点，在 300 道 HotpotQA 题上仅高 0.34 EM，且在 30 题确认集上比多数投票低
  10 个百分点。作者据此提出 EL-DGR 规则，要求 judge 只有在提供抽取式证据证书时才能推翻证据支持的共识，并仅在两个候选均未获证且修复方案获证时才执行修复。在不改变
  judge、候选池和预算的情况下，EL-DGR 在 GSM8K 上达到 58.2%，在 HotpotQA 上达到 17.33 EM / 25.46 F1，显著优于
  judge 本身和多数投票基线。决策审计还显示，EL-DGR 在 30 个试点问题中仅推翻 8 次共识，且从未将正确共识转化为错误答案。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM judge
  - GRPO
  - DeepSeek-R1-7B
  - Evidence-Locked Derive-Gate-Repair
  - EL-DGR
  - GSM8K
  - HotpotQA
  key_people: []
key_logic_flow:
- LLM judge 在推理管道中不仅评估答案质量，还直接决定哪个答案被输出，因此其嵌入的决策规则比 judge 本身的准确率更关键。
- 在冻结的 GRPO 候选池上，无约束标量 DeepSeek-R1-7B judge 相比答案级多数投票提升微弱，甚至在确认集上降低准确率。
- 作者提出 Evidence-Locked Derive-Gate-Repair（EL-DGR），一种任务自适应的非补偿性选择规则，约束 judge 的决策权限。
- EL-DGR 要求 judge 只有在提供抽取式证据证书时，才能推翻证据支持的共识。
- 修复操作仅在两个候选均未获证且修复方案本身获证时才被触发。
- 在不改变 judge、候选池和预算的条件下，EL-DGR 在 GSM8K 和 HotpotQA 上均显著优于 judge 本身、多数投票和首个候选基线。
- 决策审计显示 EL-DGR 在 30 个试点问题中仅推翻 8 次共识，且从未将正确共识转化为错误答案。
- 将同样的七通道分解作为步骤级门控训练奖励时效果为空，且通道丢弃消融显示没有单一通道是必要的。
object_mentions:
- object_type: paper
  name: 'When the Judge Should Not Decide: Evidence-Locked, Non-Compensatory Selection
    Bounds LLM-Judge Failure in Reasoning Pipelines'
  canonical_name: arXiv:2608.07813
  url: https://arxiv.org/abs/2608.07813
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - '论文标题为 When the Judge Should Not Decide: Evidence-Locked, Non-Compensatory Selection
    Bounds LLM-Judge Failure in Reasoning Pipelines，发表于 arXiv。'
  - 文章摘要系统阐述了 LLM judge 在推理管道中的决策作用，以及 EL-DGR 方法在 GSM8K 和 HotpotQA 上的实验结果。
  - 该论文给出了明确的实验数据，包括 GSM8K 上 58.2% 的准确率和 HotpotQA 上 17.33 EM / 25.46 F1 的表现。
  article_id: 03eec964cb0c8dac
- object_type: project
  name: Evidence-Locked Derive-Gate-Repair (EL-DGR)
  canonical_name: EL-DGR
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者提出 Evidence-Locked Derive-Gate-Repair（EL-DGR），一种任务自适应的非补偿性规则，用于约束 LLM judge
    在推理管道中的决策权限。
  - EL-DGR 要求 judge 偏好只有在附带抽取式证据证书时，才能推翻证据支持的候选共识。
  - 在 EL-DGR 规则下，修复操作仅在两个候选均未获证且修复方案获证时才会执行。
  article_id: 03eec964cb0c8dac
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:When the Judge Should Not Decide: Evidence-Locked, Non-Compensatory Selection Bounds LLM-Judge Failure in Reasoning Pipelines

View PDF HTML (experimental)Abstract:An LLM judge deployed inside a reasoning pipeline does not merely measure quality, it decides which answer ships. We show that the cost of that decision depends less on judge accuracy than on the decision rule the judge is embedded in. On frozen candidate pools from four GRPO policies, an unconstrained scalar DeepSeek-R1-7B judge buys almost nothing over answer-level majority vote (+1.0 pp on 500 GSM8K questions, +0.34 EM on 300 HotpotQA questions), and on a frozen-rule 30-question confirmation split it is 10 points worse than majority, a judge that destroys accuracy while scoring candidates confidently. We then subordinate the same judge to Evidence-Locked Derive-Gate-Repair (EL-DGR), a task-adaptive non-compensatory rule under which a judge preference may override evidence-supported consensus only with an extractive evidence certificate, and a repair only when neither alternative is certified and the repair is. With no change to the judge, the candidates, or the budget, EL-DGR reaches 58.2% on GSM8K (vs. 56.8% judge, 55.8% majority, 55.4% first candidate) and 17.33 EM / 25.46 F1 on HotpotQA (vs. 15.67/23.49, 15.33/23.19, 15.33/22.97), improving on first-candidate GRPO by +2.8 pp (exact McNemar p=0.0026) and +2.00 EM (p=0.070, borderline). A decision audit shows why: EL-DGR overturns consensus on only 8 of 30 pilot questions and never converts a correct consensus into an incorrect answer. We also report what did not work: the same seven-channel decomposition used as a step-level gated training reward is null, and corrected channel-drop ablations show no channel is individually necessary (p=1.0 throughout). The practitioner-facing finding is negative about judges and positive about admissibility, bound the judge's blast radius rather than trying to make it accurate.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.