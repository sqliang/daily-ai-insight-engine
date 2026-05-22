---
title: 'DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic
  Workflows'
source: https://arxiv.org/abs/2605.19099
author:
- '[[Yuxuan Gao, Megan Wang, Yi Ling Yu, Zijian Carl Ma, Ao Qu]]'
published: '2026-05-20'
created: '2026-05-21'
description: 'arXiv:2605.19099v1 Announce Type: new Abstract: We introduce DecisionBench,
  a benchmark substrate for emergent delegation in long-horizon agentic workflows.
  The substrate fixes a task suite (GAIA, tau-bench, BFCL multi-turn), a peer-model
  pool (11 models, 7 vendor families), a delegation interface (call_model plus an
  optional read_profile channel), a deterministic skill-annotation layer, and a multi-axis
  metric suite covering quality, cost, latency, delegation rate, routing fidelity-at-k,
  vendor self-preference, and a counterfactual-delegation ceiling. The substrate is
  agnostic to how peer information is generated or delivered, so learned routers,
  richer peer memories, adaptive profile construction, and multi-step delegation can
  all be evaluated against it. We characterize the substrate with a five-condition
  reference sweep on the full pool (n=23,375 task instances). Three benchmark-level
  findings emerge: (i) mean end-task quality is statistically indistinguishable across
  the four awareness conditions (|beta| = 0.21), so quality-only evaluation would
  miss the orchestration signal; (ii) routing fidelity-at-1 ranges from 7.5% to 29.5%
  across conditions at near-equal mean quality, with delivery channel (on-demand tool
  vs. preloaded description) dominating description content; (iii) a counterfactual
  ceiling places perfect delegation 15-31 percentage points above measured performance
  on every suite, locating large unrealized headroom for future orchestration methods.
  We release the substrate, annotation layer, reference intervention suite, analysis
  pipeline, and 220 per-condition run archives.'
tags:
- clippings
extraction_status: success
id: 6dd8aa396fd1fab6
---

# Computer Science > Artificial Intelligence

# Title:DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic Workflows

View PDF HTML (experimental)Abstract:We introduce DecisionBench, a benchmark substrate for emergent delegation in long-horizon agentic workflows. The substrate fixes a task suite (GAIA, tau-bench, BFCL multi-turn), a peer-model pool (11 models, 7 vendor families), a delegation interface (call_model plus an optional read_profile channel), a deterministic skill-annotation layer, and a multi-axis metric suite covering quality, cost, latency, delegation rate, routing fidelity-at-k, vendor self-preference, and a counterfactual-delegation ceiling. The substrate is agnostic to how peer information is generated or delivered, so learned routers, richer peer memories, adaptive profile construction, and multi-step delegation can all be evaluated against it. We characterize the substrate with a five-condition reference sweep on the full pool (n=23,375 task instances). Three benchmark-level findings emerge: (i) mean end-task quality is statistically indistinguishable across the four awareness conditions (|beta| <= 0.010, p >= 0.21), so quality-only evaluation would miss the orchestration signal; (ii) routing fidelity-at-1 ranges from 7.5% to 29.5% across conditions at near-equal mean quality, with delivery channel (on-demand tool vs. preloaded description) dominating description content; (iii) a counterfactual ceiling places perfect delegation 15-31 percentage points above measured performance on every suite, locating large unrealized headroom for future orchestration methods. We release the substrate, annotation layer, reference intervention suite, analysis pipeline, and 220 per-condition run archives.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.