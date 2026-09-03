# AUDIT_DOC_CLAIMS.md — Oridecon Documentation Claims Audit

> **Source**: Every `ORI_*` env var and `ProviderPriority.*` mention in every
> package `docs/*.md` file (prose + python blocks), resolved against the
> installed framework. Env vars must map to a real `*Config` field
> (`ORI_<SECTION>__<KEY>` / `ORI_<PACKAGE>__<KEY>`) or be read directly by
> framework code.

## Summary

- Env vars verified: 804
- Priorities verified: 26
- Unresolved claims: 0

## Resolved Claims

| Doc | Claim | Resolution |
|-----|-------|------------|
| `experimental/apps/oridecon-admin/docs/CONFIGURATION.md` | `ORI_ADMIN__AUDIT__REDACTION_FIELD_DENYLIST` | Removed — field is in core logging configurator, not admin config |
| `experimental/apps/oridecon-admin/docs/CONFIGURATION.md` | `ORI_ADMIN__AUDIT__REDACTION_PATTERNS` | Removed — field is in core logging configurator, not admin config |
| `packages/oridecon-auth/docs/CONFIGURATION.md` | `ORI_AUTH__TOKEN__ALLOW_UNVERIFIED_DEV` | Removed — field does not exist; JWTConfig enforces verified-only decoding |
