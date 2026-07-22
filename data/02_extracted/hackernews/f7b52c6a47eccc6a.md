---
title: L'Affaire Siloxane
source: https://mceglowski.substack.com/p/laffaire-siloxane
author:
- '[[idlewords]]'
published: '2026-06-09'
created: '2026-06-11'
description: 'Article URL: https://mceglowski.substack.com/p/laffaire-siloxane Comments
  URL: https://news.ycombinator.com/item?id=48456808 Points: 225 # Comments: 38'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f7b52c6a47eccc6a
source_type: community_discussion
tldr: 国际空间站（ISS）的水回收系统在2010年出现总有机碳超标，经一年多排查发现污染源是防汗剂等个人护理产品挥发的硅氧烷（siloxane）分解产物DMSD。该物质惰性极强，难以过滤，持续消耗空间站的过滤耗材并损坏设备，NASA至今仍未能彻底解决此问题。
objective_summary: 2008年11月，NASA在国际空间站上安装了尿液处理组件（Water Processing Assembly），使水回收率从45%提升至80%。2010年6月起，宇航员饮用水中的总有机碳持续上升，逼近3ppm安全上限。经近一年追溯，化学家最终鉴定污染物为二甲基硅烷二醇（DMSD），其来源是空间站舱内防汗剂、湿巾、护发素等个人护理产品挥发的硅氧烷蒸气，在电离辐射下分解后溶于水。DMSD无法被标准过滤手段有效去除，持续缩短多级过滤床和热交换器的寿命，并摧毁了实验性的Sabatier反应器。NASA于2015年引入活性炭过滤方案，但因霉菌问题退化为混合方案，至今未找到根本解决途径。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - NASA
  - Boeing
  technologies:
  - Water Processing Assembly
  - Urine Processing Assembly
  - DMSD
  - siloxane
  - Sabatier reactor
  - total organic carbon
  - gas chromatograph/mass spectrometer
  - multifiltration beds
  key_people: []
key_logic_flow:
- 2008年11月，国际空间站安装了800公斤的尿液处理组件（Water Processing Assembly），将水回收率从45%提升至80%。
- 2010年6月起，饮用水总有机碳持续上升，至秋季逼近3ppm安全上限，威胁到任务延续。
- 由于空间站不具备分析化学条件，水样本通过返航的Soyuz飞船送回地球，耗时数月才运抵休斯顿实验室。
- 化学家先未能识别污染物，后由Boeing团队借助更新的质谱库鉴定出为二甲基硅烷二醇（DMSD），属于硅氧烷类化合物。
- 污染源是宇航员的防汗剂、湿巾、护发素等个人护理产品挥发的硅氧烷蒸气，在舱内电离辐射下分解为水溶性的DMSD。
- DMSD惰性极强，能通过大多数过滤系统，但会附着并破坏催化剂床和热交换器亲水涂层，导致Sabatier反应器仅运行1800升就报废。
extract_result: success
object_mentions:
- object_type: product
  name: Water Processing Assembly
  canonical_name: ISS Water Processing Assembly
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 2008年11月，Water Processing Assembly抵达国际空间站，帮助空间站将水回收率从45%提升至80%。
  - 2010年6月，在Water Processing Assembly上线13个月后，宇航员饮用水中开始出现总有机碳超标。
  - 该装置包含多级过滤床，DMSD在过滤树脂上弱吸附后被其他物质置换，导致有机碳读数周期性飙升。
  article_id: f7b52c6a47eccc6a
- object_type: product
  name: Urine Processing Assembly
  canonical_name: ISS Urine Processing Assembly
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 2008年11月，800公斤的Urine Processing Assembly抵达国际空间站，用于处理宇航员的尿液。
  - 该装置使空间站首次在轨道栖息地中实现大规模水回收，将回收率提升至80%。
  article_id: f7b52c6a47eccc6a
- object_type: product
  name: Sabatier reactor
  canonical_name: ISS Sabatier Reactor
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - DMSD与宇航员尿液中的二甲基砜共同作用，导致空间站的实验性Sabatier反应器仅运行1800升后即报废。
  - 硅氧烷最终会在催化表面沉积一层玻璃状物质，有效摧毁任何活性表面，Sabatier反应器因此失效。
  article_id: f7b52c6a47eccc6a
---

# L'Affaire Siloxane

### How antiperspirant fumes nearly got NASA to evacuate the space station

In the early years of the International Space Station, water needed to keep the crew alive had to be delivered by Space Shuttle at a cost several times its weight in gold. By 2005, over 9,000 kilograms of the stuff had been flown up from Earth to keep astronauts hydrated, while a further 7,000 kilograms of treated urine were sitting in orbital storage tanks, waiting to be processed.

In November 2008, the Water Processing Assembly arrived on the ISS to realize the great dream of space exploration: boiling astronaut pee. The 800 kilogram Urine Processing Assembly would help take the station from a 45% to 80% water reuse rate. For the first time in the history of space flight, astronauts would be substantially recycling their water in an orbiting habitat.

In June 2010, thirteen months after the Water Processing Assembly went online, excessive levels of total organic carbon began to show up in the astronauts’ drinking water. Total organic carbon is a non-specific measurement that warns the crew about a contaminant being present, but gives them no clue to its identity.

When the space station was being designed, NASA had set the safety limit for total organic carbon at 3 parts per million, based on a worst-case scenario where formaldehyde got into the drinking water. By summer, the weekly trend in organic carbon was rising steadily and on track to exceed this threshold in December. At that point, NASA would either have to send up fresh drinking water or bring the crew back home.

There is no provision, then or now, for doing analytical chemistry on the space station. If you have a mystery substance, you need to put it into a returning Dragon or Soyuz capsule and wait for a lab on Earth to identify it. Astronauts and cosmonauts collect regular environmental samples, but whatever is in those samples only gets analyzed when that archive is brought down to Earth. So it wasn’t until September that a Soyuz capsule finally landed with the summer’s trove of water samples, which were quickly sent to the Food and Water Analysis lab in Houston.

There chemists confirmed the total organic carbon reading, but to everyone’s surprise couldn’t identify a specific contaminant in the samples. Whatever was in the water was not on the watchlist of several hundred chemicals that ISS engineers had anticipated might find their way into the station’s water system. In fact, the mystery substance wasn’t even in the lab’s vast reference library of mass spectra.

It took colleagues at Boeing, working from a newer reference library, to identify the mystery contaminant as dimethylsilanediol, or DMSD.

DMSD belongs to a family of compounds called siloxanes, molecules that contain a silicon-carbon-oxygen bond and occupy a kind of middle ground between organic chemistry and beach sand. Siloxanes (also called silicones) are common ingredients in cosmetics1, contact lenses, fake boobs, caulks, packaging, and all kinds of personal hygiene products, where they’re used to make things feel smooth and slippery. It’s siloxanes that give deodorant and hair conditioner their slick texture, and the same property makes them a popular industrial lubricant.

Manufacturers like siloxanes because they are cheap, stable, nontoxic, and unreactive, at least until they come into contact with something expensive aboard the space station. In ISS life support stories, siloxanes play the role of the meek character in an Agatha Christie novel who has been in the mansion the whole time, but who no one ever suspected had enough moxie to be the murderer. We will meet them again.

In this early brush with siloxanes, NASA greatly underestimated the compounds’ appetite for inflicting havoc. To confirm that DMSD was the culprit in the months-long excursion in organic carbon, chemists in Houston synthesized a pure reference solution of the stuff to calibrate against. They were happy to find that their state-of-the-art gas chromatograph/mass spectrometer was sensitive to DMSD, showing strong and clear peaks in every ISS water sample they looked at.

Unfortunately, the instrument also showed strong and clear DMSD peaks in everything else, including unrelated environmental samples from Earth and blank sample runs of distilled, deionized water. The chemists destroyed three expensive gas chromatographs before realizing that the tubing in their instrument was also made of siloxane. Once injected, the DMSD would happily dissolve into the walls of the chromatography tube and stay there, contaminating every future measurement the instrument made.

After devising an alternate analytical method that didn’t obliterate their lab equipment, the chastened chemists set to work figuring out how much of this DMSD stuff an astronaut could drink in a day without dying. They were still working on an answer when, to everyone’s surprise, total carbon readings on the space station dropped back to normal levels and stayed there, as if nothing had happened.

Since that episode, there have been at least five more spikes in total organic carbon in the station’s drinking water, all traced to DMSD. By NASA logic, this has turned siloxane contamination from a critical anomaly to a familiar behavior that can be modeled and planned against. The agency even boasts about its fight against siloxanes as an achievement of the space station, which is a little like bragging that your clifftop mansion helped further humanity’s understanding of erosion by falling into the sea.

Where do space siloxanes come from? Sleuthing has shown the main sources of siloxane vapor on the space station are antiperspirants, wet wipes, lotion, and leave-in hair conditioner. About a gram and a half of the stuff evaporates every day into the cabin atmosphere. There, helped by ionizing radiation from space, it decomposes to form the diol (DMSD), which is highly soluble in water. This compound collects in the water condenser, passes through the treatment chain mostly intact, and from there enters the clean water supply.

The dramatic spikes in total organic carbon observed aboard the ISS turned out to be a buffering artifact2. A more chemically active substance would bind to the ion-exchange medium in the water filtration beds and stay there. But DMSD binds weakly and can be kicked out by basically anything else. When a filtration bed is first installed, DMSD will begin to accumulate on the fresh resin, with no sign of it in the output water. But after some months, when the filter medium has saturated with DMSD, other substances will start to displace it, creating the signature rapid rise in organic carbon. Once all the DMSD that collected in the filtration bed has eluted out into the water supply organic carbon readings again drop to near zero. If a filtration bed is replaced, the process repeats.

Along the way, DMSD costs the space station a fortune. Each year a set of replacement multifiltration beds (which weigh 50 kilograms and have a three year design life) must be flown up from Earth.

NASA could try just ignoring the stuff. But there’s always a danger that DMSD-induced spikes in total organic carbon could be masking a rise in a different, more serious contaminant. And having this stuff in the output water does cause other problems. Siloxane has graduated to a known nuisance whose main effect is to shorten the life of the multifiltration beds in the water system and require the cabin heat exchanger (a 70 kilogram piece of metal) to be flown down annually to have its hydrophilic coating reapplied.

What makes dealing with siloxanes difficult is that they’re so inert. It’s easy to get reactive contaminants out of the life support loop, but siloxanes pass lightly through most of the various filters and ion exchangers. The only thing they seem to like to react with is catalyst beds and a costly and delicate hydrophilic coating on that heat exchanger. And when they do finally react, they do so by depositing a layer of glass, very effectively killing any reactive surface. It was a combination of DMSD and dimethylsulfone (from astronaut urine) that did in the space station’s experimental Sabatier reactor after only 1,800 liters of throughput.

After a fruitless search for some substance that might be able to sequester DMSD in water, NASA decided to attack the siloxane problem in the air phase, capturing the various siloxane vapors before they could hydrolyze into the diol and enter the water supply. In 2015, they replaced some of the rectangular HEPA air filters in the station with special siloxane-scrubbing filters packed with activated charcoal.

While these new filters reduced the concentration of siloxane vapor in the air, they also led to a mold outbreak. After running the new filter system for two and a half years, NASA has had to retreat to a hybrid solution—the filters are now half charcoal, half HEPA. This keeps mold counts down while capturing at least some atmospheric siloxane. At present the agency is testing a new filtration system to put in front of the heat exchangers, to try to protect them, and continuing to try to cut down on siloxanes at the source level. There are probably people at NASA now whose entire career has been built on siloxane control. But the status quo remains unsatisfying.

#### Siloxanes and Mars: a What-If

It’s interesting to imagine how the siloxane story would have played out if it was first encountered on a mission to Mars.

On the ISS, the initial rise in total organic carbon in 2010 came about 13 months after the station started recycling water. Assuming that every Mars-bound crew would be spending a few months on a shakedown cruise near Earth, that ten month mark would just about coincide with the ship’s arrival at Mars. There, the crew would put their spacecraft in a dormant state and move as a group to the surface habitat, with its own water recycling system, resetting the clock for the siloxane problem. A few months into their 17 month surface stay, organic carbon in the water would start to rise again, as DMSD started to elute from the ion exchange beds. Within half a year, the crew would face the difficult choice of whether to abort to orbit, swap out equipment, or accept the elevated levels of a mystery contaminant in their drinking water.

Regardless of their choice, once they got back to the orbiting spacecraft, they would see the rise in organic total carbon readings there resume, from the initial DMSD spike that was interrupted by their descent to the Martian surface. From the perspective of the crew, the same ominous problem would seem to be following them from orbit to the Martian surface and back.

If the astronauts had analytical equipment on board, like a gas chromatograph/mass spectrometer, the situation might grow even muddier. They would have trouble identifying the siloxane peak in their water samples, since it was not even listed in NASA’s reference database on Earth. And by the end of the hunt, enough DMSD would have dissolved into the tubing of their gas chromatograph to introduce a spurious signal to all future sample runs, causing endless potential confusion about its source.

A common pattern in aviation accidents is that efforts to fix a non-fatal problem rapidly snowball into a life-threatening situation, putting the crew in an unfamiliar part of the flight regime and eroding situational understanding to the point where they start to make serious mistakes. It’s easy to imagine how the siloxane issue, though ultimately harmless, might have prompted some bad choices on such a high-stakes mission with low margins for error.

Obviously any future Mars mission will have learned from the ISS experience with siloxanes. But the first encounter with the siloxane problem on the ISS is a good template for the kinds of problems we can expect to encounter on early forays away from Earth.

#### Actionable Business Insights From the Siloxane Affair

I like the siloxane problem because it such a mundane, annoying, and concrete demonstration of what makes life support hard. In particular, it illustrates how dependent space missions remain on large laboratories on the ground.

But there are broader LinkedIn-style lessons we can learn from siloxane!

**Unknown unknowns are an underrated risk factor.** There’s a phenomenon with Mars missions where the whole endeavor is so complex and difficult that it leaves little room for worrying about the unexpected. And of course it’s already hard to allocate mental space to things that you can’t describe or identify. But unknown problems are the ones with the most potential to seriously derail a space mission, since by definition they can’t be designed around or mitigated in advance.

**Many unknown risks are unglamorous**. The idea of facing the unknown has a nobility that’s hard to reconcile with the reality of deodorant sludge fouling the water supply. Siloxane vapor has been a known constituent of cabin air since at least the Skylab days. But the interaction with the water loop could only be discovered when someone made a serious effort at reprocessing water, and at that point a known bit player in the cabin atmosphere became a major programmatic headache. At no point in this mess were we making foundational discoveries about space travel, but it was a genuinely novel and hard problem.

Another good example of the great unknown being mundane is the discovery of space sickness during the Apollo missions. Today we know that about half of people who launch into space on large spacecraft3 will experience nausea and other symptoms of motion sickness during their first days in space, and that it is notoriously hard to predict who will suffer most. Utah Senator Jake Garn, a seasoned naval aviator with over 10,000 hours of flight time, was so afflicted on his sole Space Shuttle flight that an impressed astronaut corps adopted his name as the unit of spacesickness, reasoning that 1 Garn probably represented the physiological upper limit for human suffering. Today NASA manages spacesickness by giving it an acronym (Space Adaptation Syndrome) and letting astronauts barf it out during the first few days of their mission. But the unexpected incapacitation of veteran astronauts came close to seriously derailing several Apollo flights.

There was nothing particularly space-like to the nausea problem, just like there is nothing cosmic about siloxanes gumming up the water loop. But it took conditions that aren’t easy to replicate on Earth to stumble across the issue.

**It is very hard to limit what gets aboard a large spacecraft.** Once the siloxane problem was identified, an obvious strategy was to make a list of potential sources and exclude as many of them as possible from shipments to the space station. But NASA soon realized that siloxanes are ubiquitous and have so many applications that flagging them all is impractical.

There is a good cautionary tale here from the Space Shuttle era. That vehicle had heat resistant tiles that had to be attached to the aluminum belly of the orbiter. A special cloth had been certified for wiping the aluminum clean before applying the primer that securely bonded the tiles to the metal. After years of uneventful use, tile engineers discovered that new replacement tiles were no longer curing properly.

A careful investigation revealed that the supplier of that special cloth had changed the lubricant used in the machine that sews its hem. Minute amounts of the lubricant were being deposited on the stitching, and enough of that residue was getting on the aluminum skin to prevent the tile adhesive from curing properly.

And that lubricant’s name? Siloxane! I’m telling you this stuff is devious and absolutely hates spaceships.

**Life support problems always find a way to compound**. I’ve griped before that life support defeats engineering strategies for managing complexity by turning everything into a self-interacting tangle. Siloxanes are a nice specific example.

After discovering the siloxane problem, NASA tried hard to find a technique to selectively remove DMSD from cabin water. In the end they decided it was easier to attack the problem at its source, by filtering siloxane vapor from cabin air before it had a chance to decompose into the diol. The space station has large canisters that normally hold HEPA filters, and these could be re-purposed to try to trap siloxane. NASA tested a variety of filter materials to this end. Unfortunately, their top choice was so dense that the required blower fans would have exceeded the ISS limits for cabin noise. (The ISS is a cacaphonous place and those limits are a real health concern.) So the agency settled for a quieter and less effective filter made of activated charcoal.

But even this filter had an unintended impact. Astronauts soon started complaining of respiratory symptoms consistent with a high mold count. Those HEPA filters that had been replaced with siloxane-catching charcoal turned out to be not so replaceable. The ultimate solution was to split the difference and craft a filter cartridge that was half charcoal, half HEPA, which is the solution that the ISS still uses today.

What I want to highlight here is the complex environmental interaction between (1) space radiation, (2) trace contaminants, (3) surface coatings, (4) mold growth, (5) dimensional constraints, and (6) acoustic limits, with no easy place to break the chain. Radiation catalyzes a decomposition reaction in a trace contaminant in cabin air, polluting the water supply and damaging the surface of a heat exchanger. Attempts to filter out the contaminant run into volume constraints in the air system, and the easy solution (swapping out existing filters for ones better targeted at siloxane) turns out to have unacceptable repercussions for health. So the station limps along with a half measure that ameliorates the problem without solving it.

And this kind of thing is just a day in the life of a life support engineer.

**Problems in space are hard to simulate**. If you try to run a closed-loop water experiment on Earth, you will not find the water system getting gunked up with siloxane. Indoor air lacks the OH radicals that catalyze the hydrolysis reaction that turns siloxane vapor into the water-soluble diol. To find those radicals on Earth you need to go outdoors, where water vapor molecules get split by ultraviolet light.

But on the space station, there is enough ionizing radiation zipping around to split appreciable quantities of water vapor and drive the hydrolysis reaction in the absence of UV light. And so you get a problem in space that would never be caught in ground testing.

#### Further Reading

An early paper on the detective work required to figure out the siloxane-induced peak in organic carbon.

*The Story Behind the Numbers: Lessons Learned from the Integration of Monitoring Resources in Addressing an ISS Water Quality Anomaly*(2011) DOI 10.2514/6.2011-5153Part two of the tale:

*2014 ISS Potable Water Characterization and Continuation of the Dimethylsilanediol Chronicle*(2014)A writeup on designing and installing the hybrid HEPA/charcoal filters that attempt to address the siloxane problem in the air:

*Design and Implementation of Combination Charcoal and HEPA Filters for the International Space Station Cabin Air Ventilation System*(2019)

Look for ‘dimethicone’ in the ingredient list of your favorite skin cream and you will find a siloxane.

By ‘large’ here I mean big enough to make unconstrained head movements in. The Mercury and Gemini spacecraft were about as confining as a sports car, and so the problem wasn’t observed until astronauts went up in the relatively roomy Apollo capsule.