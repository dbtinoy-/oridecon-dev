from oridecon.admin.ui.organisms.data_table import DataTable
from oridecon.ui import Zones
from oridecon.ui.columns.types import TextColumn


def test_pagination_does_not_duplicate():
    cols = [TextColumn("id"), TextColumn("name")]
    # initial data for page 1
    data = [{"id": i, "name": f"name{i}"} for i in range(1, 11)]

    dt = DataTable(columns=cols, data=data, total=100, resource_prefix="/admin/posts")

    pagination_id = Zones.table_zone_id(
        Zones.PAGINATION,
        table_key="/admin/posts",
    )
    marker = f'id="{pagination_id}"'

    html1 = str(dt.render())
    assert html1.count(marker) == 1

    # Simulate moving to next page / filter change and re-render
    dt.state.page = 2
    dt.data = [{"id": i, "name": f"name{i}"} for i in range(11, 21)]
    html2 = str(dt.render())
    assert html2.count(marker) == 1

    # Simulate a sort/filter change
    dt.state.sort_by = "name"
    html3 = str(dt.render())
    assert html3.count(marker) == 1
