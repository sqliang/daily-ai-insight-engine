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
pipeline_stage: ingested
id: 8c3dc2a0187cafcc
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