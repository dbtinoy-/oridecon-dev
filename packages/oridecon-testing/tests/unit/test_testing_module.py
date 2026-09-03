"""Tests for testing module."""

import pytest
from oridecon.testing import TestingModule
from oridecon.di.module import DynamicModule


class TestTestingModule:
    def test_testing_module_exists(self) -> None:
        assert TestingModule is not None

    def test_configure_returns_dynamic_module(self) -> None:
        result = TestingModule.configure()
        assert isinstance(result, DynamicModule)
        assert result.module is TestingModule
