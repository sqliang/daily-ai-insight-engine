---
title: The short leash AI coding method for beating Fable
source: https://blog.okturtles.org/2026/07/short-leash-ai-method/
author:
- '[[Riseed]]'
published: '2026-07-02'
created: '2026-07-03'
description: 'Article URL: https://blog.okturtles.org/2026/07/short-leash-ai-method/
  Comments URL: https://news.ycombinator.com/item?id=48766026 Points: 130 # Comments:
  156'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0e7fdbf2be5bffb3
manifest_dates:
- '2026-07-03'
source_type: community_discussion
tldr: 专家开发者应全程参与AI编程，审查每次diff，拒绝不良变更以产出高质量代码。
objective_summary: okTurtles 的 Greg Slepak 基于一年以上研究，提出"短绳"AI 编程方法论。该方法要求专家开发者的人工介入保持在循环中，审查
  AI 的每次 diff 变更并拒绝不良提议，替代当前流行的"氛围编程"方式。同时提出 AI 与人类联合审查 PR 的流程，要求 AI 辅助的 PR
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - okTurtles
  technologies:
  - AI coding agents
  - Fable
  key_people:
  - Greg Slepak
key_logic_flow:
- 作者 Greg Slepak 经过一年研究，认为当前 AI 编程的"氛围编程"方式（多智能体并行、开发者脱离代码审查）无法产出高质量代码，仅适用于不关注质量的场景。
- 短绳方法要求开发者全程参与：使用规划阶段制定任务计划，从不使用"YOLO"模式，AI 从不脱离人工监控独立工作。
- 开发者必须坐在屏幕前逐行审查 AI 提出的每次 diff 变更，随时拒绝不良变更以防止 AI 偏离轨道，每个子任务结束时提交一次 commit 以保护已完成的代码。
- AI 代码审查应作为"linter"角色快速捕获常见错误，而人类审查者负责发现高层次问题和方向性变更，两者结合优于单一审查方式。
- 使用 AI 辅助的 PR 作者必须以审查他人 PR 的态度逐行自审自己的 PR，确认理解后再提交给维护者，并在 PR 描述中披露所用 AI 模型。
extract_result: success
impact_score:
  score: 3.5
  reason: 这是一篇来自个人技术博客的方法论文章，提出了'短绳编程'概念作为对'氛围编程'的反拨。文章本身不涉及新产品发布、融资或技术突破，其影响力受限于作者个人影响力（okTurtles）和传播渠道。虽然'人工监督回归'是业界正在讨论的趋势，但该文更多是对已有实践的系统化总结，而非开创性贡献。短期行业冲击力有限，属于小圈子内的方法论讨论。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: AI编程是否需要开发者全程人工监督，以及'氛围编程'是否牺牲了代码质量
hype_assessment:
  level: low
  reason: 文章基于作者一年以上的实际使用经验，提供了具体可操作的方法论步骤（规划阶段→逐diff审查→拒绝不良变更→子任务提交→联合审查），语言风格务实克制。没有使用'颠覆性'、'革命性'、'改变游戏规则'等PR词汇，也没有推销任何产品或服务，属于实打实的经验分享。
information_entropy: medium
domain_disruption:
  technical_innovation: 无——本文属于AI编程方法论和最佳实践总结，不涉及技术架构或工程实现的突破。其核心建议（人工保持循环、逐diff审查、拒绝不良变更）本质上是工程流程规范，而非技术创新。
  business_model: 无——不涉及商业模式或SaaS生态影响。
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 本文提出'短绳'方法论，主张专家开发者全程介入AI编程流程，拒绝当前流行的'氛围编程'（多智能体并行、开发者脱离代码审查）模式。该观点若被企业工程团队采纳为主流实践，将重塑AI编程工具的市场格局：资本将从追求完全自主的AI编码平台（如Fable）转向人机协作的增强型工具。但作为一篇方法论博客，其本身不具备复利效应或网络效应——无产品、无商业模式、无用户锁定，仅通过思想传播影响行业认知与资金流向。长期价值取决于该理念能否在注重代码质量的行业（金融、安全、基础设施）形成标准实践。估值4.5分：有潜力成为AI工程实践的指导思想，但非直接的投资标的。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- GitHub Copilot
- Cursor
- Anthropic
competitive_casualty:
- Fable
- Devin
- 自主编码代理平台
market_opportunities:
- 企业级AI代码审查工具可围绕"短绳"方法论设计，内置强制人工审批、逐行diff审查和AI信息披露功能，满足安全关键系统的高质量标准
- 可为金融、医疗、基础设施等受监管行业提供"短绳AI编程"咨询与培训服务，帮助组织在不牺牲代码质量的前提下提升开发效率
- AI编程Agent产品可增加"短绳模式"作为可选工作流，默认禁用YOLO模式并强制每步diff人工确认，在保证质量的同时提升专家开发者的采用率
risk_matrix:
  regulatory: AI辅助编程的透明度要求日益严格（如欧盟AI Act对高风险系统的可解释性要求），该文提倡的AI信息披露和人工审查流程有助于合规，但方法论本身未涉及数据隐私、出口管制等具体合规条款
  technological: 短绳方法依赖开发者技能超过AI模型能力，随着前沿模型推理能力持续提升，该方法对于非安全关键场景的必要性可能下降；此外，该方法高度依赖特定工具链（如Crush
    fork、diff展示Agent），存在工具生态演变导致的适配风险
  competitive: 在AI编程效率竞赛中，短绳方法的逐行人工审查模式可能显著降低开发速度，采用该方法的团队可能在快速原型验证和功能迭代上落后于采用自主Agent的竞争对手
  ethical: 该方法明确要求开发者全程参与并理解AI生成的每一行代码，有助于防止技术债积累和代码质量下滑；但拒绝对AI代码不加审查的"氛围编程"可能加剧"专家越强、AI辅助越有效"的马太效应，拉大资深开发者与初级开发者之间的技能鸿沟，对软件工程人才培养产生负面影响
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
---

This post is the culmination of over a year of research into how to properly use AI agents to write high-quality software in security-critical systems.

I will be writing this post primarily from my perspective as a software developer, protocol developer, and maintainer of security-critical software.

Over the past year I dove deep into AI agents. I have explored their limits, what they can and cannot be relied upon to do. I’ve created our own AI review tools that perform just as well as multi-billion dollar AI-review systems. I’ve maintained my own custom fork of an AI coding agent called Crush. And this post is my distillation of what I’ve learned to be the best approach if you want to create high-quality software using AI tools.

There are some people who hate AI. Indeed, many developers *should* hate AI, because it is an enemy to their own learning of software development. This post is not for them. This post is for the few expert developers whose skills have reached the point where they outclass any and all “frontier AI models” in their area of expertise. It is for these expert developers, who want to use AI as a method of increasing their performance *without sacrificing any quality* that I write this post.

## Problems With Current Approaches

If you’ve used AI agents much, you know that during the course of a session the following can happen:

- You can discover that your initial idea was dumb and a better one exists
- Your agent might go “off the rails” and start doing something you don’t want it to do

I’ve watched videos with hundreds of thousands of views where YouTubers explain how they invented complicated systems of 12 parallel agents managed by an orchestrator, doing a billion things simultaneously. How they no longer have to involve themselves in the coding process. It’s just slop writing and reviewing slop while the YouTuber sits on a beach, goes to the bathroom, or sips coffee for no reason.

It is humanly impossible to build your own understanding of a codebase if you use such a “Vibe” approach. The AI will have gone off the rails multiple times and you will only notice it later when you actually try to use the software. This method may be perfectly OK in situations where you do not care about quality, but if you *do care*, a different approach is needed.

The problem is that even code written and/or reviewed by Fable 5, will stink:

The code works, but it is horribly inefficient and ugly. And this will definitely happen more often if you are working in some kind of a niche area that doesn’t have much training data for the model to fall back on. Contrary to marketing statements made by certain CEOs, these models are not able to think beyond their training data.

## AI Code Generation — The “Short Leash” Method

That brings us to the “short leash method” for using AI coding agents.

This method cannot be employed by just anyone. Only professional software developers can use this method. But what’s great about it is that it will lead to Fable-beating results even if you aren’t using a frontier model.

In the Short Leash method:

- You use a planning phase to research the task and formulate a plan, along with something like my tasks skill to track progress and break large tasks into steps (this is one point of commonality with many “vibe engineering” methods; the approach diverges in the following bullet points.)
- You never use “YOLO” mode (aka “dangerously skip permissions”)
- The AI never works “while you play video games”
- You use a coding agent that displays a diff of the changes that are about to be made via the permissions prompt
- You sit there like some crazed person from the 20th century, and actually analyze the changes the AI is proposing to make
- You keep yourself in the loop at all times instead of removing yourself (the trend promoted by YouTubers)
- You use the diffs in the permissions prompts as a way to keep your understanding of the codebase up-to-date and the AI on a “short leash”
- You DENY permissions any time you see that the AI is about to do something you don’t want it to do
- You intervene frequently and as needed to prevent the AI from “going off the rails”
- At all times, the AI is “kept on a short leash”
- Commits are made at the end of every subtask to protect you from the AI screwing up and deleting previously done work (this can happen, I’ve seen Opus do it)
- Finally, we do a review

## How to do AI Reviews

A PR reviewed by just a human or just an AI will have more mistakes in it than a PR that’s reviewed by *both* a human and an AI.

The AI can be treated as a linter. It will quickly catch common mistakes, while the human will catch higher-level issues and directional changes that need to be made.

So when it comes to reviews:

- You should be using AI to review every single PR.
- The AI must have access to sufficient context (the issue, the PR description, the codebase, and the changes).
- You should use the latest and greatest models available to review.
- The PR description must disclose the precise models used (if any) in assisting with the creation of the PR under an “AI Disclosure” heading. This serves multiple purposes:
- It informs the maintainer that AI was used.
- It lets them suggest better models if weak ones were used.
- It signals that you’re a “good guy” developer and aren’t trying to “sneak AI in”.

- Finally, and most importantly, the PR
**must be reviewed by the PR ‘author’ if it used AI.**

That last point is worth expounding upon a bit.

AI-assisted PRs are really PRs from an AI with human assistance. Therefore, the human submitting the PR is expected to understand what they are submitting, and they cannot do that if they haven’t reviewed the code the AI wrote.

So they must treat their own PR as if they’re reviewing someone else’s PR, and review it themselves, line-by-line. Once finished, they can confirm their own approval of the PR, and request attention from the maintainer. This builds and demonstrates their understanding of the codebase.

## Fin

And that’s how we use AI at okTurtles. You can read our official AI Usage Policy.

We hope this post has been helpful.

*AI Disclosure: this post was entirely written by human fingers connected to a human brain. A final AI-style “spell check” was performed before publishing.*

**Donating = Loving!**

Without our supporters, we can't do what we do.

Please take this moment to support our work.