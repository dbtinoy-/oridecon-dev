"""Admin configuration package — re-exports the full public surface."""

from __future__ import annotations

from oridecon.admin.config.app import AdminConfig as AdminConfig
from oridecon.admin.config.app import default_admin_config as default_admin_config
from oridecon.admin.config.app import make_admin_config as make_admin_config
from oridecon.admin.config.auth import AdminAuthConfig as AdminAuthConfig
from oridecon.admin.config.auth import AdminEmailOtpConfig as AdminEmailOtpConfig
from oridecon.admin.config.auth import (
    AdminEmailVerificationConfig as AdminEmailVerificationConfig,
)
from oridecon.admin.config.auth import AdminMfaConfig as AdminMfaConfig
from oridecon.admin.config.auth import (
    AdminRegistrationConfig as AdminRegistrationConfig,
)
from oridecon.admin.config.defaults import AdminNavigationGroup as AdminNavigationGroup
from oridecon.admin.config.defaults import FormDefaults as FormDefaults
from oridecon.admin.config.defaults import ResourceDefaults as ResourceDefaults
from oridecon.admin.config.defaults import ResourceYAMLConfig as ResourceYAMLConfig
from oridecon.admin.config.defaults import TableDefaults as TableDefaults
from oridecon.admin.config.features import AdminFeaturesConfig as AdminFeaturesConfig
from oridecon.admin.config.features import ContributorConfig as ContributorConfig
from oridecon.admin.config.features import FrameworkPagesConfig as FrameworkPagesConfig
from oridecon.admin.config.integrations import (
    AdminIntegrationsConfig as AdminIntegrationsConfig,
)
from oridecon.admin.config.integrations import (
    CacheIntegrationConfig as CacheIntegrationConfig,
)
from oridecon.admin.config.integrations import (
    FeaturesIntegrationConfig as FeaturesIntegrationConfig,
)
from oridecon.admin.config.integrations import (
    MonitorIntegrationConfig as MonitorIntegrationConfig,
)
from oridecon.admin.config.integrations import (
    ResilienceIntegrationConfig as ResilienceIntegrationConfig,
)
from oridecon.admin.config.integrations import (
    SearchIntegrationConfig as SearchIntegrationConfig,
)
from oridecon.admin.config.integrations import (
    StorageIntegrationConfig as StorageIntegrationConfig,
)
from oridecon.admin.config.integrations import (
    TasksIntegrationConfig as TasksIntegrationConfig,
)
from oridecon.admin.config.observability import (
    AdminNotificationConfig as AdminNotificationConfig,
)
from oridecon.admin.config.observability import (
    AdminObservabilityConfig as AdminObservabilityConfig,
)
from oridecon.admin.config.observability import AdminStorageConfig as AdminStorageConfig
from oridecon.admin.config.security import AdminAuditConfig as AdminAuditConfig
from oridecon.admin.config.security import (
    AdminPasswordPolicyConfig as AdminPasswordPolicyConfig,
)
from oridecon.admin.config.security import AdminRateLimitConfig as AdminRateLimitConfig
from oridecon.admin.config.security import AdminRbacConfig as AdminRbacConfig
from oridecon.admin.config.security import AdminSecurityConfig as AdminSecurityConfig
from oridecon.admin.config.tenancy import TenancyConfig as TenancyConfig
from oridecon.admin.config.ui import AdminClustersConfig as AdminClustersConfig
from oridecon.admin.config.ui import AdminDataConfig as AdminDataConfig
from oridecon.admin.config.ui import AdminUIConfig as AdminUIConfig
from oridecon.admin.config.ui import ClusterSpec as ClusterSpec
from oridecon.admin.config.ui import DashboardLayoutConfig as DashboardLayoutConfig
from oridecon.admin.resources.config import ResourceConfig as ResourceConfig
from oridecon.admin.resources.config import TableConfiguration as TableConfiguration

__all__ = [
    "AdminAuditConfig",
    "AdminAuthConfig",
    "AdminClustersConfig",
    "AdminConfig",
    "AdminDataConfig",
    "AdminEmailOtpConfig",
    "AdminEmailVerificationConfig",
    "AdminFeaturesConfig",
    "AdminIntegrationsConfig",
    "AdminMfaConfig",
    "AdminNavigationGroup",
    "AdminNotificationConfig",
    "AdminObservabilityConfig",
    "AdminPasswordPolicyConfig",
    "AdminRateLimitConfig",
    "AdminRbacConfig",
    "AdminRegistrationConfig",
    "AdminSecurityConfig",
    "AdminStorageConfig",
    "AdminUIConfig",
    "CacheIntegrationConfig",
    "ClusterSpec",
    "ContributorConfig",
    "DashboardLayoutConfig",
    "FeaturesIntegrationConfig",
    "FormDefaults",
    "FrameworkPagesConfig",
    "MonitorIntegrationConfig",
    "ResilienceIntegrationConfig",
    "ResourceConfig",
    "ResourceDefaults",
    "ResourceYAMLConfig",
    "SearchIntegrationConfig",
    "StorageIntegrationConfig",
    "TableConfiguration",
    "TableDefaults",
    "TasksIntegrationConfig",
    "TenancyConfig",
    "default_admin_config",
    "make_admin_config",
]
