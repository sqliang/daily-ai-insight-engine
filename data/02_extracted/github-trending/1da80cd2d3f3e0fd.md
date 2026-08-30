---
title: NVIDIA-NeMo/Switchyard
source: https://github.com/NVIDIA-NeMo/Switchyard
author: []
published: ''
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
- '2026-08-14'
description: 'Switchyard Switchyard is a Rust proxy and library for LLM traffic. It
  routes requests across providers, translates between OpenAI and Anthropic APIs,
  records operational metrics, and provides typed, composable routing algorithms.
  Why Switchyard? Point a coding agent such as Claude Code or Codex at an open-source
  model. Switchyard translates between the OpenAI Chat, Anthropic Messages, and OpenAI
  Responses formats, so the agent keeps speaking its native API while the request
  is served by vLLM, NVIDIA NIM, Ollama, or any OpenAI-compatible endpoint. The same
  proxy can spread traffic across several models for A/B benchmarking, apply signal-driven
  stage routing, or run a custom algorithm you write yourself. Features Protocol Translation:
  convert between OpenAI Chat, Anthropic Messages, and OpenAI Responses formats Multi-Backend
  Routing: random routing, LLM-as-classifier routing, signal-driven stage-router,
  or your own algorithm Operational Metrics: Prometheus metrics cover requests, errors,
  latency, tokens, and routing overhead Maturity Switchyard is pre-alpha software
  that is evolving rapidly. The API and algorithms are expected to change significantly
  before we reach v1.0. Warning Experimental software. Not for production use. Quick
  Start Choose the launcher path to run Claude Code, Codex CLI, or OpenClaw through
  Switchyard. Choose the server path to run Switchyard as a standalone proxy. Choose
  the library path to embed routing in your own Rust application. Launcher Path Install
  uv if it is not already available, then install the published Switchyard tool: curl
  -LsSf https://astral.sh/uv/install.sh | sh source "$HOME/.local/bin/env" uv tool
  install --python 3.10 "nemo-switchyard[cli]" The coding agent you launch must also
  be installed and on your PATH. This does not install the standalone switchyard-server
  binary; use the Server Path for that. Set an OpenRouter key and launch against the
  packaged deployment: export OPENROUTER_API_KEY="your-openrouter-key" # pragma: allowlist
  secret switchyard launch claude --model switchyard switchyard launch codex --model
  switchyard switchyard launch openclaw --model switchyard To use your own native
  TOML deployment, pass its route ID and configuration: switchyard launch claude --model
  my-route --config routes.toml Server Path Use this path to install and run the standalone
  Rust proxy. Install Rust with Cargo, then install the published binary: cargo install
  --locked switchyard-server switchyard-server --help Cargo builds the release binary
  and installs it into ~/.cargo/bin by default. Create routes.toml using the Getting
  Started guide, then validate it and start the server: export OPENROUTER_API_KEY="your-openrouter-key"
  # pragma: allowlist secret switchyard-server --config routes.toml --dry-run switchyard-server
  --config routes.toml --host 127.0.0.1 --port 4000 Verify the proxy in another terminal:
  curl http://localhost:4000/health For a complete configuration and a test request,
  follow Getting Started. Library Path switchyard-libsy embeds the routing algorithms
  in your own Rust application. It never calls a model itself: an algorithm decides
  which target to use and hands every model call back to you, so it drops into an
  existing proxy, gateway, or agent runtime without owning an HTTP stack. Pair it
  with switchyard-llm-client when you want the calls made for you. [dependencies]
  switchyard-libsy = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" } switchyard-protocol
  = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" } See Getting Started
  for setup and the algorithm list, or the switchyard-libsy crate docs. Routing Strategies
  Strategy Use it when Route type LLM Classifier Request content should decide whether
  a turn needs the weak or strong tier. llm_classifier Stage Router Signals already
  in the conversation, such as tool results and errors, should route most turns without
  an extra model call. stage_router Escalation Router Every turn runs on the weak
  tier first, and a judge reads that answer to decide whether to send the same request
  to the strong tier. llm_classifier with mode = "escalation" Random You need a fixed
  traffic split for A/B tests, baselines, or cost experiments. random A passthrough
  route registers one target under one model ID with no routing decision. See the
  Routing Overview for the common route shape and self-hosted targets. Architecture
  flowchart LR clients["Clients"] switchyard["Switchyard<br/>routing · translation
  · fallback"] backends["Model backends"] clients -->|"OpenAI / Anthropic API"| switchyard
  switchyard -->|"provider-native format"| backends Clients keep their native OpenAI
  or Anthropic API format. Switchyard picks a configured backend, forwards the request
  in that backend''s own format, and translates the response back into the shape the
  client expects. The server accepts OpenAI Chat Completions, OpenAI Responses, and
  Anthropic Messages. Each configured LLM client selects one upstream format. Documentation
  Getting Started: complete launcher and standalone server walkthroughs Core Concepts:
  LLM clients, targets, routes, model IDs, and routing algorithms Routing Overview:
  choose and configure a routing algorithm switchyard-server: server configuration,
  routing algorithms, and metrics switchyard-libsy: embed routing algorithms in a
  Rust application switchyard-protocol: provider-neutral request, response, and streaming
  types switchyard-translation: request, response, and stream translation Community
  Issues: GitHub Issues Code of Conduct: Code of Conduct License Apache 2.0 License.
  Copyright NVIDIA Corporation.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 1da80cd2d3f3e0fd
source_type: community_discussion
tldr: NVIDIA NeMo 开源了 Switchyard：一个用 Rust 编写的 LLM 流量代理与库，可在 OpenAI/Anthropic API 与
  vLLM、NVIDIA NIM、Ollama 等后端之间做协议转换与多后端路由，目前为 pre-alpha 实验软件。
objective_summary: NVIDIA 的 NeMo 团队在 GitHub 上发布了名为 Switchyard 的 Rust 项目，这是一个面向大语言模型流量的代理与库。它通过转换
  OpenAI Chat、Anthropic Messages 和 OpenAI Responses 协议，把来自 Claude Code、Codex CLI 等编码代理的请求路由到
  vLLM、NVIDIA NIM、Ollama 等后端，并支持随机、LLM 分类器、信号驱动阶段路由等算法以及 Prometheus 运维指标。项目目前处于 pre-alpha
  阶段，API 与算法在 v1.0 前预计会有较大变化，不建议用于生产环境。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - NVIDIA
  technologies:
  - Rust
  - LLM proxy
  - OpenAI API
  - Anthropic Messages API
  - OpenAI Responses API
  - vLLM
  - NVIDIA NIM
  - Ollama
  - Prometheus
  - TOML
  key_people: []
key_logic_flow:
- Switchyard 是用 Rust 编写的 LLM 流量代理与库，核心能力包括协议转换、多后端路由和运维指标采集。
- 在 Launcher 路径中，用户安装 nemo-switchyard CLI 后，可将 Claude Code、Codex CLI、OpenClaw 等编码代理的
  OpenAI/Anthropic 格式请求转接至 OpenRouter 或本地 TOML 配置的后端。
- 在 Server 路径中，用户通过 cargo 安装 switchyard-server，用 routes.toml 配置并启动独立代理服务，对外暴露 /health
  等端点。
- 在 Library 路径中，switchyard-libsy 把路由算法嵌入用户自己的 Rust 应用，switchyard-protocol 提供供应商中立的请求/响应/流类型，可与
  switchyard-llm-client 配对使用。
- 项目支持随机路由、LLM 分类器、阶段路由、升级路由等策略，也支持 passthrough 直连单个目标。
- Switchyard 当前为 pre-alpha 软件，API 与算法在达到 v1.0 前预计会大幅变化，不适用于生产环境。
object_mentions:
- object_type: project
  name: NVIDIA-NeMo/Switchyard
  canonical_name: Switchyard
  url: https://github.com/NVIDIA-NeMo/Switchyard
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章指出，Switchyard 是一个面向大模型流量的 Rust 代理与库，可在不同供应商之间转发请求并完成 OpenAI 与 Anthropic API
    的协议转换。
  - 它记录 Prometheus 运维指标，并提供类型化、可组合的路由算法。
  - 项目采用 Apache 2.0 许可证，版权归 NVIDIA Corporation 所有。
  article_id: 1da80cd2d3f3e0fd
- object_type: product
  name: nemo-switchyard
  canonical_name: nemo-switchyard
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章介绍 Launcher 路径时指出，可通过 uv tool install --python 3.10 'nemo-switchyard[cli]' 安装已发布的
    Switchyard 命令行工具。
  - 安装后可用 switchyard launch claude --model switchyard 等命令把编码代理的流量导入 Switchyard。
  article_id: 1da80cd2d3f3e0fd
- object_type: product
  name: switchyard-server
  canonical_name: switchyard-server
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Server 路径使用 cargo install --locked switchyard-server 安装独立 Rust 代理，并用 switchyard-server
    --config routes.toml 启动服务。
  - 启动后可通过 curl http://localhost:4000/health 验证代理是否正常运行。
  article_id: 1da80cd2d3f3e0fd
- object_type: project
  name: switchyard-libsy
  canonical_name: switchyard-libsy
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Library 路径中，switchyard-libsy 把路由算法嵌入用户自己的 Rust 应用，本身不调用模型，只决定目标并把模型调用交回调用方。
  - 用户可在 Cargo 依赖中通过 GitHub 仓库地址引入 switchyard-libsy。
  article_id: 1da80cd2d3f3e0fd
- object_type: project
  name: switchyard-protocol
  canonical_name: switchyard-protocol
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - switchyard-protocol 提供与供应商无关的请求、响应和流式类型，支撑在不同后端之间完成格式转换。
  - 它可以与 switchyard-libsy 一起通过 GitHub 仓库地址引入到 Rust 项目中。
  article_id: 1da80cd2d3f3e0fd
- object_type: project
  name: switchyard-llm-client
  canonical_name: switchyard-llm-client
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 当需要由库自动发起模型调用时，用户可以将 switchyard-libsy 与 switchyard-llm-client 配对使用。
  - 这样既能复用 Switchyard 的路由算法，又不必自己实现上游模型的 HTTP 调用。
  article_id: 1da80cd2d3f3e0fd
extract_result: success
---

Switchyard is a Rust proxy and library for LLM traffic. It routes requests across providers, translates between OpenAI and Anthropic APIs, records operational metrics, and provides typed, composable routing algorithms.

**Why Switchyard?** Point a coding agent such as Claude Code or Codex at an
open-source model. Switchyard translates between the OpenAI Chat, Anthropic
Messages, and OpenAI Responses formats, so the agent keeps speaking its native
API while the request is served by vLLM, NVIDIA NIM, Ollama, or any
OpenAI-compatible endpoint. The same proxy can spread traffic across several
models for A/B benchmarking, apply signal-driven stage routing, or run a custom
algorithm you write yourself.

**Protocol Translation**: convert between OpenAI Chat, Anthropic Messages, and OpenAI Responses formats**Multi-Backend Routing**: random routing, LLM-as-classifier routing, signal-driven stage-router, or your own algorithm**Operational Metrics**: Prometheus metrics cover requests, errors, latency, tokens, and routing overhead

Switchyard is pre-alpha software that is evolving rapidly. The API and algorithms are expected to change significantly before we reach v1.0.

Warning

Experimental software. Not for production use.

Choose the launcher path to run Claude Code, Codex CLI, or OpenClaw through Switchyard. Choose the server path to run Switchyard as a standalone proxy. Choose the library path to embed routing in your own Rust application.

Install `uv`

if it is
not already available, then install the published Switchyard tool:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

The coding agent you launch must also be installed and on your `PATH`

. This does
not install the standalone `switchyard-server`

binary; use the Server Path for
that.

Set an OpenRouter key and launch against the packaged deployment:

```
export OPENROUTER_API_KEY="your-openrouter-key" # pragma: allowlist secret
switchyard launch claude --model switchyard
switchyard launch codex --model switchyard
switchyard launch openclaw --model switchyard
```

To use your own native TOML deployment, pass its route ID and configuration:

`switchyard launch claude --model my-route --config routes.toml`

Use this path to install and run the standalone Rust proxy. Install Rust with Cargo, then install the published binary:

```
cargo install --locked switchyard-server
switchyard-server --help
```

Cargo builds the release binary and installs it into `~/.cargo/bin`

by default.

Create `routes.toml`

using the
Getting Started guide, then validate it
and start the server:

```
export OPENROUTER_API_KEY="your-openrouter-key" # pragma: allowlist secret
switchyard-server --config routes.toml --dry-run
switchyard-server --config routes.toml --host 127.0.0.1 --port 4000
```

Verify the proxy in another terminal:

`curl http://localhost:4000/health`

For a complete configuration and a test request, follow Getting Started.

`switchyard-libsy`

embeds the routing algorithms in your own Rust application.
It never calls a model itself: an algorithm decides which target to use and
hands every model call back to you, so it drops into an existing proxy, gateway,
or agent runtime without owning an HTTP stack. Pair it with
`switchyard-llm-client`

when you want the calls made for you.

```
[dependencies]
switchyard-libsy = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" }
switchyard-protocol = { git = "https://github.com/NVIDIA-NeMo/Switchyard.git" }
```

See Getting Started for setup and the
algorithm list, or the `switchyard-libsy`

crate docs.

| Strategy | Use it when | Route `type` |
|---|---|---|
| LLM Classifier | Request content should decide whether a turn needs the weak or strong tier. | `llm_classifier` |
| Stage Router | Signals already in the conversation, such as tool results and errors, should route most turns without an extra model call. | `stage_router` |
| Escalation Router | Every turn runs on the weak tier first, and a judge reads that answer to decide whether to send the same request to the strong tier. | `llm_classifier` with `mode = "escalation"` |
| Random | You need a fixed traffic split for A/B tests, baselines, or cost experiments. | `random` |

A `passthrough`

route registers one target under one model ID with no routing
decision. See the Routing Overview for
the common route shape and self-hosted targets.

```
flowchart LR
clients["Clients"]
switchyard["Switchyard<br/>routing · translation · fallback"]
backends["Model backends"]
clients -->|"OpenAI / Anthropic API"| switchyard
switchyard -->|"provider-native format"| backends
```

Clients keep their native OpenAI or Anthropic API format. Switchyard picks a configured backend, forwards the request in that backend's own format, and translates the response back into the shape the client expects. The server accepts OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages. Each configured LLM client selects one upstream format.

**Getting Started**: complete launcher and standalone server walkthroughs**Core Concepts**: LLM clients, targets, routes, model IDs, and routing algorithms**Routing Overview**: choose and configure a routing algorithm: server configuration, routing algorithms, and metrics`switchyard-server`

: embed routing algorithms in a Rust application`switchyard-libsy`

: provider-neutral request, response, and streaming types`switchyard-protocol`

: request, response, and stream translation`switchyard-translation`


**Issues**: GitHub Issues**Code of Conduct**: Code of Conduct

Apache 2.0 License. Copyright NVIDIA Corporation.