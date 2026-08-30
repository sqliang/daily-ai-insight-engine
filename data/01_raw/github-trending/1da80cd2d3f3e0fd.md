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
pipeline_stage: ingested
id: 1da80cd2d3f3e0fd
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