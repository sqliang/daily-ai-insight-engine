---
title: How to Block Some of the Bots
source: https://nochan.net/b/Internet-Crap/20260606-How-To-Block-Some-Of-The-Bots/
author:
- '[[Bender]]'
published: '2026-07-26'
created: '2026-07-27'
manifest_dates:
- '2026-07-27'
description: 'Article URL: https://nochan.net/b/Internet-Crap/20260606-How-To-Block-Some-Of-The-Bots/
  Comments URL: https://news.ycombinator.com/item?id=49060945 Points: 102 # Comments:
  118'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4c1b6ef7face44a5
source_type: community_discussion
tldr: 一篇技术博文详细介绍了9种在Web服务器上拦截爬虫和扫描器的方法，涵盖HTTP协议过滤、数据中心IP封禁、国家/代理/Tor封锁、客户端信号检测、NFTables规则、TLS指纹识别等，作者基于自身长期运营经验给出了具体的nginx配置和shell代码示例。
objective_summary: 作者于2026年7月在个人博客上发表技术指南，系统介绍了从HTTP协议版本过滤（仅允许HTTP/2.0）到网络层NFTables规则共9种拦截机器人/爬虫的方法。每种方法标注了对真实用户和搜索引擎的误伤风险等级，并提供了nginx配置片段、BGP路由查询工具使用方式、FireHOL黑名单IP集加载命令以及JA4
  TLS指纹识别部署指引。作者强调所有方法均需在测试后使用，不适用于营收环境。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - HTTP/2
  - Brotli
  - TLS Fingerprinting
  - JA4
  - NFTables
  - BGP
  - nginx
  key_people:
  - Miloslav Homer
key_logic_flow:
- 作者提出在拦截机器人前需先决定目标——拦截部分、大部分还是全部机器人，并承认不同方法对真实用户和搜索引擎存在不同程度的误伤风险。
- 方法一强制客户端使用HTTP/2.0协议，不符合条件的请求返回301重定向、403禁止或444关闭连接。
- 方法二通过分析访问日志中的可疑IP，使用BGP工具查询其AS归属并封禁整个数据中心IP段，但提醒需谨慎避免封禁CDN和搜索引擎。
- 方法三推荐使用FireHOL Blocklists项目中的黑名单IP集，通过循环命令在路由表中添加黑洞路由以屏蔽恶意IP。
- 方法四至九涵盖客户端信号（User-Agent、Sec-Fetch-Mode、Referer等）过滤、NFTables TCP窗口和MSS检测、RTA成人内容头部、JA4
  TLS指纹识别、仅提供Brotli压缩内容以及利用"Help Attackers Self Report"让扫描器自曝。
- 作者在摘要中展示了2小时内未启用黑洞路由的对比数据：访问日志37行/13KB，而被拦截的bot日志达1126行/350KB。
object_mentions:
- object_type: project
  name: FireHOL Blocklists
  canonical_name: firehol/blocklist-ipsets
  url: https://github.com/firehol/blocklist-ipsets
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者推荐克隆FireHOL Blocklists仓库并使用其中的firehol_abusers_30d.netset和firehol_level2.netset文件，通过for循环将恶意IP批量添加为黑洞路由。
  - 该仓库提供分类的IP黑名单集合，作者特别指出需要使用grep -Ev ^#来去除配置文件中的注释行再进行加载。
  article_id: 4c1b6ef7face44a5
- object_type: project
  name: FoxIO-LLC/ja4
  canonical_name: FoxIO-LLC/ja4
  url: https://github.com/FoxIO-LLC/ja4
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者将JA4 TLS指纹识别列为方法七，认为在机器人不进化的情况下它可能是更好的长期拦截方案。
  - 作者首先建议阅读Miloslav Homer关于Deploying JA4的说明，然后访问FoxIO-LLC/ja4仓库进行部署。
  article_id: 4c1b6ef7face44a5
- object_type: project
  name: Help Attackers Self Report
  canonical_name: Help Attackers Self Report
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 作者在方法九中引用"Help Attackers Self Report"作为让脚本小子停止扫描的参考资源。
  article_id: 4c1b6ef7face44a5
extract_result: success
---

**26 July 2026 - Update:** Recently linked to from
**HN**
and the general take-away for me is to move *most of* the blocking from this silly blog over
to a demo site so that more people can read the options and then optionally try to access the demo site, thus making it more like a fun puzzle
rather than a frustrating experience.

**How far do we go?**

Before we start blocking things we have to decide which is more important, blocking *some* of the bots, *most* of
the bots or **ALL** of the bots. In this document I will describe some generalized and very simple methods
that can block most of the poorly coded and configured bots. I will attempt to suggest what level of risk and false positives
each method *may* introduce.


**DISCLAIMER:** These are methods I have used for a very long time and they work for me. They may not work for you. They may
cause you to block your Aunt Martha, Your Boss, Other things you depend on hitting your site. Use at your own peril after extensive testing.
I take no responsibility for damages, being red faced, explosive sharts, financial losses or anything else. The person testing these methods assumes full
responsibility for anything and everything. It is assumed and implied that anyone trying anything listed here either already knows what they
are doing or will research each item until they are completely omniscient.

**Every method I list is entirely optional, tunable, editable and delectable.** If there is something that twerks you the wrong way
or you do not understand, research the option or just avoid it all together.

** 💰 Not for use in a revenue generating environment.**


**Method 1: HTTP Protocol**

**Method 2: Blocking Data-Centers**

**Method 3: Blocking countries, Some Proxies, Some Tor, Some other asshats**

**Method 4: Client Signals**

**Method 5: NFTables to Block some crappy bots**

**Method 6: Adult Content and Robot Headers**

**Method 7: Fingerprint Detection**

**Method 8: Compress Content with Brotli**

**Method 9: Make the skiddies stop scanning you**


¶
**Method 1: HTTP Protocol**

Risk of blocking real people: **Low**

Risk of blocking a few search engines: **Moderate**


`if ($server_protocol != HTTP/2.0) { return 301 https://moot.ytmnd.com/; }`

or ...`if ($server_protocol != HTTP/2.0) { return 200 'Upgrade your client'; }`

or ...`if ($server_protocol != HTTP/2.0) { return 403 'Upgrade your client'; }`

or ...`if ($server_protocol != HTTP/2.0) { return 444 ''; }`

¶
**Method 2: Blocking Data-Centers**

Risk of blocking real people: **Moderate for VPN Users, Low for Home and LTE Users**

Risk of blocking search engines: **High as they are in data-ceters, pick and choose carefully.**

Collect your access logs from the last year or two.

Looking at signals like HTTP protocol, user-agent, accept-language, sec-fetch-mode (if you log this), accept and other variables
look for the obvious bots. While user-agents can be spoofed, it is rare for botters to do this. *They are lazy and are using
crappy code that only cares about speed most of the time.*

For each suspicious looking IP, look them up in one of the BGP tool sites:
**BGP Tools** or
**bgp.he.net**.

Here are a few to get you started. **20260714_network_blackholes.tar.bz2**

**Choose carefully as some of these are CDN's and search engines.**

This is after I already blackhole 3/8, 10/8, 11/8, 25/8, 26/8, 38/8, 41/8, 60/8, 61/8, 200/8, 224/3.

To generate these files I look up the IP of a bot in one of the BGP sites, click on their AS Number, click on "Prefixes" select the entire page,
copy into paste buffer and save the contents into a temporary file in /dev/shm and then run this shell script against it:


```
cidr()
{
InNowFile="$1"
grep "/" "${InNowFile}" | awk '{print $1}' | grep -E "^[1-9]" | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}/[1-9][0-9]\b" | sort | uniq | /usr/local/sbin/sum_cidr.pl | grep -E "^[1-9]" | sort | uniq > "${InNowFile}".sum
ls -alh "${InNowFile}".sum
# mv /dev/shm/${InNowFile}".sum /usr/local/etc/_some_name.netset # after reviewing it
}
```


`for CflIP in $(grep -E ^[1-9] /usr/local/etc/_cloudflare.netset); do /sbin/ip route add blackhole "${CflIP}" 2>/dev/null;done`

¶
**Method 3: Blocking countries, Some Proxies, Some Tor, Some other asshats**

Clone this repo: **FireHOL Blocklists**

Repeat the process above using "for" loops to blackhole anything you need not see on your server again. Be sure to use `grep -Ev ^#`

to strip out comments. The files in that repo contain comments.

A couple of files from that repo I would strongly recommend are: **firehol_abusers_30d.netset** and **firehol_level2.netset**.

Example:

`for BadIP in $(grep -Ev ^# /usr/local/etc/blocklist-ipsets/firehol_abusers_30d.netset); do ip route add blackhole 2>/dev/null;done`


¶
**Method 4: Client Signals** *Examples using NGinx format*

Clients can spoof many variables ... except that most don't either due to laziness
or speed or lack of knowledge or using vibe coding or too much alcohol.

People always claim the user-agent is spoofed but in truth it rarely is. Here are some partial strings I have observed recently.

**Before using this** grab at least 2 years of your access logs, grab the user-agent field, do a `sort | uniq -c | sort`

into a text file and use the string below with a `grep -E`

to see what would have been matched. If the client was using http/1.1 they were probably a bot and could be ignored. *GoogleBot aside*. If they were using HTTP/2.0 then use the BGP tool sites listed
above to see what they were. Once comfortable then test this on a silly hobby site that you do not care about.


`if ($http_user_agent ~ (eadless|oogle|ing|bot|Bot|gpt|llm|pider|gent|earch|etch|eed|ead|iphon|ython|Ruby|Go-h|uzzl) ) { return 410 '\n\n\t\t$http_user_agent\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


`grep -E`

through your access logs, maybe 2 or 3 years worth.`if ($http_sec_fetch_mode !~ (cors|no-cors|navigate|same-origin|websocket) ) { return 410 'SFM: $http_sec_fetch_mode\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


`if ($http_referer ~ (172.238.221.88|localhost|nochan|google) ) { return 410 '\n\n\t\t$http_referer\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


`if ($request_method !~ (^GET$) ) { return 410 '$request_method\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


`if ($http_x_forwarded_for) { return 410 '$http_x_forwarded_for\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


`if ($http_user_agent !~ (Linux|BSD|Macintosh|Windows|Mozilla|WhatsApp) ) { return 410 '\n\n\t\t$http_user_agent\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


`if ($http_accept_encoding !~ (br) ) { return 410 '\n\n$http_accept_encoding\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


`if ($request_uri ~ (\.git$|\.yml$|\.db$|\.sql$|\.conf$|\.php$|\.avi$|wp) ) { return 410 '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (\_/)\n (=\'.\'=)\n (\")_(\")\n\n\n\n'; }`


¶
**Method 5: NFTables to Block some crappy bots** *This actually stops a lot of scanners.*

**Note:** The references to the IP address 172.238.221.88 are the eth0 address of the VM you are browsing right now. The reason to specify the server IP is to avoid some false positives during packet loss events.

**Raw Table:**

```
table ip raw {
chain PREROUTING {
type filter hook prerouting priority raw; policy accept;
iifname "lo" notrack
iifname "eth0" ip daddr 172.238.221.88 tcp flags & (fin | syn | rst | ack) == syn tcp window < 12288 tcp dport { 80, 443 } counter drop
iifname "eth0" ip daddr 172.238.221.88 tcp flags & (fin | syn | rst | ack) == syn tcp option maxseg size != 1220-1460 tcp dport { 80, 443 } counter drop
iifname "eth0" ip daddr 172.238.221.88 tcp dport 443 notrack
iifname "eth0" ip daddr 172.238.221.88 tcp dport 80 notrack
}
chain OUTPUT {
type filter hook output priority raw; policy accept;
oifname "lo" notrack
oifname "eth0" ip saddr 172.238.221.88 tcp sport 443 notrack
oifname "eth0" ip saddr 172.238.221.88 tcp sport 80 notrack
}
}
```


```
nft -osu list table ip filter | grep -E "80|443"
iifname "eth0" ip daddr 172.238.221.88 tcp sport 1000-65535 tcp dport 443 counter accept
iifname "eth0" ip daddr 172.238.221.88 tcp sport 1000-65535 tcp dport 80 accept
oifname "eth0" ip saddr 172.238.221.88 tcp sport 443 tcp dport 1000-65535 accept
oifname "eth0" ip saddr 172.238.221.88 tcp sport 80 tcp dport 1000-65535 accept
```


¶
**Method 6: Adult Content and Robot Headers**

Bots mostly ignore headers unless they are search engines or bots trying to avoid adult content.

**RTA: Restricted To Adults**
is the only appropriate way to restrict access to a website that may contain content not suitable for small children.
The only missing part is the legislation to make that a required thing. All other methods are strictly for tracking and monetization of users, without exception.


```
add_header Rating 'RTA-5042-1996-1400-1577-RTA' always;
add_header adult 'porn, sex, politics, religion, philosophy' always;
add_header X-Robots-Tag "none,noindex,nofollow,nosnippet,noai" always;
```


¶
**Method 7: Fingerprint Detection**

Methods 1 through 6 thus far have been very crude.

Method 7 *TLS fingerprinting* may be a better long term option assuming bots do not evolve in this area.

First read the instructions at **Miloslav Homer: Deploying JA4**

Then head on over to **https://github.com/FoxIO-LLC/ja4**


¶
**Method 8: Compress Content with Brotli**

Pre-Compress your site with Brotli and configure your web daemon to always serve up the pre-compressed content only.
Most bots can not parse brotli compressed text.

Verified many of the bots are no longer following links meaning they are not actually parsing the HTML.

In NGinx:

`brotli_static always;`


For my index files i.html: `cat ./i.html | brotli --best -fncv > ./i.html.br`



¶
**Method 9: Make the skiddies stop scanninng you**

See **Help Attackers Self Report**


**Summary, without any blackhole routing in place:**


# access.log is anything with status 1 through 2. # botpoop.log is anything with status 3 through 5. # timespan: 2 hours # sizes: 13K access.log 350K botpoop.log # line count: 37 access.log 1126 botpoop.log

# from /etc/nginx/nginx.conf map $status $statlog { ~^[12] 1; default 0; } map $status $statwog { ~^[345] 1; default 0; } log_format nog '$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for" "$host" "$request_length" "$connection" "$connection_requests" "$http_accept_language" "$http_accept_encoding" "$tcpinfo_snd_cwnd" "$tcpinfo_rcv_space" "$tcpinfo_rtt" "$tcpinfo_rttvar" "$http_sec_fetch_mode" '; # from /etc/nginx/http.d/40_nochan.net.conf access_log /var/log/nginx/access.log nog if=$statlog; access_log /var/log/nginx/botpoop.log nog if=$statwog; error_log /dev/null crit; Filesystem Size Used Avail Use% Mounted on tmpfs 420M 420K 420M 1% /var/log/nginx