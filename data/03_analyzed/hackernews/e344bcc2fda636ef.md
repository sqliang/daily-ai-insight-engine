---
title: .NET (OK, C#) finally gets union types
source: https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/
author:
- '[[ingve]]'
published: '2026-05-22'
created: '2026-05-24'
description: 'Article URL: https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/
  Comments URL: https://news.ycombinator.com/item?id=48234954 Points: 178 # Comments:
  164'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e344bcc2fda636ef
source_type: community_discussion
tldr: C# 15/.NET 11 预览版正式引入 union 关键字，支持可穷尽模式匹配的联合类型。
objective_summary: 2026年，.NET 11 预览版 4 中 C# 15 引入了 union 关键字，允许开发者声明可表示多种不相关类型的联合类型。编译器生成实现
  IUnion 接口的 struct，通过 [Union] 属性驱动隐式转换和 switch 表达式穷尽检查。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Microsoft
  technologies:
  - C# 15
  - .NET 11
  - union types
  - IUnion
  - UnionAttribute
  - OneOf
  - Sasa
  key_people:
  - Andrew Lock
key_logic_flow:
- 联合类型允许一个类型表示多种可能不相关的数据类型，常见例子包括 Option<T> 和 Result<TSuccess, TError>。
- C# 15 通过 union 关键字声明联合类型，语法为 `public union TypeName(CaseType1, CaseType2, ...)`。
- 编译器将 union 声明生成为一个实现 IUnion 接口的 struct，包含 object? Value 属性和每个 case 类型的构造函数，并标注 [Union]
  属性。
- '[Union] 属性驱动隐式转换（从 case 类型到 union 类型）和 switch 表达式的穷尽性检查，遗漏 case 会触发 CS8509 警告。'
- 默认实现将值类型参数装箱为 object 存储在 Value 属性中，在值类型较多的场景下会产生不必要的堆分配。
- 开发者可通过手动实现 IUnion 接口并添加 [Union] 属性来创建自定义联合类型，以此避免装箱开销并复用编译器的模式匹配支持。
impact_score:
  score: 3.5
  reason: C# 联合类型是 .NET 生态期待已久的语言特性，但其对 AI 行业的短期冲击有限。一方面，C# 并非 AI/ML 主流开发语言（Python
    占据主导），该特性不直接改变 AI 模型训练、推理或部署范式；另一方面，它对 ML.NET、Semantic Kernel 等微软 AI 中间件的 API
    设计有改善作用，提升类型安全和错误处理的人体工学。整体属于编程语言演进中的增量改进，影响力局限于 .NET 开发者圈子，不具备跨生态的行业范式转移效应，因此评为
    3.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 编译器生成的穷尽性模式匹配检查与零额外依赖的联合类型实现
hype_assessment:
  level: low
  reason: 文章为 Andrew Lock 撰写的深度技术解析，提供了完整的代码示例、编译器内部实现细节（IUnion 接口、[Union] 属性驱动隐式转换、装箱开销分析）以及自定义实现方案。文中未使用'颠覆''革命性'等
    PR 滥用词汇，对预览版的实验性状态有明确警示，整体属于实打实的技术干货。
information_entropy: high
domain_disruption:
  technical_innovation: 编译器将 union 声明生成为实现 IUnion 接口的 struct，通过 [Union] 属性驱动隐式转换（从
    case 类型到 union 类型）和 switch 表达式的编译期穷尽性检查，遗漏 case 触发 CS8509 警告。这是编译器工程层面的精巧设计，将联合类型的运行时开销最小化并深度集成到现有模式匹配基础设施中，但本质上是将其他语言（F#、Rust、TypeScript）早已成熟的
    discriminated union 概念以 C# 惯用方式落地，并非计算机科学的原创突破。
  business_model: 无直接影响。该特性降低 .NET 生态中采用函数式错误处理模式（Result<T, TError>、Option<T>）的门槛，间接增强
    Microsoft 在企业级应用和 AI 中间件（Semantic Kernel）领域的平台吸引力，但不改变 SaaS 商业模式或定价结构。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 联合类型作为语言特性，一旦正式发布将成为 C#/.NET 生态的永久基础设施，3-5 年后开发者将习以为常地使用。但作为单一语言特性而非独立产品或平台，其复利效应有限——真正的复利在
    .NET 平台层累积：每增加一个语言特性，开发者留存率提升、迁移成本增加，微软 Azure 的锁定效应随之加强。评分取中等偏上，因为它消灭了一个细分第三方库赛道（OneOf
    等），体现了平台吞噬生态的经典模式，但独立看不足以产生爆发式价值增长。
value_capture_layer: cloud_platform
moat_impact: strengthens_monopoly
key_beneficiaries:
- Microsoft
- Azure
- .NET 企业开发者
competitive_casualty:
- OneOf 库
- Sasa 库
- 其他 .NET 第三方联合类型实现
- 以联合类型为差异化卖点的替代语言/平台
market_opportunities:
- 基于 .NET 生态的函数式编程教育内容需求将激增，建议开发面向 C# 开发者的 Union Types/Result 模式实战课程与认证体系，覆盖从 OneOf
  迁移到原生 union 的最佳实践
- 工具链创业者可开发自动化迁移工具（Roslyn Analyzer/Code Fix），将现有第三方联合类型库（OneOf、Sasa）批量转换为 C# 15 原生
  union 声明，解决企业级代码库升级痛点
- AI 应用框架（如 Semantic Kernel、LangChain.NET）可借助原生 union types 重构错误处理与中间件链，推出类型安全的 AI
  Agent 编排 DSL，提升企业级 .NET AI 应用的可靠性与可维护性
risk_matrix:
  regulatory: 无
  technological: 当前编译器生成的默认联合类型对值类型参数执行装箱操作（存储在 object? Value 中），在高频交易、游戏引擎等性能敏感场景下会产生不可忽视的堆分配开销；开发者需手写
    IUnion 实现来规避，增加了落地复杂度。此外，若预览版实现发生重大变更，早期采用者可能面临代码迁移成本。
  competitive: Java 21+ 已通过 sealed classes + pattern matching 实现类似能力且进入稳定版，TypeScript
    在 Web 端拥有更成熟的 discriminated union 生态，F# discriminated unions 在 .NET 内部构成替代竞争，C#
    15 联合类型属于追赶型特性而非差异化优势，可能难以吸引已使用其他语言的开发者回流。
  ethical: 无
  additional:
  - 生态碎片化风险：OneOf 库（NuGet 下载量数千万）已形成事实标准，原生 union 与社区三方实现在互操作性上可能存在摩擦，短期内导致 .NET 项目中两种模式并存，增加维护复杂度
  - 版本锁定风险：如需使用 union 关键字则必须依赖 .NET 11 SDK 构建（即使可 target 旧运行时），企业级 CI/CD 管线升级 SDK
    存在惯性和合规障碍，可能延迟大规模采用
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

Unions are one of those features that have been requested for years, and in .NET 11 (or rather, C# 15) they're *finally* here. In this post I describe what that support looks like, how you can use them, how they're implemented, and how you can implement your own custom types.

This post was written using the features available in .NET 11 preview 4. Many things may change between now and the final release of .NET 11.


## What are union types?

Unions are one of those basic data structures which are used all the time in the functional programming world; they're available in F#, TypeScript, Rust…pretty much any functional-first language. There are many different *types* of union, but at their core they allow having a type that can represent two different things.

Some of the simplest union types are the `Option<T>`

and `Result<TSuccess, TError>`

types. There's no "standard" version of these, but it's *super* common to see custom implementations. `Result<>`

is one of the easiest to explain as it can be in one of two states:

- Success—in this case the
`Result<>`

object contains a`TSuccess`

value representing the "success" result for an operation that succeeded. - Error—in this case the
`Result<>`

object contains a`TError`

value representing the "error" for an operation that failed.

You return a `Result<>`

object from your method, and then the caller has to *explicitly* handle both cases instead of assuming success.

This pattern is often called the result pattern and it has both pros and cons in C#. I wrote a series about using this pattern, as well as considering whether it's worth it here.


Union types don't have to be the super generic form like this though. They can be used to represent any arbitrary combined set of types.

## Union types in C# 15 with the `union`

keyword

In the previous section I used the classic `Result<>`

type as an example of a union, but unions are far more versatile than that. They're ideal whenever you want to deal with data that could be one of several potentially unrelated types.

For example, imagine we have three different `record`

types, containing different properties, representing Operating Systems:

```
public record Windows(string Version);
public record Linux(string Distro, string Version);
public record MacOS(string Name, int Version);
```


Note that these types *don't* have any values in common. Prior to C# 15, the main options for handling something which could be a `Windows`

*or* `Linux`

*or* `MaxOS`

object would be:

- Try to create a base class from which all the types derive. That
*might*work, but what if you don't control these types because they come from a library? - Store the type in an
`object`

instance. This works, but you lose all the safety of working with types in this case. - Use some "tag" value for keeping track of which type your object contains, e.g. using an
`enum`

to track this.

In C# 15, we get direct support for this scenario with the `union`

keyword, as shown below:

```
// 👇 Use `union` as the type
public union SupportedOS(Windows, Linux, MacOS);
// 👆 List the types that are part of the union
```


You can create an instance of the `SupportedOS`

type in a couple of ways:

```
// You can call new and pass in an instance
SupportedOS os = new SupportedOS(new MacOS("Tahoe", 25));
// Or you can use implict conversion (which calls new() behind the scenes)
SupportedOS os = new MacOS("Tahoe", 25);
```


The generated `union`

type implements the `IUnion`

interface:

```
public interface IUnion
{
object? Value { get; }
}
```


so you can always get the "inner" case value back out as an `object?`

if you need to:

```
// You can access the stored "inner" object using `.Value`
Console.WriteLine(os.Value); // MacOS { Name = Tahoe, Version = 25 }
```


However, the canonical way to work with unions is to use a `switch`

expression:

```
string GetDescription(SupportedOS os) => os switch
{
Windows windows => $"Windows {windows.Version}",
Linux linux => $"{linux.Distro} {linux.Version}",
MacOS macOS => $"MacOS {macOS.Name} ({macOS.Version})",
}; // note: no discard _ required
```


The `switch`

expression automatically extracts the inner case type, and a very neat thing is that you *don't* need to include the `_ => `

"discard" case either: the compiler enforces that you check for each of the allowed values, but you *only* need to check these values. And if you forget one, you'll get a warning:

```
warning CS8509: The switch expression does not handle all possible values of its input type
(it is not exhaustive). For example, the pattern 'MacOS' is not covered.
```


Note that if one of your case types is nullable, e.g.

`MacOS?`

then you'll need to handle`null`

in your`switch`

expressions too.

To come full circle, we could perhaps implement the `Result<>`

type as the following (just an example, there's lots of different implementations we could choose!)

```
public union Result<T>(T, Exception);
```


or to show another classic, the `Option<T>`

type:

```
public record class None;
public union Option<T>(None, T);
```


That's the basics of the `union`

types in C# 15, so next we'll look at how you can use them today, before we look behind the scenes at how they're implemented.

## Using `union`

types in .NET 11

To use `union`

types you need to do two things:

- Install .NET 11 preview 2+ SDK. The initial
`union`

support was added in preview 2, but you'll have a smoother experience if you install preview 4+. - Enable preview language support in your .csproj files, by adding
`<LangVersion>preview</LangVersion>`


```
<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup>
<OutputType>Exe</OutputType>
<!-- 👇 Add this -->
<LangVersion>preview</LangVersion>
<TargetFrameworks>net11.0;net8.0;net48</TargetFrameworks>
<ImplicitUsings>enable</ImplicitUsings>
<Nullable>enable</Nullable>
</PropertyGroup>
</Project>
```


Note that although you need to use the .NET 11 SDK, you *can* target earlier versions of the runtime, such as I'm doing in the above *.csproj* file. The `union`

support is implemented as a compiler feature, so it's available on earlier runtimes (even if it's not *technically* supported on them).

However, if you're targeting earlier runtimes (or you're using .NET 11 preview 2 or preview 3), then you'll *also* need to add some helper types to your project:

```
#if !NET11_0_OR_GREATER
namespace System.Runtime.CompilerServices;
[AttributeUsage(Class | Struct, AllowMultiple = false, Inherited = false)]
public sealed class UnionAttribute : Attribute;
public interface IUnion
{
object? Value { get; }
}
```


These were added to .NET 11 in preview 4, so they'll be available automatically if you're using a newer SDK, but you'll need to include them if you're targeting earlier runtimes, regardless.

As you might have guessed, when the compiler creates the `union`

types, it uses this attribute and implements this interface. In the next section we'll take a look at what the generated code looks like, to understand how the `union`

types are implemented.

In terms of IDE support, if you're using either Visual Studio Preview, or VS Code's C# DevKit Insiders, then you should have initial support. Support for JetBrains Rider is still pending.

## How are `union`

types implemented

You can see the full spec for `union`

types here, but the standard generated code is really pretty simple:

```
using System.Runtime.CompilerServices;
[Union]
public struct SupportedOS : IUnion
{
public object? Value { get; }
// Constructors for each case type
public SupportedOS(Windows value) => this.Value = (object) value;
public SupportedOS(Linux value) => this.Value = (object) value;
public SupportedOS(MacOS value) => this.Value = (object) value;
}
```


As you can see, the generated `SupportedOS`

type:

- Is a
`struct`

, decorated with the`[Union]`

attribute. - Has a single, readonly,
`object? Value`

property, implementing the`IUnion`

interface. - Has a constructor for each of the case types it supports.

I was somewhat surprised to find there was no implicit conversion from the case types to the `SupportedOS`

type, given that we can write code like this:

```
SupportedOS os = new MacOS("Tahoe", 25);
```


However it looks like the compiler simply rewrites this to use the `[Union]`

constructor:

```
// SupportedOS os = new MacOS("Tahoe", 25);
// The compiler emits code that looks like this:
SupportedOS os = new SupportedOS(new MacOS("Tahoe", 25));
```


This implicit conversion is all driven by the `[Union]`

attribute. You can see this in action if we rewrite our example to *not* use the `union`

keyword, and instead use the implementation code shown previously but we "forget" to include the `[Union]`

attribute:

```
using System.Runtime.CompilerServices;
SupportedOS os = new MacOS("Tahoe", 25); // Cannot implicitly convert type 'MacOS' to 'SupportedOS'
var description = os switch
{
Windows windows => $"Windows {windows.Version}", // An expression of type 'SupportedOS' cannot be handled by a pattern of type 'Windows'
Linux linux => $"{linux.Distro} {linux.Version}", // An expression of type 'SupportedOS' cannot be handled by a pattern of type 'Linux'
MacOS macOS => $"MacOS {macOS.Name} ({macOS.Version})", // An expression of type 'SupportedOS' cannot be handled by a pattern of type 'MacOS'
};
public record Windows(string Version);
public record Linux(string Distro, string Version);
public record MacOS(string Name, int Version);
// 👇 This attribute is required to be a valid Union type,
// just removed here for demo purposes
// [Union]
public struct SupportedOS : IUnion
{
public object? Value { get; }
public SupportedOS(Windows value) => this.Value = (object) value;
public SupportedOS(Linux value) => this.Value = (object) value;
public SupportedOS(MacOS value) => this.Value = (object) value;
}
```


The code above fails to compile with the following, demonstrating how the `[Union]`

attribute drives the implicit conversions and `switch`

expressions:

```
error CS0029: Cannot implicitly convert type 'MacOS' to 'SupportedOS'
error CS8121: An expression of type 'SupportedOS' cannot be handled by a pattern of type 'Windows'.
error CS8121: An expression of type 'SupportedOS' cannot be handled by a pattern of type 'Linux'.
error CS8121: An expression of type 'SupportedOS' cannot be handled by a pattern of type 'MacOS'.
```


If you re-instate the `[Union]`

attribute, everything compiles and runs just fine, which shows how you can create your own *custom* union types.

## Avoiding boxing with custom Union implementations

Given we're *just* getting support for `union`

types, why might you want to create *custom* `Union`

types? One reason is that you might *already* be using custom union types, such as provided by OneOf, or Sasa (two packages I've used in the past). In these cases, the libraries could benefit from built-in language support (e.g. `switch`

expression support) by simply implementing the `IUnion`

interface and adding the `[Union]`

attribute.

Another case is when the "store the case type in an `object`

instance" just isn't good enough for you. The generated union type is *always* a `struct`

with a single `object`

field. That means that if you're creating a `union`

of multiple `struct`

types, those types are going to be boxed onto the heap.

For example, imagine you need this `union`

, which can represent either an `int`

or a `bool`

:

```
public union IntOrBool(int, bool);
```


The problem is that the `int`

or `bool`

passed into the constructor of `IntOrBool`

is immediately boxed to an `object`

and stored in the `Value`

property:

```
[Union]
public struct IntOrBool : IUnion
{
public object? Value { get; }
// The struct arguments are always boxed, allocating on the heap
public IntOrBool(int value) => this.Value = (object) value;
public IntOrBool(bool value) => this.Value = (object) value;
}
```


This allocates on the heap, which is generally undesirable, as `union`

types are intended to be largely transparent performance-wise. Any `switch`

expressions using this implementation will similarly use the `Value`

property. For example, with the basic built-in `union`

implementation, the following expression:

```
IntOrBool intOrBool;
var description = intOrBool switch
{
int i => "integer",
bool b => "bool",
};
```


would lower to code similar to this:

```
IntOrBool unmatchedValue = new IntOrBool(23);
object obj = unmatchedValue.Value; // 👈 Access the boxed value
string str;
if (obj is int _)
{
str = "integer";
}
else if (obj is bool _)
{
str = "bool";
}
else
{
ThrowSwitchExpressionException((object) unmatchedValue); // can't happen, but handled anyway
}
```


In many cases, the boxing allocation won't really matter, but in other places, such as in hot paths, the boxing is undesirable. To account for this, the `union`

feature allows for a "non-boxing" implementation, using a `TryGetValue`

pattern. This requires that you implement:

`bool HasValue { get; }`

which returns`true`

if the stored value is non-`null`

`bool TryGetValue(out T value)`

for each case type,`T`


For example, the following is a potential implementation of the `IntOrBool`

type above that avoids boxing

```
[Union]
public struct IntOrBool : IUnion
{
private readonly bool _isBool;
private readonly int _value;
public IntOrBool(int value)
{
_isBool = false;
_value = value;
}
public IntOrBool(bool value)
{
_isBool = true;
_value = value ? 1 : 0;
}
public bool HasValue => true; // the values are never null
public bool TryGetValue(out int value) // get the int value without boxing
{
value = _value;
return !_isBool;
}
public bool TryGetValue(out bool value) // get the bool value without boxing
{
value = _isBool && _value is 1;
return _isBool;
}
// 👇 Have to implement this to satisfy IUnion,
// and it still boxes, but it won't be used by default.
public object Value => _isBool ? _value is 1 : _value;
}
```


When you implement the `TryGetValue()`

methods, the compiler automatically uses them in `switch`

expressions instead of the `Value`

property, so the switch expression above becomes the following:

```
IntOrBool unmatchedValue = new IntOrBool(23);
string str;
// 👇 Calls TryGetValue instead of using the boxing Value property
if (unmatchedValue.TryGetValue(out int _))
{
str = "integer";
}
else if (unmatchedValue.TryGetValue(out bool _))
{
str = "bool";
}
else
{
ThrowSwitchExpressionException((object) unmatchedValue); // can't happen, but handled anyway
}
```


Depending on your code paths and use-cases, it may or may not be worth creating custom non-boxing implementations like this, it depends on what you're using the `union`

types for in your code base.

## What other features are yet to come?

The `union`

implementation is usable as currently shipped, but there's even more to the language proposal than I've covered. Here are some of the related features that are yet to come:

- Union member providers. These provide a way to define the members that are part of the union type on a
*different*type to the union itself. - Closed enums. These are
`enum`

s in which you*don't*need to include a "catch-all" expression (`_ =>`

) in the`switch`

expression for the`enum`

. - Closed hierarchies. This allows adding the
`closed`

modifier on a`class`

to prevent derived classes from being declared*outside*the defining assembly, which then similarly allows exhaustive`switch`

expressions without a catch-all expression.

These features may or may not make it into .NET 11, but I'll be sure to cover them if they do!

## Summary

In this post I described the support for union types introduced in .NET 11 preview 2. I described the steps you need to implement them, as well as how to deconstruct union types using `switch`

expressions. I showed the `union`

declaration syntax, how they're implemented behind the scenes, as well as how to implement a non-boxing version of a union type. Finally I discussed some of the plans and roadmap for union types and for exhaustiveness improvements in C# that are yet to be released.