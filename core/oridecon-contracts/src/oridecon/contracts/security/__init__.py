"""Security contracts for Oridecon Framework.

Provides protocols and types for security-related concerns, including
secret management, guards, input sanitization, and response headers.
"""

from __future__ import annotations

from oridecon.contracts.exceptions.components import (
    SecretNotFoundError,
)
from oridecon.contracts.exceptions.security import (
    CORSViolationError,
    GuardDeniedError,
    InputSanitizationError,
    SecretAccessError,
    SecurityError,
)
from oridecon.contracts.security.protocols import (
    CORSProtocol,
    CSPProtocol,
    CSRFProtocol,
    EncryptionProtocol,
    GuardChainProtocol,
    HasherProtocol,
    InputSanitizerProtocol,
    KeyDerivationProtocol,
    SecurityHeadersProtocol,
)
from oridecon.contracts.security.rotation import SecretRotationPolicy
from oridecon.contracts.security.secrets import (
    SecretStoreProtocol,
)
from oridecon.contracts.security.stores import AsyncSecretStoreProtocol
from oridecon.contracts.security.url_safety import (
    HostResolver,
    is_safe_url_for_request,
    resolve_hostname,
)

__all__ = [
    "AsyncSecretStoreProtocol",
    "CORSProtocol",
    "CORSViolationError",
    "CSPProtocol",
    "CSRFProtocol",
    "EncryptionProtocol",
    "GuardChainProtocol",
    "GuardDeniedError",
    "HasherProtocol",
    "HostResolver",
    "InputSanitizationError",
    "InputSanitizerProtocol",
    "KeyDerivationProtocol",
    "SecretAccessError",
    "SecretNotFoundError",
    "SecretRotationPolicy",
    "SecretStoreProtocol",
    "SecurityError",
    "SecurityHeadersProtocol",
    "is_safe_url_for_request",
    "resolve_hostname",
]
