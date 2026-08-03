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
object_insights:
- object_type: project
  name: The Website Specification
  canonical_name: The Website Specification
  url: https://specification.website/
  positioning: 一份平台无关的网站技术规范清单，覆盖基础、SEO、可访问性、安全、性能、隐私等十个领域，以 WHATWG、W3C 和 IETF 等官方标准为基准。
  technical_signal: 以 WHATWG、W3C、IETF RFC、WCAG 和 MDN 等标准机构官方文档为来源，构建了涵盖十个技术领域共上百条可验证检查项的完整体系。
  adoption_signal: 项目通过开放的 MCP 服务器和 Agent Skill 降低集成门槛，但目前处于发布初期，实际社区采用情况有待进一步观察。
  ecosystem_relevance: 同时对接 Web 标准机构生态和 AI 代理协议（MCP）生态，可作为网站开发标准与 AI 可发现性之间的桥梁。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该项目创新性地将传统 Web 技术标准与 AI 代理可读性（MCP、llms.txt）结合起来，若获得社区采纳可能成为新一代网站开发质量基准，其
    MCP 服务器也为标准化 AI-Web 交互提供了参考范例。
  risk_notes:
  - 作为社区驱动的规范项目缺乏官方权威机构背书，推广依赖开发者自愿采纳。
  - 覆盖面广但深度有限，可能无法替代 MDN 等既有专业指南的参考地位。
  score: 7.0
  article_ids:
  - f9cb2c160bbcd29a
  evidence_snippets:
  - The Website Specification 是一份平台无关的技术规范清单，定义了每个优秀网站应有的功能特性。
  - 该规范涵盖基础、SEO、可访问性、安全、性能、隐私等十个核心领域，并链接到 WHATWG、W3C 和 IETF RFC 等官方标准。
- object_type: project
  name: specification.website MCP Server
  canonical_name: specification.website MCP Server
  url: https://mcp.specification.website/mcp
  positioning: The Website Specification 项目附属的开放 MCP 服务器，允许 AI 代理以只读方式查询网站技术规范，无需认证即可通过
    HTTP 协议访问。
  technical_signal: 基于 MCP HTTP 传输协议实现，提供无认证只读查询接口，配置只需一行 JSON，可作为 MCP 服务器设计与部署的参考实践。
  adoption_signal: 作为主项目的附属服务，采用情况直接受 The Website Specification 推广进度影响，目前处于早期发布阶段。
  ecosystem_relevance: 与 MCP 协议生态直接相关，是少数提供公开可访问 MCP 服务器的项目之一，可为社区开发者提供实现参考。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为首批对公众开放且无需认证的 MCP 服务器之一，其架构设计和接口规范对 MCP 生态发展具有参考价值，但独立发展空间与主项目的推广深度绑定。
  risk_notes:
  - 附属项目特性限制了独立发展空间，生命周期完全依赖主项目的维护持续性。
  score: 4.0
  article_ids:
  - f9cb2c160bbcd29a
  evidence_snippets:
  - 项目提供开放的 MCP 服务器（mcp.specification.website），允许 AI 代理以只读方式查询规范，无需认证。
  - 'MCP 服务器的配置为 transport: http, url: https://mcp.specification.website/mcp。'
- object_type: project
  name: llms.txt
  canonical_name: llms.txt
  url: null
  positioning: 一项让网站对 AI 代理和爬虫更友好的标准化约定，通过在网站提供 Markdown 格式的内容摘要来优化 AI 的信息获取效率。
  technical_signal: 采用简单的文本文件约定，通过 /llms.txt 路径提供网站内容的 Markdown 摘要，无需额外基础设施即可实现。
  adoption_signal: 已被 The Website Specification 纳入 Agent Readiness 标准领域，标志着该方案在网站标准社区中获得初步认可。
  ecosystem_relevance: 作为 AI 代理可发现性领域的关键组件，与 MCP 服务器互补，共同构成网站对 AI 友好的基础设施栈。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: llms.txt 作为连接 Web 内容与 AI 代理的轻量级标准，若被广泛采纳将显著提升 AI 代理获取 Web 信息的效率，值得关注其在标准社区中的推广进展。
  risk_notes:
  - 作为社区提案而非官方标准，长期推广面临与既有站点地图等主流机制的竞争。
  score: 3.0
  article_ids:
  - f9cb2c160bbcd29a
  evidence_snippets:
  - 规范通过 /llms.txt 提供每页的 Markdown 内容，便于 AI 代理和爬虫读取。
  - llms.txt 是项目中 Agent Readiness 领域的一部分，用于让网站对 AI 代理更可读。
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