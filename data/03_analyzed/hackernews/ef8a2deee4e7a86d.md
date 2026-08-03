---
title: Building an HTML-first site doubled our users overnight
source: https://mohkohn.co.uk/writing/html-first/
author:
- '[[edent]]'
published: '2026-06-10'
created: '2026-06-11'
description: 'Article URL: https://mohkohn.co.uk/writing/html-first/ Comments URL:
  https://news.ycombinator.com/item?id=48475483 Points: 1123 # Comments: 506'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ef8a2deee4e7a86d
source_type: community_discussion
tldr: 作者为一家公用事业公司使用 Astro 构建了 HTML-first 的多步骤表单网站，上线后次日完成表单的用户数翻倍。该站点无需 JavaScript
  即可运行，并通过后端会话持久化确保用户数据永不丢失。
objective_summary: 一家受监管的垄断型公用事业公司面临客户满意度低于 96% 将导致数百万英镑罚款的压力。此前两次尝试包括一次外包 React 方案均告失败，React
  应用上线仅 3 天即因大量加载转圈和全局状态问题被撤回。作者 Moh Kohn 使用 Astro 构建了 HTML-first 的渐进增强表单应用，每个步骤作为独立页面，通过表单提交和后端重定向实现流程。上线后次日完成表单的用户数翻倍。作者还开发了
  validation-enhancer 这个不到 1KB 的 HTML Web Component，用于渐进增强原生表单验证。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - Astro
  - React
  - Web Components
  - Remix
  - HTML-first
  - WCAG
  - ARIA
  key_people:
  - Moh Kohn
  - Terence Eden
key_logic_flow:
- 作者客户是一家受监管的垄断型公用事业公司，客户满意度低于 96% 将面临数百万英镑罚款。
- 此前两次尝试（包括一次外包 React 应用）均失败，React 应用因大量加载转圈和全局 JavaScript 状态问题上线 3 天即被撤回。
- 作者使用 Astro 构建 HTML-first 方案，每个表单步骤为独立页面，通过后端提交和重定向实现流程流转。
- 作者构建了 validation-enhancer Web Component，体积不到 1KB，可渐进增强原生 HTML 表单验证。
- 上线后次日完成表单的用户数翻倍，JavaScript 分析工具甚至无法追踪这些新增用户的来源。
- 有用户在一个月前启动表单填写，一个月后才完成提交，后端会话持久化策略保证了数据不丢失。
extract_result: success
object_mentions:
- object_type: project
  name: validation-enhancer
  canonical_name: validation-enhancer
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者构建了一个名为 validation-enhancer 的 HTML Web Component，包装在表单外部并利用浏览器原生验证进行渐进增强。
  - 该组件不到 1KB，如果加载失败则回退到浏览器内置验证，后端 API 作为最终验证兜底。
  - 作者声称这是从业 20 多年来用过最好的表单验证库，并已从零重写了一版面向通用使用的版本。
  article_id: ef8a2deee4e7a86d
- object_type: project
  name: HTML-first Astro form site
  canonical_name: HTML-first Astro utility form
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者使用 Astro 构建了 HTML-first 的渐进增强表单网站，无需 JavaScript 即可完成整个申请流程。
  - 每个步骤在表单向导中是独立页面，用户点击下一步时提交数据，通过 API 验证后重定向到下一步。
  - 上线后次日完成表单的用户数翻倍，分析团队甚至无法追踪这些新增用户的来源。
  article_id: ef8a2deee4e7a86d
- object_type: project
  name: GOV.UK
  canonical_name: GOV.UK
  url: https://www.gov.uk
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章引用 Terence Eden 的见闻，描述用户在 PSP 游戏机浏览器上访问 GOV.UK 住房补助页面。
  - GOV.UK 页面使用简单 HTML 编写，轻量级且在糟糕的浏览器上也能正常工作，被作者视为设计标杆。
  article_id: ef8a2deee4e7a86d
impact_score:
  score: 3.5
  reason: 这是一篇高质量的工程案例分享，通过HTML优先架构和渐进增强策略成功解决了一个真实业务问题，用户完成量翻倍。但该事件属于Web开发领域最佳实践的再次验证，而非范式级突破。对于AI行业而言不构成直接影响，但对Web表单工程和前端架构选型有一定启发价值。评分3.5反映了它作为工程案例的扎实性，但影响力局限于特定技术社区。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: HTML优先架构和原生HTML验证的工程价值，以及不到1KB的Web组件实现的极简设计哲学
hype_assessment:
  level: low
  reason: 文章以第一人称工程案例形式呈现，提供了完整的技术决策脉络、架构选型理由和量化结果（用户翻倍），没有使用'颠覆''革命性'等PR包装词汇。标题虽然具有吸引力，但内容本身务实、数据支撑充分，属于实打实的工程经验分享。
information_entropy: high
domain_disruption:
  technical_innovation: 不到1KB的Validation-enhancer HTML Web组件实现了浏览器原生验证API的渐进增强封装，在极小体积内完成了表单验证UI现代化、错误提示可访问性处理和三级降级策略（Web组件→浏览器原生→后端验证），体现了极致的工程简约美学。但核心架构模式（HTML优先、渐进增强、表单步骤独立页面+后端重定向）是Web开发领域已确立的经典模式，非全新突破。
  business_model: 无。这是一个产品工程实现的技术案例，不涉及商业模式或SaaS生态的创新。
engineering_complexity: production_ready
compound_value:
  score: 3.0
  reason: 这是一篇社区案例分享，验证了HTML优先+渐进增强策略在特定场景（公用事业表单）下的有效性，用户完成量翻倍提供了有力的实证数据。但从VC视角看，该方法论不构成可投资的商业资产——validation-enhancer组件体量极小（<1KB）且偏工程模式，难以形成可扩展的商业模式或平台壁垒。该案例对技术社区有教育意义，但缺乏长期复利效应，难以支撑独立的投资逻辑。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Astro
competitive_casualty:
- React-heavy前端咨询公司
- 过度工程化的表单SaaS厂商
market_opportunities:
- 为公共服务和强监管行业（公用事业、金融、政务）提供HTML优先/渐进增强架构咨询，帮助这类组织避免重前端框架导致的用户流失和合规罚款风险
- 基于validation-enhancer Web组件模式，开发轻量级（<1KB）的浏览器原生表单验证增强工具库，可作为开源项目建立技术影响力并衍生企业级支持服务
- 面向发展中国家市场和低端设备用户群体的产品策略——采用HTML优先架构替代SPA方案，可显著扩大可触达用户基数并提升转化率
risk_matrix:
  regulatory: 无
  technological: 无
  competitive: 以React为代表的单页应用框架生态可能面临部分场景下被HTML优先架构替代的压力，但两者适用场景不同（复杂交互应用 vs 内容/表单型应用），直接竞争有限
  ethical: HTML优先和渐进增强策略显著提升数字包容性（老旧设备、弱网环境、辅助技术用户），对这一事件的采纳将改善而非恶化AI伦理和社会影响问题
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: validation-enhancer
  canonical_name: validation-enhancer
  url: null
  positioning: 一个依赖浏览器原生验证 API 的 HTML Web Component，体积不到 1KB，通过三层渐进增强策略为表单提供现代化的验证体验。
  technical_signal: 采用 Web Component 优先的三层渐进增强架构：组件优先渲染，加载失败回退到浏览器原生验证提示，后端 API 作为最终验证兜底。
  adoption_signal: 已应用于受监管垄断公用事业公司的生产环境表单，作者已从零重写面向通用使用的独立版本并公开发布。
  ecosystem_relevance: 以极轻量的方式解决了 Web 表单验证这一普适痛点，为社区提供了替代重型 React 验证库的无依赖方案。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 以不到 1KB 的体积实现了完整的表单验证渐进增强方案，展示了 Web Component 替代重型框架验证库的可行路径，对追求轻量化前端实践的团队具有参考价值。
  risk_notes:
  - 目前为单人维护项目，尚未验证广泛的社区采用和跨浏览器兼容性边界情况。
  score: 5.0
  article_ids:
  - ef8a2deee4e7a86d
  evidence_snippets:
  - 作者构建了一个名为 validation-enhancer 的 HTML Web Component，包装在表单外部并利用浏览器原生验证进行渐进增强。
  - 该组件不到 1KB，如果加载失败则回退到浏览器内置验证，后端 API 作为最终验证兜底。
  - 作者声称这是从业 20 多年来用过最好的表单验证库，并已从零重写了一版面向通用使用的版本。
- object_type: project
  name: HTML-first Astro form site
  canonical_name: HTML-first Astro utility form
  url: null
  positioning: 为受监管垄断公用事业公司构建的 HTML-first 多步骤表单网站，无需 JavaScript 即可完成完整申请流程，后端会话确保持久化。
  technical_signal: 每个表单步骤为独立页面，通过表单提交到后端 API 验证后重定向到下一步，采用经典 Web 表单模式而非客户端路由。
  adoption_signal: 上线后次日完成表单的用户数翻倍，分析工具甚至无法追踪新增用户来源，成功替代了上线 3 天即被撤回的 React 方案。
  ecosystem_relevance: 用真实业务数据验证了 HTML-first 渐进增强架构在公共服务场景中优于 SPA 方案，为行业技术选型提供了有力参考案例。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 这是一个用真实业务数据验证 HTML-first 架构优势的典型案例，上线次日完成表单用户翻倍，对公共服务网站技术选型具有重要参考价值。
  risk_notes:
  - 成功高度依赖业务场景（受监管垄断企业的公众服务表单），可能不适用于交互密集的实时数据应用类型。
  score: 7.0
  article_ids:
  - ef8a2deee4e7a86d
  evidence_snippets:
  - 作者使用 Astro 构建了 HTML-first 的渐进增强表单网站，无需 JavaScript 即可完成整个申请流程。
  - 每个步骤在表单向导中是独立页面，用户点击下一步时提交数据，通过 API 验证后重定向到下一步。
  - 上线后次日完成表单的用户数翻倍，分析团队甚至无法追踪这些新增用户的来源。
- object_type: project
  name: GOV.UK
  canonical_name: GOV.UK
  url: https://www.gov.uk
  positioning: 英国政府官方网站，采用简洁 HTML 构建，确保在包括老旧游戏机浏览器在内的所有设备上可正常访问和使用。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: 作为 HTML-first 和包容性设计的长期标杆，被开发者社区广泛引证为公共服务网站的可访问性标准。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该文章引用 GOV.UK 作为 HTML-first 设计的典范案例，其在老旧设备和弱网环境下的可用性表现为开发者社区提供包容性设计的重要参考。
  risk_notes:
  - 文章仅作为设计理念参考引用，未涉及 GOV.UK 自身的新动态或技术变更。
  score: 2.0
  article_ids:
  - ef8a2deee4e7a86d
  evidence_snippets:
  - 文章引用 Terence Eden 的见闻，描述用户在 PSP 游戏机浏览器上访问 GOV.UK 住房补助页面。
  - GOV.UK 页面使用简单 HTML 编写，轻量级且在糟糕的浏览器上也能正常工作，被作者视为设计标杆。
---

# How building an HTML-first site doubled our users overnight

This is a story of how building HTML-first doubled a company’s users literally overnight.

My client was a utility company, and they had a big problem. To apply for their services, customers could either use an old ASP form on the website, or follow a manual process. The manual process was more expensive for the company, of course. Adding a lot of pressure, this was a regulated monopoly, and if their customer satisfaction dropped below 96% (if I remember correctly) it could result in millions of pounds in fines.

There were two previous failed (and very expensive) attempts to solve the problem. In the most recent, contractors in another country had built a React app. The React app was online for 3 days before being pulled because of customer complaints. I took one look at it and told my boss “we can’t take ownership of this.” It was a mess of loading spinners and global javascript states. It was not accessible. Image upload was a vital part of the form, and it attempted to store images (along with all other form data) in localstorage which has a 5mb limit!

I took a very bold decision and built a new version of the site using Astro. It was HTML-first. Javascript existed, in web components, but only to progressively-enhance a website that worked perfectly fine without it.

My logic was thus:

- This is a public service
- It should work on every machine possible
- It should work when connections are poor
- The forms must never lose data once it is entered

I was very moved by this anecdote from Terence Eden:

A few years ago I was doing policy research in a housing benefits office in London. They are singularly unlovely places. The walls are brightened up with posters offering helpful services for people fleeing domestic violence. The security guards on the door are cautiously indifferent to anyone walking in. The air is filled with tense conversations between partners - drowned out by the noise of screaming kids.

In the middle, a young woman sits on a hard plastic chair. She is surrounded by canvas-bags containing her worldly possessions. She doesn’t look like she is in a great emotional place right now. Clutched in her hands is a games console - a PlayStation Portable. She stares at it intensely; blocking out the world with Candy Crush.

Or, at least, that’s what I thought.

Walking behind her, I glance at her console and recognise the screen she’s on. She’s connected to the complementary WiFi and is browsing the GOV.UK pages on Housing Benefit. She’s not slicing fruit; she’s arming herself with knowledge.

The PSP’s web browser is - charitably - pathetic. It is slow, frequently runs out of memory, and can only open 3 tabs at a time.

But the GOV.UK pages are written in simple HTML. They are designed to be lightweight and will work even on rubbish browsers. They have to. This is for everyone.


Some requirements I derived:

- Each session with the form should have a unique ID
- At every step in the form wizard, submitted data should be stored on the backend, including uploads
- It should be possible to complete the form without javascript
- It should be possible to complete the form on outdated and crap web browsers
- We had to meet WCAG accessibility (the team settled on AA rather than AAA)
- Javascript and modern CSS should be used to enhance the experience

The basic setup ended up being that each step in the form wizard was its own page. When the user clicked next, the form would submit. If the data was judged to be valid by the API, the browser would be redirected to the next step.

A venerable web application pattern that has had a small modern renaissance thanks to Remix, form submissions and redirects took a while to explain to my colleagues, on account of everyone being used to heavily client-side web applications. I have nothing against heavily client-side applications, in their place. But this is just a big form - it’s not showing real-time data. Our user could be standing in the middle of a field on a new-build housing estate, holding a decade-old commodity android phone they bought in Tesco. Shipping them 20MB of javascript before we even render a form would be a ridiculous thing to do.

Next, I tackled one of my biggest bugbears, form validation (and form and form error rendering). I have seen teams waste person-months of effort wrangling React validation libraries. If you are a React person, you might be scoffing at this - skill issue, I guess - but it is the reality for many teams. I would like to humbly suggest that you too may be spending more time than you realise, and a lot more time than is necessary, interacting with and maintaining poor imitations of the validation system that ships with every browser.

So I built an HTML web component. These are simple custom elements that wrap around existing HTML and bring it to life. No shadow DOM, no (or little) rendering HTML in javascript. Mine wrapped around any HTML form, picked up the HTML validation, and made it look modern. It would prevent those HTML validation popup tooltips, and instead place the error in the aria-describedby element associated with the field (today, aria-errormessage is advised instead). It would clear validation while you typed, if you reached a valid state, and assess it again on blur and submit.

Exactly the user experience a form needs, delivered in under 1KB. If it failed, the form would fall back to built-in browser validation. If that failed, the backend API would handle validation. We reported validation issues to the user as early as possible given their browser, and always fell back to an acceptable experience if it failed.

I have since written a new version of this web component from scratch, aimed for general use. It’s called validation-enhancer. I have been in this industry for over 20 years, and it is the best form validation library I have ever used. I am very proud of it.

The code is so simple to work with:

```
<validation-enhancer>
<form>
<label for="my-email">Email</label>
<input type="email" name="my-email" aria-errormessage="my-email-error" required />
<div id="my-email-error"></div>
<button type="submit">Submit</button>
</form>
</validation-enhancer>
```


The results? When we launched, the number of people completing the form doubled. The analytics people didn’t even know where these users were coming from. Of course, your javascript-based analytics package doesn’t see the users you are bouncing because of javascript failures. It was a flood! We also saw my “keep a backend session, never lose user data” approach pay off. In one case, someone completed a form a month after starting it.

There was a sad coda; as is the way of contract work, I moved on. I explained what I had built to my replacement, that it always worked even without javascript. He was appalled and said, “but that’s a lot more work for us.”

It is not acceptable to bounce users on old browsers, users with bad network connections, users using assistive technologies. Certainly not from a monopoly public service. A lot of hype and noise is pressing us to extend the cowboy, wild-west phase of the software industry’s expansion. We should set that aside, and take ourselves seriously as a mature industry. Build a web application that works on a playstation portable on a 3G connection - if you do, it will work for all your users, and it will still work 30 years from now.