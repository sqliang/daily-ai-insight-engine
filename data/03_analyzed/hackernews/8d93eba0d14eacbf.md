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
tldr: 本文对比了 Linux 的两种异步 I/O 机制 epoll 和 io_uring，介绍了作者基于两者三次重写 TinyGate 反向代理服务器的经历。epoll
  采用就绪通知模型，每次 I/O 需两次系统调用；io_uring 采用完成通知模型，通过共享环形缓冲区实现批量 I/O，大幅减少系统调用次数。
objective_summary: 一位教师作者与学生们构建了反向代理服务器 TinyGate，因架构受限先后基于 epoll 和 io_uring 两次完全重写。文章从架构层面对比了
  epoll（2002 年加入内核，就绪通知模型，每次 I/O 事件需要 epoll_wait 加 read/write 两次系统调用）和 io_uring（2019
  年内核 5.1+ 引入，完成通知模型，通过内核与用户态共享的环形缓冲区实现批量提交与收割）。作者提供了两种机制的 C 语言代码示例，并指出在支持 io_uring
  的现代 Linux 系统上，新项目应优先选择 io_uring 而非 epoll。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - epoll
  - io_uring
  - Linux
  - SQPOLL
  - liburing
  - IORING_OP_SEND_ZC
  key_people: []
key_logic_flow:
- 作者与学生们构建了名为 TinyGate 的反向代理服务器，因架构限制性能远不及 nginx 和 haproxy，随后基于 epoll 重写了第二版。
- 第二版 TinyGate 性能大幅提升但基准测试仍不及 nginx 和 haproxy，团队最终切换到 io_uring 并从头完全重写了项目。
- epoll 采用就绪通知模型，每次 I/O 事件需要两次系统调用（epoll_wait 通知就绪 + read/write 执行读写），高并发下上下文切换开销巨大。
- io_uring 于 2019 年在 Linux 内核 5.1 版本中引入，采用完成通知模型，通过共享环形缓冲区实现单次系统调用批量提交和收割多笔 I/O 操作。
- io_uring 的 SQPOLL 模式启动专用内核线程轮询提交队列，稳态下可接近零系统调用，但空闲时仍会额外消耗 CPU 资源。
- io_uring 还支持预注册缓冲区实现零拷贝 I/O（需内核 6.0+ 的 IORING_OP_SEND_ZC）和异步错误处理，作者认为现代 Linux 新项目应优先选用。
extract_result: success
object_mentions:
- object_type: project
  name: TinyGate
  canonical_name: TinyGate
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者与学生们构建了一款名为 TinyGate 的反向代理服务器，它是一个教育项目但达到了生产就绪水平。
  - 第一版 TinyGate 因架构限制无法超越 nginx 和 haproxy，团队基于 epoll 重写了第二版获得大幅性能提升。
  - 团队最终切换到 io_uring 并从头完全重写了整个 TinyGate 项目，作者认为这是现代 Linux 上构建新项目的正确选择。
  article_id: 8d93eba0d14eacbf
- object_type: project
  name: liburing
  canonical_name: liburing
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - io_uring 的代码示例使用了 liburing 用户空间辅助库，可通过 liburing-dev 或 liburing-devel 软件包安装，也可选择直接使用原始系统调用。
  article_id: 8d93eba0d14eacbf
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
object_insights:
- object_type: project
  name: TinyGate
  canonical_name: TinyGate
  url: null
  positioning: TinyGate 是一款基于 io_uring 实现的反向代理服务器，从教育项目起步历经三次架构迭代，旨在探索现代 Linux 异步
    I/O 在高性能代理场景中的应用。
  technical_signal: 项目从 worker 模型演进到 epoll 再切换到 io_uring，验证了完成通知模型相比就绪通知模型在减少系统调用方面的架构优势。
  adoption_signal: 基于 io_uring 的第三版在 benchmark 中仍不及 nginx/haproxy，但相比前两版有质的性能飞跃，证明了
    io_uring 在生产场景的潜力。
  ecosystem_relevance: 作为 io_uring 在反向代理领域的实践案例，为开发者从 epoll 迁移到 io_uring 提供了 C 语言代码参考和架构设计参考。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: TinyGate 完整记录了从传统 epoll 到 io_uring 的迁移路径和架构决策，是理解现代 Linux 异步 I/O 选型的宝贵实践案例，值得持续跟踪其性能优化进展。
  risk_notes:
  - TinyGate 在基准测试中仍不及 nginx 和 haproxy 等成熟方案，性能差距的根因尚不明确。
  - 项目定位为教育项目，缺乏长期维护承诺和社区生态支持，可持续性存疑。
  score: 5.0
  article_ids:
  - 8d93eba0d14eacbf
  evidence_snippets:
  - 作者与学生们构建了一款名为 TinyGate 的反向代理服务器，它是一个教育项目但达到了生产就绪水平。
  - 第一版 TinyGate 因架构限制无法超越 nginx 和 haproxy，团队基于 epoll 重写了第二版获得大幅性能提升。
  - 团队最终切换到 io_uring 并从头完全重写了整个 TinyGate 项目，作者认为这是现代 Linux 上构建新项目的正确选择。
- object_type: project
  name: liburing
  canonical_name: liburing
  url: null
  positioning: liburing 是 io_uring 的用户空间辅助库，封装了内核原始系统调用，为开发者提供更简洁的异步 I/O 编程接口。
  technical_signal: 通过 liburing 可避免直接使用 io_uring_setup/io_uring_enter 等原始系统调用，大幅降低
    io_uring 的使用门槛。
  adoption_signal: liburing 作为官方推荐的 io_uring 用户态库，可通过 liburing-dev/liburing-devel
    软件包安装，广泛用于高性能 I/O Linux 应用。
  ecosystem_relevance: liburing 是 io_uring 生态中重要的基础组件，简化了异步 I/O 编程模型，是连接内核能力与应用开发的关键桥梁。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: liburing 作为 io_uring 生态的标准用户空间库，其演进方向直接影响 Linux 高性能 I/O 应用的开发体验和生态繁荣程度。
  risk_notes:
  - liburing 依赖内核 io_uring 支持（v5.1+），在老旧 Linux 系统上不可用，限制了适用范围。
  score: 5.0
  article_ids:
  - 8d93eba0d14eacbf
  evidence_snippets:
  - io_uring 的代码示例使用了 liburing 用户空间辅助库，可通过 liburing-dev 或 liburing-devel 软件包安装，也可选择直接使用原始系统调用。
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