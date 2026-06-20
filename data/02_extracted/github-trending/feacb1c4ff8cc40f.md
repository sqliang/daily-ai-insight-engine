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
tldr: trycua/cua 是一个开源的计算机使用代理框架，提供沙箱、代理驱动和基准测试完整工具链
objective_summary: trycua/cua 发布了计算机使用代理全栈工具集，包含后台桌面驱动（cua-driver）、多平台沙箱 SDK（cua-sandbox）、代理框架（cua-agent）和基准测试（cua-bench），支持通过
  MCP 协议集成到 AI 编码工具中。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - trycua
  technologies:
  - MCP
  - QEMU
  - Virtualization.Framework
  key_people: []
key_logic_flow:
- trycua/cua 项目发布了计算机使用代理的完整工具链，包括 cua-driver（后台桌面驱动）、cua-agent（代理框架）、cua-sandbox（沙箱
  SDK）、cua-bench（基准测试）和 lume（VM 管理工具）。
- cua-driver 可在 macOS、Windows 和 Linux 后台操作桌面应用，不抢占用户光标焦点，支持作为 MCP 服务器集成到 Claude Code、Cursor
  等 AI 编码工具中。
- cua-sandbox 提供统一的 Python API，支持 Linux 容器/VM、macOS、Windows 和 Android 等多种运行环境，可通过
  QEMU 本地运行或 cua.ai 云端运行。
- cua-bench 支持 OSWorld、ScreenSpot、Windows Arena 等基准测试，可导出代理执行轨迹用于模型训练和评估。
- Lume 基于 Apple Virtualization.Framework 在 Apple Silicon 上创建和管理 macOS/Linux VM，提供接近原生的性能。
- 项目采用 MIT 许可证，部分组件使用 Kasm（MIT）、OmniParser（CC-BY-4.0）和 Ultralytics（AGPL-3.0）等第三方许可证。
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