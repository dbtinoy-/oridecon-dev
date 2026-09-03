"""Tests for CLI error hierarchy."""

from oridecon.cli.exceptions import CliError


class TestCliError:
    def test_basic_error(self):
        err = CliError("something broke")
        assert "something broke" in str(err)
        assert err.message == "something broke"

    def test_error_with_hints(self):
        err = CliError(
            "Database connection failed",
            causes=["PostgreSQL is not running", "Database does not exist"],
            suggestions=["Start PostgreSQL: sudo systemctl start postgresql",
                         "Check config: oridecon config show database"],
        )
        assert err.causes == ["PostgreSQL is not running", "Database does not exist"]
        assert len(err.suggestions) == 2

    def test_error_with_no_extras(self):
        err = CliError("simple error")
        assert err.causes == []
        assert err.suggestions == []

    def test_error_inherits_oridecon_error(self):
        from oridecon.contracts.exceptions import OrideconError
        err = CliError("test")
        assert isinstance(err, OrideconError)

    def test_config_not_found_error(self):
        from oridecon.cli.exceptions import ConfigNotFoundError
        err = ConfigNotFoundError()
        assert "application.yaml" in err.message
        assert any("oridecon init" in s for s in err.suggestions)

    def test_provider_not_installed_error(self):
        from oridecon.cli.exceptions import ProviderNotInstalledError
        err = ProviderNotInstalledError("oridecon-sql")
        assert "oridecon-sql" in err.message
