"""Tests for Oridecon exception hierarchy."""

import pytest

from oridecon.contracts.exceptions.base import OrideconError
from oridecon.contracts.exceptions.provider import ModuleError
from oridecon.exceptions import (
    ConfigurationError,
    DomainModelError,
    InjectionError,
    OrideconException,
    SerializationError,
    ValidationError,
)


class TestExceptionHierarchy:
    """Tests for exception inheritance hierarchy."""

    def test_oridecon_exception_extends_oridecon_error(self) -> None:
        """OrideconException must extend OrideconError from contracts."""
        assert issubclass(OrideconException, OrideconError)

    def test_oridecon_exception_is_base(self) -> None:
        """OrideconException is the base for all framework exceptions."""
        assert issubclass(ConfigurationError, OrideconException)
        assert issubclass(InjectionError, OrideconException)
        assert issubclass(ValidationError, OrideconException)
        assert issubclass(SerializationError, OrideconException)
        assert issubclass(DomainModelError, OrideconException)
        # ModuleError is from contracts and inherits OrideconError, not OrideconException
        assert issubclass(ModuleError, OrideconError)

    def test_all_exceptions_inherit_from_exception(self) -> None:
        """All Oridecon exceptions inherit from Exception."""
        assert issubclass(OrideconException, Exception)
        assert issubclass(ConfigurationError, Exception)
        assert issubclass(InjectionError, Exception)
        assert issubclass(ValidationError, Exception)
        assert issubclass(SerializationError, Exception)
        assert issubclass(DomainModelError, Exception)
        assert issubclass(ModuleError, Exception)  # via OrideconError → Exception

    def test_all_exceptions_inherit_from_oridecon_error(self) -> None:
        """All domain exceptions inherit from OrideconError."""
        assert issubclass(OrideconException, OrideconError)
        assert issubclass(ConfigurationError, OrideconError)
        assert issubclass(InjectionError, OrideconError)


class TestExceptionMessages:
    """Tests for exception messages and instantiation."""

    def test_oridecon_exception_with_message(self) -> None:
        """OrideconException can be instantiated with a message."""
        msg = "Something went wrong"
        exc = OrideconException(msg)
        # OrideconError.__str__ includes the code prefix, but the message is present
        assert msg in str(exc)

    def test_oridecon_exception_message_attribute(self) -> None:
        """OrideconException stores message on .message attribute."""
        msg = "Something went wrong"
        exc = OrideconException(msg)
        assert exc.message == msg

    def test_configuration_error_with_context(self) -> None:
        """ConfigurationError includes context in message."""
        exc = ConfigurationError("Invalid setting: debug")
        assert "Invalid setting" in str(exc)

    def test_injection_error_with_service_name(self) -> None:
        """InjectionError includes service information."""
        exc = InjectionError("Cannot resolve: UserService")
        assert "UserService" in str(exc)

    def test_validation_error_with_message(self) -> None:
        """ValidationError includes message in string representation."""
        exc = ValidationError("email: Invalid email format")
        assert "email" in str(exc)
        assert "Invalid" in str(exc)


class TestExceptionChaining:
    """Tests for exception chaining."""

    def test_exception_with_cause(self) -> None:
        """Exceptions can chain from other exceptions."""
        original = ValueError("original error")
        exc = OrideconException("wrapped")
        exc.__cause__ = original
        assert exc.__cause__ is original

    def test_injection_error_chains_resolution_error(self) -> None:
        """InjectionError can chain from underlying errors."""
        original = RuntimeError("container error")
        exc = InjectionError("resolution failed")
        exc.__cause__ = original
        assert exc.__cause__ is original


class TestExceptionCatching:
    """Tests for exception catching patterns."""

    def test_catch_all_oridecon_exceptions(self) -> None:
        """Can catch all Oridecon exceptions with base class."""
        framework_errors = [
            ConfigurationError("config"),
            InjectionError("inject"),
            ValidationError("validation failed"),
            SerializationError("json"),
            DomainModelError("domain"),
        ]
        for error in framework_errors:
            assert isinstance(error, OrideconException)

        # ModuleError is from contracts — catches as OrideconError, not OrideconException
        assert isinstance(ModuleError("module"), OrideconError)

    def test_catch_all_as_oridecon_error(self) -> None:
        """Can catch all Oridecon exceptions as OrideconError."""
        errors = [
            ConfigurationError("config"),
            InjectionError("inject"),
            ValidationError("validation failed"),
        ]
        for error in errors:
            assert isinstance(error, OrideconError)

    def test_catch_specific_exception(self) -> None:
        """Can catch specific exception types."""
        with pytest.raises(ConfigurationError):
            raise ConfigurationError("specific error")

    def test_catch_by_parent_exception(self) -> None:
        """Specific exceptions can be caught by parent type."""
        with pytest.raises(OrideconException):
            raise ValidationError("validation failed")
