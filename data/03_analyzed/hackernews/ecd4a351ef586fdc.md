---
title: Interview with Mitchell Hashimoto about Ghostty and Zig
source: https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/
author:
- '[[veqq]]'
published: '2026-07-09'
created: '2026-07-10'
description: 'Article URL: https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/
  Comments URL: https://news.ycombinator.com/item?id=48849292 Points: 239 # Comments:
  109'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ecd4a351ef586fdc
source_type: community_discussion
tldr: Mitchell Hashimoto 访谈：关于终端模拟器 Ghostty、Zig 语言及开源哲学
objective_summary: Mitchell Hashimoto 在访谈中分享了离开 HashiCorp 后为磨砺 GPU 编程、桌面系统编程和 Zig
  技能而开发终端模拟器 Ghostty 的经历，讨论了终端生态的局限性并提出 n-screen API 和按钮协议两项改进方案，同时阐述了他对开源维护者无义务、用户应自行
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - HashiCorp
  technologies:
  - Zig
  - Wayland
  - PTY
  - GPU
  key_people:
  - Mitchell Hashimoto
key_logic_flow:
- Mitchell Hashimoto 离开 HashiCorp 后为重新磨砺 GPU 编程、桌面系统编程和 Zig 三方面技术技能，选择开发终端模拟器 Ghostty
  作为学习项目。
- Ghostty 最初仅以运行 vim 和编译器并能自举构建为目标，后因朋友在 Discord 中实际日常使用而转向公开，经历了长期私密测试阶段。
- 终端生态目前缺乏权威标准制定机构，过去 20 年的标准化基于流行终端的行为演变，导致功能混杂且缺乏统一的审美愿景。
- Mitchell 提出两项终端协议改进：n-screen API（支持创建无限数量屏幕、叠加和独立窗口渲染）和按钮协议（类似 OSC 8 超链接的点击交互，历史滚动中仍可注册）。
- Mitchell 认为开源维护者对用户没有义务，许可证明确声明'按现状、无担保'，用户应通过 fork 自行解决问题而非要求维护者满足需求。
- Ghostty 的设计哲学是功能丰富但不臃肿，通过架构设计确保未使用的功能不会消耗执行资源，同时支持高度可定制化。
extract_result: success
impact_score:
  score: 2.5
  reason: 该访谈讨论的是终端模拟器 Ghostty、Zig 语言和开源哲学，属于开发者工具生态的社区讨论，并非 AI 行业核心事件。虽然 Mitchell
    Hashimoto 是知名技术人物（HashiCorp 创始人），但 Ghostty 作为终端模拟器对 AI 行业的直接冲击力有限。文中提及的终端协议改进（n-screen
    API、按钮协议）可能间接利好运行在终端中的 AI 编码代理（如 Claude Code），但整体属于窄众开发者工具话题，短期行业影响力弱。
sentiment: neutral
developer_sentiment:
  tone: excited
  primary_focus: Ghostty 使用 Zig + GPU 渲染的终端架构设计，以及 n-screen API 和按钮协议两项终端协议改进提案
hype_assessment:
  level: low
  reason: 访谈内容务实，Mitchell Hashimoto 本人明确表示'不支持将终端功能推向极端'，未使用'颠覆性''革命性'等 PR 话术。讨论聚焦于具体的技术决策（为何选
    Zig、终端协议如何渐进改进）和开源哲学，没有夸大宣传。Ghostty 经历了长期私密测试后才公开，发布节奏克制。
information_entropy: high
domain_disruption:
  technical_innovation: 提出 n-screen API（支持创建无限数量屏幕、叠加与独立窗口渲染）和按钮协议（类似 OSC 8 超链接的点击交互，历史滚动中仍可注册）两项终端协议改进构想。Ghostty
    本身以 Zig 语言实现 GPU 加速终端渲染，在跨平台原生终端模拟器领域展现了较高的工程水准。
  business_model: 无
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Mitchell Hashimoto 是 HashiCorp 创始人（Terraform、Vagrant、Consul 等），其技术判断力和产品
    sense 已经过多款数十亿美元级开源项目验证。Ghostty 并非又一个终端模拟器，而是他以'学习 GPU 编程 + 桌面系统 + Zig'为起点、逐渐发现的终端生态结构性机会——现有终端缺乏权威标准制定机构，20
    年来的功能演进基于碎片化的行为模仿。Mitchell 提出的 n-screen API 和按钮协议两项协议改进，指向一个更大的叙事：终端正在从纯文本展示层升级为
    AI Agent 的交互基础设施（文章明确提及 Claude Code 等 AI 编程工具）。如果这两项协议被行业采纳为事实标准，Ghostty 的先行者优势将形成网络效应——终端模拟器之间的切换成本低，但协议生态的锁定效应强。Zig
    语言作为底层技术栈也为 Ghostty 提供了性能差异化。限制性因素在于：终端模拟器市场长期碎片化、开源 MIT 协议缺乏直接变现路径、协议标准化需要 iTerm2
    等竞品的采纳合作、以及 Warp 等融资充足的竞品也在抢夺同一心智。3-5 年后 Ghostty 大概率成为终端生态的关键一极，但能否成为真正的基础设施取决于协议推广速度和开发者社区的持续贡献。综合评估
    7.5 分：有潜力成为细分赛道基础设施，但协议标准化和生态系统建设仍需持续验证。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Ghostty
- Zig
- Vouch
- Anthropic
competitive_casualty:
- Warp
- iTerm2
- Kitty
- Alacritty
market_opportunities:
- 基于 Ghostty 提出的 n-screen API 和按钮协议，开发者可构建新型 TUI 应用（如多窗口终端 IDE、历史可点击交互的 CLI 工具），填补传统终端与现代桌面体验之间的空白
- Ghostty 用 Zig 实现高性能跨平台终端模拟器的成功实践，为 Zig 语言在桌面系统编程领域的商业化工具链和咨询服务提供了标杆案例
- 终端生态缺乏标准制定机构带来的市场空白——可推出终端协议兼容性测试套件或标准化联盟服务，帮助工具作者减少跨终端兼容成本
risk_matrix:
  regulatory: 无
  technological: 终端模拟器赛道竞争激烈，iTerm2、Kitty、Alacritty、Warp 等已有成熟产品和忠实用户群；Ghostty 提出的
    n-screen API 和按钮协议需要生态多方采纳才能发挥价值，单个实现存在被孤立的技术风险
  competitive: Apple Terminal、Windows Terminal、GNOME Console 等平台厂商内置终端持续进化，可能原生集成类似功能挤压
    Ghostty 差异化空间；Warp 等商业化终端已获资本加持，在功能迭代和市场推广上拥有资源优势
  ethical: 无
  additional:
  - Ghostty 目前高度依赖 Mitchell Hashimoto 个人维护，长期项目可持续性和社区治理模式存在不确定性
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: deep_dive
---

Mitchell Hashimoto was behind Vagrant, Packer, Consul, Terraform, Vault, Nomad, Waypoint and now builds Ghostty and Vouch.

In this interview, we talk about terminals, Zig and open source.

**You’ve been interviewed a lot. Why do people like to interview you?**

In interviews, everyone comes from a different angle. Many people want to know how the software engineering to business founder mindset transition went. Then others are interested in product stuff, the work I did at Hashicorp or Ghostty now. What’s different here is there’s no known agenda coming into it; neither of us have anything to sell.

**What do you find so fun about terminals? Like, why Ghostty?**

I spent ~15 years building CLI applications (not TUIs like we see nowadays). Through that process, I accidentally learned how to color things, move cursors etc. Leaving Hashicorp, I wanted to sharpen my technical skills (where they’d grown dull from neglect) and specifically work on: Pre-AI GPU programming, desktop/single node systems programming (spending so much time on the distributed side where you didn’t worry about cache locality or vector operations, since network costs dominated). I also really wanted to play with Zig. I wanted to satisfy those 3 things.

After 15 years building CLIs, I didn’t understand how a terminal emulator worked. I knew the components of a terminal but really wanted to understand how it worked, which would also let me work on the GPU, desktop and in Zig. My goal was to run vim and the compiler in it, have it build itself, then throw it away. But as I learned more about the terminal ecosystem, I understood nothing fit the niche I wanted: fast, feature-rich and natively cross-platform. I shared it with a few friends in Discord, who asked if they could share it with others because they were actually using it every day. The Ghostty Discord was just my friends’ group chat which got repurposed. I didn’t want to publish because my public persona would generate too much undue attention, so I ran a private beta for a long time.

**How can we push terminals harder?**

I don’t support pushing terminals to the extreme. Sure, they’re an application platform capable of the same things other application platforms on top of the OS are like the browser, old Java app runtime environments. You could build all functionality into it: video and microphone access, responsive layouts… You could.

But the browser is good at something, the desktop is good at something else and text-based (monospaced-grid) applications are also good at something unique. These text-based applications should be quick to implement, easy to interact with, clear in their security model. There’s a lot of opportunity in the ecosystem here and I’d love to build more protocols to enable that.

Terminal-based applications lend themselves to composition better than other paradigms. TUIs less so, but most CLI tools have mechanisms (beyond stdin and stdout) to use them like a function (the UNIX do one thing philosophy is the extreme). Neovim and AI tooling offer ever more cmdline flags. A world of better terminal applications, is a world of better automation, scriptability.

I want to make the terminal a special place for applications. The PTY’s in-band signalling (an unstructured byte stream with escape sequences) is a big problem. The Nushell ecosystem tries to fix it with another layer, but we need a fundamental improvement. Many people dislike the Microsoft ecosystem, but PowerShell gets a lot right with structured data.

**What do you think about non-legacy terminal APIs?**

My guiding star is how we now have multiple major, huge application platforms: the browser, emacs, the whole Apple ecosystem, Microsoft ecosystem, Android, video game console platforms. These ecosystems have strengths and weaknesses, but how do their frameworks work? On the web, it’s the DOM and JS APIs. On Apple, it’s AppKit, Cocoa and SwiftUI. On Windows, it’s Win32, WinUI etc. On Linux, it’s GTK and Qt etc. When someone says we need a better way of accessing clipboard data (historical protocols are text only, what about images, multiple MIME types etc. which desktops have handled for decades), I would grab the docs for clipboard managers on every platform to see what we’ve landed on. There’s no reason for us to build something based on our own understanding without researching decades of prior art. That’s the approach I’m trying to take here. I’ve not introduced any custom protocols yet.

Two protocols scream at me. Currently, terminals have a main screen and an alt (sometimes called primary and secondary) with different properties. Main screen is like your shell with scrollback etc. and the alternate screen is like Neovim, most TUIs etc. There are only 2, you either turn a mode on or off putting you into primary or secondary (taking up the whole screen, losing scrollback etc.)

I’d like to introduce an n-screen API to create and populate an unlimited number of screens in the background, let you overlay screens with separate grid sizes etc. The terminal emulator could handle line wrapping, selection, routing mouse events etc. You could specify a screen as a standalone window which the terminal emulator renders outside of the grid - imagine your Neovim tabs being native window tabs opened at the same time! This foundational layer would solve a lot of things.

I also have a spec’d out button protocol. Currently, there are mouse protocols to get notified when someone clicks a grid cell. But you only receive events for what’s currently on the screen, not history, when things scroll back… We currently support hyperlinks (OSC 8) and I’d like something similar to OSC 8 where clicking sends a message (which you specify) to the program. You could create a button with an `open_profile`

ID which will still register when the user scrolls back in history. This affects main screen applications (the only ones with scroll back) like Claude Code. I have no interest discussing AI here, it’s just a really popular main screen application. The moment things go into history, you lose the ability to open files, in-app links etc.

**To what extent is that just redoing the entire user space? There’s a lot of room for scope creep there.**

I experimented with replacing the entire pty protocol with Wayland. If you squint, a terminal’s just a windowing server, managing windows and widgets on windows. I studied Wayland to make Ghostty run better on it and thought it’s a pretty good protocol for what it tries to solve (local desktops, rendering windows). But I threw that out.

A problem with terminals is that there’s no standards body *any more*. There are old specs, de jure standardized, but the past 20 years have seen standardization based on what the most popular terminals do. We have a hodge-podge of features, but no entity pushing a tasteful vision.

I don’t know what the right path forward is. You could make an alternate home for text-based applications, not called a terminal anymore, build something new (with a terminal translation layer on top to bring legacy applications on) which is trying to do something different.

**How do you balance these ideas with users’ day to day demands?**

I’m very public about open-source maintainers having 0 obligation to users. The first line in OS licenses is “as is, no warranty”. That’s the agreement, you get free software and can’t make demands on it. But I like striving to build good software (some may disagree and say my software’s shitty), so I do feel an obligation to fix problems, to make the software better.

Some days I wake up expecting to go through issues just fixing other people’s problems. But sometimes I wake up and focus on what I want, not reading a single issue, discussion nor PR. Sometimes, you need to push the bigger vision; sometimes, you need to address the reality on the ground.

You can build a perfect city in the sky, then come back and find terror and suffering in the real world. So you need to clean that up sometimes.

If all I did was pick through user issues every single day, you’d get stable, stagnant software. If you accept all PRs, you will change but without vision. I don’t mean to insult contributors, but only one person every few years fundamentally gets it. Most contributions just scratch someone’s specific itch, accepting them all leads to a mountain of code. Really understanding, you can sometimes discover graceful systems which solve everything succinctly.

I once did feature design video where I closed 3-4 separate feature requests solving people’s individual problems, because a single feature (different from all of them) could solve them all at the same time. Very few people can do this, not because it’s difficult but because it requires a level of care few people give to other projects.

I’ve been thinking about this off and on for like a year (along with hundreds of other things, nothing dedicated, I’m always just thinking about this stuff when not at a computer). When I finally sat down and thought “I’m going to solve this,” maybe… 1 hour? https://x.com/mitchellh/status/2003957851514126510


**Fewer features composing better attracts people to exotic programming paradigms. It demands a lot of perspective.**

I got on an internet spat with someone recently about my philosophy. One of the highest requested Ghostty features is search, which is done and shipped. But someone complained search bloated and broke Ghostty’s minimalism. I advertise Ghostty as feature rich! But I do distinguish that from bloat. I don’t think you should have to pay for the things you don’t use (besides disk space or resident code memory). I explained the way I architected search means it will take up disk space and be loaded into RAM but nothing will execute; this is a free feature if you don’t use it. I want Ghostty to be a riceable, customizable terminal fitting peoples’ needs, but also working out of the box and hiding them until you need or search for them, without costing anything.

But if you really want this, just fork and maintain it yourself. That’s not asking any more of you than you’re asking of me. If you want me to maintain a flag to remove it, I can ask you to maintain a fork removing it. Telling people to “fork it” often upsets them.

**Very few people maintain their own patches etc. and demand entire projects to move to comfort them. It’s a very disempowering mindset to beg others to do what they could very easily do themselves, forgoing their own agency.**

I’ve always believed there should be way more forks, both personal and maintained ones.

I do blame myself and venture-backed opensource in general here. There’s a whole generation which expects highly polished, funded, opinionated projects with websites and paid support staff (in Discord, Slack etc.) believing an open sourced project is a product - and it was a product in these venture backed cases. But that’s such a minute part of the ecosystem.

Open source includes sharing, but it’s about freedoms and rights. That’s the core part of open source, defining OSI-approved open source licenses. Use the software as you want, modify and fork it. None of those rights are about stability or obligation to maintain. People blame maintainers for shipping security vulnerabilities, but why didn’t *you* review that commit? You’re just as obligated to review the commit as the maintainer. But people hold maintainers to this higher responsibility, when they could fork and become a maintainer just like that.

If you want better guarantees, if you want the entitlement to blame someone, pay for software. When you have a vendor-customer relationship, you are now entitled to things. But there’s no entitlement in open source. Use it how you love it, that’s the path to getting what you want. If more people forked, they’d have more empathy for builders too.

Sometimes people assume some project of mine is a company or send a PR fixing a bug I don’t personally hit, and I don’t merge it because merging means committing to maintain it forever. In a personal project, I won’t merge because I don’t hit that bug.

**Consuming someone else’s not-product, what’re your thoughts on Zig’s development? Clearly you’re fine without the 1.0.**

I knew what I signed up for. I got into Zig by doing compiler patches and got to know the community well. I grasp the culture, philosophy etc. well, so I’m not upset by any of this.

I expect the I/O change to be one of the hardest things we’ve done, but we haven’t started yet.

Zig’s getting more popular and Andrew, the BDFL, isn’t backing down from changes he feels are necessary, which I like as a downstream consumer. 0.15 was pretty significant, changing the writer interface and thus anything printing anything. But the API is truly so much better.

Zig is just getting better and better. They focus a lot on compilation tooling and even removed language features to improve compilation speed, mind blowing. You can build lib-ghostty (the entire terminal) instantly, and Andrew still thinks these milliseconds are too slow.

I do think Zig will eventually reach a 1.0, though I think it’s still years away. It matters far less when AI’s involved. I hope people know, reading this, that I’m no AI hype-master.

At a very basic level, we know these neural nets are really good at pattern matching and pattern filling. For these kind of language changes, I showed how to do it in a variety of contexts then asked it to draw the rest of the owl. And though, the diffs were huge, 90% was done automatically while I was in the kitchen. This hints to a future where backwards compatibility means a lot less if you explain how to go from state A to B.

This is a bit ironic given Zig’s strict anti-AI policy, but AI dulls the pain changes inflict on downstream users.

**How do you approach library and API design? Ghostty uses lib-ghostty. A friend was raving about how nice your libraries are to use. Do you have concrete methods to improve them besides just caring?**

The most concrete way is to use a lot of libraries in a lot of communities. Just like learning a programming language you won’t actually use (professionally), using libraries across ecosystems expands your perspective and benefits you. In university, I spent a lot of time dabbling with esoteric languages. I made many toy products in Prolog, Haskell, Clojure and even Java (I was never a professional Java programmer so it was new for me. I wrote a full web side project in it. I didn’t like it but learned a lot about the build system, ergonomics, libraries, web frameworks, web servers, app servers and all that stuff.) Every ecosystem has a different culture. That culture is human for sure, but it bleeds into how they separate concerns at a library and framework level, how they make those APIs look. For the longest time, Java used the builder pattern all over the place, which I didn’t see in any other language but I tried it in Ruby and it felt pretty good. That’s an example of porting concepts. This is how I approach library design: Try to use the concepts I found the most enjoyable and hope others with similar taste also enjoy it.

I firmly believe that “nouns” matter and the problem with Docker to me is there a ton of stuff that is focused on deployment/runtime aspects and it meddles with the human flow. The fact that Vagrant was focused directly, exclusively on development was by design: the configuration, the CLI, etc. revolved around development-focused nouns, and I think that was a good thing. - https://lobste.rs/c/ddl137


**Do you yourself make terminal applications dogfooding and testing these APIs and thoughts?**

Not enough, honestly. I’ve been a tool maker my entire career and firmly believe in the *tool maker’s dilemma* where you desperately need something and understand the problem space well, then build an ideal tool, but others like it and you become an ungrounded tool maker instead of the tool user. I’ve had this bite me many times. From the terminal perspective, I live in the terminal but from a TUI development perspective, I’m not doing enough, but a few of our maintainers are prolific TUI creators like rockorager who maintains multiple email and IRC clients and authored a few specifications. I’ve been leaning on him for this.

**Are you happy with today’s tech stacks? In the past, You mentioned nice-polished OS as products, big tech used to distinguish itself by technology too. But it seems like they’ve given up entirely, not dogfooding nor caring. Their open-source feels stagnated (with exception of the occasional exception like Jujutsu).**

I’m… … … …*okay* with today’s tech stacks. They’re *okay*. There’s obviously so much I wish were different but I can’t get too bogged down stressing about things I can’t change, about battles that aren’t mine to fight. For example, there’s a lot of good in the frontend, TypeScript, React type communities. But there’s also way too much churn, too much complexity, the layers of abstraction aren’t clear at all. I spent time studying them but just don’t agree at all with how the community culturally addresses them. But I’m not going to fight it, replace it. So I go with the flow, stick with the mainstream to assist with community, hiring etc.

I’m **fine** with today’s tech stacks. I think some of the more recent developments are overly complicated across the board. HTTP/1 vs. HTTP/2 and HTTP/3, there’s a non-linear change in complexity, justified in various ways but still difficult to swallow. You see that in frontend tech, terminal tech etc. I wonder if we’re moving so fast that we’re building complicated stuff which could have been simpler. “I didn’t have time to write a short letter, so I wrote a long one instead.” This seems to be playing out industry-wide, accelerated by AI and such tooling.

**Talking about Zig, you said you understood its values etc. At Hashicorp, you wrote a principles document. How do you decide, create, get buy-in and use principles day to day? Why is Ghostty e.g. feature-rich? How do principles concretely impact development?**

Even when my cofounder and I wrote the Hashicorp principles or when I decided how Ghostty would develop, it was all just personal, a reflection of me, so very easy for me to live those principles day to day. I just have to act myself. People run into problems when they make principles unlike themselves. It’s that New Year’s resolution problem where you make these grandiose intentions towards dramatic changes in your life but it’s very hard, because it’s hard to actually make those dramatic changes.

For Ghostty, I cared about some less human, more technical, feature-rich choices like having a cross platform core and very much not cross-platform but unapologetically native GUI. People who valued them would come on board and collaborate; those who disagreed just wouldn’t. And that’s awesome. I’m a really big fan of open-source projects and the internet being a collection of tribes.

I’m most annoyed by programming languages here, where so many languages are becoming like least common denominator **things** with people criticizing so and so for because it lacks this feature every other language has and is therefore useless. Some hyperbolic statement, you know. I really like the fact that certain languages lack certain features other languages enjoy, because these constraints breed creativity and culture. I want different places to feel different. I don’t need every place to feel welcoming to every person.

People are going to get mad at me for this, but you can keep it in. For example, for me, I don’t like the Rust culture. There’s no better way to put it. Every time I’ve interacted with them or hear how they talk about Rust, I just don’t like it. That doesn’t mean they’re bad people; I think they are really good people. The philosophy behind the language and the language itself is really good. I just don’t want to use it and there’s no problem with that. Just because I don’t want to be around a community doesn’t mean it’s bad. I also don’t like soccer.

But people on the internet get stuck into such binary views about good and bad, which bleeds into how technologies become this conformist pool of bleh.

Back to Zig, Zig has a really polarizing specific stance on what it does from technology, to community management and funding to PR, blog posts and how they talk. I don’t agree with all of it but I *so respect* that they are unapologetically weird. So I continue to support them financially and use their technology because I support people trying to be their own person.

**Large companies have gaping quality assurance issues, while smaller projects like Ghostty or Zig let you apply taste to replace 4 PRs with a single, holistic solution (human scale). How do you reconcile shipping quality with shipping fast, yea AI-generated code etc.?**

To ship the right thing, there has to be a bigger understanding of the product you’re working on. This role’s solved by different people in different companies but generally corporate America doesn’t do a great job of this at scale. You can’t just listen to a specific problem a set of customers or users have and solve that specific problem. You need to understand how they got to that problem in the first place, outside of your software. What motivated that problem? Whether they should have reached this in the first place or whether something upstream would have resolved 3 other problems? You need a bigger, holistic understanding. IDK how to solve that at the corporate scale. But I handle it by being a big user of my own software.

I know not everyone can do this, but I’ve only worked in jobs whose product I’m a user of, so I can be a good human judge of whether my work is good. If you’re too far removed from the customer, you shift to “I completed the spec” or “I checked the box” lacking a deep enough understanding to say whether it’s good or bad.

I know this community has a pretty polarizing split on the AI side, but I’ve been a big proponent of rational AI usage. I fully sloppified demos etc. because I won’t ship it. The code is complete trash, but I can play and check whether something’s a useful direction. If it’s good, I can restart with the care it deserves. Right now, I have a 6 week old baby and am only on the computer about 3 hours a day, so any time savings really helps. Now, I can do so much more because I can ship ideas to myself without being on the computer.

You just have to ship quality, read and understand the code you ship and have empathy with the users who will use this. You want to create something they’re going to have joy using. That’s all that matters.

**How would you suggest someone learn C today? Would it make sense to start directly with Zig?**

It’s more important to learn how computers work and make the language just a means to understanding how they work. My heaviest usage of C was in college, revolving around file systems and operating systems in 3 classes. C was just the mechanism by which we interfaced closely with the lower level systems involved. My suggestion, even in this age of higher level abstractions and web development, it’s still important to understand the basics of CPU scheduling, memory, cache hierarchies, file systems, disc and file access. When you work directly above the syscall layer, whether in C, Zig or Rust, it really helps you understand what’s happening. If you go too high level, a Python, JavaScript or a Ruby’s file open API really abstracts quite a lot from you.

Another way I learned a lot was reading how the higher level languages are implemented. Don’t take a standard library function for granted, some human wrote that and you could too. How does it work? Read the stdlib and dig into how things work. Languages are easy; languages don’t matter. The underlying understanding is what matters.