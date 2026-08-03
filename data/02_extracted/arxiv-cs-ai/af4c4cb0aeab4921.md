---
title: 'Procedural Knowledge Is Not Low-Rank: Why LoRA Fails to Internalize Multi-Step
  Procedures'
source: https://arxiv.org/abs/2607.21612
author:
- '[[Simon Dennis, Kevin Shabahang, Hao Guo, Rivaan Patil]]'
published: '2026-07-27'
created: '2026-07-27'
manifest_dates:
- '2026-07-27'
description: 'arXiv:2607.21612v1 Announce Type: new Abstract: Parameter-efficient
  fine-tuning methods like LoRA have become the default for adapting large language
  models, succeeding across instruction following, style transfer, and factual adaptation.
  We show that for procedural knowledge--the ability to follow multi-step procedures
  with conditional branching through to terminal states--LoRA fails to match full
  fine-tuning at the ranks where it retains its efficiency advantage. In a systematic
  ablation (r = 16--128) on a procedural travel booking task (14 nodes), all LoRA
  configurations fail uniformly (task success <= 2.54 vs. 4.11 for full fine-tuning,
  all p < 0.001), with scores decreasing at higher ranks--despite maintaining 95--99%
  conversation completion rates. Cross-domain replication on Zoom support (14 nodes)
  and insurance claims (55 nodes) at 8B confirms the failure generalizes: LoRA underperforms
  full fine-tuning by 0.8--2.2 points on average at both r = 32 and r = 128, with
  the largest gap on the most complex procedure. Quadrupling rank from 32 to 128 provides
  marginal improvement but does not close the gap. SVD analysis of the weight changes
  produced by full fine-tuning explains why: across three domains at both 3B and 8B,
  the mean effective rank of the update ranges from 761 to 1,026, and rank 128 captures
  only 43--51% of the squared Frobenius norm. Together, these findings establish that
  for procedural tasks LoRA falls well short of full fine-tuning--a fundamental limitation
  for agentic applications.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: af4c4cb0aeab4921
source_type: academic_paper
tldr: 研究发现，参数高效微调方法LoRA在程序性知识（多步骤条件分支任务）上无法匹配全参数微调的性能，即使将秩从32提升至128也无法缩小差距，原因是全量微调的权重更新有效秩高达761-1026，低秩近似无法捕获。
objective_summary: 该论文通过在旅行预订（14节点）、Zoom客服（14节点）和保险理赔（55节点）三个程序性任务上的系统消融实验，对比了LoRA与全参数微调的性能。在8B模型规模下，LoRA在秩16-128范围内任务成功率始终显著低于全量微调（如旅行预订任务2.54
  vs 4.11，p<0.001），且更高效秩反而得分下降。SVD分析表明全量微调权重更新的平均有效秩在761-1026之间，秩128仅能捕获43-51%的Frobenius范数。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Zoom
  technologies:
  - LoRA
  - SVD
  key_people: []
key_logic_flow:
- LoRA在程序性知识——即需要多步骤条件分支并抵达终态的任务——上无法匹配全参数微调的表现。
- 在旅行预订（14节点）任务上，所有LoRA配置（秩16-128）的任务成功率均显著低于全量微调（≤2.54 vs 4.11，p<0.001），且越高的秩得分反而下降。
- 在Zoom客服（14节点）和保险理赔（55节点）两个跨域任务上，LoRA在8B模型下平均落后全量微调0.8-2.2分，差距在最复杂流程上最大。
- 将LoRA秩从32翻四倍至128仅带来微小改进，无法弥合与全参数微调的差距。
- SVD分析揭示根本原因：全量微调权重更新的平均有效秩在761-1026之间，秩128仅能捕获43-51%的Frobenius范数。
- 这些发现表明程序性任务对低秩近似存在根本性限制，对智能体应用具有重要影响。
object_mentions:
- object_type: paper
  name: 'Procedural Knowledge Is Not Low-Rank: Why LoRA Fails to Internalize Multi-Step
    Procedures'
  canonical_name: Procedural Knowledge Is Not Low-Rank
  url: https://arxiv.org/abs/2607.21612
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文通过系统消融实验证明，在程序性知识任务上LoRA在所有高效秩范围内均显著落后于全参数微调。
  - SVD分析表明全量微调权重更新的有效秩远超LoRA所能捕获的范围，解释了低秩近似在程序性任务上的根本性失效。
  - 跨三个域（旅行预订、Zoom客服、保险理赔）的复制实验确认该失败模式具有泛化性。
  article_id: af4c4cb0aeab4921
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Procedural Knowledge Is Not Low-Rank: Why LoRA Fails to Internalize Multi-Step Procedures

View PDF HTML (experimental)Abstract:Parameter-efficient fine-tuning methods like LoRA have become the default for adapting large language models, succeeding across instruction following, style transfer, and factual adaptation. We show that for procedural knowledge--the ability to follow multi-step procedures with conditional branching through to terminal states--LoRA fails to match full fine-tuning at the ranks where it retains its efficiency advantage. In a systematic ablation (r = 16--128) on a procedural travel booking task (14 nodes), all LoRA configurations fail uniformly (task success <= 2.54 vs. 4.11 for full fine-tuning, all p < 0.001), with scores decreasing at higher ranks--despite maintaining 95--99% conversation completion rates. Cross-domain replication on Zoom support (14 nodes) and insurance claims (55 nodes) at 8B confirms the failure generalizes: LoRA underperforms full fine-tuning by 0.8--2.2 points on average at both r = 32 and r = 128, with the largest gap on the most complex procedure. Quadrupling rank from 32 to 128 provides marginal improvement but does not close the gap. SVD analysis of the weight changes produced by full fine-tuning explains why: across three domains at both 3B and 8B, the mean effective rank of the update ranges from 761 to 1,026, and rank 128 captures only 43--51% of the squared Frobenius norm. Together, these findings establish that for procedural tasks LoRA falls well short of full fine-tuning--a fundamental limitation for agentic applications.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.