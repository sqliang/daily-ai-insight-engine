---
title: Anonymous GitHub account mass-dropping undisclosed 0-days
source: https://github.com/bikini/exploitarium
author:
- '[[binyu]]'
published: '2026-06-27'
created: '2026-06-28'
description: 'Article URL: https://github.com/bikini/exploitarium Comments URL: https://news.ycombinator.com/item?id=48698617
  Points: 797 # Comments: 311'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b2cf1ddaebde42be
source_type: community_discussion
extract_result: success
tldr: 匿名研究人员通过 GitHub 账户 bikini 创建 exploitarium 仓库，批量公开了 7-zip、FFmpeg、libssh2、Docker、Firefox、Ghidra
  等 20 余款主流软件的大量未公开零日漏洞 PoC，并披露其使用 GPT-5.5-3-Codex-Spark 模型辅助自动化 fuzzing 以发现这些漏洞。
objective_summary: 安全研究人员通过 GitHub 账户 bikini 于 2026 年 6 月下旬创建 exploitarium 仓库，集中发布了此前多个独立
  PoC 仓库的零日漏洞利用代码。该仓库包含至少 23 个漏洞研究项目，涉及 7-zip（RAR5 MOTW 链绕过）、AnyDesk（打印机 COM 模拟攻击）、c-ares（TCP
  释放后使用）、Docker（cp 复制目的地逃逸）、Firefox（SmartWindow 私有 URL 泄露）、Floci/AWS API Gateway（VTL
  远程代码执行）、FFmpeg（RASC DLTA 计算错误）、Ghidra 12.1.2（远程代码执行）、libssh2（CVE-2026-55200）、PHP
  8.5.7（流桶 SOAP RCE）、RustDesk（会话权限绕过）、VLC（VP9 分辨率切换崩溃）等主流软件的未公开漏洞。作者自称拥有 fuzzing 方法论学位并发表过多篇相关论文，使用
  GPT-5.5-3-Codex-Spark 模型配合严格 harness 自动化 fuzzing 流程，所有 PoC 代码为手工编写而非 AI 生成。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - AWS
  - Docker
  - Mozilla
  - Gitea
  - OpenVPN
  - VideoLAN
  - Oracle
  - RustDesk
  technologies:
  - GPT-5.5-3-Codex-Spark
  - fuzzing
  - RCE
  - LPE
  - UAF
  - ACE
  - MCP
  - VTL
  key_people:
  - bikini
  - 4D4J
key_logic_flow:
- 匿名安全研究人员通过 GitHub 账户 bikini 创建了 exploitarium 仓库，集中发布了大量此前未公开的零日漏洞 PoC，涉及 7-zip、FFmpeg、libssh2、Docker
  等 20 余款主流软件。
- 作者使用 GPT-5.5-3-Codex-Spark 模型自动化 fuzzing 流程，在配合高效 harness 和人工监督的条件下完成了漏洞发现工作。
- 该仓库列出了 23 个漏洞 PoC 项目，包括 Floci（AWS API Gateway VTL 远程代码执行）、libssh2 CVE-2026-55200、Firefox
  SmartWindow 隐私 URL 泄露、Docker cp 目的地逃逸等严重漏洞。
- 仓库由原独立 PoC 仓库合并而来，通过 Git tree 数据验证了 12 个原仓库共 96 个跟踪条目与原始文件完全一致，零差异。
- 作者在 objdump 漏洞上承认另一位研究者 4D4J 更早发现并拥有更优的 PoC，要求社区将相关荣誉归给该研究者。
- 作者声明所有内容为善意公开披露的漏洞研究，禁止恶意使用，旨在促进安全社区对漏洞挖掘领域的关注。
object_mentions:
- object_type: project
  name: bikini/exploitarium
  canonical_name: bikini/exploitarium
  url: https://github.com/bikini/exploitarium
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该仓库是匿名安全研究者集中发布零日漏洞 PoC 的存档库，包含 7-zip、FFmpeg、libssh2、Docker 等主流软件的未公开漏洞利用代码。
  - 仓库由原独立 PoC 仓库合并而来，通过 Git tree 数据验证了 12 个原仓库共 96 个跟踪条目与原始文件完全一致。
  - 该仓库包含至少 23 个漏洞研究项目文件夹，其中有 Floci API Gateway VTL RCE、libssh2 CVE-2026-55200、Firefox
    SmartWindow 隐私 URL 泄露等严重漏洞的 PoC。
  article_id: b2cf1ddaebde42be
- object_type: model
  name: GPT-5.5-3-Codex-Spark
  canonical_name: GPT-5.5-3-Codex-Spark
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 作者使用 GPT-5.5-3-Codex-Spark 模型自动化所有 fuzzing 工作，在具备高效 harness 和人工监督的情况下该模型足以完成漏洞发现任务。
  article_id: b2cf1ddaebde42be
- object_type: project
  name: 4D4J/objdump-Out-Of-Bounds-write
  canonical_name: 4D4J/objdump-Out-Of-Bounds-write
  url: https://github.com/4D4J/objdump-Out-Of-Bounds-write
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者在 objdump 漏洞发现上承认另一位研究者 4D4J 更早发现并拥有更优的 PoC，要求社区将相关荣誉归给该研究者。
  article_id: b2cf1ddaebde42be
---

This repo was incomplete when published. That's why some findings are kinda ass (ghidra) and some are better. Going forward, only serious vulnerabilities will be shared (Floci, libssh2, FFmpeg, c-ares).

In regard to AI usage, my fuzzing workflow was automated by AI with a strict harness. I used GPT-5.5-3-Codex-Spark for ALL the fuzzing, as barely any "thought" is necessary when provided with an efficient harness. Contrary to the growing narrative that I'm just some random child burning tokens, I DO actually have a degree in the subject and have published multiple papers on fuzzing methodology. I spent years researching and developing new tools and ideas for how to fuzz. You do NOT need a SOTA model to help you identify these issues, I promise! While being able to afford a better model is helpful, my data seems to show that it is only marginal when paired with decent human oversight and a good harness. None of the actual PoCs themselves were vibe-coded; I did, in fact, hand-type them. I did use AI assistance for RustDesk, however, as I'm not as familiar with the language. The README files are very clearly entirely AI, however, as AI can format a pretty mean Markdown file. I reviewed them to make sure they were accurate.

I'd also like to credit someone for the objdump finding. It turns out, someone beat me to the punch (they also have a better PoC too!). Please give them the credit they deserve: https://github.com/4D4J/objdump-Out-Of-Bounds-write

New drops today ;) Biggest thing yet

I've also noticed a surprising amount of "security researchers" aren't able to adjust the PoC to work in their environment. I will broaden the PoCs for those select few...

If you wish to collaborate/discuss with me, contact me on discord @ashdfrkl

Sharing this repo keeps me motivated to continue dropping my findings for you all.

A consolidated archive of my public proof-of-concept and vulnerability research writeups.

Most folders contain one of my former standalone PoC repos, preserved with its original README and tracked files. New research entries are added directly here as self-contained folders.

| Folder | Source | Tracked entries |
|---|---|---|
`7zip-rar5-motw-chain-poc` |
`bd9533f532c1e4ee6af783b9bb49d1133c600e2c` |
3 |
`anydesk-printer-com-impersonation-poc` |
`7491303301093b2d40bee9dadf6b38f757ce78e0` |
4 |
`c-ares-tcp-uaf-calc-poc` |
direct entry, June 24, 2026 | 7 |
`docker-cp-copyout-destination-escape` |
`d1367b1381736d7f961ac808ce88d4e24a633adc` |
5 |
`firefox-smartwindow-private-url-exfil-poc` |
direct entry, June 24, 2026 | 3 |
`floci-apigateway-vtl-rce-poc` |
direct entry, June 23, 2026 | 3 |
`flowise-mcp-env-case-bypass-poc` |
`ed9fab0086674f1b16467990b33bb9299e93429e` |
3 |
`ffmpeg-rasc-dlta-calc-poc` |
direct entry, June 26, 2026 | 7 |
`ghidra-12.1.2-rce-ace-calc-poc` |
`52dee6362990c03c0d753d074c85428824d46368` |
9 |
`gitea-act-runner-container-options-poc` |
`f06d78fb111732f3e7737f4c07e77ef94c4b64bf` |
4 |
`imagemagick-gs-delegate-hijack-poc` |
`8140e8ee0ed78beaf5e8303a795b70b138f5891b` |
5 |
`libssh2-cve-2026-55200-poc` |
direct entry, June 23, 2026 | 3 |
`libssh2-publickey-list-calc-poc` |
direct entry, June 25, 2026 | 10 |
`lunar-modrinth-chain-poc` |
`ffd02120708b6503f11585858ce3724872f3b7a7` |
6 |
`mybb-limited-acp-to-admin` |
`1610e0373943c2f6562a99f917d3a3d1fdd9056d` |
5 |
`nghttp2-nghttpx-upgrade-queue-poison-poc` |
direct entry, June 26, 2026 | 3 |
`nmap-ipv6-extlen-wrap-poc` |
direct entry, June 23, 2026 | 4 |
`objdump-dlx-calc-poc` |
`7df01e4e20c7375a89e8ccf760526c52eb6ad582` |
41 |
`openvpn-connect-echo-script-ace-poc` |
`d2f904d9272d4388c9862131d40e32e072e85e38` |
8 |
`php857-streambucket-soap-rce-rpoc` |
direct entry, June 26, 2026 | 6 |
`rustdesk-session-permission-pocs` |
direct entry, June 25, 2026 | 17 |
`systeminformer-phsvc-trusted-host-lpe-poc` |
direct entry, June 24, 2026 | 3 |
`vlc-vp9-reschange-crash-poc` |
`fae72b82f24d03cf2fb9cb55fbb2e7774f684ff3` |
3 |

This section applies to the former standalone repositories listed above by commit hash.

The consolidation was checked from fresh GitHub clones on June 23, 2026 before the old standalone repos were removed.

The check compared each former standalone repo's `HEAD`

tree against the matching folder here using Git tree data rather than a loose filesystem diff. For every tracked entry, the check required:

- the same relative path;
- the same Git object type;
- the same tree mode, including executable bits;
- the same Git blob ID.

Matching Git blob IDs means the tracked file bytes are identical. The check covered 12 repos and 96 tracked entries with zero mismatches.

This repository preserves the contents of those PoCs. Repository-level metadata such as stars, issues, pull requests, releases, and separate Git history remain in the original repository histories.

Direct entries, including `c-ares-tcp-uaf-calc-poc`

, `ffmpeg-rasc-dlta-calc-poc`

, `firefox-smartwindow-private-url-exfil-poc`

, `floci-apigateway-vtl-rce-poc`

, `libssh2-cve-2026-55200-poc`

, `libssh2-publickey-list-calc-poc`

, `nghttp2-nghttpx-upgrade-queue-poison-poc`

, `nmap-ipv6-extlen-wrap-poc`

, `php857-streambucket-soap-rce-rpoc`

, `rustdesk-session-permission-pocs`

, and `systeminformer-phsvc-trusted-host-lpe-poc`

, are tracked by this repository's commit history.

Do NOT, under any circumstances, use any material in this repository maliciously. This is good-faith, open-disclosure vulnerability research intended to get more people interested in exploring this area of cybersecurity.

Cybercrime is cringe.