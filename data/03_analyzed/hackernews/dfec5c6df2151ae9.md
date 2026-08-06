---
title: 200 Milliseconds
source: https://200ms.thenodebook.com
author:
- '[[dimitarpanov]]'
published: '2026-08-01'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: 'Article URL: https://200ms.thenodebook.com Comments URL: https://news.ycombinator.com/item?id=49132992
  Points: 272 # Comments: 80'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dfec5c6df2151ae9
source_type: community_discussion
tldr: 这是 thenodebook.com 推出的交互式教学页面，用精确时钟和可视化动画完整还原一次点击购买按钮后、一个 HTTP POST 请求在 200
  毫秒内从触控板经 DNS 解析、TCP/TLS 握手抵达弗吉尼亚州服务器的全过程。
objective_summary: 《200 Milliseconds》是 thenodebook.com 发布的交互式教学页面，以时间轴形式拆解一个 HTTP
  POST 请求的完整生命周期。请求从旧金山笔记本的触控板出发，经 Wi-Fi、运营商与 4700 公里光纤到达弗吉尼亚州 Ashburn，负载均衡器将其转发给一台
  AWS 上已运行 23 天的 Node.js 进程（PID 1447），并访问 0.35 毫秒外建筑内的 Postgres 数据库。页面详细讲解了 Chrome
  多进程架构、HSTS/CSP 策略、DNS 解析链与 anycast、TCP/TLS 握手等底层原理，统计显示建连与握手耗时 127 毫秒、服务器处理 3 毫秒、飞行与绘制
  74 毫秒。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Amazon
  - AWS
  - Verisign
  - Route 53
  technologies:
  - TCP
  - TLS
  - DNS
  - HSTS
  - CSP
  - HID
  - BGP
  - Anycast
  - Node.js
  - Postgres
  - CDN
  - HTTP
  - UDP
  key_people: []
key_logic_flow:
- 请求从触控板电容变化开始，经过 HID 驱动、窗口服务器、Chrome 浏览器进程与渲染器的命中测试，在约 0.8 毫秒内触发 fetch("/api/checkout")
  的 POST 请求。
- Chrome 依次执行 HSTS preload、混合内容检查、CSP connect-src 三项策略，并确认内存缓存、Service Worker 与 HTTP
  磁盘缓存均不为 POST 请求服务。
- 浏览器缓存与操作系统缓存都没有 DNS 记录，请求经由 anycast 地址到达解析器，从缓存中获得 TTL 212 秒的 A 记录答案，解析过程耗时约 2 毫秒。
- 冷连接需要新建 TCP 连接并在其上完成 TLS 握手，跨美三个往返共约 127 毫秒，之后请求才真正进入网络飞行阶段。
- 负载均衡器将连接转发给 AWS 上已运行 23 天的 Node.js 进程 PID 1447，服务器与隔壁建筑中 0.35 毫秒外的 Postgres 数据库共同处理这次
  22 字节的请求。
- 文章时间线统计显示：建立连接与握手占 127 毫秒、服务器处理占 3 毫秒、飞行与绘制占 74 毫秒、浏览器端占 5 毫秒，总体在 211.4 毫秒内完成往返。
object_mentions:
- object_type: project
  name: 200ms.thenodebook.com
  canonical_name: The Node Book
  url: https://200ms.thenodebook.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该页面来自 thenodebook.com，是一个以交互方式讲解 Node.js 与网络底层原理的在线项目，文章标题为《200 Milliseconds》。
  - 页面用精确到 t=0.211400 秒的时钟，从触控板电容变化开始逐步还原一次点击购买按钮后 HTTP 请求穿越网络的完整过程。
  article_id: dfec5c6df2151ae9
- object_type: product
  name: Route 53
  canonical_name: AWS Route 53
  url: https://aws.amazon.com/route53/
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文中说明 thenodebook.com 的记录存放在从 AWS 租用的 Route 53 托管 DNS 上，由它返回 TTL 为 300 秒的 A 记录。
  - DNS 解析链的第三层由 Route 53 承接，解析器从根服务器经 .com 服务器逐级下探后，最终在 Route 53 处取回 A 3.213.44.7。
  article_id: dfec5c6df2151ae9
extract_result: success
impact_score:
  score: 3.5
  reason: 评分依据：这是一款高质量的交互式网络教学页面，而非 AI 产品发布、融资或范式转移事件。其短期行业冲击力集中在开发者社区的口碑传播与教学价值——时钟精确的请求全链路还原、深度的网络协议讲解很可能在
    Hacker News 等社区引发热议，并树立交互式技术教育的新标杆，但不会改变任何竞争格局、技术路线或商业生态，故属于社区层面的亮点事件而非行业级冲击。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 200 毫秒请求全链路的可视化精度与时钟驱动的交互叙事
hype_assessment:
  level: low
  reason: 判定依据：全文以 verified_fact 的已验证事实呈现，用精确时钟和真实协议细节（HSTS/CSP、DNS anycast、TCP/TLS
    握手 127ms、服务器处理 3ms）逐层展开，未出现'颠覆''革命性'等 PR 滥用词汇，也不涉及任何商业产品的夸大宣传，属于实打实的技术科普内容，无水分。
information_entropy: high
domain_disruption:
  technical_innovation: 非 AI 领域的技术突破，其工程亮点在于把一次真实 HTTP POST 请求的 200 毫秒生命周期做成确定性、时钟精确的可视化叙事——涵盖
    HID 驱动、窗口服务器、Chrome 多进程命中测试、HSTS/CSP 策略、缓存链路、DNS anycast、TCP/TLS 握手、负载均衡转发与 Postgres
    时延等全栈细节，代表了交互式技术教育在保真度与信息密度上的新高度。
  business_model: 以高保真交互叙事作为开发者教育与内容营销的新形态，通过'一次点击背后的 200 毫秒'建立专业品牌势能，为 thenodebook
    后续的付费课程、开发者工具或技术文档服务积累口碑与流量，本质上是优质内容驱动开发者生态的获客路径，尚未形成可直接量化的商业模式冲击。
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 这是一个高质量的交互式技术科普页面，而非可商业化的产品。从资本视角严格评估：TCP/TLS/DNS/CDN 等网络底层原理属于半衰期极长的知识，优质讲解内容具有典型的'慢热、长尾'复利属性，可长期作为教学参考被引用，对
    thenodebook 的品牌与 SEO 资产有持续沉淀价值。但该事件本质是单页创意内容（single-page），缺乏平台化、系列化或可订阅的产品形态，无法形成
    DevTools/Infra 那种可估值、可增长的商业飞轮；其商业闭环仍依赖 thenodebook 后续的 Node.js 课程转化，且科普内容本身不产生直接收入或定价权。因此评分落在
    4-5 区间：有潜力成为开发者教育细分赛道的一个常青参考节点，但复利效应受限于内容形态，能否转化为基础设施级资产需观察其能否沉淀为系列产品并建立稳定流量入口。
value_capture_layer: cloud_platform
moat_impact: democratizes_access
key_beneficiaries:
- thenodebook
- AWS
- Route 53
- Postgres
- Node.js
competitive_casualty:
- 低质量付费技术教程
- 传统网络运维培训内容
market_opportunities:
- AI 基础设施与开发者工具团队可借鉴《200 Milliseconds》的"精确时钟+时间轴动画"叙事手法，将 LLM 推理链路（输入预处理、上下文检索、token
  生成、流式返回）的逐段延迟拆解为可视化教程，用于技术品牌建设与开发者获客
- 可观测性/APM 平台可参考该页面把 DNS/TCP/TLS/服务端/数据库全链路可视化的思路，将真实请求追踪做成交互式链路剖析界面，降低开发者理解分布式系统的门槛，形成差异化卖点
- 技术内容创作者可围绕"复杂系统延时解剖"题材（如数据库查询、Kubernetes 调度、GPU 集群通信）复刻该叙事格式，为云厂商与 AI 公司提供定制化开发者教育内容，形成可持续的内容服务模式
risk_matrix:
  regulatory: 无
  technological: 页面中的 TCP/TLS/DNS 等协议细节随 HTTP/3、QUIC 与 TLS 版本演进会部分过时；若被当作当前 Web 栈教材使用，需注意时效性校验与版本标注
  competitive: 交互式技术科普叙事形式的复制门槛较低，云厂商与开发者工具公司可快速模仿，内容差异化窗口有限；需要依靠持续的新题材产出与品牌沉淀来维持影响力
  ethical: 无
  additional:
  - 该页面本质是 thenodebook.com 的产品营销内容，教育价值与商业推广意图交织，读者宜将其视为案例演示而非系统性学习教材
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: 200ms.thenodebook.com
  canonical_name: The Node Book
  url: https://200ms.thenodebook.com
  positioning: 一个用精确时钟与可视化动画还原 HTTP POST 请求在 200 毫秒内穿越网络全过程的交互式教学页面，聚焦 Node.js 与 Web
    底层原理科普。
  technical_signal: 以 t=0.211400 秒精确时钟拆解请求全程，量化建连握手 127 毫秒、服务器处理 3 毫秒、飞行与绘制 74 毫秒，并讲解
    Chrome 多进程、HSTS/CSP、DNS anycast 与 TCP/TLS 握手原理。
  adoption_signal: null
  ecosystem_relevance: 项目将 Node.js 服务端、Postgres 数据库与 Chrome 浏览器链路串联成完整技术栈图谱，对 Web
    开发者生态具有通识教育价值。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该页面以可观测的精确时序把浏览器、网络与服务器三层知识整合进一个真实请求场景，教学形态新颖且信息密度高，值得跟踪其后续是否扩展为系列课程或开源可复用组件。
  risk_notes:
  - 作为一次性发布的静态教学页面，其内容与精度依赖人工打磨，后续维护与更新的持续性存疑。
  - 页面中 127 毫秒握手耗时等数据基于特定网络路径实测，不代表一般网络条件下的普遍表现。
  score: 7.0
  article_ids:
  - dfec5c6df2151ae9
  evidence_snippets:
  - 该页面来自 thenodebook.com，是一个以交互方式讲解 Node.js 与网络底层原理的在线项目，文章标题为《200 Milliseconds》。
  - 页面用精确到 t=0.211400 秒的时钟，从触控板电容变化开始逐步还原一次点击购买按钮后 HTTP 请求穿越网络的完整过程。
- object_type: product
  name: Route 53
  canonical_name: AWS Route 53
  url: https://aws.amazon.com/route53/
  positioning: AWS 提供的托管式权威 DNS 服务，在 DNS 解析链中处于末端，直接为 thenodebook.com 等域名返回权威 A 记录。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 部署在 AWS 上的 Web 应用团队
  - 需要托管域名解析的开发者与企业
  product_signal: 文中 Route 53 作为解析链末端的权威 DNS 直接返回 TTL 300 秒的 A 记录，在真实请求链路中验证了其托管 DNS
    的可用性与低延迟响应能力。
  market_signal: null
  differentiation: 相较于自建 DNS 或他云服务，Route 53 以托管方式承接权威解析职责并深度绑定 AWS 生态，但文中未给出与其他 DNS
    方案的直接对比依据。
  watch_reason: 作为 AWS 基础设施的核心组件，Route 53 频繁出现在此类底层请求链路拆解内容中，其解析速度与稳定性直接影响 Web 应用的首字节时间，值得跟踪其产品演进与故障事件。
  risk_notes:
  - 文中仅将其作为 DNS 链路的一环引用，未提供与其他 DNS 服务的性能对比，难以据此评估其相对优势。
  - 若 Route 53 出现解析延迟或故障，将直接影响依赖它的站点可用性，但此类风险在文中未展开讨论。
  score: 4.0
  article_ids:
  - dfec5c6df2151ae9
  evidence_snippets:
  - 文中说明 thenodebook.com 的记录存放在从 AWS 租用的 Route 53 托管 DNS 上，由它返回 TTL 为 300 秒的 A 记录。
  - DNS 解析链的第三层由 Route 53 承接，解析器从根服务器经 .com 服务器逐级下探后，最终在 Route 53 处取回 A 3.213.44.7。
---

from thenodebook.com

the rules of this page

Scroll down. The story and the clock both advance.

The clock at the top is exact. It ends at t = 0.211 400 s.

When the story pauses for a lesson, the clock at the top freezes and turns white. Keep scrolling; it picks the story back up.

Violet marks the data as it moves, always top to bottom. Nothing else on the page uses that color.

the cast

The request makes seven stops, top to bottom on the line below. The laptop is on the shop's Wi-Fi. The access point on the ceiling receives its radio signal and sends it on over a wire. The ISP the shop buys its connection from carries the traffic out to the wider internet, then onto 4,700 km° of glass fiber between here and Virginia.

san francisco → ashburn · follow the violet dot

In Ashburn, a load balancer accepts each incoming connection and forwards it to one of the four node processes behind it. Ours lands on PID 1447, a Node.js process on a rented Amazon machine, deployed 23 days ago.° Postgres, the database, runs in the building next door, 0.35 ms° away. All seven handle the same 22 bytes before the screen changes.

next · the clock starts

act 1 - t = 0 → 5 ms

Five milliseconds of hardware and browser bookkeeping before a single byte leaves the laptop.

milliseconds pass here

the tap — inside the touchpad

The click starts as a change in an electric field.

Δ capacitance at col 9, row 2: threshold crossed

the delivery chain — touchpad to chrome

touchpad controller

capacitance dip → interrupt raised

hid driver

report: x 512 · y 288 · button 1 down

HID is the generic protocol shared by keyboards, mice, and touchpads, so a single driver reads them all.

window server

frontmost window: chrome

The window server is the OS process that owns the screen and routes each input event to a window.

chrome · browser process

mouse event → renderer, tab 4

Chrome is several processes: a browser process handles the windows, the network, and input; the tab's page runs in its own sandboxed renderer.

hit testing — renderer main thread

Chrome resolves which element you clicked.

html

└ body

└ main

└ section.product

└ div.actions

└ button.buy

hit: <button class="buy"> · 6 boxes deep · ~0.8 ms°

the listener runs

fetch("/api/checkout", {

method: "POST",

headers: {

"Content-Type": "application/json",

},

body: JSON.stringify(

{ sku: "NB-1", qty: 1 },

),

});

parsing the url

The URL is split, then checked.

three policy checks

HSTS preload

passapi.thenodebook.com is on the list → https required

The preload list is compiled into Chrome itself: hosts that must never be reached over plain, unencrypted HTTP. This host is on it, so https applies even on a first-ever visit.

mixed content

passpage and target both https → nothing to block

An https page is barred from loading http resources. Page and target are both https, so there is nothing to block.

CSP connect-src

pass'self' permits this destination

connect-src is the page's own rule for where fetch may call. 'self', the site the page came from, covers this destination.

cleared: POST https://api.thenodebook.com/api/checkout

Three caches are checked, and none of them serves a POST.

memory cache

no entry; POSTs are never stored

service worker

handler ignores POST; pass-through

http disk cache

POST is not stored or served

The images and stylesheets on the page you clicked came from caches closer than Virginia. The day this product launched, the origin, the single server that runs the application, sent each image out once. From then on a CDN, caching servers placed in cities around the world so a copy sits near whoever asks, served every later request from a stored copy. Caching like this is most of the reason the web feels fast, and it does nothing for a request that changes data on the server.

the socket pool

A reusable socket here would save 127 milliseconds.°

what tcp and tls do

The lower layers that carry the bytes make no guarantee about them. Data moves as small independent chunks that can arrive late, doubled, or not at all. TCP numbers every byte, confirms what landed, and resends what didn't, so the code on top reads a single ordered, complete stream.

the wire delivers: #2 · #1 · #1 again · #3 lost, resent

after tcp: #1 #2 #3 - in order, complete

TLS encrypts that stream, so the forty or so machines° between this laptop and Virginia can forward your session cookie without reading it.

the app writes: Cookie: session=9f3ab1

the wire carries: 17 03 03 00 d5 8a 3f c2 91 …

→ open a new connection: TCP first, then TLS on top of it

A socket is the handle your code gets once a connection exists. In Node it is the object net.createConnection returns. You call .write() on it, and it emits 'data' events, while the operating system moves the bytes and tracks the connection's state underneath.

const socket = net.createConnection({

host: "api.thenodebook.com",

port: 443,

});

socket.write(request);

socket.on("data", (chunk) => { ... });

Underneath, a connection is an agreement between two machines to exchange bytes, identified by four numbers: local address, local port, remote address, remote port.

A port lets one machine run many listeners on a single address, much as one Express app routes /api and /admin to different handlers; the machine itself routes port 443 and port 22 to different programs. A port is only a number, 0 to 65,535,° and 443 is the conventional one for https, which is why the rows in Chrome's pool all end in :443.

express routes

app.post("/api/…") → checkout()

app.get("/admin/…") → dashboard()

ports on a single address

port 443 → the https server

port 22 → ssh

port 5432 → postgres

The pool holds these objects after earlier requests finish, in case the same host is needed again. A connection cannot be constructed locally the way an object can, though. The other machine has to agree to it, message by message, from 4,700 km° away, and getting that agreement is the subject of the next two acts.

setup 7 · handshakes 127 · flight + paint 74 · server 3

browser 5 · one crossing 62° · server 3 · paint 25

A kept-alive socket plus a session ticket, a token the server issues so the browser can resume the secure session without repeating the negotiation, together remove the handshakes entirely. Cold means nothing reusable exists yet, while warm means the connection and its keys from last time are still alive. Request #2 makes the same trip in about 95 ms, one crossing of the country instead of six. This page follows request #1, which pays the setup cost that later requests skip; the epilogue returns to this chart.

the request is drafted

Chrome serializes the request.

http is plain text

The whole request is a single string.

029 · Host

the connection reaches a machine; this header says which site on it is meant

088 · Content-Length

the body's length in bytes, so the far side knows when to stop reading

179 · the blank line

an empty line (\r\n\r\n) ends the headers

act 2 - t = 5 → 7 ms

Two milliseconds to turn a name into a place.

≈ 2 ms pass here

from name to number

Routers deliver by IP address, and the URL has a name.

The system that turns name into number is DNS.

the 203 bytes° are still queued in Chrome until the address arrives.

the resolver chain

Neither cache on the laptop has the answer.

browser cache

chrome's list of recent names

os cache

names the OS answered recently

network

ask the resolver · 203.0.113.53

the udp datagram

packet anatomy · rfc 1035

Twelve bytes of header, each bit defined.

id 0x3f2a - a transaction ID chosen at random. UDP has no connections, so this number is how the OS matches the reply to the question. The reply has to echo the same number back. A forger who cannot see the traffic has to guess all sixteen bits, a 1 in 65,536 chance.°

rd 1 - recursion desired. The flag tells the resolver to walk the delegation chain itself and return the final answer. The full walk comes at the end of this act.

the other seven flags - reply and error signaling, all zero on a fresh question.

On the wire the name has no dots.

after the name - the question type and the class. The type is A, a request for the IPv4 address (AAAA requests the IPv6 address instead). The class is IN, for internet, the only class still in common use. After the question, an OPT record carries the largest reply size the sender can accept.

anycast

203.0.113.53 is in dozens of cities at once.

The internet has no central routing table. Each network announces to its neighbors which address blocks it can reach; neighbors forward those announcements with their own network prepended, and a router keeps the best path it has received for each block. The protocol that carries these announcements is BGP, and BGP has no field that records whether two announcements of the same block come from one machine or from forty different ones.

Anycast relies on that missing field. The resolver's operators announce the same address block from dozens of cities on purpose, and the routers in each region, following the same shortest-path selection they always use, deliver traffic to whichever announcement is nearest. The routers need no central coordination, because each one already forwards along its shortest path. DNS works well this way because a lookup is a single UDP round trip that keeps no connection state, so a query that lands at a different site tomorrow still gets the same answer.

the resolver's cache

The answer is already cached.

the answer

3.213.44.7api.thenodebook.com · type A · ttl 212

Three hundred seconds is short on purpose, because the records do change. A server can fail and a backup take its place, or a site can move to a new machine, and each change gives the record a new address. A cache keeps returning the old address until its countdown reaches zero, so the TTL sets the longest an answer can stay out of date. Before a risky change, the usual practice is to lower the TTL ahead of time and wait for the old value to expire.

The answer returns in a single UDP packet and lands at t = 7 ms. Next come the handshakes from last act, which will take several times longer than the name lookup did.

The cached answer exists because another client asked first. Their query found nothing stored, so the resolver walked the full delegation tree, three levels down.

The tree stores the answer in parts, one at each level. The root servers list who runs the top-level domains. The .com servers, operated by Verisign under contract, list the nameservers for names registered beneath it. thenodebook.com's records are stored on nameservers rented from Route 53, AWS's managed DNS. Each level stores only the address of the servers one level down, so the resolver starts at the root and follows that reference from one level to the next until it reaches the answer.

The root is 13 named servers, a count fixed by how many addresses fit in one 512-byte UDP reply back in the 1980s, with more than 1,900 anycast instances behind those names today°. The root replied with a referral, naming the next servers to ask, the ones for .com. Verisign's servers referred it again, to ns-482.awsdns-60.com. That nameserver is itself a name, so the referral included its IP address as a glue record, which spares the resolver a second lookup just to find it. Route 53 then returned the record itself, A 3.213.44.7 with a 300-second TTL. The resolver cached it, and 88 seconds later this request was answered from that cache.

act 3 - t = 7 → 134 ms

A cold connection takes three round trips across the country before the first useful byte.

milliseconds pass here

birth of a socket

socket(AF_INET, SOCK_STREAM, 0) = 41

41 is a file descriptor, a small integer the kernel gives your program to refer to something it opened. Your code passes the number back, and the kernel keeps the real socket on its side. The input, output, and error streams every program starts with are numbered the same way, which is why they are 0, 1, and 2. AF_INET means the socket uses internet addresses. SOCK_STREAM asks for an ordered, reliable flow of bytes, which means TCP.

connect(41, 3.213.44.7:443) = -1 EINPROGRESS

the kernel assigns local port 49732° from the ephemeral range

10.0.0.23:49732→3.213.44.7:443

Two addresses and two ports, the four-tuple that identifies this connection.

The drafted request, POST /api/checkout, 203 bytes°, waits in userspace, the memory where ordinary programs run. Before it can travel, both machines must run the handshake. The SYN goes first, the opening packet of a TCP connection, named for its SYNchronize flag. It carries no data, only the sequence number this side will start counting its bytes from.

the encapsulation peel

Before the SYN can leave the machine, the kernel wraps it in three headers, each one enclosing the last. Below, the layers go on from the inside out, and each is inspected in turn.

Three headers go on before the SYN can leave, each with an address for a different scope.

tcp · program to program - the layer that numbers every byte, collects acknowledgments, and resends anything lost, so your fetch() receives the bytes as one reliable, in-order stream.

ipv4 · across the internet - IP handles addressing. It carries a source, a destination, and the fields each router in between needs to pass the chunk one step closer.

802.11 · the local hop - Wi-Fi’s formal name. Its addresses are set on each radio at the factory and never travel past this room.

TCP - program to program40 B

TCP numbers every byte of the stream. The sequence number says where this packet’s bytes begin, so the far end can put them back in order and notice any that go missing. 2 921 748 316° is the starting value for this connection, drawn at random so a stranger who cannot see the wire cannot forge a plausible next packet. The options are MSS 1460°, SACK permitted, window scaling ×128, and timestamps. The window, 64 240 bytes°, is how much the receiver is prepared to buffer before the sender must pause.

IPv4 - the internet20 B

TTL 64° allows sixty-four router hops before the packet is dropped, and this route uses about seventeen. Total length 60 covers the two headers, with no payload.

802.11 - the local hop34 B + FCS

This header covers only the local hop. Address 1 is the access point, the box whose radio the laptop is exchanging frames with, ten meters away. The hex values are hardware addresses, set on each radio at the factory, and they do not travel past this room. The Virginia address sits in the IP header wrapped inside; this layer never reads it.

802.11 + FCS 38 B

LLC/SNAP 8 B

IPv4 20 B

TCP + options 40 B

0 B

total 106 B

All 106 bytes are headers. A SYN carries no application data; the request is still sitting in userspace.

layers 5 and 6 exist in the model but rarely in practice. real stacks mostly jump from 4 to 7

t = 8 ms - the first hop

The air is one shared channel.

the request stays on the laptop; only the SYN is traveling

other devices’ frames on the same channel

No acknowledgment came back.

backoff 12 slots

slots are fixed microsecond-scale pauses. the radio picks a random count of them and waits that long

attempt two - channel clear

ack

The first ten meters are the least reliable of the whole route.

modem, isp, metro

The neighborhood shares this wire.

coax - shared with the neighborhood

upstream airtime is scheduled

fiber

Copper ends at the headend.

| inside | outside | proto | state |
|---|---|---|---|
| 203.0.113.9:28114 | TCP | SYN_SENT | |
| 10.0.0.87:51204 | 203.0.113.9:41866 | TCP | ESTABLISHED |
| 10.0.0.61:44102 | 203.0.113.9:44102 | UDP | - |
| 10.0.0.19:60310 | 203.0.113.9:60311 | TCP | TIME_WAIT |

The state column is each connection’s phase. SYN_SENT means the handshake is in flight, ESTABLISHED means it is open for data, and TIME_WAIT means it was recently closed and is kept briefly in case late packets arrive.

3.213.44.7 = 00000011 11010101 00101100 00000111the check, first 16 bits match the chosen prefix

the long haul - eastbound

The longest leg of the trip.

sacramento°

km 140

km 400

Every 80 km or so, an EDFA, a doped stretch of the fiber itself, boosts the signal as light, without converting it to electricity. The packet is amplified around sixty times and never becomes an electrical signal on the way.

km 800

meanwhile

On the order of 10^15 bits° cross this fiber every second, spread across dozens of wavelengths, with each wavelength of light carrying a separate channel in the same strand. The SYN’s 106 bytes are a tiny fraction of that.

salt lake city

km 1,040

km 1,200

km 1,600

denver

km 1,700

km 2,000

meanwhile

Two wavelengths over, a video stream is traveling the opposite direction toward a home in Denver. The SYN shares the strand with it for a few hundred kilometers.

km 2,400

km 2,800

chicago

km 3,250

At Chicago the route turns southeast. This crossing has taken more clock time than everything before it combined.

km 3,600

meanwhile

No computer has processed the packet since the regional PoP. For roughly twenty milliseconds it has existed only as light traveling through the fiber.

km 4,000

km 4,400

The packet crosses into Amazon’s network.

t = 39 ms - arrival at the edge

Amazon’s network takes over.

layer 4 - what this API chose

A layer-4 balancer works with addresses, ports, flags, and sequence numbers. It rewrites them, forwards the packet, and tracks the flow. One TCP connection runs unbroken from the laptop to the instance, and the bytes inside pass through without being read.

layer 7 - the alternative

An application balancer would answer the handshake itself. It would terminate TCP and TLS (terminate meaning it acts as the endpoint rather than passing them along), then parse the request, route on the path, and open a second connection inward. That gives per-route rules, retries, and request metrics. It also requires a copy of the certificate, which you inspect at t = 103 ms, and its private key, kept at the edge.

t = 39.5 ms - the SYN meets the kernel

*:443 means any local address on port 443. LISTEN marks a socket that waits for inbound connections rather than opening one of its own. The accept queue holds finished connections until the application collects them with accept(), and that collection is what fires your server’s ‘connection’ event.

The kernel handles the reply on its own.

A SYN is small and its sender keeps no state for it, while the server must hold a queue slot for every one it receives. An attacker who forges the source address and sends a million a second fills the queue with entries that never complete, and real clients are refused. The attack is decades old and still works on a machine that is not prepared for it.

The defense is to keep no state at all. When the queue fills, the kernel encodes the connection's parameters into a number it has to send anyway, the sequence number of the SYN-ACK.° This is a SYN cookie. The client carries the server's state on its behalf.

Real clients return that number, plus one, in their final ACK. The kernel recomputes the keyed hash (keyed means only someone holding the secret can compute or verify it) and rebuilds the connection from the cookie alone. Forged SYNs never send that ACK, so they use the server's bandwidth and none of its memory. The cost is that any options that do not fit in the cookie, such as window scaling and SACK, are lost while the flood lasts.

t = 40 → 71 ms - crossing 2, westbound

Back across the continent.

4,700 km · the same fiber, westbound

EDFA amplifiers - every ~80 km

The request has not moved.

t = 71 ms - established, on one coast

What each of the three messages proves.

a detail, node’s listen backlog

511°

node's default listen backlog

The ACK will carry more than an acknowledgment.

The first is symmetric encryption, where one shared key both encrypts and decrypts, fast enough to protect gigabytes per second.° Its weakness is key distribution. Both sides need the same key, and the only channel available for sharing it is the untrusted wire itself.

The second idea gets around that. A public-key pair is two mathematically linked numbers. Data transformed with one of them can only be reversed with the other. One number is published, and the other is kept secret.

If you encrypt with the public number, only the private number can decrypt, which lets you send a secret to someone you have never met. If you sign with the private number, anyone holding the public number can verify the signature, which is what a certificate uses to prove identity later in this handshake. Public-key math is much slower than symmetric math,° so TLS uses it only to agree, in the open, on one small shared secret, then switches to fast symmetric keys worked out from it.

Over the next two crossings, both sides exchange public values, compute the same secret independently, derive the session keys, and confirm the server is who it claims to be.

t = 72 → 103 ms - crossing 3 · ACK + ClientHello

TLS is the encryption layer of HTTPS.

ClientHello - record 1 · plaintext

cipher_suites lists the client’s options. A cipher suite is a fixed, named set of an encryption algorithm, a tamper-detection method, and a hash, so both sides can pick one and run exactly the same operations. legacy_version claims 1.2 because middleboxes, the firewalls and hotel proxies inserted into the middle of connections, mishandle version numbers they don’t recognize. The version actually in use sits in an extension, an optional added field that old parsers skip. alpn settles which protocol will run inside the tunnel once it is up, plain HTTP/1.1 here.

One field stays readable to everyone.

TLS 1.3 sends its key material immediately.

t = 103 → 134 ms - crossing 4 · ServerHello + certificate

ServerHello - the server’s choices

In the chosen suite, AES-128 encrypts, GCM makes any tampering detectable, and SHA256 is the hash the handshake uses to summarize its messages and derive its keys.

A certificate binds a key to a name.

Certificate - inspected

subject and subjectAltName are the names this certificate covers. ECDSA P-256 is the signature math, the same elliptic-curve family as the key exchange.

E5 is Let’s Encrypt’s day-to-day signing certificate, the middle link. The root is self-signed, meaning no one else signs for it, so it proves nothing on its own. It has to already be in the laptop’s trust store, since a copy arriving over the wire would prove nothing.

Two more records close the handshake.

t = 134 ms. The tunnel is up.

Order a certificate for api.thenodebook.com · POST /acme/new-order.

A challenge: prove you control the name, carried as token K7v9....

Publish the token at /.well-known/acme-challenge/K7v9..., served over plain HTTP on port 80.

The CA fetches that token from several networks at once, confirming it resolves to this host.

Send a CSR, a certificate signing request: a public key and the name to certify it for.

Return the signed certificate, the leaf, the chain’s bottom link, signed by E5.

all six steps run unattended

Weeks before you clicked, a timer on the instance ran and used ACME to reach a certificate authority, an organization that verifies domain control and whose signing keys your laptop already trusts. ACME makes issuance routine. The client proves it controls the name, submits a key, and receives a certificate, and no person takes part at any step.

These certificates are valid for only 90 days° by design. A short lifetime limits the damage a stolen key can do, and it forces renewal to be automated.

Before handing the certificate over, the CA also published it to certificate transparency logs, which are public and append-only. Anyone can enumerate the certificates issued for any name, so a misissued certificate is publicly discoverable.

the field, integers mod 2²⁵⁵ − 19 · only A and B ever crossed the wire

real values - RFC 7748 §6.1 test vectors

Scalar multiplication means adding a curve point to itself a chosen number of times. Computing A from the secret a is fast. Recovering a from A runs the other way and is the discrete logarithm problem, which has no known feasible solution on this curve.° An eavesdropper who recorded A and B still cannot work out K from them.

from K to session keys - HKDF

K - the shared point │ HKDF-Extract ▼ handshake secret ├─ "c hs traffic" ├─ "s hs traffic" │ HKDF-Extract ▼ master secret ├─ "c ap traffic" - encrypts the request └─ "s ap traffic" - encrypts the reply

hs = handshake · ap = application data

The exchange produced one 32-byte secret, and a session needs several keys. HKDF expands K into separate keys for each direction and each phase, each one tied to a running hash of the whole handshake. The two at the bottom will encrypt the request and the reply, which have been blocked on the laptop for 127 ms° until exactly these keys existed.

the book goes deeperVolume 2 - TLS & Networking →act 4 - t = 134 → 165 ms

Encrypted the whole way to Virginia.

milliseconds pass here

The request leaves with the last handshake message.

the request from act 1 · 203 bytes

application_data · 225 bytes · encrypted

the shared key

Both ends hold a secret that was never sent.

one segment

The whole request fits in a single packet.

the record header

Five bytes anyone on the path can read.

crossing #5 - eastbound

The fifth crossing of six.°

long-haul fiber corridor · sacramento → ashburn

meanwhile, near the coffee shop

A cache server, a CDN edge, sits a few milliseconds from the coffee shop, keeping copies of pages and images so nobody crosses a continent for them. It played no part in this request.° A cache can only replay answers somebody already computed, and a POST that creates an order has no precomputed answer. Only the server in Ashburn can produce one.

amplifier huts

The tick marks are real buildings.

2,000 km south

A backbone link between Dallas and Atlanta, one of the long-haul carrier routes that run between major cities, just dropped off the internet's routing map and came back.° Routers exchange that map with each other over BGP, the protocol behind the anycast trick in Act 2, and thousands of them re-learned that corner of it inside a minute. None of it touched the route this packet is on.

somewhere in kansas

A cosmic-ray secondary, a particle knocked loose when a cosmic ray hits the atmosphere, just flipped one bit° in someone else's frame, the wrapper each cable or radio hop puts around a packet. Each frame ends with a checksum, a short arithmetic summary of its bytes. The receiving port recomputed it, got a different value, and dropped the frame, and TCP on the two ends noticed the gap and resent the missing bytes.

aws network edge

Past the balancer, which read only your addresses.

nlb

routes by address only

i-0f3…

node · pid 1447

four milliseconds at a time

held across the continent · too coarse for what comes next

The rest happens inside the machine.

act 5 - t = 165 → 165.05 ms

The kernel receives the request.

microseconds pass here

t = 165.000 ms - the scale changes sharply

the scale expands ×1

From here the clock advances in microseconds, and a microsecond is a thousandth of a millisecond. Each earlier stretch of the journey crossed thousands of kilometers of fiber. The next fifty microseconds fill the rest of this act.

Everything now happens inside one computer.

t = 165.000 ms - the outermost layer

The frame goes no further than this card.

t = 165.000 ms - photons to electrons

The CPU will never check this math.

eight microseconds in - into memory

So far, only the card has done any work.

t = 165.008 ms - what an interrupt is

The interrupted code resumes where it stopped, with no record of the pause.

t = 165.010 ms - the harvest

That one interrupt handled a whole batch of packets.

t = 165.015 ms - softirq: NET_RX, the network-receive chore

This is where the packet is actually processed.

t = 165.020 ms - whose bytes are these

Constant time, no matter how busy the box.

t = 165.030 ms - TCP numbers every byte

The in-order bytes are ready for the socket.

t = 165.035 ms - the socket buffer

The kernel queues bytes it cannot read.

t = 165.040 ms - the wake-up

epoll instance - owned by node, pid 1447

interest list · every socket this process serves

Node is awake and ready to run.

select(2) - 1983

the (2) is Unix manual-speak for chapter 2: syscalls

epoll - 2002°

level-triggered: keep reminding me while data remains. edge-triggered: tell me once, when it arrives.

libuv - the C library under Node that runs the event loop - drives epoll level-triggered: Node keeps being told about data until it drains it.

act 6 - t = 165.05 → 165.4 ms

One loop, one thread, and the eleven lines everything else exists to reach.

microseconds pass here

one while-loop in c

where the loop runs

The loop runs six phases, and it runs them in the same order every iteration.

uv_run(&loop, UV_RUN_DEFAULT), running since boot

loop iteration

#48,113,207°

the loop runs six phases in a fixed order, every iteration

You arrive in the poll phase.

check and close callbacks run later in this iteration. first, the poll callbacks run, and yours is one of them.

the read, the last copy

the slab: a 64 KB° buffer node set aside at startup and hands out in slices, so a busy socket never allocates fresh memory per read

Your bytes are now in user space.

decrypting the record

tlswrap → openssl · aes-256-gcm

The record is decrypted.

plaintext, readable for the first time since san francisco

how to read http without a regex

one rule per step. a space means stop collecting the method and start collecting the url

llhttp, byte by byte

␍␊ is \r\n, CRLF, the line ending HTTP took from teletype machines. · marks a space.

node builds two objects

Your request is a JavaScript object now.

new IncomingMessage

method: 'POST'

url: '/api/checkout'

headers: 6

httpVersion: '1.1'

new ServerResponse

statusCode: 200

headersSent: false

socket: the one from act 3

routed by hand, node:http style. a framework's radix-tree router would answer on this exact line.

This is the part you wrote.

handlers/checkout.js

V8, the JavaScript engine inside both Chrome and Node and the part that actually runs your code, has already run this handler many times. This is request #1,203,001° through this process, and V8 JIT-compiled the handler to machine code weeks of uptime ago.

It has run the handler enough to fill its inline caches, and every object the handler builds has the same internal layout, its hidden class, so reading a field is a direct memory lookup.

The eleven lines you just read do not run as JavaScript text. V8 runs the machine code it compiled from them earlier.

v8 is too large for one page. volume 1 gives it two chapters

const order = await db.query(

'INSERT INTO orders (sku, qty) VALUES ($1, $2) RETURNING id',

[sku, qty],

);

db.query(...) → Promise { <pending> }

The query is already sent, out over one of the pool's ten° connections to Postgres, each one opened at boot and lent out per request. The next act covers where the pool comes from. The answer does not exist yet.

await, checkout() suspends

The rest of the function is stored as a reaction on that promise, the same registration .then(fn) makes. No thread waits on it. Nothing spins.

microtask queue: [ ]

Empty. Promise callbacks run from here, but only when something settles, meaning it resolves or rejects, and nothing settles for another two milliseconds.

The handler does not block. It returns, and the call stack empties.

what await compiles to

what you wrote

const order = await db.query(...); res.writeHead(200, ...); res.end(...);

what the engine registers

db.query(...).then((order) => { res.writeHead(200, ...); res.end(...); });

meanwhile, in the same thread

You are not the only request in here.

the gray dots are live, the only self-running motion on this page

Node does have a thread pool, and your request never used it. Sockets do not go through the pool. Everything in this act ran on the one loop thread, because Linux can watch thousands of sockets at once without blocking on any of them.

A few operations cannot be watched this way and can only be run to completion, such as file reads, dns.lookup, and crypto.pbkdf2. For those, libuv keeps four° worker threads that run the blocking call off the loop thread, then hand the result back to the poll phase.

So this process that people call single-threaded runs five threads, plus the threads V8 uses for compilation and garbage collection. Your JavaScript runs on one of them, and the blocking work runs on the pool. If checkout() had needed a password hash instead of an INSERT, that work would have run on the pool.

sockets go to the loop. files, dns.lookup, and pbkdf2 go to the pool

act 7 - t = 165.4 → 167.5 ms

The shortest hop carries the heaviest promise.

microseconds pass here

t = 165.4 ms - the pool

The connection is already open, so there is no handshake.

Twenty-three days ago,° at deploy, this process opened ten connections before it accepted a single request. Here is what each one cost.

deploy · 23 days ago

connect() × 10

├─ tcp handshake 3 packets

├─ scram-sha-256 2 round trips

└─ fork() backend pids 30187-30196

pool ready before request #1

The SCRAM line is a password check. The password never crosses the network. The server sends a random challenge, and the client answers with a computation that only someone holding the password could produce, which takes two round trips.

The fork() line is the expensive one. Postgres gives every connection its own dedicated server process. To make one it calls fork(), which clones the running server into a second process. Each of these ten connections is therefore a full operating-system process on the database machine, which uses far more memory and setup time than a thread, and much more than a single Node callback. That cost, paid once at deploy, is why connection pools exist.

The alternative is to open a fresh connection for every request, which repeats the full connection setup, including the TCP handshake and the SCRAM check, before every query. That work would then run between the click and each order the site takes. Doing it once at deploy, when no user is waiting, keeps it out of the request entirely.

t = 165.5 ms - the wire protocol

Postgres has its own wire protocol, separate from HTTP.

parse

unnamed statement (one-shot)

INSERT INTO orders

(sku, qty)

VALUES ($1, $2)

RETURNING id

bind

values, no SQL

$1 = 'NB-1'

$2 = 1

describe

portal ""

asks which columns come back

execute

portal ""

max rows 0 = all

sync

end of batch

errors reset here

pooled socket · conn #4

5 frames · 218 bytes · one write() syscall

t = 165.7 ms - why the injection cannot run

the old pattern · string pasting

db.query("INSERT INTO orders (sku, qty)

VALUES ('" + sku + "', 1)")

what postgres receives

VALUES (''); DROP TABLE orders;--', 1)

the quote closes the string early, and the text after it runs as SQL.

values only, never SQL

$1 = '); DROP TABLE orders;--

$2 = 1

slot $1 is typed text · never re-parsed as SQL

stored in the sku column as twenty-four characters of ordinary text

t = 165.7 ms - the availability-zone hop

0.35 ms, there and back.°

at this scale, act 3's first crossing ends ~20 rulers below ↓

t = 166.05 ms - inside postgres

The planner has almost nothing to plan.

explain - ask postgres to print its plan · hover or tap the lines

Insert on orders (cost=0.00..0.01 rows=0 width=0)

-> Result (cost=0.00..0.01 rows=1 width=72)

Planning Time: 0.048 ms

cost = startup..total, measured in the planner's own internal units, not milliseconds. the units are only meaningful for comparing plans for the same query · rows and width are the planner's estimates of the output

the index - orders_pkey

3 levels,° 3 page reads, all three already in postgres's RAM cache (shared_buffers), because the last few thousand inserts read these same pages

the write-ahead log

each record tagged with its transaction id (xid) · the log is written as a series of 16 MB files called segments°

A normal write() call returns as soon as the kernel has copied your bytes into its page cache, which is memory, not the disk. The kernel reports success right away and writes the bytes to the device later, on its own schedule, perhaps seconds afterward. If the power is lost before that happens, the write is gone.

fsync does not return until the device reports that the bytes are stored on permanent media, which makes it the slowest step in committing a transaction. Because it is so slow, Postgres uses group commit. It holds commits for a fraction of a millisecond so that several of them can be written by one fsync. Here three transactions are made permanent by a single flush, and each one pays a third of its cost.

The disk adds one more network step. This instance's disk is an EBS volume. The instance sees an ordinary drive, but each write travels to a storage server a short network hop away, which copies the bytes to more than one machine before it acknowledges them.° The confirmation that fsync waits for is therefore a small round trip across the network to another machine.

Even the disk write here includes a network round trip.

t = 167.1 ms - the flush returns

flushed · the row is now on durable storage

For the only time in these 211 milliseconds,° your order is written to storage that survives a power cut.

epoll_wait returns · act 5 again, in one line

pooled socket

socket (fd 23) readable

pg driver

parses DataRow

promise

db.query resolves

microtask queue

resume handler()

the loop drains microtasks before anything else · the rest of the handler runs next

act 8 - t = 167.5 → 168 ms

Half a millisecond to turn one row into westbound light.

microseconds pass here

t = 167.5 ms - the resumption

drained - the continuation is running

The parked continuation runs now.

handlers/checkout.js - resuming

order.rows[0].id === 1203982

{ ok: true, id: 1203982 }- the object

│ JSON.stringify - synchronous, character by character

{"ok":true,"id":1203982}- 24 bytes

the handoff

the request - 22 bytes, sent east

the response - 24 bytes, sent west

The response body is 24 bytes, two more than the request.°

t = 167.7 ms - res.end()

the header string - serialized

HTTP/1.1 200 OK\r\n

content-type: application/json\r\n

Content-Length: 24\r\n

Date: Tue, 07 Apr 2026 16:41:00 GMT\r\n

Connection: keep-alive\r\n

\r\n

{"ok":true,"id":1203982}

every line ends in \r\n, HTTP's line break, two bytes each, all counted in the 132

132 B° of headers + 24 B of body = 156 B of plaintext

The two writes leave the machine as one packet.

Without cork and without TCP_NODELAY, this reply would go out in two steps. The 132 bytes of headers leave as the first packet. The 24-byte body is ready next, but Nagle's algorithm holds it back. Nagle's rule is that a socket may not send a second small packet while an earlier small packet is still unacknowledged, so the body waits for the laptop to acknowledge the headers. The rule exists to stop a program from sending many tiny packets when it could send fewer full ones.

The laptop follows its own rule, delayed ACK. That rule says a bare acknowledgment is not worth a packet of its own, so the laptop holds the acknowledgment for up to 40 ms in case it gets reply data to send with it. Now the two rules stall each other. The body will not go until the headers are acknowledged, the acknowledgment will not go until the laptop has reply data to carry it, and the only reply data *is* the body Nagle is holding back.

Each rule is reasonable by itself, and together they can delay a small response by the full 40 ms. Node prevents this by setting TCP_NODELAY on every socket when the socket is created, which turns Nagle off so small writes go out immediately. On this connection the 40 ms stall° never happens.

TCP_NODELAY is set by default in Node's net module

The writev syscall hands the kernel a list of buffers in one call, so there is one crossing into the kernel instead of one per buffer. It has just returned, and so far none of the bytes have gone onto the network.

write() does not transmit. It copies your bytes into the socket's send buffer, which is kernel memory, and returns. TCP decides when the bytes actually leave, and it keeps its own copy of them after they leave, because the network can drop packets and TCP has to be able to send them again. That copy is freed only when the laptop's acknowledgment arrives, 62 ms° from now.

This send buffer is also what backpressure is built on. When res.write() returns false and a drain event follows later, that is the send buffer filling up and then emptying, reported back to your JavaScript. Our 178 bytes stay far below the buffer's limit.

The buffer holds them, TCP packages them into one segment, and the driver posts a descriptor to the NIC's transmit ring, the sending-side counterpart of the receive ring from Act 5. The card reads the bytes from RAM directly and computes the checksum in hardware as they leave. This is checksum offload, the same hardware step that checked our request when it arrived. Sending costs the kernel far less than receiving did, about a tenth of the work.°

t = 167.9 ms - encrypted and sent

TLS encrypts the response.

encrypted until san francisco

out of the machine, top to bottom

next, the return and the paint

act 9 - t = 168 → 211.4 ms

The answer crosses home and waits at a red light.

milliseconds pass here

crossing #6, westbound

Crossing six of six.° The one that carries the answer.

your response

long-haul fiber corridor, westbound · route mirrored, you are heading west

meanwhile, back in ashburn

The process that answered you has already emitted 'request' twice more. Your socket stays open. On the server it sits in the keep-alive list, held open because another request is likely soon. In Chrome it sits in the socket pool, grouped by hostname and ready to reuse.

a light boost every ~80 km, the same amplifiers, the other direction

the last ten meters are wi-fi. only one radio can talk at a time. the channel is quiet, so the access point transmits immediately, with no backoff and no retry.

arriving · the coffee shop

t = 199 ms, the laptop's kernel

This is the receive path from Act 5, now running on the laptop instead of the server.

act 5's receive path, drawn smaller

network card on the left, chrome's socket thread on the right.

Now a thread inside Chrome wakes up.

Before Chrome even wakes, your laptop's kernel has already written back. TCP sends a receipt for everything it delivers. That receipt is an ACK, a packet carrying zero bytes of data, that says only 'I have every byte up to number so-and-so.' One leaves for Ashburn now, thirty-one more milliseconds east. The story does not count this as a crossing,° because it carries no data of its own, only the acknowledgment.

Back in Ashburn, the server's kernel still holds a copy of your response in its send buffer, the same one you watched the answer enter in Act 8, and it keeps holding it until this receipt arrives. If the receipt never comes, a timer fires and the kernel sends the answer again, and neither you nor the Node process would ever know it happened.

This is the mechanism that makes TCP reliable, and this is the only place on the page you see it directly. Every byte is numbered, every arrival is acknowledged, and anything left unacknowledged is sent again. The reliability you have counted on for two hundred milliseconds is built entirely from these acknowledgments traveling back the other way.

your pixels will change before the server learns you received the answer

t = 201 ms, chrome unwraps

The record is decrypted, for the last time on this page.

AES-256-GCM, the cipher agreed in Act 3. The tag matches.

{"ok":true,"id":1203982}

The keys that decrypt this record never crossed the wire. Both sides computed the same secret during Act 3's handshake and have been deriving keys from it ever since. Anyone who recorded all 4,700 km of traffic captured only ciphertext they cannot read. AES-GCM decrypts the 178 bytes° of ciphertext into 156 bytes° of plaintext, then recomputes the 16-byte tag and compares it against the one that was sent. If a single bit was flipped anywhere along the way, the two values disagree, and Chrome drops the connection instead of handing your code a corrupted byte.

What comes out is plain text. A status line, four headers, a blank line, and the body.

HTTP/1.1 200 OK

content-type: application/json

Content-Length: 24 ← marks the end

Date: Tue, 07 Apr 2026 16:41:00 GMT

Connection: keep-alive


{"ok":true,"id":1203982}

This connection is staying open for your next request, so no end-of-file will ever arrive to mark where the response stops. The Content-Length: 24 header is the only thing that tells Chrome where the response ends. Chrome reads exactly 24 bytes° and stops. If you set that header wrong on your own server, every client keeps waiting for a 25th byte that never arrives, and the request hangs.

t = 202 ms, the main thread

task queue

the promise settled over in the network service. its callback runs here as a task, one callback that runs to completion, when the main thread reaches it in the queue.

Your code runs last.

const res = await fetch('/api/checkout', { method: 'POST', body })

const data = await res.json()

setStatus('confirmed')

t = 203 ms, the dom changes

The words Order confirmed now exist as text, not yet as pixels.

<p id="status">Order confirmed</p>

Getting this one change onto the screen takes four steps.

the frame is ready at t = 207 ms, but the display cannot show it yet.

t = 207 ms, the compositor waits

The GPU has finished the frame, but the screen will not show it yet.

Twenty-eight thousand kilometers of travel,° and now the answer waits about thirty centimeters° from your eyes for the display's next refresh.

4.4 ms

the frame waits here, longer than the whole server spent computing the answer°

next · the refresh

epilogue, after t = 211.4 ms

They noticed nothing.

The whole request took a fifth of a second.

Once more, at a glance.

scroll runs it · scrolling back rewinds it

0.0 ms°

click → order confirmed · san francisco → ashburn → back

~0 km°

traveled

0°

continental crossings

~0°

machines

0°

protocols' handshakes

0°

wi-fi retransmission

0°

lines of your code

The handshakes took 60% of the 211 milliseconds. The request and response spent 35% of it traveling. Everything the server did, the kernel included, came to 1.4%.°

↑ your server

The second request reuses everything.

the book

You just watched one request, end to end. nodebook goes this deep on every hard part of Node.