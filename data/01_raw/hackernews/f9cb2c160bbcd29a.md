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
pipeline_stage: ingested
id: f9cb2c160bbcd29a
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