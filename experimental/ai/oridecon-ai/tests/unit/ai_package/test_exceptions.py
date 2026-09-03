"""Tests for oridecon.ai.exceptions."""

from __future__ import annotations

import pytest


class TestAIPackageException:
    """Tests for oridecon.ai.exceptions.AIError."""

    def test_ai_error_is_instantiable(self) -> None:
        from oridecon.ai.exceptions import AIError

        err = AIError("something went wrong in AI")
        assert "something went wrong" in str(err)

    def test_ai_error_is_subclass_of_contracts_base(self) -> None:
        from oridecon.ai.exceptions import AIError
        from oridecon.contracts.ai.exceptions import AIError as ContractsAIError
        from oridecon.contracts.exceptions import OrideconError

        assert issubclass(AIError, ContractsAIError)
        assert issubclass(AIError, OrideconError)

    def test_ai_error_has_error_code(self) -> None:
        from oridecon.ai.exceptions import AIError

        assert AIError._code == "ORI_ERR_AI_005"

    def test_ai_error_can_be_raised_and_caught(self) -> None:
        from oridecon.ai.exceptions import AIError
        from oridecon.contracts.exceptions import OrideconError

        with pytest.raises(OrideconError):
            raise AIError("test error")
