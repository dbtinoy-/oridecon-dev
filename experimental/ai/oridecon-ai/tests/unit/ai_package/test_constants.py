"""Tests for oridecon.ai.constants."""

from __future__ import annotations


class TestAIConstants:
    """Tests for oridecon.ai.constants."""

    def test_env_prefix(self) -> None:
        from oridecon.ai.constants import ENV_PREFIX

        assert ENV_PREFIX == "ORI_AI__"

    def test_env_nested_delimiter(self) -> None:
        from oridecon.ai.constants import ENV_NESTED_DELIMITER

        assert ENV_NESTED_DELIMITER == "__"

    def test_default_max_tokens(self) -> None:
        from oridecon.ai.constants import DEFAULT_MAX_TOKENS

        assert isinstance(DEFAULT_MAX_TOKENS, int)
        assert DEFAULT_MAX_TOKENS > 0

    def test_default_temperature(self) -> None:
        from oridecon.ai.constants import DEFAULT_TEMPERATURE

        assert 0.0 <= DEFAULT_TEMPERATURE <= 2.0

    def test_default_request_timeout(self) -> None:
        from oridecon.ai.constants import DEFAULT_REQUEST_TIMEOUT_S

        assert isinstance(DEFAULT_REQUEST_TIMEOUT_S, int)
        assert DEFAULT_REQUEST_TIMEOUT_S > 0

    def test_default_context_window_messages(self) -> None:
        from oridecon.ai.constants import DEFAULT_CONTEXT_WINDOW_MESSAGES

        assert isinstance(DEFAULT_CONTEXT_WINDOW_MESSAGES, int)
        assert DEFAULT_CONTEXT_WINDOW_MESSAGES > 0

    def test_version_is_string(self) -> None:
        from oridecon.ai.constants import __version__

        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_all_exports_present(self) -> None:
        import oridecon.ai.constants as constants_mod

        for name in constants_mod.__all__:
            assert hasattr(constants_mod, name), f"Missing export: {name}"
