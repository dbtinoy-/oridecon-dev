"""Shared fixtures for oridecon-ai-guard unit tests."""

from __future__ import annotations

import pytest

from oridecon.ai.guard.pipeline.guard_pipeline import GuardPipeline
from oridecon.ai.guard.pipeline.result import GuardCheckResult
from oridecon.result import Result
from oridecon.result import Ok


class AlwaysPassInputGuard:
    """Stub input guard that always passes."""

    name = "always_pass_input"

    async def check(
        self,
        content: str,
        *,
        messages: object = None,
        metadata: object = None,
    ) -> GuardCheckResult:
        return Ok(GuardCheckResult.allow(guard_name=self.name))


class AlwaysBlockInputGuard:
    """Stub input guard that always blocks."""

    name = "always_block_input"

    async def check(
        self,
        content: str,
        *,
        messages: object = None,
        metadata: object = None,
    ) -> GuardCheckResult:
        return Ok(GuardCheckResult.block(guard_name=self.name, reason="blocked by stub"))


class AlwaysRedactInputGuard:
    """Stub input guard that always redacts with a fixed replacement."""

    name = "always_redact_input"

    async def check(
        self,
        content: str,
        *,
        messages: object = None,
        metadata: object = None,
    ) -> GuardCheckResult:
        return Ok(GuardCheckResult.redact(
            guard_name=self.name,
            redacted_content="[REDACTED]",
            reason="redacted by stub",
        ))


class AlwaysPassOutputGuard:
    """Stub output guard that always passes."""

    name = "always_pass_output"

    async def check(
        self,
        content: str,
        *,
        original_input: str = "",
        metadata: object = None,
    ) -> GuardCheckResult:
        return Ok(GuardCheckResult.allow(guard_name=self.name))


class AlwaysBlockOutputGuard:
    """Stub output guard that always blocks."""

    name = "always_block_output"

    async def check(
        self,
        content: str,
        *,
        original_input: str = "",
        metadata: object = None,
    ) -> GuardCheckResult:
        return Ok(GuardCheckResult.block(guard_name=self.name, reason="output blocked"))


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def empty_pipeline() -> GuardPipeline:
    return GuardPipeline(input_guards=[], output_guards=[])


@pytest.fixture()
def pass_pipeline() -> GuardPipeline:
    return GuardPipeline(
        input_guards=[AlwaysPassInputGuard()],
        output_guards=[AlwaysPassOutputGuard()],
    )
