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
tldr: Let's Encrypt 宣布采用 Merkle Tree Certificates（MTC）实现后量子 Web PKI，2026 年底上线测试环境。
objective_summary: Let's Encrypt 于 2026 年 6 月 3 日发布公告，计划采用 Merkle Tree Certificates（MTC）作为后量子
  Web PKI 的技术路线。MTC 通过批量签发证书并用单个签名覆盖整个批次，将 TLS 握手中的认证路径压缩为单个签名+公钥+包含证明，比当前
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Let's Encrypt
  - Cloudflare
  - Google
  - Chrome
  - IETF
  - NSA
  - NIST
  technologies:
  - Merkle Tree Certificates (MTCs)
  - ML-DSA
  - ML-DSA-44
  - RSA-2048
  - ECDSA-P256
  - X.509
  - TLS
  - ACME
  - Certificate Transparency
  - Web PKI
  - X25519MLKEM768
  - CNSA 2.0
  - PLANTS
  key_people: []
key_logic_flow:
- Let's Encrypt 宣布将采用 Merkle Tree Certificates（MTC）作为后量子 Web PKI 的技术路线，目标在 2026 年底上线测试环境、2027
  年投入生产。
- 后量子签名（如 ML-DSA-44）体积远大于当前 RSA-2048 和 ECDSA-P256 签名，导致 TLS 握手包超过 10KB，现实网络中会导致连接失败和性能下降。
- MTC 的核心创新是批量签发证书：CA 一批次签发多个证书，用一个签名覆盖整批，浏览器通过独立于 TLS 握手的方式获取批次签名（landmark）。
- 在常见场景下，MTC 握手的认证路径仅包含一个签名、一个公钥和一个包含证明，比当前 PKI 握手更小，同时使用后量子算法。
- MTC 将证书透明度（Certificate Transparency）内建于签发过程本身，证书无法脱离 Merkle 树存在，无需额外的透明度日志签名。
- Google 宣布 2029 年前完成迁移，Cloudflare 同步承诺，Go 1.27 已将 ML-DSA 加入标准库，多方推动后量子认证时间表大幅提前。
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