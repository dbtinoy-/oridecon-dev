"""Web configuration facade.

Re-exports every public name so that
``from oridecon.web.config import X`` continues to work unchanged.
"""

from oridecon.web.config.api_docs import (
    APIDocsConfig as APIDocsConfig,
)
from oridecon.web.config.api_docs import (
    StaticFileConfig as StaticFileConfig,
)
from oridecon.web.config.provider import WebProviderConfig as WebProviderConfig
from oridecon.web.config.rate_limit import (
    RateLimitConfig as RateLimitConfig,
)
from oridecon.web.config.rate_limit import (
    RateLimitRuleConfig as RateLimitRuleConfig,
)
from oridecon.web.config.rate_limit import (
    RoleGuardConfig as RoleGuardConfig,
)
from oridecon.web.config.rate_limit import (
    RoleGuardRuleConfig as RoleGuardRuleConfig,
)
from oridecon.web.config.server import ServerConfig as ServerConfig
from oridecon.web.config.top_level import WebConfig as WebConfig
from oridecon.web.security.config import (
    CORSConfig as CORSConfig,
)
from oridecon.web.security.config import (
    CrossOriginConfig as CrossOriginConfig,
)
from oridecon.web.security.config import (
    CSPConfig as CSPConfig,
)
from oridecon.web.security.config import (
    CSRFConfig as CSRFConfig,
)
from oridecon.web.security.config import (
    HSTSConfig as HSTSConfig,
)
from oridecon.web.security.config import (
    SecurityConfig as SecurityConfig,
)


def __getattr__(name: str) -> object:  # noqa: ANN001
    if name == "VersioningStrategy":
        from oridecon.web.routing.versioning import VersioningStrategy

        return VersioningStrategy
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "CORSConfig",
    "CrossOriginConfig",
    "CSPConfig",
    "CSRFConfig",
    "HSTSConfig",
    "RateLimitConfig",
    "RateLimitRuleConfig",
    "RoleGuardConfig",
    "RoleGuardRuleConfig",
    "SecurityConfig",
    "ServerConfig",
    "StaticFileConfig",
    "VersioningStrategy",
    "WebConfig",
    "WebProviderConfig",
]
