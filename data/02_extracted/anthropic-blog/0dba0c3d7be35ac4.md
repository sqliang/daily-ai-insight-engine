---
title: Claude Design Anthropic Labs
source: https://www.anthropic.com/news/claude-design-anthropic-labs
author: []
published: '2026-05-28'
created: '2026-06-01'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0dba0c3d7be35ac4
source_type: tech_blog
tldr: Anthropic 发布 Claude Design，这是一款基于 Claude Opus 4.7 的视觉设计协作产品，支持创建原型、幻灯片、营销素材等视觉作品，已面向
  Pro、Max、Team 和 Enterprise 订阅用户开放研究预览。
objective_summary: 2026年7月21日，Anthropic 通过官方博客宣布推出 Anthropic Labs 的首款产品 Claude Design。该产品由
  Claude Opus 4.7 视觉模型驱动，用户可通过自然语言描述需求，与 Claude 协作创作设计稿、原型、幻灯片和一页纸等视觉作品。Claude Design
  支持导入团队设计系统、从代码库读取品牌规范，并提供内联评论、直接编辑和自定义滑块等精细化控制功能。该产品以研究预览形式面向 Claude Pro、Max、Team
  和 Enterprise 订阅用户逐步开放。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  technologies:
  - Claude Opus 4.7
  key_people: []
key_logic_flow:
- Anthropic 推出 Anthropic Labs 的首款产品 Claude Design，这是一款基于 Claude Opus 4.7 的视觉设计协作工具。
- Claude Design 以研究预览形式向 Claude Pro、Max、Team 和 Enterprise 订阅用户逐步开放。
- 用户可以通过自然语言描述需求，由 Claude 搭建初版，再通过对话、内联评论、直接编辑或自定义滑块进行精细化调整。
- Claude Design 在 onboarding 阶段通过读取团队代码库和设计文件自动构建设计系统，后续项目自动使用统一的颜色、字体和组件。
- 团队已将 Claude Design 用于交互原型、产品线框图、设计探索、提案演示、营销物料和前沿设计等多种场景。
- 用户可以从文本提示、上传文件或代码库导入内容，最终可导出为 PPTX 或发送到 Canva。
extract_result: success
object_mentions:
- object_type: product
  name: Claude Design
  canonical_name: Claude Design
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 推出了 Anthropic Labs 的首款产品 Claude Design，允许用户与 Claude 协作创建设计稿、原型、幻灯片等视觉作品。
  - Claude Design 由 Claude Opus 4.7 驱动，以研究预览形式面向 Claude Pro、Max、Team 和 Enterprise
    订阅用户开放。
  - Claude Design 支持导入团队设计系统，用户可通过内联评论、直接编辑和自定义滑块进行精细化调整。
  article_id: 0dba0c3d7be35ac4
- object_type: model
  name: Claude Opus 4.7
  canonical_name: Claude Opus 4.7
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Claude Design 由 Anthropic 目前最强的视觉模型 Claude Opus 4.7 驱动。
  article_id: 0dba0c3d7be35ac4
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 产品经理可以把功能流程草图交给 Claude Code 进行实现，或者与设计师协作进一步细化。
  article_id: 0dba0c3d7be35ac4
---

# Introducing Claude Design by Anthropic Labs

Today, we’re launching Claude Design, a new Anthropic Labs product that lets you collaborate with Claude to create polished visual work like designs, prototypes, slides, one-pagers, and more.

Claude Design is powered by our most capable vision model, Claude Opus 4.7, and is available in research preview for Claude Pro, Max, Team, and Enterprise subscribers. We’re rolling out to users gradually throughout the day.

## Design with Claude

Even experienced designers have to ration exploration—there's rarely time to prototype a dozen directions, so you limit yourself to a few. And for founders, product managers, and marketers with an idea but not a design background, creating and sharing those ideas can be daunting.

Claude Design gives designers room to explore widely and everyone else a way to produce visual work. Describe what you need and Claude builds a first version. From there, you refine through conversation, inline comments, direct edits, or custom sliders (made by Claude) until it’s right. When given access, Claude can also apply your team’s design system to every project automatically, so the output is consistent with the rest of your company’s designs.

Teams have been using Claude Design for:

**Realistic prototypes:**Designers can turn static mockups into easily-shareable interactive prototypes to gather feedback and user-test, without code review or PRs.**Product wireframes and mockups:**Product Managers can sketch out feature flows and hand them off to Claude Code for implementation, or share them with designers to refine further.**Design explorations:**Designers can quickly create a wide range of directions to explore.**Pitch decks and presentations:**Founders and Account Executives can go from a rough outline to a complete, on-brand deck in minutes, and then export as a PPTX or send to Canva.**Marketing collateral:**Marketers can create landing pages, social media assets, and campaign visuals, then loop in designers to polish.**Frontier design**: Anyone can build code-powered prototypes with voice, video, shaders, 3D and built-in AI.

## How it works

Claude Design follows a natural creative flow.

**Your brand, built in.** During onboarding, Claude builds a design system for your team by reading your codebase and design files. Every project after that uses your colors, typography, and components automatically. You can refine the system over time, and teams can maintain more than one.

**Import from anywhere.** Start from a text prompt, upload images and documents (DOCX, PPTX, XLSX), or point Claude at your codebase. You can also use the web capture tool to grab elements directly from your website so prototypes look like the real product.

**Refine with fine-grained controls.** Comment inline on specific elements, edit text directly, or use adjustment knobs to tweak spacing, color, and layout live. Then ask Claude to apply your changes across the full design.