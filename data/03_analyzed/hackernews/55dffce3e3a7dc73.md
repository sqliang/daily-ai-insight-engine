---
title: Pokémon Go Scans Trained the Navigation Tech for Military Drones
source: https://dronexl.co/2026/06/09/pokemon-go-scans-niantic-vantor-military-drone-navigation/
author:
- '[[vrganj]]'
published: '2026-06-11'
created: '2026-06-11'
description: 'Article URL: https://dronexl.co/2026/06/09/pokemon-go-scans-niantic-vantor-military-drone-navigation/
  Comments URL: https://news.ycombinator.com/item?id=48487029 Points: 201 # Comments:
  75'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 55dffce3e3a7dc73
source_type: community_discussion
tldr: Pokémon Go玩家拍摄的300亿张扫描数据被用于训练军事无人机导航系统
objective_summary: Pokémon Go玩家在不知情下拍摄了约300亿张环境扫描，Niantic Spatial将其训练为视觉定位系统（VPS），并于2025年12月与国防承包商Vantor合作，将系统整合用于GPS拒止环境下的无人机和军事机器人导航。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Niantic Spatial
  - Vantor
  - Maxar Intelligence
  - Niantic
  - Google
  - Scopely
  - Savvy Games Group
  - In-Q-Tel
  - Keyhole
  - Coco Robotics
  technologies:
  - VPS
  - Visual Positioning System
  - GPS
  key_people:
  - Brian McClendon
  - John Hanke
  - Floris De Hingh
  - Jeroen van den Hoven
  - Iris Muis
  - Adrian Hon
  - Haye Kesteloo
key_logic_flow:
- Pokémon Go自2021年起要求玩家拍摄现实世界场景以获取游戏奖励，累计收集约300亿张环境扫描数据，用户授予了可转让、可再许可的扫描使用权。
- Niantic Spatial利用这些扫描数据训练了视觉定位系统（VPS），该系统无需卫星信号，通过摄像头图像与3D模型匹配即可确定位置。
- 2025年12月16日，Niantic Spatial与国防承包商Vantor（前身为Maxar Intelligence）宣布合作，将地面VPS与Vantor的Raptor空中导航软件整合，用于GPS拒止环境下的无人机和军事装备协同定位。
- Vantor否认直接使用Pokémon Go数据，但拒绝说明其部署的模型是否曾使用这些扫描数据进行训练，这一模糊立场引发了数据来源争议。
- Niantic的前身Keyhole曾接受CIA风投机构In-Q-Tel资助，其技术被用于支持伊拉克战争中的美军；2025年Niantic分拆后，游戏业务被沙特主权基金收购，地图技术则独立为Niantic
  Spatial并向防务领域发展。
- 该事件引发广泛的数据同意伦理争议：玩家为游戏目的提供的扫描数据可能被用于武器系统，而用户无法预见或追溯其数据的最终用途。
impact_score:
  score: 6.0
  reason: 该事件并非AI模型或算法的技术突破，但其揭示的数据同意伦理危机具有深远的行业影响。Pokémon Go通过游戏奖励机制收集约300亿张环境扫描数据，用户授予了可转让、可再许可的权限，这些数据最终被训练为视觉定位系统(VPS)并整合到军事无人机导航中。这起事件将AI数据治理的'同意困境'推向公众视野——游戏用户无法预见其数据被用于武器系统，且一旦数据融入模型训练，追溯和删除几乎不可能。这对所有依赖UGC（用户生成内容）训练AI的公司的数据合规策略构成了实质性冲击，可能引发监管收紧和用户信任危机。评分理由：虽然不是技术范式转移，但数据伦理风暴可能改变行业的数据采集和许可实践。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: 用户生成数据的同意边界与军事化应用伦理
hype_assessment:
  level: low
  reason: 该报道来自行业媒体 dronexl.co 的调查性文章，采用事实驱动叙事而非营销语言。文中未出现'颠覆''革命性'等PR滥用词汇，而是以具体的日期（2025年12月16日合作公告）、具体数据（300亿张扫描、7000万美元合同）、具体人物引述（TU
    Delft伦理教授、荷兰玩家）支撑论述。Vantor否认直接使用但拒绝排除模型训练数据的模糊立场被如实呈现，没有过度渲染或耸人听闻。判定为低炒作度。
information_entropy: high
domain_disruption:
  technical_innovation: 视觉定位系统(VPS)通过匹配摄像头图像与3D世界模型实现GPS拒止环境下的精确定位，结合Vantor的Raptor空中导航软件实现空地协同定位。其技术本质是利用大规模众包视觉数据构建可搜索的3D空间索引，使无人机和地面装备在没有卫星信号时仍能共享统一坐标框架。
  business_model: 游戏公司通过'奖励式数据采集'积累海量高价值空间数据，随后将数据使用权通过可转让、可再许可的条款打包出售给国防承包商。这一模式揭示了AI时代数据货币化的新路径：面向消费者的应用（游戏/社交）作为数据采集前端，B2G（面向政府）的防务解决方案作为变现出口。Niantic分拆为游戏（被沙特收购）和地图技术（独立为Niantic
    Spatial）两个实体后，后者向防务领域转型，体现了空间数据资产的独立商业价值。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: VPS技术填补了一个根本性且日益严重的市场真空——GPS拒止环境下的自主导航。随着电子战和GPS干扰从战场扩散至民用空域，该需求确定性极高。Niantic
    Spatial拥有约300亿张实景扫描数据，这一数据护城河在可预见的未来几乎无法复制，形成极强的网络效应（更多扫描→更优模型→更多客户→更多扫描）。国防领域的政府合同提供稳定且长期的现金流（Vantor已持有NGA
    7000万美元合同），且VPS可横跨军用无人机、地面机器人、AR眼镜、自动驾驶等多个终端场景，TAM天花板高。但6分扣在：数据同意的伦理争议可能导致监管限制（欧盟GDPR追溯风险、数据使用权诉讼），且当前盈利模式高度依赖国防领域，民用商业化路径尚未验证。综合来看，这是GPS-denied导航赛道的潜在基础设施，但伦理和监管不确定性需要在后续轮次定价中充分折现。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Niantic Spatial
- Vantor
- Anduril
- Shield AI
competitive_casualty:
- 传统 GPS 导航方案提供商
- 缺乏大规模实景数据的 VPS 初创公司
- 纯民用地图技术公司
market_opportunities:
- 数据溯源与同意管理工具——开发AI训练数据生命周期追溯平台，帮助企业和监管机构验证数据是否在用户知情同意下收集，尤其适用于存在军事/防务二次用途争议的场景
- 视觉定位系统（VPS）在非军事场景的商用落地——仓库机器人、室内导航、自动驾驶城市峡谷等GPS盲区领域需求旺盛，Niantic Spatial的VPS技术有巨大商业化溢出潜力，创业者可聚焦物流、零售、智慧城市等垂直场景
- 消费者数据伦理审计咨询——随着公众对游戏/社交数据被用于武器系统警觉性上升，面向游戏公司、地图科技公司提供数据伦理风险评估和合规体系设计服务将成为刚需
risk_matrix:
  regulatory: GDPR目的限制原则风险：用户授权仅限于游戏内扫描，未明示军事/防务用途，Niantic的"可转让、可再许可"条款可能不满足GDPR第5条目的限制原则，欧盟用户可提起集体诉讼；欧美防务数据出口管制也可能限制该技术跨境部署
  technological: VPS面临替代性技术路线竞争：基于基础模型的视觉SLAM（如Meta、Google、Apple的替代方案）和低成本惯性导航方案均可实现GPS拒止导航，架构过时或被通用视觉模型替代的风险存在
  competitive: 地图与防务巨头同时挤压：Google（Street View+VPS）、Apple（ARKit定位）、Maxar原身竞品以及Palantir等防务AI公司均在布局同类能力，Niantic
    Spatial可能面临大厂数据规模和军方关系双重挤压
  ethical: 这是该事件的核心争议：约30亿张扫描数据由用户在不知情场景下贡献，数据最终流向军事无人机导航系统，用户无法追溯或撤回同意；这构成了典型的"知情同意缺口"和数据伦理滑坡，且一旦AI模型完成训练，原始数据贡献无法被移除或追责
  additional:
  - Niantic Spatial与Vantor之间的数据隔离声明模棱两可（否认直接使用但拒绝澄清模型是否曾使用扫描数据训练），这种不透明姿态可能引发更广泛的公众信任危机，进而波及其游戏业务（如Scopely运营下的Pokémon
    Go用户流失）
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
---

Hundreds of millions of Pokémon Go players spent years filming the streets, parks, and buildings around them to earn in-game rewards. Those roughly 30 billion environmental scans are now owned by **Niantic Spatial**, and they helped train a camera-based navigation model that a U.S. defense contractor is preparing to put into drones and other military robots. Most of the players had no idea.

The pipeline runs from a mobile game to the battlefield in three steps. Players scanned the physical world. Niantic Spatial turned those scans into a 3D map that lets a machine locate itself by sight when satellite signals fail. And in December 2025, Niantic Spatial announced a partnership with **Vantor**, the defense and intelligence firm formerly known as Maxar Intelligence, to fuse that ground-level system with Vantor’s aerial navigation software for use in GPS-denied operations.

I have spent years covering how drones lose their way the moment an electronic warfare unit switches on a jammer, a problem that has spread from the battlefield into civilian airspace, from Ukrainian workshops cycling through navigation generations to American programs scrambling for alternatives. The unsettling part of this story is not the technology. It is where the training data came from, and whether the people who supplied it would have agreed had anyone explained the destination.

## Pokémon Players Filmed Their Surroundings for Rewards and Fed a 3D Map

Since 2021, Pokémon Go has asked players to record short videos of real-world locations, called Pokéstops, to earn extra in-game items. Scanning all the buildings, streets, and trees in a 360-degree sweep was optional, and Niantic asked separately for permission to keep the footage. Granting it meant agreeing to extra terms.

Those terms handed Niantic a transferable, sublicensable license to the scans, meaning the company could resell the imagery to third parties. Floris De Hingh, a 34-year-old Dutch player who downloaded the game on its first available day in 2016, told Trouw he never connected the footage he captured to a system that would steer military drones. “I was just playing a game,” he said. He had even scanned the inside of his own apartment.

The collected scans, around 30 billion of them according to Trouw, became the raw material for a Visual Positioning System, or **VPS**. Where GPS depends on a satellite signal, VPS works out where a camera is by matching what it sees against a detailed 3D model of the world. Two recognizable reference points a few pixels wide can be enough to fix a location. Niantic Spatial CTO Brian McClendon, who previously led the team behind Google Maps, Google Earth, and Street View, has said the approach suits robots operating where GPS regularly drops out, such as dense cities, and where signals are deliberately blocked, such as war zones.

## Vantor Will Pair the Ground Map With Aerial Drone Navigation

The Vantor partnership, announced on December 16, 2025, joins two positioning systems into one. Niantic Spatial handles localization on the ground by aligning a camera feed against its model. Vantor’s Raptor software, launched in February 2025, does the same job in the air using a drone’s camera and Vantor’s proprietary 3D terrain data. Combined, the companies say, a drone overhead and a vehicle or dismounted operator below can share the same coordinates in real time with no satellite link. The principle is already turning up on the other side of the front, where a downed Russian drone was found matching live camera feeds against preloaded terrain imagery rather than trusting a single GPS module.

Vantor’s own framing is blunt about the problem it targets. The joint release names GPS “unavailability, spoofing, interference, and jamming” as the vulnerability, and lists autonomous drones, vehicles, augmented reality glasses, and other field assets as the platforms meant to run on the shared system. Niantic Spatial’s go-to-market lead told defense outlet Tectonic the goal is thousands of devices operating on one coordinate framework in an electronic-warfare-heavy environment. Field testing of the integrated system is planned for early 2026.

Vantor is not a startup dabbling in defense. Rebranded from Maxar Intelligence on October 1, 2025, it is a prime contractor to the National Geospatial-Intelligence Agency, holding a follow-on award worth $70 million under the agency’s Global Enhanced GEOINT Delivery program, which serves more than 400,000 U.S. government users. This is a company built around national security imagery, now adding GPS-independent navigation to its catalog.

## Vantor Denies Using the Pokémon Game Data, Then Declines to Rule It Out

Asked directly whether the military-bound system relies on Pokémon Go imagery, Vantor told Trouw it would not use the game’s data. The company then declined to say whether the model it plans to deploy was trained on those scans in the past. Niantic Spatial, responding to earlier questions about a separate deal, said the scans were used to train an “early version” of its navigation model. On the defense partnership specifically, the company said it had no new information to share.

That gap is the heart of the dispute. Jeroen van den Hoven, a professor of ethics and technology at TU Delft, told Trouw the conclusion is hard to avoid. “Without the huge number of scans from all those gamers, the development of this system would never have progressed so quickly,” he said. He added that AI models begin with a dataset and then absorb far more data until the original contributions blur into patterns that can no longer be traced. Once a scan is folded into the model, in other words, proving it is or is not in there becomes nearly impossible.

Van den Hoven did not condemn battlefield VPS outright. If it helps Ukraine win a just war against an aggressor, he said, that is a good development. His worry is the system falling into the wrong hands, and the broader pattern of players being misled about where their data goes. He called the episode a red flag.

## Niantic’s Roots Run Back to a CIA-Backed Mapping Firm

The military turn looks less like a swerve once you trace the company’s lineage. Niantic grew out of Keyhole, a geographic data firm that took funding in 2003 from In-Q-Tel, the venture arm financed by the CIA. An In-Q-Tel release from that year stated Keyhole’s services were used to support U.S. troops during the Iraq War. Google bought Keyhole the following year, and Keyhole CEO John Hanke went on to lead the team behind Google Maps, Google Earth, and Street View.

Hanke formed Niantic Labs inside Google in 2010, then spun it out in 2015. The company collected camera imagery from players once before, through its 2014 game Ingress, using the same method later applied in Pokémon Go. In 2025 the structure split again: Scopely, owned by Saudi Arabia’s Savvy Games Group and ultimately the kingdom’s Public Investment Fund, acquired Niantic’s games business for $3.5 billion in a deal that closed in late May, while the technology platform spun off as the standalone Niantic Spatial under Hanke. The games went to a Saudi sovereign wealth fund. The map went to defense.

## The Consent Question Reaches Far Beyond One Game

Pokémon Go is not the only camera in your pocket feeding a map. Meta’s smart glasses continuously scan a wearer’s surroundings, Apple’s AR hardware builds 3D models of interiors, and Waymo’s self-driving cars reconstruct detailed street layouts. Niantic Spatial has signaled interest in more indoor footage specifically, and in March 2025 it announced a deal with Coco Robotics to guide delivery robots already rolling through U.S. cities and Helsinki.

Iris Muis, a data-ethics expert at Utrecht University’s Data School, framed the trap plainly: a user cannot picture how their data might be used later. Maybe in five years there is an application with effects you fundamentally disagree with. British game designer Adrian Hon has gone further, advising Pokémon Go players to stop making scans and consider smaller games less likely to resell data. De Hingh, who quit the game over a year ago because he was tired of the updates rather than the data terms, called the news an enormous eye-opener. “A game should stay a game,” he said.

## DroneXL’s Take

The navigation problem this solves is real, and DroneXL has documented it from the trenches. When I wrote about Ukraine’s FirePoint in March, the detail that stuck was not the 200 strike drones a day. It was that the company had built seven generations of navigation systems in roughly three years, landing on a terrain-matching setup that uses a cheap night camera to fly without GPS. Russia can jam GPS. It cannot jam a drone that does not need it. Visual positioning is the same insight, scaled up and packaged for export.

So I am not going to pretend GPS-denied navigation is sinister on its face. It is one of the most important capability gaps in the industry, the reason Shield AI’s V-BAT keeps flying when radio links die, the reason the Pentagon’s Drone Dominance evaluations are adding GPS denial to Phase II this year. The discomfort here is narrower and sharper. The training data came from people who thought they were catching Pikachu, under a license most never read, sold up a chain that ends at a sovereign wealth fund and a defense prime. Consent obtained for a game is not consent for a weapons program, even if the end use turns out to be defensible.

Vantor’s non-answer is what I would watch. The company says it will not use Pokémon Go data and refuses to say whether the model it is fielding was already trained on it. Those are not the same statement, and the difference is the whole story. Van den Hoven is right that once scans are baked into a model, tracing them back is close to impossible, which conveniently makes the denial unfalsifiable. The early-2026 field tests will tell us whether this air-to-ground system is real or a press release. They will not tell us whose footage is inside the model, and so far nobody at either company will.

*Sources: Trouw, Volkskrant.*

*DroneXL uses automated tools to support research and source retrieval. All reporting and editorial perspectives are by Haye Kesteloo.*

Check out our Classic Line of T-Shirts, Polos, Hoodies and more in our new store today!

## MAKE YOUR VOICE HEARD

Proposed legislation threatens your ability to use drones for fun, work, and safety. The **Drone Advocacy Alliance** is fighting to ensure your voice is heard in these critical policy discussions.Join us and tell your elected officials to protect your right to fly.

## Get your Part 107 Certificate

Pass the Part 107 test and take to the skies with the Pilot Institute. We have helped thousands of people become airplane and commercial drone pilots. Our courses are designed by industry experts to help you pass FAA tests and achieve your dreams.

Copyright © DroneXL.co 2026. All rights reserved. The content, images, and intellectual property on this website are protected by copyright law. Reproduction or distribution of any material without prior written permission from DroneXL.co is strictly prohibited. For permissions and inquiries, please contact us first. DroneXL.co is a proud partner of the Drone Advocacy Alliance. Be sure to check out DroneXL's sister site, EVXL.co, for all the latest news on electric vehicles.

FTC: DroneXL.co is an Amazon Associate and uses affiliate links that can generate income from qualifying purchases. We do not sell, share, rent out, or spam your email.