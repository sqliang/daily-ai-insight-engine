---
title: When str.lower() is a security vulnerability in Python
source: https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability
author:
- '[[rbanffy]]'
published: '2026-08-25'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
description: 'Article URL: https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability
  Comments URL: https://news.ycombinator.com/item?id=49440410 Points: 120 # Comments:
  49'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 9f66add6a4dee5f4
source_type: community_discussion
tldr: Python 的 IDNA 2003 编码在 StringPrep 大小写折叠步骤调用 `str.lower()`，因其使用解释器自带的 Unicode
  版本而非规范要求的 Unicode 3.2.0，导致同一域名编码结果不一致，构成安全漏洞（CVE-2026-17084），已通过补充 Unicode 3.2.0
  例外表修复。
objective_summary: 安全研究员 Seth Michael Larson 在个人博客披露，Python 的 IDNA 2003 实现（`str.encode("idna")`
  与标准库 `stringprep` 模块）在 StringPrep 大小写折叠步骤调用 `str.lower()`，该函数使用解释器内嵌的 Unicode 17.0.0
  数据而非 RFC 3454 要求的 Unicode 3.2.0，导致域名编码结果与规范不一致。例如 `"ᎠᎠ".encode("idna")` 按规范应得到 `xn--58da`，实际却可能得到
  `xn--kz9aa`。修复方案是为行为存在差异的码点建立额外例外表，使 IDNA 2003 与规范一致。该漏洞编号为 CVE-2026-17084，由 Bitshift
  报告，Stan Ulbrych 共同开发修复方案，Marc-Andre Lemburg 与 Petr Viktorin 负责审阅。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Python Software Foundation
  technologies:
  - IDNA 2003
  - IDNA 2008
  - StringPrep
  - NamePrep
  - Unicode 3.2.0
  - CVE-2026-17084
  key_people:
  - Seth Michael Larson
  - Bitshift
  - Stan Ulbrych
  - Marc-Andre Lemburg
  - Petr Viktorin
key_logic_flow:
- 域名国际化依赖 IDNA，其中 IDNA 2003 基于 NamePrep（RFC 3491）与 StringPrep（RFC 3454），其大小写折叠规则需固定为
  Unicode 3.2.0 才能保证跨实现一致。
- Python 通过内置 idna codec（`str.encode("idna")`）支持 IDNA 2003，StringPrep 由标准库 `stringprep`
  模块实现，其中 B.2 表等价于 `str.lower()`，B.3 表为补充例外。
- 漏洞根因是 `str.lower()` 使用解释器自带的 Unicode 数据（当前为 17.0.0），而规范要求 Unicode 3.2.0，导致同一字符串编码结果不一致，例如
  `"ᎠᎠ"` 编码为 `xn--58da`（规范）而非 `xn--kz9aa`（Unicode 17.0.0）。
- 修复方式是遍历所有 Unicode 码点，为 `str.lower()` 行为与 Unicode 3.2.0 不一致的字符生成额外例外表，使 IDNA 2003
  与规范保持一致。
- 该漏洞编号为 CVE-2026-17084，由 Bitshift 报告，Stan Ulbrych 共同开发修复方案，Marc-Andre Lemburg 与 Petr
  Viktorin 负责审阅。
object_mentions:
- object_type: project
  name: stringprep
  canonical_name: CPython stringprep module
  url: https://docs.python.org/3/library/stringprep.html
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 文章说明 Python 标准库中的 `stringprep` 模块实现了 StringPrep 算法，其大小写折叠步骤依赖 `str.lower()`，因
    Unicode 版本差异导致 IDNA 2003 编码与规范不一致。
  article_id: 9f66add6a4dee5f4
- object_type: project
  name: idna
  canonical_name: idna (PyPI package)
  url: https://pypi.org/project/idna/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到 IDNA 2008 由 Python Package Index 上的 `idna` 包支持，并建议一般情况应使用该包而非 Python 内置的
    IDNA 2003 编码。
  article_id: 9f66add6a4dee5f4
extract_result: success
impact_score:
  score: 4.5
  reason: 该事件是 Python 标准库 IDNA 2003 实现的一处真实安全漏洞（CVE-2026-17084）修复：str.lower() 使用解释器内嵌的
    Unicode 17.0.0 而非 RFC 3454 要求的 3.2.0，导致域名编码结果与规范不一致，存在被利用引发域名解析混淆或同形异义攻击的潜在风险；且修复方案严谨（遍历全码点生成例外表）、已合入
    CPython，属于实打实的基础设施安全加固。但影响面相对有限：IDNA 2003 已被 IDNA 2008 取代，现代应用普遍使用独立的 idna 包而非
    str.encode('idna')，且该事件与 AI 行业主线（模型/产品/论文）关联较弱，属于基础设施卫生类披露而非范式级事件。综合判定为中等偏低冲击力，评分
    4.5。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 标准库依赖解释器运行时 Unicode 版本而非规范固定版本所导致的行为漂移隐患
hype_assessment:
  level: low
  reason: 文章为典型的技术安全披露，通篇无'颠覆/革命'等 PR 滥用词汇；提供了根因定位（str.lower() 与 ucd_3_2_0 的差异）、可复现示例（xn--58da
    vs xn--kz9aa）、完整修复思路与 CVE 编号，属于实打实的干货，无包装炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 修复方法为遍历全部 Unicode 码点，逐一对比 str.lower() 在当前 Unicode 17.0.0 与规范要求的
    3.2.0 下的行为差异，为存在差异的码点生成硬编码例外表，使 IDNA 2003 的 StringPrep 大小写折叠与 RFC 3454 严格一致。这体现了一种可复用的安全加固范式：任何依赖带版本数据（Unicode
    表、时区库、证书链等）的算法必须锁定规范指定的数据版本，而非解释器/运行时自带的漂移版本，对标准库实现者具有普适警示意义。
  business_model: 无
engineering_complexity: infrastructure
compound_value:
  score: 2.0
  reason: 投资逻辑推演：此事件本质是 Python 标准库对 IDNA 2003 编码与 Unicode 3.2.0 规范不一致的安全漏洞修复（CVE-2026-17084），根因是
    str.lower() 使用了解释器自带的 Unicode 17.0.0 而非规范要求的 3.2.0。这属于存量基础设施的防腐性维护，而非新资产或新增长曲线的创造。修复消除了同一域名跨
    Unicode 版本编码不一致所导致的安全风险，其价值是防御性的——避免 Python 生态在域名解析、邮件网关、安全校验等场景出现信任折损，但不会带来任何可复利的商业增量或新的现金流。对资本而言，这等同于给地基补裂缝：必须做、值得肯定，但
    3-5 年后不会因此形成新的基础设施壁垒，也无法支撑估值逻辑，故评分处于低分区间。
value_capture_layer: agent_middleware
moat_impact: neutral
key_beneficiaries:
- Python Software Foundation
- Bitshift
competitive_casualty:
- 运行未修复版本的存量 Python 域名处理服务
market_opportunities:
- 安全工具创业者可开发自动检测 `str.encode('idna')` 等 IDNA 2003 调用路径的扫描工具，帮助企业将存量代码迁移至 `idna` 包（IDNA
  2008）并落实修复补丁
- 该漏洞揭示了'运行时 Unicode 数据版本与规范固定版本不一致'这一通用缺陷类别，建议关注国际化域名（IDN）规范化与同形字攻击防护产品的创业机会
- Python 基础设施团队可将该修复模式沉淀为 CI 回归测试，为所有依赖固定 Unicode 版本（如 Unicode 3.2.0）的编码逻辑建立规范一致性校验
risk_matrix:
  regulatory: CVE-2026-17084 已分配编号，涉及邮件服务、URL 解析、域名校验等场景的企业需按漏洞管理流程升级 Python 修复版本，以满足
    SOC 2、ISO 27001 等安全合规要求
  technological: IDNA 2003 已被 IDNA 2008 取代，Python 官方建议改用 `idna` 包；更大的技术风险是 Go、Rust、Node.js
    等其他运行时可能存在同类'Unicode 版本不一致'缺陷，属于系统性隐患
  competitive: 无显著竞争威胁；修复为 CPython 上游开源贡献，反而巩固官方标准库生态，第三方 `idna` 包因兼容性与长期维护获得更强采用地位
  ethical: 该漏洞可被用于同形字（homograph）域名欺骗，扩大钓鱼攻击面；在修复版本普及前，依赖 IDNA 2003 的域名解析存在被定向欺骗的伦理与安全风险
  additional:
  - 供应链升级风险：修复依赖企业升级 Python 版本，可能引入与旧版第三方依赖不兼容的问题，需评估升级窗口
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: stringprep
  canonical_name: CPython stringprep module
  url: https://docs.python.org/3/library/stringprep.html
  positioning: Python 标准库中实现 StringPrep 算法的模块，为 IDNA 2003 等需要字符串预处理的协议提供大小写折叠与字符映射支持。
  technical_signal: 其大小写折叠步骤直接调用 `str.lower()`，而后者使用解释器内嵌的 Unicode 17.0.0 数据，与 RFC
    3454 要求的 Unicode 3.2.0 存在差异，是 CVE-2026-17084 的根因。
  adoption_signal: 作为 Python 标准库模块，`stringprep` 被 `str.encode('idna')` 等内置编码路径依赖，任何使用
    IDNA 2003 的应用都会受到其行为影响。
  ecosystem_relevance: 该模块的安全修复需随 CPython 主版本发布才能覆盖用户，第三方发行版与长期支持版本存在修复时间差，影响生态中的域名编码一致性。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该漏洞揭示了标准库在遵守固定版本规范时的隐性风险，`str.lower()` 依赖解释器 Unicode 版本导致 IDNA 2003
    编码结果不一致，修复方案为补充例外表，值得跟踪其是否完整覆盖所有差异码点及对既有域名解析兼容性的影响。
  risk_notes:
  - 修复仅针对 IDNA 2003 的例外表，若 Unicode 未来版本再次改变大小写规则，仍可能出现新的编码不一致。
  - 标准库模块的修复依赖用户升级 Python 版本，存量部署若不及时更新，域名编码漏洞仍可被利用。
  score: 7.0
  article_ids:
  - 9f66add6a4dee5f4
  evidence_snippets:
  - 文章说明 Python 标准库中的 `stringprep` 模块实现了 StringPrep 算法，其大小写折叠步骤依赖 `str.lower()`，因
    Unicode 版本差异导致 IDNA 2003 编码与规范不一致。
- object_type: project
  name: idna
  canonical_name: idna (PyPI package)
  url: https://pypi.org/project/idna/
  positioning: Python Package Index 上支持 IDNA 2008 的第三方库，是 RFC 5890 系列规范在 Python 生态中的主要实现，被推荐替代内置
    IDNA 2003 编码。
  technical_signal: IDNA 2008 基于 RFC 5890/5891/5892/5893，与基于 StringPrep 的 IDNA 2003
    采用不同的国际化域名处理机制，不依赖 Unicode 3.2.0 大小写折叠表。
  adoption_signal: 文章明确建议一般情况应使用 `idna` 包而非 Python 内置的 IDNA 2003 编码，说明其在生产环境中的推荐地位和广泛采用。
  ecosystem_relevance: 作为 PyPI 上的独立包，`idna` 可独立迭代发布，不受 CPython 版本节奏限制，能更快跟进 IDNA 规范演进与安全修复。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该包是 Python 生态中处理国际化域名的主流选择，文章建议优先使用，其规范实现质量与发布节奏直接关系到大量依赖方，值得持续跟踪其在
    IDNA 规范演进中的适配情况。
  risk_notes:
  - 文章指出仅在需要旧行为时才使用内置 IDNA 2003，若项目仍依赖 `.encode('idna')`，则不受 `idna` 包修复保护。
  - 作为第三方依赖，`idna` 的采用取决于各项目的依赖管理，供应链中断或版本冲突可能影响安全性更新到达速度。
  score: 5.0
  article_ids:
  - 9f66add6a4dee5f4
  evidence_snippets:
  - 文章提到 IDNA 2008 由 Python Package Index 上的 `idna` 包支持，并建议一般情况应使用该包而非 Python 内置的
    IDNA 2003 编码。
---

Some internet standards only support ASCII characters, but the world uses much more than the Latin alphabet. Thus, a mapping from Unicode to ASCII for use in domain names is required.

NamePrep was part of that solution, defined in RFC 3491 as a profile of StringPrep, and is crucially a component of Internationalizing Domain Names in Applications (IDNA), also known as “IDNA 2003”. The StringPrep algorithm is defined in RFC 3454. IDNA 2003 has been obsoleted by IDNA 2008 defined in RFC 5890, 5891, 5892, and 5893.

Python supports IDNA 2003 through the `idna`

codec (`str.encode('idna')`

) and
IDNA 2008 is supported by the `idna`

package on the Python package Index.
Python's implementation of StringPrep is implemented in the `stringprep`

module
in the standard library. In general, you should be using the `idna`

package (IDNA 2008)
and not `.encode("idna")`

(IDNA 2003), but sometimes you
do need the older behavior.

StringPrep defines the “case folding” step (case folding is approximately “how to lowercase/uppercase a codepoint”) in Section 3.2, enabling case-insensitive
comparisons of strings, by mapping all characters through mapping tables B.2 and B.3.
B.2 is effectively `str.lower()`

, lowercasing all characters according to
Unicode rules and B.3 contains the exceptions. The Python code implementing
this (and assuming B.3 table is captured correctly) is the following code below:

```
def map_table_b3(code):
r = b3_exceptions.get(ord(code))
if r is not None: return r
return code.lower()
```


And that might seem fine... and the title probably gave it away already.
The `str.lower()`

call in this function is a vulnerability!

Why? Because `str`

uses whatever Unicode data that the particular Python
interpreter is shipped with, you can figure out what Unicode version your
Python interpreter uses by accessing `unicodedata.unidata_version`

:

```
>>> import unicodedata
>>> unicodedata.unidata_version
'17.0.0'
```


There's also a database of Unicode 3.2.0 data available on every version
of Python (`unicodedata.ucd_3_2_0`

) specifically for the StringPrep and IDNA algorithms:

```
$ grep -I "ucd_3_2_0" -R Lib/
Lib/stringprep.py:from unicodedata import ucd_3_2_0 as unicodedata
Lib/encodings/idna.py:from unicodedata import ucd_3_2_0 as unicodedata
```


This is important! StringPrep depends on this specific version of Unicode
to operate consistently, the B.2 and B.3 tables in RFC 3454 are essentially
Unicode 3.2.0 case-folding rules encoded into
a table. So we need to use Unicode 3.2.0 case-folding rules, not newer
Unicode case-folding rules. This is why calling `str.lower()`

represents
a difference in the implementation and the specification,
and therefore a vulnerability:

```
# RFC 3454 compliant value ('Ꭰ' is U+13A0)
>>> "ᎠᎠ".encode("idna")
'xn--58da'
# Value if using Unicode 17.0.0 case-folding
>>> "ᎠᎠ".encode("idna")
'xn--kz9aa'
```


The fix was to create new exceptions so that `str.lower()`

would behave
as if it was using Unicode 3.2.0 for only particular function. So, we
go through each Unicode codepoint and record when the behavior of
`str.lower()`

is different when comparing the Unicode version shipped with Python and Unicode 3.2.0.
And that's all, now IDNA 2003 is consistent with the specification.

Thanks to Bitshift for reporting the vulnerability, Stan Ulbrych for co-developing the remediation, and Marc-Andre Lemburg and Petr Viktorin for reviewing the remediation. See CVE-2026-17084 for more details.

md5-372ecb8017279e9daff2de5f9c3b41f6


Wow, you made it to the end!


- Share your thoughts with me on Mastodon, email, or Bluesky.
- Browse this blog’s archive of 193 entries.
- Check out this list of cool stuff I found on the internet.
- Follow this blog on RSS or the email newsletter.
- Go outside (best option)