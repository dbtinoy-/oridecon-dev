# AUDIT_DOC_IMPORTS.md — Oridecon Documentation Import Audit

> **Source**: Every `oridecon.*` `from`/`import` statement in the python
> blocks of every package `docs/*.md` file, resolved against the installed
> framework with `importlib`. An import fails when its module cannot be
> imported or when an imported name is missing from that module.

## Summary

- Imports verified: 1529
- Unresolved imports: 0

No unresolved `oridecon.*` imports detected.
