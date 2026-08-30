---
title: Ben's session
source: https://www.bensbites.com/p/bens-session
author: []
published: '2026-08-07'
created: '2026-08-08'
manifest_dates:
- '2026-08-08'
- '2026-08-09'
- '2026-08-10'
description: Field notes from my agent activity
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: ccb81ea8cc6ce5fe
---

# Ben's session

### Field notes from my agent activity

Hello again :)

I’m trying something new - this email walks through one of my actual agent sessions and I’ll explain what’s happening along the way. The build or task I’m doing isn’t important. But I’m looking at how I could be using agents more effectively.

You might pick up a thing or two, I’m finding it helpful to solidify my own learning.

Please comment what you thought of this, was it helpful? anything unclear? want to see other things?

### What I was trying to do

I was setting up a bookable appointment link in Google Calendar and got annoyed that you can’t just drag time slots on the calendar grid, you have to type each date and time range into a clunky form. I wanted something that would let me drag slots directly on the week view and have the form update automatically.

So I fired up ChatGPT (I use Codex mode but works in ‘Work’ or Claude Cowork etc). I wanted to test Luna on Max reasoning as the price has been cut 80% and people have been saying how great it is to use.

It’s not the best prompt, I’ll admit.

But it gives the agent enough understanding of what I want so it can explore options. Plus a screenshot so it knew what screen I was on about.

This kicks off the ‘agent loop’. The agent thinks about what to do (what can be done with Google Calendar), then acts by using a tool (in this instance, web search) to gather context on how to solve my task.

The websites it read are now in the context window. I didn’t look at them so I have no idea what info it found or if its true. All the text it read is now in its ‘memory’.

Imagine 20 websites went in, there could be wrong or contradictory info that could mislead the agent. This is why you hear so much talk about context. It’s important, and you want it to be full of the best possible information.


Agents often do many loops for a task. They’re ‘go-getters’ by nature. Which is why they need babysitting.

They keep looping, gathering more context until they have what they need to complete the task. For my fantastic prompt, 55 seconds and 2 web searches was enough.

### Build it

The agent came back with a mini plan. I skimmed it, as usual (which cost me...).

I overlooked one point which was not how I wanted the extension to work, it should create the times automatically in the form as you drag tiles, not manually click to sync.

**What I should’ve done** is gone back and forth to ask how things would work, maybe mockup some wireframes I could annotate with feedback.

But I didn’t.

I just said build it...

It cycled through it’s loops and it was built!

Ha, not quite.

My first thought here was:

I shouldn’t need to install this myself

If its not installed, the agent can’t have tested this live

Why did I just say ‘build it’!?


The agent has tools it could’ve used when looping over the task, specifically Computer use and Browser use. It could’ve installed it and tested it live on my actual calendar page.

It didn’t, so I knew there’d be hiccups.

I installed it and tried dragging time frames but the form syncing didn’t work (shock).

**What I should’ve done** is say something like

“build it. install the extension in chrome, open a google calendar booking form and test it end to end. test multiple days/weeks, merging selections and check that the form updates correctly. iterate and keep testing until it works”.

That would’ve saved me time and tokens...

I went through my frustration escalation.

I start by typing the issues I run into.

14 minutes later still had issues. I moved to stage 2 - voice ramble and a screenshot.

61 (!!) minutes later still had issues. I moved to stage 3 - I record my screen with a voiceover, pointing my cursor at moments with issues. Agents can break videos down frame by frame and transcribe to pinpoint what you’re talking about.


Each turn (back-and-forth) the context gets fuller. After the first set of issues I sent it, it started actually using Chrome to test, thankfully.

But from reading it’s thinking, it didn’t test fully as it didn’t want to override my ‘work’ but that page was for the agent to absolutely use, that’s kind of key to test if this thing worked properly.

So on the second attempt at fixes I rambled a voice note and added a screenshot. This time I added things it should check and tests it should do.

This is that verification layer an agent considers when it’s thinking about the task being complete. Do all the tests (that the agent comes up with) pass with no issues = extension works.

When giving an agent a task, you should think about what criteria would mean this task is ‘done’. For a website it could be that all the content is formatted well with spacing, your design system, and works on mobile. For email triaging it could be that all the emails in your inbox have a label and are moved to the correct folder.

Verification is something I’m still working on as a lot of my tasks are not code.