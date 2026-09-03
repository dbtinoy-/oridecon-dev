---
title: oridecon-ai-llm Configuration
description: Every config key for `ClientConfig` with types, defaults, and env-var names.
---

The config section key is `ai_llm`. Environment prefix: `ORI_AI_LLM__`.

## ClientConfig

| Key | Type | Default | Env Var | Description |
|-----|------|---------|---------|-------------|
| `enabled` | `bool` | `True` | `ORI_AI_LLM__ENABLED` | Enable the LLM subsystem |
| `provider` | `ModelProvider` (str enum) | `"openai"` | `ORI_AI_LLM__PROVIDER` | LLM provider name |
| `model` | `str` | `"gpt-4-turbo"` | `ORI_AI_LLM__MODEL` | Model name or identifier |
| `api_key` | `SecretStr \| None` | `None` | `ORI_AI_LLM__API_KEY` | API key for the provider |
| `api_base` | `str \| None` | `None` | `ORI_AI_LLM__API_BASE` | Custom API base URL |
| `temperature` | `float` | `0.7` | `ORI_AI_LLM__TEMPERATURE` | Sampling temperature (0.0–2.0) |
| `max_tokens` | `int \| None` | `None` | `ORI_AI_LLM__MAX_TOKENS` | Max tokens in response |
| `timeout` | `float` | `60.0` | `ORI_AI_LLM__TIMEOUT` | Request timeout in seconds |
| `enable_cache` | `bool` | `False` | `ORI_AI_LLM__ENABLE_CACHE` | Enable response caching |
| `cache_ttl` | `int` | `3600` | `ORI_AI_LLM__CACHE_TTL` | Cache TTL in seconds |
| `thinking` | `ThinkingConfig \| None` | `None` | `ORI_AI_LLM__THINKING__*` | Thinking/reasoning config |
| `extra` | `dict[str, Any]` | `{}` | `ORI_AI_LLM__EXTRA__*` | Provider-specific extra params |

## ThinkingConfig sub-fields

When `thinking` is set, the `ThinkingConfig` object supports:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `suppress` | `bool` | `False` | Actively suppress thinking tokens |
| `budget_tokens` | `int` | `10000` | Max tokens for reasoning |
| `level` | `str \| None` | `None` | Gemini 3 thinking level (`minimal`, `low`, `medium`, `high`) |
| `effort` | `str \| None` | `None` | OpenAI reasoning effort (`low`, `medium`, `high`) |

## Example YAML

```yaml
# application.yaml
ai_llm:
  provider: openai
  model: gpt-4o
  temperature: 0.3
  max_tokens: 2000
  timeout: 30
  enable_cache: true
  cache_ttl: 7200
  thinking:
    budget_tokens: 5000
```

## Env-var overrides

```bash
export ORI_AI_LLM__PROVIDER=anthropic
export ORI_AI_LLM__MODEL=claude-sonnet-4-20250514
export ORI_AI_LLM__API_KEY=sk-ant-...
export ORI_AI_LLM__TEMPERATURE=0.0
export ORI_AI_LLM__ENABLE_CACHE=true
```

## Provider extras

Install the provider-specific client library:

```bash
uv add "oridecon-ai-llm[openai]"    # openai, tiktoken
uv add "oridecon-ai-llm[anthropic]" # anthropic
uv add "oridecon-ai-llm[ollama]"    # ollama
uv add "oridecon-ai-llm[groq]"     # groq
uv add "oridecon-ai-llm[cohere]"   # cohere
uv add "oridecon-ai-llm[mistral]"  # mistralai
```
