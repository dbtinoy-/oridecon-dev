# oridecon-multimedia-image

Image generation for the Oridecon Framework — local and API-based backends (`local-http`, `stability`, `openai`, `comfyui`).

---

## Overview

`oridecon-multimedia-image` generates still images from a text prompt. The default backend calls a local HTTP reference server (`http://localhost:5005`) so the package works out of the box with no API keys; hosted backends (Stability AI, OpenAI) and ComfyUI workflows are selectable via config.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)

## Install

```bash
uv add oridecon-multimedia-image
# Optional extras
uv add "oridecon-multimedia-image[stability]"  # Stability AI API
uv add "oridecon-multimedia-image[openai]"     # OpenAI images API
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.multimedia.image import ImageModule
from oridecon.contracts.multimedia import ImageProvider, ImageRequest


@module(imports=[ImageModule.configure()])
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        image = await app.container.resolve(ImageProvider)
        result = await image.generate(ImageRequest(prompt="a cozy cabin in the snow"))
        if result.is_ok():
            asset = result.unwrap()  # MediaAsset — image bytes or URI


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `ImageModule.configure()` with no arguments to use the `local-http` backend at `http://localhost:5005`.

### Option 1 — YAML file

```yaml
# application.yaml
multimedia:
  image:
    backend: "stability"
    comfyui_base_url: "http://localhost:8188"
```

### Option 2 — Profiles + Environment Variables

```bash
export ORI_PROFILE=production
export ORI_MULTIMEDIA__IMAGE__BACKEND=openai
export ORI_MULTIMEDIA__IMAGE__OPENAI_MODEL=dall-e-3
```

### Option 3 — Python

```python
from oridecon.multimedia.image import ImageModule
from oridecon.multimedia.image.config import ImageConfig

ImageModule.configure(config=ImageConfig(backend="openai", openai_model="dall-e-3"))
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `backend` | `"local-http"` | `ORI_MULTIMEDIA__IMAGE__BACKEND` | `local-http`, `stability`, `openai`, `comfyui` |
| `local_http_base_url` | `"http://localhost:5005"` | `ORI_MULTIMEDIA__IMAGE__LOCAL_HTTP_BASE_URL` | Local reference server URL |
| `openai_api_key_secret_name` | `"openai_api_key"` | `ORI_MULTIMEDIA__IMAGE__OPENAI_API_KEY_SECRET_NAME` | Secret name for the OpenAI API key |
| `openai_model` | `"dall-e-3"` | `ORI_MULTIMEDIA__IMAGE__OPENAI_MODEL` | OpenAI image model |
| `openai_base_url` | `"https://api.openai.com"` | `ORI_MULTIMEDIA__IMAGE__OPENAI_BASE_URL` | OpenAI-compatible base URL |
| `stability_api_key_secret_name` | `"stability_api_key"` | `ORI_MULTIMEDIA__IMAGE__STABILITY_API_KEY_SECRET_NAME` | Secret name for the Stability AI API key |
| `comfyui_base_url` | `"http://localhost:8188"` | `ORI_MULTIMEDIA__IMAGE__COMFYUI_BASE_URL` | ComfyUI server URL |
| `comfyui_checkpoint` | `"sd_xl_base_1.0.safetensors"` | `ORI_MULTIMEDIA__IMAGE__COMFYUI_CHECKPOINT` | ComfyUI checkpoint name |
| `comfyui_workflow_path` | `None` | `ORI_MULTIMEDIA__IMAGE__COMFYUI_WORKFLOW_PATH` | Path to a custom ComfyUI workflow JSON |
| `comfyui_steps` | `20` | `ORI_MULTIMEDIA__IMAGE__COMFYUI_STEPS` | ComfyUI sampling steps |
| `comfyui_cfg_scale` | `7.0` | `ORI_MULTIMEDIA__IMAGE__COMFYUI_CFG_SCALE` | ComfyUI CFG scale |
| `comfyui_poll_interval` | `1.0` | `ORI_MULTIMEDIA__IMAGE__COMFYUI_POLL_INTERVAL` | ComfyUI progress poll interval in seconds |
| `timeout` | `60.0` | `ORI_MULTIMEDIA__IMAGE__TIMEOUT` | Request timeout in seconds |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `ImageModule.configure(config)` | Configure with explicit image config |
| `ImageModule.stub()` | Real module pinned to the default `local-http` backend for tests |

## Key Features

- **Four backends** — `local-http`, `stability`, `openai`, `comfyui`
- **ComfyUI workflows** — custom workflow JSON with checkpoint, steps, and CFG scale
- **Secret-managed API keys** — provider keys resolved by name through the secrets backend
- **Result-based** — `generate() -> Result[MediaAsset, MultimediaError]`; errors are domain values, not exceptions

## Testing

```python
from oridecon import Application
from oridecon.multimedia.image import ImageModule


async def test_boot():
    async with Application.boot(modules=[ImageModule.stub()]) as app:
        assert app.container is not None
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/multimedia/image/module.py` | `ImageModule.configure()` and `.stub()` |
| `src/oridecon/multimedia/image/config.py` | `ImageConfig` |
| `src/oridecon/multimedia/image/di/provider.py` | `ImageGenerationProvider` — registers `ImageProvider`, wires task handlers |
| `src/oridecon/multimedia/image/providers/` | Backend implementations (`local_http`, `stability`, `openai`, `comfyui`) |
| `src/oridecon/multimedia/image/tasks.py` | Background generation task handlers |
| `src/oridecon/multimedia/image/exceptions.py` | `ImageGenerationError` hierarchy |
