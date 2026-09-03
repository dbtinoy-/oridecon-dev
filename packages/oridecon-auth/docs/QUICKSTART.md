---
title: oridecon-auth Quickstart
description: Install and configure authentication for your Oridecon application
---

:::note[What you'll learn]
- Install `oridecon-auth` with `uv`
- Wire the full auth stack with `AuthModule` or `AuthBundleProvider`
- Run a minimal authenticated application
:::

## Install

```bash
uv add oridecon-auth
```

:::tip
For OAuth2 support, add the optional dependency:

```bash
uv add oridecon-auth[oauth2]
```

For SAML: `uv add oridecon-auth[saml]`. For LDAP: `uv add oridecon-auth[ldap]`.
:::

## Minimal Setup — AuthModule

The quickest way to add authentication is through `AuthModule.configure()`:

```python
import asyncio
from oridecon import Application
from oridecon.auth import AuthModule
from oridecon.auth.config import AuthConfig, JWTConfig


async def main():
    config = AuthConfig(
        secret_key="your-256-bit-secret-here-must-be-long",
        token=JWTConfig(secret_key="your-256-bit-secret-here-must-be-long"),
    )

    async with Application.boot(
        name="my-app",
        modules=[AuthModule.configure(config=config)],
    ) as app:
        print(f"App running: {app.state}")


asyncio.run(main())
```

## Using AuthBundleProvider Directly

When you're wiring providers explicitly (Pattern 2), use `AuthBundleProvider`:

```python
from oridecon import Application
from oridecon.auth import AuthBundleProvider
from oridecon.auth.config import AuthConfig


def create_app() -> Application:
    app = Application(name="my-app")
    app.add_provider(AuthBundleProvider(
        config=AuthConfig(secret_key="your-secret-key"),
    ))
    return app
```

## Testing with AuthModule.stub()

For unit tests, use the in-memory stub to avoid external dependencies:

```python
from oridecon.auth import AuthModule

# Returns a DynamicModule backed by ephemeral in-memory storage
test_module = AuthModule.stub()
```

## Next Steps

- [Guide](./GUIDE.md) — authentication, authorization, and token management workflows
- [How-Tos](./HOWTOS.md) — JWT, RBAC, OAuth2 recipes
- [Configuration](./CONFIGURATION.md) — all configuration keys
