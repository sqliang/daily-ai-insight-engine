---
title: Why is everyone trying to build a solid-state battery?
source: https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a
author:
- '[[crescit_eundo]]'
published: '2026-07-30'
created: '2026-07-31'
manifest_dates:
- '2026-07-31'
description: 'Article URL: https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a
  Comments URL: https://news.ycombinator.com/item?id=49109193 Points: 194 # Comments:
  242'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: abeae2d27bc60a17
source_type: community_discussion
tldr: 固态电池用固体材料替代锂电池液体电解质，理论上更轻、更安全且能量密度更高。截至2024年宁德时代已有超过1000人从事相关研发，比亚迪、LG、三星等厂商跟进，美欧创业公司截至2025年累计融资超40亿美元。
objective_summary: 本文以科普视角解释固态电池受追捧的原因：它用固体电解质替代可燃的液体电解质，理论上可消除锂枝晶穿透隔膜引发的热失控风险，从而允许采用纯金属锂负极并大幅减轻电池的材料支架重量。文章引用数据称，截至2024年宁德时代有超过1000人专职研发固态电池，比亚迪、LG、三星等电池厂商也在推进该技术，截至2025年美国和欧洲的固态电池创业公司累计融资超过40亿美元。文章同时指出，宁德时代董事长将固态电池技术成熟度评为9级中的4级，商业可行性尚未确立。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - CATL
  - BYD
  - LG
  - Samsung
  technologies:
  - solid-state battery
  - lithium-ion battery
  - dendrite
  - intercalation
  - lithium metal anode
  - lithium iron phosphate
  key_people: []
key_logic_flow:
- 固态电池是锂离子电池的一种变体，用固体材料替代液体电解质，理论上可减轻重量、提升安全性并提高能量密度。
- 截至2024年，仅中国电池制造商宁德时代就有超过1000人从事固态电池研究，比亚迪、LG、三星等厂商也在开发该技术。
- 截至2025年，美国和欧洲的固态电池创业公司累计融资超过40亿美元，显示资本高度关注这一技术路线。
- 当前锂离子电池依赖大量材料支架来结构化反应，2019年时每克参与反应的锂需要约70克支撑材料，固态电池的核心价值在于大幅削减这部分支架。
- 锂枝晶穿透隔膜会引发热失控并摧毁电池，这是现有锂电池研发的重点难题，理论上固体电解质可阻止枝晶穿透。
- 若枝晶风险被消除，电池可改用纯金属锂负极并摆脱石墨嵌锂结构，同时消除易燃电解质，但宁德时代董事长将技术成熟度评为9级中的4级，商业可行性尚未确立。
object_mentions: []
extract_result: success
---

# Why Is Everyone Trying to Build a Solid-State Battery?

A battery technology that’s getting a lot of attention is solid-state batteries, lithium-ion batteries that replace the liquid electrolyte with a solid material. Chinese battery manufacturer CATL alone had more than 1,000 people devoted to solid-state battery research as of 2024, and battery manufacturers like BYD, LG, and Samsung are also working on the technology. US and European startups making solid-state batteries have collectively raised over $4 billion as of 2025.

Solid-state batteries have several potential advantages over the lithium-ion batteries with liquid electrolyte we use now. For one, replacing the liquid electrolyte with a solid should allow for lighter batteries, requiring less mass per unit of energy delivered. And because the liquid electrolyte currently used in batteries is flammable, replacing it with a solid could make batteries safer and less susceptible to fire.

I wanted to better understand why, exactly, solid-state batteries have these advantages compared to conventional lithium-ion batteries, and how they fit into the broader arc of lithium battery improvements.

#### Battery basics

Batteries supply energy by way of chemical reactions. And chemical reactions, regardless of the chemicals involved, all release or absorb energy using the same mechanism: an electron or electrons move from one potential energy well to another. In a chemical reaction that gives off energy (an exothermic reaction), electrons move from a higher potential well to a lower potential well, giving off energy in the process.

“Potential well” is fairly abstract, so I find it useful to consider an analogy with gravity. Say a ball is in a shallow groove at the top of a tall hill, and there’s another shallow groove at the bottom. The ball is being tugged downward by gravity, which gives it potential energy, a function of how much mass the ball has and how high it is above the bottom of the hill. By itself, the ball at the top of the hill won’t move, but if you give it a little push to nudge it out of its groove, it will roll downhill, releasing its potential energy in the process. This potential energy is converted to kinetic energy (the velocity of the ball), which in turn converts to thermal energy from friction, slowing the ball down until it stops in the lower groove.

Chemical reactions work in a somewhat similar way. But instead of gravity, the potential energy comes from electromagnetism: the positively charged nuclei tugging on the negatively charged electrons. In an exothermic reaction, atoms start in some particular “groove,” their electrons in some particular arrangement. But if you give the atoms a little kick (say, by heating them up so their collisions become more energetic), you can knock them out of their groove, letting them “roll downhill” into a lower-energy configuration, converting their electric potential energy in the process. Some of that potential energy (half, in fact) will go to increasing the electrons’ velocities; the rest will be released as vibration (heat), or as a photon.

So, for instance, say you start with one methane molecule (one carbon and four hydrogens, CH4) and two oxygen molecules (each with two oxygen atoms, O2). These molecules start with their electrons in a particular configuration, the oxygen atoms bonded with each other and the hydrogen atoms bonded with the carbon. At room temperature, O2 and CH4 largely won’t react with each other: each is sitting in its own potential well that takes energy to climb out of. But give them a kick by adding heat, and they can “fall downhill,” going through a series of reactions and ending up in a lower-energy configuration — the hydrogen and carbon atoms each bond with oxygen, forming H2O and CO2. The resulting electron configurations are in lower potential energy wells, with much of the difference being released as heat.

Lithium-ion batteries work by using, unsurprisingly, chemical reactions with lithium. When a lithium-ion battery discharges, lithium ions and their electrons “fall downhill,” moving from one configuration at the anode (inserted between sheets of graphite, known as “intercalation”) into a different, lower-energy configuration at the cathode (intercalated in another material, such as lithium iron phosphate, LiFePO4). The battery is structured to capture energy from this reaction. Lithium ions can pass from the anode into the electrolyte, but electrons can’t: they must go around, through a metallic conductor that connects the anode and the cathode. This flow of electrons is the electrical current that batteries generate. (When a battery is charging, the reverse happens: a voltage placed on the conductor forces electrons back uphill into the anode, with lithium ions flowing back through the electrolyte to keep the charge balanced.)1

Lithium is a favored choice for a battery because an electron leaving lithium has farther to fall than an electron leaving any other metal when coupled with the appropriate reactant. Lithium is also a very light atom (an atomic mass of around 7), which, combined with the large “drop,” means that lithium reactions yield a high amount of energy. Per unit mass, lithium reactions release roughly as much energy as burning gasoline.

But if this is true, why are lithium-ion batteries so much less energy dense than gasoline?

One big reason is the oxidizer. The chemical reactions we rely on for energy typically require some downhill destination for electrons to end up at, which is known as an oxidizer. When burning gasoline, the oxidizer is oxygen in the surrounding air: inside a gasoline engine, fuel and air are mixed together and then ignited, triggering the chemical reaction — an explosion — that powers the engine. Gasoline-powered cars, in other words, don’t need to carry their oxidizer with them, because there’s always one available in the surroundings.

Lithium-ion batteries, on the other hand, aren’t so fortunate. They need to carry their electron destination with them, in the form of the cathode. This adds a lot of extra mass compared to what a gasoline-powered car needs to carry. If a car needed to carry its own oxidizer with it, it would need about 3.5 kilograms of oxygen for every 1 kilogram of gasoline.

More generally, it just requires a lot of material scaffolding to structure the lithium reaction in a way that lets you extract energy from it in the form of electric current. At the anode, each lithium ion requires an additional six atoms of carbon, forming graphite sheets that the lithium ions can nestle into. A similar intercalation structure is required at the cathode. On top of this is the extra mass for the electrolyte, the separator, the current collectors, and so on. As of 2019, every gram of reacting lithium in a battery required about 70 grams of supporting material (though this number has probably fallen somewhat since then).

Without this material scaffolding, the reaction can still take place, but in a non-useful way. If something creates a direct path between the cathode and the anode, the reaction will run nearly instantly, creating a lot of heat and triggering other chemical reactions that will destroy the battery, but no useful electric current. Modern battery design, in fact, takes a lot of effort to prevent these runaway reactions from taking place.

The benefit of all this material scaffolding, of course, is that you can use the same chemicals for the reaction over and over again. The intercalating electrodes on modern lithium-ion batteries in particular are very good at this; because the electrode structure is maintained when the battery charges/discharges, lithium-ion batteries can be used for very large numbers of cycles while maintaining most of their capacity. When you burn gasoline, on the other hand, you’re discharging the products of the reaction continuously (which, of course, is the whole reason we want to switch away from fossil fuels in the first place, to stop the discharged CO2 from building up in the atmosphere). You could, theoretically, dispose of the lithium-ion battery’s scaffolding by having some sort of lithium-based internal combustion engine, but this would work terribly and be outrageously expensive to run (though some people are interested in using oxygen in the air as a battery oxidizer with lithium-air batteries).

#### The promise of solid-state batteries

The major potential benefit of solid-state batteries is a substantial reduction in this material scaffolding.

A pernicious issue with current lithium-ion batteries is dendrites. As we’ve noted, at the anode, lithium ions are nestled between sheets of graphite. But the anode holds the lithium ions very loosely, only slightly better than metallic lithium does. This is useful, because ions can easily migrate into the electrolyte, thus letting the battery work, but it’s a double-edged sword: under the right conditions, the lithium ions that are supposed to enter the anode during charging might instead acquire an electron at the surface of the anode, forming tree-shaped structures of metallic lithium called dendrites, instead of nestling between the sheets of graphite. If a dendrite pierces the separator between the anode and the cathode, it creates a direct path between the two, letting that runaway reaction that batteries are designed to prevent take place. (This doesn’t immediately react all the lithium in the battery — as electric current flows through the dendrite, the dendrite heats up, eventually melting and breaking the path — but the heat from the brief reaction can be enough to trigger other chemical reactions, resulting in thermal runaway and destroying the battery.) A great deal of battery development effort is devoted to preventing these dendrites from forming.

If, however, the liquid electrolyte were replaced with some sort of solid material, these dendrites might stop being a problem.2 With a strong, solid electrolyte, dendrites wouldn’t (in theory) be able to make their way through it, though with current solid electrolytes dendrites still seem to find their way through. And if the risk of dendrites were eliminated, you could switch to a different anode, dispensing with the graphite intercalating structure entirely, using an anode of pure lithium metal.3 And because the solid material would eliminate the flammable electrolyte, the resulting battery might be safer as well.

Solid-state batteries probably aren’t imminent — the chairman of CATL ranks them as 4 out of 9 on the technological readiness scale, and has indicated that commercial viability “has yet to be established.” But the expectation that they could be “[p]otentially safer, more energy dense, and perhaps eventually cheaper than today’s batteries” is pushing manufacturers around the world to try and make them happen.

*Thanks to Austin Vernon for reading a draft of this. All errors are my own.*

The reason that electrons migrate during discharge is somewhat complex. At the anode, lithium ions migrate into the electrolyte, because the electrolyte is a more appealing location with a lower potential energy well. At the cathode, the reverse occurs; lithium ions migrate from the electrolyte into the cathode. At each electrode, this creates a net charge which generates an electric field, which stops further migration. But because you now have a net negative charge at the anode interface (since positively charged lithium ions have left) and a net positive charge at the cathode interface (because positively charged lithium ions have entered), electrons flow between the two electrodes when they’re connected by a conductor to equalize the charges. But because each arriving electron is paired with an arriving lithium ion, the charge differences between the anode and the cathode don’t equalize, letting current flow continuously until there’s no more room for lithium ions in the cathode or no more lithium ions left in the anode (though most batteries have a cutoff that stops current flowing when the voltage drops below some level).

In a crystalline solid electrolyte, lithium ions migrate through it by hopping from one vacancy in a solid crystal lattice to the next. Thanks to their thermal energy, the ions vibrate back and forth trillions of times per second, and occasionally a vibration will have enough energy and be in the correct direction to squeeze past the surrounding atoms into a nearby vacancy.