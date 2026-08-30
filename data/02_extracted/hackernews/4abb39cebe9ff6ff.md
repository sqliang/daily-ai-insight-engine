---
title: The Life and Death of Direct File [pdf]
source: https://www.ischool.berkeley.edu/sites/default/files/vinton_report_5.pdf
author:
- '[[ronbenton]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4abb39cebe9ff6ff
source_type: community_discussion
tldr: IRS于2024年1月上线Direct File，这是美国历史上首个政府运营的免费在线报税服务。两个报税季内超过40万美国人免费报税，94%用户给予好评，但该服务于2025年被DOGE关闭。
objective_summary: 《通胀削减法案》第10301(1)(B)条责成IRS在2023年5月前向国会提交免费直接报税系统的可行性报告。IRS联合USDS、18F和GSA在报告基础上开发了Direct
  File原型，并于2024年1月正式向纳税人开放。该服务两个报税季内服务超40万用户，获94%好评率和+80的净推荐值。2025年Direct File被DOGE关闭。本文是UC
  Berkeley应用技术政策执行奖学金项目撰写的领导力案例研究。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - IRS
  - U.S. Digital Service (USDS)
  - 18F
  - General Services Administration (GSA)
  - UC Berkeley
  - DOGE
  - U.S. Treasury Department
  - White House
  - MacArthur Foundation
  technologies:
  - IEP
  - e-file
  - Direct File
  key_people:
  - Danny Werfel
  - Bridget Roberts
  - Merici Vinton
  - Chris Given
  - Amy Paris
  - Steve Leibman
key_logic_flow:
- 2021年儿童税收抵免扩大后，政策制定者意识到通过税码发放的安全网项目必须依赖更简单、免费且无中介的报税方式才能触达最脆弱人群。
- 2022年8月16日国会通过《通胀削减法案》，其中第10301(1)(B)条责成IRS成立工作组，在2023年5月前就免费IRS直接报税系统的可行性向国会提交报告。
- IRS在完成法定报告之外还制作了一个原型系统，该原型最终演变为2024年1月向纳税人开放的免费报税服务Direct File。
- 2023年9月21日，工程团队因数周无法在IRS云基础设施IEP上部署产品而判定无法如期上线，白宫、财政部和IRS的联合新闻发布被迫推迟，团队随即进入冲刺模式。
- Direct File上线后获得94%的用户好评率、+80的净推荐值，两个报税季内累计服务超过40万美国人，并提升了用户对政府的信任度。
- 2025年Direct File因与DOGE的优先级相冲突而被关闭，但其开源代码、工作方法及经验教训仍然留存，为未来政府数字服务提供借鉴。
object_mentions:
- object_type: product
  name: Direct File
  canonical_name: IRS Direct File
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Direct File于2024年1月向纳税人开放，是美国历史上首个由IRS运营的免费在线报税服务，两个报税季内有超过40万美国人免费使用。
  - 94%的Direct File用户将体验评为优秀或高于平均水平，其净推荐值达到+80，高于私人报税软件平均的+52。
  - 2025年Direct File被DOGE关闭，但其开源代码、工作方法和经验教训仍然留存，供未来政府领导者借鉴。
  article_id: 4abb39cebe9ff6ff
- object_type: project
  name: IEP
  canonical_name: IEP (IRS Cloud Infrastructure)
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Direct File工程师曾数周无法在IEP（IRS云基础设施）上部署产品，导致2023年9月白宫、财政部和IRS的联合新闻发布被迫推迟。
  - IEP是将Direct File试点纳入IRS云端的关键步骤，团队在无法部署的压力下不得不推迟公开宣布并重新冲刺。
  article_id: 4abb39cebe9ff6ff
extract_result: success
---

The Life and Death of Direct File




                 The Life
                 and Death
                 of Direct File
                 A LEADERSHIP CASE STUDY FOR
                 HIGH STAKES LAUNCHES


                 Merici Vinton
                 Executive Fellow in Applied Technology Policy

                 Melanie Girod, MPP
                 Omar Morales, MPP




UC BERKELEY EXECUTIVE FELLOWSHIP
IN APPLIED TECHNOLOGY POLICY
               UC Berkeley Executive Fellowship in Applied Technology Policy • 1
                The Life and Death of Direct File




 THE EXECUTIVE FELLOWSHIP IN APPLIED TECHNOLOGY POLICY
 is a groundbreaking partnership between UC Berkeley’s
 School of Information and the Goldman School of Public
 Policy. This prestigious eight-month program unites the
 socio-technical expertise of the School of Information
 with the policy acumen of the Goldman School to prepare
 distinguished leaders for the future of technology policy.
 The non-residential fellowship is structured to provide
 a dynamic platform for policy leaders to reflect on their
 experiences, mentor the next generation, and document
 their contributions to digital transformation in government.
 Fellows will participate in research, teaching, and high-
 impact meetings and events.

 The Executive Fellowship in Applied Technology Policy
 is grateful for the support of the John D. and Catherine T.
 MacArthur Foundation, the PIT Infrastructure Fund and
 the Berkeley School of Information Bellwether Strategic
 Priorities Fund.




UC Berkeley Executive Fellowship in Applied Technology Policy • 2
                                                             The Life and Death of Direct File




Contents
Executive Summary |              4
Everything on the line |             5
Background |        6
The Long Road to Direct File |                 9
   April 2021–August 2022: How the Child Tax Credit Paved the Way for Direct File |                   9
   September 2021–August 2022: The Policy Process: Taking an Idea and Turning into a Policy Priority |    9
With the IRA, the IRS Takes Over |                 11
   August 2022–May 2023: Report to Congress and Prototyping |                         11
Countdown to Launch |                13
   May 2023–September 2023: Building a New Service in a Bureaucracy |                            13
      Tax Scope |           13
      State Integration |                13
      Compliance, not Outcomes |                    14
      Creating a Best-in-Class Customer Support Team |                           14
   September 2023: Four Months Until Launch: Breaking the Glass |                          14
   September–October 2023: The Sprint Forward |                        16
      Never Waste a Crisis: Leverage for Opportunity |                      17
   October–December 2023: Getting Ready for Launch |                         18
Direct File Launch |         20
   Starting Small to Get it Right |                20
   The Results: A Trusted, Beloved Pilot |                    22
The 2025 Tax Season |                24
   Direct File is Shuttered |                 25
The Lessons of Direct File |                  26
Conclusion |     30
Appendix: The Direct File Playbook |                    31
About the Authors       | 34
Acknowledgments         |    35




                                     UC Berkeley Executive Fellowship in Applied Technology Policy • 3
                                     The Life and Death of Direct File




Executive Summary
In 2024, the IRS launched Direct File — the first free, government-run online tax filing ser-
vice in U.S. history. In its two filing seasons, more than 400,000 Americans filed their taxes
directly with the IRS at no cost, with 94% rating the experience as excellent or above average.
Then DOGE shut it down.

Direct File’s story is not primarily about tax policy. It is about what happens when deter-
mined leaders decide that government can deliver world-class digital services, and then
actually do it and do it well.

When the Child Tax Credit (CTC) expanded in 2021, it became clear that safety net programs
delivered through the tax code could only reach the most vulnerable if filing itself became
simpler: free, straightforward, and free of intermediaries.

Direct File was not a Presidential campaign promise, nor mandated by Congress; rather, it
was an idea whose time had come and proof that government can deliver excellent digital
services. It also demonstrated that, after several failed government launches, government
was capable of building an in-house team, rewiring the IRS operating model, and having a
successful launch, all within a matter of months.

The Direct File team set its own pace and ways of working, drawing on USDS experience, IRS
tax expertise, and private-sector methods to develop an approach largely unprecedented in
US government service delivery. In doing so, Direct File paved a new way for future govern-
ment leaders to deliver bold, user-centered products.

Direct File succeeded not simply because taxpayers used it and loved it, nor only because
the team that built it set a new standard for government technology. It succeeded because it
helped rebuild something more fundamental: public trust in government’s ability to serve its
citizens.

Though Direct File was shuttered in 2025, its open-source code, its methods, and its lessons
remain. This case study documents the leadership lessons and opportunities for future
leaders.

This case study and accompanying playbook was produced as part of UC Berkeley’s Exec-
utive Fellowship in Applied Technology Policy, between June 2025 and February 2026. It is
authored by Merici Vinton and two research assistants, Melanie Girod and Omar Morales. To
develop the case, they spoke to 15 senior government officials from both the executive and
legislative branch, as well as Direct File teammates.




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 4
                                      The Life and Death of Direct File




Everything on the line
It was September 21, 2023. The Direct File leadership team, including Bridget Roberts, Merici
Vinton, Chris Given, Amy Paris, and Steve Leibman sat down for their weekly meeting with
IRS Commissioner Danny Werfel. Every Thursday for months, they had gathered in his office
to report progress on building Direct File, a new software platform that would allow U.S. tax-
payers to file their tax returns directly to the IRS, at no cost. The team had cultivated a strong
relationship with the Commissioner, who had grown increasingly supportive over time. But
today would test that trust.

The night before, as the Direct File team celebrated the end of their on-site over happy
hour, the Direct File leadership team was somber. Just hours prior, Direct File engineers
had reported that the product was headed for disaster and meeting the January launch date
would be impossible. The leadership team was resolute: “We can’t not launch, too much is at
stake.” However, as they discussed options, the facts were clear: Direct File engineers had
been unable to deploy the product on IEP, the IRS cloud infrastructure, for weeks. They had
worked tirelessly to develop a functioning pilot outside the IRS’s outdated systems, and IEP
was a critical step to bring it within the IRS cloud. Adding to the pressure, the White House,
the Treasury Department, and the IRS were planning a press announcement the following
week, the first public update with details on the IRS’ first-ever online tax filing pilot since it
was announced in May 2023. Now, with little confidence of success, the press announcement
would have to be postponed. The next 12 hours would prove pivotal or Direct File, the IRS,
and the wider civic tech community. Indeed, there was a lot at stake.

As Commissioner Werfel settled into his chair that morning at the IRS headquarters in
Washington, DC, he had no idea this routine meeting would become one of the most con-
sequential moments for the development of the free tax service. The team broke the news,
the press announcement was postponed, and a new race against time began to get Direct
File operational on IRS systems before the start of the 2024 tax season in January. The path
to production that followed set the team on a sprint to get the platform ready for launch and
maintain the trust and support of the decision-makers, from the IRS to the White House, who
had invested years in making Direct File a reality.

Under intense pressure and scrutiny, the team pressed forward. They adapted their
approach, evolved their working methods, and launched into a sprint to make Direct File
ready for American taxpayers. The decisions made that day built a platform that served
American taxpayers for two years - until it ran counter to DOGE’s priorities and was shut
down.




                      UC Berkeley Executive Fellowship in Applied Technology Policy • 5
                                           The Life and Death of Direct File




Background
The Basics of Direct File

Task force to design an IRS-run free ``direct efile’’ tax return system…a report on (I) the cost
(including options for differential coverage based on taxpayer adjusted gross income and return
complexity) of developing and running a free direct efile tax return system, including costs to build
and administer each release, with a focus on multi-lingual and mobile-friendly features and safe-
guards for taxpayer data; (II) taxpayer opinions, expectations, and level of trust, based on surveys,
for such a free direct efile system.

Passage from the Inflation Reduction Act, passed by Congress in August 2022

On August 16, 2022, Congress passed the Inflation Reduction Act (IRA), including an $80 billion
package for the IRS to modernize its processes and get the agency out of its COVID backlog. As
part of this legislation, Section 10301(1)(B) directed the IRS to establish a task force to prepare a
report for Congress by May 2023 about the feasibility of a free, IRS-run direct filing system.

In addition to writing the congressionally mandated report, the IRS produced a prototype.
That prototype is what became the IRS’s new tax filing service, Direct File, which opened to
taxpayers in January 2024. Direct File provided eligible taxpayers with an accurate, secure,
and electronic way to file their taxes directly with the agency, free of charge. The project was
a collaborative effort across the IRS, the U.S. Digital Service (USDS), 18F, the General Services
Administration’s tech and design consultancy, as well as two small business contractors.

When it launched, taxpayers found something rare: a government digital service that they
loved. The project’s strong public support stemmed from its taxpayer-centered design,
which prioritized usability, accessibility, and clarity. This paid off: Direct File successfully
established trust with the public, as evidenced by exceptionally high satisfaction and Net
                         1
Promoter Scores (NPS) : 94% of users rated Direct File as excellent or above average, and it
maintained an NPS of +80, significantly higher than the average NPS of +52 for private tax
                       2
preparation software. It also achieved something few believed could be done: it increased




1 Net Promoter Score is a standard customer service metric. It is a service mark of Bain & Company, Inc., NICE Systems,
Inc., and Fred Reichheld.
2 IRS Direct File - Filing Season 2025 Report, May 13, 2025, https://taxpayer-rights.org/wp-content/
uploads/2025/06/2025-14762.pdf




                          UC Berkeley Executive Fellowship in Applied Technology Policy • 6
                                               The Life and Death of Direct File




taxpayers’ trust in government. Not only were users satisfied, but 86% of them said that using
                                             3
Direct File increased their trust in the IRS.

Direct File served taxpayers for two filing seasons, before being shut down by the Trump
administration and the Department of Government Efficiency (DOGE) in November 2025.

Direct File was an idea whose time had come. Then-President Biden didn’t campaign on free
tax filing, nor did Congress mandate its launch. But it was a service that people wanted and
expected from their government, and the IRS delivered. Direct File showed taxpayers that
the government can meet their needs, and showed the government itself that it was capable
of delivering complex software.

Industry Resistance to Direct File

The path to Direct File was shaped by decades of resistance from the private sector. Compa-
nies like Intuit and H&R Block spent millions annually on federal lobbying to block free pub-
lic filing tools, even though the U.S. tax system is considered one of the most complex and
burdensome in the world. In 2002, the private sector secured the Free File program (FFP),
a partnership through which tax software platforms promised free services for low-income
taxpayers in exchange for the IRS agreeing to stay out of the tax software market.

The clause was removed when ProPublica revealed in 2019 that FFP members had been
deliberately hiding free services and upselling users, resulting in less than 2% of eligible tax-
                            4,5
payers actually benefiting. Under mounting scrutiny and public pressure, H&R Block and
Intuit exited the FFP in 2020 and 2022, effectively rendering the partnership obsolete.

Today, the FFP is widely viewed as the industry’s attempt to strategically delay and prevent Direct
File. The private sector’s failure to deliver on its promises revived the case for a public alter-
native. However, political reluctance to openly support Direct File prolonged the status quo.

Benefits and Administrative Burden

Despite industry lobbying, free, government-provided tax filing had its cheerleaders. The
U.S. tax system is considered to be one of the most complex and burdensome in the world:
                                                                                     6
average individual taxpayers spent nine hours and $150 to file their 2023 tax return, while


3 IRS Direct File Pilot Program - Filing Season 2024 After Action Report, May 3, 2024, https://www.irs.gov/pub/irs-pdf/p5969.pdf
4 IRS - Addendum to the Eighth MOU on Service Standards and Disputes [...] between the IRS and Free File, Inc., Decem-
ber 2019, https://www.irs.gov/pub/irs-wi/FFI%20Signed%20MOU%20Addendum%2012-26-19.pdf
5 ProPublica - Inside TurboTax’s 20-Year Fight to Stop Americans From Filing Their Taxes for Free, October 17, 2019,
https://www.propublica.org/article/inside-turbotax-20-year-fight-to-stop-americans-from-filing-their-taxes-for-free
6 Internal Revenue Service - The IRS Research Bulletin, June 14, 2024, https://www.irs.gov/pub/irs-access/p1500_acces-
sible.pdf




                            UC Berkeley Executive Fellowship in Applied Technology Policy • 7
                                           The Life and Death of Direct File




many Direct File users completed the process in under 30 minutes for no cost. Advocates of
Direct File were driven by a simple idea: as Direct File Product Owner Chris Given explained,
“Taxes are hard, they should be easier. How can we make it less burdensome and increase trust?”.

For many, Direct File addressed the longstanding lack of a free public filing option in the
United States — a service that was already a standard in most of the world. Indeed, most
developed nations, from Australia to Sweden, have such an option for taxpayers, and most of
them offer pre-filled returns, requiring no action on behalf of taxpayers to fulfill their obli-
gation. Direct File also addresses equity: because much of the U.S. safety net runs through
refundable tax credits like the Earned Income Tax Credit (EITC) and Child Tax Credit,
ensuring low-income taxpayers can file for free is essential. Finally, providing a free, public
filing option also aligns with the IRS’s mission to expand access alongside programs like the
                                               7
IRS’ Volunteer Income Tax Assistance (VITA) initiative for low-income taxfilers, as well as
enabling taxpayers to file on paper forms.

Avoiding another healthcare.gov

The lack of political will stemmed in part from one of the central arguments against Direct
File: that the government was not in the business of building products, and it was typically
bad at it anyway. The team had to repeatedly persuade Biden-appointed political leadership
of the value that the tool could deliver and convince them that building in-house capacity
would lead to a product that users would love.

The shadow of Healthcare.gov amplified the skepticism. The platform’s 2013 launch was a
spectacular failure: plagued by bugs, only six people signed up on the first day. Costs bal-
looned to $2.1 billion, as the Obama Administration had to bring in a crisis team of experts to
                    8
salvage the rollout. Healthcare.gov became a cautionary tale proving that high-scale, high-
stakes government digital projects are simply too risky to attempt.

The scars ran deep. Politicians and appointees were reluctant to put their reputation at risk
by endorsing government-led digital initiatives. Inside agencies, Healthcare.gov slowed mod-
ernization efforts due to fear of another failure, further eroding public trust. Ironically, since
Healthcare.gov’s failure was largely due to over-reliance on external contractors and rigid
government procurement processes, no significant changes have been put in place in the
ensuing years, and federal agencies still largely outsource the majority of their IT workforce
and products.



7 VITA is the IRS’s volunteer run, free tax return program: https://www.irs.gov/individuals/
free-tax-return-preparation-for-qualifying-taxpayers
8 IBM Center for The Business of Government - Managing Mission-Critical Government Software Projects: Lessons
Learned from the HealthCare.gov Project, Fall 2017, https://www.businessofgovernment.org/sites/default/files/View-
points%20Dr%20Gwanhoo%20Lee.pdf




                          UC Berkeley Executive Fellowship in Applied Technology Policy • 8
                                     The Life and Death of Direct File




The Long Road to Direct File
April 2021–August 2022: How the Child Tax Credit Paved the Way for Direct File

A free, government-run tax filing service remained elusive until 2021, when the American
Rescue Plan Act expanded the Child Tax Credit (CTC), making the tax credit fully refundable
for the first time. This created a policy challenge: low-income families who needed the credit
most typically had no filing obligation, meaning they would not file returns. The complex
and expensive filing process put the benefit at risk of never reaching them.

Senior Biden officials recognized the need for a simplified filing tool, but political concerns
about Healthcare.gov and industry lobbying made them reluctant to build one themselves.
Instead, their implementation efforts were buttressed by a USDS team, led by Merici Vinton,
who supported with outreach, as well as a non-profit partner, Code for America, which
created GetCTC.org, a free, mobile-friendly platform available in English and Spanish that
allowed non-filers to claim their CTC without filing a full return.

GetCTC.org demonstrated to White House officials that taxpayers were willing to use free,
simple, easy-to-navigate tax filing services, which helped to set the stage for Direct File.

September 2021–August 2022: The Policy Process: Taking an Idea and Turning into a
Policy Priority

Even after the success of GetCTC.org, Direct File implementation was delayed due to hesitant
leadership and lack of clear, decisive decision-making. As Jason Miller, then-Deputy Director
at the OMB, said, “We took 18 months to examine the problem. We should have started a year
earlier”.

During that time, stakeholders across different agencies were meeting and discussing Direct
File. The outcome: many memos, from the National Economic Council (NEC) at the White
House, to OMB and Treasury, but no decision in sight. These agencies, under the auspices
of the Interagency Policy Committee (IPC), set out to identify relevant policy considerations
and explore paths to executing a free tax filing service. But the talks could not overcome the
slow-moving process and the absence of political commitment to build Direct File.

Moreover, external events came to disturb and further delay this already slow process. The
White House was consumed with President Biden’s Build Back Better agenda, which included
$80 billion in IRS funding. When the Build Back Better bill collapsed in December 2021,
Direct File’s future became even more uncertain. To add to the inertia, the Russian invasion
of Ukraine at the end of February forced the Department of Treasury to redirect its attention




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 9
                                      The Life and Death of Direct File




to the implementation of sanctions against Russia, giving reluctant stakeholders cover to
sideline Direct File discussions.

Despite a lack of forward political momentum, the U.S. Digital Service (USDS) team carried
out foundational work during this period that moved both stakeholders and the product con-
cept itself forward. USDS was a team of technologists in the White House that were deployed
to key initiatives across the government. In many policy situations, it is standard for govern-
ment policy leaders to make a decision without heavy consultation of technologists or user
experience professionals. But the USDS team knew that approach would lead to potential
disaster: when it came to a potential new tax product, experience was just as important as
policy and, in fact, the policy would fail if it had a poor user experience. They produced the
first demo and user journey, which brought the product to life for key stakeholders. Many
were expecting a minimally designed experience or, as one stakeholder said, “I would be fine
with an online PDF of the 1040.” Instead, the early question-based flow, which was very sim-
ilar to the final product, was produced to demonstrate that taxpayer experience was integral
to the execution of the product itself. The team wanted to show an experience so excellent
that it would be difficult for stakeholders to say no.

At the end of May, White House leadership declared Direct File a priority, but without IRS
buy-in, progress ground to a halt. In July 2022, the entire USDS team was dismantled. The
absence of clarity made the work highly unstable for the Direct File team. For a while, as
Direct File Deputy Merici Vinton described, the team’s motto was a reference to the film
“The Princess Bride”: “Good night, good work, I’ll most likely kill you in the morning” due to
uncertainty around the project.

Just when the team thought it was over, things dramatically changed and, once again, Direct
File had a chance.




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 10
                                             The Life and Death of Direct File




With the IRA, the IRS Takes Over
August 2022–May 2023: Report to Congress and Prototyping

With the passage of the Inflation Reduction Act (IRA), the IRS was finally given congressional
mandate to explore development of Direct File. Additionally, the Treasury Department
became actively engaged in the process: the IRS received $80 billion through the IRA, raising
expectations for meaningful results. The IRS developed a strategic operating plan (SOP)
to guide the new funding and strategic direction, and asked the USDS to provide technical
expertise and guidance on the taxpayer experience throughout the strategic planning
process. IRS executives oversaw various SOP workstreams, including the Deputy National
Taxpayer Advocate, Bridget Roberts, who was tasked with reimagining taxpayer services.

Initially, the planning assumption was that the IRS would spend the $15 million to procure
a vendor to write the congressionally mandated report and perform a quantitative survey to
assess taxpayer opinion. But Roberts and the USDS team had a different proposal: instead of
understanding taxpayer opinion in abstract, the IRS should use the $15 million to build a pro-
totype to put in front of users to tangibly and qualitatively gauge taxpayer opinion, adjacent
to a traditional survey. IRS and Treasury agreed, and eventually appointed Roberts as the
                            9
Direct File Service Owner.



      Game-changing decision: The decision to use the $15m from Congress to build a prototype, as well as deliver
      a report, meant the team could start getting feedback from users as early as possible to understand “taxpayer
      interest,” as well as use this time to explore different product and engineering concepts. This early prototype
      became the foundation of what would become the product on launch day.



This was a critical decision point for the product. With the proposal approved, between
August 2022 and May 2023, a small team at the IRS started working on the prototype and
drafting the report to Congress. User research was conducted thanks to four sources of
information. First, the IRS leveraged its annual Taxpayer Experience Survey (TES) to inquire
about a potential free e-filing program. Second, the team incorporated a MITRE survey about
taxpayer opinion on tax software. Third, an independent analysis was carried out to under-




9 The title Service Owner is borrowed from the UK’s Government Digital Service’s Service Manual: https://ddat
-capability-framework.service.gov.uk/role/service-owner




                           UC Berkeley Executive Fellowship in Applied Technology Policy • 11
                                            The Life and Death of Direct File




stand the overall feasibility of the project. Finally, significant formative user research and
usability testing was conducted during the development of the internal prototype.

All insights collected during this period led to the same conclusion, as highlighted in
the report delivered to Congress in May 2023: there was clear public interest in a govern-
ment-run e-file system. Indeed, 45% of taxpayers said they were “somewhat interested” in
using Direct File, and 28% said they were “very interested.” The ability to file for free while
bypassing third parties was important to many users. The report also highlighted some of
the challenges to bringing Direct File to life. The IRS needed ongoing appropriate funding
to develop in-house technical expertise and expand its customer service capabilities. Some
operational hurdles would also need to be cleared, such as coordination with state tax
          10
agencies.

Despite the challenges, support for Direct File was growing within the Treasury Department.
Danny Werfel, who was appointed Commissioner of the IRS in March 2023, and Janet Yellen,
the Secretary of the Treasury, were among the supporters. Following the release of the
feasibility report in May 2023, Secretary Yellen directed the IRS to launch a Direct File pilot
during the 2024 tax filing season. The Direct File team was finally receiving the leadership
                                                              11
buy-in it needed to move from research to implementation. It was May 16th, 2023, and tax
filing season would begin in January 2024. It was a race against the clock to launch the pilot
                                      12
on time for the following tax season.




10 IRS Report to Congress - Inflation Reduction Act §10301(1)(B), IRS-run Direct e-File Tax Return System, May 16, 2023,
https://www.irs.gov/pub/irs-pdf/p5788.pdf
11 Department of the Treasury - Letter from Commissioner Werfel to Secretary Yellen, May 16, 2023, https://www.irs.
gov/pub/newsroom/letter-to-secretary-yellen-direct-file.pdf
12 Reuters - US IRS to launch free tax e-file pilot program in 2024, May 16, 2023, https://www.reuters.com/world/us/
irs-launch-free-us-direct-tax-filing-pilot-program-2024-2023-05-16/




                          UC Berkeley Executive Fellowship in Applied Technology Policy • 12
                                      The Life and Death of Direct File




Countdown to Launch

May 2023-September 2023: Building a New Service in a Bureaucracy

In May 2023, the Direct File team faced an uphill climb. They had leadership support — some
leaders later admitted they wished they had given their support sooner — but no time to
waste. The stakes could not have been higher, yet they had to build in a complex environ-
ment where key policy decisions required negotiation across the IRS, Department of Trea-
sury, and OMB.

Tax Scope

The first question was “tax scope”: which returns could Direct File support? From the White
House down to the Direct File team, there was a strong conviction that the platform should
be available to everyone, with no income cap. But some financial situations are more com-
plex than others, and the team had to find a realistic scope that still covered as many Amer-
icans as possible. They landed on an ambitious scope: the software would be usable by U.S.
residents with any filing status, using the standard deduction, with potential dependents,
reporting wages, interest of $1,500 or less, unemployment compensation, and Social Security
benefits. Eligible users could also claim the Child Tax Credit (CTC), the Earned Income Tax
Credit (EITC), Credit for Other Dependents, the student loan interest deduction, and the edu-
cator expenses deduction. With this scope, the estimated eligible population across 12 pilot
states was about 15.4 million — more than 10% of U.S. taxpayers.

State Integration

State integration was the next challenge looming over the pilot. A federal-only system would
be inefficient and unattractive for taxpayers, forcing them to effectively enter the same
information twice. The team found a path that would import, with the taxpayers’ consent,
information submitted to Direct File directly into a state tool. Despite the strategic impor-
tance and high risk of failure, the IRS had established no similar prexisiting partnerships
with states, nor could it rely on any previous work to get this done.

Working first with states that had no state income tax — Florida, Nevada, New Hampshire,
South Dakota, Tennessee, Texas, Washington, and Wyoming — was low-hanging fruit, as no
technical integration was required. For states with income tax, it was essential for the pilot
to integrate with at least one state to demonstrate the overall viability of Direct File. The IRS
invited all states to participate, and four states with state income tax had the capacity to join:




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 13
                                            The Life and Death of Direct File




Arizona, California, Massachusetts, and New York. Arizona, New York, and Massachusetts
                                                                                   13
connected via a new Direct File state API, and California used a PDF import method.

Compliance, not Outcomes

Facing skepticism inside the IRS, the team was forced to lean into risk management, some-
times to a fault. The tension between those ready to embrace risk and those determined
to minimize it was constant. Engineers spent significant time on compliance paperwork, a
reflection of the slow-moving realities of institutions, even as the clock kept ticking.

Often, the team’s greatest challenge was not technical, but bureaucratic. Suzanne Chapman,
who became the IRS’s Director of User Experience, knew that the project’s success depended
on getting the work-in-progress product into users’ hands as often as possible to create short
feedback loops, and pivot strategy where necessary. But the IRS research approval process took
up to six weeks per study, a pace incompatible with the team’s rapid, iterative methods. As Ser-
vice Owner, Bridget Roberts escalated the team’s concerns to Commissioner Werfel, and a new
path forward was found that would allow the team to operate on its rapid schedule, shortening
the timeline to 10 days. As a result, the team engaged with 195 taxpayers in interviews and
usability testing. The direct line to users became a cornerstone of Direct File’s success.

Creating a Best-in-Class Customer Support Team

The Direct File team knew they needed to have not just an excellent product, but also an
excellent customer support experience, with trained agents that could answer user questions
in the same tone that felt similar to using the Direct File product itself. The team set up a
unique operating model: they brought the customer support representatives (CSRs) onto
the Direct File team, reporting to Bridget Roberts. This model not only benefited users, but
also the product itself: by sitting alongside the product team, the customer support agents
created a seamless feedback loop, flagging questions or issues that users had in real time
directly to teammates who could fix those issues.

The IRS also decided to pilot Live Chat for all Direct File inquiries; it was the first time that
the IRS used this channel at this scale. They brought on nearly 400 IRS customer support
agents to support the product during filing season.

September 2023: Four Months Until Launch: Breaking the Glass

The team was making fast, meaningful progress. Leadership was all-in, a talented group had
been assembled, the scope had been defined, user research was under way, and a functional,

13 IRS Direct File Pilot Program - Filing Season 2024 After Action Report, May 3, 2024, https://www.irs.gov/pub/irs-pdf/
p5969.pdf




                           UC Berkeley Executive Fellowship in Applied Technology Policy • 14
                                      The Life and Death of Direct File




high-quality pilot was taking shape. Momentum was so strong that Treasury and IRS were
going to announce exciting details about the pilot, including eligibility. But in September
2023, technical realities were about to catch up.

In mid-September, the entire Direct File team gathered for an on-site meeting at the IRS
office, flying in staff from across the country. They had managed to create a working proto-
type that impressed everyone who saw it. The platform had a clean design, clear content,
and worked flawlessly —on the team’s own cloud infrastructure. It would now have to be
deployed on the IRS’s infrastructure. It was a critical, make-or-break milestone.

However, the engineering team, led by Steve Leibman, were not confident that they could
deploy the software on the IRS systems as needed. The IRS’s Integrated Enterprise Portal
(IEP), nor the policies that surrounded it that governed its use, was not built for products
like Direct File. IEP was Accenture’s vendor-run cloud environment, and the Direct File team
had been working for weeks, unsuccessfully, to gain access to be able to deploy to the IRS
environment.

There was also a cultural divide. The Direct File team, heavily influenced by standard soft-
ware development and agile practices, ran into the IRS IT team’s rigid timelines and sequen-
tial processes, meaning that the deployment was not possible to complete in less than a
couple years. At the IRS, deployment meant navigating never-ending compliance documents,
security assessments, and risk-management frameworks. Coordination with the external
contractors who operated parts of IEP was slow and inefficient. Paperwork was stacking up,
consuming more and more of Ryan Ahearn’s time, leaving little room for the engineering
work he had been hired to do.

At the end of the offsite, Ahearn and a small group gathered in the Secretary of War Suite at
the Eisenhower Executive Office Building. Ahearn and the engineers exposed the team to the
roadblocks they were facing: deploying on IEP, a vital prerequisite to getting the Authority to
Operate (ATO), felt increasingly out of reach. Alternatives were brainstormed, like deploying
on Cloud.gov instead. But for technical and political reasons, there was only one path for-
ward, and the path would be bumpy, if not totally blocked: they had to deploy on IEP.

That night, as the team relaxed over a happy hour, Chris Given delivered the news to Bridget
Roberts: on the current path, there was no way Direct File could launch in January 2024. The
tension was high. For months, Vinton, Given, and Roberts had reassured Commissioner Wer-
fel that the pilot was on track. They were about to blindside the Commissioner and challenge
the trust that had been built over time.




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 15
                                           The Life and Death of Direct File




                                                                           The following morning, on
     Leadership in action: Jason Miller immediately understood the         September 21, 2023, they
     severity of the situation and cleared his calendar to discuss         sat down with the Com-
     options and next steps with Merici Vinton. This was a key moment,     missioner, uneasy. Roberts
     as it established both accountability for delivery and trust and      recommended delaying
     transparency between the project and one of its key stakeholders.
                                                                           the press announcement,
     Miller then went on to explain the situation to other White House
                                                                           as the team no longer had
     stakeholders to ensure that the team would be given the top cover,
                                                                           confidence in a filing sea-
     space, and time they needed to address the issue.
                                                                           son launch. It was a blow
     Vinton and Miller had begun their collaboration a few months prior    not only for the team but
     when they established a 15 minute, bi-weekly check in; Vinton         also for the Commissioner,
     asked Miller if “it would be good to establish a working relationship Treasury, and the Biden
     and learn how to communicate while things are good, just in case      Administration. Vinton
     they go bad and we need to work together.”                            called Jason Miller at OMB
                                                                           to discuss the situation, as
     As it turned out, that was a good idea.                               well as Bharat Ramamurti
                                                                           at the NEC. With the IRA’s
                                                                           $80-billion investment,
they needed tangible results to show the public. Direct File was the result they needed and
hoped for. The press announcement had to be postponed.

Despite the setback, the team rallied and embarked on a sprint to keep Direct File alive.

September–October 2023: The Sprint Forward

Knowing this was a situation that needed a solution, and fast, Ahearn and team proposed a
short sprint to assess feasibility and paths forward: each day, the team would set out a new
goal to achieve, with update meetings with Commissioner Werfel and the CIO mid-day daily,
as well as evening emails providing a progress update. Ahearn was the right person to lead
the sprint: after months of drafting extensive documentation, he knew better than anyone
the burdensome processes impeding deployment, as well as Accenture, the vendor that ran
the fully outsourced IEP cloud environment. The two-week goal was to finally deploy on IEP,
an objective that had been unattainable previously. Ahearn led a team of engineers through
an intense, two-week sprint to work with vendor partners, holding daily updates and multi-
ple 12-hour team calls to clear roadblocks in real time. Even the IEP contractors were pulled




                         UC Berkeley Executive Fellowship in Applied Technology Policy • 16
                                      The Life and Death of Direct File




in, forcing the Direct File team to deal with realities of government contracting that they had
long tried to avoid.

The sprint achieved its objectives: by the end, the team was able to deploy and put Direct File
back on track to deliver the pilot in time for the upcoming filing season.

Never Waste a Crisis: Leverage for Opportunity

The crisis gave the team permission to raise and solve issues that previously had been
unsolvable. Daily meetings with the Commissioner, direct access to contractors, real-
time decision-making — none of this would have been possible without the urgency of
near-failure.

These two weeks had a lasting impact on the team’s ways of working. Not only did they save
Direct File by achieving the deployment on IEP, but they also gained a renewed conviction
that, from now on, the team could not wait for bottlenecks to appear: they had to be more
proactive. Continued development of the platform, with frequent and quick deployment,
would be used to surface any issues and avoid another make-or-break situation. Moving
forward, the IRS saw the value of having additional in-house talent to manage vendor-driven
products like IEP.

The deployment crisis also exposed how some aspects of change management inside the
agency had been overlooked, and the sprint gave a chance for the agency to reset its relation-
ship with the Direct File team. Chris Given and the IRS Chief Information Officer (CIO) began
meeting more regularly, smoothing tensions and accelerating turnaround for deployment
approvals, an essential step for the quick feature-shipping strategy of the Direct File engi-
neering team.

On the leadership side, trust with Commissioner Werfel had to be strengthened and main-
tained, but it was understandably rocky going. Even though the Commissioner still sup-
ported the project and team, the uneasy feeling lingered, and Commissioner Werfel recalled
his shock and frustration about the sudden urgency. Why had the team not told him about
the issues sooner? While the engineers worked to troubleshoot the technical issues, the team
focused on repairing the relationship. They created a “no-surprises” tracker, shared weekly
with Commissioner Werfel, and worked together to identify all potential surprises. Transpar-
ent and regular communication would lay the foundation for a stronger future relationship.

Closing on the two-week sprint, the team celebrated: Direct File was now live on IEP. They
had not wasted the crisis: they started on a new foundation, incorporating the learnings




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 17
                                              The Life and Death of Direct File




gained, and stayed on track for launch by the opening of the tax season. After the delay, the
                                                                14
pilot was officially announced to the press on October 17, 2023.

October -December 2023: Getting Ready for Launch

While one roadblock had been cleared, many others remained. State tax integration was
next. Of the states joining the pilot, three would be integrated via API: Arizona, New York,
and Massachusetts. By late October, the engineering team started testing the APIs with the
state tax agencies.

The team was pushing on multiple fronts. Engineers built out the many features they wanted
taxpayers to have, while also building relationships with state tax agencies to secure state
filing through Direct File. Meanwhile, designers continuously tested new releases with users
to get quick and timely feedback. They worked to make sure that Direct File used plain
language, which would build user confidence on the platform, but also, indirectly, trust in
the IRS. To do so, they worked closely with the IRS’s Office of Chief Counsel for language
accuracy, as well as other users and taxpayers, to avoid tax lingo and reduce confusion. In
parallel, the Spanish version of Direct File was being developed to ensure millions of Amer-
icans could file in their preferred language. Taxpayers using assistive technology were also
involved to uphold the principles of accessible product design. Given the complexity of the
tax code and the need for an accessible and easy-to-use product, the challenge of using plain
language in both English and Spanish was a priority for the design team.

Despite the pace, there were many moving parts. By the end of November, the team realized
that launching to all taxpayers on the opening of the filing season in January 2024 was not
realistic. Direct File teammate, Amy Paris, devised a launch plan in phases that would main-
tain their iterative approach. Indeed, rather than launching widely and opening the platform
to the 15.4 million eligible taxpayers at once, they would roll it out in waves. This strategy
would minimize risks, avoid a healthcare.gov-style disaster, and give them the opportunity to
fix bugs before they affected hundreds or thousands of taxpayers.

At the end of December 2023, with a phased launch decoupled from the opening of filing
season, the Direct File team was ready to start training agency employees more widely and
demo the product to agency leadership. Training for customer support representatives
(CSR) began in early January 2024, preparing the IRS frontline for the expected surge in user
inquiries, whether on the phone and through chat. A total of 400 IRS employees were trained




14 IRS - IRS Direct File Update: Free, secure, IRS-run, electronic filing option on track
to be available in 2024 as a limited pilot, October 2023, https://www.irs.gov/newsroom/
irs-direct-file-update-free-secure-irs-run-electronic-filing-option-on-track-to-be-available-in-2024-as-a-limited-pilot




                            UC Berkeley Executive Fellowship in Applied Technology Policy • 18
                                           The Life and Death of Direct File




                                                                                       to answer questions
     The Direct File project followed an unorthodox path for high-stakes               about Direct File. Some
     launches: starting slow and gradually increasing the number of users. In          CSRs had collaborated
     government, most launch deadlines are included in legislation. The Direct         with the designers
     File team had what should be the standard for the government: the ability         for months to resolve
     to set their own launch date, based on when the platform was ready.               any issues ahead of an
                                                                                       agency-wide training.
     If you were Commissioner Werfel and had a congressionally mandated
     launch date, how would you ensure that your team and launch were set up
                                                                      On January 18, 2024,
     for success?
                                                                      Commissioner Werfel
                                                                      and several Direct FIle
team members gathered at Treasury headquarters to demo Direct File for Secretary Janet
Yellen. The presentation was a success. Even though Direct File would not be available for
most taxpayers for at least another month, Treasury leadership left convinced and excited.

After additional testing, Direct File was ready for prime time.




                         UC Berkeley Executive Fellowship in Applied Technology Policy • 19
                                             The Life and Death of Direct File




Direct File Launch
Starting Small to Get it Right

Paris’ plan set out an iterative launch process with gradual growth of the user base as mile-
stones were reached. The pilot would validate core functionalities, then scale gradually to
test system limits.

PHASE A: JANUARY 22, 2024: All IRS employees were invited to use Direct File once the platform
opened for them, at the launch of tax season. This controlled environment allowed for bugs
to be detected and fixed in real-time with internal and knowledgeable users.

On February 1, 2024, Dixie Warden, an IRS employee in Texas, became the first person to
file her taxes on Direct File. Initially, her return did not get submitted, but after a quick fix,
Warden’s tax return went through, marking a historic milestone. “The way that it was laid out
was just so darn easy to understand and I just see it being helpful for so many millions of people,”
               15
Warden said. Taxpayers in states with state income tax had to wait another week. The first
state API export took place on February 9, 2024.

PHASE B: FEBRUARY 22, 2024: Direct File was open during limited and unannounced windows of
public availability. Gradual and controlled growth tested system capacity and allowed bugs
to be resolved before they affected more users.

While the rollout was going well, some on the team worried that the product did not yet have
enough users to have full confidence that it would be ready to handle the end-of-filing-season
volume; most tax filers file their taxes during the last week of filing season. To date, being
risk-aware worked to the product’s favor: no significant bugs were found, and user trust was
maintained. The team’s objectives were never about user acquisition, so no user goals had




15 AP News - A new IRS program is helping its first users file their income taxes electronically. And it’s free, March 6,
2024, https://apnews.com/article/irs-income-taxes-direct-file-program-free-4b0917e281b63e06527343598dde650c




                           UC Berkeley Executive Fellowship in Applied Technology Policy • 20
                                            The Life and Death of Direct File




been set. But would this approach cause problems later: would Direct File be able to scale to
meet the demand?

After conversations with the Commissioner to better align on objectives, it was determined
that the benefit of opening up to more users and making Direct File more widely available
outweighed the risks. The product had performed well to date and needed more users to
determine if it could safely scale as the end of the filing season approached.

PHASE C: MARCH 12, 2024: Direct File became available 24/7, with the IRS reserving the right to
limit usage if needed. The Spanish version also went live. The team was being prudent, con-
cerned with the risk of glitches or outages.

PHASE D: MARCH 19, 2024: with Phase C successful, the IRS gave the green light to move Phase D,
allowing all eligible taxpayers to participate.

The benefits of a controlled rollout were evident for the team. They had prepared for many
scenarios: more than 1,600 test cases had been written and tested before launch. But inevita-
bly, with each new wave, unanticipated bugs would surface that were swiftly handled by the
team. In total, however, only four types of bugs were identified after the platform went live,
and quick action contained them: the bugs only affected 26 tax returns.

The Direct File team consistently made decisions based on both user feedback and data.
An example of this successful strategy happened in March 2024, when the team noticed
unusually high rejection rates in one category: prior year’s adjusted gross income (AGI) veri-
fication. To file electronically, Modernized e-File (MeF), the program that is the foundation of
electronic filing, requires taxpayers to verify their previous year’s AGI to confirm their iden-
tity. The problem: Direct File had no previous year’s data for taxpayers, leading to a higher
error rate than other filing options. Yet the IRS had that information for all taxpayers. On
March 25, 2024, the team embarked on a two-week sprint involving engineering, UX, trans-
lation, and testing to integrate prior-year AGI into Direct File for authenticated users. The fix
                                                       16
shipped on April 5, reducing rejection rates by 25%. This was the team’s first foray into data




16 IRS Direct File Pilot Program - Filing Season 2024 After Action Report, May 3, 2024, https://www.irs.gov/pub/irs-pdf/
p5969.pdf




                           UC Berkeley Executive Fellowship in Applied Technology Policy • 21
                                            The Life and Death of Direct File




import — something the user research had indicated was what taxpayers most wanted to see
from Direct File.

On April 15, 2024, the tax season ended. Direct File remained open until April 20 to allow
resubmission for rejected returns. It was time for the team to conduct a post-mortem of the
pilot, and for Treasury to decide on the future of Direct File.

The Results: A Trusted, Beloved Pilot

On May 3, 2024, the IRS released the Filing Season 2024 After-Action Report, summarizing
the key lessons learned from the pilot. The document highlighted both the results and the
work that led to them, crediting the team’s values and ways of working.

The outcomes were encouraging. Of the 15.4 million eligible taxpayers, approximately 3.3
million used the Direct File Eligibility Checker. Of those, 423,450 logged in to Direct File, and
140,803 submitted accepted returns — far exceeding the initial target of 100,000. Most users
were able to file in under 30 minutes. Participation was highest in California, Texas, and
        17
Florida.

The team was thrilled: more than 140,000 households had filed their return directly with
the IRS — quickly, accurately, and free of charge. However, they knew there was room for
better outcomes. Indeed, due to the time spent on technical troubleshooting and the tight
deadlines, the marketing and outreach strategy had not been a priority until late into the tax
season. Despite the IRS’s press announcement, there was little initial traction, and users did
not come right away. It was noted that more efforts were needed to make sure the public was
aware of the new option.

Despite a slow start, limited resources, and largely manual efforts to raise awareness, Direct
File reached a significant number of taxpayers. More than 15,000 Direct File users responded
to the IRS Touchpoints survey, with 90% rating their experience as “excellent” or “above aver-
age.” They found Direct File to be easy to use and trustworthy, and appreciated the ability to
file their returns for free.

The project’s experiment with customer support was also a success: the live chat operated by
dedicated IRS customer support agents proved to be key in supporting taxpayers. Ninety per-
cent of respondents rated their experience as “excellent” or “above average.” Many praised
Direct File’s clear and straightforward instructions, while others expressed high levels of
enthusiasm: “It was amazing, easiest taxes I’ve ever prepared! Really impressed that this was
put together by the IRS,” one user wrote. The agents handled a total of 38,600 chats, serving

17 IRS Direct File Pilot Program - Filing Season 2024 After Action Report, May 3, 2024, https://www.irs.gov/pub/irs-pdf/
p5969.pdf




                          UC Berkeley Executive Fellowship in Applied Technology Policy • 22
                                            The Life and Death of Direct File




10% of pilot participants who resorted to the chat for help. The average time for chats was
nine minutes, with an average wait time of less than one minute.

Perhaps more surprisingly, 86% of users reported that using Direct File increased their trust
           18
in the IRS. This was a testament to the team’s focus on accessibility and plain language. For
the product designers, this validated their key assumption and intention: well-designed,
user-friendly government services can build public trust. For observers, it was a meaningful
learning: Americans expect government technology to be easy to use, free, and accessible.

The financial investment was also worthwhile. The total cost of the pilot at the IRS was $24.6
million, with an additional $7.2 million at USDS. With this investment, the IRS estimated that
                                                                 19
Direct File users saved $5.6 million in tax preparation services.

With a successful pilot completed — and numerous promises for the digital transformation
of tax administration — the IRS announced that Direct File would become permanent. It was
a victory for the team, who had hoped for this outcome, but also for taxpayers, as Direct File
                                                20
would expand to cover more filers in the future.




18 IRS Direct File Pilot Program - Filing Season 2024 After Action Report, May 3, 2024, https://www.irs.gov/pub/irs-pdf/
p5969.pdf
19 IRS Direct File Pilot Program - Filing Season 2024 After Action Report, May 3, 2024, https://www.irs.gov/pub/irs-pdf/
p5969.pdf
20 IRS - IRS makes Direct File a permanent option to file federal tax returns; expanded access for more taxpayers
planned for the 2025 filing season, May 30, 2024, https://www.irs.gov/newsroom/irs-makes-direct-file-a-permanent-option-
to-file-federal-tax-returns-expanded-access-for-more-taxpayers-planned-for-the-2025-filing-season




                          UC Berkeley Executive Fellowship in Applied Technology Policy • 23
                                            The Life and Death of Direct File




The 2025 Tax Season
Between May 2024 and the start of the 2025 tax season, the team remained focused on
expanding Direct File. The geographic coverage grew significantly, from 12 to 25 states.
Eligibility was also broadened to support the Child and Dependent Care Credit, the Premium
Tax Credit, the Credit for the Elderly and Disabled, and the Retirement Savings Contribu-
tion Credits. It also added coverage for taxpayers claiming deductions for Health Savings
                                                                                   21
Accounts. As a result, Direct File’s 2025 reach expanded to 32.2 million taxpayers.

Technical capabilities were also improved. A One-Step Signature feature was added to
allow taxpayers to sign and validate returns with a single checkbox. Authenticated live chat
provided logged-in users with more efficient support, while the data import feature enabled
more taxpayer information to flow directly into the returns. The IRS invested $41 million to
prepare and operate the program during the 2025 tax season, funding enhancements that
allowed the submission acceptance rate to increase from 73.4% to 87.9% between 2024 and
        22
2025 ().

Despite these technical achievements, the newly elected Trump administration did not com-
municate to taxpayers about Direct File. In early February, the President’s technology czar,
Elon Musk, shared a confusing tweet indicating that he had “deleted” Direct File. From there,
media coverage echoed confusing statements, with headlines such as ““Elon Musk says he
                                                                     23
‘deleted IRS Direct File.’ Can taxpayers still use the free service?”

A total of 296,531 returns were filed and accepted in 2025 through Direct File, an increase
of 111% over the prior year. Satisfaction remained high, with 94% of taxpayers rating their
                                                                   24
experience as “excellent” or “above average,” up from 90% in 2024. Yet the tax season was
marked by political turbulence that undermined public outreach, created confusion, and
eroded public trust. Commissioner Werfel resigned just as the season opened, three years
before the end of his term. From there, partisan attacks and inconsistent messaging inten-




21 IRS - IRS Direct File Filing Season 2025 Report, May 13, 2025, https://taxpayer-rights.org/wp-content/
uploads/2025/06/2025-14762.pdf
22 IRS - IRS Direct File Filing Season 2025 Report, May 13, 2025, https://taxpayer-rights.org/wp-content/
uploads/2025/06/2025-14762.pdf
23 IRS - IRS Direct File Filing Season 2025 Report, May 13, 2025, https://taxpayer-rights.org/wp-content/
uploads/2025/06/2025-14762.pdf
24 IRS - IRS Direct File Filing Season 2025 Report, May 13, 2025, https://taxpayer-rights.org/wp-content/
uploads/2025/06/2025-14762.pdf




                          UC Berkeley Executive Fellowship in Applied Technology Policy • 24
                                            The Life and Death of Direct File




sified. This environment coincided with a drop in reported trust: only 68% of users said that
Direct File increased their trust in government, compared to 86% in 2024.

Direct File is Shuttered

In March 2025, President Trump’s Department of Government Efficiency (DOGE) made
clear to IRS leadership that the Direct File team would be stood down and no future work in
preparation for the 2026 filing season should continue. In May 2025, the IRS made Direct File
              25
open source, giving the wider civic tech community and state tax administrations an option
to build from the platform if they so choose. After Congress directed the IRS to write another
report to explore future tax filing partnerships with the private sector, Treasury officially
                                                   26
confirmed that they would shut down Direct File.




25 Github - direct-file, https://github.com/IRS-Public/direct-file
26 Congress.gov, H.R.1 - One Big Beautiful Bill Act, July 4, 2025, https://www.congress.gov/bill/119th-congress/
house-bill/1/text




                          UC Berkeley Executive Fellowship in Applied Technology Policy • 25
                                      The Life and Death of Direct File




The Lessons of Direct File
Direct File offers valuable insights for leaders at every level. From engineers like Ryan and
Paul to team leads such as Bridget, Merici, Chris, Suzanne, and Steve, to agency heads like
Commissioner Werfel and Deputy Secretary Adeyemo, a successful product launch requires
collaboration, as well as protection and advocacy from leadership.

Direct File also showcases a shift in how government can work by adopting the agility of
startup practices while meeting the public’s needs responsibly and efficiently. High-level
executives play a critical role in creating an environment where empowered teams can thrive
and deliver meaningful results within a system traditionally characterized by red tape rather
than tools like Slack.

TIME IS YOUR MOST CRITICAL RESOURCE
The decision-making process to launch Direct File took too long; between autumn of 2021
and the launch in January 2024, the team lost a valuable 18 months that could have led to
broader usage and, eventually, greater tax scope. Direct File should give future leaders confi-
dence that a small pilot can lead to astonishing results — and those small pilots should start
early and pivot often.

NEW GOVERNANCE IS REQUIRED
“The tech is the easy part, people are the hard part” is a common refrain across complex bureau-
cracies. Mobilizing organizations to create the conditions for successful, transformative ser-
vices requires strong governance, supported by strong, accountable leaders. Agency leaders
need to have visibility into issues as they arise, and the most effective approach is to establish
a cadence and structure that allows teams to surface roadblacks and blockers in real time.

Additionally, being responsive to users requires that product or service teams have the
capacity and permission to rapidly fix bugs, update the product based on feedback, and
pivot their strategy if necessary. Different decisions need to be made at the right moments,
and it is important that teams have the authorizing structures to deliver accordingly. For
example, decisions about deploying a product update to fix a bug need to be made on a min-
ute-by-minute basis, not through a bi-weekly or monthly governance committee.

BUILD A TEAM THAT UNDERSTANDS TECH, EVEN IF YOU DON’T
Agency leaders are often hired for their policy expertise. As organizations embed more
software into their operations, technical expertise is required at the most strategic level to
support mission-level planning and execution. Commissioner Werfel, for example,under-
stood how to partner with and support an empowered service team like the developers of
Direct File. This level of comfort and support is rare at the federal level, but it should not




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 26
                                      The Life and Death of Direct File




be. Agency leaders need to surround themselves with technical leaders and embed them in
critical decision-making processes.

MOVE BEYOND ORGANIZATIONAL STRUCTURES
Consumer-facing launches should be a strategic agency priority, surpassing individual busi-
ness and IT objectives. Federal agencies make decisions based on organizational silos, often
throwing requirements from one side to the other, and without the consumer-facing product
development expertise necessary to ensure success. Historically, websites and new products
are treated within the federal government — both organizationally and culturally — with the
attitude, “It’s an IT thing.”. Now, consumer-facing digital products are mission-level, strate-
gic priorities, and they must be treated as such, with empowered, cross-functional teams
empowered to deliver.

SUPPORT EARLY AND OFTEN
The first step for agency leaders is to establish the necessary permission structure that
allows agile teams to flourish. This means using institutional authority to shield delivery
teams and enable bold experimentation. In the early days of Direct File, the talented USDS
team worked tirelessly to persuade White House leaders, particularly principals at the
National Economic Council, of the project’s promise. Yet no formal permission structure
emerged until the IRA passed, two years into the Administration, costing precious time that
could have accelerated the pilot’s launch.

When Ryan Ahearn took the lead during the sprint to production, his mandate was simple
yet critical: remove any obstacles in his team’s way. Through daily Zoom check-ins and
weekly sprints, he provided the necessary cover and support, allowing the team to focus
on the product. This illustrates how engaged and empowering leadership at every level of
government is essential to getting complex projects across the finish line.

Commission Werfel demonstrated this principle in action during the summer of 2023. When
Suzanne Chapman, the design team lead, faced long approval timelines for surveys and user
research within the IRS, she escalated her concerns to her supervisors. Werfel intervened,
securing a 10-day turnaround for approvals and ensuring the Direct File team could stay true
to its user-centered practices.

Werfel’s ability to step in was not only a function of his position at the IRS, but also of the
support he received from Treasury. Deputy Secretary Adeyemo recognized the project’s
significance to the Administration and provided the high-level backing necessary to clear
institutional hurdles. This highlights an essential truth: for agency leaders, time is a scarce
but powerful currency. By dedicating time and energy to removing obstacles and signaling




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 27
                                      The Life and Death of Direct File




priorities, leaders enable delivery teams to succeed, especially when projects enter the polit-
ical spotlight.

LEADING THROUGH RISK
Additionally, high-profile projects can’t be managed under the perception of zero risk. “No
risk” leads to inaction and favors the status quo, which in this case leaves many Americans
having to pay to file their taxes each year. Leaders need to be comfortable with the manage-
able risks that large-scale projects entail, and maintain a problem-solving mindset: when
challenges arise, the priority should be to assess risks quickly, remove obstacles, and keep
the project moving, rather than adding layers of risk-management paperwork and slowing
the project down.

When the engineering team reported the delay in deploying on IEP, leadership’s response
was measured and solution-oriented. Instead of halting the progress, they supported a
temporary postponement and gave the team the flexibility they needed to respond to the
challenge while empowering them to change their ways of working. The backing of the IRS,
Treasury, OMB, and the White House made this possible, ensuring that the project stayed
on track. Along with setting priorities and creating the necessary permission structure for
teams to operate, the ability to manage setbacks when they happen should be an essential
tool in every leader’s toolbox.

A MULTIPLE-WAY STREET
Building trust during high-stakes, high-profile launches requires constant, transparent com-
munication across all levels of government. Within the delivery team, progress updates and
roadblock reports are essential. Delivery team leaders not only set timelines and deliverables
that reflect project constraints, but they also listen closely to feedback from their teams and
management. Communicating often and early is key. For high-level leadership, commu-
nication involves staying up-to-date on a project and using influence to resolve challenges
quickly and sustain progress.

In September 2023, the announcement that Direct File could not be deployed on IEP exem-
plified a breakdown in the chain of communication. Indeed, feedback from the engineers
was slow to reach the team leads, who continued reporting to Commissioner Werfel that
deployment was on track. Once the news broke, leadership reaffirmed its support, and the
team adopted a new communication style: full transparency, including the creation of a
“no-surprise” tracker to ensure that all information flowed early and openly, up and down
the chain, helping rebuild trust.

Achieving this level of openness required breaking down silos and entrenched working
habits. Direct File introduced a new way of working at the IRS, featuring a fully integrated
team on which contractors and government employees collaborated daily. Instead of rigid
contracts with lengthy lists of specs and major milestones, contractors embarked on weekly



                     UC Berkeley Executive Fellowship in Applied Technology Policy • 28
                                      The Life and Death of Direct File




sprints and engaged in continuous open dialogue. Contractors, accustomed to shielding
issues to avoid penalties, had to adjust and report setbacks promptly, creating opportunities
for feedback and course correction. This cultural shift was key to keeping Direct File on track.

IN-HOUSE CAPACITY: BUILDING A GOVERNMENT PRODUCT
The success of Direct File reflects the effective application of the USDS playbook, with its
startup-like approach to agile government. Blended teams, iterative processes, and a com-
mitment to user-centered design supported the project from concept to completion. The
first principle of the USDS Playbook — spending time with users to understand their needs
and testing prototypes early — proved essential. The Direct File team adopted short feedback
loops, with designers and engineers collaborating closely with taxpayers and IRS customer
representatives to test scenarios and ensure accessibility.

This proximity to end-users shaped every aspect of the product. Suzanne Chapman and the
design team collaborated with hundreds of users and reviewed thousands of use cases to
create a simple and intuitive tax filing experience. The team was obsessed with using plain
language and giving people confidence in their ability to file taxes directly with the govern-
ment. This user-focused approach ensured that Direct File addressed taxpayers’ pain points
and provided real value.

Iterative practices were in the DNA of the Direct File team. Understanding that the most
efficient way to build was incrementally, they set realistic goals for the pilot and delivered
updates rapidly. Once on IEP, they shipped new fixes and features on a regular schedule.
With a work cadence based on sprint-based demos every two weeks, they built a reliable
product fast. Their data-driven approach to releasing updates, assessing their effectiveness,
and testing them on users led to a successful pilot. This rapid loop marked a sharp departure
from traditional government projects.

Finally, the team behind Direct File was its greatest asset. They navigated complex political
environments and resisted great pressure to deliver a successful end product. Despite the
almost certain termination of Direct File, its work now lives as an open source project, feed-
ing into the hope that it could return and serve American taxpayers again in the near future.




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 29
                                      The Life and Death of Direct File




Conclusion
While Direct File has long been a dream for a few civic tech visionaries, its realization in just
a couple of years was truly extraordinary. Despite political turmoil, technical hurdles, hours
of user testing, tight budgets, and constant scrutiny, the team delivered what few thought
possible: a product that was almost universally praised by the taxpayers who used it.

Agency and department leaders played a pivotal role in making this happen. Beyond
ensuring that delivery teams implement best practices and have best-in-class skills, leaders
also need to advocate early for high-stake projects, create a permission structure to enable
progress, embrace and manage the risks, provide cover through turbulence, and act as
champions to ensure success, from beginning to end. During the two years following the
IRA, the high-level executives involved with Direct File navigated a complex environment in
an unchartered territory of government technology, sometimes with mixed results.

The key lessons from Direct File’s success with taxpayers is clear: Americans not only appre-
ciate when their government makes their life easier; they demand it. Thanks to the roadmap
provided by Direct File, future government leaders won’t have to start from scratch to take
on that call to action. As a senior Treasury official noted, “Whoever takes this job three years
from now will look back at the IRS’s tech modernization and the impact the Direct File team
had.” What future leaders will need is the courage to take on ambitious projects and the con-
viction that government can and should deliver big things.




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 30
                                      The Life and Death of Direct File




Appendix: The Direct File Playbook
The Direct File team had a little over seven months to build a complex product and integrate
it into state tax systems before the start of filing season. With Treasury’s green light, the
backing of Commissioner Werfel, and an ambitious deadline, Bridget Roberts, Merici Vinton
and Chris Given created the context to not only deliver a great product but to assemble a
team capable of building it. Together, they paved a path forward and created a new playbook
for delivering technology in the federal government. Here are key lessons learned from
Direct File that future leaders and delivery owners and teams can follow.

APPOINT A SERVICE OWNER
Taking a page from the UK’s successful Government Digital Service (GDS) team, Bridget Rob-
erts was appointed as Direct File’s Service Owner. A Service Owner12 is fully accountable,
empowered to make the majority of daily decisions, and owns the entire service, end-to-end.
Like most government agencies, the IRS makes most decisions through arduous governance
boards and committees. The Service Owner approach breaks that model and simplifies
decision-making, which, in the case of Direct File, was critical, given the near-impossible
deadline.

OWN THE STRATEGY AND EXECUTION: BUILD AN IN-HOUSE TEAM
From there, the leaders of the Direct File project went on to build a team that fully owned the
strategy and execution. As previously stated, most government agencies outsource product
development and strategy entirely to external vendors, an approach that rarely incorporates
user feedback or leads to a successful delivery.

The Direct File team had a head start: they could draw from the talented pool of employees
with technical expertise and experience at USDS, several of whom had already supported
the prototyping process. The team grew to include additional IRS employees, as well as 18F
and vendor teams. When working with contractors, the approach was “badgeless” to inte-
grate them into the team and tie contracts to regular, tangible deliverables, avoiding the trap
of distant milestones and siloed work.12

The team was structured around product goals, not organizational or vendor siloes. Unlike
most government projects, which rely heavily on external contractors delivering milestones
based on generic specs, Direct File was led by a blended team. Engineers, designers, contrac-
tors, legal counsel, and policy experts worked closely and collaboratively as one team. Over




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 31
                                     The Life and Death of Direct File




time, the team built its own identity and culture, from all-hands and regular product demos
to goofy Slack channels and custom-branded merch.

BUILD A JOINED-UP “SERVICE TEAM”
Unifying the customer support and product teams was an effective example of how govern-
ment can work across existing silos to deliver excellent customer experience. Creating an
ongoing feedback loop between users, front-line IRS staff, and the product team meant that
issues facing taxpayers could be addressed in real time. Changes like this do not require a
new budget, but rather result from leadership with a relentless focus on delivery.

CULTURE MATTERS
Clear-eyed on their objective to build the best team, the USDS team developed onboarding
exercises to reinforce mission alignment from the start. Indeed, Direct File had been a
“white whale” of civic technologists for so long that the interest from would-be team mem-
bers was high. But they also sought people motivated by more than the tech challenge. In
one exercise, new hires played a “spectrum” exercise: Was Direct File’s main purpose to ease
the burden on taxpayers on one end, or to make benefit administration more efficient on the
other end? There was no right answer: the goal was to surface values and ensure every team
member bought into the broader vision of public service.

PROTOTYPE EARLY AND OFTEN
The Direct FIle team used prototyping as a strategy throughout the process. Initially, they
prototyped to strengthen the case for an excellent user experience and set clear baseline
expectations. Until the initial prototype demo, stakeholders had different expectations
for what was possible, and each version of the prototype aligned stakeholders and drove
momentum forward. The prototype was also used to get feedback from potential users; this
allowed the team to pivot their approach and ensured they were building a product that
made sense to taxpayers. Finally, the team gained invaluable momentum by prototyping as
part of the initial report to Congress.

GO DEEP ON TAXES
To create a team that could deliver a new tax service, skills alone were not enough: the team
set out to build a learning culture. Few of the incoming engineers and designers had expe-
rience with the details of tax filing; they would need to learn quickly. With the right people
on, team members were regularly encouraged to read IRS bulletins and reports, immerse
themselves in the work, and grow a shared knowledge of the policy context.

DESIGN WITH USERS, NOT FOR THEM
The Direct File design team knew that the success of their product centered on delivering
an excellent user experience. Led by Suzanne Chapman, this team relentlessly tested the
product with users to better understand their needs, identify confusing words to simplify,




                    UC Berkeley Executive Fellowship in Applied Technology Policy • 32
                                      The Life and Death of Direct File




and pivot strategy when needed. The Direct File team talked to over 150 people before and
throughout filing season. Without this feedback, the final Direct File product would not have
had the accessible user experience it did.

DESIGN FOR TRUST AND ACCESSIBILITY
In addition to ongoing user research, the design team worked to ensure that Direct File
would exceed best practices for accessible users, going beyond standard compliance with
Section 508 (which requires that government technologies are accessible to people with dis-
abilities). Chapman enlisted Louise Clarke, the head of accessibility at USDS, to continuously
push the team to ensure standards were not just met, but exceeded. The team also partnered
with the American Council for the Blind to give feedback and ensure the product was usable
for taxpayers who are visually impaired.

TAXES ARE THE PRODUCT
This was a core value the Direct File team wove into every decision: an IRS-run tax product
had to be accurate and secure. Tax law changes frequently, so the Direct File needed to be
easily and quickly updated to reflect tax code changes via a configuration file. The Direct File
engineering team built not just the ability to calculate and file taxes, but also to nimbly make
updates to the software — a near miracle, given the short period of time the team had.

PRIORITIZE DATA-DRIVEN DECISION MAKING
Direct File had a Data Product team whose sole responsibility was to analyze data as it came
in and recommend product updates to reduce rejected returns or simplify the journey. This
team provided Bridget and agency leadership with a consistent stream of information about
the product’s performance and improvements. Build the capacity to support continuous
improvement and iterate services based on analytics.

START SMALL TO GET IT RIGHT: LAUNCH CONTROL
To avoid a potentially catastrophic launch, the Direct File team took a phased approach to
launch. They started slowly, initially with just one user, and observed the product’s progress
when it had just a handful of users filing at one time. The objective was to catch bugs early.
This strategy worked: the first filer encountered a bug that would have been catastrophic had
the product been widely available. Instead, the team quickly spotted the minor issue in IEP,
redeployed, and successfully submitted the tax return. This approach ensured that trust was
maintained and set new expectations for government products.




                     UC Berkeley Executive Fellowship in Applied Technology Policy • 33
                                                 The Life and Death of Direct File




About the Author
                                	MERICI VINTON spent four years helping build and launch Direct File, the
                                  IRS’s first free tax filing service, serving as its Deputy and later as
                                  Senior Advisor for Digital Delivery to IRS Commissioner Danny Wer-


Author photo by Dina Litovsky
                                  fel. This case study is the product of her research as an Executive Fel-
                                  low in Applied Technology Policy at UC Berkeley’s Goldman School of
                                  Public Policy and School of Information.

She currently serves as a Senior Advisor to the Federation of American Scientists and a
Senior Fellow at the Center for American Progress, where her work focuses on the future of
digital government and new models for public service delivery.

Prior to her current roles, Merici served as Deputy of Direct File, overseeing all aspects of
its launch to the American public in 2024, and later as Senior Advisor for Digital Delivery
to IRS Commissioner Danny Werfel, where she applied those lessons to IRS-wide digital
transformation.

Before Direct File, Merici led Child Tax Credit implementation for the US Digital Service at
the White House. She was one of the first employees at the Consumer Financial Protection
Bureau, where she built the agency’s digital team and established a groundbreaking strategy
based on open source, open data, and transparency- setting the standard for modern web
services across the federal government.

Merici is also the co-founder and former CEO of Ada’s List, a women’s leadership community
she successfully exited in 2022. Before her government work, she held senior roles at IDEO
and Accenture/Fjord.




                                UC Berkeley Executive Fellowship in Applied Technology Policy • 34
                                      The Life and Death of Direct File




Acknowledgments
Thank you to the UC Berkeley Executive Fellowship in Applied Technology Policy program
and its sponsors — the Goldman School of Public Policy and the School of Information — for
creating the space and support for this case study. Thank you to Deirdre Mulligan for her
leadership, vision, and the opportunity to participate in the fellowship. Thank you also to
Dan Zhukov for his support throughout the fellowship. Thank you to my fellow fellows for
their brilliance, vision, and inspiration. I so enjoyed working with you all, as well as drawing
on the energy and inspiration from the wider UC Berkeley campus.

Special thanks go out to my research assistants and co-authors — Melanie Girod and Omar
Morales — for their contributions to this project’s planning, research, drafting, editing, and
final publication.

Thank you to my husband, Dominic Campbell, and kids, Hopkins and Dakota, for their end-
less support, patience, and love.

FINALLY — TO THE DIRECT FILE TEAM — THANK YOU FOR MAKING THE IMPOSSIBLE, POSSIBLE.

This project would not have been possible without the former government officials who
shared their time and insights. The following agreed to be named:

Ryan Ahearn, Former Direct File Engineer, 18F, General Services Administration

Suzanne Chapman, Former Direct File Director of User Experience, IRS

Hannah Garden-Monheit, Former Special Assistant to the President for Economic Policy,
National Economic Council

Chris Given, Former IRS Direct File Product Owner, USDS Project Co-Lead

Mina Hsiang, Former US Digital Service Administrator

Jason Miller, Former Deputy Director for Management of the Office of Management and
Budget

Natalie Quillian, Former Deputy Chief of Staff of the White House

Bharat Ramamurti, Former Deputy Director of the National Economic Council

Bridget Roberts, Former Direct File Service Owner, IRS

Neera Tanden, Former Director of the Domestic Policy Council and Senior Advisor to the
President overseeing USDS

Danny Werfel, Former IRS Commissioner



                     UC Berkeley Executive Fellowship in Applied Technology Policy • 35
                                    The Life and Death of Direct File




UC BERKELEY EXECUTIVE FELLOWSHIP
IN APPLIED TECHNOLOGY POLICY
                   UC Berkeley Executive Fellowship in Applied Technology Policy • 36