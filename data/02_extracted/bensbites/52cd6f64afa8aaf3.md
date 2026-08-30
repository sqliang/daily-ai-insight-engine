---
title: Who let the agents in
source: https://www.bensbites.com/p/who-let-the-agents-in
author: []
published: '2026-08-27'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
- '2026-08-29'
description: It&#8217;s you, and it&#8217;s getting easier
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 52cd6f64afa8aaf3
source_type: community_discussion
tldr: ChatGPT Work 借鉴 Grok Bot 推出新登录流程：AI 代理遇到登录页时暂停并弹出表单，用户凭据直接传给云端浏览器而非进入聊天记录，登录后代理继续执行。该期通讯还汇总
  OpenAI 芯片 Jalapeño 超越 Nvidia Blackwell、Nvidia 拟收购 Hugging Face、多款新模型发布等头条。
objective_summary: Ben's Bites 通讯在"Who let the agents in"一期中报道，多数 AI 代理通过浏览器执行任务但常被登录页拦截，手动输入凭据繁琐且不总是可行，把密码或
  API token 粘贴进聊天则存在安全隐患。为此 ChatGPT Work 借鉴 Grok Bot 引入新的登录流程：代理遇到登录页时暂停并弹出表单，用户输入的账号、密码与
  2FA 验证码由系统直接传递给云端浏览器完成登录，不进入聊天记录，登录后代理继续执行且会话可保持。该期还汇总了多项头条，包括 OpenAI 新芯片 Jalapeño
  在能效与速度上超越 Nvidia Blackwell、OpenAI 完成其模型攻击 Hugging Face 的调查并发布报告、Nvidia 拟以 129 亿美元收购
  Hugging Face，以及 GLM-5.3-Flash、Muse Image、Gemini 3.5 Transcribe 等模型发布。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Anthropic
  - Meta
  - Google
  - Nvidia
  - Hugging Face
  - xAI
  - ElevenLabs
  - Perplexity
  - Gravitee
  - Loom
  - Screen Studio
  technologies:
  - cloud browser
  - 2FA
  - GLM-5.3-Flash
  - GPT-5.6-Luna
  - Gemini 3.5 Transcribe
  - Muse Image
  - Blackwell
  - Jalapeño
  - DGX Spark
  - Codex
  key_people:
  - Elon Musk
  - Theo
  - Hamel
key_logic_flow:
- 多数 AI 代理通过浏览器替用户完成任务，但大量目标网站位于登录页之后，手动输入凭据或把密码、API token 粘贴进聊天记录都不是理想方案。
- ChatGPT Work 借鉴 Grok Bot 的机制推出新登录流程：代理遇到登录页时暂停并弹出表单，用户输入的账号、密码与 2FA 验证码直接传给云端浏览器而非进入聊天。
- 网站完成登录后代理继续执行任务，会话登录态可保留供后续任务使用，用户也可以在设置中清除。
- 头条方面，OpenAI 自研推理芯片 Jalapeño 在三个开源模型上实现每瓦特 1.5 至 1.9 倍计算量并降低 1.7 至 3.6 倍时延，超越 Nvidia
  Blackwell，计划年底部署。
- OpenAI 完成了对其模型攻击 Hugging Face 事件的调查并发布报告，同时据 The Information 报道 Nvidia 拟以 129 亿美元收购
  Hugging Face。
- 该期还盘点多项动态：Claude Chat 与 Cowork 共享记忆、GLM-5.3-Flash 开源模型发布、Muse Image 接入 Meta API、Gemini
  3.5 Transcribe 上线等。
object_mentions:
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ChatGPT Work 新增了介于手动输入与粘贴密码之间的登录流程，代理遇到登录页时会暂停并弹出表单。
  - 用户在表单中输入的账号、密码与两步验证码不会进入聊天记录，而是由 ChatGPT Work 直接传递给云端浏览器。
  - 网站完成登录后代理继续执行任务，会话登录态可保留供后续任务使用，并可在设置中清除。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: Grok Bot
  canonical_name: Grok Bot
  url: https://grok.com
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 文章指出 ChatGPT Work 的新登录流程借鉴自 Grok Bot，两者都采用遇到登录页时暂停并弹出表单的机制。
  - 作者调侃称通过 Grok Bot 操作银行账户时 Elon Musk 会负责赔偿用户损失，暗示该方案仍存在安全顾虑。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: Claude Cowork
  canonical_name: Claude Cowork
  url: https://claude.ai
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Claude Chat 与 Cowork 现在共享记忆，作者担心用户在闲聊中表达的对同事的不满会影响通过 Cowork 撰写的邮件语气。
  - 文章还提到 Claude 的 Cowork 现已内置浏览器，可供代理在协作流程中直接访问网页内容。
  article_id: 52cd6f64afa8aaf3
- object_type: model
  name: GLM-5.3-Flash
  canonical_name: GLM-5.3-Flash
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GLM-5.3-Flash 被描述为 Ox Alpha 秘密揭晓后公开的模型，是 GPT-5.6-Luna 的优秀开源替代方案。
  article_id: 52cd6f64afa8aaf3
- object_type: model
  name: Muse Image
  canonical_name: Muse Image
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Meta 已将 Muse Image 模型接入自家 API，支持以每张图片 0.01 美元的价格生成或编辑图像。
  article_id: 52cd6f64afa8aaf3
- object_type: model
  name: Gemini 3.5 Transcribe
  canonical_name: Gemini 3.5 Transcribe
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Gemini 3.5 Transcribe 是 Google 新推出的音频转录模型，价格偏高但错误率远低于其他同类模型。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: OpenAI Jalapeño
  canonical_name: OpenAI Jalapeño chip
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 自研的首款推理芯片 Jalapeño 在三个开源模型上实现每瓦特 1.5 至 1.9 倍的计算量，并降低 1.7 至 3.6 倍时延。
  - Jalapeño 在速度与能效上均超越 Nvidia 的 Blackwell 芯片，计划于今年年底开始部署。
  article_id: 52cd6f64afa8aaf3
- object_type: project
  name: screendrop
  canonical_name: screendrop
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - screendrop 是一款开源的 Loom 与 Screen Studio 替代品，提供可下载的 Mac 桌面应用版本。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: ElevenLabs Composer
  canonical_name: ElevenLabs Composer
  url: https://elevenlabs.io
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - ElevenLabs 推出 Composer 功能，允许用户逐段编辑歌曲，对音乐作品的各个章节进行精细调整。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: opencomputer.dev
  canonical_name: opencomputer.dev
  url: https://opencomputer.dev
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - opencomputer.dev 允许用户将 AI 代理作为函数进行部署，并为每个代理配备一台独立的 Linux 计算机。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: Perplexity Computer (local)
  canonical_name: Perplexity Computer local
  url: https://www.perplexity.ai
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 有开发者构建了 Perplexity Computer 的完全本地化版本，专门设计为在 Nvidia DGX Spark 本地设备上运行。
  article_id: 52cd6f64afa8aaf3
- object_type: product
  name: OpenAI Codex
  canonical_name: OpenAI Codex
  url: https://openai.com/codex/
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Hamel 在个人笔记中分享了使用 OpenAI Codex 自动化重复性评估工作的实践经验与心得。
  article_id: 52cd6f64afa8aaf3
- object_type: dataset
  name: Robot-training dataset (16M videos)
  canonical_name: Robot Training Dataset 16M
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到一个包含来自 100 多个国家共 1600 万条视频的机器人训练数据集，可用于教机器人仅凭一段视频学会新任务。
  article_id: 52cd6f64afa8aaf3
extract_result: success
---

Hey folks,

Most agents now use a browser to complete tasks for you. But a lot of the websites you want them to visit are behind a login page.

There are a couple of ways around this. You could type in your details in the browser yourself. Fine, but annoying, and not always possible. Or you could paste the password or an API token into the chat. We’ve all done that, but that’s not secure now, is it?

ChatGPT Work has a new sign-in flow that sits between the two. I think they picked it up from Grok Bot.

When Work reaches a login page, it pauses and shows you a widget/form. You enter your username, password and 2FA code there. They don’t go into the chat. Work passes them along directly to the cloud browser on your behalf.

Once the website signs that browser in, the agent carries on.

The session can stay signed in for later tasks, and you can clear it in settings.

Much easier. Still maybe don’t start with your bank (though Elon will make you whole if you do it with Grok Bot).

*Ben’s Bites is brought to you by Gravitee*


🕵️ We know what your AI agents did last night.Gravitee is the platform built to make AI agents accountable. We give every agent a verified identity, enforce exactly what they can access, and record exactly what they did, so enterprises never have to ask their agents, “Where were you last night?”


### Headlines

**Claude Chat and Cowork now share their memory**. I’m not sure that’s a good thing. You don’t want your frustration with a colleague (that you mentioned to Claude in a random chat) to change the tone of your emails with them (written via Cowork).

It’s still separate from Claude Code’s memory, but that's not great either. Theo made a video about it: Turn off Claude Code’s memory.

Despite everyone’s attempts to get Memory right, it keeps saving irrelevant stuff to memory or referring to it unnecessarily. I touched a bit on my current memory setup in last Friday’s post.

**Three new-ish models to look at:**

GLM-5.3-Flash - The reveal of the Ox Alpha secret. It’s a great open-source alternative for GPT-5.6-Luna.

Muse Image is now in Meta’s API. Generate or edit images at $0.01 per image.

Gemini 3.5 Transcribe - New model from Google for audio transcription. It’s quite pricey, but makes way fewer errors than other models.


**OpenAI’s new chip Jalapeño beats Nvidia’s Blackwell chips** on both speed and efficiency. Across three open models, its first inference chip delivered 1.5-1.9x more work per watt and 1.7-3.6x lower latency. It starts deploying by year-end.

Also, remember when an OpenAI model hacked Hugging Face? They completed the investigation into it and released a report. Btw, Nvidia is buying Hugging Face for $12.9B (via The Information).

Looks like a toxic love triangle between these three.

### My feed

fuck cancer - skill for agents to help patients and caregivers.

A $50k hackathon to help one kid fight a rare disease.

Claude now has its own built-in browser in Cowork.

Scheduled tasks in ChatGPT can now also run from a trigger like a Slack message, new email, etc.

Search and spot trends in over 130,000 actively transcribed podcasts. (examples)

Patterns in how people use Claude from 250k anonymised chats.

screendrop - Open source alternative to Loom and Screen Studio, downloadable as a Mac app.

Edit a song section by section with ElevenLabs Composer.

Cosy listening room so you can flip through & play your Spotify albums.

Using Codex to automate repetitive eval work. (Hamel’s notes)

The latest personal agent making investors go crazy (already valued at $2.5B).

opencomputer.dev - Deploy your agents as functions, with a Linux computer for each one.

Fully local version of Perplexity Computer, built to run on Nvidia DGX Spark.

Teach a robot new tasks from just one video.

Robot-training dataset with 16M videos from 100+ countries.


#### Afters

Read about me and Ben’s Bites

📷 thumbnail via @keshavatearth



* sponsors who make this newsletter possible :)

Wanna partner with us for the next quarter?

Email us at shanice@bensbites.com or k@bensbites.com