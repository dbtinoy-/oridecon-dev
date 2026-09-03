"""Per-format mappers between wire DTOs and the canonical relay IR."""

from __future__ import annotations

from oridecon.ai.relay.mappers.base import FormatMapper, record_loss, warning_messages
from oridecon.ai.relay.mappers.claude import ClaudeMapper
from oridecon.ai.relay.mappers.gemini import GeminiMapper
from oridecon.ai.relay.mappers.openai_chat import OpenAIChatMapper
from oridecon.ai.relay.mappers.openai_responses import OpenAIResponsesMapper

__all__ = [
    "ClaudeMapper",
    "FormatMapper",
    "GeminiMapper",
    "OpenAIChatMapper",
    "OpenAIResponsesMapper",
    "record_loss",
    "warning_messages",
]
