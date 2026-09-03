"""Security primitives for the Oridecon Framework.

Transport-agnostic security utilities: guards, encryption, secrets,
and input sanitization.

HTTP-specific middleware (CORS, CSRF, CSP, HSTS, security response headers)
lives in ``oridecon-web`` at ``oridecon.web.security``.
"""

from __future__ import annotations

# -- Exceptions (Task 1) -----------------------------------------------------
from oridecon.contracts.security import SecretNotFoundError as SecretNotFoundError

# -- Hashing (Task 3) --------------------------------------------------------
from oridecon.security.config import HashingConfig as HashingConfig
from oridecon.security.config import SecurityConfig as SecurityConfig

# -- Decorators (Task 2) -----------------------------------------------------
from oridecon.security.decorators import sanitize_input as sanitize_input

# -- Encryption (Task 2) -----------------------------------------------------
from oridecon.security.encryption import EncryptionService as EncryptionService
from oridecon.security.events import CsrfViolationEvent as CsrfViolationEvent
from oridecon.security.events import SecretRotatedEvent as SecretRotatedEvent
from oridecon.security.events import (
    SecurityGuardDeniedEvent as SecurityGuardDeniedEvent,
)

# -- Domain events (Task 2) --------------------------------------------------
from oridecon.security.events import ThreatDetectedEvent as ThreatDetectedEvent
from oridecon.security.exceptions import DecryptionError as DecryptionError
from oridecon.security.exceptions import EncryptionError as EncryptionError
from oridecon.security.exceptions import MiddlewareGuardError as MiddlewareGuardError
from oridecon.security.exceptions import SecretAccessError as SecretAccessError
from oridecon.security.exceptions import SecretError as SecretError
from oridecon.security.exceptions import SecurityError as SecurityError

# -- Guards (Task 2) ---------------------------------------------------------
from oridecon.security.guards import GuardChainImpl as GuardChainImpl
from oridecon.security.guards import use_guards as use_guards
from oridecon.security.hashing import PBKDF2KDF as PBKDF2KDF
from oridecon.security.hashing import Blake2bHasher as Blake2bHasher
from oridecon.security.hashing import Sha256Hasher as Sha256Hasher

# -- Hooks (Task 2) ----------------------------------------------------------
from oridecon.security.hooks import SecurityGuardBlockedHook as SecurityGuardBlockedHook
from oridecon.security.hooks import SecurityGuardPassedHook as SecurityGuardPassedHook
from oridecon.security.hooks import (
    SecurityThreatDetectedHook as SecurityThreatDetectedHook,
)

# -- Provider (Task 2) -------------------------------------------------------
from oridecon.security.provider import SecurityProvider as SecurityProvider

# -- Sanitization (Task 2) ---------------------------------------------------
from oridecon.security.sanitization import InputSanitizer as InputSanitizer
from oridecon.security.secrets import EnvSecretStore as EnvSecretStore
from oridecon.security.secrets import FileSecretStore as FileSecretStore

# -- Secrets (Task 2) --------------------------------------------------------
from oridecon.security.secrets import InMemorySecretStore as InMemorySecretStore
from oridecon.security.secrets import SecretValue as SecretValue

__all__ = [
    "PBKDF2KDF",
    "Blake2bHasher",
    "CsrfViolationEvent",
    "DecryptionError",
    "EncryptionError",
    "EncryptionService",
    "EnvSecretStore",
    "FileSecretStore",
    "GuardChainImpl",
    "HashingConfig",
    "InMemorySecretStore",
    "InputSanitizer",
    "MiddlewareGuardError",
    "SecretAccessError",
    "SecretError",
    "SecretNotFoundError",
    "SecretRotatedEvent",
    "SecretValue",
    "SecurityConfig",
    "SecurityError",
    "SecurityGuardBlockedHook",
    "SecurityGuardDeniedEvent",
    "SecurityGuardPassedHook",
    "SecurityProvider",
    "SecurityThreatDetectedHook",
    "Sha256Hasher",
    "ThreatDetectedEvent",
    "sanitize_input",
    "use_guards",
]
