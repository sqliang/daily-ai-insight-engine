---
title: 'To Add Is Machine, To Delete Is Human: Measuring and Mitigating Deletion Avoidance
  in LLM Code Editing'
source: https://arxiv.org/abs/2607.28887
author:
- '[[Amir M. Ebrahimi, Mohammed Mehedi Hasan, Aaditya Bhatia, Gopi Krishnan Rajbahadur,
  Ahmed E. Hassan]]'
published: '2026-08-04'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d18cc62aaec40bcc
source_type: academic_paper
tldr: 研究论文揭示大模型代码编辑中的"删除回避"现象：模型即使通过测试也倾向保留本应删除的代码。在 SWE-bench Verified 上五大模型删除召回率最高仅
  71.7%，新基准 CanItDelete 显示最佳模型仍有五分之一任务失败，后训练阶段教学可缓解此问题。
objective_summary: 该研究系统测量了大语言模型在代码编辑中的删除回避现象。在 SWE-bench Verified 官方排行榜上，五个领先模型对开发者补丁的删除召回率最高仅
  71.7%，超过 92% 的应删代码被定位到正确文件，但精确行删除率不足 52%。29% 的通过补丁采用 Guard-and-Go 模式绕过删除；将 34 个任务改装为删除检测测试后，四个前沿模型通过率从
  63.2% 降至 41.9%。团队构建了含 200 个纯删除任务的 CanItDelete 基准，并验证后训练阶段教授删除行为可降低删除回避并提升整体代码编辑性能。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  technologies:
  - SWE-bench Verified
  - CanItDelete
  - Guard-and-Go
  - post-training
  - LLM code editing
  key_people: []
key_logic_flow:
- 研究团队识别出大模型代码编辑中的"删除回避"现象，即模型系统性地保留本应删除的代码，导致代码库更难维护。
- 在 SWE-bench Verified 官方排行榜上，五个领先模型的删除召回率最高仅 71.7%，即使任务被全部解决时也是如此。
- 模型能到达应删除代码所在文件的比例超过 92%，但精确删除目标行的比例不足 52%，且有 29% 的通过补丁采用 Guard-and-Go 模式将目标代码包裹在守卫或回退逻辑中。
- 原始测试很少检查代码是否被移除；将 34 个 Verified 任务改装为删除检测测试后，四个前沿模型的通过率从 63.2% 下降到 41.9%。
- 团队构建了包含 200 个纯删除任务的 CanItDelete 基准，最佳模型仍有五分之一任务失败，小型开放模型的通过率仅 18.0%。
- 对 GPT-5.6 Sol 的消融实验显示，提供精确删除行后成功率达到 80.5%，但模型会过度删除或额外添加代码；后训练阶段教授删除行为可降低删除回避并提升整体代码编辑性能。
object_mentions:
- object_type: dataset
  name: CanItDelete
  canonical_name: CanItDelete
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 研究团队从真实提交中挖掘出 200 个任务构建 CanItDelete 基准，这些任务要求的全部编辑内容就是删除。
  - 即使删除工作单独存在，最佳模型在 CanItDelete 上仍有五分之一任务失败，小型开放模型的通过率仅 18.0%。
  article_id: d18cc62aaec40bcc
- object_type: dataset
  name: SWE-bench Verified
  canonical_name: SWE-bench Verified
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 五个领先模型在官方 SWE-bench Verified 排行榜上的删除召回率最高仅 71.7%，即便五个模型都解决的任务也是如此。
  - 模型能到达应删除代码所在文件的比例超过 92%，但精确删除目标行的比例不足 52%。
  article_id: d18cc62aaec40bcc
- object_type: model
  name: GPT-5.6 Sol
  canonical_name: GPT-5.6 Sol
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 研究团队在 GPT-5.6 Sol 上进行了四组累积提示消融实验，补充精确删除行后几乎消除了不完整删除。
  - 即便提供精确行，GPT-5.6 Sol 的成功率也只提升到 80.5%，因为模型会删除超出范围的内容或额外添加代码。
  article_id: d18cc62aaec40bcc
extract_result: success
---

# Computer Science > Software Engineering

# Title:To Add Is Machine, To Delete Is Human: Measuring and Mitigating Deletion Avoidance in LLM Code Editing

View PDF HTML (experimental)Abstract:Large language models increasingly write and repair production code, yet evidence is mounting that their test-passing patches leave codebases harder to maintain. We identify one concrete source: deletion avoidance, the systematic tendency to retain code that an intended edit requires removing. Across the five leading models on the official SWE-bench Verified leaderboard, deletion recall against the developer patch reaches at most 71.7% even on tasks all five solve, and models reach the right file for over 92% of required deletions but cut the exact line in under 52% of cases. Instead, 29.0% of passing patches wrap the targeted code in a guard or fallback, a pattern we call Guard-and-Go. Such patches pass because the original tests rarely check removal: when we retrofit 34 Verified tasks with tests that fail if the targeted code remains, four frontier models spanning closed and open weights fall from 63.2% to 41.9%. Because real repairs mix removal with addition, we curate CanItDelete, a benchmark of 200 tasks mined from real commits whose entire required edit is deletion. Even with the addition work gone, the best model still fails one task in five, and smaller open models fall to 18.0%. We then ablate GPT-5.6 Sol under four cumulative prompts; success moves little until we supply the exact lines, which nearly eliminate incomplete deletion yet raise success only to 80.5% because the model then deletes beyond the spans or adds code instead. Finally, through a pilot study we show one potential fix: teaching deletion during post-training reduces deletion avoidance and improves broader code-editing performance, suggesting the behavior is undertrained rather than beyond reach.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.