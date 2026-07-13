# Security Review Checklist

## Secrets & Credentials

- [ ] Are API keys, tokens, or passwords hardcoded in source?
- [ ] Are secrets stored in `.env` (not committed)?
- [ ] Are `.env` / `.env.local` / `*.pem` in `.gitignore`?
- [ ] Are credential values logged or printed in error messages?

## Input Validation

- [ ] Is user input validated server-side (not just client-side)?
- [ ] Are file uploads checked for type, size, and content?
- [ ] Is base64 data validated before decoding?
- [ ] Are URL parameters sanitized (path traversal, null bytes)?

## Authentication & Authorization

- [ ] Are endpoints protected by auth where needed?
- [ ] Is there privilege escalation risk (user A accessing user B's data)?
- [ ] Are session tokens / API keys properly scoped?

## Data Exposure

- [ ] Are error messages revealing system internals?
- [ ] Are response fields filtering sensitive data (passwords, tokens)?
- [ ] Are log statements redacting PII (phone numbers, email, names)?
- [ ] Is debug mode disabled in production?

## Dependency Risks

- [ ] Are new dependencies from trusted sources?
- [ ] Are dependency versions pinned (not floating)?
- [ ] Are there known vulnerabilities in added/updated packages?

## Network

- [ ] Is CORS restricted to specific origins (not `*`)?
- [ ] Are HTTP headers setting proper security policies?
- [ ] Is proxy configuration explicit (not relying on env vars)?

## iOS Specific

- [ ] Is sensitive data stored in Keychain (not UserDefaults)?
- [ ] Is App Transport Security properly configured?
- [ ] Are URL schemes validated (no open redirect)?
