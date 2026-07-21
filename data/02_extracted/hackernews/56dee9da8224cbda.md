---
title: 'A road to Lisp: Why Lisp'
source: https://scotto.me/blog/2026-07-09-why-lisp/
author:
- '[[silcoon]]'
published: '2026-07-09'
created: '2026-07-10'
description: 'Article URL: https://scotto.me/blog/2026-07-09-why-lisp/ Comments URL:
  https://news.ycombinator.com/item?id=48845209 Points: 227 # Comments: 174'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 56dee9da8224cbda
source_type: community_discussion
tldr: Lisp 是一门可编程的编程语言，通过宏实现语言扩展性，利用同像性让代码像数据一样被操作，并通过 REPL 驱动开发提供实时编程体验。文章解释了 Blub
  悖论以及 Lisp 能让程序员以其他语言无法实现的方式思考问题。
objective_summary: 该文章由开发者 Scott O. 撰写，发表于个人博客，旨在解释 Lisp 编程语言的独特价值。文章阐述了 Lisp 的三大核心特性：宏扩展让程序员能够创建新的语言构造、同像性使代码与数据都用列表表示，以及
  REPL 驱动的实时开发环境。文章引用 Paul Graham 的 Blub 悖论来说明为什么来自较弱语言的程序员难以理解 Lisp 的优势。作者认为即使最终不使用
  Lisp，学习它也能让程序员获得关于编程语言能力的全新视角。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Lisp
  - Common Lisp
  - REPL
  key_people:
  - Paul Graham
key_logic_flow:
- Lisp 的学习曲线陡峭，但它能让程序员做到其他语言无法实现的事情，因为 Lisp 改变了使用代码解决问题的思维方式。
- Paul Graham 提出的 Blub 悖论指出，只使用过较弱语言的程序员无法感知更强大语言（如 Lisp）的优势，因为他们缺少理解这些优势所需的概念。
- Lisp 通过宏（macro）实现语言扩展性，宏不同于其他语言的宏，它允许创建成为语言本身一部分的新构造，而不仅仅是消除模板代码。
- Lisp 具有同像性（homoiconicity），代码和数据都用列表表示，这一特性使宏成为可能——程序员可以像操作数据一样操作代码，实现程序编写程序。
- Lisp 是一个实时系统，通过 REPL 驱动开发，程序员在运行中的进程内连续评估代码并立即观察输出，无需传统的编写-编译-运行-调试循环。
- Lisp 的热重载是原生特性而非独立工具，每次重新定义符号（函数、数据或宏）都会在实时环境中自动生效，无需停止和重新编译。
extract_result: success
object_mentions: []
---

The question that most programmers face when seeing some Lisp code for the first time is, without doubt, “what the hell is this?”. I asked myself the same thing when I first read its unconventional syntax: all those parentheses, the weird indentation, and who thought to use the first argument of `format`

to print to stdout?

After getting comfortable reading code with so many parentheses, I had to learn how to use packages and symbols, how to create new projects and import libraries, how to use the REPL, and how to use conditions and restarts. Most importantly, I had to switch to a new way of thinking when constructing algorithms.

The Lisp journey has a steep learning curve compared to most common languages. But it can also unlock skills that those languages never will. Why? Because **in Lisp you can do things that are not possible in other languages**. Lisp enables new possibilities and allows algorithms to take different shapes, giving the programmer more power and flexibility.

Paul Graham coined the term Blub paradox to explain why it is difficult for programmers who have only used less powerful languages to understand the power of Lisp. In short, it’s because they are missing the concepts needed to perceive what is lacking in those languages and the advantage Lisp has over them. Louis Armstrong said something similar about jazz:

If you have to ask what jazz is, you’ll never know. — Louis Armstrong.


In this article, I’ll explain a few features that show why this special language is worth learning. It’s not an easy path, and to truly grasp its power you’ll need to use Lisp yourself. And even if you don’t end up using Lisp, you will gain a different perspective on what programming languages can do.

Lisp is going to make you a better programmer because **it changes the way you think about problems using code**. To be more specific, it will teach you an approach that is not possible with other programming languages. You will be able to program Lisp itself and thus adapt the language you use to the problems you are solving. Using Lisp, you will learn to *grow the language toward your problem, then write the program in that language*.

## Extensibility

Lisp is extensible within itself. Experts — called lispers — commonly refer to it as *the programmable programming language*1. Not only will you write code for your programs, but you can write code that extends Lisp itself.

This is possible thanks to the *macro* operator. If you’ve used macros before in languages like C, Rust, or Swift, don’t expect the same thing. Those macros are primarily a way to eliminate boilerplate or generate repetitive code. Beyond that, macros in Lisp allow you to create new constructs that become part of the language itself.

They are one of the hardest features to master for Lisp programmers, so I won’t try to teach you how to use them or how they work here. I just want to give you a taste of what they do. For example, C programmers might want to use the `while`

operator to define a simple loop. Common Lisp does not provide it, so the programmer can write a macro and add it to the language.

The new `while`

macro executes a series of instructions (the `body`

) for as long as the `condition`

is true. It uses `loop`

, which is itself a macro used to write complex iterations (notice that it uses a `while`

symbol as well). `progn`

is a special form that takes multiple expressions, runs them in order, and returns the result of the last one.

Instead of writing `(loop while ... do (progn ...))`

, we can use the new `while`

operator, shortening the code and making it similar to C. We just extended the language available to us.

The beginner might not grasp what is really magical here, since, other than the unique syntax, `defmacro`

looks pretty similar to `defun`

, which was used in the first code example to define new functions.

To better understand the difference between the two, let’s define a new `while`

as a function, then call it.

`loop`

is the same macro we used before; `funcall`

calls the function received as the first parameter, in this case `body`

. Try to execute the code above in a Common Lisp REPL. You will receive a condition of type error, similar to this: `The value 2 is not of type FUNCTION`

.

This happens because the arguments to `fake-while`

are evaluated immediately. `(< x 3)`

evaluates to `t`

— true. Because `progn`

is a function, its arguments are evaluated. `(print counter)`

prints `3`

, and `(decf counter)`

returns `2`

. Since `progn`

returns the value of its last expression, `body`

becomes `2`

. So fake-while receives `t`

as its first argument and `2`

as its second, not a block of code. It will enter the `while`

since the condition is true, and then `funcall`

expects `body`

to be the function to be called, but `body`

is the value `2`

. This raises the condition above. The code executed by the compiler is the one below. `(funcall 2)`

raises the condition.

The macro `while`

defined earlier works because it keeps the arguments — `condition`

and `body`

— intact, without evaluating them until needed. We can inspect the transformation that a macro operates in the REPL. This transformation is called *expansion*. `macroexpand`

is a special Lisp command we can use to expand code.

The code returned from the macro expansion is the one received and executed by the compiler. We can see that this time the `while`

macro preserved the arguments so they will be executed together with the rest of the code.

A macro, unlike a function, does not evaluate the arguments in advance. Instead, it treats them as pure data. This is possible because (almost) everything you see in Lisp is made of lists. They are the main data structure, and they are used to write code.

## It’s lists all the way down

Programs in Lisp are composed of a series of **symbolic expressions** (abbreviated *s-expr*). *Expression* is a mathematical term meaning anything that evaluates to a value; *symbolic* means that expressions are created using values and symbols.

An *s-expression* is one of two things:

- an
*atom*, which is a unit of data (a number, a string, a symbol, etc) - a
*list*, which is a collection of elements that can be atoms or other lists

Lisp means *LISt Processing*, so the purpose of the language is to process the series of instructions expressed as lists that compose the program.

Since lists are used both as the main data structure and to write the code, we can extract an interesting property of the language. In Lisp, **code-as-data** means that both code and data are expressed using lists. This property is called **homoiconicity**.

I’ve used two lists with the same content; the only difference is that I put `'`

in front of the second one, but the output is different. The first list is treated as *code*. It gets evaluated, and specifically the symbol `+`

maps to a function that performs the sum of the arguments. Lisp uses what’s called *Polish notation*, where the function name is the first element of the list and what follows are the arguments. So instead of writing `print("hello")`

, we write `(print "hello")`

, moving the function name inside the parentheses. The output is 3, which is the result of the code execution.

The second list is treated as *data*. `'`

is an operator that tells the interpreter not to evaluate the following list and keep it as manipulable data. The output is the same list, not evaluated.

The subtle distinction between code and data is what makes macros possible. We can manipulate code as we manipulate data. By transforming the source code, we are able to write **programs that write programs**, a capability other languages have spent decades trying to imitate.

Extending the language means that by creating new constructs that are more expressive for your program’s specific scope, you can make your code more *concise*. Repetitive boilerplate code can be replaced with custom macros to shorten the code and save time. New control structures can be created to control resource access and the evaluation of forms. Macros can generate code, improve performance, and, most importantly, create new syntactic abstractions that are easier to use to hide complex and error-prone code.

## A live system

Lisp is not only a programming language, it’s a **live system**. To clarify this point, let’s start with how different the workflow is between Lisp and other languages.

With other languages, you open the project in the editor and start writing code. The first thing a lisper does is start a Lisp process, attach it to the REPL, and then load the project into that process.

The **Read-Eval-Print Loop** is an interactive environment used to evaluate code and immediately see the result. It’s a window into the Lisp living process that is currently running your program.

In other languages, once you change the code, you have to stop and compile it, then run the project to observe, test, and debug the changes. If something’s wrong, you go back to the write-compile-run-debug cycle.

Instead, a lisper continuously evaluates code in the running process and observes the output directly in the REPL, since **the Lisp process is the running program**. Every single function can be immediately tested in the REPL as a single unit of code, as well as any other action useful for development, such as querying a database, inspecting variables, or debugging.

A Lisp process is usually kept alive for weeks on end since there is no need to stop it. It can stay attached to the REPL in the editor for as long as needed. New functions, macros, and variables are continuously defined and redefined, a process called *binding* within an internal memory called the *environment*. This particular workflow even has a name: **REPL-driven development**. This is a real killer feature. It has been available in Lisp since its invention in the 60s, and it has been imitated by other languages (where possible), like many other Lisp original features.

Does the word *hot-reloading* tell you anything? I’ve been lucky since I started my career working with web frontends, where the JavaScript code of the app is hot-reloaded with every hard refresh of the page. And thanks to modern tools, I now only need to *save a file* and the webpage will automatically refresh itself with the new changes. Under the hood, hot-reloading means there is a process watching the files, recompiling the modules that changed, and a websocket connection is used to inject the changes silently into the page. But not all software stacks are that lucky. Some backend frameworks still require recompilation, the situation is mixed for desktop and mobile development, and low-level languages require full compilation every time.

In Lisp, hot-reloading is not a separate tool or technique. It comes for free when evaluating code in the live environment. Every time I redefine a symbol, it picks up the new definition, whether it’s a function, data, or a macro. I don’t need to stop and compile, run tests separately, or use some special debugger. Everything comes automatically by evaluating in the REPL. A good analogy is that programming in Lisp is like *evolving* a program rather than constructing it. Once a new Lisp process has started and code gets evaluated into it, that system will become the program itself.

Lisp allows you to approach programming in a new way. You can evolve the programs while writing them, and at the same time, as discussed before, evolve the language to your needs. A Lisp CAD program has evolved by turning Lisp into a language that writes CAD programs. A high-frequency trading system has evolved with a language adapted to write similar trading systems. This is the nature of Lisp, and it offers many advantages.

## Extensible software

This is something probably even less known, but the two features explained above (language extensibility and the Lisp live system) allow you to easily **create extensible software**.

We’re used to desktop programs being extensible mainly through plugins, such as in text editors, or sometimes through scripting languages for customization, as in game modding. These solutions usually work well, but they require programmers to design and maintain an entire system for extensibility, and they require users to learn a specific set of APIs to write plugins or extensions. In Lisp, this comes almost for free.

While extending the language, lispers write macros to encapsulate actions and make code easy to reuse. In doing so, beyond just creating new symbols, they are effectively writing a **DSL**, a *domain-specific language* for the program. When lispers need to make their software extensible, all they need to do is let users use the DSL they’ve created.

To understand this concept, let’s look at some use case scenarios. I wrote a custom CMS server for clients’ websites. I wrote some macros for generating webpages server-side.

I can expose the same DSL I’ve written internally to the users so they can write their own views and customise their CMS instance.

Notice how the `html`

macro seamlessly integrates with Lisp’s variables (`user-name`

), loops (`dolist`

), and string formatting (`format`

). In a traditional templating language, you’d need to learn a separate syntax with special brackets like `{{ user_name }}`

or `{% for %}`

. In Lisp, you don’t need a new language since you just use Lisp itself to build your templates.

This integration means your DSL inherits all the power of Lisp: conditionals, recursion, higher-order functions, and even the ability to debug your templates step-by-step in the REPL.

Another scenario: I wrote a math software where users can write formulas and the program renders them on a Cartesian graph. So I wrote a DSL to write math and draw. I can expose a small subset of the language to users so they can draw directly without having to use math formulas.

With this DSL, users can draw complex mathematical functions with minimal code. Since it’s just Lisp, they can use variables, define helper functions, or even generate multiple curves in a loop. This gives the users a clean interface while leaving the complex rendering code safely hidden away.

This technique for extending programs has been used successfully. AutoCAD uses *AutoLISP* to automate repeating tasks and create complex geometries. Emacs is the most extensible text editor that has ever existed on this planet, and most of it is implemented in its own Lisp dialect in order to make it infinitely expandable. There’s a running joke that hardcore Emacs users never have to leave the editor because it already contains everything they would ever need. In fact, Emacs has been extended to be a PDF reader, a web browser, an email client, an RSS reader, a terminal multiplexer, a Git client, a music player, a chat client, a spreadsheet, an IRC client, and even a window manager for your entire desktop, all thanks to using Lisp under the hood2.

The most powerful programming language is Lisp. If you don’t know Lisp, you don’t know what it means for a programming language to be powerful and elegant. Once you learn Lisp, you will see what is lacking in most other languages. — R. M. Stallman creator of GCC, Emacs, the GNU project.


## So why Lisp (or when)

A lot of people have argued that one day in the future there would be a time for Lisp. A time where it becomes popular, almost the default language, when the majority of programmers will come to appreciate what a fantastic experience it is to work with it. A time when Lisp would be taught at universities all over the world so companies would have no issues finding lispers, and engineers would become unafraid of incompatibility or performance issues. Programmers would joyfully spend their days using REPL-driven development, and most of the software we use would become extensible using variations of a single language.

This time never happened, and probably never will.

Still, Lisp has survived from the 60s, becoming the second oldest programming language still in use after Fortran. So many languages were inspired by it, and so many languages are still being created, missing some of the features that helped Lisp survive. So even if there isn’t a time for Lisp, that doesn’t mean it’s not a powerful language worth knowing.

Better programmers than me have said that it’s hard to justify Lisp’s use by picking a single feature among its extensibility, its interactive environment, the REPL, and a lot of other features we haven’t touched yet. It is **the combination of all of them** that makes Lisp programming what it is.

So get ready to learn what the most powerful programming language truly is.

### Footnotes

-
This quote belongs to John Foderaro, co-founder of Franz Lisp. ↩︎

-
To be fair, some people argue that Emacs is “a great operating system, lacking only a decent editor”. ↩︎