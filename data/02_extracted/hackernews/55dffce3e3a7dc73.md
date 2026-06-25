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
extract_result: success
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