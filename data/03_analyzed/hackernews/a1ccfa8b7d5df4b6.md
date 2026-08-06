---
title: We finally learned to center a div, then browsers added sidebars
source: https://seg6.space/posts/center-div/
author:
- '[[seg6]]'
published: '2026-08-04'
created: '2026-08-05'
manifest_dates:
- '2026-08-05'
description: 'Article URL: https://seg6.space/posts/center-div/ Comments URL: https://news.ycombinator.com/item?id=49176055
  Points: 131 # Comments: 105'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a1ccfa8b7d5df4b6
source_type: community_discussion
tldr: 作者在个人技术博客记录了一个前端居中问题：浏览器侧边栏开启时，CSS grid 的 place-items 会把内容居中在缩小后的 webview 里而非整个窗口正中。他利用
  window.outerWidth 与可信 pointer 事件计算出偏移，并发布浏览器扩展 center, actually 供用户手动选择居中元素。
objective_summary: 作者在 seg6.space 的博客中记录一个前端居中问题：浏览器侧边栏开启时，CSS grid 的 place-items
  居中基于被压缩的 webview 矩形而非整个窗口，内容偏离窗口真正的中心。他先用 window.outerWidth 与 window.innerWidth
  之差估算浏览器 UI 宽度，并用 CSS translate 对居中容器做位移修正，但 DevTools 停靠右侧后无法得知差值如何分配。随后他借助可信 pointer
  事件的 screenX 与 clientX 之差定位 webview 在窗口内的位置，得出正确的位移量。最终他发布浏览器扩展 center, actually，自动识别或让用户手动选择居中元素，以
  opt-in 方式应用修正。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - CSS Grid
  - place-items
  - CSS translate
  - Pointer Events
  - Firefox
  - Chromium
  key_people: []
key_logic_flow:
- 'CSS 的 grid 布局配合 place-items: center 可以轻松实现 div 水平垂直居中，作者最初用这种方式对站点主容器进行居中。'
- 当浏览器侧边栏可见时，居中是相对于被压缩的 webview 矩形而非整个浏览器窗口，导致内容偏离窗口真正的中心。
- 作者先通过 window.outerWidth 与 window.innerWidth 的差值计算浏览器 UI 宽度，再用 CSS translate 对居中容器施加负半宽位移进行修正。
- DevTools 停靠在窗口右侧时，宽度差混入了两侧的浏览器 UI，无法判断差值如何分配，简单的修正因此失效。
- 作者改用可信 pointer 事件，利用 event.screenX 与 event.clientX 的差值定位 webview 在窗口内的确切位置，从而算出正确的位移量。
- Firefox 直接暴露视口位置，Chromium 不提供该信息，因此扩展先按用户选择的侧边栏位置初始化，等指针进入页面后再修正。
object_mentions:
- object_type: product
  name: center, actually
  canonical_name: center, actually
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者制作了名为 center, actually 的浏览器扩展，它试图自动识别页面中居中的元素，如果猜错就允许用户手动指定一个。
  - 该扩展以 opt-in 方式将居中修正的决定权交给用户，而不是由网站替所有人选择，官方演示页是最直观的对比场景。
  article_id: a1ccfa8b7d5df4b6
extract_result: success
impact_score:
  score: 1.5
  reason: 这是一篇个人技术博客，讨论的是浏览器侧边栏开启时 CSS grid 居中偏移这一非常细分的 UX 问题。事件本身不涉及任何公司、融资或主流框架更新，也未改变局部竞争格局，属于典型的'小圈子自嗨'范畴。其核心价值仅在于一个巧妙的工程小技巧（用可信
    pointer 事件定位 webview 偏移），对行业范式没有任何影响，故评分落在 1-3 分区间。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 利用可信 pointer 事件的 screenX 与 clientX 差值在 Chromium 中反推 webview 视口位置这一非显而易见的工作区技巧
hype_assessment:
  level: low
  reason: 全文没有出现任何'颠覆''革命'等 PR 滥用词汇，作者以第一人称记录了从发现问题、尝试 outerWidth 差值法、到 DevTools 场景失效、最终用
    pointer 事件坐标定位的完整推导过程，并诚实说明了各方案的局限（Firefox 直接暴露视口位置而 Chromium 不支持）。这是实打实的技术经验分享，没有任何商业包装或概念炒作，判定为干货。
information_entropy: medium
domain_disruption:
  technical_innovation: 提出了一个非显而易见的工程解法：在 Chromium 不暴露视口在窗口内位置的前提下，借助可信 pointer 事件的
    screenX 与 clientX 差值（结合缩放比例 scale）精确反推出 webview 相对浏览器窗口的偏移量，从而对 CSS grid 居中容器施加正确的
    translate 位移。该技巧对处理'浏览器 UI 侵占视口'类布局问题的开发者有直接借鉴价值，但它只是局部修补手段，并非平台级能力创新。
  business_model: 无。本文不涉及商业模式或 SaaS 生态，唯一产物是一个 opt-in 理念的浏览器扩展（center, actually），其分发与变现意义可忽略，对行业生态无重塑力。
engineering_complexity: prototype
compound_value:
  score: 1.5
  reason: 从投资逻辑逐层拆解：第一，目标市场规模趋近于零——受众是'同时使用浏览器侧边栏、又在意像素级绝对居中、还愿意手动安装扩展'的极窄开发者子集，且该问题不涉及生产力损失或商业成本，付费意愿几乎不存在。第二，无任何复利机制——该方案是纯客户端
    CSS/JS 修正，不产生数据积累、网络效应或平台锁定，无法沿着'细分赛道基础设施'路径积累长期价值，3-5 年后不会成为行业基石。第三，替代风险高且不可防御——这是对浏览器平台层缺陷的临时补丁，一旦
    Chromium/Firefox 原生暴露视口偏移信息或直接修复居中坐标，扩展即被官方能力一键替代；同时分发完全依赖浏览器商店政策，无法形成独立商业壁垒。第四，无资本事件支撑——作者未成立公司、无融资、无商业模式，属于个人技术博客作品而非商业标的。综合判定为'昙花一现'区间。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries:
- Mozilla Firefox
competitive_casualty: []
market_opportunities:
- 前端工程团队可将作者'窗口真实居中'的偏移测量方案（screenX/clientX 差值定位 webview）封装为通用工具库，服务需要精确对齐浏览器窗口的桌面级
  Web 应用，如截图工具、远程控制面板与设计协作产品
- 浏览器型 AI Agent 工具链厂商可将视口几何测量能力纳入自动化层，提升代理在真实浏览器环境中执行点击、截图与元素定位时的空间精度，作为差异化能力沉淀
- '''center, actually'' 采用的 opt-in 用户偏好覆盖模式，可启发面向用户体验定制的小众扩展赛道（如个性化排版、可访问性微调），以轻量订阅或企业授权形式变现'
risk_matrix:
  regulatory: 无。该扩展为 opt-in 且本地处理指针坐标，不涉及数据收集或跨境传输；但若后续申请过宽权限（如读取所有页面的指针事件），可能面临浏览器商店审核与
    GDPR/隐私合规审查
  technological: 修正方案依赖 window.outerWidth、screenX 等非标准浏览器行为，Firefox 与 Chromium 行为不一致；若
    Chromium 未来新增视口位置 API 或平台层原生支持'相对窗口居中'，该 workaround 将失效或需重构
  competitive: 浏览器厂商可能在平台层原生实现该能力，使扩展价值归零；同时开发者工具类扩展同质化严重，细分市场极小、付费意愿与变现空间有限
  ethical: 扩展通过可信 pointer 事件获取屏幕坐标，理论上存在隐私敏感信息暴露风险；但当前 opt-in 模式与本地处理基本规避了该问题，整体伦理风险较低
  additional:
  - 跨浏览器兼容性维护成本高（Firefox 直接暴露视口位置而 Chromium 不提供），且依赖未文档化的私有行为，浏览器版本更新可能导致静默失效
confidence:
  impact: high
  compound: low
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: center, actually
  canonical_name: center, actually
  url: null
  positioning: 一款解决浏览器侧边栏下居中参考系偏移问题的 opt-in 浏览器扩展，自动识别居中元素，识别错误时允许用户手动指定并施加窗口级修正。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 浏览器侧边栏常开的开发者与重度用户
  - 对页面居中位置精确性敏感的前端工程师
  - 使用 DevTools 多面板布局布局的技术工作者
  product_signal: 扩展能自动识别页面中的居中元素，识别出错时允许用户手动指定，并以 opt-in 方式把居中修正的决定权交给用户而非网站替所有人选择。
  market_signal: 该需求源于浏览器侧边栏与 DevTools 的常见使用组合，属于小众人群的精确居中痛点，目前未见同类商业化产品或大范围推广迹象。
  differentiation: 与依赖 CSS 布局容器的常规居中方案不同，扩展借助可信 pointer 事件的 screenX 与 clientX 之差推算
    webview 在窗口中的实际位置，实现窗口级精确居中。
  watch_reason: 该扩展针对一个真实存在却常被忽略的前端布局问题：浏览器侧边栏开启时，CSS 居中参考系会从整窗退化为被压缩的 webview。其借助可信
    pointer 事件定位视口位置的技术思路颇具巧思，对多栏浏览器布局下的页面适配有参考价值，值得跟踪其后续采用与迭代。
  risk_notes:
  - 扩展依赖可信 pointer 事件推算视口位置，若浏览器收紧相关 API 或权限，定位逻辑可能失效。
  - Chromium 不直接暴露视口位置，扩展需先按侧边栏位置初始化，指针进入页面前修正可能不精确。
  - 该工具定位小众人群的具体痛点，使用门槛偏高，长期维护与浏览器兼容性跟进存在不确定性。
  score: 3.0
  article_ids:
  - a1ccfa8b7d5df4b6
  evidence_snippets:
  - 作者制作了名为 center, actually 的浏览器扩展，它试图自动识别页面中居中的元素，如果猜错就允许用户手动指定一个。
  - 该扩展以 opt-in 方式将居中修正的决定权交给用户，而不是由网站替所有人选择，官方演示页是最直观的对比场景。
---

Centering a div used to require this little ritual:

```
.thing {
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
}
```


These days, it is almost disappointingly easy:

```
body {
display: grid;
min-height: 100dvh;
place-items: center;
}
```


I used that for the `.site`

div you’re reading. It looked centered until I opened it in a browser with the sidebar visible.

This is a fairly specific itch. I use one browser window tiled directly in front of me, usually with its sidebar open. When a site deliberately centers a narrow layout, I want it at the dead center of that window, not the space left over beside the sidebar.

The `.site`

div was still perfectly centered, just inside the wrong rectangle. I figured the fix would be simple enough: JavaScript knows the width of both the webview and the browser window.

```
window.innerWidth // the webview
window.outerWidth // the whole browser window
const browserChrome = window.outerWidth - window.innerWidth;
```


With the sidebar on the left, I could move `.site`

back by half of that difference:

`const shift = -browserChrome / 2;`


```
.site {
translate: var(--window-center-shift, 0px);
}
```


The sidebar still narrows the webview and the page still reflows normally. This only repositions the container that was already centered. If there is not enough visible space for it, the correction should stop rather than hide content.

That worked, right up until I opened DevTools.

# devtools ruins the easy fix

Mine is docked on the right, so the width difference now included browser UI on both sides. It gave me the total, but no way to tell how that total was split.

What finally gave me the missing coordinate was the pointer. A trusted pointer event knows where it is on the screen and where it is inside the webview, which is enough to locate the webview inside the window:

```
const viewportLeft = event.screenX - event.clientX * scale;
const viewportRight = viewportLeft + innerWidth * scale;
const left = viewportLeft - window.screenX;
const right = window.screenX + outerWidth - viewportRight;
const shift = (right - left) / (2 * scale);
```


Firefox exposes the same viewport position directly. Chromium does not, so the extension starts with the selected sidebar position and corrects it as soon as the pointer enters the page.

# center, actually

I wanted to try the same fix on pages I do not control, so I made **center, actually**. It tries to find the centered element itself; if it guesses wrong, you can pick one. This is where the preference belongs: opt-in, rather than chosen by a site for everyone. The demo is the simplest place to see the difference.