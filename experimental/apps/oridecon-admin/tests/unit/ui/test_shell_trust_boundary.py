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


def test_theme_css_is_never_rendered_inline() -> None:
    # Runtime theme CSS used to be injected as an inline <style> element;
    # under the strict CSP candidate it is applied by admin-head.js from the
    # data-admin-primary-color attribute. Untrusted theme_css must not
    # produce markup at all.
    output = render_to_string(
        AdminShell(
            content="safe",
            theme_css="body{} </style><script id=theme-attack>attack()</script>",
        )
    )

    assert "<script id=theme-attack>" not in output
    assert "<style" not in output
    assert "admin-theme-css" not in output


def test_partial_renderer_rejects_forged_html_protocol() -> None:
    response = AdminRenderer().render_partial(_ForgedHTML())
    output = response.body.decode()

    assert "<script>" not in output
    assert "&lt;img src=x" in output
