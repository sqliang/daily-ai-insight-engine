---
title: Orca (GitHub Repo)
source: https://github.com/stablyai/orca?utm_source=tldrai
author: []
published: ''
created: '2026-06-26'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aae751d1d8aace5f
source_type: news_media
tldr: Orca 是一个开源 AI 编排器，可并行运行多个 CLI 代码代理（Claude Code、Codex 等）并统一管理。
objective_summary: stablyai 发布了 Orca，一款 MIT 协议的开源 AI 编排桌面工具，支持在独立工作树中并行运行 Codex、Claude
  Code、OpenCode 等多种 CLI 代理，提供跨工作树搜索、账户切换用量追踪、富文件预览和 Computer Use 等功能，并配有
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - stablyai
  technologies:
  - Computer Use
  key_people: []
key_logic_flow:
- Orca 允许用户在独立工作树中并行运行 Codex、Claude Code、OpenCode、Pi 等多种 CLI 代理，并在一个统一界面中追踪所有代理。
- 内置跨工作树快速搜索功能，支持搜索文件、代理、命令和仓库上下文。
- 支持账户切换和 Claude/Codex 用量追踪，可查看使用情况和速率限制重置时间。
- 提供 Markdown、图片、PDF 和仓库文档的富预览功能，以及让代理操控桌面应用的 Computer Use 功能。
- 支持通知推送和未读状态标记，并提供 iOS/Android 移动端配套应用用于远程监控代理。
- Orca 采用 MIT 开源协议，可通过 Homebrew 或 GitHub Releases 获取 macOS、Windows、Linux 各平台构建版本。
extract_result: success
---

Español · Português · 中文 · 日本語 · 한국어

**The AI Orchestrator for 100x builders.**

Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place.

**Also in the box:**

**Quick open**— Search across worktrees, files, agents, commands, and repo context without leaving your flow.**Account switcher & usage tracking**— See Claude and Codex usage and rate-limit resets, and hot-swap accounts without re-logging in.**Rich repo previews**— Preview Markdown, images, PDFs, and repo docs in the workspace.**Computer Use**— Let agents operate desktop apps and visible UI when a workflow needs real interaction.**Notifications and unread state**— Know when an agent finishes or needs attention, then mark threads unread to come back later.**And many, many more**— we ship daily, so this list is perpetually behind. The changelog is the real feature list.

Works with **any CLI agent** — if it runs in a terminal, it runs in Orca.

` Claude Code`
` Codex`
` Grok`
` Cursor`
` GitHub Copilot`
` OpenCode`
` MiMo Code`
` Amp`
` OpenClaude`
` Antigravity`
` Pi`
` oh-my-pi`
` Hermes Agent`
` Devin`
` Goose`
` Auggie`
` Autohand Code`
` Charm`
` Cline`
` Codebuff`
` Command Code`
` Continue`
` Droid`
` Kilocode`
` Kimi`
` Kiro`
` Mistral Vibe`
` Qwen Code`
` Rovo Dev`
`+ any CLI agent`

**Download from onOrca.dev**- Or grab a build directly: macOS Apple Silicon · macOS Intel · Windows (.exe) · Linux AppImage · All builds
- Running
`orca serve`

on a headless Linux server? See the headless Linux server guide.

*Or via a package manager:*

```
# macOS (Homebrew)
brew install --cask stablyai/orca/orca
# Arch Linux (AUR) — or stably-orca-git to build from source
yay -S stably-orca-bin
```

Pair with your desktop app to monitor and steer your agents from your phone.

**iOS:**Download on the App Store or join TestFlight**Android:**Download APK 0.0.27

-
**Discord:**Join the community on**Discord**. -
**Twitter / X:**Follow**@orca_build**for updates and announcements. -
**WeChat:**Scan the QR code to join the community. If the first group is full, use the backup group. -
**Feedback & Ideas:**We ship fast. Missing something? Request a new feature. -
**Privacy:**See the privacy & telemetry docs for what anonymous usage data Orca collects and how to opt out. -
**Show Support:**Star this repo to follow along with our daily ships.

Want to contribute or run locally? See our CONTRIBUTING.md guide.

Orca is free and open source under the MIT License.