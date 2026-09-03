"""Web security configuration facade.

Re-exports every public name so that
``from oridecon.web.security.config import X`` continues to work unchanged.
"""

from oridecon.web.security.config.cors import CORSConfig as CORSConfig
from oridecon.web.security.config.csp import CSPConfig as CSPConfig
from oridecon.web.security.config.csrf import CSRFConfig as CSRFConfig
from oridecon.web.security.config.headers import (
    CrossOriginConfig as CrossOriginConfig,
)
from oridecon.web.security.config.headers import (
    HSTSConfig as HSTSConfig,
)
from oridecon.web.security.config.headers import (
    SecurityHeadersConfig as SecurityHeadersConfig,
)
from oridecon.web.security.config.top_level import SecurityConfig as SecurityConfig

__all__ = [
    "CORSConfig",
    "CSPConfig",
    "CSRFConfig",
    "CrossOriginConfig",
    "HSTSConfig",
    "SecurityConfig",
    "SecurityHeadersConfig",
]
