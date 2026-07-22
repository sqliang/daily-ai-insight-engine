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