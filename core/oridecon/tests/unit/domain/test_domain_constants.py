"""Tests for domain constants."""

from __future__ import annotations

from oridecon.domain.constants import ENV_NESTED_DELIMITER, ENV_PREFIX


class TestDomainConstants:
    """Tests for domain constants."""

    def test_env_prefix(self) -> None:
        assert ENV_PREFIX == "ORI_DOMAIN__"

    def test_env_nested_delimiter(self) -> None:
        assert ENV_NESTED_DELIMITER == "__"
