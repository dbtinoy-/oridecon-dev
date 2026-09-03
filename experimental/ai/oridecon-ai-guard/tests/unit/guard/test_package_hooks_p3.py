"""P3 hook surface import verification for oridecon-ai-guard."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, fields, is_dataclass

import pytest


def test_guard_hooks_root_module_exists() -> None:
    import oridecon.ai.guard
    from oridecon.ai.guard.hooks import (
        GuardInputCheckedHook,
        GuardOutputCheckedHook,
        GuardPipelineCompletedHook,
    )

    assert oridecon.ai.guard.GuardInputCheckedHook is GuardInputCheckedHook
    assert oridecon.ai.guard.GuardOutputCheckedHook is GuardOutputCheckedHook
    assert oridecon.ai.guard.GuardPipelineCompletedHook is GuardPipelineCompletedHook

    assert "GuardInputCheckedHook" in oridecon.ai.guard.__all__
    assert "GuardOutputCheckedHook" in oridecon.ai.guard.__all__
    assert "GuardPipelineCompletedHook" in oridecon.ai.guard.__all__


def test_guard_hook_payloads_are_frozen_and_keyword_only() -> None:
    from oridecon.ai.guard.hooks import (
        GuardInputCheckedHook,
        GuardOutputCheckedHook,
        GuardPipelineCompletedHook,
    )

    checked_input = GuardInputCheckedHook(guard_name="PromptInjectionDetector", blocked=False)
    checked_output = GuardOutputCheckedHook(guard_name="PIIRedactor", blocked=False)
    completed = GuardPipelineCompletedHook(blocked=False)

    assert is_dataclass(checked_input)
    assert is_dataclass(checked_output)
    assert is_dataclass(completed)

    # Field shape assertions
    input_field_names = {f.name for f in fields(checked_input)}
    assert input_field_names == {"guard_name", "blocked"}

    output_field_names = {f.name for f in fields(checked_output)}
    assert output_field_names == {"guard_name", "blocked"}

    completed_field_names = {f.name for f in fields(completed)}
    assert completed_field_names == {"blocked"}

    # keyword-only enforcement
    with pytest.raises(TypeError):
        GuardInputCheckedHook("PromptInjectionDetector", False)  # type: ignore[misc]

    with pytest.raises(TypeError):
        GuardOutputCheckedHook("PIIRedactor", False)  # type: ignore[misc]

    with pytest.raises(TypeError):
        GuardPipelineCompletedHook(False)  # type: ignore[misc]

    # frozen enforcement
    with pytest.raises(FrozenInstanceError):
        checked_input.blocked = True  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        checked_output.blocked = True  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        completed.blocked = True  # type: ignore[misc]
