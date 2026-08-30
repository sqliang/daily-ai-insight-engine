---
title: agent-substrate/substrate
source: https://github.com/agent-substrate/substrate
author: []
published: ''
created: '2026-08-21'
manifest_dates:
- '2026-08-21'
description: 'Agent Substrate: the core systemAgent Substrate NOTE: This is not an
  officially supported Google product. This project is not eligible for the Google
  Open Source Software Vulnerability Rewards Program. What is Agent Substrate? Agent
  Substrate delivers a performant, high density runtime environment for large scale
  agent deployments. The agent substrate control plane provides full lifecycle management
  for agent sandboxes, delivering sub-second agent resume/suspend operations, and
  allows heavy multiplexing of agents onto the same computer infrastructure. It supports
  multiple sandbox technologies including microVMs and gVisor, enabling consistent
  lifecycle operations for all sandbox types. At its core, Agent Substrate maps a
  larger set of “actors” (applications such as agents) onto a smaller set of ready
  “workers”, relying on the fact that agent-like applications tend to be idle most
  of the time to achieve heavy multiplexing. It provides functionality to manage an
  actor’s lifecycle (e.g. create/destroy, suspend/resume), to assign actors to workers
  in real time, and to route incoming traffic to them. Agent Substrate is intended
  to be a low-opinion system. The workloads it manages don''t have to be literal AI
  agents, but those are the best example of the kind of applications it is designed
  for. It is not an SDK for building agents, but rather a system for running them
  at scale. Agent Substrate leverages Kubernetes for the infrastructure provisioning
  and worker lifecycle management (Kubernetes Pods). It builds on top of Kubernetes
  features like Pods and Pod autoscaling, while Agent Substrate provides agent-specific
  scheduling and control to achieve lower latency. Using Kubernetes as the underlying
  system enables consistent infrastructure management across all workloads types that
  are required for end to end agentic deployments and allows holistic infrastructure
  optimizations for RL scenarios that span agentic, inference and training cycles.
  Demo Watch the Agent Substrate cluster multiplex ~250 stateful actors across just
  8 physical pods. This demo highlights the core developer experience and "Agentic
  Infrastructure" capabilities of Substrate: Instant Actor Teleport: High-performance
  suspend and resume of actors onto any available worker in the pool with sub-second
  activation. State Persistence: Persistent working memory (volatile RAM) and filesystem
  state preserved perfectly across hibernation cycles via full-state snapshots. Agent
  Swarm Multiplexing: Demonstrates 30x+ oversubscription by "juggling" a large registry
  of stateful actors onto a small pool of shared physical pods. To reproduce this
  demo in your own cluster, please refer to the detailed walkthrough in the Counter
  Demo. For more videos and walkthroughs, visit our YouTube channel: agent-substrate.
  Framework Agnostic & Compatibility Agent Substrate is designed to be framework and
  agent harness agnostic. Because it manages standard OCI containers at the kernel
  level (via gVisor), it can host agents built on any stack. Agent Development Kit
  (ADK): Native support for ADK-compatible actor identity and persistent working memory.
  LangChain: Ideal execution environment for long-running, stateful LangChain agents
  and sandboxed tool-calling. Claude Code & CodeX: Support for high-density, stateful
  coding environments that preserve terminal and filesystem state across sessions.
  Model Context Protocol (MCP): Deploy secure, sandboxed MCP servers as Substrate
  Actors to provide durable tools for any LLM. Ecosystem & Examples Agent Executor:
  A distributed agent runtime that demonstrates building a secure, hyper-scalable
  agent harness on Agent Substrate (see the announcement blog and integration guide).
  Status and compatibility Agent Substrate is currently in early development. It is
  not ready for production use, and the APIs are almost guaranteed to change. We are
  not making any guarantees about backward compatibility at this stage, and everything
  in this project may be changed. Supported Kubernetes Releases Currently we aim to
  support the latest stable release of Kubernetes, and the previous minor release.
  Community For announcements, technical discussions, and community support, please
  join the ate-dev Google Group. We host a weekly community meeting every Thursday
  from 10:00am - 11:00am PST. Video call link: https://meet.google.com/uhq-cxvn-dhy
  Or dial: (US) +1 253-289-6971 PIN: 787 664 574 59# More phone numbers: https://tel.meet/uhq-cxvn-dhy?pin=9044088223662
  We also have channels in the CNCF slack; request an invite here if you don''t have
  access. #substrate-users to discuss using substrate. #substrate-dev to discuss developing
  substrate. Developing Please see CONTRIBUTING.md for guidelines on contributing
  to the project. We welcome contributions of all kinds, but the project is VERY young.
  Our immediate focus is on building out the core system and demos, so we may not
  be able to review or merge contributions that don''t align with those goals in the
  near term. Quickstart (Development) To quickly set up the complete environment:
  Make sure you have Go, kubectl, and docker installed and configured on your dev
  machine. We will automatically manage other dependencies via Go, including kind.
  Run the following steps: # create cluster and local registry (IPv4; IP_FAMILY=dual|ipv6
  overrides) hack/create-kind-cluster.sh # install ate, valkey, rustfs hack/install-ate-kind.sh
  --deploy-ate-system # install counter demo hack/install-ate-kind.sh --deploy-demo-counter
  # install kubectl-ate go install ./cmd/kubectl-ate # create an atespace (required
  before creating actors), then a counter actor in it kubectl ate create atespace
  demo kubectl ate create actor my-counter-1 -a demo --template=ate-demo-counter/counter
  # port-forward the network router to bind to local port `8000` kubectl port-forward
  -n ate-system svc/atenet-router 8000:80 In a separate terminal, send an HTTP request
  to increment the counter: curl -X POST -H "Host: my-counter-1.demo.actors.resources.substrate.ate.dev"
  -i http://localhost:8000/ GKE Quickstart (Development) Create and configure your
  environment file: cp hack/ate-dev-env.sh.example .ate-dev-env.sh # Edit .ate-dev-env.sh
  to match your project and preferences, then source it: source .ate-dev-env.sh Enable
  application-default credentials for gcloud: gcloud auth application-default login
  --project=${PROJECT_ID} Provision the required GCP resources (GKE cluster, Redis,
  GCS, and IAM bindings): go run ./tools/setup-gcp bootstrap Deploy the Agent Substrate
  system to your cluster: ./hack/install-ate.sh --deploy-ate-system You can then deploy
  the sample applications. See demos/counter/README.md or demos/sandbox/README.md
  for detailed walkthroughs. ./hack/install-ate.sh --deploy-demo-counter Custom Setup
  and Deployment You can run individual setup steps to create GCP resources as needed.
  See go run ./tools/setup-gcp --help for available options. For example: go run ./tools/setup-gcp
  create cluster go run ./tools/setup-gcp create bucket Similarly, you can deploy
  or cleanup specific Agent Substrate components using the installation script. See
  ./hack/install-ate.sh --help for all options. # Re-deploy only ate-apiserver of
  the ATE system ./hack/install-ate.sh --deploy-ate-apiserver # Delete everything
  (core system and all demos) ./hack/install-ate.sh --delete-all Tearing down resources
  (GCP) If you need to delete the resources created by the setup script, you can use
  the provided script hack/teardown.sh. This script will delete resources in the reverse
  order of creation and handles partial failures gracefully. ./hack/teardown.sh --all
  Or run individual teardown steps as needed (see ./hack/teardown.sh for available
  options). Tearing down local kind resources If you need to delete the local kind
  cluster and its registry (if it was created by hack/create-kind-cluster.sh): ./hack/delete-kind-cluster.sh
  Demos We provide several sample applications demonstrating Agent Substrate''s capabilities:
  Counter Demo: A stateful Go HTTP server demonstrating state preservation across
  suspends/resumes, and dynamic CRD routing. Sandbox Demo (Antigravity): A secure,
  sandboxed execution environment (running Alpine Linux) that allows arbitrary shell
  execution while preserving filesystem state across sessions. Claude Code Multiplex:
  Demonstrates oversubscribing physical hardware by multiplexing multiple Claude Code
  agents onto a limited pool of workers. Multi-Template: Two ActorTemplates running
  different binaries share one WorkerPool, across three namespaces. Request Parking:
  An oversubscribed pool where the router holds inbound requests until a worker frees
  up, instead of returning 503. Autoscaled WorkerPool: Scales a WorkerPool on its
  assigned-worker count with an HPA fed by prometheus-adapter. Documentation & Guides
  Architecture: How the control plane, node supervisor, and networking stack fit together.
  API Configuration Guide: Detailed reference for configuring WorkerPools, ActorTemplates,
  Secrets, and Volumes. Full CLI Documentation: Installation and usage for kubectl-ate.
  Glossary: Core terms (Actor, Atespace, ActorTemplate, WorkerPool, Worker, ate-api-server,
  atenet, atelet, ateom) and how they relate. Integration Repositories: Where integrations
  live, how their repositories are named, and how fixes flow back to core. Observability
  Guide: Guide to actor logging, metrics, and distributed tracing. Authentication
  Guide: Configure trusted JWT providers and human credentials. Request Parking: How
  the router parks requests through transient worker-pool saturation. Threat Model:
  Trust boundaries, assumptions, and known risks. Roadmap: Current limitations and
  what is planned next. Benchmarking Guide: Locust-based load tests, monitoring stack,
  and the orchestrated benchmark harness. Tour Commands cmd/ateapi: The core control
  plane API server exposing gRPC endpoints to manage actor and worker lifecycles.
  cmd/atelet: A node-level DaemonSet that supervises physical worker pods, coordinates
  snapshotting, and manages state transfers. cmd/atecontroller: A Kubernetes controller
  that reconciles WorkerPool and ActorTemplate custom resources. cmd/atenet: A combined
  networking controller providing DNS, Envoy routing, and proxy sidecars. cmd/ateom-gvisor:
  An interior-pod helper running inside sandboxed worker pods to execute runsc checkpoint
  and restore commands. cmd/ateom-microvm: The micro-VM peer of ateom-gvisor, running
  actors as cloud-hypervisor VMs. cmd/podcertcontroller: A "polyfill" that provides
  Pod Certificate signers that will eventually ship in upstream Kubernetes (with different
  names). cmd/kubectl-ate: A CLI tool for managing Agent Substrate resources. See
  its README. cmd/benchmarking: Synthetic workloads used by the load tests, including
  glutton, which consumes RAM, disk, and file descriptors on demand. tools/setup-gcp:
  A provisioning utility to set up the necessary GCP infrastructure resources (GKE,
  GCS, IAM). demos/: Sample applications demonstrating Agent Substrate capabilities.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a5ffcd0a46dd44fd
source_type: community_discussion
tldr: Agent Substrate 是 Google 非官方支持的开源项目，基于 Kubernetes 提供高密度、高性能的 agent 大规模部署运行时。其控制平面把大量
  actor 映射到少量物理 worker 上，实现亚秒级挂起/恢复与 30 倍以上超额复用，支持 gVisor 和 microVM 沙箱。项目目前处于早期开发阶段，API
  可能随时变更，不推荐生产使用。
objective_summary: Google（通过 agent-substrate 组织，注明为非官方支持产品）发布了 Agent Substrate 开源项目。该系统基于
  Kubernetes 的 Pod 与自动扩缩容构建，通过控制平面把大量有状态 actor 映射到少量 worker 上，利用 gVisor 与 microVM
  沙箱技术实现全状态快照与亚秒级挂起/恢复，并兼容 ADK、LangChain、Claude Code/CodeX 及 MCP。官方演示在 8 个物理 Pod 上复用约
  250 个有状态 actor，展示 30 倍以上超额订阅。项目仍处于早期开发阶段，官方不保证 API 向后兼容性，也声明其不适合生产环境。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Google
  - CNCF
  technologies:
  - gVisor
  - microVM
  - Kubernetes
  - OCI
  - MCP
  - ADK
  - LangChain
  - Envoy
  - runsc
  key_people: []
key_logic_flow:
- Agent Substrate 是 Google 非官方支持的开源项目，提供面向大规模 agent 部署的高性能、高密度运行时环境。
- 其核心思路是把大量 actor 映射到少量就绪 worker 上，利用 agent 类应用大部分时间空闲的特点实现超额复用，并支持创建销毁、挂起恢复与实时流量路由。
- 系统基于 Kubernetes 的 Pod 与自动扩缩容构建，同时提供 agent 专属调度以降低延迟，并支持 gVisor 与 microVM 等多种沙箱技术。
- 项目设计为框架无关，可托管 ADK、LangChain、Claude Code/CodeX 与 MCP 服务器等任意技术栈构建的 agent。
- 官方演示在 8 个物理 Pod 上复用了约 250 个有状态 actor，展示 30 倍以上超额订阅及跨休眠周期的完整状态保留。
- 项目仍处于早期开发阶段，官方声明 API 几乎肯定会变化、不保证向后兼容性，并明确其当前不适合生产环境使用。
object_mentions:
- object_type: project
  name: agent-substrate/substrate
  canonical_name: agent-substrate/substrate
  url: https://github.com/agent-substrate/substrate
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Agent Substrate 提供高性能、高密度的运行时环境，用于大规模 agent 部署，其控制平面支持亚秒级的挂起与恢复操作。
  - Agent Substrate 基于 Kubernetes 构建，通过 Pod 管理基础设施，并支持 gVisor 与 microVM 等多种沙箱技术。
  - 官方演示在 8 个物理 Pod 上复用了约 250 个有状态 actor，展示 30 倍以上超额订阅与跨休眠周期的状态保留。
  article_id: a5ffcd0a46dd44fd
- object_type: project
  name: Agent Executor
  canonical_name: Agent Executor
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent Executor 是一个分布式 agent 运行时，演示如何在 Agent Substrate 上构建安全且可超大规模扩展的 agent harness。
  article_id: a5ffcd0a46dd44fd
- object_type: project
  name: Counter Demo
  canonical_name: Counter Demo
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Counter Demo 是一个有状态的 Go HTTP 服务，用于演示跨挂起与恢复周期的状态保留以及动态 CRD 路由。
  article_id: a5ffcd0a46dd44fd
- object_type: project
  name: Sandbox Demo (Antigravity)
  canonical_name: Sandbox Demo (Antigravity)
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Sandbox Demo（Antigravity）提供一个运行 Alpine Linux 的安全沙箱执行环境，允许任意 shell 执行并保留跨会话的文件系统状态。
  article_id: a5ffcd0a46dd44fd
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent Substrate 支持 Claude Code 与 CodeX 的高密度有状态编码环境，可跨会话保留终端与文件系统状态。
  article_id: a5ffcd0a46dd44fd
- object_type: project
  name: kubectl-ate
  canonical_name: kubectl-ate
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - kubectl-ate 是用于管理 Agent Substrate 资源的命令行工具，支持创建 atespace、actor 等资源并配有完整 CLI 文档。
  article_id: a5ffcd0a46dd44fd
extract_result: success
compound_value:
  score: 7.5
  reason: 核心投资逻辑在于：Agent Substrate 精准命中了 agent 规模化部署的算力成本痛点——通过全状态快照+亚秒级挂起/恢复，把大量有状态
    actor 复用映射到少量物理 worker 上，演示达成 30 倍超额订阅，这直接改写了 agent 的单位运行成本曲线。该设计洞察（agent 大部分时间空闲，可重度复用）即便本仓库因早期
    API 不稳定而失败，也很可能沉淀为 agent 基础设施层的行业标准设计范式，具备跨项目复利。同时它基于 Kubernetes Pod 与 CNCF 生态构建，能借力庞大的云原生基础设施生态获得分发与演进惯性，且框架无关（兼容
    ADK/LangChain/Claude Code/MCP），一旦成熟会成为 agent 大规模部署的底层基座。但当前阶段官方明确'非官方支持、不推荐生产、API
    几乎必变'，3-5 年维度存在被更快的闭源方案（如 Modal/E2B）或大厂内部实现超越的风险，故给予 7.5 分而非更高。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Google
- Kubernetes/CNCF
- LangChain
- ADK
- MCP 生态
competitive_casualty:
- E2B、Modal 等托管沙箱运行时
- 按沙箱计费的闭源 agent 基础设施初创
- 传统 VM/Serverless 型 agent 编排平台
market_opportunities:
- 云厂商与 AI 基础设施团队可借鉴 Agent Substrate 的 actor-worker 超额复用模式，构建高密度 agent 托管服务，将大量有状态
  agent 映射到少量物理 worker，显著降低大规模 agent 部署的算力与闲置成本
- 围绕 gVisor/microVM 沙箱化部署存在商业化机会，可打造"即插即用"的 sandboxed MCP 服务器与编码 agent 托管平台，为长时运行、有状态的工作负载提供安全隔离与亚秒级挂起恢复能力
- 对个人开发者而言，掌握 Kubernetes + 沙箱技术 + agent 生命周期调度（Go/kubectl/OCI 容器生态）的技能组合，将成为下一代 AI
  基础设施方向的高价值稀缺能力
risk_matrix:
  regulatory: 项目标注为非官方支持产品、不纳入 Google OSS 漏洞奖励计划，说明 Google 在法律责任与支持义务上刻意切割；早期阶段暂无直接监管风险，但若用于承载编码
    agent 或 MCP 服务器，后续需关注出口管制、云服务合规及沙箱供应链安全审查
  technological: 项目处于早期开发，官方明确 API 几乎必然变更且不保证向后兼容，存在架构重构与废弃风险；其深度依赖 Kubernetes Pod
    与自动扩缩容，若 Kubernetes 演进方向变化或 Google 内部战略调整（非官方项目），项目可能被搁置
  competitive: 微软（Azure 容器应用/智能体托管）、AWS（EKS/App Runner）及 Temporal 等开源编排框架可能推出或已有同类高密度
    agent 运行时；作为非官方 Google 项目，若社区热度不足或被内部优先级挤压，存在被生态边缘化的风险
  ethical: 30 倍以上超额复用意味着大量有状态 actor 共享物理基础设施，多租户数据隔离边界与"全状态快照（RAM+文件系统）"的隐私安全需重点审计；agent
    跨 worker 迁移时携带的会话状态若含敏感数据，可能扩大数据暴露面
  additional:
  - 项目明确"不适合生产环境"且不保证向后兼容，企业若过早绑定其 API 将面临锁死与迁移成本风险；演示中的 30 倍超额倍率受实际负载特征限制，可能造成过度预期
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: agent-substrate/substrate
  canonical_name: agent-substrate/substrate
  url: https://github.com/agent-substrate/substrate
  positioning: 面向大规模 agent 部署的高性能、高密度运行时，基于 Kubernetes 构建，通过控制平面实现 actor 到 worker
    的超额复用与亚秒级挂起恢复。
  technical_signal: 基于 Kubernetes Pod 与自动扩缩容构建，支持 gVisor 与 microVM 沙箱，通过全状态快照实现跨休眠周期的状态保留。
  adoption_signal: 官方演示在 8 个物理 Pod 上复用约 250 个有状态 actor，并已开设每周社区会议与 CNCF Slack 讨论渠道。
  ecosystem_relevance: 框架无关设计，兼容 ADK、LangChain、Claude Code/CodeX 与 MCP，可托管任意技术栈构建的
    agent。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Google 以非官方身份开源的高密度 agent 运行时，直击 agent 大规模部署成本与延迟痛点，30 倍超额复用思路具有显著基础设施创新价值，值得跟踪其
    API 演进与生态落地。
  risk_notes:
  - 项目处于早期开发阶段，官方声明 API 几乎肯定会变化且不保证向后兼容。
  - 官方明确该项目当前不适合生产环境使用，且不参与 Google 开源漏洞奖励计划。
  score: 9.0
  article_ids:
  - a5ffcd0a46dd44fd
  evidence_snippets:
  - Agent Substrate 提供高性能、高密度的运行时环境，用于大规模 agent 部署，其控制平面支持亚秒级的挂起与恢复操作。
  - Agent Substrate 基于 Kubernetes 构建，通过 Pod 管理基础设施，并支持 gVisor 与 microVM 等多种沙箱技术。
  - 官方演示在 8 个物理 Pod 上复用了约 250 个有状态 actor，展示 30 倍以上超额订阅与跨休眠周期的状态保留。
- object_type: project
  name: Agent Executor
  canonical_name: Agent Executor
  url: null
  positioning: 在 Agent Substrate 之上构建的分布式 agent 运行时，演示如何打造安全且可超大规模扩展的 agent harness。
  technical_signal: 作为分布式 agent 运行时，展示在 Agent Substrate 上构建安全且可超大规模扩展的 agent 执行框架的能力。
  adoption_signal: null
  ecosystem_relevance: 属于 Agent Substrate 生态的参考实现，配套公告博客与集成指南，帮助开发者理解其运行时的安全模型与扩展方式。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 Agent Substrate 官方展示的参考运行时，其安全模型与超大规模扩展方式体现了该平台的典型用法，可帮助判断平台实际能力与最佳实践。
  risk_notes:
  - 目前仅作为示例与参考实现存在，缺乏独立成熟度证据与生产使用案例。
  score: 5.0
  article_ids:
  - a5ffcd0a46dd44fd
  evidence_snippets:
  - Agent Executor 是一个分布式 agent 运行时，演示如何在 Agent Substrate 上构建安全且可超大规模扩展的 agent harness。
- object_type: project
  name: Counter Demo
  canonical_name: Counter Demo
  url: null
  positioning: 一个有状态的 Go HTTP 服务示例，用于演示跨挂起与恢复周期的状态保留以及动态 CRD 路由能力。
  technical_signal: 通过有状态 Go HTTP 服务验证全状态快照在休眠与恢复周期中的保留效果，并展示动态 CRD 路由机制。
  adoption_signal: null
  ecosystem_relevance: 作为 Agent Substrate 的官方演示应用，为开发者提供在其集群上复现超额复用与状态保留效果的操作指南。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该示例是理解 Agent Substrate 核心能力（状态保留、动态路由）的最小可复现载体，其演进可反映平台 API 与行为变化。
  risk_notes:
  - 作为演示示例，其实现细节可能随平台早期 API 变更而频繁调整。
  score: 4.0
  article_ids:
  - a5ffcd0a46dd44fd
  evidence_snippets:
  - Counter Demo 是一个有状态的 Go HTTP 服务，用于演示跨挂起与恢复周期的状态保留以及动态 CRD 路由。
- object_type: project
  name: Sandbox Demo (Antigravity)
  canonical_name: Sandbox Demo (Antigravity)
  url: null
  positioning: 运行 Alpine Linux 的安全沙箱执行环境示例，支持任意 shell 执行并跨会话保留文件系统状态。
  technical_signal: 基于安全沙箱技术提供任意 shell 执行能力，并通过文件系统状态持久化支持跨会话的连续操作。
  adoption_signal: null
  ecosystem_relevance: 作为 Agent Substrate 沙箱能力的示例，展示其在隔离执行与状态保留方面的产品化潜力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该示例展示 Agent Substrate 在安全代码执行与持久化开发环境场景的应用潜力，是评估其沙箱生态可用性的窗口。
  risk_notes:
  - 仅为演示性质示例，安全性未经独立审计，不适合作为生产沙箱方案。
  score: 4.0
  article_ids:
  - a5ffcd0a46dd44fd
  evidence_snippets:
  - Sandbox Demo（Antigravity）提供一个运行 Alpine Linux 的安全沙箱执行环境，允许任意 shell 执行并保留跨会话的文件系统状态。
- object_type: project
  name: kubectl-ate
  canonical_name: kubectl-ate
  url: null
  positioning: 用于管理 Agent Substrate 资源的命令行工具，支持创建 atespace、actor 等资源并配有完整 CLI 文档。
  technical_signal: 作为 kubectl 插件提供 atespace、actor 等资源的创建与管理能力，是操作 Agent Substrate
    集群的主要交互入口。
  adoption_signal: null
  ecosystem_relevance: 作为 Agent Substrate 官方工具链的一部分，其命令设计反映平台资源模型与开发者工作流。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: kubectl-ate 是开发者上手 Agent Substrate 的必经工具，其功能演进直接反映平台资源模型与操作流程的成熟度。
  risk_notes:
  - 工具随平台早期迭代而快速变化，命令与资源模型可能发生不兼容变更。
  score: 4.0
  article_ids:
  - a5ffcd0a46dd44fd
  evidence_snippets:
  - kubectl-ate 是用于管理 Agent Substrate 资源的命令行工具，支持创建 atespace、actor 等资源并配有完整 CLI 文档。
impact_score:
  score: 6.8
  reason: 评分依据：该项目由 Google 组织背书（尽管注明非官方支持），直击大规模有状态 agent 部署的核心痛点——agent 类应用大部分时间空闲导致的资源浪费与状态管理成本。其
    actor/worker 复用架构配合全状态快照的亚秒级挂起/恢复，在官方 demo 中实现 8 个 Pod 承载约 250 个有状态 actor 的 30
    倍以上超额订阅，若经独立验证将显著改变 agent 基础设施的算力经济模型，故给予 6.8 分。但项目明确处于早期开发阶段、API 几乎必然变更、官方声明不适合生产，且采用
    Kubernetes 为底座而非全新范式，短期对行业的冲击力仍属'重要基础设施探索'而非'范式转移'，未达到 8 分门槛。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 30 倍超额复用与亚秒级挂起/恢复能否真正降低大规模有状态 agent 的部署与算力成本
hype_assessment:
  level: low
  reason: 判定依据：README 措辞高度克制且诚实——主动声明'非 Google 官方支持产品'、'不适合生产使用'、'API 几乎肯定会变化且不保证向后兼容'，未出现'颠覆''革命'等
    PR 滥用词汇，整体营销包装很少。唯一需警惕的是 30 倍超额订阅等数据来自官方 demo 演示，属厂商自证口径，需社区独立复现验证，但基于其坦诚的定位声明，判定炒作水分较低。
information_entropy: high
domain_disruption:
  technical_innovation: 核心突破在于将 agent 抽象为有状态 actor，通过控制平面把大量 actor 映射到少量就绪 worker，利用
    agent 大部分时间空闲的特性实现重度复用；以全状态快照（含易失内存与文件系统）实现亚秒级挂起/恢复与实时流量路由，并支持 gVisor/microVM
    多沙箱统一生命周期管理。同时巧妙分层：用 Kubernetes Pod 与自动扩缩容做基础设施供给，叠加 agent 专属调度层降低延迟，兼顾生态一致性与低延迟需求。
  business_model: 若技术验证成立，将直接改变大规模 agent 集群的算力与内存成本结构——由'每 agent 独占资源'转向'高密度共享池'，可能催生按活跃时间计费的
    agent 基础设施商业模式，推动多租户 agent 平台与'agent 基础设施即服务'的兴起。开源形式亦有助于 Google 强化 Kubernetes
    生态在 agent 时代作为事实标准底层的地位，属战略卡位。
engineering_complexity: prototype
---

NOTE: This is not an officially supported Google product. This project is not eligible for the Google Open Source Software Vulnerability Rewards Program.

Agent Substrate delivers a performant, high density runtime environment for large scale agent deployments. The agent substrate control plane provides full lifecycle management for agent sandboxes, delivering sub-second agent resume/suspend operations, and allows heavy multiplexing of agents onto the same computer infrastructure. It supports multiple sandbox technologies including microVMs and gVisor, enabling consistent lifecycle operations for all sandbox types.

At its core, Agent Substrate maps a larger set of “actors” (applications such as agents) onto a smaller set of ready “workers”, relying on the fact that agent-like applications tend to be idle most of the time to achieve heavy multiplexing. It provides functionality to manage an actor’s lifecycle (e.g. create/destroy, suspend/resume), to assign actors to workers in real time, and to route incoming traffic to them.

Agent Substrate is intended to be a low-opinion system. The workloads it manages don't have to be literal AI agents, but those are the best example of the kind of applications it is designed for. It is not an SDK for building agents, but rather a system for running them at scale.

Agent Substrate leverages Kubernetes for the infrastructure provisioning and worker lifecycle management (Kubernetes Pods). It builds on top of Kubernetes features like Pods and Pod autoscaling, while Agent Substrate provides agent-specific scheduling and control to achieve lower latency. Using Kubernetes as the underlying system enables consistent infrastructure management across all workloads types that are required for end to end agentic deployments and allows holistic infrastructure optimizations for RL scenarios that span agentic, inference and training cycles.

*Watch the Agent Substrate cluster multiplex ~250 stateful actors across just 8 physical pods.*

This demo highlights the core developer experience and "Agentic Infrastructure" capabilities of Substrate:

**Instant Actor Teleport:**High-performance suspend and resume of actors onto any available worker in the pool with sub-second activation.**State Persistence:**Persistent working memory (volatile RAM) and filesystem state preserved perfectly across hibernation cycles via full-state snapshots.**Agent Swarm Multiplexing:**Demonstrates 30x+ oversubscription by "juggling" a large registry of stateful actors onto a small pool of shared physical pods.

To reproduce this demo in your own cluster, please refer to the detailed walkthrough in the **Counter Demo**.

For more videos and walkthroughs, visit our YouTube channel: **agent-substrate**.

Agent Substrate is designed to be **framework and agent harness agnostic**. Because it manages standard OCI containers at the kernel level (via gVisor), it can host agents built on any stack.

**Agent Development Kit (ADK):**Native support for ADK-compatible actor identity and persistent working memory.**LangChain:**Ideal execution environment for long-running, stateful LangChain agents and sandboxed tool-calling.**Claude Code & CodeX:**Support for high-density, stateful coding environments that preserve terminal and filesystem state across sessions.**Model Context Protocol (MCP):**Deploy secure, sandboxed MCP servers as Substrate Actors to provide durable tools for any LLM.

**Agent Executor:**A distributed agent runtime that demonstrates building a secure, hyper-scalable agent harness on Agent Substrate (see the announcement blog and integration guide).

Agent Substrate is currently in early development. It is not ready for production use, and the APIs are almost guaranteed to change. We are not making any guarantees about backward compatibility at this stage, and everything in this project may be changed.

Currently we aim to support the latest stable release of Kubernetes, and the previous minor release.

For announcements, technical discussions, and community support, please join
the **ate-dev** Google Group.

We host a weekly community meeting every Thursday from 10:00am - 11:00am PST.

- Video call link: https://meet.google.com/uhq-cxvn-dhy
- Or dial: (US) +1 253-289-6971 PIN: 787 664 574 59#
- More phone numbers: https://tel.meet/uhq-cxvn-dhy?pin=9044088223662

We also have channels in the CNCF slack; request an invite here if you don't have access.

- #substrate-users to discuss using substrate.
- #substrate-dev to discuss developing substrate.

Please see CONTRIBUTING.md for guidelines on contributing to the project. We welcome contributions of all kinds, but the project is VERY young. Our immediate focus is on building out the core system and demos, so we may not be able to review or merge contributions that don't align with those goals in the near term.

To quickly set up the complete environment:

-
Make sure you have Go,

`kubectl`

, and`docker`

installed and configured on your dev machine. We will automatically manage other dependencies via Go, including`kind`

. -
Run the following steps:


```
# create cluster and local registry (IPv4; IP_FAMILY=dual|ipv6 overrides)
hack/create-kind-cluster.sh
# install ate, valkey, rustfs
hack/install-ate-kind.sh --deploy-ate-system
# install counter demo
hack/install-ate-kind.sh --deploy-demo-counter
# install kubectl-ate
go install ./cmd/kubectl-ate
# create an atespace (required before creating actors), then a counter actor in it
kubectl ate create atespace demo
kubectl ate create actor my-counter-1 -a demo --template=ate-demo-counter/counter
# port-forward the network router to bind to local port `8000`
kubectl port-forward -n ate-system svc/atenet-router 8000:80
```

- In a
**separate terminal**, send an HTTP request to increment the counter:

`curl -X POST -H "Host: my-counter-1.demo.actors.resources.substrate.ate.dev" -i http://localhost:8000/`

-
Create and configure your environment file:

cp hack/ate-dev-env.sh.example .ate-dev-env.sh # Edit .ate-dev-env.sh to match your project and preferences, then source it: source .ate-dev-env.sh

-
Enable application-default credentials for gcloud:

`gcloud auth application-default login --project=${PROJECT_ID}`

-
Provision the required GCP resources (GKE cluster, Redis, GCS, and IAM bindings):

go run ./tools/setup-gcp bootstrap

-
Deploy the Agent Substrate system to your cluster:

./hack/install-ate.sh --deploy-ate-system

-
You can then deploy the sample applications. See demos/counter/README.md or demos/sandbox/README.md for detailed walkthroughs.

./hack/install-ate.sh --deploy-demo-counter


You can run individual setup steps to create GCP resources as needed. See `go run ./tools/setup-gcp --help`

for available options. For example:

```
go run ./tools/setup-gcp create cluster
go run ./tools/setup-gcp create bucket
```

Similarly, you can deploy or cleanup specific Agent Substrate components using the installation script. See `./hack/install-ate.sh --help`

for all options.

```
# Re-deploy only ate-apiserver of the ATE system
./hack/install-ate.sh --deploy-ate-apiserver
# Delete everything (core system and all demos)
./hack/install-ate.sh --delete-all
```

If you need to delete the resources created by the setup script, you can use the provided script `hack/teardown.sh`

. This script will delete resources in the reverse order of creation and handles partial failures gracefully.

`./hack/teardown.sh --all`

Or run individual teardown steps as needed (see `./hack/teardown.sh`

for available options).

If you need to delete the local `kind`

cluster and its registry (if it was created by `hack/create-kind-cluster.sh`

):

`./hack/delete-kind-cluster.sh`

We provide several sample applications demonstrating Agent Substrate's capabilities:

**Counter Demo**: A stateful Go HTTP server demonstrating state preservation across suspends/resumes, and dynamic CRD routing.**Sandbox Demo (Antigravity)**: A secure, sandboxed execution environment (running Alpine Linux) that allows arbitrary shell execution while preserving filesystem state across sessions.**Claude Code Multiplex**: Demonstrates oversubscribing physical hardware by multiplexing multiple Claude Code agents onto a limited pool of workers.**Multi-Template**: Two`ActorTemplate`

s running different binaries share one`WorkerPool`

, across three namespaces.**Request Parking**: An oversubscribed pool where the router holds inbound requests until a worker frees up, instead of returning`503`

.**Autoscaled WorkerPool**: Scales a`WorkerPool`

on its assigned-worker count with an HPA fed by prometheus-adapter.

- Architecture: How the control plane, node supervisor, and networking stack fit together.
- API Configuration Guide: Detailed reference for configuring WorkerPools, ActorTemplates, Secrets, and Volumes.
- Full CLI Documentation: Installation and usage for
`kubectl-ate`

. - Glossary: Core terms (Actor, Atespace, ActorTemplate, WorkerPool, Worker, ate-api-server, atenet, atelet, ateom) and how they relate.
- Integration Repositories: Where integrations live, how their repositories are named, and how fixes flow back to core.
- Observability Guide: Guide to actor logging, metrics, and distributed tracing.
- Authentication Guide: Configure trusted JWT providers and human credentials.
- Request Parking: How the router parks requests through transient worker-pool saturation.
- Threat Model: Trust boundaries, assumptions, and known risks.
- Roadmap: Current limitations and what is planned next.
- Benchmarking Guide: Locust-based load tests, monitoring stack, and the orchestrated benchmark harness.

`cmd/ateapi`

: The core control plane API server exposing gRPC endpoints to manage actor and worker lifecycles.`cmd/atelet`

: A node-level DaemonSet that supervises physical worker pods, coordinates snapshotting, and manages state transfers.`cmd/atecontroller`

: A Kubernetes controller that reconciles WorkerPool and ActorTemplate custom resources.`cmd/atenet`

: A combined networking controller providing DNS, Envoy routing, and proxy sidecars.`cmd/ateom-gvisor`

: An interior-pod helper running inside sandboxed worker pods to execute`runsc`

checkpoint and restore commands.`cmd/ateom-microvm`

: The micro-VM peer of`ateom-gvisor`

, running actors as cloud-hypervisor VMs.`cmd/podcertcontroller`

: A "polyfill" that provides Pod Certificate signers that will eventually ship in upstream Kubernetes (with different names).`cmd/kubectl-ate`

: A CLI tool for managing Agent Substrate resources. See its README.`cmd/benchmarking`

: Synthetic workloads used by the load tests, including`glutton`

, which consumes RAM, disk, and file descriptors on demand.`tools/setup-gcp`

: A provisioning utility to set up the necessary GCP infrastructure resources (GKE, GCS, IAM).`demos/`

: Sample applications demonstrating Agent Substrate capabilities.