"""Trust contracts for lazy HTMX placeholders."""

from __future__ import annotations

from oridecon.ui import Element, trusted_html
from oridecon.ui.performance.performance import lazy_load_placeholder


def test_plain_placeholder_markup_is_escaped_display_text() -> None:
    output = lazy_load_placeholder(
        "/load",
        "orders",
        placeholder='<img src=x onerror="window.pwned=true">',
    )

    assert "<img" not in output
    assert "&lt;img src=x onerror=" in output


def test_structured_placeholder_is_preserved() -> None:
    output = lazy_load_placeholder(
        "/load",
        "orders",
        placeholder=Element("strong", "Loading orders"),
    )

    assert "<strong>Loading orders</strong>" in output


def test_explicit_trusted_placeholder_markup_remains_supported() -> None:
    output = lazy_load_placeholder(
        "/load",
        "orders",
        placeholder=trusted_html(
            '<span class="loading">Loading</span>',
            source="test-authored loading fragment",
        ),
    )

    assert '<span class="loading">Loading</span>' in output


def test_placeholder_attributes_remain_escaped() -> None:
    output = lazy_load_placeholder(
        '/load" onload="window.pwned=true',
        'orders" autofocus onfocus="window.pwned=true',
        trigger='revealed" onmouseover="window.pwned=true',
    )

    assert 'hx-get="/load&quot; onload=&quot;window.pwned=true"' in output
    assert 'id="orders&quot; autofocus onfocus=&quot;window.pwned=true"' in output
    assert 'hx-trigger="revealed&quot; onmouseover=&quot;window.pwned=true"' in output
