"""Tests for contributor widget rendering."""

from __future__ import annotations

import re

import pytest

from oridecon.admin.dashboard.widgets import WidgetRegistry
from oridecon.contracts.admin import (
    DashboardWidgetDefinition,
    WidgetCategory,
    WidgetKind,
    WidgetSize,
)
from oridecon.ui import TrustedHTML


class TestWidgetRegistry:
    def test_trusted_contributor_widgets_attributes_registry_markup(self) -> None:
        rendered = WidgetRegistry().trusted_contributor_widgets([])

        assert isinstance(rendered, TrustedHTML)
        assert rendered.source == "structured admin contributor-widget card renderer"
        assert "widget-empty-state" in rendered.value

    def test_render_contributor_widgets_empty(self) -> None:
        """Empty widget list returns styled empty state."""
        registry = WidgetRegistry()
        result = registry.render_contributor_widgets([])
        assert "widget-empty-state" in result
        # Copy no longer asserts "none configured": the list is also emptied
        # by the assembler's permission filter, so that wording can be false.
        assert "No widgets to show" in result

    def test_render_contributor_widgets_unknown_widget(self) -> None:
        """Unregistered widget type renders placeholder card."""
        registry = WidgetRegistry()
        widget = DashboardWidgetDefinition(
            name="test-widget",
            title="Test Widget",
            contributor="test",
            description="A test widget",
            category=WidgetCategory.METRICS,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/test/widget",
            view_kind=WidgetKind.STAT,
        )
        result = registry.render_contributor_widgets([widget])
        assert "Test Widget" in result
        assert "widget-card" in result

    def test_widget_dom_ids_are_scoped_normalized_and_stable(self) -> None:
        widget = DashboardWidgetDefinition(
            name="Sales / EU",
            title="Sales",
            contributor="test",
            category=WidgetCategory.METRICS,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/sales",
            view_kind=WidgetKind.STAT,
        )
        registry = WidgetRegistry()

        first = registry.render_contributor_widgets([widget])
        second = registry.render_contributor_widgets([widget])
        ids = re.findall(r' id="([^"]+)"', first)

        assert first == second
        assert ids
        assert all(re.fullmatch(r"[a-z][a-z0-9-]*", value) for value in ids)
        assert "Sales / EU" not in ids

    def test_duplicate_widget_names_fail_before_emitting_duplicate_ids(self) -> None:
        widget = DashboardWidgetDefinition(
            name="sales",
            title="Sales",
            contributor="test",
            category=WidgetCategory.METRICS,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/sales",
            view_kind=WidgetKind.STAT,
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            WidgetRegistry().render_contributor_widgets([widget, widget])

    def test_render_contributor_widgets_contributor_label(self) -> None:
        """Widget card includes contributor name and description."""
        registry = WidgetRegistry()
        widget = DashboardWidgetDefinition(
            name="test-widget",
            title="Test Widget",
            description="Widget description",
            category=WidgetCategory.METRICS,
            size=WidgetSize.SMALL,
            contributor="test-contributor",
            render_endpoint="/admin/test/widget",
            view_kind=WidgetKind.STAT,
        )
        result = registry.render_contributor_widgets([widget])
        assert "test-contributor" in result
        assert "Widget description" in result

    def test_render_contributor_widgets_refresh_interval(self) -> None:
        """Widget with refresh interval includes hx-trigger for polling."""
        registry = WidgetRegistry()
        widget = DashboardWidgetDefinition(
            name="polling-widget",
            title="Polling Widget",
            contributor="test",
            category=WidgetCategory.METRICS,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/test/poll",
            refresh_interval_seconds=30,
            view_kind=WidgetKind.STAT,
        )
        result = registry.render_contributor_widgets([widget])
        assert "every 30000ms" in result
        assert "hx-trigger" in result

    def test_render_contributor_widgets_multiple(self) -> None:
        """Multiple widgets are rendered consecutively."""
        registry = WidgetRegistry()
        widgets = [
            DashboardWidgetDefinition(
                name="widget-a",
                title="Widget A",
                contributor="test",
                category=WidgetCategory.METRICS,
                size=WidgetSize.SMALL,
                render_endpoint="/admin/widget/a",
                view_kind=WidgetKind.STAT,
            ),
            DashboardWidgetDefinition(
                name="widget-b",
                title="Widget B",
                contributor="test",
                category=WidgetCategory.METRICS,
                size=WidgetSize.MEDIUM,
                render_endpoint="/admin/widget/b",
                view_kind=WidgetKind.STAT,
            ),
        ]
        result = registry.render_contributor_widgets(widgets)
        assert "Widget A" in result
        assert "Widget B" in result
        assert "lg:col-span-2" in result  # MEDIUM size spans 2 columns

    def test_render_contributor_widgets_live_resource_drops_polling(self) -> None:
        """A live-resource widget gets no hx-trigger poll interval, only load + live-refresh."""
        registry = WidgetRegistry()
        widget = DashboardWidgetDefinition(
            name="live-widget",
            title="Live Widget",
            contributor="test",
            category=WidgetCategory.ACTIVITY,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/test/live",
            refresh_interval_seconds=15,
            live_resource_types=("*",),
            view_kind=WidgetKind.TABLE,
        )
        result = registry.render_contributor_widgets([widget])
        assert "every 15000ms" not in result
        assert "live-refresh" in result
        assert 'data-live-resources="*"' in result

    def test_render_contributor_widgets_live_resource_emits_shared_script(self) -> None:
        """Exactly one EventSource script is emitted regardless of widget count."""
        registry = WidgetRegistry()
        widgets = [
            DashboardWidgetDefinition(
                name=f"live-{i}",
                title=f"Live {i}",
                contributor="test",
                category=WidgetCategory.ACTIVITY,
                size=WidgetSize.SMALL,
                render_endpoint=f"/admin/test/live{i}",
                live_resource_types=("users",),
                view_kind=WidgetKind.TABLE,
            )
            for i in range(3)
        ]
        result = registry.render_contributor_widgets(widgets)
        assert result.count("new EventSource(") == 1

    def test_live_event_source_serializes_the_admin_prefix(self) -> None:
        widget = DashboardWidgetDefinition(
            name="live-widget",
            title="Live Widget",
            contributor="test",
            category=WidgetCategory.ACTIVITY,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/test/live",
            live_resource_types=("users",),
            view_kind=WidgetKind.TABLE,
        )
        payload = "';</script><script>alert(1)</script>"
        result = WidgetRegistry().render_contributor_widgets(
            [widget],
            admin_prefix=payload,
        )

        assert payload not in result
        assert "\\u003c/script\\u003e" in result
        assert result.count("<script>") == 2

    def test_render_contributor_widgets_no_live_resource_no_script(self) -> None:
        """A dashboard with only polling widgets emits no EventSource script."""
        registry = WidgetRegistry()
        widget = DashboardWidgetDefinition(
            name="poll-only",
            title="Poll Only",
            contributor="test",
            category=WidgetCategory.METRICS,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/test/poll",
            refresh_interval_seconds=30,
            view_kind=WidgetKind.STAT,
        )
        result = registry.render_contributor_widgets([widget])
        assert "new EventSource(" not in result

    def test_render_contributor_widgets_live_script_reads_nested_resource_type(
        self,
    ) -> None:
        """The dispatch script reads resource_type from the wire payload shape.

        The SSE frame carries AdminEvent.to_dict() JSON: {event, data:
        {..., resource_type, resource_id}, id} — resource_type is nested
        under `data`, so the lookup must be data.data.resource_type.
        Reading data.resource_type directly is always undefined and
        silently disables the exact-match branch (only the '*' wildcard
        would still fire).
        """
        registry = WidgetRegistry()
        widget = DashboardWidgetDefinition(
            name="live-widget",
            title="Live Widget",
            contributor="test",
            category=WidgetCategory.ACTIVITY,
            size=WidgetSize.SMALL,
            render_endpoint="/admin/test/live",
            live_resource_types=("users",),
            view_kind=WidgetKind.TABLE,
        )
        result = registry.render_contributor_widgets([widget])
        assert "(data.data||{}).resource_type" in result
        assert "var resourceType=data.resource_type;" not in result
