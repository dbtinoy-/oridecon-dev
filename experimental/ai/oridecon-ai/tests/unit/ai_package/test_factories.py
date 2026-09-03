"""Tests for oridecon.ai.di.factories."""

from __future__ import annotations


class TestDIFactories:
    """Tests for oridecon.ai.di.factories."""

    def test_factories_module_importable(self) -> None:
        import oridecon.ai.di.factories as factories  # noqa: F401

        assert factories is not None

    def test_factories_all_is_list(self) -> None:
        from oridecon.ai.di import factories

        assert isinstance(factories.__all__, list)
