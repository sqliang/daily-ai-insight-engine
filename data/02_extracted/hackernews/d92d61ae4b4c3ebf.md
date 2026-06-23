---
title: 'UHF X11: X11 Built for VisionOS and Apple Vision Pro'
source: https://www.lispm.net/apps/uhf-x11/
author:
- '[[zdw]]'
published: '2026-06-20'
created: '2026-06-21'
description: 'Article URL: https://www.lispm.net/apps/uhf-x11/ Comments URL: https://news.ycombinator.com/item?id=48610853
  Points: 203 # Comments: 38'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d92d61ae4b4c3ebf
source_type: community_discussion
tldr: UHF X11 将 Apple Vision Pro 变为原生 X11 显示服务器，X11 窗口以 visionOS 空间窗口形式呈现。
objective_summary: UHF X11 是一款专为 visionOS 和 Apple Vision Pro 构建的 X11 显示服务器。它将每个 X11
  顶级窗口渲染为独立的 visionOS 空间窗口，支持用户自由放置。该应用通过标准 X11 TCP 接受来自可信机器的连接，使用 X authority cookie
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Apple
  technologies:
  - X11
  - visionOS
  - GLX
  - OpenGL
  key_people: []
key_logic_flow:
- UHF X11 是一款专为 visionOS 和 Apple Vision Pro 构建的现代 X11 显示服务器。
- 每个 X11 顶级窗口会作为独立的 visionOS 空间窗口打开，用户可将其放置在空间中的任意位置。
- 应用支持通过标准 X11 TCP 协议接受来自可信机器的远程连接，并使用 X authority cookie 进行设备端生成的身份认证。
- X 帧缓冲区内容以原生分辨率呈现，小尺寸表面采用最近邻缩放算法。
- 内置 CRT 扫描线、荧光粉遮罩、辉光和暗角等复古显示器外观预设。
- 支持 GLX 渲染，允许 OpenGL 客户端通过 X11 进行 3D 渲染，但兼容性因具体环境而异。
---

### Rootless Spatial Windows

Each X11 top-level opens as its own visionOS window. Position them anywhere in your space.

L:>PROJECTS>CONFIDENTIAL>SPATIAL-UNIX>*.*.*

X11 built for visionOS and Apple Vision Pro.

A modern X11 built for basking in the past. Send your favorite Xlib clients to spatial windows, and live out the future you were promised.

UHF X11 turns Apple Vision Pro into a full X11 display server.

Attach X clients and vintage machines to send X11 calls into native, pixel-pretty spatial windows in visionOS.

Each X11 top-level opens as its own visionOS window. Position them anywhere in your space.

Accept connections from trusted machines over standard, native X11 TCP.

X framebuffer content is presented at native resolution with nearest-neighbor scaling for small surfaces.

CRT scanlines, phosphor masks, glow, and vignette presets for classic display character.

X authority cookies are generated on device and copied to client machines for authenticated connections.

3D in 2D in 3D. OpenGL clients can use GLX rendering over X11. Compatibility varies, as it did in the 2000s.

Import bitmap font directories from visionOS folders. Core X11 fonts ship with the app.