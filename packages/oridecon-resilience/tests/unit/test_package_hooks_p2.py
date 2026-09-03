"""P2 hook surface import verification for oridecon-resilience."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, is_dataclass

import pytest


def test_resilience_hooks_root_module_exists() -> None:
    import oridecon.resilience
    from oridecon.resilience.hooks import (
        CircuitClosedHook,
        CircuitOpenedHook,
        RetryAttemptedHook,
    )

    assert CircuitOpenedHook.__name__ == "CircuitOpenedHook"
    assert CircuitClosedHook.__name__ == "CircuitClosedHook"
    assert RetryAttemptedHook.__name__ == "RetryAttemptedHook"
    assert oridecon.resilience.CircuitOpenedHook is CircuitOpenedHook
    assert oridecon.resilience.CircuitClosedHook is CircuitClosedHook
    assert oridecon.resilience.RetryAttemptedHook is RetryAttemptedHook


def test_resilience_hook_payloads_are_frozen_and_keyword_only() -> None:
    from oridecon.resilience.hooks import CircuitOpenedHook, RetryAttemptedHook

    opened = CircuitOpenedHook(circuit_name="payment-service")
    retry = RetryAttemptedHook(operation="send_payment", attempt=2)

    assert is_dataclass(opened)
    assert is_dataclass(retry)

    with pytest.raises(TypeError):
        CircuitOpenedHook("payment-service")  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        opened.circuit_name = "other"  # type: ignore[misc]
