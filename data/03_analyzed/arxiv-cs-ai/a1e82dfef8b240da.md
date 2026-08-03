---
title: Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models
source: https://arxiv.org/abs/2607.21617
author:
- '[[Gwang Gook Lee, Kenan Emir Ak, Jay Mohta, Yan Xu, Dimitrios Dimitriadis]]'
published: '2026-07-27'
created: '2026-07-27'
manifest_dates:
- '2026-07-27'
description: 'arXiv:2607.21617v1 Announce Type: new Abstract: Vision Language Models
  (VLMs) are increasingly used in place of traditional OCR pipelines for document
  understanding. In this paper, we show they do not always act as faithful transcribers:
  when text is imperfect, they often tend to rewrite it into a more plausible form
  - a behavior that clean-text OCR benchmarks cannot detect. We introduce FaithC4,
  a multilingual perturbation benchmark of 1,455 single-page documents (English, Chinese,
  Korean) with three perturbation families: scramble, random substitution, and visually
  similar substitution. We use the benchmark to evaluate 15 systems spanning general-purpose
  VLMs, OCR-specialized VLMs, and traditional OCR pipelines. These three categories
  differ in WER degradation under perturbation: general-purpose VLMs degrade by up
  to 4.5 points, OCR-specialized VLMs by 0.2-2 points, and traditional OCR by less
  than 0.6 points on English. Probing Qwen3-VL-4B layer-by-layer, we identify a consistent
  pattern: rewriting fires only when a perturbed word''s final layer FFN representation
  stays close to the original encoding; when the representation diverges sufficiently,
  the model transcribes faithfully. Word length affects rewriting rate: short words
  (4-6 characters) are rewritten up to 10% of the time, with a sharp cutoff at 8 characters
  above which rewriting drops to 0%.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a1e82dfef8b240da
source_type: academic_paper
tldr: 该论文发现视觉语言模型（VLM）在转录瑕疵文本时倾向于将其"重写"为更合理形式而非忠实转录，并发布了包含1,455份多语言文档的FaithC4基准测试集来验证这一现象。
objective_summary: 研究者通过引入FaithC4多语言扰动基准测试集（含1,455份英语、中文和韩语单页文档），对15个系统（通用VLM、OCR专用VLM和传统OCR管线）进行转录忠实性评估。结果显示通用VLM在扰动下词错误率退化高达4.5个百分点，而传统OCR管线退化小于0.6个百分点。对Qwen3-VL-4B的逐层分析表明重写行为仅在扰动词最后一层FFN表示接近原始编码时触发，短词（4-6字符）被重写的概率达10%，超过8字符后降至0%。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - VLM
  - OCR
  - FaithC4
  - Qwen3-VL-4B
  key_people: []
key_logic_flow:
- 论文指出视觉语言模型在替代传统OCR管线进行文档理解时，并不始终忠实转录原文，而是倾向于将瑕疵文本重写为更合理的形式，传统干净文本OCR基准无法检测此行为。
- 研究者发布了FaithC4多语言扰动基准测试集，包含1,455份单页文档，覆盖英语、中文和韩语三种语言以及三种扰动类型：打乱顺序、随机替换和视觉相似替换。
- 在15个系统的评估中，通用VLM的词错误率退化高达4.5个百分点，OCR专用VLM退化0.2至2个百分点，传统OCR管线退化小于0.6个百分点。
- 对Qwen3-VL-4B的逐层分析发现，重写行为仅当扰动词最后一层前馈网络表示接近原始编码时才被激活，当表示偏离足够大时模型会忠实转录。
- 词长度影响重写率：4至6个字符的短词重写率高达10%，而8个字符以上的词重写率骤降至0%。
object_mentions:
- object_type: dataset
  name: FaithC4
  canonical_name: FaithC4
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - FaithC4是一个包含1,455份单页文档的多语言扰动基准测试集，涵盖英语、中文和韩语三种语言以及三种扰动类型。
  - 该基准测试集专为评估视觉语言模型在文本瑕疵条件下的转录忠实性而设计，填补了传统干净文本OCR基准的检测盲区。
  article_id: a1e82dfef8b240da
- object_type: model
  name: Qwen3-VL-4B
  canonical_name: Qwen3-VL-4B
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 研究团队对Qwen3-VL-4B进行逐层分析，发现重写行为仅在扰动词最后一层前馈网络表示接近原始编码时才会触发。
  - 当扰动词的最终层表示与原始编码偏离足够大时，Qwen3-VL-4B会放弃重写并忠实地转录所见文本。
  article_id: a1e82dfef8b240da
extract_result: success
impact_score:
  score: 6.8
  reason: 该论文揭示了一个此前未被系统检测到的VLM关键缺陷——在转录瑕疵文本时倾向于'重写'而非'忠实转录'。对于正快速用VLM替代传统OCR的文档理解领域（发票识别、表单处理、文档数字化等），这一发现具有直接实践意义：通用VLM在扰动下词错误率退化高达4.5个百分点，短词（4-6字符）重写率达10%。虽非范式转移级别（如ChatGPT发布），但足以让相关工程团队重新评估VLM替代OCR的可靠性边界，属于中等偏上的行业冲击力。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: VLM在文档转录中的忠实性缺陷——4-6字符短词10%的重写率对生产级OCR管线可靠性构成实质性威胁
hype_assessment:
  level: low
  reason: 论文毫无概念炒作成分。提供了完整的实验设计：1,455份多语言文档基准（FaithC4）、15个系统的横向对比（含通用VLM、OCR专用VLM和传统OCR管线）、三种扰动类型（打乱/随机替换/视觉相似替换）、逐层机制分析和词长度效应。结论有充分的数据支撑，且明确指出局限性（仅限单页文档、特定扰动类型），属于高质量的学术贡献。
information_entropy: high
domain_disruption:
  technical_innovation: 首次系统性地识别和量化了VLM在文档转录中的'重写'现象（rewriting），发布FaithC4多语言扰动基准测试集（1,455份文档，覆盖英语/中文/韩语及三种扰动类型），并通过Qwen3-VL-4B逐层分析揭示了重写的机制——仅当扰动词最后一层前馈网络表示接近原始编码时才触发，偏离足够大时模型恢复忠实转录。这一发现为VLM的忠实性研究提供了可复现的评估框架。
  business_model: 对正在用VLM替代传统OCR的商业场景（发票识别、表单处理、文档归档、票据数字化等）提出明确的可靠性警告。短期内可能推动企业采用'VLM做高层面理解
    + 传统OCR做底层转录'的混合架构而非纯VLM替代；中长期可能催生以忠实性为优化目标的VLM微调服务或专用转录模型市场，以及围绕FaithC4基准的评估服务。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 该论文揭示了 VLM 在文档理解场景中的一个系统性缺陷——对瑕疵文本的"重写"倾向，这是一个基础性的可靠性问题，直接关系到企业级文档理解（发票、合同、表单等）能否放心用
    VLM 替代传统 OCR。FaithC4 基准测试集本身作为独立资产的复利效应有限，它更可能被整合进更大的评估框架而非独立成为长期标准。但论文的核心洞察（重写行为仅在
    FFN 层表示接近原始编码时触发、短词重写率高达 10%、8 字符以上骤降至 0%）具有持久学术价值，将推动行业共识从"VLM 全面替代 OCR"转向"VLM
    + 传统 OCR 混合架构"。从 VC 视角看，这不会颠覆格局，但会修正资本配置方向：纯 VLM 文档理解创业公司的估值逻辑承压，而混合方案和评估工具获得结构性利好。综合评分
    5.5，属于重要的细分认知资产，但非基础设施级复利标的。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- ABBYY
- Google Cloud Document AI
- Microsoft Azure Document Intelligence
- Tesseract OCR
- 混合架构文档 AI 初创公司
competitive_casualty:
- 端到端纯 VLM 文档理解初创公司
- 过度营销 VLM 替代传统 OCR 的方案商
- 未配备 OCR 回退机制的通用 VLM 文档管线
market_opportunities:
- 面向金融、法律、医疗等强监管行业开发带有忠实转录保障机制的VLM文档处理系统，将FaithC4基准测试嵌入CI/CD管线作为质量门禁
- 基于本研究发现，打造混合OCR+VLM架构即服务产品，在保持传统OCR转录忠实度的同时叠加VLM的语义理解能力，形成差异化竞争优势
- 将FaithC4多语言扰动基准测试集商业化，提供面向企业级VLM文档管线的忠实性评估与合规认证服务
risk_matrix:
  regulatory: 若VLM被用于身份证件、合同、法律文件等强监管场景，非忠实转录行为可能导致合规违规（如GDPR数据准确性要求），甚至产生法律效力争议
  technological: 本论文揭示了当前VLM架构在转录任务上的根本性局限：FFN层的重写机制是架构级行为而非表面bug，传统OCR在忠实性维度仍不可替代，短期内VLM难以完全替代OCR管线
  competitive: 传统OCR厂商（ABBYY、Google Cloud Vision、百度OCR等）可引用本研究发现作为差异化论据，强化'忠实可靠'的品牌定位，挤压VLM文档处理产品的市场空间
  ethical: 非忠实转录可能导致文档信息被无意识篡改，在历史档案数字化、学术文献转录、个人信息采集等场景下引发数据完整性和信息真实性问题
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models

View PDF HTML (experimental)Abstract:Vision Language Models (VLMs) are increasingly used in place of traditional OCR pipelines for document understanding. In this paper, we show they do not always act as faithful transcribers: when text is imperfect, they often tend to rewrite it into a more plausible form - a behavior that clean-text OCR benchmarks cannot detect. We introduce FaithC4, a multilingual perturbation benchmark of 1,455 single-page documents (English, Chinese, Korean) with three perturbation families: scramble, random substitution, and visually similar substitution. We use the benchmark to evaluate 15 systems spanning general-purpose VLMs, OCR-specialized VLMs, and traditional OCR pipelines. These three categories differ in WER degradation under perturbation: general-purpose VLMs degrade by up to 4.5 points, OCR-specialized VLMs by 0.2-2 points, and traditional OCR by less than 0.6 points on English. Probing Qwen3-VL-4B layer-by-layer, we identify a consistent pattern: rewriting fires only when a perturbed word's final layer FFN representation stays close to the original encoding; when the representation diverges sufficiently, the model transcribes faithfully. Word length affects rewriting rate: short words (4-6 characters) are rewritten up to 10% of the time, with a sharp cutoff at 8 characters above which rewriting drops to 0%.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.