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