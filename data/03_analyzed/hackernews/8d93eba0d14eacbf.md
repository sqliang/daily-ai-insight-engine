---
title: Epoll vs. io_uring in Linux
source: https://sibexi.co/posts/epoll-vs-io_uring/
author:
- '[[Sibexico]]'
published: '2026-06-20'
created: '2026-06-21'
description: 'Article URL: https://sibexi.co/posts/epoll-vs-io_uring/ Comments URL:
  https://news.ycombinator.com/item?id=48613872 Points: 158 # Comments: 37'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 8d93eba0d14eacbf
source_type: community_discussion
tldr: Linux 中 epoll 与 io_uring 两种异步 I/O 机制的对比，io_uring 通过减少系统调用显著提升性能。
objective_summary: 作者在构建反向代理 TinyGate 的过程中，从 worker 模型切换到 epoll，最终重写为 io_uring。文章从架构原理、系统调用开销、代码示例等维度对比了
  epoll 的 readiness 模型与 io_uring 的 completion 模型，指出 io_uring 将每次
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - epoll
  - io_uring
  - liburing
  - SQPOLL
  - IORING_SETUP_SQPOLL
  - IORING_OP_SEND_ZC
  key_people: []
key_logic_flow:
- epoll 采用 readiness 模型，只通知用户态 I/O 就绪，用户态仍需调用 read()/write() 完成操作，每次 I/O 事件至少需要两次系统调用（epoll_wait
  + read/write），每次系统调用都导致用户态/内核态上下文切换。
- io_uring 采用 completion 模型，通过用户态与内核态共享内存的环形缓冲区（ring buffer）传递提交和完成事件，不再需要每笔 I/O 单独调用系统调用。
- io_uring 的默认模式仍需要 io_uring_enter() 通知内核检查提交队列，但一次调用可以提交一批操作并收割一批完成事件；启用 IORING_SETUP_SQPOLL
  后可由内核线程持续轮询提交队列，稳态下接近零系统调用。
- io_uring 支持零拷贝 I/O：通过 io_uring_register_buffers() 预注册缓冲区避免内存重映射，IORING_OP_SEND_ZC（内核
  6.0+）可跳过数据拷贝到内核缓冲区的步骤。
- SQPOLL 模式的代价是在提交队列为空时内核线程仍会空转消耗 CPU，可通过 sq_thread_idle 设置空闲超时使其休眠。
- io_uring 自 Linux 内核 5.1（2019 年）起可用，对于在新系统上从零开始的项目，io_uring 是异步 I/O 的首选方案。
impact_score:
  score: 3.5
  reason: 该文章是一篇高质量的社区技术深度对比，详细阐述了 epoll 与 io_uring 的架构差异、系统调用开销和代码实践。但 io_uring 自
    Linux 内核 5.1（2019年）发布以来已存在多年，文章并未宣布任何新的技术突破或行业事件。对于 AI 基础设施工程师而言，这是一篇有参考价值的教育性内容，但不会改变当前行业竞争格局。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: io_uring 将每次 I/O 操作的系统调用从两次减少为每批次一次甚至接近零（SQPOLL 模式），对高并发网络服务有显著的性能提升
hype_assessment:
  level: low
  reason: 文章没有使用'颠覆'、'革命性'等 PR 术语。作者从 worker 模型→epoll→io_uring 的实际迁移经历出发，提供了完整的 C
    代码示例对比，客观说明了两种模型的架构差异（readiness vs completion），并且明确指出了 SQPOLL 模式的 CPU 空转代价和 sq_thread_idle
    空闲超时机制等 trade-off，是典型的干货型技术文章。
information_entropy: high
domain_disruption:
  technical_innovation: io_uring 通过用户态与内核态共享内存的环形缓冲区（ring buffer）实现 completion 模型，将每次
    I/O 所需的系统调用从两次（epoll_wait + read/write）降为每批次一次或接近零（SQPOLL 模式），并且支持预注册缓冲区（io_uring_register_buffers）和零拷贝网络发送（IORING_OP_SEND_ZC），是
    Linux 异步 I/O 基础设施层面的范式改进。
  business_model: 无
engineering_complexity: infrastructure
compound_value:
  score: 8.5
  reason: io_uring 自 Linux 5.1（2019年）进入内核以来已稳定演进7年以上，并非短期热点。它从根本上改变了 Linux 异步 I/O
    的架构范式——从 epoll 的 readiness 模型（每笔 I/O 至少两次系统调用）转向 completion 模型（共享内存环形缓冲区实现批处理提交/收割，SQPOLL
    下稳态近乎零系统调用）。这一改进对所有 I/O 密集型基础设施产生结构性性能提升：数据库（PostgreSQL 15+、MySQL 8.0、ScyllaDB）、反向代理（NGINX、HAProxy、Cloudflare
    Pingora）、键值存储（RocksDB）、消息队列。复利效应体现在：应用一旦完成迁移，后续内核版本持续优化（如 IORING_OP_SEND_ZC 零拷贝网络发送）自动带来性能增益，无需额外适配投入。3-5
    年后 io_uring 将成为所有新 Linux 系统项目的默认异步 I/O 层，其基础设施地位等效于当年 epoll 替代 select/poll 的进程。风险点在于老旧系统（<5.1
    内核）无法使用，以及 SQPOLL 空闲时 CPU 空转代价需工程权衡，但长期趋势明确。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- Cloudflare
- ScyllaDB
- PostgreSQL 社区
- MySQL 社区 (Oracle)
- NGINX
- AWS (Nitro 及 EC2 实例)
competitive_casualty:
- 基于 DPDK 内核旁路方案的传统中间件
- 依赖 epoll 架构且无力重构的 Legacy 系统
market_opportunities:
- 构建高性能 AI 推理网关和模型代理服务的基础设施团队，可基于 io_uring 重构核心 I/O 路径，显著降低服务端延迟和系统调用开销，提升整体吞吐量
- 云原生和边缘计算平台可将 io_uring 与 SQPOLL 结合，为高并发数据管道（如日志采集、消息队列桥接、实时特征工程）提供接近零系统调用的 I/O 层，形成性能差异化竞争壁垒
- 面向 Linux 系统编程的开源库和开发者工具（如 io_uring 的 Rust/Go 绑定、性能分析套件）存在商业化机会，可填补生产环境中 epoll 迁移到
  io_uring 的中间件空白
risk_matrix:
  regulatory: 无
  technological: io_uring 需要 Linux 内核 5.1+，零拷贝特性（IORING_OP_SEND_ZC）需要 6.0+，无法在老旧内核或非
    Linux 平台上使用；SQPOLL 模式在队列空闲时内核线程空转消耗 CPU，需要精细的 idle timeout 配置以避免资源浪费
  competitive: 采用 epoll 的系统（如早期的反向代理、API 网关）在极端高并发场景下性能劣势明显，可能被采用 io_uring 的竞品在基准测试和用户感知层面拉开差距，形成技术代差
  ethical: 无
  additional: []
confidence:
  impact: high
  compound: high
  hype: low
actionable_insight: deep_dive
---

# epoll vs io_uring in Linux

First, I want to tell you how exactly I got to this point and why I started researching different options for handling asynchronous I/O on Linux… Last year, my students and I built a reverse proxy server called TinyGate. It was super simple, worker-based, and it basically worked well. Of course, I didn’t expect it to be very fast, but it was an educational project, and since we’d made a real, kind of production-ready tool, I was really proud of it. But my students weren’t as happy as I was - they wanted to build something genuinely useful, and they were really disappointed that our “product” had strong architectural limits and couldn’t outperform titans like nginx and haproxy. So they literally forced me to research together how those tools work under the hood and how to handle asynchronous I/O to cut down on the heavy overhead… Long story short, we made a second version of TinyGate, based on epoll. It still lost to nginx/haproxy in benchmarks, but it had a dramatic performance boost compared to the first version. But epoll isn’t perfect either (as I’ll explain below), and we eventually switched to io_uring, which led to a full rewrite of our project from scratch, again… So it’s a really interesting topic, and today I’ll share an overview of the two queueing systems Linux gives you for asynchronous I/O.

When I just started developing for Linux, epoll was a new feature, and basically it had no alternatives. Everyone used it to manage asynchronous execution - there was no other choice. The problem is, epoll relies heavily on syscalls: it tells you when I/O is possible, but you still have to call read()/write() yourself afterward - that’s two syscalls per I/O event, on top of the one-time epoll_ctl registration. Each of these syscalls causes a context switch between user and kernel mode, which creates HUGE overhead once you’re handling a lot of connections. But we have a solution! About 17 years after epoll landed in the Linux kernel (2002), io_uring appeared (2019)! Instead of telling you when I/O is possible, it tells you when I/O is done - no polling loop, and far less associated syscalls.

The kernel consumes submissions from memory shared between your app and the kernel, and posts completions back into that same shared memory - both live in ring buffers, hence the name. The catch: by default you still have to call `io_uring_enter()`

to tell the kernel “go check the submission queue” - but one call can submit a whole batch of operations and reap a whole batch of completions, instead of one syscall pair per operation like with epoll + read. If you want close to zero syscalls during steady state, there’s `IORING_SETUP_SQPOLL`

, which spins up a dedicated kernel thread that polls the submission queue for you - at the cost of that thread burning CPU (more on this below).

Basic architecture: as I said before, epoll notifies you when I/O is possible, io_uring notifies you when I/O is done. Where epoll makes every I/O operation cross the kernel boundary, io_uring lets you pay a small “setup fee” once (creating the ring) plus a per-batch fee (the `io_uring_enter()`

call) instead of a fee per operation. So instead of a syscall pair per I/O, you get a syscall per batch of I/Os - or, with SQPOLL, close to none at all. As you can see, with a ton of I/O happening, this saves a lot of syscalls.

On relatively new systems where io_uring is supported (kernel v5.1+, released in 2019), there’s often not much reason to reach for epoll. The shift from a readiness model to a completion model is a huge architectural change - it moves a big part of the work out of your application and into the kernel.

Of course, I won’t leave you without some code showing how both systems work. We’ll use C. (The io_uring example uses liburing, the userspace helper library - install it via `liburing-dev`

/`liburing-devel`

, or drop down to the raw `io_uring_setup`

/`io_uring_enter`

syscalls if you want zero dependencies.)

Let’s make a simple example of how epoll works. We’ll create the instance, register a file descriptor (stdin, in our case), and process the incoming event.

As you can see, this example uses three syscalls in total: `epoll_ctl`

(a one-time registration), then `epoll_wait`

and `read`

for the event - so two syscalls per actual I/O event, like I mentioned above. The code itself is pretty easy to follow.

Now let’s do the same thing with io_uring instead of epoll.

What can we see here?

- Similar instance creation step.
- No epoll_ctl registration step needed.
- No readiness check needed before submission.
- No separate read() call at completion.

Yeah, io_uring takes way fewer resources for this - though, as noted above, there’s still one `io_uring_enter()`

call hiding inside `io_uring_submit()`

and `io_uring_wait_cqe()`

unless you’re running with SQPOLL.

When you test these examples, keep in mind that for the sake of simplicity, some important parts are missing. For example, it will block forever if `stdin`

never produces any data, and the io_uring example skips checking for a `NULL`

sqe (which `io_uring_get_sqe()`

can return if the submission queue is full).

**Zero-copy.**For real zero-copy I/O, register your buffers ahead of time with`io_uring_register_buffers()`

- this avoids the kernel re-mapping memory on every single operation. For network sends specifically, look at`IORING_OP_SEND_ZC`

(kernel 6.0+ needed), which skips copying the buffer into the kernel entirely.**SQPOLL uses CPU.**Even when your queue is empty,`IORING_SETUP_SQPOLL`

keeps a kernel thread spinning and polling, which burns CPU. There’s an idle timeout (`sq_thread_idle`

) after which it backs off to sleeping, but it’s not free.**Asynchronous error handling.**Errors come back (and must be handled) asynchronously, as part of the`cqe`

’s`res`

field - not as a direct return value like a normal synchronous syscall.

io_uring is the new standard for async I/O in the modern Linux world, and honestly, I don’t see much reason to still reach for epoll on a system that has it. For a from-scratch project on a modern Linux server, like our TinyGate rewrite, io_uring is absolutely the way to go. I’m a die-hard supporter of dropping support for old systems as soon as it’s reasonable - if you’re still running a kernel released more than 7 years ago, in my opinion, that’s not a great idea…