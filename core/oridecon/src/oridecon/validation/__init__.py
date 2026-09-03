"""Oridecon Validation — composable imperative validation pipeline.

Complements the declarative ``Field()`` constraints from
``oridecon.validation.schema`` with a runtime validation pipeline that
returns ``Result`` types, enabling pre-domain-object data validation.

Rules are composable and chainable; the ``ValidatorImpl`` accumulates
field-level ``FieldError`` instances and surfaces them as a
``ValidationError`` wrapped in an ``Err`` result — never raising.

Basic Usage::

    from oridecon.validation import ValidatorImpl, required, min_length, email_format

    user_validator = (
        ValidatorImpl()
        .rule("name", required(), min_length(2))
        .rule("email", required(), email_format())
    )

    result = user_validator.validate({"name": "Jo", "email": "jo@example.com"})
    if result.is_ok():
        data = result.unwrap()

Module Structure:
    - config: Configuration models (``ValidationConfig``)
    - decorators: ``@validate_input`` decorator
    - engine: Sync and async validators (``ValidatorImpl``, ``AsyncValidator``)
    - exceptions: Validation exception hierarchy (``ValidationError``, ``ValidationSystemError``)
    - module: ``ValidationModule`` IoC registration
    - rules: Built-in validation rules (``Required``, ``MinLength``, ``EmailFormat``, …)
    - schema: Pydantic schema utilities (``Field``, ``EmailStr``, ``model_validator``, …)
    - types: Type aliases (``FieldName``)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.validation.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.contracts.core.validation import (
        AsyncRuleProtocol,
        RuleProtocol,
        RuleResult,
        ValidationResult,
        ValidatorProtocol,
    )
    from oridecon.contracts.exceptions.domain import FieldError
    from oridecon.validation.config import ValidationConfig
    from oridecon.validation.constants import (
        CODE_CUSTOM,
        CODE_EMAIL,
        CODE_MAX_LENGTH,
        CODE_MIN_LENGTH,
        CODE_ONE_OF,
        CODE_PATTERN,
        CODE_RANGE,
        CODE_RANGE_MAX,
        CODE_RANGE_MIN,
        CODE_REQUIRED,
        CODE_TYPE,
    )
    from oridecon.validation.decorators import validate_input
    from oridecon.validation.engine import AsyncValidator, ValidatorImpl
    from oridecon.validation.exceptions import ValidationError, ValidationSystemError
    from oridecon.validation.module import ValidationModule
    from oridecon.validation.rules import (
        AbstractAsyncRule,
        AbstractRule,
        Custom,
        EmailFormat,
        MaxLength,
        MinLength,
        OneOf,
        Pattern,
        Range,
        Required,
        custom,
        email_format,
        max_length,
        min_length,
        one_of,
        pattern,
        range_check,
        required,
        validate_range,
        validate_required,
        validate_type,
    )
    from oridecon.validation.schema import (
        ConfigDict,
        EmailStr,
        Field,
        HttpUrl,
        SecretStr,
        field_validator,
        model_validator,
    )
    from oridecon.validation.types import FieldName

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Module ---
    "ValidationModule": ("oridecon.validation.module", "ValidationModule"),
    # --- Config ---
    "ValidationConfig": ("oridecon.validation.config", "ValidationConfig"),
    # --- Exceptions ---
    "ValidationError": ("oridecon.validation.exceptions", "ValidationError"),
    "ValidationSystemError": (
        "oridecon.validation.exceptions",
        "ValidationSystemError",
    ),
    "FieldError": ("oridecon.contracts.exceptions.domain", "FieldError"),
    # --- Decorators ---
    "validate_input": ("oridecon.validation.decorators", "validate_input"),
    # --- Fields ---
    "ConfigDict": ("oridecon.validation.schema", "ConfigDict"),
    "EmailStr": ("oridecon.validation.schema", "EmailStr"),
    "Field": ("oridecon.validation.schema", "Field"),
    "HttpUrl": ("oridecon.validation.schema", "HttpUrl"),
    "SecretStr": ("oridecon.validation.schema", "SecretStr"),
    "field_validator": ("oridecon.validation.schema", "field_validator"),
    "model_validator": ("oridecon.validation.schema", "model_validator"),
    # --- Rules (classes) ---
    "AbstractAsyncRule": ("oridecon.validation.rules", "AbstractAsyncRule"),
    "AbstractRule": ("oridecon.validation.rules", "AbstractRule"),
    "Custom": ("oridecon.validation.rules", "Custom"),
    "EmailFormat": ("oridecon.validation.rules", "EmailFormat"),
    "MaxLength": ("oridecon.validation.rules", "MaxLength"),
    "MinLength": ("oridecon.validation.rules", "MinLength"),
    "OneOf": ("oridecon.validation.rules", "OneOf"),
    "Pattern": ("oridecon.validation.rules", "Pattern"),
    "Range": ("oridecon.validation.rules", "Range"),
    "Required": ("oridecon.validation.rules", "Required"),
    # --- Rules (factory functions) ---
    "custom": ("oridecon.validation.rules", "custom"),
    "email_format": ("oridecon.validation.rules", "email_format"),
    "max_length": ("oridecon.validation.rules", "max_length"),
    "min_length": ("oridecon.validation.rules", "min_length"),
    "one_of": ("oridecon.validation.rules", "one_of"),
    "pattern": ("oridecon.validation.rules", "pattern"),
    "range_check": ("oridecon.validation.rules", "range_check"),
    "required": ("oridecon.validation.rules", "required"),
    # --- Result-based helpers (merged from helpers.py → rules.py) ---
    "validate_range": ("oridecon.validation.rules", "validate_range"),
    "validate_required": ("oridecon.validation.rules", "validate_required"),
    "validate_type": ("oridecon.validation.rules", "validate_type"),
    # --- Validator ---
    "AsyncValidator": ("oridecon.validation.engine", "AsyncValidator"),
    "ValidatorImpl": ("oridecon.validation.engine", "ValidatorImpl"),
    # --- Types ---
    "FieldName": ("oridecon.validation.types", "FieldName"),
    # --- Constants ---
    "CODE_REQUIRED": ("oridecon.validation.constants", "CODE_REQUIRED"),
    "CODE_MIN_LENGTH": ("oridecon.validation.constants", "CODE_MIN_LENGTH"),
    "CODE_MAX_LENGTH": ("oridecon.validation.constants", "CODE_MAX_LENGTH"),
    "CODE_PATTERN": ("oridecon.validation.constants", "CODE_PATTERN"),
    "CODE_RANGE": ("oridecon.validation.constants", "CODE_RANGE"),
    "CODE_RANGE_MIN": ("oridecon.validation.constants", "CODE_RANGE_MIN"),
    "CODE_RANGE_MAX": ("oridecon.validation.constants", "CODE_RANGE_MAX"),
    "CODE_ONE_OF": ("oridecon.validation.constants", "CODE_ONE_OF"),
    "CODE_EMAIL": ("oridecon.validation.constants", "CODE_EMAIL"),
    "CODE_TYPE": ("oridecon.validation.constants", "CODE_TYPE"),
    "CODE_CUSTOM": ("oridecon.validation.constants", "CODE_CUSTOM"),
    # --- Protocols (from contracts) ---
    "RuleResult": ("oridecon.contracts.core.validation", "RuleResult"),
    "ValidationResult": ("oridecon.contracts.core.validation", "ValidationResult"),
    "RuleProtocol": ("oridecon.contracts.core.validation", "RuleProtocol"),
    "AsyncRuleProtocol": ("oridecon.contracts.core.validation", "AsyncRuleProtocol"),
    "ValidatorProtocol": ("oridecon.contracts.core.validation", "ValidatorProtocol"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "CODE_CUSTOM",
    "CODE_EMAIL",
    "CODE_MAX_LENGTH",
    "CODE_MIN_LENGTH",
    "CODE_ONE_OF",
    "CODE_PATTERN",
    "CODE_RANGE",
    "CODE_RANGE_MAX",
    "CODE_RANGE_MIN",
    "CODE_REQUIRED",
    "CODE_TYPE",
    "AbstractAsyncRule",
    "AbstractRule",
    "AsyncRuleProtocol",
    "AsyncValidator",
    "ConfigDict",
    "Custom",
    "EmailFormat",
    "EmailStr",
    "Field",
    "FieldError",
    "FieldName",
    "HttpUrl",
    "MaxLength",
    "MinLength",
    "OneOf",
    "Pattern",
    "Range",
    "Required",
    "RuleProtocol",
    "RuleResult",
    "SecretStr",
    "ValidationConfig",
    "ValidationError",
    "ValidationModule",
    "ValidationResult",
    "ValidationSystemError",
    "ValidatorImpl",
    "ValidatorProtocol",
    "custom",
    "email_format",
    "field_validator",
    "max_length",
    "min_length",
    "model_validator",
    "one_of",
    "pattern",
    "range_check",
    "required",
    "validate_input",
    "validate_range",
    "validate_required",
    "validate_type",
]
