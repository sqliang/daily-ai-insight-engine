---
title: AI data centers just got a government-mandated fast lane to the grid
source: https://techcrunch.com/2026/06/18/ai-data-centers-just-got-a-government-mandated-fast-lane-to-the-grid/
author:
- '[[Tim De Chant]]'
published: '2026-06-18'
created: '2026-06-19'
description: FERC told grid operators to give data centers a fast lane for interconnections,
  but it failed to address electricity supply shortages.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cadb3123daaa89ba
source_type: news_media
tldr: FERC 下令电网运营商为 AI 数据中心并网开设快速通道
objective_summary: FERC 于 2026 年 6 月 18 日一致通过指令，要求六大电网运营商为数据中心等大型用电户提供并网快速通道，数据中心承担并网成本。运营商需在
  30 天内提交容量报告，60 天内调整电价。此举因 AI 数据中心电力需求预计到 2035 年增长近三倍。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - FERC
  - PJM
  - Bloomberg
  technologies: []
  key_people:
  - Chris Wright
key_logic_flow:
- FERC 于 2026 年 6 月 18 日一致通过指令，要求美国六大电网运营商为 AI 数据中心等大型用电户建立并网快速通道，数据中心需自行承担并网成本。
- FERC 同时要求电网运营商考虑固态变压器、超导输电线路等替代输电技术，为电网技术初创公司提供机会。
- 电网运营商需在 30 天内提交可用发电容量报告，60 天内说明或修订区域电价，并需更包容地对待数据中心的表后电力方案。
- 截至 2023 年底，发电厂并网请求总量已超过现有发电厂总装机容量，电网拥堵严重，新建电厂本身也面临并网困难。
- AI 数据中心电力需求预计到 2035 年增长近三倍，部分区域批发电价较五年前上涨最高 267%，PJM 等电网运营商陷入混乱。
- 能源部长 Chris Wright 于 2025 年 10 月敦促 FERC 处理数据中心并网延迟问题，称其威胁美国 AI 竞争力。
impact_score:
  score: 7.5
  reason: 该事件是美国联邦能源监管委员会（FERC）针对AI数据中心电力瓶颈出台的强制性法规指令，要求六大电网运营商为数据中心开辟并网快速通道。电力供应是目前制约AI算力扩张的首要物理瓶颈，直接关系到所有AI公司的基础设施建设能力。虽然不属于技术范式转移，但在行业影响面上覆盖整个AI产业链，且带有政府强制力，短期内将显著改变美国AI数据中心的选址逻辑、建设周期和成本结构。评分依据：类比重要产品发布（4-7分）的上限之上，因为其影响范围更广、约束力更强，但尚未达到ChatGPT发布级别的范式转移（8-10分），故给7.5分。
sentiment: mixed
developer_sentiment:
  tone: neutral
  primary_focus: 电力基础设施瓶颈有望缓解但并网成本转嫁给数据中心，以及电网实际容量不足的根本问题未被解决
hype_assessment:
  level: low
  reason: 该报道基于FERC于2026年6月18日正式通过的监管指令，提供了具体的合规时间表（30天内提交容量报告、60天内调整电价）、数据支撑（2035年电力需求增长近三倍、批发电价上涨最高267%、截至2023年底并网请求超过现有装机容量）以及政策背景链（能源部长2025年10月施压）。没有使用'颠覆'、'革命性'等PR修辞，属于政策性事实报道，水分极低。
information_entropy: high
domain_disruption:
  technical_innovation: FERC要求电网运营商评估固态变压器、超导输电线路等替代输电技术，为电网技术初创公司打开了政策驱动的市场准入通道，可能加速新一代输电技术的工程化落地。
  business_model: 数据中心需自行承担并网成本但获得优先通道，改变了AI基础设施的投资回报模型——选址权重的核心从'电价低'转向'并网速度快'；对表后电力方案（behind-the-meter）的包容性要求，为分布式发电+数据中心合建模式打开了政策空间，可能催生'发电-算力'一体化项目的新商业模式。
engineering_complexity: infrastructure
compound_value:
  score: 7.5
  reason: 该政策的长期复利价值在于移除 AI 扩展的核心物理瓶颈——电网并网。AI 算力需求到 2035 年预计增长近三倍，而此前发电厂并网请求已超过现有总装机容量，拥堵已成
    AI 基础设施扩张的硬天花板。FERC 的快速通道指令理论上打破了这一僵局，让数据中心建设从'不可能'变为'可预期'，为超大规模算力投资提供了 regulatory
    certainty。但有两个制约因素：其一，该指令是行政命令而非立法，受政治周期和 FERC 委员更迭影响，长期稳定性存疑；其二，指令并未解决发电容量本身的短缺问题——快速并网不等于快速发电，若发电侧跟不上，批发电价上涨
    267% 的压力将持续侵蚀 AI 推理/训练的单位经济性。总体而言，该政策为 AI 基础设施的开疆拓土扫清了最大的制度障碍，复利效应显著，但根基建立在政策沙地上，需要后续立法或发电技术突破才能稳固。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- Microsoft
- Amazon
- Google
- NVIDIA
- OpenAI
- Meta
competitive_casualty:
- 小型 AI 初创公司
- 传统电网运营商 (PJM 等)
- 欧洲 AI 基础设施
market_opportunities:
- 电网技术初创企业可抓住FERC要求电网运营商评估替代输电技术（固态变压器、超导输电线路等）的窗口期，加速产品落地和电网准入合作
- 表后电力（behind-the-meter）解决方案提供商迎来爆发机会，科技公司因并网延迟已转向自备电源，FERC明确要求运营商更包容地对待此类方案
- 数据中心选址与能源成本咨询服务需求激增，批发电价在部分区域已上涨267%，企业对不同区域电力成本、并网可行性和政策环境的专业评估需求迫切
risk_matrix:
  regulatory: 各电网运营商的执行细则存在差异风险，PJM等已陷入混乱，30天内提交容量报告和60天内调整电价的强制时间表可能导致合规偏差或仓促决策；快速通道可能因绕过常规环评程序而面临环保组织诉讼
  technological: 固态变压器、超导输电等替代输电技术尚未大规模商用，技术成熟度和供应链稳定性风险高；若替代技术无法按期落地，快速通道可能因输电物理容量不足而形同虚设
  competitive: 大型科技公司（谷歌、微软、亚马逊、Meta）凭借更强的资金和政商资源抢先利用快速通道锁定有限并网容量，进一步挤压中小企业和AI创业公司的算力获取空间，加速行业马太效应
  ethical: AI数据中心电力需求预计到2035年增长近三倍，将挤占居民和普通工商业用电，推高全社会电价，加剧能源不平等和'AI优先于民生'的伦理争议
  additional:
  - 执行落地风险：截至2023年底发电厂并网请求总量已超现有总装机容量，电网物理瓶颈并非行政指令能解决，实际改善可能远低于预期
  - 社会政治风险：电价飙升（最高涨267%）可能引发公众反弹和政策摇摆，中期选举周期中能源成本议题可能成为政治火药桶
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
---

The Federal Energy Regulatory Commission (FERC) told grid operators on Thursday to fast-track interconnection requests from data centers and other large electricity users.

Under the orders, six major grid operators have to show that data centers are “able to connect to the transmission system in a timely and orderly manner.” Data centers will be responsible for paying the costs of the interconnection. Commissioners approved the orders unanimously.

FERC also provided an opening to grid tech startups, directing grid operators to consider “alternative transmission technologies.” The commission didn’t name specific technologies, but the directive could include things like solid-state transformers or superconducting transmission lines.

Grid operators now have 30 days to submit a report detailing how much generating capacity they have to spare, if any. They also have 60 days to “defend or revise” electricity rates within their regions. FERC also directed grid operators to be more accommodating to behind-the-meter power for data centers.

While FERC’s directives gave data centers a fast lane to connect, they did not address the shortage of generating capacity.

Grid connections have been slow to materialize in part because new power plants are also having problems connecting. At the end of 2023, grid connection requests for power plants exceeded the total capacity of the existing power plant fleet, meaning the line to get on the grid was longer than the grid itself could theoretically serve.

Against this backdrop, electricity demand from data centers is expected to nearly triple through 2035. Grid operators, which had grown accustomed to near-zero demand growth over the last two decades, have strained under the load. Some, like PJM, the country’s largest grid operator, have descended into something resembling chaos, with major utilities threatening to withdraw.

Tech companies and developers, unable to connect to the grid in a timely manner in many locations, have been turning to on-site, or behind-the-meter, power (which is typically more expensive and complicated) out of desperation.

Still, enough projects have been able to connect that electricity prices have soared in many regions. Wholesale electricity rates are up as much as 267% compared with five years ago, according to Bloomberg.

FERC was prodded to take on the issue by Secretary of Energy Chris Wright, who in October said delays in data center grid connections had threatened to undermine U.S. competitiveness in AI. Since then, public sentiment toward AI and data centers has soured considerably.