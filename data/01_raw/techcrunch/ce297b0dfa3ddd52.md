---
title: The ‘first’ AI-run ransomware attack still needed a human
source: https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/
author:
- '[[Connie Loizos]]'
published: '2026-07-06'
created: '2026-07-07'
description: An AI agent carried out the technical execution of a real-world ransomware
  attack for the first known time, but new details show a human still chose the victim,
  set up the infrastructure, and supplied stolen credentials — meaning it wasn't quite
  the fully autonomous cybercrime debut that last week's headlines suggested.
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: ce297b0dfa3ddd52
---

Last week, researchers at cloud security firm Sysdig said they’d documented the first known case of “agentic ransomware.” It was an extortion operation, dubbed JadePuffer, in which an AI agent — not a human — handled the technical execution of a real-world cyberattack from start to finish. The agent broke into a vulnerable server, stole credentials, moved through the target’s network, encrypted files, and even wrote its own ransom note, adapting to obstacles along the way like a human hacker would. Coverage of the funding described it as run “without any human oversight,” with “no human at the keyboard.”

That’s not quite the *full* picture. In an interview on Monday with CyberScoop, Sysdig’s Michael Clark, the company’s senior director of threat research, clarified that a human was still very much involved — just not in the technical execution. “A human still set up and pointed the operation and provisioned the infrastructure behind it, the command-and-control server, the staging server used for the stolen data and chose a victim,” Clark said. The credentials used to break into the victim’s database, he added, weren’t harvested by the AI agent itself; someone obtained them separately, through a prior compromise, and handed them to the operation.

None of this contradicts Sysdig’s original claim, and the technical details of the attack remain notable on their own — wild, even. The agent got in through a known bug in Langflow, a popular open-source tool for building LLM apps, then moved on to a production MySQL server and exploited another known flaw to gain admin access. It encrypted over 1,300 configuration records and not only left behind a ransom note that it wrote itself but it left a Bitcoin address where the ransom could be sent. Sysdig hasn’t disclosed who was targeted.

The techniques were fairly ordinary apparently, what stood out was the speed and transparency involved. The agent fixed a failed login in 31 seconds, narrating its own reasoning in natural-language code comments the whole way.

One detail that initially seemed to muddy the picture has since been clarified. Clark had told CyberScoop that Sysdig found “multiple models were used in the attack,” citing harvested keys for OpenAI, Anthropic, DeepSeek, and Gemini — language that left open the question of whether several models actively powered different stages of the intrusion. Asked to clarify, Clark told TechCrunch that those keys were simply part of what the agent stole, not evidence of what was driving it.

“The agent swept the Langflow host for anything valuable — provider API keys, cloud credentials, cryptocurrency wallets, and database configs — and those provider keys were part of the loot,” he said via email. “They are indicative of what the attacker considered worth taking, but they do not tell us which model was making the decisions.”