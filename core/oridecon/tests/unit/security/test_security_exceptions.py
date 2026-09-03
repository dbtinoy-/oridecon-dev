"""Unit tests for oridecon core security exceptions.

Adapted from oridecon-security/tests/unit/test_security_exceptions.py.
The critical addition is test_exceptions_module_is_core_package which
verifies that the module resolves to oridecon core, not oridecon-security.
That test fails before oridecon/src/oridecon/security/ exists and passes
once the core package is created (core's __path__ position takes priority).
"""

from __future__ import annotations

import importlib.util

from oridecon.contracts.exceptions import OrideconError
from oridecon.contracts.exceptions.components import ComponentError
from oridecon.contracts.security import SecretNotFoundError
from oridecon.security.exceptions import (
    DecryptionError,
    EncryptionError,
    MiddlewareGuardError,
    SecretAccessError,
    SecretError,
    SecurityError,
)


class TestSecurityExceptionHierarchy:
    """Tests for security exception hierarchy."""

    def test_security_error_inherits_from_oridecon_error(self) -> None:
        assert issubclass(SecurityError, OrideconError)

    def test_secret_error_inherits_from_security_error(self) -> None:
        assert issubclass(SecretError, SecurityError)

    def test_secret_not_found_error_inherits_from_component_error(self) -> None:
        assert issubclass(SecretNotFoundError, ComponentError)

    def test_secret_access_error_inherits_from_secret_error(self) -> None:
        assert issubclass(SecretAccessError, SecretError)

    def test_guard_error_inherits_from_oridecon_error(self) -> None:
        assert issubclass(MiddlewareGuardError, OrideconError)

    def test_encryption_error_inherits_from_security_error(self) -> None:
        assert issubclass(EncryptionError, SecurityError)

    def test_decryption_error_inherits_from_security_error(self) -> None:
        assert issubclass(DecryptionError, SecurityError)


class TestSecurityError:
    """Tests for SecurityError."""

    def test_security_error_default_message(self) -> None:
        error = SecurityError()
        assert error.message is not None


class TestSecretError:
    """Tests for SecretError."""

    def test_secret_error_default_message(self) -> None:
        error = SecretError()
        assert error.message is not None


class TestSecretNotFoundError:
    """Tests for SecretNotFoundError."""

    def test_secret_not_found_error_inherits(self) -> None:
        assert issubclass(SecretNotFoundError, ComponentError)


class TestSecretAccessError:
    """Tests for SecretAccessError."""

    def test_secret_access_error_inherits(self) -> None:
        assert issubclass(SecretAccessError, SecretError)


class TestMiddlewareGuardError:
    """Tests for MiddlewareGuardError (from contracts)."""

    def test_guard_error_inherits(self) -> None:
        assert issubclass(MiddlewareGuardError, OrideconError)

    def test_guard_error_default_message(self) -> None:
        error = MiddlewareGuardError()
        assert error.message is not None


class TestExceptionAllExports:
    """Tests to verify __all__ exports."""

    def test_all_contains_all_exceptions(self) -> None:
        from oridecon.security import exceptions as exc_module

        expected = [
            "DecryptionError",
            "EncryptionError",
            "MiddlewareGuardError",
            "SecretAccessError",
            "SecretError",
            "SecurityError",
        ]
        for item in expected:
            assert item in exc_module.__all__


class TestExceptionsModuleIsCore:
    """Verify the exceptions module resolves to oridecon core, not oridecon-security.

    This test is the TDD signal for Task 1: it fails while only
    oridecon-security exists, and passes once oridecon/src/oridecon/security/
    is created (core takes priority in oridecon.__path__).
    """

    def test_exceptions_module_is_core_package(self) -> None:
        spec = importlib.util.find_spec("oridecon.security.exceptions")
        assert spec is not None, "oridecon.security.exceptions must be importable"
        assert spec.origin is not None, "module must have a known origin path"
        assert "oridecon-security" not in spec.origin, (
            f"Expected oridecon.security.exceptions to resolve to oridecon core, "
            f"but it resolved to: {spec.origin!r}. "
            f"Create oridecon/src/oridecon/security/exceptions.py to fix this."
        )
