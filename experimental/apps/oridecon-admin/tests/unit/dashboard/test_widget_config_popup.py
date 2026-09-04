"""Rendering contracts for dashboard widget configuration panels."""

from __future__ import annotations

import re

from oridecon.admin.dashboard.widget_config_popup import render_widget_config_popup
from oridecon.admin.dashboard.widget_types import ConfigField


def test_config_fields_remain_structured_and_labelled() -> None:
    html = render_widget_config_popup(
        "sales",
        "Sales",
        [
            ConfigField(name="limit", type="number", label="Limit"),
            ConfigField(
                name="period",
                type="select",
                label="Period",
                options=[("7d", "Seven days")],
            ),
        ],
        {"limit": 10, "period": "7d"},
    )

    assert "&lt;input" not in html
    assert "&lt;select" not in html
    field_ids = re.findall(r'<(?:input|select)[^>]*id="([^"]+)"', html)
    assert len(field_ids) == 2
    for field_id in field_ids:
        assert f'for="{field_id}"' in html


def test_config_form_identity_is_stable_and_normalized() -> None:
    first = render_widget_config_popup("Sales / EU", "Sales", [], {})
    second = render_widget_config_popup("Sales / EU", "Sales", [], {})
    form_id = re.search(r'<form[^>]*id="([^"]+)"', first)

    assert first == second
    assert form_id is not None
    assert re.fullmatch(r"[a-z][a-z0-9-]*", form_id.group(1))
    assert f'form="{form_id.group(1)}"' in first


def test_config_popup_escapes_contributor_copy_and_values() -> None:
    payload = '"><script>alert(1)</script>'
    html = render_widget_config_popup(
        payload,
        payload,
        [ConfigField(name=payload, type="text", label=payload)],
        {payload: payload},
    )

    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
