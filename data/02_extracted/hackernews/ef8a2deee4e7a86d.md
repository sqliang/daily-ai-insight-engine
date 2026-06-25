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
tldr: 为公用事业公司构建HTML优先网站，用户量一夜翻倍
objective_summary: 作者为一家公用事业公司用Astro框架构建了HTML优先的表单网站，替代了此前失败的React实现。采用渐进增强策略，每个表单步骤独立提交到后端，并构建了不到1KB的HTML验证Web组件。上线后用户完成量翻倍，分析工具无法追踪新增用户来源。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - Astro
  - React
  - Web Components
  - HTML
  - ASP
  key_people:
  - Moh Kohn
  - Terence Eden
key_logic_flow:
- 一家公用事业公司面临客户满意度低于96%将面临数百万英镑罚款的压力，此前两次用React构建在线申请表均因用户投诉而失败。
- 作者选择Astro构建HTML优先架构，JavaScript仅通过Web组件实现渐进增强，确保表单在不支持JS的环境下仍可正常使用。
- 每个表单步骤为独立页面，用户点击下一步时提交数据到后端验证，验证通过后重定向到下一步，杜绝前端LocalStorage存储的5MB限制问题。
- 作者构建了不到1KB的validation-enhancer HTML Web组件，利用浏览器原生HTML验证API提供现代化UI，失败时优雅降级到浏览器内置验证或后端验证。
- 上线后表单完成用户量一夜翻倍，JS分析工具无法识别这些来自JS失败用户的流量来源。
- 后端会话机制确保用户数据永不丢失，有用户在一个月后继续完成之前开始的表单提交。
extract_result: success
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