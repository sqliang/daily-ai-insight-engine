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
tldr: AI行业预测80%工作负载将在12-18个月内迁移到价格便宜99%的小模型
objective_summary: TechCrunch报道了AI行业从追求最大模型向成本敏感型模型选择的转变趋势。Coinbase联合创始人Brian Armstrong预测80%的AI工作负载将在12-18个月内转向便宜99%的模型。法律AI工具Harvey与Fireworks
  AI合作测试显示，组合使用Claude
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Coinbase
  - Harvey
  - Fireworks AI
  - OpenAI
  - Anthropic
  - TechCrunch
  technologies:
  - Claude Opus
  - GLM 5.1
  - GPT-5.5
  - DeepSeek V4 Flash
  - GPT-5.4-mini
  key_people:
  - Brian Armstrong
  - Gabe Pereyra
key_logic_flow:
- AI行业长期以来以"模型越大越强"为基本假设，但不断攀升的成本正迫使企业重新审视更小、更便宜的模型。
- Coinbase联合创始人Brian Armstrong预测，未来12-18个月内80%的工作负载将运行在价格便宜99%的模型上，仅20%的工作负载继续使用最先进的模型。
- 若该预测成真，大部分成本节省将来自大型AI实验室，对即将进行IPO的OpenAI和Anthropic造成财务冲击。
- 法律AI工具Harvey与Fireworks AI合作测试显示，组合使用Claude Opus和Fireworks的GLM 5.1可在不降低质量的情况下将推理成本降低3倍。
- Harvey联合创始人Gabe Pereyra表示，质量的定义正在从"使用最强大的模型做所有事"演变为"用最合适的模型最高效地得到正确答案"。
- 真正的分界线不在于专有模型与开源模型之争，而在于大模型与小模型之分，用户可通过选择任一类小型模型来降低成本。
extract_result: success
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