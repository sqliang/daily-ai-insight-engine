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