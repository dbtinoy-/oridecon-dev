"""Tests for contracts/exceptions/base.py — OrideconError and related."""

from __future__ import annotations

from oridecon.contracts.exceptions.base import OrideconError
from oridecon.contracts.exceptions.domain import NotFoundError, ValidationError


class TestOrideconErrorBasics:
    """Tests for OrideconError basic functionality."""

    def test_oridecon_error_default_message(self) -> None:
        """OrideconError has default message when none provided."""
        error = OrideconError()
        assert error.message == "An internal error occurred"

    def test_oridecon_error_custom_message(self) -> None:
        """OrideconError accepts custom message."""
        error = OrideconError(message="Custom error")
        assert error.message == "Custom error"

    def test_oridecon_error_default_code(self) -> None:
        """OrideconError has default code."""
        error = OrideconError()
        assert error.code == "ORI_ERR_CORE_001"

    def test_oridecon_error_subclass_code(self) -> None:
        """Subclass can override _code."""

        class CustomError(OrideconError):
            _code = "CUSTOM_001"

        error = CustomError(message="test")
        assert error.code == "CUSTOM_001"

    def test_oridecon_error_details_default(self) -> None:
        """OrideconError has empty details by default."""
        error = OrideconError()
        assert error.details == {}

    def test_oridecon_error_details_custom(self) -> None:
        """OrideconError accepts custom details."""
        error = OrideconError(details={"key": "value"})
        assert error.details["key"] == "value"

    def test_oridecon_error_cause(self) -> None:
        """OrideconError stores cause exception."""
        original = ValueError("original")
        error = OrideconError(cause=original)
        assert error.cause is original

    def test_oridecon_error_hint(self) -> None:
        """OrideconError stores hint."""
        error = OrideconError(hint="Try again later")
        assert error.hint == "Try again later"

    def test_oridecon_error_repr(self) -> None:
        """OrideconError has useful repr."""
        error = OrideconError(message="Test error")
        repr_str = repr(error)
        assert "OrideconError" in repr_str
        assert "ORI_ERR_CORE_001" in repr_str
        assert "Test error" in repr_str


class TestOrideconErrorStr:
    """Tests for OrideconError string representation."""

    def test_str_contains_code_and_message(self) -> None:
        """str() contains code and message."""
        error = OrideconError(message="Test error")
        error_str = str(error)
        assert "ORI_ERR_CORE_001" in error_str
        assert "Test error" in error_str

    def test_str_includes_hint(self) -> None:
        """str() includes hint when present."""
        error = OrideconError(message="Error", hint="Try this")
        error_str = str(error)
        assert "Fix: Try this" in error_str

    def test_str_excludes_docs_url_for_default_code(self) -> None:
        """str() excludes docs URL for default code."""
        error = OrideconError(message="Error")
        error_str = str(error)
        assert "oridecon.dev" not in error_str

    def test_str_includes_docs_url_for_custom_code(self) -> None:
        """str() includes docs URL for non-default code."""

        class CustomError(OrideconError):
            _code = "CUSTOM_001"

        error = CustomError(message="Error")
        error_str = str(error)
        assert "oridecon.dev" in error_str


class TestOrideconErrorToDict:
    """Tests for OrideconError.to_dict()."""

    def test_to_dict_basic(self) -> None:
        """to_dict returns basic structure."""
        error = OrideconError(message="Test")
        d = error.to_dict()
        assert d["code"] == "ORI_ERR_CORE_001"
        assert d["message"] == "Test"
        assert d["details"] == {}

    def test_to_dict_with_details(self) -> None:
        """to_dict includes custom details."""
        error = OrideconError(message="Test", details={"key": "value"})
        d = error.to_dict()
        assert d["details"]["key"] == "value"

    def test_to_dict_with_hint(self) -> None:
        """to_dict includes hint when present."""
        error = OrideconError(message="Test", hint="Try this")
        d = error.to_dict()
        assert d["hint"] == "Try this"

    def test_to_dict_excludes_hint_when_none(self) -> None:
        """to_dict excludes hint when not set."""
        error = OrideconError(message="Test")
        d = error.to_dict()
        assert "hint" not in d

    def test_to_dict_with_cause(self) -> None:
        """to_dict includes cause info."""
        original = ValueError("original error")
        error = OrideconError(message="Wrapped", cause=original)
        d = error.to_dict()
        assert "cause" in d
        assert d["cause"]["type"] == "ValueError"
        assert d["cause"]["message"] == "original error"

    def test_to_dict_excludes_cause_when_none(self) -> None:
        """to_dict excludes cause when not set."""
        error = OrideconError(message="Test")
        d = error.to_dict()
        assert "cause" not in d


class TestOrideconErrorWithDetails:
    """Tests for OrideconError.with_details()."""

    def test_with_details_returns_self(self) -> None:
        """with_details returns self (mutate-and-return pattern)."""
        error = OrideconError(message="Original")
        new_error = error.with_details(extra="value")

        assert new_error is error
        assert new_error.message == "Original"
        assert new_error.details["extra"] == "value"

    def test_with_details_preserves_original_details(self) -> None:
        """with_details preserves existing details."""
        error = OrideconError(message="Test", details={"existing": "data"})
        new_error = error.with_details(new="value")

        assert new_error.details["existing"] == "data"
        assert new_error.details["new"] == "value"

    def test_with_details_preserves_cause(self) -> None:
        """with_details preserves cause."""
        original = ValueError("cause")
        error = OrideconError(message="Test", cause=original)
        new_error = error.with_details(extra="value")

        assert new_error.cause is original

    def test_with_details_preserves_hint(self) -> None:
        """with_details preserves hint."""
        error = OrideconError(message="Test", hint="Try this")
        new_error = error.with_details(extra="value")

        assert new_error.hint == "Try this"


class TestOrideconErrorChaining:
    """Tests for error chaining and inheritance."""

    def test_subclass_inherits_base_code(self) -> None:
        """Subclass inherits default code correctly."""

        class MyError(OrideconError):
            pass

        error = MyError(message="test")
        assert error.code == "ORI_ERR_CORE_001"

    def test_isinstance_check_works(self) -> None:
        """isinstance check works across exception hierarchy."""
        error = OrideconError(message="test")
        assert isinstance(error, OrideconError)
        assert isinstance(error, Exception)


class TestBuilderSubtypePreservation:
    """Tests that builder methods preserve the exception subtype (01.C-01)."""

    def test_with_details_preserves_subtype(self) -> None:
        err = ValidationError("bad input")
        err2 = err.with_details(field="email")
        assert isinstance(err2, ValidationError), (
            f"Expected ValidationError, got {type(err2).__name__}"
        )

    def test_with_hint_preserves_subtype(self) -> None:
        err = NotFoundError("user not found")
        err2 = err.with_hint("Check the user ID")
        assert isinstance(err2, NotFoundError), (
            f"Expected NotFoundError, got {type(err2).__name__}"
        )

    def test_with_cause_preserves_subtype(self) -> None:
        cause = ValueError("original")
        err = ValidationError("validation failed")
        err2 = err.with_cause(cause)
        assert isinstance(err2, ValidationError), (
            f"Expected ValidationError, got {type(err2).__name__}"
        )
        assert err2.__cause__ is cause

    def test_chained_builders_preserve_subtype(self) -> None:
        err = ValidationError("bad input")
        err2 = err.with_details(field="email").with_hint("Use a valid email")
        assert isinstance(err2, ValidationError)
        assert err2.details.get("field") == "email"
