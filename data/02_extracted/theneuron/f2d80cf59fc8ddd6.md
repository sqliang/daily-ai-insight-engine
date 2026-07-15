---
title: 😺 Fable 5 is back baby
source: https://www.theneurondaily.com/p/july-1-claude-got-a-workhorse-upgrade
author:
- '[[Grant Harvey]]'
published: '2026-07-01'
created: '2026-07-02'
description: 'PLUS: Claude 5 Sonnet, AWS embeds agents, Etched exits stealth, and
  SF gets pricier.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f2d80cf59fc8ddd6
manifest_dates:
- '2026-07-02'
- '2026-07-03'
source_type: newsletter_rss
tldr: Anthropic恢复Claude Fable 5全球可用并发布Claude Sonnet 5作为默认模型
objective_summary: Anthropic于7月1日宣布美国出口管制解除，Claude Fable 5恢复全球可用，Mythos 5通过合作伙伴扩展访问。同日发布Claude
  Sonnet 5，作为Free和Pro用户的默认模型，面向代理工作负载优化，定价低于Opus且幻觉率降低。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Amazon
  - Etched
  - Google
  - OpenAI
  technologies:
  - Claude Sonnet 5
  - Claude Fable 5
  - Claude Mythos 5
  - GeneBench-Pro
  - Gemini Omni Flash
  key_people:
  - Matt Shumer
  - Rob Hallam
key_logic_flow:
- Anthropic宣布美国出口管制解除，Claude Fable 5于7月1日恢复全球可用，Mythos 5通过已批准合作伙伴扩展访问
- Anthropic发布Claude Sonnet 5，作为Free和Pro用户的默认模型，在代理工作、工具使用、编码和浏览任务上接近Opus 4.8水平
- Claude Sonnet 5的API定价为每百万输入/输出token $2/$10（8月31日前优惠价），之后调整为$3/$15
- Claude Sonnet 5的幻觉率和谄媚率低于Sonnet 4.6，默认启用网络安全防护
- 亚马逊启动了10亿美元的前沿部署AI工程组织
- Etched以50亿美元估值走出隐身模式，签订了10亿美元的已签约合同
extract_result: success
---

# 😺 Fable 5 is back baby

## PLUS: Claude 5 Sonnet, AWS embeds agents, Etched exits stealth, and SF gets pricier.

Welcome, humans.

AI Independence day just came early, as late yesterday afternoon Anthropic announced Fable 5 is coming back online today.

*Technically,* that means U.S. export controls on Claude Fable 5 and Mythos 5 were lifted, with Fable 5 returning globally later today on July 1 and Mythos 5 access expanding through approved partners.

That’s a big deal because Fable 5 had become the model people were treating like some forbidden power locked away. Before access disappeared, Matt Shumer used it to build an explorable, screen-accurate 3D Hogwarts castle from one prompt

**And now, a dash of cold water:** Rob Hallam called it "happy, but mostly disappointed," since routine coding now gets flagged more often and access is capped at half of weekly limits through July 7. *Welcome back, have fun, but not for long...*

**Here’s what happened in AI today:**

😺

**Anthropic**released Claude Sonnet 5 and Claude Science.📰

**Amazon**launched a $1B forward-deployed AI engineering org.📰

**Etched**exited stealth at a $5B valuation with $1B in signed contracts.🍪

**Google**launched Nano Banana 2 Lite and Gemini Omni Flash.📰

**OpenAI**introduced GeneBench-Pro, a computational biology benchmark.

# 😼 Claude Sonnet 5 brings Anthropic’s agent push to the default model

Every AI lab wants you to hand more work to agents. The catch: agents get expensive when they need the giant model, and riskier when that model starts touching browsers, terminals, codebases, and company data.

Anthropic’s answer is Claude Sonnet 5, its new default model for Free and Pro users, built to plan, use tools, code, browse, and run longer tasks without needing the pricier Opus tier.

**Here’s what happened:**

Sonnet 5 is now available across Claude plans, Claude Code, and the API.

Anthropic says it performs close to Opus 4.8 on agentic work, at lower prices.

Intro API pricing is $2 / $10 per million input / output tokens through Aug. 31, then $3 / $15.

Early testers praised its follow-through: bug fixes, pull requests, Salesforce updates, insurance workflows, legal research, and data exploration.

Anthropic says it has lower rates of hallucination and sycophancy than Sonnet 4.6, with cyber safeguards on by default.


**How to try it:**

Open Claude; Free and Pro users should see Sonnet 5 as the default.

In Claude Code, select Sonnet 5 for coding workflows.

For developers, call claude-sonnet-5 through the Claude API.


**Why this matters: **Sonnet is the model most Claude normies actually touch. Opus is the fancy chef’s knife, while Sonnet is the one that lives in the drawer and actually gets used for Tuesday dinner. *Congrats Chef, you have a better everyday knife! Yes, Chef!*