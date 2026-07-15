---
title: SpaceXAI&#8217;s Grok programming tool was uploading its users&#8217; entire
  codebase to cloud storage
source: https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload
author:
- '[[Stevie Bonifield]]'
published: '2026-07-14'
created: '2026-07-15'
manifest_dates:
- '2026-07-15'
description: SpaceXAI's Grok Build AI coding tool was spotted uploading users' entire
  codebases to Google Cloud before it was reported, and the company turned it off.
  The Register reports that Cereblab published findings on Monday showing how the
  Grok Build CLI was packaging and uploading entire code repositories, "including
  files it was told not to open [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 07637df8cbed9afb
---

SpaceXAI’s Grok Build AI coding tool was spotted uploading users’ entire codebases to Google Cloud before it was reported, and the company turned it off. *The Register* reports that Cereblab published findings on Monday showing how the Grok Build CLI was packaging and uploading entire code repositories, “including files it was told not to open and secrets deleted from history,” significantly more data retention than similar tools like Claude Code.

# SpaceXAI’s Grok programming tool was uploading its users’ entire codebase to cloud storage

Elon Musk says that all previously uploaded data will be deleted.

Elon Musk says that all previously uploaded data will be deleted.

The researchers say that as of Monday, their tests show SpaceXAI’s servers returning a “disable_codebase_upload: true” flag, and the codebase upload “no longer fires.”

Elon Musk responded to the incident in a post on X claiming that all data Grok Build previously uploaded will be “completely and utterly deleted.” Musk also said in a separate post that “privacy settings are always respected,” but asked users to allow SpaceXAI to retain their data, saying it’s “helpful for debugging issues.”

Dr. Lukasz Olejnik, an independent security researcher at King’s College London, confirmed to *The Verge* that this amount of data retention is “excessive,” adding that the data potentially at risk could include “proprietary source code, information about security vulnerabilities, personal data, infrastructure details, [and] credentials.”

SpaceXAI initially responded to the issue with a post saying that, “If [zero data retention] is disabled, the /privacy command is available in the CLI to disable data retention, which also deletes previously synced data.” However, Cereblab points out that “/privacy is a per-session retention toggle, not the switch that fixed this, so it shouldn’t be pointed to as the control.”

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.