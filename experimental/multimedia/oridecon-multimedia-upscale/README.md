# oridecon-multimedia-upscale

Image and video super-resolution for the Oridecon Framework — local reference-server backends (`real-esrgan`, `hat`).

---

## Overview

`oridecon-multimedia-upscale` upscales images 2x or 4x with Real-ESRGAN or HAT reference servers, and registers a `VideoUpscaleService` for frame-level video upscaling when a `VideoProcessor` is available in the container.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)

## Install

```bash
uv add oridecon-multimedia-upscale
# Optional extras
uv add "oridecon-multimedia-upscale[real-esrgan-server]"  # Real-ESRGAN server deps
uv add "oridecon-multimedia-upscale[hat-server]"          # HAT server deps
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.multimedia.upscale import UpscaleModule
from oridecon.contracts.multimedia import UpscaleProvider, UpscaleRequest, MediaAsset


@module(imports=[UpscaleModule.configure()])
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        upscale = await app.container.resolve(UpscaleProvider)
        asset = MediaAsset(mime_type="image/png", provider="local", bytes_data=b"<png>")
        result = await upscale.upscale(UpscaleRequest(asset=asset, scale_factor=4))
        if result.is_ok():
            upscaled = result.unwrap()  # MediaAsset — upscaled image bytes or URI


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `UpscaleModule.configure()` with no arguments to use the `real-esrgan` backend at `http://localhost:5400`.

### Option 1 — YAML file

```yaml
# application.yaml
multimedia:
  upscale:
    backend: "hat"
```

### Option 2 — Profiles + Environment Variables

```bash
export ORI_PROFILE=production
export ORI_MULTIMEDIA__UPSCALE__BACKEND=real-esrgan
```

### Option 3 — Python

```python
from oridecon.multimedia.upscale import UpscaleModule
from oridecon.multimedia.upscale.config import UpscaleConfig

UpscaleModule.configure(config=UpscaleConfig(backend="hat"))
```

> The upscale factor is a per-request parameter — `UpscaleRequest(asset=..., scale_factor=Literal[2, 4])`, default `4`. It is not part of `UpscaleConfig`.

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `backend` | `"real-esrgan"` | `ORI_MULTIMEDIA__UPSCALE__BACKEND` | `real-esrgan`, `hat` |
| `real_esrgan_base_url` | `"http://localhost:5400"` | `ORI_MULTIMEDIA__UPSCALE__REAL_ESRGAN_BASE_URL` | Real-ESRGAN server URL |
| `hat_base_url` | `"http://localhost:5401"` | `ORI_MULTIMEDIA__UPSCALE__HAT_BASE_URL` | HAT server URL |
| `timeout` | `30.0` | `ORI_MULTIMEDIA__UPSCALE__TIMEOUT` | Request timeout in seconds |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `UpscaleModule.configure(config)` | Configure with explicit upscale config |
| `UpscaleModule.stub()` | Real module pinned to the default `real-esrgan` backend for tests |

## Key Features

- **Two backends** — `real-esrgan`, `hat` reference servers
- **Video upscaling** — `VideoUpscaleService` for frame-level video super-resolution (when `VideoProcessor` is available)
- **Reference servers** — `oridecon-upscale-real-esrgan-serve` and `oridecon-upscale-hat-serve` console scripts run each local model server
- **Result-based** — `upscale() -> Result[MediaAsset, MultimediaError]`; errors are domain values, not exceptions

## Testing

```python
from oridecon import Application
from oridecon.multimedia.upscale import UpscaleModule


async def test_boot():
    async with Application.boot(modules=[UpscaleModule.stub()]) as app:
        assert app.container is not None
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/multimedia/upscale/module.py` | `UpscaleModule.configure()` and `.stub()` |
| `src/oridecon/multimedia/upscale/config.py` | `UpscaleConfig` |
| `src/oridecon/multimedia/upscale/di/provider.py` | `UpscaleGenerationProvider` — registers `UpscaleProvider`, wires task handlers |
| `src/oridecon/multimedia/upscale/providers/` | Backend implementations (`real_esrgan`, `hat`) |
| `src/oridecon/multimedia/upscale/servers/` | Reference-server entry points (`oridecon-upscale-*-serve`) |
| `src/oridecon/multimedia/upscale/video_upscale_service.py` | `VideoUpscaleService` — frame-level video upscaling |
| `src/oridecon/multimedia/upscale/tasks.py` | Background upscale task handlers |
| `src/oridecon/multimedia/upscale/exceptions.py` | `UpscaleError` hierarchy |
