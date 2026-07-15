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
impact_score:
  score: 6.0
  reason: AI 编码代理赛道目前已极度拥挤（Claude Code、Codex CLI、Cursor、Windsurf、Continue.dev、Aider
    等），OpenCode 作为后来者并未带来范式级别的技术突破。但其差异化在于：完全开源 + CLI 与桌面应用双形态 + 横跨 macOS/Windows/Linux
    全平台 + 支持 npm/brew/scoop/pacman/nix 等十余种包管理器，安装体验极佳。内置 build（全权限）和 plan（只读）双代理模式的产品设计也体现了工程成熟度。在编码代理工具日趋同质化的阶段，OpenCode
    凭借开源策略和多平台覆盖有望获取一定市场份额，但不足以改变行业格局。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 与 Claude Code、Codex CLI 等现有编码代理的实际能力对比，以及开源社区的后续迭代活力
hype_assessment:
  level: medium
  reason: 该 README 整体较为务实，以安装说明为主，没有出现'革命性''颠覆'等过度宣传词汇。但作为新产品发布，必然存在一定市场包装成分。OpenCode
    宣称支持'所有主要平台和包管理器'是事实而非夸张，因此 hype 程度属于中等。
information_entropy: medium
domain_disruption:
  technical_innovation: 无显著技术突破。build/plan 双代理模式是产品层面的合理分层设计（权限隔离），并非工程架构层面的本质创新。general
    子代理支持 @mention 调用的交互模式值得关注，但技术实现上不构成突破。
  business_model: 开源策略有望通过社区生态形成对闭源竞品（如 Cursor、Claude Code）的替代压力。商业模式可能延续'开源核心 + 企业功能付费'的典型路径，对现有
    AI 编码工具定价体系形成一定冲击。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: OpenCode 作为开源 AI 编码代理，在产品成熟度上表现不错：跨平台桌面应用（macOS/Windows/Linux）、多种包管理器覆盖（brew/scoop/choco/npm/pacman/nix）、内置
    build（全权限）和 plan（只读）双代理模式，以及 @general 子代理调用能力。长期复利价值取决于三个关键变量：(1) 开源社区能否形成插件/扩展生态的网络效应，进而成为
    AI 编码领域的'VS Code 时刻'；(2) 在 Cursor（Anysphere 融资超 4 亿美元）、GitHub Copilot（微软生态绑定）、Claude
    Code（Anthropic 原生）、Windsurf（Codeium）等强敌环伺下，能否通过开放性和可定制性建立差异化壁垒；(3) 开源商业化路径是否可持续——纯靠捐赠难以支撑长期迭代，需观察
    anomalyco 团队是否会推出企业版或托管服务。当前评分 6.0：有潜力成为开发者工具链的基础设施，但 AI 编码代理赛道竞争极剧、技术迭代快、且开源模型面临被闭源产品快速复制的风险，需持续验证
    PMF 和商业化能力。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- anomalyco
- 开源 AI 开发者社区
- Anthropic
- OpenAI
competitive_casualty:
- Cursor
- Windsurf
- 小型纯订阅制 AI 编码助手创业公司
market_opportunities:
- 企业可基于 OpenCode 开源代码构建内部私有化 AI 编码助手，在保障代码数据不外泄的前提下提升团队开发效率
- 开发者可利用 OpenCode 的 build/plan/general 多代理架构，针对安全审计、遗留系统重构等垂直场景定制专用编码代理
- OpenCode 的全平台（CLI + 桌面端）和多包管理器分发策略，为 AI 编码工具的开源商业化提供了可复用的增长范式
risk_matrix:
  regulatory: AI 辅助生成代码的版权归属和开源合规问题尚不明确，企业在生产环境使用前需进行法律风险评估
  technological: 与 Cursor、Claude Code、GitHub Copilot 等商业化产品存在明显技术代差，且开源项目社区迭代节奏不稳定，可能落后于闭源竞品的快速演进
  competitive: AI 编码代理赛道已被巨头和明星创业公司占据（GitHub Copilot 深度绑定 IDE、Anthropic Claude Code、Cursor），OpenCode
    作为新晋开源项目获取用户和贡献者的成本极高
  ethical: AI 编码代理可能生成包含安全漏洞或逻辑缺陷的代码，增加软件供应链风险；同时自动化编码能力可能冲击初级开发者的就业市场
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
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