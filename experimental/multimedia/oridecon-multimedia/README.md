# oridecon-multimedia

Multimedia generation umbrella for Oridecon Framework — TTS, music, video, image, upscale, interpolation, and beat analysis in one DI module.

---

## Overview

`oridecon-multimedia` is the **orchestration layer** for the Oridecon multimedia subsystem. It wires seven independent generation packages (`oridecon-multimedia-tts`, `oridecon-multimedia-music`, `oridecon-multimedia-video`, `oridecon-multimedia-image`, `oridecon-multimedia-upscale`, `oridecon-multimedia-interpolate`, `oridecon-multimedia-beat`) through the framework's DI container and entry-point discovery, and exposes a single `MultimediaModule` for application composition. Generated assets are normalized into blob storage (`MediaAsset` with bytes or URI), and long-running jobs are submitted to the task queue.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)

## Install

```bash
uv add oridecon-multimedia
# Subsystem extras (per backend, e.g. torch-based reference servers)
uv add "oridecon-multimedia-tts[elevenlabs,openai]"
uv add "oridecon-multimedia-music[ace-step-server]"
uv add "oridecon-multimedia-video[wan22-server,cogvideox-server]"
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.multimedia import MultimediaModule
from oridecon.contracts.multimedia import TTSProvider, TTSRequest


@module(imports=[MultimediaModule.configure()])
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        tts = await app.container.resolve(TTSProvider)
        result = await tts.generate(TTSRequest(text="Hello from Oridecon"))
        if result.is_ok():
            asset = result.unwrap()  # MediaAsset — bytes or URI in blob storage


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `MultimediaModule.configure()` with no arguments to use defaults. Default backends: `local-http` for TTS, music, video, and image; `librosa` for beat analysis; `rife` for frame interpolation; `real-esrgan` for upscaling.

### Option 1 — YAML file

```yaml
# application.yaml
multimedia:
  tts:
    backend: "elevenlabs"
    elevenlabs_voice_id: "21m00Tcm4TlvDq8ikWAM"
  music:
    backend: "stable-audio-open"
  video:
    backend: "local-http"
  storage_path_prefix: "multimedia/"
  cache_results: true
```

### Option 2 — Profiles + Environment Variables

```bash
export ORI_PROFILE=production
export ORI_MULTIMEDIA__TTS__BACKEND=elevenlabs
export ORI_MULTIMEDIA__STORAGE_PATH_PREFIX=multimedia/
```

### Option 3 — Python

```python
from oridecon.multimedia import MultimediaModule, MultimediaConfig
from oridecon.multimedia.tts.config import TTSConfig

MultimediaModule.configure(
    config=MultimediaConfig(
        tts=TTSConfig(backend="elevenlabs", elevenlabs_voice_id="21m00Tcm4TlvDq8ikWAM"),
        cache_results=True,
    )
)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `tts` | `TTSConfig()` | `ORI_MULTIMEDIA__TTS__*` | TTS subsystem config |
| `music` | `MusicConfig()` | `ORI_MULTIMEDIA__MUSIC__*` | Music generation config |
| `video` | `VideoConfig()` | `ORI_MULTIMEDIA__VIDEO__*` | Video generation + processing config |
| `image` | `ImageConfig()` | `ORI_MULTIMEDIA__IMAGE__*` | Image generation config |
| `upscale` | `UpscaleConfig()` | `ORI_MULTIMEDIA__UPSCALE__*` | Image/video upscale config |
| `interpolate` | `InterpolationConfig()` | `ORI_MULTIMEDIA__INTERPOLATE__*` | Frame interpolation config |
| `beat` | `BeatAnalysisConfig()` | `ORI_MULTIMEDIA__BEAT__*` | Beat analysis config |
| `storage_path_prefix` | `"multimedia/"` | `ORI_MULTIMEDIA__STORAGE_PATH_PREFIX` | Blob storage key prefix for generated assets |
| `cache_results` | `False` | `ORI_MULTIMEDIA__CACHE_RESULTS` | Cache generation results in the cache backend |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `MultimediaModule.configure(config)` | Configure with all seven subsystems wired |
| `MultimediaModule.stub()` | Stub module for testing — discovers installed subsystem stubs via `oridecon.multimedia.modules` entry points |

## Key Features

- **One module, seven subsystems** — TTS, music, video, image, upscale, interpolation, and beat analysis wired through DI
- **Entry-point discovery** — subsystem providers register via `oridecon.multimedia.subsystems`; no manual wiring
- **`SubsystemAccessor`** — single accessor to generate any media type (`generate(request) -> Result[MediaAsset, MultimediaError]`)
- **`VideoAccessor` / `ComposeAccessor` / `BeatAccessor`** — video processing, timeline composition, and beat analysis with dedicated accessors
- **Async job submission** — `submit()` dispatches generation to the task queue with idempotency and generation events
- **Blob-backed assets** — results normalized into `MediaAsset` (bytes or URI) via `oridecon-storage`

## Testing

```python
from oridecon import Application
from oridecon.multimedia import MultimediaModule


async def test_boot():
    async with Application.boot(modules=[MultimediaModule.stub()]) as app:
        assert app.container is not None
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/multimedia/__init__.py` | Public API: `MultimediaModule`, `MultimediaProvider`, `MultimediaConfig`, accessors, `Timeline` |
| `src/oridecon/multimedia/module.py` | `MultimediaModule.configure()` and `MultimediaModule.stub()` |
| `src/oridecon/multimedia/config.py` | `MultimediaConfig` — nested subsystem configs + storage/cache options |
| `src/oridecon/multimedia/di/provider.py` | `MultimediaProvider` — registers and boots the seven sub-providers |
| `src/oridecon/multimedia/accessors/` | `SubsystemAccessor`, `VideoAccessor`, `ComposeAccessor`, `BeatAccessor` |
| `src/oridecon/multimedia/timeline/` | `Timeline`, `TimelineRenderTask` — timeline composition |
| `src/oridecon/multimedia/types.py` | `JobHandle` and accessor types |
