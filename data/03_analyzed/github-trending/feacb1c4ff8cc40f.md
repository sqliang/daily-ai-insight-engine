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
impact_score:
  score: 6.8
  reason: 该项目的评分依据如下：这是一个开源计算机使用代理全栈工具链的发布，整合了沙箱、驱动、代理框架和基准测试四大模块，并通过MCP协议与主流AI编码工具（Claude
    Code、Cursor等）打通。其价值在于将此前分散在各AI实验室的计算机使用代理能力标准化、开源化，降低了开发者的准入门槛。但该领域仍处于早期阶段，项目本身是现有技术（QEMU、Apple
    Virtualization.Framework）的工程化整合而非全新的理论突破，且社区尚未形成大规模采用。综合评估：改变局部竞争格局，但尚未达到行业范式转移级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MCP协议集成与不抢占焦点的后台桌面操作能力，可直接接入Claude Code和Cursor等AI编码工具
hype_assessment:
  level: low
  reason: 项目README采用技术驱动的客观描述方式，详细列出了各模块功能、API示例、支持平台和限制条件（如Linux标注为pre-release、第三方组件许可证声明），没有使用'颠覆''革命性'等PR滥用词汇，宣传水分较低。
information_entropy: high
domain_disruption:
  technical_innovation: 提供了统一的多平台沙箱API抽象层（Linux/Windows/macOS/Android），后台桌面驱动支持不抢占光标焦点运行计算机使用代理，并通过MCP协议将这种能力暴露为AI编码工具的标准工具接口，打通了智能体与桌面应用的桥梁。
  business_model: 开源核心（MIT许可证）+云端执行服务（cua.ai）的双轨商业模式，通过MCP协议生态绑定开发者，将开源社区转化为付费云端沙箱客户，类似GitHub
    Codespaces模式在计算机使用代理领域的迁移。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 计算机使用代理是AI Agent能力的关键基础设施层，trycua/cua是业界首个提供从沙箱(Sandbox)、后台桌面驱动(Driver)、Agent框架到基准测试(Bench)完整开源工具链的项目。核心投资逻辑：1)
    MIT许可证+ MCP协议深度绑定，有望形成'计算机使用代理的默认开源基建'定位，驱动开发者生态网络效应——越多项目基于其构建，切换成本越高，复利效应越强；2)
    后台非抢占式桌面驱动技术（不抢光标/焦点）在技术上构成差异化壁垒，解决了Agent自动化中用户痛点；3) 跨平台一站式API（Linux/macOS/Windows/Android）极大降低集成成本，单一接口即可对接多种运行环境。长期风险在于：项目尚处早期，面临OpenAI
    CUA等闭源方案的生态和品牌竞争，纯开源模式的可商业变现路径（如云服务cua.ai）尚待验证。综合评定7.5分，位于细分赛道基础设施潜力段的上沿，3-5年后若开发者生态形成临界规模则大概率成为行业基石。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- trycua
- Cursor
competitive_casualty:
- OpenAI
- 传统RPA厂商
- 闭源Agent基础设施提供商
market_opportunities:
- 企业级RPA厂商可将cua-driver的背景桌面操控能力集成到现有自动化流程中，实现不抢占光标的无感自动化，显著提升用户体验和部署接受度
- AI编码工具（如Cursor、Claude Code）可通过MCP接入cua-driver，赋予代理操作本地桌面应用的能力，开辟'代码编辑+桌面自动化'的融合产品形态
- cua-bench与沙箱SDK可用于构建计算机使用代理的训练数据生产线，为模型微调和强化学习提供标准化的轨迹数据采集与评估平台
risk_matrix:
  regulatory: 计算机使用代理可操控桌面应用执行任意操作，可能触发各国对自动化软件的安全审查与合规要求（如欧盟AI Act对高风险自动化系统的分类），且涉及屏幕截图传输可能违反数据保护法规
  technological: 依赖QEMU和Apple Virtualization.Framework等虚拟化技术，在Windows/Linux非容器场景下的稳定性和性能有待验证；Lume仅支持Apple
    Silicon，限制了x86 macOS用户的可用性
  competitive: Anthropic Computer Use、OpenAI Operator、Google Mariner等巨头产品在原生能力和生态整合上更具优势；开源替代项目（如Open-Interpreter、CogAgent）可能形成碎片化竞争
  ethical: 屏幕抓取与桌面操控能力可被滥用于自动化攻击、数据窃取或监控；背景操作特性降低了用户感知度，增加了无授权操控的风险；benchmark导出的执行轨迹若包含敏感数据可能引发隐私问题
  additional:
  - 项目采用MIT许可证但部分依赖组件（如Ultralytics使用AGPL-3.0），AGPL的传染性可能对商业集成构成许可合规风险
  - 云服务(cua.ai)与本地运行的混合架构可能导致用户对数据流向和隐私边界产生混淆
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
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