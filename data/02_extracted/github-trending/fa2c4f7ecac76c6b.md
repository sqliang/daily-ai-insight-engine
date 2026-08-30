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