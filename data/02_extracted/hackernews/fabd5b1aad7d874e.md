---
title: A digestion of the Jacobian conjecture counterexample
source: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
author:
- '[[jeremyscanvic]]'
published: '2026-07-21'
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
description: 'Article URL: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
  Comments URL: https://news.ycombinator.com/item?id=48998362 Points: 257 # Comments:
  95'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fabd5b1aad7d874e
source_type: community_discussion
tldr: 陶哲轩发文解析了近期利用Fable AI发现的雅可比猜想三维反例，从几何角度给出了该反例的构造原理和坐标计算公式。
objective_summary: 菲尔兹奖得主陶哲轩（Terence Tao）在其个人博客撰文，解析了近期利用Fable AI发现的雅可比猜想（Jacobian
  conjecture）三维反例。该反例构造了一个具有非零常数雅可比行列式但不可逆的三变量多项式映射，证明了雅可比猜想在三维及更高维度上不成立。陶哲轩从局部单射性出发，通过齐次多项式乘法映射、缩放对称性商化、以及特定仿射超平面切片等步骤，用分析语言（大O记号）给出了该反例的几何解释和多项式坐标变换公式。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Fable AI
  technologies: []
  key_people:
  - Terence Tao
key_logic_flow:
- 雅可比猜想断言在复数域上，若多项式映射的雅可比行列式为非零常数，则该映射可逆且逆映射也是多项式。
- 近期利用Fable AI发现了一个三维空间中的反例：存在一个七次多项式映射，其雅可比行列式为非零常数，但该映射不可逆。
- 该反例可重新表述为：存在一个与仿射空间同构的代数簇，及其上的一个局部单射但非全局单射的多项式映射。
- 反例构造基于两个复变量的三次齐次多项式乘法映射，该映射在商去缩放对称性后仍具有三对一的非单射性。
- 通过选用具有两个相同根的微分算子对应的仿射超平面切片，并用分析手法处理零纤维处的奇异性，构造了多项式坐标变换证明该切片与仿射空间同构。
- 最终构造的三维多项式映射同时满足局部单射性（雅可比非零常数）、非全局单射性和定义域与仿射空间的同构性。
object_mentions:
- object_type: product
  name: Fable AI
  canonical_name: Fable AI
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章指出近期利用Fable AI证明了雅可比猜想在三维空间中存在反例，从而在三维及更高维度上该猜想不成立。
  article_id: fabd5b1aad7d874e
extract_result: success
---

The notorious Jacobian conjecture can be formulated concretely over the complex numbers as follows.


Conjecture 1 (Jacobian Conjecture)Let be a polynomial map in complex variables, whose Jacobian is a non-zero constant. Then is invertible (with polynomial inverse).


The condition that the Jacobian is non-zero is equivalent to being locally invertible. (The implication of local invertibility from non-vanishing Jacobian follows from the inverse function theorem; the converse implication can be derived from the Weierstrass preparation theorem, but is omitted here.) Also, from the fundamental theorem of algebra, once the Jacobian polynomial is non-zero, it must be constant. So the hypothesis “Jacobian is a non-zero constant” can be replaced with “ is locally invertible”. So the Jacobian conjecture can be viewed as an assertion that local invertibility implies global invertibility. The complex numbers can be easily replaced with other fields of characteristic zero by the Lefschetz principle, but I prefer to work in the concrete setting of the complex numbers.

It was recently shown (using the Fable AI) that the conjecture is false in three dimensions (and thus in higher dimensions as well):


Theorem 2 (Counterexample to conjecture)There exists a polynomial which has non-zero constant Jacobian, but is not invertible.


The conjecture remains open in two dimensions, and is easy to establish in one dimension.

The example can be stated completely explicitly: one can take

*a priori*the Jacobian ought to be a polynomial in three variables of degree as large as , so the fact that all non-constant coefficients of this polynomial vanish looks like a massive cancellation involving equations, which is much larger than the degrees of freedom for a generic degree seven polynomial of three variables. So finding such a polynomial looks highly unlikely to be located by brute force.

The example has since been retroactively explained in more geometric terms. As a “digestion” exercise to myself, I sought to write this explanation with relatively little use of algebraic geometry, in a manner that minimizes the amount of “miracles” required, although there are still a few places were some remarkable phenomena occur.

It is convenient to use the local injectivity formulation, and to generalize the domain to an equivalent affine variety. Namely, we will show


Theorem 3 (Counterexample, reformulated)There exists an affine variety that is isomorphic to by polynomial changes of variable, and a polynomial map which is locally injective, but not globally injective.


Clearly one can get from Theorem 3 to Theorem 2 by composing with the isomorphism and using the previously mentioned fact that local injectivity implies non-zero constant Jacobian. Our objective is now to find data , that obeys three separate properties:

- (a) is locally injective on .
- (b) is not globally injective on .
- (c) is isomorphic to by polynomial changes of variable.

It turns out that and can be built out of the operation of multiplication of low degree polynomials. Namely, consider the following three simple affine spaces:

- The space of linear homogeneous polynomials of two complex variables .
- The space of quadratic homogeneous polynomials of two complex variables .
- The space of cubic homogeneous polynomials of two complex variables .

The map , essentially a map from to , is clearly polynomial; it is given explicitly in coordinates as

The map also enjoys two basic (and commuting) symmetries:- If one applies a scaling for some non-zero complex numbers , then the product is scaled by : .
- If one applies a change of variables for some invertible linear transformation , then the product is transformed by : .

The five-dimensional domain is of course larger than the four-dimensional range , so the map clearly cannot be injective. This can already be seen from the scaling symmetry, as the specific scalings

for modify the linear and quadratic polynomials but not their product . But even if one quotients out by this symmetry (3) to cut the dimension of the domain down to four, the map is still not injective for the following basic reason. A generically chosen cubic polynomial will split into the product of three independent linear polynomials. Then there are three pairs which all map to the same cubic polynomial (3). Thus, we see that even after quotienting out by the scaling symmetry (3), the multiplication map is generically non-injective in a three-to-one fashion. Thus we already have achieved something resembling goal (b)!It will be convenient to “spend” the scaling symmetry to obtain a useful normalization. If is a linear polynomial and is a quadratic polynomial, the resultant can be defined by the determinant

If we have a factoring (3) multiplies by : Thus, we can (generically) normalize away this scaling symmetry by imposing the conditionWe now have a restricted multiplication map (which by abuse of notation we will continue to call ) from the four-dimensional variety

to the four-dimensional space . This map is still not globally injective, as we can take the three pairs in (4) from before and apply the scaling (3) separately to each of the three pairs to obtain the normalization (7). So we have kept property (b). Furthermore, this map retains the -equivariance (and also one remaining scaling symmetry, though we will not make much further use of that symmetry).But we now also have property (a)! Suppose we want to show the local injectivity of in the neighborhood of a pair with . As the resultant is non-vanishing, the root of (which exists in the Riemann sphere, or projective line if you prefer) is distinct from the two roots of (though the latter two roots could be equal to each other). Applying the action (which performs Möbius transforms on the roots), one can assume without loss of generality that is the point at infinity (or equivalently ), thus for some complex number and for some complex numbers , with the resultant condition (7) simplifies to (so in particular are also non-zero). It is then clear that if one perturbs and by a small amount (say, modifying each coefficient by ), then the root of will perturb to something large (), while the roots of stay bounded. Thus, just from knowledge of the product , one can reconstruct which of the three roots of this cubic polynomial will be the perturbed root of , and which two will be the perturbed roots of ; from this and (6), (7) we can also reconstruct the leading coefficient of , and this completely determines both and . This establishes the local injectivity property (a). (In fact it is étale, but we will not need the machinery of étale maps here.)

Unfortunately, (the four-dimensional analogue of) condition (c) fails: the quadric hypersurface (8) is not isomorphic to the affine space . But we can try to get around this by passing to a three-dimensional slice. Let be some three-dimensional affine plane of (which we will take to avoid the origin for technical reasons), then we can restrict as a map from the set

(8), this continues to be the case after restricting to (9) (unless was somehow so degenerate that it had no generic elements, but this turns out to be impossible). So we have retained properties (a) and (b). The miracle is that, with a good choice of , we can also obtain (c) and obtain the desired counterexample to the Jacobian conjecture: despite appearances, the variety (9) is in fact equivalent to the affine space by polynomial changes of variable!Let’s see how. The affine hyperplanes in avoiding the origin are parameterized by the dual space of avoiding the origin, which one can think of as the non-zero third order homogeneous differential operators in two variables. Indeed, every such operator generates an affine hyperplane that avoids the origin, and conversely by duality every affine hyperplane avoiding the origin arises in this form uniquely. Just as the cubic polynomials in can be factored into three linear polynomials, the differential operators in the dual space can also be factored into three linear differential operators, e.g.,

- Operators where the three roots are all distinct, thus for independent first-order operators .
- Operators where two roots coincide and one is distinct, thus for independent first-order operators .
- Operators where all three roots coincide, thus for some first-order operator .

It turns out that the affine miracle for (9) occurs precisely in the second case, when has two identical roots. I do not have a completely satisfactory geometric explanation for this miracle, but one can verify it by the following coordinate computation.

By applying the action, we can normalize so that , thus is now the affine hyperplane of cubic polynomials with . Using (2) and (5), the variety (9) can now be described explicitly in coordinates as

At first glance this seems to be a generic-looking variety cut out by a cubic equation and a quadratic equation – hardly a candidate to be affine! But observe that if is non-zero, then the second equation can be solved for , and the first equation can be solved for , Putting these two equations together, we see that as long as one removes the case , the quintuple is uniquely determined by by a change of variables which is Laurent in and polynomial in . Thus we have a nice birational equivalence*almost*established property (c): the variety (9) becomes birationally equivalent to after cutting out the subvariety. In particular, for each fixed non-zero value of , the corresponding fiber (10) is equivalent to by polynomial changes of variable, since we can reconstruct from the coordinates by the polynomial formulae

So we just need to glue back in the fiber. Indeed, from (10) we see that the fiber at is just

(10) has the structure of an -bundle over , which is already extremely close to being isomorphic to the affine space . The main remaining task is to make sure that nothing singular happens in the limit , and that a global polynomial coordinate chart for (10) that covers both the and fibers can be constructed.The standard way to proceed here is to manipulate various tangent spaces using the modern machinery of algebraic geometry and commutative algebra, but given my own background, I prefer to adopt the language of analysis, and in particular big-O notation (in place of the ideals used in algebraic geometry), in order to investigate the limit by hand. On the variety (10), let us use to denote any multiple of by a polynomial expression in . Thus, for instance, the equation implies that

while the equation implies that as well as the more refined estimate In the case we could conclude that . Now we perturb this observation. Multiplying (13) by we have , which on substitution into (14) gives ; substituting this back into either (13) or (14) also gives .We can get some more precise asymptotics by also taking advantage of (15). Substituting into (15), we obtain after some algebra

Substituting this back into (11) gives an asymptotic for : (12), although one only gets a trivial bound in this case:Expanding the error term in (16) as , and doing a little more algebra, we thus have a polynomial change of variables

(10) by polynomial combinations of three coordinates . This already gives (a) and thus completes the proof of Theorem 3.The previous computations, when expanded out, also gives polynomial inverse maps:

(1).AI disclosure: I used an AI chatbot to discuss various aspects of this problem and to confirm several of the calculations made here.