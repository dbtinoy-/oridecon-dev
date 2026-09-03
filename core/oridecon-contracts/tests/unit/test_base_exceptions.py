"""Tests for contract base exceptions."""

import pytest
from oridecon.contracts.exceptions.base import OrideconError


class TestOrideconError:
    def test_oridecon_error_default(self) -> None:
        exc = OrideconError()
        assert exc.code == "ORI_ERR_CORE_001"
        assert exc.message == "An internal error occurred"
        assert exc.details == {}
        assert exc.cause is None
        assert exc.hint is None

    def test_oridecon_error_with_message(self) -> None:
        exc = OrideconError(message="Custom error")
        assert exc.message == "Custom error"

    def test_oridecon_error_with_details(self) -> None:
        exc = OrideconError(details={"key": "value"})
        assert exc.details == {"key": "value"}

    def test_oridecon_error_with_cause(self) -> None:
        original = ValueError("original")
        exc = OrideconError(cause=original)
        assert exc.cause is original

    def test_oridecon_error_with_hint(self) -> None:
        exc = OrideconError(hint="Try again later")
        assert exc.hint == "Try again later"

    def test_oridecon_error_str(self) -> None:
        exc = OrideconError(message="Test error")
        assert str(exc) == "[ORI_ERR_CORE_001] Test error"

    def test_oridecon_error_repr(self) -> None:
        exc = OrideconError(message="Test error")
        assert "OrideconError" in repr(exc)
        assert "ORI_ERR_CORE_001" in repr(exc)

    def test_oridecon_error_to_dict(self) -> None:
        exc = OrideconError(message="Test", details={"key": "value"})
        d = exc.to_dict()
        assert d["code"] == "ORI_ERR_CORE_001"
        assert d["message"] == "Test"
        assert d["details"] == {"key": "value"}

    def test_oridecon_error_to_dict_with_hint(self) -> None:
        exc = OrideconError(message="Test", hint="Try again")
        d = exc.to_dict()
        assert d["hint"] == "Try again"

    def test_oridecon_error_to_dict_with_cause(self) -> None:
        original = ValueError("original error")
        exc = OrideconError(message="Test", cause=original)
        d = exc.to_dict()
        assert "cause" in d
        assert d["cause"]["type"] == "ValueError"

    def test_oridecon_error_with_details_method(self) -> None:
        exc = OrideconError(message="Test", details={"key1": "value1"})
        exc2 = exc.with_details(key2="value2")
        assert exc2.details["key1"] == "value1"
        assert exc2.details["key2"] == "value2"
        assert exc2.code == "ORI_ERR_CORE_001"

    def test_oridecon_error_with_hint_method(self) -> None:
        exc = OrideconError(message="Test")
        exc2 = exc.with_hint("Try again")
        assert exc2.hint == "Try again"

    def test_oridecon_error_with_cause_method(self) -> None:
        original = ValueError("original")
        exc = OrideconError(message="Test")
        exc2 = exc.with_cause(original)
        assert exc2.cause is original

    def test_oridecon_error_format(self) -> None:
        exc = OrideconError(message="Test error", details={"key": "value"})
        formatted = exc.format()
        assert "Test error" in formatted
        assert "key: value" in formatted

    def test_oridecon_error_format_with_hint(self) -> None:
        exc = OrideconError(message="Test", hint="Try again")
        formatted = exc.format()
        assert "Hint: Try again" in formatted
