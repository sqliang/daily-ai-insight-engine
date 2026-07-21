---
title: 'Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s'
source: https://news.ycombinator.com/item?id=48968606
author:
- '[[section33]]'
published: '2026-07-19'
created: '2026-07-20'
manifest_dates:
- '2026-07-20'
description: 'I might be the only SRE on Earth with his own bowling center. It''s
  a more in-depth gig than you''d think.My family and I bought an abandoned 8-lane
  bowling center in the rural mid-west. In our small town there weren''t many recreation
  options for families. You''ve heard of a food desert? This is an R&R desert.It had
  been abandoned for a good reason. The roof leaks, the electrical system was constantly
  surging, and my 70-year-old bowling equipment (still) doesn''t work perfectly. The
  system that keeps your score is particularly interesting to me. It''s the thing
  you watch during your game, but it fades into the background beyond that. Turns
  out these things are really cool, but absurdly expensive.Ours was installed in 2008
  and cost six figures. It''s calculating ball speed and trajectory, camera-based
  pin detection (object detection and trig, on ICs!), runs the fouling, the animations,
  the pinsetting machine and ball return. Very cool stuff for its age.From the business
  perspective, my facility only cost me $105k. To forklift-replace the score keeping
  system runs anywhere between $80-$120k, depending on features, vendor, and unit
  age. No upgrades or service contracts, mind you, and every feature and customization
  is a new line item. That''s for a 1:1 replacement on a system installed in 2008.
  Incredible, given how fast the tech world moves.Replacement parts cost a shocking
  $4000 per pair of lanes. But wait, the bowling machines themselves are 70 years
  old, so what''s this "advanced" system actually doing back there? Actuating a single
  relay to trigger that big old machine. Everything else is strictly mechanical. Meanwhile
  I''ve got a six-figure invoice in my hand. I''m upset.Given the state of open hardware,
  computer vision, real-time event streaming, and open source running megascale products
  worldwide, there had to be a way to do this myself.So far I''ve built an equivalent
  prototype for about $200 per lane-pair, $400 if you''re fancy. ESP32 and ESPNow
  with an RS485 fallback, reporting to a raspberry pi lane computer that''s really
  just redis and a state machine bolted to an ESP32 gateway for the mesh.Since it''s
  all ESP32, I''ve got a fistful of spare controllers in a drawer, pre-flashed or
  waiting to be. All common off-the-shelf hardware: microcontrollers wired to relays,
  optocouplers, and IR-break-beam sensors, each running slightly different firmware.
  Writing the firmware and protocol is the actual hard part.It''s an ESPNow star-topology
  mesh: each node emits events from its sensors and accepts commands for its controls,
  reporting to a gateway node connected to the raspi over UART. From there it''s event
  streaming: RX packets get translated and tossed into redis, commands relay back
  out to the mesh as needed. RS485 sits underneath as a wired fallback for noisy RF
  environments.Once the data''s in redis, it''s familiar middleware/React/websocket/pub-sub
  stuff. Any React dev can build their own UI and bowling animations. Since it all
  runs on commodity hardware, I can do legit anything I want as the proprietor, and
  I own all my data. Repairs take five minutes; I can swap the rig on a lane pair
  in under 10. I''d bet a house like mine could go from zero to running in an hour
  or two.We''re calling it OpenLaneLink, and I plan to open source the hardware, firmware,
  and software stack when it''s ready. Bowling is fun, and I want to help keep it
  affordable for alleys like mine. I hate vendor lock-in. I''m not a fan of closed
  systems, calling support for every hiccup, or paying to "white label" my own equipment.
  Want to go Tron-themed for a night? Good luck finding a neon neumorphic theme in
  something bought at the turn of the century.All that bugged me. Sure, bowling equipment
  is niche, but the open hardware and software landscape is amazing.Thanks for reading!
  Let me know if anyone''s interested in more posts about this bowling nonsense. Comments
  URL: https://news.ycombinator.com/item?id=48968606 Points: 2275 # Comments: 243'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 7a5ada317dd6ddd7
---

I might be the only SRE on Earth with his own bowling center. It's a more in-depth gig than you'd think.

My family and I bought an abandoned 8-lane bowling center in the rural mid-west. In our small town there weren't many recreation options for families. You've heard of a food desert? This is an R&R desert.

It had been abandoned for a good reason. The roof leaks, the electrical system was constantly surging, and my 70-year-old bowling equipment (still) doesn't work perfectly. The system that keeps your score is particularly interesting to me. It's the thing you watch during your game, but it fades into the background beyond that. Turns out these things are really cool, but absurdly expensive.

Ours was installed in 2008 and cost six figures. It's calculating ball speed and trajectory, camera-based pin detection (object detection and trig, on ICs!), runs the fouling, the animations, the pinsetting machine and ball return. Very cool stuff for its age.

From the business perspective, my facility only cost me $105k. To forklift-replace the score keeping system runs anywhere between $80-$120k, depending on features, vendor, and unit age. No upgrades or service contracts, mind you, and every feature and customization is a new line item. That's for a 1:1 replacement on a system installed in 2008. Incredible, given how fast the tech world moves.

Replacement parts cost a shocking $4000 per pair of lanes. But wait, the bowling machines themselves are 70 years old, so what's this "advanced" system actually doing back there? Actuating a single relay to trigger that big old machine. Everything else is strictly mechanical. Meanwhile I've got a six-figure invoice in my hand. I'm upset.

Given the state of open hardware, computer vision, real-time event streaming, and open source running megascale products worldwide, there had to be a way to do this myself.

So far I've built an equivalent prototype for about $200 per lane-pair, $400 if you're fancy. ESP32 and ESPNow with an RS485 fallback, reporting to a raspberry pi lane computer that's really just redis and a state machine bolted to an ESP32 gateway for the mesh.

Since it's all ESP32, I've got a fistful of spare controllers in a drawer, pre-flashed or waiting to be. All common off-the-shelf hardware: microcontrollers wired to relays, optocouplers, and IR-break-beam sensors, each running slightly different firmware. Writing the firmware and protocol is the actual hard part.

It's an ESPNow star-topology mesh: each node emits events from its sensors and accepts commands for its controls, reporting to a gateway node connected to the raspi over UART. From there it's event streaming: RX packets get translated and tossed into redis, commands relay back out to the mesh as needed. RS485 sits underneath as a wired fallback for noisy RF environments.

Once the data's in redis, it's familiar middleware/React/websocket/pub-sub stuff. Any React dev can build their own UI and bowling animations. Since it all runs on commodity hardware, I can do legit anything I want as the proprietor, and I own all my data. Repairs take five minutes; I can swap the rig on a lane pair in under 10. I'd bet a house like mine could go from zero to running in an hour or two.

We're calling it OpenLaneLink, and I plan to open source the hardware, firmware, and software stack when it's ready. Bowling is fun, and I want to help keep it affordable for alleys like mine.
I hate vendor lock-in. I'm not a fan of closed systems, calling support for every hiccup, or paying to "white label" my own equipment. Want to go Tron-themed for a night? Good luck finding a neon neumorphic theme in something bought at the turn of the century.

All that bugged me. Sure, bowling equipment is niche, but the open hardware and software landscape is amazing.

Thanks for reading! Let me know if anyone's interested in more posts about this bowling nonsense.