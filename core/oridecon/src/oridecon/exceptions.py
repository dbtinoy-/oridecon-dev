"""Public exception facade for the oridecon framework.

Provides two layers of exceptions:

1. **Contracts base exceptions** — imported directly from ``oridecon-contracts``
   so application code can catch at the right level without knowing the deep
   import path::

       from oridecon.exceptions import DomainError, InfrastructureError

2. **Framework leaf exceptions** — raised by the core framework for
   configuration, DI, and validation failures::

       from oridecon.exceptions import ConfigurationError, InjectionError

All exceptions ultimately inherit from ``OrideconError`` so a single
``except OrideconError`` covers the entire hierarchy.

Note: ``ValidationError`` and ``SerializationError`` each have two definitions
in the monorepo (here and in ``oridecon-contracts``).  Use the contracts
versions for domain-layer code; the versions here are framework-internal.
This duplication is tracked as a known cleanup item.

See AGENTS.md §3.3 for error-handling rules.
"""

from __future__ import annotations

# -- Contracts base exceptions (re-exported for convenience) -----------------
from oridecon.contracts.exceptions.base import OrideconError as OrideconError
from oridecon.contracts.exceptions.container import (
    ContainerError as ContainerError,
)
from oridecon.contracts.exceptions.domain import DomainError as DomainError
from oridecon.contracts.exceptions.domain import NotFoundError as NotFoundError
from oridecon.contracts.exceptions.infra import (
    InfrastructureError as InfrastructureError,
)
from oridecon.contracts.exceptions.provider import ProviderError as ProviderError

# -- Framework leaf exceptions -----------------------------------------------


class OrideconException(OrideconError):  # noqa: N818
    """Base exception for all oridecon domain errors.

    Extends :class:`~oridecon.contracts.exceptions.base.OrideconError` so
    that ``isinstance(exc, OrideconError)`` holds for every framework
    exception, enabling unified handling across all packages.

    Use for catchable, domain-level failures such as configuration
    validation, dependency-injection resolution, input validation, and
    domain-model invariant violations.  For infrastructure failures
    (database, network, I/O), raise the exception directly without
    wrapping it in this hierarchy.

    Example::

        try:
            service = await container.resolve(MyService)
        except OrideconException as e:
            logger.error("resolution_failed", error=str(e))
            raise
    """

    _code: str = "ORI_ERR_CORE_002"


class ConfigurationError(OrideconException):
    """Configuration loading, parsing, or validation failed.

    Raised by:

    - ``ConfigProvider`` during initialisation
    - Config loaders when sources are invalid
    - Validation of ``ConfigProtocol`` implementations
    """

    _code: str = "ORI_ERR_CFG_002"


class InjectionError(OrideconException):
    """Dependency injection or container resolution failed.

    Raised by:

    - ``Container.resolve()`` when a service is not registered
    - ``Provider.register()`` on configuration errors
    - Module resolution when imports fail
    - Circular dependency detection
    """

    _code: str = "ORI_ERR_DI_010"


class ValidationError(OrideconException):
    """Input validation against rules failed.

    Raised by:

    - ``ValidatorImpl.validate()`` when rules do not pass
    - ``validate_input()`` decorator
    - Field coercion errors
    """

    _code: str = "ORI_ERR_VAL_003"


class SerializationError(OrideconException):
    """JSON serialisation or deserialisation failed.

    Raised by:

    - ``JsonSerializer`` implementations
    - Domain model serialisation
    - Schema validation during decode
    """

    _code: str = "ORI_ERR_SERIAL_002"


class DomainModelError(OrideconException):
    """Domain model invariant violated or business rule broken.

    Raised by:

    - Domain event handlers
    - Aggregate root validations
    - Entity lifecycle violations
    """

    _code: str = "ORI_ERR_DOM_008"


__all__ = [
    "ConfigurationError",
    "ContainerError",
    "DomainError",
    "DomainModelError",
    "InfrastructureError",
    "InjectionError",
    "OrideconError",
    "OrideconException",
    "NotFoundError",
    "ProviderError",
    "SerializationError",
    "ValidationError",
]
