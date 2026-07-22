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