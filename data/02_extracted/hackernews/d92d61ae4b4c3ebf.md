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
tldr: UHF X11 是一款专为 visionOS 和 Apple Vision Pro 打造的现代 X11 显示服务器，支持根窗口空间化窗口、原生 X11
  TCP 连接、CRT 扫描线特效以及 GLX 渲染。
objective_summary: UHF X11 将 Apple Vision Pro 转变为完整的 X11 显示服务器。每个 X11 顶级窗口作为独立的 visionOS
  空间窗口打开，用户可将其放置在空间任意位置。应用支持来自可信机器的原生 X11 TCP 连接、X authority cookie 认证、CRT 扫描线和辉光等经典显示预设，以及
  OpenGL 客户端的 GLX 渲染。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Apple
  technologies:
  - X11
  - GLX
  - OpenGL
  - visionOS
  key_people: []
key_logic_flow:
- UHF X11 是一款为 visionOS 和 Apple Vision Pro 打造的 X11 显示服务器。
- 每个 X11 顶级窗口会作为独立的 visionOS 空间窗口打开，用户可随意放置在空间中。
- 应用支持从可信机器通过原生 X11 TCP 协议发送 X11 调用到 visionOS 空间窗口中。
- X 帧缓冲区内容以原生分辨率呈现，小表面使用最近邻缩放，并支持 CRT 扫描线等经典显示预设。
- X authority cookie 在设备上生成并复制到客户端机器以完成认证连接。
- OpenGL 客户端可通过 GLX 在 X11 上进行 3D 渲染，兼容性因环境而异。
extract_result: success
object_mentions:
- object_type: product
  name: UHF X11
  canonical_name: UHF X11
  url: https://www.lispm.net/apps/uhf-x11/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - UHF X11 是一款专为 visionOS 和 Apple Vision Pro 打造的现代 X11 显示服务器。
  - UHF X11 将 Apple Vision Pro 转变为一个完整的 X11 显示服务器，每个 X11 顶级窗口作为独立的 visionOS 空间窗口打开。
  - 应用支持原生 X11 TCP 连接、X authority cookie 认证以及 CRT 扫描线等经典显示预设。
  article_id: d92d61ae4b4c3ebf
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