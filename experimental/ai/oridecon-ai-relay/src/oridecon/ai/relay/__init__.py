"""Relay protocol conversion engine for the Oridecon AI subsystem.

This package implements the pure, synchronous conversion engine that
shapes OpenAI Chat Completions, OpenAI Responses, Anthropic Messages,
and Gemini generateContent wire payloads into one canonical IR.  It
performs no HTTP, channel selection, billing, or model selection.
"""

from __future__ import annotations

from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

from oridecon.ai.relay.context import ConversionContext
from oridecon.ai.relay.engine import (
    RelayConverterEngine,
    convert_request_by_id,
    convert_request_via,
    convert_response_by_id,
    convert_response_via,
)
from oridecon.ai.relay.errors import (
    malformed_payload,
    media_resolution_required,
    missing_required_option,
    translate,
    unsupported_feature,
    unsupported_format,
)
from oridecon.ai.relay.mappers.base import FormatMapper, record_loss, warning_messages
from oridecon.ai.relay.module import RelayModule
from oridecon.ai.relay.quality import ROUTE_QUALITY, route_quality
from oridecon.ai.relay.registry import (
    CONVERTER_VERSION,
    RelayConverterRegistry,
    RouteSpec,
)

__all__ = [
    "CONVERTER_VERSION",
    "ROUTE_QUALITY",
    "ConversionContext",
    "FormatMapper",
    "RelayConverterEngine",
    "RelayConverterRegistry",
    "RelayModule",
    "RouteSpec",
    "convert_request_by_id",
    "convert_request_via",
    "convert_response_by_id",
    "convert_response_via",
    "malformed_payload",
    "media_resolution_required",
    "missing_required_option",
    "record_loss",
    "route_quality",
    "translate",
    "unsupported_feature",
    "unsupported_format",
    "warning_messages",
]
