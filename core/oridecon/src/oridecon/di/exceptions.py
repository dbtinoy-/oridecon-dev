"""Exceptions for the DI subsystem.

Re-exports all container contract exceptions plus the module/provider
error bases.
"""

from __future__ import annotations

from oridecon.contracts.exceptions import ModuleError as ModuleError
from oridecon.contracts.exceptions import ProviderError as ProviderError
from oridecon.contracts.exceptions.container import (
    CircularDependencyError as CircularDependencyError,
)
from oridecon.contracts.exceptions.container import (
    ContainerBuildError as ContainerBuildError,
)
from oridecon.contracts.exceptions.container import ContainerError as ContainerError
from oridecon.contracts.exceptions.container import DependencyError as DependencyError
from oridecon.contracts.exceptions.container import (
    RegistrationError as RegistrationError,
)
from oridecon.contracts.exceptions.container import (
    UnresolvableDependencyError as UnresolvableDependencyError,
)

__all__ = [
    "CircularDependencyError",
    "ContainerBuildError",
    "ContainerError",
    "DependencyError",
    "ModuleError",
    "ProviderError",
    "RegistrationError",
    "UnresolvableDependencyError",
]
