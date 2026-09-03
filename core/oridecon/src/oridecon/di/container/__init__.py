"""DI container package — Container, Scope, and component facades."""

from __future__ import annotations

from oridecon.di.container.container import Container
from oridecon.di.container.registrar import ContainerRegistrarImpl
from oridecon.di.container.resolver import ContainerResolverImpl
from oridecon.di.container.scope import Scope
from oridecon.di.container.validation import ContainerValidator, OrphanedRegistration

__all__ = [
    "Container",
    "ContainerRegistrarImpl",
    "ContainerResolverImpl",
    "ContainerValidator",
    "OrphanedRegistration",
    "Scope",
]
