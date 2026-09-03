"""Admin contract errors — base exceptions for the admin domain.

Leaf exceptions live in oridecon-admin, not here. Admin errors are returned as
frozen dataclass values in Result.Err(), not raised as exceptions.
"""

from __future__ import annotations

from dataclasses import dataclass

from oridecon.contracts.exceptions.base import OrideconError


class AdminError(OrideconError):
    """Base exception for all admin-domain errors.

    Extended by leaf exceptions in oridecon-admin.
    """

    _code = "ORI_ERR_ADMIN_001"


@dataclass(frozen=True, slots=True)
class WidgetNotFoundError:
    """Returned as ``Err(WidgetNotFoundError(...))`` when a contributor
    cannot render a requested widget.

    Frozen immutable value type for use as error payload in Result.Err().
    """

    contributor_name: str
    widget_name: str


@dataclass(frozen=True, slots=True)
class HealthCheckNotFoundError:
    """Returned as ``Err(HealthCheckNotFoundError(...))`` when a contributor
    cannot execute a requested health check.

    Frozen immutable value type for use as error payload in Result.Err().
    """

    contributor_name: str
    check_name: str


__all__ = [
    "AdminError",
    "HealthCheckNotFoundError",
    "WidgetNotFoundError",
]
