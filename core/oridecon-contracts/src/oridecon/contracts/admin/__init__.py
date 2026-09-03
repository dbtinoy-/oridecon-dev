"""Admin contracts — protocols and types for the admin contributor system."""

from __future__ import annotations

from oridecon.contracts.admin.action_hooks import ActionHookProtocol, HasActionHooks
from oridecon.contracts.admin.audit_entry import AuditEntry, AuditOutcome
from oridecon.contracts.admin.audit_logger import AdminAuditLoggerProtocol
from oridecon.contracts.admin.cache_provider import CacheProviderProtocol
from oridecon.contracts.admin.contributor import BaseAdminContributor
from oridecon.contracts.admin.cqrs import AdminCommand, AdminQuery
from oridecon.contracts.admin.errors import (
    AdminError,
    HealthCheckNotFoundError,
    WidgetNotFoundError,
)
from oridecon.contracts.admin.health_payload import HealthCheckPayload
from oridecon.contracts.admin.operations import (
    AdminSearchableProtocol,
    AggregatableProtocol,
    AuditableProtocol,
    BulkOperationsProtocol,
    CacheAwareProtocol,
    ExportableProtocol,
    RelationLoaderProtocol,
    TransactionalProtocol,
    ValidatableProtocol,
)
from oridecon.contracts.admin.page_content import PageContent, PaginationContent
from oridecon.contracts.admin.page_handler import (
    AdminPageHandlerProtocol,
    ManagementPageHandler,
)
from oridecon.contracts.admin.pii_redactor import PiiRedactorProtocol
from oridecon.contracts.admin.principal import (
    AdminPrincipal,
    AdminPrincipalProviderProtocol,
)
from oridecon.contracts.admin.protocols import (
    AdminContributorProtocol,
    AdminContributorRegistryProtocol,
    AdminDashboardProtocol,
)
from oridecon.contracts.admin.repository import AdminRepositoryProtocol
from oridecon.contracts.admin.route_spec import AdminRouteSpec
from oridecon.contracts.admin.stats import (
    CacheStatsProtocol,
    DlqStatsProtocol,
    HealthOverviewProtocol,
    MetricsReadbackProtocol,
    NamedHealthCheckProtocol,
    QueueStatsProtocol,
    SessionCountProtocol,
)
from oridecon.contracts.admin.types import (
    AdminActionDefinition,
    AdminHealthDefinition,
    DashboardWidgetDefinition,
    ManagementPageDefinition,
    NavigationContribution,
    PageCategory,
    PageFilterField,
    SettingsPanelDefinition,
    WidgetCategory,
    WidgetParams,
    WidgetSize,
    WidgetViewModel,
)
from oridecon.contracts.admin.widget_content import (
    ChartContent,
    ChartPoint,
    EmptyContent,
    MessageContent,
    Stat,
    StatContent,
    TableCell,
    TableContent,
    Tone,
    WidgetContent,
    WidgetKind,
)
from oridecon.contracts.admin.widget_protocols import WidgetHandlerProtocol
from oridecon.contracts.data.data_source import DataSourceProtocol

__all__ = [
    "ActionHookProtocol",
    "AdminActionDefinition",
    "AdminAuditLoggerProtocol",
    "AdminCommand",
    "AdminContributorProtocol",
    "AdminContributorRegistryProtocol",
    "AdminDashboardProtocol",
    "AdminError",
    "AdminHealthDefinition",
    "AdminPageHandlerProtocol",
    "AdminPrincipal",
    "AdminPrincipalProviderProtocol",
    "AdminQuery",
    "AdminRepositoryProtocol",
    "AdminRouteSpec",
    "AdminSearchableProtocol",
    "AggregatableProtocol",
    "AuditEntry",
    "AuditOutcome",
    "AuditableProtocol",
    "BaseAdminContributor",
    "BulkOperationsProtocol",
    "CacheAwareProtocol",
    "CacheProviderProtocol",
    "CacheStatsProtocol",
    "ChartContent",
    "ChartPoint",
    "DashboardWidgetDefinition",
    "DataSourceProtocol",
    "DlqStatsProtocol",
    "EmptyContent",
    "ExportableProtocol",
    "HasActionHooks",
    "HealthCheckNotFoundError",
    "HealthCheckPayload",
    "HealthOverviewProtocol",
    "ManagementPageDefinition",
    "ManagementPageHandler",
    "MessageContent",
    "MetricsReadbackProtocol",
    "NamedHealthCheckProtocol",
    "NavigationContribution",
    "PageCategory",
    "PageContent",
    "PageFilterField",
    "PaginationContent",
    "PiiRedactorProtocol",
    "QueueStatsProtocol",
    "RelationLoaderProtocol",
    "SessionCountProtocol",
    "SettingsPanelDefinition",
    "Stat",
    "StatContent",
    "TableCell",
    "TableContent",
    "Tone",
    "TransactionalProtocol",
    "ValidatableProtocol",
    "WidgetCategory",
    "WidgetContent",
    "WidgetHandlerProtocol",
    "WidgetKind",
    "WidgetNotFoundError",
    "WidgetParams",
    "WidgetSize",
    "WidgetViewModel",
]
