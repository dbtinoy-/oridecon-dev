"""P2 hook surface import verification for oridecon-queue."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, is_dataclass

import pytest


def test_queue_hooks_root_module_exists() -> None:
    import oridecon.queue
    from oridecon.queue.hooks import (
        MessageConsumedHook,
        MessagePublishedHook,
        QueueDrainedHook,
    )

    assert MessagePublishedHook.__name__ == "MessagePublishedHook"
    assert MessageConsumedHook.__name__ == "MessageConsumedHook"
    assert QueueDrainedHook.__name__ == "QueueDrainedHook"
    assert oridecon.queue.MessagePublishedHook is MessagePublishedHook
    assert oridecon.queue.MessageConsumedHook is MessageConsumedHook
    assert oridecon.queue.QueueDrainedHook is QueueDrainedHook


def test_queue_hook_payloads_are_frozen_and_keyword_only() -> None:
    from oridecon.queue.hooks import MessagePublishedHook, QueueDrainedHook

    published = MessagePublishedHook(queue_name="orders", message_type="OrderCreated")
    drained = QueueDrainedHook(queue_name="orders")

    assert is_dataclass(published)
    assert is_dataclass(drained)

    with pytest.raises(TypeError):
        MessagePublishedHook("orders", "OrderCreated")  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        published.queue_name = "payments"  # type: ignore[misc]
