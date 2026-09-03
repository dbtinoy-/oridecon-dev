"""Factory function for bootstrapping a Oridecon application.

Provides :func:`create_app` as a zero-dependency convenience entrypoint
that creates a bare :class:`Application` and optionally registers an
explicit list of providers.  Provider auto-discovery via entry points is
the responsibility of ``oridecon-plugins`` — this module intentionally
has no knowledge of any extension package.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.app.base import Application

if TYPE_CHECKING:
    from oridecon.config.main import OrideconConfig

__all__ = ["create_app"]


def create_app(
    name: str = "oridecon-app",
    config: OrideconConfig | None = None,
) -> Application:
    """Create and return a new Oridecon application.

    Returns a :class:`Application` with no providers registered.
    Call :meth:`Application.add_provider` (or
    :meth:`Application.add_providers`) before :meth:`Application.boot`
    to register providers.

    For entry-point-based auto-discovery, use
    ``oridecon.plugins.discovery.discover_providers`` — the plugin system
    ships inside the core ``oridecon`` package.

    Args:
        name: Human-readable application name used in log output.
            Defaults to ``"oridecon-app"``.
        config: Application configuration.  If omitted an empty
            :class:`OrideconConfig` is created, which reads values from
            environment variables via the standard ``LX_*`` prefix.

    Returns:
        A new :class:`Application` ready for provider registration and boot.

    Example::

        app = create_app(config=OrideconConfig.from_env_profile("production"))
        app.add_provider(WebProvider(web_config))
        await app.boot()
    """
    return Application(name=name, config=config)
