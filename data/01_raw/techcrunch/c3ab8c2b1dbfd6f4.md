---
title: Cybersecurity researchers aren’t happy about the guardrails on Anthropic’s
  Fable
source: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
author:
- '[[Lorenzo Franceschi-Bicchierai]]'
published: '2026-06-10'
created: '2026-06-11'
description: Cybersecurity researchers are complaining that Anthropic's new model
  Fable has guardrails that are too strict for any cybersecurity work.
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: c3ab8c2b1dbfd6f4
---

Anthropic released its latest model Fable on Tuesday, billing it as a public and limited version of its powerful and much-hyped cybersecurity model Mythos.

But not everyone is happy with the restrictions, and a number of cybersecurity researchers and professionals have aired complaints online.

“[Fable] rejects any request that could be tangentially cyber related. Even innocuous tasks like reading a blog post,” said Valentina “Chompie” Palmiotti, a well-known security researcher who works at IBM X-Force.

When a prompt triggers its guardrails, Fable pauses the chat and says that its “safety measures flagged this message for cybersecurity or biology topics.”

The guardrails were put in place to limit the risk that Fable could be used to develop malware or compromise software — a long-standing concern within Anthropic. The restrictions on biology come from a similar concern around developing biological weapons.

When the AI giant released Mythos in April, it restricted the model to a limited number of companies and organizations in what it called Project Glasswing, an effort to deploy the model to secure critical software and infrastructure. Last week, Anthropic expanded access to Mythos to hundreds of organizations in 15 countries.

But despite the good intentions, many cybersecurity experts are still put off by the haphazard nature of the restrictions. Matt Suiche, a cybersecurity veteran, told TechCrunch that “if you ask it to write secure code, it assumes it is cybersecurity related work instead of software engineering best practices, and you get downgraded.” Fable is programmed to fall back to Claude Opus 4.8 if it hits a guardrail. “It seems to be keyword based, so anything in the lexical field of ‘cybersecurity’ triggers the guardrails.”


#### Contact Us

Do you have more information about how hackers are using AI? Or how cybersecuity companies are using AI? We’d love to hear from you. From a non-work device and network, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or email.“But it is understandable as we are still in the early days and they are still adapting their guardrails. I am sure they are going to evolve over time as Anthropic and other frontier model companies will collaborate more with the current new generation of cybersecurity companies,” said Suiche, who is a member of the technical staff at Tolmo, an AI cybersecurity startup. “It’s better to catch more people than not enough when you do such a release and to relax the guardrails over time.”

Another researcher griped on X that “even asking for a code review” triggers Fable’s guardrails.

Anthropic did not immediately respond to a request for comment.