---
title: The Website Specification
source: https://specification.website/
author:
- '[[k1m]]'
published: '2026-05-31'
created: '2026-06-01'
description: 'Article URL: https://specification.website/ Comments URL: https://news.ycombinator.com/item?id=48343683
  Points: 430 # Comments: 180'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f9cb2c160bbcd29a
source_type: community_discussion
tldr: The Website Specification 是一份平台无关的技术规范清单，定义了每个优秀网站应有的功能特性，涵盖 SEO、可访问性、安全、性能等十个领域，并提供
  MCP 服务器和 Agent Skill 供 AI 代理查询。
objective_summary: 'The Website Specification 项目发布了一份平台无关的网站技术规范，从 HTML 基础到安全头、可访问性、性能优化和国际化的完整检查清单。该规范以标准组织（WHATWG、W3C、IETF、WCAG、MDN）的官方标准为依据，适用于
  WordPress、Next.js、Astro 等任意技术栈。项目同时提供了开放的 MCP 服务器（mcp.specification.website）和 Agent
  Skill，允许 AI 代理以编程方式查询规范，还通过 /llms.txt 和 Accept: text/markdown 提供每页的 Markdown 版本。'
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - MCP
  - llms.txt
  - WCAG
  - SEO
  key_people: []
key_logic_flow:
- The Website Specification 是一份平台无关的网站技术规范，列出了每个优秀网站应具备的功能特性。
- 规范涵盖十个核心领域：基础、SEO、可访问性、安全、Well-Known URIs、代理就绪、性能、隐私、弹性和国际化。
- 每一项都链接回 WHATWG、W3C、IETF RFC、WCAG 和 MDN 等标准机构的官方标准。
- 该规范通过开放的 MCP 服务器（mcp.specification.website）提供只读查询接口，无需认证。
- 项目还发布了 Agent Skill，可教导兼容的 AI 代理在何时以及如何使用该规范。
- '每页内容可通过 /llms.txt 和 Accept: text/markdown 获取 Markdown 格式。'
extract_result: success
object_mentions:
- object_type: project
  name: The Website Specification
  canonical_name: The Website Specification
  url: https://specification.website/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - The Website Specification 是一份平台无关的技术规范清单，定义了每个优秀网站应有的功能特性。
  - 该规范涵盖基础、SEO、可访问性、安全、性能、隐私等十个核心领域，并链接到 WHATWG、W3C 和 IETF RFC 等官方标准。
  article_id: f9cb2c160bbcd29a
- object_type: project
  name: specification.website MCP Server
  canonical_name: specification.website MCP Server
  url: https://mcp.specification.website/mcp
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 项目提供开放的 MCP 服务器（mcp.specification.website），允许 AI 代理以只读方式查询规范，无需认证。
  - 'MCP 服务器的配置为 transport: http, url: https://mcp.specification.website/mcp。'
  article_id: f9cb2c160bbcd29a
- object_type: project
  name: llms.txt
  canonical_name: llms.txt
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 规范通过 /llms.txt 提供每页的 Markdown 内容，便于 AI 代理和爬虫读取。
  - llms.txt 是项目中 Agent Readiness 领域的一部分，用于让网站对 AI 代理更可读。
  article_id: f9cb2c160bbcd29a
---

# What a good website does.

A platform-agnostic specification of the technical features every
decent website should have — from `<title>`

to `/.well-known/security.txt`

,
from WCAG contrast to `llms.txt`

.
Written for humans and agents.

-
### Foundations

14The HTML, head, and document basics every page needs.

-
### SEO

13Search visibility — robots.txt, sitemaps, canonicals, structured data.

-
### Accessibility

20WCAG-aligned rules so people of all abilities can use the site.

-
### Security

12Headers, transport, and policies that keep visitors safe.

-
### Well-Known URIs

9Standard, agreed-upon paths under /.well-known/.

-
### Agent Readiness

18Things that make a site legible to AI agents and crawlers.

-
### Performance

19Core Web Vitals, caching, images, fonts, network behaviour.

-
### Privacy

6Consent, signals, and respecting visitor choice.

-
### Resilience

5Graceful failure — error pages, offline, redirects.

-
### Internationalisation

12Language, locale, direction, and translated content.


### Standards, not opinions

Each topic links back to the source standard — WHATWG, W3C, IETF RFCs, WCAG, MDN, and the organisations defining the modern web.

### Platform agnostic

Whether you ship WordPress, Drupal, TYPO3, Next.js, Astro, Hugo, a Django app, or plain HTML, the spec is the spec. Implementation hints follow it, not the other way round.

## Let your agent query the spec.

The whole spec is available as an open MCP server — read-only, no auth — plus a published Agent Skill that teaches any compatible agent when and how to use it. Per-page Markdown is available via `/llms.txt`

and `Accept: text/markdown`

on any spec URL.

```
{
"mcpServers": {
"specification-website": {
"transport": "http",
"url": "https://mcp.specification.website/mcp"
}
}
}
```


## How to use this site

- 01
### Audit

Run through the checklist. Each item is a “does the site do this — yes or no.”

- 02
### Learn

Click into any item for what it is, why it matters, and how to implement it.

- 03
### Improve

Found a gap, a stale fact, or a missing topic? Open a PR. Sources required.