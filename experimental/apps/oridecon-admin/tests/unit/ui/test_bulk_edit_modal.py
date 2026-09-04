"""Trust and identity regressions for the bulk-edit slide-over."""

from __future__ import annotations

import re

from oridecon.admin.actions.bulk_manager import BulkEditField
from oridecon.admin.ui.organisms.bulk_edit_modal import (
    bulk_assign_modal,
    bulk_confirm_dialog,
    bulk_edit_modal,
    bulk_progress_indicator,
)
from oridecon.ui import render_to_string


def test_bulk_edit_form_and_fields_use_stable_scoped_ids() -> None:
    fields = [
        BulkEditField(name="status", label="Status", required=True),
        BulkEditField(name="notes", label="Notes", field_type="textarea"),
    ]

    first = bulk_edit_modal(2, fields, "/admin/items/bulk-edit")
    second = bulk_edit_modal(2, fields, "/admin/items/bulk-edit")

    assert first == second
    form_match = re.search(r'<form[^>]*id="([^"]+)"', first)
    assert form_match is not None
    form_id = form_match.group(1)
    assert f'form="{form_id}"' in first

    field_ids = re.findall(r'<(?:input|textarea)[^>]*id="([^"]+)"', first)
    assert len(field_ids) == 2
    for field_id in field_ids:
        assert f'for="{field_id}"' in first


def test_bulk_edit_structurally_escapes_fields_options_and_action_url() -> None:
    payload = '"><script>alert(1)</script>'
    html = bulk_edit_modal(
        1,
        [
            BulkEditField(
                name=payload,
                label=payload,
                field_type="select",
                options=[(payload, payload)],
                help_text=payload,
            )
        ],
        payload,
    )

    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert "&quot;&gt;&lt;script&gt;" in html


def test_bulk_edit_accepts_an_instance_specific_swap_target() -> None:
    html = bulk_edit_modal(
        1,
        [BulkEditField(name="status", label="Status")],
        "/admin/items/bulk-edit",
        hx_target="#oridecon-table-data-items",
    )

    assert 'hx-target="#oridecon-table-data-items"' in html


def test_legacy_bulk_overlays_no_longer_share_fixed_ids() -> None:
    html = render_to_string(
        [
            bulk_assign_modal(
                2,
                "Owner",
                [("1", "Ada")],
                "/admin/orders/assign",
            ),
            bulk_assign_modal(
                3,
                "Owner",
                [("2", "Grace")],
                "/admin/customers/assign",
            ),
            bulk_confirm_dialog(
                "archive",
                2,
                action_url="/admin/orders/archive",
            ),
            bulk_progress_indicator("archive", "/admin/orders/progress"),
        ]
    )

    for old_id in (
        "bulk-assign-modal",
        "bulk-assign-form",
        "bulk-assign-value",
        "bulk-confirm-dialog",
        "bulk-progress",
        "progress-bar",
        "progress-status",
        "progress-errors",
    ):
        assert f'id="{old_id}"' not in html

    ids = re.findall(r' id="([^"]+)"', html)
    assert len(ids) == len(set(ids))
    assert "Assign" in html
    assert "Cancel" in html
    assert "object at 0x" not in html
    assert "#table-body" not in html
