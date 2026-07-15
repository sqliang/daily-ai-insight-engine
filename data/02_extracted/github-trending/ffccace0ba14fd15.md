---
title: anomalyco/opencode
source: https://github.com/anomalyco/opencode
author: []
published: ''
created: '2026-06-28'
description: 'The open source coding agent. The open source AI coding agent. English
  | 简体中文 | 繁體中文 | 한국어 | Deutsch | Español | Français | Italiano | Dansk | 日本語 | Polski
  | Русский | Bosanski | العربية | Norsk | Português (Brasil) | ไทย | Türkçe | Українська
  | বাংলা | Ελληνικά | Tiếng Việt Installation # YOLO curl -fsSL https://opencode.ai/install
  | bash # Package managers npm i -g opencode-ai@latest # or bun/pnpm/yarn scoop install
  opencode # Windows choco install opencode # Windows brew install anomalyco/tap/opencode
  # macOS and Linux (recommended, always up to date) brew install opencode # macOS
  and Linux (official brew formula, updated less) sudo pacman -S opencode # Arch Linux
  (Stable) paru -S opencode-bin # Arch Linux (Latest from AUR) mise use -g opencode
  # Any OS nix run nixpkgs#opencode # or github:anomalyco/opencode for latest dev
  branch Tip Remove versions older than 0.1.x before installing. Desktop App (BETA)
  OpenCode is also available as a desktop application. Download directly from the
  releases page or opencode.ai/download. Platform Download macOS (Apple Silicon) opencode-desktop-mac-arm64.dmg
  macOS (Intel) opencode-desktop-mac-x64.dmg Windows opencode-desktop-windows-x64.exe
  Linux .deb, .rpm, or .AppImage # macOS (Homebrew) brew install --cask opencode-desktop
  # Windows (Scoop) scoop bucket add extras; scoop install extras/opencode-desktop
  Installation Directory The install script respects the following priority order
  for the installation path: $OPENCODE_INSTALL_DIR - Custom installation directory
  $XDG_BIN_DIR - XDG Base Directory Specification compliant path $HOME/bin - Standard
  user binary directory (if it exists or can be created) $HOME/.opencode/bin - Default
  fallback # Examples OPENCODE_INSTALL_DIR=/usr/local/bin curl -fsSL https://opencode.ai/install
  | bash XDG_BIN_DIR=$HOME/.local/bin curl -fsSL https://opencode.ai/install | bash
  Agents OpenCode includes two built-in agents you can switch between with the Tab
  key. build - Default, full-access agent for development work plan - Read-only agent
  for analysis and code exploration Denies file edits by default Asks permission before
  running bash commands Ideal for exploring unfamiliar codebases or planning changes
  Also included is a general subagent for complex searches and multistep tasks. This
  is used internally and can be invoked using @general in messages. Learn more about
  agents. Documentation For more info on how to configure OpenCode, head over to our
  docs. Contributing If you''re interested in contributing to OpenCode, please read
  our contributing docs before submitting a pull request. Building on OpenCode If
  you are working on a project that''s related to OpenCode and is using "opencode"
  as part of its name, for example "opencode-dashboard" or "opencode-mobile", please
  add a note to your README to clarify that it is not built by the OpenCode team and
  is not affiliated with us in any way. Join our community Discord | X.com'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ffccace0ba14fd15
source_type: community_discussion
tldr: OpenCode 开源 AI 编码代理，支持 CLI 和桌面应用
objective_summary: anomalyco 团队发布 OpenCode，一个开源 AI 编码代理，提供 curl 脚本及多种包管理器安装的 CLI 版本，以及
  macOS、Windows、Linux 桌面应用。内置 build（全权限）和 plan（只读）两种代理模式。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - anomalyco
  technologies: []
  key_people: []
key_logic_flow:
- OpenCode 是一个开源的 AI 编码代理，支持通过 curl 一键安装脚本以及 npm、brew、scoop、choco、pacman、mise、nix
  等多种包管理器进行安装。
- OpenCode 提供桌面应用版本，支持 macOS（Apple Silicon 和 Intel）、Windows 和 Linux 平台，可通过 DMG、EXE、DEB、RPM、AppImage
  等格式下载。
- OpenCode 内置两种代理模式：build 代理为默认模式，拥有全权限用于开发工作；plan 代理为只读模式，用于代码分析和探索，默认禁止文件编辑，执行命令前需请求许可。
- OpenCode 还包含一个 general 子代理，用于复杂搜索和多步骤任务，可通过 @general 在消息中调用。
specialized_tags:
  github:
    projectName: anomalyco/opencode
    projectUrl: https://github.com/anomalyco/opencode
    primaryLanguage: TypeScript
    licenseType: null
    domain: ai_ml
    crossTags:
    - open-source-alternative
    - cli-tool
    aiDetail:
      primaryCategories:
      - code_gen
      agentSubcategory: []
      techTags: []
extract_result: success
---

The open source AI coding agent.

English | 简体中文 | 繁體中文 | 한국어 | Deutsch | Español | Français | Italiano | Dansk | 日本語 | Polski | Русский | Bosanski | العربية | Norsk | Português (Brasil) | ไทย | Türkçe | Українська | বাংলা | Ελληνικά | Tiếng Việt

```
# YOLO
curl -fsSL https://opencode.ai/install | bash
# Package managers
npm i -g opencode-ai@latest # or bun/pnpm/yarn
scoop install opencode # Windows
choco install opencode # Windows
brew install anomalyco/tap/opencode # macOS and Linux (recommended, always up to date)
brew install opencode # macOS and Linux (official brew formula, updated less)
sudo pacman -S opencode # Arch Linux (Stable)
paru -S opencode-bin # Arch Linux (Latest from AUR)
mise use -g opencode # Any OS
nix run nixpkgs#opencode # or github:anomalyco/opencode for latest dev branch
```

Tip

Remove versions older than 0.1.x before installing.

OpenCode is also available as a desktop application. Download directly from the releases page or opencode.ai/download.

| Platform | Download |
|---|---|
| macOS (Apple Silicon) | `opencode-desktop-mac-arm64.dmg` |
| macOS (Intel) | `opencode-desktop-mac-x64.dmg` |
| Windows | `opencode-desktop-windows-x64.exe` |
| Linux | `.deb` , `.rpm` , or `.AppImage` |

```
# macOS (Homebrew)
brew install --cask opencode-desktop
# Windows (Scoop)
scoop bucket add extras; scoop install extras/opencode-desktop
```

The install script respects the following priority order for the installation path:

`$OPENCODE_INSTALL_DIR`

- Custom installation directory`$XDG_BIN_DIR`

- XDG Base Directory Specification compliant path`$HOME/bin`

- Standard user binary directory (if it exists or can be created)`$HOME/.opencode/bin`

- Default fallback

```
# Examples
OPENCODE_INSTALL_DIR=/usr/local/bin curl -fsSL https://opencode.ai/install | bash
XDG_BIN_DIR=$HOME/.local/bin curl -fsSL https://opencode.ai/install | bash
```

OpenCode includes two built-in agents you can switch between with the `Tab`

key.

**build**- Default, full-access agent for development work**plan**- Read-only agent for analysis and code exploration- Denies file edits by default
- Asks permission before running bash commands
- Ideal for exploring unfamiliar codebases or planning changes


Also included is a **general** subagent for complex searches and multistep tasks.
This is used internally and can be invoked using `@general`

in messages.

Learn more about agents.

For more info on how to configure OpenCode, **head over to our docs**.

If you're interested in contributing to OpenCode, please read our contributing docs before submitting a pull request.

If you are working on a project that's related to OpenCode and is using "opencode" as part of its name, for example "opencode-dashboard" or "opencode-mobile", please add a note to your README to clarify that it is not built by the OpenCode team and is not affiliated with us in any way.