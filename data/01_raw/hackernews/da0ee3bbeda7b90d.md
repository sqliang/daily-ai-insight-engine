---
title: 45°C cooling design cuts data center water use to near zero
source: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
author:
- '[[nitin_flanker]]'
published: '2026-06-24'
created: '2026-06-25'
description: 'Article URL: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
  Comments URL: https://news.ycombinator.com/item?id=48660178 Points: 328 # Comments:
  219'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: da0ee3bbeda7b90d
---

Hot tubs sit at about 38 to 40 degrees Celsius, warm enough that most people can only soak for about 15 minutes. NVIDIA’s newest AI servers can run their cooling liquid even hotter — up to 45 degrees Celsius, or 113 degrees Fahrenheit. That higher temperature limit is precisely what makes them more energy efficient.

The Rubin generation of NVIDIA AI infrastructure is the world’s first to achieve 100% liquid cooling — every chip, every networking component, cooled entirely by liquid in a closed loop with no fans anywhere in the system. This liquid cooling methodology is outlined in the NVIDIA DSX AI factory reference design, a guide that outlines best practices to design, build and operate the entire AI factory infrastructure stack.

Although each generation offers significantly more computing power for each watt, full liquid-cooled AI compute infrastructure enables data centers to dramatically reduce cooling energy consumption — making a meaningful difference to overall data center energy use at hyperscale.

“The NVIDIA DSX reference design for AI factories has zero water consumption — we have eliminated massive amounts of power usage and pretty much all water usage,” said Ali Heydari, director of data center cooling and infrastructure at NVIDIA. “With dry-cooler-based designs, it’s a closed-loop system with no evaporative water cooling — outside of maybe 1% of the year when we might need chillers in some climates.”

Historically, cooling alone has accounted for up to 40% of a data center’s electricity consumption, making it one of the most significant areas where efficiency improvements can drive down both operational expenses and energy demands.

Industry estimates suggest that raising chiller plant temperatures by just one degree can cut cooling energy costs by about 4%. At scale, those savings add up quickly. A 50-megawatt hyperscale facility can save over $4 million annually in cooling-related energy and water costs by moving to liquid-cooled infrastructure.

In favorable climates, NVIDIA’s 45-degree liquid-cooling architecture can enable chiller-less operation with dry coolers, reducing facility cooling water consumption from roughly 2.6 million gallons per megawatt per year for conventional cooling-tower-based systems to near zero — up to a 100% reduction in water use.

The reason: traditional air-cooled data centers depend on large volumes of cooled air to remove heat from IT equipment, often requiring energy-intensive cooling infrastructure during hot weather. With NVIDIA’s 45-degree liquid cooling, heat is captured directly at the chip and transported through liquid loops operating at much higher temperatures, allowing outdoor dry coolers to reject heat efficiently for much of the year while significantly reducing mechanical cooling requirements and facility water consumption.

The data center ambient temperature is flexible — warm summer air is fine — because nothing in the server depends on cool air. The liquid does all the work — and the same liquid can be recirculated in a closed loop so no new water is consumed to cool the chips.


**A New Standard for the Industry**

Because the NVIDIA Rubin platform integrates 100% liquid-cooled infrastructure, every cloud provider and data center operator building for it is making the transition.

The ecosystem is keeping pace. Motivair, the advanced cooling division of Schneider Electric, has worked alongside NVIDIA’s product roadmap for nearly a decade — and Richard Whitmore, its president and CEO, says the relationship only intensified as power densities crossed the threshold where air cooling was no longer a viable option.

“Once the watts per chip crossed a certain level, liquid cooling became mandatory,” said Whitmore.

**Too Hot to Cool AI Infrastructure Is Hotter Than You’d Think**

There’s a long-standing misconception in the industry that a cold data center is an efficient one. Decades ago, if a data center didn’t feel like a walk-in freezer, people would assume something was wrong.

In reality, chips can sustain far warmer environments than that instinct suggests. Silicon processors generate enormous internal heat — the coolant entering a fully liquid-cooled chip at 45 degrees Celsius exits at roughly 55 degrees, having absorbed that heat load across the chip surface. Yet performance doesn’t degrade.

The processors continue to operate at full performance because liquid-cooled cold plates keep device temperatures within validated operating limits, even with coolant entering the rack at 45 degrees Celsius.

**No Fans, No Cold Aisles — A Fundamentally Different Machine**

Walk into a traditional data center and notice two things: the noise — cooling fans contribute to total noise levels at or above 85 decibels, loud enough to require ear protection — and the physical choreography of hot aisles and cold aisles, carefully managed to push cooled air across components.

The Rubin architecture changes the picture.

Coolant — 75% water and 25% propylene glycol — flows through cold plates that sit directly on processors, pulling heat out at the source. Running that coolant at up to 45 degrees Celsius means that in many climates, the facility loop can reject heat without turning on mechanical chillers and noisy fans.

That unlocks something beyond energy savings: the possibility of eliminating water consumption entirely.

In the right geography — somewhere with reliably cool outdoor air — a liquid-cooled data center can reject its heat through coolant distribution units that capture heat directly at the source and transport it to outdoor dry coolers, essentially large radiator coils positioned outside the building.

The loop is filled once and runs closed for the life of the facility. And it takes dramatically less space in the AI factory compared to traditional air-cooling infrastructure.

“In the right geographic location, with the right system design, you don’t need any refrigeration equipment,” Whitmore said. “You can just put big radiator coils outside and use the air temperature for all your cooling. It’s incredibly efficient.”

The geography caveat matters. A data center in the Scottish Highlands and one in Phoenix, Arizona, face very different realities. But even in warmer climates, the shift toward 45-degrees-Celsius coolant moves operators significantly closer to that chiller-less ideal — where chillers may turn on just a few days a year when the outside air temperature demands it.

Another key benefit of this new model for AI factories is the potential for waste heat recovery, where residual heat from AI factory operations can be repurposed to heat commercial or residential buildings nearby.

**The Engineering Problem Nobody Had Solved**

Previous liquid-cooled servers were hybrid: GPUs and CPUs got cold plates, but the rest of the system stayed air-cooled, with finned heat sinks designed to shed heat into moving air. In a fully liquid-cooled server, the cooling for these components needed to be completely redesigned to use liquid.

NVIDIA’s thermal engineering team reworked how those components handle heat, designing cooling loops that simplify how liquid is routed to multiple high-power chips on the board using a single inlet and outlet, resulting in a cleaner tray-level cooling architecture.

One visible outcome: Rubin servers have clean, sealed front panels where air-cooled servers have perforated bezels. Another: fully liquid cooled servers enable higher rack density than air-cooled servers, so a system that previously occupied six rack units now fits in two — more compute, less space, less noise.

AI workloads are not getting lighter. The compute demand driving data center construction is growing faster than almost any other category of infrastructure investment.

Without efficiency improvements in how that compute is cooled, the energy cost of running AI at scale would grow in lockstep with the hardware. Liquid cooling at up to 45 degrees Celsius — hotter than a hot tub, cooler for the planet — is one of the most important tools the industry has to close that gap.

*Learn more about **liquid cooling**, the **NVIDIA DSX** platform for AI factories and NVIDIA’s approach to **energy-efficient AI infrastructure.*