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
pipeline_stage: ingested
id: a1ccfa8b7d5df4b6
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