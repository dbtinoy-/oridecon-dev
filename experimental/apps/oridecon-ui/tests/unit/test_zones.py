"""Tests for UI zones module."""

import pytest

from oridecon.ui import RenderScope
from oridecon.ui.core.zones import SwapMode, Zone, Zones


class TestSwapMode:
    def test_swap_mode_values(self) -> None:
        assert SwapMode.OUTER_HTML.value == "outerHTML"
        assert SwapMode.INNER_HTML.value == "innerHTML"
        assert SwapMode.BEFORE_END.value == "beforeend"
        assert SwapMode.AFTER_BEGIN.value == "afterbegin"
        assert SwapMode.NONE.value == "none"


class TestZone:
    def test_zone_creation(self) -> None:
        zone = Zone(
            id="test-zone",
            description="Test zone",
            swappable=True,
            swap_mode=SwapMode.INNER_HTML,
        )
        assert zone.id == "test-zone"
        assert zone.swappable is True
        assert zone.swap_mode == SwapMode.INNER_HTML

    def test_zone_selector(self) -> None:
        zone = Zone(
            id="my-zone",
            description="Test",
            swappable=True,
            swap_mode=SwapMode.OUTER_HTML,
        )
        assert zone.selector == "#my-zone"

    def test_zone_str(self) -> None:
        zone = Zone(id="test", description="", swappable=True, swap_mode=SwapMode.NONE)
        assert str(zone) == "test"

    def test_zone_repr(self) -> None:
        zone = Zone(id="test", description="", swappable=True, swap_mode=SwapMode.NONE)
        assert repr(zone) == "Zone('test')"

    def test_zone_preserve_alpine_default(self) -> None:
        zone = Zone(id="test", description="", swappable=True, swap_mode=SwapMode.NONE)
        assert zone.preserve_alpine is False

    def test_zone_oob_only_default(self) -> None:
        zone = Zone(id="test", description="", swappable=True, swap_mode=SwapMode.NONE)
        assert zone.oob_only is False


class TestZones:
    def test_table_zone(self) -> None:
        assert Zones.TABLE.id == "oridecon-table"
        assert Zones.TABLE.swappable is True
        assert Zones.TABLE.swap_mode == SwapMode.OUTER_HTML

    def test_data_zone(self) -> None:
        assert Zones.DATA.id == "table-data"
        assert Zones.DATA.swappable is True
        assert Zones.DATA.swap_mode == SwapMode.INNER_HTML
        assert Zones.DATA.preserve_alpine is True

    def test_toolbar_zone_oob_only(self) -> None:
        assert Zones.TOOLBAR.oob_only is True

    def test_search_zone_not_swappable(self) -> None:
        assert Zones.SEARCH.swappable is False
        assert Zones.SEARCH.swap_mode == SwapMode.NONE

    def test_table_scope_resolves_stable_role_ids_and_restores_defaults(self) -> None:
        scope = RenderScope()

        with Zones.table_scope(scope, "orders"):
            resolved = {
                "table": Zones.TABLE.id,
                "data": Zones.DATA.id,
                "select_all": Zones.SELECT_ALL.id,
            }
            assert resolved == {
                "table": "oridecon-table-orders",
                "data": "oridecon-table-data-orders",
                "select_all": "oridecon-table-select-all-orders",
            }
            assert Zones.data_refresh_oob_select() == (
                "#oridecon-table-toolbar-orders-switchers,"
                "#oridecon-table-scope-tabs-orders"
            )

        assert Zones.TABLE.id == "oridecon-table"
        assert Zones.DATA.id == "table-data"

        with Zones.table_scope(RenderScope(), "orders"):
            assert Zones.TABLE.id == resolved["table"]
            assert Zones.DATA.id == resolved["data"]

    def test_table_scope_rejects_duplicate_explicit_key_in_one_response(self) -> None:
        scope = RenderScope()
        with Zones.table_scope(scope, "orders"):
            pass

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            with Zones.table_scope(scope, "orders"):
                pass

    def test_table_zone_id_matches_render_scope_contract(self) -> None:
        assert Zones.table_zone_id(Zones.DATA, table_key="orders") == (
            "oridecon-table-data-orders"
        )
        with pytest.raises(ValueError, match="not scoped"):
            Zones.table_zone_id(Zones.FLASH, table_key="orders")

    def test_all_zones_returns_list(self) -> None:
        zones = Zones.all_zones()
        assert isinstance(zones, list)
        assert len(zones) == 14

    def test_swappable_zones(self) -> None:
        swappable = Zones.swappable()
        assert Zones.TABLE in swappable
        assert Zones.DATA in swappable
        assert Zones.SEARCH not in swappable

    def test_get_by_id_exists(self) -> None:
        zone = Zones.get_by_id("table-data")
        assert zone is not None
        assert zone.id == "table-data"

    def test_get_by_selector_with_hash(self) -> None:
        zone = Zones.get_by_selector("#table-data")
        assert zone is not None
        assert zone.id == "table-data"

    def test_get_by_selector_without_hash(self) -> None:
        zone = Zones.get_by_selector("table-data")
        assert zone is not None
        assert zone.id == "table-data"

    def test_dashboard_grid_zone(self) -> None:
        assert Zones.DASHBOARD_GRID.id == "dashboard-grid"
        assert Zones.DASHBOARD_GRID.swappable is True
        assert Zones.DASHBOARD_GRID.swap_mode == SwapMode.INNER_HTML

    def test_widget_container_zone(self) -> None:
        assert Zones.WIDGET_CONTAINER.id == "widget-container"
        assert Zones.WIDGET_CONTAINER.swappable is True
        assert Zones.WIDGET_CONTAINER.swap_mode == SwapMode.INNER_HTML
        assert Zones.WIDGET_CONTAINER.preserve_alpine is True

    def test_all_zones_includes_dashboard(self) -> None:
        zones = Zones.all_zones()
        assert Zones.DASHBOARD_GRID in zones
        assert Zones.WIDGET_CONTAINER in zones

    def test_get_by_id_not_exists(self) -> None:
        zone = Zones.get_by_id("nonexistent")
        assert zone is None
