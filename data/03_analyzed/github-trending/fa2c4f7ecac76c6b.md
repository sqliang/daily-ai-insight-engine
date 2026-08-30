---
title: megadose/holehe
source: https://github.com/megadose/holehe
author: []
published: ''
created: '2026-08-14'
manifest_dates:
- '2026-08-14'
- '2026-08-15'
- '2026-08-16'
description: 'holehe allows you to check if the mail is used on different sites like
  twitter, instagram and will retrieve information on sites with the forgotten password
  function.Holehe OSINT - Email to Registered Accounts 👋 Hi there! For any professional
  inquiries or collaborations, please reach out to me at: megadose@protonmail.com
  📧 Preferably, use your professional email for correspondence. Let''s keep it short
  and sweet, and all in English! Holehe Online Version Summary Efficiently finding
  registered accounts from emails. Holehe checks if an email is attached to an account
  on sites like twitter, instagram, imgur and more than 120 others. Retrieves information
  using the forgotten password function. Does not alert the target email. Runs on
  Python 3. 🛠️ Installation With PyPI pip3 install holehe With Github git clone https://github.com/megadose/holehe.git
  cd holehe/ python3 setup.py install With Docker docker build . -t my-holehe-image
  docker run my-holehe-image holehe test@gmail.com Quick Start Holehe can be run from
  the CLI and rapidly embedded within existing python applications. 📚 CLI Example
  holehe test@gmail.com 📈 Python Example import trio import httpx from holehe.modules.social_media.snapchat
  import snapchat async def main(): email = "test@gmail.com" out = [] client = httpx.AsyncClient()
  await snapchat(email, client, out) print(out) await client.aclose() trio.run(main)
  Module Output For each module, data is returned in a standard dictionary with the
  following json-equivalent format : { "name": "example", "rateLimit": false, "exists":
  true, "emailrecovery": "ex****e@gmail.com", "phoneNumber": "0*******78", "others":
  null } rateLitmit : Lets you know if you''ve been rate-limited. exists : If an account
  exists for the email on that service. emailrecovery : Sometimes partially obfuscated
  recovery emails are returned. phoneNumber : Sometimes partially obfuscated recovery
  phone numbers are returned. others : Any extra info. Rate limit? Change your IP.
  Maltego Transform : Holehe Maltego Thank you to : navlys Chris socialscan UhOh365
  soxoj mxrch (and for the logo) novitae Donations For BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ
  📝 License GNU General Public License v3.0 Built for educational purposes only. Modules
  Name Domain Method Frequent Rate Limit aboutme about.me register ✘ adobe adobe.com
  password recovery ✘ amazon amazon.com login ✘ amocrm amocrm.com register ✘ anydo
  any.do login ✔ archive archive.org register ✘ armurerieauxerre armurerie-auxerre.com
  register ✘ atlassian atlassian.com register ✘ axonaut axonaut.com register ✘ babeshows
  babeshows.co.uk register ✘ badeggsonline badeggsonline.com register ✘ biosmods bios-mods.com
  register ✘ biotechnologyforums biotechnologyforums.com register ✘ bitmoji bitmoji.com
  login ✘ blablacar blablacar.com register ✔ blackworldforum blackworldforum.com register
  ✔ blip blip.fm register ✔ blitzortung forum.blitzortung.org register ✘ bluegrassrivals
  bluegrassrivals.com register ✘ bodybuilding bodybuilding.com register ✘ buymeacoffee
  buymeacoffee.com register ✔ cambridgemt discussion.cambridge-mt.com register ✘ caringbridge
  caringbridge.org register ✘ chinaphonearena chinaphonearena.com register ✘ clashfarmer
  clashfarmer.com register ✔ codecademy codecademy.com register ✔ codeigniter forum.codeigniter.com
  register ✘ codepen codepen.io register ✘ coroflot coroflot.com register ✘ cpaelites
  cpaelites.com register ✘ cpahero cpahero.com register ✘ cracked_to cracked.to register
  ✔ crevado crevado.com register ✔ deliveroo deliveroo.com register ✔ demonforums
  demonforums.net register ✔ devrant devrant.com register ✘ diigo diigo.com register
  ✘ discord discord.com register ✘ docker docker.com register ✘ dominosfr dominos.fr
  register ✔ ebay ebay.com login ✔ ello ello.co register ✘ envato envato.com register
  ✘ eventbrite eventbrite.com login ✘ evernote evernote.com login ✘ fanpop fanpop.com
  register ✘ firefox firefox.com register ✘ flickr flickr.com login ✘ freelancer freelancer.com
  register ✘ freiberg drachenhort.user.stunet.tu-freiberg.de register ✘ garmin garmin.com
  register ✔ github github.com register ✘ google google.com register ✔ gravatar gravatar.com
  other ✘ hubspot hubspot.com login ✘ imgur imgur.com register ✔ insightly insightly.com
  login ✘ instagram instagram.com register ✔ issuu issuu.com register ✘ koditv forum.kodi.tv
  register ✘ komoot komoot.com register ✔ laposte laposte.fr register ✘ lastfm last.fm
  register ✘ lastpass lastpass.com register ✘ mail_ru mail.ru password recovery ✘
  mybb community.mybb.com register ✘ myspace myspace.com register ✘ nattyornot nattyornotforum.nattyornot.com
  register ✘ naturabuy naturabuy.fr register ✘ ndemiccreations forum.ndemiccreations.com
  register ✘ nextpvr forums.nextpvr.com register ✘ nike nike.com register ✘ nimble
  nimble.com register ✘ nocrm nocrm.io register ✘ nutshell nutshell.com register ✘
  odnoklassniki ok.ru password recovery ✘ office365 office365.com other ✔ onlinesequencer
  onlinesequencer.net register ✘ parler parler.com login ✘ patreon patreon.com login
  ✔ pinterest pinterest.com register ✘ pipedrive pipedrive.com register ✘ plurk plurk.com
  register ✘ pornhub pornhub.com register ✘ protonmail protonmail.ch other ✘ quora
  quora.com register ✘ rambler rambler.ru register ✘ redtube redtube.com register
  ✘ replit replit.com register ✔ rocketreach rocketreach.co register ✘ samsung samsung.com
  register ✘ seoclerks seoclerks.com register ✘ sevencups 7cups.com register ✔ smule
  smule.com register ✔ snapchat snapchat.com login ✘ soundcloud soundcloud.com register
  ✘ sporcle sporcle.com register ✘ spotify spotify.com register ✔ strava strava.com
  register ✘ taringa taringa.net register ✔ teamleader teamleader.com register ✘ teamtreehouse
  teamtreehouse.com register ✘ tellonym tellonym.me register ✘ thecardboard thecardboard.org
  register ✘ therianguide forums.therian-guide.com register ✘ thevapingforum thevapingforum.com
  register ✘ tumblr tumblr.com register ✘ tunefind tunefind.com register ✔ twitter
  twitter.com register ✘ venmo venmo.com register ✔ vivino vivino.com register ✘ voxmedia
  voxmedia.com register ✘ vrbo vrbo.com register ✘ vsco vsco.co register ✘ wattpad
  wattpad.com register ✔ wordpress wordpress login ✘ xing xing.com register ✘ xnxx
  xnxx.com register ✔ xvideos xvideos.com register ✘ yahoo yahoo.com login ✔ zoho
  zoho.com login ✔'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fa2c4f7ecac76c6b
source_type: community_discussion
tldr: Holehe 是基于 Python 3 的开源命令行工具，利用各网站的忘记密码功能，在不惊动目标邮箱的前提下检测邮箱是否在 Twitter、Instagram、Imgur
  等 120 多个平台注册过账号。它支持 CLI 直接运行和嵌入 Python 应用两种使用方式，项目声明仅供教育用途。
objective_summary: Holehe 由 GitHub 用户 megadose 开发，是一款基于 Python 3 的邮箱账号检测开源工具，可通过 pip3
  安装、源码安装或 Docker 运行。它通过调用超过 120 个网站（包括 Twitter、Instagram、Imgur 等）的忘记密码接口，返回邮箱是否注册、部分脱敏的找回邮箱与手机号等结构化信息，全程不向目标邮箱发送提醒。工具提供命令行与
  Python 异步嵌入两种使用方式，每个模块以统一的 JSON 字典返回结果，项目声明仅用于教育目的。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Twitter
  - Instagram
  - Imgur
  technologies:
  - Python 3
  - httpx
  - trio
  - Docker
  key_people:
  - megadose
key_logic_flow:
- Holehe 是一个开源命令行工具，用于检测指定邮箱是否在 Twitter、Instagram、Imgur 等超过 120 个网站上注册过账号。
- 该工具通过各网站的忘记密码功能检索账号存在性信息，并且不会向目标邮箱发送任何提醒通知。
- Holehe 基于 Python 3 开发，支持 pip3 install 安装、源码安装和 Docker 容器运行等多种部署方式。
- 工具既可以独立从命令行运行，也可以通过 trio 与 httpx 异步库嵌入到现有的 Python 应用当中。
- 每个检测模块以统一格式返回 JSON 字典，包含 rateLimit、exists、emailrecovery、phoneNumber 和 others 等字段。
- 项目声明仅供教育用途，并列出全部受支持网站及其对应的注册、登录或密码找回检测方法。
object_mentions:
- object_type: project
  name: megadose/holehe
  canonical_name: megadose/holehe
  url: https://github.com/megadose/holehe
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Holehe 是一款开源命令行工具，用于检测指定邮箱是否在 Twitter、Instagram、Imgur 等超过 120 个网站上注册过账号。
  - 该工具利用各网站的忘记密码功能获取账号存在性信息，且全程不会向目标邮箱发送任何提醒通知。
  - 项目支持通过 pip3 安装、源码安装和 Docker 容器运行，既能从命令行直接调用，也能嵌入现有 Python 应用。
  article_id: fa2c4f7ecac76c6b
extract_result: success
impact_score:
  score: 2.5
  reason: 该事件属于安全/OSINT 领域的成熟开源工具，与 AI 行业无直接关联。Holehe 是已在安全圈流传多年的账号枚举工具，本次社区讨论既非新产品发布也非范式创新，未改变任何
    AI 竞争格局。虽然它在渗透测试、隐私研究小圈子中有稳定实用价值，但按 1-3 分对应'日常更新、小圈子自嗨'的标准，短期行业冲击力有限，故给出 2.5 分。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 120+ 平台覆盖的静默账号枚举能力，以及'不惊动目标邮箱'的隐蔽检测特性
hype_assessment:
  level: low
  reason: 项目 README 通篇为客观的功能描述、安装方式与受支持站点清单，明确标注'Built for educational purposes only'，未出现'颠覆'、'革命性'等
    PR 滥用词汇，也没有夸大其能力边界（如实列出 rateLimit 与检测方法），属于实打实的工具文档，无概念炒作成分。
information_entropy: medium
domain_disruption:
  technical_innovation: 该工具将各平台'忘记密码/账号找回'流程作为账号存在性判定的预言机（side-channel enumeration），通过
    trio + httpx 异步并发对 120+ 站点进行静默批量探测，并统一返回含 rateLimit、exists、脱敏找回邮箱/手机号的结构化 JSON。其技术本质是安全领域早已成熟的账号枚举侧信道技术的系统化、模块化工程封装，而非
    AI 领域的技术突破。
  business_model: 无直接商业模式重塑力。该工具可作为 OSINT 侦察、渗透测试、账号泄露排查、欺诈调查等安全服务链路中的一环，但本身是免费开源项目，对
    AI/SaaS 生态的商业模式没有影响。
engineering_complexity: production_ready
compound_value:
  score: 3.0
  reason: Holehe 是一款 OSINT 细分工具，其核心价值在于把'邮箱账号枚举'能力免费化、标准化，并已进入 Kali Linux 等渗透测试发行版的默认工具箱，具备一定的持久性。但从复利角度看短板明显：每个站点模块都依赖目标网站的前端/接口行为，站点改版即失效，属于典型的高维护成本、无沉淀资产的工具型项目；无数据积累、无网络效应、无平台化延展，无法升级为基础设施或数据护城河。其价值更接近'一次性效率工具'而非'长期积累型资产'，3-5
    年后大概率仍是一款小众开源单品，而非行业基石，故评分落在低位区间。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Kali Linux (Offensive Security)
- Maltego
- 安全研究/红队社区
- 商业威胁情报公司 (如 Recorded Future)
competitive_casualty:
- 商业邮箱枚举/OSINT 查询服务（如 Dehashed）
- 账号枚举防护薄弱的社交平台（如 Twitter、Instagram）
- 名单内 120+ 中小论坛/社区站点
market_opportunities:
- 安全厂商与渗透测试团队可将此类邮箱枚举能力整合进 OSINT 侦察工具链，用于授权红队演练、资产暴露面评估与账号接管防护测试
- 面向个人与企业用户的'数字足迹隐私审计'服务有机会兴起，帮助用户发现邮箱在 120+ 平台注册过哪些账号、主动清理隐私暴露面
- 数据泄露响应与社工防御场景可借鉴该思路，将邮箱枚举结果与威胁情报关联，提前识别钓鱼与定向攻击的潜在切入点
risk_matrix:
  regulatory: GDPR、法国数据保护法等隐私法规及各大平台服务条款均限制未授权的程序化邮箱枚举行为；项目'仅教育用途'声明不构成法律豁免，滥用可能触犯非法访问计算机系统与个人信息保护相关条款
  technological: 工具高度依赖 120+ 平台'忘记密码'接口的稳定性，平台频繁调整流程、引入验证码与人机校验会导致模块大面积失效，需持续维护；目标平台风控封禁风险高
  competitive: 存在 sherlock、GHunt、theHarvester、Maltego transforms 等大量同类 OSINT 工具及商业情报平台竞争，功能同质化严重，单点工具难以形成差异化壁垒
  ethical: 可被用于大规模枚举他人网络足迹，便利人肉搜索、骚扰与定向社工攻击；返回的脱敏找回邮箱与手机号仍属敏感个人信息，存在隐私侵犯与数据伦理风险
  additional:
  - 可能被攻击者用于验证窃取/购买的账号凭证列表真实性，或作为钓鱼、社工攻击前的情报踩点工具
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: megadose/holehe
  canonical_name: megadose/holehe
  url: https://github.com/megadose/holehe
  positioning: Holehe 是一款基于 Python 3 的开源命令行邮箱账号检测工具，通过各网站忘记密码功能排查邮箱在超过 120 个平台的注册情况，并保持对目标邮箱静默。
  technical_signal: 项目基于 Python 3 开发，支持 pip3 安装、源码安装与 Docker 运行，可通过 trio 与 httpx 异步库嵌入现有
    Python 应用，各检测模块统一返回 JSON 字典。
  adoption_signal: null
  ecosystem_relevance: 该工具属于开源 OSINT（开源情报）工具生态，提供邮箱维度的账号存在性排查能力，可嵌入 Python 安全研究与审计流程。
  target_users:
  - 安全研究人员
  - 渗透测试人员
  - OSINT 分析师
  product_signal: null
  market_signal: null
  differentiation: 区别于常见注册检测手段，该工具利用忘记密码接口实现全程不向目标邮箱发送提醒，且统一返回结构化 JSON 结果，便于自动化集成。
  watch_reason: Holehe 在单一命令行工具中整合超过 120 个网站的邮箱注册检测能力，并保持对目标邮箱静默，对 OSINT 与安全审计场景有实用价值；其模块化
    Python 接口与统一 JSON 返回格式降低了二次开发门槛，值得持续跟踪其覆盖站点更新与稳定性表现。
  risk_notes:
  - 项目声明仅供教育用途，但邮箱枚举能力存在被滥用于骚扰或社工攻击的风险，合规边界模糊。
  - 工具依赖第三方网站忘记密码接口，站点改版或速率限制可能导致检测失效，维护成本随站点数量上升。
  - 输出包含部分脱敏的找回邮箱与手机号等敏感个人信息，使用与再分发可能面临隐私与数据合规风险。
  score: 6.0
  article_ids:
  - fa2c4f7ecac76c6b
  evidence_snippets:
  - Holehe 是一款开源命令行工具，用于检测指定邮箱是否在 Twitter、Instagram、Imgur 等超过 120 个网站上注册过账号。
  - 该工具利用各网站的忘记密码功能获取账号存在性信息，且全程不会向目标邮箱发送任何提醒通知。
  - 项目支持通过 pip3 安装、源码安装和 Docker 容器运行，既能从命令行直接调用，也能嵌入现有 Python 应用。
---

👋 Hi there! For any professional inquiries or collaborations, please reach out to me at: megadose@protonmail.com

📧 Preferably, use your professional email for correspondence. Let's keep it short and sweet, and all in English!

*Efficiently finding registered accounts from emails.*

Holehe checks if an email is attached to an account on sites like twitter, instagram, imgur and more than 120 others.

- Retrieves information using the forgotten password function.
**Does not alert the target email.**- Runs on Python 3.

`pip3 install holehe`


```
git clone https://github.com/megadose/holehe.git
cd holehe/
python3 setup.py install
```

```
docker build . -t my-holehe-image
docker run my-holehe-image holehe test@gmail.com
```

Holehe can be run from the CLI and rapidly embedded within existing python applications.

`holehe test@gmail.com`

```
import trio
import httpx
from holehe.modules.social_media.snapchat import snapchat
async def main():
email = "test@gmail.com"
out = []
client = httpx.AsyncClient()
await snapchat(email, client, out)
print(out)
await client.aclose()
trio.run(main)
```

For each module, data is returned in a standard dictionary with the following json-equivalent format :

```
{
"name": "example",
"rateLimit": false,
"exists": true,
"emailrecovery": "ex****e@gmail.com",
"phoneNumber": "0*******78",
"others": null
}
```

- rateLitmit : Lets you know if you've been rate-limited.
- exists : If an account exists for the email on that service.
- emailrecovery : Sometimes partially obfuscated recovery emails are returned.
- phoneNumber : Sometimes partially obfuscated recovery phone numbers are returned.
- others : Any extra info.

Rate limit? Change your IP.

For BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ

Built for educational purposes only.

| Name | Domain | Method | Frequent Rate Limit |
|---|---|---|---|
| aboutme | about.me | register | ✘ |
| adobe | adobe.com | password recovery | ✘ |
| amazon | amazon.com | login | ✘ |
| amocrm | amocrm.com | register | ✘ |
| anydo | any.do | login | ✔ |
| archive | archive.org | register | ✘ |
| armurerieauxerre | armurerie-auxerre.com | register | ✘ |
| atlassian | atlassian.com | register | ✘ |
| axonaut | axonaut.com | register | ✘ |
| babeshows | babeshows.co.uk | register | ✘ |
| badeggsonline | badeggsonline.com | register | ✘ |
| biosmods | bios-mods.com | register | ✘ |
| biotechnologyforums | biotechnologyforums.com | register | ✘ |
| bitmoji | bitmoji.com | login | ✘ |
| blablacar | blablacar.com | register | ✔ |
| blackworldforum | blackworldforum.com | register | ✔ |
| blip | blip.fm | register | ✔ |
| blitzortung | forum.blitzortung.org | register | ✘ |
| bluegrassrivals | bluegrassrivals.com | register | ✘ |
| bodybuilding | bodybuilding.com | register | ✘ |
| buymeacoffee | buymeacoffee.com | register | ✔ |
| cambridgemt | discussion.cambridge-mt.com | register | ✘ |
| caringbridge | caringbridge.org | register | ✘ |
| chinaphonearena | chinaphonearena.com | register | ✘ |
| clashfarmer | clashfarmer.com | register | ✔ |
| codecademy | codecademy.com | register | ✔ |
| codeigniter | forum.codeigniter.com | register | ✘ |
| codepen | codepen.io | register | ✘ |
| coroflot | coroflot.com | register | ✘ |
| cpaelites | cpaelites.com | register | ✘ |
| cpahero | cpahero.com | register | ✘ |
| cracked_to | cracked.to | register | ✔ |
| crevado | crevado.com | register | ✔ |
| deliveroo | deliveroo.com | register | ✔ |
| demonforums | demonforums.net | register | ✔ |
| devrant | devrant.com | register | ✘ |
| diigo | diigo.com | register | ✘ |
| discord | discord.com | register | ✘ |
| docker | docker.com | register | ✘ |
| dominosfr | dominos.fr | register | ✔ |
| ebay | ebay.com | login | ✔ |
| ello | ello.co | register | ✘ |
| envato | envato.com | register | ✘ |
| eventbrite | eventbrite.com | login | ✘ |
| evernote | evernote.com | login | ✘ |
| fanpop | fanpop.com | register | ✘ |
| firefox | firefox.com | register | ✘ |
| flickr | flickr.com | login | ✘ |
| freelancer | freelancer.com | register | ✘ |
| freiberg | drachenhort.user.stunet.tu-freiberg.de | register | ✘ |
| garmin | garmin.com | register | ✔ |
| github | github.com | register | ✘ |
| google.com | register | ✔ | |
| gravatar | gravatar.com | other | ✘ |
| hubspot | hubspot.com | login | ✘ |
| imgur | imgur.com | register | ✔ |
| insightly | insightly.com | login | ✘ |
| instagram.com | register | ✔ | |
| issuu | issuu.com | register | ✘ |
| koditv | forum.kodi.tv | register | ✘ |
| komoot | komoot.com | register | ✔ |
| laposte | laposte.fr | register | ✘ |
| lastfm | last.fm | register | ✘ |
| lastpass | lastpass.com | register | ✘ |
| mail_ru | mail.ru | password recovery | ✘ |
| mybb | community.mybb.com | register | ✘ |
| myspace | myspace.com | register | ✘ |
| nattyornot | nattyornotforum.nattyornot.com | register | ✘ |
| naturabuy | naturabuy.fr | register | ✘ |
| ndemiccreations | forum.ndemiccreations.com | register | ✘ |
| nextpvr | forums.nextpvr.com | register | ✘ |
| nike | nike.com | register | ✘ |
| nimble | nimble.com | register | ✘ |
| nocrm | nocrm.io | register | ✘ |
| nutshell | nutshell.com | register | ✘ |
| odnoklassniki | ok.ru | password recovery | ✘ |
| office365 | office365.com | other | ✔ |
| onlinesequencer | onlinesequencer.net | register | ✘ |
| parler | parler.com | login | ✘ |
| patreon | patreon.com | login | ✔ |
| pinterest.com | register | ✘ | |
| pipedrive | pipedrive.com | register | ✘ |
| plurk | plurk.com | register | ✘ |
| pornhub | pornhub.com | register | ✘ |
| protonmail | protonmail.ch | other | ✘ |
| quora | quora.com | register | ✘ |
| rambler | rambler.ru | register | ✘ |
| redtube | redtube.com | register | ✘ |
| replit | replit.com | register | ✔ |
| rocketreach | rocketreach.co | register | ✘ |
| samsung | samsung.com | register | ✘ |
| seoclerks | seoclerks.com | register | ✘ |
| sevencups | 7cups.com | register | ✔ |
| smule | smule.com | register | ✔ |
| snapchat | snapchat.com | login | ✘ |
| soundcloud | soundcloud.com | register | ✘ |
| sporcle | sporcle.com | register | ✘ |
| spotify | spotify.com | register | ✔ |
| strava | strava.com | register | ✘ |
| taringa | taringa.net | register | ✔ |
| teamleader | teamleader.com | register | ✘ |
| teamtreehouse | teamtreehouse.com | register | ✘ |
| tellonym | tellonym.me | register | ✘ |
| thecardboard | thecardboard.org | register | ✘ |
| therianguide | forums.therian-guide.com | register | ✘ |
| thevapingforum | thevapingforum.com | register | ✘ |
| tumblr | tumblr.com | register | ✘ |
| tunefind | tunefind.com | register | ✔ |
| twitter.com | register | ✘ | |
| venmo | venmo.com | register | ✔ |
| vivino | vivino.com | register | ✘ |
| voxmedia | voxmedia.com | register | ✘ |
| vrbo | vrbo.com | register | ✘ |
| vsco | vsco.co | register | ✘ |
| wattpad | wattpad.com | register | ✔ |
| wordpress | wordpress | login | ✘ |
| xing.com | register | ✘ | |
| xnxx | xnxx.com | register | ✔ |
| xvideos | xvideos.com | register | ✘ |
| yahoo | yahoo.com | login | ✔ |
| zoho | zoho.com | login | ✔ |