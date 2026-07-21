---
title: 'Mesh LLM: distributed AI computing on iroh'
source: https://www.iroh.computer/blog/mesh-llm
author:
- '[[tionis]]'
published: '2026-07-11'
created: '2026-07-12'
manifest_dates:
- '2026-07-12'
description: 'Article URL: https://www.iroh.computer/blog/mesh-llm Comments URL: https://news.ycombinator.com/item?id=48876505
  Points: 251 # Comments: 58'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0cb2a7c0c0cba9c6
source_type: community_discussion
tldr: Mesh LLM 是基于 iroh 的去中心化 AI 计算系统，将用户已有的 GPU 和内存跨机器池化，暴露为兼容 OpenAI API 的 localhost:9337/v1
  接口，无需中心服务器即可运行 40 多种模型。
objective_summary: iroh 公司发布了开源项目 Mesh LLM，通过 iroh 的 QUIC 协议在任意机器间建立认证直连，将多台机器的 GPU
  和内存聚合成单一计算池。Mesh LLM 支持三种推理模式——本地执行、路由到远端节点、或按层范围分片在多个节点间流水执行（Skippy 模式），最大可运行 235B
  参数的 MoE 模型。系统约 18 MB，用户可加入公共 mesh 或自建私有部署，移动端应用基于 iroh Swift SDK 开发中。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - iroh
  - n0-computer
  technologies:
  - Mesh LLM
  - QUIC
  - ALPN
  - MCP
  - NAT traversal
  - ACP
  - iroh
  key_people: []
key_logic_flow:
- Mesh LLM 将多台机器上已有的 GPU 和内存资源池化，通过一个兼容 OpenAI API 的接口统一暴露。
- 系统基于 iroh 端点的 QUIC 协议实现节点间认证直连，无中心服务器，依靠打洞和中继回退穿越 NAT。
- 请求可通过三种方式处理：本地 GPU 执行、路由到已加载模型的远端节点、或将超大模型按层切分到多台机器流水执行。
- Skippy 分片模式将模型按层范围分配到不同节点，激活值在节点间流动，使多台普通机器能运行单机装不下的大型模型。
- Mesh LLM 支持从 5 亿参数到 235B MoE 的 40 多种模型，安装包约 18 MB，用户可加入公共 mesh 或自建私有部署。
- 移动端应用正在开发中，计划采用 ACP 代理标准，使更多客户端能够接入 mesh。
extract_result: success
object_mentions:
- object_type: project
  name: Mesh LLM
  canonical_name: Mesh LLM
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Mesh LLM 将用户已有的 GPU 和内存资源跨机器池化，整体暴露为一个兼容 OpenAI API 的接口。
  - 请求可通过三种方式处理：本地执行、路由到已加载模型的节点、或将超大模型分层切分到多台机器上流水执行。
  - Mesh LLM 支持从 5 亿参数小模型到 235B MoE 大模型在内的 40 多种模型，安装包约 18 MB。
  article_id: 0cb2a7c0c0cba9c6
- object_type: project
  name: iroh
  canonical_name: iroh
  url: https://www.iroh.computer
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Mesh LLM 基于 iroh 端点构建，每个节点启动 iroh 端点作为身份标识（公钥），无中心服务器。
  - iroh 处理打洞、NAT 穿越和中继回退，使任意两个节点之间建立经过认证的 QUIC 直连。
  - Mesh LLM 在不同区域运行两个 iroh 中继，确保无法直连的节点始终有备用路径。
  article_id: 0cb2a7c0c0cba9c6
---

When people picture running a large language model, they picture a data center. Racks of GPUs that belong to someone else, a metered API, and a bill that grows every month you succeed. You send your prompts off to a black box and hope the price, the model, and the privacy policy all stay the way they were when you signed up.

For a lot of teams that is a bad trade. You give up control over when models change, where your data goes, and what hardware runs your workloads. And as usage grows, so does the bill, with no lever to pull except "pay more."

Mesh LLM is a different shape. It pools the GPUs and memory you already have, across as many machines as you want to add, and exposes the whole thing as one OpenAI-compatible API. Start one node. Add more later. Let the mesh decide whether a model runs on the box in front of you, routes to a peer, or splits across several machines.

The popular models are monoliths. Most people reach them through a UI or an API key and pay a large provider to run everything. That is convenient, and it is also a surrender. You do not control when the model gets updated, what memory it runs in, or what hardware sits underneath.

Plenty of businesses and services that depend on these models want the opposite: more control, more pluggability, lower cost. They have GPUs sitting in offices, in closets, under desks. What they are missing is a way to make those machines act like one.

The pitch is simple. Run bigger models without buying bigger GPUs. Share compute privately with your team, or publicly with the world, to power agents and chat. Point any OpenAI client at http://localhost:9337/v1 and stop caring where the work actually happens.

Under the hood, Mesh LLM distributes model compute across a mesh of iroh endpoints. A request can be served three ways:

- Run it locally, on this machine's GPU.
- Route it to a peer that already has the model loaded.
- Split a model too big for any single box across several machines, as a pipeline.

The architecture is pluggable. Plugins declare what they provide in a manifest, the runtime starts them, routes calls, and exposes their capabilities over MCP, HTTP, inference, and mesh events. The catalog ships with 40+ models, from half-a-billion-parameter models that fit on a laptop to 235B mixture-of-experts giants.

For the giants, Mesh LLM has a split mode (internally, "Skippy"). A model gets partitioned by layer ranges into stages: layers 0 to 15 on one node, 16 to 31 on the next, and so on down the pipeline. Activations flow from one stage to the next, so several modest machines can run a model none of them could hold alone. The OpenAI client never sees any of this. It still just talks to localhost.

Every node, whether it serves models or only sends requests, boots an iroh endpoint. That endpoint is the node's identity, a public key, and its only network surface. There is no central server. iroh handles the hole-punching, NAT traversal, and relay fallback needed to open a direct, authenticated QUIC connection between any two nodes, wherever they sit.

To keep that working across the open internet, Mesh LLM runs two iroh relays in different regions, so nodes that cannot reach each other directly always have a fallback path nearby.

The whole protocol rides on QUIC's ALPN negotiation. There are three:

| ALPN | What it carries |
|---|---|
| mesh-llm/1 | Main mesh: gossip, routing, HTTP tunnels, plugin channels |
| mesh-llm-control/1 | Owner control plane (config sync, ownership attestation) |
| skippy-stage/2 | Latency-sensitive activation transport for split models |

Inside the main `mesh-llm/1`

connection, everything is a bidirectional QUIC stream tagged with a single leading byte that says what kind of stream it is. One connection carries gossip, inference, route queries, and peer-lifecycle events, all demuxed by that first byte:

| Byte | Stream type | Description |
|---|---|---|
| 0x01 | GOSSIP | peer announcements (models, GPU, RTT, capabilities) |
| 0x04 | TUNNEL_HTTP | inference requests proxied to a peer |
| 0x05 | ROUTE_REQUEST | "which models do you host?" |
| 0x06 | PEER_DOWN | dead-peer notification |
| 0x07 | PEER_LEAVING | graceful shutdown |
| 0x08 | PLUGIN_CHANNEL | plugin RPC |
| 0x0e | DIRECT_PATH_REQUEST | share direct addresses for NAT traversal |

The neat part is what this buys you. iroh gives authenticated, NAT-traversing QUIC between any two machines, addressed by public key. So "route to a peer" and "stream activations to the next pipeline stage" become the same primitive as "talk to localhost," just with a different endpoint ID. The networking stops being something you have to think about.

iroh provides the secure transport. Mesh LLM builds its own gossip layer on top, so it controls exactly who gets admitted to the mesh, which versions are compatible, and which peers to trust.

Users can install the lightweight software (about 18 MB) and either join the
public mesh or configure private deployments. The system presents itself as
`localhost:9337/v1`

to any standard OpenAI client.

A mobile app is coming, built on iroh's Swift SDK. The plan is to speak ACP, the emerging agent standard, so other clients can join the mesh too. The throughline is the same one that motivated the whole project: more peer to peer, fewer closed servers, and no lock-in.

To get started, take a look at our docs, dive directly into the code, or chat with us in our discord channel.