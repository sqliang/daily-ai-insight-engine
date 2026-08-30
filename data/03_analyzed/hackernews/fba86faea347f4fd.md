---
title: eigendrum
source: https://eigendrum.com/#p=circle
author:
- '[[bookofjoe]]'
published: '2026-08-14'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'Article URL: https://eigendrum.com/#p=circle Comments URL: https://news.ycombinator.com/item?id=49305250
  Points: 149 # Comments: 37'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fba86faea347f4fd
source_type: community_discussion
tldr: Eigendrum 是一个基于有限元法在浏览器中数值求解鼓面特征值问题的免费交互式网页工具，支持手绘或公式书写形状并聆听各模态振动；求解器经圆形与矩形闭式谱验证，并内置
  Kac 鼓 I、II 两组同谱异形鼓作为听音辨形问题的经典反例。
objective_summary: Eigendrum 是托管于 eigendrum.com 的免费网页应用，它将形状三角网格化，构造有限元刚度与质量矩阵并求解
  Kφ=λMφ 的最小特征值，从而数值求解听音辨形问题。求解器在每次变更时对照圆形与矩形的闭式谱测试，误差优于千分之一。用户可手绘或通过公式书写形状，敲击位置决定各模态的混合比例，按行播放可单独聆听单一模态。应用内置
  Kac 鼓 I 与 II 两组同谱异形鼓，无后端且全部计算在本地浏览器完成，依靠 Vercel Analytics、Google Analytics 与 AdSense
  维持免费运营。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Vercel
  - Google
  technologies:
  - Finite Element Method
  - Eigenvalue Problem
  - Rayleigh Damping
  - Bessel Functions
  - Isospectral Drums
  - Parametric Equations
  key_people:
  - Mark Kac
  - Carolyn Gordon
  - David Webb
  - Scott Wolpert
  - Tobin Driscoll
  - Basel Ashraf
key_logic_flow:
- Eigendrum 将用户形状网格化为三角形，构造有限元刚度矩阵与质量矩阵，求解 Kφ=λMφ 的最小特征值，从而得到各模态频率与驻波形状。
- 求解器在每次变更时对照圆形（Bessel 函数零点）与矩形（π²(m²/a²+n²/b²)）的闭式谱进行测试，误差优于千分之一，且有限元法的能量最小化性质保证结果是轻微高估而非低估。
- 敲击位置按模态在该处的位移幅度成比例地驱动各模态，敲在模态静止线上便无法激发该模态；按行播放可单独聆听单一模态，这是任何敲击都无法做到的。
- 除手绘轮廓外，用户可用极坐标或参数方程书写形状，公式本身作为链接文本可读可重打，过薄的形状会被拒绝而非给出错误数值。
- 文章回顾 Kac 于 1966 年提出听音辨形问题，1992 年 Gordon、Webb 与 Wolpert 用两组同谱异形鼓（Kac drum I 与 II）给出了否定回答。
- 'Eigendrum 无构建步骤、无应用后端，网格划分、求解与音频全部在本地运行，部署使用 Vercel Analytics、Google Analytics
  与 AdSense，用户形状保存在地址栏 # 之后且不会上报服务器。'
object_mentions:
- object_type: product
  name: Eigendrum
  canonical_name: Eigendrum
  url: https://eigendrum.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Eigendrum 托管于 eigendrum.com，这是官方链接与引用地址，旧镜像 baselashraf81.github.io/eigendrum
    现已重定向至此。
  - Eigendrum 没有构建步骤也没有应用后端，网格划分、求解与音频全部在用户自己的机器上运行。
  - Eigendrum 用有限元法数值求解特征值问题，将形状网格化为三角形并构造刚度与质量矩阵，求 Kφ=λMφ 的最小特征值。
  article_id: fba86faea347f4fd
- object_type: project
  name: BaselAshraf81/eigendrum
  canonical_name: BaselAshraf81/eigendrum
  url: https://github.com/BaselAshraf81/eigendrum
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 源码仓库 github.com/BaselAshraf81/eigendrum 包含求解器以及对照闭式谱验证求解精度的测试代码。
  - 作者建议将数学或界面问题提交到该仓库的 issue，因为这样修复过程对公众可见。
  article_id: fba86faea347f4fd
- object_type: product
  name: baselashraf81.github.io/eigendrum
  canonical_name: baselashraf81.github.io/eigendrum
  url: https://baselashraf81.github.io/eigendrum
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 旧版 baselashraf81.github.io/eigendrum 是镜像站点，现已重定向到主域名 eigendrum.com。
  article_id: fba86faea347f4fd
extract_result: success
impact_score:
  score: 3.0
  reason: 该事件是免费交互式数学工具 Eigendrum 的发布，属于面向数学/声学/数值计算爱好者的细分圈层作品。工程上它把有限元广义特征值求解器完整部署到浏览器本地实时运行，并用圆与矩形的闭式谱持续验证精度，颇具匠心，但底层算法是成熟的有限元理论，工具本身不改变任何行业竞争格局，也未触及
    AI 或商业范式的转移，短期行业冲击力有限，属于质量较高的日常更新。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 浏览器端实时求解广义特征值问题的数值精度、无后端纯本地计算与音频合成的工程实现
hype_assessment:
  level: low
  reason: 正文措辞克制，未出现'颠覆''革命性'等 PR 滥用词汇；文章如实说明求解器误差优于千分之一，并坦诚有限元方法只会高估不会低估的数值特性；对 Kac
    鼓这一同谱反例也明确归功于 1992 年 Gordon-Webb-Wolpert 的成果，而非自我标榜。综合判定为实打实的干货。
information_entropy: high
domain_disruption:
  technical_innovation: 将有限元刚度/质量矩阵的广义特征值求解器完整封装进浏览器端，支持手绘与公式定义形状的实时模态分解、敲击位置驱动模态混合与逐模态音频回放，并以闭式谱（Bessel
    零点、矩形谱公式）在每次变更时自动校验，误差优于千分之一；工程上做到无构建步骤、无应用后端、全部本地计算。突破点在于实时交互数值求解的工程化封装与验证严谨性，而非算法理论本身。
  business_model: 无；工具以 Google AdSense 广告覆盖域名成本，采用无后端、零边际计算成本的极简独立 Web 应用模式运营，但属于个人爱好项目，不对任何既有商业模式构成重塑。
engineering_complexity: production_ready
compound_value:
  score: 2.5
  reason: 这是一款单人开发、托管于 eigendrum.com 的免费数学教育类网页应用，用浏览器端有限元法求解鼓面特征值问题。从资本视角看，它不具备任何长期复利要素：所有计算在本地完成、形状数据不上传、无账号体系、无后端，意味着没有用户锁定、数据积累或网络效应，也无法形成可被商业化的资产沉淀。其价值本质是数学可视化科普的公共物品——开源仓库与内置
    Kac 同谱异形鼓经典反例确实让它具备一定的学术参考持久性，但这属于一次性创作内容，而非能随规模递增的基础设施。商业模式依赖 AdSense 与 Ko-fi
    打赏，天花板极低。结论：属于低强度的教育型利基工具，长期复利效应微弱，不构成值得资本追逐的资产。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Vercel
- Google
- eigendrum 开源项目
competitive_casualty:
- MATLAB
- COMSOL
- Mathematica
market_opportunities:
- 可借鉴该项目的浏览器端有限元求解与交互式可视化方案，将特征值模拟扩展到热传导、量子力学本征态、声学振动等教学邻域，打造系列化科学教育互动产品
- 其无后端、数据不落服务器的客户端计算架构，为隐私敏感场景（如在线 CAD 预演、工业声学设计预览）提供了低成本即时仿真范式，值得相关方向创业者参考
- 独立开发者可参考其开源项目叠加广告与捐赠（AdSense/Ko-fi）的轻量变现路径，用于 AI 与数学科普类内容的冷启动与可持续运营
risk_matrix:
  regulatory: 面向欧盟地区用户时需注意 Google Analytics 与 AdSense 的 cookie 同意及 GDPR 合规要求；其余无重大监管风险
  technological: 纯浏览器计算在高模态数量或复杂网格下受终端算力限制，可能影响体验；作为个人开源项目，求解器与前端依赖的长期维护和技术栈更新存在不确定性
  competitive: 同类网页鼓面/模态模拟工具以及 Wolfram、MATLAB 等综合计算平台存在替代压力；项目高度依赖单一开发者和平台生态，商业壁垒较低
  ethical: 无重大伦理风险；已声明不记录地址栏中的形状数据，但广告追踪仍属常规隐私告知范畴，需保持透明
  additional:
  - 项目依赖 Vercel 托管与 AdSense 广告收入维持运营，存在平台政策变动或收入波动的持续性风险
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: Eigendrum
  canonical_name: Eigendrum
  url: https://eigendrum.com
  positioning: Eigendrum 是一款免费交互式网页工具，在浏览器中基于有限元法数值求解鼓面特征值问题，支持手绘或公式书写形状并聆听各模态振动。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 数学与物理学习者
  - 声学与数值计算爱好者
  - 教育工作者
  product_signal: 求解器在每次变更时对照圆形与矩形的闭式谱测试，误差优于千分之一，且有限元能量最小化保证结果是轻微高估而非低估。
  market_signal: 该工具以免费开放、广告与捐赠支持的运营模式存在，尚无明确的商业化或市场推广信号。
  differentiation: 相较于传统数值软件，Eigendrum 无需安装即可在浏览器完成网格划分、求解与音频渲染，并以听音辨形的同谱异形鼓作为可交互反例。
  watch_reason: Eigendrum 以有限元法在浏览器中实时求解鼓面特征值问题，并将 Kac 同谱异形鼓作为可听反例，兼具数值精度验证与数学教育价值，值得跟踪其在教学互动与开源社区中的后续演进。
  risk_notes:
  - 免费工具依赖广告与捐赠维持运营，收入不足时长期维护与域名可持续性存在不确定性。
  - 浏览器端网格划分与特征值求解的规模有限，复杂形状或高密度网格可能带来实时性能瓶颈。
  score: 5.0
  article_ids:
  - fba86faea347f4fd
  evidence_snippets:
  - Eigendrum 托管于 eigendrum.com，这是官方链接与引用地址，旧镜像 baselashraf81.github.io/eigendrum
    现已重定向至此。
  - Eigendrum 没有构建步骤也没有应用后端，网格划分、求解与音频全部在用户自己的机器上运行。
  - Eigendrum 用有限元法数值求解特征值问题，将形状网格化为三角形并构造刚度与质量矩阵，求 Kφ=λMφ 的最小特征值。
- object_type: project
  name: BaselAshraf81/eigendrum
  canonical_name: BaselAshraf81/eigendrum
  url: https://github.com/BaselAshraf81/eigendrum
  positioning: BaselAshraf81/eigendrum 是 Eigendrum 的开源源码仓库，包含有限元求解器以及对照圆形与矩形闭式谱验证精度的测试代码。
  technical_signal: 仓库包含求解器与测试代码，求解结果对照圆形和矩形的闭式谱误差优于千分之一，有限元能量最小化保证结果轻微高估。
  adoption_signal: null
  ecosystem_relevance: 该项目与数值计算、声学与数学教育生态相关，同谱异形鼓数据源自 Driscoll 的研究，并部署于 Vercel 平台。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该仓库同时承载求解器实现与可复现的数值验证测试，为浏览器端有限元计算提供了一个开源参照实现，值得跟踪其求解精度改进、同谱异形鼓扩展以及社区采纳情况。
  risk_notes:
  - 项目依赖单个维护者与个人邮箱联系，长期维护、功能迭代和 issue 响应的持续性存在不确定性。
  - 项目主要服务于数学教育与演示场景，受众较窄，可能限制其社区活跃度与长期演进动力。
  score: 5.0
  article_ids:
  - fba86faea347f4fd
  evidence_snippets:
  - 源码仓库 github.com/BaselAshraf81/eigendrum 包含求解器以及对照闭式谱验证求解精度的测试代码。
  - 作者建议将数学或界面问题提交到该仓库的 issue，因为这样修复过程对公众可见。
---

## how it works

A drumhead clamped at its rim can only vibrate in certain shapes, at certain frequencies.
Those shapes and frequencies are the solutions of

−∇²u = λu inside the shape, u = 0 on the edge

Each solution *u* is a mode, a standing wave, and each λ gives a frequency
proportional to √λ. This is an eigenvalue problem, and for almost every shape it has no
formula. So Eigendrum solves it numerically: it covers your shape with a mesh of
triangles, builds the finite element stiffness and mass matrices, and finds the smallest
eigenvalues of Kφ = λMφ.

### why you can trust the numbers

A few shapes have spectra that can be written down exactly, and the solver is tested
against them on every change. A circle's frequencies are the zeros of Bessel functions; a
rectangle's are π²(m²/a² + n²/b²). The solver reproduces both to
better than a tenth of a percent, and because a conforming finite element method minimises
energy over a restricted space, its answers are guaranteed slight
*over*estimates, never under. The measured error is in “the numbers”.

### where you strike it matters

Striking a spot drives each mode in proportion to how much that mode moves there. Hit a
line where a mode stands still and you cannot excite it at all. That was not programmed
in; it falls out of projecting the mallet onto the modes.

So a strike is never one mode: it is every mode at once, in a mixture set by where your
mallet landed. The rules along the mode list are that mixture, and the modes marked with a
square were the ones your mallet could not reach. Pressing a row instead plays that single
mode *alone* - something no mallet can do, and the only way to hear what one
frequency of a shape actually sounds like.

### drums from equations

Besides tracing an outline you can write one. r(t) gives the
radius as t sweeps one full turn, so
1 + 0.3cos(5t) is a five-lobed flower; a parametric
x(t), y(t) pair reaches the closed curves polar cannot, like a
nephroid or an egg. This is not a shortcut for drawing. It reaches shapes no hand traces
accurately - eleven even lobes, a superellipse partway between a circle and a square - and
it makes a shape something you *vary*: change one number and hear what moved.

A written shape travels as its own text. The link for a formula holds the formula, so it
is something you can read and retype rather than a few hundred characters of encoded
outline, and editing it in the address bar works. Anything too thin to mesh honestly is
refused rather than answered, because a sliver would still return numbers and they would
be wrong.

### can one hear the shape of a drum?

Mark Kac asked exactly that in 1966. In 1992 Carolyn Gordon, David Webb and Scott Wolpert
answered **no**, by building two different shapes with identical spectra.
Both are in the form list as Kac drum I and II. Each is made from the same seven
triangles, rearranged. They enclose the same area and the same perimeter, and every
frequency matches. Switch between them and listen: the outlines are plainly different and
the sound is not.

### what is a modelling choice

The frequency ratios, the mode shapes and the pitch of the fundamental are physics, fixed
entirely by the outline. What is not in the outline is the wave speed, which is tension and
density: the pitch slider sets that by naming the note a circle of this area would sound,
and each shape then lands above the reference by its own amount. Every shape is scaled to
the same area before solving, so that offset is shape and not size - about six semitones
across the built-in shapes, with the circle lowest, which is Faber-Krahn rather than a
choice. How fast each overtone fades is material and air, so that stays a slider rather
than a silent assumption.

The mallet is modelled too. Its width is a slider; its contact time is fixed at a few
milliseconds, because no real beater is instantaneous and one that was would drive every
mode equally hard. Both decide how much of a mode a strike can reach, and neither can move
a mode's frequency. Damping is Rayleigh damping, so loss rises with the square of
frequency: the high overtones die away first, which is why a drum darkens as it rings.

### where it lives, and how to reach me

Eigendrum is hosted at
eigendrum.com. That is the address to link
to and to cite; the older baselashraf81.github.io/eigendrum
is a mirror that now redirects there.

For advertising or partnership enquiries, write to
u2679054@uel.ac.uk. For anything wrong
with the maths or the interface, an issue on the repository is better, because
then the fix is public.

### colophon

No build step and no application backend: the mesh, the solve and the audio all run
on your own machine. The deployed site uses Vercel Analytics, Google Analytics and
Google AdSense, which is what pays for the domain and keeps this free to use. The
shape you draw lives in the address bar after the #, which
browsers never send to a server, and analytics is configured not to record it.
Details in the privacy notice. Set in Jost* by
indestructible type*. After Kac, *Can One Hear the Shape of a Drum?* (1966);
Gordon, Webb and Wolpert (1992); and Driscoll, *Eigenmodes of Isospectral Drums*
(1997), whose coordinates the two Kac drums use.

Source, including the solver and the tests that check it against the closed-form
spectra:
github.com/BaselAshraf81/eigendrum

Free to use, with no account and nothing to install. If you would like to put
something towards it, or would rather it were not ad-supported:
ko-fi.com/baselashraf