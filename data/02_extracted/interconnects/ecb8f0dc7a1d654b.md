---
title: 'GLM-5.3: How Chinese labs keep stride with the frontier'
source: https://www.interconnects.ai/p/glm-53-how-chinese-labs-keep-stride
author:
- '[[Nathan Lambert]]'
published: '2026-08-14'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
- '2026-08-16'
- '2026-08-17'
- '2026-08-18'
- '2026-08-19'
- '2026-08-20'
- '2026-08-21'
description: 'Hint: It&#8217;s really not a distillation story.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ecb8f0dc7a1d654b
source_type: newsletter_rss
tldr: Z.ai 发布 GLM-5.3 模型，参数量约 750B，与 GLM-5.2 共用基础模型并仅扩展后训练，在多个基准上超越 Kimi K3，部分超过 Claude
  Fable 5 与 GPT-5.6-Sol。该模型两周后将以开放权重上线 Hugging Face。
objective_summary: Z.ai（智谱）今日宣布发布 GLM-5.3 模型，目前仅在其编程套餐中提供，后续将上线 API，并计划两周后以开放权重形式发布到
  Hugging Face。该模型与 GLM-5.2 共用相同基础模型，仅大幅扩展后训练，参数量约 750B，约为 Kimi K3 的三分之一。在基准测试上它超越
  Moonshot AI 的 Kimi K3，部分基准上超过 Claude Fable 5 或 GPT-5.6-Sol。作者分析认为 Z.ai 的优势在后训练能力，而
  Kimi 更偏向预训练杰作，这解释了其小参数模型如何匹配美国前沿模型。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Z.ai
  - Moonshot AI
  - THUDM
  - Tsinghua University
  - Hugging Face
  - Anthropic
  - OpenAI
  technologies:
  - GLM
  - GLM-5.3
  - GLM-5.2
  - Kimi K3
  - post-training
  - agentic coding
  key_people: []
key_logic_flow:
- Z.ai 今日宣布发布 GLM-5.3 模型，目前仅在编程套餐中提供，后续将上线其 API，并计划两周后以开放权重形式发布到 Hugging Face。
- GLM-5.3 与 GLM-5.2 共用相同基础模型，仅大幅扩展了后训练，参数量约 750B，约为 Moonshot AI 的 Kimi K3 的三分之一。
- GLM-5.3 在多个基准测试上超越 Kimi K3，部分基准上超过 Claude Fable 5 或 GPT-5.6-Sol，处于智能体编程基准的前沿水平。
- 作者分析认为 Z.ai 的优势在于后训练能力，而 Kimi 更偏向预训练杰作，这解释了小参数模型如何匹配美国领先模型。
- GLM 系列历史沿革清晰：2019 年智谱成立，2021 年 THUDM 发布 GLM，历经 GLM-130B、ChatGLM 系列、GLM-4、GLM-5，至
  2026 年 6 月发布 GLM-5.2。
- GLM-5.2 因速度快、无回滚等特性，在发布后数周仍被 AI 研究者广泛使用，证明了该模型系列的实用性。
object_mentions:
- object_type: model
  name: GLM-5.3
  canonical_name: GLM-5.3
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Z.ai 今日宣布发布 GLM-5.3 模型，目前仅在编程套餐中提供，之后将上线 API，并计划两周后以开放权重形式发布到 Hugging Face。
  - GLM-5.3 与 GLM-5.2 共用相同基础模型，仅大幅扩展后训练，参数量约 750B，约为 Kimi K3 的三分之一。
  - GLM-5.3 在多个基准测试上超越 Moonshot AI 的 Kimi K3，部分基准上超过 Claude Fable 5 或 GPT-5.6-Sol。
  article_id: ecb8f0dc7a1d654b
- object_type: model
  name: GLM-5.2
  canonical_name: GLM-5.2
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - GLM-5.2 于今年 6 月 22 日发布并引起广泛关注，因其速度快且简单无回滚，发布数周后仍有 AI 研究者持续使用。
  - GLM-5.3 是在 GLM-5.2 基础上扩展后训练的迭代版本，两者共享同一基础模型。
  article_id: ecb8f0dc7a1d654b
- object_type: model
  name: Kimi K3
  canonical_name: Kimi K3
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - GLM-5.3 在多个基准上超越 Moonshot AI 的 Kimi K3，而 Kimi K3 的参数量约为 GLM-5.3 的三倍。
  - 作者将 Kimi K3 称为预训练杰作，认为其在预训练上更擅长，而 Z.ai 的优势在于后训练。
  article_id: ecb8f0dc7a1d654b
- object_type: model
  name: Claude Fable 5
  canonical_name: Claude Fable 5
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GLM-5.3 在部分基准测试上超越了 Claude Fable 5，这是文章用于衡量其前沿水平的美国公开模型之一。
  article_id: ecb8f0dc7a1d654b
- object_type: model
  name: GPT-5.6-Sol
  canonical_name: GPT-5.6-Sol
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GLM-5.3 在部分基准测试上超越了 GPT-5.6-Sol，这是文章用于对比其性能的另一美国前沿模型。
  article_id: ecb8f0dc7a1d654b
- object_type: company
  name: Z.ai
  canonical_name: Z.ai
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Z.ai（智谱）成立于 2019 年，自 2021 年起经 THUDM 发布 GLM 系列模型，作者认为其相比 Kimi 更擅长后训练。
  - Z.ai 在官方博客中称扩展后训练是 GLM-5.3 的全部工作，并称其几乎处于智能体编程基准的前沿。
  article_id: ecb8f0dc7a1d654b
extract_result: success
---

# GLM-5.3: How Chinese labs keep stride with the frontier

### Hint: It’s really not a distillation story.

##### Housekeeping: I’m traveling so cannot make a voiceover for this post. EDIT — I added a bullet point 5 on the Chinese data industry after sending the email out.

Today, Z.ai announced their GLM-5.3 model, currently only available in the coding plan, coming soon to their API and in two weeks’ time to Hugging Face (open weights). This model looks exceptional, with a somewhat astounding increase in scores. On many benchmarks the model has surpassed Moonshot AI’s Kimi K3 and on some it’s surpassed Claude Fable 5 or GPT-5.6-Sol.

Here’s a more complete comparison:

This puts the model more or less at the frontier of agentic coding benchmarks, with only ~750B parameters – a third of Kimi K3! The Z.ai blog post is rather straightforward, and starts with a bold sentence:

Scaling post-training is all we did for GLM-5.3.


GLM-5.3 is the same base model as GLM-5.2 with substantially extended post-training. To risk a broad oversimplification, Z.ai seems to have a strength in post-training when compared to Kimi, which is more of a pretraining masterpiece. Following this release there have been a lot of discussions wondering how China can keep up so well? How can such a small model be matching the leading public American models? Are these results real?

The simplest explanation is that Z.ai is very good at what they do – it’s worth recalling that they’ve been working on this line of models longer than almost anyone in the industry. Here’s a brief history of the GLM models.

**Zhipu AI Founded**– 2019

**GLM**(General Language Model) — March 2021 — released by**THUDM**, Tsinghua University’s Data Mining / Knowledge Engineering group. Weights**GLM-130B**— August 2022 — Scaled version. Technical report for GLM-130B through GLM-4 — Weights**ChatGLM**— March 14, 2023 — first chat version. Weights**ChatGLM2**— June 25, 2023 — Weights**ChatGLM3**— October 27, 2023 — Weights**GLM-4**— January 16, 2024 — rebranded as just GLM; open-weight GLM-4-9B followed in June. Weights**GLM-5**— February 11, 2026 — latest major generation. Weights

GLM 5.2, released on June 22 of this year, was a big deal – weeks after the release, I regularly heard from AI researchers I know who still used the model due to its speed (some deploy the model on internal clusters for faster speeds than public offerings) and simplicity (as a model with no rollbacks, etc., when working on frontier AI systems). GLM-5.2 altogether stood up to the hype.