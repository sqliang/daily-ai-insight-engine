---
title: Developers don't understand CORS (2019)
source: https://fosterelli.co/developers-dont-understand-cors
author:
- '[[toilet]]'
published: '2026-06-21'
created: '2026-06-21'
description: 'Article URL: https://fosterelli.co/developers-dont-understand-cors Comments
  URL: https://news.ycombinator.com/item?id=48614844 Points: 188 # Comments: 95'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7fdc72df421fcac2
source_type: community_discussion
tldr: 文章指出许多开发者不理解CORS，以Zoom本地服务器绕过CORS导致安全漏洞为例说明问题。
objective_summary: 2019年，安全研究员Jonathan Leitschuh发现Zoom在本地端口19421运行web服务器，通过图片尺寸编码数据绕过CORS。作者认为Zoom因不理解CORS而采用不安全方案，导致任意网站均可调用本地特权接口。正确做法应设置Access-Control-Allow-Origin头限制
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies:
  - Zoom
  technologies:
  - CORS
  - CSP
  - XHR
  - AJAX
  key_people:
  - Jonathan Leitschuh
key_logic_flow:
- 作者指出许多web开发者不理解CORS的工作原理，导致在实际开发中绕过而非正确实现跨域安全策略。
- Zoom在本地运行web服务器监听端口19421，但使用图片尺寸编码响应数据的方式绕过CORS，而非设置Access-Control-Allow-Origin头。
- 由于未限制来源，Zoom本地web服务器暴露的特权功能（如安装软件）可被互联网上任意网站调用，构成严重安全漏洞。
- '正确的安全实现应为本地服务器设置Access-Control-Allow-Origin: https://zoom.us，并配合Content Security
  Policy阻止iframe嵌套。'
- Stack Overflow上大量CORS相关问题中，许多推荐的不安全默认配置（如express的*通配符）加剧了安全隐患。
- 作者认为CORS API过于复杂且开发者教育不足是导致普遍误解的主要原因。
impact_score:
  score: 3.5
  reason: 该文章是一篇技术评论/教育类文章，以2019年Zoom安全漏洞为案例，指出Web开发者对CORS的普遍误解。Zoom漏洞本身在当时有一定行业影响（影响数十万用户），但文章本身并未提出新技术或范式转移。其核心价值在于警示开发者不要绕过安全机制，属于持续性的安全教育内容，而非改变行业格局的事件。评分较低因为：(1)文章发表于2019年，观点已被广泛讨论；(2)未引入新理论或实践；(3)影响范围局限于Web安全领域内的开发者认知层面。
sentiment: neutral
developer_sentiment:
  tone: frustrated
  primary_focus: CORS机制过于复杂且开发者教育不足，导致普遍采取不安全的绕过方案
hype_assessment:
  level: low
  reason: 文章没有使用'颠覆性''革命性'等PR包装词汇，而是基于具体漏洞案例（Zoom本地服务器绕过CORS）进行事实性技术分析和批评。文章逻辑清晰，引用了安全研究员Jonathan
    Leitschuh的实际发现，并给出了可操作的正确实现建议（设置Access-Control-Allow-Origin头+CSP策略），属于实打实的技术批评文。
information_entropy: medium
domain_disruption:
  technical_innovation: 无（文章分析了现有CORS机制被绕过的原因，未提出新技术架构或工程突破）
  business_model: 无（纯技术安全讨论，不涉及商业模式影响）
engineering_complexity: conceptual
compound_value:
  score: 2.0
  reason: 该文章是2019年发布的一篇CORS技术与安全意识科普文，以Zoom本地服务器绕过CORS导致安全漏洞为例，揭示开发者对跨域安全策略的普遍误解。从VC视角评估：它不描述任何新技术突破、新商业模式或新市场需求，而是对已有web安全标准的反思性讨论。CORS作为浏览器安全模型的核心机制已存在十余年，该文章讨论的问题本质上是开发者教育与API设计复杂度之间的张力，并未指向任何可资本化的增量机会。文章本身不具备产生长期复利效应的基础——它既不定义新赛道，也不创造新资产或网络效应，更不推动供需结构变化。唯一可能的间接价值在于强化了'开发者安全工具'赛道的需求逻辑，但这一逻辑早已被市场充分定价，没有增量信息。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries:
- 浏览器厂商（Chrome、Safari、Firefox）
- 网络安全教育/培训平台
- Web安全测试工具
competitive_casualty:
- Zoom（声誉受损，暴露安全架构缺陷）
- 安全意识薄弱的桌面应用厂商
market_opportunities:
- 开发者可围绕 CORS/CSP 安全配置开发自动化审计工具，集成到 CI/CD 流水线中，帮助团队在开发阶段发现跨域安全漏洞
- 面向全栈开发者的 Web 安全培训课程存在持续需求，特别是针对 CORS、CSP、Same-Origin Policy 等基础但易误用的安全机制进行实战教学
- 本地进程间通信的安全性标准化方案存在市场空白，可开发封装了正确 CORS 配置的本地 Web 服务器 SDK 或工具库
risk_matrix:
  regulatory: GDPR 等隐私法规下，因 CORS 配置不当导致用户数据泄露可能面临高额罚款；Zoom 事件后监管机构对本地服务器暴露特权接口持更严格的审查态度
  technological: Modern frameworks（如 Next.js、Vite）虽改进了 CORS 默认配置，但开发者仍可能在自定义后端或内嵌
    WebSocket 时引入相同漏洞；2019 年至今 CORS API 本身未发生根本简化，认知门槛依旧存在
  competitive: 无
  ethical: CORS 绕过导致任意网站可调用本地特权接口（如安装软件、开启摄像头/麦克风），直接侵犯用户隐私与设备安全；错误的 CORS 实现使得用户对浏览器安全模型的信任被瓦解
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
---

### Developers don't understand CORS

One of the best things about working in full stack consulting is that I get to work with a great number of developers with different skill levels in companies from various sizes and industries. This provides an opportunity to see what universal struggles come up. One that seems common and relevant recently is this: Too many web developers do not understand how CORS works.

This seems particularly timely to point out because of the recent Zoom vulnerability. Security researcher Jonathan Leitschuh found Zoom has a web server listening on the machine at `http://localhost:19421`

. When you load a Zoom link, Zoom’s website sends a request to the localhost webserver and tells it to open up the native Zoom app. The whole article is worth a read, but these parts stuck out to me:

I also found that, instead of making a regular AJAX request, this page instead loads an image from the Zoom web server that is locally running. The different dimensions of the image dictate the error/status code of the server. You can see that case-switch logic here.

One question I asked is, why is this web server returning this data encoded in the dimensions of an image file? The reason is, it’s done to bypass Cross-Origin Resource Sharing (CORS). For very intentional reasons, the browser explicitly ignores any CORS policy for servers running on localhost.


That last sentence is incorrect – Chrome does respect CORS headers for localhost webservers. If you’re a web developer you’ve probably done this when you have Create React App with your frontend app on one port and your backend API on another port. Your app is making cross origin requests against localhost, and this is supported in all browsers.

What this says to me is that Zoom may have needed to get this feature out and did not understand CORS. They couldn’t make the AJAX requests without the browser disallowing the attempt. Instead, they built this image hack to work *around* CORS. By doing this, they opened Zoom up to a big vulnerability because not only can the Zoom website trigger operations in the native client and access the response, but every other website on the internet can too.

So what would a secure implementation of this feature look like? The webserver listening in on `localhost:19421`

should implement a REST API and set a `Access-Control-Allow-Origin`

header with the value `https://zoom.us`

. This will ensure that only Javascript running on the zoom.us domain can talk to the localhost webserver. Further, to stop pages being able to open Zoom meetings automatically in the background zoom.us should have a Content Security Policy header that blocks rendering within an iframe.

This still leaves the vulnerability that any page can redirect your browser to a zoom.us link for a meeting that you didn’t expect, but this is a user experience decision that Zoom has made rather than a software vulnerability. Personally, I think the approach is wrong here too. They mention they desired a better user experience by opening the application directly, but one of the rules of good user experience design is that your software must be predictable.

If I am clicking a link, I expect that it will not suddenly make my camera and microphone available to people I do not know. Zoom is breaking this expectation. Even if they don’t want the built-in browser popup for UX reasons, put this popup in-app! Google Meet does this well:

I don’t want to take away from the CORS focus of this post. Regardless of the user experience side of the argument, running a webserver on localhost is a risky endeavour to begin with. It should absolutely not be providing privileged access to functions, such as *installing software*, to every website on the internet. CORS enables you to securely do this – don’t hack around it!

I can’t know for sure if failure to understand CORS is why Zoom implemented the feature this way. However, I’ve talked to a few people and none of us can collectively find any legitimate reason to implement their existing approach. On reddit, lerunicorn did find and suggest that Firefox may block XHRs from secure to non-secure origins which could explain the motivation behind this approach. However, Firefox supports this when the origin is localhost. Further, native apps can generate a unique self-signed certificate. Alternatively, they could have used a browser extension. In any possible case, this is not a valid reason to forget to filter origins.

It’s not just Zoom. Anecdotally, lots of developers I’ve talked with don’t understand well how CORS works. There’s also very a generous quantity of examples from questions on Stack Overflow. Unfortunately, these are often paired with pages that recommend very insecure defaults like this one in express which would make your application vulnerable if copied verbatim. Other vendors have been caught with the exact same vulnerability found in Zoom.

Developers just want to get their code to work, and bypassing the same-origin policy entirely might get it to work, but when someone finds out what you’ve done you’ll get problems like Zoom has now.

I’ve seen CORS confusion from both experienced and new developers. Is the CORS API too complex and confusing, or do we only need better developer education around issues like CORS and CSP? I’m not sure, but the current approach definitely doesn’t seem like it’s working.