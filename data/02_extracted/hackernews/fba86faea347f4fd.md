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