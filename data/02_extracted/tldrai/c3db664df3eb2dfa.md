---
title: Claude Sonnet 5 (4 minute read)
source: https://www.anthropic.com/news/claude-sonnet-5?utm_source=tldrai
author: []
published: ''
created: '2026-07-02'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c3db664df3eb2dfa
manifest_dates:
- '2026-07-02'
source_type: news_media
tldr: Anthropic 发布 Claude Sonnet 5，这是迄今为止最具智能体能力的 Sonnet 系列模型，性能接近 Opus 4.8 但价格更低。该模型即日起在所有套餐中可用，促销定价为输入
  $2/百万 token、输出 $10/百万 token。
objective_summary: 2026年7月22日，Anthropic 发布了 Claude Sonnet 5 模型。该模型在推理、工具使用、编码和知识工作等智能体性能上较前代
  Sonnet 4.6 有显著提升，性能接近 Opus 4.8 但价格更低。Sonnet 5 即日起作为 Free 和 Pro 套餐的默认模型，并向 Max、Team
  和 Enterprise 用户开放，同时可通过 claude-sonnet-5 在 Claude API 中调用。定价方面，2026年8月31日前为促销价，之后恢复标准价。安全评估显示其不良行为率低于
  Sonnet 4.6，且网络安全能力远低于当前 Opus 模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies:
  - Claude Sonnet 5
  - Sonnet 4.6
  - Opus 4.8
  - BrowseComp
  - OSWorld-Verified
  key_people: []
key_logic_flow:
- Anthropic 发布了 Claude Sonnet 5 模型，这是迄今为止最具智能体能力的 Sonnet 系列模型，能够制定计划、使用浏览器和终端等工具并自主运行。
- Sonnet 5 在推理、工具使用、编码和知识工作等智能体性能关键指标上较前代 Sonnet 4.6 有显著提升，性能接近 Opus 4.8 但价格更低。
- Sonnet 5 即日起在所有套餐中可用，包括 Free、Pro、Max、Team 和 Enterprise，同时在 Claude Code 和 Claude
  平台通过 claude-sonnet-5 名称提供调用。
- 定价方面，2026年8月31日前的促销价为输入 $2/百万 token、输出 $10/百万 token，之后恢复为标准价输入 $3/百万 token、输出 $15/百万
  token。
- 安全评估显示 Sonnet 5 的不良行为率低于 Sonnet 4.6，在智能体场景中整体更安全，且网络安全能力远低于当前 Opus 模型。
- 早期访问合作伙伴反馈表明 Sonnet 5 能完成更复杂的多步骤任务，检查自身输出并以更少的步骤实现同等质量的成果。
extract_result: success
object_mentions:
- object_type: model
  name: Claude Sonnet 5
  canonical_name: Claude Sonnet 5
  url: https://www.anthropic.com/news/claude-sonnet-5
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Claude Sonnet 5 是 Anthropic 发布的最新模型，被描述为迄今为止最具智能体能力的 Sonnet 系列模型，能够制定计划、使用浏览器和终端等工具并自主运行。
  - Sonnet 5 在推理、工具使用、编码和知识工作等智能体性能上较前代 Sonnet 4.6 有显著提升，性能接近 Opus 4.8 但价格更低。
  - Sonnet 5 即日起在所有套餐中可用，开发者可通过 claude-sonnet-5 名称在 Claude API 中调用，促销定价为输入 $2/百万 token、输出
    $10/百万 token。
  article_id: c3db664df3eb2dfa
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: https://claude.ai/code
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到 Claude Sonnet 5 在 Claude Code 中也可用，作为该模型可访问的平台之一。
  article_id: c3db664df3eb2dfa
- object_type: product
  name: Claude API
  canonical_name: Claude API
  url: https://docs.anthropic.com/en/api
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 开发者可以通过 claude-sonnet-5 名称在 Claude API 中调用 Sonnet 5 模型。
  article_id: c3db664df3eb2dfa
---

# Introducing Claude Sonnet 5

Claude Sonnet 5 is built to be the most agentic Sonnet model yet. It can make plans, use tools like browsers and terminals, and run autonomously at a level that, just a few months ago, required larger and more expensive models.

For many developers, the agentic AI era began with Sonnet-class models: Claude Sonnet 3.5, 3.6, and 3.7 were the first models that showed impressive skills in coding and tool use. More recently, though, the clearest gains in agentic capabilities have been in our Opus-class models.

Sonnet 5 narrows the gap: its performance is close to that of Opus 4.8, but at lower prices. It’s a substantial improvement over its predecessor, Sonnet 4.6, on important aspects of agentic performance like reasoning, tool use, coding, and knowledge work:

Our safety assessments found that Sonnet 5 shows an overall lower rate of undesirable behaviors than Sonnet 4.6, and is generally safer to use in agentic contexts. Evaluations also show that it has a much lower ability to perform cybersecurity tasks than our current Opus models.

From today, Claude Sonnet 5 is available across all plans: it is the default model for Free and Pro plans, and is available to Max, Team, and Enterprise users. It’s also available in Claude Code and on the Claude Platform, where it launches with introductory pricing of $2 per million input tokens and $10 per million output tokens through August 31, 2026, after which it will be priced at $3 per million input tokens and $15 per million output tokens. Developers can use `claude-sonnet-5`

via the Claude API.

## Working with Claude Sonnet 5

The charts below compare the performance of Sonnet 5 with Sonnet 4.6 and Opus 4.8 at different effort levels on the agentic search evaluation BrowseComp and the computer use evaluation OSWorld-Verified. Sonnet 5 (orange line) is a strict improvement over Sonnet 4.6 (gray line) and covers a much wider range of cost-performance options than Opus 4.8 (yellow line). It provides substantially improved cost efficiency at medium effort; its higher-effort performance can match Opus 4.8 on some tasks. Between Sonnet 5 and Opus 4.8, users can adjust the effort level to find the right balance of cost and performance.

Feedback from our early access partners has been consistent: Sonnet 5 is much more agentic than its predecessors. Testers described how it finishes complex tasks where previous Sonnet models would stop short, how it checks its own output without explicitly being asked, and how it does all this agentic work at an attractive price point:

Claude Sonnet 5 gives our agents a strong execution layer for multi-step software engineering work. It handles sustained coding, tool use, and debugging well across messy technical contexts, and has been especially useful for workflows where follow-through and technical grounding matter.

We handed Claude Sonnet 5 a two-part job—update Salesforce account tiers, send a launch announcement to enterprise contacts—and it finished end to end. That used to stall halfway. For day-to-day automation, it’s a no-brainer.

Claude Sonnet 5 gets more done with less. Same output quality, fewer steps to get there. It refuses unsafe requests cleanly and consistently, too. At Lovable, we’re putting powerful tools in the hands of millions of builders. A model that knows when to say no is just as important as one that knows how to build.

We ran Claude Sonnet 5 against dozens of our most challenging real pull requests, and it carried each one through to a tested, verified result on its own — freeing our engineers to focus on the judgment, the decision, and the final sign-off.

I asked Claude Sonnet 5 to investigate a bug. Unprompted, it wrote a reproducing test, implemented the fix, then stashed it to confirm the bug came back without the change. All in a single pass.

With Claude Sonnet 5, agents stay on plan, follow our conventions, and ship clean multi-step changes, all at an efficient cost.

Claude Sonnet 5 is at its best on brownfield code—race conditions, hidden tests, the parts nobody wants to touch. It traces a failure to its actual root cause and ships a durable fix instead of patching the symptom.

Claude Sonnet 5 sits on the Pareto frontier for Eve’s plaintiff-law tasks. We see the clearest gains in legal research and analysis, at a price-to-performance ratio that made the choice to migrate easy.

ClickHouse agents explore live data and produce insights on the fly, so time-to-insight matters when testing new models. Claude Sonnet 5 reasons in tighter steps and gets our users to answers noticeably faster. That speed is a difference our customers feel.

At Pace, our computer-use agents run insurance workflows—submission intake, FNOL, loss runs—on the systems our operations teams already use. Claude Sonnet 5 consistently takes the right action and does it quickly, which is what real insurance work demands.

## Safety evaluations