---
title: Don't Wordle
source: https://dontwordle.com/
author:
- '[[Hbruz0]]'
published: '2026-08-25'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
description: 'Article URL: https://dontwordle.com/ Comments URL: https://news.ycombinator.com/item?id=49432319
  Points: 349 # Comments: 122'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7d7b26ea8e4bd4de
source_type: community_discussion
tldr: Don't Wordle 是一个免费每日谜题游戏，玩法与 Wordle 相反，玩家需要刻意避免猜中隐藏单词，同时被迫遵守已获得的信息线索。页面会显示剩余可用单词数，并提供撤销功能辅助策略调整。
objective_summary: Don't Wordle 是一个免费每日单词谜题游戏，在其官网发布，外观和玩法与 Wordle 相似，但目标完全相反。玩家的目标是刻意不猜中隐藏的五字母单词，每次猜测后字母被标记为绿色、黄色或灰色，同时必须复用绿色和黄色字母。游戏在页面顶部显示剩余可用单词数，并支持撤销操作。文章还介绍了包括
  Purist 在内的多种玩法策略。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies: []
  technologies: []
  key_people: []
key_logic_flow:
- Don't Wordle 是一个免费每日谜题游戏，外观和玩法与 Wordle 相似，但目标从猜中隐藏单词反转为刻意不猜中。
- 每次猜测后，字母会像 Wordle 一样被标记为绿色、黄色或灰色，玩家必须尊重此前获得的信息，在正确位置复用绿色字母并在新位置复用黄色字母。
- 游戏在页面顶部显示剩余可用单词数，该数字会快速下降，数字过低时玩家可以使用撤销功能回退。
- 文章介绍了多种策略：先做几次猜测推导出隐藏词后撤销重置、使用较少见和重复字母的单词保存可用字母，以及不使用撤销且只用常用单词的 Purist 玩法。
- 作者指出，由于规则强迫玩家利用已获得的信息，主动输掉游戏比主动赢得 Wordle 更加困难。
object_mentions:
- object_type: product
  name: Don't Wordle
  canonical_name: Don't Wordle
  url: https://dontwordle.com/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Don't Wordle 是一个免费每日谜题游戏，外观和玩法与 Wordle 相似，但玩家的目标是刻意不猜中隐藏的单词。
  - 游戏在每次猜测后为字母标记绿、黄、灰三种颜色，并在页面顶部显示剩余可用单词数量，数量过低时可用撤销功能回退。
  - 文章介绍了多种策略，包括先推导隐藏词再撤销重置、使用较少见和重复字母的单词，以及不使用撤销的 Purist 玩法。
  article_id: 7d7b26ea8e4bd4de
- object_type: product
  name: Wordle
  canonical_name: Wordle
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在 Wordle 中，玩家的目标是在有限的猜测次数内猜中隐藏的五字母单词，而 Don't Wordle 将这一目标完全反转。
  article_id: 7d7b26ea8e4bd4de
extract_result: success
---

# Welcome to Don’t Wordle

Don’t Wordle is a free daily puzzle with similar appearance and gameplay as Wordle. In Wordle, the goal is to guess the 5 letter hidden word. In Don’t Wordle, the goal is to **not** guess the hidden word. Just like Wordle, after each guess, each letter is labeled as either green (correct letter, correct spot), yellow (correct letter, incorrect spot), or gray (letter not in the word). However, the strategy and feel of the game is completely different to Wordle, and many users find it frustrating. The full rules are explained here.

Wordle is calibrated so that it’s hard to win on the first guess, but the clues usually nudge you toward the answer before you run out of guesses. It’s surprisingly tough to *lose* Wordle if you’re making an honest attempt to try to win. By the same virtue, it is surprisingly difficult to win at Don’t Wordle, because the game forces you to respect the information you have learned in previous guesses (i.e. you must re-use green letters in the same spot, and re-use yellow letters in a new spot) while still avoiding the hidden word. The **valid words remaining** shows at the top of the page to clue you in on how many words you can still play. It’s quite surprising just how quickly the number decreases. If the number gets uncomfortably low, you can use an undo to reverse course.

There are many different strategies for playing Don’t Wordle. The most basic strategy is to make a few guesses to derive the hidden word without accidentally guessing it, then undoing to reset the game and then you can intentionally avoid letters in the hidden word. It’s also very popular to use words with less common and repeat letters to save as many useful letters as possible for the later guesses. However, the "Purist" strategy is to start with a random word, not use any undos, and only use "common" words—that’s closest to the spirit of the game of trying to make an honest attempt to lose at Wordle.