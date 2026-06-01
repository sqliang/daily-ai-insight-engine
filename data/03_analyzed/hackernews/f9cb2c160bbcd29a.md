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
tldr: 一份平台无关的网站技术规范，涵盖SEO、可访问性、安全等10个类别，并提供MCP服务器接口。
objective_summary: 一份名为The Website Specification的开放技术规范发布，定义了每个网站应具备的技术特性标准，涵盖HTML基础、SEO、可访问性、安全、Well-Known
  URI、Agent就绪性、性能、隐私、弹性和国际化10个类别，并提供MCP服务器和Agent Skill供AI代理查询。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - MCP
  - WCAG
  - SEO
  - llms.txt
  key_people: []
key_logic_flow:
- 该规范定义了每个合格网站应具备的技术特性，内容覆盖HTML基础、SEO、可访问性、安全、Well-Known URI、Agent就绪性、性能、隐私、弹性和国际化10个类别。
- 每个规范条目均链接回对应的权威标准来源，包括WHATWG、W3C、IETF RFC、WCAG和MDN。
- 该规范支持WordPress、Drupal、Next.js、Astro、Hugo、Django及纯HTML等所有平台，实现提示跟随规范而非反过来。
- 整套规范以开源MCP服务器形式提供，无需认证的只读访问，同时发布了Agent Skill供兼容的AI代理使用。
- '用户可通过llms.txt和Accept: text/markdown头获取每页的Markdown版本。'
- 该站点提供审计清单供开发者逐项检查、点击进入学习实现细节，并通过GitHub PR接受改进建议。
impact_score:
  score: 4.5
  reason: 该规范本身是对已有Web标准（WHATWG、W3C、IETF RFC等）的编排整理，而非技术突破，短期对行业冲击有限。但其以MCP服务器+Agent
    Skill形式提供规范查询接口的模式具有示范意义——这是将技术文档/规范以机器可读可查询方式交付给AI代理的早期实践，可能催生更多'规范即MCP服务'的生态。不过当前影响力仅限于Web开发社区的小众讨论。评分4.5：介于'日常更新'和'局部格局变化'之间，模式创新加分，内容本身无冲击。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: MCP服务器作为技术规范交付方式的可行性
hype_assessment:
  level: low
  reason: 网站原文无任何'颠覆'、'革命性'等PR滥用词汇，表述克制且务实（'What a good website does'、'Standards,
    not opinions'）。内容以清单形式呈现已有标准并链接至权威来源，不存在概念包装或夸大宣传。
information_entropy: medium
domain_disruption:
  technical_innovation: 技术内容本身为已有Web标准的聚合，无本质突破。但其以MCP Server作为规范交付媒介的方式具有模式创新——将原本面向人类的静态文档转化为AI代理可交互查询的接口，可能成为'文档即MCP服务'这一新范式的参考模板。
  business_model: 无
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 该规范的长期复利价值在于它试图成为AI时代网站质量的'基准层'——通过MCP服务器为AI Agent提供标准化的网站查询接口，同时聚合WHATWG/W3C/WCAG等权威标准形成一站式审计清单。其复利效应来自网络效应：越多网站遵循该规范，Agent生态对其依赖越深，进而倒逼更多网站采纳，形成正向循环。然而，其本质是对已有标准的整理而非底层技术创新，没有专有协议锁定或数据飞轮，且完全开源无商业壁垒，容易被更权威的组织（如W3C自身）或更大体量的平台（如Google
    Web.dev）的类似倡议覆盖。短期1-2年内价值有限，但若Agent生态爆发，作为'Agent读网站的第一本词典'可能成为细分基础设施。评分6.5反映了'潜力可观但执行风险和替代风险并存'的判断。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- OpenAI
- WordPress
- Next.js
- Astro
- 小型Web开发团队
competitive_casualty:
- 付费网站审计工具(Siteimprove、Monsido等)
- 封闭式SEO检测服务
- 平台绑定的Web质量文档
market_opportunities:
- 开发者可基于该规范的 MCP 服务器接口，构建 AI 驱动的网站合规性自动审计工具，为企业和代理机构提供自动化检测服务
- Web 开发和咨询团队可将该规范作为标准化服务产品，推出网站技术健康度评估与改造套餐，覆盖 SEO/可访问性/安全等十大维度
- 前端的 Agent Readiness 类别为希望被 AI 代理良好索引的网站提供了明确指引，可衍生出面向 AI 友好的网站优化咨询服务
risk_matrix:
  regulatory: 该规范本身是社区驱动的技术指南而非监管要求，但引用 WCAG 可访问性标准，在某些司法管辖区（如 EU 的 EAA 法案）可能间接与法律合规要求挂钩，实施不完整时存在合规隐患
  technological: 该规范是对已有权威标准（WHATWG、W3C、IETF RFC 等）的汇总而非原创技术标准，技术替代风险较低；但若长期缺乏维护，部分条目可能因底层标准更新而过时
  competitive: 存在同类网站质量检查工具（如 Lighthouse、web.dev、PageSpeed Insights）的竞争压力；规范本身是开放、免费的，差异化壁垒不高，但
    MCP 服务器的形式是一大特色
  ethical: 无显著伦理风险；规范倡导的隐私、可访问性等价值观本身具有正面社会意义
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
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