"""Tests that OrideconConfig() with no file/env produces working defaults."""

from __future__ import annotations

import pytest

from oridecon.config.main import OrideconConfig


class TestOrideconConfigDefaults:
    """Verify bare OrideconConfig() has sensible defaults."""

    def test_bare_config_instantiates_without_error(self) -> None:
        cfg = OrideconConfig()
        assert cfg is not None

    def test_bare_config_has_default_app_name(self) -> None:
        cfg = OrideconConfig()
        assert cfg.app_name == "oridecon-app"

    def test_bare_config_debug_is_false(self) -> None:
        cfg = OrideconConfig()
        assert cfg.debug is False

    def test_get_section_web_returns_default_web_config(self) -> None:
        """When no [web] section is present, get_section returns WebConfig()."""
        from oridecon.web.config import WebConfig

        cfg = OrideconConfig()
        web = cfg.get_section("web", WebConfig)
        assert isinstance(web, WebConfig)

    def test_get_section_db_returns_default_database_config(self) -> None:
        """When no [db] section is present, get_section returns DatabaseConfig()."""
        from oridecon.sql.config import DatabaseConfig

        cfg = OrideconConfig()
        db = cfg.get_section("db", DatabaseConfig)
        assert isinstance(db, DatabaseConfig)
        # Default URL should be sqlite
        assert "sqlite" in db.backend.url.get_secret_value().lower()

    def test_get_section_absent_without_model_returns_none(self) -> None:
        """A missing untyped section yields None (ConfigProtocol contract)."""
        cfg = OrideconConfig()
        result = cfg.get_section("nonexistent_section")
        assert result is None

    def test_has_section_returns_false_for_absent_key(self) -> None:
        cfg = OrideconConfig()
        assert cfg.has_section("billing") is False

    def test_to_dict_does_not_raise(self) -> None:
        cfg = OrideconConfig()
        d = cfg.to_dict()
        assert isinstance(d, dict)
        assert "app_name" in d
