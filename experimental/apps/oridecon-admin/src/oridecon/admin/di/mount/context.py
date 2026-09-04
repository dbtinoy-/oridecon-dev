"""Shared mutable context for the admin mount pipeline.

Collects state produced by one mount phase and consumed by later phases so
that the individual mount steps stay decoupled from each other.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class MountContext:
    """Cross-phase state produced while mounting the admin panel."""

    resources: dict[str, Any] = field(default_factory=dict)
    controllers: list[Any] = field(default_factory=list)
    middlewares: list[tuple[type, dict[str, Any]]] = field(default_factory=list)
    contributors: list[Any] = field(default_factory=list)
    settings_service: Any | None = None
    snapshot_service: Any | None = None
    saved_view_service: Any | None = None
    progress_tracker: Any | None = None
    progress_access: Any | None = None
    contributor_registry: Any | None = None
    cluster_registry: Any | None = None
    nav_builder: Any | None = None
    router: Any | None = None
    admin_app: Any | None = None
    # Doc 33: SecurityHeadersRegistry stored here at mount time so
    # _mount_app_state can expose it on app.state under the attribute
    # ``security_headers_middleware`` (kept for test/controller compatibility).
    # The registry holds a weak reference to the real middleware instance once
    # it handles its first request, enabling invalidate() calls from the
    # settings save path without a dummy instance.
    security_headers_middleware: Any | None = None
