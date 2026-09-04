"""Tests for UI exceptions."""

import pytest

from oridecon.ui.exceptions import UIError


class TestUIError:
    """Tests for UIError exception."""

    def test_ui_error_message(self) -> None:
        """Test UIError can be created with a message."""
        error = UIError("Test error message")
        assert str(error) == "Test error message"

    def test_ui_error_inherits_from_lexigram_error(self) -> None:
        """Test UIError inherits from OrideconError."""
        from oridecon.contracts.exceptions import OrideconError

        error = UIError("Test")
        assert isinstance(error, OrideconError)

    def test_ui_error_with_code(self) -> None:
        """Test UIError can have an error code."""
        error = UIError("Test error", code="UI_001")
        assert error.code == "UI_001"

    def test_ui_error_types_exported(self) -> None:
        """Test that exceptions are in __all__."""
        from oridecon.ui.exceptions import __all__

        assert "UIError" in __all__
