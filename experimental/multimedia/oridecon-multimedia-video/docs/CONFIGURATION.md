# Configuration

Configuration options for `oridecon-multimedia-video`.

---

## Overview

Configuration lives on two `BaseConfig` classes:

| Class | `config_section` | Purpose |
|-------|------------------|---------|
| `VideoConfig` | `"multimedia_video"` | Generation subsystem (backend, base URLs, API secrets, ComfyUI knobs) |
| `VideoProcessingConfig` | `"multimedia_video_processing"` | ffmpeg processing pipeline (nested under `VideoConfig.processing`) |

As a subsystem of the `oridecon-multimedia` umbrella, config is nested under the `multimedia:` key in `application.yaml` with prefix `ORI_MULTIMEDIA__VIDEO__`. Or pass a `VideoConfig` directly to `VideoModule.configure(...)`.

### Zero-config default

`VideoModule.configure()` → `VideoConfig(backend="local-http")` — generation against a local server at `http://localhost:5004`, processing enabled when the `ffmpeg` binary is on `PATH`.

---

## Basic Example

```yaml
multimedia:
  video:
    backend: "comfyui"
    comfyui_base_url: "http://localhost:8188"
    comfyui_checkpoint: "svd_xt_1_1.safetensors"
    processing:
      ffmpeg_binary: "ffmpeg"
      max_concurrent_jobs: 4
      temp_dir: "/var/tmp/oridecon"
      timeout: 300.0
```

```python
from oridecon.multimedia.video import VideoModule
from oridecon.multimedia.video.config import VideoConfig, VideoProcessingConfig

VideoModule.configure(
    config=VideoConfig(
        backend="comfyui",
        comfyui_base_url="http://localhost:8188",
        processing=VideoProcessingConfig(max_concurrent_jobs=4),
    )
)
```

---

## Options

### `VideoConfig`

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `backend` | `Literal["local-http", "runway", "openai", "wan22", "cogvideox", "svd", "comfyui"]` | `"local-http"` | Generation backend selected at registration |
| `local_http_base_url` | `str` | `"http://localhost:5004"` | Local reference server base URL |
| `runway_api_key_secret_name` | `str` | `"runway_api_key"` | Secret name resolved via `AsyncSecretStoreProtocol` for Runway |
| `openai_api_key_secret_name` | `str` | `"openai_api_key"` | Secret name for the OpenAI gateway |
| `openai_model` | `str` | `"sora-2"` | Default model sent as `payload["model"]` (`VideoRequest.model` overrides) |
| `openai_base_url` | `str` | `"https://api.openai.com"` | OpenAI-compatible base URL (gateway routing) |
| `wan22_base_url` | `str` | `"http://localhost:5200"` | Wan2.2 reference server |
| `cogvideox_base_url` | `str` | `"http://localhost:5201"` | CogVideoX reference server |
| `svd_base_url` | `str` | `"http://localhost:5202"` | SVD reference server |
| `comfyui_base_url` | `str` | `"http://localhost:8188"` | ComfyUI server |
| `comfyui_checkpoint` | `str` | `"svd_xt_1_1.safetensors"` | Checkpoint name filled into the workflow |
| `comfyui_workflow_path` | `str \| None` | `None` | Custom workflow JSON template (default: bundled `workflows/default_svd.json`) |
| `comfyui_fps` | `int` | `6` | Frames-per-second placeholder |
| `comfyui_motion_bucket_id` | `int` | `127` | SVD motion bucket placeholder |
| `comfyui_poll_interval` | `float` | `1.0` | History poll interval in seconds |
| `timeout` | `float \| None` | `None` | Overall request timeout; `None` → each backend's own default |
| `processing` | `VideoProcessingConfig` | default factory | Nested ffmpeg pipeline config |

### `VideoProcessingConfig`

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `ffmpeg_binary` | `str` | `"ffmpeg"` | ffmpeg executable (`ffprobe` is derived from its name) |
| `max_concurrent_jobs` | `int` | `2` | Semaphore cap on concurrent ffmpeg jobs |
| `temp_dir` | `str \| None` | `None` | Workdir root for materialized inputs/outputs |
| `timeout` | `float` | `300.0` | Per-job ffmpeg timeout in seconds (kills the process) |

### Backend constructor mapping (`VideoGenerationProvider.register()`)

| `backend` | Class | Key construction args |
|-----------|-------|-----------------------|
| `"local-http"` | `LocalHttpVideoProvider` | `base_url=local_http_base_url` |
| `"runway"` | `RunwayVideoProvider` | `api_key` from secret `runway_api_key_secret_name` |
| `"openai"` | `OpenAIVideoProvider` | `api_key` from secret `openai_api_key_secret_name`, `model=openai_model`, `base_url=openai_base_url` |
| `"wan22"` | `Wan22VideoProvider` | `base_url=wan22_base_url` |
| `"cogvideox"` | `CogVideoXVideoProvider` | `base_url=cogvideox_base_url` |
| `"svd"` | `SVDVideoProvider` | `base_url=svd_base_url` |
| `"comfyui"` | `ComfyUiVideoProvider` | `base_url`, `checkpoint`, `workflow_path`, `fps`, `motion_bucket_id`, `poll_interval` |
| anything else | raises `ProviderNotInstalledError` | — |

`timeout` is forwarded only when set (`_TimeoutKwargs`); otherwise provider defaults apply: `local-http`/`runway`/`openai` `60.0`, `wan22`/`cogvideox` `180.0`, `svd` `120.0`, `comfyui` `120.0`. All constructors also receive optional `retry`/`circuit_breaker`.

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `ORI_MULTIMEDIA__VIDEO__BACKEND` | Backend selection |
| `ORI_MULTIMEDIA__VIDEO__LOCAL_HTTP_BASE_URL` | Local server URL |
| `ORI_MULTIMEDIA__VIDEO__RUNWAY_API_KEY_SECRET_NAME` | Secret name for Runway key |
| `ORI_MULTIMEDIA__VIDEO__OPENAI_API_KEY_SECRET_NAME` | Secret name for OpenAI key |
| `ORI_MULTIMEDIA__VIDEO__OPENAI_MODEL` | Default OpenAI gateway model |
| `ORI_MULTIMEDIA__VIDEO__OPENAI_BASE_URL` | OpenAI-compatible base URL |
| `ORI_MULTIMEDIA__VIDEO__WAN22_BASE_URL` | Wan2.2 server URL |
| `ORI_MULTIMEDIA__VIDEO__COGVIDEOX_BASE_URL` | CogVideoX server URL |
| `ORI_MULTIMEDIA__VIDEO__SVD_BASE_URL` | SVD server URL |
| `ORI_MULTIMEDIA__VIDEO__COMFYUI_BASE_URL` | ComfyUI URL |
| `ORI_MULTIMEDIA__VIDEO__COMFYUI_CHECKPOINT` | ComfyUI checkpoint |
| `ORI_MULTIMEDIA__VIDEO__COMFYUI_WORKFLOW_PATH` | Custom workflow JSON path |
| `ORI_MULTIMEDIA__VIDEO__COMFYUI_FPS` | Workflow fps |
| `ORI_MULTIMEDIA__VIDEO__COMFYUI_MOTION_BUCKET_ID` | Workflow motion bucket |
| `ORI_MULTIMEDIA__VIDEO__COMFYUI_POLL_INTERVAL` | Poll interval seconds |
| `ORI_MULTIMEDIA__VIDEO__TIMEOUT` | Request timeout |
| `ORI_MULTIMEDIA__VIDEO__PROCESSING__FFMPEG_BINARY` | ffmpeg binary |
| `ORI_MULTIMEDIA__VIDEO__PROCESSING__MAX_CONCURRENT_JOBS` | Concurrency cap |
| `ORI_MULTIMEDIA__VIDEO__PROCESSING__TEMP_DIR` | Workdir root |
| `ORI_MULTIMEDIA__VIDEO__PROCESSING__TIMEOUT` | Per-job ffmpeg timeout |

```bash
export ORI_PROFILE=production
export ORI_MULTIMEDIA__VIDEO__BACKEND=runway
export ORI_MULTIMEDIA__VIDEO__PROCESSING__MAX_CONCURRENT_JOBS=4
```

---

## Advanced Configuration

### Secrets for hosted backends

Keys are resolved by name at registration:

```python
# Secrets stored under name "runway_api_key" → RunwayVideoProvider(api_key=...)
# Secrets stored under name "openai_api_key" → OpenAIVideoProvider(api_key=...)
```

No key → `api_key=""` and `_credential_resolved=False`; the health check then reports `DEGRADED` for that provider. A `401` at call time raises `VideoGenerationAuthenticationError`.

### Testing with `stub()`

```python
module = VideoModule.stub()
# VideoConfig(backend="local-http"), real module — safe for boot smoke tests.
```

### Resolving health per backend

- HTTP backends check `GET /health` (ComfyUI uses `GET /system_stats`) — `200 → HEALTHY`, else `DEGRADED`.
- Runway/OpenAI: `HEALTHY` only when `_credential_resolved` (an API key was found).

### Entry-point discovery

The umbrella imports this subsystem via `oridecon.multimedia.subsystems` (`video`) and `oridecon.multimedia.modules` (`video`); the compound config there nests under `multimedia:` / `video:`.

---

## Best Practices

- ✅ Keep config minimal — backend + one base URL per deployment.
- ✅ Store API keys in the secrets backend; reference them by name — never commit keys.
- ✅ Give `processing.timeout` headroom over your longest encode.
- ✅ Isolate each reference server in its own venv (torch is heavy).
- ❌ Don't rely on `timeout: null` semantics — set it explicitly if your generation SDK is slow.
- ❌ Don't set `comfyui_workflow_path` to an unreadable/unreachable path — the provider reads it at request time.