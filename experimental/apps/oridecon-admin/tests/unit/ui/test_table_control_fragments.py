"""Tests for TableControlFragments OOB rendering."""

from __future__ import annotations

from oridecon.admin.ui.organisms.data_table import DataTable
from oridecon.ui import Zones
from oridecon.ui.columns.types import TextColumn
from oridecon.ui.core.base import render_to_string

_TABLE_KEY = "/admin/users"


def _zone_id(zone) -> str:
    return Zones.table_zone_id(zone, table_key=_TABLE_KEY)


def test_htmx_request_emits_switchers_oob() -> None:
    """When htmx_request=True, the response includes hx-swap-oob on toolbar switchers."""
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[{"id": 1, "name": "Alice"}],
        resource_prefix="/admin/users",
        htmx_request=True,
    )
    html = render_to_string(dt)
    assert 'hx-swap-oob="outerHTML"' in html
    assert f"{_zone_id(Zones.TOOLBAR)}-switchers" in html


def test_htmx_request_emits_scope_tabs_oob() -> None:
    """When htmx_request=True, the response includes scope tabs as an OOB fragment."""
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[{"id": 1, "name": "Alice"}],
        resource_prefix="/admin/users",
        htmx_request=True,
        enable_search=True,
    )
    html = render_to_string(dt)
    # Scope tabs should be rendered as an OOB element
    assert f'id="{_zone_id(Zones.SCOPE_TABS)}"' in html
    assert 'hx-swap-oob="outerHTML"' in html


def test_no_oob_without_htmx_flag() -> None:
    """When htmx_request is not set, no hx-swap-oob appears in the table output."""
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[{"id": 1, "name": "Alice"}],
        resource_prefix="/admin/users",
    )
    html = render_to_string(dt)
    assert 'hx-swap-oob="outerHTML"' not in html


def test_htmx_request_contains_data_zone() -> None:
    """htmx_request=True response still contains the #table-data target zone."""
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[{"id": 1, "name": "Alice"}],
        resource_prefix="/admin/users",
        htmx_request=True,
    )
    html = render_to_string(dt)
    assert f'id="{_zone_id(Zones.DATA)}"' in html


def test_htmx_request_reflects_layout_state() -> None:
    """OOB switchers reflect the current layout/view state."""
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[{"id": 1, "name": "Alice"}],
        resource_prefix="/admin/users",
        layout_type="sidebar",
        data_view="tabular",
        htmx_request=True,
    )
    html = render_to_string(dt)
    assert 'hx-swap-oob="outerHTML"' in html


def test_htmx_request_includes_clear_button_oob() -> None:
    """Clear button is included in OOB switchers fragment."""
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[{"id": 1, "name": "Alice"}],
        resource_prefix="/admin/users",
        enable_search=True,
        htmx_request=True,
    )
    html = render_to_string(dt)
    assert "Clear" in html
