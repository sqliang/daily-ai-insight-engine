---
title: Can tech companies learn to love cheaper AI models?
source: https://techcrunch.com/2026/06/09/can-tech-companies-learn-to-love-cheaper-models/
author:
- '[[Russell Brandom]]'
published: '2026-06-09'
created: '2026-06-10'
description: If those same AI workloads can be handled by cheaper models without affecting
  quality, it would mean a massive shift in the economics of AI.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b4c83c3dc96abd8b
source_type: news_media
tldr: AI行业长期信奉"模型越大越强"，但成本压力正促使企业转向更便宜的小模型。Coinbase联合创始人Brian Armstrong预测80%的工作负载将在12-18个月内转移到便宜99%的模型上，法律AI工具Harvey的实测已证实成本可降3倍而不牺牲质量。
objective_summary: TechCrunch报道了AI行业从追求旗舰大模型向经济型小模型转变的趋势，核心驱动力是不断攀升的推理成本。Coinbase联合创始人Brian
  Armstrong预测未来12-18个月内80%的工作负载将运行在便宜99%的模型上。法律AI工具Harvey与推理平台Fireworks AI合作测试，通过组合Claude
  Opus和Fireworks的GLM 5.1并仅对最密集任务使用Opus，将推理成本降低3倍且质量未下降。文章指出真正的分界线不在于闭源与开源模型之间，而在于大模型与小模型之间。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Coinbase
  - Harvey
  - Fireworks AI
  - OpenAI
  - Anthropic
  - DeepSeek
  - TechCrunch
  technologies:
  - GLM 5.1
  - Claude Opus
  - GPT-5.5
  - DeepSeek V4 Flash
  - GPT-5.4-mini
  key_people:
  - Brian Armstrong
  - Gabe Pereyra
key_logic_flow:
- AI行业长期以来的假设是模型越大越强、最强大的模型获胜，但成本压力正在打破这一假设并迫使企业重新审视更小更便宜的模型。
- Coinbase联合创始人Brian Armstrong在X上预测，未来12-18个月内80%的工作负载将运行在便宜99%的模型上，仅20%需要最新旗舰模型。
- 法律AI工具Harvey与推理平台Fireworks AI合作测试，通过组合Claude Opus和Fireworks的GLM 5.1并对最密集任务使用Opus，将推理成本降低了3倍且未降低质量。
- Harvey联合创始人Gabe Pereyra表示质量的定义正在从简单的使用最强模型演变为使用能最高效得到正确答案的最佳模型。
- 真正的行业分界线不在于闭源模型与开源模型之间，而在于大模型与小模型之间，从GPT-5.5切换到DeepSeek V4 Flash或切换到GPT-5.4-mini都能节省成本。
- 大小模型之间的价格战正在大实验室的内部推理和独立服务的开源权重模型之间激烈进行，但无论哪种小模型胜出都不影响小模型替代大模型的宏观趋势。
extract_result: success
object_mentions:
- object_type: product
  name: Harvey
  canonical_name: Harvey
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 法律AI工具Harvey与推理平台Fireworks AI合作进行测试，通过组合Claude Opus和Fireworks的GLM 5.1，将推理成本降低了3倍且未降低质量。
  - Harvey联合创始人Gabe Pereyra对TechCrunch表示，质量的定义正在从为所有任务使用最强模型演变为使用能最高效得到正确答案的最佳模型。
  article_id: b4c83c3dc96abd8b
- object_type: company
  name: Fireworks AI
  canonical_name: Fireworks AI
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 推理平台Fireworks AI与Harvey合作提供GLM 5.1模型，在与Claude Opus组合的测试中帮助Harvey实现了3倍的推理成本降低。
  - 文章指出独立服务的开源权重模型与各大AI实验室的内部推理之间正在展开一场价格战。
  article_id: b4c83c3dc96abd8b
- object_type: model
  name: Claude Opus
  canonical_name: Claude Opus
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Harvey在测试中将Claude Opus用于最密集的任务，同时使用Fireworks的GLM 5.1处理常规任务，显著降低了服务端负载和总体成本。
  article_id: b4c83c3dc96abd8b
- object_type: model
  name: GLM 5.1
  canonical_name: GLM 5.1
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Fireworks AI的GLM 5.1与Claude Opus组合使用，在Harvey的测试中承担非密集型任务，实现了成本降低而不牺牲质量。
  article_id: b4c83c3dc96abd8b
- object_type: model
  name: DeepSeek V4 Flash
  canonical_name: DeepSeek V4 Flash
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章将DeepSeek V4 Flash作为便宜模型的代表，指出从GPT-5.5切换到DeepSeek V4 Flash可以节省推理成本。
  article_id: b4c83c3dc96abd8b
- object_type: model
  name: GPT-5.4-mini
  canonical_name: GPT-5.4-mini
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章指出从GPT-5.5切换到GPT-5.4-mini同样可以节省成本，强调节省的关键在于选择小模型而非区分闭源与开源。
  article_id: b4c83c3dc96abd8b
---

The AI boom has been built on a basic assumption: Bigger models are more powerful, and the most powerful models win. Now, the industry is about to learn what happens if that assumption starts to break.

Mounting costs have already pressured users to give smaller and cheaper models a second look. This cost-conscious model-shopping is new and it’s unclear how it will affect the industry, but the impact is likely to be significant.

One prediction, laid out best by Coinbase co-founder Brian Armstrong, is that it will result in the vast majority of tasks shifting to cheaper models.

“[D]emand for intelligence is near infinite, but 80% of workloads will be running on 99% cheaper models within 12-18 months,” Armstrong wrote on X. “20% of workloads will still run on latest gen models where IQ maxing is important.”

It’s hard to overstate what a significant shift it will be for the AI industry if Armstrong’s prediction comes true.

Before now, most AI companies have competed on quality, which has meant defaulting to the most advanced available model. If those same jobs can be handled by cheaper models without affecting quality, it would mean a massive shift in the economics of AI. And critically, much of the savings would be coming out of the pockets of the big labs, dealing a financial blow to OpenAI and Anthropic just as they’re heading for their IPOs.

It’s a potentially seismic change in the industry, resting on one basic question: Are companies ready to switch to smaller models?

Initial tests suggest that, when the system is arranged right, cheaper models could sub in without any sacrifice in quality. In a recent test by the legal AI tool Harvey, the company was able to reduce inference costs by 3x without reducing quality. The test, performed in partnership with the inference platform Fireworks AI, combined Claude Opus and Fireworks’ GLM 5.1, and shifted to Opus for the most intensive tasks. The result was a significantly lower load in terms of server time and overall cost.

“Quality comes first, and in legal it always will,” Harvey co-founder Gabe Pereyra told TechCrunch, referring to the AI legal services his startup provides. “However, the definition of quality is evolving from simply using the most powerful model for everything, to using the best model that gets the right answer most efficiently.”

This trend is often framed in terms of major labs versus Chinese models or open-weight ones, but that misses the bigger point. The real divide isn’t between proprietary and open models; it’s between large models and small ones. You can save money by switching from GPT-5.5 to DeepSeek’s V4 Flash, but switching to GPT-5.4-mini works just as well.

There’s an active price war going on between in-house inference from the big labs and independently served open-weight models. For the bigger question of small versus large, it doesn’t really matter which kind of small model wins out.