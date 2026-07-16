---
title: 'Stop Using If-Else Chains: Use the Registry Pattern in Python Instead'
source: https://www.kdnuggets.com/stop-using-if-else-chains-use-the-registry-pattern-in-python-instead
author:
- '[[Kanwal Mehreen]]'
published: '2026-07-15'
created: '2026-07-16'
manifest_dates:
- '2026-07-16'
description: Learn a cleaner, more extensible way to dispatch logic in Python.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: eb6fa8f8e9eaba1d
source_type: news_media
tldr: 本文讲解如何用注册表模式（Registry Pattern）替代 Python 中的长 if-else 链，通过字典查找和解耦注册机制实现 O(1) 分发、开闭原则兼容和外部可扩展性，并演示了从手写字典到装饰器注册的演进路径。
objective_summary: KDnuggets 发布了一篇技术教程，指出 if-else 链违反开闭原则、将无关逻辑耦合在一起、随分支增多认知负担加重且无法从外部扩展。文章提出了注册表模式作为替代方案：先通过字典查找替换条件链实现
  O(1) 分发，再进一步演进为装饰器驱动的自动注册，让每个函数或类在自己定义处声明注册键，最终实现无需修改分发器即可添加新类型的效果。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - KDnuggets
  technologies:
  - Python
  - LogisticRegression
  - RandomForestClassifier
  - SVC
  - XGBClassifier
  - Registry Pattern
  key_people: []
key_logic_flow:
- 长 if-else 链违反开闭原则，每次新增分支都需要修改已有函数的中央调度逻辑，增加了回归风险。
- 条件分支将多个无关领域（如信用卡、PayPal、加密货币支付）强行耦合到同一个函数中，导致逻辑混杂。
- 随着分支数量增加，阅读和调试整个函数的认知负担线性增长。
- 硬编码的分发器无法从外部扩展，库的使用者无法添加自己的处理逻辑而不使用猴子补丁或 fork。
- 注册表模式的核心思想是用字典作为中央查找表，将键映射到函数、类或实例，各组件自行注册而不是被硬编码到条件中。
- 最小化实现是将 if-else 链替换为字典查找（O(1) 分发），进阶方案是用装饰器让每个函数或类在其定义处声明自己的注册键，实现被动注册。
object_mentions: []
extract_result: success
---

# Stop Using If-Else Chains: Use the Registry Pattern in Python Instead

Learn a cleaner, more extensible way to dispatch logic in Python.



## # Introduction


Every Python codebase has this problem. A function that starts small. Two branches, maybe three. Then someone adds a case, someone else adds another, and a year later you've got 200 lines of `if/elif/else`

that nobody wants to touch. Here's an example:

```
def get_model(name):
if name == "logreg":
return LogisticRegression()
elif name == "random_forest":
return RandomForestClassifier()
elif name == "svm":
return SVC()
elif name == "xgboost":
return XGBClassifier()
# ... 15 more branches
else:
raise ValueError(f"Unknown model: {name}")
```



And yeah, it works. But it also breaks the **Open/Closed Principle**, which states that software entities (classes, modules, and functions) should be open for extension but closed for modification. There is a better way to handle this problem: the **registry pattern**. This article covers what the registry pattern is, how to build it up from a five-line dictionary to a production-grade reusable class, and when it actually earns its place in your code. So, let's get started.


## # The Problem With If-Else Chains


A long conditional chain fails in a few specific ways:

**It violates the Open/Closed Principle.**New case, new edit to a function that already worked. Yesterday's tested code gets cracked open, retested, and reviewed again. The unit of change should be "add a file," not "modify the central dispatcher."**It piles unrelated logic into one place.**Say your payment dispatcher covers credit cards, PayPal, and crypto. Now three domains that have nothing to do with each other are sharing one function. The`elif`

ladder forces them to share a room anyway.**It scales badly.**Every new branch adds to the cognitive weight of the whole function. Twenty branches is twenty things to scroll past every time you are debugging branch number three.**It cannot be extended from outside.**Ship a library with a hardcoded`get_model()`

chain and your users are stuck. They cannot add their own model without monkey-patching or forking. The logic is sealed shut.

The registry pattern fixes all four by flipping the relationship. Instead of the dispatcher knowing about every option, each option announces itself to the dispatcher.

**What is the registry pattern?**

It is basically a central lookup table that maps keys to objects (functions, classes, instances), where each object registers itself instead of being hardcoded into some conditional. In Python, that lookup table is almost always a dictionary, and "registering" is usually done with a decorator.


## # Going From If-Else to a Dictionary


The smallest possible win is to swap the chain for a dictionary lookup. One step, and the linear scan is gone:

```
MODEL_REGISTRY = {
"logreg": LogisticRegression,
"random_forest": RandomForestClassifier,
"svm": SVC,
"xgboost": XGBClassifier,
}
def get_model(name):
try:
return MODEL_REGISTRY[name]
except KeyError:
raise ValueError(
f"Unknown model: {name!r}. "
f"Available: {list(MODEL_REGISTRY)}"
) from None
```



This is already a registry — just a hand-maintained one. Dispatch is O(1), the options are introspectable with `list(MODEL_REGISTRY)`

, and the dispatcher never changes. One wart remains: every new model still means editing the dict and importing its class at the top of the file. You can do better by letting each component register itself.


## # Building a Decorator-Based Registry


This is the version you'll actually use day to day. Registration happens in a decorator, so every function or class declares its own key right where it is defined: