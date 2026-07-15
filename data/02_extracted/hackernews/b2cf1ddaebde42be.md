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
tldr: 匿名研究员在 GitHub 发布 22 个未公开 0-day 漏洞 PoC，涉及 Docker、Firefox、FFmpeg 等知名软件
objective_summary: 匿名安全研究员在 GitHub 创建 exploitarium 仓库，集中发布 22 个未公开漏洞的 PoC，覆盖 7zip、Docker、Firefox、FFmpeg、Ghidra、libssh2、OpenVPN、PHP、VLC
  等软件。该研究员声称使用 GPT-5.
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - GitHub
  - Docker
  - Mozilla
  - Amazon
  - VideoLAN
  - OpenVPN
  - PHP Group
  technologies:
  - GPT-5.5-3-Codex-Spark
  - Ghidra
  - fuzzing
  key_people:
  - 4D4J
key_logic_flow:
- 匿名安全研究员在 GitHub 创建 exploitarium 仓库，集中发布 22 个未公开漏洞的 PoC（概念验证代码）。
- 仓库覆盖 Docker、Firefox、FFmpeg、Ghidra、libssh2、OpenVPN、PHP、VLC 等多个知名软件的漏洞，部分为 0-day 且未分配
  CVE。
- 该研究员使用 GPT-5.5-3-Codex-Spark 模型自动化模糊测试工作流，但强调 PoC 代码为手动编写而非 AI 生成。
- 该研究员自称拥有相关学位并发表过多篇模糊测试方法论论文，否认完全依赖 AI 进行漏洞发现。
- 仓库中 libssh2 漏洞已获 CVE 编号（CVE-2026-55200），另有多个漏洞涉及 c-ares、nghttp2、Nmap、System Informer
  等基础设施软件。
- 研究员声明该仓库为善意公开披露的漏洞研究，禁止恶意使用，并在 Discord 上以 @ashdfrkl 身份接受协作讨论。
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