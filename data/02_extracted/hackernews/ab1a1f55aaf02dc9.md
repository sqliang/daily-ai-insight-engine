---
title: Free the Icons
source: https://weblog.rogueamoeba.com/2026/06/26/free-the-icons/
author:
- '[[zdw]]'
published: '2026-06-27'
created: '2026-06-30'
description: 'Article URL: https://weblog.rogueamoeba.com/2026/06/26/free-the-icons/
  Comments URL: https://news.ycombinator.com/item?id=48698908 Points: 450 # Comments:
  129'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ab1a1f55aaf02dc9
manifest_dates:
- '2026-06-30'
source_type: community_discussion
tldr: Paul Kafasis 呼吁 Apple 在 MacOS 中恢复允许第三方应用图标使用不同形状，而非强制统一的圆角矩形。
objective_summary: Paul Kafasis 于 2026 年 6 月 26 日发表博文，批评 Apple 在 MacOS 26 (Tahoe)
  中强制第三方应用图标统一为圆角矩形形状，认为此举损害了可用性和创意表达，并呼吁 Apple 在 MacOS 27 (Golden Gate) 中恢复图标形状的自由。
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies:
  - Apple
  technologies:
  - MacOS
  key_people:
  - Paul Kafasis
key_logic_flow:
- Apple 在 MacOS 26 (Tahoe) 中为第一方应用引入了模糊的「Liquid Glass」图标风格，并强制所有第三方应用图标必须采用统一的圆角矩形形状。
- MacOS 27 (Golden Gate) 的测试版中，Apple 改进了第一方应用图标的清晰度，去除了 Liquid Glass 的多余效果。
- 强制统一图标形状导致应用图标失去辨识度，颜色成为区分应用的唯一视觉线索。
- 对色觉障碍用户和使用相似配色方案的应用（如 Slack 和 Photos），仅靠颜色区分效果不佳。
- 作者提交了反馈 FB23388490，要求 Apple 取消对第三方应用图标形状的限制。
extract_result: success
---

### Apple should end their prohibition on shapes in MacOS app icons

Posted By Paul Kafasis on June 26th, 2026

With last year’s release of MacOS 26 (Tahoe), Apple made a mess of app icons. In the first betas of MacOS 27 (Golden Gate), however, there are signs of a turnaround. We’re urging Apple to continue making improvements, by restoring the ability for MacOS app icons to have distinct shapes.

### Apple’s Liquid Glass App Icons

In Tahoe, Apple modified the icons for dozens of their first-party apps to give them a “Liquid Glass” appearance. The changes were a substantial regression, leading to blurry, dumbed-down icons.

With the recently unveiled Golden Gate, Apple has again updated their MacOS app icons. This time, however, the changes are genuine improvements. Here’s the refined Automator icon, for example:

The newer icon is sharper, with superfluous Liquid Glass removed. Dozens of Apple’s apps have seen similar updates. The result is that Golden Gate’s icons are superior to Tahoe’s, as this comparison from Basic Apple Guy shows. Seeing these improvements led me to think about another fix Apple should make in MacOS.

### The Problem of Tahoe’s Dictated Squircles

With the Tahoe release, Apple didn’t just mess with their own icons. They also dictated the shape of every third-party app icon, forcing them to adopt the same prescribed squircle. Any icon that failed to do so found itself shrunk down and imprisoned in an ugly gray background, in order to fit Apple’s desired aesthetic.

To avoid this icon jail, developers were forced to redesign their icons to match Apple’s preferred form. After decades of beautiful, memorable Mac icons in varying shapes, Tahoe flattened personality to obtain bland uniformity. The platform is worse for it.

Past icons weren’t just more expressive. They were also more usable. Having distinct shapes provided a useful way to tell icons apart. Tahoe eliminates that cue by forcing everything into the same squircle, leaving color as the primary way to tell icons apart at a glance.

That falls down if you’ve got color vision deficiency, or even just multiple icons with similar color schemes.1 I’m looking at you, Slack and Photos. I have to look closely, because it’s so difficult to tell you apart now.

### It Doesn’t Have to Be Like This

Apple’s prohibition on shapes is a step backward for both usability and creativity in app icons. Icons are now harder to distinguish because they’re no longer allowed to be distinctive. But there’s no technical reason for it. Apple could, and should, once again allow icons to take on a wide variety of shapes.

It’s clear that some people within Apple recognize that the transition to Liquid Glass introduced mistakes. They also appear to have the authority to fix those mistakes. Refinements to Apple’s own icons in Golden Gate are a welcome course correction, as is the much-celebrated Liquid Glass opacity slider. It’s time to correct the mistake of banning icon shapes as well.2

Apple should stop forcing every icon into the same squircle. Let’s return to a world of gorgeous app icons like these:

Free the icons.

Footnotes:

-
With color now so critical to tell icons apart, it should be no surprise that the new “Clear” and “Tinted” icon styles added in Tahoe are seeing so little uptake. As Adam Engst noted, “[I]t’s nearly impossible to identify a particular app when they’re all clear or tinted squircles, as you can see below. My brain just shuts down when it sees them.”

I’m not sure this “Tinted” style would be a good idea even if these icons had distinct shapes, but I know it’s a very bad one given their uniformity. ↩︎

-
For folks within Apple, this was feedback filed as FB23388490 (“Third-Party App Icons Should Not Be Restricted to Apple’s Dictated Squircle Shape”). I imagine it is a duplicate many times over. ↩︎