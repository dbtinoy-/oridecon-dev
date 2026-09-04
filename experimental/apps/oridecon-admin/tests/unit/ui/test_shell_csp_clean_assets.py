"""Shell pages must carry no inline executable code (CSP v2 candidate).

The strict report-only candidate (``STRICT_CSP``: ``script-src 'self'`` /
``style-src 'self'``) reports every inline ``<script>`` / ``<style>`` block
and every ``on*`` event-handler attribute. This test renders the same page
composition used for e.g. ``/admin/users`` (``base.html`` + ``AdminShell``)
and pins it to zero inline executable code, so the developer console stays
quiet for the shell classes and the candidate can eventually be flipped.

Per-component dynamic data is allowed as non-executable
``<script type="application/json">`` data islands (CSP-exempt); external
assets (``admin-shell.css``, ``admin-head.js``, ``admin-shell.js``) carry
the behaviour.
"""

from __future__ import annotations

import re
from pathlib import Path

from oridecon.admin.ui.templates.shell import AdminShell
from oridecon.ui import (
    RenderContext,
    RenderScope,
    render_context,
    render_to_string,
    trusted_html,
    trusted_template_output,
)

_ADMIN_ROOT = Path(__file__).parents[3] / "src" / "oridecon" / "admin"
_TEMPLATES_DIR = _ADMIN_ROOT / "views" / "templates"


def _render_users_shell_page() -> str:
    """Render the same composition as rendered by AdminRenderer.render_page."""
    from starlette.templating import Jinja2Templates

    templates = Jinja2Templates(directory=str(_TEMPLATES_DIR))

    shell = AdminShell(
        content=trusted_html(
            "<table><tr><td>users</td></tr></table>",
            source="test shell content",
        ),
        title="Users",
        user={"user_id": "u-1", "email": "a@b.c", "name": "u-1", "is_superuser": True},
        nav_items=[],
        user_menu_items=[],
        system_menu_items=[],
        breadcrumbs=[{"label": "Home", "url": "/admin"}, {"label": "Users", "url": "/admin/users"}],
        flash_messages=[{"message": "Welcome", "type": "success"}],
        theme_css="",
        features={},
        site_name="Oridecon Admin",
        logo_url="",
        dark_mode="",
        current_tenant_id=None,
        current_tenant_name="",
        tenant_list=[],
        csrf_token="tok",
        admin_prefix="/admin",
    )

    with render_context(RenderContext(scope=RenderScope())):
        shell_html = render_to_string(shell)
    shell_html = trusted_template_output(
        shell_html, template="admin_shell.html (test harness, autoescape on)"
    )

    return templates.env.get_template("admin_shell.html").render(
        content=shell_html,
        title="Users",
        site_name="Oridecon Admin",
        favicon_url="",
        dark_mode="",
        csrf_token="tok",
        static_prefix="/admin",
        primary_color="#6b7280",
    )


class TestShellPageHasNoInlineExecutableCode:
    def test_no_inline_script_blocks(self) -> None:
        html = _render_users_shell_page()

        inline = re.findall(
            r"<script(?![^>]*(?:src=|type=[\"']application/json[\"']))[^>]*>",
            html,
        )
        assert inline == []

    def test_no_inline_style_blocks(self) -> None:
        html = _render_users_shell_page()

        assert "<style" not in html

    def test_no_inline_event_handler_attributes(self) -> None:
        html = _render_users_shell_page()

        assert re.findall(r"\son\w+\s*=", html) == []

    def test_data_islands_are_non_executable_json(self) -> None:
        html = _render_users_shell_page()

        assert 'type="application/json"' in html
        assert '<script type="application/json"' in html

    def test_shell_assets_are_referenced_externally(self) -> None:
        html = _render_users_shell_page()

        assert 'src="/admin/static/js/admin-shell.js"' in html
        assert 'src="/admin/static/js/admin-head.js"' in html
        assert 'href="/admin/static/css/admin-shell.css"' in html

    def test_runtime_config_arrives_via_data_attributes(self) -> None:
        html = _render_users_shell_page()

        assert 'data-admin-dark-mode=' in html
        assert 'data-admin-login-url="/admin/login"' in html
        assert 'data-admin-primary-color="#6b7280"' in html
