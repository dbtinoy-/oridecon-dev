"""Oridecon CLI - Command-line tools for Oridecon Framework."""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.cli.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.cli.config import CLIConfig
    from oridecon.cli.exceptions import (
        CliError,
        ConfigNotFoundError,
        ProviderNotInstalledError,
    )
    from oridecon.cli.lib import (
        find_config,
        load_config_yaml,
    )
    from oridecon.cli.output import OutputManager
    from oridecon.cli.protocols import (
        CLIApplicationProtocol,
        CLIRunnerProtocol,
        CommandProtocol,
    )
    from oridecon.cli.runtime import (
        CLIContext,
        handle_errors,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "CLIApplicationProtocol": ("oridecon.cli.protocols", "CLIApplicationProtocol"),
    "CLIConfig": ("oridecon.cli.config", "CLIConfig"),
    "CLIContext": ("oridecon.cli.runtime", "CLIContext"),
    "CLIModule": ("oridecon.cli.module", "CLIModule"),
    "CLIRunnerProtocol": ("oridecon.cli.protocols", "CLIRunnerProtocol"),
    "CliError": ("oridecon.cli.exceptions", "CliError"),
    "CommandProtocol": ("oridecon.cli.protocols", "CommandProtocol"),
    "ConfigNotFoundError": ("oridecon.cli.exceptions", "ConfigNotFoundError"),
    "ProviderNotInstalledError": (
        "oridecon.cli.exceptions",
        "ProviderNotInstalledError",
    ),
    "OutputManager": ("oridecon.cli.output", "OutputManager"),
    "handle_errors": ("oridecon.cli.runtime", "handle_errors"),
    "find_config": ("oridecon.cli.lib", "find_config"),
    "load_config_yaml": ("oridecon.cli.lib", "load_config_yaml"),
}


def __getattr__(name: str) -> Any:
    """Lazy load attributes to avoid circular imports."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """List available attributes for IDE support."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "CLIApplicationProtocol",
    "CLIConfig",
    "CLIContext",
    "CLIModule",
    "CLIRunnerProtocol",
    "CliError",
    "CommandProtocol",
    "ConfigNotFoundError",
    "OutputManager",
    "ProviderNotInstalledError",
    "find_config",
    "handle_errors",
    "load_config_yaml",
]
