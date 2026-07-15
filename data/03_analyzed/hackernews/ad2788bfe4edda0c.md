---
title: Why American ambulance rides are so expensive
source: https://davidoks.blog/p/why-american-ambulance-rides-are
author:
- '[[jyunwai]]'
published: '2026-07-09'
created: '2026-07-10'
description: 'Article URL: https://davidoks.blog/p/why-american-ambulance-rides-are
  Comments URL: https://news.ycombinator.com/item?id=48853091 Points: 205 # Comments:
  273'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ad2788bfe4edda0c
source_type: community_discussion
tldr: 美国救护车费用高昂的根本原因是1965年Medicare按次付费制度未匹配待命成本结构
objective_summary: 2023年旧金山一名叫Jagdish Whitten的25岁男子因车祸被救护车转运6英里，收到12,873美元的账单，其中基础费率就占11,670美元。2024年民调显示23%的美国人因费用问题放弃叫救护车。2020年美国国会禁止全医疗系统的意外账单，但地面救护车是唯一例外。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - American Medical Response
  - San Francisco Fire Department
  - Johns Hopkins
  technologies:
  - CPR
  key_people:
  - Jagdish Whitten
key_logic_flow:
- 美国救护车费用极其昂贵，约一半的私保患者每次紧急叫车都会收到意外账单（surprise bill），2024年民调显示23%的美国人曾因费用问题放弃叫救护车。
- 2020年国会通过《无意外账单法案》禁止全医疗系统的意外账单，但地面救护车是唯一被豁免的领域。
- 1965年Medicare将救护车运输按单次运输收费纳入报销体系，商业保险公司随后效仿，锁定了"按次付费"模式。
- 救护车服务的经济本质是"救援期权"（option on rescue），大部分成本用于全天候待命（站场、车辆、轮班人员），而非单次运输本身，但付费方式从未反映这一成本结构。
- 20世纪初救护车由殡仪馆用灵车兼营，成本极低且作为葬礼业务的引流手段，这使得1960年代的按次付费在当时是合理的。
- 1960年代Johns Hopkins开发CPR技术后急救医学成本急剧上升，但1965年锁定的按次付费制度未能随之调整，造成制度性错配。
extract_result: success
impact_score:
  score: 2.0
  reason: 本文是一篇美国医疗政策与经济学深度分析，与AI行业无直接关联。文章的核心价值在于揭示了'制度锁定效应'——1965年Medicare按次付费制度锁定了救护车服务的支付方式，导致在60年间成本结构发生根本性变化后（从殡仪馆灵车兼职到专业化急救医学），支付模型却从未调整。这种'历史路径依赖→制度错配→消费者受害'的分析范式对AI治理领域有类比参考价值（如AI定价模型、算力基础设施的容量成本分摊），但属于边缘交叉启示，不具备AI行业冲击力。
sentiment: negative
developer_sentiment:
  tone: neutral
  primary_focus: 医疗政策经济学分析，非技术开发者核心关注领域；可作为'制度锁定导致市场失灵'的跨领域案例分析
hype_assessment:
  level: low
  reason: 文章基于具体案例（Jagdish Whitten的$12,873账单分解）、民调数据（23%因费用放弃叫救护车）、制度历史（1965年Medicare立法细节、2020年《无意外账单法案》豁免条款）及经济建模（'救援期权'框架）进行论证，数据来源清晰，逻辑链条完整。没有使用'颠覆式'、'革命性'等PR话术，属于扎实的深度分析长文，不存在炒作成分。
information_entropy: high
domain_disruption:
  technical_innovation: 本文为政策经济学分析，非技术文章。其概念贡献在于将救护车服务建模为'救援期权'（option on rescue），揭示了按次付费与待命成本之间的制度性错配。这一分析框架对AI行业有一定类比价值：AI推理集群也面临类似的成本结构——预留容量（待命GPU集群）成本远高于单次推理的实际算力消耗，若仅按token计费而忽略容量保证成本，可能重蹈救护车定价的覆辙。
  business_model: 揭示了1965年Medicare锁定的按次付费（per-ride fee）模式与当代急救医学成本结构（固定待命成本占主导）之间的根本性错位。商业启示：任何涉及'随时待命'性质的服务——云计算预留实例、AI推理集群、实时监控系统——若支付模型仅按用量计费而忽视容量准备成本，都会面临类似的价格扭曲。这为AI基础设施的定价模型设计提供了反面教材。
engineering_complexity: conceptual
compound_value:
  score: 4.0
  reason: 该文章是一篇制度经济学深度分析，而非技术或产品创新事件。它揭示了美国救护车行业的核心矛盾：1965年Medicare锁定的按次付费模式与救护车'救援期权'（待命成本占绝对大头）的经济本质严重脱节，且2020年《无意外账单法案》将地面救护车单独豁免，进一步固化了这一制度性套利空间。从VC视角看，该分析本身不具备科技投资的典型复利效应——它不描述任何技术突破、产品创新或可投资的商业事件。但其长期认知价值在于：为healthcare-tech领域的投资框架构建提供了底层逻辑支撑，暗示了订阅制急救服务、替代性医疗转运、AI驱动急救调度优化等方向的商业合理性。由于制度惯性极强（60年未变），短期颠覆可能性低，评分中等偏低。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- American Medical Response
- Global Medical Response
competitive_casualty:
- 商业保险公司
- 医疗账单透明化初创公司
- 非营利性社区急救服务
market_opportunities:
- 借鉴救护车'待命期权'成本结构分析，AI基础设施（如GPU算力池）可按此逻辑设计预付费/订阅制的弹性预留服务，而非纯按token用量计费
- 创业者可开发急救医疗账单透明化与意外账单保险科技产品，填补2020年《无意外账单法案》豁免地面救护车后的合规与消费者保护空白
- 基于该案例的'制度性成本错配'逻辑，可衍生出医疗与AI行业支付制度审计咨询服务，帮助企业识别历史锁定(fee schedule lock-in)带来的定价扭曲风险
risk_matrix:
  regulatory: 2020年《无意外账单法案》将地面救护车豁免，意味着监管缺位持续，但未来可能被重新纳入，届时将引发行业收费模式被迫重构的合规风险
  technological: CPR等急救技术革新大幅推高了急救医学成本，但1965年锁定的按次付费制度未能同步调整——这警示AI行业：技术代际跃迁可能使既有的定价/付费制度迅速过时，产生结构性错配
  competitive: 私人股本公司收购救护车运营商后并未带来暴利（行业普遍薄利），说明市场已陷入低价抢单与高额意外账单并存的恶性竞争；类似现象可能出现在AI医疗诊断、远程监护等新兴赛道
  ethical: 23%的美国人因费用放弃叫救护车——当基础服务的定价机制不透明且不可预测时，会直接导致公众规避必要的安全服务，产生严重的社会公平与公共健康伦理问题
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
---

# Why American ambulance rides are so expensive

### The unfortunately botched economics of emergency care

In July 2023, a 25-year-old man named Jagdish Whitten was out for a run in San Francisco. As he crossed a busy street, a car hit him; he did, in his words, “a little flip” over the vehicle, landed in the road, and dragged himself to the curb. Those who had seen the accident called an ambulance for him. But Whitten waved them off and called a friend, who drove him to a nearby hospital instead: “I knew that ambulances were expensive,” he said, “and I didn’t think I was going to die.”

Whitten was right on both counts. At the hospital, doctors found that he had a mild concussion, a broken toe, and a few bruises—nothing too serious. But because he’d suffered a traumatic injury, they were obligated to send him to San Francisco General, the city’s only designated trauma center. This time he didn’t have a choice. He was loaded into an ambulance for a six-mile transfer, evaluated without additional treatment, and sent home the same night.

Over the weeks that followed, Whitten got bills from both hospitals. Everything was roughly what he expected, and all of it would be covered by his insurance plan. But a few months later, Whitten got another bill—this time from American Medical Response, the ambulance provider that had transferred him between hospitals. The ambulance ride, he learned, would cost him $12,873: $737 for the miles traveled, $314 for monitoring his heart on the trip, $151 for infection control, and $11,670 as a “base rate.”

He sent the bill to his insurance provider, which at first denied the claim, saying that AMR was out of network and that the ride hadn’t been pre-authorized. (Whitten, of course, hadn’t chosen the ambulance, or anything else about the trip.) On appeal, his insurance agreed to cover $9,967 of the charge—better than nothing, but it still left him on the hook for about $3,000. After several failed attempts to contest the bill with AMR, and not wanting it sent to collections to hurt his credit score, he paid the remaining $2,900 or so. The brief ambulance ride from one hospital to another had cost him far more than any other part of the experience.

What Whitten had received was a “surprise bill”—a charge that lands on a patient when they’re treated, without knowledge or consent, by a provider outside their insurer’s network. The insurer pays what they consider reasonable; the provider bills the patient for the difference; and the patient, despite having insurance that’s meant to pay for treatment, is left holding the balance. This is a terrible situation to be in.

It’s also the default way that ambulance billing in the United States works. Each year, roughly three million privately insured Americans take an emergency ambulance ride; about half of them get an out-of-network bill for it, a rate unmatched anywhere else in medicine. And the uninsured have it worse still: with no insurer to absorb any of the charge, they face the full, undiscounted bill on their own.

This has proven quite difficult to fix. When Congress banned surprise billing across virtually the entire healthcare system in 2020, ground ambulances were the great exception. If you’re privately insured and need an emergency ambulance, you’re entering a lottery whose ticket price you’ll learn weeks or months later.

And that’s why so many Americans, like Whitten, avoid ambulances whenever they can. One poll from 2024 found that 23 percent of Americans have forgone an ambulance ride because of concerns about cost.

So why are American ambulances so expensive?

The standard answer is greed: rapacious ambulance operators, owned by villainous private equity firms, exploit patients at their most helpless. But I don’t think that’s actually what’s going on. Ambulance providers are chronically unprofitable businesses; margins are thin, crews are underpaid, and operators exit the industry every year. Whatever is being extracted from patients like Whitten, it isn’t padding anyone’s pockets.

The real problem is much more specific and much more interesting. American ambulance bills are enormous and unpredictable because of how American law forces ambulance services to work. In 1965, almost as an afterthought, Medicare decided to pay for ambulances the way it paid for everything else: as a per-ride fee, after the fact, as though a trip to the hospital were just another medical procedure. Commercial insurers, who build their payment systems on top of Medicare’s fee schedules, followed suit.

In the decades since then, the cost structure of ambulance services has changed enormously, and very little of their cost now comes from the ride itself: nearly all of it goes to standing ready—the stations, the vehicles, the crews waiting around the clock for a call that may never come. But the way we pay for ambulance rides has stayed the same. And nearly everything strange and cruel about ambulance billing follows from that disjunction.

To understand what went wrong, we need to learn a little bit about the economic logic of ambulances, and why ambulance services are more like option sellers than taxi companies. It’s more interesting than it sounds.

### Ambulances are option sellers

If you want to think in crude financial terms—not a terrible way to go through life, all things considered—you can think of an ambulance service as *an option on rescue*.

What does that mean? An “option,” in finance, is simply a contract that gives its holder the right, but not the obligation, to make some transaction in the future—to buy a share at a fixed price at some point in the next three months, for example. And when I *write* an option—sell it, in the jargon—I take on the mirror-image obligation: if the holder ever chooses to exercise it, I have to deliver, whether it suits me or not. Options, in this broad sense, are all around us. Insurance, for example, is one type of option: when I buy a fire policy, I pay a small premium every year for the right to a large payout if my house ever burns down, and the insurer takes on the obligation to pay it whether or not the timing suits them. So are fire departments: they keep engines and firefighters ready at all times so that any moment people can call them for help—a readiness that residents pay for with their taxes.

And ambulance services work a lot like option sellers as well.

Let’s say I live in San Francisco. By dint of living there, I hold a perpetual right to summon an ambulance from the San Francisco Fire Department: whenever I call, they’re obligated to come and rescue me. I haven’t entered into an explicit contract with them, but the arrangement functions the same way regardless. The SFFD, in other words, is selling me—and every other resident of San Francisco—an option on being rescued in an emergency. If I ever need an ambulance, I can exercise that option. But even if I never do, simply having it is valuable to me: knowing that help would come if I needed it allows me to take risks I wouldn’t take otherwise. In that sense, I’m consuming the option of rescue every day of my life.

Of course, offering me that option isn’t free for the SFFD. Selling options always imposes costs on the seller: the SFFD has to spend money, around the clock, to ensure that if I ever collapse on the sidewalk and someone calls 911, it’s prepared to arrive rapidly and resuscitate me.

And for the whole system to work, they need to be compensated for that cost. The product is the readiness, not the ride; and the readiness has to be funded whether or not the ride ever happens.

An ambulance service, then, should work the same way. The SFFD should collect a small premium from every household that enjoys the guarantee of rescue, and use the proceeds to pay for everything it needs to be ready to pick people up. And because everyone would pay, no one would pay very much.

But—for strange and particular reasons of American history and law—that’s not how the American ambulance system works.

### The transformation of the American ambulance

As long as there have been hospitals, there’s been an occasional need to get people to them rapidly. For most of history, there was no specialized infrastructure for this. The badly sick and injured might travel by cart or horse to the nearest doctor, and a great many of them simply died on the way; or they might just give up and die in place.

This began to change in the nineteenth century, with innovations in battlefield medicine that eventually migrated into civilian life. And by the early twentieth century, with the arrival of the automobile, the ambulance as we know it today began to take shape: a motor vehicle dedicated to bringing people to the hospital as quickly as possible.

But the ambulance couldn’t just be *any* motor vehicle. Patients generally needed to be transported lying flat, since sitting a badly injured person upright worsens shock and blood loss: so the car needed a long, low, flat cargo bed. The only car that had one, in most places, was the funeral hearse: the car that carried coffins to the cemetery.

And so for most of the twentieth century, ambulance services were provided by funeral homes. They would use their hearses as “combination cars,” able to transport both living patients and dead bodies. They were open at every hour of the day anyway—since people can die at any time—and you could call at any hour of the night and they’d send someone out with the hearse to pick you up. It was common, in fact, for the same car to make both kinds of trip in a single day, perhaps even for the same person.

As you can probably guess, the ambulance services these funeral homes provided weren’t very good. Their equipment was crude—a stretcher, a blanket, perhaps an oxygen bottle—and the attendant sent out on a call was simply whichever employee was free, with no pretense of medical training. Death rates, unsurprisingly, were extremely high.

But death wasn’t a huge problem for the funeral homes, since they provided ambulance runs as a loss leader for the high-margin business of funeral services. The real prize was the relationship: the family that called you for the ride to the hospital was likely to also call you for the funeral. The runs weren’t very expensive to provide, basically amounting to an employee driving the hearse somewhere nearby. So the funeral homes might charge the patient a nominal fee and not try very hard to collect it, or they might not charge anything at all.

In other words: the cost of writing the option was low, because ambulance services were simple and cheap.

And in the 1960s, the logic of that peculiar arrangement was written into federal law. In 1965, the United States government created two massive programs of social insurance: Medicare, which provided public health insurance for Americans over 65, and Medicaid, which did the same for the poor. Both programs worked by enumerating the medical services they would pay for, and reimbursing each per unit of service rendered: a hospital that performed an appendectomy, say, billed the government for one appendectomy. And among those services, added almost as an afterthought, was ambulance transportation. Trips would be covered by both programs, with a fee paid to the operator for each trip, after the fact.

At the time it was a perfectly reasonable choice: it made sense, given how cheap ambulance rides were at the time, to treat them as just another procedure to be billed. But that innocuous classification turned out to warp the entire system of emergency care in the United States.

### How ambulances got expensive

In the 1960s, at the very moment that American law codified how emergency care would be paid for, the nature of emergency care began to change.

The transformation had started around 1960, when CPR—cardiopulmonary resuscitation—was developed at Johns Hopkins: rhythmic compression of the chest, it was found, could keep blood circulating through a stopped heart. In 1965 came the portable defibrillator, which dramatically improved chances of surviving a heart attack outside the hospital; and around the same time came radio telemetry, which let a crew in the field transmit a patient’s vital signs to a physician miles away. With all these innovations, the chance of surviving a cardiac arrest or a bad accident increased dramatically.

Within the space of a few years, then, it became possible to reimagine emergency care. The funeral homes’ combination car simply ferried people to the hospital; but with these new techniques, you could imagine something like real medicine being practiced on the way there.

Against that backdrop, the system of funeral home ambulances began to look badly inadequate. In 1966, the National Academy of Sciences published a report called *Accidental Death and Disability: The Neglected Disease of Modern Society*, which found that American ambulance systems were badly untrained and unequipped for emergency care. A soldier gravely wounded in Vietnam, the report found, had a better chance of survival than a motorist gravely injured on an average city street.

With a surge of public interest and technological possibility, from the mid-1960s onward there was a revolution in American emergency medicine. Soon there was talk of EMS, “emergency medical services,” and of “paramedics,” people who weren’t quite doctors but could nonetheless practice medicine on the way to the hospital. (One important part of this cultural shift was the medical drama *Emergency!*, which ran for six seasons on NBC and proved important in popularizing EMS.) The Emergency Medical Services Systems Act of 1973 financed some three hundred regional EMS systems, with trained paramedics and standards for equipment and dispatch; and countless more EMS systems sprouted up in the years that followed, with or without federal support. In the early 1960s, there had been essentially no certified emergency medical technicians in the United States; by the early 1980s, there were hundreds of thousands.

The result was a transformation of the American emergency care system.

The funeral homes, facing new standards and no way to profit from meeting them, fled the industry; and for a time the gap was filled by volunteer squads, small private operators, and public programs like Seattle’s much-admired Medic One. In the 1980s, fire departments began to enter the business. They had fewer and fewer fires to fight, thanks to better building codes and the diffusion of smoke detectors; and they needed to justify their generous municipal budgets. Soon, many fire departments were EMS agencies in everything but name: by 2020, 64 percent of American fire department runs were EMS-related, and only 4 percent had anything to do with fires.

From the 1960s onward, in short, a professional and capital-intensive infrastructure emerged around emergency care. And as the character of the ambulance industry was transformed, its economics were transformed as well.

In the days of funeral home ambulance services, EMS was a business with low fixed costs: indeed that’s the whole reason why funeral homes were willing to provide it as a loss leader for funerals. The funeral home was already paying for the staff and the hearse; it didn’t cost much to send them out to pick people up and bring them to the hospital.

But now EMS was an industry with high fixed costs. There were trained professionals, who had to be paid; there was an ambulance, filled with expensive equipment; and there was the station. The cost of dispatching an ambulance on a run was trivial. But the cost of keeping that ambulance ready to be dispatched was huge.

And those high fixed costs were made more severe by the nature of the product. In a normal industry with high fixed costs, like an airline or a taxi fleet, you compensate by maximizing utilization: you keep the expensive assets working as many hours as possible, so that the fixed costs are spread over as much revenue as possible. But because ambulance services are selling an option they can never refuse to honor, they’re required to hold idle capacity against their calls. A well-run emergency service will target utilization of about 30 to 50 percent; anything higher risks dropping a call, particularly if there’s a surge in demand.

From 1970 onward, then, the fixed cost of running an ambulance service soared. But the way people paid for ambulances didn’t change at all. Medicare had established the per-ride template in 1965, and commercial insurers universally followed it. This meant that the payment structure and the cost structure were increasingly mismatched: and so ambulance services had to pay for their round-the-clock readiness by billing for individual rides.

From the perspective of ambulance services as option sellers, this makes no sense. It’s as if a fire insurer gave its policies away for free, and then billed the whole cost of the firehouse to whichever unlucky customer’s house happened to burn down. It’s the *exact opposite of how insurance is supposed to work*: but it’s what the payment structure of Medicare made necessary. The entire cost of writing the option had to be recovered from the unlucky minority of people who actually exercised it.

Or, rather, *some* of the people who exercised it: by design, the most frequent users, in fact, were exempt. The heaviest users of ambulances are the elderly, who are covered by Medicare; and since Medicare is the largest purchaser of medical services in the country and is backed by the force and authority of the U.S. government, it enjoys the rare privilege of setting its own prices. And since 2002, Medicare has imposed a national fee schedule on ambulance services—a fixed maximum payment for each category of ride.

And notably, the fees that Medicare sets run *far below cost*. The average ambulance transport costs $2,673 to provide; Medicare pays only about $329 of that. A typical ambulance ride for a Medicare patient, in other words, loses theambulance service thousands of dollars. With Medicaid it’s even worse: state programs typically pay a fraction of what Medicare does, and the services lose even more per ride. Normally, when an insurer pays less than the provider charges, the provider bills the patient for the balance, a practice known as “balance billing”; but with Medicare and Medicaid, balance billing is illegal.

On most of their book, then—rides for Medicare and Medicaid beneficiaries—EMS providers lose money on every run. And that’s before accounting for the fixed costs that make up the large majority of their expenses.

That leaves two groups from whom ambulance services can try to recover the cost of their operations: the uninsured and the privately insured.

Let’s start with the uninsured. On paper, they should be the most lucrative patients an ambulance service could ask for: they receive the full, undiscounted charge, with no insurer to negotiate it down. But uninsured patients are disproportionately unlikely to pay, since they’re disproportionately poor; and EMS providers typically end up selling most of that debt to collections firms for pennies on the dollar. So in practice, the uninsured look less like a profit center and more like the Medicare and Medicaid patients: another class of patients that pays below cost.

And that leaves the one group who actually can be made to pay: the privately insured. All the costs of the EMS system—the fixed costs of round-the-clock readiness, plus the losses on every Medicare, Medicaid, and uninsured ride—must be extracted from them for the service to come close to breaking even.

But here there’s another problem.

In ordinary medical care, when an insurer wants to bring a hospital into its network, it makes a deal: *accept our discounted rates, and we will steer our members to you*. But even though Medicare treats them like one, ambulance rides aren’t like other medical procedures. The insurer doesn’t steer anyone to the ambulance: the ambulance goes wherever the emergency calls come from. So the insurer has nothing to offer the EMS provider: a network contract is simply a pay cut in exchange for nothing. The rational response, then, is simply to decline, and charge insurance companies the full amount. And so the vast majority of ambulances in the U.S. don’t take insurance, and about 80 percent of ground ambulance rides in the U.S. are billed to insurance companies as out-of-network charges.

The result is what you’d expect. Ambulances set their own charges, to defray the full cost of their readiness; insurers pay whatever fraction of them they consider reasonable; and the patient gets a surprise bill for the difference—which is exactly how Jagdish Whitten had to pay $2,900 for a six-mile ambulance ride.

### Someone has to compensate the option sellers

So the American ambulance industry is the victim of a terribly designed payment structure, enshrined by American law. Ideally, it would operate like an insurance company, charging premiums in exchange for service; but instead it’s forced to pay for itself through huge bills to the small minority of people who will pay, either through out-of-network bills to insurance providers or through surprise bills to the patients themselves. And because of this upside-down arrangement, emergency medical services are chronically insolvent. Public services, whether run by fire departments or municipal agencies, don’t come close to covering their costs from billing; and the private industry, though it charges far more, is a perennial money-loser. So many operators exit the industry each year that “ambulance deserts”—areas more than 25 minutes from the nearest ambulance station—have spread across rural America. American ambulance firms have managed the unusual feat of charging extraordinary prices while also going broke.

The classic remedy for a business with high fixed costs and low marginal costs is scale—spreading fixed costs out over more volume. And indeed, high-volume ambulance providers do considerably better than low-volume ones: in a 2012 study, the Government Accountability Office found that costs per transport ranged from $224 at the high-volume end to $2,204 at the low-volume end, a tenfold difference.

But even scale hasn’t been enough to save the industry. AMR, the same company that transferred Jagdish Whitten between hospitals, is the country’s largest private operator of ground ambulances; and despite the enormous scale it has assembled over decades of acquisitions and rollups, it still runs on thin margins and a heavy debt load. Rural/Metro, for a time its largest competitor, filed for bankruptcy in 2013.

The upshot is a system that leaves everyone unhappy. Insurers resent paying charges they never negotiated; the ambulance services themselves, despite charging more than anywhere else on earth, can barely stay solvent; and patients either fear the costs and wave off the ambulance or are left with large surprise bills for services they never requested.

Most of the political attention, of course, has focused on the problem of surprise billing. But no one has attempted to solve the actual underlying problem: attempts to restrict surprise bills have simply led the costs to migrate somewhere else.

In 2015, for example, the state of New York banned surprise ambulance bills by requiring insurers to pay out-of-network providers close to their billed charges—which, since providers set their own charges, meant paying whatever the ambulance providers asked. This was done in the name of “enforcing fairness in healthcare costs.” But it didn’t do much of anything for consumers. Insurers paid what the providers required, and passed the costs along to consumers as higher premiums: ambulance ride prices increased by 13 percent.

Actually capping ambulance charges, meanwhile, would simply kill the ambulance industry entirely. Since charges to the privately insured are the only revenue that covers the fixed cost of readiness, capping them would leave that cost with no payer at all. In 2020, Congress passed the No Surprises Act, which banned surprise balance bills for most parts of emergency care. But by necessity, it exempted ground ambulances from the law: actually restricting the practice would have rendered much of the EMS industry insolvent.

And so thanks to a small drafting decision in 1965—a Medicare provision to reimburse rides like medical procedures—the United States has ended up with an emergency care system that is expensive, insolvent, and distrusted all at once.

The reason for that really isn’t very complicated. Force ambulance services to charge only when a ride occurs, and then force them to provide below-cost rides to the large majority of their patients, and those few patients whom they *can*charge will get charged enormously.

The most efficient way to fund ambulance services would simply be to pay for the option the way that options are normally paid for: with a premium, collected from everyone the service stands ready to rescue. That’s how it’s done in the rest of the rich world. Some places, like the United Kingdom or Japan, simply fund ambulance services directly out of taxes; others, like the Australian state of Victoria, sell memberships in “Ambulance Victoria,” with unlimited exercise at the cost of about $70 a year per family.

There are parts of the U.S. that do this already. Ambulance rides are already subsidized by taxpayers in most places, thanks to public funding for fire departments; and a growing number of places have taken this further. Some rural counties simply fund ambulance services entirely out of property taxes. In Tulsa and Oklahoma City, meanwhile, the government buys staffed unit-hours from an ambulance operator, while households can prepay a few dollars a month on their utility bill and owe nothing if the ambulance ever comes.

Over time, more places will be forced to make similar concessions to reality. The economics of readiness don’t care how the bills are written; someone, in the end, has to pay for the waiting. Until Americans agree to pay for the option, they’ll be forced to pay for the exercise.