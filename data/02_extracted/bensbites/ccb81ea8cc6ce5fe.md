---
title: Ben's session
source: https://www.bensbites.com/p/bens-session
author: []
published: '2026-08-07'
created: '2026-08-08'
manifest_dates:
- '2026-08-08'
- '2026-08-09'
- '2026-08-10'
description: Field notes from my agent activity
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ccb81ea8cc6ce5fe
source_type: community_discussion
tldr: Ben's Bites 作者通过 ChatGPT Codex 模式的一次真实代理会话，尝试为 Google Calendar 构建可拖拽时间槽的预约链接扩展，并复盘了从方案遗漏、未端到端测试到分级排障的全过程，总结出明确验证标准对代理工作流的重要性。
objective_summary: Ben's Bites 作者（Ben）使用 ChatGPT 的 Codex 模式，尝试为 Google Calendar 打造一个可在周视图上直接拖拽时间槽、并自动同步预约表单的
  Chrome 扩展。代理经过 55 秒和两次网页搜索生成方案并完成构建，但因作者未核对方案细节且代理未在真实环境中安装测试，扩展上线后表单同步失效。作者随后经历文字描述、语音加截图、屏幕录制配音三级排障，最终代理开始使用
  Chrome 实机测试并修复问题。作者由此总结出为代理任务明确验证标准与端到端测试指令的重要性。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - OpenAI
  - Google
  - Anthropic
  - Ben's Bites
  technologies:
  - AI agent
  - Computer use
  - Browser use
  - Chrome extension
  - Luna
  - Max reasoning
  key_people:
  - Ben Tossell
key_logic_flow:
- 作者想在 Google Calendar 中设置可拖拽时间槽的预约链接，因无法直接拖拽而只能手动输入表单感到不满，于是启动代理会话来解决。
- 作者使用 ChatGPT 的 Codex 模式并计划测试 Luna 模型在 Max 推理下的表现，代理通过两次网页搜索在 55 秒内生成了解决方案。
- 代理返回迷你方案后作者只粗略浏览便直接说构建它，漏掉了拖拽时自动同步表单的关键需求。
- 代理构建完成后未自行安装测试，作者手动安装后发现表单同步失效，排障经历从文字描述到语音加截图再到屏幕录制配音的三级升级。
- 在第二轮修复中作者明确要求代理执行端到端测试清单，代理开始使用 Chrome 实机测试，说明验证层对代理完成任务至关重要。
object_mentions:
- object_type: product
  name: ChatGPT Codex
  canonical_name: OpenAI Codex
  url: https://openai.com/codex
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者使用 ChatGPT 的 Codex 模式来执行整个代理任务，从生成方案到构建 Chrome 扩展都在该模式下完成。
  - 文章指出同样任务也可以运行在 Work 模式或 Claude Cowork 等代理工具中，说明 Codex 是多种代理入口之一。
  article_id: ccb81ea8cc6ce5fe
- object_type: product
  name: Google Calendar
  canonical_name: Google Calendar
  url: https://calendar.google.com
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 作者需要为 Google Calendar 设置可预订的预约链接，但因无法直接拖拽时间槽而只能手动输入日期范围，这成为本次代理任务的起点。
  article_id: ccb81ea8cc6ce5fe
- object_type: project
  name: Google Calendar 拖拽时间槽扩展
  canonical_name: Google Calendar 拖拽时间槽扩展
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 作者让代理构建了一个可在 Google Calendar 周视图上直接拖拽时间槽并自动同步预约表单的 Chrome 扩展，但初次构建后表单同步功能失效。
  article_id: ccb81ea8cc6ce5fe
- object_type: model
  name: Luna
  canonical_name: Luna
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 作者原本打算测试 Luna 在 Max 推理模式下的表现，因为该模型价格已下调 80%，但最终任务在 ChatGPT Codex 中完成。
  article_id: ccb81ea8cc6ce5fe
- object_type: product
  name: Claude Cowork
  canonical_name: Claude Cowork
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 作者提到相同的代理任务也可以在 Claude Cowork 等工具中完成，表明该工作流并非 Codex 独占。
  article_id: ccb81ea8cc6ce5fe
extract_result: success
---

# Ben's session

### Field notes from my agent activity

Hello again :)

I’m trying something new - this email walks through one of my actual agent sessions and I’ll explain what’s happening along the way. The build or task I’m doing isn’t important. But I’m looking at how I could be using agents more effectively.

You might pick up a thing or two, I’m finding it helpful to solidify my own learning.

Please comment what you thought of this, was it helpful? anything unclear? want to see other things?

### What I was trying to do

I was setting up a bookable appointment link in Google Calendar and got annoyed that you can’t just drag time slots on the calendar grid, you have to type each date and time range into a clunky form. I wanted something that would let me drag slots directly on the week view and have the form update automatically.

So I fired up ChatGPT (I use Codex mode but works in ‘Work’ or Claude Cowork etc). I wanted to test Luna on Max reasoning as the price has been cut 80% and people have been saying how great it is to use.

It’s not the best prompt, I’ll admit.

But it gives the agent enough understanding of what I want so it can explore options. Plus a screenshot so it knew what screen I was on about.

This kicks off the ‘agent loop’. The agent thinks about what to do (what can be done with Google Calendar), then acts by using a tool (in this instance, web search) to gather context on how to solve my task.

The websites it read are now in the context window. I didn’t look at them so I have no idea what info it found or if its true. All the text it read is now in its ‘memory’.

Imagine 20 websites went in, there could be wrong or contradictory info that could mislead the agent. This is why you hear so much talk about context. It’s important, and you want it to be full of the best possible information.


Agents often do many loops for a task. They’re ‘go-getters’ by nature. Which is why they need babysitting.

They keep looping, gathering more context until they have what they need to complete the task. For my fantastic prompt, 55 seconds and 2 web searches was enough.

### Build it

The agent came back with a mini plan. I skimmed it, as usual (which cost me...).

I overlooked one point which was not how I wanted the extension to work, it should create the times automatically in the form as you drag tiles, not manually click to sync.

**What I should’ve done** is gone back and forth to ask how things would work, maybe mockup some wireframes I could annotate with feedback.

But I didn’t.

I just said build it...

It cycled through it’s loops and it was built!

Ha, not quite.

My first thought here was:

I shouldn’t need to install this myself

If its not installed, the agent can’t have tested this live

Why did I just say ‘build it’!?


The agent has tools it could’ve used when looping over the task, specifically Computer use and Browser use. It could’ve installed it and tested it live on my actual calendar page.

It didn’t, so I knew there’d be hiccups.

I installed it and tried dragging time frames but the form syncing didn’t work (shock).

**What I should’ve done** is say something like

“build it. install the extension in chrome, open a google calendar booking form and test it end to end. test multiple days/weeks, merging selections and check that the form updates correctly. iterate and keep testing until it works”.

That would’ve saved me time and tokens...

I went through my frustration escalation.

I start by typing the issues I run into.

14 minutes later still had issues. I moved to stage 2 - voice ramble and a screenshot.

61 (!!) minutes later still had issues. I moved to stage 3 - I record my screen with a voiceover, pointing my cursor at moments with issues. Agents can break videos down frame by frame and transcribe to pinpoint what you’re talking about.


Each turn (back-and-forth) the context gets fuller. After the first set of issues I sent it, it started actually using Chrome to test, thankfully.

But from reading it’s thinking, it didn’t test fully as it didn’t want to override my ‘work’ but that page was for the agent to absolutely use, that’s kind of key to test if this thing worked properly.

So on the second attempt at fixes I rambled a voice note and added a screenshot. This time I added things it should check and tests it should do.

This is that verification layer an agent considers when it’s thinking about the task being complete. Do all the tests (that the agent comes up with) pass with no issues = extension works.

When giving an agent a task, you should think about what criteria would mean this task is ‘done’. For a website it could be that all the content is formatted well with spacing, your design system, and works on mobile. For email triaging it could be that all the emails in your inbox have a label and are moved to the correct folder.

Verification is something I’m still working on as a lot of my tasks are not code.