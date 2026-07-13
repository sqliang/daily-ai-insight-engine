# Architecture Review Checklist

## Design Consistency

- [ ] Does the change follow existing project patterns (not introducing a new paradigm)?
- [ ] Are new modules placed in the correct layer (api/agent/services/storage)?
- [ ] Are file/class/function sizes reasonable (<200 lines per function, <500 per class)?
- [ ] Is the directory structure consistent with peer modules (e.g., `prompts/`, `subagents/`, `validators/` all use one-file-per-concept)?

## Coupling & Cohesion

- [ ] Does the change introduce circular imports?
- [ ] Are cross-layer dependencies one-directional (api → agent → services → storage)?
- [ ] Is each module doing one thing (single responsibility)?
- [ ] Are there convenience imports that pull in unnecessary dependencies?

## Anti-Patterns

- [ ] God class / god function (too many responsibilities)
- [ ] Dead code (unused imports, unreachable branches, variables assigned but never read)
- [ ] Magic numbers / magic strings without constants
- [ ] Copy-paste between files (should extract shared logic)
- [ ] Premature abstraction (over-engineering for future use cases)

## API Design

- [ ] Are new endpoints following REST conventions?
- [ ] Are request/response schemas consistent with existing ones?
- [ ] Is backward compatibility maintained (no breaking changes without versioning)?
- [ ] Are SSE events following the established protocol (event:/id:/data: lines)?

## Config & Environment

- [ ] Are new config values added to both `config.py` and `.env.example`?
- [ ] Are defaults reasonable for development?
- [ ] Is environment-specific logic isolated (not scattered across files)?

## Testability

- [ ] Is the code testable without mocking too many dependencies?
- [ ] Are side effects (DB writes, API calls) separated from pure logic?
- [ ] Can the new code be tested in isolation?

## Documentation Consistency

- [ ] Do new files have module-level docstrings?
- [ ] Do new functions have parameter/return documentation?
- [ ] Are comments in Chinese where project convention requires it?
- [ ] Is the design documented in `docs/DESIGN.md` if it's a significant change?
