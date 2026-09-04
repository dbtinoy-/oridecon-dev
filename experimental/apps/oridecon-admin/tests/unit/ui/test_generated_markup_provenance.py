"""Provenance contracts for intentionally generated admin markup."""

from __future__ import annotations

from oridecon.admin.lib.template.auth_mfa import render_mfa_setup_page
from oridecon.admin.ui.templates.shell_scripts import (
    admin_form_ux_script,
    loading_bar_script,
    search_overlay_markup,
)
from oridecon.ui import TrustedHTML, render_to_string, trusted_html


def test_shell_markup_builders_have_specific_provenance() -> None:
    search = search_overlay_markup()
    loading = loading_bar_script("flash-zone")
    forms = admin_form_ux_script()

    assert isinstance(search, TrustedHTML)
    assert search.source == "AdminShell search overlay markup"
    assert isinstance(loading, TrustedHTML)
    assert loading.source == "AdminShell loading and error markup"
    assert isinstance(forms, TrustedHTML)
    assert forms.source == "AdminShell delegated form UX markup"


def test_loading_script_serializes_flash_zone_identity() -> None:
    payload = "flash'); window.pwned=true; </script><script>"

    output = render_to_string(loading_bar_script(payload))

    assert "</script><script>" not in output
    assert "\\u003c/script\\u003e\\u003cscript\\u003e" in output
    assert 'document.getElementById("flash&#x27;)' not in output


def test_plain_mfa_qr_markup_is_escaped() -> None:
    output = render_mfa_setup_page(
        enabled=False,
        qr_svg='<svg onload="window.pwned=true"></svg>',
    )

    assert '<svg onload="window.pwned=true">' not in output
    assert "&lt;svg onload=" in output


def test_attributed_mfa_service_qr_markup_is_rendered() -> None:
    output = render_mfa_setup_page(
        enabled=False,
        qr_svg=trusted_html(
            "<svg><path></path></svg>",
            source="MFA service QR SVG generator",
        ),
    )

    assert "<svg><path></path></svg>" in output
