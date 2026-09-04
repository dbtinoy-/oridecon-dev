"""Provenance contracts for intentionally generated admin markup."""

from __future__ import annotations

from oridecon.admin.lib.template.auth_mfa import render_mfa_setup_page
from oridecon.admin.ui.templates.shell_scripts import loading_bar_script
from oridecon.ui import TrustedHTML, render_to_string, trusted_html


def test_loading_bar_markup_is_structured_and_script_free() -> None:
    output = render_to_string(loading_bar_script("flash-zone"))

    assert "htmx-loading-bar" in output
    assert "data-flash-zone=\"flash-zone\"" in output
    assert "<script" not in output


def test_loading_bar_escapes_flash_zone_identity() -> None:
    payload = "flash'); window.pwned=true; </script><script>"

    output = render_to_string(loading_bar_script(payload))

    # The zone id is data, not script: it is attribute-escaped and can never
    # terminate an element or open a script block.
    assert "&#x27;" in output
    assert "<script" not in output
    assert "&lt;/script&gt;" in output


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
