---
title: 'Marking the Wrong Symptoms: Evaluating LLM Watermarks in Medical Texts'
source: https://arxiv.org/abs/2607.20462
author:
- '[[Melanie Rieff, Robin Staab, Thibaud Gloaguen, Stefan Hegselmann, Martin Vechev]]'
published: '2026-07-24'
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
description: 'arXiv:2607.20462v1 Announce Type: new Abstract: Large language models
  (LLMs) are increasingly integrated into clinical workflows, stressing the need for
  reliable traceability of model-generated output with watermarking. Yet, most watermarks
  are evaluated on general-purpose benchmarks, leaving domains like medicine, where
  small token-level perturbations can result in significant semantic changes, underexplored.
  In this work, we present the first rigorous study of how LLM watermarks affect medical
  performance, benchmarking 5 watermarking schemes across 11 LLMs and 7 VLMs on various
  tasks spanning unimodal and multimodal clinical reasoning. Importantly, we complement
  existing evaluations by introducing a human-expert-validated pipeline for systematically
  auditing medical reasoning quality, terminological precision, and induced hallucinations.
  Our results reveal that watermarking can induce substantial degradation across multiple
  failure modes, including lexical corruption, hallucinated terminology, and amplified
  misattribution or omission of image findings. Notably, we find that the absence
  of domain-specific analyses, combined with aggregate metrics that miss failures
  inherent to clinical text, can systematically obscure practical watermark-induced
  degradations. Our findings establish domain-specific evaluation as a prerequisite
  for the safe deployment of watermarked models in medicine, where current benchmarks
  can otherwise mask clinically consequential failures.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b7df8dbfcc50ba6b
source_type: academic_paper
tldr: 该论文首次系统评估了LLM水印技术对医学文本性能的影响，在11个LLM和7个VLM上基准测试了5种水印方案，发现水印会导致词汇损坏、幻觉术语和图像发现归因错误等严重退化，且通用指标无法捕捉这些临床关键缺陷。
objective_summary: 研究人员在11个LLM和7个VLM上对5种水印方案进行了系统基准测试，涵盖单模态和多模态临床推理任务。他们引入了一个经人类专家验证的流水线，用于审计医学推理质量、术语精确度和诱导幻觉。结果表明水印会引发词汇损坏、幻觉术语以及图像发现的错误归因或遗漏，而缺乏领域特定分析的聚合指标会掩盖这些实际退化。研究结论认为领域特定评估是水印模型在医学中安全部署的前提条件。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - arXiv
  technologies:
  - LLM Watermarking
  - VLM
  - Clinical Reasoning
  key_people: []
key_logic_flow:
- 该论文首次系统研究了LLM水印对医学文本性能的影响，此前的水印评估主要集中在通用基准上。
- 研究在11个LLM和7个VLM上对5种水印方案进行了基准测试，覆盖单模态和多模态临床推理任务。
- 研究引入了一个经人类专家验证的审计流水线，用于系统评估医学推理质量、术语精确度和诱导幻觉。
- 结果发现水印会导致多种失效模式，包括词汇损坏、幻觉术语以及图像发现的错误归因或遗漏。
- 缺乏领域特定分析的聚合指标会系统性地掩盖水印引起的实际性能退化。
- 研究结论指出领域特定评估是水印模型在医学领域安全部署的必要前提。
object_mentions: []
extract_result: success
impact_score:
  score: 6.2
  reason: 该论文首次系统评估了LLM水印在医学领域的实际影响，揭示了此前被通用基准掩盖的关键失效模式（词汇损坏、幻觉术语、图像发现错误归因）。这一发现对水印技术的安全部署和医疗AI监管审批具有直接指导意义，可能改变水印评估范式和医疗AI产品合规路径。但论文本身属于评估/审计类研究，未提出新的水印技术或医学模型，冲击力局限在水印安全评估和医疗AI部署两大交叉领域，未达到行业范式转移级别。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: 水印技术在医学场景中引发幻觉和术语损坏，且通用评估指标系统性地掩盖这些临床关键缺陷
hype_assessment:
  level: low
  reason: 该论文是严谨的学术基准研究工作，在11个LLM和7个VLM上对5种水印方案进行系统测试，引入经人类专家验证的审计流水线，结论有充分实验数据支撑，未使用任何营销性或PR夸张词汇。
information_entropy: high
domain_disruption:
  technical_innovation: 首次构建了经医学专家验证的域特定水印评估流水线，系统性地揭示了水印在临床推理任务中导致的词汇损坏、术语幻觉和图像发现归因错误等多种失效模式，证明了通用聚合指标无法捕捉这些对临床安全至关重要的退化。
  business_model: 对医疗AI产品的合规部署构成实质性警示——若无域特定的水印安全性评估，AI生成内容的可追溯性机制本身可能引入临床误诊风险，这将影响医疗AI产品的监管审批要求和保险责任界定。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 该论文首次系统性地揭示了LLM水印技术在医学高保真场景中的严重退化问题（词汇损坏、幻觉术语、图像归因错误），为医疗AI的投资和部署提供了关键风险锚点。从中长期看：(1)
    它创造了'领域特异性水印评估'这一新需求缺口，催生专业评估工具和合规框架的市场空间，相关服务商将受益于监管趋严的趋势；(2) 结论大概率成为医疗AI部署水印的标准前置条件，影响行业技术选型和监管走向，具备持久的参考价值；(3)
    但作为一篇诊断性学术论文而非产品创新，其复利效应依赖于产业界对其结论的采纳与转化速度，本身不具备直接商业回报的指数增长曲线。综合判断为中等偏上的长期影响力，但非直接复利型资产。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- 医疗AI合规与评估工具公司
- Hippocratic AI
- OpenAI
- Anthropic
- 专业医学AI评测服务商
competitive_casualty:
- 通用型LLM水印技术提供商
- 缺乏领域验证即部署水印的医疗AI厂商
- 仅使用通用基准评估水印质量的模型服务商
market_opportunities:
- 医疗AI质量审计工具——基于该论文的审计流水线，可开发面向医疗AI部署的专用水印安全性评测SaaS，检测词汇损坏、幻觉术语和归因错误等临床关键缺陷
- 领域自适应水印方案——针对医学等高敏感性领域，研发保留领域语义完整性的新型水印算法，满足监管溯源需求的同时避免性能退化
- 评估基准即服务(BaaS)——构建经人类专家验证的医学AI评估基准数据集与评估流水线，为医疗AI厂商和监管机构提供合规性验证服务
risk_matrix:
  regulatory: 全球监管趋严（FDA医疗AI审批、EU AI Act对高风险系统的水印要求、中国生成式AI标识规定）背景下，部署未经验证的通用水印方案可能导致合规风险——监管要求溯源但水印本身可能引发医疗质量事故，形成合规悖论
  technological: 现有通用水印技术在医学领域系统性失效且该缺陷被聚合指标掩盖，可能误导行业滥用不成熟的水印方案；同时该论文未提出修复方案，技术替代窗口期不确定
  competitive: 医疗AI赛道中，早期忽视水印质量影响的厂商可能因临床事故面临信任危机，而率先推出领域适配水印方案的厂商将获取竞争优势，形成市场洗牌压力
  ethical: 水印引起的幻觉术语和图像发现归因错误直接威胁患者安全；如果带有缺陷水印的医疗AI生成错误诊断或遗漏关键发现，将造成不可逆的临床伤害；医疗AI厂商可能在不了解风险的情况下部署水印，引发系统性伦理危机
  additional:
  - 就业冲击——如果水印缺陷导致医疗AI信任危机，可能延迟AI在医疗领域的落地速度，影响已投入的AI医疗人才和基础设施
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:Marking the Wrong Symptoms: Evaluating LLM Watermarks in Medical Texts

View PDF HTML (experimental)Abstract:Large language models (LLMs) are increasingly integrated into clinical workflows, stressing the need for reliable traceability of model-generated output with watermarking. Yet, most watermarks are evaluated on general-purpose benchmarks, leaving domains like medicine, where small token-level perturbations can result in significant semantic changes, underexplored. In this work, we present the first rigorous study of how LLM watermarks affect medical performance, benchmarking 5 watermarking schemes across 11 LLMs and 7 VLMs on various tasks spanning unimodal and multimodal clinical reasoning. Importantly, we complement existing evaluations by introducing a human-expert-validated pipeline for systematically auditing medical reasoning quality, terminological precision, and induced hallucinations. Our results reveal that watermarking can induce substantial degradation across multiple failure modes, including lexical corruption, hallucinated terminology, and amplified misattribution or omission of image findings. Notably, we find that the absence of domain-specific analyses, combined with aggregate metrics that miss failures inherent to clinical text, can systematically obscure practical watermark-induced degradations. Our findings establish domain-specific evaluation as a prerequisite for the safe deployment of watermarked models in medicine, where current benchmarks can otherwise mask clinically consequential failures.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.