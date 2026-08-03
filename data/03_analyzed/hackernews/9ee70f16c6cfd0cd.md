---
title: The Beam Engine
source: https://glinscott.github.io/beam-engine/
author:
- '[[glinscott]]'
published: '2026-07-22'
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
description: 'Article URL: https://glinscott.github.io/beam-engine/ Comments URL:
  https://news.ycombinator.com/item?id=49007221 Points: 378 # Comments: 74'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 9ee70f16c6cfd0cd
source_type: community_discussion
tldr: 该文章通过交互式图解，从蒸汽的基本原理出发，逐步讲解纽科门大气压蒸汽机、瓦特分离冷凝器、滑阀配汽机构等关键技术，完整还原了梁式蒸汽机从第一性原理到实际工程实现的演进过程。
objective_summary: 文章以梁式蒸汽机为主题，从蒸汽受热膨胀至原体积1700倍的物理现象讲起，依次介绍活塞与气缸的工作原理、大气压力驱动活塞形成真空的力学机制、托马斯·纽科门于1712年发明的矿井排水蒸汽机、詹姆斯·瓦特于1765年提出的分离冷凝器（节省约三分之二煤耗）、滑阀配汽机构对进排气的自动控制、锅炉从haystack式到圆柱形的结构演进以及瓦特于1782年专利的切割膨胀（cutoff）技术，完整展示了蒸汽机从煤矿排水专用设备发展为工业革命核心动力的技术演进路径。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - University of Glasgow
  technologies:
  - Steam Engine
  - Beam Engine
  - Newcomen Engine
  - Separate Condenser
  - Slide Valve
  - Double-Acting Engine
  - Cutoff
  key_people:
  - Thomas Newcomen
  - James Watt
  - Matthew Boulton
  - Otto von Guericke
  - Joseph Black
  - Richard Trevithick
  - John Southern
key_logic_flow:
- 蒸汽受热后体积膨胀至原水的1700倍，在密闭容器内产生压力，这是蒸汽做功的物理基础。
- 活塞与气缸构成蒸汽机核心运动机构，蒸汽压力推动活塞，力的大小取决于蒸汽压强和活塞面积。
- 早期锅炉无法承受高压，纽科门通过向气缸内喷水冷凝蒸汽形成真空，利用大气压力驱动活塞，获得约每平方厘米一公斤的力。
- 纽科门于1712年在达德利煤矿安装第一台成功运行的蒸汽机，每分钟约12个冲程，每个冲程可将45升水提升50米。
- 瓦特在1765年发明分离冷凝器，使气缸保持高温而冷凝器保持低温，将煤耗降低约三分之二。
- 瓦特进一步封闭气缸顶部实现双作用式蒸汽机，并采用滑阀自动控制气缸两端进排气时序，使蒸汽机更适合驱动旋转机械。
object_mentions:
- object_type: product
  name: Newcomen's Engine (1712)
  canonical_name: Newcomen Atmospheric Engine
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 托马斯·纽科门于1712年在达德利附近的一座煤矿安装了第一台成功运行的蒸汽机，每分钟约12个冲程。
  - 每个冲程可将约45升水提升50米，与马匹不同，它可以昼夜不停地运行而无需食物或休息。
  article_id: 9ee70f16c6cfd0cd
- object_type: product
  name: Watt's Separate Condenser (1765)
  canonical_name: Watt's Separate Condenser
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 瓦特在1765年维修格拉斯哥大学的纽科门模型时产生灵感，增加一个可保持低温的第二容器来冷凝蒸汽。
  - 瓦特与商业伙伴马修·博尔顿以节省煤耗的三分之一作为收费模式，将这项发明商业化。
  article_id: 9ee70f16c6cfd0cd
- object_type: product
  name: Watt's Double-Acting Engine
  canonical_name: Watt Double-Acting Steam Engine
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 瓦特封闭气缸顶部并使用蒸汽推动活塞两侧，使同一气缸在两个冲程中都产生动力。
  - 稳定的推拉作用使双作用式蒸汽机更适合驱动机器设备。
  article_id: 9ee70f16c6cfd0cd
- object_type: product
  name: Slide Valve
  canonical_name: Slide Valve (D-slide valve)
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 滑阀位于蒸汽阀箱内，通过偏心轮驱动，用单个阀门完成气缸两端进气和排气的交替切换。
  article_id: 9ee70f16c6cfd0cd
extract_result: success
impact_score:
  score: 1.0
  reason: 该文章为一篇交互式历史工程技术科普，从第一性原理讲解梁式蒸汽机（纽科门机→瓦特机）的技术演进。与AI行业完全无关，对AI行业短期冲击力为零。无论作为技术事件还是商业事件，均不构成任何竞争格局或范式变化的影响。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 该文章与AI开发者生态无关，属于历史工程教育内容，开发者对此无特定情绪反应
hype_assessment:
  level: low
  reason: 文章内容为成熟历史知识，采用交互式图解（3D模型可拖拽缩放）辅助教学，没有任何'颠覆''革命性'等PR话术，是实打实的第一性原理工程技术科普，无水分。
information_entropy: medium
domain_disruption:
  technical_innovation: 无（该文章为18世纪蒸汽机技术的历史回顾，不涉及AI领域的技术突破）
  business_model: 无（与AI商业模式无关）
engineering_complexity: infrastructure
compound_value:
  score: 2.5
  reason: 该文章是18世纪蒸汽机技术演进的历史科普内容，与当前AI产业投资格局无直接关联。从VC视角看，它不构成任何可定价的行业事件——没有新产品发布、没有融资轮次、没有技术突破、没有市场格局变化。唯一可能产生微弱价值的是其第一性原理工程方法论（从蒸汽膨胀1700倍逐步推导到工程实现），对AI领域的技术型创始人有一定思维启发，但这种通识教育价值无法形成可追踪的复利效应或投资回报，不属于可配置资产的范畴。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries: []
competitive_casualty: []
market_opportunities:
- 基于第一性原理的AI交互式教育内容产品——借鉴本文从蒸汽基础物理逐步推演至完整引擎的渐进式讲解方式，可开发针对Transformer架构、注意力机制、反向传播等AI核心概念的互动式教程，面向开发者与学生群体构建教育变现路径
- AI推理与训练效率优化工具——本文揭示的分离冷凝器降低2/3煤耗的效率突破，类比当前AI领域的推理加速、模型量化、稀疏计算、投机解码等效率优化赛道，创业者可关注面向大模型部署的推理优化中间件机会
- AI从专用走向通用的基础设施层布局——蒸汽机从煤矿排水专用设备演进为驱动整个工业革命的通用动力，提示AI正在经历类似的通用化进程，可前瞻性布局AI基础设施平台层（调度编排、资源管理、多模型网关等），等待通用化拐点到来
risk_matrix:
  regulatory: 无
  technological: 无
  competitive: 无
  ethical: 无
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: speculative_watch
object_insights:
- object_type: product
  name: Newcomen's Engine (1712)
  canonical_name: Newcomen Atmospheric Engine
  url: null
  positioning: 纽科门大气压蒸汽机，1712年安装在达德利煤矿，利用大气压力驱动活塞实现矿井排水，是人类首台成功运行的工业蒸汽机。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 18世纪初面临严重矿井水患的煤矿主，急需可昼夜持续运转的排水动力
  product_signal: 每分钟约12个冲程，每个冲程可将约45升水提升50米，能够昼夜不停地运行而无需食物或休息。
  market_signal: 深矿井水患迫切驱动需求，使用矿场废煤为燃料使其在矿区经济可行，很快从康沃尔推广至纽卡斯尔。
  differentiation: 相比马匹驱动的水泵可连续运行无需换班，但每冲程约四分之三蒸汽浪费在重新加热气缸上，煤耗极高。
  watch_reason: 作为工业革命的开端之作，纽科门蒸汽机首次验证了蒸汽驱动机器的工程可行性，但其极端低效直接催生了瓦特的关键改进，是理解技术演进路径不可绕过的基石。
  risk_notes:
  - 煤耗极高，每冲程约四分之三蒸汽用于重新加热气缸，经济性严重依赖矿场废煤燃料。
  score: 5.0
  article_ids:
  - 9ee70f16c6cfd0cd
  evidence_snippets:
  - 托马斯·纽科门于1712年在达德利附近的一座煤矿安装了第一台成功运行的蒸汽机，每分钟约12个冲程。
  - 每个冲程可将约45升水提升50米，与马匹不同，它可以昼夜不停地运行而无需食物或休息。
- object_type: product
  name: Watt's Separate Condenser (1765)
  canonical_name: Watt's Separate Condenser
  url: null
  positioning: 瓦特于1765年发明的分离式冷凝器，通过独立低温冷凝容器避免气缸冷却，将蒸汽机煤耗降低约三分之二，是效率革命的关键突破。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 矿业和制造业的蒸汽机用户，尤其是煤矿以外需额外购买燃料、对煤耗敏感的工业企业
  product_signal: 分离冷凝器使气缸保持高温同时冷凝器保持低温，将纽科门机的煤耗降低约三分之二，大幅提升了蒸汽机的经济性。
  market_signal: 瓦特与博尔顿以节省煤耗的三分之一作为收费模式商业化该技术，使蒸汽机从煤矿走向更广泛的工业应用领域。
  differentiation: 相比纽科门机直接向气缸喷水冷凝导致的巨大热损失，分离冷凝器实现了冷热区域的物理隔离，是工程效率的跨越式创新。
  watch_reason: 瓦特分离冷凝器是工业革命中最重要的效率创新之一，其"隔离冷热区域"的设计哲学至今在热力学工程中影响深远，也是蒸汽机走出矿山的根本推手。
  risk_notes:
  - 分离冷凝器增加了机械复杂度，对密封和制造精度要求更高，初期制造成本显著上升。
  score: 6.0
  article_ids:
  - 9ee70f16c6cfd0cd
  evidence_snippets:
  - 瓦特在1765年维修格拉斯哥大学的纽科门模型时产生灵感，增加一个可保持低温的第二容器来冷凝蒸汽。
  - 瓦特与商业伙伴马修·博尔顿以节省煤耗的三分之一作为收费模式，将这项发明商业化。
- object_type: product
  name: Watt's Double-Acting Engine
  canonical_name: Watt Double-Acting Steam Engine
  url: null
  positioning: 瓦特双作用式蒸汽机封闭气缸顶部并利用蒸汽推动活塞两侧，使上下冲程均产生动力，是蒸汽机从排水泵走向通用动力源的关键转型。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要稳定旋转动力驱动纺织机、机床等设备的工厂主和制造业者
  product_signal: 封闭气缸顶部并使用蒸汽推动活塞两侧，使上升和下降冲程都产生动力，稳定的推拉作用使其更适合驱动机器设备。
  market_signal: 双作用式设计使蒸汽机从往复式水泵升级为可直接驱动旋转机械的通用动力源，推动了工厂机械化进程的加速。
  differentiation: 相比纽科门和早期瓦特机的单作用设计，双作用式实现了双向动力输出，将蒸汽机从排水专用设备转变为工业通用动力平台。
  watch_reason: 双作用式是蒸汽机从矿井排水专用设备转型为工业通用动力源的决定性一步，标志着蒸汽动力全面进入工厂时代并驱动了工业革命的纵深发展。
  risk_notes:
  - 需要更复杂的滑阀配汽机构精确控制气缸两端进排气时序，对制造工艺和密封技术提出了更高要求。
  score: 5.0
  article_ids:
  - 9ee70f16c6cfd0cd
  evidence_snippets:
  - 瓦特封闭气缸顶部并使用蒸汽推动活塞两侧，使同一气缸在两个冲程中都产生动力。
  - 这种稳定的推拉作用使双作用式蒸汽机比单作用设计更适合驱动机器设备。
---

This is a beam engine. It produced about fifteen horsepower continuously, roughly as much power as 150 people. Engines like this turned steam into the power that drove the Industrial Revolution. This article builds the engine up from first principles, using interactive figures to explore each idea (try rotating the engine above with two fingers, or pinching to zoom indragging the engine above, or zooming with ⌘/Ctrl + scroll). Let's start our journey through the engine with steam.

## Steam

Below, we have a pot filled with water and a fire underneath. As the fire heats the water, some of it begins to boil and turns into steam.

Steam undergoes an amazing transformation: it expands to **1,700 times** the volume of the original water. One cup of water becomes roughly 400 litres of steam, enough to fill two bathtubs. If the steam doesn't have enough room to expand it will push on all the walls of the container. This push on every wall is *pressure*, and we will measure it in atmospheres, multiples of the ordinary pressure of the air around us. The steam also presses on the surface of the water, which transmits the pressure evenly to everywhere the water touches.

Now we need a way to harness the properties of steam.

## Pistons and cylinders

A *piston* is a round disc that fits snugly inside a *cylinder*. Steam pushes on one face of the piston and a rod transmits the force elsewhere. The force depends on two things: the pressure of the steam and the area of the piston. At a pressure difference of one atmosphere, each square centimetre of piston provides about one kilogram of force.

Early boiler builders didn't know how to safely harness high-pressure steam.1 Instead, to get more force they made the piston wider. Because area grows with the square of the diameter, doubling the width of a piston gives it four times the area and four times the force at the same pressure. This is why early steam engines had enormous cylinders, sometimes wide enough for a person to stand inside. In the figure below, the boiler pressure never changes; try increasing only the bore until the piston can lift the car.

With steam pushing on our piston, we can do real work. But low-pressure steam is not very strong. To move heavy machinery, engineers turned to a surprising source: the atmosphere.

## The weight of air

Air feels weightless, but only because we are surrounded by it. Imagine a column of air one centimetre square, extending from your hand all the way to the top of the atmosphere. That column weighs about one kilogram, so the atmosphere presses on every square centimetre with roughly one kilogram of force.

We do not feel this enormous pressure because the air and fluid inside us push back at the same pressure. But if the pressure falls on one side of a surface, the pressure on the other side remains. This is what happens when you drink through a straw. Your mouth lowers the pressure inside the straw, and the atmosphere pushing on the drink in the cup forces it upward.

Otto von Guericke gave a spectacular demonstration of this effect in 1654. He joined two copper hemispheres into a sphere about half a metre across and pumped out the air. To the amazement of the observers, teams of horses could not pull the halves apart. The atmosphere was clamping them together with about two tonnes of force! As soon as he opened a valve and let the air back in, they came apart by hand.

Creating a vacuum was extremely difficult at first. Guericke had to laboriously pump the air out of his sphere, but steam gives us a much faster way to make one. If we fill a vessel with steam and then cool it with a spray of water, the steam condenses back into roughly 1/1,700 of its volume.

Fill a cylinder with steam, condense it underneath a piston, and the atmosphere will drive the piston down into the vacuum. A near-perfect vacuum gives us the same pressure difference we used earlier: about one kilogram of force for every square centimetre of piston. A piston half a metre across could collect almost two tonnes of force from the atmosphere.

## Newcomen's engine

In the early 1700s, mines were getting deeper, and flooding was becoming a huge problem. Once a shaft reached below the water table, water seeped in continuously and had to be pumped out day and night. The pumps were driven by teams of horses walking in circles. As one team tired, another took over, but the deepest mines still flooded during wet weather and valuable coal had to be abandoned. A new solution was needed, and steam would provide the answer.

Thomas Newcomen supplied tools to the mines and knew that flooding was both a huge problem and an opportunity. He spent years turning the vacuum piston stroke into an engine that could run all day. He connected the piston to one end of a huge rocking beam and hung heavy pump rods from the other. The atmosphere drove the piston down and lifted the pump rods; their weight then pulled the piston back up while the cylinder filled with steam again.

Newcomen's first successful engine was installed at a coal mine near Dudley in 1712. It ran at about twelve strokes per minute, lifting roughly forty-five litres of water fifty metres on every stroke. Unlike the horses, it could continue around the clock without food or rest. Similar engines soon appeared in mines from Cornwall to Newcastle.3

Newcomen's engine worked! But it used an extraordinary amount of coal. The cold water sprayed directly into the cylinder, chilling a huge mass of iron along with the steam. Roughly three quarters of the steam was wasted heating the cylinder back up on every stroke.

The mines were happy with this tradeoff because they burned *slack*, small pieces of coal that were considered waste. Anywhere else, the fuel cost was simply too much. This kept the steam engine stuck in coal mines for the next fifty years.

## The boiler

Why did Newcomen use the atmosphere to push the piston instead of the steam itself? His boiler was simply not strong enough. The *haystack boiler* produced only about a twentieth of an atmosphere above the surrounding air. It was built from thin copper or iron plates joined with rivets, and the wide walls and weak seams could not safely hold much pressure.

James Watt, who we will meet in the next section, used the *waggon boiler* shown below. Water sat in the broad chamber above the furnace, the hot gases passed underneath, and steam collected beneath the rounded roof.

The broad bottom was good at catching heat, but the waggon shape was terrible at holding pressure. Raise the steam pressure in the figure below and compare what happens to the rounded roof, the flat sides and the inward-curved bottom.

The figure also shows why later builders curved the whole boiler outward like the roof. They rolled iron plate into long cylinders, removing the flat sides and inward-curved bottom. They kept the boilers narrow because making a cylinder wider increases the force trying to split it open, even when the pressure stays the same.4 Better iron and riveting then made much higher pressures possible, and around 1800 Richard Trevithick was running engines at several atmospheres.

Now Newcomen's use of a vacuum makes sense. His boiler could push with perhaps fifty grams per square centimetre above atmospheric pressure. By condensing the steam and letting the atmosphere push the piston instead, he got close to one kilogram per square centimetre, around twenty times as much force from the same boiler.

## Watt's separate condenser

In 1765, Watt was repairing a model Newcomen engine at the University of Glasgow. He was amazed by how much steam it consumed and began trying to understand where it all went. He discussed the problem with his colleague Joseph Black, who was studying the heat absorbed while water boils. Black called it *latent heat*. For a kilogram of water, boiling it away takes more than five times as much energy as heating it from freezing to boiling.

With this knowledge, Watt calculated the exact amount of water needed to condense the volume of steam in the cylinder. He was surprised to find that this exact amount barely made a vacuum at all: the condensing steam dumped its latent heat into the spray, warming the water until it stopped condensing anything. Adding in more cold water just cooled the cylinder down more, wasting steam to heat the cylinder back up on the next stroke. Watt's brilliant insight was to add a second vessel that could stay cold while the cylinder stayed hot.5

At the end of the stroke, a valve opened and the steam rushed into the cold vessel, called the *condenser*. As the steam turned back into water, the pressure fell in the condenser and, through the connecting pipe, in the cylinder as well. A small *air pump* driven by the engine drew out the condensed water, along with any air that had leaked in, on every stroke. Keeping the cylinder hot and the condenser cold cut coal consumption by about two thirds! Watt and his business partner Matthew Boulton turned the saving into a business model, charging customers one third of the money they saved on coal.

Better tools for making precise cylinders allowed Watt to make another important change: he closed the top of the cylinder and used steam on both sides of the piston. Steam pushed down while the condenser lowered the pressure below; on the return stroke, the same thing happened in the opposite direction. This was the *double-acting* engine. Below, we can compare it with the single-acting cylinder it replaced.

The same cylinder now produced power on both strokes, and the steady push-pull made the engine much better suited to driving machinery. But getting steam in and out of the cylinder was now more complicated. One end had to connect to the boiler while the other connected to the exhaust, and then the two connections had to switch before the piston returned.

## The slide valve

Early steam engines used several separate valves and linkages to route the steam. Our engine does all of this with one *slide valve*. It moves only a few centimetres, connecting one end of the cylinder to fresh steam and the other to the exhaust. As the piston reaches the end of its stroke, the valve slides across and swaps the two connections.

The valve sits inside the *steam chest*, an iron box bolted to the side of the cylinder and kept full of fresh steam. Three ports open into the chest. The two outer ports connect to the ends of the cylinder, while the middle one carries away the exhaust. The valve is shaped like a wide, hollow D. One edge uncovers a cylinder port and lets fresh steam enter, while the hollow back joins the other cylinder port to the exhaust.

The valve needs to move in perfect synchronization with the piston, or the engine will not work. This motion comes from an *eccentric* on the engine's rotating shaft. The eccentric is a circular disc mounted slightly off-centre, so its centre travels in a small circle as the shaft turns. A strap around the disc follows this motion and drives the valve rod back and forth. Its position on the shaft is chosen so the next steam port begins opening before the piston reaches the end of its stroke.

Now, we can see how the piston, valve gear and eccentric work on our beam engine.

### Using less steam

We can save a surprising amount of coal by closing the steam port before the piston reaches the end of its stroke. The trapped steam continues to expand and push the piston, although its pressure falls as the volume grows. Closing the valve at halfway, called *cutoff*, uses half as much steam while still producing about 85 percent of the ideal work.6 Watt patented this idea in 1782. Later compound engines sent the exhaust from one cylinder into a larger cylinder, then sometimes into a third, extracting more work as the steam expanded.

### Measuring the work

Everything we have just discussed happens inside an opaque cylinder. In 1796, Watt's assistant John Southern built an instrument that let them see inside. A small spring-loaded piston moved a pencil up and down with the pressure, while a card moved sideways with the main piston. The resulting *indicator diagram* showed the pressure through the entire stroke, and the area inside the loop measured the work produced.

A leaking piston, late cutoff and restricted exhaust each produce a different shape, allowing an engineer to diagnose the engine from a single card. Boulton & Watt found the instrument so valuable that they kept it secret for years.7

We can now control the steam and produce power in both directions, but the piston still moves back and forth. This is called *reciprocating motion*. Pumps can use it directly, but the mills driving the Industrial Revolution needed rotation.

## Making rotation

To turn the piston's back-and-forth motion into rotation, our beam engine uses a *crank*, although Watt's first rotating engines could not use one.8 A pin offset from the centre of the shaft is joined to the piston by a *connecting rod*. The push on the pin turns the shaft, but not equally through the revolution. Twice per turn the crank and connecting rod line up, at positions called *dead centres*, where the piston pushes straight through the shaft and produces no rotation at all. With nothing to carry it past these points, the engine would stop the first time the crank reached one.

The large *flywheel* fixes this problem. It stores energy while the crank has good leverage, then returns that energy to keep the engine spinning past the dead centres. In the figure below, the shaded band in the inset shows the flywheel collecting and repaying energy through each revolution. Try the flywheel mass slider: a heavier wheel changes speed less, giving the engine a smooth and steady rotation.

Our engine can now turn a shaft without stopping. But joining the piston rod to the crank turns out to be harder than it looks.

## The beam and the parallel motion

Now, look closely at the connecting rod in the figure below. As the crank turns, its pin moves sideways as well as up and down. The piston rod cannot follow it because it must travel straight through the seal at the top of the cylinder. If we connect them directly, the rod pushes the piston sideways and quickly destroys the seal.

The beam carried the sideways load into a large round bearing, which workshops could make accurately. But its end moved in an arc, and Watt still needed the piston rod to travel in a straight line.

His ingenious solution was the *parallel motion*, patented in 1784. A set of hinged links joins the beam to a fixed point on the engine. As the beam pulls the piston rod sideways in one direction, another link pulls it almost exactly the same amount in the other. The two curves cancel, leaving a path that is remarkably close to a straight line. Watt was so pleased with the mechanism that he wrote he was “more proud of the parallel motion than of any other mechanical invention I have ever made.”

Our piston can now turn the crank without being pulled sideways. At the far end of the beam, we also get a convenient source of back-and-forth motion, which the engine uses to keep its boiler filled with water.

## The pump

As the engine runs, the boiler turns water into steam. To keep it going, we need to replace that water without stopping. We can't simply connect a water tank, because the pressure inside the boiler would push the water back out. Instead, the far end of the beam drives the small pump beside the base of the engine, forcing fresh water into the boiler.

Inside the pump is a narrow plunger and two one-way *check valves*. As the plunger rises, the pressure falls, the inlet valve opens and water enters from the tank. On the way down, the pressure rises, closing the inlet valve and opening the outlet towards the boiler. The changing water pressure operates both valves automatically.

The pump must produce slightly more pressure than the boiler, but it does not need to move much water on each stroke. Making the plunger narrow keeps the required force small, for the same pressure-times-area reason that made our engine piston wide. A small part of the engine's power can now keep the boiler full, while the rest turns the flywheel.

## Powering the mill

We talked about why mills need rotation, but not how they used it. Before steam engines, water-powered mills had to sit beside a river. The flowing water turned a large waterwheel, which drove a main shaft, and iron shafts, pulleys and leather belts carried that rotation through the building to power the machines. Our example mill here has a saw for cutting wood and a power loom which wove cloth. Click either machine to shift its belt onto the loose pulley; that machine will coast to a stop while the shaft and the other machine continue running.

It is not intuitive that a leather belt can transmit enough power to drive a machine that ten strong people could not. With only friction between the iron pulleys and the leather providing the connection, it seems that the belt would slip. The physics underlying friction is fascinating. Imagine a huge ship tied to an iron bollard on the dock with a rope. Tension in the first small part of the rope presses it against the iron, and the resulting friction reduces the tension that reaches the next part, and so on around the post.9

Now, let's return to leather belts and iron pulleys. A belt is installed under tension, so at rest its two sides pull with roughly equal force. Once the machine needs power, friction transfers some of that pull from the returning side to the driving side.10

The power transferred by a belt is the difference in tension multiplied by the belt speed. At full mill scale, a sixteen-foot flywheel at sixty revolutions per minute has a belt speed of about fifteen metres a second. If the load makes one side pull with 2,000 newtons more than the other, a foot-wide leather belt can carry about forty horsepower.

### The fight for water

Richard Arkwright's water-powered mill at Cromford opened in 1771, and the factory system that followed created fierce demand for the best river sites. Water-powered mills were also dependent on the weather: a dry season could shut down the factory.

Steam pumping engines offered a solution. An engine lifted the water that had passed beneath the wheel back up the hill, allowing the same water to fall through the wheel again. This kept the smooth turn of the water wheel, but wasted coal moving the water. Watt sold sixteen to twenty horsepower pumping engines to deliver ten horsepower to the machines.

Watt's double-acting engine, beam, crank and flywheel let the engine directly turn the line shaft. This met a huge demand from mill owners who wanted to build near workers and materials rather than around a particular stretch of river.11 One problem remained, though: every time a machine was turned on or off, the load on the engine changed.

## The governor

The beam engine still needed a way to keep its speed constant. Imagine it at the beginning of the day, turning at 30 rpm with no machines connected. When the first machine is connected, it draws power from the engine and slows it down. The engine driver could open the throttle by hand until the shaft returned to 30 rpm, but this was tiring work, and mistakes had severe consequences. A cast-iron flywheel could burst if it spun too quickly.

Instead, Watt adapted a device used on windmills to adjust the steam automatically.12 Bevel gears turn a vertical spindle, and two heavy balls hang from hinged arms attached to it. As the engine speeds up, the balls swing outward and lift a sliding collar. A fork and long rod carry this motion across the engine and turn the *steam cock* towards closed. When the engine slows, the balls fall and open the cock again.13

## The whole machine

Let's return to the complete engine from the beginning of the article. Every mechanism we studied on its own is here, running in its place. The figure follows the power once along its whole path, from the boiler steam to the belt that leaves for the mill.14

## Epilogue

The beam engine was a product of the tools and science of its time. Watt used a beam and parallel motion partly because the workshops of the 1780s could not make long, accurate guides for a crosshead. As planing machines improved during the nineteenth century, those straight guides became practical. The heavy beam was no longer required, and by the 1860s most new mill engines drove the flywheel directly.15

Line shafts and leather belts outlived the beam engine, remaining above factory floors well into the twentieth century. Electric motors finally gave each machine its own source of rotation. Wires replaced the long shafts and belts, and stopping one lathe no longer changed the load on a central engine driving the entire mill.

The most dramatic change was how much power newer engines extracted from coal. Corliss valves controlled steam expansion more precisely, compound engines expanded it through several cylinders, and turbines eventually replaced the piston with a continuously rotating wheel. Newcomen converted only about half a percent of the heat into useful work. Watt's condenser raised the useful share to roughly three percent, enough for steam power to move away from the coal mines. By the 1890s, high pressure and compound expansion pushed large marine engines such as the Titanic's beyond ten percent. A modern steam turbine plant converts more than forty percent.

## Footnotes

Thomas Savery tried to use higher-pressure steam in the 1690s with boilers made from soldered copper. The fire could soften the solder, and the leaking joints needed frequent repair. Newcomen took a different route. Because the steam in his boiler was barely above atmospheric pressure, he could use thin lead and wrought-iron plates joined with rivets. The seams still leaked and the metal corroded, but the boiler did not have to contain the pressure that Savery's pump required. ↩

Casting a large iron cylinder was much easier than making the inside straight and round. Newcomen's cylinders were ground by hand, then sealed with a leather flap covered by a layer of water, which could follow the uneven bore. Denis Papin had proposed the vacuum-piston principle in 1690: a small amount of water boiled beneath a piston and pushed it upward, then condensation allowed the atmosphere to force it down again. His apparatus demonstrated a single stroke but did not become a continuously running engine. ↩

A piston 50 centimetres across has about 2,000 square centimetres of area, enough to collect two tonnes of force from a perfect vacuum. After allowing for leaks and the weight of the pump rods, it might do about four kilowatts of useful work. A horse can sustain much less than one horsepower over a working day, so replacing the engine required a relay of perhaps fifteen or twenty animals. Watt later sold his engines by the number of horses they replaced, and fixed one horsepower at 33,000 foot-pounds per minute. ↩

For a barrel with radius

*r*and length*L*, the cut has an area of 2*rL*, so pressure*p*pushes the halves apart with a force of 2*prL*. Two edges of length*L*resist that force, leaving*pr*in each metre of plate. At two atmospheres and a half-metre radius, this is about ten tonnes per metre. The stress running lengthwise is only half as large, which is why a cylindrical boiler tends to split along its length like a sausage. A sphere divides the load equally and is stronger still, but it was much harder to make from rolled and riveted plate. ↩Watt's engine needed a much more accurate cylinder than Newcomen's loose, water-sealed piston. Around 1775, the ironmaster John Wilkinson built a boring mill with a rigid cutting bar supported at both ends, adapting techniques he had developed for boring cannons. In 1776, Matthew Boulton reported that a 50-inch cylinder installed at Tipton varied by less than the thickness of an old shilling. This accuracy kept the steam from leaking around Watt's piston and made the new engine practical. ↩

For a cylinder with volume

*V*and pressure*p*, admitting steam for the full stroke produces work*pV*. With cutoff at half stroke, the admitted steam produces*pV*/2 during the first half. As it expands through the rest of the cylinder, it adds about 0.35*pV*more, assuming it follows Boyle's law and remains hot. This gives 85 percent of the full-stroke work from half the steam. Cutting off earlier saves still more steam, but eventually the falling pressure becomes too weak to overcome friction and the poor leverage near dead centre. ↩The pressure and volume graph outlived the mechanical indicator. In 1834, Émile Clapeyron used the same type of diagram to explain Sadi Carnot's theory of heat engines, and thermodynamics still plots pressure against volume today. ↩

-
James Pickard patented the use of a crank on a steam engine in 1780, so William Murdoch designed the

*sun-and-planet gear*as a way around the patent. A gear attached to the connecting rod travelled around a second gear on the flywheel shaft, turning the shaft twice for every cycle of the beam. Once Pickard's patent expired in 1794, builders returned to the much simpler crank used on our engine.Murdoch's mechanism belongs to the

*epicyclic*, or planetary, family of gears. Several planet gears can share the load while the input and output remain on the same axis, making the arrangement compact and strong. Planetary gears appear in cordless drills, bicycle hubs, automatic transmissions and wind turbines. Hybrid cars even use them to divide power between the engine, electric motor and wheels. ↩ -
If we slice the wrapped rope into small pieces and add the force vectors, each piece has a small inward force equal to the local tension multiplied by the angle it covers. Friction can remove up to

*μ*times that inward force, about 0.3 for rope on cast iron.Repeating that fractional reduction produces the exponential

*e*−μθ. With a 2,000-newton pull, about the weight of an upright piano, one turn around the post leaves 300 newtons, two leave 46, and three leave seven. ↩ A flat belt tends to wander off a truly cylindrical pulley. Millwrights made the pulley slightly larger at the centre, forming a shallow

*crown*that continually steers the belt back. When the belt arrives off-centre it first meets a coned surface, and the tilted contact carries its leading edge a little towards the crown on each turn. Once centred, both halves of the crown steer equally and the belt remains centred. This simple change kept the belt on the pulley without guides. ↩Between 1775 and 1800, the Boulton & Watt partnership built 496 engines. Thirty-eight percent were pumping engines, while sixty-two percent produced rotation, mostly for the textile industry. ↩

In 1788, Boulton told Watt that he had seen spinning balls used to regulate millstones in Manchester. Watt adapted the mechanism to steam engines, but never patented the borrowed idea. ↩

The height of the balls gives a surprisingly direct measurement of speed. Balancing their outward motion against gravity gives

*h*=*g*/*ω*2, where*h*is the vertical distance below the hinge. The mass cancels, so heavier balls push harder on the linkage but rise to the same height. At the crankshaft's speed the arms would need to be about a metre long, so the bevel gears spin the governor faster and let it fit on the short pillar. ↩The oldest rotative engine still in existence, installed at Whitbread's brewery in London in 1785, is built to the same pattern as ours. Its cylinder was 64 centimetres across and the piston swept 1.8 metres on each stroke, a column of steam taller than a person. The flywheel, 4.3 metres across, turned twenty times a minute — a leisurely one revolution every three seconds — burning roughly forty kilograms of coal an hour. Watt rated it at ten horsepower, and it replaced the wheel of horses that had driven the brewery's mills. When it was converted to double action in 1795, the same cylinder was re-rated to fifteen horsepower; the brewery declined twenty, because Boulton & Watt's annual fee rose with the power. It stayed at work for a hundred and two years. ↩

American paddle steamers kept the beam engine into the 1880s, mounting a

*walking beam*high above the deck. Their paddle wheels needed high torque at only about twenty revolutions per minute, and a shallow riverboat had more room above the water than below it. Ocean-going ships folded similar machinery into the hull, then moved to smaller and faster engines as the screw propeller replaced the paddle wheel. ↩