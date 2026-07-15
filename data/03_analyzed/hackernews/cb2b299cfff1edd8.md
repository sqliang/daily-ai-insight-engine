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
tldr: Linux 6.9 起 LUKS 挂起时未擦除内存加密密钥，已通过内核补丁和 cryptsetup 补丁修复
objective_summary: Joachim Breitner 发现自 Linux 6.9 起，系统挂起时 LUKS 磁盘加密密钥未被从内存中擦除。他复活
  Pali Rohár 的旧内核补丁实现 NixOS 安全挂起；Ondrej Kozina 为 cryptsetup 开发了规避补丁，将在 2.8.
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - NixOS
  - Debian
  technologies:
  - LUKS
  - cryptsetup
  key_people:
  - Joachim Breitner
  - Pali Rohár
  - Ondrej Kozina
key_logic_flow:
- 自 Linux 6.9 起，系统挂起后 LUKS 加密密钥未被从内存中擦除，/proc/keys 中仍可见密钥条目，存在冷启动攻击风险
- Joachim Breitner 在移植 Debian 的 cryptsetup-suspend 到 NixOS 时发现竞态条件问题，通过 QEMU 虚拟机转储内存确认了密钥泄露
- Pali Rohár 曾提交但未被合入的内核补丁被复活，用于在挂起时擦除 LUKS 加密密钥，避免竞态条件并增加额外保护措施
- Ondrej Kozina（cryptsetup 团队）开发了 cryptsetup 的规避补丁，计划在 cryptsetup 2.8.7 中发布
- Ondrej Kozina 还发现 loop 块设备存在类似密钥泄露问题，单行内核补丁仅覆盖物理块设备场景，无法保护虚拟 loop 设备
extract_result: success
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