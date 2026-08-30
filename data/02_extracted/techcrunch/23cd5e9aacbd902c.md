---
title: How to tell if your AI platforms’ accounts have been hacked
source: https://techcrunch.com/2026/08/15/how-to-tell-if-your-ai-platforms-accounts-have-been-hacked/
author:
- '[[Lorenzo Franceschi-Bicchierai]]'
published: '2026-08-15'
created: '2026-08-16'
manifest_dates:
- '2026-08-16'
- '2026-08-17'
description: A guide on how to check if hackers have broken into your accounts on
  the most popular AI platforms.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 23cd5e9aacbd902c
source_type: news_media
tldr: TechCrunch 发布安全指南，教用户如何检查 ChatGPT、Claude、Perplexity 三个 AI 平台账户是否被黑客入侵，包括查看活动会话、单独或全部登出设备、重置密码等具体操作步骤。
objective_summary: TechCrunch 于 2026 年 8 月发布指南文章，介绍如何判断 AI 平台账户是否被黑客入侵，并建议使用密码管理器与开启多因素认证。ChatGPT
  和 Perplexity 支持多因素认证，而 Claude 使用邮件登录链接代替密码。文章分别给出三个平台检查可疑登录设备的方法：ChatGPT 可在 Security
  and Login 中查看活动会话并重置密码，Claude 可在账户设置中终止可疑会话且无密码可修改，Perplexity 因不显示登录位置只能通过退出所有会话应对风险。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - TechCrunch
  - OpenAI
  - Anthropic
  - Perplexity
  technologies:
  - MFA
  key_people: []
key_logic_flow:
- TechCrunch 发布指南，指出黑客可像攻击其他在线服务一样入侵 ChatGPT、Claude 和 Perplexity 等 AI 平台账户，并建议使用唯一密码与开启多因素认证（MFA）。
- ChatGPT 和 Perplexity 支持多因素认证，而 Claude 不使用密码，而是通过向用户邮箱发送登录链接来验证身份。
- ChatGPT 用户可通过 Settings 中的 Security and Login 查看 Active Sessions 登录设备，对不认识的设备可单独登出或点击
  Log out all，并可通过邮箱验证码重置密码。
- Claude 用户可在 Settings 的 Account 中查看 Active sessions，对可疑会话选择 Log out 或 Terminate，也可登出所有设备，但因无密码机制无法修改密码。
- Perplexity 不显示用户的登录位置，用户只能进入 All settings 点击 Sign out of all sessions 并确认，强制登出所有会话以应对潜在的账户入侵。
object_mentions:
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: https://chatgpt.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ChatGPT 用户可在账户设置的 Security and Login 页面查看 Active Sessions 登录设备列表，对不认识的设备可单独登出或一键退出全部会话。
  - ChatGPT 支持多因素认证，用户可在忘记密码时通过邮箱接收六位验证码并设置新密码。
  article_id: 23cd5e9aacbd902c
- object_type: product
  name: Claude
  canonical_name: Claude
  url: https://claude.ai
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Claude 不使用密码，而是通过向用户邮箱发送登录链接完成身份验证，用户可在账户设置的 Active sessions 中终止可疑会话或登出所有设备。
  - Claude 因完全采用邮件链接登录机制，没有可修改的密码。
  article_id: 23cd5e9aacbd902c
- object_type: product
  name: Perplexity
  canonical_name: Perplexity
  url: https://www.perplexity.ai
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Perplexity 不显示用户的当前登录位置，若怀疑账户被入侵，用户只能进入 All settings 点击 Sign out of all sessions
    并确认，强制退出所有会话。
  - Perplexity 作为 AI 驱动的搜索引擎支持多因素认证以保护账户安全。
  article_id: 23cd5e9aacbd902c
extract_result: success
---

Just like any other online service, hackers can target and break into your accounts on popular AI platforms such as ChatGPT, Claude, and Perplexity.

TechCrunch has created a comprehensive guide to help you protect yourself if you suspect someone has broken into your account on one of the internet’s most popular platforms, social networks, or messaging apps. Now, we’re here to show you how to check whether your accounts on AI platforms have been hacked.

As usual, we recommend using unique passwords stored in a password manager, and turning on multi-factor authentication (MFA), so that even if someone steals your password, they won’t be able to log in without that second piece of information.

ChatGPT and Perplexity offer MFA. Claude doesn’t, because instead of asking for a password, Anthropic’s AI chatbot sends a login link to your email address.

All three of these AI platforms offer similar ways to check if there’s a suspicious device logged into your account. Here’s exactly how each platform works.

**ChatGPT**

To find out if someone has broken into your ChatGPT account, open it on your computer’s browser, click on your username in the bottom left corner, go to “Settings,” then “Security and Login,” and finally click on “Active Sessions.”

You will see where you are logged into your ChatGPT account. If you see any device you don’t recognize, you can log out of that single device. You can also click on “Log out all.”

At this point, if you want to change your password, you need to log out of your account.

Then, on ChatGPT’s website, click “Log in” located in the bottom-left corner, enter your email address, click on “Forgot password,” and then “Continue.”

ChatGPT will then send you an email containing a six-digit code. Enter the code on the ChatGPT login page, click “Continue,” and then enter a new password.

You can also click “reset your password” in the email you received to see the official instructions on how to do that.

**Claude**

For Claude, open it in your computer’s browser, click on your username in the bottom-left corner, then “Settings,” and click on “Account.” That’s where you will see your “Active sessions.”

If you don’t recognize one of them, hover over it, click on the three vertical dots that appear on the right, and click “Log out” or “Terminate.”

If you want, you can click on “Log out of all devices.”

At that point, you’ll be able to log back into your account using your email address. You will receive an email with a link to log in. Claude does not allow you to use passwords at all, so there’s no password to change.

**Perplexity**

In the case of Perplexity, the AI-powered search engine does not show you where you are logged in.

So if you’re worried someone may have broken into your account, go to Perplexity in your browser and click your username in the bottom-left corner, then “All settings.” Finally, click on “Sign out of all sessions,” and then “Confirm.”