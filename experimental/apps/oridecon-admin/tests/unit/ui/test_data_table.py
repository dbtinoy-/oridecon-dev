import pytest

from oridecon.admin.config import TableConfiguration
from oridecon.admin.resources.base import Resource
from oridecon.admin.resources.config import ResourceConfig
from oridecon.admin.ui.organisms.data_table import DataTable
from oridecon.ui import TrustedHTML, Zones
from oridecon.ui.columns.types import TextColumn
from oridecon.ui.core.base import render_to_string


def test_data_table_attributes_its_serialized_component_output() -> None:
    rendered = DataTable(columns=[TextColumn("name")], data=[]).render()

    assert isinstance(rendered, TrustedHTML)
    assert rendered.source == "structured admin DataTable renderer"


def test_data_table_renders_empty_state_when_no_data():
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[],
        resource_prefix="/admin/users",
    )
    html = render_to_string(dt)
    assert "No results found" in html
    assert "Try adjusting your filters" in html


def test_data_table_empty_state_overrides_honored():
    config = TableConfiguration(
        columns=[TextColumn("name")],
        empty_state_title="Nothing here yet",
        empty_state_message="Create your first record to get started.",
        empty_state_icon="🗂️",
    )
    dt = DataTable(columns=[TextColumn("name")], data=[], config=config)
    html = render_to_string(dt)
    assert "Nothing here yet" in html
    assert "Create your first record to get started." in html
    assert "🗂️" in html
    assert "No results found" not in html


def test_resource_empty_state_class_attrs_flow_through_config():
    class ProductResource(Resource):
        empty_state_title = "No products"
        empty_state_message = "Add your first product."
        empty_state_icon = "📦"

    config = ProductResource.get_table_config()
    assert config.empty_state_title == "No products"
    assert config.empty_state_message == "Add your first product."
    assert config.empty_state_icon == "📦"


def test_resource_header_actions_flow_through_config():
    from oridecon.admin.actions.standard import ImportAction

    class ProductResource(Resource):
        header_actions = [ImportAction()]

    config = ProductResource.get_table_config()
    assert config.header_actions == ProductResource.header_actions


def test_resource_config_fluent_empty_state_flow_through():
    class ProductResource(Resource):
        config = ResourceConfig.builder().empty_state(
            title="No products",
            message="Add your first product.",
            icon="📦",
        )

    config = ProductResource.get_table_config()
    assert config.empty_state_title == "No products"
    assert config.empty_state_message == "Add your first product."
    assert config.empty_state_icon == "📦"


def test_data_table_renders_header_with_search_and_create():
    dt = DataTable(
        columns=[TextColumn("name")],
        data=[],
        resource_prefix="/admin/users",
    )
    html = render_to_string(dt)
    # header should contain search input wrapper and Create button
    assert "Create New" in html
    # Search input should be present
    assert "<input" in html or "Search" in html


def test_sibling_tables_resolve_distinct_internal_zones() -> None:
    def table(key: str) -> DataTable:
        return DataTable(
            columns=[TextColumn("name")],
            data=[{"id": key, "name": key.title()}],
            resource_prefix=f"/admin/{key}",
            total=40,
            table_key=key,
        )

    html = render_to_string([table("orders"), table("customers")])

    for key in ("orders", "customers"):
        table_id = Zones.table_zone_id(Zones.TABLE, table_key=key)
        data_id = Zones.table_zone_id(Zones.DATA, table_key=key)
        assert f'id="{table_id}"' in html
        assert f'id="{data_id}"' in html
        assert f'hx-target="#{data_id}"' in html


def test_table_zones_remain_stable_between_full_and_htmx_renders() -> None:
    def table(*, htmx_request: bool) -> DataTable:
        return DataTable(
            columns=[TextColumn("name")],
            data=[{"id": "1", "name": "Order"}],
            resource_prefix="/admin/orders",
            total=40,
            table_key="orders",
            htmx_request=htmx_request,
        )

    full_html = render_to_string(table(htmx_request=False))
    fragment_html = render_to_string(table(htmx_request=True))

    for zone in (Zones.TABLE, Zones.DATA, Zones.TOOLBAR, Zones.SCOPE_TABS):
        zone_id = Zones.table_zone_id(zone, table_key="orders")
        assert zone_id in full_html
        assert zone_id in fragment_html


def test_sibling_tables_reject_a_duplicate_explicit_table_key() -> None:
    def table() -> DataTable:
        return DataTable(
            columns=[TextColumn("name")],
            data=[],
            table_key="orders",
        )

    with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
        render_to_string([table(), table()])
