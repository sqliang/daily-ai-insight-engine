---
title: trycua/cua
source: https://github.com/trycua/cua
author: []
published: ''
created: '2026-06-16'
description: 'Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs,
  and benchmarks to train and evaluate AI agents that can control full desktops (macOS,
  Linux, Windows). Build, benchmark, and deploy agents that use computers Choose Your
  Path Building your own agent? Start with Cua · Giving a coding agent a computer?
  Cua Drivers · Evaluating or training models? Cua Bench · Need macOS VMs? Lume Cua
  Drivers - Background computer-use on macOS and Windows, with Linux pre-release Drive
  native desktop apps in the background. Agents click, type, and verify without stealing
  the cursor or focus. Use the same CLI and MCP server on macOS and Windows from Claude
  Code, Cursor, Codex, OpenClaw, and custom clients. Linux support is available as
  a pre-release backend while platform testing is still in progress. macOS / Linux
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
  Windows (PowerShell) irm https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.ps1
  | iex Then wire it into Claude Code as an MCP server and your agent can drive the
  desktop in the background: claude mcp add --transport stdio cua-driver -- cua-driver
  mcp Full tool reference, architecture notes, and the optional agent skill pack live
  here: libs/cua-driver/README.md. Cua - Agent-Ready Sandboxes for Any OS Build agents
  that see screens, click buttons, and complete tasks autonomously. One API for any
  VM or container image — cloud or local. pip install cua # Requires Python 3.11 or
  later from cua import Sandbox, Image # Same API regardless of OS or runtime async
  with Sandbox.ephemeral(Image.linux()) as sb: # or .macos() .windows() .android()
  result = await sb.shell.run("echo hello") screenshot = await sb.screenshot() await
  sb.mouse.click(100, 200) await sb.keyboard.type("Hello from Cua!") await sb.mobile.gesture((100,
  500), (100, 200)) # multi-touch gestures Linux container Linux VM macOS Windows
  Android BYOI (.qcow2, .iso) Cloud (cua.ai) ✅ ✅ ✅ ✅ ✅ 🔜 soon Local (QEMU) ✅ ✅ ✅ ✅
  ✅ ✅ Get Started | Examples | API Reference Cua-Bench - Benchmarks & RL Environments
  Evaluate computer-use agents on OSWorld, ScreenSpot, Windows Arena, and custom tasks.
  Export trajectories for training. # Clone, install, and create base image git clone
  https://github.com/trycua/cua && cd cua/cua-bench uv tool install -e . && cb image
  create linux-docker # Run benchmark with agent cb run dataset datasets/cua-bench-basic
  --agent cua-agent --max-parallel 4 Get Started | Partner With Us | Registry | CLI
  Reference Lume - macOS Virtualization Create and manage macOS/Linux VMs with near-native
  performance on Apple Silicon using Apple''s Virtualization.Framework. # Install
  Lume /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
  # Pull & start a macOS VM lume run macos-sequoia-vanilla:latest Get Started | FAQ
  | CLI Reference Packages Package Description cua-driver Background computer-use
  agent for macOS, Windows, and Linux cua-agent AI agent framework for computer-use
  tasks cua-sandbox SDK for creating and controlling sandboxes cua-computer-server
  Driver for UI interactions and code execution in sandboxes cua-bench Benchmarks
  and RL environments for computer-use lume macOS/Linux VM management on Apple Silicon
  lumier Docker-compatible interface for Lume VMs Resources Documentation — Guides,
  examples, and API reference Blog — Tutorials, updates, and research Discord — Community
  support and discussions GitHub Issues — Bug reports and feature requests Contributing
  We welcome contributions! See our Contributing Guidelines for details. License MIT
  License — see LICENSE for details. Third-party components have their own licenses:
  Kasm (MIT) OmniParser (CC-BY-4.0) Optional cua-agent[omni] includes ultralytics
  (AGPL-3.0) Trademarks Apple, macOS, Ubuntu, Canonical, and Microsoft are trademarks
  of their respective owners. This project is not affiliated with or endorsed by these
  companies. Thank you to all our GitHub Sponsors!'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: feacb1c4ff8cc40f
source_type: community_discussion
tldr: trycua/cua 是一个开源计算机操作代理框架，支持通过单一 API 在 macOS、Windows、Linux 和 Android 上控制桌面应用，提供
  CLI、MCP 服务器、Python SDK 和沙箱环境。
objective_summary: trycua/cua 发布了计算机操作代理框架，包含 cua-driver、cua-agent、cua-sandbox、cua-bench
  和 lume 等多个子项目。该项目支持在后台驱动桌面应用（点击、输入、验证），不抢占光标焦点，可通过 CLI 和 MCP 服务器从 Claude Code、Cursor、Codex
  等客户端调用。Cua 提供 Python SDK（pip install cua），支持 Linux 容器、Linux VM、macOS、Windows 和 Android
  环境，同时包含计算机使用基准测试和 macOS/Linux VM 管理工具。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - trycua
  technologies:
  - MCP
  - QEMU
  - Apple Virtualization.Framework
  key_people: []
key_logic_flow:
- Cua 是一个开源计算机操作代理框架，提供统一 API 用于在多种操作系统上控制桌面应用。
- cua-driver 允许代理在后台执行点击、输入和验证操作，不抢占用户光标焦点，支持 macOS、Windows 和 Linux。
- cua-sandbox 提供 Python SDK（通过 pip install cua 安装），支持 Linux 容器、Linux VM、macOS、Windows
  和 Android 环境。
- cua-bench 提供计算机使用代理的基准测试和强化学习环境，支持 OSWorld、ScreenSpot、Windows Arena 等数据集。
- lume 是基于 Apple Virtualization.Framework 的 macOS/Linux VM 管理工具，在 Apple Silicon 上提供接近原生性能。
- 该项目使用 MIT 许可证，依赖的 OmniParser 使用 CC-BY-4.0 许可证，可选组件 cua-agent[omni] 包含 AGPL-3.0 的
  ultralytics。
extract_result: success
object_mentions:
- object_type: project
  name: trycua/cua
  canonical_name: trycua/cua
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cua 是一个开源计算机操作代理框架，提供 Python SDK 和统一 API 用于控制桌面应用。
  - 该项目包含 cua-driver、cua-agent、cua-sandbox、cua-bench 和 lume 等多个子项目。
  - Cua 支持通过 MCP 服务器从 Claude Code、Cursor 和 Codex 等客户端调用。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-driver
  canonical_name: trycua/cua/cua-driver
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-driver 是 Cua 的桌面驱动组件，允许代理在后台驱动 macOS、Windows 和 Linux 桌面应用。
  - cua-driver 支持通过 MCP 服务器集成到 Claude Code、Cursor 和 Codex 等客户端中。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-agent
  canonical_name: trycua/cua/cua-agent
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-agent 是 Cua 中用于计算机操作任务的 AI 代理框架。
  - 可选组件 cua-agent[omni] 包含 ultralytics，使用 AGPL-3.0 许可证。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-sandbox
  canonical_name: trycua/cua/cua-sandbox
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-sandbox 是 Cua 的沙箱 SDK，用于创建和控制虚拟机或容器环境。
  - 开发者可通过 pip install cua 安装后使用 Sandbox.ephemeral() 创建临时沙箱实例。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-bench
  canonical_name: trycua/cua/cua-bench
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - cua-bench 用于在 OSWorld、ScreenSpot 和 Windows Arena 等数据集上评估计算机操作代理。
  - cua-bench 支持导出轨迹数据用于训练，并通过 uv tool install 安装后使用 cb 命令运行。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: lume
  canonical_name: trycua/cua/lume
  url: https://github.com/trycua/cua
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - lume 是基于 Apple Virtualization.Framework 的 VM 管理工具，在 Apple Silicon 上提供接近原生性能。
  - lume 支持创建和管理 macOS 和 Linux 虚拟机，可通过 lume run 命令启动。
  article_id: feacb1c4ff8cc40f
- object_type: product
  name: cua.ai
  canonical_name: cua.ai
  url: https://cua.ai
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - cua.ai 是 Cua 的云服务，支持 Linux 容器、Linux VM、macOS、Windows 和 Android 环境。
  - Cua 提供本地（QEMU）和云（cua.ai）两种运行方式，本地支持 BYOI 自定义镜像。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: cua-computer-server
  canonical_name: trycua/cua/cua-computer-server
  url: https://github.com/trycua/cua
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - cua-computer-server 是 Cua 中负责 UI 交互和沙箱内代码执行的驱动组件。
  article_id: feacb1c4ff8cc40f
- object_type: project
  name: lumier
  canonical_name: trycua/cua/lumier
  url: https://github.com/trycua/cua
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - lumier 是 Cua 生态中的项目，为 Lume VM 提供 Docker 兼容接口。
  article_id: feacb1c4ff8cc40f
---

**Building your own agent?** Start with Cua ·
**Giving a coding agent a computer?** Cua Drivers ·
**Evaluating or training models?** Cua Bench ·
**Need macOS VMs?** Lume

Drive native desktop apps **in the background**. Agents click, type, and verify without stealing the cursor or focus. Use the same CLI and MCP server on macOS and Windows from Claude Code, Cursor, Codex, OpenClaw, and custom clients. Linux support is available as a pre-release backend while platform testing is still in progress.

**macOS / Linux**

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"`

**Windows (PowerShell)**

`irm https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.ps1 | iex`

Then wire it into Claude Code as an MCP server and your agent can drive the desktop in the background:

`claude mcp add --transport stdio cua-driver -- cua-driver mcp`

Full tool reference, architecture notes, and the optional agent skill pack live here: `libs/cua-driver/README.md`

.

Build agents that see screens, click buttons, and complete tasks autonomously. One API for any VM or container image — cloud or local.

`pip install cua`

```
# Requires Python 3.11 or later
from cua import Sandbox, Image
# Same API regardless of OS or runtime
async with Sandbox.ephemeral(Image.linux()) as sb: # or .macos() .windows() .android()
result = await sb.shell.run("echo hello")
screenshot = await sb.screenshot()
await sb.mouse.click(100, 200)
await sb.keyboard.type("Hello from Cua!")
await sb.mobile.gesture((100, 500), (100, 200)) # multi-touch gestures
```

| Linux container | Linux VM | macOS | Windows | Android | BYOI (.qcow2, .iso) | |
|---|---|---|---|---|---|---|
Cloud (cua.ai) |
✅ | ✅ | ✅ | ✅ | ✅ | 🔜 soon |
Local (QEMU) |
✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Get Started** | **Examples** | **API Reference**

Evaluate computer-use agents on OSWorld, ScreenSpot, Windows Arena, and custom tasks. Export trajectories for training.

```
# Clone, install, and create base image
git clone https://github.com/trycua/cua && cd cua/cua-bench
uv tool install -e . && cb image create linux-docker
# Run benchmark with agent
cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4
```

**Get Started** | **Partner With Us** | **Registry** | **CLI Reference**

Create and manage macOS/Linux VMs with near-native performance on Apple Silicon using Apple's Virtualization.Framework.

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

**Get Started** | **FAQ** | **CLI Reference**

| Package | Description |
|---|---|
| cua-driver | Background computer-use agent for macOS, Windows, and Linux |
| cua-agent | AI agent framework for computer-use tasks |
| cua-sandbox | SDK for creating and controlling sandboxes |
| cua-computer-server | Driver for UI interactions and code execution in sandboxes |
| cua-bench | Benchmarks and RL environments for computer-use |
| lume | macOS/Linux VM management on Apple Silicon |
| lumier | Docker-compatible interface for Lume VMs |

- Documentation — Guides, examples, and API reference
- Blog — Tutorials, updates, and research
- Discord — Community support and discussions
- GitHub Issues — Bug reports and feature requests

We welcome contributions! See our Contributing Guidelines for details.

MIT License — see LICENSE for details.

Third-party components have their own licenses:

- Kasm (MIT)
- OmniParser (CC-BY-4.0)
- Optional
`cua-agent[omni]`

includes ultralytics (AGPL-3.0)

Apple, macOS, Ubuntu, Canonical, and Microsoft are trademarks of their respective owners. This project is not affiliated with or endorsed by these companies.