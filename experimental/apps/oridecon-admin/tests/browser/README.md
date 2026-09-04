# Browser tests

Playwright tests cover behavior that only exists once a real browser has parsed
the page: form dirty-state and submit locking, unsaved-change prompts, HTMX
swaps, URL history, and settings navigation.

## Running locally

Browser tests are opt-in for the normal local unit-test path:

```bash
# one-time
uv run playwright install chromium

# run the browser suite
uv run pytest experimental/apps/oridecon-admin/tests/browser --run-browser
```

Without either browser flag, tests marked `browser` are collected and skipped.
The browser-independent server-harness tests still run.

If Playwright or Chromium is unavailable in local opt-in mode, the fixture skips
with the exact remediation. CI uses the stricter mode:

```bash
uv run pytest experimental/apps/oridecon-admin/tests/browser --browser-gate
```

`--browser-gate` implies `--run-browser` and converts missing Playwright or
Chromium into a test failure. This prevents a required browser job from passing
because all engine-backed tests skipped.

## Harness ownership

`conftest.py` owns the complete per-test lifecycle:

- **`live_server`** pre-binds an ephemeral listening socket before starting
  Uvicorn, eliminating the release-and-rebind race from “find a free port”
  helpers. It waits for ASGI lifespan startup and fails if a server thread leaks
  during teardown.
- **`browser_type`** owns one session-scoped headless Chromium process.
- **`page`** owns a fresh browser context per test, so cookies and storage cannot
  leak between tests.

Tests do not require an operator-started server or a fixed port. Pages load the
vendored `static/js/htmx.min.js`, not a CDN, so the suite remains offline and
exercises the asset shipped by the admin package.

`test_harness.py` drives server startup over HTTP without requiring Chromium.
That keeps server lifecycle failures visible even on a machine where the
engine-backed suite is not enabled.

## Current scope

- `test_harness.py`: server startup, unique ephemeral listeners, and teardown.
- `test_form_behavior.py`: dirty forms, reset announcements, navigation guards,
  and submit locking.
- `test_sidebar_navigation.py`: HTMX swaps, fragment/full-page responses, URL
  history, and consecutive navigation.
- `test_settings_panel_navigation.py`: settings panel navigation behavior.

The production-browser plan in `docs/09-04-2026/06-production-browser-release-gate.md`
tracks the remaining migration from focused behavior fixtures to the complete
playground/admin lifecycle, offline network interception, accessibility scans,
and retained failure artifacts.
