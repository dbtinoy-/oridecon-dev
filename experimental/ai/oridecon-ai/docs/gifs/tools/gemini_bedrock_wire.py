"""Gemini and Bedrock/Cohere wire format checks for tool-calling demo."""

import json

from oridecon.ai.llm.docs.gifs.tools.registry import WEATHER_TOOL, p, check


def example5_gemini_wire():
    """Gemini + Vertex wire format (offline)."""
    from oridecon.ai.llm.clients.gemini_helpers import (
        messages_to_gemini,
        parse_gemini_response_with_tools,
        tool_to_gemini_function,
    )
    from oridecon.ai.llm.types import (
        ChatMessage,
        FunctionCall,
        Role,
        ToolCall,
    )
    from oridecon.contracts.ai.agents import ToolDefinition

    fn = tool_to_gemini_function(ToolDefinition(**WEATHER_TOOL))
    p(f"    functionDeclaration -> {json.dumps(fn)}")
    check(
        "tool converted to Gemini functionDeclaration",
        fn["name"] == "get_weather" and "parameters" in fn,
    )

    contents = messages_to_gemini(
        [
            ChatMessage(role=Role.USER, content="Weather for Paris?"),
            ChatMessage(
                role=Role.ASSISTANT,
                content="",
                tool_calls=[
                    ToolCall(
                        id="get_weather",
                        type="function",
                        function=FunctionCall(
                            name="get_weather", arguments={"city": "Paris"}
                        ),
                    )
                ],
            ),
            ChatMessage(
                role=Role.TOOL, content="22C, sunny", tool_call_id="get_weather"
            ),
        ]
    )
    model_parts = contents[1]["parts"]
    tool_round_trip = contents[2]["parts"]
    check(
        "assistant tool_calls become functionCall parts",
        any(
            "functionCall" in part and part["functionCall"]["name"] == "get_weather"
            for part in model_parts
        ),
    )
    check(
        "tool result becomes functionResponse part",
        tool_round_trip[0]["functionResponse"]["name"] == "get_weather",
    )

    completion = parse_gemini_response_with_tools(
        {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "functionCall": {
                                    "name": "get_weather",
                                    "args": {"city": "Paris"},
                                }
                            }
                        ]
                    }
                }
            ],
            "usageMetadata": {
                "promptTokenCount": 5,
                "candidatesTokenCount": 3,
                "totalTokenCount": 8,
            },
        },
        model="gemini-test",
    )
    check(
        "functionCall response parsed into ToolCall",
        completion.tool_calls is not None
        and completion.tool_calls[0].function.name == "get_weather",
    )


async def example6_bedrock_cohere_wire():
    """Bedrock + Cohere wire format (offline)."""
    from oridecon.ai.llm.clients._bedrock_mappers import (
        parse_bedrock_response,
        tool_to_bedrock,
    )
    from oridecon.ai.llm.clients._cohere_mappers import map_cohere_tools
    from oridecon.ai.llm.clients.aws_bedrock import BedrockClient
    from oridecon.ai.llm.types import (
        ChatMessage,
        FunctionCall,
        Role,
        ToolCall,
    )
    from oridecon.contracts.ai.agents import ToolDefinition

    tool = ToolDefinition(**WEATHER_TOOL)

    spec = tool_to_bedrock(tool)
    p(f"    bedrock toolSpec -> {json.dumps(spec)}")
    check(
        "bedrock tool converted to toolSpec",
        spec["toolSpec"]["name"] == "get_weather"
        and "json" in spec["toolSpec"]["inputSchema"],
    )

    client = object.__new__(BedrockClient)

    async def _bedrock_msgs():
        return await client._to_bedrock_messages_async(
            [
                ChatMessage(
                    role=Role.ASSISTANT,
                    content="",
                    tool_calls=[
                        ToolCall(
                            id="tool-1",
                            type="function",
                            function=FunctionCall(
                                name="get_weather", arguments={"city": "Paris"}
                            ),
                        )
                    ],
                ),
                ChatMessage(
                    role=Role.TOOL, content="22C, sunny", tool_call_id="tool-1"
                ),
            ]
        )

    blocks = await _bedrock_msgs()
    used_tool_use = any(
        b.get("toolUse") and b["toolUse"]["name"] == "get_weather"
        for b in blocks[0]["content"]
    )
    used_result = blocks[1]["role"] == "user" and any(
        b.get("toolResult") and b["toolResult"]["toolUseId"] == "tool-1"
        for b in blocks[1]["content"]
    )
    check("bedrock assistant tool_calls become toolUse blocks", used_tool_use)
    check("bedrock tool result becomes toolResult user turn", used_result)

    bedrock_completion = parse_bedrock_response(
        {
            "output": {
                "message": {
                    "content": [
                        {
                            "toolUse": {
                                "toolUseId": "tool-1",
                                "name": "get_weather",
                                "input": {"city": "Paris"},
                            }
                        }
                    ]
                }
            },
            "usage": {"inputTokens": 5, "outputTokens": 3, "totalTokens": 8},
            "stopReason": "tool_use",
        },
        model="bedrock-test",
    )
    check(
        "bedrock toolUse parsed into ToolCall",
        bedrock_completion.tool_calls is not None
        and bedrock_completion.tool_calls[0].function.name == "get_weather",
    )

    cohere_tools = map_cohere_tools([tool])
    p(f"    cohere tools[0] -> {json.dumps(cohere_tools[0])}")
    check(
        "cohere tool converted to parameter_definitions",
        cohere_tools[0]["name"] == "get_weather"
        and "city" in cohere_tools[0]["parameter_definitions"],
    )

    from oridecon.ai.llm.clients._cohere_mappers import _cohere_assistant_tool_calls

    calls = _cohere_assistant_tool_calls(
        [
            ToolCall(
                id="call-1",
                type="function",
                function=FunctionCall(name="get_weather", arguments={"city": "Paris"}),
            )
        ]
    )
    check(
        "cohere assistant tool_calls serialized",
        calls == [{"name": "get_weather", "parameters": {"city": "Paris"}}],
    )
