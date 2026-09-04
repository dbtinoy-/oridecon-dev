"""Settings-panel navigation contracts (R52, docs/09-01-2026/48).

The panel sidebar must retain a stable content target, and the shell's
history-aware script must be present to keep active styling and ARIA state
truthful after an in-place HTMX swap.

The shell scripts ship as the generated static asset
``static/js/admin-shell.js`` (CSP v2 migration); the contracts below assert
against that file.
"""

from __future__ import annotations

from pathlib import Path

_SHELL_JS = (
    Path(__file__).parents[3]
    / "src"
    / "oridecon"
    / "admin"
    / "static"
    / "js"
    / "admin-shell.js"
)


def _shell_js() -> str:
    return _SHELL_JS.read_text(encoding="utf-8")


def test_shell_script_syncs_settings_panel_state_after_history_navigation() -> None:
    html = _shell_js()

    assert "syncSettingsPanelNavigation" in html
    assert "htmx:pushedIntoHistory" in html
    assert "htmx:historyRestore" in html
    assert "data-settings-panel-nav" in html
    assert "setAttribute('aria-current', 'page')" in html
    assert "dark:bg-primary-900/30" in html


def test_shell_script_handles_browser_back_forward_for_panel_state() -> None:
    html = _shell_js()

    assert "window.addEventListener('popstate'" in html
    assert "new URL(path || location.href, location.href).pathname" in html
    assert "removeAttribute('aria-current')" in html
