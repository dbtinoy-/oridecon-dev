from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol
    from oridecon.events.config import EventsConfig
    from oridecon.events.stores.base import AbstractEventStore


async def create_inmemory_store(
    config: EventsConfig,
    container: ContainerResolverProtocol | None,
) -> AbstractEventStore:
    """Create an in-memory event store."""
    from oridecon.events.stores.memory import InMemoryEventStore

    return InMemoryEventStore(
        max_events_per_stream=config.memory.max_events_per_stream,
    )


async def create_postgres_store(
    config: EventsConfig,
    container: ContainerResolverProtocol | None,
) -> AbstractEventStore:
    """Create a PostgreSQL event store using the injected DB provider."""
    from oridecon.contracts.data.sql.database import DatabaseProviderProtocol
    from oridecon.events.stores.postgres.event_store import PostgresEventStore

    if container is None:
        raise ValueError(
            "PostgreSQL backend requires a DI container to resolve the "
            "database provider"
        )
    provider = await container.resolve(DatabaseProviderProtocol)
    pg_config = config.postgres
    if pg_config is None:
        raise ValueError("PostgreSQL backend selected but postgres config is missing")
    return PostgresEventStore(config=pg_config, provider=provider)


async def create_mongodb_store(
    config: EventsConfig,
    container: ContainerResolverProtocol | None,
) -> AbstractEventStore:
    """Create a MongoDB event store."""
    from oridecon.contracts.data import DocumentStoreProtocol
    from oridecon.events.stores.mongodb.event_store import MongoDBEventStore

    mongo_config = config.mongodb
    if mongo_config is None:
        raise ValueError("MongoDB backend selected but mongodb config is missing")
    if container is None:
        raise ValueError(
            "MongoDB backend requires a DI container to resolve the document store"
        )
    document_store = await container.resolve(DocumentStoreProtocol)
    return MongoDBEventStore(  # type: ignore[abstract]
        document_store=document_store,
        config=mongo_config,
    )


async def create_sqlite_store(
    config: EventsConfig,
    container: ContainerResolverProtocol | None,
) -> AbstractEventStore:
    """Create a SQLite event store.

    Note: SQLite support is not yet fully integrated into EventsConfig.
    Raises NotImplementedError until sqlite config field is added.
    """
    raise NotImplementedError(
        "SQLite backend support is not yet fully integrated. "
        "Awaiting sqlite config field in EventsConfig."
    )
