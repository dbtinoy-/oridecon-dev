# oridecon-multimedia-video

Video generation and processing for the Oridecon Framework — local and API-based backends (`local-http`, `runway`, `openai`, `wan22`, `cogvideox`, `svd`, `comfyui`) plus an ffmpeg-backed `VideoProcessor`.

---

## Overview

`oridecon-multimedia-video` generates video from a text prompt and edits existing clips. The default backend calls a local HTTP reference server (`http://localhost:5004`) so the package works out of the box with no API keys; hosted backends (Runway, OpenAI), ComfyUI workflows, and local reference servers (Wan2.2, CogVideoX, SVD) are selectable via config. A built-in `VideoProcessor` provides ffmpeg-based editing (trim, concat, overlay, transcode, subtitles, GIF, and more).

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)

## Install

```bash
uv add oridecon-multimedia-video
# Optional extras
uv add "oridecon-multimedia-video[runway]"            # Runway API
uv add "oridecon-multimedia-video[openai]"            # OpenAI Sora API
uv add "oridecon-multimedia-video[cogvideox-server]"  # local CogVideoX server (torch)
uv add "oridecon-multimedia-video[svd-server]"        # local SVD server (torch)
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.multimedia.video import VideoModule
from oridecon.contracts.multimedia import VideoProvider, VideoRequest


@module(imports=[VideoModule.configure()])
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        video = await app.container.resolve(VideoProvider)
        result = await video.generate(
            VideoRequest(prompt="a drone flying over mountains")
        )
        if result.is_ok():
            asset = result.unwrap()  # MediaAsset — video bytes or URI


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `VideoModule.configure()` with no arguments to use the `local-http` backend at `http://localhost:5004`.

### Option 1 — YAML file

```yaml
# application.yaml
multimedia:
  video:
    backend: "comfyui"
    comfyui_base_url: "http://localhost:8188"
    processing:
      max_concurrent_jobs: 4
```

### Option 2 — Profiles + Environment Variables

```bash
export ORI_PROFILE=production
export ORI_MULTIMEDIA__VIDEO__BACKEND=runway
export ORI_MULTIMEDIA__VIDEO__PROCESSING__MAX_CONCURRENT_JOBS=4
```

### Option 3 — Python

```python
from oridecon.multimedia.video import VideoModule
from oridecon.multimedia.video.config import VideoConfig, VideoProcessingConfig

VideoModule.configure(
    config=VideoConfig(
        backend="comfyui",
        processing=VideoProcessingConfig(max_concurrent_jobs=4),
    )
)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `backend` | `"local-http"` | `ORI_MULTIMEDIA__VIDEO__BACKEND` | `local-http`, `runway`, `openai`, `wan22`, `cogvideox`, `svd`, `comfyui` |
| `local_http_base_url` | `"http://localhost:5004"` | `ORI_MULTIMEDIA__VIDEO__LOCAL_HTTP_BASE_URL` | Local reference server URL |
| `runway_api_key_secret_name` | `"runway_api_key"` | `ORI_MULTIMEDIA__VIDEO__RUNWAY_API_KEY_SECRET_NAME` | Secret name for the Runway API key |
| `openai_api_key_secret_name` | `"openai_api_key"` | `ORI_MULTIMEDIA__VIDEO__OPENAI_API_KEY_SECRET_NAME` | Secret name for the OpenAI API key |
| `openai_model` | `"sora-2"` | `ORI_MULTIMEDIA__VIDEO__OPENAI_MODEL` | OpenAI video model |
| `openai_base_url` | `"https://api.openai.com"` | `ORI_MULTIMEDIA__VIDEO__OPENAI_BASE_URL` | OpenAI-compatible base URL |
| `wan22_base_url` | `"http://localhost:5200"` | `ORI_MULTIMEDIA__VIDEO__WAN22_BASE_URL` | Wan2.2 server URL |
| `cogvideox_base_url` | `"http://localhost:5201"` | `ORI_MULTIMEDIA__VIDEO__COGVIDEOX_BASE_URL` | CogVideoX server URL |
| `svd_base_url` | `"http://localhost:5202"` | `ORI_MULTIMEDIA__VIDEO__SVD_BASE_URL` | SVD server URL |
| `comfyui_base_url` | `"http://localhost:8188"` | `ORI_MULTIMEDIA__VIDEO__COMFYUI_BASE_URL` | ComfyUI server URL |
| `comfyui_checkpoint` | `"svd_xt_1_1.safetensors"` | `ORI_MULTIMEDIA__VIDEO__COMFYUI_CHECKPOINT` | ComfyUI checkpoint name |
| `comfyui_workflow_path` | `None` | `ORI_MULTIMEDIA__VIDEO__COMFYUI_WORKFLOW_PATH` | Path to a custom ComfyUI workflow JSON |
| `comfyui_fps` | `6` | `ORI_MULTIMEDIA__VIDEO__COMFYUI_FPS` | Output frames per second |
| `comfyui_motion_bucket_id` | `127` | `ORI_MULTIMEDIA__VIDEO__COMFYUI_MOTION_BUCKET_ID` | SVD motion bucket |
| `comfyui_poll_interval` | `1.0` | `ORI_MULTIMEDIA__VIDEO__COMFYUI_POLL_INTERVAL` | ComfyUI progress poll interval in seconds |
| `timeout` | `60.0` | `ORI_MULTIMEDIA__VIDEO__TIMEOUT` | Request timeout in seconds |
| `processing.ffmpeg_binary` | `"ffmpeg"` | `ORI_MULTIMEDIA__VIDEO__PROCESSING__FFMPEG_BINARY` | ffmpeg executable path |
| `processing.max_concurrent_jobs` | `2` | `ORI_MULTIMEDIA__VIDEO__PROCESSING__MAX_CONCURRENT_JOBS` | Max concurrent ffmpeg jobs |
| `processing.temp_dir` | `None` | `ORI_MULTIMEDIA__VIDEO__PROCESSING__TEMP_DIR` | Temp dir for intermediate frames |
| `processing.timeout` | `300.0` | `ORI_MULTIMEDIA__VIDEO__PROCESSING__TIMEOUT` | Processing job timeout in seconds |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `VideoModule.configure(config)` | Configure with explicit video config |
| `VideoModule.stub()` | Real module pinned to the default `local-http` backend for tests |

## Key Features

- **Seven generation backends** — `local-http`, `runway`, `openai`, `wan22`, `cogvideox`, `svd`, `comfyui`
- **`VideoProcessor`** — ffmpeg-backed editing: trim, concat, overlays, composition, subtitles, audio mux, thumbnails, GIF, transcode, speed, crop, color filters, raw filter graphs
- **Reference servers** — `oridecon-video-*-serve` console scripts run each local model server
- **Secret-managed API keys** — provider keys resolved by name through the secrets backend
- **Result-based** — `generate() -> Result[MediaAsset, MultimediaError]`; errors are domain values, not exceptions

## Testing

```python
from oridecon import Application
from oridecon.multimedia.video import VideoModule


async def test_boot():
    async with Application.boot(modules=[VideoModule.stub()]) as app:
        assert app.container is not None
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/multimedia/video/module.py` | `VideoModule.configure()` and `.stub()` |
| `src/oridecon/multimedia/video/config.py` | `VideoConfig`, `VideoProcessingConfig` |
| `src/oridecon/multimedia/video/di/provider.py` | `VideoGenerationProvider` — registers `VideoProvider` + `VideoProcessor`, wires task handlers |
| `src/oridecon/multimedia/video/providers/` | Generation backends (`local_http`, `runway`, `openai`, `wan22`, `cogvideox`, `svd`, `comfyui`) |
| `src/oridecon/multimedia/video/processing/` | ffmpeg-backed `VideoProcessor` (argv, ffmpeg, media I/O) |
| `src/oridecon/multimedia/video/servers/` | Reference-server entry points (`oridecon-video-*-serve`) |
| `src/oridecon/multimedia/video/tasks.py` | Background generation task handlers |
| `src/oridecon/multimedia/video/exceptions.py` | `VideoGenerationError` hierarchy |
