---
title: NousResearch/hermes-agent
source: https://github.com/NousResearch/hermes-agent
author: []
published: ''
created: '2026-06-08'
description: 'The agent that grows with you Hermes Agent ☤ The self-improving AI agent
  built by Nous Research. It''s the only agent with a built-in learning loop — it
  creates skills from experience, improves them during use, nudges itself to persist
  knowledge, searches its own past conversations, and builds a deepening model of
  who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure
  that costs nearly nothing when idle. It''s not tied to your laptop — talk to it
  from Telegram while it works on a cloud VM. Use any model you want — Nous Portal,
  OpenRouter (200+ models), NovitaAI (AI-native cloud for Model API, Agent Sandbox,
  and GPU Cloud), NVIDIA NIM (Nemotron), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax,
  Hugging Face, OpenAI, or your own endpoint. Switch with hermes model — no code changes,
  no lock-in. A real terminal interface Full TUI with multiline editing, slash-command
  autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.
  Lives where you do Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from
  a single gateway process. Voice memo transcription, cross-platform conversation
  continuity. A closed learning loop Agent-curated memory with periodic nudges. Autonomous
  skill creation after complex tasks. Skills self-improve during use. FTS5 session
  search with LLM summarization for cross-session recall. Honcho dialectic user modeling.
  Compatible with the agentskills.io open standard. Scheduled automations Built-in
  cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly
  audits — all in natural language, running unattended. Delegates and parallelizes
  Spawn isolated subagents for parallel workstreams. Write Python scripts that call
  tools via RPC, collapsing multi-step pipelines into zero-context-cost turns. Runs
  anywhere, not just your laptop Six terminal backends — local, Docker, SSH, Singularity,
  Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent''s
  environment hibernates when idle and wakes on demand, costing nearly nothing between
  sessions. Run it on a $5 VPS or a GPU cluster. Research-ready Batch trajectory generation,
  trajectory compression for training the next generation of tool-calling models.
  Quick Install Linux, macOS, WSL2, Termux curl -fsSL https://hermes-agent.nousresearch.com/install.sh
  | bash Windows (native, PowerShell) Heads up: Native Windows runs Hermes without
  WSL — CLI, gateway, TUI, and tools all work natively. If you''d rather use WSL2,
  the Linux/macOS one-liner above works there too. Found a bug? Please file issues.
  Run this in PowerShell: iex (irm https://hermes-agent.nousresearch.com/install.ps1)
  The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, and
  a portable Git Bash (MinGit, unpacked to %LOCALAPPDATA%\hermes\git — no admin required,
  completely isolated from any system Git install). Hermes uses this bundled Git Bash
  to run shell commands. If you already have Git installed, the installer detects
  it and uses that instead. Otherwise a ~45MB MinGit download is all you need — it
  won''t touch or interfere with any system Git. Android / Termux: The tested manual
  path is documented in the Termux guide. On Termux, Hermes installs a curated .[termux]
  extra because the full .[all] extra currently pulls Android-incompatible voice dependencies.
  Windows: Native Windows is fully supported — the PowerShell one-liner above installs
  everything. If you''d rather use WSL2, the Linux command works there too. Native
  Windows install lives under %LOCALAPPDATA%\hermes; WSL2 installs under ~/.hermes
  as on Linux. The only Hermes feature that currently needs WSL2 specifically is the
  browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway
  both run natively). After installation: source ~/.bashrc # reload shell (or: source
  ~/.zshrc) hermes # start chatting! Getting Started hermes # Interactive CLI — start
  a conversation hermes model # Choose your LLM provider and model hermes tools #
  Configure which tools are enabled hermes config set # Set individual config values
  hermes gateway # Start the messaging gateway (Telegram, Discord, etc.) hermes setup
  # Run the full setup wizard (configures everything at once) hermes claw migrate
  # Migrate from OpenClaw (if coming from OpenClaw) hermes update # Update to the
  latest version hermes doctor # Diagnose any issues 📖 Full documentation → Skip the
  API-key collection — Nous Portal Hermes works with whatever provider you want —
  that''s not changing. But if you''d rather not collect five separate API keys for
  the model, web search, image generation, TTS, and a cloud browser, Nous Portal covers
  all of them under one subscription: 300+ models — pick any of them with /model <name>
  Tool Gateway — web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI),
  cloud browser (Browser Use), all routed through your sub. No extra accounts. One
  command from a fresh install: hermes setup --portal That logs you in via OAuth,
  sets Nous as your provider, and turns on the Tool Gateway. Check what''s wired up
  any time with hermes portal info. Full details on the Tool Gateway docs page. You
  can still bring your own keys per-tool whenever you want — the gateway is per-backend,
  not all-or-nothing. CLI vs Messaging Quick Reference Hermes has two entry points:
  start the terminal UI with hermes, or run the gateway and talk to it from Telegram,
  Discord, Slack, WhatsApp, Signal, or Email. Once you''re in a conversation, many
  slash commands are shared across both interfaces. Action CLI Messaging platforms
  Start chatting hermes Run hermes gateway setup + hermes gateway start, then send
  the bot a message Start fresh conversation /new or /reset /new or /reset Change
  model /model [provider:model] /model [provider:model] Set a personality /personality
  [name] /personality [name] Retry or undo the last turn /retry, /undo /retry, /undo
  Compress context / check usage /compress, /usage, /insights [--days N] /compress,
  /usage, /insights [days] Browse skills /skills or /<skill-name> /<skill-name> Interrupt
  current work Ctrl+C or send a new message /stop or send a new message Platform-specific
  status /platforms /status, /sethome For the full command lists, see the CLI guide
  and the Messaging Gateway guide. Documentation All documentation lives at hermes-agent.nousresearch.com/docs:
  Section What''s Covered Quickstart Install → setup → first conversation in 2 minutes
  CLI Usage Commands, keybindings, personalities, sessions Configuration Config file,
  providers, models, all options Messaging Gateway Telegram, Discord, Slack, WhatsApp,
  Signal, Home Assistant Security Command approval, DM pairing, container isolation
  Tools & Toolsets 40+ tools, toolset system, terminal backends Skills System Procedural
  memory, Skills Hub, creating skills Memory Persistent memory, user profiles, best
  practices MCP Integration Connect any MCP server for extended capabilities Cron
  Scheduling Scheduled tasks with platform delivery Context Files Project context
  that shapes every conversation Architecture Project structure, agent loop, key classes
  Contributing Development setup, PR process, code style CLI Reference All commands
  and flags Environment Variables Complete env var reference Migrating from OpenClaw
  If you''re coming from OpenClaw, Hermes can automatically import your settings,
  memories, skills, and API keys. During first-time setup: The setup wizard (hermes
  setup) automatically detects ~/.openclaw and offers to migrate before configuration
  begins. Anytime after install: hermes claw migrate # Interactive migration (full
  preset) hermes claw migrate --dry-run # Preview what would be migrated hermes claw
  migrate --preset user-data # Migrate without secrets hermes claw migrate --overwrite
  # Overwrite existing conflicts What gets imported: SOUL.md — persona file Memories
  — MEMORY.md and USER.md entries Skills — user-created skills → ~/.hermes/skills/openclaw-imports/
  Command allowlist — approval patterns Messaging settings — platform configs, allowed
  users, working directory API keys — allowlisted secrets (Telegram, OpenRouter, OpenAI,
  Anthropic, ElevenLabs) TTS assets — workspace audio files Workspace instructions
  — AGENTS.md (with --workspace-target) See hermes claw migrate --help for all options,
  or use the openclaw-migration skill for an interactive agent-guided migration with
  dry-run previews. Contributing We welcome contributions! See the Contributing Guide
  for development setup, code style, and PR process. Quick start for contributors
  — clone and go with setup-hermes.sh: git clone https://github.com/NousResearch/hermes-agent.git
  cd hermes-agent ./setup-hermes.sh # installs uv, creates venv, installs .[all],
  symlinks ~/.local/bin/hermes ./hermes # auto-detects the venv, no need to `source`
  first Manual path (equivalent to the above): curl -LsSf https://astral.sh/uv/install.sh
  | sh uv venv .venv --python 3.11 source .venv/bin/activate uv pip install -e ".[all,dev]"
  scripts/run_tests.sh Community 💬 Discord 📚 Skills Hub 🐛 Issues 🔌 computer-use-linux
  — Linux desktop-control MCP server for Hermes and other MCP hosts, with AT-SPI accessibility
  trees, Wayland/X11 input, screenshots, and compositor window targeting. 🔌 HermesClaw
  — Community WeChat bridge: Run Hermes Agent and OpenClaw on the same WeChat account.
  License MIT — see LICENSE. Built by Nous Research.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ec2b8bd43eefd65f
source_type: community_discussion
tldr: Nous Research 发布 Hermes Agent，一款自带学习循环的自我进化 AI 代理
objective_summary: Nous Research 发布了开源 AI 代理 Hermes Agent，具有内置学习循环、自主技能创建、跨会话记忆和用户画像建模等能力。支持
  300+ 模型、多平台网关（Telegram/Discord/Slack 等）和六种终端后端，可在 $5 VPS 到 GPU 集群上运行，MIT
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Nous Research
  - OpenAI
  - Hugging Face
  - NVIDIA
  - Xiaomi
  - MiniMax
  - Modal
  - Daytona
  - NovitaAI
  technologies:
  - MCP
  - FTS5
  - TTS
  - TUI
  - RPC
  key_people: []
key_logic_flow:
- Nous Research 发布了 Hermes Agent，这是第一款自带闭环学习循环的 AI 代理，能够从经验中自主创建技能并在使用中自我改进。
- Hermes Agent 通过单一网关进程同时支持 Telegram、Discord、Slack、WhatsApp、Signal 和 CLI 六种交互平台，并具备语音备忘录转录和跨平台对话连续性能力。
- Hermes Agent 支持 300 多种模型，用户可通过 Nous Portal、OpenRouter、OpenAI、Hugging Face 等任意提供商切换，使用
  hermes model 命令无需修改代码。
- Hermes Agent 内置定时自动化系统（cron），支持自然语言定义日报、备份、审计等定时任务，无人值守运行。
- Hermes Agent 提供六种终端后端——本地、Docker、SSH、Singularity、Modal 和 Daytona，可在低至 $5 的 VPS 到
  GPU 集群上运行，其中 Modal 和 Daytona 支持无服务器持久化（空闲时休眠）。
- Hermes Agent 支持从 OpenClaw 一键迁移设置、记忆、技能和 API 密钥，并兼容 agentskills.io 开放标准。
extract_result: success
---

**The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — Nous Portal, OpenRouter (200+ models), NovitaAI (AI-native cloud for Model API, Agent Sandbox, and GPU Cloud), NVIDIA NIM (Nemotron), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, or your own endpoint. Switch with `hermes model`

— no code changes, no lock-in.

A real terminal interface | Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output. |
Lives where you do | Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity. |
A closed learning loop | Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling. Compatible with the agentskills.io open standard. |
Scheduled automations | Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended. |
Delegates and parallelizes | Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns. |
Runs anywhere, not just your laptop | Six terminal backends — local, Docker, SSH, Singularity, Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster. |
Research-ready | Batch trajectory generation, trajectory compression for training the next generation of tool-calling models. |

`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`


Heads up:Native Windows runs Hermes without WSL — CLI, gateway, TUI, and tools all work natively. If you'd rather use WSL2, the Linux/macOS one-liner above works there too. Found a bug? Please file issues.

Run this in PowerShell:

`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`

The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, **and a portable Git Bash** (MinGit, unpacked to `%LOCALAPPDATA%\hermes\git`

— no admin required, completely isolated from any system Git install). Hermes uses this bundled Git Bash to run shell commands.

If you already have Git installed, the installer detects it and uses that instead. Otherwise a ~45MB MinGit download is all you need — it won't touch or interfere with any system Git.


Android / Termux:The tested manual path is documented in the Termux guide. On Termux, Hermes installs a curated`.[termux]`

extra because the full`.[all]`

extra currently pulls Android-incompatible voice dependencies.

Windows:Native Windows is fully supported — the PowerShell one-liner above installs everything. If you'd rather use WSL2, the Linux command works there too. Native Windows install lives under`%LOCALAPPDATA%\hermes`

; WSL2 installs under`~/.hermes`

as on Linux. The only Hermes feature that currently needs WSL2 specifically is the browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway both run natively).

After installation:

```
source ~/.bashrc # reload shell (or: source ~/.zshrc)
hermes # start chatting!
```

```
hermes # Interactive CLI — start a conversation
hermes model # Choose your LLM provider and model
hermes tools # Configure which tools are enabled
hermes config set # Set individual config values
hermes gateway # Start the messaging gateway (Telegram, Discord, etc.)
hermes setup # Run the full setup wizard (configures everything at once)
hermes claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes update # Update to the latest version
hermes doctor # Diagnose any issues
```

Hermes works with whatever provider you want — that's not changing. But if you'd rather not collect five separate API keys for the model, web search, image generation, TTS, and a cloud browser, **Nous Portal** covers all of them under one subscription:

**300+ models**— pick any of them with`/model <name>`

**Tool Gateway**— web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI), cloud browser (Browser Use), all routed through your sub. No extra accounts.

One command from a fresh install:

`hermes setup --portal`

That logs you in via OAuth, sets Nous as your provider, and turns on the Tool Gateway. Check what's wired up any time with `hermes portal info`

. Full details on the Tool Gateway docs page.

You can still bring your own keys per-tool whenever you want — the gateway is per-backend, not all-or-nothing.

Hermes has two entry points: start the terminal UI with `hermes`

, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action | CLI | Messaging platforms |
|---|---|---|
| Start chatting | `hermes` |
Run `hermes gateway setup` + `hermes gateway start` , then send the bot a message |
| Start fresh conversation | `/new` or `/reset` |
`/new` or `/reset` |
| Change model | `/model [provider:model]` |
`/model [provider:model]` |
| Set a personality | `/personality [name]` |
`/personality [name]` |
| Retry or undo the last turn | `/retry` , `/undo` |
`/retry` , `/undo` |
| Compress context / check usage | `/compress` , `/usage` , `/insights [--days N]` |
`/compress` , `/usage` , `/insights [days]` |
| Browse skills | `/skills` or `/<skill-name>` |
`/<skill-name>` |
| Interrupt current work | `Ctrl+C` or send a new message |
`/stop` or send a new message |
| Platform-specific status | `/platforms` |
`/status` , `/sethome` |

For the full command lists, see the CLI guide and the Messaging Gateway guide.

All documentation lives at **hermes-agent.nousresearch.com/docs**:

| Section | What's Covered |
|---|---|
| Quickstart | Install → setup → first conversation in 2 minutes |
| CLI Usage | Commands, keybindings, personalities, sessions |
| Configuration | Config file, providers, models, all options |
| Messaging Gateway | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| Security | Command approval, DM pairing, container isolation |
| Tools & Toolsets | 40+ tools, toolset system, terminal backends |
| Skills System | Procedural memory, Skills Hub, creating skills |
| Memory | Persistent memory, user profiles, best practices |
| MCP Integration | Connect any MCP server for extended capabilities |
| Cron Scheduling | Scheduled tasks with platform delivery |
| Context Files | Project context that shapes every conversation |
| Architecture | Project structure, agent loop, key classes |
| Contributing | Development setup, PR process, code style |
| CLI Reference | All commands and flags |
| Environment Variables | Complete env var reference |

If you're coming from OpenClaw, Hermes can automatically import your settings, memories, skills, and API keys.

**During first-time setup:** The setup wizard (`hermes setup`

) automatically detects `~/.openclaw`

and offers to migrate before configuration begins.

**Anytime after install:**

```
hermes claw migrate # Interactive migration (full preset)
hermes claw migrate --dry-run # Preview what would be migrated
hermes claw migrate --preset user-data # Migrate without secrets
hermes claw migrate --overwrite # Overwrite existing conflicts
```

What gets imported:

**SOUL.md**— persona file**Memories**— MEMORY.md and USER.md entries**Skills**— user-created skills →`~/.hermes/skills/openclaw-imports/`

**Command allowlist**— approval patterns**Messaging settings**— platform configs, allowed users, working directory**API keys**— allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)**TTS assets**— workspace audio files**Workspace instructions**— AGENTS.md (with`--workspace-target`

)

See `hermes claw migrate --help`

for all options, or use the `openclaw-migration`

skill for an interactive agent-guided migration with dry-run previews.

We welcome contributions! See the Contributing Guide for development setup, code style, and PR process.

Quick start for contributors — clone and go with `setup-hermes.sh`

:

```
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
./setup-hermes.sh # installs uv, creates venv, installs .[all], symlinks ~/.local/bin/hermes
./hermes # auto-detects the venv, no need to `source` first
```

Manual path (equivalent to the above):

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

- 💬 Discord
- 📚 Skills Hub
- 🐛 Issues
- 🔌 computer-use-linux — Linux desktop-control MCP server for Hermes and other MCP hosts, with AT-SPI accessibility trees, Wayland/X11 input, screenshots, and compositor window targeting.
- 🔌 HermesClaw — Community WeChat bridge: Run Hermes Agent and OpenClaw on the same WeChat account.

MIT — see LICENSE.

Built by Nous Research.