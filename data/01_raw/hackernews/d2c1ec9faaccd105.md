---
title: The Economic Benefit of Refactoring
source: https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html
author:
- '[[javaeeeee]]'
published: '2026-07-30'
created: '2026-07-31'
manifest_dates:
- '2026-07-31'
description: 'Article URL: https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html
  Comments URL: https://news.ycombinator.com/item?id=49111176 Points: 235 # Comments:
  100'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: d2c1ec9faaccd105
---

# The Economic Benefit of Refactoring

As part of getting to grips with the new world of agentic engineering, I built an application to support my work. It’s a sophisticated app: high-quality web UI with dynamic refresh and look-up, modals and auto-save, integrations to external systems, machine learning and text analysis, background jobs, and a proper environment setup with fully automated deployment. It’s approximately 150,000 lines of code, primarily in Rust (~120 kLoC) with the remainder in TypeScript and Terraform.

This was entirely written by agents. Mostly Claude Code, and some use of Cursor. I didn’t read or review any of the code, except occasionally, out of interest.

While building the application, I could see some things going awry. After watching an edit to line 4,000 of a file scroll by in the terminal, I had a closer look. The data access layer had grown to over 6,000 lines. As more features landed, this continued to grow. Every query, read or write, repeated the same HTTP request setup, the same JSON encoding and decoding. Eventually, it reached 17,155 lines. In a single Rust file.

## An experiment in refactoring

The 17,155 line file was the entire data access layer. A single, self-contained module. Reviewing the code, there was no de-duplication, no internal language, limited extraction of functions, and very little extraction of classes. It did have a clear boundary with an interface to preserve. It was a great target for refactoring.

The goal of refactoring an agentic code base is to spend tokens now in refactoring to make token consumption for future work lower. An experiment should be able to show that as this file was refactored the token cost of making separate feature implementations in this code base would decrease.

Precisely because agents never learn this was now possible to run as an experiment. I could prompt a fresh agent to make exactly the same change after every refactoring stage. Unlike a human engineer, the experiment would not be tainted by learning from previous steps.

- Create an overall refactoring plan, following strict refactoring discipline.
- Craft a representative change, described in a single prompt.
- Establish a baseline cost of change: in a sub-agent, execute that prompt, including asking the sub-agent to report token consumption.
- Throw away the change.
- In a loop:
- Apply a single step of the overall refactoring.
- In a sub-agent, execute
*exactly*the same change receiving the token cost of the change. - Throw away the change.

- Record all token costs, time to execute the change, and lines of code after each step of the refactoring, including the baseline.

The prompt used for the representative change and the refactoring steps applied are shown in the appendices, below.

One caveat: Claude doesn’t provide reliable methods for counting
tokens live despite showing token counts, reporting tokens consumed
per session, and **billing** for tokens. I’m assuming this is a
temporary issue that will improve over time. Instead, the sub-agent
reported the number of characters received and sent and used
tiktoken to approximate tokens, by dividing character count by
four.

## Results

| Step | Data Access Layer LoC | Largest file LoC | Total Rust LoC | Input tokens per change | Output tokens per change | Time per change (s) |
|---|---|---|---|---|---|---|
| Baseline | 17,155 | 17,155 | 50,359 | 159,564 | 1,705 | 342 |
| Step 1 (FirestoreClient) | 16,706 | 16,706 | 49,910 | 155,205 | 1,723 | 530 |
| Step 2 (extract_doc_id, new_link) | 16,562 | 16,562 | 49,766 | 159,227 | 2,105 | 574 |
| Step 3 (link-query helpers) | 16,567 | 16,567 | 49,771 | 154,054 | 2,105 | 524 |
| Step 4 (FakeStore predicates) | 16,577 | 16,577 | 49,781 | 154,146 | 2,060 | 654 |
| Step 5 (value ctors) | 16,469 | 16,469 | 49,673 | 171,251 | 2,036 | 1,353 |
| Step 6 (FieldsBuilder) | 16,469 | 16,469 | 49,673 | 171,251 | 2,036 | 1,353 |
| Step 7 (queries.rs) | 16,474 | 15,670 | 49,678 | 151,850 | 1,800 | 587 |
| Step 8 (traits.rs) | 16,508 | 13,845 | 49,712 | 132,558 | 1,723 | 446 |
| Step 9 (traits/ split) | 16,508 | 13,845 | 49,712 | 132,558 | 1,723 | 446 |
| Step 10 (codec.rs) | 16,521 | 12,846 | 49,725 | 131,871 | 1,750 | 540 |
| Step 11 (fake_store.rs) | 16,535 | 11,122 | 49,739 | 133,016 | 2,460 | 600 |
| Step 12 (store/ split) | 16,550 | 9,269 | 49,754 | 104,080 | 2,050 | 490 |
| Step 13 (co-locate tests) | 16,550 | 9,269 | 49,754 | 104,080 | 2,050 | 490 |
| Step 14 (complete fake_store.rs) | 16,553 | 7,225 | 49,757 | 107,205 | 2,453 | 523 |
| Step 15 (store/ split) | 16,608 | 3,695 | 49,812 | 27,360 | 2,113 | 454 |

The interesting metrics here are the total lines of code in the data
access layer, the total lines of code in the *largest single file* in
the data access layer and the input tokens consumed while producing
the change.

This chart shows four things. The first point is the baseline, step 0,
and then the same metrics are repeated *after* each refactoring step
has been applied.

- The total lines of code in the data access layer as a whole. Initially, this is just the single file I started with. This becomes many files as refactorings are applied. By the end there are 19 Rust files.
- The lines of code in the single largest file in the data access layer. This started as the entirety of the data layer in the single initial file. By the end, the single largest file is a test library. Further refactoring passes could apply the same approach to this.
- The total input tokens consumed by the sub-agent while applying the representative change.
- The total output tokens produced by the sub-agent while applying the representative change.

## Refactoring reduces token consumption

The results are clear. Input tokens stay fairly flat until the largest file starts to fall, and then they drop before, in the words of Claude, falling off a cliff.

Between the base line and the final refactoring, input tokens for the
same task reduced from **159,564** to **27,360**. A saving of
**132,204** tokens, or **83%**. And that saving is not a one-off. Every single
change that touches the data access layer from this point forward now
costs significantly less.

How much of a saving? Assuming Sonnet 5 pricing at the time of writing
of $3/MTok, 39.7 cents. Not a lot. Does it multiply? How will this
play out across debugging? More complicated features? This is
refactoring only one portion of the code base, can the whole code base
be aggressively refactored to find savings everywhere? How much would
those refactorings *cost?*

This saving is because the agent has to read less code. But it is not because there is less code to read. The overall code in the data access layer as a whole has stayed fairly constant. Therefore to be able to bank this saving, the agent must be able to successfully identify the smallest subset of files necessary to read. The results make it appear this was happening. Reading the Claude Code thinking output and file read summaries as the change was being applied also indicates the sub-agent was successfully reading smaller and smaller sections of code each time.

In other words, randomly cutting the file into smaller files is unlikely to help as much: even if each file were smaller, the agent would be forced to read through many files looking for the relevant code. While the step with the biggest effect happens at the end, the previous steps were refactorings to set up this saving. This was not planned. It was simply a result of how refactoring typically proceeds: local file changes to extract duplication, before breaking down into smaller files once a repeating core emerges.

The refactoring did not make the representative change smaller. The number of tokens produced when writing code was largely unaffected: the output tokens do not move very much. Those tokens are five times the price of the input tokens. But, there are a lot less of them. Are there refactorings that could be applied to reduce output token production? I need a more complex sample change to explore these questions. The noise of the non-deterministic code generation process is hiding any variance caused by changes in the factoring of the code.

## Notes on the process

Claude was not good at refactoring. If you read the prompt and the refactoring steps below, it’s clear that the refactorings produced were directly in response to the prompt. Claude is unable to look at code, look at refactorings in general and work out which are suitable to apply: a human needs to actively guide it. This marries with wider experience in this app. The development harness includes an explicit refactoring step. That refactoring step did not prompt Claude into improving this file. More anecdotally, Claude.ai was better than Claude Code. I used both interfaces to create the refactoring plan. Claude Code spotted extract function as the first step. Claude.ai went further and saw an entire client class to be extracted.

It was also bad at applying them. The mechanical act of refactoring was performed by writing Python scripts using grep and sed. These scripts frequently got confused by indentation. Oh, the irony. In addition, the single most valuable refactoring was missed in the first pass, and had to be re-applied as a follow-up step. This is why the number of steps in the figure don’t match the refactoring steps in the appendix.

It took about eight hours to complete the entire experiment. This was mostly unattended. The only intervention was after six hours 40 minutes when it appeared to have finished, but had skipped that step and needed to be redirected. This experiment was running on slow hotel WiFi. I wondered if that contributed to time taken. But on deeper analysis of the code base, the cargo temporary build cache had become very large. Test execution was suffering, significantly.

## Further work and broader implications

Unfortunately, it didn’t occur to me to perform a count of the tokens required to create and execute the refactoring plan until it was already complete. I’ve looked at my aggregate consumption across the time window where I was doing this work, including designing and running the experiment. I can’t say how many tokens were required to perform the refactoring. The upper bound is five million, however. This includes creating the refactoring plan twice, the work to design the experiment including the representative change, and various other tasks. Future work should include a more accurate count of tokens consumed to refactor.

This is just one experiment, on a significant application that is still greenfield and built and maintained by a single developer. But, I believe this is a potentially interesting first step. This effort shows the value, in time and money of refactoring. As well as measuring how expensive refactoring is. It would be interesting to look at more complex changes, at wider refactoring, refactoring continuously, and even the relative value of different refactoring approaches.

This is just the beginning.

## Appendices

*Note: These appendices include the prompts that I used, and the
output that was returned. The only editing applied has been to remove
the specific code changes to be made. These are included without
editing to show how the agents were directed. There are no hidden
tricks. As such, there is some language in here that might be
confusing. The error is in the original.*

## The representative change

This is the recorded prompt that was fed to each sub-agent, there was no further context supplied other than the code base and accompanying architecture documentation. Every sub-agent was starting with exactly the same information.

You are working in the Rust project at

`~/dev/your-project-name`

.Add a new

`ItemWatchStore`

public async trait to the Firestore layer, following existing patterns exactly. The trait must have three methods:

`async fn watch_item(&self, item_id: &str, user_id: &str) -> Result<()>`

`async fn unwatch_item(&self, item_id: &str, user_id: &str) -> Result<()>`

`async fn watched_items_for_user(&self, user_id: &str) -> Result<Vec<String>>`

Watches are stored in a

`item_watches`

Firestore collection. Each document has fields:`itemId`

(string),`userId`

(string),`createdAt`

(timestamp). There is no Rust struct for a watch record — the methods return`Vec<String>`

(item ids).Implement the trait for both

`FakeStore`

(using an in-memory`Vec<(String, String)>`

field added to`FakeStoreInner`

) and`FirestoreStore`

(using the same HTTP patterns used for other store impls in this file).

At the very end of your response, output exactly this JSON block (fill in real values):`{ "files_read": [ {"path": "src/firestore.rs", "chars": 123456}, ... ], "response_chars": 7890 }`

Do NOT commit the change. Stop after writing the code.


## Refactoring steps

This is the prompt that was used to create the refactoring plan.

Following the strict definition that a refactoring is a provably correctness preserving series of code edits, and using Martin Fowler’s 2nd edition of Refactoring as the source, examine @src/firestore.rs. This is a 17K LoC Rust file. No file should be that long. It is almost certainly not using an internal language to build and manage queries. Produce and describe, but don’t execute, a sequence of refactorings that would massively reduce the line count of that file, without changing the interface at all.


Following is the description of the refactorings applied, extracted from the plan built and followed by Claude. The actual plan includes predicted code changes. For each refactoring, the individual steps to follow were listed. Each of those steps was individually testable, and was individually tested. This is a stricter refactoring than most human engineers would follow.

The steps listed here don’t line up directly with the measured changes above as Claude skipped the most valuable single refactoring (splitting out the store into sub-files) on the first pass and had to complete that afterwards as two additional steps.

#### Step 1 — Extract Class: `FirestoreClient`

(Fowler §7.5) + Extract Function × 4 (Fowler §6.1)

**Fowler ref:** *Extract Class* (7.5); *Extract Function* (6.1) for
each primitive

`FirestoreStore`

currently conflates two responsibilities:

**Domain query orchestration**— which query to run, which documents to write, how to parse results into domain types**Firestore HTTP transport**— auth headers, URL construction, JSON encoding/decoding of Firestore wire types, retry-on-PRECONDITION_FAILED

Fowler §7.5 calls for extracting a new class when you can identify a
coherent subset of a class’s data and behaviour. The transport
responsibility owns: `client: reqwest::Client`

, `project_id: String`

,
`MetadataAuth`

, and `documents_url()`

/ `auth_header()`

. Extract these
into a new `FirestoreClient`

struct.

**Estimated savings: ~1,200 lines in FirestoreStore impls;
FirestoreClient adds ~120 lines net.**


#### Step 2 — Extract Function: `extract_doc_id`

and `new_link`

(Fowler §6.1)

**Fowler ref:** *Extract Function* (6.1)

-
— The expression`extract_doc_id`

`doc.name.rsplit('/').next()?.to_string()`

appears verbatim at the start of all 20`parse_*_document`

functions. Extract it. -
— Building a`new_link`

`Link`

struct with`metadata: HashMap::new()`

and`provenance: None`

and a fresh UUID appears 62 times. Extract a factory function.

**Estimated savings: ~500 lines** (62 × ~10-line structs → 62 ×
~2-line calls; 20 parse functions each lose 1 line of boilerplate).

#### Step 3 — Extract Function: link-query pipeline helpers (Fowler §6.1)

**Fowler ref:** *Extract Function* (6.1)

Two sub-patterns recur inside the `FirestoreStore`

trait impls after running a link query:

-
**Pattern A — collect all link documents from query rows (~15 sites).** -
**Pattern B — query links and return exactly one target ID, error if missing (~8 sites):**

**Estimated savings: ~200 lines.**

#### Step 4 — Extract Function: FakeStore link predicates on `FakeStoreInner`

(Fowler §6.1)

**Fowler ref:** *Extract Function* (6.1)

Inside the FakeStore impls, ~15 methods repeat variations of
`inner.links.iter()...`

.

Extract two methods on `FakeStoreInner`

. The 15 callsites then become
single-line. Methods that additionally filter by a second predicate
(e.g. also checking `to_kind`

) chain `.into_iter().filter(…)`

on the
result of the helper.

**Estimated savings: ~120 lines.**

#### Step 5 — Replace Inline Code with Function Call × 4: Firestore value constructors

**Fowler ref:** *Replace Inline Code with Function Call* (8.5)

Add four private free functions (file-level, not methods) before the
codec block. Replace all 128+ `json!({"stringValue": …})`

/
`json!({"timestampValue": …})`

etc. inline expressions with calls to
these functions. Each multi-word json macro call becomes a single
short call.

**Estimated savings: ~80 lines (mostly from multi-line json macros collapsing to one-liners).**

#### Step 6 — Extract Class: `FieldsBuilder`

(Fowler §7.3)

**Fowler ref:** *Extract Class* (7.3)

The ~20 encoder functions all follow this shape:

```
let mut fields = serde_json::Map::new();
fields.insert("foo".to_string(), str_val(&x.foo));
fields.insert("bar".to_string(), ts_val(x.bar));
json!({"name": path, "fields": fields})
```


Extract a small builder. Rewrite each encoder function to use the builder. A ~40-line encoder shrinks to ~12 lines.

**Estimated savings: ~500–600 lines across the 20 encoder functions.**

#### Step 7 — Move Function: extract `src/firestore/queries.rs`


**Fowler ref:** *Move Function* (8.1)

Convert `src/firestore.rs`

to a module directory: rename to
`src/firestore/mod.rs`

. Then create `src/firestore/queries.rs`

and
move all 32 `LinkQuery`

constants and the
`LinkQuery`

/`EqFilter`

/`EqValue`

/`Ordering`

/`Direction`

type
definitions into it. Add `pub(super) use queries::*;`

in `mod.rs`

.

No behaviour changes; all callsites already reference names that were in scope via the flat file.

**Reduces mod.rs by ~800 lines.**

#### Step 8 — Move Function: extract `src/firestore/traits.rs`


**Fowler ref:** *Move Function* (8.1)

Move all 17 `pub trait`

definitions (and their associated error types)
to `src/firestore/traits.rs`

. Re-export them from `mod.rs`

with ```
pub
use traits::*;
```

.

**Reduces mod.rs by ~1,900 lines. Produces a ~1,900-line traits.rs
that needs further decomposition.**


#### Step 9 — Move Function: split `traits.rs`

into a `traits/`

module directory

**Fowler ref:** *Move Function* (8.1)

Convert `src/firestore/traits.rs`

to a module directory by grouping the 17 traits into four domain-aligned files:

| File | Traits | Approx lines |
|---|---|---|
`traits/planning.rs` |
`ConcentrationStore` , `GoalStore` , `ItemStore` , `NoteStore` , `PursuitStore` , `FocusPassStore` |
~650 |
`traits/content.rs` |
`CaptureStore` , `TagStore` , `UrlReferenceStore` , `DocumentStore` , `PaperStore` |
~550 |
`traits/people.rs` |
`ThoughtworkerStore` , `ExternalContactStore` , `CompanyStore` |
~300 |
`traits/system.rs` |
`SessionState` , `LinkStore` , `SuggestionStore` , `SuggestionVetoStore` , `OAuthTokenStore` , `MigrationLedger` , `EmbeddingStore` , `RuntimeConfigStore` , `SalesforceSyncStateStore` |
~400 |

`traits/mod.rs`

becomes a pure re-export file (~20 lines). Associated
error types (`FocusPassError`

, `SuggestionDecisionError`

, etc.) move
with the trait that produces them.

**No trait definition changes, no callsite changes — only
relocation. Each resulting file is 300–650 lines.**

#### Step 10 — Move Function: extract `src/firestore/codec.rs`


**Fowler ref:** *Move Function* (8.1)

Move all document encoder/decoder functions (`*_document`

,
`parse_*_document`

, `kind_str`

, `parse_kind`

, `parse_capture_source`

,
`parse_outcome`

, etc.) plus `FieldsBuilder`

and the value constructors
from Steps 5 and 6 into `src/firestore/codec.rs`

. Make them
`pub(super)`

.

After Step 6 this module will be ~400–500 lines rather than ~1,200.

**Reduces mod.rs by ~500 lines (post-Step-6).**

#### Step 11 — Move Function: extract `src/firestore/fake_store.rs`


**Fowler ref:** *Move Function* (8.1)

Move `FakeStore`

, `FakeStoreInner`

, and all 18 trait impl blocks for
`FakeStore`

into `src/firestore/fake_store.rs`

. Re-export `FakeStore`

from `mod.rs`

with `pub use fake_store::FakeStore;`

.

`FakeStoreInner`

and helper methods stay private to the module.

**Reduces mod.rs by ~4,700 lines.**

#### Step 12 — Move Function: split `FirestoreStore`

impls into per-trait files under `src/firestore/store/`


**Fowler ref:** *Move Function* (8.1)

Create `src/firestore/store/mod.rs`

with `FirestoreStore`

struct
definition, `impl FirestoreStore`

(constructor + `FirestoreClient`

from Step 1), and `MetadataAuth`

.

Then create one file per logical domain grouping.

Each file contains only `use super::*;`

(or explicit imports) and the
trait impl block(s). No type definitions, no helpers. Helpers used by
multiple impl blocks stay in `store/mod.rs`

.

**Reduces what would be a ~10,000-line file into ten files of 120–650
lines each. mod.rs becomes a ~100-line re-export manifest.**

#### Step 13 — Move Function: co-locate tests with their modules

**Fowler ref:** *Move Function* (8.1)

The existing `#[cfg(test)]`

modules test specific domain areas and
belong with the modules created in Step 12 rather than in a single
`tests.rs`

.Each test module moves inside a ```
#[cfg(test)] mod tests { …
}
```

block at the bottom of the target file, with `use super::*;`

to
access the module’s internals. No test is changed, only relocated.

Any shared test fixtures (`FakeStore::new`

, helper builders) that are
already in `fake_store.rs`

are accessible via the existing ```
use
super::fake_store::FakeStore
```

import chain.

**Reduces mod.rs by ~2,000 lines; each target file gains 200–700
lines of tests that are directly adjacent to the code they exercise.**