# Quickstart

Generating images with `oridecon-multimedia-image` in minutes — zero API keys required.

---

## Install

```bash
uv add oridecon-multimedia-image
```

The default backend (`local-http`) needs nothing else. Only pick an extra when you switch backends:

```bash
uv add "oridecon-multimedia-image[stability]"   # Stability AI
uv add "oridecon-multimedia-image[openai]"      # OpenAI images API
```

`oridecon-multimedia-image` depends on `oridecon` and `oridecon-contracts` (installed automatically).

---

## Minimal Working Example

```python
import asyncio

from oridecon import Application
from oridecon.contracts.multimedia import ImageProvider, ImageRequest
from oridecon.multimedia.image import ImageModule


async def main() -> None:
    async with Application.boot(modules=[ImageModule.configure()]) as app:
        image: ImageProvider = await app.container.resolve(ImageProvider)

        result = await image.generate(
            ImageRequest(prompt="a cozy cabin in the snow", width=1024, height=1024)
        )

        if result.is_ok():
            asset = result.unwrap()  # MediaAsset(mime_type, provider, bytes_data, ...)
            with open("cabin.png", "wb") as f:
                f.write(asset.bytes_data)
        else:
            print(f"generation failed: {result.unwrap_err()}")


if __name__ == "__main__":
    asyncio.run(main())
```

Point `ImageModule.configure()` at a server implementing `POST /generate`
(`{"prompt", "width", "height", "format"}` → image bytes) at
`http://localhost:5005`, and this runs as-is.

---

## What Just Happened

1. `ImageModule.configure()` created a `DynamicModule` wrapping an
   `ImageGenerationProvider` and exporting `ImageProvider` and
   `ImageGenerationTask`.
2. During `Application.boot()` the provider's `register()` ran:
   - `ImageConfig` was bound in the container as a singleton.
   - The `backend` field (`"local-http"` by default) selected
     `LocalHttpImageProvider`, which was registered as the `ImageProvider`.
   - `ImageGenerationTask` was wired around the same backend for the
     `oridecon-tasks` `submit()` path.
3. Your code resolved `ImageProvider` from the container and called
   `generate(ImageRequest(...))` — the provider returned
   `Result[MediaAsset, ImageGenerationError]`, so the failure case was a
   handled `Err`, never a silent crash.

---

## Next Steps

- [Guide](./GUIDE.md) — backends, concepts, patterns
- [How-Tos](./HOWTOS.md) — task-oriented recipes
- [Configuration](./CONFIGURATION.md) — all config keys and env-var overrides