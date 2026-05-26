---
title: janestreet/magic-trace
source: https://github.com/janestreet/magic-trace
author: []
published: ''
created: '2026-05-24'
description: 'magic-trace collects and displays high-resolution traces of what a process
  is doing magic-trace Overview magic-trace collects and displays high-resolution
  traces of what a process is doing. People have used it to: figure out why an application
  running in production handles some requests slowly while simultaneously handling
  a sea of uninteresting requests, look at what their code is actually doing instead
  of what they think it''s doing, get a history of what their application was doing
  before it crashed, instead of a mere stacktrace at that final instant, ...and much
  more! magic-trace: has 2%-10% overhead, doesn''t require application changes to
  use, traces every function call with ~40ns resolution, and renders a timeline of
  call stacks going back (a configurable) ~10ms. You use it like perf: point it to
  a process and off it goes. The key difference from perf is that instead of sampling
  call stacks throughout time, magic-trace uses Intel Processor Trace to snapshot
  a ring buffer of all control flow leading up to a chosen point in time[1]. Then,
  you can explore an interactive timeline of what happened. You can point magic-trace
  at a function such that when your application calls it, magic-trace takes a snapshot.
  Alternatively, attach it to a running process and detach it with Ctrl+C, to see
  a trace of an arbitrary point in your program. Testimonials "Magic-trace is one
  of the simplest command-line debugging tools I have ever used." Francis Ricci, Jane
  Street "Magic-trace is not just for performance. The tool gives insight directly
  into what happens in your program, when, and why. Consider using it for all your
  introspective goals!" Andrew Hunter, Jane Street I use perf a ton, and I think that
  both perf and magic-trace give perspectives that the other doesn''t. The benefit
  I got from magic-trace was entirely based on the fact that it works in slices at
  any zoom level, so I was able to see all the function calls that a 70ns function
  was performing, which was invisible in perf. Doug Patti, Jane Street more testimonials...
  Install Make sure the system you want to trace is supported. The constraints that
  most commonly trip people up are: VMs are mostly not supported, Intel only (Skylake[2]
  or later), Linux only. Grab a release binary from the latest release page. If downloading
  the prebuilt binary (not package), chmod +x magic-trace[3] If downloading the package,
  run sudo dpkg -i magic-trace*.deb Then, test it by running magic-trace -help, which
  should bring up some help text. Getting started Here''s a sample C program to try
  out. It''s a slightly modified version of the example in man 3 dlopen. Download
  that, build it with gcc demo.c -ldl -o demo, then leave it running ./demo. We''re
  going to use that program to learn how dlopen works. Run magic-trace attach -pid
  $(pidof demo). When you see the message that it''s successfully attached, wait a
  couple seconds and Ctrl+C magic-trace. It will output a file called trace.fxt.gz
  in your working directory. Open magic-trace.org, click "Open trace file" in the
  top-left-hand and give it the trace file generated in the previous step. That should
  have expanded into a trace. Zoom in until you can see an individual loop through
  dlopen/dlsym/cos/printf/dlclose. W zooms into wherever your mouse cursor is pointed
  (you''ll need to zoom in a bunch to see anything useful), S zooms out, A moves left,
  D moves right, and scroll wheel moves your viewport up and down the stack. You''ll
  only need to scroll to see particularly deep stack traces, it''s probably not useful
  for this example. Click and drag on the white space around the call stacks to measure.
  Plant flags by clicking in the timeline along the top. Using the measurement tool,
  measure how long it takes to run cos. On my screen it takes ~5.7us. Congratulations,
  you just magically traced your first program! In contrast to traditional perf workflows,
  magic-trace excels at hypothesis generation. For example, you might notice that
  taking 6us to run cos is a really long time! If you zoom in even more, you''ll see
  that there''s actually five pink "[untraced]" cells in there. If you re-run magic-trace
  with root and pass it -trace-include-kernel, you''ll see stacktraces for those.
  They''re page fault handlers! The demo program actually calls cos twice. If you
  zoom in even more near the end of the 6us cos call, you''ll see that the second
  call takes far less time and does not page fault. How to use it magic-trace continuously
  records control flow into a ring buffer. Upon some sort of trigger, it takes a snapshot
  of that buffer and reconstructs call stacks. There are two ways to take a snapshot:
  We just did this one: Ctrl+C magic-trace. If magic-trace terminates without already
  having taken a snapshot, it takes a snapshot of the end of the program. You can
  also trigger snapshots when the application calls a function. To do so, pass magic-trace
  the -trigger flag. -trigger ''?'' brings up a fuzzy-finding selector that lets you
  choose from all symbols in your executable, -trigger SYMBOL selects a specific,
  fully mangled, symbol you know ahead of time, and -trigger . selects the default
  symbol magic_trace_stop_indicator. Stop indicators are powerful. Here are some ideas
  for where you might want to place one: If you''re using an asynchronous runtime,
  any time a scheduler cycle takes too long. In a server, when a request takes a surprisingly
  long time. After the garbage collector runs, to see what it''s doing and what it
  interrupted. After a compiler pass has completed. You may leave the stop indicator
  in production code. It doesn''t need to do anything in particular, magic-trace just
  needs the name. It is just an empty, but not inlined, function. It will cost ~10us
  to call, but only when magic-trace actually uses it to take a snapshot. Documentation
  More documentation is available on the magic-trace wiki. Discussion Join us on Discord
  to chat synchronously, or the GitHub discussion group to do so asynchronously. Contributing
  If you''d like to contribute: read the build instructions, set up your editor, take
  a quick tour through the codebase, then hit up the issue tracker for a good starter
  project. Privacy policy magic-trace does not send your code or derivatives of your
  code (including traces) anywhere. magic-trace.org is a lightly modified fork of
  Perfetto, and runs entirely in your browser. As far as we can tell, it does not
  send your trace anywhere. If you''re worried about that changing one day, set up
  your own local copy of the Perfetto UI and use that instead. Acknowledgements Tristan
  Hume is the original author of magic-trace. He wrote it while working at Jane Street,
  who currently maintains it. Intel PT is the foundational technology upon which magic-trace
  rests. We''d like to thank the people at Intel for their years-long efforts to make
  it available, despite its slow uptake in the greater software community. magic-trace
  would not be possible without perfs extensive support for Intel PT. perf does most
  of the work in interpreting Intel PT''s output, and magic-trace likely wouldn''t
  exist were it not for their efforts. Thank you, perf developers. magic-trace.org
  is a fork of Perfetto, with minor modifications. We''d like to thank the people
  at Google responsible for it. It''s a high quality codebase that solves a hard problem
  well. The ideas behind magic-trace are in no way unique. We''ve written down a list
  of prior art that has influenced its design. perf can do this too, but that''s not
  how most people use it. In fact, if you peek under the hood you''ll see that magic-trace
  uses perf to drive Intel PT. ↩︎ Strictly speaking, anything newer than Broadwell,
  but this is not a platform we regularly test on, and timing resolution is worse
  (~1us). ↩︎ https://github.com/actions/upload-artifact/issues/38 ↩︎'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d4a7381fbdcf2f2b
source_type: community_discussion
tldr: Jane Street开源magic-trace，基于Intel PT实现纳秒级函数调用追踪与可视化。
objective_summary: Jane Street在GitHub开源了magic-trace，一款基于Intel Processor Trace的Linux进程追踪调试工具。无需修改应用代码，以2%-10%的低开销和约40ns分辨率记录所有函数调用，生成可交互的调用栈时间线，用于性能分析与根因定位。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Jane Street
  - Intel
  - Google
  technologies:
  - Intel Processor Trace
  - perf
  - Perfetto
  - magic-trace
  key_people:
  - Tristan Hume
  - Francis Ricci
  - Andrew Hunter
  - Doug Patti
key_logic_flow:
- magic-trace利用Intel Processor Trace持续将进程的所有控制流记录到环形缓冲区中，而非像perf那样对调用栈进行离散采样
- 用户可通过Ctrl+C手动触发快照，或通过-trigger标志指定符号/函数，当应用调用该函数时自动捕获快照
- 触发快照时，magic-trace从环形缓冲区中提取触发点前约10ms内的全部控制流，并重建完整的函数调用栈
- 生成的trace文件（trace.fxt.gz）可通过magic-trace.org（基于Perfetto的Web UI）打开，支持缩放、平移和耗时测量等交互式分析
- magic-trace不发送任何用户代码或追踪数据到外部，Web界面完全在浏览器本地运行
- 核心作者Tristan Hume在Jane Street工作期间开发了magic-trace，项目目前由Jane Street维护
impact_score:
  score: 4.5
  reason: magic-trace 是 Jane Street 开源的一款高质量 Linux 性能追踪工具，基于 Intel Processor Trace
    实现纳秒级函数调用追踪，无需修改应用代码。技术实现精巧（连续控制流记录 vs perf 的离散采样），对性能工程领域有实际价值。但该工具限定 Intel CPU
    + Linux 平台，且并非 AI 行业专属创新，属于优秀的开发者工具开源发布，改变局部调试实践而非行业范式。综合评估为 4.5 分——重要工具发布，局部影响力显著但行业波及面有限。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Intel PT 连续控制流记录替代采样式 profiling 的范式差异，以及约 40ns 分辨率下交互式调用栈时间线的调试体验
hype_assessment:
  level: low
  reason: README 和文档以技术细节和可复现示例为主，给出了具体的开销数据（2%-10%）、分辨率（~40ns）、平台限制（Intel Skylake+、Linux
    only、不支持大多数 VM），并提供了完整的命令行演示流程。通篇未使用'颠覆'、'革命性'等 PR 滥用词汇，引述均为 Jane Street 内部工程师的务实评价。
information_entropy: medium
domain_disruption:
  technical_innovation: 利用 Intel Processor Trace 将进程全部控制流连续记录到环形缓冲区，触发快照时提取触发点前约 10ms
    的完整控制流并重建调用栈——这与传统 perf 的离散采样有本质差异，实现了'任意缩放级别下的切片分析'能力，可观测到 70ns 级函数的内部调用细节。配合基于
    Perfetto 的浏览器端交互式可视化，形成了从采集到分析的闭环工具链。
  business_model: 纯开源工具，不涉及商业模式创新。对 Jane Street 而言，此举提升了其在系统工程领域的技术品牌影响力，类似 Google
    开源 perftools、Meta 开源 folly 的工程师品牌策略。对可观测性/SaaS 生态无直接冲击，但为 APM 厂商提供了 Intel PT 路线的技术验证参考。
engineering_complexity: production_ready
compound_value:
  score: 5.0
  reason: magic-trace 解决了系统性能工程中一个真实且持久的痛点——以极低开销获取函数级调用栈的全量追踪，而非采样式快照。其技术壁垒来自 Intel
    PT 硬件能力与环形缓冲区快照机制的工程化结合，竞品难以简单复制。但作为开源单点工具，它缺乏平台型产品的网络效应和数据飞轮：用户增长不会自动提升产品价值，也没有直接的收入模型。在
    AI 领域，它的价值是间接的——帮助优化 AI 推理引擎、模型服务基础设施的 CPU 侧性能，但不会直接改变 AI 模型能力或商业格局。3-5 年后它大概率仍是
    Linux 性能工程师工具箱中的重要选项，但不太可能成为 AI 行业的基础设施级基石。属于'有护城河的利基工具'而非'复合增长平台'。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Jane Street
- Intel
- Google
- Linux 性能工程社区
- 高性能 AI 推理基础设施团队
competitive_casualty:
- 商业级 APM/可观测性厂商（Datadog、Dynatrace 等 CPUMetrics 模块）
- AMD（Intel PT 独占形成开发者工具链偏好锁定）
- 传统采样型 profiler 工具（在与 magic-trace 重叠的使用场景中被替代）
market_opportunities:
- 量化交易与高性能计算团队可将 magic-trace 集成到内部性能回归测试流水线中，利用纳秒级调用栈时间线自动检测生产环境中偶发的延迟抖动根因，显著降低线上事故的MTTR（平均修复时间）
- 可观测性与APM厂商（如Datadog、New Relic）可借鉴 magic-trace 的Intel PT连续录制+触发快照机制，在商业化产品中构建「时间旅行调试」功能，填补传统采样与全量插桩之间的市场空白
- 性能工程师和基础设施SRE可将 magic-trace 作为个人技能栈的差异化工具，掌握基于硬件追踪的根因定位方法论，在高频交易、数据库内核、游戏引擎等延迟敏感领域建立竞争壁垒
risk_matrix:
  regulatory: 无
  technological: 强依赖Intel PT硬件特性（Skylake及以上、仅Intel CPU），AMD平台完全不可用，虚拟机环境支持有限；若Intel在未来架构中调整或废弃PT功能，该工具将面临根本性替代风险；且40ns分辨率依赖特定硬件能力，在云环境共享实例中可能不可靠
  competitive: 传统perf和eBPF生态已占据Linux性能分析主流心智，新兴的连续录制方案（如rr、Pernosco）也在争夺「时间旅行调试」赛道；Datadog、Grafana
    Pyroscope等商业可观测性平台若集成类似能力，将凭借已有用户基数形成生态挤压
  ethical: Intel PT可捕获进程的完整控制流数据，理论上可被恶意利用进行侧信道攻击或商业秘密逆向工程；在金融、医疗等强合规行业中，对生产环境进程的全量追踪可能触及数据隐私与审计边界
  additional:
  - 维护可持续性风险：magic-trace核心作者Tristan Hume已从Jane Street离职，项目长期维护依赖Jane Street内部资源分配，若该团队优先级调整可能导致项目停滞
  - 操作系统锁定风险：仅支持Linux，无法覆盖macOS（ARM架构）和Windows开发者群体，随着Apple Silicon在企业开发场景的渗透率提升，工具受众可能收窄
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

magic-trace collects and displays high-resolution traces of what a process is doing. People have used it to:

- figure out why an application running in production handles some requests slowly while simultaneously handling a sea of uninteresting requests,
- look at what their code is
*actually*doing instead of what they*think*it's doing, - get a history of what their application was doing before it crashed, instead of a mere stacktrace at that final instant,
- ...and much more!

magic-trace:

- has 2%-10% overhead,
- doesn't require application changes to use,
- traces
*every function call*with ~40ns resolution, and - renders a timeline of call stacks going back (a configurable) ~10ms.

You use it like `perf`

: point it to a process and off it goes. The key difference from `perf`

is that instead of sampling call stacks throughout time, magic-trace uses Intel Processor Trace to snapshot a ring buffer of *all control flow* leading up to a chosen point in time1. Then, you can explore an interactive timeline of what happened.

You can point magic-trace at a function such that when your application calls it, magic-trace takes a snapshot. Alternatively, attach it to a running process and detach it with `Ctrl`+`C`, to see a trace of an arbitrary point in your program.

"Magic-trace is one of the simplest command-line debugging tools I have ever used."


- Francis Ricci, Jane Street

"Magic-trace is not just for performance. The tool gives insight directly into what happens in your program, when, and why. Consider using it for all your introspective goals!"


- Andrew Hunter, Jane Street

I use perf a ton, and I think that both perf and magic-trace give perspectives that the other doesn't. The benefit I got from magic-trace was entirely based on the fact that it works in slices at any zoom level, so I was able to see all the function calls that a 70ns function was performing, which was invisible in perf.


- Doug Patti, Jane Street

-
Make sure the system you want to trace is supported. The constraints that most commonly trip people up are: VMs are mostly not supported, Intel only (Skylake

2or later), Linux only. -
Grab a release binary from the latest release page.

- If downloading the prebuilt binary (not package),
`chmod +x magic-trace`

3 - If downloading the package, run
`sudo dpkg -i magic-trace*.deb`


Then, test it by running

`magic-trace -help`

, which should bring up some help text. - If downloading the prebuilt binary (not package),

-
Here's a sample C program to try out. It's a slightly modified version of the example in

`man 3 dlopen`

. Download that, build it with`gcc demo.c -ldl -o demo`

, then leave it running`./demo`

. We're going to use that program to learn how`dlopen`

works. -
Run

`magic-trace attach -pid $(pidof demo)`

. When you see the message that it's successfully attached, wait a couple seconds and`Ctrl`+`C``magic-trace`

. It will output a file called`trace.fxt.gz`

in your working directory.

- Open magic-trace.org, click
*"Open trace file"*in the top-left-hand and give it the trace file generated in the previous step.

- That should have expanded into a trace. Zoom in until you can see an individual loop through
`dlopen`

/`dlsym`

/`cos`

/`printf`

/`dlclose`

.`W`zooms into wherever your mouse cursor is pointed (you'll need to zoom in a bunch to see anything useful),`S`zooms out,`A`moves left,`D`moves right, and- scroll wheel moves your viewport up and down the stack. You'll only need to scroll to see particularly deep stack traces, it's probably not useful for this example.


- Click and drag on the white space around the call stacks to measure. Plant flags by clicking in the timeline along the top. Using the measurement tool, measure how long it takes to run
`cos`

. On my screen it takes ~5.7us.

Congratulations, you just magically traced your first program!

In contrast to traditional `perf`

workflows, magic-trace excels at hypothesis generation. For example, you might notice that taking 6us to run `cos`

is a really long time! If you zoom in even more, you'll see that there's actually five pink "[untraced]" cells in there. If you re-run magic-trace with root and pass it `-trace-include-kernel`

, you'll see stacktraces for those. They're page fault handlers! The demo program actually calls `cos`

twice. If you zoom in even more near the end of the 6us `cos`

call, you'll see that the second call takes *far* less time and does not page fault.

magic-trace continuously records control flow into a ring buffer. Upon some sort of trigger, it takes a snapshot of that buffer and reconstructs call stacks.

There are two ways to take a snapshot:

We just did this one: `Ctrl`+`C` magic-trace. If magic-trace terminates without already having taken a snapshot, it takes a snapshot of the end of the program.

You can also trigger snapshots when the application calls a function. To do so, pass magic-trace
the `-trigger`

flag.

`-trigger '?'`

brings up a fuzzy-finding selector that lets you choose from all symbols in your executable,`-trigger SYMBOL`

selects a specific, fully mangled, symbol you know ahead of time, and`-trigger .`

selects the default symbol`magic_trace_stop_indicator`

.

Stop indicators are powerful. Here are some ideas for where you might want to place one:

- If you're using an asynchronous runtime, any time a scheduler cycle takes too long.
- In a server, when a request takes a surprisingly long time.
- After the garbage collector runs, to see what it's doing and what it interrupted.
- After a compiler pass has completed.

You may leave the stop indicator in production code. It doesn't need to do anything in particular, magic-trace just needs the name. It is just an empty, but not inlined, function. It will cost ~10us to call, but *only when magic-trace actually uses it to take a snapshot*.

More documentation is available on the magic-trace wiki.

Join us on Discord to chat synchronously, or the GitHub discussion group to do so asynchronously.

If you'd like to contribute:

- read the build instructions,
- set up your editor,
- take a quick tour through the codebase, then
- hit up the issue tracker for a good starter project.

magic-trace does not send your code or derivatives of your code (including traces) anywhere.

magic-trace.org is a lightly modified fork of Perfetto, and runs entirely in your browser. As far as we can tell, it does not send your trace anywhere. If you're worried about that changing one day, set up your own local copy of the Perfetto UI and use that instead.

Tristan Hume is the original author of magic-trace. He wrote it while working at Jane Street, who currently maintains it.

Intel PT is the foundational technology upon which magic-trace rests. We'd like to thank the people at Intel for their years-long efforts to make it available, despite its slow uptake in the greater software community.

magic-trace would not be possible without `perf`

s extensive support for Intel PT. `perf`

does most of the work in interpreting Intel PT's output, and magic-trace likely wouldn't exist were it not for their efforts. Thank you, `perf`

developers.

magic-trace.org is a fork of Perfetto, with minor modifications. We'd like to thank the people at Google responsible for it. It's a high quality codebase that solves a hard problem well.

The ideas behind magic-trace are in no way unique. We've written down a list of prior art that has influenced its design.