---
title: Updated Claude Voice Mode (9 minute read)
source: https://www.engadget.com/2221938/claude-voice-mode-just-got-smarter/?utm_source=tldrai
author: []
published: ''
created: '2026-07-25'
manifest_dates:
- '2026-07-25'
- '2026-07-26'
- '2026-07-27'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6c4bbd0f57d1da8a
source_type: news_media
tldr: Anthropic 更新了 Claude 语音模式，使它能调用 Sonnet 和 Opus 等更强大的模型处理复杂请求，并可连接 Gmail 和 Slack
  等外部应用获取上下文。新语音模式以测试版形式向所有桌面端、移动端和网页端用户逐步推出。
objective_summary: Anthropic 于今日发布 Claude 语音模式更新，将此前仅使用 Haiku 模型的语音查询路由策略升级为支持 Sonnet
  和 Opus 模型，并默认使用用户上次文本聊天所用的模型。更新后的语音模式可以连接 Gmail 和 Slack 等已授权外部应用以获取上下文信息。Anthropic
  正在向所有桌面端、移动端和网页端用户逐步推出该测试版，免费用户仍仅限使用 Haiku 模型。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Engadget
  - OpenAI
  technologies:
  - Claude Voice Mode
  - Haiku
  - Sonnet
  - Opus
  - GPT-Live
  key_people: []
key_logic_flow:
- Anthropic 此前为降低延迟，Claude 语音模式仅使用最小的 Haiku 模型，导致复杂请求处理能力受限。
- Anthropic 今日发布语音模式更新，使其能够调用 Sonnet 和 Opus 模型，并默认使用用户上次文本聊天所用的模型。
- 用户可以通过模型选择器在 Haiku、Sonnet 和 Opus 之间实时切换，语音模式会自动选取相应模型的最快版本以保证对话流畅。
- 更新后的语音模式可以连接 Gmail 和 Slack 等已授权外部应用以获取上下文信息，但需用户事先授予权限。
- Claude 语音模式采用轮流对话架构，与 OpenAI 的 GPT-Live 全双工系统不同，无法同时处理语音输入和输出。
- Claude 语音模式无法自动检测语言切换，用户需口头告知或手动在设置中选择目标语言；同时新增对印尼语等更多语言的支持。
object_mentions:
- object_type: product
  name: Claude Voice Mode
  canonical_name: Claude Voice Mode
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 今日更新 Claude 语音模式，使其能够调用 Sonnet 和 Opus 等更强大的模型处理复杂请求，此前仅使用 Haiku 模型。
  - 更新后的语音模式可以连接 Gmail 和 Slack 等已授权外部应用以获取上下文信息，但需要用户授予权限。
  - Anthropic 正在向所有桌面端、移动端和网页端用户逐步推出新的语音模式测试版，免费用户仅限使用 Haiku 模型。
  article_id: 6c4bbd0f57d1da8a
- object_type: product
  name: GPT-Live
  canonical_name: GPT-Live
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 与 OpenAI 的 GPT-Live 系统不同，Claude 语音模式采用轮流对话架构，无法同时处理语音输入和生成输出。
  article_id: 6c4bbd0f57d1da8a
extract_result: success
---

# Claude's voice mode just got smarter

And you can connect it to apps like Gmail and Slack.

Since last year, Anthropic has offered a voice mode through Claude, allowing you to speak to its chatbot instead of writing out your prompts. If I had to guess, most people probably don't know Claude has voice input. However, for those that have used it, the consensus has been that it could use work. One issue is that before today Anthropic routed voice mode queries through Haiku, its smallest model, to reduce latency. That meant voice mode worked well enough for simple questions, but could struggle with more complicated requests. Today, Anthropic is releasing an update to address that complaint.

Now when you use voice mode, it can turn to the company's Sonnet and Opus models for help. Provided you pay for Claude access, the tool will default to the last system you used for text chat. You can also switch between Haiku, Sonnet or Opus mid-conversation through the model picker. "Voice mode uses the fastest version of whichever model you've selected, so the conversation runs smoothly," Anthropic notes. Additionally, voice mode can now pull context from connected apps such as Gmail and Slack, as long as you grant Claude permission to do so.

An Anthropic spokesperson told Engadget voice mode uses a turn-based architecture, so all interactions will see Claude listen to you, pause to think and then respond. It's not fully duplex like OpenAI's new GPT-Live system, which can simultaneously process speech and generate an output. In practice, that should make talking to Claude feel less natural than ChatGPT. Another limitation of Claude's voice mode is that it can't automatically detect the language you're speaking in if you decide to switch languages mid-conversation. You need to either tell it out loud you're about to switch or select the language you're about to speak in from the voice settings menu. However, Anthropic has added support for additional languages, including Indonesian.

"This release is focused on intelligence and tool access," Anthropic told Engadget. "We're continuing to invest in voice and we'll have more to share later this year."

Anthropic is rolling out the new voice mode in beta to all users across its desktop and mobile apps, as well as web client. If you're using Claude through a free account, Anthropic will limit you to a single connection and your prompts will all go through Haiku, though you can speak to Claude in all of the languages voice mode now supports.