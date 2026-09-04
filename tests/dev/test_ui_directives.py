from __future__ import annotations

from pathlib import Path

from dev.checks.ui_directives import main, scan_file, scan_sources


def _source(tmp_path: Path, text: str) -> Path:
    path = tmp_path / "component.py"
    path.write_text(text, encoding="utf-8")
    return path


def test_scanner_rejects_dead_keyword_families(tmp_path: Path) -> None:
    path = _source(
        tmp_path,
        "el('div', x_on_click='x', x_bind_value='y', x_transition_enter='opacity-0')\n",
    )

    assert [finding.name for finding in scan_file(path)] == [
        "x_on_click",
        "x_bind_value",
        "x_transition_enter",
    ]


def test_scanner_rejects_malformed_literal_names(tmp_path: Path) -> None:
    path = _source(
        tmp_path,
        "attrs = {'x-on-click': 'x', 'x-bind--class': 'y', "
        "'x-on:click.window.window': 'z'}\n",
    )

    assert [finding.name for finding in scan_file(path)] == [
        "x-on-click",
        "x-bind--class",
        "x-on:click.window.window",
    ]


def test_scanner_allows_canonical_alpine_and_htmx(tmp_path: Path) -> None:
    path = _source(
        tmp_path,
        "el('button', {'x-on:click.prevent': 'x', 'x-bind:class': 'y', "
        "'x-transition:enter-start': 'opacity-0'}, hx_on_click='back()')\n",
    )

    assert scan_file(path) == []


def test_scanner_ignores_explanatory_comments_and_strings(tmp_path: Path) -> None:
    path = _source(
        tmp_path,
        '"""Do not use x_bind_value."""\n# x_on_click is dead\n',
    )

    assert scan_file(path) == []


def test_repository_ui_sources_have_no_dead_directives() -> None:
    root = Path(__file__).resolve().parents[2]

    assert scan_sources(root) == []


def test_cli_passes_for_repository() -> None:
    root = Path(__file__).resolve().parents[2]

    assert main(["--root", str(root)]) == 0
