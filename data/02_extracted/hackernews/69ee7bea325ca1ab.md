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
tldr: HackerRank 开源了 ATS 工具 hiring-agent，作者测试发现同一份简历的 LLM 评分在 66 到 99 之间随机波动，项目评分存在巨大随机性，而工作经验类目无论资历均给满分，暴露出
  LLM 筛选简历的根本性不可靠。
objective_summary: HackerRank 将其 ATS 工具开源为 hiring-agent 项目（GitHub 仓库 interviewstreet/hiring-agent），使用
  LLM 对简历进行自动化评分。作者 Dan 对同一份简历进行了上百次重复测试，发现评分结果在 66 到 99 之间大幅波动，项目评分类目存在极高随机性，技术技能检查则几乎恒定。工作经验类目因提示词缺乏评分锚点，导致初级和资深工程师均获得满分
  25 分。即使切换为 Gemini 或 Claude Opus 4.8 等模型，评分的不确定性依然存在。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - HackerRank
  technologies:
  - LLM
  - Gemma 3
  - Gemini
  - Claude Opus 4.8
  key_people: []
key_logic_flow:
- HackerRank 将其内部使用的 ATS 工具开源为 hiring-agent 项目，代码托管于 GitHub 仓库 interviewstreet/hiring-agent。
- 该工具利用 LLM 对简历进行自动化评分，评分维度包括开源贡献（35 分）、个人项目（30 分）、工作经验（25 分）和技术技能（10 分），另有最高 20 分的额外奖励分。
- 作者使用同一份简历运行上百次测试后发现，评分结果在 66 到 99 之间大幅波动，项目评分类目存在极高随机性，但技术技能检查几乎恒定。
- 工作经验类目的 LLM 提示词仅有两行内容，缺乏详细评分锚点和示例，导致无论初级工程师还是资深架构师均获得满分 25 分，评分结果完全无法区分候选人的资质层级。
- 即使切换为 Gemini 或 Claude Opus 4.8 等更强大的模型，项目评分的不确定性依然存在，说明 LLM 输出非确定性是设计层面的根本性问题，而非模型性能的差异。
extract_result: success
object_mentions:
- object_type: project
  name: interviewstreet/hiring-agent
  canonical_name: interviewstreet/hiring-agent
  url: https://github.com/interviewstreet/hiring-agent
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - HackerRank 将其 ATS 工具开源为 hiring-agent 项目，代码托管于 GitHub 仓库 interviewstreet/hiring-agent，在
    LinkedIn 和 Reddit 上获得了数百次点赞和广泛讨论。
  - 该工具将简历 PDF 解析为文本，调用 LLM 六次提取结构化信息，再从 GitHub 档案获取候选人仓库信息作为补充上下文，最后统一评分。
  - 作者用同一份简历对 hiring-agent 运行了上百次测试，评分结果在 66 到 99 之间大幅波动，项目评分存在极大随机性，而技术技能检查几乎恒定。
  article_id: 69ee7bea325ca1ab
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