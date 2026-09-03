"""OpenAI-family wire format checks for tool-calling demo."""

import json

from oridecon.ai.llm.docs.gifs.tools.registry import WEATHER_TOOL, p, check


def example3_openai_family_wire():
    """OpenAI-family wire format (offline)."""
    from oridecon.ai.llm.clients._tools_utils import (
        parse_openai_tool_calls,
        serialize_message_for_openai,
        tool_to_openai_format,
    )
    from oridecon.ai.llm.types import (
        ChatMessage,
        FunctionCall,
        Role,
        ToolCall,
    )
    from oridecon.contracts.ai.agents import ToolDefinition

    tool = ToolDefinition(**WEATHER_TOOL)
    wire = tool_to_openai_format(tool)
    p(f"    tools[{0}] -> {json.dumps(wire)}")
    check(
        "tool converted to OpenAI function format",
        wire["type"] == "function" and wire["function"]["name"] == "get_weather",
    )

    assistant = ChatMessage(
        role=Role.ASSISTANT,
        content="",
        tool_calls=[
            ToolCall(
                id="call-1",
                type="function",
                function=FunctionCall(name="get_weather", arguments={"city": "Paris"}),
            )
        ],
    )
    msgs = [serialize_message_for_openai(assistant)]
    check(
        "assistant tool_calls serialized with JSON-encoded arguments",
        msgs[0]["tool_calls"][0]["function"]["name"] == "get_weather"
        and isinstance(msgs[0]["tool_calls"][0]["function"]["arguments"], str),
    )

    parsed = parse_openai_tool_calls(
        [
            {
                "id": "1",
                "type": "function",
                "function": {"name": "get_weather", "arguments": {"city": "Paris"}},
            }
        ]
    )
    check(
        "tool_calls parsed back into ToolCall objects",
        parsed is not None
        and parsed[0].function.name == "get_weather"
        and parsed[0].function.arguments == {"city": "Paris"},
    )


def example4_anthropic_wire():
    """Anthropic wire format (offline)."""
    from oridecon.ai.llm.clients.anthropic import (
        AnthropicClient,
        _tool_to_anthropic,
    )
    from oridecon.ai.llm.types import (
        ChatMessage,
        FunctionCall,
        Role,
        ToolCall,
    )

    client = object.__new__(AnthropicClient)

    tool = _tool_to_anthropic({"function": WEATHER_TOOL})
    p(f"    tools[{0}] -> {json.dumps(tool)}")
    check(
        "tool converted to Anthropic input_schema",
        tool["name"] == "get_weather" and "input_schema" in tool,
    )

    tool_result = client._convert_message(
        ChatMessage(role=Role.TOOL, content="22C, sunny", tool_call_id="call-1")
    )
    check(
        "tool result becomes user turn with tool_result block",
        tool_result["role"] == "user"
        and tool_result["content"][0]["type"] == "tool_result"
        and tool_result["content"][0]["tool_use_id"] == "call-1",
    )

    assistant = client._convert_message(
        ChatMessage(
            role=Role.ASSISTANT,
            content="",
            tool_calls=[
                ToolCall(
                    id="call-1",
                    type="function",
                    function=FunctionCall(
                        name="get_weather", arguments={"city": "Paris"}
                    ),
                )
            ],
        )
    )
    check(
        "assistant tool_calls become tool_use blocks",
        any(
            b.get("type") == "tool_use" and b.get("name") == "get_weather"
            for b in assistant["content"]
        ),
    )
