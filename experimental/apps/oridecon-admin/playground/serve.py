"""Live dev playground for the oridecon-admin panel.

Boots the REAL admin lifecycle — ``Container`` → ``DatabaseProvider``
(SQLite) → ``create_app()`` → uvicorn — with two demo resources backed by
in-memory stores, while every auth/session/audit store runs on real SQL.
Default security settings are kept ON so the first-run path behaves exactly
like a fresh production install.

Usage (from the repository root)::

    rm -f experimental/apps/oridecon-admin/playground/playground.db*  # fresh start
    uv run python experimental/apps/oridecon-admin/playground/serve.py

Then open http://localhost:8000/admin/ — the setup wizard appears on a
fresh database. Setup token: ``dev-setup-token``. The bare host root
serves a landing page that forwards to ``/admin/``.

When running inside an E2B/Arena preview sandbox (``E2B_SANDBOX`` set)
the panel must be embeddable, so the ``frame_options`` setting is cleared
and ``frame-ancestors`` is relaxed to the E2B preview origins. Outside a
preview sandbox the production-identical security defaults are kept.
Override with ``ORIDECON_PLAYGROUND_ALLOW_EMBED=0|1``.

Verification workflow: docs/09-01-2026/04-verification-playbook.md.
A clean boot must print ZERO tracebacks (roadmap R8).
"""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from oridecon.admin.actions.standard.header import CreateAction
from oridecon.admin.actions.standard.imports import ImportAction
from oridecon.admin.actions.standard.row import DeleteAction, EditAction
from oridecon.admin.config import AdminConfig
from oridecon.admin.data.data_source import QueryResult
from oridecon.admin.resources import Resource
from oridecon.di.container import Container
from oridecon.sql.di.provider import DatabaseProvider
from oridecon.ui.columns.types import TextColumn

HERE = Path(__file__).parent
DB_PATH = HERE / "playground.db"
SETUP_TOKEN = "dev-setup-token"  # noqa: S105 — local dev playground only
PORT = 8000


# ── In-memory demo store ────────────────────────────────────────────────────


class MemoryStore:
    """IDataSource-compatible in-memory store."""

    def __init__(self, seed: list[dict[str, Any]] | None = None) -> None:
        self._records: dict[int, dict[str, Any]] = {}
        self._next_id = 1
        for rec in seed or []:
            rid = int(rec["id"])
            self._records[rid] = dict(rec)
            self._next_id = max(self._next_id, rid + 1)

    def _items(self, query: Any) -> list[dict[str, Any]]:
        items = list(self._records.values())
        search = getattr(query, "search", None)
        fields = getattr(query, "search_fields", None)
        if search and fields:
            term = search.lower()
            items = [
                i
                for i in items
                if any(term in str(i.get(f, "")).lower() for f in fields)
            ]
        sort_by = getattr(query, "sort_by", None) or "id"
        reverse = (getattr(query, "sort_order", None) or "asc") == "desc"
        items.sort(key=lambda i: (i.get(sort_by) is None, str(i.get(sort_by))))
        if reverse:
            items.reverse()
        return items

    async def find_many(self, query: Any) -> QueryResult:
        items = self._items(query)
        total = len(items)
        page = getattr(query, "page", 1) or 1
        per_page = getattr(query, "per_page", 20) or 20
        start = (page - 1) * per_page
        paged = items[start : start + per_page]
        return QueryResult(
            items=paged,
            total=total,
            page=page,
            per_page=per_page,
            has_next=start + per_page < total,
            has_prev=page > 1,
        )

    async def find_one(self, item_id: Any) -> dict[str, Any] | None:
        try:
            return self._records.get(int(item_id))
        except (TypeError, ValueError):
            return None

    async def count(self, query: Any) -> int:
        return len(self._items(query))

    async def create(self, data: dict[str, Any]) -> dict[str, Any]:
        rid = self._next_id
        self._next_id += 1
        rec = {**data, "id": rid}
        self._records[rid] = rec
        return rec

    async def update(
        self, item_id: Any, data: dict[str, Any]
    ) -> dict[str, Any] | None:
        rec = self._records.get(int(item_id))
        if rec is None:
            return None
        rec.update(data)
        return rec

    async def delete(self, item_id: Any) -> bool:
        return self._records.pop(int(item_id), None) is not None

    async def bulk_create(self, items: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [await self.create(d) for d in items]

    async def bulk_update(self, ids: list[Any], data: dict[str, Any]) -> int:
        return sum(1 for i in ids if (await self.update(i, data)) is not None)

    async def bulk_delete(self, ids: list[Any]) -> int:
        return sum(1 for i in ids if await self.delete(i))


class ProductStore(MemoryStore):
    pass


class CustomerStore(MemoryStore):
    pass


# ── Demo resources ──────────────────────────────────────────────────────────


class ProductModel(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    sku: str = Field(min_length=1, max_length=40)
    price: float = Field(ge=0)


class ProductResource(Resource):
    name = "products"
    label = "Products"
    icon = "package"
    model = ProductModel
    _data_source_class = ProductStore

    columns = [
        TextColumn("name").sortable(),
        TextColumn("sku").sortable(),
        TextColumn("price").sortable(),
    ]
    search_fields = ["name", "sku"]
    page_size = 10
    default_sort = "name"
    actions = [EditAction(), DeleteAction()]
    header_actions = [
        CreateAction(),
        ImportAction(example_columns=["name", "sku", "price"]),
    ]
    permissions = None


class CustomerModel(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: str = Field(min_length=3, max_length=254)


class CustomerResource(Resource):
    name = "customers"
    label = "Customers"
    icon = "users"
    model = CustomerModel
    _data_source_class = CustomerStore

    columns = [TextColumn("name").sortable(), TextColumn("email").sortable()]
    search_fields = ["name", "email"]
    page_size = 10
    default_sort = "name"
    actions = [EditAction(), DeleteAction()]
    header_actions = [CreateAction()]
    permissions = None


def _seed_products() -> list[dict[str, Any]]:
    return [
        {"id": i, "name": f"Product {i:02d}", "sku": f"SKU-{i:04d}", "price": 9.5 + i}
        for i in range(1, 21)
    ]


def _seed_customers() -> list[dict[str, Any]]:
    return [
        {"id": i, "name": f"Customer {i:02d}", "email": f"customer{i:02d}@example.dev"}
        for i in range(1, 11)
    ]


# ── Boot ────────────────────────────────────────────────────────────────────


async def build_app():
    """Container → DatabaseProvider → create_app, the real lifecycle."""
    from oridecon.admin.bootstrap import create_app

    container = Container()
    db = DatabaseProvider(config=f"sqlite+aiosqlite:///{DB_PATH}")
    await db.register(container)
    await db.boot(container)

    container.singleton(ProductStore, ProductStore(_seed_products()))
    container.singleton(CustomerStore, CustomerStore(_seed_customers()))

    auth_config: dict[str, Any] = {
        "session_secret": "playground-session-secret-not-for-prod",
        "security": {"setup_token": SETUP_TOKEN},
        # Email verification enforcement stays at its default (ON)
        # and no mailer is configured — the fresh-install path.
    }
    if _preview_embed_enabled():
        # The Arena/E2B preview can embed the panel as a third-party
        # iframe; SameSite=lax cookies are then dropped by the browser
        # and every CSRF-protected POST fails. SameSite=None (+Secure,
        # implied by the builder) keeps the session/CSRF flow working.
        auth_config["cookie_same_site"] = "none"
        auth_config["cookie_secure"] = True

    config = AdminConfig.from_dict(
        {
            "prefix": "/admin",
            "title": "Oridecon Admin Playground",
            # Debug on: exercises the R11 console-mailer fallback so
            # verification/reset emails land in the server log.
            "debug": True,
            "auth": auth_config,
        }
    )

    return await create_app(
        resources=[ProductResource, CustomerResource],
        config=config,
        container=container,
    )


def _attach_root_landing(app: Any) -> None:
    """Serve a minimal landing at the bare host root (sandbox preview /
    localhost:8000) instead of Starlette's 404.

    The admin panel is mounted at ``/admin``; the landing forwards there
    immediately (meta refresh + link, no JS required) and shows the
    playground credentials so a fresh preview needs no doc-lookup.
    """

    landing = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="0; url=/admin/">
  <title>Oridecon Admin Playground</title>
  <style>
    body {{ font-family: ui-sans-serif, system-ui, sans-serif; background: #0b1220; color: #e2e8f0;
           display: grid; place-items: center; min-height: 100vh; margin: 0; }}
    main {{ max-width: 34rem; padding: 2rem; }}
    a {{ color: #7dd3fc; }}
    code {{ background: #1e293b; padding: .15rem .4rem; border-radius: .25rem; }}
  </style>
</head>
<body>
  <main>
    <h1>Oridecon Admin Playground</h1>
    <p>Opening the admin panel… <a href="/admin/">open now</a>.</p>
    <p>Sign in: <code>dev@example.dev</code> / <code>DevAdmin#123</code></p>
  </main>
</body>
</html>"""

    async def _root(request: Any) -> Any:
        from starlette.responses import HTMLResponse

        return HTMLResponse(landing)

    app.add_route("/", _root, methods=["GET"])


def _preview_embed_enabled() -> bool:
    """True when this playground should relax security for the live preview.

    The Arena/E2B preview embeds the app on a ``*.arena.site`` /
    ``*.e2b.app`` origin, which requires iframe-friendly framing headers
    and a cross-site session cookie. Base the decision on the sandbox
    environment; operators can override with
    ``ORIDECON_PLAYGROUND_ALLOW_EMBED=0|1``.
    """
    env_value = os.environ.get("ORIDECON_PLAYGROUND_ALLOW_EMBED")
    if env_value is None:
        return bool(os.environ.get("E2B_SANDBOX") or os.environ.get("E2B_SANDBOX_ID"))
    return env_value.strip().lower() not in {"0", "false", "off", "no", ""}


def main() -> None:
    import uvicorn

    app = asyncio.run(build_app())
    _attach_root_landing(app)
    asyncio.run(_allow_preview_embedding())
    print(f"\n▶ Admin playground: http://localhost:{PORT}/admin/")
    print(f"▶ Setup token: {SETUP_TOKEN}\n")
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="info")  # noqa: S104 — dev playground binds all interfaces for sandbox preview


async def _allow_preview_embedding() -> None:
    """Relax framing for the Arena/E2B live preview (playground only).

    The admin security middleware ships ``X-Frame-Options: DENY`` and
    ``frame-ancestors 'none'``, which is correct for production but makes
    the embedded preview block the iframe. When this process runs inside
    a preview sandbox, write the two inherited settings the middleware
    reads:

    * ``admin.security.frame_options`` → ``""``  (no X-Frame-Options)
    * ``admin.security.csp`` → DEFAULT_CSP with ``frame-ancestors *``
      (the preview parent may be ``*.arena.site``, ``*.e2b.app`` or a
      related host; the playground is the only surface that runs this)

    Values are JSON-encoded exactly like ``oridecon.serialization`` stores
    them. The report-only STRICT_CSP candidate is left untouched (it never
    blocks framing and keeps the console diagnostics).
    """

    if not _preview_embed_enabled():
        print("▶ preview embedding: NOT relaxed (secure defaults kept)")
        return

    from oridecon.admin.settings.panel.models import DEFAULT_CSP

    relaxed_csp = DEFAULT_CSP.replace(
        "frame-ancestors 'none';",
        "frame-ancestors *;",
    )
    rows = [
        ("admin_ui.admin.security.frame_options", json.dumps("")),
        ("admin_ui.admin.security.csp", json.dumps(relaxed_csp)),
    ]
    import aiosqlite

    async with aiosqlite.connect(DB_PATH) as db:
        for key, value in rows:
            await db.execute(
                "INSERT INTO tenant_configs (tenant_id, key, value)"
                " VALUES ('default', ?, ?)"
                " ON CONFLICT (tenant_id, key) DO UPDATE SET"
                " value = excluded.value, updated_at = CURRENT_TIMESTAMP",
                (key, value),
            )
        await db.commit()
    print("▶ preview embedding: relaxed (frame_options cleared, frame-ancestors *, SameSite=None cookie)")


if __name__ == "__main__":
    main()
