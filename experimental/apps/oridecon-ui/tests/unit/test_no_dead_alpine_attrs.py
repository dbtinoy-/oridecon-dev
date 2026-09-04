"""Regression guards for Alpine attributes that browsers keep but ignore.

``el()`` converts keyword underscores to hyphens. That is correct for HTMX,
but ``x_on_click``, ``x_bind_value``, and ``x_transition_enter`` become dead
Alpine attributes. Alpine requires colon-delimited directive arguments.
"""

from __future__ import annotations

import ast
from collections.abc import Callable
from pathlib import Path

import pytest

from oridecon.ui.attributes import AlpineExpression, alpine, expression
from oridecon.ui.core.base import el

_APPS = Path(__file__).resolve().parents[3]
SOURCE_ROOTS = {
    "oridecon-admin": _APPS / "oridecon-admin" / "src" / "oridecon" / "admin",
    "oridecon-ui": _APPS / "oridecon-ui" / "src" / "oridecon" / "ui",
}

_DEAD_PREFIXES = ("x_on_", "x_bind_", "x_transition_")


def _dead_alpine_names(path: Path) -> list[tuple[int, str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    offenders: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            offenders.extend(
                (keyword.lineno, keyword.arg)
                for keyword in node.keywords
                if keyword.arg and keyword.arg.startswith(_DEAD_PREFIXES)
            )
        elif isinstance(node, ast.Dict):
            offenders.extend(
                (key.lineno, key.value)
                for key in node.keys
                if isinstance(key, ast.Constant)
                and isinstance(key.value, str)
                and key.value.startswith(_DEAD_PREFIXES)
            )
    return offenders


def test_no_dead_alpine_directive_attributes_in_source() -> None:
    offenders: list[str] = []
    for package, root in SOURCE_ROOTS.items():
        for path in sorted(root.rglob("*.py")):
            relative = path.relative_to(root)
            offenders.extend(
                f"{package}/{relative}:{line}: {name}"
                for line, name in _dead_alpine_names(path)
            )

    assert not offenders, (
        "Alpine x_on_*, x_bind_*, and x_transition_* kwargs render as dead "
        "dash-delimited attributes. Use oridecon.ui.attributes.alpine or a "
        "canonical dict key. Offending lines:\n" + "\n".join(offenders)
    )


class TestAlpineAttributes:
    def test_expression_is_explicit_value_type(self) -> None:
        value = expression("open = false")

        assert isinstance(value, AlpineExpression)
        assert str(value) == "open = false"

    @pytest.mark.parametrize("value", ["", "   ", "open\x00 = false"])
    def test_expression_rejects_empty_or_nul(self, value: str) -> None:
        with pytest.raises(ValueError, match="must not"):
            expression(value)

    def test_helpers_render_canonical_directives(self) -> None:
        html = str(
            el(
                "button",
                "Close",
                **alpine.data(alpine.expr("{ open: true }")),
                **alpine.on("click", alpine.expr("open = false"), "prevent", "stop"),
                **alpine.bind("aria-expanded", alpine.expr("open")),
            )
        )

        assert 'x-data="{ open: true }"' in html
        assert 'x-on:click.prevent.stop="open = false"' in html
        assert 'x-bind:aria-expanded="open"' in html
        assert "x-on-click" not in html
        assert "x-bind-aria-expanded" not in html

    def test_transition_helper_uses_colon_phase(self) -> None:
        html = str(
            el(
                "div",
                **alpine.transition("enter-start", alpine.expr("opacity-0")),
            )
        )

        assert 'x-transition:enter-start="opacity-0"' in html

    @pytest.mark.parametrize(
        ("factory", "message"),
        [
            (lambda: alpine.on("", alpine.expr("x")), "event name"),
            (lambda: alpine.bind("Bad Name", alpine.expr("x")), "bound attribute"),
            (
                lambda: alpine.on("click", alpine.expr("x"), "prevent", "prevent"),
                "unique",
            ),
            (
                lambda: alpine.transition("middle", alpine.expr("x")),
                "transition phase",
            ),
        ],
    )
    def test_helper_rejects_invalid_tokens(
        self, factory: Callable[[], object], message: str
    ) -> None:
        with pytest.raises(ValueError, match=message):
            factory()


class TestElementAlpineValidation:
    @pytest.mark.parametrize(
        "attrs",
        [
            {"x_on_click": "open = false"},
            {"x_bind_value": "value"},
            {"x_bind__class": "active ? 'on' : 'off'"},
            {"x_transition_enter": "duration-300"},
            {"x-on:click.window.window": "close()"},
            {"x-on:Click": "close()"},
        ],
    )
    def test_dead_or_malformed_alpine_names_fail_render(
        self, attrs: dict[str, str]
    ) -> None:
        with pytest.raises(ValueError, match="Alpine"):
            str(el("div", **attrs))

    def test_valid_longhand_and_shorthand_names_render(self) -> None:
        html = str(
            el(
                "button",
                **{
                    "x-on:htmx:after-request.window": "done = true",
                    "x-bind:class": "active ? 'on' : 'off'",
                    "x-transition": "",
                    "@click": "open = false",
                    ":disabled": "busy",
                },
            )
        )

        assert "x-on:htmx:after-request.window" in html
        assert "x-bind:class" in html
        assert " x-transition=" in html
        assert "@click" in html
        assert ":disabled" in html

    def test_htmx_dash_alias_remains_valid(self) -> None:
        html = str(el("button", hx_on_click="history.back()"))

        assert 'hx-on-click="history.back()"' in html


def test_migrated_components_render_canonical_bindings() -> None:
    from oridecon.ui.molecules.tabs import TabPanel, Tabs
    from oridecon.ui.organisms.query_builder import QueryBuilder
    from oridecon.ui.organisms.task_progress import TaskProgress

    tabs = str(
        Tabs(
            [("First", "first")],
            tabs_id="directive-tabs",
            children=[TabPanel("first", "First panel")],
        ).render()
    )
    query = str(QueryBuilder("filters").render())
    progress = str(TaskProgress("task-1").render())

    assert "x-bind:class" in tabs
    assert "x-bind:value" in query
    assert "x-bind:style" in progress
    for html in (tabs, query, progress):
        assert "x-bind-" not in html


def test_slide_over_close_button_uses_canonical_alpine_syntax() -> None:
    from oridecon.ui.organisms.slide_over import SlideOver

    html = str(SlideOver("Test", slide_id="test", is_open=True).render())
    assert 'x-on:click="open = false"' in html
    assert "x-on-click" not in html


def test_submit_button_loading_state_uses_canonical_alpine_syntax() -> None:
    from oridecon.ui.atoms.button import SubmitButton

    html = str(SubmitButton("Save").render())
    assert "x-on:click" in html
    assert "x-on:htmx:after-request" in html
    assert "x-on-click" not in html
    assert "x-on-htmx-after-request" not in html


def test_get_icon_is_decorative_by_default() -> None:
    from oridecon.ui.atoms.icons import get_icon

    html = str(get_icon("home"))
    assert 'aria-hidden="true"' in html
    assert 'focusable="false"' in html


def test_get_icon_respects_explicit_accessible_identity() -> None:
    from oridecon.ui.atoms.icons import get_icon

    html = str(get_icon("home", **{"aria-label": "Home", "role": "img"}))
    assert 'aria-label="Home"' in html
    assert "aria-hidden" not in html
