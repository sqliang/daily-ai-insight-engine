---
title: 'Scriptc by Vercel: TypeScript-to-Native compiler, no JavaScript engine in
  binary'
source: https://github.com/vercel-labs/scriptc
author:
- '[[maxloh]]'
published: '2026-07-26'
created: '2026-07-27'
manifest_dates:
- '2026-07-27'
description: 'Article URL: https://github.com/vercel-labs/scriptc Comments URL: https://news.ycombinator.com/item?id=49063175
  Points: 168 # Comments: 86'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0dadaefdea9260e5
source_type: community_discussion
tldr: Vercel Labs 发布 Scriptc，一个 TypeScript 到原生可执行文件的编译器，生成的二进制文件不包含 Node 或 V8 等 JavaScript
  引擎，启动时间约 2.4ms，静态二进制体积 170-200KB，内存占用 1-4MB。
objective_summary: Vercel Labs 于 2026 年 7 月 29 日在 GitHub（vercel-labs/scriptc）发布了 Scriptc
  编译器。该工具将普通 TypeScript 代码编译为原生可执行文件，内部不含任何 JavaScript 引擎（默认静态编译模式），通过 clang 生成机器码。Scriptc
  支持 TypeScript 大部分语言特性、标准库、Node.js API 和 WHATWG Web 子集，并通过差异测试（与 Node 字节级对比）与内存安全检测保障正确性。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Vercel
  - Vercel Labs
  technologies:
  - TypeScript
  - LLVM
  - quickjs-ng
  - AddressSanitizer
  - mbedTLS
  key_people: []
key_logic_flow:
- Scriptc 将普通 TypeScript 编译为原生可执行文件，二进制中不包含 Node.js 或 V8 等 JavaScript 引擎，但行为与 Node
  逐字节一致。
- Scriptc 分为三种处理模式：编译为静态原生代码（默认）、通过嵌入的 quickjs-ng 引擎动态执行（--dynamic）、以及拒绝编译并给出具体错误码。
- Scriptc 的静态编译覆盖了 TypeScript 核心语言特性、标准库、Node.js API（fs、http、crypto、net 等）以及 WHATWG
  Web 子集（fetch、Headers、AbortSignal）。
- Scriptc 的基准测试显示启动时间约 2.4ms、静态二进制大小 170-200KB、典型内存占用 1-4MB，均显著优于 Node.js。
- Scriptc 通过差异测试（800+ 测试用例在 Node 和原生二进制下比对输出）和 AddressSanitizer 内存安全检测两个通道保障正确性。
- Scriptc 支持 npm 依赖（通过 --dynamic 模式），在构建时将依赖的 JS 代码嵌入二进制，运行时不再读取 node_modules。
object_mentions:
- object_type: project
  name: vercel-labs/scriptc
  canonical_name: vercel-labs/scriptc
  url: https://github.com/vercel-labs/scriptc
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Scriptc 是 Vercel Labs 开源的 TypeScript 到原生可执行文件编译器，生成的二进制文件不包含任何 JavaScript 引擎。
  - Scriptc 支持将普通 TypeScript 代码编译为原生二进制，行为与 Node 逐字节一致，无需修改代码或添加注解。
  - Scriptc 的基准测试显示启动时间约 2.4ms，静态二进制大小 170-200KB，典型内存占用 1-4MB。
  article_id: 0dadaefdea9260e5
extract_result: success
impact_score:
  score: 7.8
  reason: Scriptc 是近年来 TypeScript/JavaScript 生态中最具突破性的工程创新之一。它将 TypeScript 直接编译为原生二进制，彻底移除了
    Node.js/V8 运行时依赖，启动时间从 ~47ms 降至 ~2.4ms（20x 提升），内存占用从 67-116MB 降至 1-4MB（~30x 缩减），静态二进制仅
    170-200KB。这直接挑战了 Node.js、Deno、Bun 等运行时统治了十多年的 JS 执行范式。对云函数/边缘计算场景，冷启动成本和资源消耗的降低具有颠覆性——如果成熟，Serverless
    函数的经济模型可能重构。然而，目前仍处于 vercel-labs 实验阶段，仅原生支持 macOS arm64，静态编译覆盖并非 100% TypeScript（约
    99% 可静态化），npm 依赖需 --dynamic 模式退回到 quickjs-ng 引擎，广泛的生产级验证仍需时间。综合而言，这是一个技术范式层面的创新，但当前阶段属于
    '发布会冲击波' 而非 '行业立即转向'，因此打 7.8 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: TypeScript 零运行时编译成原生二进制的可行性及与 Node.js 的字节级兼容性
hype_assessment:
  level: low
  reason: 项目 README 展示了对自身局限性的诚实披露：明确标注了三层编译模式（静态/动态/拒绝），对无法静态编译的构造给出具体错误码和改写建议，详细记录了与
    Node.js 的刻意偏离点（几十处，均编号且不静默偏离），并提供了 'scriptc coverage' 工具让用户评估静态编译覆盖率。这种技术透明度和严谨的文档风格与典型的
    PR 包装截然不同。800+ 差异测试 + AddressSanitizer 内存安全检测的双重验证机制也表明工程质量过硬。没有出现 '颠覆'、'革命性'
    等 PR 词汇的滥用。
information_entropy: high
domain_disruption:
  technical_innovation: TypeScript 到原生机器码的直接编译技术栈：通过 tsc 完成解析和类型检查，经自研 IR 降级为 C 代码再由
    clang 编译为原生二进制。核心创新在于对 JS 语义（UTF-16 精确字符串、闭包捕获、async/await 栈式纤程、异常 finally 语义、generics
    单态化、discriminated union 基于 TypeScript narrowing 的标记值表示）的执行级精确还原，同时通过 difftest（与
    Node 字节级对比）和 AddressSanitizer 两个通道保障语义保真度。'comptime' 编译时求值和对 JSON.parse as 的运行时校验类型守卫也属于编译器级别的创新。
  business_model: 对云函数和边缘计算平台的成本结构有深远影响。当前 Serverless 平台（Vercel Functions、AWS Lambda
    等）的冷启动和常驻内存成本主要由 Node.js 运行时开销驱动。Scriptc 如果投入生产，Vercel Functions 可以以接近原生二进制的方式运行
    TypeScript 代码，单实例内存占用从 ~100MB 级降至 ~MB 级，启动时间从 ~50ms 降至 ~2ms，这意味着同一台服务器可承载数量级更多的函数实例，函数计算定价模型可能随之重构。Vercel
    将 Node 生态的开发者体验与原生编译的性能优势结合，可能成为 Serverless 平台差异化竞争的关键筹码。
engineering_complexity: prototype
compound_value:
  score: 8.0
  reason: Scriptc 的长期复利价值极高，核心逻辑有三层：第一，性能红利随规模放大——启动时间从 Node 的 47ms 降至 2.4ms、内存占用从
    67-116MB 降至 1-4MB、二进制体积从 60-100MB 降至 170KB，这些指标在边缘计算和 Serverless 场景下直接转化为更低的冷启动成本和更高的部署密度，每多一个用户迁移，Vercel
    的边际基础设施成本就下降一档。第二，兼容性网络效应——Scriptc 通过差异测试（800+ 用例与 Node 逐字节比对）建立了信任基础，随着覆盖的 Node
    API 和 npm 生态面扩大，开发者迁移门槛持续降低，形成越多人用越多人敢用的正循环。第三，平台锁定效应——Scriptc 不仅是独立编译器，更是 Vercel
    在 Fluid Compute 之上的战略差异化能力。一旦部署流程与 Scriptc 深度绑定（build-time 编译、comptime 元编程、FFI
    原生扩展），用户的迁移成本将指数级上升。风险在于：Vercel Labs 项目阶段意味着技术成熟度和长期维护承诺仍待验证；--dynamic 模式下嵌入 quickjs-ng
    约 620KB 的开销在极端边缘场景仍是隐患；且 Deno/Bun 也在快速进化，竞争格局未定。综合而言，若能跨越从实验室项目到主流基础设施的鸿沟，Scriptc
    有望在 3-5 年后成为 TypeScript 服务端部署的默认范式。
value_capture_layer: cloud_platform
moat_impact: creates_new_moat
key_beneficiaries:
- Vercel
- TypeScript 开发者生态
- Edge/Serverless 基础设施提供商
competitive_casualty:
- Node.js 传统运行时
- Bun
- Deno
- Go/Rust 在 TypeScript 适用场景的替代方案
market_opportunities:
- 利用 Scriptc 的毫秒级启动和极低内存占用（1-4MB），为 Serverless/Edge 计算场景构建超轻量函数，显著降低冷启动延迟和资源成本，尤其适合
  Vercel、AWS Lambda 等 FaaS 平台
- 使用 Scriptc 将 TypeScript 编写的 CLI 工具编译为单个原生可执行文件分发，消除用户需预装 Node.js 运行时的门槛，终端体验接近 Go/Rust
  系工具但保留 TypeScript 开发效率
- 基于 Scriptc 静态编译的 170-200KB 二进制产物，优化 Docker 镜像体积和 IoT/嵌入式设备的 TypeScript 部署方案，适用于资源敏感的微服务和边缘节点场景
risk_matrix:
  regulatory: 无
  technological: Scriptc 静态编译仅覆盖 TypeScript 语言子集（示例中约 99%），复杂动态特性（any 类型、npm 依赖运行时行为）需
    --dynamic 模式嵌入 QuickJS-ng 引擎，带来功能一致性和性能折衷风险；依赖 LLVM/clang 工具链，Linux/Windows 交叉编译成熟度有待验证
  competitive: 面临 Bun 运行时、Deno compile、Node.js SEA（Single Executable Application）等多条技术路线的直接竞争，且
    Go/Rust 在原生二进制编译领域已有成熟生态和广泛实践
  ethical: 无
  additional:
  - 与 Vercel 平台及 LLVM 工具链强绑定，长期采用可能带来技术栈锁定风险
  - --dynamic 模式下嵌入 npm 依赖可能增大攻击面并增加安全审计复杂度
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: vercel-labs/scriptc
  canonical_name: vercel-labs/scriptc
  url: https://github.com/vercel-labs/scriptc
  positioning: Scriptc 是 Vercel Labs 开源的 TypeScript 原生编译器，将普通 TypeScript 编译为不含任何 JS
    引擎的静态可执行文件，启动约 2.4ms，二进制仅 170-200KB。
  technical_signal: Scriptc 通过 clang 生成机器码，采用差异测试和 AddressSanitizer 双重保障，支持 TypeScript
    大部分语言特性和 Node.js API 的原生编译。
  adoption_signal: Scriptc 已通过 npm 开源发布，支持全局安装，当前主要面向 macOS arm64，Linux 和 Windows
    通过交叉编译验证。
  ecosystem_relevance: Scriptc 填补了 TypeScript 原生编译的空白，为 Node.js 生态提供了零运行时部署路径，对 Serverless
    和边缘计算场景意义重大，可能重塑 JS 部署形态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Scriptc 代表了 TypeScript 从解释执行走向原生编译的重要技术方向，零运行时设计对 Serverless、边缘计算和容器化部署有颠覆性潜力，是
    Vercel 生态的重要技术布局，值得持续跟踪其生态进展和采用情况。
  risk_notes:
  - Scriptc 目前主要支持 macOS arm64，Linux 和 Windows 依赖交叉编译，跨平台成熟度有待验证。
  - Scriptc 静态编译不支持任意类型和部分动态特性，npm 依赖需通过 --dynamic 模式运行，制约了适用范围。
  - Scriptc 作为全新编译器项目，长期维护能力和生态兼容性尚需时间检验，Node.js API 覆盖仍不完整。
  score: 8.0
  article_ids:
  - 0dadaefdea9260e5
  evidence_snippets:
  - Scriptc 是 Vercel Labs 开源的 TypeScript 到原生可执行文件编译器，生成的二进制文件不包含任何 JavaScript 引擎，从而显著降低了运行开销。
  - Scriptc 支持将普通 TypeScript 代码编译为原生二进制，行为与 Node 逐字节一致，无需修改代码或添加注解，兼容现有 TypeScript
    项目。
  - Scriptc 的基准测试显示启动时间仅约 2.4ms，静态二进制大小仅 170-200KB，典型内存占用仅 1-4MB，相比 Node.js 有数量级上的性能和效率提升。
---

**Zero-runtime TypeScript.** scriptc compiles ordinary TypeScript into small, fast native executables — no Node, no V8, no JavaScript engine in the binary.

```
$ cat fib.ts
function fib(n: number): number {
return n < 2 ? n : fib(n - 1) + fib(n - 2);
}
console.log(fib(30));
$ scriptc run fib.ts
832040
$ scriptc build fib.ts && ls -la fib
-rwxr-xr-x 178K fib # a self-contained native binary, ~2ms startup
```

No changes to your code. No annotations, no dialect — the same TypeScript you run on Node, type-checked by the real TypeScript compiler and compiled to native. What compiles behaves byte-for-byte like Node.

`$ npm install -g scriptc`

Requires clang (preinstalled with Xcode Command Line Tools). macOS arm64 is the primary platform; Linux and Windows binaries build by cross-compilation, each verified by its own differential test lane.

Most TypeScript is far more static than the ecosystem assumes. scriptc decides, construct by construct, what can compile to native code — and tells you:

```
$ scriptc coverage app.ts
statements analyzed 4481
compile statically 4451 (99%)
blockers:
×2 functions with optional parameters as values SC1090
×1 Promise.reject SC2020
```

Three tiers, always explicit:

**Compiled statically**— native code, no engine. The default, and the only mode unless you opt out.**Runs dynamically**(`--dynamic`

) — an embedded JavaScript engine (quickjs-ng, ~620KB) executes what can't be static: npm dependencies' shipped JS,`any`

-typed code. Every value crossing back into static code is validated at runtime — a lying type throws a catchable`TypeError`

instead of corrupting memory.**Rejected**— everything else fails with a specific error code, a code frame, and usually a rewrite hint. Nothing is ever silently miscompiled.

The static surface covers the language and the standard library real programs use:

**The language**— classes with single inheritance and true dynamic dispatch (devirtualized when provably safe), closures with JS capture semantics, generics (monomorphized), discriminated unions as tagged values driven by TypeScript's own narrowing,`async`

/`await`

on stackful fibers with JS-exact scheduling, exceptions with`finally`

, destructuring, spread, optional/default/rest parameters, getters/setters, iterators over strings/arrays/Maps/Sets, template literals, regular expressions (the engine is the same ECMAScript-exact bytecode interpreter QuickJS uses, linked only into regex-using binaries).**The standard library**— strings with UTF-16-exact semantics, arrays/Maps/Sets with JS-exact ordering and identity,`JSON`

with runtime-validated casts,`Math`

, typed arrays and`Buffer`

,`Error`

hierarchies with typed`catch`

.**Node's API surface**—`fs`

(sync and promises),`path`

(byte-exact port),`process`

,`child_process`

with piped streams,`os`

,`crypto`

,`url`

/`URL`

,`zlib`

, timers and signal handlers on a dependency-free event loop — and the server stack:(vendored mbedTLS),`net`

,`http`

,`https`

,`tls`

`dgram`

,`dns`

,`fs.watch`

,`readline`

. Real proxy servers compile.and the WHATWG web subset (streams,`fetch`

`Headers`

,`AbortSignal`

) over the same native net/TLS stack — redirects, gzip,`AbortSignal.timeout`

, Node-shaped error causes; no libcurl, no system HTTP dependency.**npm dependencies**(with`--dynamic`

) — packages resolve with Node's own algorithm, typecheck against their shipped`.d.ts`

, and their JS is embedded into the binary at build time. Binaries never read`node_modules`

at runtime.

Programs typecheck against TypeScript's real `es2025`

lib (plus `@types/node`

when your project has it), and your `tsconfig.json`

governs checker strictness. Anything reached that has no lowering is a precise diagnostic, never a surprise.

Two enforcement mechanisms run on every change:

**Differential testing**— every corpus program (800+ tests) runs under Node*and*as a native binary; stdout, stderr, and exit codes must match byte-for-byte. Number formatting is JS-exact (shortest-roundtrip, fuzz-verified against Node on a million doubles). Servers are tested with live client drivers against both implementations.**Memory-safety lane**— the entire corpus re-runs under AddressSanitizer with a reference-count audit; leaks and use-after-free are build failures.

The deliberate divergences from Node (there are a few dozen, mostly around timing internals and error-object properties) are documented and numbered; nothing diverges silently.

Measured on Apple M-series against the same workloads in Node, Go, Rust, and Zig (all byte-identical output, verified):

| dimension | scriptc | context |
|---|---|---|
| startup | ~2.4ms | Node: ~47ms; on par with Zig, ahead of Go/Rust |
| binary size | 170–200KB static, ~3MB with `--dynamic` + embedded deps |
Go: ~2MB; Node SEA: 60–100MB |
| memory (RSS) | 1–4MB typical | Node: 67–116MB |
| runtime | JS-faithful f64 semantics; competitive with the systems languages on most workloads | integer inference and ownership analysis are on the roadmap |

runs TypeScript at build time (in an isolated VM inside the compiler) and bakes the result into the binary as a literal.`comptime(() => ...)`

**Native FFI (**binds signature-only TypeScript declarations to direct C ABI calls and links manifest-declared archives, objects, and system libraries. The boundary is explicit and length-delimited; see the Native FFI guide.`--ffi`

)embeds the engine for npm deps and`--dynamic`

`any`

code.`scriptc coverage --dynamic`

reports exactly which statements run where and what the remaining blockers are. Static stays the default: a binary never silently grows an engine.**Checked casts**—`JSON.parse(...) as Config`

inserts a runtime validation that throws a catchable error naming the offending path (`expected number at $.port, got string`

). TypeScript's`as`

is a promise; scriptc verifies it.

```
flowchart LR
TS[TypeScript] -->|tsc: parse + typecheck| L[lowering]
L --> IR[typed IR]
IR --> C[C]
C -->|clang| BIN[native executable]
```

`packages/compiler`

— frontend (tsc API → IR), the IR with validator/serializer, the LLVM and C backends. The IR is the only interface between the ends; LLVM is the default code generator (with a transparent fallback for programs outside its tier), and C is the reference backend forever (readable, source-line-annotated output via`--backend c`

).`packages/runtime`

— the C runtime: refcounted values with a cycle collector, stackful fibers and the event loop (kqueue), the server stack, JS-exact number formatting. Feature units are link-gated: binaries pay only for what they use.`packages/cli`

—`scriptc build | run | coverage`

.

```
$ pnpm install && pnpm build
$ pnpm test # differential corpus + diagnostics snapshots
$ SCRIPTC_SAN=1 pnpm test # the same corpus under ASan + RC audit
$ pnpm scriptc build x.ts --emit-ir # keep .scriptc/x.c and x.ir.json
```

Every feature lands with differential tests; both lanes green is the merge bar.