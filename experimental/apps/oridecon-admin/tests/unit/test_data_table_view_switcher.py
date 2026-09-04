from oridecon.admin.ui.organisms.data_table import DataTable
from oridecon.ui import Zones
from oridecon.ui.columns.types import TextColumn

_TABLE_ID = Zones.table_zone_id(Zones.TABLE, table_key="/admin/users")
_DATA_ID = Zones.table_zone_id(Zones.DATA, table_key="/admin/users")


def test_view_switcher_singleton_and_htmx_attrs():
    cols = [TextColumn("name")]
    data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    # Stack layout (header placement)
    dt_stack = DataTable(
        columns=cols,
        data=data,
        resource_prefix="/admin/users",
        filter_options={
            "status": {"type": "select", "options": ["active", "inactive"]}
        },
        layout_type="stack",
    )
    out = str(dt_stack.render())

    # Exactly one switcher
    assert out.count('class="view-switcher') == 1
    # Items include data_view query param and target/swap attributes
    assert 'hx-get="/admin/users?data_view=' in out
    assert f'hx-target="#{_TABLE_ID}"' in out
    assert 'hx-swap="outerHTML"' in out
    assert 'hx-push-url="true"' in out

    # Sidebar layout (injected into right column)
    dt_sidebar = DataTable(
        columns=cols,
        data=data,
        resource_prefix="/admin/users",
        filter_options={
            "status": {"type": "select", "options": ["active", "inactive"]}
        },
        layout_type="sidebar",
    )
    out2 = str(dt_sidebar.render())

    assert out2.count('class="view-switcher') == 1
    assert 'hx-get="/admin/users?data_view=' in out2
    assert f'hx-target="#{_TABLE_ID}"' in out2


def test_controls_outside_container_and_filters_below_search():
    cols = [TextColumn("name")]
    data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    dt = DataTable(
        columns=cols,
        data=data,
        resource_prefix="/admin/users",
        filter_options={
            "status": {"type": "select", "options": ["active", "inactive"]}
        },
        layout_type="stack",
    )
    out = str(dt.render())

    # Controls (view-switcher) should appear before the main container to be outside it
    assert out.find('class="view-switcher') < out.find("oridecon-data-table-container")

    # Search input should be present and appear before table content
    assert 'name="search"' in out
    assert out.find('name="search"') < out.find(f'id="{_DATA_ID}"')

    # Filter options (derived from filter_options) should appear in the controls area before the table
    assert 'option value="active"' in out
    assert out.find('option value="active"') < out.find(f'id="{_DATA_ID}"')
