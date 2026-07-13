# Style Review Checklist

## Naming

- [ ] Are names descriptive and unambiguous (not `data`, `tmp`, `obj`, `result`)?
- [ ] Do names follow project conventions (snake_case for Python, camelCase for Swift)?
- [ ] Are boolean variables prefixed with `is_`, `has_`, `should_`?
- [ ] Are constants in UPPER_SNAKE_CASE?

## Code Organization

- [ ] Are imports grouped (stdlib → third-party → local) and sorted?
- [ ] Are related functions placed near each other?
- [ ] Are long functions broken into smaller, named helper functions?
- [ ] Is there consistent spacing between logical sections?

## Comments & Documentation

- [ ] Are comments explaining **why**, not **what** (the code shows what)?
- [ ] Are TODO/FIXME/HACK comments tagged with a reason or issue number?
- [ ] Are docstrings present on public functions and classes?
- [ ] For this project: are comments in Chinese where project convention requires?

## Formatting (Language-Agnostic)

- [ ] Consistent indentation
- [ ] Line length reasonable (no horizontal scrolling needed)
- [ ] No trailing whitespace
- [ ] Consistent brace/parenthesis style

## Project Conventions (lite-ailoha specific)

- [ ] Server comments use Chinese for SSE pipeline, data persistence, agent tool I/O, model config
- [ ] Card types are consistent across Python and Swift (4 canonical types)
- [ ] SSE protocol: every event has `event:`, `id:`, `data:` lines
- [ ] Endpoint paths use `/api/v1/` prefix
- [ ] Python 3.11+ features (`match`/`case`) used where appropriate

## Git Hygiene

- [ ] Are committed files intended to be committed (no `.env`, `.db`, test artifacts)?
- [ ] Are debug prints / console.logs removed?
- [ ] Are large binary files excluded?
- [ ] Is the commit message descriptive and in conventional format?

## Duplication

- [ ] Are there >3 identical code blocks that should be extracted?
- [ ] Are similar functions across files candidates for shared utilities?
- [ ] Are there copy-pasted test cases that could use parameterized tests?
