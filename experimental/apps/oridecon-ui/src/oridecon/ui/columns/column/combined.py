from __future__ import annotations

from oridecon.ui.columns.column.base import Column
from oridecon.ui.columns.column.config import ColumnConfigMixin
from oridecon.ui.columns.column.formatting import ColumnFormattingMixin
from oridecon.ui.columns.column.rendering import ColumnRenderingMixin
from oridecon.ui.columns.column.visibility import ColumnVisibilityMixin


class ColumnBase(  # type: ignore[misc]
    Column,
    ColumnConfigMixin,
    ColumnFormattingMixin,
    ColumnVisibilityMixin,
    ColumnRenderingMixin,
):
    """Complete Column base class with all functionality."""
