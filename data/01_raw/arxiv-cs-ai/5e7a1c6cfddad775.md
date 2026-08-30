---
title: 'Representation Affects Retrieval: A Case Study of Skill Discovery and Routing
  in a Multimodal Agent Harness'
source: https://arxiv.org/abs/2608.20389
author:
- '[[Kevin Dela Rosa]]'
published: '2026-08-24'
created: '2026-08-24'
manifest_dates:
- '2026-08-24'
description: 'arXiv:2608.20389v1 Announce Type: new Abstract: A production agent harness
  must discover and rank, from a growing library of skills, the one most appropriate
  for a user''s task. At small scale this selection happens in context: the LLM planner
  chooses among skill representations exposed in its system prompt, without an explicit
  embedding-based retrieval step. We treat this in-context selection as the small-N
  counterpart to embedding-based skill retrieval at scale, and present a case study
  of how Tinycloud, a production multimodal video agent harness, represents its skills
  for the planner. The harness ships skills under two recurring representations: tool-skills
  that wrap a single external API or system tool and serve as primitive vocabulary,
  and workflow-skills that orchestrate tool-skill calls plus a template render to
  produce one named deliverable. The harness exposes them via two surfaces in the
  system prompt: an inlined-body surface (full instructions, scripts, templates) for
  autoloaded skills, and a one-line listing for on-demand skills. A six-task selection
  ablation across three exposure regimes (all-on, default, all-off) shows that full
  autoload selects the gold skill on every task; all-off slows execution and produces
  hard discovery failures; and the production default misroutes one task because its
  lexical signal collides with an autoloaded tool-skill that pulls planner attention
  away from a listed workflow-skill. The headline finding is that in-prompt exposure
  of skills is not monotonically helpful: partial exposure can create lexical competition
  that suppresses correct selection. We connect this small-N observation to recent
  retrieval-based skill-routing work at large scale, and frame this contribution as
  a case study rather than a benchmark.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 5e7a1c6cfddad775
---

# Computer Science > Artificial Intelligence

# Title:Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness

View PDF HTML (experimental)Abstract:A production agent harness must discover and rank, from a growing library of skills, the one most appropriate for a user's task. At small scale this selection happens in context: the LLM planner chooses among skill representations exposed in its system prompt, without an explicit embedding-based retrieval step. We treat this in-context selection as the small-N counterpart to embedding-based skill retrieval at scale, and present a case study of how Tinycloud, a production multimodal video agent harness, represents its skills for the planner. The harness ships skills under two recurring representations: tool-skills that wrap a single external API or system tool and serve as primitive vocabulary, and workflow-skills that orchestrate tool-skill calls plus a template render to produce one named deliverable. The harness exposes them via two surfaces in the system prompt: an inlined-body surface (full instructions, scripts, templates) for autoloaded skills, and a one-line listing for on-demand skills. A six-task selection ablation across three exposure regimes (all-on, default, all-off) shows that full autoload selects the gold skill on every task; all-off slows execution and produces hard discovery failures; and the production default misroutes one task because its lexical signal collides with an autoloaded tool-skill that pulls planner attention away from a listed workflow-skill. The headline finding is that in-prompt exposure of skills is not monotonically helpful: partial exposure can create lexical competition that suppresses correct selection. We connect this small-N observation to recent retrieval-based skill-routing work at large scale, and frame this contribution as a case study rather than a benchmark.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.