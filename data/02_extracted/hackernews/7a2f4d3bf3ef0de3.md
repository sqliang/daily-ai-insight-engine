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
tldr: Tenda 多款路由器固件（FH1201、W15E、AC10、AC5、AC6）存在隐藏认证后门漏洞，编号 CVE-2026-11405。攻击者可绕过密码验证直接获得
  Web 管理界面管理员权限，厂商无法联系，目前无可用补丁。
objective_summary: CERT/CC 披露 Tenda 多款路由器固件中存在隐藏认证后门漏洞（CVE-2026-11405）。该漏洞位于 /bin/httpd
  的 login() 函数中，在正常 MD5 密码验证失败后会从设备配置中读取 sys.rzadmin.password 字段值进行明文 strcmp() 比较，匹配成功即授予
  role=2 管理员权限且不验证用户名。受影响固件包括 US_FH1201、US_W15E、US_AC10、US_AC5、US_AC6 等多个型号版本。CERT/CC
  无法联系厂商进行协调，目前无正式补丁，仅建议用户禁用远程管理并更改默认 LAN IP 作为缓解措施。
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
- Tenda 多款路由器固件中存在未 documented 的认证后门漏洞，编号为 CVE-2026-11405。
- 该后门位于 /bin/httpd 二进制文件的 login() 函数中，正常 MD5 密码验证失败后会触发隐藏后门逻辑。
- 后门逻辑通过 GetValue("sys.rzadmin.password") 从设备配置中获取备选密码，并与用户输入进行明文 strcmp() 比较。
- 只要密码匹配，攻击者无需验证用户名即可获得 role=2 级别的完全管理员访问权限。
- 受影响固件包括 US_FH1201、US_W15E、US_AC10、US_AC5、US_AC6 共五个型号的特定版本。
- CERT/CC 无法联系厂商提供补丁，建议用户禁用远程管理功能并更改默认 LAN IP 地址以降低风险。
extract_result: success
object_mentions:
- object_type: product
  name: Tenda Router Firmware (multiple versions)
  canonical_name: Tenda Router Firmware
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Tenda 多款路由器固件（FH1201、W15E、AC10、AC5、AC6）的 /bin/httpd 文件中存在隐藏认证后门，攻击者可绕过密码验证获得完全管理员权限。
  - 该后门在正常 MD5 验证失败后读取 sys.rzadmin.password 配置值进行明文对比，匹配后授予 role=2 级别访问权限且不验证用户名。
  article_id: 7a2f4d3bf3ef0de3
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