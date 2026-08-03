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
impact_score:
  score: 5.5
  reason: 该事件是 CERT/CC 公开披露的 Tenda 多款固件隐藏后门漏洞（CVE-2026-11405），属于重大网络安全事件但并非 AI 行业核心事件。从
    AI 技术架构师视角看，影响力体现在三方面：其一，AI 训练和推理依赖的网络基础设施（路由器/交换机）存在可被完全控制的后门，攻击者可篡改网络配置、禁用安全功能，对部署
    AI 系统的边缘侧网络构成直接威胁；其二，该漏洞无需用户名、密码明文比对、不显示于管理界面，利用门槛极低，影响面覆盖 FH1201 等多款产品线且无补丁可用；其三，CERT/CC
    无法联系到厂商进行协调，意味着大量已部署设备将长期暴露在风险中。但局限在于：这是一款特定厂商的固件漏洞，未涉及 AI 模型、训练框架或推理引擎本身，属于 AI
    产业链的外围安全事件而非范式转移。综合评分 5.5。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: login() 函数中通过 GetValue('sys.rzadmin.password') 读取明文密码做 strcmp 比对的机制疑似故意留出的后门，而非无意的代码缺陷
hype_assessment:
  level: low
  reason: CERT/CC 发布的漏洞通告严格遵循 CVE 披露规范，语言客观克制，全文未使用任何'颠覆'、'革命性'等 PR 式表述。具体技术细节（函数名
    GetValue、strcmp 比对、role=2 赋权、login() 代码路径）完备且可复现，影响版本号精确到固件构建号。没有出现炒作或概念包装。
information_entropy: high
domain_disruption:
  technical_innovation: 漏洞本身不涉及新颖的攻击技术（经典的硬编码后门密码比对模式），但其在主流厂商固件中被发现且涉及多种产品线，揭示了物联网/消费级网络设备在认证机制安全审计上的系统性缺失，对
    IoT 设备供应链安全审查标准有警示意义
  business_model: 后门漏洞曝光且厂商失联无补丁的局面，可能加速各国对网络设备安全合规的立法和采购审查趋严（如美国 BIS、欧盟 Cyber Resilience
    Act），对 Tenda 品牌信誉和全球市场渠道构成实质性冲击，也可能推动企业客户重新评估消费级网络设备在办公网络中的使用策略
engineering_complexity: prototype
compound_value:
  score: 2.0
  reason: 该事件为消费级路由器固件（Tenda）中的隐藏认证后门漏洞披露（CVE-2026-11405），属于负面安全事件而非正向技术积累。从VC资本视角看，单一消费品牌的后门漏洞不具备长期复利效应——它不是一项可扩展的技术资产，而是暴露了消费级IoT供应链安全的系统性信任风险。虽然该事件可能在边际上推动企业网络安全预算向高端/企业级方案倾斜，但市场涟漪范围有限，不足以构成独立的复利投资主题。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- Cisco
- Ubiquiti
- Palo Alto Networks
- Fortinet
competitive_casualty:
- Tenda
- TP-Link
- D-Link
- 低端消费路由器厂商
market_opportunities:
- 物联网设备安全审计服务需求激增，可针对消费级路由器/交换机固件开展后门检测与渗透测试，为企业和家庭用户提供安全评估报告
- 开源固件替代方案（如OpenWrt、DD-WRT）的定制化部署与长期维护服务迎来商机，帮助用户规避厂商后门风险
- 网络异常行为检测工具可开发针对已植入后门设备的流量指纹识别模块，服务于企业内网IoT资产安全管理
risk_matrix:
  regulatory: Tenda可能面临多国监管处罚（FCC、欧盟《网络韧性法案》），且CERT/CC无法联系厂商协调漏洞，暴露出严重的合规治理缺陷，可能触发进口限制或销售禁令
  technological: 后门存在于固件层，无官方补丁可用，受影响的设备型号（FH1201、W15E、AC10、AC5、AC6等）将永久处于可被完全接管的风险中，且用户无法自行修复
  competitive: 此事件严重损害Tenda品牌信誉，TP-Link、Netgear、华硕等竞争对手可借机抢占市场份额；同时可能引发连锁效应，消费者对其他低端路由器的固件安全性产生普遍质疑
  ethical: 后门机制完全不验证用户名，任意用户配合配置中的明文密码即可获得role=2管理员权限，攻击者可窃取家庭/企业的网络流量、植入恶意固件、将设备纳入僵尸网络，严重侵犯用户隐私与数据安全
  additional:
  - 供应链安全风险：预装后门的设备在出厂时就埋下隐患，终端用户完全无法感知，集体诉讼风险上升
  - 物联网僵尸网络扩大化风险：参考Mirai攻击路径，此漏洞可能被大规模自动化利用组建DDoS僵尸网络，影响整个互联网基础设施
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Tenda Router Firmware (multiple versions)
  canonical_name: Tenda Router Firmware
  url: null
  positioning: Tenda 多款路由器固件是面向家庭与中小企业的网络设备嵌入式操作系统，为 FH1201、W15E、AC10 等型号提供 Web 管理界面的认证与配置功能。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 家庭网络用户
  - 中小企业 IT 运维人员
  - 网络设备管理员
  product_signal: /bin/httpd 的 login() 函数中存在隐藏后门认证机制，MD5 验证失败后通过 GetValue() 读取配置中的明文密码进行
    strcmp() 比对，匹配即授予 role=2 管理员权限。
  market_signal: CERT/CC 公开披露 CVE-2026-11405 漏洞后无法联系厂商协调补丁，五款受影响固件版本均无正式修复方案，仅推荐缓解措施降低风险。
  differentiation: 该后门认证机制完全未被文档化且不可见，与正常 MD5 密码验证流程并行存在，攻击者无需提供用户名即可完全绕过身份验证。
  watch_reason: Tenda 路由器固件的隐藏后门漏洞（CVE-2026-11405）暴露了物联网设备供应链安全风险，厂商失联与补丁缺失使大量设备长期处于暴露状态，值得持续跟踪厂商安全回应与行业响应机制演变。
  risk_notes:
  - CERT/CC 无法与厂商取得联系，受影响的五款固件版本均无正式补丁可用。
  - 用户目前仅能通过禁用远程管理和更改默认 LAN IP 等缓解措施降低风险，无法根除漏洞。
  - 攻击者获得网络访问权限后即可利用后门完全接管设备管理界面，进而渗透整个本地网络。
  score: 7.0
  article_ids:
  - 7a2f4d3bf3ef0de3
  evidence_snippets:
  - Tenda 多款路由器固件（FH1201、W15E、AC10、AC5、AC6）的 /bin/httpd 文件中存在隐藏认证后门，攻击者可绕过密码验证获得完全管理员权限。
  - 该后门在正常 MD5 验证失败后读取 sys.rzadmin.password 配置值进行明文对比，匹配后授予 role=2 级别访问权限且不验证用户名。
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