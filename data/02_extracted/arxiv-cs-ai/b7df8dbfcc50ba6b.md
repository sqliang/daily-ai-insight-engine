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