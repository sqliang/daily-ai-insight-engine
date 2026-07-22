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