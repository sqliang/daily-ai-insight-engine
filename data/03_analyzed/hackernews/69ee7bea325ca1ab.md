---
title: HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74. No –
  88
source: https://danunparsed.com/p/hackerrank-open-source-ats
author:
- '[[sambellll]]'
published: '2026-06-29'
created: '2026-06-29'
manifest_dates:
- '2026-06-29'
description: 'Article URL: https://danunparsed.com/p/hackerrank-open-source-ats Comments
  URL: https://news.ycombinator.com/item?id=48713832 Points: 400 # Comments: 139'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 69ee7bea325ca1ab
source_type: community_discussion
tldr: HackerRank开源ATS评分系统测试：同一简历得分66-99，LLM评分极不稳定
objective_summary: 作者测试HackerRank开源的简历评分工具hiring-agent，发现同一份简历在100次运行中得分从66到99不等。技术检查项评分一致，项目经验等主观项波动极大。降低温度或换用Gemini、Claude
  Opus等模型仍无法根本解决评分不稳定性问题。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - HackerRank
  - interviewstreet
  technologies:
  - ATS
  - LLM
  - gemma3:4b
  - Gemini
  - Claude Opus 4.8
  key_people: []
key_logic_flow:
- HackerRank开源了其简历评分工具hiring-agent，该工具使用LLM对简历进行六维度评分并给出总分。
- 作者将同一份简历重复运行100次，发现得分在66到99之间大幅波动，导致基于固定阈值的筛选完全依赖运气。
- 技术技能等客观检查项评分一致性很高（98/100次拿到8/10），但项目经验等需要主观判断的类别评分波动极大。
- 即使将温度参数降至0或换用Gemini、Claude Opus等更先进模型，评分不稳定的问题仍然存在，说明这是LLM评分系统的根本性设计缺陷。
- 工作经验评分维度仅有两行简短标准，缺乏具体锚定值，导致初级实习生和资深工程师都获得满分25/25，完全失去区分度。
- 工具将65%的权重分配给开源贡献和项目经验，严重低估了资深工程师的实际工作经验价值。
extract_result: success
impact_score:
  score: 7.2
  reason: 该文章通过严谨的对照实验（100次运行、多模型对比、温度参数调试）揭示了LLM简历评分的本质缺陷：主观维度评分高度随机，同一简历得分跨度达66-99。文章在Hacker
    News、LinkedIn、Reddit上广泛传播（数百至数千点赞），直接动摇了业界对AI筛选工具的信任基础。它对正在快速采用LLM进行招聘筛选的HR科技行业形成了实质性冲击——不仅影响HackerRank这一开源工具的可信度，更对整个AI辅助招聘赛道提出了根本性质疑。虽然不是范式转移级（8-10分），但足以改变局部竞争格局，属于重要产品缺陷曝光级事件。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: LLM在主观评分维度上的非确定性本质缺陷无法通过调参或换模型解决
hype_assessment:
  level: low
  reason: 文章本身不包含任何PR宣传或概念炒作。恰恰相反，它是对一个开源工具的真实压力测试，提供了详实的实验数据：100次循环运行、温度从0.1降到0、模型从gemma3:4b换到Gemini再到Claude
    Opus 4.8的完整对比。每个评分维度的波动范围都有量化数据支撑（技术技能98/100次稳定8/10，项目经验6-25大幅波动），并精确指出了prompt模板中工作经验评分标准仅两行、缺乏锚定值的具体缺陷。判定为'low'——这是实打实的干货揭露，没有任何包装成分。
information_entropy: high
domain_disruption:
  technical_innovation: 揭示了LLM作为评分系统时的根本性架构缺陷：客观检查项（技术技能）可以做到高一致性，但需要主观判断的维度（项目复杂度、工作经验的深度评估）即使降低温度、换用前沿模型也无法解决评分随机性问题。这一发现对任何依赖LLM进行定性评估的系统（不限于招聘）都有警示意义。
  business_model: 直接冲击AI招聘SaaS行业的价值主张。如果AI简历评分本质上等同于'运气过滤器'，那么基于此的收费筛选服务将面临信任危机。可能推动行业从'纯AI自动筛选'转向'AI辅助结构化解析+人工决策'的混合模式，或促使创业公司重新设计评分体系（如仅用LLM做客观信息提取，放弃主观打分）。
engineering_complexity: production_ready
compound_value:
  score: 3.0
  reason: 该事件的核心价值在于通过大规模实证（100次运行）揭示了LLM在简历主观评分场景中的根本性缺陷：同一份简历得分从66到99大幅波动，技术检查项一致性高（98/100次8/10），但项目经验等需判断力的维度评分极不稳定。即使使用Gemini、Claude
    Opus 4.8等前沿模型或将温度降至0，评分波动问题仍无法根本解决。工具权重设计也存在严重偏差（65%分配给开源贡献和项目经验，资深工程师的工作经验仅占25%且无区分度）。这一发现为行业提供了重要的'AI能力边界'认知证据，可能影响监管和企业采购决策，但作为独立技术资产不具备任何复利积累效应——工具本身被证实是不可靠的幸运过滤器，难以成为行业基础设施。长期来看，该案例可能被引用为'AI主观评估局限性'的经典教材，但对价值创造的贡献有限。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries:
- HackerRank
- Codility
- CodeSignal
competitive_casualty:
- AI简历筛选初创公司
- LLM驱动的主观评估工具
market_opportunities:
- 创业者可开发基于确定性规则+LLM混合架构的简历筛选工具，将LLM限定在擅长的结构化提取和技能匹配环节，主观评分部分使用预设评分矩阵而非自由生成
- 企业可建立AI招聘审计流程，对LLM评分工具进行多轮稳定性测试并设定统计置信区间，而非依赖单次分数做筛选决策
- 咨询公司可推出'AI招聘工具风险评估'服务，帮助HR团队识别和规避LLM评分的不确定性风险，制定人机协同的筛选标准
risk_matrix:
  regulatory: 欧盟AI Act将就业相关的AI系统列为高风险类别，使用这种评分波动极大的工具进行简历筛选可能违反合规要求，企业面临法律责任和监管处罚风险
  technological: LLM在主观判断任务上的非确定性是根本性设计缺陷而非bug，降低温度参数或换用更先进的模型均无法根本解决，技术替代方案（确定性算法+LLM混合架构）正在形成竞争
  competitive: HackerRank将该工具开源降低了市场准入门槛，大量公司可能盲目采用此类工具导致招聘质量下降，同时合规要求高的企业可能转向更保守的解决方案
  ethical: 65%权重分配给开源贡献和项目经验，系统性贬低了无GitHub足迹的优秀工程师；资深与初级工程师在'工作经验'维度无法区分，评分完全沦为运气筛选，加剧就业不平等
  additional:
  - 招聘团队面临成本压力可能过度依赖此类工具，形成'虚假效率'——看起来自动化了筛选，实际将人才选拔变成了随机抽奖
  - 如果行业广泛采用此类不稳定评分系统，可能导致候选人简历优化军备竞赛，而非真正能力匹配
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
---

# HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74/100. No — 88/100. Actually 83/100.

### How hiring is becoming a luck filter.

This open-source ATS by HackerRank has been blowing up recently: https://github.com/interviewstreet/hiring-agent

It’s popped up on LinkedIn and Reddit with hundreds, sometimes thousands, of likes.1 A coworker mentioned it to me in passing a few days ago.

I’ve decided to test it out.

First working run: 90/100. Felt pretty good!

I had some debug prints scattered around from troubleshooting the setup, so I cleaned those up and ran it again.

74/100.

Same resume. Same command. The only thing I changed was deleting print statements.

I disabled `DEVELOPMENT_MODE`

and put it in a loop to run a hundred times.

The scores range from 66 to 99.

If your company’s cutoff sits at 85, I fail 65% of the time. Same exact resume, different luck.

Here a quick rundown on how the tool works:

Your PDF gets parsed into text. An LLM is called six times to extract structured information — your basics, work history, education, skills, projects, awards. It pulls your GitHub profile, scans your top repos, appends them as extra context. Then everything gets fed into the LLM at once to be graded.

The scoring is out of 100, with up to 20 bonus points on top:

35 points for open source contributions

30 for personal projects

25 for work experience

10 for technical skills

Up to 20 bonus points for startup experience, a portfolio site, a technical blog, etc.


The default model is gemma3:4b, running at temperature 0.1 — low, supposedly nudging the model toward deterministic outputs.

Here’s what I found when I looked at those individual categories.

Look at technical skills: I scored 8/10 in 98 out of 100 runs. Nearly perfect consistency. How come? Because technical skills are a checklist. You either know React or you don’t. There’s nothing for an LLM to judge — a five year old could match that check-list.

Now look at projects — there’s HUGE variation.

LLMs struggle to make a judgment call like that consistently. Sometimes my projects “lack architectural complexity”, sometimes they “demonstrate real-world deployment”. Which one the LLM spits out is a roll of the dice.

Temperature 0.1 is already low, but even going down to temperature 0 doesn’t fix this. Someone opened a GitHub issue back in October showing scores of 27, 34, 32, 34, 34, 30 across six consecutive runs at temperature 0.2 This non-determinism isn’t a bug you can just fine-tune away, it’s a fundamental design flaw.

I was worried part of this might be the model. After all, gemma3:4b was a local model running on my machine.

Gemini resulted in a tighter distribution — scores clustered between 48 and 64. But if your cutoff is 60, you’re still failing 28% of the time through no fault of your own.

The Open Source scores have become consistent — that’s a legit improvement. But project scores are still all over the place.

Experience has me the most concerned.

25/25.

Every single run.

I went back and pulled up an old resume — one internship on it.

Also 25/25.

The clue is in the prompt…

```
### Production (0-25 points)
- Analyze the 'work' and 'volunteer' sections for real-world, internship, or production experience
- **SPECIAL CONSIDERATION**: Give extra points for founder roles, co-founder positions, or early-stage engineer roles (first 10-20 employees) at startups
```


The entire thing is two lines long.

No rubric. No examples. No anchors for what earns a 15 versus a 25.

A junior engineer with one internship gets 25/25. A principal engineer with a decade of distributed systems gets 25/25. I get 25/25. Experience has two lines and no anchors — consistent, but useless. Projects has a detailed rubric with examples but it’s the noisiest category — inconsistent, also useless. There are some things that LLMs just can’t do well, no matter how you prompt.

Use an LLM to parse a resume into structured data — great, that’s what they’re good at. Use one to check whether someone knows Python — amazing. Use one to judge whether a candidate’s experience is worth 18 points or 24 points? You get a vibe-check. Something HR teams, bar raisers, and a dozen other initiatives have spent decades trying to avoid.

The 65% weighting on open source + projects doesn’t help either. I’d take the engineer with 30 years of experience who built S3 over someone with two internships and an open source project — but this tool wouldn’t. Some of the best engineers I know have built things that never ended up on GitHub. That’s over half of their score gone before any human looks their way.

If you’re an engineer with any say in how your company handles resume screening: please be very careful with AI-screening tools. A tool that can’t differentiate isn’t filtering for quality — it’s just filtering. You might as well throw out half the resumes and tell the the applicants you don’t fuck with bad luck.

*Correction (June 28): A reader flagged that the resume_evaluation_criteria.jinja template says “Software Intern” on line 1 — nowhere documented, nowhere else referenced in the repo. The same template that later gives bonus points for “founder roles, co-founder positions, or early-stage engineer roles.” I re-ran with an explicit Senior SWE prompt and got identical results — the scoring dimensions are position-agnostic.*

*Update (June 30): This blew up on Hacker News, if you’re curious to see that thread — here it is.*

*A few people noted that frontier models do not have this problem. I checked out one of the GitHub PRs that introduced support for Claude and ran Opus 4.8 in a loop until my credits ran out.*

*The range has tightened slightly — the score has gone down from 48-64 to 49-63, and projects from 12-25 down to 13-23. At its core, the point is the same: projects inconsistent, skills perfect.*