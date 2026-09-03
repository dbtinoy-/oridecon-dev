"""Config panel UI subsystem for the Configuration Center.

This package contains all UI-layer components for the admin configuration
panel: node definitions, spec registry, category types, layout, dashboard UI,
controller, and the built-in spec registrations.

Public exports for the settings panel. Spec bindings and models are imported
by spec modules, not re-exported here.
"""

from __future__ import annotations

from oridecon.admin.settings.panel.branding_spec import BrandingSpec
from oridecon.admin.settings.panel.branding_spec import (
    register_spec as register_branding_spec,
)
from oridecon.admin.settings.panel.cache_spec import CacheSpec
from oridecon.admin.settings.panel.cache_spec import (
    register_spec as register_cache_spec,
)
from oridecon.admin.settings.panel.deployment_spec import DeploymentInfoSpec
from oridecon.admin.settings.panel.deployment_spec import (
    register_spec as register_deployment_spec,
)
from oridecon.admin.settings.panel.features_spec import FeaturesSpec
from oridecon.admin.settings.panel.features_spec import (
    register_spec as register_features_spec,
)
from oridecon.admin.settings.panel.i18n_spec import I18nSpec
from oridecon.admin.settings.panel.i18n_spec import register_spec as register_i18n_spec
from oridecon.admin.settings.panel.layout import ConfigLayout
from oridecon.admin.settings.panel.nodes import (
    AbstractConfigNode,
    BooleanNode,
    ColorNode,
    ConfigSpec,
    ConfigSpecMeta,
    EnumNode,
    IntNode,
    PydanticConfigSpec,
    SecretNode,
    StringNode,
)
from oridecon.admin.settings.panel.profiler_spec import ProfilerSpec
from oridecon.admin.settings.panel.profiler_spec import (
    register_spec as register_profiler_spec,
)
from oridecon.admin.settings.panel.rate_limit_spec import RateLimitSpec
from oridecon.admin.settings.panel.rate_limit_spec import (
    register_spec as register_rate_limit_spec,
)
from oridecon.admin.settings.panel.rbac_spec import RBACSpec
from oridecon.admin.settings.panel.rbac_spec import register_spec as register_rbac_spec
from oridecon.admin.settings.panel.registry import (
    ConfigRegistry,
    EnvStore,
    MemoryStore,
    StoreBase,
)
from oridecon.admin.settings.panel.security_spec import SecuritySpec
from oridecon.admin.settings.panel.security_spec import (
    register_spec as register_security_spec,
)
from oridecon.admin.settings.panel.types import ConfigCategory
from oridecon.admin.settings.panel.ui import ConfigDashboardUI

__all__ = [
    "AbstractConfigNode",
    "BooleanNode",
    "BrandingSpec",
    "CacheSpec",
    "ColorNode",
    "ConfigCategory",
    "ConfigDashboardUI",
    "ConfigLayout",
    "ConfigRegistry",
    "ConfigSpec",
    "ConfigSpecMeta",
    "DeploymentInfoSpec",
    "EnumNode",
    "EnvStore",
    "FeaturesSpec",
    "I18nSpec",
    "IntNode",
    "MemoryStore",
    "ProfilerSpec",
    "PydanticConfigSpec",
    "RBACSpec",
    "RateLimitSpec",
    "SecretNode",
    "SecuritySpec",
    "StoreBase",
    "StringNode",
    "register_branding_spec",
    "register_cache_spec",
    "register_deployment_spec",
    "register_features_spec",
    "register_i18n_spec",
    "register_profiler_spec",
    "register_rate_limit_spec",
    "register_rbac_spec",
    "register_security_spec",
]
