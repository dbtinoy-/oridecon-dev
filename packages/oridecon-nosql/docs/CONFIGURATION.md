---
title: oridecon-nosql Configuration
description: Every configuration key, its type, default, and environment variable.
---

Config section: `nosql:`  
Env prefix: `ORI_NOSQL__`

## NoSQLConfig (Top Level)

| Key | Type | Default | Env Variable | Description |
|-----|------|---------|-------------|-------------|
| `enabled` | `bool` | `true` | `ORI_NOSQL__ENABLED` | Enable NoSQL subsystem |
| `driver` | `str` | `"mongodb"` | `ORI_NOSQL__DRIVER` | NoSQL driver name (`mongodb`, `firestore`) |
| `mongodb` | `MongoDBConfig` | defaults | `ORI_NOSQL__MONGODB__*` | MongoDB connection settings |
| `firestore` | `FirestoreConfig \| None` | `null` | `ORI_NOSQL__FIRESTORE__*` | Firestore settings (used when `driver="firestore"`) |
| `backends` | `list[NamedNoSQLConfig]` | `[]` | `ORI_NOSQL__BACKENDS__*` | Named multi-backend entries |

## MongoDBConfig

| Key | Type | Default | Env Variable | Description |
|-----|------|---------|-------------|-------------|
| `uri` | `str` | `"mongodb://localhost:27017"` | `ORI_NOSQL__MONGODB__URI` | Connection URI |
| `database` | `str` | `"oridecon"` | `ORI_NOSQL__MONGODB__DATABASE` | Database name |
| `max_pool_size` | `int` | `100` | `ORI_NOSQL__MONGODB__MAX_POOL_SIZE` | Max connection pool size |
| `min_pool_size` | `int` | `10` | `ORI_NOSQL__MONGODB__MIN_POOL_SIZE` | Min connection pool size |
| `server_selection_timeout_ms` | `int` | `5000` | `ORI_NOSQL__MONGODB__SERVER_SELECTION_TIMEOUT_MS` | Server selection timeout (ms) |
| `connect_timeout_ms` | `int` | `10000` | `ORI_NOSQL__MONGODB__CONNECT_TIMEOUT_MS` | Connection timeout (ms) |
| `socket_timeout_ms` | `int` | `30000` | `ORI_NOSQL__MONGODB__SOCKET_TIMEOUT_MS` | Socket timeout (ms) |
| `retry_writes` | `bool` | `true` | `ORI_NOSQL__MONGODB__RETRY_WRITES` | Enable write retries |
| `retry_reads` | `bool` | `true` | `ORI_NOSQL__MONGODB__RETRY_READS` | Enable read retries |
| `read_preference` | `str` | `"primaryPreferred"` | `ORI_NOSQL__MONGODB__READ_PREFERENCE` | Read preference mode |
| `write_concern_w` | `str \| int` | `"majority"` | `ORI_NOSQL__MONGODB__WRITE_CONCERN_W` | Write concern level |
| `auth_source` | `str` | `"admin"` | `ORI_NOSQL__MONGODB__AUTH_SOURCE` | Authentication database |

## FirestoreConfig

| Key | Type | Default | Env Variable | Description |
|-----|------|---------|-------------|-------------|
| `project_id` | `str` | *(required)* | `ORI_NOSQL__FIRESTORE__PROJECT_ID` | Google Cloud project ID |
| `credentials_json` | `str \| None` | `null` | `ORI_NOSQL__FIRESTORE__CREDENTIALS_JSON` | Service account JSON key (path or raw) |
| `database_id` | `str` | `"(default)"` | `ORI_NOSQL__FIRESTORE__DATABASE_ID` | Firestore database ID |

## DynamoDBConfig

| Key | Type | Default | Env Variable | Description |
|-----|------|---------|-------------|-------------|
| `table_name` | `str` | `"oridecon"` | — | Default table name |
| `region` | `str` | `"us-east-1"` | — | AWS region |
| `access_key` | `str \| None` | `null` | — | AWS access key ID |
| `secret_key` | `str \| None` | `null` | — | AWS secret access key |
| `endpoint_url` | `str \| None` | `null` | — | Custom endpoint (e.g., `http://localhost:8000`) |
| `pk_field` | `str` | `"_id"` | — | Partition key attribute name |

`DynamoDBConfig` has no environment variable overrides — `NoSQLConfig` wires only Mongo and Firestore backends. Configure DynamoDB programmatically via `DynamoDBConfig(...)`.

Named backends follow the same env pattern with an index: `ORI_NOSQL__BACKENDS__0__NAME`, `ORI_NOSQL__BACKENDS__0__DRIVER`, etc.

---

## Minimal YAML Example

```yaml
nosql:
  driver: mongodb
  mongodb:
    uri: mongodb://localhost:27017
    database: myapp
```

## Production YAML Example

```yaml
nosql:
  driver: mongodb
  mongodb:
    uri: mongodb://admin:${MONGODB_PASSWORD}@cluster0.example.mongodb.net
    database: myapp
    max_pool_size: 50
    retry_writes: true
    write_concern_w: majority
```

## Multi-Backend Example

```yaml
nosql:
  backends:
    - name: primary
      driver: mongodb
      primary: true
      mongodb:
        uri: mongodb://primary:27017
        database: app
    - name: analytics
      driver: mongodb
      mongodb:
        uri: mongodb://analytics:27017
        database: analytics
```

## Environment Variable Override

```bash
export ORI_NOSQL__MONGODB__URI="mongodb://prod-cluster:27017"
export ORI_NOSQL__MONGODB__DATABASE="production_db"
export ORI_NOSQL__DRIVER="mongodb"
```
