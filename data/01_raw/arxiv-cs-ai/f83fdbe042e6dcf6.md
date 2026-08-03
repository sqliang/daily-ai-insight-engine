---
title: 'Library Reachability in LSR-Synth: How Anti-Memorization Design Changes the
  Measurement of Symbolic Discovery'
source: https://arxiv.org/abs/2607.28684
author:
- '[[Zhan''ao Yao, Liang Yin, Zhihao Gao, Boxuan Zhang, Xiaoyu Wu, Linjing Li, Rongyan
  Wang, Tingwei Chen, Youwei Wang, Xiaolin Zhao, Jiahui Shi, Jianjun Liu]]'
published: '2026-08-03'
created: '2026-08-03'
manifest_dates:
- '2026-08-03'
description: 'arXiv:2607.28684v1 Announce Type: new Abstract: Existing benchmarks
  for scientific equation discovery are largely composed of well-known equations available
  in the public domain, making it difficult to determine whether a model is discovering
  laws from data or merely recalling answers from its training corpus. LSR-Synth mitigates
  this problem by introducing novel synthetic terms into established scientific mechanisms
  and filtering the resulting tasks for novelty, solvability, and scientific plausibility.
  This paper examines a narrower measurement question: can these tasks further distinguish
  scientific priors supplied by language models from conventional operator search
  that does not access task semantics? We construct a semantics-free baseline using
  a fixed vocabulary with publicly documented provenance, and assess the role of candidate
  coverage through semantic blinding, library weakening, and matched operator-family
  knockouts. Under the current task snapshot, search budget, and scoring protocol,
  the fixed vocabulary already covers most tasks, while language-model-generated candidates
  rarely expand the set of solvable instances. Their marginal contribution becomes
  substantial only when vocabulary coverage is selectively disrupted. Strict out-of-distribution
  evaluation lowers the absolute success rates of all methods but does not alter this
  relationship. These findings neither invalidate LSR-Synth''s controls against memorization
  of complete formulas nor imply that language-model priors are generally unhelpful.
  Rather, they support a more limited conclusion: most current tasks remain suitable
  for evaluating the fitting and recombination of previously unseen expressions, but
  are insufficient on their own to identify contributions from priors beyond a fixed
  search space.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: f83fdbe042e6dcf6
---

# Computer Science > Artificial Intelligence

# Title:Library Reachability in LSR-Synth: How Anti-Memorization Design Changes the Measurement of Symbolic Discovery

View PDF HTML (experimental)Abstract:Existing benchmarks for scientific equation discovery are largely composed of well-known equations available in the public domain, making it difficult to determine whether a model is discovering laws from data or merely recalling answers from its training corpus. LSR-Synth mitigates this problem by introducing novel synthetic terms into established scientific mechanisms and filtering the resulting tasks for novelty, solvability, and scientific plausibility. This paper examines a narrower measurement question: can these tasks further distinguish scientific priors supplied by language models from conventional operator search that does not access task semantics? We construct a semantics-free baseline using a fixed vocabulary with publicly documented provenance, and assess the role of candidate coverage through semantic blinding, library weakening, and matched operator-family knockouts. Under the current task snapshot, search budget, and scoring protocol, the fixed vocabulary already covers most tasks, while language-model-generated candidates rarely expand the set of solvable instances. Their marginal contribution becomes substantial only when vocabulary coverage is selectively disrupted. Strict out-of-distribution evaluation lowers the absolute success rates of all methods but does not alter this relationship. These findings neither invalidate LSR-Synth's controls against memorization of complete formulas nor imply that language-model priors are generally unhelpful. Rather, they support a more limited conclusion: most current tasks remain suitable for evaluating the fitting and recombination of previously unseen expressions, but are insufficient on their own to identify contributions from priors beyond a fixed search space.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.