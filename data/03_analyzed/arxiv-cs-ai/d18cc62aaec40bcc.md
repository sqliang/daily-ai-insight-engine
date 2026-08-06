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
impact_score:
  score: 6.0
  reason: 论文首次系统量化了主流代码大模型的'删除回避'缺陷：SWE-bench Verified 头部模型的删除召回率最高仅 71.7%，29% 的通过补丁用
    Guard-and-Go 模式绕过删除，且发现现有测试几乎不校验代码是否被删除。这是对行业'测试通过=编辑成功'评估范式的一记警钟，会直接影响代码智能体厂商（Cursor、Copilot、Claude
    Code 等）的评测指标与后训练数据策略。但论文本质是缺陷测量+缓解路径，尚未提出新架构或新训练范式，不构成范式转移，故定 6 分。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: SWE-bench 等基准通过率存在水分——测试通过不代表代码库更可维护，删除行为根本未被评测覆盖
hype_assessment:
  level: low
  reason: 论文基于真实 git 提交挖掘 200 个纯删除任务构建 CanItDelete 基准，对五个前沿模型做系统性消融实验，并给出后训练 pilot
    验证，数据详实、方法可复现。通篇未使用'颠覆''革命性'等 PR 词汇，是实打实的实证研究。
information_entropy: high
domain_disruption:
  technical_innovation: 首次系统识别并量化'删除回避'现象，提出 Guard-and-Go 模式（将目标代码包裹进守卫/回退逻辑）的识别方法；通过'删除检测式测试改写'证明现有评测盲区；并基于真实提交构建纯删除任务基准
    CanItDelete，验证后训练阶段教授删除行为可同时降低删除回避并提升整体代码编辑性能——揭示该缺陷是训练不足而非能力天花板。
  business_model: 对代码智能体与 AI 编程助手产品有直接重塑力：现有 SWE-bench 类基准被证明系统性高估了代码可维护性，厂商需在评测指标、RLHF/后训练数据管线中新增'删除/清理'维度，这将成为代码质量差异化竞争的新抓手，也可能催生'代码整洁度'类的新评估服务与产品卖点。
engineering_complexity: prototype
compound_value:
  score: 6.0
  reason: 该研究揭示了'测试通过≠代码可维护'这一系统性缺陷，并构建了 CanItDelete 基准（200 个纯删除任务），有潜力成为继 SWE-bench
    之后的代码编辑评估基础设施。投资逻辑推演：(1) 核心发现——删除回避源于'欠训练'而非不可达，且后训练可缓解——意味着对高质量删除/重构训练数据与后训练管道的需求将长期增长，利好拥有数据飞轮的模型厂商；(2)
    评估范式将从'通过率单一指标'转向'代码质量多维指标'，这一转变具有持续累积效应，会重塑编码 Agent 的采购标准；(3) 但单篇论文本身不构成产品壁垒，CanItDelete
    能否被行业主流采纳为基准仍需 1-2 年验证，故给 6 分：具备成为细分赛道评估基础设施的潜力，尚需持续观察其扩散速度。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Anthropic
- Google DeepMind
- Cursor (Anysphere)
- SWE-bench
competitive_casualty:
- 小型开源模型厂商
- 以测试通过率为唯一指标的编码 Agent
- 传统静态代码审查工具
market_opportunities:
- AI 编程工具厂商可将'删除回避'检测能力集成进代码审查与 CI/CD 流水线，开发自动识别 Guard-and-Go 模式及未删除冗余代码的审计产品，作为区别于竞品的功能卖点
- 借鉴 CanItDelete 基准思路，可构建'代码可维护性评测'第三方服务，以删除精确率等指标补充传统测试通过率，为企业采购 AI 编码助手提供更全面的量化依据
- 研究证实后训练阶段教授删除行为可降低删除回避并提升整体编辑性能，为模型微调服务商和 Agent 定制团队提供了新的数据构造与指令优化方向
risk_matrix:
  regulatory: 无直接监管风险；但删除回避导致的隐藏逻辑残留若进入医疗、金融等高合规要求行业代码库，可能间接触发软件审计与产品责任问题
  technological: 当前以'测试通过率'为核心的评估体系会系统性高估模型编辑能力，主流模型在精确删除上存在明确缺陷；若后训练缓解方案无法规模化复现，模型在代码删除场景的能力可能长期停滞，并成为新一代模型的共性短板
  competitive: AI 编码助手赛道竞争加剧：率先解决删除回避并提供'可维护性评分'的厂商可获得差异化优势；反之依赖传统指标营销的厂商可能因代码质量口碑受损而流失企业客户；小型开放模型在该基准上仅
    18% 通过率，形成显著的市场能力分层
  ethical: 模型保留的死代码与守卫回退逻辑可能隐藏安全漏洞和意外行为，增加下游软件故障风险；低质量编辑加重开发者维护负担，侵蚀人机协作信任，可能强化一线工程师对
    AI 编码工具的抵触情绪
  additional:
  - 基准过拟合风险——CanItDelete 作为新基准可能重蹈 SWE-bench 被针对性优化的'聪明汉斯'效应，后续评测需要持续对抗式更新
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
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