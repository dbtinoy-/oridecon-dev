"""P3 hook surface import verification for oridecon-ai-feedback."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, fields, is_dataclass

import pytest


def test_feedback_hooks_root_module_exists() -> None:
    import oridecon.ai.feedback
    from oridecon.ai.feedback.hooks import (
        FeedbackProcessedHook,
        FeedbackStoredHook,
        FeedbackSubmittedHook,
    )

    assert oridecon.ai.feedback.FeedbackSubmittedHook is FeedbackSubmittedHook
    assert oridecon.ai.feedback.FeedbackProcessedHook is FeedbackProcessedHook
    assert oridecon.ai.feedback.FeedbackStoredHook is FeedbackStoredHook
    assert "FeedbackSubmittedHook" in oridecon.ai.feedback.__all__
    assert "FeedbackProcessedHook" in oridecon.ai.feedback.__all__
    assert "FeedbackStoredHook" in oridecon.ai.feedback.__all__


def test_feedback_hook_payloads_are_frozen_and_keyword_only() -> None:
    from oridecon.ai.feedback.hooks import (
        FeedbackProcessedHook,
        FeedbackStoredHook,
        FeedbackSubmittedHook,
    )

    submitted = FeedbackSubmittedHook(feedback_type="thumbs_up")
    processed = FeedbackProcessedHook(feedback_type="thumbs_up")
    stored = FeedbackStoredHook(feedback_type="thumbs_up")

    assert is_dataclass(submitted)
    assert is_dataclass(processed)
    assert is_dataclass(stored)
    assert [field.name for field in fields(submitted)] == ["feedback_type"]
    assert [field.name for field in fields(processed)] == ["feedback_type"]
    assert [field.name for field in fields(stored)] == ["feedback_type"]

    with pytest.raises(TypeError):
        FeedbackSubmittedHook("thumbs_up")  # type: ignore[misc]

    with pytest.raises(TypeError):
        FeedbackProcessedHook("thumbs_up")  # type: ignore[misc]

    with pytest.raises(TypeError):
        FeedbackStoredHook("thumbs_up")  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        submitted.feedback_type = "thumbs_down"  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        processed.feedback_type = "thumbs_down"  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        stored.feedback_type = "thumbs_down"  # type: ignore[misc]
