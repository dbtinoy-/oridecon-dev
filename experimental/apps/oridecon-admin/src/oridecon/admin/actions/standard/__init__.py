"""Standard action implementations for oridecon-admin.

Provides ready-to-use :class:`~oridecon.admin.actions.base.RowAction`,
:class:`~oridecon.admin.actions.base.BulkAction`, and
:class:`~oridecon.admin.actions.base.HeaderAction` subclasses that wrap
common data-source operations such as edit, view, delete, create, and
bulk delete. Each action comes with sensible defaults for name, label,
icon, and color.

Class implementations live in sibling modules grouped by action family
(``row``, ``bulk``, ``header``, ``export``, ``imports``).
"""

from __future__ import annotations

from oridecon.admin.actions.standard.bulk import (
    DeleteBulkAction,
    PurgeBulkAction,
    RestoreBulkAction,
)
from oridecon.admin.actions.standard.export import ExportAction, ExportBulkAction
from oridecon.admin.actions.standard.header import CreateAction
from oridecon.admin.actions.standard.imports import ImportAction, ImportBulkAction
from oridecon.admin.actions.standard.row import (
    CloneAction,
    DeleteAction,
    EditAction,
    ImpersonateAction,
    PermissionsAction,
    PurgeAction,
    RestoreAction,
    ViewAction,
)

__all__ = [
    "CloneAction",
    "CreateAction",
    "DeleteAction",
    "DeleteBulkAction",
    "EditAction",
    "ExportAction",
    "ExportBulkAction",
    "ImpersonateAction",
    "ImportAction",
    "ImportBulkAction",
    "PurgeAction",
    "PurgeBulkAction",
    "RestoreAction",
    "RestoreBulkAction",
    "ViewAction",
]
