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
pipeline_stage: ingested
id: af4c4cb0aeab4921
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