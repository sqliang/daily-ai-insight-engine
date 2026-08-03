---
title: A Post-Quantum Future for Let's Encrypt
source: https://letsencrypt.org/2026/06/03/pq-certs
author:
- '[[SGran]]'
published: '2026-06-03'
created: '2026-06-04'
description: 'Article URL: https://letsencrypt.org/2026/06/03/pq-certs Comments URL:
  https://news.ycombinator.com/item?id=48385114 Points: 216 # Comments: 127'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d1f7889f5cffd7ec
source_type: community_discussion
tldr: Let's Encrypt 宣布将采用 Merkle Tree Certificates（MTCs）作为后量子 Web PKI 的技术路线，目标 2026
  年底推出 MTC 签发测试环境、2027 年投入生产。MTCs 通过批量签发证书将单次 TLS 握手认证路径压缩为一条签名+一条公钥+一条包含证明，解决了 ML-DSA
  后量子签名体积过大导致连接失败和延迟的问题。
objective_summary: Let's Encrypt 于 2026 年 6 月 3 日发布公告，计划采用 Merkle Tree Certificates（MTCs）实现后量子安全的
  Web PKI。MTCs 将证书批量签发，用一个签名覆盖整批证书，浏览器的批量签名（landmarks）在 TLS 握手之外更新。常见情况下 MTC 握手只携带一条签名、一条公钥和一条包含证明，比当前
  Web PKI 握手的体积更小。该项目基于 Let's Encrypt 自 2019 年起运营的 Certificate Transparency 日志（同样使用
  Merkle 树数据结构）。Cloudflare 和 Chrome 已在互联网真实流量中开展 MTC 可行性实验，IETF PLANTS 工作组正在推进标准化。Let's
  Encrypt 计划 2026 年底上线 MTC 签发测试环境、2027 年进入生产环境，同时强调现有证书不受影响，后量子证书将以免费和自动化的方式提供给所有
  ACME 客户端用户。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Let's Encrypt
  - Cloudflare
  - Google
  - Chrome
  - Internet Engineering Task Force
  - National Institute of Standards and Technology
  - National Security Agency
  - European Union
  technologies:
  - Merkle Tree Certificates (MTCs)
  - ML-DSA
  - ML-DSA-44
  - TLS
  - ACME
  - Certificate Transparency
  - X.509
  - RSA-2048
  - ECDSA-P256
  - CNSA 2.0
  - PLANTS
  - X25519MLKEM768
  key_people: []
key_logic_flow:
- 后量子密码学此前聚焦于加密而非认证，但 NSA 的 CNSA 2.0 要求在 2030-2035 年间迁移、NIST 计划 2030 年后弃用 RSA-2048
  和 P-256、Google 宣布 2029 年完成迁移、Cloudflare 跟进承诺，这些时间表将认证紧迫性大幅提前。
- ML-DSA-44 签名约 2420 字节、公钥 1312 字节，替代 Web PKI 现有算法（RSA-2048 签名 256 字节、ECDSA-P256 签名
  64 字节）后单次 TLS 握手将超过 10KB，Cloudflare 的研究显示大量连接会失败、其余变慢。
- Merkle Tree Certificates（MTCs）采用批量签发模式：CA 用一个签名覆盖整批证书，浏览器在 TLS 握手之外更新批量签名（landmarks），常见情况下握手仅包含一条签名、一条公钥和一条包含证明。
- MTCs 将 Certificate Transparency 内建于证书签发本身——证书无法脱离 Merkle 树存在，而 Let's Encrypt 自 2019
  年起已有生产级 Merkle 树日志（CT 日志）的运营经验。
- Let's Encrypt 计划 2026 年底上线 MTC 测试环境、2027 年投入生产，需要改造签发基础设施、ACME 协议、撤销和运营工具以及透明度日志系统。
- 当前证书不受影响，后量子到来时将以免费、自动化、ACME 客户端可用的方式交付，同时建议服务器运维人员立即启用混合后量子密钥交换（X25519MLKEM768）以防范现有流量被记录后解密的风险。
extract_result: success
object_mentions:
- object_type: project
  name: Merkle Tree Certificates (MTCs)
  canonical_name: Merkle Tree Certificates
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Let's Encrypt 计划采用 Merkle Tree Certificates（MTCs）作为后量子 Web PKI 的技术路线，MTCs 将证书批量签发，用一个签名覆盖整批证书。
  - 常见情况下 MTC 握手只携带一条签名、一条公钥和一条包含证明，体积比当前 Web PKI 握手更小。
  - Cloudflare 和 Chrome 已在真实互联网流量中开展 MTC 可行性实验，IETF PLANTS 工作组正在推进标准化。
  article_id: d1f7889f5cffd7ec
- object_type: project
  name: IETF PLANTS working group
  canonical_name: IETF PLANTS
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - The IETF's PLANTS working group is working on standardizing the design of Merkle
    Tree Certificates.
  - Let's Encrypt 已在 IETF PLANTS 和 ACME 工作组中参与标准制定。
  article_id: d1f7889f5cffd7ec
- object_type: project
  name: Let's Encrypt Certificate Transparency logs
  canonical_name: Let's Encrypt Certificate Transparency
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Let's Encrypt 自 2019 年起运营 Certificate Transparency 日志，这些日志是追加型 Merkle 树，MTCs 所使用的核心数据结构与之一致。
  article_id: d1f7889f5cffd7ec
- object_type: paper
  name: RFC 9881
  canonical_name: RFC 9881
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Let's Encrypt 跟踪 ML-DSA 签名在 X.509 中的标准（RFC 9881）以及在 TLS 中的草案（draft-ietf-tls-mldsa）。
  article_id: d1f7889f5cffd7ec
- object_type: project
  name: Go ML-DSA standard library
  canonical_name: Go ML-DSA
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Go 1.27 在标准库中新增 ML-DSA（NIST 标准化后量子签名方案），表明后量子签名正在成为实际可用的基础设施。
  - Web PKI 向后量子安全的过渡需要 ML-DSA 在浏览器、库和 ACME 客户端中落地。
  article_id: d1f7889f5cffd7ec
- object_type: project
  name: X25519MLKEM768
  canonical_name: X25519MLKEM768
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Let's Encrypt 建议服务器运维人员立即启用混合后量子密钥交换 X25519MLKEM768，因为任何没有后量子密钥交换的 TLS 连接都可能在将来被解密。
  article_id: d1f7889f5cffd7ec
impact_score:
  score: 7.5
  reason: Let's Encrypt 作为全球最大的证书颁发机构（服务超过 5 亿网站），其对 MTC 路线的公开承诺具有极强的行业牵引力。MTC 解决了一个真实的工程危机——后量子签名（ML-DSA-44
    约 2420 字节）直接替换会导致 TLS 握手超过 10KB，在现实网络中造成大范围连接失败（Cloudflare 已证实）。MTC 将认证路径压缩到比当前
    PKI 更小，同时将 Certificate Transparency 内建于签发流程，是一个设计优雅的架构级创新。Google 2029 年迁移承诺、Cloudflare
    同步跟进、Go 1.27 将 ML-DSA 纳入标准库，构成了强大的生态协同。但测试环境要到 2026 年底才上线，2027 年才投产，短期对开发者无直接影响，故给
    7.5 分而非更高。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: ACME 协议变更及现有证书管理流程需要如何适配 MTC 批量签发模式
hype_assessment:
  level: low
  reason: 文章完全符合 Let's Encrypt 一贯务实的技术写作风格。提供了精确的数据对比（RSA-2048 签名 256 字节 vs ML-DSA-44
    约 2420 字节）、具体的握手大小分析（超过 10KB）、明确的时间表（2026 年底测试、2027 年生产），以及标准化进展（IETF PLANTS、ACME
    working groups）。没有使用任何空泛的营销词汇，而是坦诚地描述了工程挑战（'This is not a small endeavor'）。
information_entropy: high
domain_disruption:
  technical_innovation: Merkle Tree Certificates 的批量签发机制是 Web PKI 近 20 年来最重大的架构创新：CA
    一批次签发多个证书，用一个后量子签名覆盖整批，浏览器通过独立于 TLS 握手的信道获取批次签名（landmark），使得认证路径压缩为单签名+单公钥+包含证明，比当前
    PKI 握手更小。同时将 Certificate Transparency 从后置附加内建为签发过程的固有属性——证书无法脱离 Merkle 树独立存在，消除了传统
    CT 日志签名冗余和日志作弊风险。
  business_model: Let's Encrypt 保持免费 CA 模式，但 MTC 从架构上解决了后量子时代大规模证书签发的成本瓶颈（单签覆盖整批显著降低计算和带宽成本）。这巩固了其作为公共互联网基础设施提供者的定位，同时给商业
    CA（DigiCert、Sectigo 等）带来巨大的技术路线跟随压力——若 MTC 成为 IETF 标准并被 Chrome 强制要求，商业 CA 将被迫重构其签发和透明日志基础设施。CA
    行业运营模式从'独立签发+事后透明日志'转向'批量签发+内建透明'。
engineering_complexity: prototype
compound_value:
  score: 8.5
  reason: 'Let''s Encrypt 作为全球最大的证书颁发机构（服务3亿+网站），其宣布采用 Merkle Tree Certificates（MTC）路线，标志着后量子
    Web PKI 的标准化路径已基本收敛。核心投资逻辑如下：


    【规模效应与网络效应】MTC 是一种协议级创新，一旦在 Let''s Encrypt 的规模上部署，将迫使浏览器、服务器软件、CDN 等全栈适配同一标准。内置
    Certificate Transparency 意味着证书无法脱离 Merkle 树存在，形成天然技术锁定。3亿+网站的迁移本身就是最强的 adoption
    force。


    【成本结构逆转】后量子签名（ML-DSA-44 ~2.4KB）相比当前 RSA-2048（256B）体积大 10 倍，这是后量子 PKI 最大的采用障碍。MTC
    的批量签发机制将握手认证路径压缩至『1个签名+1个公钥+1个包含证明』，比当前 PKI 更小。这本质上是『安全升级同时性能提升』的罕见组合，极大降低了部署阻力。


    【生态协同确定性强】Google（2029 年完成迁移）、Cloudflare（同步承诺）、Chrome（已声明 MTC 为首选路径）、Go 1.27（ML-DSA
    进标准库）形成了从浏览器→CDN→运行时→CA 的全链路生态共识。2026 年底测试环境+2027 年生产的时间表可信。


    【风险考量】IETF PLANTS 标准化尚未完成；Let''s Encrypt 作为非营利组织，直接商业回报有限，但基础设施价值不可替代；实施复杂度高（涉及
    ACME 协议改造、吊销系统、透明度日志等全栈变更）。


    综合评分 8.5：未来 3-5 年互联网安全基石的确定性极高，MTC 一旦标准化部署，将成为后量子时代的 Web PKI 基础设施，复利效应体现在协议级锁定+生态级协同+性能优势三重叠加。'
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Let's Encrypt
- Cloudflare
- Google
- Internet Society
competitive_casualty:
- 商业证书颁发机构（付费 CA）
- 非标准化后量子 PKI 方案
- 滞后迁移的传统 CDN 服务商
market_opportunities:
- PKI基础设施服务商可围绕MTC批量签发流程开发企业级迁移工具，帮助组织从传统X.509证书体系平滑过渡到后量子认证架构
- CDN和云服务商可提前布局MTC兼容的TLS加速方案，利用MTC握手的认证路径压缩优势提升网络性能并作为差异化卖点
- 面向IoT和嵌入式设备的安全团队可探索MTC的轻量级变体应用场景，利用其内建透明度日志特性解决海量设备证书管理难题
risk_matrix:
  regulatory: CNSA 2.0、NIST过渡指南和欧盟路线图均设定2030-2035年后量子迁移时间表，虽然不直接约束公共Web PKI，但供应链上下游（浏览器、操作系统、硬件厂商）的合规压力将逐级传导，延迟适配可能导致审计不合规或商业合同违约
  technological: MTC仍处于IETF PLANTS工作组标准化阶段（2026年），若标准化过程中出现重大设计变更或竞争性方案（如传统X.509压缩变体）获得更多支持，早期投入可能面临重新实现的风险
  competitive: Cloudflare和Google已启动面向真实互联网流量的MTC可行性实验，Chrome明确将MTC作为首选路线；Let's Encrypt计划2026年底上线测试环境，中小型CA若未同步跟进可能被生态边缘化
  ethical: 无
  additional:
  - MTC迁移需要全栈改造（签发基础设施、ACME协议、撤销机制、透明度日志），对依赖老旧PKI系统的组织构成沉重的技术和财务负担，可能加剧安全鸿沟
  - MTC的批量签发模式改变了证书生命周期管理范式，现有的监控、审计和应急响应流程需要重新设计，过渡期内可能出现操作事故或安全盲区
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Merkle Tree Certificates (MTCs)
  canonical_name: Merkle Tree Certificates
  url: null
  positioning: Let's Encrypt 选定的后量子 Web PKI 技术路线，基于 Merkle 树批量签发机制将 TLS 握手压缩至比当前方案更小的体积。
  technical_signal: MTCs 将证书批量签发，用一个签名覆盖整批证书，常见情况下握手仅携带一条签名、一条公钥和一条包含证明。
  adoption_signal: Cloudflare 和 Chrome 已在真实互联网流量中开展 MTC 可行性实验，IETF PLANTS 工作组正在推进标准化。
  ecosystem_relevance: Let's Encrypt 自 2019 年起已运营生产级的 Merkle 树 CT 日志，可直接复用于 MTC 基础设施。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Let's Encrypt 计划 2026 年底上线 MTC 测试环境、2027 年投入生产，Chrome 已将其列为后量子证书首选路径，一旦落地将彻底变革
    Web PKI 认证体系。
  risk_notes:
  - MTC 需要改造 Let's Encrypt 签发基础设施、ACME 协议和运营工具，工程复杂度极高。
  - MTC 作为全新证书体系，浏览器和服务器等客户端广泛采用需要数年时间才能完成生态迁移。
  score: 8.0
  article_ids:
  - d1f7889f5cffd7ec
  evidence_snippets:
  - Let's Encrypt 计划采用 Merkle Tree Certificates（MTCs）作为后量子 Web PKI 的技术路线，MTCs 将证书批量签发，用一个签名覆盖整批证书。
  - 常见情况下 MTC 握手只携带一条签名、一条公钥和一条包含证明，体积比当前 Web PKI 握手更小。
  - Cloudflare 和 Chrome 已在真实互联网流量中开展 MTC 可行性实验，IETF PLANTS 工作组正在推进标准化。
- object_type: project
  name: X25519MLKEM768
  canonical_name: X25519MLKEM768
  url: null
  positioning: 混合后量子密钥交换协议，结合 X25519 椭圆曲线与 ML-KEM 后量子密钥封装机制，保护 TLS 连接免受未来量子计算机解密威胁。
  technical_signal: X25519MLKEM768 将经典椭圆曲线密钥交换与 ML-KEM 后量子密钥封装结合，是目前 Web 生态广泛推荐的混合后量子密钥交换方案。
  adoption_signal: Let's Encrypt 建议服务器运维人员立即启用 X25519MLKEM768，防范现有 TLS 流量被记录后将来解密的存储即解密风险。
  ecosystem_relevance: 混合密钥交换是后量子迁移的第一步，X25519MLKEM768 已被主流浏览器和 TLS 库支持，是目前最成熟的过渡方案。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: X25519MLKEM768 是防范存储即解密攻击的关键措施，Let's Encrypt 的明确推荐将加速 Web 服务器大规模采用混合后量子密钥交换。
  risk_notes:
  - X25519MLKEM768 仅是密钥交换层面的后量子化，TLS 认证层面仍需等待 MTC 等方案落地才能完成全面后量子迁移。
  score: 5.0
  article_ids:
  - d1f7889f5cffd7ec
  evidence_snippets:
  - Let's Encrypt 建议服务器运维人员立即启用混合后量子密钥交换 X25519MLKEM768，因为任何没有后量子密钥交换的 TLS 连接都可能在将来被解密。
---

Let’s Encrypt is committed to a post-quantum-safe Web PKI. The path we’re planning to take is Merkle Tree Certificates (“MTCs”), a new approach that adds post-quantum authentication to the web without sacrificing the speed and reliability that have made TLS universal.

This post is about these plans and why we believe MTCs are worth pursuing as a key to a post-quantum future.

For much of the last several years, the conversation about post-quantum cryptography has been a conversation about encryption. The reasoning was straightforward: an attacker who records encrypted traffic today might be able to decrypt it years from now once quantum computers can break the underlying math. Authentication, the part of TLS that indicates a server is who it says it is, has been a less urgent problem. A quantum computer needs to forge a signature in real time, not retroactively, so threats to authentication hinge on the existence of a cryptographically relevant quantum computer (CRQC).

That comfort has been eroding for a while. In the United States, the NSA’s CNSA 2.0 suite has directed national security systems toward post-quantum algorithms on a 2030-to-2035 schedule since 2022, and NIST’s draft transition guidance would deprecate RSA-2048 and P-256 after 2030 and disallow them after 2035. The European Union’s roadmap targets high-risk systems by the end of 2030 and broad migration by 2035. These mandates don’t bind the public Web PKI directly, but they set the end-of-decade timeline that the vendors, libraries, and standards bodies it relies on are already working toward.

This year, the timeline shortened further. Google announced that it would migrate its services by 2029, citing tightening estimates for the potential arrival of a CRQC. Cloudflare followed with a parallel commitment. In addition, Go 1.27 adds ML-DSA, a NIST-standardized post-quantum signature scheme, to the standard library, a sign that post-quantum signatures are becoming practical infrastructure.

Post-quantum authentication is no longer a problem the Web PKI ecosystem should defer. Long-lived keys (root certificate authorities, code-signing keys, identity systems) are particularly valuable targets, and new technology takes years to gain broad adoption, so the work has to start early.

The Web PKI is one of the trickiest places to deploy post-quantum signatures. The reason is size.

ML-DSA-44, one of the smaller NIST standardized post-quantum signature schemes, has a signature roughly 2,420 bytes long. The algorithms used in the Web PKI today are much smaller. RSA-2048 signatures are 256 bytes and ECDSA-P256 signatures are 64 bytes. Public keys are bigger as well: 1,312 bytes for ML-DSA-44, 256 bytes for RSA-2048, and 64 bytes for ECDSA-P256. A typical Web PKI handshake today carries five signatures and two public keys. Replacing those with ML-DSA equivalents would push a single TLS handshake well past 10 kilobytes. Cloudflare’s research has shown that, at that scale, a meaningful share of TLS connections fail on real-world networks, and the rest get slower.

Larger handshakes would affect every TLS connection, not just those that would fail. They would mean constrained bandwidth, slower connections, and a worse experience for users, all in exchange for security against a threat that hasn’t materialized yet. That’s a steep cost to enable by default, and defaults are what actually move security at web scale.

A different design called Merkle Tree Certificates (“MTCs”) has been emerging over the past year, and we believe it is a strong path forward for the post-quantum Web PKI.

Instead of issuing certificates one at a time and signing each one individually, an MTC certificate authority issues certificates in batches, with a single signature covering the entire batch. Browsers stay up to date on those batch signatures (called “landmarks”) separately from the TLS handshake.

In the common case, the entire authentication path in an MTC handshake is one signature, one public key, and one inclusion proof. That’s smaller than today’s Web PKI handshake, even though MTCs use post-quantum algorithms. The other case is the “standalone” form. It uses slightly larger handshakes as a fallback when a client’s landmark is out of date.

There is more to MTCs than size optimization. Because every certificate is part of a published Merkle tree, transparency becomes a property of issuance itself. Today’s Certificate Transparency ecosystem is bolted on after the fact: certificates are issued by CAs, then logged separately, with extra signatures riding along in the TLS handshake to attest to that logging. With MTCs, a certificate cannot exist outside the Merkle tree. Certificate Transparency is built in.

This is not entirely new ground for us. Let’s Encrypt has operated Certificate Transparency logs since 2019. Those logs are append-only Merkle trees, the same core data structure MTCs are built on, and ones we have run in production, at scale, for years.

Cloudflare and Chrome are already running a feasibility experiment with MTCs against real internet traffic. The IETF’s PLANTS working group is working on standardizing the design. Chrome has announced that MTCs are its preferred path for adding post-quantum certificates to the public web.

We are planning to support Merkle Tree Certificates as the path forward for the post-quantum Web PKI. We are targeting late 2026 for a staging environment that issues MTCs, and 2027 for a production-ready environment.

This is not a small endeavor. Issuing MTCs at the scale of Let’s Encrypt requires meaningful changes throughout our stack: in our issuance infrastructure, in the ACME protocol our subscribers use to obtain certificates, in revocation and operational tooling, and in the transparency-log infrastructure that MTCs subsume. We have been participating in the IETF PLANTS and ACME working groups as the standards take shape.

Alongside the MTC work, we are tracking the standards for ML-DSA signatures in X.509 (RFC 9881) and TLS (draft-ietf-tls-mldsa), and the ecosystem work this depends on, like the addition of ML-DSA to the Go standard library. The Web PKI’s transition to post-quantum security needs all of this to land in browsers, libraries, and ACME clients, whether the certificates ultimately delivered are MTCs or ML-DSA signed X.509.

Nothing changes today. Your current Let’s Encrypt certificates will continue to be issued and renewed exactly as they always have been. When post-quantum certificates become available from Let’s Encrypt, they will arrive the way our service always has: free, automated, and available to anyone with an ACME client.

The transition will take time. There are standards still being finalized, root programs still defining their requirements, and engineering work that has to land in the broader ecosystem (browsers, libraries, ACME clients) before any of this matters at scale. We will keep the community informed as the work progresses and as the timelines firm up.

If you maintain an ACME client or run an ACME-driven certificate pipeline, this is a good moment to start tracking the work in the PLANTS working group and the discussions on the mtcs@chromium.org mailing list. Some of the changes coming will require client-side support, and the ecosystem will benefit from clients that are ready when the issuance side is.

For the broader internet community: post-quantum encryption is the more urgent problem, because any TLS connection without post-quantum key exchange is potentially harvestable for later decryption. If you operate servers, please ensure they support hybrid post-quantum key exchange (X25519MLKEM768). Major browsers and operating systems already do, and turning it on at the server is one of the highest-leverage things you can do this year.

We have been building infrastructure for the public web since 2013 on the principle that security should be available to everyone, automatically, at no cost. The quantum transition is a generational change in how that security works under the hood.