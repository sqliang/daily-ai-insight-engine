# Correctness Review Checklist

## Data Flow

- [ ] Are function parameters validated before use?
- [ ] Are return values checked (especially None/null)?
- [ ] Is data transformed correctly across layers (API → schema → storage)?
- [ ] Are type conversions safe (no lossy casts, implicit truncation)?

## Error Handling

- [ ] Are exceptions caught at the right level (not too broad, not too narrow)?
- [ ] Do error responses leak internal state (stack traces, file paths)?
- [ ] Are retryable errors distinguished from non-retryable?
- [ ] Is there a fallback when external services (LLM, DB) are unavailable?
- [ ] Are async tasks properly awaited or cancelled on error?

## Edge Cases

- [ ] Empty input (null, empty string, empty list)
- [ ] Very large input (oversized image, long text, many items)
- [ ] Unicode / special characters in user input
- [ ] Concurrent requests on shared state
- [ ] Timeout / slow response from external APIs

## Logic Correctness

- [ ] Are conditions correct (off-by-one, inverted boolean)?
- [ ] Are loops guaranteed to terminate?
- [ ] Is shared mutable state properly synchronized?
- [ ] Are regex patterns correct (no catastrophic backtracking)?
- [ ] Are date/time calculations timezone-aware?

## Database

- [ ] Are SQL queries using parameterized statements (no string concatenation)?
- [ ] Are transactions used for multi-step writes?
- [ ] Are schema migrations backward-compatible?
- [ ] Are indices needed for new query patterns?

## Common Python Pitfalls

- [ ] Mutable default arguments (`def f(x=[])`)
- [ ] Late binding closures in loops
- [ ] Module-level mutable state without synchronization
- [ ] `except:` without specifying exception type
- [ ] `if x is None` vs `if not x` confusion

## Common Swift Pitfalls

- [ ] Force unwrapping optional (`!`) without guard
- [ ] Retain cycles in closures (capture self strongly)
- [ ] `@Published` updates on background thread
- [ ] Unhandled async task cancellation
- [ ] Core Data thread confinement violations
