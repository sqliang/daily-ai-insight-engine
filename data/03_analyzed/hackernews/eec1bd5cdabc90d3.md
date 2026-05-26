---
title: Blog ran on Ubuntu 16.04 for 10 years. I migrated it to FreeBSD
source: https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/
author:
- '[[speckx]]'
published: '2026-05-21'
created: '2026-05-22'
description: 'Article URL: https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/
  Comments URL: https://news.ycombinator.com/item?id=48227397 Points: 224 # Comments:
  119'
tags:
- clippings
extraction_status: success
id: eec1bd5cdabc90d3
source_type: community_discussion
tldr: 一位开发者将其运行10年的博客从Digital Ocean的Ubuntu 16.04 VPS迁移至Hetzner的FreeBSD 14.
objective_summary: 作者于2026年将运行在Digital Ocean纽约节点上已达1491天uptime的Ubuntu 16.04 VPS（$13/月），迁移至Hetzner德国节点的FreeBSD
  14.3虚拟机（约€6/月）。迁移中采用FreeBSD Jails+Bastille实现每站点独立隔离，
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Digital Ocean
  - Hetzner
  technologies:
  - FreeBSD
  - FreeBSD Jails
  - Bastille
  - ZFS
  - Caddy
  - nginx
  - Hugo
  - PF
  - Btrfs
  key_people: []
key_logic_flow:
- 旧服务器为Digital Ocean纽约节点VPS，运行Ubuntu 16.04 LTS超10年，已停止安全更新支持至少5年，存在安全隐患
- 新服务器选用Hetzner德国节点虚拟机，配置为旧机两倍内存和CPU，月费仅为旧机一半以下（从$13降至约€6）
- 迁移动机之一是学习FreeBSD，尤其是其Jails容器化技术和成熟的ZFS文件系统的快照功能
- 通过Bastille工具管理Jails，为Caddy反向代理和每个站点分别创建独立Jail，实现网络隔离
- 使用PF防火墙配置NAT出站规则和HTTP/HTTPS端口重定向，将外部流量引导至Caddy Jail
- 用Caddy替代nginx作为Web服务器，主要原因是Caddy可自动处理SSL证书的申请和续期，避免手动运行certbot
pipeline_stage: fact_extracted
impact_score:
  score: 1.2
  reason: 该文章是一篇个人博客基础设施迁移的技术记录，与AI行业完全无关。内容涉及的是Ubuntu迁移至FreeBSD的操作系统切换、Jails容器化配置、以及VPS成本优化，属于个人开发者运维实践分享，对AI行业无任何冲击力。评分1.2分，归入'日常更新，小圈子自嗨'范畴。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: FreeBSD Jails与Docker容器化的实际体验对比，以及ZFS文件系统在生产环境中的可靠性
hype_assessment:
  level: low
  reason: 文章是纯粹的技术实践记录，作者明确承认'不假装自己完全懂自己在做什么'，没有任何'颠覆'或'革命性'等PR词汇。内容朴实，以操作步骤和经验分享为主，水分极低。
information_entropy: medium
domain_disruption:
  technical_innovation: 无AI相关技术突破。文章在系统工程层面展示了FreeBSD Jails+Bastille实现多站点隔离的轻量级方案，以及用Caddy自动SSL替代nginx+手动certbot的运维简化思路，但这些属于传统运维领域的成熟实践，不具备技术新颖性。
  business_model: 无。文章仅在个人层面展示了从Digital Ocean（$13/月）迁移至Hetzner（约€6/月）的成本优化，属于个人消费决策，不涉及任何商业模式变革。
engineering_complexity: production_ready
compound_value:
  score: 2.5
  reason: 这是一篇个人技术博客的迁移记录，不涉及任何商业产品发布、公司动态或行业结构性变化。文中涉及的技术（FreeBSD Jails、Bastille、ZFS、Caddy）均为成熟开源项目，无新增商业价值。从
    VC 视角看，该事件不具备长期复利积累效应——它不会催生新市场、不会改变行业格局、也不会形成可规模化的商业模式。唯一的微弱信号是开发者从高价 VPS（Digital
    Ocean $13/月）向高性价比 VPS（Hetzner €6/月）迁移的成本优化趋势，但这属于个体决策而非系统性资本流动。评分 2.5 反映其作为技术参考文档对社区有一定实用价值，但对资本格局几乎无影响。
value_capture_layer: cloud_platform
moat_impact: democratizes_access
key_beneficiaries:
- Hetzner
- FreeBSD
- Bastille
- Caddy
competitive_casualty:
- Digital Ocean
- nginx
- Docker
market_opportunities:
- 面向个人开发者和中小团队，可推出基于 FreeBSD Jails + Bastille 的轻量级多站点托管方案，主打低成本（€6/月级别）、高隔离性和 ZFS
  快照备份，形成与 Docker/K8s 差异化竞争的小众托管产品
- Caddy 自动 SSL 证书管理的特性可封装为 AI Agent 工具或 SaaS 产品的内置网关模块，降低 AI 应用部署中 HTTPS 配置的运维门槛，尤其适合边缘推理节点的快速安全上线
- 成本优化驱动的'去大云'趋势为 Hetzner 等欧洲性价比 VPS 带来增量市场，AI 创业公司可将非 GPU 工作负载（CI/CD、静态文档站、轻量 API
  网关）迁移至此，显著降低基础设施固定支出
risk_matrix:
  regulatory: Hetzner 位于德国，受 GDPR 严格管辖，若托管涉及用户数据的 AI 服务需额外关注数据跨境合规；Digital Ocean 美区迁移至欧洲机房可能触发数据驻留策略变更
  technological: FreeBSD 生态远小于 Linux，AI/ML 工具链（如 CUDA、PyTorch、Docker）在 FreeBSD 上支持有限或缺失，若后续需扩展
    AI 推理能力将面临平台兼容性瓶颈；ZFS 虽成熟但运维人才稀缺
  competitive: Hetzner 以极致性价比挤压 Digital Ocean、Linode 等传统 VPS 厂商利润空间，可能引发新一轮价格战；但 FreeBSD
    技术栈的小众性使其难以撼动 Linux 在 AI 基础设施中的主导地位
  ethical: 原文提及旧服务器运行已停止安全更新的 Ubuntu 16.04 长达 5 年，大量互联网基础设施长期处于'僵尸运维'状态，若被恶意利用可能成为
    DDoS 跳板或数据泄露源头，构成公共网络安全隐患
  additional:
  - FreeBSD Jails 作为 Docker 替代方案的叙事可能吸引部分'反复杂化'开发者，但其社区规模和商业支持远不及容器生态，存在人才断档和工具链断层风险
  - 个人博客迁移故事虽小，但折射出开发者对云成本敏感度上升和'去大厂依赖'的心态转变，可能加速中小型项目的多云/混合云策略
confidence:
  impact: low
  compound: low
  hype: low
actionable_insight: speculative_watch
---

This blog has been running on a Digital Ocean VPS for over ten years. A machine hosted in New York City, running **Ubuntu 16.04 LTS**. An LTS that hasn’t been in support for at least 5 years. It was about time to change it. After some considerations, I migrated to a Hetzner virtual machine that is way better than my old Ubuntu one, less than half the price of what I used to pay, and just across the country from me. Not only that, but I took the challenge to move my stack to **FreeBSD**. It’s a long text, but stay for a cool introduction of *FreeBSD Jails* with *Bastille* and some interesting site load benchmarks.

# Motivation

If you know how releases on Ubuntu work (I’m not very familiar myself), once the release is out of support, the apt package repository is out, so you can’t get any updates from it anymore. There are several implications of running such an outdated system, and the most obvious is that your server is just not as secure anymore. There might be several bots out there just trying to find nodes with vulnerabilities to introduce malicious stuff onto them. Luckily (I think), nothing ever happened. Not that there was anything important to be stolen in there either way. But I remember a long time ago, one WordPress blog that I had, which was also running on an old VPS, randomly got a lot of very suspicious links to casino and gambling spread across the text in the posts.

I was already using a Hetzner VPS as a remote development machine, where I SSH into from anywhere, and it’s been a reliable good VPS for the price. So I decided to start by comparing the specs. This was the droplet running my blog and my other websites:

My old Digital Ocean server

That has 2GB of RAM, one vCPU, 50GB disk, 2TB of monthly traffic and runs Ubuntu 16.04 x64. It’s located in their datacenter in New York City. That’s probably why it’s so expensive, I was paying $13 monthly for that.

Hetzner is an established European IT company and has big data-centers in Germany, where I live. The cheapest Hetzner server I could get, at only **3.56** euros is already way better than my old one:

A cup of coffee per month

Double the memory and CPU, slightly less storage space, but ten times more traffic. But I decided to go with a beefier setup, for less than €6 a month:

A *fancier* cup of coffee per month

It might even be a bit overkill for my sites, but why not?

## The old setup

My old setup was serving a few more sites than just this blog. Nothing too popular; this blog, the most popular of all sites in there, wouldn’t get more than a couple thousand page views a month. Except when a couple of posts went viral on Hacker News, there wasn’t a lot of traffic. In the end, the machine was basically serving static sites, no fancy CGI or custom code running. The stack was simple. Everything was served with **nginx/1.10.3**, statically. So I’d just basically have several config files in `/etc/nginx/sites-available`

for each one of the sites. Extra necessary programs like static site generators and a LaTeX suite (e.g.: this blog is generated by **Hugo**) were installed either via `apt`

or `snap`

. In fact, my process to update my blog was:

- write the text locally
- commit and push to the repository
- ssh into the server
- pull the repo updates
- run
`hugo`


During the first years of this VPS, I also used it to run some tests and do some programming. So it was bloated with a lot of outdated software that I didn’t use anymore. But it worked. And worked quite well.

Yep, it was running Linux 4.4!

So well, in fact, that its uptime was 1491 days when I shut it off! That’s roughly 4 years without interruption!

## Why FreeBSD

Not gonna lie, one of my main motivations was to get my hands on something different. I’ve been reading and watching a lot of stuff about BSDs in general, and I had a short previous experience with FreeBSD, so I thought it would be a good way to put it to a real-world test. FreeBSD is usually praised for its stability, due to its integrated design, security, and **Jails**. We’ll get to that in a bit.

I don’t wanna sound like I knew exactly what I was doing, but when I read about **Jails**, I knew exactly what I wanted to do. **Jails** is a form of virtualization/containerization that’s been part of FreeBSD for over 25 years, way before Docker was even a thing. At first glance, it does exactly what you’d expect from a Docker container: it sandboxes a “minisystem” within it so you can run stuff that doesn’t have access to your host system. The main difference, I think, is that Docker and other container solutions are more suited for “packaging programs”. It’s ephemeral and immutable. It will operate on data that comes from outside the container, but within it, everything will always be the same. Whereas Jails are really subsystems, almost like mini-VMs, but that are in reality sharing the same kernel.

On top of that, its filesystem, **ZFS**, is actually really good and useful for servers. If you come from a Linux world, you probably have heard about **Btrfs**, which is the newer filesystem that’s been adopted by more and more distros lately. It has some similarities to ZFS: data integrity and snapshots. Except **ZFS** is probably way more mature than Btrfs. If I take frequent snapshots of my system, I don’t need to rely on the VPS provider snapshot or backup system, which I have to pay extra.

My idea was to have one Jail for each one of my sites with whatever tools they needed to build (like **Hugo**, for the blog) and an instance of nginx to serve it. And one Jail for the main web server that connected all of them with the world via reverse proxy. That way, if one of the jails get compromised, I can just destroy it and create a new one. I’ll get more in detail how to set them up.

## Hetzner VPS

Here are more details about it, for all you *fetchists*:

I don’t know why fastfetch always report more memory being used than the actual values. I’ve never seen more than 3GiB used in btop for this server

# Setup

I’ll go through quickly how I set this server up and what the most important points are. I usually keep a dev journal, so I was documenting as I was doing. However, I wouldn’t take this as a guide because I might have had missed steps. This is more of a taste of what it was to set up a web server with FreeBSD on Hetzner.

## Installing FreeBSD

Hetzner offers some images upon the creation of the VM, but they’re fairly limited:

No BSD

But I saw a guide explaining how to install it on Hetzner from the official FreeBSD YouTube channel. Totally recommend the channel, by the way.

The thing is that Hetzner actually provide the FreeBSD image, but it’s just hidden, a couple of steps away. It offers as an ISO image. So, when prompted to select an OS image in the creation process, you just need to pick any, then you’ll eventually wipe it all out. After creating the VM, all you need is to go to the **ISO Images** tab in the Console and mount the image you want:

FreeBSD ISO Images available

I picked **14.3**. And rebooted. Then I basically followed the installer. Don’t remember if I changed anything from the standard options, but I was following the install video from the official FreeBSD channel. Boom, in no time, I had the system installed and running.

### Bastille

I mentioned Jails a few times already. But I’m not only using Jails, but also **Bastille**, a system that helps managing Jails. The thing is that creating Jails by hand is a bit more complicated than I would like. There are several different steps that need to be taken care of individually, and for every new Jail created. Bastille simplifies that and offers everything you need one command away from `bastille`

. Such as `bastille list`

to show all the jails in the system, `bastille create`

to create a new one, `bastille console`

to open a shell in a jail, etc.

Installing and enabling it is (almost) as easy as:

```
pkg install bastille
sysrc bastille_enable="YES"
```


There are also other Jail managers, I just went with the one with the coolest name.

## The Stack

The whole idea is having a Jail running **Caddy** to serve all the sites and deal with domains and their SSL certificates. Then each site will have its own jail with whatever is necessary for them to build and serve. The sever jail will reverse proxy all the traffic to the respective jails. So the first thing needed is to configure an internal virtual network adapter. We can think of this stack as something similar to a bunch of virtual machines in a network.

To set up a virtual network interface:

```
sudo sysrc cloned_interfaces+="lo1"
sudo sysrc ifconfig_lo1_name="bastille0"
sudo service netif cloneup
sudo sysrc ifconfig_bastille0="inet 10.0.0.1 netmask 255.255.255.0"
```


It basically clones a loopback interface, names it “bastille0” and assigns network parameters to it. The jails will work on that network interface, only. The caddy jail will have to access to the outside world, since that’ll be the one listening to the requests. For that, we need to create some internet access rule using PF (Packet Filter), FreeBSD’s *firewall*.

We need to edit `/etc/pf.conf`

:

```
# the main interface `vtnet0` and the virtual one we created `bastille0`
ext_if = "vtnet0"
int_if = "bastille0"
vpn_if = "tailscale1"
# skip internal traffic
set skip on $int_if
set skip on $vpn_if
# allow outbound access to the internet from the jails
nat on $ext_if from 10.0.0.0/24 to any -> ($ext_if)
# redirect HTTP/HTTPS traffic from the web to the server jail (10.0.0.5)
rdr pass on $ext_if proto tcp from any to any port {80, 443} -> 10.0.0.5
# block everything else
block all
# allows outbound traffic from host
pass out quick on $ext_if keep state
```


As commented in the config, it’s basically setting all internal traffic on our `bastille0`

and `tailscale1`

networks; then setting up outbound traffic for our jails and host system; and then redirecting all the `80`

or `443`

(HTTP and HTTPS) traffic to the internal ip `10.0.0.5`

, which will be our Caddy server.

Now we need to enable PF:

```
sysrc pf_enable="YES"
service pf start
sysrc gateway_enable="YES"
```


That’s all for the networking stack. Let’s create the Caddy server jail.

### Creating the first Jail: Caddy Server

My old server ran on good old `nginx`

. Except for a bit of `Apache`

, I ran nginx for most of my life. But there’s an annoying thing with nginx that `Caddy`

solves swiftly: SSL certificates. Back in my old server, I’d have to run `certbot`

every now and then to renew the domain SSL certificates, and I missed renewals more often than I’d like. Caddy deals with that automatically.

To create a new jail, first we need to bootstrap with the version of FreeBSD we’ll be using, in my case it’s `14.3-RELEASE`

:

```
bastille bootstrap 14.3-RELEASE
```


Then we create the actual jail:

```
bastille create caddy 14.3-RELEASE 10.0.0.5 bastille0
bastille start caddy
```


We create a jail named `caddy`

, using `14.3-RELEASE`

, with ip `10.0.0.5`

on the `bastille0`

interface.

To check the state of the jail:

```
# bastille list
JID Name Boot Prio State Type IP Address Published Ports Release Tags
3 caddy on 99 Up thin 10.0.0.5 - 14.3-RELEASE -
```


There, it’s already running! Remember, jails are not supposed to be *ephemeral* like a Docker container, where you set up the whole config of the container and just start it and expect the machine to be exactly the same forever. We’re almost dealing with virtual machines here. We can access a shell at any moment with:

```
# bastille console caddy
[caddy]:
root@caddy:~ #
```


#### Setting up the Caddy Server

Since we’re already within the `caddy`

jail, we just need to install Caddy:

```
pkg install caddy
sysrc caddy_enable="YES"
service caddy start
```


All the configuration for Caddy will be in `/usr/local/etc/caddy/Caddyfile`

, within the jail. If we want to be able to access that config file from the host system, we need to mount a directory from the host system into the jail. We can even do it in read-only mode, so the jail can’t change the config. It’s something like:

```
bastille mount caddy /usr/local/etc/my-caddy-config /usr/local/etc/caddy nullfs ro 0 0
```


Ok, the server is almost all configured, but we don’t have a site yet. So let’s create a site jail, and then we go back to config Caddy.

## The first site: *es.cro.to*

Back during the Pandemic, the Brazilian President decided to act as if Covid-19 was just a cold and didn’t enact any urgent policies for lockdowns. He was constantly saying that the country wouldn’t stop because it couldn’t afford it, and if some people had to die, they would. Completely ignoring Science and even commonsense. History proves how wrong he was. Unsatisfied with that, I wanted to *“protest”*.

So I created a small page `es.cro.to`

, which literally means “scrotum” in Portuguese, but is often used to describe someone who is a *scumbag*, an *asshole*, or something like that. I got the domain `cro.to`

(which in retrospect, is really cool and sounds rather nice in English) and added a subdomain `es`

. It’s divided in the exact syllables of the word, just like you find in dictionaries, so I added both the definitions of the word and a picture of the creature:

escroto

It was, of course, being hosted by my old server, and got quite big traffic during that time of lockdown. I decided to start with it, after all it’s just one page with a terribly compressed photo, and it’s not really that relevant at the moment anymore.

That site is a git repository, just like all the other sites I’ll run. So I prepared to have all the sites in `/usr/local/www`

in the host system and then just mount the specific site directories to their respective jails, read-only. So once I had this site in `/usr/local/www/escroto`

, I proceeded to create the jail with bastille. This time, I’ll be using a bastille template for nginx: `www/nginx`

. Templates are just small scripts that pre-installs some software. I didn’t have to do it, but why not?

```
bastille bootstrap https://github.com/bastillebsd/templates
bastille create escroto 14.3-RELEASE 10.0.0.11 bastille0
bastille template escroto www/nginx
```


I created it using IP `10.0.0.11`

. We’ll need that in a second. At this point, that jail’s nginx is already serving the nginx default page. And it’s located at `/usr/local/www/nginx`

(note that FreeBSD puts almost everything in `/usr/local`

).

Then I mounted the host’s website directory to the jail with:

```
bastille mount escroto /usr/local/www/escroto /usr/local/www/escroto nullfs ro 0 0
```


Now, from within the jail I can access the site in `/usr/local/www/escroto`

. Since it’s a git repo, it has files (`.git`

) that shouldn’t be served. So I wrote a `deploy.sh`

script to copy the contents of `/usr/local/www/escroto/*`

to `/usr/local/www/nginx/*`

and delete the `.git`

directory:

```
rm -fr /usr/local/www/nginx/*
cp -R /usr/local/www/escroto/* /usr/local/www/nginx/
rm -fr /usr/local/www/nginx/.git
```


The idea is that every time I need to deploy a new version of that site, I’ll log into my host server, update the repo and run that script:

```
cd /usr/local/www/escroto
git pull
bastille cmd escroto /root/deploy.sh
```


I ended up adding a `/root/deploy.sh`

script to all my other sites there too.

#### Setting Caddy’s domain to point to that jail

Back to the Caddy config:

```
cro.to {
redir https://es.cro.to{uri} permanent
}
es.cro.to {
reverse_proxy 10.0.0.11
}
```


Really simple config. Serve the main domain to redirect to `es.cro.to`

, and then reverse proxy to the IP `10.0.0.11`

, the `escroto`

jail.

After configuring the DNS records, the site was already online.

# Deploying this Blog

This blog uses **Hugo** and is a git repository on GitHub. So I cloned it in `/usr/local/www/blog`

and created a new Jail, just like `escroto`

:

```
bastille create blog 14.3-RELEASE 10.0.0.12 bastille0
bastille template blog www/nginx
bastille mount blog /usr/local/www/blog /usr/local/www/blog nullfs ro 0 0
```


Then I installed Hugo within the jail with:

```
bastille pkg blog update
bastille pkg blog install gohugo
```


The deploy script is rather similar:

```
rm -fr /usr/local/www/nginx/*
cd /usr/local/www/blog
hugo -d /usr/local/www/nginx
```


Before I moved over from the old server, I wanted to do some benchmarks, so I assigned the blog to my old domain:

```
crocidb.cro.to {
reverse_proxy 10.0.0.12
}
```


And just as simple as that, my blog was being served on my new server.

# Benchmarking my Servers

Before I updated my DNS records, I wanted to check if the new server was going to hold the traffic. I mean, on paper it would, but I wouldn’t know if I messed some step. So I set out to find ways to benchmark my sites `crocidb.com`

pointing to the old server vs `crocidb.cro.to`

.

First I started by thinking *what* I wanted to test. Testing latency is useless because I know that for the majority of the people accessing my blog it would be slightly longer. Usually most of the traffic of this site comes from North America, followed by Europe and then South America. But it really shouldn’t affect the experience. So it’s better to test serving speed and big loads.

There are some free online tools that can do general tests, like GTMetrix, Pingdom and WebPageTest. But honestly the differences between the two servers were mostly only the latency. All the rest was pretty much the same. So I had to go a bit deeper.

I found out about wrk and hey. Two different tools to benchmark HTTP load. They’ll basically generate thousands of concurrent requests to the website and collect information such as the latency of the requests, error responses, transfer per second, etc. For example, I ran `wrk`

on another VPS in Hetzner:

```
wrk -t4 -c100 -d30s --latency https://crocidb.com/
```


This tells `wrk`

to run in `4`

threads, to keep `100`

concurrent requests for `30`

seconds. Not really an unrealistic number. The results were:

```
Running 30s test @ https://crocidb.com/
4 threads and 100 connections
Thread Stats Avg Stdev Max +/- Stdev
Latency 89.63ms 18.31ms 189.09ms 95.29%
Req/Sec 211.74 38.44 313.00 87.69%
Requests/sec: 833.41
Transfer/sec: 8.29MB
```


On `crocidb.cro.to`

test:

```
Running 30s test @ https://crocidb.cro.to/
4 threads and 100 connections
Thread Stats Avg Stdev Max +/- Stdev
Latency 6.75ms 3.59ms 51.98ms 74.41%
Req/Sec 3.08k 260.11 4.34k 81.83%
Requests/sec: 12260.10
Transfer/sec: 130.80MB
```


The old server handled `833`

requests per second vs `12,260`

on the new server. With a latency average of `89ms`

vs `6ms`

. But of course that was not fair: the test machine was in the same data-center as my new server. So I thought… what if I use a VPN and do the tests from several locations?

I use Proton VPN, so I wrote a quick script that would get a location from a list, connect, and run `wrk`

. The results were absurdly underwhelming. It recorded an average of `300`

requests per second on the old server and `800`

on the new one, using these locations:

```
LOCATIONS=(
"US//New York|US - New York"
"US//Los Angeles|US - Los Angeles"
"BR//São Paulo|BR - São Paulo"
"GB//London|GB - London"
"DE//Frankfurt|DE - Frankfurt"
"FR//Paris|FR - Paris"
"SE//Stockholm|SE - Stockholm"
"CH//Zurich|CH - Zurich"
"IN//Mumbai|IN - Mumbai"
"JP//Tokyo|JP - Tokyo"
"KR//Seoul|KR - Seoul"
"SG//Singapore|SG - Singapore"
"AU//Sydney|AU - Sydney"
"ZA//Johannesburg|ZA - Johannesburg"
"AR//Buenos Aires|AR - Buenos Aires"
)
```


So I ditched the idea of using an end-user VPN. I decided to go for a more robust solution: create real VPS on data-centers across the world.

### Vultr VPS Benchmarks

I needed a different VPS provider than the ones hosting my servers to avoid any infrastructure advantage. The only other VPS provider I’ve ever used outside DigitalOcean and Hetzner was Vultr. Then I decided to create a server for each location and run the tests. I settled for only four different regions, because the process was manual: **London**, **São Paulo**, **Silicon Valley** and **Tokyo**. So I created 4 of the cheapest Fedora VMs available in those locations.

After several tests, I found out that `hey`

was more aligned with what I wanted to do. So my work was basically to ssh into the server, run this script and then copy the results. I started with São Paulo:

```
dnf install -y tmux vim htop
wget https://storage.googleapis.com/hey-releases/hey_linux_amd64
chmod +x hey_linux_amd64
./hey_linux_amd64 -n 1000000 -c 10000 -t 10 -z 5m -h2 https://crocidb.com/ > crocidb.com.log
./hey_linux_amd64 -n 1000000 -c 10000 -t 10 -z 5m -h2 https://crocidb.cro.to/ > crocidb.cro.to.log
```


It downloads `hey`

, runs it with these unrealistically heavy numbers: `1M`

total requests, `10k`

concurrent requests, `10s`

timeout (hey would stop if any particular request took longer than 10 seconds) and a total of `5m`

.

On the very first try, I noticed a real problem with my new FreeBSD server. It was failing rather early, because it couldn’t handle 10k concurrent connections. After a lot of research, I found out that you can check the size of the socket queue with `netstat -Lan`

, and it was all `128`

. Turns out `kern.ipc.somaxconn`

was stock-set for that number. So I increased it:

```
sysctl kern.ipc.somaxconn=16384
```


After roughly 10 minutes running, my logs were ready and I went ahead and looked:

Comparison of the output of `hey`

for both of the servers in the São Paulo VPS

Left side is the old server and right one is the new one. The difference is mindblowing.

While both servers returned a substantial amount of errors, the FreeBSD managed to respond to the expected `1M`

requests, while the Ubuntu one couldn’t return `20k`

! That’s a **MASSIVE** difference.

### Benchmark Analysis

crocidb.com was running on the old server, while crocidb.cro.to was on the new one

The fact that the old server could only finish a few of the requests is mindblowing. In fact, it only completed around 7% of them, versus 94% of the FreeBSD server. There is a slight decrease of success rate in the new server on Tokyo, but nothing to worry about, I think.

Considering the amount of requests per second, the new server is at least 3x better and at most 11x!

Requests per second: the higher the better

Here the variation looks even more dramatic, and my guess is that the latency was much bigger in Tokyo?

Latency Percentiles: `p90`

is especially interesting because it measure that **90%** of the users will experience less latency than that value

Looking at the latency percentiles (e.g.: `p50`

means 50% of requests were answered faster than that value), we see an interestingly different shape for each server. The new one has a more *linear* growth until around 90%, which makes it more predictable, while the old server grows more unpredictably.

That shows me that 90% of people trying to load the main page of my blog will get the content in less than **3.5** seconds, from pretty much anywhere in the world, even under high demand. That’s pretty good.

I didn’t go far enough to understand the issue with Tokyo, but I’m not that worried at the moment. Using the request phase breakdown, where `hey`

analyzes the duration of each step of the request, there’s an indication that the traffic to Japan is slower:

The breakdown of the time it took on each phase of the request

But this data looked way off to me. First because the DNS dial-up and lookup are incredibly low on the second domain. Maybe because it’s a CNAME record? And second because `resp wait`

(pretty much time to first byte) and `resp read`

(transfer time) were weirdly high here. But that could be explained by the fact that it’s only counting successful requests, which can indicate that the first server was quick at first until it basically shut down any new requests.

#### Conclusion

I don’t think this difference has to do specifically with the stack I picked. It’s probably because of misconfiguration on the old Ubuntu system and the fact that the Hetzner VPS I picked has 4 cpu cores, vs one in the DigitalOcean one: much more requests can be processed concurrently. I also don’t think that means a lot either, since it’s very unlikely these servers would ever need to serve that many requests at the same time. Maybe just one web benchmark like WebPageTest would’ve been enough.

# Biting the Bullet

Although the benchmark left many unanswered questions, I was really happy with it. So I went ahead and updated the DNS records. This is now officially running on that machine.

In the end, after many hours experimenting, tinkering, building, and breaking stuff, I figured that it isn’t that complicated to set up a FreeBSD site hosting machine. There are several web hosting services satisfying my constraints that I could’ve used instead. Or I could have installed Proxmox to deal with my containers and admin my system with a visual dashboard. Or even Sylve, the FreeBSD counterpart. But I like the path I took, because I learned a lot throughout it.

Some of the main takeaways:

- The Ubuntu server was really sturdy. It handled really well all the load in my sites for ten years. Four of the last ones without even a reboot. That all without much effort to set it up.
- Configuring FreeBSD was easier than I thought. I like the idea of centralizing all the system configuration in one place. Also, the online documentation is really good.
- Configuring a machine to host your own blog can require a lot of knowledge of networking that goes way beyond what a gamedev knows.
- I had so much fun learning another system. Maybe next time I’ll do OpenBSD or NetBSD.

In the end, this is all useless, since most of my traffic comes from AI systems crawling it anyway…