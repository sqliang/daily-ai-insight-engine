---
title: Claude Fable 5
source: https://www.anthropic.com/news/claude-fable-5-mythos-5
author:
- '[[Philpax]]'
published: '2026-06-09'
created: '2026-06-10'
description: 'System Card [pdf]: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c3...
  Comments URL: https://news.ycombinator.com/item?id=48463808 Points: 2216 # Comments:
  1709'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e11fcea9cd94bb20
source_type: community_discussion
tldr: Anthropic发布Claude Fable 5（通用版）和Claude Mythos 5（受限版），性能超越此前所有公开模型。
objective_summary: Anthropic于2026年6月发布Claude Fable 5和Claude Mythos 5。Fable 5面向所有用户，配备安全分类器对高风险查询降级至Opus
  4.8；Mythos 5通过Project Glasswing向网络防御者提供。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Stripe
  - GitHub
  - Cursor
  - IMC
  - Hebbia
  - Cognition
  technologies:
  - Claude Fable 5
  - Claude Mythos 5
  - Project Glasswing
  key_people: []
key_logic_flow:
- Anthropic同时发布了Claude Fable 5（通用安全版）和Claude Mythos 5（受限高能力版），二者基于同一底层Mythos-class模型。
- Fable 5配备安全分类器，对高风险查询会降级至Claude Opus 4.8响应，分类器误报率在平均不到5%的会话中触发。
- Mythos 5通过Project Glasswing与美国政府合作部署，具备全球最强的网络安全能力，后续将通过更广泛的信任访问计划开放。
- 定价为每百万输入token 10美元、每百万输出token 50美元，低于Claude Mythos Preview的一半。
- Fable 5在软件工程、知识工作、视觉、记忆与长上下文、生命科学研究等多个领域的基准测试中达到业界领先水平。
- Mythos 5在蛋白质设计中加速了约10倍的流程，能自主完成科学家级别的全流程任务，并在分子生物学假设生成和基因组学研究中取得突破。
impact_score:
  score: 8.0
  reason: Anthropic 发布 Claude Fable 5（通用安全版）和 Mythos 5（受限高能力版），这是 2026 年最重要的模型发布之一。Fable
    5 在软件工程、知识工作、视觉、长上下文、生命科学等几乎所有基准测试中达到业界领先水平，且定价仅为 Mythos Preview 的一半（$10/$50 per
    M tokens）。Stripe 实战验证了其在 5000 万行 Ruby 代码库中将数月工程压缩为一天的效率。Mythos 5 在蛋白质设计中实现约 10
    倍加速，并能自主完成科学家级别的全流程任务。双轨部署策略（安全分类器降级 + 政府受限访问）为前沿模型治理提供了新范式。这改变了头部大模型的竞争格局，对应用层和基础设施层均有深远影响，但尚未达到
    ChatGPT 发布级别的范式转移，故评分 8.0。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Fable 5 编程能力大幅提升且价格减半，自主 Agent 能力显著增强
hype_assessment:
  level: medium
  reason: 文章使用了 'state-of-the-art on nearly all tested benchmarks'、'profound good
    for the world' 等典型 PR 表述。但提供了大量可验证的具体信息：明确的产品定价（$10/$50）、安全分类器误报触发率（平均不到 5% 会话）、具体客户案例（Stripe
    5000 万行代码库迁移、IMC 交易分析、Cognition FrontierCode 评测）、量化结果（蛋白质设计加速约 10 倍、9/14 靶点产生候选药物、分子生物学假设被独立实验室证实）。干货与包装并存，整体水分中等。
information_entropy: high
domain_disruption:
  technical_innovation: Fable 5 基于 Mythos-class 底层模型，通过安全分类器对高风险查询自动降级至 Opus 4.8 响应，实现前沿模型的安全通用部署。模型在无需人类辅助的情况下自主执行完整的蛋白质设计流程（选择结合位点、运行工具、错误恢复），在
    Pokemon FireRed 中以纯视觉 minimal harness 完成通关，并具备持久化文件记忆显著提升长任务表现。Mythos 5 在分子生物学假设生成和基因组学自主研究中展示了媲美科学家的能力，是首个能持续产生新颖科学假设的模型。
  business_model: 双轨部署策略是本次发布的商业模式创新核心：Fable 5 面向公众（带安全过滤器），Mythos 5 通过 Project Glasswing
    与美国政府合作向网络防御者提供，后续将通过信任访问计划扩展。定价较 Mythos Preview 降低 50% 以上，对 OpenAI、Google 等竞争对手形成显著的性价比压力。这种
    '安全通用版 + 受限高能力版' 的分层模式可能成为前沿模型商业化的新标准，也验证了 AI 安全治理与商业利益可以协同演进。
engineering_complexity: production_ready
compound_value:
  score: 9.2
  reason: Claude Fable 5 代表当前公开可用的最强模型能力，在软件工程、科学研究、知识工作、视觉等多个维度实现全面领先。其定价（$10/$50
    per M tokens）仅为上一代旗舰 Mythos Preview 的一半，大幅降低使用门槛，加速采纳飞轮——Stripe 的案例显示单日完成全代码库迁移体现了极强的生产力复利。安全分类器架构+Project
    Glasswing 政府绑定形成了制度性护城河，Mythos 5 在蛋白质设计（10倍加速）和分子生物学假设生成方面的突破打开了生命科学这一全新价值池。长上下文和自主任务能力的提升意味着该模型将成为复杂
    Agent 工作流的首选底座。3-5 年内，随着更多数据反馈和微调，Fable 5 极大概率仍是行业关键基础设施。主要风险在于 OpenAI/Google
    的追赶速度，但 Anthropic 安全优先策略和政企合作提供了差异化壁垒。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Stripe
- GitHub
- Cursor
- Cognition
- IMC
- Hebbia
- AWS
competitive_casualty:
- OpenAI
- Google DeepMind
- xAI
- Mistral
- 专业蛋白质设计初创公司
- 传统知识工作自动化SaaS
market_opportunities:
- 生命科学领域的企业可基于Mythos 5构建蛋白质设计与分子生物学假设生成的自动化管线，将药物发现流程从数月压缩至数天，具备明确的商业变现路径
- 大型企业的工程团队可利用Fable 5在千万行级代码库中执行自动化迁移和重构，将此能力封装为'AI驱动的技术债务清理'服务，具有高客单价的SaaS或项目制变现潜力
- 金融和咨询机构可基于Fable 5在文档推理、图表解读和根因分析方面的领先能力，开发面向投行研报、审计合规的高级分析助手，切入知识工作自动化的高附加值场景
risk_matrix:
  regulatory: 安全分类器将高风险查询降级至Opus 4.8的机制可能面临欧盟AI Act下'通用目的人工智能系统'的合规审查；Mythos 5通过Project
    Glasswing与美国政府合作部署的排他性安排可能引发出口管制和地缘政治敏感性质疑
  technological: 安全分类器的误报（平均不到5%的会话触发）可能导致部分合法请求被不必要降级，影响用户体验和开发者的预期确定性；底层Mythos-class模型的技术优势窗口可能被竞品（如GPT-5、Gemini
    Ultra）迅速缩小
  competitive: OpenAI、Google DeepMind等竞争对手可能在未来数月内发布对标模型，引发新一轮基准测试军备竞赛和价格战；定价已低于Mythos
    Preview一半以上，进一步压缩下游AI应用开发商的利润空间
  ethical: 模型在网络安全和自主科研领域的强大能力存在双重用途困境：既可用于防御性网络保护，也可能被恶意行为者滥用；蛋白质设计与基因组学研究的加速可能引发生物安全和伦理审查的边界争议
  additional:
  - 对Anthropic单一供应商的依赖风险——Fable 5在多个基准上领先但API仍受限于Anthropic的基础设施和可用性SLA
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

# Claude Fable 5 and Claude Mythos 5

Today we’re launching **Claude Fable 5**: a Mythos-class1 model that we’ve made safe for general use.

Fable 5’s capabilities exceed those of any model we’ve ever made generally available. It is state-of-the-art on nearly all tested benchmarks of AI capability, showing exceptional performance in software engineering, knowledge work, vision, scientific research, and many other areas. The longer and more complex the task, the larger Fable 5’s lead over our other models.

Releasing a model this capable comes with risks. Without safeguards, Fable 5’s capabilities in areas like cybersecurity could be misused to cause serious damage. We’ve therefore launched the model with safeguards that mean queries on some topics will instead receive a response from our next-most-capable model, Claude Opus 4.8. To release the model both safely and quickly, we’ve tuned these safeguards conservatively—they’ll sometimes catch harmless requests, though they trigger, on average, in less than 5% of sessions. With more capable models arriving in the coming months, we’re working to improve our safeguards and reduce false positives as quickly as we can.

For a small group of cyberdefenders and infrastructure providers, we’re also launching **Claude Mythos 5**. It’s the same underlying model as Fable 5, but with the safeguards lifted in some areas.2 Mythos 5 will initially be deployed through Project Glasswing, in collaboration with the US government, as an upgrade to Claude Mythos Preview. It has the strongest cybersecurity capabilities of any model in the world. Soon, we intend to expand access to Mythos 5 through a broader trusted access program.

The capabilities of models like Fable 5 and Mythos 5 have the potential to do profound good for the world. We’ve seen the beginnings of this in Project Glasswing, where the models have helped cyber defenders secure critically important software. We’ve also seen it in life sciences research, where the models are positing novel hypotheses and speeding up the development of new therapeutics.

Fable 5 and Mythos 5 are being offered at $10 per million input tokens and $50 per million output tokens—less than half the price of Claude Mythos Preview. Today’s joint launch is another step towards our goal of bringing advanced AI capabilities to as many users as possible, as quickly and as safely as we can.

## Evaluating Claude Fable 5 and Claude Mythos 5

The table below compares the capabilities of Fable 5 and Mythos 5 to other leading models.


Fable 5 and Mythos 5 can work autonomously for longer than any previous Claude models. Below we discuss how these skills apply to software engineering, and cover the model’s improved capabilities in knowledge work, vision, memory, and life sciences research.

*Software engineering. *During early testing, Stripe reported that Fable 5 compressed months of engineering into days. In a 50-million-line Ruby codebase, the model performed a codebase-wide migration in a day that would otherwise have taken a whole team over two months by hand. Fable 5 is also more token-efficient than past Claude models: on Cognition’s FrontierCode evaluation, which tests whether models can pass difficult coding tasks while meeting the standards of high-quality production codebases, Fable 5 scores highest among frontier models, even at medium effort.

*Knowledge work*. Fable 5 shows strong performance on complex analytical tasks. On Hebbia’s Finance Benchmark for senior-level reasoning, Fable 5 has the highest score of any model, with substantial gains in document-based reasoning, chart and table interpretation, and problem solving. IMC noted that Fable 5 aced their trading-analysis evaluations nearly across the board, including factual lookup, conceptual reasoning, root-cause analysis, and expected-value analysis.

*Vision.* Fable 5 is the new state-of-the-art model for tasks involving vision. It can extract precise numbers from detailed scientific figures and can perform complex vision-based tasks like rebuilding a web app’s source code from screenshots alone. It also needs less scaffolding: for example, previous Claude models struggled to play Pokémon FireRed even with harnesses that gave them additional helpful tools, but Fable 5 beat FireRed with a minimal, vision-only harness.

*Memory and long-context. *Fable 5 stays focused across millions of tokens in long-running tasks and improves its outputs using its own notes. When we had the model play the deck-building game *Slay the Spire*, giving it access to persistent file-based memory improved its performance three times more than for Opus 4.8; Fable also reached the game’s final act three times more often.

*Drug design:* Using Mythos 5, our internal protein design experts accelerated aspects of the drug design process by around ten times. In one example, they found that Mythos 5, with protein design and bioinformatics tools but no human assistance, matches or beats skilled human operators. In doing so, the model executes all of the tasks that are normally completed by a scientist: choosing binding sites, selecting and running protein design tools, and recovering from failures along the way. Nine of the 14 protein targets from this study (shown below) yielded strong candidates for drug design that we’re currently investigating.

*Novel hypotheses in molecular biology.* Mythos 5 is our first model to consistently produce novel, compelling scientific hypotheses. In blinded head-to-head comparisons against Opus-class models, our scientists preferred Mythos’s molecular biology hypotheses ~80% of the time, and have advanced several to experimental evaluation. In the meantime, one Mythos hypothesis—a novel mechanism for an *E. coli* protein—was corroborated in a study from a lab independently working on the same problem.

*Novel research in genomics.*** **Mythos 5 conducted novel genomics research in over a week of largely autonomous work. It assembled single-cell data for millions of cells spanning 138 animal species and designed and trained a custom machine learning model to identify cells performing the same role in even distantly related organisms. With only high-level human input, Mythos 5’s trained model outperformed a recent model published in the journal *Science*—despite being 100 times smaller. We intend to publish these results in the coming months.

*Alignment*. In our automated alignment assessment we found that Mythos 5’s level of misaligned behavior (including misaligned actions taken by the model such as deception, and cooperation with misuse of the model by a user) was low, and similar to that of Opus 4.8. Given they are the same underlying model, Fable 5’s level of alignment will be similar. The assessment is described in full, along with a detailed suite of other safety and capabilities tests, in the model’s system card.

## Early feedback for Claude Fable 5

Customers with early access ran their own tests on Fable 5. Below, in their words, is a selection of what they’re seeing:

Claude Fable 5 is the state of the art model on CursorBench. It's opened up a class of long-horizon problems that were out of reach for earlier models.

Claude Fable 5 is a real step forward for the developers GitHub serves. In our early testing, it took on complex, long-horizon coding tasks with a level of autonomy and reliability that exceeded previous benchmarks. But what excites us most is the direction it points: a future where developers can hand increasingly ambitious work to agents and trust the results across the software lifecycle.

These are the strongest results of any Claude model we've had the opportunity to test. Claude Fable 5 is a clear step forward on agentic coding and prototyping.

Claude Fable 5's reasoning is a clear step beyond Opus 4.8. It works at senior research scientist grade — picking directions, allocating resources, killing its incorrect beliefs, and producing novel first-principles outputs.

Claude Fable 5 understands what builders mean, not just what they type. Apps that took a hundred prompts a year ago, it now one-shots. When a customer really hits a wall, it's the model we reach for to get them past it quickly, so they can finish what they set out to build.

Claude Fable 5 feels materially different. In blind review, our lawyers found its redlines matched or beat our current model every time.

At the highest effort, Claude Fable 5 reflects on and validates its own work. For us, that's what makes highly autonomous operations possible — the extra thinking pays for itself.

Claude Fable 5 delivers more capable engineering in fewer turns than prior models — handling the complex multi-agent workflows our employees run daily in Claude Code.

Claude Fable 5 is the highest-scoring model on FrontierBench, Cognition's frontier coding eval. It excels at long-horizon reasoning and generalizes to unfamiliar tools out of the box.

Claude Fable 5 is the strongest finance-first model we've tested, both on general finance and reasoning. It's a notable step up.

Claude Fable 5 is the first to break 90% on our core analytics benchmark of complex, long-running analytical tasks — a 10-point jump over Opus. On the hardest questions, it shows strong judgment and attention to nuance.

Claude Fable 5 is the strongest model we've tested on frontier physics research while using a third of the reasoning tokens. In 36 hours it got nearly to where GPT-5.5 landed after four days.

On ViBench, our end-to-end vibe-coding benchmark, Claude Fable 5 is the highest-performing model we've tested — nearly saturating our base use cases and building apps in less time with fewer tokens.

Claude Fable 5 beats Opus 4.8 on our everyday spreadsheet suite at every effort level — and it does it with fewer turns, finishing runs 25–30% faster.

## Claude Fable 5’s new safeguards

Mythos-class models have reached a threshold where they present significant risks. In April we began Project Glasswing, releasing the first Mythos-class model (Claude Mythos Preview) to only a limited group of cyber defenders and critical software infrastructure providers. When we did so, we stated that we hoped to eventually release Mythos-level capabilities to all our users, so long as we had developed new safeguards that were strong enough to reliably prevent misuse.

Over the past few months we have been improving these safeguards, and they are now robust enough for a general release. Because we have prioritized safety, we’ve deliberately tuned the safeguards to be cautious, and they are still stricter than would be ideal—for example, sometimes benign requests will trigger our classifiers. We recognize that this will be frustrating to some users, and our aim is to reduce false positives as we update and refine the safeguards after launch.

Below we discuss each of Fable 5’s new safeguards in turn. Our wider suite of safeguards is discussed and evaluated in the model’s system card and our most recent risk report.

### Safety classifiers

The frontier cybersecurity and research biology capabilities of Mythos-class models mean that they pose a substantial risk of *uplift* to malicious actors. That is, these models could provide information or advice that assists those actors in causing serious harm that they couldn’t have received from other sources (for example, from internet search engines). Furthermore, a great deal of advanced usage of AI models is dual use: the same queries that are beneficial in the hands of cybersecurity professionals and biology researchers could be dangerous if available to malicious actors.

We therefore need strong safeguards to prevent misuse, and their coverage needs to be broad. The safeguards themselves have to stand up to sustained and sophisticated attempts to bypass them (also known as “jailbreaking” the system). The uplift from Mythos-level capabilities is valuable to many adversaries—for instance, those who could financially gain from cyberattacks—and we therefore expect them to be motivated to try to circumvent our safety measures.

Fable 5 comes with a new set of *classifiers*: separate AI systems that detect potential misuse, including jailbreak attempts, and prevent the main model (in this case Fable 5) from responding. We’ve been running classifiers on our models for some time, and Fable 5’s classifiers are an extension of this previous work with extra coverage.

When Fable’s classifiers detect a request related to cybersecurity, biology and chemistry, or distillation, the response is automatically handled by Claude Opus 4.8 instead. Users will be informed whenever this occurs. Opus 4.8 is a highly capable model in its own right: a response that falls back to Opus is a far better experience than an outright refusal from Fable. Our early data shows that more than 95% of Fable sessions involve no fallback at all—for those sessions, Fable 5’s performance is effectively the same as that of Mythos 5.

The following are the areas covered by the classifiers:

*1. Cybersecurity*. Mythos-class models excel at discovering and exploiting software vulnerabilities. They can thus make cyberattacks substantially easier and cheaper to commit. Mythos-class models also show strong skills in agentic hacking. This involves performing multiple different parts of a cyberattack in addition to finding exploits—reconnaissance, discovery, lateral movement, and more. To prevent these agentic hacking skills providing uplift in cyberattacks, we designed our cybersecurity classifiers to cover both exploitation and offensive cyber tasks in a broader sense. As shown in the graph below, our classifiers prevent Fable from making any progress on these tasks.

We extensively red-teamed our classifiers to test their robustness against jailbreaks. As well as internal testing, we ran an external bug bounty that produced no universal jailbreaks in over 1,000 hours of testing. External red-teaming organizations we engaged also failed to find any universal jailbreaks on long-form agentic tasks so far—although the UK AISI has made progress towards one within a brief initial testing window.4 It is likely impossible to *completely* prevent universal jailbreaks, but our goal is to make any remaining jailbreaks sufficiently slow and costly that we can detect and prevent them before they are used at scale.

The graph below, from one of our internal evaluations, illustrates how Fable 5’s safeguards give it greater resistance to jailbreaks than our previous generally accessible models:

One of our external partners found that Fable 5’s safeguards against harmful cyber queries were the most robust of any model tested (including Opus 4.8 and Opus 4.7). Fable 5 complied with zero harmful single-turn requests relating to planning a cyberattack, exploit development, or defense evasion. This held whether or not one of the requests used any of 30 different public jailbreak techniques.

*2. Biology and chemistry.* We have long used our classifiers to block our models from responding on a narrow selection of bioweapons-related queries. But we are no longer certain that blocking this narrow selection is enough. This is for two reasons: first, we have reason for concern about well-resourced malicious actors attempting to gain uplift from our models for highly risky biological research. Second, models now have a greater ability to accomplish real-world scientific tasks.

For example, we tested Mythos 5’s ability to complete a challenging step in designing adeno-associated viruses (AAVs). AAVs are a component for delivering gene therapies, but the same capability, in the wrong hands, could enable the design of dangerous viruses. In this task, various AI models were evaluated on their ability to predict how a genetic modification would impact the assembly of the virus’s outer shell (among a set of therapeutically-relevant unpublished candidates developed by Dyno Therapeutics). We did not explicitly train our models to perform this task—and yet Mythos-class models outperformed sophisticated models dedicated to protein tasks (known as “protein language models”) using their biological reasoning alone. This demonstrates a promising ability to complete simple but important tasks in gene therapy research and development—but also highlights the risk posed by such dual-use capabilities.

Our priority was to safely release Fable as soon as we could, even at the cost of overly broad safeguards. Therefore, for the time being we have arranged for Fable to fall back to Opus 4.8 on most requests related to biology and chemistry. As with all of our classifiers, we hope to narrow these safeguards as soon as possible: as can be seen from the evidence above, there is great potential for positive applications of Fable for science, and we do not want false positives from our classifiers to get in the way. In the coming weeks, some biomedical researchers and companies will be able to join our trusted access program for biology capabilities in Mythos 5 (discussed below).

*3. Distillation*. We’ve previously identified large-scale attempts to extract (“distill”) Claude’s capabilities to train competing models in authoritarian countries. Distillation of Fable 5’s abilities could indirectly lead to the proliferation of near-frontier AI capabilities—and these could be released without the appropriate safeguards. Requests that are flagged by our classifiers as being part of such distillation attempts will fall back to Opus 4.8.

### A new data retention policy

Finally, we’re making a change to the way we handle business customer data for Fable 5, Mythos 5, and future models with similar or higher capability levels. We will require 30-day retention for all traffic on Mythos-class models, on both first- and third-party surfaces. We won’t use this data to train new Claude models, or for any non-safety-related purpose, and we’ve instituted new privacy protections including logging all human access to the data and ensuring its deletion after 30 days in almost all cases (see this post for further details). The data will help us defend against complex and novel attacks (including new jailbreaks and attacks that operate across many requests) as well as help us identify and reduce false positives.

## Claude Mythos 5 and the trusted access program

Beginning today, all users who currently have access to Claude Mythos Preview (for example, our cybersecurity partners in Project Glasswing) will be able to upgrade to Claude Mythos 5—the same model as Claude Fable 5 but with cyber safeguards lifted. Users will find Mythos 5 comparable to, or somewhat stronger than, Mythos Preview in most cases, while costing substantially less.

In consultation with the US government, we plan to steadily expand access to Claude Mythos 5, continuing our periodic addition of new partners, as well as pursuing a trusted access program that allows cybersecurity organizations to apply in a more systematic manner.

Our plans also include opening a trusted access program for biology, to help accelerate biomedical research and discover new therapies with Mythos-class capabilities. This program will provide access to Fable 5 with the biology and chemistry safeguards removed (but the cyber safeguards still in place). It will enroll a small number of researchers from a variety of life science organizations spanning fundamental and translational research; we’re planning to expand access to this program while simultaneously making our safeguards better.

## Availability

Claude Fable 5 is available everywhere today. Claude Mythos 5 is restricted to Glasswing partners (with cyber safeguards lifted) and soon to select biology researchers (with biology and chemistry safeguards lifted) only, until our broader trusted access program is available.

Pricing for both models is $10 per million input tokens and $50 per million output tokens. Developers can use claude-fable-5 via the Claude API.

We expect demand for Fable 5 to be very high, and difficult to predict. On the Claude API and consumption-based Enterprise plans, Fable 5 is fully available from today. For subscription plans, we’d rather give access sooner than later, so we’re rolling out more conservatively, in stages:

- From today through June 22, Fable 5 is included on Pro, Max, Team, and seat-based Enterprise plans at no extra cost.
- On June 23, we’ll remove Fable 5 from those plans. Using it after that will require usage credits. If capacity allows, we’ll extend the included window.
- After this point—when sufficient capacity allows us to do so—we aim to restore Fable 5 as a standard part of subscription plans. We intend to do this as quickly as we can.

Throughout this period, we’ll communicate any changes ahead of time so users know where things stand.

*Edit June 9, 2026: Updated the discussion of AAVs to note that the candidates were developed by Dyno Therapeutics.*

#### Footnotes

- Mythos-class models are a tier of Claude models that sit above our Opus class in capability. The first, Claude Mythos Preview, was released in April through Project Glasswing. That is followed today by Claude Fable 5 and Claude Mythos 5.
- Fable is from the Latin
*fabula*, “that which is told,” akin to the Greek*mythos*. The safeguards are what distinguish the two models (Fable and Mythos) and are why we’ve given them different names. - Metrics: Firefox = fraction of trials achieving arbitrary code execution (the exploit's full-success tier). OSS-Fuzz = severity-weighted mean of the five-tier score (0.2 crash → 1.0 control-flow hijack), so values are a weighted average rather than a success rate. CyberGym = fraction reproducing the target vulnerability (the public leaderboard metric). CyScenarioBench = success rate averaged equally across its challenges.
- A universal jailbreak can be defined as any prompt, script, or harness that allows a user to interact with a model as if its safeguards were not present. This is opposed to more minor jailbreaks that are only effective in very limited contexts or require additional effort to be adapted to each new situation.

## Related content

### What we learned mapping a year’s worth of AI-enabled cyber threats

As AI transforms the nature of and methods behind cyberattacks, how well do the techniques and frameworks used by the security community hold up? In a new report, we seek to answer that question.

Read more