"""OpenAI Responses request and response mapper.

Converts the OpenAI Responses wire DTOs
(:class:`ResponsesRequest` / :class:`ResponsesResponse`) into the
canonical relay IR and back.  Stream conversion is handled by the shared
stream lifecycle task and reports ``unsupported_feature`` until then.
"""

from __future__ import annotations

from oridecon.ai.relay.mappers.openai_responses.items import ItemsMixin
from oridecon.ai.relay.mappers.openai_responses.request import RequestMixin
from oridecon.ai.relay.mappers.openai_responses.response import ResponseMixin
from oridecon.ai.relay.mappers.openai_responses.stream import StreamMixin
from oridecon.ai.relay.mappers.openai_responses.utils import _TARGET

__all__ = ["OpenAIResponsesMapper"]


class OpenAIResponsesMapper(
    RequestMixin,
    ItemsMixin,
    ResponseMixin,
    StreamMixin,
):
    """Bidirectional OpenAI Responses converter.

    Attributes:
        format: The wire format this mapper handles.
    """

    format = _TARGET
