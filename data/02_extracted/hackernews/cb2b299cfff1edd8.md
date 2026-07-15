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