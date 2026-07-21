---
title: The human-in-the-loop is tired
source: https://pydantic.dev/articles/the-human-in-the-loop-is-tired
author:
- '[[haritha1313]]'
published: '2026-07-17'
created: '2026-07-17'
manifest_dates:
- '2026-07-17'
description: 'Article URL: https://pydantic.dev/articles/the-human-in-the-loop-is-tired
  Comments URL: https://news.ycombinator.com/item?id=48942000 Points: 208 # Comments:
  110'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4cfba9bf3df018bc
source_type: community_discussion
tldr: Pydantic 团队成员撰文指出，LLM 辅助编程在提高效率的同时带来了新的"监督疲劳"：开发者从亲手编码的满足感转向无休止的审查和纠错，工作变得更加孤独且缺乏成就感。作者将此定义为"人类奖励函数问题"，认为这并非个人失败而是工程挑战，核心技能正从编写代码转向工程判断力与品味。
objective_summary: Pydantic 团队成员在其公司博客发文，从亲身经历剖析了 LLM 辅助编程对开发者的心理冲击。文章提出"监督疲劳"概念：LLM
  每天自动生成大量代码，开发者需要花费大量时间审查、纠正和重新指定意图，工作强度增加但满足感下降。作者将此称为"人类奖励函数问题"——LLM 自动化了编码中产生多巴胺满足感的部分（解决问题、编译成功），但未提供新的奖励机制替代，导致反馈回路断裂。文章还指出
  LLM 编程是一种高度孤独的活动，减少了团队协作中自然的知识交流，具有成瘾性（斯金纳箱效应）。作者将当前转变与 2009 年响应式设计转型类比，认为软件工程的核心技能（判断力、品味、架构决策）正在变得更关键而非过时。
event_type: application_landing
epistemic_status: theoretical_claim
entities:
  companies:
  - Pydantic
  technologies:
  - LLM
  key_people:
  - Douwe
  - Simon Willison
  - Marcelo
  - Ethan Marcotte
key_logic_flow:
- LLM 辅助编程既真实有用又令人不安，这两个事实同时存在，忽视后者会导致集体倦怠。
- 作者提出"监督疲劳"概念：开发者每天需要审查大量 LLM 生成的代码，判断力成为瓶颈，工作强度增加而满足感下降。
- 作者提出"人类奖励函数问题"：LLM 自动化了编码中产生多巴胺满足感的部分，却未提供新的奖励来填补缺口，导致反馈回路断裂。
- LLM 编程是高度孤独的活动，减少了自然产生的同事协作与知识交流，且具有成瘾性的斯金纳箱效应。
- 作者将当前转变与 2009 年响应式设计转型类比，认为核心软件工程技能（判断力、品味、架构决策）正在变得更关键而非过时。
- 新的应对技能正在涌现，例如对复杂计划进行"事前验尸"（pre-mortems），以及将隐性工程判断编码为 LLM 可读的指令文件。
object_mentions:
- object_type: project
  name: Pydantic AI
  canonical_name: Pydantic AI
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者同事 Douwe 维护 Pydantic AI 框架，每天需要审查数十个由 AI 生成的 PR，面临将审查也委托给 AI 的诱惑。
  - Pydantic 公司构建的工具帮助开发者验证数据、构建 AI 代理并观测生产系统的运行状态。
  article_id: 4cfba9bf3df018bc
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Pydantic 同事 Marcelo 在被问及其 Claude Code 会话冻结时开玩笑说，开五个 Claude 会话就不会注意到，因为忙于给其他会话提供反馈。
  article_id: 4cfba9bf3df018bc
extract_result: success
impact_score:
  score: 5.0
  reason: 这是一篇观点文章而非技术产品发布或融资事件，不直接改变竞争格局。但其提出的'监督疲劳'和'人类奖励函数问题'两个概念精准命名了LLM辅助编程时代广泛存在但未曾被系统表述的心理体验，具有较高的概念传播潜力。Pydantic作为AI开发者工具领域的知名公司，其团队成员的反思在开发者社区中有较强公信力。短期内不会引发行业范式转移，但可能促使更多关于AI工具开发者体验的讨论，并对AI辅助编程工具的产品设计方向产生温和的长期影响。
sentiment: mixed
developer_sentiment:
  tone: frustrated
  primary_focus: LLM辅助编程虽提高了产出效率，但代码审查和纠错成为新的认知负担，编码的满足感和团队协作感反而下降
hype_assessment:
  level: low
  reason: 文章完全没有使用'颠覆'、'革命性'等PR话术，反而主动抵制了AI hype叙事。作者明确声明'这不是一篇关于AI是否会取代程序员的思考文章，不是末日论也不是炒作文'，并以亲身经历坦诚描述LLM编程带来的心理困境，整体文风诚实、自省、有洞察力。
information_entropy: high
domain_disruption:
  technical_innovation: 无。本文为观点文章，不涉及技术突破，但提出的'人类奖励函数问题'概念框架可能影响未来AI辅助编程工具在反馈机制和开发者体验方面的设计方向。
  business_model: 无直接商业模式影响。但文章指出的LLM编程导致团队协作减少、知识传递断裂以及斯金纳箱成瘾效应，可能推动AI开发工具市场从单纯的'代码生成效率'竞争转向更注重开发者长期福祉和团队协作体验的产品差异化方向。
engineering_complexity: conceptual
compound_value:
  score: 7.5
  reason: 文章提出的'监督疲劳'与'人类奖励函数问题'精准定义了LLM辅助编程时代的结构性瓶颈——代码生成能力大幅提升，但人类审查能力成为不可扩容的稀缺资源，且随生成量增加这一矛盾只会持续恶化。这不是暂时性问题，而是AI开发生态演进中的核心矛盾，将催生一类新的基础设施需求：能降低审查认知负荷、重建开发者反馈回路、将隐性工程判断编码为可执行规则的工具链。Pydantic作为Python生态中数据验证的事实标准（日均下载量数千万），其团队对该问题的深度认知进一步强化了其在AI中间件层的生态站位。该问题对应的解决方案（验证层、可观测性、AI代码质量门禁）在3-5年后大概率成为AI开发工作流的标配组件。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Pydantic
- GitHub Copilot
- AI可观测性平台
- AI代码质量与验证工具
competitive_casualty:
- 纯代码生成工具（缺乏质量反馈闭环）
- 传统静态分析厂商
- 低代码/无代码平台（LLM加速其替代）
market_opportunities:
- 开发者工具团队可打造"LLM 代码审查质量仪表盘"，通过批量差异高亮、语义归类（安全风险/风格问题/逻辑错误）和优先级排序，直接缓解监督疲劳中的判断力瓶颈问题
- 企业培训与工程效能咨询市场可围绕"AI 辅助工作流重塑"开辟新业务线，帮助团队将编码满足感重新引入 AI 驱动的工作流程（如结构化代码评审仪式、结对编程的 AI
  替代方案）
- 创业者可开发将隐性工程判断编码为 LLM 可读指令的知识管理工具（如自动化"事前验尸"模板与架构决策记录生成器），填补人类品味与 AI 生成之间的鸿沟
risk_matrix:
  regulatory: 无
  technological: 若监督疲劳问题长期得不到系统性解决，团队可能被迫接受低质量 LLM 输出，导致代码库隐性技术债务加速累积，架构一致性在大型变更中持续退化
  competitive: 大型云厂商（GitHub Copilot、Cursor）具备将"减少审查负担"作为差异化功能的资源和数据优势，独立工具厂商如 Pydantic
    可能面临生态挤压
  ethical: LLM 编程的去社交化特性正在削弱师徒制知识传递机制，可能系统性削弱初级开发者成长路径；叠加斯金纳箱式的成瘾性交互模式，开发者心理健康风险显著上升
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Pydantic AI
  canonical_name: Pydantic AI
  url: https://ai.pydantic.dev
  positioning: Pydantic AI 是 Pydantic 公司开发的 AI 代理框架，专注于将数据验证能力融入 LLM 应用，帮助开发者构建可靠的
    AI 驱动软件系统。
  technical_signal: Pydantic AI 将类型安全的数据验证与 AI 代理编排深度结合，确保 LLM 输出结构化且符合预期的格式要求。
  adoption_signal: Pydantic 团队在开源维护中深度使用该框架，每天需处理数十个 AI 生成的 PR，频繁面临审查代理代码的挑战。
  ecosystem_relevance: 与 Pydantic 数据验证库形成互补生态，填补了 LLM 应用中结构化输出验证与代理编排的关键需求空白。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Pydantic AI 是 AI 代理框架领域的重要参与者，其将数据验证与代理编排结合的设计理念，为解决 LLM 应用可靠性问题提供了独特路径，值得持续关注其生态演进与社区采纳趋势。
  risk_notes:
  - 团队自身面临 AI 辅助编程带来的监督疲劳，框架的开发体验与迭代效率可能受此负面影响。
  - 框架的采用高度依赖 Pydantic 生态渗透率，在非 Python 或非 Pydantic 用户群中缺乏天然竞争力。
  score: 6.0
  article_ids:
  - 4cfba9bf3df018bc
  evidence_snippets:
  - 作者同事 Douwe 维护 Pydantic AI 框架，每天需要审查数十个由 AI 生成的 PR，面临将审查也委托给 AI 的诱惑。
  - Pydantic 公司构建的工具帮助开发者验证数据、构建 AI 代理并观测生产系统的运行状态。
---

Yet another thought piece about LLMs. I know. Bear with me.

This is an attempt to put words around something I think most developers are experiencing right now but haven't had time to make sense of. **Programming with LLMs is genuinely useful and genuinely destabilizing. These two things coexist. If we pretend the second one isn't happening, we will all burn out.**

At Pydantic, we build tools that developers use to validate data, build AI agents, and observe what their systems are doing in production. We are, quite literally, in the business of making LLM-powered software more reliable. And we are *also* having a weird time.

This isn't a thinkpiece about whether AI will replace programmers. It's not a doomer essay and it's not a hype piece. It's an honest account of what it feels like to be a developer right now, from someone inside it, and some thoughts on what might actually help.

When I was first learning to code in my early twenties, I remember having this distinct sensation that programming let me dip my hands into the fabric of the universe and shape it to my will. This was, of course, before I'd hit too many compile errors. But that feeling of touching some deep fundamental layer of abstraction, of being able to *make things* from nothing but logic, has always stuck with me.

I'm not a Computer Science graduate. I'm a designer and a programmer — formally trained in the first, self-taught in the second. I came to the formalisms of software engineering through painful experience rather than academic instruction. If anything, that made me take those principles *more* seriously once I understood them. When you've earned your opinions about architecture and code quality the hard way, they feel less like textbook rules and more like scar tissue.

That primal feeling of creation? It's the same promise that the low-code and no-code tools of the 2010s kept making but never quite delivered on. I'm old enough to remember building web pages in Dreamweaver, watching Adobe spruik zero-code design tools that generated absolute spaghetti under the hood. It was always *almost* there, just good enough to hint at a future that was just around the corner (if only you were smart enough to grasp it).

If you're cynical about the current wave of AI tools, I get it. We've been promised this before. But this time the gap between promise and reality has actually, finally, narrowed to something meaningful. And that's exactly what makes it so unsettling.

Yes the code (sorta) writes itself, but the human reviewing, directing, and course-correcting feels worse, not better.

I recently had a conversation with my colleague Douwe, who maintains the Pydantic AI framework and has been one of the most thoughtful people I know about integrating LLMs into open source workflows. He described waking up to thirty PRs every morning, each one pulled overnight by someone's AI, and needing to make snap judgment calls on every single one. The temptation to delegate the review itself to an AI was enormous. But, as he put it: *"at that point, what am I still doing here?"*.

The honest truth is that in the last few months, there have been days when I have spent close to two full days writing a plan for an LLM to execute: obsessively clarifying, specifying, re-specifying, only to have it still do something inexplicably stupid. Port a React hook into a Storybook story file. Read from the wrong plan. Invent components that don't exist. And these aren't errors of capability; they're errors of coherence. The models are smart enough to produce plausible code, but not always smart enough to maintain a coherent intent across a complex change.

This creates a peculiar new kind of fatigue, the fatigue of *supervision*: of holding the intent in your head while the machine generates volumes of mostly-correct output that still needs your eyes, your judgment, and your taste. Douwe put it well: he used to get a dopamine hit from collaborating with a real person on a cool feature in open source. Helping someone become better at their craft. Now, he said, *"everything I write goes into some AI black hole. There's no person on the other side actually learning anything."* That loss is real and it's worth naming.

Simon Willison recently highlighted a Berkeley Haas study which describes how AI usage increases the *intensity* of work. The constant pull of "one more prompt at the end of the day, one more feature that could make this perfect." I felt that one in my bones. I was up until nearly 2am recently, prompting, because I was *so close* to getting a plan right. Or so I thought.

Marcelo, another Pydantic colleague, when asked about his Claude Code session freezing said: *"just open 5 claude sessions. You'll never notice because you're busy giving feedback to the others."* He was joking. I think. But it captures something true about the current moment. The parallelism is exhilarating and kind of feral. The number of things you can *start* has dramatically increased. The number of things you can thoughtfully finish hasn't changed at all, because that part still requires the one resource we can't parallelise: your brain.

Here's a term for what I think is happening: **the human reward function problem**. In machine learning, a reward function tells an agent what *good* looks like. Writing code by hand was never easy, but it was full of small rewards. Solving a problem in your head. Understanding a gnarly bit of logic. Watching the code compile. The feeling of control. LLM-assisted programming has automated much of the work that generated those dopamine hits and replaced it with the cognitive load of review and supervision. The satisfying part shrank. The exhausting part grew. And there are no new rewards to fill the gap.

If you're feeling like your work is simultaneously more productive *and* less satisfying, you're not broken. The feedback loop is broken. And I think we need to start treating that as an engineering problem in its own right, not a personal failure.

It's also, frankly, quite lonely. Programming with an LLM is an intensely solitary activity.

You and the machine, going back and forth, refining and prompting and reviewing. The natural moments where you'd turn to a colleague to ask a question, to rubber-duck a problem, to share the small victory of something finally clicking. Those moments get quietly replaced by another prompt. In a team without a strong existing culture of collaboration, this has a tendency to further separate people, to chill communication at precisely the moment when you most need the reassurance that other humans are finding this hard too.

And it's addictive in a way that makes the isolation worse. Sometimes you get something brilliant, sometimes garbage, and you never quite know which. Textbook Skinner Box. It can be genuinely hard to step back and remember that you're allowed to just... write code. But switching between LLM-assisted and manual work is jarring and uncomfortable, two very different modes of thinking, and it takes a kind of maturity and confidence to give yourself permission to switch.

This moment brings to mind the fear and angst caused by responsive design. I was working as a designer and frontend developer at the time, following Ethan Marcotte and the Zeldman / A Book Apart crowd like everyone else, and I remember how unsettling it felt to be told that the fixed-width layouts we'd all mastered were basically over.

For the younger devs: there was a genuine cultural moment around 2009 when websites moved from fixed, pixel-perfect, magazine-style layouts to fluid, responsive ones. And designers *hated* it. The loss of control was existential for people whose entire identity was built around precise layouts and perfect grids. You're telling me the user might see my design at *any* width? On *any* device? That the layout I crafted would... *flow?*

Image design by Jyotika Sofia Lindqvist


The resistance was intense. And it was understandable. People had built real expertise in a paradigm that was being fundamentally disrupted. The designers who thrived through that transition were the ones who reframed their skills. The eye for proportion still mattered. The understanding of hierarchy still mattered. The craft didn't die, it evolved. What became less relevant was the obsession with pixel-level control. What became more relevant was understanding systems, adaptability, and designing for uncertainty.

I don't want to oversell this parallel. Responsive design played out over years. The current shift is measured in months. Agencies lost clients and designers lost gigs over the responsive transition, but it didn't carry the same existential dread. The stakes are materially different, and the pace is genuinely exhausting in a way that the responsive transition never was. But the underlying pattern, of craft evolving rather than dying, of the core skills mattering more not less, I think that holds.

Working with LLMs on code feels like a similar inflection point. The skill isn't gone, it's shifting. You're not less of an engineer because you didn't hand-write every line. But you do still need to know what good looks like, arguably more than ever, because you're now the quality gate for a much higher volume of output.

In an era when anyone can produce reasonable-looking UI and code that compiles, the distinguishing markers become: taste, nuance, mature architectural opinions, and the contrarian calls that come from genuine expertise rather than pattern-matching.

It's noticeable to me that we are most successful guiding LLMs in the domains where we understand the code, the decisions, and the trade-offs most deeply. As we venture into the shallow ends of our skill sets, the outputs become markedly more *impressionistic*. Further from production-ready. More plausible-looking, less actually correct. The model doesn't know what it doesn't know, so it fills the gaps with confidence. Sound familiar? It's a very human failure mode, too.

But new skills are also emerging. I've started running what I call pre-mortems on complex plans: asking a fresh LLM session to assume the plan has catastrophically failed and diagnose why. It catches specification gaps that I miss after two days of being too deep in the details. One of our engineers built a tool that extracts rules from thousands of his past code review comments to seed an `AGENTS.md`

file, essentially encoding years of implicit engineering judgment into instructions an LLM can follow. That's not the death of expertise. That's expertise being *distilled*.

The people who are finding their footing right now seem to share a few traits: they have strong opinions earned through practice, they can distinguish between principles that still apply and habits that were just bandwidth constraints, and they're willing to evolve their workflow without abandoning their standards.

I don't think the current wave of AI represents the end of software engineering as a profession. I do think it represents a serious contraction and a fundamental reshaping of what the work *is*. The fear of obsolescence is legitimate. The fear of skill rot is legitimate. And the fear that if you don't go fast enough you'll be left behind is — while often overstated — not entirely unfounded.

But the bottleneck was never the code. It was always the human attention, the engineering judgment, the ability to hold a coherent vision for a system. We just didn't notice because writing code *felt* like the hard part. Now that it's being automated, those human capacities are revealed as the actual scarce resource. And scarce resources are valuable.

So if you're feeling overwhelmed, destabilized, simultaneously more productive and less happy, know that you're not alone. The team building the tools you're probably using to navigate this moment is feeling it too. We're debugging our reward functions in real time, same as you.

The code is changing. What we do with it is changing. How it feels is... a work in progress.

But the humans are still in the loop. We're just tired. And that's worth talking about.

*We're building tools to make this less chaotic: Pydantic AI and Logfire. We're also hiring.*