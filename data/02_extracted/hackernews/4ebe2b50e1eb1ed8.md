---
title: 'Show HN: Ante, a coding agent in a single binary that runs offline'
source: https://github.com/AntigmaLabs/ante
author:
- '[[ubermon]]'
published: '2026-08-10'
created: '2026-08-11'
manifest_dates:
- '2026-08-11'
description: 'Article URL: https://github.com/AntigmaLabs/ante Comments URL: https://news.ycombinator.com/item?id=49245437
  Points: 131 # Comments: 79'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4ebe2b50e1eb1ed8
source_type: community_discussion
tldr: Antigma Labs 发布 Ante，一款约 15MB 的单二进制离线编码智能体，用 Rust 手写、内置 llama.cpp 本地推理，在 Terminal-Bench
  2.1 上取得 82.7% 分数，并开源文档、协议与 SDK。
objective_summary: 2026 年，Antigma Labs 在 Hacker News 通过 Show HN 发布编码智能体 Ante。它是一个用
  Rust 手写的约 15MB 单二进制程序，核心 harness 以预编译二进制形式发布，仓库内开源了文档、协议、SDK 与评测管线。Ante 在 Terminal-Bench
  2.1 上搭配 DeepSeek V4 Flash 0731 取得 82.7% 准确率，并宣称在 Docker 并行任务下比 Claude Code 节省约 7
  倍峰值内存与 9 倍平均 CPU。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Antigma Labs
  - DeepSeek
  - Anthropic
  - OpenAI
  - Google
  - xAI
  - Open Router
  technologies:
  - Rust
  - llama.cpp
  - GGUF
  - MCP
  - Terminal-Bench
  - TUI
  - JSONL
  key_people: []
key_logic_flow:
- Ante 是 Antigma Labs 开发的单二进制编码智能体，约 15MB 的 Rust 程序，零运行时依赖，可在终端内自组织运行。
- 核心 harness 在 alpha 阶段以预编译二进制发布，仓库开源了 docs-site 文档、protocol-shape 协议、agent-sdk SDK、ante-harbor
  评测管线与 exec 库。
- Ante 在 Terminal-Bench 2.1 上以 DeepSeek V4 Flash 0731 取得 82.7% 准确率，共 368/445 trials，推理成本约
  68 美元。
- Ante 内置固定版本的 llama.cpp 推理引擎，可直接加载本地 GGUF 模型完全离线运行，无需 API key 与网络连接。
- 相比 Claude Code，Ante 在 Docker 中 20 个并行任务下使用约 7 倍更少的峰值内存、9 倍更少的平均 CPU 与 5 倍更少的磁盘 I/O。
- Ante 支持交互式 TUI、headless、serve 服务器与 gateway 网关四种模式，兼容 12 家以上模型提供商并支持 MCP 与多智能体编排。
object_mentions:
- object_type: product
  name: Ante
  canonical_name: Ante
  url: https://github.com/AntigmaLabs/ante
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Ante 是 Antigma Labs 开发的单二进制编码智能体，约 15MB 的 Rust 程序，零运行时依赖，可在终端内自组织运行。
  - Ante 在 Terminal-Bench 2.1 上搭配 DeepSeek V4 Flash 0731 取得 82.7% 准确率，并支持本地 GGUF 模型完全离线推理。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: ante-harbor
  canonical_name: ante-harbor
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - ante-harbor 是 Ante 的 Harbor 智能体适配器，负责产出 Terminal-Bench 结果，可用于复现 antigma.ai/eval
    上的任何评测运行。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: crates/agent-sdk
  canonical_name: Ante agent-sdk
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - crates/agent-sdk 是 Antigma Labs 开源的 Rust SDK 与客户端，用于基于 agent 运行时构建应用，遵循 Apache
    2.0 许可。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: crates/protocol-shape
  canonical_name: Ante protocol-shape
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - crates/protocol-shape 定义了 ante serve 模式所遵循的 schema 与线缆消息协议，是 Ante 核心协议的开源实现。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: nanochat-rs
  canonical_name: nanochat-rs
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - nanochat-rs 是 Ante 团队开源的教学版玩具引擎，用于研究内置 llama.cpp 本地推理引擎的工作原理。
  article_id: 4ebe2b50e1eb1ed8
- object_type: project
  name: crates/exec
  canonical_name: Ante exec crate
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - crates/exec 是 Ante 核心库中第一个被渐进开源到仓库的独立进程执行库，作为稳定化的核心组件随 alpha 发布。
  article_id: 4ebe2b50e1eb1ed8
extract_result: success
---

Alpha preview: expect breaking changes and incomplete functionality. macOS and Linux only; on Windows we suggest WSL.

Two things many people ask about:

**Where is the source?** The core harness currently ships as a prebuilt binary; this repo holds the docs, protocol, SDK, and eval pipeline (details). We are working out a way to ship the source code along with the binary, to address security and privacy concerns first, while taking the time to figure out how open source should work in the agentic era. If you have concerns today, run Ante in a sandbox: it is a single binary with minimal runtime dependencies, built to be easy to deploy in a container or on a remote machine.

**Is there telemetry?** Yes, and it is opt-out: set `ANTE_TELEMETRY=off`

to disable export entirely. What it sends is anonymous — a random installation label you can delete and re-mint, never your username, hostname, or machine id. The `RUST_LOG`

filter also applies to exported logs, a convenience carried over from the Rust ecosystem. A better UX is in the works. Details →

**A ghost in your shell.** Ante is a self-contained coding agent that lives in your terminal and self-organizes. One ~15MB Rust binary from Antigma Labs, zero runtime dependencies, built to get the most out of any model.

It works like Claude Code or Codex, with none of their dependencies or model constraints. It can also be the optimized core for building your own harness and high-performing assistants.

```
curl -fsSL https://ante.run/install.sh | bash
ante
```

Every agent claims to be good. Here are numbers you can check:

Ante runs Terminal-Bench 2.1 continuously under official leaderboard constraints: 89 tasks, 5 trials each. Each result pins the exact build you can download and links the raw Harbor run for independent audit. Latest full run: **82.7%** with open-weight **DeepSeek V4 Flash 0731** (368/445 trials, Ante 0.preview.71, about $68 of inference). DeepSeek reports the same 82.7 for this model, measured with its unreleased DeepSeek Harness in minimal mode.

**Live results →** · Methodology →

Ante is hand-written Rust with the heavy parts (`Grep`

, `git`

) embedded in one binary, one process, and local inference handled by a pinned, managed llama.cpp. Across the same 20 parallel tasks in Docker, Ante uses **~7× less peak memory**, **~9× less average CPU**, and **~5× less disk I/O** than Claude Code.

**Raw numbers →** · Benchmark details →

Ante's inference engine is a pinned, managed version of llama.cpp. Point it at a GGUF file and the whole loop runs on your machine: no API key, no account, no internet.

```
ante --offline-model ~/.ante/models/Qwen3.5-9B-Q4_K_M.gguf \
-p "add error handling to src/main.rs"
```

**Offline mode →** · nanochat-rs, a toy engine for study →

The three are one design decision. An agent you can **verify**, **afford**, and **run anywhere** is light enough to run by the *thousands*: the substrate for self-organizing intelligence.

Ante is a single, self-contained binary with no external dependencies: download and run.

```
curl -fsSL https://ante.run/install.sh | bash
# Install a specific release channel
curl -fsSL https://ante.run/install.sh | bash -s -- nightly
# Install into a directory already on PATH
curl -fsSL https://ante.run/install.sh | ANTE_INSTALL_DIR=/usr/local/bin bash
```

| Mode | Command | Use it for |
|---|---|---|
| Interactive TUI | `ante` |
day-to-day work in the terminal |
| Headless | `ante -p "..."` |
one-shot tasks, scripts, CI |
| Server | `ante serve` |
editor plugins and integrations, over a JSONL protocol |
| Gateway | `ante gateway` |
running Ante as a Slack or Discord bot |

```
# Fix a bug
ante -p "find and fix the failing test in src/auth"
# Review a diff
git diff | ante -p "review this for security issues"
# Use a different provider
ante --provider openai --model gpt-5.5 -p "refactor the database module"
# Resume a saved session
ante --resume ses_01ARZ3NDEKTSV4RRFFQ69G5FAV -p "now add tests"
# Run fully offline with a local GGUF model
ante --offline-model ~/.ante/models/Qwen3.5-9B-Q4_K_M.gguf \
-p "add error handling to src/main.rs"
```

```
ante update
# One-off update from a different channel
ante update --channel nightly
# Roll back or pin to an exact release
ante update --version v0.preview.71
```

**Zero vendor lock-in**: bring your own API key, subscription, or local model. Switch between 12+ providers freely. No account required, not even with us.**Multi-agent orchestration**: spawn sub-agents and coordinate complex tasks across independent, decentralized, and centralized architectures. See the patterns →**Channel integrations**: run Ante as a Slack or Discord bot with`ante gateway`

.**Extensible**: custom skills, sub-agents, MCP, and persistent memory across sessions.

Ante works with 12+ providers out of the box:

| Provider | Example Models |
|---|---|
| Anthropic | Claude Sonnet 4.5, Opus 4.6 |
| OpenAI | GPT-5 family |
| Google Gemini | Gemini 3 family |
| Grok (xAI) | Grok 4 |
| Open Router | Multiple providers |
| Local (GGUF) | Any GGUF model via built-in llama.cpp |
| ...and more | Vertex AI, Zai, Antix, OpenAI-compatible |

Configure providers via environment variables (`ANTHROPIC_API_KEY`

, `OPENAI_API_KEY`

, etc.) or OAuth. Add custom providers in `~/.ante/catalog.json`

.

We open sourced what really matters in the age of agentic coding, all under Apache 2.0:

**Detailed documentation, the descriptive truth.**`docs-site/`

is the source for docs.antigma.ai: a precise description of what the harness does and how to drive it.**The protocol, the algorithm of the core.**`crates/protocol-shape`

defines the schema and wire messages spoken by`ante serve`

;`crates/agent-sdk`

is the Rust SDK and client for building against agent runtimes.**The eval pipeline, constraint and continuous improvement.**`ante-harbor/`

is the Harbor agent adapter behind our Terminal-Bench results: use it to reproduce any run at antigma.ai/eval.`CHANGELOG.md`

records the improvement, release by release.

The core harness itself is developed in a private repository during the alpha and ships as a prebuilt binary via releases. Core libraries from it are included here progressively as they stabilize; `crates/exec`

, standalone process execution, is the first.

The protocol surface maps to Ante's client-daemon architecture:

```
┌─────────────────────────────────────────────────────────────┐
│ Clients │
│ │
│ ┌───────────┐ ┌───────────┐ ┌────────────────────┐ │
│ │ TUI │ │ Headless │ │ ante serve │ │
│ │ (ante) │ │ (ante -p) │ │ (stdio / ws) │ │
│ └─────┬─────┘ └─────┬─────┘ └─────────┬──────────┘ │
└─────────┼────────────────┼─────────────────────┼────────────┘
│ │ │
▼ ▼ ▼
┌─────────────────────────────────────────────────────────────┐
│ Daemon │
│ │
│ Session ──▶ Turn ──▶ Step │
│ │
│ ┌──────────┐ ┌──────────────┐ ┌───────────────────┐ │
│ │ Tools │ │ Permission │ │ Skills / Agents │ │
│ └──────────┘ └──────────────┘ └───────────────────┘ │
└────────────────────────┬────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ LLM Providers │
│ │
│ Anthropic · OpenAI · Gemini · Grok · Open Router · Local │
└─────────────────────────────────────────────────────────────┘
```



We care about the harness, not the model or the prompts.

Documentation is the new source code.

Ante is designed for **cellular-native** agents: like cells in an organism, tiny, expendable, massively replicated. That thesis is why the three headline claims exist. A cell-scale agent must be *verified* (reliability compounds at scale), *tiny* (every byte is multiplied by thousands), and *self-contained* (no runtime to install, no service to phone home to). Read more in our philosophy and agent organization patterns.

The name is the answer: **An**other **Te**rminal agent, and *ante*, the stake you put on the table to play. Ante is fast, lightweight, and the only terminal agent with native local inference built in. We believe a self-contained agent core that self-organizes is the foundation of the coming agent economy.

**How is Ante different from other agents?**

Ante has most of the features you expect from agents like Claude Code or Codex: multi-agents, skills, MCP, persistent memory. The difference is the build philosophy.

- Built from scratch in Rust. Core components like
`Grep`

(fully rebuilt and customized) and`git`

are embedded in the same ~15MB binary and run in the same process at runtime, so nothing is shelled out and no resources leak. Most similar projects ship on Node.js or CPython and carry an order-of-magnitude larger footprint. - Local inference is built in: the engine is a pinned, managed version of llama.cpp, so a local GGUF model is all Ante needs to run without any provider. To study how such an engine works, see nanochat-rs, our toy version.
- No vendor lock-in, not even to ourselves: no account needed, reuse your existing API credentials. An opt-in, fully integrated server-side experience lives at antix.antigma.ai.
- Every claim is backed by public, reproducible benchmarks of the exact builds we ship: antigma.ai/eval.

Beyond the footprint it comes down to agent architecture, and ultimately to *who* is building it and with what philosophy. Anyone can fork a binary; taste and engineering rigor don't copy. Those differences leak into every detail of the product.

**Why care about runtime optimization like memory and I/O if model inference is usually the biggest bottleneck?**

For one-on-one agent interactions, runtime overhead like memory usage and I/O is often less important than model inference.

But our vision is much bigger: millions of agents self-organizing and communicating at massive scale. At that point, even small inefficiencies get multiplied millions or billions of times, so runtime optimization becomes economically significant.

**Can I run Ante completely offline?**

Yes. Ante has a built-in llama.cpp engine that runs GGUF models locally. It handles engine installation, model discovery, and memory management automatically. No API keys or internet connection required.

**Can I use my own custom models or providers?**

Yes. Create a `~/.ante/catalog.json`

file to add or override providers and models with custom endpoints, API keys, and configurations. Any OpenAI-compatible API works.

**What is the **`ante serve`

mode for?

`ante serve`

mode for?Server mode runs Ante as a long-lived daemon that communicates over a structured JSONL protocol. It's ideal for building editor plugins, web UIs, and custom integrations on top of Ante.

Full documentation is available at docs.antigma.ai.

Source code in this repository (including the SDK and protocol crates) is licensed under the Apache License 2.0.

The prebuilt `ante`

binary is free to use — including commercially — during
the alpha preview under the Binary Preview Terms. The core
harness is currently developed in a private repository and shipped as a
binary; the SDK and protocol surface you build against here will remain
permissively licensed.