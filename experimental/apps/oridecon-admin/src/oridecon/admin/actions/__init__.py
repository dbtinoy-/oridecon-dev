"""Action managers for Oridecon Admin.

PEP 562 lazy loading to avoid import-time dependency issues.
"""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.admin.actions.audited import AuditedAction
    from oridecon.admin.actions.bulk_manager import (
        BulkActionManager,
        BulkActionProgress,
        BulkActionResult,
        BulkActionSnapshot,
        BulkAssignConfig,
        BulkEditField,
        IBulkDataSource,
    )
    from oridecon.admin.actions.header_manager import (
        ColumnVisibilityConfig,
        DensityConfig,
        HeaderAction,
        HeaderActionManager,
        HeaderActionStyle,
        IHeaderDataSource,
        TableDensity,
    )
    from oridecon.admin.actions.polymorphic import PolymorphicBulkAction
    from oridecon.admin.actions.row_manager import (
        ActionGroup,
        ActionPosition,
        ActionStyle,
        IRowDataSource,
        RowAction,
        RowActionManager,
    )
    from oridecon.admin.actions.standard import (
        CloneAction,
        CreateAction,
        DeleteAction,
        DeleteBulkAction,
        EditAction,
        ExportAction,
        ExportBulkAction,
        ImpersonateAction,
        ImportAction,
        ImportBulkAction,
        PermissionsAction,
        PurgeAction,
        PurgeBulkAction,
        RestoreAction,
        RestoreBulkAction,
        ViewAction,
    )

_EXPORTS = {
    # standard
    "EditAction": "oridecon.admin.actions.standard",
    "ViewAction": "oridecon.admin.actions.standard",
    "DeleteAction": "oridecon.admin.actions.standard",
    "CreateAction": "oridecon.admin.actions.standard",
    "DeleteBulkAction": "oridecon.admin.actions.standard",
    "PurgeBulkAction": "oridecon.admin.actions.standard",
    "RestoreBulkAction": "oridecon.admin.actions.standard",
    "CloneAction": "oridecon.admin.actions.standard",
    "RestoreAction": "oridecon.admin.actions.standard",
    "PurgeAction": "oridecon.admin.actions.standard",
    "ExportAction": "oridecon.admin.actions.standard",
    "ExportBulkAction": "oridecon.admin.actions.standard",
    "ImportAction": "oridecon.admin.actions.standard",
    "ImportBulkAction": "oridecon.admin.actions.standard",
    "PermissionsAction": "oridecon.admin.actions.standard",
    "ImpersonateAction": "oridecon.admin.actions.standard",
    # audited
    "AuditedAction": "oridecon.admin.actions.audited",
    # polymorphic
    "PolymorphicBulkAction": "oridecon.admin.actions.polymorphic",
    # bulk_manager
    "IBulkDataSource": "oridecon.admin.actions.bulk_manager",
    "BulkEditField": "oridecon.admin.actions.bulk_manager",
    "BulkAssignConfig": "oridecon.admin.actions.bulk_manager",
    "BulkActionResult": "oridecon.admin.actions.bulk_manager",
    "BulkActionSnapshot": "oridecon.admin.actions.bulk_manager",
    "BulkActionProgress": "oridecon.admin.actions.bulk_manager",
    "BulkActionManager": "oridecon.admin.actions.bulk_manager",
    # header_manager
    "HeaderActionStyle": "oridecon.admin.actions.header_manager",
    "TableDensity": "oridecon.admin.actions.header_manager",
    "HeaderAction": "oridecon.admin.actions.header_manager",
    "ColumnVisibilityConfig": "oridecon.admin.actions.header_manager",
    "DensityConfig": "oridecon.admin.actions.header_manager",
    "IHeaderDataSource": "oridecon.admin.actions.header_manager",
    "HeaderActionManager": "oridecon.admin.actions.header_manager",
    # row_manager
    "ActionStyle": "oridecon.admin.actions.row_manager",
    "ActionPosition": "oridecon.admin.actions.row_manager",
    "RowAction": "oridecon.admin.actions.row_manager",
    "ActionGroup": "oridecon.admin.actions.row_manager",
    "IRowDataSource": "oridecon.admin.actions.row_manager",
    "RowActionManager": "oridecon.admin.actions.row_manager",
    # relation
    "AssociateAction": "oridecon.admin.actions.relation",
    "AttachAction": "oridecon.admin.actions.relation",
    "DetachAction": "oridecon.admin.actions.relation",
    "DissociateAction": "oridecon.admin.actions.relation",
}

__all__ = list(_EXPORTS.keys())


def __getattr__(name: str) -> Any:
    if name in _EXPORTS:
        module = importlib.import_module(_EXPORTS[name], __package__)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> Any:
    return __all__
