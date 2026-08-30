---
title: openai/codex
source: https://github.com/openai/codex
author: []
published: ''
created: '2026-08-23'
manifest_dates:
- '2026-08-23'
- '2026-08-24'
- '2026-08-25'
- '2026-08-26'
- '2026-08-27'
description: 'Lightweight coding agent that runs in your terminalCodex CLI is a coding
  agent from OpenAI that runs locally on your computer. If you want Codex in your
  code editor (VS Code, Cursor, Windsurf), install in your IDE. If you want the desktop
  app experience, run codex app or visit the Codex App page. If you are looking for
  the cloud-based agent from OpenAI, Codex Web, go to chatgpt.com/codex. Quickstart
  Installing and running Codex CLI Run the following on Mac or Linux to install Codex
  CLI: curl -fsSL https://chatgpt.com/codex/install.sh | sh Run the following on Windows
  to install Codex CLI: powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1
  | iex" The standalone installers download from https://releases.openai.com/codex
  by default and fall back to GitHub Releases if a metadata or asset download is unavailable.
  To force GitHub Releases, set CODEX_INSTALLER_USE_RELEASES_OPENAI_COM to false (0
  and no are also accepted): curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=false
  sh $env:CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=''false''; irm https://chatgpt.com/codex/install.ps1
  | iex Codex CLI can also be installed via the following package managers: # Install
  using npm npm install -g @openai/codex # Install using Homebrew brew install --cask
  codex Then simply run codex to get started. You can also go to the latest GitHub
  Release and download the appropriate binary for your platform. Each GitHub Release
  contains many executables, but in practice, you likely want one of these: macOS
  Apple Silicon/arm64: codex-aarch64-apple-darwin.tar.gz x86_64 (older Mac hardware):
  codex-x86_64-apple-darwin.tar.gz Linux x86_64: codex-x86_64-unknown-linux-musl.tar.gz
  arm64: codex-aarch64-unknown-linux-musl.tar.gz Each archive contains a single entry
  with the platform baked into the name (e.g., codex-x86_64-unknown-linux-musl), so
  you likely want to rename it to codex after extracting it. Using Codex with your
  ChatGPT plan Run codex and select Sign in with ChatGPT. We recommend signing into
  your ChatGPT account to use Codex as part of your Plus, Pro, Business, Edu, or Enterprise
  plan. Learn more about what''s included in your ChatGPT plan. You can also use Codex
  with an API key, but this requires additional setup. Docs Codex Documentation Contributing
  Installing & building Open source fund This repository is licensed under the Apache-2.0
  License.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 8c3dc2a0187cafcc
source_type: community_discussion
tldr: OpenAI 在 GitHub 发布 Codex CLI，这是一个在本地运行的编程代理，支持 Mac、Linux 与 Windows，可通过安装脚本、npm、Homebrew
  或 GitHub Release 二进制安装，并支持 VS Code 等 IDE 集成。
objective_summary: OpenAI 在 GitHub 上发布 openai/codex 仓库，介绍其本地运行的编程代理 Codex CLI。该工具支持
  Mac、Linux 与 Windows 系统，用户可通过安装脚本、npm、Homebrew 或 GitHub Release 二进制文件安装，并可集成到 VS
  Code、Cursor、Windsurf 等编辑器。文章同时区分了云端代理 Codex Web（位于 chatgpt.com/codex）与桌面应用 Codex
  App，并建议使用 ChatGPT 账号登录以纳入 Plus、Pro、Business、Edu 或 Enterprise 订阅套餐。该仓库采用 Apache-2.0
  许可证。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  technologies:
  - Codex CLI
  - Codex Web
  key_people: []
key_logic_flow:
- OpenAI 发布 Codex CLI，它是一个在本地计算机上运行的编程代理。
- 用户可通过 Mac/Linux 安装脚本、Windows PowerShell 命令、npm、Homebrew 或 GitHub Release 二进制文件安装
  Codex CLI。
- Codex CLI 支持 VS Code、Cursor、Windsurf 等代码编辑器的 IDE 集成，并可通过 codex app 获得桌面应用体验。
- OpenAI 还提供云端代理 Codex Web，位于 chatgpt.com/codex，与本地运行的版本相区别。
- 文章推荐使用 ChatGPT 账号登录以纳入 Plus、Pro、Business、Edu 或 Enterprise 订阅套餐，也可通过 API 密钥使用但需要额外配置。
- 该仓库采用 Apache-2.0 许可证发布。
object_mentions:
- object_type: project
  name: openai/codex
  canonical_name: openai/codex
  url: https://github.com/openai/codex
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Codex CLI 是 OpenAI 推出的本地运行的编程代理，可通过 curl 脚本、npm、Homebrew 或 GitHub Release 二进制文件安装。
  - Codex CLI 可在 Mac、Linux 与 Windows 上安装，并支持 VS Code、Cursor、Windsurf 等编辑器的 IDE 集成。
  article_id: 8c3dc2a0187cafcc
- object_type: product
  name: Codex Web
  canonical_name: Codex Web
  url: https://chatgpt.com/codex
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到 OpenAI 的云端代理 Codex Web 位于 chatgpt.com/codex，与本地运行的 Codex CLI 相区别。
  article_id: 8c3dc2a0187cafcc
- object_type: product
  name: Codex App
  canonical_name: Codex App
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章说明如需桌面应用体验，可运行 codex app 命令或访问 Codex App 页面获取。
  article_id: 8c3dc2a0187cafcc
extract_result: success
---

**Codex CLI** is a coding agent from OpenAI that runs locally on your computer.

If you want Codex in your code editor (VS Code, Cursor, Windsurf), install in your IDE.

If you want the desktop app experience, run

`codex app`

or visit the Codex App page.
If you are looking for the

*cloud-based agent*from OpenAI,

**Codex Web**, go to chatgpt.com/codex.

Run the following on Mac or Linux to install Codex CLI:

`curl -fsSL https://chatgpt.com/codex/install.sh | sh`

Run the following on Windows to install Codex CLI:

`powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`

The standalone installers download from `https://releases.openai.com/codex`

by default and fall back to GitHub Releases if a metadata or asset download is unavailable. To force GitHub Releases, set `CODEX_INSTALLER_USE_RELEASES_OPENAI_COM`

to `false`

(`0`

and `no`

are also accepted):

`curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=false sh`

`$env:CODEX_INSTALLER_USE_RELEASES_OPENAI_COM='false'; irm https://chatgpt.com/codex/install.ps1 | iex`

Codex CLI can also be installed via the following package managers:

```
# Install using npm
npm install -g @openai/codex
```

```
# Install using Homebrew
brew install --cask codex
```

Then simply run `codex`

to get started.

## You can also go to the latest GitHub Release and download the appropriate binary for your platform.

Each GitHub Release contains many executables, but in practice, you likely want one of these:

- macOS
- Apple Silicon/arm64:
`codex-aarch64-apple-darwin.tar.gz`

- x86_64 (older Mac hardware):
`codex-x86_64-apple-darwin.tar.gz`


- Apple Silicon/arm64:
- Linux
- x86_64:
`codex-x86_64-unknown-linux-musl.tar.gz`

- arm64:
`codex-aarch64-unknown-linux-musl.tar.gz`


- x86_64:

Each archive contains a single entry with the platform baked into the name (e.g., `codex-x86_64-unknown-linux-musl`

), so you likely want to rename it to `codex`

after extracting it.

Run `codex`

and select **Sign in with ChatGPT**. We recommend signing into your ChatGPT account to use Codex as part of your Plus, Pro, Business, Edu, or Enterprise plan. Learn more about what's included in your ChatGPT plan.

You can also use Codex with an API key, but this requires additional setup.

This repository is licensed under the Apache-2.0 License.