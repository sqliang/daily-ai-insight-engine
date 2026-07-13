# Performance Review Checklist

## I/O Patterns

- [ ] Are there N+1 query patterns (fetching in a loop instead of batching)?
- [ ] Are DB connections properly pooled and released?
- [ ] Are file reads/writes buffered (not byte-by-byte)?
- [ ] Are large responses streamed (not loaded entirely into memory)?

## Network Calls

- [ ] Are external API calls made concurrently where possible (`asyncio.gather`)?
- [ ] Are HTTP connections reused (not creating a new client per request)?
- [ ] Is there appropriate timeout configuration on external calls?
- [ ] Are retries using exponential backoff?

## Memory

- [ ] Are large objects (base64 strings, JSON payloads) held longer than needed?
- [ ] Are there potential memory leaks (unbounded caches, growing lists)?
- [ ] Is image data being double-loaded (raw bytes + decoded bitmap)?

## Algorithm Efficiency

- [ ] Are there O(n²) or worse algorithms on potentially large inputs?
- [ ] Could binary search / hash map replace linear scan?
- [ ] Are expensive operations cached when results are stable?

## Python Specific

- [ ] Are list comprehensions / generators used instead of building intermediate lists?
- [ ] Is `async for` used correctly (not accidentally sync)?
- [ ] Are database queries using `LIMIT` / `OFFSET` for pagination?
- [ ] Is `json.loads` called only when needed (not on already-parsed data)?

## iOS Specific

- [ ] Are image operations on background threads?
- [ ] Are large images resized before upload?
- [ ] Is Core Data fetch using batch size / fetch limit?
- [ ] Is the main thread free of blocking I/O?

## SSE Streaming

- [ ] Are SSE events flushed promptly (not buffered)?
- [ ] Is there backpressure handling for slow clients?
- [ ] Are pings sent to keep connections alive?
