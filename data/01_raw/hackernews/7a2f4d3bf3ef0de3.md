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
pipeline_stage: ingested
id: 7a2f4d3bf3ef0de3
manifest_dates:
- '2026-07-08'
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