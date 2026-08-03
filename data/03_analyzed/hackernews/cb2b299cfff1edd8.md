---
title: Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory
source: https://mathstodon.xyz/@iblech/116769502749142438
author:
- '[[IngoBlechschmid]]'
published: '2026-07-02'
created: '2026-07-03'
description: 'Article URL: https://mathstodon.xyz/@iblech/116769502749142438 Comments
  URL: https://news.ycombinator.com/item?id=48763035 Points: 465 # Comments: 203'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cb2b299cfff1edd8
manifest_dates:
- '2026-07-03'
source_type: community_discussion
tldr: 开发者 iblech 发现 Linux 内核自 6.9 版起存在一个安全漏洞：LUKS 全盘加密的密钥在系统挂起到 RAM 后未从内存中清除。他通过复活
  Pali Rohár 的旧内核补丁为 NixOS 推出了实验性安全挂起方案，cryptsetup 团队也开发了对应的工作补丁并计划在 2.8.7 版本中发布。
objective_summary: 开发者 iblech 在将 Debian 的 cryptsetup-suspend 移植到 NixOS 时，通过 QEMU 虚拟机内存转储确认
  Linux 内核自 6.9 版本起未在挂起时清除 LUKS 加密密钥，导致密钥在内存中易受冷启动攻击。他复活了 Pali Rohár 从未被合并的内核补丁，为
  NixOS 推出了实验性安全挂起到 RAM 方案。cryptsetup 团队的 Ondrej Kozina 迅速为此开发了绕过内核 bug 的工作补丁，计划在
  cryptsetup 2.8.7 版本中发布。Ondrej 同时发现了 loop 块设备系统中的相关安全问题。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - NixOS
  - Debian
  - Red Hat
  technologies:
  - LUKS
  - QEMU
  - loop block device
  key_people:
  - Pali Rohár
  - Ondrej Kozina
  - iblech
key_logic_flow:
- Linux 内核自 6.9 版本起存在安全漏洞：LUKS 全盘加密密钥在系统挂起到 RAM 后仍驻留内存，未按预期被清除，易受冷启动攻击。
- 开发者 iblech 在将 Debian 的 cryptsetup-suspend 移植到 NixOS 时发现该 bug，通过 QEMU 虚拟机内存转储确认了密钥泄露的事实。
- Pali Rohár 曾提交在挂起时清除 LUKS 加密密钥的内核补丁，但该补丁从未被合并到主线内核中，iblech 的方案复活了该补丁。
- cryptsetup 团队的 Ondrej Kozina 为 cryptsetup 开发了绕过内核 bug 的工作补丁，计划随 cryptsetup 2.8.7
  版本发布。
- Ondrej 在审查补丁时还发现了 loop 块设备系统中的相关安全问题，表明物理块设备和虚拟 loop 设备都受影响。
- iblech 发布的 NixOS 实验性安全挂起方案支持根文件系统加密，并包含集成测试来验证密钥确实被清除。
extract_result: success
object_mentions:
- object_type: project
  name: NixOS experimental secure suspend-to-RAM
  canonical_name: nixos-secure-suspend-ram
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - iblech 发布了一个实验性的 NixOS 安全挂起方案，通过复活 Pali Rohár 的内核补丁来在挂起时清除 LUKS 加密密钥。
  - 该项目支持根文件系统加密，并提供了集成测试来验证密钥是否真正在挂起时被清除。
  - 该方案受 Debian 的 cryptsetup-suspend 启发，但通过内核补丁避免了偶尔阻止系统进入睡眠的竞态条件。
  article_id: cb2b299cfff1edd8
- object_type: project
  name: cryptsetup
  canonical_name: cryptsetup
  url: https://gitlab.com/cryptsetup/cryptsetup
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Ondrej Kozina 为 cryptsetup 开发了绕过内核 bug 的工作补丁，该补丁计划在 cryptsetup 2.8.7 版本中发布。
  - 该补丁对应的合并请求位于 GitLab 上：https://gitlab.com/cryptsetup/cryptsetup/-/merge_requests/937。
  article_id: cb2b299cfff1edd8
- object_type: project
  name: Pali Rohár's kernel patch for LUKS key wiping on suspend
  canonical_name: pali-rohar-luks-suspend-patch
  url: https://lore.kernel.org/linux-pm/1428254419-7334-1-git-send-email-pali.rohar@gmail.com/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Pali Rohár 曾提交过在挂起时清除 LUKS 加密密钥的内核补丁，但该补丁从未被合并到主线内核中。
  - iblech 在审查 cryptsetup 和内核文档后发现已在 /proc/keys 中可见的密钥实际未被清除，随后复活了该补丁。
  article_id: cb2b299cfff1edd8
- object_type: project
  name: FridgeLock
  canonical_name: FridgeLock
  url: https://www.sec.in.tum.de/i20/publications/fridgelock-preventing-data-theft-on-suspended-linux-with-usable-memory-encryption
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - iblech 在讨论中提到未来复活 FridgeLock 项目可能是有意义的，该项目会在挂起前加密大量 RAM 内容。
  article_id: cb2b299cfff1edd8
impact_score:
  score: 5.5
  reason: 该事件揭示了自 Linux 6.9 以来（已存在约两年）LUKS 全盘加密在系统挂起时未擦除内存密钥的安全回归，影响所有使用 LUKS 的 Linux
    发行版。对 AI 行业而言，这主要影响开发者/研究者的笔记本设备安全，但 AI 生产环境（数据中心/训练集群）几乎不依赖 suspend-to-RAM，因此直接冲击有限。真正的行业意义在于：核心加密原语的内核级回归能长期未被发现，反映出关键基础设施代码审查的盲区，对
    AI 领域的安全工程文化有警示价值。Ondrej Kozina 的快速响应和 cryptsetup 2.8.7 修复方案展示了社区修复能力，但该 bug 的存在时间之久令人担忧。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 内核内存管理回归导致 LUKS 加密密钥在挂起后未被擦除，且该漏洞存在超过两年未被发现
hype_assessment:
  level: low
  reason: 该报道为技术社区的真实安全发现，作者通过 QEMU 虚拟机内存转储提供了确凿的实验证据，技术细节详实可复现。完全没有使用 '颠覆'、'革命性'
    等 PR 词汇，而是以工程化的方式描述问题发现、补丁复活和社区协作过程。Ondrej Kozina 额外发现的 loop 设备问题也增强了技术报告的深度和诚实性。
information_entropy: high
domain_disruption:
  technical_innovation: 复活了 Pali Rohár 此前未被合入的内核补丁，在内核层面实现挂起时擦除 LUKS 加密密钥，消除了原有 userspace
    方案（Debian cryptsetup-suspend）的竞态条件问题。Ondrej Kozina 同时发现 loop 块设备也存在类似的密钥泄露路径，揭示了内核密钥管理在虚拟设备场景下的系统性设计缺陷——单行内核补丁仅覆盖物理块设备，对
    loop 设备无效。
  business_model: 无
engineering_complexity: production_ready
compound_value:
  score: 4.0
  reason: 该事件是 Linux 内核与 cryptsetup 工具链的一次安全性修复，解决了自 Linux 6.9 起全盘加密密钥在系统挂起时未被从内存擦除的问题。从
    VC 视角看，这是一次重要的增量安全改进而非市场颠覆性事件：修复增强了 Linux 生态在企业级场景下的安全可信度，维护了开源基础设施的长期价值，但并未创造新的商业模式、市场规模或可投资的商业实体。其复利效应体现在
    Linux 作为云计算和企业 IT 基础设施的信任基础被加固，但这种加固属于'维护护城河'而非'创造新价值'，直接商业回报有限。
value_capture_layer: cloud_platform
moat_impact: democratizes_access
key_beneficiaries:
- Red Hat
- Canonical
- SUSE
- NixOS
competitive_casualty:
- 商业全盘加密软件厂商
- 部分硬件安全模块(HSM)方案
market_opportunities:
- 面向企业 Linux 用户提供挂起状态加密密钥安全审计与加固服务，填补传统全盘加密方案在 suspend-to-RAM 场景下的安全盲区，满足金融、政务等高合规要求行业的需求
- 基于 NixOS secure-suspend 项目的技术路线，可为其他 Linux 发行版（如 Ubuntu、Fedora、Debian）提供定制化的安全挂起适配方案，作为企业安全托管服务的增值模块
- FridgeLock 类内存加密技术（在挂起前加密大部分 RAM 内容）具备产品化潜力，可发展为面向高安全需求场景的 Linux 笔记本物理安全加固软件套件
risk_matrix:
  regulatory: 该漏洞使全盘加密在笔记本挂起状态下形同虚设，可能违反 GDPR 第32条关于数据安全的技术措施要求，对金融（PCI DSS）、医疗（HIPAA）等受监管行业中部署
    Linux 加密笔记本的组织构成合规风险
  technological: Linux 内核密钥环(keyring)设计存在文档说明与实际行为不符的根本缺陷；loop 块设备的类似密钥泄露问题仍未完全修复；该
    bug 从 Linux 6.9 起存在多个内核版本未被发现，反映内核安全审查流程中电源管理场景的测试盲区
  competitive: 无
  ethical: 磁盘加密密钥在挂起期间裸露于内存，使冷启动攻击和 DMA 攻击可轻易绕过全盘加密保护，严重威胁使用 Linux 笔记本的高危人群（记者、人权活动家、企业高管等）的数据隐私安全
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: NixOS experimental secure suspend-to-RAM
  canonical_name: nixos-secure-suspend-ram
  url: null
  positioning: 实验性 NixOS 安全挂起项目，通过复活 Pali Rohár 的内核补丁在系统挂起时清除 LUKS 加密密钥，防止冷启动攻击获取全盘加密密钥，支持根文件系统加密。
  technical_signal: 项目使用内核补丁在挂起时清除 LUKS 加密密钥，并提供了集成测试验证密钥是否真正被清除，同时避免了 cryptsetup-suspend
    的竞态条件。
  adoption_signal: 该项目目前为实验性方案，仅适用于 NixOS 发行版，但理念和工具链可被其他 Linux 发行版借鉴和适配。
  ecosystem_relevance: 该方案直接回应了 Linux 内核自 6.9 版起未在挂起时清除 LUKS 密钥的安全漏洞，影响了所有使用全盘加密的
    Linux 用户。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该实验性项目揭示了 Linux 内核自 6.9 以来存在的全盘加密密钥未在挂起时清除的安全漏洞，其方案和 cryptsetup 工作补丁可能推动上游内核修复，值得跟踪后续影响。
  risk_notes:
  - 该内核补丁仅覆盖物理块设备场景，无法处理虚拟 loop 设备上的加密卷，存在覆盖范围不完整的问题。
  - 该项目尚处实验阶段，仅支持 NixOS 发行版，生产环境部署需要更多验证和测试。
  score: 7.0
  article_ids:
  - cb2b299cfff1edd8
  evidence_snippets:
  - iblech 发布了一个实验性的 NixOS 安全挂起方案，通过复活 Pali Rohár 的内核补丁来在挂起时清除 LUKS 加密密钥。
  - 该项目支持根文件系统加密，并提供了集成测试来验证密钥是否真正在挂起时被清除。
  - 该方案受 Debian 的 cryptsetup-suspend 启发，但通过内核补丁避免了偶尔阻止系统进入睡眠的竞态条件。
- object_type: project
  name: cryptsetup
  canonical_name: cryptsetup
  url: https://gitlab.com/cryptsetup/cryptsetup
  positioning: cryptsetup 是 Linux 全盘加密的标准工具套件，负责管理 LUKS 加密卷，正在针对内核 6.9+ 的密钥清除漏洞开发工作补丁并计划在
    2.8.7 版本中发布。
  technical_signal: cryptsetup 团队为 cryptsetup 开发了绕过内核 bug 的工作补丁，通过用户空间手段在不修改内核的情况下保护加密密钥。
  adoption_signal: cryptsetup 是 Linux 生态中事实上的全盘加密标准工具，被几乎所有主流 Linux 发行版采用和依赖。
  ecosystem_relevance: 作为 Linux dm-crypt 的用户空间管理工具，cryptsetup 对内核 bug 的快速响应能力直接影响全
    Linux 生态系统的数据安全防线。
  target_users: []
  product_signal: cryptsetup 团队为 cryptsetup 开发了绕过内核 bug 的工作补丁，计划随 2.8.7 版本发布，在不修改内核的情况下保护加密密钥。
  market_signal: 作为 Linux 生态中最广泛使用的全盘加密工具，cryptsetup 2.8.7 的修补将影响所有采用 LUKS 加密的 Linux
    发行版和用户。
  differentiation: cryptsetup 是 Linux 内核 dm-crypt 的用户空间管理工具，其对内核 bug 的快速响应体现了在加密存储生态系统中的关键桥梁角色。
  watch_reason: cryptsetup 2.8.7 将引入对内核关键安全漏洞的工作补丁，作为 Linux 全盘加密的标准工具，其版本更新将直接影响各发行版的安全策略和用户数据保护能力。
  risk_notes:
  - 该工作补丁仅绕过内核 bug 而非根本修复，真正的修复需要上游内核社区的配合和补丁合并。
  - Ondrej Kozina 还发现 loop 块设备存在相关安全问题，物理和虚拟设备均受影响，问题范围比预想更大。
  score: 8.0
  article_ids:
  - cb2b299cfff1edd8
  evidence_snippets:
  - Ondrej Kozina 为 cryptsetup 开发了绕过内核 bug 的工作补丁，该补丁计划在 cryptsetup 2.8.7 版本中发布。
  - 该补丁对应的合并请求位于 GitLab 上：https://gitlab.com/cryptsetup/cryptsetup/-/merge_requests/937。
- object_type: project
  name: Pali Rohár's kernel patch for LUKS key wiping on suspend
  canonical_name: pali-rohar-luks-suspend-patch
  url: https://lore.kernel.org/linux-pm/1428254419-7334-1-git-send-email-pali.rohar@gmail.com/
  positioning: 这是 Pali Rohár 提交的 Linux 内核补丁，旨在清除挂起时内存中的 LUKS 加密密钥以防止冷启动攻击，但从未被主线内核合并。
  technical_signal: 该补丁通过在内核挂起路径中主动清除 LUKS 卷密钥来防止密钥驻留内存，但仅覆盖了物理块设备场景。
  adoption_signal: 该补丁从未被主线内核合并，只在 NixOS 实验性项目中被复活使用，缺乏上游社区的广泛采用。
  ecosystem_relevance: 该补丁的长期未合状态凸显了 Linux 内核安全审查流程的一个缺口：全盘加密在挂起到 RAM 时的密钥保护没有得到充分重视。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该补丁代表了已知未修复的内核安全漏洞，被 NixOS 项目复活和 cryptsetup 团队跟进后，可能推动上游内核正式接纳这一安全改进，值得关注后续进展。
  risk_notes:
  - 该补丁仅覆盖物理块设备，对 loop 虚拟设备无效，Ondrej Kozina 已发现额外相关安全问题。
  - 该补丁已存在多年未被合并，上游内核社区的态度和合并意愿存在较大不确定性。
  score: 6.0
  article_ids:
  - cb2b299cfff1edd8
  evidence_snippets:
  - Pali Rohár 曾提交过在挂起时清除 LUKS 加密密钥的内核补丁，但该补丁从未被合并到主线内核中。
  - iblech 在审查 cryptsetup 和内核文档后发现已在 /proc/keys 中可见的密钥实际未被清除，随后复活了该补丁。
---

@nixos_org @leah @identical9213 Announcing experimental secure suspend-to-RAM for NixOS

Normally (and somewhat embarrassingly, considering that it's the 21st century), full-disk encryption gives you no protection while your laptop is suspended: the keys sit in memory, susceptible to cold boot attacks and other ways of exfiltrating your RAM.

This project fixes this, by resurrecting an old kernel patch by Pali Rohár to wipe the LUKS encryption keys on suspend. Inspired by Debian's cryptsetup-suspend, but, thanks to the kernel patch, without the (harmless but) inconvenient race condition which sometimes blocks the laptop from going to sleep, and with a couple of extra precautions.

Fully supports the root filesystem being encrypted. Integration test available.

Enjoy; bug reports are welcome!

Both the kernel patch and the userspace tooling around it could be adapted to other Linux distributions.

A quick follow-up to this key wiping bug:

Ondrej Kozina from the cryptsetup team was very quick to pick this up. Ondrej has developed a patch for cryptsetup which works around the kernel bug, which is scheduled to land in the upcoming 2.8.7 release: https://gitlab.com/cryptsetup/cryptsetup/-/merge_requests/937

Also, while reviewing my proposed kernel patch, Ondrej discovered a related issue in the loop block device system: https://lore.kernel.org/all/ea67ab0e-a039-460e-ab5b-a448995bbd31@redhat.com/

This means in particular that my one-line kernel patch is incomplete. It only covers the common case of having the encrypted volume on a physical block device rather than a virtual loop device.

I really enjoyed these open-source interactions and am grateful for the work of Ondrej and all the others :-)

@jeanas The trail started while tidying up my NixOS port of Debian's cryptsetup-suspend. This port, just like the Debian original, suffered from an inconvenient (but harmless) race condition which would sometimes cause the laptop to not go to sleep. To fix this, I wanted to resurrect a never-merged kernel patch by Pali Rohár (https://lore.kernel.org/linux-pm/1428254419-7334-1-git-send-email-pali.rohar@gmail.com/).

This got me into the source code of cryptsetup and the kernel. Both in the cryptsetup and kernel documentation, it was stated that the keyring would be attached to the calling thread and dropped on thread exit, and yet an entry in /proc/keys (a file which I did not know about before) was visible. This got me suspicious.

Eventually I fired up a virtual machine with QEMU and just dumped its memory to know for sure, and there it was, the supposedly-wiped volume key staring me in the eyes.

@iblech How would re-locking the disk on sleep even work on a laptop thought? It wakes from sleep, the screenlocker shows up, I type my password, and it can't validate it with my actual password because there's no disk access. Any processes which were running now have entirely invalidated file descriptors? Doesn't everything just crash horribly?

@iblech

Is this really desirable, ignoring the unintentional bug of it?

Regarding security, I thought in most systems memory was encrypted/scrambled and anyone concerned with security would require login on wake. Also, cold boot attacks are nearly impossible with modern ram, leaving malicious firmware as a more likely and still vulnerable attack vector. So, if you can't login and there is no path for DMA, what risk is there leaving the key in ram? Is this actually exploitable today?

Regarding the point of suspend, wouldn't this require you to login AND provide the key to reunlock the drive? This seems like an unnecessary extra step for waking from suspendend that might become annoying enough to discourage people from using FDE to begin with.

Maybe I am mistaken on some of these points, but I do not think having to manually unlock the disk after suspend is a good idea.

@xxx Yes, I meant systemctl poweroff. Obviously I cannot speak for you, but I got the impression that many people just put their laptop to sleep (i.e. close the lid), thereby suspending to RAM. That's certainly the case in my local bubble.

I typically use susptend-to-RAM, when i hold the computer in my hand anyway. E.g. when walking from one room to another. Whenever I leave it alone for longer time or transport it in my bag, I use hibernate-to-disk ("systemctl hibernate") to save battery.

Do I understand correctly, that hibernate-to-disk is safe?

@mjg59 Yes, absolutely; sorry, by "canonical software" I meant "the canonical recommendation" (by IT security nerds) not "the most widespread software". Should have been more precise, thank you for the correction :-)

@identical9213 I have now published my solution to this: https://mathstodon.xyz/@iblech/116790453840418444

But don't forget that suspend to RAM will always be a tradeoff. Suspend to encrypted swap is much more secure, but also more inconvenient.

"My" project (almost fully a remix of work by Pali Rohár and Debian's cryptsetup team) just protects the LUKS encryption keys, nothing more.

It might be fun and rewarding to resurrect FridgeLock, which would encrypt substantial parts of the RAM before suspend: https://www.sec.in.tum.de/i20/publications/fridgelock-preventing-data-theft-on-suspended-linux-with-usable-memory-encryption

@nixos_org @leah @identical9213 Announcing experimental secure suspend-to-RAM for NixOS

Normally (and somewhat embarrassingly, considering that it's the 21st century), full-disk encryption gives you no protection while your laptop is suspended: the keys sit in memory, susceptible to cold boot attacks and other ways of exfiltrating your RAM.

This project fixes this, by resurrecting an old kernel patch by Pali Rohár to wipe the LUKS encryption keys on suspend. Inspired by Debian's cryptsetup-suspend, but, thanks to the kernel patch, without the (harmless but) inconvenient race condition which sometimes blocks the laptop from going to sleep, and with a couple of extra precautions.

Fully supports the root filesystem being encrypted. Integration test available.

Enjoy; bug reports are welcome!

Both the kernel patch and the userspace tooling around it could be adapted to other Linux distributions.

@leah Indeed, that is an issue. But for full peace of mind, I want the full system to be encrypted :-) To this end, I use a hacky clone of Debian's cryptsetup-suspend (see https://discourse.nixos.org/t/existing-infrastructure-for-lukssuspend-on-suspend/5559/6) for NixOS (which I plan to release in a less hacky fashion soon).

The basic trick is to create a ramdisk (tmpfs) and put the tool for decryption there, but there are some things to consider to make this work in practice.

@iblech Can you help me understand the threat model here? If your laptop has a lock-on-suspend mechanism (like i3lock or similar), then how would an attacker be able to read the key from memory? If it doesn't, they could just directly access your data anyway.

@fl0_id

Its all worry some. But this is why police are trained to take down suspects without letting them lock or power off the machine.

With a unlocked computer they can do alot, including they can bypass iommu that prevents DMA attacks.

Otherwise they secure the pc, let techies splice in a UPS to the power cord and run cold boot attack in a lab. But i believe its more of a backup methode these days.

@leah @ncf @iblech

@ncf The answer by @leah in this thread is also my answer. The paper "Lest We Remember: Cold Boot Attacks on Encryption Keys" (https://www.usenix.org/legacy/event/sec08/tech/full_papers/halderman/halderman.pdf) is often cited as a reference.

I have used many systems with storage encryption where it’s easy to demonstrate that the media remains unlocked across suspend. If the machine wakes up and is able to access the disk immediately without it being unlocked again, then you know for certain that it was never locked to begin with.

It might be easy for the less technical users to incorrectly assume the machine waking up with a lock screen means the storage had been locked. But with a little bit of effort one can write a script that keeps running behind the lock screen and proves that it is possible to access the disk immediately after waking from suspend. Often the easiest way to prove that the disk was not locked is that when a machine wakes up from suspend you are able to connect to it using an ssh public key without first unlocking the encrypted storage.

Because of this I was a bit surprised by your post suggesting a bug in this feature as none of the storage encryptions I have worked with recently have made no attempt at even providing this protection in the first place. Neither Ubuntu nor Debian does this in the default configuration.

Though it’s easy to demonstrate the lack of this locking feature it’s much harder to prove whether an attempt to do it is actually correct. After waking up from suspend it’s going to be very hard to find out which steps of the process happened before suspending and which happened after waking up.

You may have a log file showing an event happened with a timestamp after waking up, but that log entry could have been produced before suspending and just not having made it through the logging framework until after waking up. And the other way around could also happen if a log entry shows a timestamp from the time you were suspending it could in fact have happened after waking up but before the system clock was adjusted to account for the time passed while suspended.

Because of that it’s extremely easy to miss a bug in which locking the storage happens right after waking up from suspend rather than just before suspending. This difference is invisible to user experience but is critical in terms of security. I think a good approach to allow for verifying the sequencing of events is if the code which wipes the key sends out a network packet after wiping the key just before finally going to sleep. But this is of course only going to be possible if the network stack remains functional that late during the suspend process. This might be easier to implement if that network packet is generated at a lower layer of the network stack rather than relying on the entire stack being functional. I think the code to send kernel console logs to a network interface use a similar low level approach.

@kasperd I agree with everything you wrote, and would suggest booting your system in a virtual machine and dumping its memory to carefully verify whether indeed the key is wiped on suspend or only on resume (which, as you describe, would optically look exactly the same).

The integration test I proposed for NixOS does exactly that. :-)

@iblech @kasperd I'm honestly surprised there wasn't (apparently?) a similar test already in place - "must not leak any keys on disk in plaintext" by reading the whole disk seems like something that should be in place *absolutely everywhere*, since it's the only kind of test that actually verifies it. log leaks are also kinda common in the industry, and it would catch that too.

or is there one somewhere relevant, but it was missing a suspend case with LUKS?

@iblech @kasperd First let me say that post is amazing, I particularly appreciate the links to the code (such a simple struct change with such consequence).

I was also thinking about tests to check regression when a bug is found : ideally this is what we want.

But in the Linux kernel the amount of test would be too big. I feel that it is a fundamental limit of to-big-of-a-monolith software. This is not to blame anyone but to think to build our own software with a more UNIX philosophy.