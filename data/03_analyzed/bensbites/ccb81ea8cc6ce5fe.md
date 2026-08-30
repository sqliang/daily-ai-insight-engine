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
impact_score:
  score: 4.5
  reason: 该事件并非产品发布、融资或技术突破，而是一篇 AI 代理工作流的个人实战复盘，短期不会直接改变行业竞争格局。但它准确击中了代理可靠性的核心痛点——当缺少显式验证层时，代理会因乐观偏差跳过端到端实机测试而交付有缺陷的结果——并给出了从文字描述到语音+截图再到屏幕录制配音的三级多模态排障升级路径，对代理工程实践（尤其'如何定义完成标准'）有直接可复用的参考价值。鉴于其洞见高于普通小圈子内容但影响力局限于方法论传播层面，给出
    4.5 分。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 如何为代理任务显式定义验证标准与端到端测试清单，避免代理跳过实机验证
hype_assessment:
  level: low
  reason: 全文是作者真实代理会话的第一手记录，坦承了方案遗漏、跳过安装测试、排障耗时 61 分钟等失败细节，并自我检讨'what I should've
    done'。全文未出现'颠覆''革命性'等 PR 滥用词汇，也无任何产品推销或夸大宣传，属于低炒作成分的实践复盘。
information_entropy: medium
domain_disruption:
  technical_innovation: 未提出新的技术架构突破，但总结出一条关键的代理工程方法论：代理任务需要显式'验证层'——用户须预先定义完成标准与端到端测试清单，否则代理会因'想尽快完成任务'的特性跳过实机验证而交付缺陷。同时验证了多模态上下文升级路径（文字→截图→屏幕录制逐帧分析）能显著提升代理排障效率，说明上下文信息密度与代理任务成功率正相关。
  business_model: 文中提及 Luna 模型在 Max 推理档位价格下调 80%，侧面印证推理成本下降正推动代理从实验性玩具走向日常个人生产力工具（作者用它处理非代码生活事务）。这也提示'代理即服务'类产品若要大规模落地，需在产品形态内内置验证/测试闭环，以降低普通用户的排障时间与
    token 成本。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 事件本身只是一篇社区博客复盘，但其背后是两个具备长期复利效应的结构性信号。其一，非技术背景个体已能借助前沿 agent（ChatGPT Codex
    + Luna）在 55 秒内生成方案、构建并完成真实 Chrome 扩展的修复，说明 agent 能力已跨越'能写代码'进入'端到端交付真实产品'的拐点，这会持续降低软件生产的边际成本并沉淀为新一轮生产范式。其二，作者复盘的核心教训——验证层（verification
    layer）缺失是 agent 任务失败的主要来源——指向一个高粘性、跨模型、跨场景的基础设施需求：agent 评测、可观测性、真实环境端到端测试（Computer
    use / Browser use）将逐步成为所有 agent 平台和工具链的标配，这一层具备数据飞轮效应（越多的真实会话产生越多的验证基准），3-5 年后大概率仍是行业基石。但文章本身是论据而非资产，且验证层工具的商业化路径尚需持续验证，故给予
    6.5 分。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Anthropic
- Browserbase
- Langfuse
competitive_casualty:
- 传统 RPA 厂商
- 无代码/低代码自动化平台
- 小型扩展外包开发与 QA 服务商
market_opportunities:
- 可针对'AI 代理任务验证层'开发专用工具或方法论，例如自动生成端到端测试清单并在代理宣称完成任务前强制执行的中间件，填补当前代理框架普遍缺少验证标准的空白，这是本案例最直接的商业化切口
- 可探索'多模态人机协作排障'产品方向，把屏幕录制+语音标注+光标定位的三级排障流程产品化，让用户能更高效地把复杂问题与上下文传达给代理，尤其适合面向非程序员的代理工具
- 可沉淀可复用的代理工作流模板（明确验证标准、端到端测试指令、方案逐条确认的提示词框架），面向开发者与知识工作者提供最佳实践与培训服务，将本案例的教训转化为标准化交付物
risk_matrix:
  regulatory: 无
  technological: 代理生成代码的可靠性风险显著——本案例中代理未在真实环境安装测试即交付，且作者未核对方案细节，说明当前代理对'何时算完成任务'的判断存在系统性缺陷；同时代理一次性吸收的多网页上下文未经核验，错误或矛盾信息可能被静默放大
  competitive: ChatGPT Codex 等代理开发工具的降价（文中提及 80% 降价）正在大幅拉低应用开发门槛，可能挤压低代码平台、Chrome
    扩展外包开发及小型定制开发服务商的生存空间，并引发代理工具之间的价格战
  ethical: 排障过程中涉及屏幕录制、语音描述与日历预约等敏感个人数据输入给第三方模型，存在隐私泄露与数据滥用风险；此外用户对代理能力的过度信任可能导致关键任务被静默错误执行而无人复核
  additional:
  - 多轮排障的 token 与时间成本可能超出自建成本（单轮排障耗时 61 分钟以上），存在投入产出比失控风险
  - 代理驱动开发若在团队内普及且缺少人工复核节点，长期可能形成对代理输出的系统性盲从，削弱组织质量把控能力
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: ChatGPT Codex
  canonical_name: OpenAI Codex
  url: https://openai.com/codex
  positioning: ChatGPT Codex 是 OpenAI 在 ChatGPT 内提供的代理编码模式，可在同一会话中完成方案生成、代码构建与浏览器实机验证等闭环任务。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 用自然语言驱动编码与浏览器测试的开发者
  - 希望借助 AI 代理完成端到端交付的技术用户
  product_signal: Codex 模式具备网页搜索、计算机使用与浏览器使用等工具，能在 55 秒内完成方案与构建，并在排障中通过屏幕录制视频逐帧定位问题。
  market_signal: 文中提到 Luna 模型在 Max 推理下价格已降 80%，显示 OpenAI 正以降价策略推动代理类产品的规模化采用。
  differentiation: 文章将 Codex 与 Work 模式、Claude Cowork 并列，说明其作为多种代理入口之一，差异主要体现在工具闭环能力与端到端验证机制上。
  watch_reason: 作者的真实代理会话展示了 Codex 从方案生成到端到端修复的完整工作流，也暴露了代理未主动验证、需用户设定验证标准的普遍痛点；随着模型降价与工具能力增强，Codex
    对开发工作流的渗透值得持续跟踪。
  risk_notes:
  - 代理在无明确指令时不会主动安装并实机测试，导致交付物存在功能缺陷，验证层缺失是主要不确定性。
  - 作者未核对方案细节即要求构建，说明输出质量高度依赖用户提示词质量，误用易造成时间与 token 浪费。
  - 会话中代理读取的网页信息未经用户核验，错误或矛盾信息可能误导代理决策，存在信息可信度风险。
  score: 7.0
  article_ids:
  - ccb81ea8cc6ce5fe
  evidence_snippets:
  - 作者使用 ChatGPT 的 Codex 模式来执行整个代理任务，从生成方案到构建 Chrome 扩展都在该模式下完成。
  - 文章指出同样任务也可以运行在 Work 模式或 Claude Cowork 等代理工具中，说明 Codex 是多种代理入口之一。
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