"""Constants for the docs-claims audit."""

from __future__ import annotations

import re

_ENV_TOKEN_RE = re.compile(r"\bORI_[A-Z][A-Z0-9_]*\b")
_PRIORITY_RE = re.compile(r"ProviderPriority\.([A-Z][A-Z0-9_]*)")
_SECTION_CONFIG_SUFFIX = "Config"
# `ORI_ERR_*` is the error-code namespace (ORI_ERR_<PKG>_<CODE>) — not env vars.
_ERROR_CODE_PREFIX = "ORI_ERR_"
# Trailing-delimiter tokens (`ORI_X__`) are env-source prefix claims.
_PREFIX_TOKEN_SUFFIX = "__"

# Env vars read directly by framework code (never a section/key mapping).
_DIRECT_READ_ENV_VARS = frozenset(
    {
        "ORI_CONFIG",
        "ORI_DEBUG",
        "ORI_ENV",
        "ORI_PROFILE",
        "ORI_QUIET",
    }
)

# Dynamic namespaces: any token under these prefixes is a valid env var.
_DYNAMIC_PREFIXES = (
    # Feature-flag overrides: FeatureFlagsConfig.flag_env_prefix is "ORI_FLAG_".
    "ORI_FLAG_",
)

_PRIORITY_MODULE = "oridecon.contracts.core.provider"
_PRIORITY_ENUM = "ProviderPriority"
