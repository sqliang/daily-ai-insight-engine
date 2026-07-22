---
title: Google's take on openclaw
source: https://www.bensbites.com/p/googles-take-on-openclaw
author: []
published: '2026-05-21'
created: '2026-05-22'
description: it's Anthropic's time for the mandate of heaven
tags:
- clippings
extraction_status: success
id: b60eabf0d9170bba
source_type: community_discussion
tldr: 谷歌I/O大会发布Gemini Omni Flash、Gemini 3.5 Flash和Gemini Spark以应对Claude生态竞争；Andrej
  Karpathy加入Anthropic预训练团队；SpaceX IPO文件披露Anthropic月付12.5亿美元算力费用，该公司预计6月季度收入达109亿美元并首次实现运营盈利。
objective_summary: 谷歌在I/O大会上发布了Gemini Omni Flash（首个任意输入/输出模型，可生成和编辑视频）、Gemini 3.5
  Flash（性能超越3.1 Pro）和Gemini Spark（即将推出的Workspace全天候个人代理）来应对Anthropic的Claude生态竞争。Andrej
  Karpathy加入了Anthropic预训练团队，在Nick Joseph领导下组建新小组，利用Claude加速预训练研究。SpaceX的IPO文件披露Anthropic每月将支付12.5亿美元用于算力，该公司预计6月季度收入达109亿美元并首次实现运营盈利。此外，OpenAI声称其模型解决了一个著名数学难题并获得外部数学家验证，Figma推出了画布内设计代理功能，多个AI工具和项目被提及。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - Anthropic
  - OpenAI
  - SpaceX
  - Figma
  - Datadog
  - Cohere
  - GitHub
  - The Atlantic
  - Fortune
  technologies:
  - Gemini Omni Flash
  - Gemini 3.5 Flash
  - Gemini Spark
  - Antigravity
  - C2PA
  - SynthID
  - MCP
  - Veo
  key_people:
  - Andrej Karpathy
  - Nick Joseph
key_logic_flow:
- Andrej Karpathy加入Anthropic预训练团队，在Nick Joseph领导下组建新小组，探索利用Claude加速Claude模型的预训练研究。
- SpaceX的IPO文件披露Anthropic每月将支付12.5亿美元用于算力；Anthropic预计6月季度收入达109亿美元并首次实现运营盈利。
- 谷歌在I/O大会上发布了Gemini Omni Flash（首个任意输入/输出模型，可生成和编辑视频）、Gemini 3.5 Flash（性能超越3.1 Pro但知识截止于2025年1月）和Gemini
  Spark（即将推出的Workspace全天候个人代理）。
- OpenAI声称其模型解决了一个著名数学难题并获得外部数学家验证，同时推出了基于C2PA元数据和Google SynthID的公开图片验证器。
- Figma推出了画布内设计代理功能，可以从设计图层开始并行生成多个方向、批量编辑、使用设计系统并在同一文件中支持团队协作。
- 多个AI工具和项目被报道，包括Neimo MCP（跨200+司法管辖区的合规MCP）、Factory Droid（上下文削减40%）、Roughdraft（开源Markdown评论界面）、Lapdog（Datadog的本地追踪工具）和Active
  Graph（开源长运行代理框架）。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: product
  name: Antigravity
  canonical_name: Antigravity
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 谷歌发布了Antigravity作为AI编程代理应用，它类似于Codex和Conductor，但用户无法快速绕过权限设置。
  article_id: b60eabf0d9170bba
- object_type: model
  name: Gemini Omni Flash
  canonical_name: Gemini Omni Flash
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌在I/O大会上发布了Gemini Omni Flash，这是首个任意输入/输出的模型，可以生成和编辑视频。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Gemini Spark
  canonical_name: Gemini Spark
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌推出了Gemini Spark作为OpenClaw的竞品，这是一个24/7全天候个人代理，可在Workspace中工作但目前仅显示'即将推出'状态。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Neimo MCP
  canonical_name: Neimo MCP
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Neimo MCP将Claude、OpenAI的Codex和Manus转变为横跨200多个司法管辖区的监管专家。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Factory Droid (Deferred Context Engine)
  canonical_name: Factory Droid
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Factory的延迟上下文引擎让Droid能够更有选择性地加载工具，从而将上下文大小削减40%。
  article_id: b60eabf0d9170bba
- object_type: project
  name: Roughdraft
  canonical_name: Roughdraft
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Roughdraft是一个本地开源的Markdown文档评论和修改建议界面。
  article_id: b60eabf0d9170bba
- object_type: project
  name: DiffsHub
  canonical_name: DiffsHub
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - DiffsHub允许用户在公开的GitHub diff URL中将github替换为diffshub，以虚拟化方式快速检查大型diff。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Lapdog
  canonical_name: Datadog Lapdog
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Datadog发布了Lapdog，这是一个针对Codex、Claude Code和Pi中推理和工具调用的本地追踪工具。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Granola Briefs
  canonical_name: Granola Briefs
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Granola Briefs在会议前搜索用户的邮件、网络信息和之前的会议记录，然后给出三个要点总结。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Taste MCP
  canonical_name: Taste MCP
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Taste MCP让用户的设计偏好能够跟随进入Codex、Cursor和Claude Code等开发工具中。
  article_id: b60eabf0d9170bba
- object_type: product
  name: OpenAI Guaranteed Capacity
  canonical_name: OpenAI Guaranteed Capacity
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI推出Guaranteed Capacity服务，企业可以提前预订1-3年的OpenAI算力，避免需求高峰时被限流。
  article_id: b60eabf0d9170bba
- object_type: project
  name: Active Graph
  canonical_name: Active Graph
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Active Graph是一个开源框架，用于让长时间运行的代理记住已发生的事件、响应新事件并比较不同代理的运行情况。
  article_id: b60eabf0d9170bba
- object_type: model
  name: Command A+
  canonical_name: Cohere Command A+
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Cohere发布了Command A+，这是一个开源的企业级模型，支持文本、图像和工具使用，量化后可在两块H100或一块B200上运行。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Parallel Web Systems Index
  canonical_name: Parallel Web Systems Index
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Parallel Web Systems Index让发布商可以查看哪些AI代理正在读取他们的内容并获得报酬，首批合作伙伴包括The Atlantic、Fortune、Every和Packy。
  article_id: b60eabf0d9170bba
- object_type: product
  name: Handinger
  canonical_name: Handinger
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Handinger允许用户用自然语言构建AI代理，将其连接到工具，并消除繁琐的行政工作。
  article_id: b60eabf0d9170bba
---

# Google's take on openclaw

### it's Anthropic's time for the mandate of heaven

Hey folks,

My first fund is now at 5x! I had a very notable firm not invest in my latest fund as they were assessing if I was a 5x fund returner… seems like I am. Fund 2 is also at ~3x with 55% IRR. Fund 3 I’m starting to fundraise for again, looking for operators, $100k minimum. Deployed 4 cheques so far. I invest in developer tools and infrastructure - essentially anything for an agent-first world. If you or anyone you know would be interested, please let me know.

Google’s I/O event on Tuesday was overshadowed by Andrej Karpathy joining Antrhopic’s pre-training team under Nick Joseph to build and lead a new group focused on using Claude to accelerate pre-training research. Using Claude to help pre-train Claude models.

And now they have the compute… SpaceX’s IPO filing discloses Anthropic will pay $1.25 billion monthly for compute.

Just as Anthropic project $10.9 billion June quarter revenue and its first operating profit. Which could well lead them to a valuation higher than OpenAI. Who have been reported are potentially filing for an IPO imminently (some sources say as early as tomorrow) - but nothing official or confirmed.

*Ben’s Bites is brought to you by Attio, the AI CRM*

GTM Atlas is the map for modern go-to-market. Written by top operators, Atlas is a free resource covering the full customer journey, with systems thinking that scales with you. Curated by Attio. Mapped by operators. Read now


#### Headlines

Google I/O wasn’t all that interesting.

They have a new model family aiming for any input/any output.

**Gemini Omni Flash**- the first model in that family generates and edits videos. The technical difference between Omni and Veo is similar to that between Imagen and Nano Banana.For general model upgrades, they only released

**Gemini 3.5 Flash,**which, on paper, is better than 3.1 Pro. This model is fast and intelligent, but not cheap anymore. It also has the knowledge cutoff of Jan 2025, so it does not know about vibe coding and beyond. 3.5 Pro is coming next month, but I don’t have high hopes.**Antigravity**is now a clone of Codex, Conductor and every other AI coding agent app. It’s usable — but I couldn’t find a way to bypass permission quickly. They have also made installing the IDE optional.Their answer to OpenClaw is called

**Gemini Spark**, a 24/7 personal agent that works across Workspace, but it’s “coming soon”, so no idea how well it works.

OpenAI says one of its models

**solved a famous math problem,**and external mathematicians checked the proof. They also added a**public image verifier**for images made with ChatGPT, the API and Codex. It checks C2PA metadata and also SynthID (from Google). Try it here.**Figma has a design agent inside the canvas**. It can start from a design layer, generate multiple directions in parallel, make bulk edits, use your design system, and work in the same file as your team.Now any product developer can ship globally:

**Neimo MCP**turns Claude, OpenAI's Codex, and Manus into regulatory experts across 200+ jurisdictions. Built by the team behind compliance for some of the world's largest games and platforms. Try Neimo free 👉*

#### My feed

Handinger: Build AI agents in plain English, connect them to your tools, and kill the boring admin work nobody wants.*

Factory’s Deferred Context Engine - Droid now loads tools more selectively to cut context size by 40%.

Roughdraft - local open-source interface for commenting and suggested changes on markdown docs/plans.

DiffsHub - replace

*github*with*diffshub*in a public GitHub diff URL to virtualise and inspect huge diffs quickly.Lapdog from Datadog - local tracing for reasoning and tool calls in Codex, Claude Code and Pi.

Granola Briefs - searches your email, web and previous meeting notes before a meeting, then gives you three bullets.

Taste MCP - what if your design preferences could follow you into Codex, Cursor, Claude Code?

OpenAI Guaranteed Capacity - companies can pre-book OpenAI compute for 1-3 years, so important products and agents don't get throttled when demand spikes.

Parallel Web Systems Index - lets publishers see which agents are reading their content and get paid. First partners include The Atlantic, Fortune, Every and Packy.

Active Graph - open-source framework for long-running agents to remember what happened, react to new events, and compare different agent runs.

Making computer use reliable in production.

A poisoned third-party VS Code extension compromised a GitHub employee's device, and ~3,800 internal GitHub repos were exfiltrated.

Cohere released Command A+ - an open-source enterprise model. supports text/image/tool use and runs on two H100s/one B200 with quantisation.


#### Afters

Read about me and Ben’s Bites

📷 thumbnail by @keshavatearth



* sponsors who make this newsletter possible :)

Wanna partner with us for the next quarter?