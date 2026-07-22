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
tldr: Orca 是一个开源的 AI 编排桌面工具，由 Stably AI 开发并托管在 GitHub 上，支持在同一界面中并排运行 Claude Code、Codex、OpenCode、Pi
  等多种 CLI 智能体，每个智能体拥有独立工作目录，并提供搜索、账户切换、用量追踪等配套功能。
objective_summary: Stably AI 于 GitHub 上发布了 Orca 项目，这是一款 AI 编排桌面应用，能够同时管理多个 CLI 智能体并追踪其在独立工作目录中的运行状态。Orca
  支持超过 20 种主流 AI 编码代理，提供快速搜索、账户热切换、用量监控、富仓库预览、计算机使用（Computer Use）以及通知功能，并附带 iOS 和
  Android 移动端配套应用。该项目以 MIT 许可证开源发布，可通过官网、Homebrew、AUR 等方式获取。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Stably AI
  technologies: []
  key_people: []
key_logic_flow:
- Orca 是一个 AI 编排器，允许用户并排运行 Claude Code、Codex、OpenCode、Pi 等多种 CLI 智能体，每个智能体拥有独立的工作目录。
- Orca 提供快速搜索功能，用户可在工作目录、文件、智能体、命令和仓库上下文之间跨域搜索，无需离开当前流程。
- Orca 支持账户切换和用量追踪，可查看 Claude 和 Codex 的使用情况与速率限制重置时间，并支持热切换账户。
- Orca 提供计算机使用（Computer Use）功能，允许智能体在需要真实交互时操作桌面应用和可见 UI。
- Orca 兼容任何 CLI 智能体，只要能在终端中运行的工具都可以接入 Orca 平台。
- Orca 以 MIT 许可证在 GitHub 上开源发布，由 Stably AI 维护，提供 macOS、Windows、Linux 桌面端以及 iOS、Android
  移动端应用。
extract_result: success
object_mentions:
- object_type: project
  name: stablyai/orca
  canonical_name: stablyai/orca
  url: https://github.com/stablyai/orca
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Orca 是一个 AI 编排工具，允许用户在同一界面中并排运行多个 CLI 智能体（如 Claude Code、Codex、OpenCode、Pi 等），每个智能体拥有独立的工作目录。
  - Orca 以 MIT 许可证在 GitHub 上开源发布，由 Stably AI 维护，支持通过 Homebrew 和 AUR 包管理器安装。
  article_id: aae751d1d8aace5f
- object_type: product
  name: Orca iOS App
  canonical_name: Orca iOS
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Orca 提供了 iOS 端配套应用，用户可通过 App Store 下载或在 TestFlight 上加入测试，用于从手机端监控和操控桌面端的智能体。
  article_id: aae751d1d8aace5f
- object_type: product
  name: Orca Android App
  canonical_name: Orca Android
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Orca 提供了 Android 端配套应用，用户可下载 APK 0.0.27 版本，用于从手机上监控和操控桌面端的智能体。
  article_id: aae751d1d8aace5f
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