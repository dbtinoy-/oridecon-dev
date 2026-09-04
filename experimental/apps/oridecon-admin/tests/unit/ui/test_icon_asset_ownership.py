"""Owned-icon regressions for admin and shared UI product surfaces."""

from __future__ import annotations

from html import unescape
from pathlib import Path
import re
from types import SimpleNamespace

from oridecon.admin.settings.panel.ui import ConfigDashboardUI
from oridecon.admin.ui.organisms.table.views.tabular_header import (
    render_table_header,
)
from oridecon.admin.ui.organisms.table.views.tabular_rows import render_table_rows
from oridecon.ui import Element, render_to_string

REPO = Path(__file__).resolve().parents[6]
_CLASS_TOKEN = re.compile(r"(?<![A-Za-z0-9_-])(?:fas|far|fab|fa-[a-z][a-z0-9-]*)\b")


def test_product_python_class_attributes_do_not_require_font_awesome() -> None:
    roots = (
        REPO / "experimental/apps/oridecon-ui/src",
        REPO / "experimental/apps/oridecon-admin/src",
    )
    offenders: list[str] = []
    for root in roots:
        for path in root.rglob("*.py"):
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                if "class" in line and _CLASS_TOKEN.search(line):
                    offenders.append(
                        f"{path.relative_to(REPO)}:{line_number}: {line.strip()}"
                    )

    assert not offenders, "Unowned Font Awesome class tokens:\n" + "\n".join(offenders)


def test_grouped_table_toggle_uses_owned_icon_and_dynamic_state() -> None:
    config = SimpleNamespace(
        group_by="kind",
        columns=[],
        resource_prefix=None,
        bulk_actions=[],
        expandable_relationship=None,
    )

    output = render_to_string(
        render_table_rows(
            config,
            [{"id": "1", "kind": "Priority"}],
            user=None,
            resource_name=None,
        )
    )

    assert "<svg" in output
    assert "fa-chevron-down" not in output
    assert 'aria-label="Toggle Priority group"' in output
    assert ":aria-expanded=" in output


class _HeaderColumn:
    def __init__(self, name: str) -> None:
        self.name = name
        self._width = None
        self._grow = True
        self._pinned = None

    def is_visible(self, **_kwargs: object) -> bool:
        return True

    def render_header(self, *_args: object, **_kwargs: object) -> Element:
        return Element("th", Element("span", "Column"))


def test_column_drag_handle_uses_owned_icon_and_serialized_name() -> None:
    column_name = "name'); window.pwned = true; ('"
    config = SimpleNamespace(
        columns=[_HeaderColumn(column_name)],
        resource_prefix=None,
        bulk_actions=[],
        expandable_relationship=None,
        reorderable_columns=True,
    )
    state = SimpleNamespace(sort_by=None, sort_order=None)

    output = unescape(
        render_to_string(
            render_table_header(
                config,
                state,
                data=[],
                user=None,
                resource_name=None,
            )
        )
    )

    assert "<svg" in output
    assert "fa-grip-vertical" not in output
    assert "event.dataTransfer.setData('text/plain', \"name');" in output
    assert "reorderColumn(event.dataTransfer.getData('text/plain'), \"name');" in output
    assert "'name'); window.pwned" not in output


def test_settings_sidebar_uses_registry_icon_with_owned_fallback() -> None:
    specs = [
        SimpleNamespace(namespace="known", label="Known", icon="cog"),
        SimpleNamespace(namespace="fallback", label="Fallback", icon="fa-virus"),
    ]

    output = render_to_string(
        ConfigDashboardUI().render_sidebar(
            specs,
            active_ns="known",
            category="admin",
        )
    )

    assert output.count("<svg") == 2
    assert "fas " not in output
    assert "fa-virus" not in output
    assert "Known" in output
    assert "Fallback" in output
