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