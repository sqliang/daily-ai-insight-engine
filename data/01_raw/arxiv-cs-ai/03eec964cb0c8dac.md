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
pipeline_stage: ingested
id: 03eec964cb0c8dac
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