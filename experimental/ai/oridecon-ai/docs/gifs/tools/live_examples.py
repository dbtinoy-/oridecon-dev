"""Live Ollama examples for tool-calling demo."""

import asyncio

from oridecon.ai.llm.docs.gifs.tools.registry import OLLAMA_BASE, OLLAMA_MODEL, p, check


async def example1_live_openai_compat():
    """Live OpenAI-compatible round trip on Ollama /v1."""
    from oridecon.ai.llm.clients.openai import OpenAIClient
    from oridecon.ai.llm.config import ClientConfig
    from oridecon.ai.llm.types import ChatMessage, Role
    from oridecon.contracts.ai.agents import ToolDefinition
    from oridecon.validation import SecretStr
    from oridecon.ai.llm.docs.gifs.tools.registry import WEATHER_TOOL

    config = ClientConfig(
        provider="openai",
        model=OLLAMA_MODEL,
        api_key=SecretStr("dummy"),
        api_base=f"{OLLAMA_BASE}/v1",
    )
    client = OpenAIClient(config)
    tool = ToolDefinition(**WEATHER_TOOL)

    res = await client.complete(
        [
            ChatMessage(
                role=Role.USER,
                content="Use the weather tool for Paris, reply with only the tool call.",
            )
        ],
        tools=[tool],
    )
    assert res.is_ok(), f"complete failed: {res.unwrap_err()}"
    comp = res.unwrap()
    p(f"    tool_calls -> {comp.tool_calls}")
    check(
        "tool_calls parsed from OpenAI-compatible response",
        comp.tool_calls is not None
        and comp.tool_calls[0].function.name == "get_weather",
    )


async def example2_live_native_ollama():
    """Live native tool calling on Ollama."""
    from oridecon import Application
    from oridecon.ai.agents import tool
    from oridecon.ai.agents.strategies import FunctionCallingStrategy
    from oridecon.ai.llm import ClientConfig, LLMModule
    from oridecon.contracts.ai import LLMClientProtocol
    from oridecon.ai.llm.docs.gifs.tools.registry import OLLAMA_MODEL

    KNOWLEDGE = {
        "providers": "Oridecon supports 15+ AI providers out of the box:\n"
        "- ollama, openai, anthropic, groq, cohere, mistral, deepseek, gemini\n"
        "- fireworks, together, openrouter, azure-openai, aws-bedrock, cloudflare, google-vertex",
    }

    @tool
    async def search_knowledge(topic: str) -> str:
        """Search the Oridecon knowledge base."""
        for key, info in KNOWLEDGE.items():
            if key in topic.lower():
                return info
        return "Topics: AI providers, modules, agents, extraction"

    async with Application.boot(
        modules=[
            LLMModule.configure(ClientConfig(provider="ollama", model=OLLAMA_MODEL))
        ]
    ) as app:
        llm = await app._container.resolve(LLMClientProtocol)
        strategy = FunctionCallingStrategy(max_iterations=2)
        for _ in range(2):
            try:
                result = await asyncio.wait_for(
                    strategy.execute(
                        message="What AI providers does Oridecon support? List them.",
                        tools=[search_knowledge],
                        history=[],
                        llm=llm,
                    ),
                    timeout=45,
                )
            except TimeoutError:
                p("    attempt timed out — retrying")
                continue
            if result.is_ok():
                response = result.unwrap()
                for step in response.steps:
                    if step.tool_call:
                        tc = step.tool_call
                        p(
                            f"    Tool: {tc.tool_name}({tc.arguments}) -> {str(tc.result)[:50]}"
                        )
                p(f"    Answer: {response.message[:80]}")
                check(
                    "native tool loop completed",
                    response.steps is not None and len(response.steps) >= 2,
                )
                return
            p(f"    failed: {result.unwrap_err()} — retrying")
        p("    Tool calling could not complete")
        check("native tool loop completed", False)
