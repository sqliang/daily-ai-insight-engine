---
title: Grok Build Coding Agent (GitHub Repo)
source: https://github.com/xai-org/grok-build?utm_source=tldrai
author: []
published: ''
created: '2026-07-17'
manifest_dates:
- '2026-07-17'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a1741c92ca5cbecf
source_type: news_media
tldr: xAI 发布了开源的 Grok Build，一个基于 Rust 的终端 AI 编程代理，支持全屏 TUI、文件编辑、shell 命令执行、Web 搜索和长时间运行任务管理，可通过交互模式、headless
  模式或 ACP 协议嵌入编辑器使用。
objective_summary: xAI 于 2026 年 7 月开源了 Grok Build，这是一个基于 Rust 构建的终端 AI 编程代理，仓库托管在
  GitHub 的 xai-org/grok-build。该工具提供全屏 TUI 界面，能够理解代码库、编辑文件、执行 shell 命令、搜索 Web 和管理长时间运行任务。它支持三种运行模式：交互式
  TUI、headless 脚本/CI 模式，以及通过 Agent Client Protocol (ACP) 嵌入编辑器。预编译二进制包已面向 macOS、Linux
  和 Windows 三平台发布，可通过官网脚本安装。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - xAI
  - SpaceXAI
  technologies:
  - ACP
  - MCP
  - TUI
  - Rust
  - DotSlash
  key_people: []
key_logic_flow:
- xAI 发布了 Grok Build，这是一个基于 Rust 构建的开源终端 AI 编程代理，源代码托管在 GitHub 的 xai-org/grok-build
  仓库中。
- Grok Build 提供全屏 TUI 界面，可以理解代码库、编辑文件、执行 shell 命令、搜索 Web 以及管理长时间运行的任务。
- 该工具支持三种运行模式：交互式 TUI 模式、用于脚本和 CI 的 headless 模式，以及通过 Agent Client Protocol (ACP) 嵌入编辑器使用。
- 预编译二进制包已面向 macOS、Linux 和 Windows 三平台发布，用户可通过 curl 或 PowerShell 脚本进行安装。
- 该仓库从 xAI 内部 monorepo 定期同步，包含 TUI 界面、agent 运行时、工具实现和 workspace 管理等多个 crate 模块。
- 项目附带完整的用户指南文档，涵盖快捷键、斜杠命令、配置、主题、MCP 服务器集成、sandbox 和 headless 模式等内容。
object_mentions:
- object_type: project
  name: xai-org/grok-build
  canonical_name: xai-org/grok-build
  url: https://github.com/xai-org/grok-build
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该仓库托管了 Grok Build 的 Rust 源代码，包含 TUI、agent 运行时、工具实现和 workspace 管理等完整的 crate 组织结构。
  - 项目支持交互式 TUI 模式、headless 脚本/CI 模式，以及通过 Agent Client Protocol (ACP) 嵌入编辑器的集成模式。
  - 预编译二进制包已面向 macOS、Linux 和 Windows 三平台发布，可通过 curl 或 PowerShell 脚本安装。
  article_id: a1741c92ca5cbecf
- object_type: product
  name: Grok Build
  canonical_name: Grok Build
  url: https://x.ai/cli
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Grok Build 是 xAI 开发的终端 AI 编程代理，以全屏 TUI 形式运行并理解用户的代码库。
  - 官方二进制包命名为 grok，安装后可通过命令行直接启动 TUI，首次运行需在浏览器中完成身份验证。
  - 该工具支持文件编辑、shell 命令执行、Web 搜索和长时间运行任务管理等多种功能。
  article_id: a1741c92ca5cbecf
- object_type: project
  name: Agent Client Protocol
  canonical_name: Agent Client Protocol
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Grok Build 支持通过 Agent Client Protocol (ACP) 嵌入编辑器中使用，作为编辑器集成的协议层。
  article_id: a1741c92ca5cbecf
extract_result: success
impact_score:
  score: 6.0
  reason: xAI 开源 Grok Build 是一个重要的产品发布，但不足以构成行业范式转移。它进入了一个已经相当拥挤的赛道——终端 AI 编程代理已有
    Claude Code、Codeium、OpenAI Codex CLI 等竞争者。评分 6.0 的理由：第一，基于 Rust 构建且采用 Apache 2.0
    开源协议，技术选型扎实但非独创；第二，支持 ACP (Agent Client Protocol) 嵌入编辑器是差异化亮点，可能推动编辑器生态的开放标准；第三，xAI
    品牌效应会吸引大量关注，但产品本身尚未展示出超越竞品的颠覆性能力。这在局部竞争格局上会产生影响（尤其是开源社区），但不足以改写行业规则。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 开源 Rust 实现 + ACP 协议能否打破现有编程代理的生态锁定
hype_assessment:
  level: low
  reason: 文章本身是客观的技术仓库介绍，没有使用'颠覆式'、'革命性'等 PR 用语，而是详细列举了技术架构、构建方式、运行模式和支持平台。GitHub
    仓库的 README 风格务实，提供了完整的 crate 模块说明、构建要求和文档链接。不存在概念炒作，属于实打实的产品发布。
information_entropy: high
domain_disruption:
  technical_innovation: 基于 Rust 构建的全屏 TUI 编程代理，采用多 crate 模块化架构（pager/shell/tools/workspace），支持三种运行模式（交互式
    TUI、headless CI、ACP 协议嵌入编辑器）。ACP 协议作为开放标准嵌入编辑器，有潜力打破当前编辑器 AI 插件的封闭生态。从 xAI 内部
    monorepo 定期同步的工程实践也值得关注。
  business_model: Apache 2.0 开源 + 预编译二进制分发的模式，类似 Anthropic 的 Claude Code 但更开放。xAI
    通过开源编程代理建立开发者生态和品牌认知，可能意图将 Grok 系列打造为 AI 开发的基础设施层，后续通过 xAI 云服务或企业版变现。对现有商用编程助手（GitHub
    Copilot、Cursor）形成开源替代压力。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Grok Build 是 xAI 在 AI 编程代理领域的重大战略布局，其开源策略（Apache 2.0）和 ACP 协议设计具有长期复利潜力。从
    VC 视角看：1) 开源意味着社区驱动的生态飞轮——第三方贡献、插件、企业部署都可以围绕它构建，且 Rust 实现保证了高性能基础，这对开发者工具至关重要；2)
    ACP（Agent Client Protocol）是 xAI 对抗日趋主流的 MCP（Anthropic 提出）的标准层竞争，如果 ACP 获得 VSCode/JetBrains
    等编辑器厂商的原生支持，将形成强网络效应和切换成本，这是 3-5 年维度上最大的价值来源；3) 三模式设计（TUI/headless/ACP）覆盖了从个人开发者到
    CI/CD 到编辑器集成的全场景，降低了采用门槛。但需关注风险：AI 编程代理市场已极度拥挤（Claude Code、Cursor、GitHub Copilot、Windsurf
    等），且 xAI 核心主业是 Grok 基础模型而非开发者工具，长期资源倾斜度存疑；开源虽利于采用但也意味着缺少直接变现路径，价值捕获依赖于 Grok API
    调用的间接拉动。综合判断，有潜力成为细分赛道关键基础设施，但需持续观察生态采纳速度和 xAI 的战略定力。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- xAI
- SpaceXAI
- ACP 协议生态
competitive_casualty:
- Anthropic (Claude Code)
- Cursor
- Windsurf
- GitHub Copilot
market_opportunities:
- 开发者工具团队可基于 Grok Build 的 ACP（Agent Client Protocol）协议实现编辑器深度集成，构建定制化的 AI 编程助手；该协议有望成为类似
  LSP 的行业标准接口，率先适配者将获得生态卡位优势
- 企业可基于 Grok Build 的开源 Rust 代码库，构建内部安全沙箱化的 AI 编程代理，结合私有的代码仓库和合规策略，实现安全可控的辅助编码流水线
- MCP 服务器集成能力和 DotSlash 工具链管理机制为云 IDE 和 DevContainer 提供商提供了将终端 AI 代理嵌入云端开发环境的技术路线，可探索
  DevSecOps 场景下的自动化代码审查与修复服务
risk_matrix:
  regulatory: 开源 Apache 2.0 协议兼容性风险：Grok Build 内部包含来自 openai/codex 和 sst/opencode
    的移植代码并附有单独的通知文件，企业二次分发或修改时需要仔细遵守各第三方组件的原始许可证要求；此外，AI 生成代码的版权归属在不同司法管辖区仍存在法律不确定性
  technological: AI 编程代理赛道技术迭代极快，Grok Build 须面临来自 Cursor、GitHub Copilot、Windsurf、Amazon
    Q Developer 等成熟竞品的持续功能碾压；基于 Rust 构建虽然在性能和安全性上有优势，但生态工具链（如 protoc 和 DotSlash 的前置依赖）增加了首次构建门槛，可能限制社区贡献者的涌入
  competitive: 这是一个红海市场：GitHub Copilot 拥有 VSCode 天然流量入口，Cursor 已建立强大的编辑器原生体验心智，Anthropic
    的 Claude Code 和 OpenAI 的 Codex CLI 也在同一赛道竞争；xAI 的终端 TUI 形态而非编辑器插件的定位可能面临用户习惯迁移成本高的挑战
  ethical: AI 编程代理自动执行 shell 命令和文件编辑存在安全隐患：尽管项目文档提及 sandbox 功能，但代码自动修改可能引入难以察觉的安全漏洞或逻辑缺陷；此外，由
    AI 代理主导的编码流程可能弱化开发者的代码审查意识，长期造成技术能力退化风险
  additional:
  - 预编译二进制包依赖单一的安装源（x.ai域名），如果出现服务中断或域名变更将影响持续集成环境的稳定性部署
  - 项目从 xAI 内部 monorepo 定期同步而非实时持续开发，存在上游更新与开源仓库之间的版本滞后风险
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: xai-org/grok-build
  canonical_name: xai-org/grok-build
  url: https://github.com/xai-org/grok-build
  positioning: xAI 开源的基于 Rust 构建的终端 AI 编程代理项目，采用模块化 crate 架构，支持交互式 TUI、headless 脚本和
    ACP 协议嵌入三种运行模式。
  technical_signal: 项目采用 Rust 语言构建，模块化组织为 TUI、agent 运行时、工具实现和 workspace 管理等多个独立 crate，架构清晰且可维护。
  adoption_signal: 已面向 macOS、Linux 和 Windows 三平台发布预编译二进制包，可通过一条 curl 或 PowerShell
    命令完成安装，降低了使用门槛。
  ecosystem_relevance: 支持通过 Agent Client Protocol (ACP) 嵌入编辑器使用，并集成 MCP 服务器、插件、hooks
    和 sandbox 等开放的生态扩展能力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 xAI 首个开源的编程代理项目，Grok Build 展示了 xAI 在 AI 编程工具领域的技术布局，其 Rust 实现、多模式运行和
    MCP 集成能力使其在终端 AI 代理赛道中具有独特的差异化价值。
  risk_notes:
  - 项目从 xAI 内部 monorepo 定期同步，存在版本滞后风险，且 Windows 构建为 best-effort 未获完整测试。
  score: 8.0
  article_ids:
  - a1741c92ca5cbecf
  evidence_snippets:
  - 该仓库托管了 Grok Build 的 Rust 源代码，包含 TUI、agent 运行时、工具实现和 workspace 管理等完整的 crate 组织结构。
  - 项目支持交互式 TUI 模式、headless 脚本/CI 模式，以及通过 Agent Client Protocol (ACP) 嵌入编辑器的集成模式。
  - 预编译二进制包已面向 macOS、Linux 和 Windows 三平台发布，可通过 curl 或 PowerShell 脚本安装。
- object_type: product
  name: Grok Build
  canonical_name: Grok Build
  url: https://x.ai/cli
  positioning: xAI 推出的终端 AI 编程代理产品，以全屏 TUI 界面提供代码理解、文件编辑、Shell 命令执行和长时间运行任务管理等能力，支持三种运行模式。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 开发者
  - 命令行爱好者
  - 软件工程师
  product_signal: 提供文件编辑、Shell 命令执行、Web 搜索和长时间运行任务管理等完整的 AI 编程辅助能力，支持交互式 TUI、headless
    和 ACP 嵌入三种模式。
  market_signal: xAI 继 Grok 对话模型后进入 AI 编程代理市场，与 Cursor、Claude Code 和 GitHub Copilot
    等产品形成直接竞争格局。
  differentiation: 采用全屏 TUI 交互而非传统聊天界面，同时支持 headless CI 模式和 ACP 协议编辑器嵌入，覆盖从交互开发到自动化管线的广泛使用场景。
  watch_reason: xAI 从对话模型 Grok 扩展到 AI 编程代理领域，Grok Build 的 Rust 高性能实现和多模式 TUI 设计使其在终端
    AI 代理市场中具备差异化竞争力，值得密切关注其用户增长和生态发展。
  risk_notes:
  - 作为初代产品，在功能成熟度和社区生态上可能落后于 Cursor、Claude Code 等已建立用户基础的竞品。
  score: 7.0
  article_ids:
  - a1741c92ca5cbecf
  evidence_snippets:
  - Grok Build 是 xAI 开发的终端 AI 编程代理，以全屏 TUI 形式运行并理解用户的代码库。
  - 官方二进制包命名为 grok，安装后可通过命令行直接启动 TUI，首次运行需在浏览器中完成身份验证。
  - 该工具支持文件编辑、shell 命令执行、Web 搜索和长时间运行任务管理等多种功能。
---

**Grok Build** is SpaceXAI's terminal-based AI coding agent. It runs as a
full-screen TUI that understands your codebase, edits files, executes shell
commands, searches the web, and manages long-running tasks — interactively,
headlessly for scripting/CI, or embedded in editors via the Agent Client
Protocol (ACP).

Installing the released binary · Building from source · Documentation · Repository layout · Development · Contributing · License

**Learn more about Grok Build at x.ai/cli**

This repository contains the Rust source for the `grok`

CLI/TUI and its agent
runtime. It is synced periodically from the SpaceXAI monorepo.

A small `SOURCE_REV`

file at the root records the full monorepo commit SHA
for the version of the code present in this tree.

Prebuilt binaries are published for macOS, Linux, and Windows:

```
curl -fsSL https://x.ai/cli/install.sh | bash # macOS / Linux / Git Bash
irm https://x.ai/cli/install.ps1 | iex # Windows PowerShell
grok --version
```

See the changelog for the latest fixes, features, and improvements in each release.

Requirements:

-
**Rust**— the toolchain is pinned by`rust-toolchain.toml`

;`rustup`

installs it automatically on first build. -
**DotSlash**— required so hermetic tools under`bin/`

(notably`bin/protoc`

) can download and run. Install it and ensure`dotslash`

is on your`PATH`

**before**building:cargo install dotslash # or: prebuilt packages — https://dotslash-cli.com/docs/installation/ /usr/bin/env dotslash --help # sanity check

-
**protoc**— proto codegen resolves`bin/protoc`

via DotSlash, or falls back to a`protoc`

on`PATH`

/`$PROTOC`

. -
macOS and Linux are supported build hosts; Windows builds are best-effort and not currently tested from this tree.


```
cargo run -p xai-grok-pager-bin # build + launch the TUI
cargo build -p xai-grok-pager-bin --release # release binary: target/release/xai-grok-pager
cargo check -p xai-grok-pager-bin # fast validation
```

The binary artifact is named `xai-grok-pager`

; official installs ship it as
`grok`

. On first launch it opens your browser to authenticate — see the
authentication guide.

Full online documentation is available at docs.x.ai/build/overview.

The user guide ships with the pager crate:
`crates/codegen/xai-grok-pager/docs/user-guide/`

— getting started, keyboard shortcuts, slash commands, configuration, theming,
MCP servers, skills, plugins, hooks, headless mode, sandboxing, and more.

| Path | Contents |
|---|---|
`crates/codegen/xai-grok-pager-bin` |
Composition-root package; builds the `xai-grok-pager` binary |
`crates/codegen/xai-grok-pager` |
The TUI: scrollback, prompt, modals, rendering |
`crates/codegen/xai-grok-shell` |
Agent runtime + leader/stdio/headless entry points |
`crates/codegen/xai-grok-tools` |
Tool implementations (terminal, file edit, search, ...) |
`crates/codegen/xai-grok-workspace` |
Host filesystem, VCS, execution, checkpoints |
`crates/codegen/...` |
The rest of the CLI crate closure (config, MCP, markdown, sandbox, ...) |
`crates/common/` , `crates/build/` , `prod/mc/` |
Small shared leaf crates pulled in by the closure |
`third_party/` |
Vendored upstream source (Mermaid diagram stack) — see below |

Important

The root `Cargo.toml`

(workspace members, dependency versions, lints,
profiles) is **generated** — treat it as read-only. Prefer editing per-crate
`Cargo.toml`

files.

```
cargo check -p <crate> # always target specific crates; full-workspace builds are slow
cargo test -p xai-grok-config # per-crate tests
cargo clippy -p <crate> # lint config: clippy.toml at the repo root
cargo fmt --all # rustfmt.toml at the repo root
```

First-party code in this repository is licensed under the **Apache License,
Version 2.0** — see `LICENSE`

.

Third-party and vendored code remains under its original licenses. See:

`THIRD-PARTY-NOTICES`

— crates.io / git dependencies, bundled UI themes, and**in-tree source ports**(including openai/codex and sst/opencode tool implementations)`crates/codegen/xai-grok-tools/THIRD_PARTY_NOTICES.md`

— crate-local notice for the codex and opencode ports (license texts + Apache §4(b) change notice)`third_party/NOTICE`

— vendored Mermaid-stack index