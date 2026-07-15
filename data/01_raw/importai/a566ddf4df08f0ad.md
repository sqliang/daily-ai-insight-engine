---
title: 'Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac
  essay for the human era'
source: https://importai.substack.com/p/import-ai-463-self-improving-robots
author:
- '[[Jack Clark]]'
published: '2026-06-29'
created: '2026-06-30'
description: What eras bookend our interregnum?
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: a566ddf4df08f0ad
manifest_dates:
- '2026-06-30'
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
- '2026-07-04'
- '2026-07-05'
- '2026-07-06'
---

# Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era

### What eras bookend our interregnum?

Welcome to Import AI, a newsletter about AI research. Import AI runs on arXiv, cappuccinos, and feedback from readers. If you’d like to support this, please subscribe.

**NVIDIA sets up a crude self-improvement loop for real world robotics:**

*…What if you could take the best ideas from AI agents and put them into the real world?...*

Researchers with NVIDIA have developed ENPIRE, software to get physical robotics to go through the same kind of autonomous experimentation and execution loop that AI agents go through. The research gives us a taste of what it might look like for a superintelligence to attempt to use robots to instantiate itself in the physical world - though as with all things in robotics, the current examples are suggestive at best.

**What ENPIRE is:**The software is “a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with single or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes”.

**ENPIRE works the same way that coding agents work - a scaffold supervises some physical robots**which are asked to complete tasks. The robots try to complete the tasks and attempt different strategies for completing stuff, trying and failing and learning. The system both evaluates their success and also resets itself when they fail. “This closed-loop system transforms real-world robot learning into a controllable optimization procedure that agents can manage, thus minimizing human effort while allowing fair ablations across training recipes and agent variants.”

Two of the key ingredients for making this work are an automatic evaluation system to help score “the outcome of each trial without human judgement”, as well as an automatic reset system which “returns the scene to a fresh initial state for the next trial”. (Both of these are tasks which have historically required lots of human effort, and it’s likely that more complicated tasks would also require human effort for evaluation and resets, so in some sense the complexity of tasks a system like this can attack is also defined by our ability to automatically evaluate and reset the system).

**Hardware details:**“Each station comprises two YAM (Yet Another Manipulator) arms from I2RT in a fixed bimanual configuration, a set of cameras, and a single workstation that runs the FastAPI server, policy inference, and the station’s agent.” Each workstation is running a NVIDIA RTX 5090.