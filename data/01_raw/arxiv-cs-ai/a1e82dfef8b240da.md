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
pipeline_stage: ingested
id: a1e82dfef8b240da
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