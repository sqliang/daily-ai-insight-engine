---
title: macOS Container Machines
source: https://github.com/apple/container/blob/main/docs/container-machine.md
author:
- '[[timsneath]]'
published: '2026-06-10'
created: '2026-06-10'
description: 'Article URL: https://github.com/apple/container/blob/main/docs/container-machine.md
  Comments URL: https://news.ycombinator.com/item?id=48469658 Points: 725 # Comments:
  272'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ce06dcdbb7372ccd
source_type: community_discussion
tldr: 苹果发布了 container machine 功能，可在 macOS 上运行轻量级、持久化的 Linux 容器环境，基于标准 OCI 镜像，自动共享宿主的用户和家目录，支持
  systemd 服务注册和多发行版并行测试。
objective_summary: 苹果在 GitHub 上的 apple/container 项目中推出了 Container Machine 功能，用于在 macOS
  上创建基于标准 OCI 镜像的轻量级 Linux 环境。该功能自动将宿主的用户名和家目录映射到容器中，支持运行 systemd 服务、多发行版并行测试以及直接在
  macOS 端使用编辑器编辑代码并在 Linux 环境内构建。用户可通过 container machine 命令行工具创建、运行、停止和删除容器机器，并支持动态调整
  CPU 和内存配置。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Apple
  technologies:
  - OCI
  - systemd
  - Docker
  - Linux
  key_people: []
key_logic_flow:
- Container Machine 提供与 macOS 深度集成的 Linux 容器环境，基于标准 OCI 镜像，具备快速、轻量且持久化的特性。
- 容器机器与普通应用容器的区别在于其模拟完整的 Linux 环境而非单个应用，运行镜像的 init 系统并支持注册长期运行的后台服务。
- 容器机器自动将主机的用户名和家目录映射到 Linux 环境中，使 macOS 侧的仓库和配置文件在双平台均可直接访问使用。
- 用户可通过 container machine 命令行工具执行创建、列出、检查、运行、停止和删除等管理操作，并支持设置默认容器机器以省略 -n 参数。
- 任何包含 /sbin/init 的 Linux 镜像均可作为容器机器使用，文章提供了基于 Ubuntu 24.04 的完整 Dockerfile 构建示例。
- 容器机器支持通过 set 命令动态调整 CPU 和内存配置，变更在容器机器下次重启后生效。
extract_result: success
object_mentions:
- object_type: project
  name: apple/container
  canonical_name: apple/container
  url: https://github.com/apple/container
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该文档是苹果官方在 GitHub 仓库 apple/container 中发布的 Container Machine 功能说明，详细介绍了其用法和设计理念。
  - 容器机器的创建、运行和管理均通过 container 命令行工具完成，文档中提供了完整的 CLI 操作指令和输出示例。
  article_id: ce06dcdbb7372ccd
- object_type: product
  name: Container Machine
  canonical_name: Container Machine
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Container Machine 提供与 macOS 无缝集成的 Linux 环境，基于标准 OCI 镜像构建，支持快速、轻量和持久化运行。
  - 容器机器自动将宿主的用户名和家目录映射到 Linux 环境中，开发者可在 macOS 上编辑代码，在容器中构建和运行应用。
  - 容器机器运行镜像的 init 系统，支持通过 systemctl 注册长期运行的后台服务，便于在 Mac 上测试真实 Linux 服务。
  article_id: ce06dcdbb7372ccd
impact_score:
  score: 7.0
  reason: Apple 正式推出官方 Linux 容器虚拟机方案，直接对标 Docker Desktop 和 OrbStack 等第三方工具。在 macOS
    上运行 Linux 容器是大量开发者（包括 AI/ML 工程师）的刚需，Apple 通过深度系统集成（自动用户映射、家目录挂载、OCI 镜像兼容、systemd
    支持）提供了原生体验。此举可能重塑 macOS 生态下的容器开发工具格局，对依赖第三方付费工具的商业模式构成直接冲击。但本质上仍是现有技术的平台化整合，而非范式级创新。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: macOS 原生 Linux 容器方案能否替代 Docker Desktop 和 OrbStack
hype_assessment:
  level: low
  reason: GitHub 仓库的技术文档风格，直接展示命令行用法、配置文件示例和构建步骤，没有使用'颠覆'、'革命性'等 PR 话术。内容聚焦于具体功能特性和使用方式，信息准确可验证。
information_entropy: high
domain_disruption:
  technical_innovation: Apple 在 macOS 上提供原生 Linux 容器虚拟机方案，核心突破在于深度系统集成：自动将宿主机用户名和家目录映射到容器内（无需手动挂载卷）、支持
    OCI 标准镜像、运行镜像的 init 系统（systemd）以支持长期服务注册和进程管理、资源（CPU/内存）可配置、持久化存储。这种'在 Mac 上编辑，在容器内构建'的工作流消除了传统跨平台开发中的文件同步步骤。
  business_model: 直接冲击 Docker Desktop 在 macOS 上的商业模式（Docker Desktop 对大型企业收费），以及 OrbStack、Lima
    等第三方工具的用户基础。Apple 提供免费、原生集成的第一方方案，可能改变 macOS 开发者容器工具的选择格局，迫使第三方厂商在差异化功能上竞争而非收取平台接入费。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: Apple 将 Linux 容器虚拟机深度集成到 macOS 中，基于标准 OCI 镜像，支持 systemd 初始化系统、自动用户/家目录映射和持久化服务。从
    VC 视角看，长期复利逻辑清晰：第一，此举大幅强化 macOS 对开发者的生态锁效应——开发者越依赖 macOS 原生 Linux 环境，迁移到其他平台的切换成本越高，间接提升
    Mac 硬件复购率；第二，Apple 正在 commoditize 第三方付费容器工具（Docker Desktop、OrbStack）的核心价值主张，通过免费+原生集成挤压它们的生存空间，长期将削弱其定价权；第三，基于
    OCI 标准确保与整个容器生态兼容，不会形成专有锁定。但受限于这是一项平台功能而非独立公司实体，直接资本捕获能力有限，价值通过 Mac 销量间接变现，且 Linux
    容器虚拟化并非全新赛道（Docker、Multipass、UTM 等已有成熟方案）。综合评分 7.0：3-5 年后大概率成为 macOS 开发者标配基础设施，但非独立
    venture 投资标的。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- Apple
- Mac 开发者生态
- OCI 容器生态
competitive_casualty:
- Docker Desktop
- OrbStack
- Lima
- Colima
- UTM
market_opportunities:
- 开发者工具团队可围绕 container-machine 构建图形化管理界面和高级编排能力，填补命令行工具与可视化体验之间的空白
- CI/CD 服务商可利用该工具的轻量级特性优化 macOS runner 上的 Linux 测试环境启动速度，降低持续集成成本
- 企业内部可基于 container-machine 实现 macOS 开发人员的一键式多发行版测试环境，提升微服务和跨平台应用的开发效率
risk_matrix:
  regulatory: 无
  technological: Apple 对开发者工具的长期投入存在不确定性，历史上存在工具被弃用的先例；OrbStack、Lima、Docker Desktop
    等竞品的技术迭代可能让该工具在性能或生态集成上处于劣势
  competitive: 巨头入场风险显着——Apple 凭借 macOS 平台深度集成能力（自动用户映射、家目录挂载、进程管理器支持）直接冲击 OrbStack、Docker
    Desktop、UTM、Parallels 等现有容器/虚拟机方案的生态位，可能引发价格战或生态挤压
  ethical: 无
  additional:
  - macOS 平台锁定——该工具仅适用于 Apple 平台，无法在 Linux/Windows 开发环境中使用，团队跨平台一致性管理面临碎片化风险
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: apple/container
  canonical_name: apple/container
  url: https://github.com/apple/container
  positioning: 苹果在 GitHub 开源的 macOS 容器管理项目，提供基于标准 OCI 镜像的轻量级 Linux 环境创建与运行能力。
  technical_signal: 基于 OCI 镜像标准构建容器机器，支持镜像 init 系统和 systemd 服务注册，与 macOS 深度集成并自动共享宿主用户与家目录。
  adoption_signal: 由苹果官方在 GitHub 仓库 apple/container 中发布，标志着苹果在容器基础设施领域的一次重要战略布局。
  ecosystem_relevance: 填补了 macOS 原生轻量级 Linux 容器环境的空白，与 Docker Desktop、Lima 等方案形成差异化竞争格局。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 苹果官方首次推出系统级容器工具，有望改变 macOS 开发者的容器化工作流格局，其生态影响力、社区采纳进程与 Docker 竞争态势值得持续跟踪。
  risk_notes:
  - 项目处于早期开发阶段，功能完整性和生产环境稳定性尚未充分验证。
  - 用户基础和社区生态远不及 Docker 成熟，推广和标准化面临挑战。
  score: 8.0
  article_ids:
  - ce06dcdbb7372ccd
  evidence_snippets:
  - 该文档是苹果官方在 GitHub 仓库 apple/container 中发布的 Container Machine 功能说明，详细介绍了其用法和设计理念。
  - 容器机器的创建、运行和管理均通过 container 命令行工具完成，文档中提供了完整的 CLI 操作指令和输出示例。
- object_type: product
  name: Container Machine
  canonical_name: Container Machine
  url: null
  positioning: 基于 OCI 镜像的 macOS 原生轻量级 Linux 环境产品，提供自动用户映射与家目录共享的一体化开发体验。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - macOS 后端开发者
  - 跨平台应用开发者
  - 需要本地 Linux 测试环境的 DevOps 工程师
  product_signal: 提供编辑在 Mac、构建在容器内的无缝工作流，支持自动用户和家目录映射、多发行版并行测试及 systemd 长期服务注册。
  market_signal: 苹果官方推出的 macOS 容器产品，直接与 Docker Desktop、Lima 和 OrbStack 竞争，有望重塑开发者容器工具选择格局。
  differentiation: 模拟完整 Linux 环境而非单个应用，运行 init 系统并自动集成 macOS 用户体系，由苹果官方维护且与系统深度绑定。
  watch_reason: 苹果从系统层面直接构建容器化 Linux 环境方案，与第三方工具形成直接竞争，若成功集成进 macOS 生态将大幅影响开发者工作流选择。
  risk_notes:
  - 仅面向 macOS 平台推出，跨平台适用性和可移植性存在固有局限。
  - CLI 工具生态尚不成熟，与 Docker Compose 等主流编排工具的兼容性有待观察。
  score: 8.0
  article_ids:
  - ce06dcdbb7372ccd
  evidence_snippets:
  - Container Machine 提供与 macOS 无缝集成的 Linux 环境，基于标准 OCI 镜像构建，支持快速、轻量和持久化运行。
  - 容器机器自动将宿主的用户名和家目录映射到 Linux 环境中，开发者可在 macOS 上编辑代码，在容器中构建和运行应用。
  - 容器机器运行镜像的 init 系统，支持通过 systemctl 注册长期运行的后台服务，便于在 Mac 上测试真实 Linux 服务。
---

Container machine provides a highly integrated Linux environment that works seamlessly on your Mac. Container machines are fast, lightweight and persistent. They are based on standard OCI images that can be built and shared. Host integrations such as automatic user and home directory sharing provide quick and easy access to your Linux environment no matter where you are in a terminal.

Containers are typically modeled after an application. A container machine is modeled after a Linux environment. It runs the image's init system allowing you to register long running services or test your application under a process supervisor. A container machine automatically maps your username and home directory into the Linux environment. Your repositories and dotfiles are available on both platforms. Use editors and tools directly on macOS simultaneously building and running your application inside of the Linux environment.

**Edit on the Mac, build inside.**Your repo lives in`$HOME`

on macOS and is mounted at`/Users/<username>`

inside the container machine. Use your macOS editor or IDE; compile and run inside your container machine.**Use macOS-native tooling against Linux artifacts.**Profilers, screenshot tools, browsers, and GUI debuggers on your Mac all see the same files the container machine sees — there is no copy step between "I built it" and "I am inspecting it".**Real Linux services for testing.**Run a database or whatever your stack needs as a system service —`systemctl start postgresql`

works on images with`systemd`

installed.**One environment per target distro.**Create as many container machines as you have target distros —`alpine`

,`ubuntu`

,`debian`

. Each has the same`$HOME`

and the same dotfiles from your Mac. Quickly test your application in various distributions.

```
container machine create alpine:latest --name dev
container machine run -n dev whoami # your host username, not root
container machine run -n dev pwd # /home/<you> — your Mac home dir, mounted in
container machine run -n dev # interactive shell; cd into your repos in $HOME
```

`container machine run`

is how you get a shell or run a single command. If the container machine is stopped, `run`

boots it first.

With no command, `container machine run`

opens an interactive shell as a user that matches your host account:

`container machine run -n dev`

Pass a command to run it once and exit:

```
container machine run -n dev uname -a
container machine run -n dev -- cat /proc/cpuinfo
```

Pick a default container machine so you can drop the `-n`

flag:

```
container machine set-default dev
container machine run # operates on dev
```

```
container machine ls # list all container machines
container machine inspect dev # JSON detail for one
container machine stop dev # stop the container machine
container machine rm dev # delete, including its persistent storage
```

`container machine`

has the alias `m`

, so `m ls`

, `m run`

, etc. all work.

`container machine set`

updates configuration on disk. Changes take effect after the next stop and start:

```
container machine set -n dev cpus=4 memory=8G
container machine stop dev
container machine run -n dev -- nproc
```

Memory defaults to half of host memory. The home-mount can be `rw`

(default), `ro`

, or `none`

.

Any Linux image that includes `/sbin/init`

works as a container machine. For example, this Dockerfile builds an Ubuntu 24.04 container machine image with `systemd`

and common command-line tools:

```
FROM ubuntu:24.04
ENV container container
RUN apt-get update && \
apt-get install -y \
dbus systemd openssh-server net-tools iproute2 iputils-ping curl wget vim-tiny man sudo && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* && \
yes | unminimize
RUN >/etc/machine-id
RUN >/var/lib/dbus/machine-id
RUN systemctl set-default multi-user.target
RUN systemctl mask \
dev-hugepages.mount \
sys-fs-fuse-connections.mount \
systemd-update-utmp.service \
systemd-tmpfiles-setup.service \
console-getty.service
RUN systemctl disable \
networkd-dispatcher.service
RUN sed -i -e 's/^AcceptEnv LANG LC_\*$/#AcceptEnv LANG LC_*/' /etc/ssh/sshd_config
```

Build it and create a container machine from it:

```
container build -t local/ubuntu-machine:latest .
container machine create local/ubuntu-machine:latest --name ubuntu
```

By default, `container`

runs a built-in setup script on first boot to provision the user described above. To use your own setup instead, add an executable script at `/etc/machine/create-user.sh`

to the image. It runs once, as root, on first boot, with these variables set:

`CONTAINER_GID`

`CONTAINER_HOME`

`CONTAINER_MACHINE_ID`

`CONTAINER_UID`

`CONTAINER_USER`