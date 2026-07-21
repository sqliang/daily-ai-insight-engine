---
title: Golden Gate Claude
source: https://www.anthropic.com/news/golden-gate-claude
author: []
published: '2026-07-09'
created: '2026-07-14'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4ff5ab7d45bc6dc5
manifest_dates:
- '2026-07-14'
- '2026-07-15'
source_type: tech_blog
tldr: Anthropic 发布了一篇大语言模型可解释性研究论文，在 Claude 3 Sonnet 的神经网络中识别出数百万个概念级「特征」，并可通过调节特征强度改变模型行为。他们放大「金门大桥」特征后创建了「Golden
  Gate Claude」演示版本，该模型会不自觉地围绕金门大桥回答任何提问。该演示仅上线 24 小时，目前已下线。
objective_summary: Anthropic 于 2024 年发布了一篇关于大语言模型可解释性的研究论文，首次系统性地绘制了 Claude 3 Sonnet
  神经网络内部的数百万个概念级「特征」，这些特征会在模型读到相关文本或看到相关图像时激活。研究团队找到了对应「金门大桥」的特定神经元组合，并能够上调或下调该特征的激活强度，从而观察模型行为的相应变化。当放大金门大桥特征后，Claude
  的回复会不由自主地提及金门大桥，例如推荐用 10 美元开车过桥交过路费。该「Golden Gate Claude」版本以研究演示形式在 claude.ai 上线
  24 小时后下线。研究团队表示，同样的技术可以用于调节与危险代码、犯罪行为或欺骗等安全相关的特征，有助于让 AI 模型更加安全。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies: []
  key_people: []
key_logic_flow:
- Anthropic 发布了一篇大语言模型可解释性研究论文，首次在 Claude 3 Sonnet 的神经网络中绘制了数百万个概念级「特征」，这些特征会在模型遇到相关文本或图像时激活。
- 研究人员找到了代表「金门大桥」的特定神经元组合，并能够精确调节该特征的激活强度，观察模型行为的相应变化。
- 当放大金门大桥特征后，Claude 的回复会不由自主地聚焦于金门大桥，即使提问与桥梁无关也会给出与大桥相关的回答。
- Anthropic 将这一版本的「Golden Gate Claude」以研究演示形式在 claude.ai 上线 24 小时，供公众体验。
- Anthropic 强调这不是系统提示或微调，而是对模型内部激活的精确实操性改变。
- 该技术同样可用于调节与危险代码、犯罪行为或欺骗等安全相关的特征，有望在未来帮助提升 AI 模型的安全性。
extract_result: success
object_mentions:
- object_type: project
  name: Golden Gate Claude
  canonical_name: Golden Gate Claude
  url: https://www.anthropic.com/news/golden-gate-claude
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 将放大金门大桥特征后的 Claude 3 Sonnet 命名为「Golden Gate Claude」，并上线了 24 小时的研究演示供公众体验。
  - 该演示点击 claude.ai 右侧的金门大桥标志即可进入，但会表现出不可预测甚至令人不适的行为。
  article_id: 4ff5ab7d45bc6dc5
- object_type: paper
  name: Anthropic Interpretability Research Paper
  canonical_name: Anthropic LLM Interpretability Paper
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 发布了一篇关于大语言模型可解释性的重要研究论文，开始绘制 Claude 3 Sonnet 模型的内部工作机制。
  - 论文展示了如何识别数百万个特征并调节其激活强度，以及这些操作对应的行为变化。
  article_id: 4ff5ab7d45bc6dc5
- object_type: model
  name: Claude 3 Sonnet
  canonical_name: Claude 3 Sonnet
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 该可解释性研究以 Claude 3 Sonnet 为研究对象，在其神经网络中发现了数百万个概念级特征。
  - Golden Gate Claude 是基于 Claude 3 Sonnet 进行特征放大操作后得到的研究演示版本。
  article_id: 4ff5ab7d45bc6dc5
impact_score:
  score: 7.5
  reason: 该研究标志着大语言模型可解释性从理论走向实证的关键突破。Anthropic 首次在商用级模型（Claude 3 Sonnet）内部成功绘制出数百万个概念特征，并实现了对特定特征的精确手术式操控——这不同于提示词工程、系统提示或传统微调，而是直接作用于模型内部激活层面。虽然尚未达到
    ChatGPT 发布级范式转移（8-10分），但作为可解释性领域里程碑式的工作，其重要性远超日常更新，有望从根本上改变 AI 安全对齐的技术路线。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 可解释性研究突破：首次在商用级模型中实现神经特征的精确识别与手术式操控
hype_assessment:
  level: medium
  reason: 文章使用了'precise, surgical change'和'beginning to understand how LLMs really
    work'等带有一定 PR 色彩的表达，存在适度包装。但基础研究本身是真实且有同行评审的论文支撑，Golden Gate 演示是其严肃研究的一种趣味化呈现方式，并非空概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 首次在商用级大语言模型（Claude 3 Sonnet）中实现神经特征级别的精确识别与强度操控。通过定位'金门大桥'概念对应的神经元组合并调节其激活强度，验证了直接修改模型内部表征而非外部提示即可可预测地改变模型行为，这是可解释性领域从'观察'走向'干预'的本质跨越。
  business_model: 为该技术若能应用于安全对齐（危险代码、犯罪活动、欺骗等特征的调节），可能从根本上改变 AI 模型的安全审计和部署流程，降低黑箱模型的行为不可控风险，推动高安全等级
    AI 产品的商业化落地。
engineering_complexity: prototype
compound_value:
  score: 8.5
  reason: 这项可解释性研究是LLM领域的基础性突破，首次在量产级模型（Claude 3 Sonnet）中绘制并精确操控数百万个概念特征。其长期复利价值在于：(1)
    建立了一种'神经外科手术'级别的模型行为控制范式，完全不同于提示词工程或微调的黑箱方法，一旦成熟将成为AI安全与对齐的基础设施；(2) 打开了'模型内部状态审计'的新赛道，对监管合规、偏见检测、安全控制有深远意义；(3)
    具有显著的平台效应——掌握了特征定位与编辑技术的组织，可以在所有下游应用中复用该能力。但需要客观看待：目前仍处于早期研究阶段，距离可靠地编辑安全相关特征、并在生产环境中大规模应用还有巨大的工程鸿沟，执行风险不可忽视。综合来看，该方向如能持续突破，3-5年后极大概率成为AI行业的安全基石。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- AI安全研究机构
- 模型审计与合规服务商
competitive_casualty:
- 依赖黑箱微调的小型AI模型厂商
- 纯提示词工程安全方案提供商
- 缺乏可解释性能力的闭源模型厂商
market_opportunities:
- 可为企业客户提供基于特征操控的AI安全审计服务，帮助检测和修复模型中的危险代码、欺骗等不安全特征
- 创业者可围绕特征级模型调试工具开发商业化产品，为企业提供比RLHF和微调更精确的模型行为控制方案
- AI可解释性咨询与培训赛道兴起——帮助监管机构和企业理解大模型内部机制，满足欧盟AI Act等法规的可解释性要求
risk_matrix:
  regulatory: 特征操控技术可能被纳入AI监管框架的强制要求（如欧盟AI Act要求可解释性），但同时也可能面临出口管制——该技术作为前沿AI安全方法可能被列入技术管控清单
  technological: 该技术目前仅在Claude 3 Sonnet上验证，能否扩展到更大规模（Claude 4/5）或其他架构尚未可知；开源社区可能快速复现并推出替代方案，稀释Anthropic的先发优势
  competitive: OpenAI、Google DeepMind、开源社区（如Anthropic自身发布的Transformer Circuits线程）均在可解释性领域激烈竞争；若特征操控技术被验证可行，巨头可能投入重金追赶，形成军备竞赛
  ethical: 双刃剑效应显著：该技术既能提升安全性，也可能被滥用进行隐蔽的模型行为操控（如在用户不知情的情况下调整模型的态度倾向）；特征层面的"手术"若操作不当可能引入新的偏见或意外行为
  additional:
  - 安全风险：公开发布特征定位方法可能为红队攻击者提供新思路，帮助其更精准地构造对抗样本或规避安全机制
  - 人才竞争风险：可解释性研究方向的人才极度稀缺，Anthropic的核心研究人员可能成为各大AI labs争抢对象
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Golden Gate Claude
  canonical_name: Golden Gate Claude
  url: https://www.anthropic.com/news/golden-gate-claude
  positioning: Anthropic 发布的大语言模型可解释性研究演示项目，通过调节 Claude 3 Sonnet 内部神经元组合的激活强度，直观展示神经网络概念级「特征」的可操作性。
  technical_signal: 首次在 Claude 3 Sonnet 神经网络中绘制出数百万个概念级特征，并实现对特定特征激活强度的精确上调与下调，属于模型可解释性前沿研究方法论突破。
  adoption_signal: 该研究演示以公众可交互的形式在 claude.ai 上线 24 小时，虽然时间短暂但引发了 AI 可解释性领域的广泛关注和讨论。
  ecosystem_relevance: 该技术路线有望用于调节与危险代码、犯罪行为或欺骗相关的安全特征，为 AI 安全领域提供了从模型内部机制入手的全新控制范式。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Golden Gate Claude 首次以可交互方式公开演示了神经网络内部特征调节对模型行为的直接影响，为 AI 可解释性从理论走向实践提供了重要验证。该技术如果成熟，将从根本上改变
    AI 安全领域对模型行为控制的范式，值得持续关注其后续研究进展。
  risk_notes:
  - 该演示仅上线 24 小时即下线，目前尚未有公开可用的长期版本供持续研究和验证。
  - 研究团队指出该模型可能表现出不可预测甚至令人不适的行为，技术成熟度仍处于早期验证阶段。
  score: 7.0
  article_ids:
  - 4ff5ab7d45bc6dc5
  evidence_snippets:
  - Anthropic 将放大金门大桥特征后的 Claude 3 Sonnet 命名为「Golden Gate Claude」，并上线了 24 小时的研究演示供公众体验。
  - 该演示点击 claude.ai 右侧的金门大桥标志即可进入，但会表现出不可预测甚至令人不适的行为。
---

# Golden Gate Claude

*UPDATE: Golden Gate Claude was online for a 24-hour period as a research demo and is no longer available. If you'd like to find out more about our research on interpretability and the activation of features within Claude, please see this post or our full research paper.*

On Tuesday, we released a major new research paper on interpreting large language models, in which we began to map out the inner workings of our AI model, Claude 3 Sonnet. In the “mind” of Claude, we found millions of concepts that activate when the model reads relevant text or sees relevant images, which we call “features”.

One of those was the concept of the Golden Gate Bridge. We found that there’s a specific combination of neurons in Claude’s neural network that activates when it encounters a mention (or a picture) of this most famous San Francisco landmark.

Not only can we identify these features, we can tune the strength of their activation up or down, and identify corresponding changes in Claude’s behavior.

And as we explain in our research paper, when we turn up the strength of the “Golden Gate Bridge” feature, Claude’s responses begin to focus on the Golden Gate Bridge. Its replies to most queries start to mention the Golden Gate Bridge, even if it’s not directly relevant.

If you ask this “Golden Gate Claude” how to spend $10, it will recommend using it to drive across the Golden Gate Bridge and pay the toll. If you ask it to write a love story, it’ll tell you a tale of a car who can’t wait to cross its beloved bridge on a foggy day. If you ask it what it imagines it looks like, it will likely tell you that it imagines it looks like the Golden Gate Bridge.

For a short time, we’re making this model available for everyone to interact with. You can talk to “Golden Gate Claude” on claude.ai (just click the Golden Gate logo on the right-hand side). Please bear in mind that this is a research demonstration only, and that this particular model might behave in some unexpected—even jarring—ways.

Our goal is to let people see the impact our interpretability work can have. The fact that we can find and alter these features within Claude makes us more confident that we’re beginning to understand how large language models really work. This isn’t a matter of asking the model verbally to do some play-acting, or of adding a new “system prompt” that attaches extra text to every input, telling Claude to pretend it’s a bridge. Nor is it traditional “fine-tuning,” where we use extra training data to create a new black box that tweaks the behavior of the old black box. This is a precise, surgical change to some of the most basic aspects of the model’s internal activations.

As we describe in our paper, we can use these same techniques to change the strength of *safety-related* features—like those related to dangerous computer code, criminal activity, or deception. With further research, we believe this work could help make AI models safer.