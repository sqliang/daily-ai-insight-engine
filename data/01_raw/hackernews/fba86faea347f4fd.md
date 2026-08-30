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
pipeline_stage: ingested
id: fba86faea347f4fd
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