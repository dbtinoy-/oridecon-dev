"""Admin shell trust grants stay at named framework output boundaries."""

from __future__ import annotations

from oridecon.admin.engine.renderer import AdminRenderer
from oridecon.admin.ui.templates.shell import AdminShell
from oridecon.ui import Component, render_to_string, trusted_html

_PAYLOAD = '<img src=x onerror="shellBypass()">'


class _PlainStringComponent(Component):
    def render(self) -> str:
        return _PAYLOAD


class _ForgedHTML:
    def __html__(self) -> str:
        return "<script>forgedPartial()</script>"

    def __str__(self) -> str:
        return _PAYLOAD


def test_plain_shell_content_is_text() -> None:
    output = render_to_string(AdminShell(content=_PAYLOAD))

    assert '<img src=x onerror="shellBypass()">' not in output
    assert "&lt;img src=x" in output


def test_plain_component_output_is_text_inside_shell() -> None:
    output = render_to_string(AdminShell(content=_PlainStringComponent()))

    assert '<img src=x onerror="shellBypass()">' not in output
    assert "&lt;img src=x" in output


def test_explicit_framework_page_output_remains_markup() -> None:
    content = trusted_html(
        "<section>framework page</section>",
        source="test framework page",
    )

    output = render_to_string(AdminShell(content=content))

    assert "<section>framework page</section>" in output


def test_theme_css_cannot_close_its_style_element() -> None:
    output = render_to_string(
        AdminShell(
            content="safe",
            theme_css="body{} </style><script id=theme-attack>attack()</script>",
        )
    )

    assert "<script id=theme-attack>" not in output
    assert r"\3c script id=theme-attack" in output


def test_partial_renderer_rejects_forged_html_protocol() -> None:
    response = AdminRenderer().render_partial(_ForgedHTML())
    output = response.body.decode()

    assert "<script>" not in output
    assert "&lt;img src=x" in output
