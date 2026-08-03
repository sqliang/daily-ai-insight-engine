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