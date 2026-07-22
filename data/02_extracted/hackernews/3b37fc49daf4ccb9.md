---
title: 'Jelly UI: Soft-body physics for native HTML form controls'
source: https://jelly-ui.com/
author:
- '[[baldvinmar]]'
published: '2026-07-20'
created: '2026-07-21'
manifest_dates:
- '2026-07-21'
description: 'Article URL: https://jelly-ui.com/ Comments URL: https://news.ycombinator.com/item?id=48981620
  Points: 491 # Comments: 154'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3b37fc49daf4ccb9
source_type: community_discussion
tldr: Jelly UI 发布了一个零依赖的 Web Components 库，为原生 HTML 表单控件引入软体物理动画效果，提供触感交互体验并内置无障碍支持。
objective_summary: Jelly UI 推出了一款基于 Web Components 且无需外部依赖的 UI 库。该库将软体物理效果应用于原生 HTML
  表单控件，开发者可通过 `<jelly-button>`、`<jelly-theme>` 等自定义标签直接使用。它内置了深色模式、从右到左布局支持以及 WCAG
  AA 级色彩令牌，兼顾美观与无障碍合规。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - Web Components
  - WCAG
  key_people: []
key_logic_flow:
- Jelly UI 是一个零外部依赖的 Web Components 库，专注于构建柔软触感的界面交互。
- 该库将原生 HTML 表单控件与软体物理效果相结合，为常规表单元素带来生动的物理反馈。
- Jelly UI 内置了深色模式和从右到左布局支持，满足多语言和多主题需求。
- 该库提供 WCAG AA 级色彩令牌，确保界面在色彩对比度上符合无障碍访问标准。
- 开发者可通过 `<jelly-button>`、`<jelly-theme>` 等自定义 Web Components 标签直接引入使用。
object_mentions:
- object_type: project
  name: Jelly UI
  canonical_name: Jelly UI
  url: https://jelly-ui.com/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Jelly UI 是一个零外部依赖的 Web Components 库，用于构建柔软触感的界面交互。
  - 该库将真实表单控件与软体物理效果相结合，并内置深色模式和从右到左布局支持。
  - Jelly UI 提供 WCAG AA 级色彩令牌和 `<jelly-button>`、`<jelly-theme>` 等自定义元素。
  article_id: 3b37fc49daf4ccb9
extract_result: success
---

# It's okay to be

a little jelly

Jelly UI is a dependency-free Web Components library for soft, tactile product interfaces. Real form controls meet soft-body physics, with dark mode, right-to-left support and WCAG AA color tokens built in.

```
<script type="module" src="https://jelly-ui.com/package.js"></script>
<jelly-theme mode="auto">
<jelly-button variant="mint">Publish</jelly-button>
</jelly-theme>
```