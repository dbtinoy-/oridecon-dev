# oridecon-multimedia-interpolate

Video frame-rate interpolation for the Oridecon Framework — a local RIFE reference-server backend that doubles or quadruples a clip's frame rate by synthesizing midpoint frames.

---

## Overview

`oridecon-multimedia-interpolate` synthesizes intermediate frames between two input frames (or between frames of a video) using a RIFE reference server, and registers a `VideoInterpolationService` for frame-level video interpolation when a `VideoProcessor` is available in the container.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)

## Install

```bash
uv add oridecon-multimedia-interpolate
# Optional extras
uv add "oridecon-multimedia-interpolate[rife-server]"  # RIFE server deps (torch)
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.multimedia.interpolate import InterpolationModule
from oridecon.contracts.multimedia.protocols import InterpolationProvider
from oridecon.contracts.multimedia.types import InterpolationRequest, MediaAsset


@module(imports=[InterpolationModule.configure()])
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        interpolate = await app.container.resolve(InterpolationProvider)
        frame_a = MediaAsset(
            mime_type="image/png", provider="local", bytes_data=b"<png>"
        )
        frame_b = MediaAsset(
            mime_type="image/png", provider="local", bytes_data=b"<png>"
        )
        result = await interpolate.interpolate(
            InterpolationRequest(frame_a=frame_a, frame_b=frame_b)
        )
        if result.is_ok():
            midframe = result.unwrap()  # MediaAsset — synthesized midpoint frame


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `InterpolationModule.configure()` with no arguments to use the `rife` backend at `http://localhost:5500`.

### Option 1 — YAML file

```yaml
# application.yaml
multimedia:
  interpolate:
    backend: "rife"
```

### Option 2 — Profiles + Environment Variables

```bash
export ORI_PROFILE=production
export ORI_MULTIMEDIA__INTERPOLATE__BACKEND=rife
```

### Option 3 — Python

```python
from oridecon.multimedia.interpolate import InterpolationModule
from oridecon.multimedia.interpolate.config import InterpolationConfig

InterpolationModule.configure(config=InterpolationConfig())
```

> Interpolation is frame-pair based — `InterpolationRequest(frame_a=..., frame_b=...)`. There is no configurable factor; `InterpolationConfig` only carries `backend`, `rife_base_url`, and `timeout`.

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `backend` | `"rife"` | `ORI_MULTIMEDIA__INTERPOLATE__BACKEND` | `rife` |
| `rife_base_url` | `"http://localhost:5500"` | `ORI_MULTIMEDIA__INTERPOLATE__RIFE_BASE_URL` | RIFE server URL |
| `timeout` | `15.0` | `ORI_MULTIMEDIA__INTERPOLATE__TIMEOUT` | Request timeout in seconds |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `InterpolationModule.configure(config)` | Configure with explicit interpolation config |
| `InterpolationModule.stub()` | Real module pinned to the default `rife` backend for tests |

## Key Features

- **RIFE backend** — state-of-the-art frame interpolation via a local reference server
- **Video interpolation** — `VideoInterpolationService` for frame-level video interpolation (when `VideoProcessor` is available)
- **Reference server** — `oridecon-interpolate-rife-serve` console script runs the RIFE model server
- **Result-based** — `interpolate() -> Result[MediaAsset, MultimediaError]`; errors are domain values, not exceptions

## Testing

```python
from oridecon import Application
from oridecon.multimedia.interpolate import InterpolationModule


async def test_boot():
    async with Application.boot(modules=[InterpolationModule.stub()]) as app:
        assert app.container is not None
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/multimedia/interpolate/module.py` | `InterpolationModule.configure()` and `.stub()` |
| `src/oridecon/multimedia/interpolate/config.py` | `InterpolationConfig` |
| `src/oridecon/multimedia/interpolate/di/provider.py` | `InterpolationGenerationProvider` — registers `InterpolationProvider`, wires task handlers |
| `src/oridecon/multimedia/interpolate/providers/` | Backend implementations (`rife`) |
| `src/oridecon/multimedia/interpolate/servers/` | Reference-server entry point (`oridecon-interpolate-rife-serve`) |
| `src/oridecon/multimedia/interpolate/video_interpolation_service.py` | `VideoInterpolationService` — frame-level video interpolation |
| `src/oridecon/multimedia/interpolate/tasks.py` | Background interpolation task handlers |
