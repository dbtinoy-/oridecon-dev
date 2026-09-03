"""Oridecon Config — Configuration loading, models, and sources.

This module uses lazy imports for all public symbols to keep
import overhead minimal.  Every name listed in _LAZY_IMPORTS
is available at package level:

    from oridecon.config import <Symbol>

or by accessing the attribute on the package:

    import oridecon.config as config
    config.<Symbol>
"""

from __future__ import annotations

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.config.base import BaseConfig
    from oridecon.config.constants import (
        DEFAULT_CONFIG_FILENAMES as DEFAULT_CONFIG_FILENAMES,
    )
    from oridecon.config.constants import (
        DEFAULT_ENV_VAR_PREFIX as DEFAULT_ENV_VAR_PREFIX,
    )
    from oridecon.config.constants import (
        DEFAULT_RELOAD_INTERVAL as DEFAULT_RELOAD_INTERVAL,
    )
    from oridecon.config.constants import (
        INSECURE_SECRET_VALUES as INSECURE_SECRET_VALUES,
    )
    from oridecon.config.constants import (
        SECRET_FIELD_PATTERNS as SECRET_FIELD_PATTERNS,
    )
    from oridecon.config.constants import (
        SUPPORTED_FORMATS as SUPPORTED_FORMATS,
    )
    from oridecon.config.exceptions import (
        ConfigReloadError as ConfigReloadError,
    )
    from oridecon.config.exceptions import (
        ConfigSectionNotFoundError as ConfigSectionNotFoundError,
    )
    from oridecon.config.exceptions import (
        ConfigSourceError as ConfigSourceError,
    )
    from oridecon.config.exceptions import (
        ConfigurationError as ConfigurationError,
    )
    from oridecon.config.lib.merge import deep_merge as deep_merge
    from oridecon.config.lib.merge import interpolate_env_vars as interpolate_env_vars
    from oridecon.config.lib.merge import interpolate_string as interpolate_string
    from oridecon.config.lib.registry import ConfigRegistry
    from oridecon.config.lib.sources import (
        CliConfigSource,
        ConfigLoader,
        ConfigSource,
        DirectoryConfigSource,
        DotEnvSource,
        EnvironmentConfigSource,
        FileConfigSource,
    )
    from oridecon.config.lib.validation import is_insecure_secret as is_insecure_secret
    from oridecon.config.lib.validation import (
        validate_all_configs as validate_all_configs,
    )
    from oridecon.config.lib.watcher import ConfigWatcher
    from oridecon.config.main import OrideconConfig
    from oridecon.config.protocols import ConfigSourceProtocol as ConfigSourceProtocol
    from oridecon.config.secrets import DEFAULT_MIN_LENGTHS as DEFAULT_MIN_LENGTHS
    from oridecon.config.secrets import (
        DEFAULT_PLACEHOLDER_VALUES as DEFAULT_PLACEHOLDER_VALUES,
    )
    from oridecon.config.secrets import SecretsPolicy as SecretsPolicy
    from oridecon.config.secrets import SecretsValidator as SecretsValidator
    from oridecon.config.secrets import (
        SecretsValidatorProtocol as SecretsValidatorProtocol,
    )
    from oridecon.config.secrets import SecretViolation as SecretViolation
    from oridecon.config.types import ConfigSourceType as ConfigSourceType
    from oridecon.contracts.core.config import ConfigIssue as ConfigIssue
    from oridecon.contracts.core.config import Environment as Environment
    from oridecon.contracts.exceptions import ConfigurationError
    from oridecon.logging.config import LoggingConfig, SamplingConfig

_LAZY_IMPORTS: dict[str, str] = {
    "BaseConfig": "oridecon.config.base",
    "CliConfigSource": "oridecon.config.lib.sources",
    "ConfigIssue": "oridecon.contracts.core.config",
    "ConfigLoader": "oridecon.config.lib.sources",
    "ConfigRegistry": "oridecon.config.lib.registry",
    "ConfigSource": "oridecon.config.lib.sources",
    "ConfigWatcher": "oridecon.config.lib.watcher",
    "ConfigurationError": "oridecon.contracts.exceptions",
    "DirectoryConfigSource": "oridecon.config.lib.sources",
    "DotEnvSource": "oridecon.config.lib.sources",
    "Environment": "oridecon.contracts.core.config",
    "EnvironmentConfigSource": "oridecon.config.lib.sources",
    "FileConfigSource": "oridecon.config.lib.sources",
    "OrideconConfig": "oridecon.config.main",
    "LoggingConfig": "oridecon.logging.config",
    "SamplingConfig": "oridecon.logging.config",
    "deep_merge": "oridecon.config.lib.merge",
    "interpolate_env_vars": "oridecon.config.lib.merge",
    "interpolate_string": "oridecon.config.lib.merge",
    "validate_all_configs": "oridecon.config.lib.validation",
    # secrets
    "DEFAULT_MIN_LENGTHS": "oridecon.config.secrets",
    "DEFAULT_PLACEHOLDER_VALUES": "oridecon.config.secrets",
    "SecretViolation": "oridecon.config.secrets",
    "SecretsPolicy": "oridecon.config.secrets",
    "SecretsValidator": "oridecon.config.secrets",
    "SecretsValidatorProtocol": "oridecon.config.secrets",
    # constants
    "DEFAULT_CONFIG_FILENAMES": "oridecon.config.constants",
    "DEFAULT_ENV_VAR_PREFIX": "oridecon.config.constants",
    "DEFAULT_RELOAD_INTERVAL": "oridecon.config.constants",
    "INSECURE_SECRET_VALUES": "oridecon.config.constants",
    "SECRET_FIELD_PATTERNS": "oridecon.config.constants",
    "SUPPORTED_FORMATS": "oridecon.config.constants",
    "is_insecure_secret": "oridecon.config.lib.validation",
    # exceptions
    "ConfigReloadError": "oridecon.config.exceptions",
    "ConfigSectionNotFoundError": "oridecon.config.exceptions",
    "ConfigSourceError": "oridecon.config.exceptions",
    # protocols
    "ConfigSourceProtocol": "oridecon.config.protocols",
    # types
    "ConfigSourceType": "oridecon.config.types",
    # provider
    "ConfigProvider": "oridecon.config.di.provider",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return list(_LAZY_IMPORTS.keys())


__all__ = (
    "DEFAULT_CONFIG_FILENAMES",
    "DEFAULT_ENV_VAR_PREFIX",
    "DEFAULT_MIN_LENGTHS",
    "DEFAULT_PLACEHOLDER_VALUES",
    "DEFAULT_RELOAD_INTERVAL",
    "INSECURE_SECRET_VALUES",
    "SECRET_FIELD_PATTERNS",
    "SUPPORTED_FORMATS",
    "BaseConfig",
    "CliConfigSource",
    "ConfigIssue",
    "ConfigLoader",
    "ConfigRegistry",
    "ConfigReloadError",
    "ConfigSectionNotFoundError",
    "ConfigSource",
    "ConfigSourceError",
    "ConfigSourceProtocol",
    "ConfigSourceType",
    "ConfigWatcher",
    "ConfigurationError",
    "DirectoryConfigSource",
    "DotEnvSource",
    "Environment",
    "EnvironmentConfigSource",
    "FileConfigSource",
    "OrideconConfig",
    "LoggingConfig",
    "SamplingConfig",
    "SecretViolation",
    "SecretsPolicy",
    "SecretsValidator",
    "SecretsValidatorProtocol",
    "deep_merge",
    "interpolate_env_vars",
    "interpolate_string",
    "is_insecure_secret",
    "validate_all_configs",
)
__version__ = "0.1.0"
