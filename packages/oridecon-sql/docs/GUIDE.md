---
title: oridecon-sql Guide
description: Mental model, core concepts, and end-to-end workflows for async SQL database access.
---

## Requirements

| Package | Required | Purpose |
|---------|----------|---------|
| `oridecon` | Yes | Core framework |
| `oridecon-contracts` | Yes | Protocol definitions |
| `asyncpg` | Recommended | PostgreSQL async driver |
| `aiosqlite` | Recommended | SQLite async driver |
| `oridecon-cache` | Optional | Query caching |

## Overview

`oridecon-sql` provides async SQL database access for **Postgres**, **MySQL**, and **SQLite** — built on SQLAlchemy 2.0 with repositories, migrations, query building, and unit-of-work.

**What it solves:** Wrangling async database connections, pooling, migrations, and repository boilerplate is repetitive. `oridecon-sql` gives you declarative repositories, DI-managed lifecycle, multi-backend support, and a clean query builder — all behind `DatabaseProviderProtocol` from contracts.

**The mental model:** A `DatabaseProvider` manages the connection pool. You interact through `GenericRepository[T, TKey]` for CRUD, `AsyncQueryBuilder` for custom queries, and `SimpleUnitOfWork` for transactions. Everything is registered in the DI container and injectable as `DatabaseProviderProtocol`.

---

## Core Concepts

### DatabaseProvider

The `DatabaseProvider` is the entry point — it registers the connection pool, query logger, migration manager, and unit-of-work factory in the container.

```python
from oridecon import Application
from oridecon.sql import DatabaseProvider

app = Application(name="my-app")
app.add_provider(DatabaseProvider(config=DatabaseConfig.from_url("...")))
```

It runs at `INFRASTRUCTURE` priority (10) — booting before domain services.

### DatabaseModule

The module wrapper provides `configure()` and `stub()`:

```python
from oridecon.sql import DatabaseModule

app.add_module(DatabaseModule.configure("postgresql+asyncpg://localhost/mydb"))
```

### DatabaseConfig

Configuration is loaded from the `sql` section of `application.yaml` or passed explicitly:

```python
from oridecon.sql.config import DatabaseConfig, DatabaseBackendConfig

config = DatabaseConfig(
    backend=DatabaseBackendConfig(url="postgresql+asyncpg://user:pass@localhost/db"),
)
```

### GenericRepository

The primary CRUD abstraction — typed by entity class and key type:

```python
from oridecon.sql import GenericRepository

repo = GenericRepository[User, int](
    provider=db_provider,
    table_name="users",
    entity_class=User,
    key_field="id",
)
```

Methods: `find`, `find_one`, `create`, `update`, `delete`, `count`, `exists`.

### AsyncQueryBuilder

Build SQL queries programmatically:

```python
from oridecon.sql.query import AsyncQueryBuilder, Operator

query = (
    AsyncQueryBuilder("users")
    .where("age", Operator.GTE, 18)
    .order_by("name", ascending=True)
    .limit(20)
    .offset(0)
)
results = await query.fetch(db_provider)
```

### Unit of Work

Coordinate multiple repository operations in a single transaction:

```python
from oridecon.sql import SimpleUnitOfWork


class UserService:
    def __init__(self, uow: SimpleUnitOfWork) -> None:
        self.uow = uow

    async def create_user(self, data: dict) -> Result[User, Error]:
        async with self.uow:
            user = await self.uow.users.create(data)
            await self.uow.audit_log.create({"action": "user_created", "user_id": user.id})
            await self.uow.commit()
            return Ok(user)
```

### Multi-Backend Support

Configure multiple named databases:

```yaml
sql:
  backends:
    - name: primary
      backend:
        url: postgresql+asyncpg:///primary
      primary: true
    - name: analytics
      backend:
        url: postgresql+asyncpg:///analytics
      migration_dir: migrations/analytics
```

Resolve by name: `Annotated[DatabaseProviderProtocol, Named("analytics")]`.

---

## Typical Usage

### Application Factory

```python
from oridecon import Application
from oridecon.sql import DatabaseModule


def create_app() -> Application:
    app = Application(name="my-app")
    app.add_module(DatabaseModule.configure(
        "postgresql+asyncpg://localhost/mydb",
        enable_migrations=True,
    ))
    return app
```

### Repository Service

```python
from oridecon.di import singleton
from oridecon.result import Result, Ok, Err
from oridecon.contracts.data import DatabaseProviderProtocol
from oridecon.sql import GenericRepository
from oridecon.sql.exceptions import DatabaseError, RepositoryError


@singleton
class UserRepository:
    def __init__(self, db: DatabaseProviderProtocol) -> None:
        self.repo = GenericRepository[User, int](
            provider=db,
            table_name="users",
            entity_class=User,
            key_field="id",
        )

    async def find_by_email(self, email: str) -> Result[User, RepositoryError]:
        try:
            user = await self.repo.find_one(email=email)
            if user is None:
                return Err(RepositoryError("User not found"))
            return Ok(user)
        except DatabaseError as e:
            return Err(RepositoryError(str(e)))
```

### Migration Management

```bash
# Use the CLI
uv run oridecon db upgrade

# Or the AlembicManager API
from oridecon.sql.migrations.api import AlembicManager

manager = AlembicManager("postgresql+asyncpg://localhost/mydb", "migrations")
await manager.upgrade()
```

---

## Common Patterns

### Filtering with F expressions

```python
from oridecon.sql import F, Filter

active_users = await repo.find(
    filters=[
        Filter("status", "==", "active"),
        Filter("age", ">=", 18),
    ],
    order_by=[F("created_at").desc()],
    limit=50,
)
```

### Type-Safe Identifiers

```python
from oridecon.sql import table, column, Table, Column

users = Table("users")
query = users.select().where(Column("email") == "test@example.com")
```

### Using DatabaseModule.stub() in Tests

```python
from oridecon import Application
from oridecon.sql import DatabaseModule


async def test_repository():
    async with Application.boot(
        name="test",
        modules=[DatabaseModule.stub()],
    ) as app:
        db = await app.container.resolve(DatabaseProviderProtocol)
        repo = GenericRepository[User, int](
            provider=db,
            table_name="users",
            entity_class=User,
            key_field="id",
        )
        result = await repo.create({"name": "Test", "email": "test@test.com"})
        assert result.is_ok()
```

### Row-Level Security

```python
from oridecon.sql import RowLevelSecurityPolicy, ScopeColumn

policy = RowLevelSecurityPolicy(columns=[ScopeColumn("tenant_id")])
repo = GenericRepository[User, int](
    provider=db,
    table_name="users",
    entity_class=User,
    key_field="id",
    rls_policy=policy,
)
```

---

## Best Practices

- ✅ Use `DatabaseModule.configure()` for module-based registration
- ✅ Use `DatabaseModule.stub()` in unit tests for in-memory operation
- ✅ Return `Result[T, RepositoryError]` from repository methods
- ✅ Use `SimpleUnitOfWork` for multi-repository transactions
- ✅ Use `DatabaseProviderProtocol` from contracts — never import `oridecon-sql` directly from other extensions
- ✅ Pin versions in production
- ❌ Don't create connection pools manually — always use `DatabaseProvider`
- ❌ Don't embed raw SQL strings — use `AsyncQueryBuilder` or `GenericRepository`
- ❌ Don't call `provider.boot()` manually — let the `Application` lifecycle handle it
- ❌ Don't add `oridecon-sql` as a dependency of another extension — use the contracts protocol

---

## Next Steps

- [Architecture](./ARCHITECTURE.md) — internal design, provider lifecycle, contracts
- [Configuration](./CONFIGURATION.md) — every config key
- [How-Tos](./HOWTOS.md) — task-oriented recipes
- [Troubleshooting](./TROUBLESHOOTING.md) — common errors and fixes
