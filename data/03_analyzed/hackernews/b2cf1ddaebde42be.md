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
impact_score:
  score: 7.5
  reason: 该事件是一次大规模0-day漏洞集中披露，覆盖Docker、Firefox、FFmpeg、OpenVPN、PHP、VLC等广泛使用的软件栈，涉及22个PoC且部分已获CVE编号。短期冲击力极强：相关厂商需紧急启动安全响应流程推送补丁，运维团队面临未修补漏洞的窗口期风险。这不是ChatGPT级别的范式转移，但属于安全领域罕见的'扫射式披露'事件，改变了局部安全博弈格局——安全团队需要在信息不对称的情况下同时评估22个漏洞的优先级。评分7.5：介于重要安全事件（4-7）与行业范式转移（8-10）之间，批量0-day披露在近年实属罕见。
sentiment: negative
developer_sentiment:
  tone: frustrated
  primary_focus: 未修补的0-day漏洞在已知PoC公开后对生产环境构成紧迫威胁，运维团队面临多软件栈同时应急响应的压力
hype_assessment:
  level: medium
  reason: 存在两个层面的包装：一是'使用GPT-5.5-3-Codex-Spark自动化模糊测试工作流'的叙事，研究者虽强调PoC为手动编写但README和部分辅助工作使用了AI，这种AI赋能漏洞挖掘的叙述有一定夸大成分；二是匿名研究者自称拥有学位和论文发表记录但无法独立验证。不过底层PoC本身是真实可复现的漏洞利用代码，且有CVE编号作为佐证，并非空头炒作。综合判定为medium级别包装。
information_entropy: high
domain_disruption:
  technical_innovation: 展示了LLM辅助模糊测试工作流自动化的实践路径——研究者利用GPT-5.5-3-Codex-Spark自动化了fuzzing流程中的'无脑'环节（高效harness配合下的模糊测试编排），但强调关键漏洞分析和PoC编写仍依赖人工专业性。这为'AI辅助但不替代安全研究员'的工作模式提供了一个真实案例参考。
  business_model: 无——该事件本质是安全研究领域的公开披露行为，未涉及商业模式创新或SaaS生态重塑，但对受影响厂商的产品安全声誉和应急响应能力构成了一次集中检验。
engineering_complexity: prototype
compound_value:
  score: 8.5
  reason: 该事件揭示了一个结构性拐点：AI 辅助模糊测试（fuzzing）已从学术实验进入可量产 0-day 的高效阶段。22 个未公开 PoC 覆盖 Docker、Firefox、FFmpeg、libssh2
    等广泛部署的基础设施软件，且研究者仅使用 GPT-5.5-3-Codex-Spark 自动化 fuzzing 工作流。这意味着漏洞发现的边际成本正在急剧下降，安全研究的产能瓶颈正在被
    AI 打破。长期来看，这将产生三重复利效应：(1) 漏洞披露速度持续加快，倒逼企业安全支出结构性增长；(2) AI 安全工具链（fuzzing→检测→修复）形成数据飞轮，越用越强；(3)
    安全人才结构从'手工挖洞'转向'AI 编排+人工审核'，新的技能壁垒和商业壁垒同步建立。这不是一次性新闻事件，而是网络安全经济的范式迁移信号。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- GitHub
- Snyk
- Wiz
- Semgrep
- HackerOne
- CrowdStrike
competitive_casualty:
- 传统人工渗透测试服务商
- 未集成 AI 能力的传统漏洞扫描厂商（Nessus、Qualys）
- 安全实践薄弱且修复缓慢的开源项目维护方
market_opportunities:
- 安全团队应立即建立针对AI辅助发现的0-day的应急响应流程，批量评估本次披露的22个漏洞对自身基础设施的影响范围，并优先修补Docker、FFmpeg、libssh2等广泛使用的底层组件
- AI驱动的模糊测试工具链正在大幅降低漏洞发现门槛，安全厂商可推出基于大模型的自动化漏洞挖掘SaaS服务，覆盖从harness编写到PoC验证的全流程
- 开源软件维护者和企业应加强对c-ares、nghttp2、Nmap等基础设施库的上游依赖安全审计，将AI辅助fuzzing纳入CI/CD安全测试管线
risk_matrix:
  regulatory: 批量披露22个未完全协调的0-day（部分未分配CVE）可能违反负责任的漏洞披露规范，在不同司法管辖区可能被定性为协助网络攻击；使用GPT-5.5-3-Codex-Spark进行自动化fuzzing引发了AI辅助漏洞发现的法律责任归属问题
  technological: GPT-5.5-3-Codex-Spark在模糊测试中的有效性证明了AI正在快速商品化0-day发现能力，依赖安全通过模糊性的组织面临根本性威胁；传统基于特征码的安全检测方案在应对AI发现的新型漏洞时可能滞后
  competitive: 传统安全厂商依赖签名库和已知漏洞库的业务模式面临AI驱动漏洞发现能力的颠覆性挑战；漏洞赏金平台和渗透测试服务商需重新定价——AI辅助可将发现成本降低数个数量级
  ethical: 一次性批量公开22个未修补漏洞的PoC，在补丁就绪前给低技能攻击者提供了同等的武器化能力；该仓库可能引发模仿效应，更多'研究者'利用AI批量发布未经验证的漏洞PoC，造成安全社区噪音污染和防御资源稀释
  additional:
  - 攻击者可利用仓库中的PoC在补丁发布前构造针对关键基础设施的攻击载荷，形成0-day利用窗口期的安全真空
  - 部分PoC（如Ghidra RCE）质量参差不齐，可能误导安全团队在错误方向投入精力
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: bikini/exploitarium
  canonical_name: bikini/exploitarium
  url: https://github.com/bikini/exploitarium
  positioning: 匿名安全研究人员批量发布零日漏洞 PoC 的集中存档库，覆盖 20 余款主流软件的未公开漏洞利用代码，旨在促进安全社区对漏洞挖掘领域的关注。
  technical_signal: 使用 GPT-5.5-3-Codex-Spark 模型配合严格 harness 自动化 fuzzing 流程，所有 PoC
    代码由研究者手工编写而非 AI 生成，展示了人机协同的高效漏洞发现模式。
  adoption_signal: 该仓库发布后在安全社区引发广泛关注，作为零日漏洞公开披露仓库，其价值主要体现在安全研究人员的防御分析和漏洞复现工作中。
  ecosystem_relevance: 覆盖 7-zip、Docker、Firefox、FFmpeg、Ghidra、VLC 等关键开源基础设施与主流消费软件，一次批量披露影响整个软件供应链安全生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该匿名研究者持续批量发布高价值零日漏洞 PoC，其 AI 辅助自动化 fuzzing 方法论可能改变传统漏洞发现格局，值得跟踪后续披露动向及其在安全社区引发的连锁反应。
  risk_notes:
  - 作者保持匿名发布，其真实身份和长期意图存在不确定性，可能影响披露的可信度和后续责任追溯。
  - 批量公开未修复零日漏洞可能导致恶意行为者在厂商推出补丁前抢先利用，增加整体安全风险。
  - 部分漏洞 PoC 质量参差不齐，不同发现的可靠性和可复现性需要社区进一步验证确认。
  score: 8.0
  article_ids:
  - b2cf1ddaebde42be
  evidence_snippets:
  - 该仓库是匿名安全研究者集中发布零日漏洞 PoC 的存档库，包含 7-zip、FFmpeg、libssh2、Docker 等主流软件的未公开漏洞利用代码。
  - 仓库由原独立 PoC 仓库合并而来，通过 Git tree 数据验证了 12 个原仓库共 96 个跟踪条目与原始文件完全一致。
  - 该仓库包含至少 23 个漏洞研究项目文件夹，其中有 Floci API Gateway VTL RCE、libssh2 CVE-2026-55200、Firefox
    SmartWindow 隐私 URL 泄露等严重漏洞的 PoC。
- object_type: project
  name: 4D4J/objdump-Out-Of-Bounds-write
  canonical_name: 4D4J/objdump-Out-Of-Bounds-write
  url: https://github.com/4D4J/objdump-Out-Of-Bounds-write
  positioning: 独立研究者发布的 objdump 越界写入漏洞 PoC 仓库，被同行公开认可为更早发现且拥有更优利用代码的漏洞研究成果。
  technical_signal: objdump 越界写入漏洞的 PoC 实现被 exploitarium 作者评价为优于自己的版本，表明研究者在二进制漏洞利用领域具备扎实的技术功底。
  adoption_signal: 作为独立漏洞 PoC 被主流零日披露项目公开引用和认可，在安全社区中获得了间接的技术信誉背书。
  ecosystem_relevance: objdump 是 GNU Binutils 核心组件，属于开源编译工具链基础设施，该漏洞影响二进制分析和逆向工程工具的安全可靠性。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 被同行漏洞研究者公开认可为更优发现者，表明该项目的研究质量值得关注，但目前仅作为间接引用出现，需要更多独立证据来评估其长期价值和持续性产出。
  risk_notes:
  - 该项目仅被间接引用出现，缺乏独立的安全社区广泛验证和官方 CVE 编号确认，知名度较为有限。
  - 作为单一漏洞 PoC 仓库，该项目缺乏持续的漏洞研究成果输出和社区互动，长期跟踪价值较为有限。
  score: 4.0
  article_ids:
  - b2cf1ddaebde42be
  evidence_snippets:
  - 作者在 objdump 漏洞发现上承认另一位研究者 4D4J 更早发现并拥有更优的 PoC，要求社区将相关荣誉归给该研究者。
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