---
title: Tenda firmware (multiple versions) contains hidden authentication backdoor
source: https://kb.cert.org/vuls/id/213560
author:
- '[[miniBill]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'Article URL: https://kb.cert.org/vuls/id/213560 Comments URL: https://news.ycombinator.com/item?id=48825749
  Points: 206 # Comments: 62'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7a2f4d3bf3ef0de3
manifest_dates:
- '2026-07-08'
source_type: community_discussion
tldr: Tenda 多款固件存在隐藏后门认证漏洞（CVE-2026-11405），可绕过密码验证获取管理员权限，目前无补丁。
objective_summary: CERT/CC 披露 Tenda 多款路由器/交换机固件（FH1201、W15E、AC10、AC5、AC6 等）的 /bin/httpd
  中存在未记录的后门认证机制。login() 函数在 MD5 验证失败后通过 GetValue("sys.rzadmin.
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Tenda
  - CERT/CC
  technologies: []
  key_people:
  - Bob Kemerer
key_logic_flow:
- Tenda 多款固件版本（FH1201、W15E、AC10、AC5、AC6 等）存在一个未记录的后门认证漏洞，编号为 CVE-2026-11405。
- 漏洞位于 /bin/httpd 的 login() 函数中：正常 MD5 密码验证失败后，函数调用 GetValue("sys.rzadmin.password")
  读取设备配置中的备用密码，直接通过 strcmp() 明文比对，匹配则授予 role=2 管理员权限。
- 该后门不验证用户名，任意用户名配合后门密码均可获得管理员访问权限，且该机制不在任何管理界面中显示。
- 成功利用后攻击者可获得设备 Web 管理界面的完全管理员权限，可重新配置设备、更改网络设置、禁用安全功能。
- CERT/CC 无法联系到 Tenda 进行漏洞协调，目前无官方补丁可用。
- 缓解措施包括禁用远程管理功能和修改默认 LAN IP 地址。
extract_result: success
---

### Overview

Several versions of Tenda firmware contain an undocumented authentication backdoor that grants administrative access to the devices' web management interfaces. An attacker can expoit this vulnerability, tracked as CVE-2026-11405, to bypass the password verification process and obtain full administrative control without valid credentials.

Affected Versions:

* US_FH1201V1.0BR_V1.2.0.14(408)_EN_TD

* US_W15EV1.0br_V15.11.0.5(1068_1567_841)_EN_TDE

* US_AC10V1.0re_V15.03.06.46_multi_TDE01

* US_AC5V1.0RTL_V15.03.06.48_multi_TDE01

* US_AC6V2.0RTL_V15.03.06.51_multi_T

### Description

Tenda is a supplier of home and business network devices such as routers, switches, wireless access points, and video surveillance equipment. Most of these devices include web-based interfaces that allow users to perform configuration and management operations, which are protected by username/password authentication to prevent unauthorized modifications.

The web server binary `/bin/httpd`

contains an undocumented backdoor authentication mechanism in the `login()`

function. Initially, the function follows a normal authentication path using MD5-based password verification. However, if authentication fails, the function invokes `GetValue("sys.rzadmin.password")`

to retrieve an alternate password value from the device configuration. It then performs a direct `strcmp()`

comparison in plaintext between the user-supplied password and the configuration-stored value. A successful match grants `role=2`

admin-level access and creates a valid session.

The associated username is not validated, so any provided username will succeed when paired with the backdoor password. This backdoor authentication mechanism is not documented or visible through any administrative interface.

### Impact

Successful exploitation grants full administrative access to the device's web interface, regardless of the configured administrator account credentials. With administrative control, an attacker can reconfigure the device, alter network settings, and disable security features, enabling broader compromise of the local network.

### Solution

Unfortunately, we were unable to reach the vendor to coordinate this vulnerability. Since a patch is unavailable, we can only offer mitigation strategies. The following workarounds can help mitigate this vulnerability's impact until a fixed version is released:

**Disable remote management on your device**

If your device supports remote web management, disable it. Disabling this feature prevents attackers on external networks from accessing your device’s administrative dashboard over the internet.

**Restrict local network exposure**

Changing the default LAN IP address may reduce opportunistic discovery by automated scanners that target known default IP ranges. Note that this measure does not prevent deliberate or targeted network scanning.

### Acknowledgements

Thanks to the reporter who wishes to remain anonymous. This document was written by Bob Kemerer.