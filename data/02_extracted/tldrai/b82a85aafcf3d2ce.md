---
title: SpaceXAI launches Grok Voice Think Fast 2.0 on Agent Builder (2 minute read)
source: https://www.testingcatalog.com/spacexai-launches-grok-voice-think-fast-2-0-on-agent-builder/#google_vignette?utm_source=tldrai
author: []
published: ''
created: '2026-07-31'
manifest_dates:
- '2026-07-31'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b82a85aafcf3d2ce
source_type: news_media
tldr: xAI发布新一代语音到语音模型Grok Voice Think Fast 2.0，定价每分钟0.08美元，在Artificial Analysis基准上综合得分82.9%，超越GPT-Realtime-2.1与Gemini
  3.1 Flash。该模型面向语音Agent开发者，转录准确率较前代大幅提升，8月5日起grok-voice-latest别名将自动切换至2.0。
objective_summary: xAI于2026年8月初推出语音到语音模型Grok Voice Think Fast 2.0，面向构建语音Agent的开发者，按每分钟音频0.08美元计费。在Artificial
  Analysis语音基准测试中，该模型综合得分82.9%，高于前代Think Fast 1.0的75.7%、OpenAI GPT-Realtime-2.1的79.1%及Google
  Gemini 3.1 Flash的69.5%，首次音频响应时间从1.25秒降至0.70秒。xAI称其在24种语言的短句转录准确率较Deepgram Nova 3与ElevenLabs
  Scribe v2提升1.5至2倍，在背景噪声与电话压缩场景下差距约为10倍。xAI在Starlink电话服务的A/B测试中报告了更高的销售转化与客服分流率，并宣布8月5日起grok-voice-latest别名将自动指向新模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - xAI
  - OpenAI
  - Google
  - Deepgram
  - ElevenLabs
  - Starlink
  - Artificial Analysis
  technologies:
  - speech-to-speech
  - reinforcement learning
  - word error rate
  key_people: []
key_logic_flow:
- xAI发布新一代语音到语音模型Grok Voice Think Fast 2.0，面向构建语音Agent的开发者，按每分钟音频0.08美元计费，且无需修改既有提示词即可在几乎所有用例中提升表现。
- 在Artificial Analysis语音基准上，2.0版综合得分82.9%，高于1.0版的75.7%，并超过GPT-Realtime-2.1的79.1%与Gemini
  3.1 Flash的69.5%，其智能体得分达到56.5%。
- 该模型采用与语音并行的推理设计，推理token用量降至前代的0.4倍，首次音频响应时间由1.25秒缩短至0.70秒，生产环境工具调用通常在智能体说完第一句话前即可执行。
- xAI报告其在24种语言短句上的转录准确率较Deepgram Nova 3与ElevenLabs Scribe v2提升1.5至2倍，在强背景噪声与电话压缩场景下差距约10倍。
- xAI在Starlink电话服务上进行的A/B测试显示更高的销售转化率与客服分流率，用以支撑模型在真实客户工作流中的可靠性主张。
- 2026年8月5日起grok-voice-latest别名将自动从grok-voice-think-fast-1.0切换至2.0，需要旧版的开发者必须在此之前固定1.0标识，其他用户无需任何操作。
object_mentions:
- object_type: model
  name: Grok Voice Think Fast 2.0
  canonical_name: Grok Voice Think Fast 2.0
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - xAI推出新一代语音到语音模型Grok Voice Think Fast 2.0，面向构建语音Agent的开发者，按每分钟音频0.08美元计费。
  - 在Artificial Analysis语音基准上，Think Fast 2.0综合得分82.9%，高于1.0版的75.7%并超过GPT-Realtime-2.1与Gemini
    3.1 Flash。
  - 2026年8月5日起grok-voice-latest别名将自动从grok-voice-think-fast-1.0切换至grok-voice-think-fast-2.0。
  article_id: b82a85aafcf3d2ce
- object_type: model
  name: Grok Voice Think Fast 1.0
  canonical_name: Grok Voice Think Fast 1.0
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Think Fast 2.0在Artificial Analysis语音基准上综合得分82.9%，高于前代Think Fast 1.0的75.7%，其智能体得分亦从52.1%升至56.5%。
  - 需要继续使用旧版的开发者必须在8月5日别名切换前固定grok-voice-think-fast-1.0标识。
  article_id: b82a85aafcf3d2ce
- object_type: model
  name: GPT-Realtime-2.1
  canonical_name: OpenAI GPT-Realtime-2.1
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在Artificial Analysis语音基准上，GPT-Realtime-2.1综合得分为79.1%，低于Think Fast 2.0的82.9%，仅在对话基准上以95.7%略高于后者的95.1%。
  article_id: b82a85aafcf3d2ce
- object_type: model
  name: Gemini 3.1 Flash
  canonical_name: Google Gemini 3.1 Flash
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在Artificial Analysis语音基准上，Gemini 3.1 Flash综合得分为69.5%，智能体得分为37.7%，均低于Think Fast
    2.0的82.9%与56.5%。
  article_id: b82a85aafcf3d2ce
- object_type: product
  name: Deepgram Nova 3
  canonical_name: Deepgram Nova 3
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - xAI称Think Fast 2.0在24种语言短句上的转录准确率较Deepgram Nova 3提升1.5至2倍，衡量指标采用词错误率。
  article_id: b82a85aafcf3d2ce
- object_type: product
  name: ElevenLabs Scribe v2
  canonical_name: ElevenLabs Scribe v2
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - xAI称Think Fast 2.0在24种语言短句上的转录准确率较ElevenLabs Scribe v2提升1.5至2倍，强噪声与电话压缩场景下差距约10倍。
  article_id: b82a85aafcf3d2ce
extract_result: success
---

xAI has introduced Grok Voice Think Fast 2.0, its next-generation speech-to-speech model, with gains in intelligence, transcription accuracy, conversational behavior, and tool use. The model is aimed at developers building voice agents and costs $0.08 per minute of audio. xAI expects it to raise performance across almost all use cases without changes to existing prompts.

On Artificial Analysis’ speech-to-speech benchmark, Think Fast 2.0 scored 82.9% overall, up from 75.7% for version 1.0 and ahead of GPT-Realtime-2.1 at 79.1% and Gemini 3.1 Flash at 69.5%. Its agentic score reached 56.5%, compared with 52.1% for its predecessor, 45.7% for GPT-Realtime-2.1, and 37.7% for Gemini 3.1 Flash. Time to first audio fell from 1.25 seconds to 0.70 seconds. The model’s 95.1% conversational benchmark score was just below GPT-Realtime-2.1 at 95.7%.

Transcription is another major focus. In xAI’s evaluation of thousands of short phrases across 24 languages, the company reported accuracy improvements of 1.5 to 2.0 times versus Deepgram Nova 3 and ElevenLabs Scribe v2, and 1.4 times versus Think Fast 1.0. xAI says the gap is roughly 10× under substantial background noise and telephony compression. The comparison uses the word error rate, with lower scores preferred.

Think Fast 2.0 reasons in parallel with speech, a design intended to preserve latency while handling more complex queries. Median relative reasoning-token use fell to 0.4 times, using the predecessor’s 1.0 times as a baseline. xAI says this lets production tool calls usually execute before the agent finishes its first sentence. Reinforcement learning also pushed the model toward shorter sentences, one question at a time, and less fluff while guiding users through complex workflows.

For SpaceXAI, this release is a push to make Grok Voice more dependable in real customer workflows. An A/B test on Starlink’s phone service produced higher sales conversion and support containment rates, according to the company. On August 5, 2026, the grok-voice-latest alias will automatically move from grok-voice-think-fast-1.0 to grok-voice-think-fast-2.0. Developers who want the prior model must pin the 1.0 identifier before the switch; everyone else needs to take no action.