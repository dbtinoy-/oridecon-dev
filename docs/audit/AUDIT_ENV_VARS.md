# AUDIT_ENV_VARS.md — Oridecon Framework Environment Variables

> **Source**: Extracted from `config.py` root settings classes and known non-config env reads.

---

## Summary

- Packages scanned: 1
- Documented env var entries: 2255
- Unique env var names: 1806
- Duplicate env var names: 207
- Intentional non-config env sources: 3

## Duplicate Analysis

| Env Var | Occurrences |
|---------|-------------|
| `ORI_ADMIN__BACKEND` | 2 |
| `ORI_ADMIN__BACKENDS` | 6 |
| `ORI_ADMIN__CACHE_TTL` | 2 |
| `ORI_ADMIN__COLLECTION_NAME` | 2 |
| `ORI_ADMIN__DEBUG` | 5 |
| `ORI_ADMIN__EMBEDDING_MODEL` | 2 |
| `ORI_ADMIN__ENABLED` | 19 |
| `ORI_ADMIN__ENABLE_SSE` | 2 |
| `ORI_ADMIN__ENV` | 6 |
| `ORI_ADMIN__ENVIRONMENT` | 2 |
| `ORI_ADMIN__MAX_RETRIES` | 2 |
| `ORI_ADMIN__METRICS__ENABLED` | 2 |
| `ORI_ADMIN__METRICS__HISTOGRAM_BUCKETS` | 2 |
| `ORI_ADMIN__MONGODB__MAX_POOL_SIZE` | 2 |
| `ORI_ADMIN__NAME` | 10 |
| `ORI_ADMIN__PATH` | 2 |
| `ORI_ADMIN__RATE_LIMIT__ENABLED` | 2 |
| `ORI_ADMIN__RETRY` | 2 |
| `ORI_ADMIN__RETRY_DELAY` | 2 |
| `ORI_ADMIN__TENANCY__ENABLED` | 4 |
| `ORI_ADMIN__TRACING__ENABLED` | 2 |
| `ORI_ADMIN__TRACING__SAMPLE_RATE` | 2 |
| `ORI_ADMIN__TRACING__SERVICE_NAME` | 2 |
| `ORI_AUTH__ADMIN_EMAIL` | 3 |
| `ORI_AUTH__ADMIN_PASSWORD` | 3 |
| `ORI_AUTH__ENABLED` | 3 |
| `ORI_AUTH__LOGIN_RATE_LIMIT` | 3 |
| `ORI_AUTH__MAX_SESSIONS_PER_USER` | 3 |
| `ORI_AUTH__MIDDLEWARE__BACKEND` | 3 |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PATHS` | 3 |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PREFIXES` | 3 |
| `ORI_AUTH__MIDDLEWARE__HEADER_NAME` | 3 |
| `ORI_AUTH__MIDDLEWARE__LOGIN_RATE_LIMIT` | 3 |
| `ORI_AUTH__MIDDLEWARE__LOGIN_URL` | 3 |
| `ORI_AUTH__MIDDLEWARE__OPTIONAL_AUTH` | 3 |
| `ORI_AUTH__MIDDLEWARE__PERMISSIONS_REQUIRED` | 3 |
| `ORI_AUTH__MIDDLEWARE__ROLES_REQUIRED` | 3 |
| `ORI_AUTH__MIDDLEWARE__SCHEME` | 3 |
| `ORI_AUTH__NAME` | 3 |
| `ORI_AUTH__OAUTH2_PROVIDERS` | 3 |
| `ORI_AUTH__PASSWORD__ARGON2_MEMORY_COST` | 3 |
| `ORI_AUTH__PASSWORD__ARGON2_PARALLELISM` | 3 |
| `ORI_AUTH__PASSWORD__ARGON2_TIME_COST` | 3 |
| `ORI_AUTH__PASSWORD__BANNED_PATTERNS` | 3 |
| `ORI_AUTH__PASSWORD__BCRYPT_ROUNDS` | 3 |
| `ORI_AUTH__PASSWORD__MAX_LENGTH` | 3 |
| `ORI_AUTH__PASSWORD__MIN_LENGTH` | 3 |
| `ORI_AUTH__PASSWORD__REQUIRE_DIGITS` | 3 |
| `ORI_AUTH__PASSWORD__REQUIRE_LOWERCASE` | 3 |
| `ORI_AUTH__PASSWORD__REQUIRE_SPECIAL` | 3 |
| `ORI_AUTH__PASSWORD__REQUIRE_UPPERCASE` | 3 |
| `ORI_AUTH__RBAC__CACHE_PERMISSIONS` | 3 |
| `ORI_AUTH__RBAC__DEFAULT_ROLE` | 3 |
| `ORI_AUTH__RBAC__ENABLED` | 3 |
| `ORI_AUTH__RBAC__PERMISSION_CACHE_TTL` | 3 |
| `ORI_AUTH__RBAC__SUPERUSER_BYPASS` | 3 |
| `ORI_AUTH__RELAY_VERIFICATION` | 3 |
| `ORI_AUTH__ROLES` | 3 |
| `ORI_AUTH__SECRET_KEY` | 3 |
| `ORI_AUTH__TOKEN__ACCESS_TOKEN_EXPIRE` | 3 |
| `ORI_AUTH__TOKEN__ALGORITHM` | 3 |
| `ORI_AUTH__TOKEN__ALLOW_UNVERIFIED_DEV` | 2 |
| `ORI_AUTH__TOKEN__ID_TOKEN_EXPIRE` | 3 |
| `ORI_AUTH__TOKEN__KEY_ROTATION_GRACE_PERIOD` | 3 |
| `ORI_AUTH__TOKEN__REFRESH_TOKEN_EXPIRE` | 3 |
| `ORI_AUTH__TOKEN__REQUIRED_AUDIENCE` | 3 |
| `ORI_AUTH__TOKEN__SECRET_KEY` | 3 |
| `ORI_AUTH__USERS` | 3 |
| `ORI_CLI__BACKEND` | 2 |
| `ORI_CLI__BACKENDS` | 6 |
| `ORI_CLI__CACHE_TTL` | 2 |
| `ORI_CLI__COLLECTION_NAME` | 2 |
| `ORI_CLI__DEBUG` | 4 |
| `ORI_CLI__EMBEDDING_MODEL` | 2 |
| `ORI_CLI__ENABLED` | 16 |
| `ORI_CLI__ENV` | 6 |
| `ORI_CLI__ENVIRONMENT` | 2 |
| `ORI_CLI__MAX_RETRIES` | 2 |
| `ORI_CLI__METRICS__ENABLED` | 2 |
| `ORI_CLI__METRICS__HISTOGRAM_BUCKETS` | 2 |
| `ORI_CLI__MONGODB__MAX_POOL_SIZE` | 2 |
| `ORI_CLI__NAME` | 8 |
| `ORI_CLI__PATH` | 2 |
| `ORI_CLI__RETRY` | 2 |
| `ORI_CLI__RETRY_DELAY` | 2 |
| `ORI_CLI__TENANCY__ENABLED` | 3 |
| `ORI_CLI__TRACING__ENABLED` | 2 |
| `ORI_CLI__TRACING__SAMPLE_RATE` | 2 |
| `ORI_CLI__TRACING__SERVICE_NAME` | 2 |
| `ORI_FEATURES__CACHE_TTL` | 3 |
| `ORI_FEATURES__DEFAULT_ENABLED` | 3 |
| `ORI_FEATURES__ENABLED` | 3 |
| `ORI_FEATURES__FLAG_ENV_PREFIX` | 3 |
| `ORI_FEATURES__INITIAL_FLAGS` | 3 |
| `ORI_NOTIFICATION__INBOX__MARK_READ_ON_FETCH` | 3 |
| `ORI_NOTIFICATION__INBOX__MAX_PAGE_SIZE` | 3 |
| `ORI_NOTIFICATION__INBOX__RETENTION_DAYS` | 3 |
| `ORI_NOTIFICATION__INBOX__STORE_BACKEND` | 3 |
| `ORI_NOTIFICATION__MAILER__BACKENDS` | 3 |
| `ORI_NOTIFICATION__MAILER__CONSOLE_FALLBACK` | 3 |
| `ORI_RESILIENCE__IDEMPOTENCY__AUTO_CLEANUP` | 3 |
| `ORI_RESILIENCE__IDEMPOTENCY__CLEANUP_INTERVAL` | 3 |
| `ORI_RESILIENCE__IDEMPOTENCY__KEY_PREFIX` | 3 |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_ENTRIES` | 3 |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_KEY_LENGTH` | 3 |
| `ORI_RESILIENCE__IDEMPOTENCY__TTL` | 3 |
| `ORI_SEARCH__BACKENDS` | 3 |
| `ORI_SEARCH__DATABASE` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__API_KEY` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__HOSTS` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__INDEX_PREFIX` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_REPLICAS` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_SHARDS` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__PASSWORD` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__USERNAME` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__USE_SSL` | 3 |
| `ORI_SEARCH__ELASTICSEARCH__VERIFY_CERTS` | 3 |
| `ORI_SEARCH__ENABLED` | 3 |
| `ORI_SEARCH__MEILISEARCH__API_KEY` | 3 |
| `ORI_SEARCH__MEILISEARCH__DISPLAYED_ATTRIBUTES` | 3 |
| `ORI_SEARCH__MEILISEARCH__FILTERABLE_ATTRIBUTES` | 3 |
| `ORI_SEARCH__MEILISEARCH__MAX_CONNECTIONS` | 3 |
| `ORI_SEARCH__MEILISEARCH__MIN_WORD_SIZE_FOR_TYPOS` | 3 |
| `ORI_SEARCH__MEILISEARCH__RANKING_RULES` | 3 |
| `ORI_SEARCH__MEILISEARCH__SEARCHABLE_ATTRIBUTES` | 3 |
| `ORI_SEARCH__MEILISEARCH__SORTABLE_ATTRIBUTES` | 3 |
| `ORI_SEARCH__MEILISEARCH__TIMEOUT` | 3 |
| `ORI_SEARCH__MEILISEARCH__TYPO_TOLERANCE_ENABLED` | 3 |
| `ORI_SEARCH__MEILISEARCH__URL` | 3 |
| `ORI_SEARCH__MONGO__CONNECTION_STRING` | 3 |
| `ORI_SEARCH__MONGO__DATABASE_NAME` | 3 |
| `ORI_SEARCH__MONGO__USE_ATLAS_SEARCH` | 3 |
| `ORI_SEARCH__MYSQL__CONNECTION_STRING` | 3 |
| `ORI_SEARCH__MYSQL__FULLTEXT_MODE` | 3 |
| `ORI_SEARCH__MYSQL__MIN_WORD_LENGTH` | 3 |
| `ORI_SEARCH__OPENSEARCH__HOSTS` | 3 |
| `ORI_SEARCH__OPENSEARCH__INDEX_PREFIX` | 3 |
| `ORI_SEARCH__OPENSEARCH__PASSWORD` | 3 |
| `ORI_SEARCH__OPENSEARCH__TIMEOUT` | 3 |
| `ORI_SEARCH__OPENSEARCH__USERNAME` | 3 |
| `ORI_SEARCH__OPENSEARCH__USE_SSL` | 3 |
| `ORI_SEARCH__OPENSEARCH__VERIFY_SSL` | 3 |
| `ORI_SEARCH__OPERATIONS__BULK_CHUNK_SIZE` | 3 |
| `ORI_SEARCH__OPERATIONS__MAX_RETRIES` | 3 |
| `ORI_SEARCH__OPERATIONS__REQUEST_TIMEOUT` | 3 |
| `ORI_SEARCH__OPERATIONS__RETRY_BACKOFF` | 3 |
| `ORI_SEARCH__POSTGRES__AUTO_CREATE_TABLES` | 3 |
| `ORI_SEARCH__POSTGRES__CONNECTION_STRING` | 3 |
| `ORI_SEARCH__POSTGRES__ENABLE_TRIGRAM` | 3 |
| `ORI_SEARCH__POSTGRES__TEXT_SEARCH_CONFIG` | 3 |
| `ORI_SEARCH__QUERY__DEFAULT_LIMIT` | 3 |
| `ORI_SEARCH__QUERY__ENABLE_AGGREGATIONS` | 3 |
| `ORI_SEARCH__QUERY__ENABLE_FACETING` | 3 |
| `ORI_SEARCH__QUERY__ENABLE_HIGHLIGHTING` | 3 |
| `ORI_SEARCH__QUERY__FUZZY_THRESHOLD` | 3 |
| `ORI_SEARCH__QUERY__MAX_LIMIT` | 3 |
| `ORI_SEARCH__QUERY__STRATEGY` | 3 |
| `ORI_SEARCH__SQLITE__AUTO_CREATE_TABLES` | 3 |
| `ORI_SEARCH__SQLITE__DB_PATH` | 3 |
| `ORI_SEARCH__SQLITE__TOKENIZER` | 3 |
| `ORI_SEARCH__TIMEOUT` | 3 |
| `ORI_SEARCH__TYPESENSE__API_KEY` | 3 |
| `ORI_SEARCH__TYPESENSE__CONNECTION_TIMEOUT` | 3 |
| `ORI_SEARCH__TYPESENSE__HEALTH_CHECK_INTERVAL` | 3 |
| `ORI_SEARCH__TYPESENSE__NODES` | 3 |
| `ORI_VECTOR__EMBEDDING__API_BASE` | 3 |
| `ORI_VECTOR__EMBEDDING__API_KEY` | 3 |
| `ORI_VECTOR__EMBEDDING__BATCH_SIZE` | 3 |
| `ORI_VECTOR__EMBEDDING__DIMENSION` | 3 |
| `ORI_VECTOR__EMBEDDING__FORMAT` | 3 |
| `ORI_VECTOR__EMBEDDING__MODEL` | 3 |
| `ORI_VECTOR__EMBEDDING__TIMEOUT` | 3 |
| `ORI_WEB__API_DOCS__ENABLED` | 3 |
| `ORI_WEB__API_DOCS__PROVIDER` | 3 |
| `ORI_WEB__AUTH_EXCLUDE_PATHS` | 3 |
| `ORI_WEB__COMPRESSION_ENABLED` | 3 |
| `ORI_WEB__CORS` | 3 |
| `ORI_WEB__DEBUG_ROUTES` | 3 |
| `ORI_WEB__DEBUG_ROUTES_TOKEN` | 3 |
| `ORI_WEB__ENABLED` | 4 |
| `ORI_WEB__ENABLE_AUTH` | 3 |
| `ORI_WEB__ENABLE_DEBUG_ROUTES_ENV_GATE` | 3 |
| `ORI_WEB__ENABLE_IDENTITY_RESOLUTION` | 3 |
| `ORI_WEB__ENV` | 3 |
| `ORI_WEB__MAX_BODY_SIZE` | 3 |
| `ORI_WEB__NAME` | 3 |
| `ORI_WEB__OPENAPI_TITLE` | 3 |
| `ORI_WEB__OPENAPI_URL` | 3 |
| `ORI_WEB__OPENAPI_VERSION` | 3 |
| `ORI_WEB__RATE_LIMIT__DEFAULT_LIMIT` | 3 |
| `ORI_WEB__RATE_LIMIT__DEFAULT_WINDOW` | 3 |
| `ORI_WEB__RATE_LIMIT__ENABLED` | 3 |
| `ORI_WEB__RATE_LIMIT__RULES` | 3 |
| `ORI_WEB__RATE_LIMIT__STORAGE_BACKEND` | 3 |
| `ORI_WEB__RATE_LIMIT__WHITELIST_IPS` | 3 |
| `ORI_WEB__REDOC_JS_URL` | 3 |
| `ORI_WEB__REDOC_URL` | 3 |
| `ORI_WEB__ROLE_GUARD__RULES` | 3 |
| `ORI_WEB__SECURITY` | 3 |
| `ORI_WEB__SERVER__DEBUG` | 3 |
| `ORI_WEB__SERVER__HOST` | 3 |
| `ORI_WEB__SERVER__PORT` | 3 |
| `ORI_WEB__SERVER__RELOAD` | 3 |
| `ORI_WEB__SERVER__WORKERS` | 3 |
| `ORI_WEB__STATIC__DIRECTORY` | 3 |
| `ORI_WEB__STATIC__ENABLED` | 3 |
| `ORI_WEB__STATIC__HTML` | 3 |
| `ORI_WEB__STATIC__PREFIX` | 3 |
| `ORI_WEB__SWAGGER_CSS_URL` | 3 |
| `ORI_WEB__SWAGGER_JS_URL` | 3 |
| `ORI_WEB__SWAGGER_UI_URL` | 3 |
| `ORI_WEB__TEMPLATE_DIRECTORY` | 3 |

## Package Registry

### `oridecon-dev`

| Env Var | Type | Default | Description | Source |
|---------|------|---------|-------------|--------|
| `ORI_ADMIN__ALIAS_LIMIT__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Alias` |
| `ORI_ADMIN__ALIAS_LIMIT__MAX_ALIASES` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Alias` |
| `ORI_ADMIN__ALLOWED_HOSTS` | list[str] | (required) | Hostnames permitted to reach the application. Empty by default; must be configured before production deployment. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__ALLOW_UNAUTHENTICATED` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__API_PREFIX` | str | "/admin/api" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.api_prefix` |
| `ORI_ADMIN__ASYNC_PROCESSING` | bool | True | Process feedback handlers asynchronously in the background | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/feedback/config.py:F` |
| `ORI_ADMIN__AUDIT_ACTOR_ID` | str | (complex) | Actor identifier for audit log entries | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__AUDIT_HMAC_KEY` | str  \| None | None | HMAC key for audit checksum signing. Plain text or base64. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseC` |
| `ORI_ADMIN__AUDIT__READ_AUDIT_ENABLED` | bool | False | Log read operations (off by default; compliance mode only). | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuditConfig.audit.read_audit_enab` |
| `ORI_ADMIN__AUTH__CSRF_TOKEN_LIFETIME` | int | 3600 | CSRF token expiry in seconds | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.csrf_token_lifeti` |
| `ORI_ADMIN__AUTH__EMAIL_OTP__ENABLED` | bool | True | Enable email OTP factor | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminEmailOtpConfig.auth.email_otp.ena` |
| `ORI_ADMIN__AUTH__EMAIL_OTP__RESEND_COOLDOWN_SECONDS` | int | 60 | Minimum seconds between email OTP sends | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminEmailOtpConfig.auth.email_otp.res` |
| `ORI_ADMIN__AUTH__EMAIL_OTP__TTL_MINUTES` | int | 10 | Code validity window in minutes | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminEmailOtpConfig.auth.email_otp.ttl` |
| `ORI_ADMIN__AUTH__EMAIL_VERIFICATION__ENABLED` | bool | True | Enable email verification flow | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminEmailVerificationConfig.auth.emai` |
| `ORI_ADMIN__AUTH__EMAIL_VERIFICATION__ENFORCEMENT` | bool | True | Block login until the email is verified | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminEmailVerificationConfig.auth.emai` |
| `ORI_ADMIN__AUTH__EMAIL_VERIFICATION__TOKEN_TTL_HOURS` | int | 24 | Verify link validity in hours | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminEmailVerificationConfig.auth.emai` |
| `ORI_ADMIN__AUTH__ENABLED` | bool | True | Enable authentication | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.enabled` |
| `ORI_ADMIN__AUTH__ENV` | Literal['development', 'staging', 'production'] | "development" | Deployment environment for cookie security defaults | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.env` |
| `ORI_ADMIN__AUTH__IDLE_TIMEOUT` | int | 3600 | Session idle timeout in seconds | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.idle_timeout` |
| `ORI_ADMIN__AUTH__LOGIN_URL` | str | "/admin/login" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.login_url` |
| `ORI_ADMIN__AUTH__LOGOUT_URL` | str | "/admin/logout" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.logout_url` |
| `ORI_ADMIN__AUTH__MFA__ENABLED` | bool | True | Enable TOTP 2FA | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminMfaConfig.auth.mfa.enabled` |
| `ORI_ADMIN__AUTH__MFA__FACTOR` | str | "totp" | Second factor used at login: 'totp' (authenticator app) or 'email' (one-time code) | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminMfaConfig.auth.mfa.factor` |
| `ORI_ADMIN__AUTH__MFA__ISSUER` | str | "Oridecon Admin" | TOTP issuer label shown in authenticator apps | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminMfaConfig.auth.mfa.issuer` |
| `ORI_ADMIN__AUTH__MFA__SKEW` | int | 1 | Allowed clock skew in 30 second steps | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminMfaConfig.auth.mfa.skew` |
| `ORI_ADMIN__AUTH__OAUTH_ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.oauth_enabled` |
| `ORI_ADMIN__AUTH__OAUTH_PROVIDERS` | list[str] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.oauth_providers` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__MAX_LENGTH` | int | 128 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__MIN_LENGTH` | int | 12 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__REJECT_COMMON_PASSWORDS` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__REJECT_CONTAINING_EMAIL` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__REQUIRE_DIGIT` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__REQUIRE_LOWERCASE` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__REQUIRE_SPECIAL` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PASSWORD_POLICY__REQUIRE_UPPERCASE` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminPasswordPolicyConfig.auth.passwor` |
| `ORI_ADMIN__AUTH__PERMISSION_CACHE_TTL` | int | 300 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.permission_cache_` |
| `ORI_ADMIN__AUTH__PRINCIPAL_SOURCE` | Literal['internal', 'app'] | "internal" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.principal_source` |
| `ORI_ADMIN__AUTH__REGISTRATION__ALLOWED_EMAIL_DOMAINS` | list[str] | (required) | Restrict registration to these email domains (empty = any) | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRegistrationConfig.auth.registrat` |
| `ORI_ADMIN__AUTH__REGISTRATION__DEFAULT_ROLE` | str | "admin" | Role granted to new accounts | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRegistrationConfig.auth.registrat` |
| `ORI_ADMIN__AUTH__REGISTRATION__ENABLED` | bool | False | Allow self-service registration | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRegistrationConfig.auth.registrat` |
| `ORI_ADMIN__AUTH__ROLES` | dict[str, Any] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.roles` |
| `ORI_ADMIN__AUTH__SECURITY__IP_RATE_LIMIT_ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.ip_r` |
| `ORI_ADMIN__AUTH__SECURITY__IP_RATE_LIMIT_PER_15_MINUTES` | int | 30 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.ip_r` |
| `ORI_ADMIN__AUTH__SECURITY__IP_RATE_LIMIT_PER_HOUR` | int | 60 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.ip_r` |
| `ORI_ADMIN__AUTH__SECURITY__IP_RATE_LIMIT_PER_MINUTE` | int | 10 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.ip_r` |
| `ORI_ADMIN__AUTH__SECURITY__LOCKOUT_THRESHOLDS` | list[tuple[int, int]] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.lock` |
| `ORI_ADMIN__AUTH__SECURITY__PERMANENT_LOCKOUT_THRESHOLD` | int | 50 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.perm` |
| `ORI_ADMIN__AUTH__SECURITY__SETUP_TOKEN` | str  \| None | None | Optional ADMIN_SETUP_TOKEN — when set, must be provided during first-run setup. | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.setu` |
| `ORI_ADMIN__AUTH__SECURITY__SETUP_TOKEN_OPTIN_UNSAFE` | bool | False | Explicit escape hatch: boot without a setup token. Only for local/ephemeral environments — leaves the first-run wizard o | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminSecurityConfig.auth.security.setu` |
| `ORI_ADMIN__AUTH__SESSION_LIFETIME` | int | 86400 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.session_lifetime` |
| `ORI_ADMIN__AUTH__SESSION_SECRET` | SecretStr | SecretStr(...) | Session secret for signing | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.session_secret` |
| `ORI_ADMIN__AUTH__USERS` | list[Any] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminAuthConfig.auth.users` |
| `ORI_ADMIN__AUTO_ESCAPE` | bool | True | HTML-escape user strings by default. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ui/config.py:UIConfig.a` |
| `ORI_ADMIN__BACKEND` | str | (complex) | Graph store backend to use | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphCo` |
| `ORI_ADMIN__BACKEND` | str | (complex) | Vector store backend to use | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__BACKENDS` | list[CacheBackendConfig] | (required) | Backend configs | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheCo` |
| `ORI_ADMIN__BACKENDS` | list[NamedDatabaseConfig] | (required) | Multi-database backends list. When non-empty, drives multi-DB mode. The entry with primary=True (or the first entry) als | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseC` |
| `ORI_ADMIN__BACKENDS` | list[NamedNoSQLConfig] | (required) | Named NoSQL backends for multi-store support. When non-empty, the provider registers each backend under Annotated[Docume | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:NoSQLCo` |
| `ORI_ADMIN__BACKENDS` | list[NamedStorageConfig] | (required) | Named storage backends for multi-store support. When non-empty, the provider registers each backend under Annotated[Blob | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__BACKENDS` | list[NamedTaskConfig] | (required) | Named task queue backends for multi-queue support. When non-empty, the provider registers each backend under Annotated[T | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskCon` |
| `ORI_ADMIN__BACKENDS` | list[NamedVectorConfig] | (required) | Named vector store backends for multi-store support. When non-empty, the provider registers each backend under Annotated | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__BACKEND_OPTIONS` | dict | (required) | Keyword arguments for backend constructor | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__BACKEND_TYPE` | str | (complex) | Backend store type (memory, vault, ...) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__BACKEND__AMQP_URL` | SecretStr | SecretStr(...) | AMQP connection URL (may contain credentials). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBac` |
| `ORI_ADMIN__BACKEND__POSTGRES_DSN` | SecretStr  \| None | None | Postgres DSN (required when type="postgres"; may contain credentials). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBac` |
| `ORI_ADMIN__BACKEND__QUEUE_NAME` | str | (complex) | Name of the task queue | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBac` |
| `ORI_ADMIN__BACKEND__REDIS_URL` | SecretStr | SecretStr(...) | Redis connection URL (may contain credentials). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBac` |
| `ORI_ADMIN__BACKEND__TYPE` | str | (complex) | Queue backend type | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBac` |
| `ORI_ADMIN__BACKEND__URL` | SecretStr | Ellipsis | Database connection URL (may contain credentials) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseB` |
| `ORI_ADMIN__BATCH__ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Batch` |
| `ORI_ADMIN__BATCH__MAX_BATCH_SIZE` | int | 10 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Batch` |
| `ORI_ADMIN__BULKHEAD__MAX_CONCURRENT` | int | 10 | Max concurrent requests | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bu` |
| `ORI_ADMIN__BULKHEAD__NAME` | str | "" | Bulkhead name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bu` |
| `ORI_ADMIN__BULKHEAD__QUEUE_SIZE` | int | 100 | Max queue size | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bu` |
| `ORI_ADMIN__BULKHEAD__TIMEOUT` | float | 30.0 | Execution timeout | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bu` |
| `ORI_ADMIN__BULK_BATCH_SIZE` | int | (complex) | Batch size for bulk operations | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphCo` |
| `ORI_ADMIN__CACHE_TTL` | int | 3600 | Cache TTL in seconds (default: 1 hour) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__CACHE_TTL` | int | 86400 | Cache TTL in seconds (default: 24 hours) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__CACHE__DEFAULT_MAX_AGE` | Duration  \| int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Cache` |
| `ORI_ADMIN__CACHE__DEFAULT_SCOPE` | CacheScope | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Cache` |
| `ORI_ADMIN__CACHE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Cache` |
| `ORI_ADMIN__CACHE__VARY_HEADERS` | list[str] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Cache` |
| `ORI_ADMIN__CHUNKING_STRATEGY` | str | "recursive" | Chunking strategy (recursive, semantic, token) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__CHUNK_OVERLAP` | int | 50 | Overlap between consecutive chunks | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__CHUNK_SIZE` | int | 512 | Text chunk size in tokens | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__CIRCUIT_BREAKER` | CircuitBreakerConfig | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Re` |
| `ORI_ADMIN__CITATION_STYLE` | str | "inline" | Citation style (inline, footnote, numbered) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__CLEANUP_TEMP_FILES` | bool | True | Clean up temporary files after tests | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/testing/config.py:Testi` |
| `ORI_ADMIN__CLIENT_STDIO_COMMAND` | list[str] | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__CLIENT_URL` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__CLUSTERS__EXTRA` | list[ClusterSpec] | (required) | Extra clusters beyond the built-in infrastructure cluster | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminClustersConfig.clusters.extra` |
| `ORI_ADMIN__COLLECTION_NAME` | str | "default" | Collection/index name for vector store | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__COLLECTION_NAME` | str | "default" | Default collection name for AI-layer operations | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__COMMANDS` | list[dict[str, Any]] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.commands` |
| `ORI_ADMIN__COMMAND_BUS__ENABLE_LOGGING` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Comman` |
| `ORI_ADMIN__COMMAND_BUS__ENABLE_METRICS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Comman` |
| `ORI_ADMIN__COMMAND_BUS__ENABLE_VALIDATION` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Comman` |
| `ORI_ADMIN__COMMAND_BUS__MAX_RETRIES` | int | 3 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Comman` |
| `ORI_ADMIN__COMMAND_BUS__RETRY_DELAY_SECONDS` | float | 1.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Comman` |
| `ORI_ADMIN__COMMAND_BUS__TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Comman` |
| `ORI_ADMIN__COMPLEXITY__DEFAULT_FIELD_COST` | float | 1.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Compl` |
| `ORI_ADMIN__COMPLEXITY__DEFAULT_LIST_COST` | float | 10.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Compl` |
| `ORI_ADMIN__COMPLEXITY__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Compl` |
| `ORI_ADMIN__COMPLEXITY__MAX_COMPLEXITY` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Compl` |
| `ORI_ADMIN__CONNECTORS__FILESYSTEM__READ_ONLY` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:Filesy` |
| `ORI_ADMIN__CONNECTORS__FILESYSTEM__ROOT_DIR` | str | "" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:Filesy` |
| `ORI_ADMIN__CONNECTORS__GITHUB__API_URL` | str | "https://api.github.com" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:GitHub` |
| `ORI_ADMIN__CONNECTORS__GITHUB__TOKEN` | str | "" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:GitHub` |
| `ORI_ADMIN__CONNECTORS__GOOGLE_DRIVE__IMPERSONATED_EMAIL` | str | "" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:Google` |
| `ORI_ADMIN__CONNECTORS__GOOGLE_DRIVE__SERVICE_ACCOUNT_JSON` | str | "" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:Google` |
| `ORI_ADMIN__CONNECTORS__SLACK__BOT_TOKEN` | str | "" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SlackC` |
| `ORI_ADMIN__CONNECTORS__SLACK__MAX_MESSAGES` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SlackC` |
| `ORI_ADMIN__CONNECTORS__SQL__ALLOWED_TABLES` | list[str] | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SQLCon` |
| `ORI_ADMIN__CONNECTORS__SQL__DSN` | str | "" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SQLCon` |
| `ORI_ADMIN__CONNECTORS__SQL__READ_ONLY` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SQLCon` |
| `ORI_ADMIN__CONNECTORS__WEB_FETCH__ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebFet` |
| `ORI_ADMIN__CONNECTORS__WEB_FETCH__MAX_CONTENT_BYTES` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebFet` |
| `ORI_ADMIN__CONNECTORS__WEB_FETCH__USER_AGENT` | str | "oridecon-mcp/1.0" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebFet` |
| `ORI_ADMIN__CONNECTORS__WEB_SEARCH__API_KEY` | str | "" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebSea` |
| `ORI_ADMIN__CONNECTORS__WEB_SEARCH__MAX_RESULTS` | int | 10 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebSea` |
| `ORI_ADMIN__CONNECTORS__WEB_SEARCH__PROVIDER` | str | "brave" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebSea` |
| `ORI_ADMIN__CONTRIBUTORS` | dict[str, ContributorConfig] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.contributors` |
| `ORI_ADMIN__CONTRIBUTOR_COLLISION_MODE` | Literal['warn', 'error'] | "warn" | How to handle name collisions when multiple contributors register widgets, pages, or routes with the same name. 'warn' ( | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.contributor_collision_mode` |
| `ORI_ADMIN__CORS_ORIGINS` | list[str] | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__CORS__ALLOWED_ORIGINS` | list[str] | (required) | Allowed origins (use ['*'] to allow all) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__ALLOW_CREDENTIALS` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__ALLOW_HEADERS` | list[str] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__ALLOW_METHODS` | list[str] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__ALLOW_ORIGIN_REGEX` | str  \| None | None | Regex pattern for allowed origins (matched when not in allowed_origins) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__DEBUG_PERMISSIVE` | bool | False | When True and debug mode is active, allow any origin via wildcard (explicit opt-in replacement for the old implicit debu | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__ENABLED` | bool | True | Enable CORS | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__EXPOSE_HEADERS` | list[str] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CORS__MAX_AGE` | int | 600 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CROSS_ORIGIN__EMBEDDER_POLICY` | str | "require-corp" | Cross-Origin-Embedder-Policy header value | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CROSS_ORIGIN__ENABLED` | bool | False | Emit cross-origin isolation headers | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CROSS_ORIGIN__OPENER_POLICY` | str | "same-origin" | Cross-Origin-Opener-Policy header value | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CROSS_ORIGIN__RESOURCE_POLICY` | str | "same-origin" | Cross-Origin-Resource-Policy header value | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSP__DIRECTIVES` | dict[str, Any] | (required) | CSP directives mapping directive name to source expression(s) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSP__ENABLED` | bool | True | Emit the Content-Security-Policy header | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__COOKIE_DOMAIN` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__COOKIE_HTTPONLY` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__COOKIE_NAME` | str | "csrf_token" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__COOKIE_PATH` | str | "/" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__COOKIE_SAMESITE` | str | "Lax" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__COOKIE_SECURE` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__EXCLUDED_PATHS` | list[str] | (required) | URL path prefixes exempt from CSRF validation for cookie-less requests; cookie-bearing requests on these paths are still | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__EXCLUDE_AUTH_SCHEMES` | list[str] | (required) | Authorization header schemes that bypass CSRF validation (explicit opt-in). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__EXCLUDE_CONTENT_TYPES` | list[str] | (required) | Content-Type values that bypass CSRF validation (explicit opt-in — JSON requests are validated by default so cookie-auth | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__HEADER_NAME` | str | "X-CSRF-Token" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__SECRET_KEY` | str  \| None | None | HMAC secret used to sign and verify CSRF tokens (populated via ORI_WEB__SECURITY__CSRF__SECRET_KEY) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__TOKEN_LENGTH` | int | 32 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CSRF__TOKEN_TTL` | int | 3600 | TTL in seconds for synchronizer-mode tokens stored in cache. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__CUSTOM_HEADERS` | dict[str, str] | (required) | Additional HTTP response headers emitted verbatim | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__DASHBOARD_LAYOUT__LAYOUT` | Literal['grid', 'masonry'] | "grid" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:DashboardLayoutConfig.dashboard_layout` |
| `ORI_ADMIN__DASHBOARD_LAYOUT__MAX_WIDGETS` | int | 20 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:DashboardLayoutConfig.dashboard_layout` |
| `ORI_ADMIN__DASHBOARD_LAYOUT__WIDGET_REFRESH_DEFAULT` | int | 30 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:DashboardLayoutConfig.dashboard_layout` |
| `ORI_ADMIN__DATALOADER__BATCH_DELAY_MS` | float | 2.0 | Delay in milliseconds before executing a DataLoaderProtocol batch. A small non-zero value (2ms) lets more keys accumulat | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataL` |
| `ORI_ADMIN__DATALOADER__BATCH_ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataL` |
| `ORI_ADMIN__DATALOADER__CACHE_ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataL` |
| `ORI_ADMIN__DATALOADER__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataL` |
| `ORI_ADMIN__DATALOADER__MAX_BATCH_SIZE` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataL` |
| `ORI_ADMIN__DATA__QUERY_TIMEOUT_SECONDS` | int | 5 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminDataConfig.data.query_timeout_sec` |
| `ORI_ADMIN__DB_REUSE` | bool | True | Reuse test databases between tests | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/testing/config.py:Testi` |
| `ORI_ADMIN__DEBUG` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.debug` |
| `ORI_ADMIN__DEBUG` | bool | (complex) | Debug mode | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheCo` |
| `ORI_ADMIN__DEBUG` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Events` |
| `ORI_ADMIN__DEBUG` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__DEBUG` | bool | False | Enable debug mode | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monit` |
| `ORI_ADMIN__DEBUG_COMPONENTS` | bool | False | Render data-component debug attributes. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ui/config.py:UIConfig.d` |
| `ORI_ADMIN__DEFAULT_DIMENSION` | int | 1536 | Default vector dimension | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__DEFAULT_DISTANCE_METRIC` | DistanceMetric | (complex) | Default distance metric for new collections | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__DEFAULT_DRIVER` | Literal['local', 's3', 'gcs', 'azure', 'memory', 'r2'] | (complex) | Default storage driver to use | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__DEFAULT_INDEX_TYPE` | IndexType | (complex) | Default index type for new collections | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__DEFAULT_QUERY_LIMIT` | int | (complex) | Default limit for query results | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphCo` |
| `ORI_ADMIN__DEFAULT_THEME` | str | "default" | Default CSS theme name. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ui/config.py:UIConfig.d` |
| `ORI_ADMIN__DEFAULT_TRAVERSAL_MAX_DEPTH` | int | (complex) | Default maximum depth for traversals | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphCo` |
| `ORI_ADMIN__DEPTH_LIMIT__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Depth` |
| `ORI_ADMIN__DEPTH_LIMIT__IGNORE_INTROSPECTION` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Depth` |
| `ORI_ADMIN__DEPTH_LIMIT__MAX_DEPTH` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Depth` |
| `ORI_ADMIN__DRIVER` | str | "mongodb" | NoSQL driver name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:NoSQLCo` |
| `ORI_ADMIN__DRIVERS` | dict[str, StorageLocalConfig  \| StorageS3Config  \| StorageGCSConfig  \| Storag | (required) | Driver-specific configurations | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__EMBEDDING_MODEL` | str  \| None | None | Embedding model identifier. Must be set explicitly — no vendor-specific default. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__EMBEDDING_MODEL` | str | "text-embedding-3-small" | Embedding model name for AI-layer embedding generation | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__EMBEDDING_PROVIDER` | str | "openai" | Embedding provider (openai, cohere, etc.) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable AI features | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.e` |
| `ORI_ADMIN__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.enabled` |
| `ORI_ADMIN__ENABLED` | bool | (complex) | Whether cache is enabled | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheCo` |
| `ORI_ADMIN__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseC` |
| `ORI_ADMIN__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Events` |
| `ORI_ADMIN__ENABLED` | bool | True | Master on/off switch for all feedback collection | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/feedback/config.py:F` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable the graph store subsystem | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphCo` |
| `ORI_ADMIN__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable the MCP server subsystem | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable monitoring | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monit` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable NoSQL support | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:NoSQLCo` |
| `ORI_ADMIN__ENABLED` | bool | True | Master on/off switch for all observability | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable the RAG pipeline | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__ENABLED` | bool | True | Whether secrets subsystem is enabled | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable the security subsystem | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__ENABLED` | bool | True | Whether tasks module is enabled | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskCon` |
| `ORI_ADMIN__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/testing/config.py:Testi` |
| `ORI_ADMIN__ENABLED` | bool | True | Enable the vector store subsystem | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__ENABLE_ADMIN` | bool | True | Whether to register the AuditAdminContributor | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditCo` |
| `ORI_ADMIN__ENABLE_CACHE` | bool | False | Enable embedding caching (requires a CacheBackend binding) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__ENABLE_CACHING` | bool | True | Enable caching for RAG queries | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__ENABLE_CITATIONS` | bool | True | Include source citations in responses | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__ENABLE_CORS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__ENABLE_CSRF` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__ENABLE_HALLUCINATION_DETECTION` | bool | True | Enable hallucination detection for AI responses | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__ENABLE_HYDE` | bool | False | Enable HyDE (Hypothetical Document Embeddings) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__ENABLE_IDENTITY_RESOLUTION` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__ENABLE_QUERY_EXPANSION` | bool | True | Enable query expansion techniques | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__ENABLE_REALTIME` | bool | False | Enable realtime update features. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ui/config.py:UIConfig.e` |
| `ORI_ADMIN__ENABLE_SSE` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__ENABLE_SSE` | bool | False | Enable Server-Sent Events support. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ui/config.py:UIConfig.e` |
| `ORI_ADMIN__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheCo` |
| `ORI_ADMIN__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Events` |
| `ORI_ADMIN__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monit` |
| `ORI_ADMIN__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskCon` |
| `ORI_ADMIN__ENVIRONMENT` | str | (complex) | Environment | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheCo` |
| `ORI_ADMIN__ENVIRONMENT` | Environment | (complex) | Deployment environment | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monit` |
| `ORI_ADMIN__ERRORS__DEBUG_MODE` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Error` |
| `ORI_ADMIN__ERRORS__INCLUDE_STACKTRACE` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Error` |
| `ORI_ADMIN__ERRORS__LOG_ERRORS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Error` |
| `ORI_ADMIN__ERRORS__MASK_ERRORS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Error` |
| `ORI_ADMIN__EVENT_BUS__ALLOW_NO_HANDLERS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__CONTINUE_ON_ERROR` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__ENABLE_DEAD_LETTER` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__HANDLER_TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__MAX_CONCURRENT_HANDLERS` | int | 10 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__MAX_HANDLER_RETRIES` | int | 3 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__MAX_QUEUE_PER_SUBSCRIBER` | int | 1000 | Maximum number of events queued per event type before backpressure is applied. 0 means unbounded (no backpressure). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__PARALLEL_DISPATCH` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_BUS__RETRY_FAILED_HANDLERS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventB` |
| `ORI_ADMIN__EVENT_STORE_BACKEND` | EventStoreBackend | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Events` |
| `ORI_ADMIN__EXTENSIONS` | dict[str, Any] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.extensions` |
| `ORI_ADMIN__EXTRA` | dict[str, Any] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskCon` |
| `ORI_ADMIN__FEATURES__ACTIVITY_FEED` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.activity_` |
| `ORI_ADMIN__FEATURES__API_DOCS` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.api_docs` |
| `ORI_ADMIN__FEATURES__AUDIT_LOGGING` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.audit_log` |
| `ORI_ADMIN__FEATURES__AUTOSAVE` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.autosave` |
| `ORI_ADMIN__FEATURES__COMMAND_PALETTE` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.command_p` |
| `ORI_ADMIN__FEATURES__KEYBOARD_SHORTCUTS` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.keyboard_` |
| `ORI_ADMIN__FEATURES__NOTIFICATIONS` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.notificat` |
| `ORI_ADMIN__FEATURES__OPTIMISTIC_UPDATES` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.optimisti` |
| `ORI_ADMIN__FEATURES__SEARCH` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.search` |
| `ORI_ADMIN__FEATURES__THEME_TOGGLE` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.theme_tog` |
| `ORI_ADMIN__FEATURES__UNDO_REDO` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.undo_redo` |
| `ORI_ADMIN__FEATURES__WEBHOOKS` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminFeaturesConfig.features.webhooks` |
| `ORI_ADMIN__FIRESTORE__CREDENTIALS_JSON` | str  \| None | None | Path to a service account JSON key file, or the raw JSON string. When ``None``, Application Default Credentials (ADC) ar | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:Firesto` |
| `ORI_ADMIN__FIRESTORE__DATABASE_ID` | str | "(default)" | Firestore database ID (use '(default)' for the default database) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:Firesto` |
| `ORI_ADMIN__FIRESTORE__PROJECT_ID` | str | Ellipsis | Google Cloud project ID | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:Firesto` |
| `ORI_ADMIN__FORM_DEFAULTS__AUTOSAVE_ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FormDefaults.form_defaults.autosave_en` |
| `ORI_ADMIN__FORM_DEFAULTS__AUTOSAVE_INTERVAL_MS` | int | 30000 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FormDefaults.form_defaults.autosave_in` |
| `ORI_ADMIN__FORM_DEFAULTS__CONFIRM_UNSAVED_CHANGES` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FormDefaults.form_defaults.confirm_uns` |
| `ORI_ADMIN__FORM_DEFAULTS__INLINE_VALIDATION` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FormDefaults.form_defaults.inline_vali` |
| `ORI_ADMIN__FORM_DEFAULTS__SHOW_REQUIRED_INDICATOR` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FormDefaults.form_defaults.show_requir` |
| `ORI_ADMIN__FRAMEWORK_PAGES__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FrameworkPagesConfig.framework_pages.e` |
| `ORI_ADMIN__FRAMEWORK_PAGES__REQUIRE_PERMISSION` | str | "admin:framework:access" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FrameworkPagesConfig.framework_pages.r` |
| `ORI_ADMIN__GOVERNANCE` | Any | (required) | AI governance configuration | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.g` |
| `ORI_ADMIN__HEADERS__CONTENT_TYPE_NOSNIFF` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEADERS__CSP` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEADERS__FRAME_OPTIONS` | str | "DENY" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEADERS__HSTS_INCLUDE_SUBDOMAINS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEADERS__HSTS_MAX_AGE` | int | 31536000 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEADERS__PERMISSIONS_POLICY` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEADERS__REFERRER_POLICY` | str | "strict-origin-when-cross-origin" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEADERS__XSS_PROTECTION` | str | "1; mode=block" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HEALTH_CHECKS_ENABLED` | bool | True | Enable background health checking for AI components | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config` |
| `ORI_ADMIN__HEALTH_CHECK_TIMEOUT` | float | 5.0 | Timeout in seconds for the startup health check in StorageProvider.boot() | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__HEALTH__CHECKS` | list[str] | (required) | List of health check names to run | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Healt` |
| `ORI_ADMIN__HEALTH__ENABLED` | bool | True | Enable health checks | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Healt` |
| `ORI_ADMIN__HEALTH__INCLUDE_DETAILS` | bool | True | Include detailed health info in response | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Healt` |
| `ORI_ADMIN__HEALTH__INTERVAL` | int | (complex) | Health check interval in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Healt` |
| `ORI_ADMIN__HEALTH__PATH` | str | "/health" | Health endpoint path | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Healt` |
| `ORI_ADMIN__HEALTH__TIMEOUT` | float | 5.0 | Health check timeout in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Healt` |
| `ORI_ADMIN__HMAC_KEY` | bytes  \| None | None | HMAC key for checksum computation | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditCo` |
| `ORI_ADMIN__HOST` | str | "0.0.0.0" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__HSTS__ENABLED` | bool | False | Emit the Strict-Transport-Security header | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HSTS__INCLUDE_SUBDOMAINS` | bool | True | Apply HSTS to all subdomains | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HSTS__MAX_AGE` | int | 31536000 | HSTS max-age in seconds (default 1 year) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HSTS__PRELOAD` | bool | False | Include site in HSTS preload list | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__HTMX_PREFIX` | str | "/admin/htmx" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.htmx_prefix` |
| `ORI_ADMIN__HTMX_VERSION` | str | "2.0.4" | HTMX CDN version. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ui/config.py:UIConfig.h` |
| `ORI_ADMIN__INTEGRATIONS__CACHE__DEFAULT_TTL_SECONDS` | int | 60 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:CacheIntegrationConfig.integrations.ca` |
| `ORI_ADMIN__INTEGRATIONS__CACHE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:CacheIntegrationConfig.integrations.ca` |
| `ORI_ADMIN__INTEGRATIONS__CACHE__KEY_PREFIX` | str | "admin" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:CacheIntegrationConfig.integrations.ca` |
| `ORI_ADMIN__INTEGRATIONS__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminIntegrationsConfig.integrations.e` |
| `ORI_ADMIN__INTEGRATIONS__FEATURES__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:FeaturesIntegrationConfig.integrations` |
| `ORI_ADMIN__INTEGRATIONS__MONITOR__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:MonitorIntegrationConfig.integrations.` |
| `ORI_ADMIN__INTEGRATIONS__RESILIENCE__CIRCUIT_FAILURE_THRESHOLD` | int | 5 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResilienceIntegrationConfig.integratio` |
| `ORI_ADMIN__INTEGRATIONS__RESILIENCE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResilienceIntegrationConfig.integratio` |
| `ORI_ADMIN__INTEGRATIONS__RESILIENCE__RETRY_MAX_ATTEMPTS` | int | 3 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResilienceIntegrationConfig.integratio` |
| `ORI_ADMIN__INTEGRATIONS__SEARCH__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:SearchIntegrationConfig.integrations.s` |
| `ORI_ADMIN__INTEGRATIONS__SEARCH__FALLBACK_TO_LIKE` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:SearchIntegrationConfig.integrations.s` |
| `ORI_ADMIN__INTEGRATIONS__STORAGE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:StorageIntegrationConfig.integrations.` |
| `ORI_ADMIN__INTEGRATIONS__STORAGE__PRESIGNED_URL_EXPIRY` | int | 3600 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:StorageIntegrationConfig.integrations.` |
| `ORI_ADMIN__INTEGRATIONS__TASKS__BULK_THRESHOLD` | int | 25 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TasksIntegrationConfig.integrations.ta` |
| `ORI_ADMIN__INTEGRATIONS__TASKS__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TasksIntegrationConfig.integrations.ta` |
| `ORI_ADMIN__INTEGRATION__CACHE_KEY_PREFIX` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Integ` |
| `ORI_ADMIN__INTEGRATION__SQL_CONTEXT_BRIDGE` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Integ` |
| `ORI_ADMIN__INTROSPECTION__ALLOWED_ENVIRONMENTS` | set[str] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Intro` |
| `ORI_ADMIN__INTROSPECTION__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Intro` |
| `ORI_ADMIN__KAFKA__AUTO_OFFSET_RESET` | str | "earliest" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaC` |
| `ORI_ADMIN__KAFKA__BOOTSTRAP_SERVERS` | str | Ellipsis | Kafka bootstrap servers | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaC` |
| `ORI_ADMIN__KAFKA__CONSUMER_GROUP` | str | "events-consumers" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaC` |
| `ORI_ADMIN__KAFKA__ENABLE_AUTO_COMMIT` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaC` |
| `ORI_ADMIN__KAFKA__TOPIC_PREFIX` | str | "events" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaC` |
| `ORI_ADMIN__LIFECYCLE__AUTO_PROVISION_ISOLATION` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Lifec` |
| `ORI_ADMIN__LIFECYCLE__ISOLATION_STRATEGY` | str | "row_level" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Lifec` |
| `ORI_ADMIN__LLM` | Any  \| None | None | LLM configuration (optional) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.l` |
| `ORI_ADMIN__LOGGING_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Loggin` |
| `ORI_ADMIN__LOGGING_MIDDLEWARE__INCLUDE_PAYLOAD` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Loggin` |
| `ORI_ADMIN__LOGGING_MIDDLEWARE__LOG_LEVEL` | str | "INFO" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Loggin` |
| `ORI_ADMIN__LOGGING_MIDDLEWARE__MAX_PAYLOAD_LENGTH` | int | 1000 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Loggin` |
| `ORI_ADMIN__LOGGING__ENABLED` | bool | True | Enable structured logging | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Loggi` |
| `ORI_ADMIN__LOGGING__FORMAT` | str | "json" | Log format (json, text) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Loggi` |
| `ORI_ADMIN__LOGGING__INCLUDE_TRACE_CONTEXT` | bool | True | Include trace context in logs | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Loggi` |
| `ORI_ADMIN__LOGGING__LEVEL` | str | "INFO" | Default log level | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Loggi` |
| `ORI_ADMIN__LOGGING__REDACT_FIELDS` | list[str] | (required) | Fields to redact from logs | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Loggi` |
| `ORI_ADMIN__MAX_AGE_SECONDS` | float | (complex) | Seconds before automatic rotation | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__MAX_REQUEST_SIZE` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__MAX_RETRIES` | int | (complex) | Maximum number of retries for operations | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphCo` |
| `ORI_ADMIN__MAX_RETRIES` | int | (complex) | Maximum number of retries for operations | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__MEMORY__ENABLE_SNAPSHOTS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:InMemo` |
| `ORI_ADMIN__MEMORY__MAX_COLLECTIONS` | int | 100 | Maximum number of collections in memory | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Memory` |
| `ORI_ADMIN__MEMORY__MAX_EDGES` | int | (complex) | Maximum number of edges in memory | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:MemoryC` |
| `ORI_ADMIN__MEMORY__MAX_EVENTS_PER_STREAM` | int | 10000 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:InMemo` |
| `ORI_ADMIN__MEMORY__MAX_NODES` | int | (complex) | Maximum number of nodes in memory | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:MemoryC` |
| `ORI_ADMIN__MEMORY__MAX_VECTORS_PER_COLLECTION` | int | 100000 | Maximum number of vectors per collection | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Memory` |
| `ORI_ADMIN__METRICS_ENABLED` | bool | True | Enable metrics collection | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config` |
| `ORI_ADMIN__METRICS_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Metric` |
| `ORI_ADMIN__METRICS_MIDDLEWARE__HISTOGRAM_BUCKETS` | list[float] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Metric` |
| `ORI_ADMIN__METRICS_MIDDLEWARE__INCLUDE_HISTOGRAMS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Metric` |
| `ORI_ADMIN__METRICS_MIDDLEWARE__PREFIX` | str | "events" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Metric` |
| `ORI_ADMIN__METRICS__COLLECTION_INTERVAL` | float | 60.0 | Metrics collection interval in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metri` |
| `ORI_ADMIN__METRICS__DEFAULT_LABELS` | dict[str, str] | (required) | Default labels for all metrics | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metri` |
| `ORI_ADMIN__METRICS__ENABLED` | bool | True | Enable metrics collection | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metri` |
| `ORI_ADMIN__METRICS__ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metri` |
| `ORI_ADMIN__METRICS__HISTOGRAM_BUCKETS` | list[float] | (required) | Default histogram bucket boundaries | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metri` |
| `ORI_ADMIN__METRICS__HISTOGRAM_BUCKETS` | list[float] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metri` |
| `ORI_ADMIN__METRICS__INCLUDE_LABELS` | list[str] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metri` |
| `ORI_ADMIN__METRICS__NAMESPACE` | str | "oridecon_graphql" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metri` |
| `ORI_ADMIN__METRICS__PREFIX` | str | (complex) | MetricProtocol name prefix | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metri` |
| `ORI_ADMIN__MIGRATIONS__LOCK_TIMEOUT` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseM` |
| `ORI_ADMIN__MIN_CITATION_CONFIDENCE` | float | 0.6 | Minimum confidence for citation inclusion | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__MOCK_EXTERNAL_SERVICES` | bool | True | Mock external service calls | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/testing/config.py:Testi` |
| `ORI_ADMIN__MONGODB__AUTH_SOURCE` | str | "admin" | Authentication database | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__CONNECTION_STRING` | SecretStr | Ellipsis | MongoDB connection string | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoD` |
| `ORI_ADMIN__MONGODB__CONNECT_TIMEOUT_MS` | int | 10000 | Connection timeout (ms) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__DATABASE` | str | "oridecon" | Database name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__DATABASE_NAME` | str | "events" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoD` |
| `ORI_ADMIN__MONGODB__EVENTS_COLLECTION` | str | "domain_events" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoD` |
| `ORI_ADMIN__MONGODB__MAX_POOL_SIZE` | int | 100 | Maximum connection pool size | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__MAX_POOL_SIZE` | int | 10 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoD` |
| `ORI_ADMIN__MONGODB__MIN_POOL_SIZE` | int | 10 | Minimum connection pool size | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__READ_PREFERENCE` | str | "primaryPreferred" | Read preference mode | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__RETRY_READS` | bool | True | Enable read retries | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__RETRY_WRITES` | bool | True | Enable write retries | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__SERVER_SELECTION_TIMEOUT` | int | 30000 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoD` |
| `ORI_ADMIN__MONGODB__SERVER_SELECTION_TIMEOUT_MS` | int | 5000 | Server selection timeout (ms) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__SNAPSHOTS_COLLECTION` | str | "snapshots" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoD` |
| `ORI_ADMIN__MONGODB__SOCKET_TIMEOUT_MS` | int | 30000 | Socket timeout (ms) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__URI` | str | "mongodb://localhost:27017" | MongoDB connection URI | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__MONGODB__WRITE_CONCERN_W` | str  \| int | "majority" | Write concern level | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDB` |
| `ORI_ADMIN__NAME` | str | "ai" | Configuration name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.n` |
| `ORI_ADMIN__NAME` | str | "admin" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.name` |
| `ORI_ADMIN__NAME` | str | (complex) | Provider name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheCo` |
| `ORI_ADMIN__NAME` | str | "database" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseC` |
| `ORI_ADMIN__NAME` | str | "events" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Events` |
| `ORI_ADMIN__NAME` | str | "graphql" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__NAME` | str | (complex) | Provider name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monit` |
| `ORI_ADMIN__NAME` | str | "secrets" | Configuration name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__NAME` | str | "storage" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__NAME` | str | "tasks" | Configuration name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskCon` |
| `ORI_ADMIN__NAVIGATION_GROUPS` | dict[str, AdminNavigationGroup] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.navigation_groups` |
| `ORI_ADMIN__NEO4J__CONNECTION_TIMEOUT` | float | (complex) | Connection timeout in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__DATABASE` | str | (complex) | Target database name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__ENCRYPTED` | bool | False | Whether to use SSL/TLS encryption | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__FETCH_SIZE` | int | (complex) | Default fetch size for results | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__MAX_CONNECTION_POOL_SIZE` | int | (complex) | Maximum number of connections in the pool | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__MAX_TRANSACTION_RETRY_TIME` | float | 30.0 | Maximum time for transaction retries | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__PASSWORD` | SecretStr | (required) | Neo4j password | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__TRUST` | str | "TRUST_SYSTEM_CA_SIGNED_CERTIFICATES" | Trust strategy for SSL | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__URI` | str | "bolt://localhost:7687" | Neo4j BOLT URI | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__NEO4J__USERNAME` | str | "neo4j" | Neo4j username | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jCo` |
| `ORI_ADMIN__OBSERVABILITY` | Any | (required) | AI observability configuration (tracing and metrics) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.o` |
| `ORI_ADMIN__OBSERVABILITY__HIGH_CARDINALITY_LABELS_ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminObservabilityConfig.observability` |
| `ORI_ADMIN__OBSERVABILITY__METRICS_ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminObservabilityConfig.observability` |
| `ORI_ADMIN__OPENTELEMETRY__BATCH_SIZE` | int | 512 | Export batch size | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__COMPRESSION` | str | "none" | Compression type (none, gzip) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__ENDPOINT` | str  \| None | None | OTLP endpoint URL | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__EXPORT_INTERVAL` | float | 5.0 | Export interval seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__HEADERS` | dict[str, str] | (required) | OTLP request headers | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__INSECURE` | bool | False | Use insecure connection | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__METRICS_EXPORTERS` | list[OTelExporterConfig] | (required) | List of metrics exporters to build. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__TIMEOUT` | float | 30.0 | Export timeout seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPENTELEMETRY__TRACING_EXPORTERS` | list[OTelExporterConfig] | (required) | List of tracing exporters to build. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenT` |
| `ORI_ADMIN__OPERATIONS__ECHO` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseO` |
| `ORI_ADMIN__OPERATIONS__STATEMENT_TIMEOUT` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseO` |
| `ORI_ADMIN__OUTBOX__BATCH_MAX_AGE` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseO` |
| `ORI_ADMIN__OUTBOX__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseO` |
| `ORI_ADMIN__OUTBOX__POLL_INTERVAL` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseO` |
| `ORI_ADMIN__OVERRIDES__CACHE_TTL` | int | DEFAULT_CONFIG_CACHE_TTL |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Confi` |
| `ORI_ADMIN__PATH` | str | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__PATH` | str | "/mcp" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__PERMISSIONS_POLICY` | dict[str, str] | (required) | Permissions-Policy directive map | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__PERSISTED_QUERIES__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Persi` |
| `ORI_ADMIN__PERSISTED_QUERIES__STORE_TYPE` | str | "memory" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Persi` |
| `ORI_ADMIN__PERSISTED_QUERIES__TTL_SECONDS` | Duration  \| int | 86400 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Persi` |
| `ORI_ADMIN__PERSIST_DIRECTORY` | str  \| None | None | Local directory path for vector store persistence (e.g. Chroma) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__PGVECTOR__CREATE_EXTENSION` | bool | True | Whether to create pgvector extension if missing | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVect` |
| `ORI_ADMIN__PGVECTOR__DATABASE` | str | "primary" | Name of the database backend from db.backends to use for pgvector. Matches a 'name:' entry in the db.backends list. Defa | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVect` |
| `ORI_ADMIN__PGVECTOR__DEFAULT_EF_SEARCH` | int | (complex) | Default ef_search for HNSW index | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVect` |
| `ORI_ADMIN__PGVECTOR__DEFAULT_LISTS` | int | (complex) | Default number of lists for IVFFlat index | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVect` |
| `ORI_ADMIN__PGVECTOR__DEFAULT_PROBES` | int | (complex) | Default number of probes for IVFFlat index | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVect` |
| `ORI_ADMIN__PGVECTOR__SCHEMA` | str | "public" | Database schema for vector tables | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVect` |
| `ORI_ADMIN__PGVECTOR__TABLE_PREFIX` | str | "vec_" | Prefix for vector storage tables | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVect` |
| `ORI_ADMIN__PINECONE__API_KEY` | SecretStr | SecretStr(...) | Pinecone API key | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pineco` |
| `ORI_ADMIN__PINECONE__ENVIRONMENT` | str | "" | Pinecone environment (e.g. 'us-west1-gcp') | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pineco` |
| `ORI_ADMIN__PINECONE__INDEX_NAME` | str | "" | Name of the Pinecone index | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pineco` |
| `ORI_ADMIN__PINECONE__NAMESPACE` | str | "" | Default namespace for the index | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pineco` |
| `ORI_ADMIN__PINECONE__POOL_THREADS` | int | 4 | Number of threads for the connection pool | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pineco` |
| `ORI_ADMIN__PINECONE__TIMEOUT` | float | (complex) | Request timeout in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pineco` |
| `ORI_ADMIN__PLAYGROUND__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Playg` |
| `ORI_ADMIN__PLAYGROUND__PATH` | str | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Playg` |
| `ORI_ADMIN__PLAYGROUND__TITLE` | str | "Oridecon GraphQL Playground" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Playg` |
| `ORI_ADMIN__POOL__ACQUIRE_TIMEOUT` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__POOL__IDLE_TIMEOUT` | Duration | Duration.minutes(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__POOL__MAX_LIFETIME` | Duration | Duration.hours(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__POOL__MAX_OVERFLOW` | int | 5 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__POOL__MAX_SIZE` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__POOL__MIN_SIZE` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__POOL__RECYCLE` | int | 3600 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__POOL__TIMEOUT` | float | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseP` |
| `ORI_ADMIN__PORT` | int | 8080 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__POSTGRES` | PostgresEventStoreConfig  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Events` |
| `ORI_ADMIN__PREFIX` | str | "/admin" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.prefix` |
| `ORI_ADMIN__PROJECTION__BATCH_SIZE` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projec` |
| `ORI_ADMIN__PROJECTION__CHECKPOINT_INTERVAL` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projec` |
| `ORI_ADMIN__PROJECTION__ENABLE_PARALLEL_PROJECTIONS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projec` |
| `ORI_ADMIN__PROJECTION__MAX_CATCH_UP_EVENTS` | int | 10000 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projec` |
| `ORI_ADMIN__PROJECTION__REBUILD_BATCH_SIZE` | int | 1000 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projec` |
| `ORI_ADMIN__PROMETHEUS__ENABLE_DEFAULT_METRICS` | bool | True | Enable default process metrics | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prome` |
| `ORI_ADMIN__PROMETHEUS__METRICS_TABLE` | str | "metrics_samples" | Table name for metrics samples | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prome` |
| `ORI_ADMIN__PROMETHEUS__PATH` | str | "/metrics" | Metrics endpoint path | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prome` |
| `ORI_ADMIN__PROMETHEUS__PORT` | int | (complex) | Metrics server port | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prome` |
| `ORI_ADMIN__PROMETHEUS__PUSHGATEWAY_URL` | str  \| None | None | Pushgateway URL for push-based metrics | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prome` |
| `ORI_ADMIN__PROMETHEUS__PUSH_INTERVAL` | float | 10.0 | Push interval for Pushgateway | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prome` |
| `ORI_ADMIN__PROMETHEUS__STORE_IN_DB` | bool | False | Persist metrics observations to DB | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prome` |
| `ORI_ADMIN__PUSH_BACKENDS` | list[NamedPushConfig] | (required) | Named push notification backends for multi-backend support. When non-empty, the provider registers each backend under An | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_ADMIN__QDRANT__API_KEY` | SecretStr  \| None | None | Qdrant API key | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Qdrant` |
| `ORI_ADMIN__QDRANT__GRPC_PORT` | int | 6334 | gRPC port for Qdrant | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Qdrant` |
| `ORI_ADMIN__QDRANT__PREFER_GRPC` | bool | True | Whether to prefer gRPC over HTTP | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Qdrant` |
| `ORI_ADMIN__QDRANT__TIMEOUT` | float | (complex) | Request timeout in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Qdrant` |
| `ORI_ADMIN__QDRANT__URL` | str | "http://localhost:6333" | Qdrant server URL | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Qdrant` |
| `ORI_ADMIN__QUERY_BUS__ENABLE_LOGGING` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:QueryB` |
| `ORI_ADMIN__QUERY_BUS__ENABLE_METRICS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:QueryB` |
| `ORI_ADMIN__QUERY_BUS__TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:QueryB` |
| `ORI_ADMIN__RABBITMQ__DURABLE` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Rabbit` |
| `ORI_ADMIN__RABBITMQ__EXCHANGE_NAME` | str | "events" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Rabbit` |
| `ORI_ADMIN__RABBITMQ__PREFETCH_COUNT` | int | 10 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Rabbit` |
| `ORI_ADMIN__RABBITMQ__QUEUE_PREFIX` | str | "events" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Rabbit` |
| `ORI_ADMIN__RABBITMQ__URL` | SecretStr | Ellipsis | AMQP connection URL | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Rabbit` |
| `ORI_ADMIN__RAG` | Any  \| None | None | RAG pipeline configuration (optional) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.r` |
| `ORI_ADMIN__RATE_LIMIT` | RateLimitConfig | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__RATE_LIMIT__BULK_PER_MINUTE` | int | 5 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.bulk_p` |
| `ORI_ADMIN__RATE_LIMIT__BURST` | int  \| None | None | Maximum burst size | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRat` |
| `ORI_ADMIN__RATE_LIMIT__BURST_SIZE` | int | 10 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.burst_` |
| `ORI_ADMIN__RATE_LIMIT__CREATE_PER_MINUTE` | int | 30 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.create` |
| `ORI_ADMIN__RATE_LIMIT__DELETE_PER_MINUTE` | int | 20 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.delete` |
| `ORI_ADMIN__RATE_LIMIT__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.enable` |
| `ORI_ADMIN__RATE_LIMIT__ENABLED` | bool | False | Whether rate limiting is enabled | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRat` |
| `ORI_ADMIN__RATE_LIMIT__PER` | float | 1.0 | Time period in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRat` |
| `ORI_ADMIN__RATE_LIMIT__RATE` | int | 100 | Number of tasks allowed per time period | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRat` |
| `ORI_ADMIN__RATE_LIMIT__REQUESTS_PER_HOUR` | int | 1000 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.reques` |
| `ORI_ADMIN__RATE_LIMIT__REQUESTS_PER_MINUTE` | int | 60 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.reques` |
| `ORI_ADMIN__RATE_LIMIT__UPDATE_PER_MINUTE` | int | 60 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRateLimitConfig.rate_limit.update` |
| `ORI_ADMIN__RBAC__SUPER_ADMIN_ROLE` | str | "superadmin" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminRbacConfig.rbac.super_admin_role` |
| `ORI_ADMIN__REFERRER_POLICY` | str | "strict-origin-when-cross-origin" | Referrer-Policy header value | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:` |
| `ORI_ADMIN__REQUEST_TIMEOUT` | float | 30.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__REQUIRE_AUTH` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.require_auth` |
| `ORI_ADMIN__RESOLUTION__HEADER_NAME` | str | DEFAULT_HEADER_NAME |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOLUTION__JWT_CLAIM_KEY` | str | DEFAULT_JWT_CLAIM_KEY |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOLUTION__PATH_PATTERN` | str  \| None | DEFAULT_PATH_PATTERN |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOLUTION__RESOLVERS` | list[str] | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOLUTION__STRICT_MEMBERSHIP` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOLUTION__SUBDOMAIN_PATTERN` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOLUTION__TRUSTED_RESOLVERS` | list[str] | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOLUTION__VALIDATOR_CACHE_TTL` | int | DEFAULT_VALIDATOR_CACHE_TTL |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resol` |
| `ORI_ADMIN__RESOURCES` | dict[str, ResourceYAMLConfig] | (required) |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.resources` |
| `ORI_ADMIN__RESOURCE_DEFAULTS__ACTION_LAYOUT` | Literal['horizontal', 'vertical', 'dropdown'] | "horizontal" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResourceDefaults.resource_defaults.act` |
| `ORI_ADMIN__RESOURCE_DEFAULTS__ENABLE_BULK_ACTIONS` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResourceDefaults.resource_defaults.ena` |
| `ORI_ADMIN__RESOURCE_DEFAULTS__ENABLE_EXPORT` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResourceDefaults.resource_defaults.ena` |
| `ORI_ADMIN__RESOURCE_DEFAULTS__ENABLE_SEARCH` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResourceDefaults.resource_defaults.ena` |
| `ORI_ADMIN__RESOURCE_DEFAULTS__PER_PAGE` | int | 20 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResourceDefaults.resource_defaults.per` |
| `ORI_ADMIN__RESOURCE_DEFAULTS__SOFT_DELETE` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResourceDefaults.resource_defaults.sof` |
| `ORI_ADMIN__RESOURCE_DEFAULTS__TIMESTAMP_FIELDS` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:ResourceDefaults.resource_defaults.tim` |
| `ORI_ADMIN__RETENTION_POLICY` | RetentionPolicy | (required) | Retention rules | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditCo` |
| `ORI_ADMIN__RETRY` | RetryConfig | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Re` |
| `ORI_ADMIN__RETRY` | RetryConfig | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskCon` |
| `ORI_ADMIN__RETRY_DELAY` | float | (complex) | Delay between retries in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphCo` |
| `ORI_ADMIN__RETRY_DELAY` | float | (complex) | Delay between retries in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__RETRY_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryM` |
| `ORI_ADMIN__RETRY_MIDDLEWARE__EXPONENTIAL_BASE` | float | 2.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryM` |
| `ORI_ADMIN__RETRY_MIDDLEWARE__INITIAL_DELAY_SECONDS` | float | 0.1 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryM` |
| `ORI_ADMIN__RETRY_MIDDLEWARE__MAX_DELAY_SECONDS` | float | 10.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryM` |
| `ORI_ADMIN__RETRY_MIDDLEWARE__MAX_RETRIES` | int | 3 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryM` |
| `ORI_ADMIN__SAGA__CLEANUP_COMPLETED_AFTER_HOURS` | int | 24 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaCo` |
| `ORI_ADMIN__SAGA__DEFAULT_TIMEOUT_SECONDS` | float | 300.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaCo` |
| `ORI_ADMIN__SAGA__ENABLE_COMPENSATION` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaCo` |
| `ORI_ADMIN__SAGA__MAX_RETRIES_PER_STEP` | int | 3 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaCo` |
| `ORI_ADMIN__SAGA__PERSIST_STATE` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaCo` |
| `ORI_ADMIN__SAGA__RETRY_DELAY_SECONDS` | float | 1.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaCo` |
| `ORI_ADMIN__SCHEDULER__CHECK_INTERVAL` | float | (complex) | Interval between schedule checks (seconds) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskSch` |
| `ORI_ADMIN__SCHEDULER__ENABLED` | bool | True | Whether scheduling is enabled | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskSch` |
| `ORI_ADMIN__SCHEDULER__TIMEZONE` | str | (complex) | Timezone for cron expressions | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskSch` |
| `ORI_ADMIN__SCHEMA_BASELINE_PATH` | str  \| None | None | Path to a GraphQL SDL (.graphql) file containing the baseline schema. When set, GraphQLProvider.boot() compares the curr | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Graph` |
| `ORI_ADMIN__SERVER_NAME` | str | "oridecon-mcp" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__SERVER_VERSION` | str | "1.0.0" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__SERVICE__ALLOWED_MIME_TYPES` | list[str] | (required) | Allowed MIME types for upload validation. Defaults to a safe set of common image types: ['image/jpeg', 'image/png', 'ima | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__SERVICE__CIRCUIT_BREAKER_ENABLED` | bool | (complex) | Enable circuit breaker | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__CIRCUIT_BREAKER_THRESHOLD` | int | (complex) | Circuit breaker threshold | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__DEFAULT_BACKEND` | str  \| None | None | Default backend name | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__DEFAULT_SERIALIZER` | str | (complex) | Default serializer | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__ENABLE_HEALTH_CHECKS` | bool | (complex) | Enable health checks | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__ENABLE_METRICS` | bool | (complex) | Enable metrics | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__ENABLE_PROTECTION` | bool | (complex) | Enable stampede protection | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__MAX_FILE_SIZE_MB` | int | (complex) | Maximum file size in MB | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Stora` |
| `ORI_ADMIN__SERVICE__PROTECTION_LOCK_TTL` | int | (complex) | Protection lock TTL | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__PROTECTION_MAX_WAIT` | float | (complex) | Max wait for locks | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SERVICE__PROTECTION_RETRY_INTERVAL` | float | (complex) | Lock retry interval | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheSe` |
| `ORI_ADMIN__SIMILARITY_THRESHOLD` | float | 0.7 | Minimum similarity score threshold | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__SLO__ALERT_CHANNELS` | list[str] | (required) | Alert channel names for SLO violation dispatch | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOCo` |
| `ORI_ADMIN__SLO__ENABLED` | bool | True | Enable periodic SLO evaluation worker | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOCo` |
| `ORI_ADMIN__SLO__EVALUATION_INTERVAL` | float | 60.0 | SLO evaluation interval in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOCo` |
| `ORI_ADMIN__SLO__SUPPRESSION_WINDOW_SECONDS` | int | 300 | Alert suppression window in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOCo` |
| `ORI_ADMIN__SMS_BACKENDS` | list[NamedSMSConfig] | (required) | Named SMS backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[SMSCha | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_ADMIN__SNAPSHOTS__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapsh` |
| `ORI_ADMIN__SNAPSHOTS__EVENT_COUNT_THRESHOLD` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapsh` |
| `ORI_ADMIN__SNAPSHOTS__MAX_SNAPSHOTS_PER_AGGREGATE` | int | 5 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapsh` |
| `ORI_ADMIN__SNAPSHOTS__STRATEGY` | SnapshotStrategy | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapsh` |
| `ORI_ADMIN__SNAPSHOTS__TIME_THRESHOLD_SECONDS` | int | 3600 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapsh` |
| `ORI_ADMIN__SQLITE__DATABASE` | str | "./events.db" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Sqlite` |
| `ORI_ADMIN__SQLITE__JOURNAL_MODE` | str | "WAL" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Sqlite` |
| `ORI_ADMIN__SQLITE__PRAGMAS` | dict[str, str] | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Sqlite` |
| `ORI_ADMIN__SQLITE__WAL_MODE` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Sqlite` |
| `ORI_ADMIN__STATIC_DIR` | str  \| None | None |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.static_dir` |
| `ORI_ADMIN__STATIC_PREFIX` | str | "/admin/static" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.static_prefix` |
| `ORI_ADMIN__STDIO_MODE` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPCon` |
| `ORI_ADMIN__STORE_BACKEND` | str | (complex) | Backend type — 'sql' or 'memory' | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditCo` |
| `ORI_ADMIN__STORE_RAW_PAYLOADS` | bool | False | Persist raw incoming feedback payloads for auditing | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/feedback/config.py:F` |
| `ORI_ADMIN__STREAMING__BATCH_SIZE` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Stream` |
| `ORI_ADMIN__STREAMING__BUFFER_SIZE` | int | 1000 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Stream` |
| `ORI_ADMIN__STREAMING__ENABLE_WEBSOCKET` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Stream` |
| `ORI_ADMIN__STREAMING__MAX_SUBSCRIBERS` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Stream` |
| `ORI_ADMIN__STREAMING__POLL_INTERVAL_MS` | int | 100 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Stream` |
| `ORI_ADMIN__STREAMING__WEBSOCKET_PING_INTERVAL` | int | 30 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Stream` |
| `ORI_ADMIN__STRICT_RESOURCE_RESOLUTION` | bool | True | When True (production default), resource/controller resolution failures during AdminProvider.boot() raise immediately. W | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.strict_resource_resolution` |
| `ORI_ADMIN__SUBSCRIPTIONS__CONNECTION_TIMEOUT` | Duration  \| int | 60 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subsc` |
| `ORI_ADMIN__SUBSCRIPTIONS__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subsc` |
| `ORI_ADMIN__SUBSCRIPTIONS__KEEPALIVE_INTERVAL` | Duration  \| int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subsc` |
| `ORI_ADMIN__SUBSCRIPTIONS__PATH` | str | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subsc` |
| `ORI_ADMIN__SUBSCRIPTIONS__PROTOCOL` | SubscriptionProtocol | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subsc` |
| `ORI_ADMIN__SUBSYSTEMS` | dict[str, dict[str, Any]] | (required) | Dynamic configuration for third-party AI subsystems discovered via entry points.  Keys are subsystem names; values are t | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.s` |
| `ORI_ADMIN__SYNTHESIS_STRATEGY` | str | "hybrid" | Synthesis strategy (direct, extractive, abstractive, hybrid) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__TABLE_DEFAULTS__ENABLE_COLUMN_VISIBILITY` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TableDefaults.table_defaults.enable_co` |
| `ORI_ADMIN__TABLE_DEFAULTS__HOVER_HIGHLIGHT` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TableDefaults.table_defaults.hover_hig` |
| `ORI_ADMIN__TABLE_DEFAULTS__REORDERABLE_COLUMNS` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TableDefaults.table_defaults.reorderab` |
| `ORI_ADMIN__TABLE_DEFAULTS__ROW_HEIGHT` | int | 48 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TableDefaults.table_defaults.row_heigh` |
| `ORI_ADMIN__TABLE_DEFAULTS__STICKY_HEADER` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TableDefaults.table_defaults.sticky_he` |
| `ORI_ADMIN__TABLE_DEFAULTS__VIRTUALIZED` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TableDefaults.table_defaults.virtualiz` |
| `ORI_ADMIN__TABLE_DEFAULTS__ZEBRA_STRIPES` | bool | True |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TableDefaults.table_defaults.zebra_str` |
| `ORI_ADMIN__TABLE_NAME` | str | (complex) | SQL table name for the unified audit store | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditCo` |
| `ORI_ADMIN__TEMPLATES_DIR` | str  \| None | None |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.templates_dir` |
| `ORI_ADMIN__TENANCY__COOKIE_NAME` | str | "admin_tenant" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TenancyConfig.tenancy.cookie_name` |
| `ORI_ADMIN__TENANCY__DEFAULT_TENANT_ID` | str | "" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TenancyConfig.tenancy.default_tenant_i` |
| `ORI_ADMIN__TENANCY__ENABLED` | bool | False | Enable tenant-aware graph resolution | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphTe` |
| `ORI_ADMIN__TENANCY__ENABLED` | bool | False | Enable tenant-aware collection resolution in RAG pipeline | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGTen` |
| `ORI_ADMIN__TENANCY__ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TenancyConfig.tenancy.enabled` |
| `ORI_ADMIN__TENANCY__ENABLED` | bool | False | Enable tenant-aware collection name resolution | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__TENANCY__HEADER_NAME` | str | "x-tenant-id" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TenancyConfig.tenancy.header_name` |
| `ORI_ADMIN__TENANCY__RESOLVER_KIND` | str | "templated" | Which ``TenantCollectionResolver`` to use. One of ``"templated"`` or ``"pinecone_namespace"``. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__TENANCY__ROUTE_PREFIX_TEMPLATE` | str | "" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TenancyConfig.tenancy.route_prefix_tem` |
| `ORI_ADMIN__TENANCY__STRATEGY` | str | "node_property" | Which tenancy strategy to use. One of ``"node_property"`` or ``"graph_per_tenant"``. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphTe` |
| `ORI_ADMIN__TENANCY__TEMPLATE` | str | "{logical}_t_{tenant}" | Collection name template for ``GRAPH_PER_TENANT`` strategy. Supports ``{logical}`` and ``{tenant}`` placeholders. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphTe` |
| `ORI_ADMIN__TENANCY__TENANT_FIELD` | str | "tenant_id" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:TenancyConfig.tenancy.tenant_field` |
| `ORI_ADMIN__TENANT_ID` | str  \| None | None | Optional tenant namespace | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__THEME` | str | "light" | Active UI theme. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ui/config.py:UIConfig.t` |
| `ORI_ADMIN__TIMEOUT` | TimeoutConfig | field(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Re` |
| `ORI_ADMIN__TIMEOUT__DEFAULT_TIMEOUT` | float | (complex) | Default timeout | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskTim` |
| `ORI_ADMIN__TIMEOUT__ENFORCE_TIMEOUT` | bool | True | Enforce timeouts | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskTim` |
| `ORI_ADMIN__TIMEOUT__MAX_TIMEOUT` | float | (complex) | Maximum allowed timeout | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskTim` |
| `ORI_ADMIN__TITLE` | str | "Oridecon Admin" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminConfig.title` |
| `ORI_ADMIN__TOP_K` | int | 5 | Number of documents to retrieve | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__TRACE_MAX_ATTRIBUTE_LENGTH` | int | 0 | Cap on string attribute values written to trace spans, in characters. 0 disables the cap. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config` |
| `ORI_ADMIN__TRACE_REDACTION_ENABLED` | bool | False | Redact secret-shaped keys (e.g. token, password, api_key) from trace span attributes and audit metadata. Strongly recomm | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config` |
| `ORI_ADMIN__TRACING_ENABLED` | bool | True | Enable distributed tracing | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config` |
| `ORI_ADMIN__TRACING__ENABLED` | bool | True | Enable tracing | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__ENABLED` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Traci` |
| `ORI_ADMIN__TRACING__MAX_ATTRIBUTES` | int | 128 | Max attributes per span | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__MAX_EVENTS` | int | 128 | Max events per span | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__MAX_LINKS` | int | 128 | Max links per span | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__MAX_SPANS` | int | (complex) | Max number of spans to keep in memory | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__MAX_TRACES_PER_SECOND` | int | 100 | Max traces to sample per second | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__PROPAGATION_FORMATS` | list[str] | (required) | Propagation format list | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__SAMPLE_RATE` | float | 1.0 | Sample rate (0.0 to 1.0) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__SAMPLE_RATE` | float | 1.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Traci` |
| `ORI_ADMIN__TRACING__SERVICE_NAME` | str | (complex) | Service name for traces | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Traci` |
| `ORI_ADMIN__TRACING__SERVICE_NAME` | str | "oridecon-graphql" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Traci` |
| `ORI_ADMIN__TRACING__TRACE_DATALOADERS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Traci` |
| `ORI_ADMIN__TRACING__TRACE_RESOLVERS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Traci` |
| `ORI_ADMIN__TRANSACTION_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Transa` |
| `ORI_ADMIN__TRANSACTION_MIDDLEWARE__ISOLATION_LEVEL` | str | "READ_COMMITTED" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Transa` |
| `ORI_ADMIN__TRANSACTION_MIDDLEWARE__TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Transa` |
| `ORI_ADMIN__UI__CONTENT_MAX_WIDTH` | int  \| None | None |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminUIConfig.ui.content_max_width` |
| `ORI_ADMIN__UI__FAVICON_URL` | str  \| None | None |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminUIConfig.ui.favicon_url` |
| `ORI_ADMIN__UI__LOGO_URL` | str  \| None | None |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminUIConfig.ui.logo_url` |
| `ORI_ADMIN__UI__PRIMARY_COLOR` | str | "#6B7280" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminUIConfig.ui.primary_color` |
| `ORI_ADMIN__UI__SIDEBAR_COLLAPSED_WIDTH` | int | 64 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminUIConfig.ui.sidebar_collapsed_wid` |
| `ORI_ADMIN__UI__SIDEBAR_WIDTH` | int | 256 |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminUIConfig.ui.sidebar_width` |
| `ORI_ADMIN__UI__THEME` | Literal['light', 'dark', 'system'] | "system" |  | `experimental/apps/oridecon-admin/src/oridecon/admin/config.py:AdminUIConfig.ui.theme` |
| `ORI_ADMIN__UPSERT_BATCH_SIZE` | int | (complex) | Number of vectors per upsert batch | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Vector` |
| `ORI_ADMIN__USE_HYBRID_SEARCH` | bool | True | Enable hybrid search (semantic + keyword) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__VALIDATION_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Valida` |
| `ORI_ADMIN__VALIDATION_MIDDLEWARE__STRICT_MODE` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Valida` |
| `ORI_ADMIN__VECTOR` | Any  \| None | None | Vector store configuration | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.v` |
| `ORI_ADMIN__VECTOR_DIMENSION` | int | 1536 | Embedding vector dimension (1536 for OpenAI ada-002) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__VECTOR_STORE_TYPE` | str | "pgvector" | Vector store backend (pgvector, chroma, qdrant, mock) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGCon` |
| `ORI_ADMIN__VERIFICATION_BATCH_SIZE` | int | (complex) | Entries to verify per verification run | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditCo` |
| `ORI_ADMIN__VERIFICATION_SCHEDULE` | str | (complex) | Cron expression for scheduled verification | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditCo` |
| `ORI_ADMIN__VERSION` | str | (complex) | Config version | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheCo` |
| `ORI_ADMIN__VERSION_SKEW_ALERTS_ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Events` |
| `ORI_ADMIN__WARNING_BEFORE_SECONDS` | float | (complex) | Seconds before expiry to warn | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/secrets/config.py:Secre` |
| `ORI_ADMIN__WEAVIATE__API_KEY` | SecretStr  \| None | None | Weaviate API key for authenticated clusters | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weavia` |
| `ORI_ADMIN__WEAVIATE__GRPC_PORT` | int | 50051 | gRPC port for the Weaviate cluster | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weavia` |
| `ORI_ADMIN__WEAVIATE__TIMEOUT` | float | (complex) | Request timeout in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weavia` |
| `ORI_ADMIN__WEAVIATE__URL` | str | "http://localhost:8080" | Weaviate cluster URL (HTTP) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weavia` |
| `ORI_ADMIN__WORKER__DEFAULT_TIMEOUT` | float | (complex) | Default timeout for tasks without an explicit timeout (seconds) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWor` |
| `ORI_ADMIN__WORKER__ENFORCE_TIMEOUT` | bool | True | Whether to enforce timeouts on all tasks | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWor` |
| `ORI_ADMIN__WORKER__MAX_CONCURRENT_TASKS` | int | (complex) | Maximum concurrent tasks per worker | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWor` |
| `ORI_ADMIN__WORKER__MAX_TIMEOUT` | float | (complex) | Maximum allowed timeout for any task (seconds) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWor` |
| `ORI_ADMIN__WORKER__POLL_INTERVAL` | float | (complex) | Interval between queue polls (seconds) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWor` |
| `ORI_ADMIN__WORKER__SHUTDOWN_TIMEOUT` | float | (complex) | Timeout for graceful shutdown (seconds) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWor` |
| `ORI_ADMIN__WORKER__WORKER_COUNT` | int | (complex) | Number of worker instances | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWor` |
| `ORI_AI_AGENTS__DEFAULT_MAX_TOKENS` | int | 2048 | Default max tokens for LLM responses | `experimental/ai/oridecon-ai-agents/src/oridecon/ai/agents/config.py:AgentConfig.default_max_tokens` |
| `ORI_AI_AGENTS__DEFAULT_TEMPERATURE` | float | 0.7 | Default temperature for LLM calls | `experimental/ai/oridecon-ai-agents/src/oridecon/ai/agents/config.py:AgentConfig.default_temperature` |
| `ORI_AI_AGENTS__ENABLED` | bool | True | Enable the AI agents subsystem | `experimental/ai/oridecon-ai-agents/src/oridecon/ai/agents/config.py:AgentConfig.enabled` |
| `ORI_AI_AGENTS__ENABLE_METRICS` | bool | True | Enable Prometheus metrics | `experimental/ai/oridecon-ai-agents/src/oridecon/ai/agents/config.py:AgentConfig.enable_metrics` |
| `ORI_AI_AGENTS__ENABLE_TRACING` | bool | True | Enable OpenTelemetry tracing | `experimental/ai/oridecon-ai-agents/src/oridecon/ai/agents/config.py:AgentConfig.enable_tracing` |
| `ORI_AI_AGENTS__MAX_ITERATIONS` | int | 10 | Maximum reasoning iterations per execution | `experimental/ai/oridecon-ai-agents/src/oridecon/ai/agents/config.py:AgentConfig.max_iterations` |
| `ORI_AI_AGENTS__TOOL_MAX_RETRIES` | int | 3 | Number of retries for transient tool execution errors (ConnectionError, TimeoutError, OSError) | `experimental/ai/oridecon-ai-agents/src/oridecon/ai/agents/config.py:AgentConfig.tool_max_retries` |
| `ORI_AI_EVALUATION__DEFAULT_SEED` | int  \| None | None | Default seed for reproducible experiment runs | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.default` |
| `ORI_AI_EVALUATION__DEFAULT_THRESHOLD` | float | 0.8 | Default score threshold for passing evaluations | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.default` |
| `ORI_AI_EVALUATION__EMBEDDING_MODEL` | str | "text-embedding-3-small" | Model to use for embedding-based evaluations | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.embeddi` |
| `ORI_AI_EVALUATION__ENABLED` | bool | True | Enable the AI evaluation subsystem | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.enabled` |
| `ORI_AI_EVALUATION__EXPERIMENT_DIR` | str  \| None | None | Base directory for experiment tracking and checkpoint artifacts | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.experim` |
| `ORI_AI_EVALUATION__INCLUDE_METADATA` | bool | True | Whether to include metadata in run reports | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.include` |
| `ORI_AI_EVALUATION__MAX_RETRIES` | int | 3 | Maximum retries for failed evaluations | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.max_ret` |
| `ORI_AI_EVALUATION__MAX_SAMPLES` | int  \| None | None | Maximum number of samples per evaluation run | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.max_sam` |
| `ORI_AI_EVALUATION__TIMEOUT_SECONDS` | int | 30 | Timeout for evaluation execution in seconds | `experimental/ai/oridecon-ai-evaluation/src/oridecon/ai/evaluation/config.py:EvaluationConfig.timeout` |
| `ORI_AI_FEEDBACK__ASYNC_PROCESSING` | bool | True | Process feedback handlers asynchronously in the background | `experimental/ai/oridecon-ai-feedback/src/oridecon/ai/feedback/config.py:FeedbackConfig.async_process` |
| `ORI_AI_FEEDBACK__ENABLED` | bool | True | Master on/off switch for all feedback collection | `experimental/ai/oridecon-ai-feedback/src/oridecon/ai/feedback/config.py:FeedbackConfig.enabled` |
| `ORI_AI_FEEDBACK__STORE_RAW_PAYLOADS` | bool | False | Persist raw incoming feedback payloads for auditing | `experimental/ai/oridecon-ai-feedback/src/oridecon/ai/feedback/config.py:FeedbackConfig.store_raw_pay` |
| `ORI_AI_GOVERNANCE__ENABLED` | bool | True | Enable AI governance | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.enabled` |
| `ORI_AI_GOVERNANCE__ENFORCE_BUDGET` | bool | True | Enforce budget limits | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.enforce` |
| `ORI_AI_GOVERNANCE__FAIL_OPEN_ON_PERSISTENCE_ERROR` | bool | False | Allow requests when the persistence backend is unavailable. When False (default, fail-closed), a persistence failure (e. | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.fail_op` |
| `ORI_AI_GOVERNANCE__MAX_REQUEST_COST` | float  \| None | None | Maximum cost in dollars for a single request. Requests with an estimated cost above this threshold are rejected before t | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.max_req` |
| `ORI_AI_GOVERNANCE__MAX_TOKENS_PER_REQUEST` | int  \| None | None | Max tokens per request | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.max_tok` |
| `ORI_AI_GOVERNANCE__MODEL_ALLOWLIST` | dict[str, list[str]] | (required) | Per-user/role model allowlist. Keys are user IDs or role names; values are lists of allowed model patterns (supports glo | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.model_a` |
| `ORI_AI_GOVERNANCE__MODEL_DENYLIST` | dict[str, list[str]] | (required) | Per-user/role model denylist. Keys are user IDs or role names; values are lists of denied model patterns (supports glob  | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.model_d` |
| `ORI_AI_GOVERNANCE__MONTHLY_BUDGET` | float  \| None | None | Monthly budget in dollars | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.monthly` |
| `ORI_AI_GOVERNANCE__RESOURCE_UNITS` | list | (required) | Resource units this governance instance tracks. Per-tenant limits are configured via TenantConfigService overrides. | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.resourc` |
| `ORI_AI_GOVERNANCE__RESTRICTED_MODELS` | list[str] | (required) | List of restricted models | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.restric` |
| `ORI_AI_GOVERNANCE__RPM_LIMIT` | int  \| None | None | Requests Per Minute limit | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.rpm_lim` |
| `ORI_AI_GOVERNANCE__SOFT_LIMIT_PCT` | float  \| None | None | Fraction of monthly_budget at which to emit a soft-limit warning (e.g. 0.8 = warn at 80%). No hard block is applied at t | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.soft_li` |
| `ORI_AI_GOVERNANCE__TPM_LIMIT` | int  \| None | None | Tokens Per Minute limit | `experimental/ai/oridecon-ai-governance/src/oridecon/ai/governance/config.py:GovernanceConfig.tpm_lim` |
| `ORI_AI_GUARD__ENABLED` | bool | True |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.enabled` |
| `ORI_AI_GUARD__ENABLE_LLM_GUARDS` | bool | False |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.enable_llm_guards` |
| `ORI_AI_GUARD__GUARD_MODEL` | str | "gpt-4o-mini" |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.guard_model` |
| `ORI_AI_GUARD__INJECTION_ACTION` | str | "block" |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.injection_action` |
| `ORI_AI_GUARD__INJECTION_DETECTION` | bool | True |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.injection_detection` |
| `ORI_AI_GUARD__LENGTH_ACTION` | str | "block" |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.length_action` |
| `ORI_AI_GUARD__LLM_GUARD_FAIL_OPEN` | bool | False |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.llm_guard_fail_open` |
| `ORI_AI_GUARD__LLM_GUARD_THRESHOLD` | float | 0.7 |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.llm_guard_threshold` |
| `ORI_AI_GUARD__MAX_INPUT_CHARS` | int | 0 |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.max_input_chars` |
| `ORI_AI_GUARD__MAX_OUTPUT_CHARS` | int | 0 |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.max_output_chars` |
| `ORI_AI_GUARD__PARALLEL_EXECUTION` | bool | False |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.parallel_execution` |
| `ORI_AI_GUARD__PII_ACTION` | str | "redact" |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.pii_action` |
| `ORI_AI_GUARD__PII_DETECTION` | bool | True |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.pii_detection` |
| `ORI_AI_GUARD__PII_ENTITIES` | list[str] | field(...) |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.pii_entities` |
| `ORI_AI_GUARD__PII_REDACTION_OUTPUT` | bool | True |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.pii_redaction_output` |
| `ORI_AI_GUARD__RESTRICTED_TOPICS` | list[str] | field(...) |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.restricted_topics` |
| `ORI_AI_GUARD__SENSITIVITY_LEVEL` | str | "medium" |  | `experimental/ai/oridecon-ai-guard/src/oridecon/ai/guard/config.py:GuardConfig.sensitivity_level` |
| `ORI_AI_MCP__ALLOW_UNAUTHENTICATED` | bool | False |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.allow_unauthenticated` |
| `ORI_AI_MCP__CLIENT_STDIO_COMMAND` | list[str] | field(...) |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.client_stdio_command` |
| `ORI_AI_MCP__CLIENT_URL` | str  \| None | None |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.client_url` |
| `ORI_AI_MCP__CONNECTORS__FILESYSTEM__READ_ONLY` | bool | False |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:FilesystemConnectorConfig.connectors.f` |
| `ORI_AI_MCP__CONNECTORS__FILESYSTEM__ROOT_DIR` | str | "" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:FilesystemConnectorConfig.connectors.f` |
| `ORI_AI_MCP__CONNECTORS__GITHUB__API_URL` | str | "https://api.github.com" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:GitHubConnectorConfig.connectors.githu` |
| `ORI_AI_MCP__CONNECTORS__GITHUB__TOKEN` | str | "" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:GitHubConnectorConfig.connectors.githu` |
| `ORI_AI_MCP__CONNECTORS__GOOGLE_DRIVE__IMPERSONATED_EMAIL` | str | "" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:GoogleDriveConnectorConfig.connectors.` |
| `ORI_AI_MCP__CONNECTORS__GOOGLE_DRIVE__SERVICE_ACCOUNT_JSON` | str | "" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:GoogleDriveConnectorConfig.connectors.` |
| `ORI_AI_MCP__CONNECTORS__SLACK__BOT_TOKEN` | str | "" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:SlackConnectorConfig.connectors.slack.` |
| `ORI_AI_MCP__CONNECTORS__SLACK__MAX_MESSAGES` | int | 100 |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:SlackConnectorConfig.connectors.slack.` |
| `ORI_AI_MCP__CONNECTORS__SQL__ALLOWED_TABLES` | list[str] | field(...) |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:SQLConnectorConfig.connectors.sql.allo` |
| `ORI_AI_MCP__CONNECTORS__SQL__DSN` | str | "" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:SQLConnectorConfig.connectors.sql.dsn` |
| `ORI_AI_MCP__CONNECTORS__SQL__READ_ONLY` | bool | True |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:SQLConnectorConfig.connectors.sql.read` |
| `ORI_AI_MCP__CONNECTORS__WEB_FETCH__ENABLED` | bool | False |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:WebFetchConnectorConfig.connectors.web` |
| `ORI_AI_MCP__CONNECTORS__WEB_FETCH__MAX_CONTENT_BYTES` | int | (complex) |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:WebFetchConnectorConfig.connectors.web` |
| `ORI_AI_MCP__CONNECTORS__WEB_FETCH__USER_AGENT` | str | "oridecon-mcp/1.0" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:WebFetchConnectorConfig.connectors.web` |
| `ORI_AI_MCP__CONNECTORS__WEB_SEARCH__API_KEY` | str | "" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:WebSearchConnectorConfig.connectors.we` |
| `ORI_AI_MCP__CONNECTORS__WEB_SEARCH__MAX_RESULTS` | int | 10 |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:WebSearchConnectorConfig.connectors.we` |
| `ORI_AI_MCP__CONNECTORS__WEB_SEARCH__PROVIDER` | str | "brave" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:WebSearchConnectorConfig.connectors.we` |
| `ORI_AI_MCP__CORS_ORIGINS` | list[str] | field(...) |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.cors_origins` |
| `ORI_AI_MCP__ENABLED` | bool | True | Enable the MCP server subsystem | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.enabled` |
| `ORI_AI_MCP__ENABLE_SSE` | bool | True |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.enable_sse` |
| `ORI_AI_MCP__HOST` | str | "0.0.0.0" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.host` |
| `ORI_AI_MCP__MAX_REQUEST_SIZE` | int | (complex) |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.max_request_size` |
| `ORI_AI_MCP__PATH` | str | "/mcp" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.path` |
| `ORI_AI_MCP__PORT` | int | 8080 |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.port` |
| `ORI_AI_MCP__REQUEST_TIMEOUT` | float | 30.0 |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.request_timeout` |
| `ORI_AI_MCP__SERVER_NAME` | str | "oridecon-mcp" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.server_name` |
| `ORI_AI_MCP__SERVER_VERSION` | str | "1.0.0" |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.server_version` |
| `ORI_AI_MCP__STDIO_MODE` | bool | False |  | `experimental/ai/oridecon-ai-mcp/src/oridecon/ai/mcp/config.py:MCPConfig.stdio_mode` |
| `ORI_AI_MEMORY__CONSOLIDATION__AGE_THRESHOLD_HOURS` | float | (complex) | Minimum entry age (hours) before it can be consolidated | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:ConsolidationConfig.consolidatio` |
| `ORI_AI_MEMORY__CONSOLIDATION__BATCH_SIZE` | int | (complex) | Maximum entries processed per consolidation pass | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:ConsolidationConfig.consolidatio` |
| `ORI_AI_MEMORY__CONSOLIDATION__ENABLED` | bool | True | Whether automatic background consolidation is active | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:ConsolidationConfig.consolidatio` |
| `ORI_AI_MEMORY__CONSOLIDATION__IMPORTANCE_PRUNE_THRESHOLD` | float | (complex) | Entries below this importance score are eligible for pruning | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:ConsolidationConfig.consolidatio` |
| `ORI_AI_MEMORY__CONSOLIDATION__INTERVAL_SECONDS` | float | (complex) | How often to run a consolidation pass (seconds) | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:ConsolidationConfig.consolidatio` |
| `ORI_AI_MEMORY__DEFAULT_BACKEND` | str | (complex) | Backend type to use ('in_memory', 'cache', 'database', 'vector') | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:MemoryConfig.default_backend` |
| `ORI_AI_MEMORY__ENABLED` | bool | True | Enable the AI memory subsystem | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:MemoryConfig.enabled` |
| `ORI_AI_MEMORY__EPISODIC__DEFAULT_TOP_K` | int | (complex) | Default number of episodes to retrieve | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:EpisodicMemoryConfig.episodic.de` |
| `ORI_AI_MEMORY__EPISODIC__IMPORTANCE_WEIGHT` | float | (complex) | Weight applied to entry importance during scoring | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:EpisodicMemoryConfig.episodic.im` |
| `ORI_AI_MEMORY__EPISODIC__RECENCY_WEIGHT` | float | (complex) | Weight applied to temporal recency during scoring | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:EpisodicMemoryConfig.episodic.re` |
| `ORI_AI_MEMORY__EPISODIC__RELEVANCE_WEIGHT` | float | (complex) | Weight applied to semantic similarity during scoring | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:EpisodicMemoryConfig.episodic.re` |
| `ORI_AI_MEMORY__EPISODIC__TTL_SECONDS` | int | (complex) | Time-to-live for entries in seconds (0 = never expire) | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:EpisodicMemoryConfig.episodic.tt` |
| `ORI_AI_MEMORY__SEMANTIC__MAX_FACTS_PER_ENTITY` | int | (complex) | Hard cap on stored facts per entity | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:SemanticMemoryConfig.semantic.ma` |
| `ORI_AI_MEMORY__SEMANTIC__MIN_CONFIDENCE` | float | (complex) | Minimum confidence score required to store a fact | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:SemanticMemoryConfig.semantic.mi` |
| `ORI_AI_MEMORY__TTL_SECONDS` | int | (complex) | Default entry TTL in seconds (0 = never expire) | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:MemoryConfig.ttl_seconds` |
| `ORI_AI_MEMORY__WORKING__EPISODIC_FRACTION` | float | (complex) | Fraction of remaining budget for episodic recall | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:WorkingMemoryConfig.working.epis` |
| `ORI_AI_MEMORY__WORKING__MAX_RECENT_TURNS` | int | (complex) | Hard cap on recent turns regardless of budget | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:WorkingMemoryConfig.working.max_` |
| `ORI_AI_MEMORY__WORKING__RECENT_TURNS_FRACTION` | float | (complex) | Fraction of remaining budget for recent turns | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:WorkingMemoryConfig.working.rece` |
| `ORI_AI_MEMORY__WORKING__SEMANTIC_FRACTION` | float | (complex) | Fraction of remaining budget for semantic facts | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:WorkingMemoryConfig.working.sema` |
| `ORI_AI_MEMORY__WORKING__SYSTEM_PROMPT_TOKENS` | int | (complex) | Fixed token allocation for system prompt | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:WorkingMemoryConfig.working.syst` |
| `ORI_AI_MEMORY__WORKING__TOOL_DESCRIPTIONS_FRACTION` | float | (complex) | Fraction of remaining budget for tool descriptions | `experimental/ai/oridecon-ai-memory/src/oridecon/ai/memory/config.py:WorkingMemoryConfig.working.tool` |
| `ORI_AI_OBSERVABILITY__ENABLED` | bool | True | Master on/off switch for all observability | `experimental/ai/oridecon-ai-observability/src/oridecon/ai/observability/config.py:ObservabilityConfi` |
| `ORI_AI_OBSERVABILITY__HEALTH_CHECKS_ENABLED` | bool | True | Enable background health checking for AI components | `experimental/ai/oridecon-ai-observability/src/oridecon/ai/observability/config.py:ObservabilityConfi` |
| `ORI_AI_OBSERVABILITY__METRICS_ENABLED` | bool | True | Enable metrics collection | `experimental/ai/oridecon-ai-observability/src/oridecon/ai/observability/config.py:ObservabilityConfi` |
| `ORI_AI_OBSERVABILITY__TRACE_MAX_ATTRIBUTE_LENGTH` | int | 0 | Cap on string attribute values written to trace spans, in characters. 0 disables the cap. | `experimental/ai/oridecon-ai-observability/src/oridecon/ai/observability/config.py:ObservabilityConfi` |
| `ORI_AI_OBSERVABILITY__TRACE_REDACTION_ENABLED` | bool | False | Redact secret-shaped keys (e.g. token, password, api_key) from trace span attributes and audit metadata. Strongly recomm | `experimental/ai/oridecon-ai-observability/src/oridecon/ai/observability/config.py:ObservabilityConfi` |
| `ORI_AI_OBSERVABILITY__TRACING_ENABLED` | bool | True | Enable distributed tracing | `experimental/ai/oridecon-ai-observability/src/oridecon/ai/observability/config.py:ObservabilityConfi` |
| `ORI_AI_PROMPT__DEFAULT_FORMAT` | RenderFormat | DEFAULT_RENDER_FORMAT |  | `experimental/ai/oridecon-ai-prompt/src/oridecon/ai/prompt/config.py:PromptConfig.default_format` |
| `ORI_AI_PROMPT__ENABLED` | bool | True | Enable the AI prompt subsystem | `experimental/ai/oridecon-ai-prompt/src/oridecon/ai/prompt/config.py:PromptConfig.enabled` |
| `ORI_AI_PROMPT__MAX_VARIABLE_LENGTH` | int | 0 |  | `experimental/ai/oridecon-ai-prompt/src/oridecon/ai/prompt/config.py:PromptConfig.max_variable_length` |
| `ORI_AI_PROMPT__SANITIZE_INPUTS` | bool | True |  | `experimental/ai/oridecon-ai-prompt/src/oridecon/ai/prompt/config.py:PromptConfig.sanitize_inputs` |
| `ORI_AI_PROMPT__STRICT_SANITIZER` | bool | True |  | `experimental/ai/oridecon-ai-prompt/src/oridecon/ai/prompt/config.py:PromptConfig.strict_sanitizer` |
| `ORI_AI_RAG__CACHE_TTL` | int | 3600 | Cache TTL in seconds (default: 1 hour) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.cache_ttl` |
| `ORI_AI_RAG__CHUNKING_STRATEGY` | str | "recursive" | Chunking strategy (recursive, semantic, token) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.chunking_strategy` |
| `ORI_AI_RAG__CHUNK_OVERLAP` | int | 50 | Overlap between consecutive chunks | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.chunk_overlap` |
| `ORI_AI_RAG__CHUNK_SIZE` | int | 512 | Text chunk size in tokens | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.chunk_size` |
| `ORI_AI_RAG__CITATION_STYLE` | str | "inline" | Citation style (inline, footnote, numbered) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.citation_style` |
| `ORI_AI_RAG__COLLECTION_NAME` | str | "default" | Collection/index name for vector store | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.collection_name` |
| `ORI_AI_RAG__EMBEDDING_MODEL` | str  \| None | None | Embedding model identifier. Must be set explicitly — no vendor-specific default. | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.embedding_model` |
| `ORI_AI_RAG__EMBEDDING_PROVIDER` | str | "openai" | Embedding provider (openai, cohere, etc.) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.embedding_provider` |
| `ORI_AI_RAG__ENABLED` | bool | True | Enable the RAG pipeline | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.enabled` |
| `ORI_AI_RAG__ENABLE_CACHING` | bool | True | Enable caching for RAG queries | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.enable_caching` |
| `ORI_AI_RAG__ENABLE_CITATIONS` | bool | True | Include source citations in responses | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.enable_citations` |
| `ORI_AI_RAG__ENABLE_HALLUCINATION_DETECTION` | bool | True | Enable hallucination detection for AI responses | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.enable_hallucination_detecti` |
| `ORI_AI_RAG__ENABLE_HYDE` | bool | False | Enable HyDE (Hypothetical Document Embeddings) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.enable_hyde` |
| `ORI_AI_RAG__ENABLE_QUERY_EXPANSION` | bool | True | Enable query expansion techniques | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.enable_query_expansion` |
| `ORI_AI_RAG__MIN_CITATION_CONFIDENCE` | float | 0.6 | Minimum confidence for citation inclusion | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.min_citation_confidence` |
| `ORI_AI_RAG__PERSIST_DIRECTORY` | str  \| None | None | Local directory path for vector store persistence (e.g. Chroma) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.persist_directory` |
| `ORI_AI_RAG__SIMILARITY_THRESHOLD` | float | 0.7 | Minimum similarity score threshold | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.similarity_threshold` |
| `ORI_AI_RAG__SYNTHESIS_STRATEGY` | str | "hybrid" | Synthesis strategy (direct, extractive, abstractive, hybrid) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.synthesis_strategy` |
| `ORI_AI_RAG__TENANCY__ENABLED` | bool | False | Enable tenant-aware collection resolution in RAG pipeline | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGTenancyConfig.tenancy.enabled` |
| `ORI_AI_RAG__TOP_K` | int | 5 | Number of documents to retrieve | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.top_k` |
| `ORI_AI_RAG__USE_HYBRID_SEARCH` | bool | True | Enable hybrid search (semantic + keyword) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.use_hybrid_search` |
| `ORI_AI_RAG__VECTOR_DIMENSION` | int | 1536 | Embedding vector dimension (1536 for OpenAI ada-002) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.vector_dimension` |
| `ORI_AI_RAG__VECTOR_STORE_TYPE` | str | "pgvector" | Vector store backend (pgvector, chroma, qdrant, mock) | `experimental/ai/oridecon-ai-rag/src/oridecon/ai/rag/config.py:RAGConfig.vector_store_type` |
| `ORI_AI_SESSION__AUTO_CHECKPOINT_INTERVAL` | int  \| None | (complex) | Checkpoint every N turns; None to disable | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.auto_checkpoint_` |
| `ORI_AI_SESSION__BACKEND` | str | (complex) | Persistence backend (in_memory, cache, database) | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.backend` |
| `ORI_AI_SESSION__CLEANUP_INTERVAL_S` | int | (complex) | How often the cleanup scheduler sweeps for expired sessions | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.cleanup_interval` |
| `ORI_AI_SESSION__CONSOLIDATE_ON_CLOSE` | bool | (complex) | Whether to trigger memory consolidation on session close | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.consolidate_on_c` |
| `ORI_AI_SESSION__COOKIE_NAME` | str  \| None | (complex) | Cookie name for web session ID; None disables cookies | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.cookie_name` |
| `ORI_AI_SESSION__DEFAULT_SYSTEM_PROMPT` | str  \| None | None | System prompt injected into every new session | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.default_system_p` |
| `ORI_AI_SESSION__DEFAULT_TURN_STRATEGY` | str | (complex) | Default turn-selection strategy (round_robin, priority, llm_directed) | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.default_turn_str` |
| `ORI_AI_SESSION__ENABLED` | bool | True | Enable the AI session subsystem | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.enabled` |
| `ORI_AI_SESSION__HEADER_NAME` | str | (complex) | HTTP header name for session ID pass-through | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.header_name` |
| `ORI_AI_SESSION__MAX_AGENTS_PER_GROUP` | int | (complex) | Maximum agents in a multi-agent group session | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.max_agents_per_g` |
| `ORI_AI_SESSION__MAX_BRANCHES_PER_SESSION` | int | (complex) | Maximum forked branches per session | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.max_branches_per` |
| `ORI_AI_SESSION__MAX_CHECKPOINTS_PER_SESSION` | int | (complex) | Maximum retained checkpoints per session | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.max_checkpoints_` |
| `ORI_AI_SESSION__MAX_SESSIONS_PER_USER` | int | (complex) | Maximum concurrent sessions per user | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.max_sessions_per` |
| `ORI_AI_SESSION__MAX_TURNS_PER_SESSION` | int | (complex) | Hard cap on turns before the session is closed | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.max_turns_per_se` |
| `ORI_AI_SESSION__NAME` | str | "ai-session" | Logical name used for DI registration keys | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.name` |
| `ORI_AI_SESSION__SESSION_TTL` | int | (complex) | Maximum age of a session in seconds (0 to disable) | `experimental/ai/oridecon-ai-session/src/oridecon/ai/session/config.py:SessionConfig.session_ttl` |
| `ORI_AI_SKILLS__ALLOWED_SCRIPT_TYPES` | list[str] | (required) | Allowed script types (py, sh, js) | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.allowed_script_type` |
| `ORI_AI_SKILLS__AUTO_DISCOVER` | bool | (complex) | Whether to auto-scan packages for skills on boot | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.auto_discover` |
| `ORI_AI_SKILLS__BUILTIN_SKILLS` | list[str] | (required) | Names of built-in skills to register | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.builtin_skills` |
| `ORI_AI_SKILLS__CACHE_BACKEND` | str | (complex) | Which cache backend to use (in_memory, cache) | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.cache_backend` |
| `ORI_AI_SKILLS__CACHE_ENABLED` | bool | (complex) | Whether result caching is globally enabled | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.cache_enabled` |
| `ORI_AI_SKILLS__CACHE_TTL_SECONDS` | int | (complex) | Default TTL for cached skill results (seconds) | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.cache_ttl_seconds` |
| `ORI_AI_SKILLS__DEFAULT_TIMEOUT_SECONDS` | float | (complex) | Default execution timeout per skill (seconds) | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.default_timeout_sec` |
| `ORI_AI_SKILLS__ENABLED_DIRECTORIES` | list[str] | (required) | Which skill directories to enable (claude_code, opencode, cursor, etc.) | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.enabled_directories` |
| `ORI_AI_SKILLS__ENABLE_BUILTIN` | bool | (complex) | Whether built-in skills are registered on boot | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.enable_builtin` |
| `ORI_AI_SKILLS__ENABLE_SKILL_SOURCES` | bool | True | Whether to scan for external skill sources on boot | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.enable_skill_source` |
| `ORI_AI_SKILLS__ENFORCE_PERMISSIONS` | bool | (complex) | Whether permission checks are enforced | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.enforce_permissions` |
| `ORI_AI_SKILLS__LAZY_LOAD_CONTEXT` | bool | (complex) | Whether to lazily load skill context files | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.lazy_load_context` |
| `ORI_AI_SKILLS__MAX_CONCURRENT_EXECUTIONS` | int | (complex) | Semaphore cap on concurrent skill executions | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.max_concurrent_exec` |
| `ORI_AI_SKILLS__MAX_RETRIES` | int | (complex) | Default maximum retry attempts for skill execution | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.max_retries` |
| `ORI_AI_SKILLS__NAME` | str | "ai-skills" | Logical name used for DI registration keys | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.name` |
| `ORI_AI_SKILLS__SCAN_PACKAGES` | list[str] | (required) | Fully-qualified package names to scan for skills | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.scan_packages` |
| `ORI_AI_SKILLS__SCRIPT_TIMEOUT_SECONDS` | int | (complex) | Timeout for skill script execution (seconds) | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.script_timeout_seco` |
| `ORI_AI_SKILLS__SKILL_PATHS` | list[str] | (required) | Paths to scan for skills (SKILL.md folders) | `experimental/ai/oridecon-ai-skills/src/oridecon/ai/skills/config.py:SkillsConfig.skill_paths` |
| `ORI_AI_WORKERS__BATCH_EMBEDDING_CONCURRENCY` | int | 3 | Concurrency level for batch embedding execution | `experimental/ai/oridecon-ai-workers/src/oridecon/ai/workers/config.py:WorkersConfig.batch_embedding_` |
| `ORI_AI_WORKERS__DLQ_CHECK_INTERVAL` | int | 60 | Interval in seconds for DLQ recovery sweeps | `experimental/ai/oridecon-ai-workers/src/oridecon/ai/workers/config.py:WorkersConfig.dlq_check_interv` |
| `ORI_AI_WORKERS__DOCUMENT_INGESTION_CONCURRENCY` | int | 3 | Concurrency level for document parsing and chunking | `experimental/ai/oridecon-ai-workers/src/oridecon/ai/workers/config.py:WorkersConfig.document_ingesti` |
| `ORI_AI_WORKERS__ENABLED` | bool | True | Master on/off switch for all background workers | `experimental/ai/oridecon-ai-workers/src/oridecon/ai/workers/config.py:WorkersConfig.enabled` |
| `ORI_AI_WORKERS__ENABLE_MAINTENANCE` | bool | True | Enable vector store and cache maintenance tasks | `experimental/ai/oridecon-ai-workers/src/oridecon/ai/workers/config.py:WorkersConfig.enable_maintenan` |
| `ORI_AI__ENABLED` | bool | True | Enable AI features | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.enabled` |
| `ORI_AI__GOVERNANCE` | Any | (required) | AI governance configuration | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.governance` |
| `ORI_AI__LLM` | Any  \| None | None | LLM configuration (optional) | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.llm` |
| `ORI_AI__NAME` | str | "ai" | Configuration name | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.name` |
| `ORI_AI__OBSERVABILITY` | Any | (required) | AI observability configuration (tracing and metrics) | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.observability` |
| `ORI_AI__RAG` | Any  \| None | None | RAG pipeline configuration (optional) | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.rag` |
| `ORI_AI__SUBSYSTEMS` | dict[str, dict[str, Any]] | (required) | Dynamic configuration for third-party AI subsystems discovered via entry points.  Keys are subsystem names; values are t | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.subsystems` |
| `ORI_AI__VECTOR` | Any  \| None | None | Vector store configuration | `experimental/ai/oridecon-ai/src/oridecon/ai/config.py:AIConfig.vector` |
| `ORI_AUDIT__ENABLE_ADMIN` | bool | True | Whether to register the AuditAdminContributor | `packages/oridecon-audit/src/oridecon/audit/config.py:AuditConfig.enable_admin` |
| `ORI_AUDIT__HMAC_KEY` | bytes  \| None | None | HMAC key for checksum computation | `packages/oridecon-audit/src/oridecon/audit/config.py:AuditConfig.hmac_key` |
| `ORI_AUDIT__RETENTION_POLICY` | RetentionPolicy | (required) | Retention rules | `packages/oridecon-audit/src/oridecon/audit/config.py:AuditConfig.retention_policy` |
| `ORI_AUDIT__STORE_BACKEND` | str | (complex) | Backend type — 'sql' or 'memory' | `packages/oridecon-audit/src/oridecon/audit/config.py:AuditConfig.store_backend` |
| `ORI_AUDIT__TABLE_NAME` | str | (complex) | SQL table name for the unified audit store | `packages/oridecon-audit/src/oridecon/audit/config.py:AuditConfig.table_name` |
| `ORI_AUDIT__VERIFICATION_BATCH_SIZE` | int | (complex) | Entries to verify per verification run | `packages/oridecon-audit/src/oridecon/audit/config.py:AuditConfig.verification_batch_size` |
| `ORI_AUDIT__VERIFICATION_SCHEDULE` | str | (complex) | Cron expression for scheduled verification | `packages/oridecon-audit/src/oridecon/audit/config.py:AuditConfig.verification_schedule` |
| `ORI_AUTH__ADMIN_EMAIL` | str  \| None | None | Initial admin email | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__ADMIN_EMAIL` | str  \| None | None | Initial admin email | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.admin_email` |
| `ORI_AUTH__ADMIN_EMAIL` | str  \| None | None | Initial admin email | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__ADMIN_PASSWORD` | str  \| None | None | Initial admin password | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__ADMIN_PASSWORD` | str  \| None | None | Initial admin password | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.admin_password` |
| `ORI_AUTH__ADMIN_PASSWORD` | str  \| None | None | Initial admin password | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__ENABLED` | bool | True |  | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.enabled` |
| `ORI_AUTH__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__LOGIN_RATE_LIMIT` | str | "5/minute" | Default rate limit | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__LOGIN_RATE_LIMIT` | str | "5/minute" | Default rate limit | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.login_rate_limit` |
| `ORI_AUTH__LOGIN_RATE_LIMIT` | str | "5/minute" | Default rate limit | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__MAX_SESSIONS_PER_USER` | int  \| None | None | Maximum number of concurrent sessions allowed per user. ``None`` (the default) means unlimited.  When a positive integer | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__MAX_SESSIONS_PER_USER` | int  \| None | None | Maximum number of concurrent sessions allowed per user. ``None`` (the default) means unlimited.  When a positive integer | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.max_sessions_per_user` |
| `ORI_AUTH__MAX_SESSIONS_PER_USER` | int  \| None | None | Maximum number of concurrent sessions allowed per user. ``None`` (the default) means unlimited.  When a positive integer | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__MIDDLEWARE__BACKEND` | str | "session" | Auth backend type | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__BACKEND` | str | "session" | Auth backend type | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.backend` |
| `ORI_AUTH__MIDDLEWARE__BACKEND` | str | "session" | Auth backend type | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PATHS` | list[str] | (required) | Paths excluded from auth | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PATHS` | list[str] | (required) | Paths excluded from auth | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.exclude_paths` |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PATHS` | list[str] | (required) | Paths excluded from auth | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PREFIXES` | list[str] | (required) | Path prefixes excluded | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PREFIXES` | list[str] | (required) | Path prefixes excluded | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.exclude_prefixes` |
| `ORI_AUTH__MIDDLEWARE__EXCLUDE_PREFIXES` | list[str] | (required) | Path prefixes excluded | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__HEADER_NAME` | str | "Authorization" | Header name for token | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__HEADER_NAME` | str | "Authorization" | Header name for token | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.header_name` |
| `ORI_AUTH__MIDDLEWARE__HEADER_NAME` | str | "Authorization" | Header name for token | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__LOGIN_RATE_LIMIT` | str | "5/minute" | Rate limit for auth endpoints | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__LOGIN_RATE_LIMIT` | str | "5/minute" | Rate limit for auth endpoints | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.login_rate_limit` |
| `ORI_AUTH__MIDDLEWARE__LOGIN_RATE_LIMIT` | str | "5/minute" | Rate limit for auth endpoints | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__LOGIN_URL` | str  \| None | None | URL to redirect for login | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__LOGIN_URL` | str  \| None | None | URL to redirect for login | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.login_url` |
| `ORI_AUTH__MIDDLEWARE__LOGIN_URL` | str  \| None | None | URL to redirect for login | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__OPTIONAL_AUTH` | bool | False | Whether authentication is optional | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__OPTIONAL_AUTH` | bool | False | Whether authentication is optional | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.optional_auth` |
| `ORI_AUTH__MIDDLEWARE__OPTIONAL_AUTH` | bool | False | Whether authentication is optional | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__PERMISSIONS_REQUIRED` | list[str] | (required) | Permissions required | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__PERMISSIONS_REQUIRED` | list[str] | (required) | Permissions required | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.permissions_requi` |
| `ORI_AUTH__MIDDLEWARE__PERMISSIONS_REQUIRED` | list[str] | (required) | Permissions required | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__ROLES_REQUIRED` | list[str] | (required) | Roles required | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__ROLES_REQUIRED` | list[str] | (required) | Roles required | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.roles_required` |
| `ORI_AUTH__MIDDLEWARE__ROLES_REQUIRED` | list[str] | (required) | Roles required | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__MIDDLEWARE__SCHEME` | str | (complex) | Token scheme | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMidd` |
| `ORI_AUTH__MIDDLEWARE__SCHEME` | str | (complex) | Token scheme | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthMiddlewareConfig.middleware.scheme` |
| `ORI_AUTH__MIDDLEWARE__SCHEME` | str | (complex) | Token scheme | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthMiddle` |
| `ORI_AUTH__NAME` | str | "auth" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__NAME` | str | "auth" |  | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.name` |
| `ORI_AUTH__NAME` | str | "auth" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__OAUTH2_PROVIDERS` | dict[str, dict[str, str]] | (required) | OAuth2 configs | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__OAUTH2_PROVIDERS` | dict[str, dict[str, str]] | (required) | OAuth2 configs | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.oauth2_providers` |
| `ORI_AUTH__OAUTH2_PROVIDERS` | dict[str, dict[str, str]] | (required) | OAuth2 configs | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__PASSWORD__ARGON2_MEMORY_COST` | int | 65536 | Argon2id memory cost in KiB (OWASP floor is 19456) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__ARGON2_MEMORY_COST` | int | 65536 | Argon2id memory cost in KiB (OWASP floor is 19456) | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.argon2_memory_cost` |
| `ORI_AUTH__PASSWORD__ARGON2_MEMORY_COST` | int | 65536 | Argon2id memory cost in KiB (OWASP floor is 19456) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__ARGON2_PARALLELISM` | int | 4 | Argon2id parallelism | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__ARGON2_PARALLELISM` | int | 4 | Argon2id parallelism | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.argon2_parallelism` |
| `ORI_AUTH__PASSWORD__ARGON2_PARALLELISM` | int | 4 | Argon2id parallelism | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__ARGON2_TIME_COST` | int | 3 | Argon2id time cost | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__ARGON2_TIME_COST` | int | 3 | Argon2id time cost | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.argon2_time_cost` |
| `ORI_AUTH__PASSWORD__ARGON2_TIME_COST` | int | 3 | Argon2id time cost | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__BANNED_PATTERNS` | list[str] | (required) | Substrings that must not appear in the password (case-insensitive). Use to reject common passwords or the user's own nam | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__BANNED_PATTERNS` | list[str] | (required) | Substrings that must not appear in the password (case-insensitive). Use to reject common passwords or the user's own nam | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.banned_patterns` |
| `ORI_AUTH__PASSWORD__BANNED_PATTERNS` | list[str] | (required) | Substrings that must not appear in the password (case-insensitive). Use to reject common passwords or the user's own nam | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__BCRYPT_ROUNDS` | int | 12 | bcrypt cost factor for new hashes (minimum 12 in production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__BCRYPT_ROUNDS` | int | 12 | bcrypt cost factor for new hashes (minimum 12 in production) | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.bcrypt_rounds` |
| `ORI_AUTH__PASSWORD__BCRYPT_ROUNDS` | int | 12 | bcrypt cost factor for new hashes (minimum 12 in production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__MAX_LENGTH` | int | 128 | Maximum password length | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__MAX_LENGTH` | int | 128 | Maximum password length | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.max_length` |
| `ORI_AUTH__PASSWORD__MAX_LENGTH` | int | 128 | Maximum password length | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__MIN_LENGTH` | int | 12 | Minimum password length | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__MIN_LENGTH` | int | 12 | Minimum password length | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.min_length` |
| `ORI_AUTH__PASSWORD__MIN_LENGTH` | int | 12 | Minimum password length | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__REQUIRE_DIGITS` | bool | True | Require at least one digit | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__REQUIRE_DIGITS` | bool | True | Require at least one digit | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.require_digits` |
| `ORI_AUTH__PASSWORD__REQUIRE_DIGITS` | bool | True | Require at least one digit | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__REQUIRE_LOWERCASE` | bool | False | Require at least one lowercase letter | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__REQUIRE_LOWERCASE` | bool | False | Require at least one lowercase letter | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.require_lowercase` |
| `ORI_AUTH__PASSWORD__REQUIRE_LOWERCASE` | bool | False | Require at least one lowercase letter | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__REQUIRE_SPECIAL` | bool | False | Require at least one special character (non-alphanumeric) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__REQUIRE_SPECIAL` | bool | False | Require at least one special character (non-alphanumeric) | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.require_special` |
| `ORI_AUTH__PASSWORD__REQUIRE_SPECIAL` | bool | False | Require at least one special character (non-alphanumeric) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__PASSWORD__REQUIRE_UPPERCASE` | bool | True | Require at least one uppercase letter | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:Password` |
| `ORI_AUTH__PASSWORD__REQUIRE_UPPERCASE` | bool | True | Require at least one uppercase letter | `packages/oridecon-auth/src/oridecon/auth/config.py:PasswordConfig.password.require_uppercase` |
| `ORI_AUTH__PASSWORD__REQUIRE_UPPERCASE` | bool | True | Require at least one uppercase letter | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:PasswordCo` |
| `ORI_AUTH__RBAC__CACHE_PERMISSIONS` | bool | True | Cache resolved permissions | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConf` |
| `ORI_AUTH__RBAC__CACHE_PERMISSIONS` | bool | True | Cache resolved permissions | `packages/oridecon-auth/src/oridecon/auth/config.py:RBACConfig.rbac.cache_permissions` |
| `ORI_AUTH__RBAC__CACHE_PERMISSIONS` | bool | True | Cache resolved permissions | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConfig` |
| `ORI_AUTH__RBAC__DEFAULT_ROLE` | str | "viewer" | Default role for new users | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConf` |
| `ORI_AUTH__RBAC__DEFAULT_ROLE` | str | "viewer" | Default role for new users | `packages/oridecon-auth/src/oridecon/auth/config.py:RBACConfig.rbac.default_role` |
| `ORI_AUTH__RBAC__DEFAULT_ROLE` | str | "viewer" | Default role for new users | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConfig` |
| `ORI_AUTH__RBAC__ENABLED` | bool | True | Enable RBAC enforcement | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConf` |
| `ORI_AUTH__RBAC__ENABLED` | bool | True | Enable RBAC enforcement | `packages/oridecon-auth/src/oridecon/auth/config.py:RBACConfig.rbac.enabled` |
| `ORI_AUTH__RBAC__ENABLED` | bool | True | Enable RBAC enforcement | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConfig` |
| `ORI_AUTH__RBAC__PERMISSION_CACHE_TTL` | int | 300 | Permission cache TTL in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConf` |
| `ORI_AUTH__RBAC__PERMISSION_CACHE_TTL` | int | 300 | Permission cache TTL in seconds | `packages/oridecon-auth/src/oridecon/auth/config.py:RBACConfig.rbac.permission_cache_ttl` |
| `ORI_AUTH__RBAC__PERMISSION_CACHE_TTL` | int | 300 | Permission cache TTL in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConfig` |
| `ORI_AUTH__RBAC__SUPERUSER_BYPASS` | bool | True | Allow superuser role to bypass all checks | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConf` |
| `ORI_AUTH__RBAC__SUPERUSER_BYPASS` | bool | True | Allow superuser role to bypass all checks | `packages/oridecon-auth/src/oridecon/auth/config.py:RBACConfig.rbac.superuser_bypass` |
| `ORI_AUTH__RBAC__SUPERUSER_BYPASS` | bool | True | Allow superuser role to bypass all checks | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:RBACConfig` |
| `ORI_AUTH__RELAY_VERIFICATION` | bool | False | Enable binding ``RelayAuthVerifierProtocol`` for the relay gateway's inbound API-key authentication.  When ``False`` (de | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__RELAY_VERIFICATION` | bool | False | Enable binding ``RelayAuthVerifierProtocol`` for the relay gateway's inbound API-key authentication.  When ``False`` (de | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.relay_verification` |
| `ORI_AUTH__RELAY_VERIFICATION` | bool | False | Enable binding ``RelayAuthVerifierProtocol`` for the relay gateway's inbound API-key authentication.  When ``False`` (de | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__ROLES` | dict[str, AuthRoleConfig] | (required) | Role definitions | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__ROLES` | dict[str, AuthRoleConfig] | (required) | Role definitions | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.roles` |
| `ORI_AUTH__ROLES` | dict[str, AuthRoleConfig] | (required) | Role definitions | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__SECRET_KEY` | str | (required) | Secret key for signing | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__SECRET_KEY` | str | (required) | Secret key for signing | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.secret_key` |
| `ORI_AUTH__SECRET_KEY` | str | (required) | Secret key for signing | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_AUTH__TOKEN__ACCESS_TOKEN_EXPIRE` | Duration | Duration.minutes(...) | Access token expiry duration | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__ACCESS_TOKEN_EXPIRE` | Duration | Duration.minutes(...) | Access token expiry duration | `packages/oridecon-auth/src/oridecon/auth/config.py:JWTConfig.token.access_token_expire` |
| `ORI_AUTH__TOKEN__ACCESS_TOKEN_EXPIRE` | Duration | Duration.minutes(...) | Access token expiry duration | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__TOKEN__ALGORITHM` | str | (complex) | Algorithm | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__ALGORITHM` | str | (complex) | Algorithm | `packages/oridecon-auth/src/oridecon/auth/config.py:JWTConfig.token.algorithm` |
| `ORI_AUTH__TOKEN__ALGORITHM` | str | (complex) | Algorithm | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__TOKEN__ALLOW_UNVERIFIED_DEV` | bool | False | Allow unverified JWT decode when the secret is absent. ONLY effective in Environment.DEVELOPMENT. Silently overridden to | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__ALLOW_UNVERIFIED_DEV` | bool | False | Allow unverified JWT decode when the secret is absent. ONLY effective in Environment.DEVELOPMENT. Silently overridden to | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__TOKEN__ID_TOKEN_EXPIRE` | Duration | Duration.hours(...) | ID token expiry duration | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__ID_TOKEN_EXPIRE` | Duration | Duration.hours(...) | ID token expiry duration | `packages/oridecon-auth/src/oridecon/auth/config.py:JWTConfig.token.id_token_expire` |
| `ORI_AUTH__TOKEN__ID_TOKEN_EXPIRE` | Duration | Duration.hours(...) | ID token expiry duration | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__TOKEN__KEY_ROTATION_GRACE_PERIOD` | Duration | Duration.seconds(...) | Duration during which tokens signed by a rotated-out key remain accepted. Prevents immediate logout on key rotation. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__KEY_ROTATION_GRACE_PERIOD` | Duration | Duration.seconds(...) | Duration during which tokens signed by a rotated-out key remain accepted. Prevents immediate logout on key rotation. | `packages/oridecon-auth/src/oridecon/auth/config.py:JWTConfig.token.key_rotation_grace_period` |
| `ORI_AUTH__TOKEN__KEY_ROTATION_GRACE_PERIOD` | Duration | Duration.seconds(...) | Duration during which tokens signed by a rotated-out key remain accepted. Prevents immediate logout on key rotation. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__TOKEN__REFRESH_TOKEN_EXPIRE` | Duration | Duration.days(...) | Refresh token expiry duration | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__REFRESH_TOKEN_EXPIRE` | Duration | Duration.days(...) | Refresh token expiry duration | `packages/oridecon-auth/src/oridecon/auth/config.py:JWTConfig.token.refresh_token_expire` |
| `ORI_AUTH__TOKEN__REFRESH_TOKEN_EXPIRE` | Duration | Duration.days(...) | Refresh token expiry duration | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__TOKEN__REQUIRED_AUDIENCE` | str  \| None | None | Expected ``aud`` claim for every token verified by this service. When set, tokens whose audience does not match are reje | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__REQUIRED_AUDIENCE` | str  \| None | None | Expected ``aud`` claim for every token verified by this service. When set, tokens whose audience does not match are reje | `packages/oridecon-auth/src/oridecon/auth/config.py:JWTConfig.token.required_audience` |
| `ORI_AUTH__TOKEN__REQUIRED_AUDIENCE` | str  \| None | None | Expected ``aud`` claim for every token verified by this service. When set, tokens whose audience does not match are reje | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__TOKEN__SECRET_KEY` | SecretStr | Ellipsis | Secret key for signing tokens | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfi` |
| `ORI_AUTH__TOKEN__SECRET_KEY` | SecretStr | Ellipsis | Secret key for signing tokens | `packages/oridecon-auth/src/oridecon/auth/config.py:JWTConfig.token.secret_key` |
| `ORI_AUTH__TOKEN__SECRET_KEY` | SecretStr | Ellipsis | Secret key for signing tokens | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:JWTConfig.` |
| `ORI_AUTH__USERS` | list[AuthUserConfig] | (required) | Initial users | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConf` |
| `ORI_AUTH__USERS` | list[AuthUserConfig] | (required) | Initial users | `packages/oridecon-auth/src/oridecon/auth/config.py:AuthConfig.users` |
| `ORI_AUTH__USERS` | list[AuthUserConfig] | (required) | Initial users | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/auth/config.py:AuthConfig` |
| `ORI_CACHE__BACKENDS` | list[CacheBackendConfig] | (required) | Backend configs | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheConfig.backends` |
| `ORI_CACHE__DEBUG` | bool | (complex) | Debug mode | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheConfig.debug` |
| `ORI_CACHE__ENABLED` | bool | (complex) | Whether cache is enabled | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheConfig.enabled` |
| `ORI_CACHE__ENV` | str  \| None | None | Environment (development/staging/production) | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheConfig.env` |
| `ORI_CACHE__ENVIRONMENT` | str | (complex) | Environment | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheConfig.environment` |
| `ORI_CACHE__NAME` | str | (complex) | Provider name | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheConfig.name` |
| `ORI_CACHE__SERVICE__CIRCUIT_BREAKER_ENABLED` | bool | (complex) | Enable circuit breaker | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.circuit_breaker_enab` |
| `ORI_CACHE__SERVICE__CIRCUIT_BREAKER_THRESHOLD` | int | (complex) | Circuit breaker threshold | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.circuit_breaker_thre` |
| `ORI_CACHE__SERVICE__DEFAULT_BACKEND` | str  \| None | None | Default backend name | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.default_backend` |
| `ORI_CACHE__SERVICE__DEFAULT_SERIALIZER` | str | (complex) | Default serializer | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.default_serializer` |
| `ORI_CACHE__SERVICE__ENABLE_HEALTH_CHECKS` | bool | (complex) | Enable health checks | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.enable_health_checks` |
| `ORI_CACHE__SERVICE__ENABLE_METRICS` | bool | (complex) | Enable metrics | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.enable_metrics` |
| `ORI_CACHE__SERVICE__ENABLE_PROTECTION` | bool | (complex) | Enable stampede protection | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.enable_protection` |
| `ORI_CACHE__SERVICE__PROTECTION_LOCK_TTL` | int | (complex) | Protection lock TTL | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.protection_lock_ttl` |
| `ORI_CACHE__SERVICE__PROTECTION_MAX_WAIT` | float | (complex) | Max wait for locks | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.protection_max_wait` |
| `ORI_CACHE__SERVICE__PROTECTION_RETRY_INTERVAL` | float | (complex) | Lock retry interval | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheServiceConfig.service.protection_retry_int` |
| `ORI_CACHE__VERSION` | str | (complex) | Config version | `packages/oridecon-cache/src/oridecon/cache/config.py:CacheConfig.version` |
| `ORI_CLI__ALIAS_LIMIT__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:AliasLi` |
| `ORI_CLI__ALIAS_LIMIT__MAX_ALIASES` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:AliasLi` |
| `ORI_CLI__ALLOWED_HOSTS` | list[str] | (required) | Hostnames permitted to reach the application. Empty by default; must be configured before production deployment. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__ALLOW_UNAUTHENTICATED` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__ASYNC_PROCESSING` | bool | True | Process feedback handlers asynchronously in the background | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/feedback/config.py:Fee` |
| `ORI_CLI__AUDIT_HMAC_KEY` | str  \| None | None | HMAC key for audit checksum signing. Plain text or base64. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseCon` |
| `ORI_CLI__BACKEND` | str | (complex) | Graph store backend to use | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphConf` |
| `ORI_CLI__BACKEND` | str | (complex) | Vector store backend to use | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__BACKENDS` | list[CacheBackendConfig] | (required) | Backend configs | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheConf` |
| `ORI_CLI__BACKENDS` | list[NamedDatabaseConfig] | (required) | Multi-database backends list. When non-empty, drives multi-DB mode. The entry with primary=True (or the first entry) als | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseCon` |
| `ORI_CLI__BACKENDS` | list[NamedNoSQLConfig] | (required) | Named NoSQL backends for multi-store support. When non-empty, the provider registers each backend under Annotated[Docume | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:NoSQLConf` |
| `ORI_CLI__BACKENDS` | list[NamedStorageConfig] | (required) | Named storage backends for multi-store support. When non-empty, the provider registers each backend under Annotated[Blob | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__BACKENDS` | list[NamedTaskConfig] | (required) | Named task queue backends for multi-queue support. When non-empty, the provider registers each backend under Annotated[T | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskConfi` |
| `ORI_CLI__BACKENDS` | list[NamedVectorConfig] | (required) | Named vector store backends for multi-store support. When non-empty, the provider registers each backend under Annotated | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__BACKEND__AMQP_URL` | SecretStr | SecretStr(...) | AMQP connection URL (may contain credentials). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBacke` |
| `ORI_CLI__BACKEND__POSTGRES_DSN` | SecretStr  \| None | None | Postgres DSN (required when type="postgres"; may contain credentials). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBacke` |
| `ORI_CLI__BACKEND__QUEUE_NAME` | str | (complex) | Name of the task queue | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBacke` |
| `ORI_CLI__BACKEND__REDIS_URL` | SecretStr | SecretStr(...) | Redis connection URL (may contain credentials). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBacke` |
| `ORI_CLI__BACKEND__TYPE` | str | (complex) | Queue backend type | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskBacke` |
| `ORI_CLI__BACKEND__URL` | SecretStr | Ellipsis | Database connection URL (may contain credentials) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseBac` |
| `ORI_CLI__BATCH__ENABLED` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:BatchCo` |
| `ORI_CLI__BATCH__MAX_BATCH_SIZE` | int | 10 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:BatchCo` |
| `ORI_CLI__BULKHEAD__MAX_CONCURRENT` | int | 10 | Max concurrent requests | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bulk` |
| `ORI_CLI__BULKHEAD__NAME` | str | "" | Bulkhead name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bulk` |
| `ORI_CLI__BULKHEAD__QUEUE_SIZE` | int | 100 | Max queue size | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bulk` |
| `ORI_CLI__BULKHEAD__TIMEOUT` | float | 30.0 | Execution timeout | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Bulk` |
| `ORI_CLI__BULK_BATCH_SIZE` | int | (complex) | Batch size for bulk operations | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphConf` |
| `ORI_CLI__CACHE_TTL` | int | 3600 | Cache TTL in seconds (default: 1 hour) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__CACHE_TTL` | int | 86400 | Cache TTL in seconds (default: 24 hours) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__CACHE__DEFAULT_MAX_AGE` | Duration  \| int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:CacheCo` |
| `ORI_CLI__CACHE__DEFAULT_SCOPE` | CacheScope | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:CacheCo` |
| `ORI_CLI__CACHE__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:CacheCo` |
| `ORI_CLI__CACHE__VARY_HEADERS` | list[str] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:CacheCo` |
| `ORI_CLI__CHUNKING_STRATEGY` | str | "recursive" | Chunking strategy (recursive, semantic, token) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__CHUNK_OVERLAP` | int | 50 | Overlap between consecutive chunks | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__CHUNK_SIZE` | int | 512 | Text chunk size in tokens | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__CIRCUIT_BREAKER` | CircuitBreakerConfig | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Resi` |
| `ORI_CLI__CITATION_STYLE` | str | "inline" | Citation style (inline, footnote, numbered) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__CLIENT_STDIO_COMMAND` | list[str] | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__CLIENT_URL` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__COLLECTION_NAME` | str | "default" | Collection/index name for vector store | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__COLLECTION_NAME` | str | "default" | Default collection name for AI-layer operations | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__COMMAND_BUS__ENABLE_LOGGING` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:CommandB` |
| `ORI_CLI__COMMAND_BUS__ENABLE_METRICS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:CommandB` |
| `ORI_CLI__COMMAND_BUS__ENABLE_VALIDATION` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:CommandB` |
| `ORI_CLI__COMMAND_BUS__MAX_RETRIES` | int | 3 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:CommandB` |
| `ORI_CLI__COMMAND_BUS__RETRY_DELAY_SECONDS` | float | 1.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:CommandB` |
| `ORI_CLI__COMMAND_BUS__TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:CommandB` |
| `ORI_CLI__COMPLEXITY__DEFAULT_FIELD_COST` | float | 1.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Complex` |
| `ORI_CLI__COMPLEXITY__DEFAULT_LIST_COST` | float | 10.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Complex` |
| `ORI_CLI__COMPLEXITY__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Complex` |
| `ORI_CLI__COMPLEXITY__MAX_COMPLEXITY` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Complex` |
| `ORI_CLI__CONNECTORS__FILESYSTEM__READ_ONLY` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:Filesyst` |
| `ORI_CLI__CONNECTORS__FILESYSTEM__ROOT_DIR` | str | "" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:Filesyst` |
| `ORI_CLI__CONNECTORS__GITHUB__API_URL` | str | "https://api.github.com" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:GitHubCo` |
| `ORI_CLI__CONNECTORS__GITHUB__TOKEN` | str | "" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:GitHubCo` |
| `ORI_CLI__CONNECTORS__GOOGLE_DRIVE__IMPERSONATED_EMAIL` | str | "" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:GoogleDr` |
| `ORI_CLI__CONNECTORS__GOOGLE_DRIVE__SERVICE_ACCOUNT_JSON` | str | "" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:GoogleDr` |
| `ORI_CLI__CONNECTORS__SLACK__BOT_TOKEN` | str | "" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SlackCon` |
| `ORI_CLI__CONNECTORS__SLACK__MAX_MESSAGES` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SlackCon` |
| `ORI_CLI__CONNECTORS__SQL__ALLOWED_TABLES` | list[str] | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SQLConne` |
| `ORI_CLI__CONNECTORS__SQL__DSN` | str | "" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SQLConne` |
| `ORI_CLI__CONNECTORS__SQL__READ_ONLY` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:SQLConne` |
| `ORI_CLI__CONNECTORS__WEB_FETCH__ENABLED` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebFetch` |
| `ORI_CLI__CONNECTORS__WEB_FETCH__MAX_CONTENT_BYTES` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebFetch` |
| `ORI_CLI__CONNECTORS__WEB_FETCH__USER_AGENT` | str | "oridecon-mcp/1.0" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebFetch` |
| `ORI_CLI__CONNECTORS__WEB_SEARCH__API_KEY` | str | "" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebSearc` |
| `ORI_CLI__CONNECTORS__WEB_SEARCH__MAX_RESULTS` | int | 10 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebSearc` |
| `ORI_CLI__CONNECTORS__WEB_SEARCH__PROVIDER` | str | "brave" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:WebSearc` |
| `ORI_CLI__CORS_ORIGINS` | list[str] | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__CORS__ALLOWED_ORIGINS` | list[str] | (required) | Allowed origins (use ['*'] to allow all) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__ALLOW_CREDENTIALS` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__ALLOW_HEADERS` | list[str] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__ALLOW_METHODS` | list[str] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__ALLOW_ORIGIN_REGEX` | str  \| None | None | Regex pattern for allowed origins (matched when not in allowed_origins) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__DEBUG_PERMISSIVE` | bool | False | When True and debug mode is active, allow any origin via wildcard (explicit opt-in replacement for the old implicit debu | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__ENABLED` | bool | True | Enable CORS | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__EXPOSE_HEADERS` | list[str] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CORS__MAX_AGE` | int | 600 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CO` |
| `ORI_CLI__CROSS_ORIGIN__EMBEDDER_POLICY` | str | "require-corp" | Cross-Origin-Embedder-Policy header value | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Cr` |
| `ORI_CLI__CROSS_ORIGIN__ENABLED` | bool | False | Emit cross-origin isolation headers | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Cr` |
| `ORI_CLI__CROSS_ORIGIN__OPENER_POLICY` | str | "same-origin" | Cross-Origin-Opener-Policy header value | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Cr` |
| `ORI_CLI__CROSS_ORIGIN__RESOURCE_POLICY` | str | "same-origin" | Cross-Origin-Resource-Policy header value | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Cr` |
| `ORI_CLI__CSP__DIRECTIVES` | dict[str, Any] | (required) | CSP directives mapping directive name to source expression(s) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSP__ENABLED` | bool | True | Emit the Content-Security-Policy header | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__COOKIE_DOMAIN` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__COOKIE_HTTPONLY` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__COOKIE_NAME` | str | "csrf_token" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__COOKIE_PATH` | str | "/" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__COOKIE_SAMESITE` | str | "Lax" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__COOKIE_SECURE` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__ENABLED` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__EXCLUDED_PATHS` | list[str] | (required) | URL path prefixes exempt from CSRF validation for cookie-less requests; cookie-bearing requests on these paths are still | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__EXCLUDE_AUTH_SCHEMES` | list[str] | (required) | Authorization header schemes that bypass CSRF validation (explicit opt-in). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__EXCLUDE_CONTENT_TYPES` | list[str] | (required) | Content-Type values that bypass CSRF validation (explicit opt-in — JSON requests are validated by default so cookie-auth | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__HEADER_NAME` | str | "X-CSRF-Token" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__SECRET_KEY` | str  \| None | None | HMAC secret used to sign and verify CSRF tokens (populated via ORI_WEB__SECURITY__CSRF__SECRET_KEY) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__TOKEN_LENGTH` | int | 32 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CSRF__TOKEN_TTL` | int | 3600 | TTL in seconds for synchronizer-mode tokens stored in cache. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:CS` |
| `ORI_CLI__CUSTOM_HEADERS` | dict[str, str] | (required) | Additional HTTP response headers emitted verbatim | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__DATALOADER__BATCH_DELAY_MS` | float | 2.0 | Delay in milliseconds before executing a DataLoaderProtocol batch. A small non-zero value (2ms) lets more keys accumulat | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataLoa` |
| `ORI_CLI__DATALOADER__BATCH_ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataLoa` |
| `ORI_CLI__DATALOADER__CACHE_ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataLoa` |
| `ORI_CLI__DATALOADER__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataLoa` |
| `ORI_CLI__DATALOADER__MAX_BATCH_SIZE` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DataLoa` |
| `ORI_CLI__DEBUG` | bool | (complex) | Debug mode | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheConf` |
| `ORI_CLI__DEBUG` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventsCo` |
| `ORI_CLI__DEBUG` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__DEBUG` | bool | False | Enable debug mode | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monitor` |
| `ORI_CLI__DEFAULT_DIMENSION` | int | 1536 | Default vector dimension | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__DEFAULT_DISTANCE_METRIC` | DistanceMetric | (complex) | Default distance metric for new collections | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__DEFAULT_DRIVER` | Literal['local', 's3', 'gcs', 'azure', 'memory', 'r2'] | (complex) | Default storage driver to use | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__DEFAULT_INDEX_TYPE` | IndexType | (complex) | Default index type for new collections | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__DEFAULT_QUERY_LIMIT` | int | (complex) | Default limit for query results | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphConf` |
| `ORI_CLI__DEFAULT_TRAVERSAL_MAX_DEPTH` | int | (complex) | Default maximum depth for traversals | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphConf` |
| `ORI_CLI__DEPTH_LIMIT__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DepthLi` |
| `ORI_CLI__DEPTH_LIMIT__IGNORE_INTROSPECTION` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DepthLi` |
| `ORI_CLI__DEPTH_LIMIT__MAX_DEPTH` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:DepthLi` |
| `ORI_CLI__DRIVER` | str | "mongodb" | NoSQL driver name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:NoSQLConf` |
| `ORI_CLI__DRIVERS` | dict[str, StorageLocalConfig  \| StorageS3Config  \| StorageGCSConfig  \| Storag | (required) | Driver-specific configurations | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__EMBEDDING_MODEL` | str  \| None | None | Embedding model identifier. Must be set explicitly — no vendor-specific default. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__EMBEDDING_MODEL` | str | "text-embedding-3-small" | Embedding model name for AI-layer embedding generation | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__EMBEDDING_PROVIDER` | str | "openai" | Embedding provider (openai, cohere, etc.) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__ENABLED` | bool | True | Enable AI features | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.ena` |
| `ORI_CLI__ENABLED` | bool | (complex) | Whether cache is enabled | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheConf` |
| `ORI_CLI__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseCon` |
| `ORI_CLI__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventsCo` |
| `ORI_CLI__ENABLED` | bool | True | Master on/off switch for all feedback collection | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/feedback/config.py:Fee` |
| `ORI_CLI__ENABLED` | bool | True | Enable the graph store subsystem | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphConf` |
| `ORI_CLI__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__ENABLED` | bool | True | Enable the MCP server subsystem | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__ENABLED` | bool | True | Enable monitoring | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monitor` |
| `ORI_CLI__ENABLED` | bool | True | Enable NoSQL support | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:NoSQLConf` |
| `ORI_CLI__ENABLED` | bool | True | Master on/off switch for all observability | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config.p` |
| `ORI_CLI__ENABLED` | bool | True | Enable the RAG pipeline | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__ENABLED` | bool | True | Enable the security subsystem | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__ENABLED` | bool | True | Whether tasks module is enabled | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskConfi` |
| `ORI_CLI__ENABLED` | bool | True | Enable the vector store subsystem | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__ENABLE_ADMIN` | bool | True | Whether to register the AuditAdminContributor | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditConf` |
| `ORI_CLI__ENABLE_CACHE` | bool | False | Enable embedding caching (requires a CacheBackend binding) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__ENABLE_CACHING` | bool | True | Enable caching for RAG queries | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__ENABLE_CITATIONS` | bool | True | Include source citations in responses | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__ENABLE_CORS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__ENABLE_CSRF` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__ENABLE_HALLUCINATION_DETECTION` | bool | True | Enable hallucination detection for AI responses | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__ENABLE_HYDE` | bool | False | Enable HyDE (Hypothetical Document Embeddings) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__ENABLE_IDENTITY_RESOLUTION` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__ENABLE_QUERY_EXPANSION` | bool | True | Enable query expansion techniques | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__ENABLE_SSE` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheConf` |
| `ORI_CLI__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventsCo` |
| `ORI_CLI__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monitor` |
| `ORI_CLI__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskConfi` |
| `ORI_CLI__ENVIRONMENT` | str | (complex) | Environment | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheConf` |
| `ORI_CLI__ENVIRONMENT` | Environment | (complex) | Deployment environment | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monitor` |
| `ORI_CLI__ERRORS__DEBUG_MODE` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:ErrorCo` |
| `ORI_CLI__ERRORS__INCLUDE_STACKTRACE` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:ErrorCo` |
| `ORI_CLI__ERRORS__LOG_ERRORS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:ErrorCo` |
| `ORI_CLI__ERRORS__MASK_ERRORS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:ErrorCo` |
| `ORI_CLI__EVENT_BUS__ALLOW_NO_HANDLERS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__CONTINUE_ON_ERROR` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__ENABLE_DEAD_LETTER` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__HANDLER_TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__MAX_CONCURRENT_HANDLERS` | int | 10 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__MAX_HANDLER_RETRIES` | int | 3 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__MAX_QUEUE_PER_SUBSCRIBER` | int | 1000 | Maximum number of events queued per event type before backpressure is applied. 0 means unbounded (no backpressure). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__PARALLEL_DISPATCH` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_BUS__RETRY_FAILED_HANDLERS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventBus` |
| `ORI_CLI__EVENT_STORE_BACKEND` | EventStoreBackend | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventsCo` |
| `ORI_CLI__EXTRA` | dict[str, Any] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskConfi` |
| `ORI_CLI__FIRESTORE__CREDENTIALS_JSON` | str  \| None | None | Path to a service account JSON key file, or the raw JSON string. When ``None``, Application Default Credentials (ADC) ar | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:Firestore` |
| `ORI_CLI__FIRESTORE__DATABASE_ID` | str | "(default)" | Firestore database ID (use '(default)' for the default database) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:Firestore` |
| `ORI_CLI__FIRESTORE__PROJECT_ID` | str | Ellipsis | Google Cloud project ID | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:Firestore` |
| `ORI_CLI__GOVERNANCE` | Any | (required) | AI governance configuration | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.gov` |
| `ORI_CLI__HEADERS__CONTENT_TYPE_NOSNIFF` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEADERS__CSP` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEADERS__FRAME_OPTIONS` | str | "DENY" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEADERS__HSTS_INCLUDE_SUBDOMAINS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEADERS__HSTS_MAX_AGE` | int | 31536000 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEADERS__PERMISSIONS_POLICY` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEADERS__REFERRER_POLICY` | str | "strict-origin-when-cross-origin" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEADERS__XSS_PROTECTION` | str | "1; mode=block" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__HEALTH_CHECKS_ENABLED` | bool | True | Enable background health checking for AI components | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config.p` |
| `ORI_CLI__HEALTH_CHECK_TIMEOUT` | float | 5.0 | Timeout in seconds for the startup health check in StorageProvider.boot() | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__HEALTH__CHECKS` | list[str] | (required) | List of health check names to run | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:HealthC` |
| `ORI_CLI__HEALTH__ENABLED` | bool | True | Enable health checks | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:HealthC` |
| `ORI_CLI__HEALTH__INCLUDE_DETAILS` | bool | True | Include detailed health info in response | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:HealthC` |
| `ORI_CLI__HEALTH__INTERVAL` | int | (complex) | Health check interval in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:HealthC` |
| `ORI_CLI__HEALTH__PATH` | str | "/health" | Health endpoint path | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:HealthC` |
| `ORI_CLI__HEALTH__TIMEOUT` | float | 5.0 | Health check timeout in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:HealthC` |
| `ORI_CLI__HMAC_KEY` | bytes  \| None | None | HMAC key for checksum computation | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditConf` |
| `ORI_CLI__HOST` | str | "0.0.0.0" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__HSTS__ENABLED` | bool | False | Emit the Strict-Transport-Security header | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:HS` |
| `ORI_CLI__HSTS__INCLUDE_SUBDOMAINS` | bool | True | Apply HSTS to all subdomains | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:HS` |
| `ORI_CLI__HSTS__MAX_AGE` | int | 31536000 | HSTS max-age in seconds (default 1 year) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:HS` |
| `ORI_CLI__HSTS__PRELOAD` | bool | False | Include site in HSTS preload list | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:HS` |
| `ORI_CLI__INTEGRATION__CACHE_KEY_PREFIX` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Integra` |
| `ORI_CLI__INTEGRATION__SQL_CONTEXT_BRIDGE` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Integra` |
| `ORI_CLI__INTROSPECTION__ALLOWED_ENVIRONMENTS` | set[str] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Introsp` |
| `ORI_CLI__INTROSPECTION__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Introsp` |
| `ORI_CLI__KAFKA__AUTO_OFFSET_RESET` | str | "earliest" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaCon` |
| `ORI_CLI__KAFKA__BOOTSTRAP_SERVERS` | str | Ellipsis | Kafka bootstrap servers | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaCon` |
| `ORI_CLI__KAFKA__CONSUMER_GROUP` | str | "events-consumers" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaCon` |
| `ORI_CLI__KAFKA__ENABLE_AUTO_COMMIT` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaCon` |
| `ORI_CLI__KAFKA__TOPIC_PREFIX` | str | "events" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:KafkaCon` |
| `ORI_CLI__LIFECYCLE__AUTO_PROVISION_ISOLATION` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Lifecyc` |
| `ORI_CLI__LIFECYCLE__ISOLATION_STRATEGY` | str | "row_level" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Lifecyc` |
| `ORI_CLI__LLM` | Any  \| None | None | LLM configuration (optional) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.llm` |
| `ORI_CLI__LOGGING_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:LoggingM` |
| `ORI_CLI__LOGGING_MIDDLEWARE__INCLUDE_PAYLOAD` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:LoggingM` |
| `ORI_CLI__LOGGING_MIDDLEWARE__LOG_LEVEL` | str | "INFO" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:LoggingM` |
| `ORI_CLI__LOGGING_MIDDLEWARE__MAX_PAYLOAD_LENGTH` | int | 1000 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:LoggingM` |
| `ORI_CLI__LOGGING__ENABLED` | bool | True | Enable structured logging | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Logging` |
| `ORI_CLI__LOGGING__FORMAT` | str | "json" | Log format (json, text) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Logging` |
| `ORI_CLI__LOGGING__INCLUDE_TRACE_CONTEXT` | bool | True | Include trace context in logs | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Logging` |
| `ORI_CLI__LOGGING__LEVEL` | str | "INFO" | Default log level | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Logging` |
| `ORI_CLI__LOGGING__REDACT_FIELDS` | list[str] | (required) | Fields to redact from logs | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Logging` |
| `ORI_CLI__MAX_REQUEST_SIZE` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__MAX_RETRIES` | int | (complex) | Maximum number of retries for operations | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphConf` |
| `ORI_CLI__MAX_RETRIES` | int | (complex) | Maximum number of retries for operations | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__MEMORY__ENABLE_SNAPSHOTS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:InMemory` |
| `ORI_CLI__MEMORY__MAX_COLLECTIONS` | int | 100 | Maximum number of collections in memory | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:MemoryCo` |
| `ORI_CLI__MEMORY__MAX_EDGES` | int | (complex) | Maximum number of edges in memory | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:MemoryCon` |
| `ORI_CLI__MEMORY__MAX_EVENTS_PER_STREAM` | int | 10000 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:InMemory` |
| `ORI_CLI__MEMORY__MAX_NODES` | int | (complex) | Maximum number of nodes in memory | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:MemoryCon` |
| `ORI_CLI__MEMORY__MAX_VECTORS_PER_COLLECTION` | int | 100000 | Maximum number of vectors per collection | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:MemoryCo` |
| `ORI_CLI__METRICS_ENABLED` | bool | True | Enable metrics collection | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config.p` |
| `ORI_CLI__METRICS_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MetricsM` |
| `ORI_CLI__METRICS_MIDDLEWARE__HISTOGRAM_BUCKETS` | list[float] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MetricsM` |
| `ORI_CLI__METRICS_MIDDLEWARE__INCLUDE_HISTOGRAMS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MetricsM` |
| `ORI_CLI__METRICS_MIDDLEWARE__PREFIX` | str | "events" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MetricsM` |
| `ORI_CLI__METRICS__COLLECTION_INTERVAL` | float | 60.0 | Metrics collection interval in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metrics` |
| `ORI_CLI__METRICS__DEFAULT_LABELS` | dict[str, str] | (required) | Default labels for all metrics | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metrics` |
| `ORI_CLI__METRICS__ENABLED` | bool | True | Enable metrics collection | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metrics` |
| `ORI_CLI__METRICS__ENABLED` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metrics` |
| `ORI_CLI__METRICS__HISTOGRAM_BUCKETS` | list[float] | (required) | Default histogram bucket boundaries | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metrics` |
| `ORI_CLI__METRICS__HISTOGRAM_BUCKETS` | list[float] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metrics` |
| `ORI_CLI__METRICS__INCLUDE_LABELS` | list[str] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metrics` |
| `ORI_CLI__METRICS__NAMESPACE` | str | "oridecon_graphql" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Metrics` |
| `ORI_CLI__METRICS__PREFIX` | str | (complex) | MetricProtocol name prefix | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Metrics` |
| `ORI_CLI__MIGRATIONS__LOCK_TIMEOUT` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseMig` |
| `ORI_CLI__MIN_CITATION_CONFIDENCE` | float | 0.6 | Minimum confidence for citation inclusion | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__MONGODB__AUTH_SOURCE` | str | "admin" | Authentication database | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__CONNECTION_STRING` | SecretStr | Ellipsis | MongoDB connection string | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoDBE` |
| `ORI_CLI__MONGODB__CONNECT_TIMEOUT_MS` | int | 10000 | Connection timeout (ms) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__DATABASE` | str | "oridecon" | Database name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__DATABASE_NAME` | str | "events" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoDBE` |
| `ORI_CLI__MONGODB__EVENTS_COLLECTION` | str | "domain_events" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoDBE` |
| `ORI_CLI__MONGODB__MAX_POOL_SIZE` | int | 100 | Maximum connection pool size | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__MAX_POOL_SIZE` | int | 10 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoDBE` |
| `ORI_CLI__MONGODB__MIN_POOL_SIZE` | int | 10 | Minimum connection pool size | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__READ_PREFERENCE` | str | "primaryPreferred" | Read preference mode | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__RETRY_READS` | bool | True | Enable read retries | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__RETRY_WRITES` | bool | True | Enable write retries | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__SERVER_SELECTION_TIMEOUT` | int | 30000 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoDBE` |
| `ORI_CLI__MONGODB__SERVER_SELECTION_TIMEOUT_MS` | int | 5000 | Server selection timeout (ms) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__SNAPSHOTS_COLLECTION` | str | "snapshots" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:MongoDBE` |
| `ORI_CLI__MONGODB__SOCKET_TIMEOUT_MS` | int | 30000 | Socket timeout (ms) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__URI` | str | "mongodb://localhost:27017" | MongoDB connection URI | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__MONGODB__WRITE_CONCERN_W` | str  \| int | "majority" | Write concern level | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/nosql/config.py:MongoDBCo` |
| `ORI_CLI__NAME` | str | "ai" | Configuration name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.nam` |
| `ORI_CLI__NAME` | str | (complex) | Provider name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheConf` |
| `ORI_CLI__NAME` | str | "database" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseCon` |
| `ORI_CLI__NAME` | str | "events" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventsCo` |
| `ORI_CLI__NAME` | str | "graphql" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__NAME` | str | (complex) | Provider name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Monitor` |
| `ORI_CLI__NAME` | str | "storage" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__NAME` | str | "tasks" | Configuration name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskConfi` |
| `ORI_CLI__NEO4J__CONNECTION_TIMEOUT` | float | (complex) | Connection timeout in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__DATABASE` | str | (complex) | Target database name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__ENCRYPTED` | bool | False | Whether to use SSL/TLS encryption | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__FETCH_SIZE` | int | (complex) | Default fetch size for results | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__MAX_CONNECTION_POOL_SIZE` | int | (complex) | Maximum number of connections in the pool | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__MAX_TRANSACTION_RETRY_TIME` | float | 30.0 | Maximum time for transaction retries | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__PASSWORD` | SecretStr | (required) | Neo4j password | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__TRUST` | str | "TRUST_SYSTEM_CA_SIGNED_CERTIFICATES" | Trust strategy for SSL | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__URI` | str | "bolt://localhost:7687" | Neo4j BOLT URI | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__NEO4J__USERNAME` | str | "neo4j" | Neo4j username | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:Neo4jConf` |
| `ORI_CLI__OBSERVABILITY` | Any | (required) | AI observability configuration (tracing and metrics) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.obs` |
| `ORI_CLI__OPENTELEMETRY__BATCH_SIZE` | int | 512 | Export batch size | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__COMPRESSION` | str | "none" | Compression type (none, gzip) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__ENDPOINT` | str  \| None | None | OTLP endpoint URL | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__EXPORT_INTERVAL` | float | 5.0 | Export interval seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__HEADERS` | dict[str, str] | (required) | OTLP request headers | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__INSECURE` | bool | False | Use insecure connection | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__METRICS_EXPORTERS` | list[OTelExporterConfig] | (required) | List of metrics exporters to build. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__TIMEOUT` | float | 30.0 | Export timeout seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPENTELEMETRY__TRACING_EXPORTERS` | list[OTelExporterConfig] | (required) | List of tracing exporters to build. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:OpenTel` |
| `ORI_CLI__OPERATIONS__ECHO` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseOpe` |
| `ORI_CLI__OPERATIONS__STATEMENT_TIMEOUT` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseOpe` |
| `ORI_CLI__OUTBOX__BATCH_MAX_AGE` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseOut` |
| `ORI_CLI__OUTBOX__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseOut` |
| `ORI_CLI__OUTBOX__POLL_INTERVAL` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabaseOut` |
| `ORI_CLI__OVERRIDES__CACHE_TTL` | int | DEFAULT_CONFIG_CACHE_TTL |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:ConfigO` |
| `ORI_CLI__PATH` | str | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__PATH` | str | "/mcp" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__PERMISSIONS_POLICY` | dict[str, str] | (required) | Permissions-Policy directive map | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__PERSISTED_QUERIES__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Persist` |
| `ORI_CLI__PERSISTED_QUERIES__STORE_TYPE` | str | "memory" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Persist` |
| `ORI_CLI__PERSISTED_QUERIES__TTL_SECONDS` | Duration  \| int | 86400 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Persist` |
| `ORI_CLI__PERSIST_DIRECTORY` | str  \| None | None | Local directory path for vector store persistence (e.g. Chroma) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__PGVECTOR__CREATE_EXTENSION` | bool | True | Whether to create pgvector extension if missing | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVector` |
| `ORI_CLI__PGVECTOR__DATABASE` | str | "primary" | Name of the database backend from db.backends to use for pgvector. Matches a 'name:' entry in the db.backends list. Defa | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVector` |
| `ORI_CLI__PGVECTOR__DEFAULT_EF_SEARCH` | int | (complex) | Default ef_search for HNSW index | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVector` |
| `ORI_CLI__PGVECTOR__DEFAULT_LISTS` | int | (complex) | Default number of lists for IVFFlat index | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVector` |
| `ORI_CLI__PGVECTOR__DEFAULT_PROBES` | int | (complex) | Default number of probes for IVFFlat index | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVector` |
| `ORI_CLI__PGVECTOR__SCHEMA` | str | "public" | Database schema for vector tables | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVector` |
| `ORI_CLI__PGVECTOR__TABLE_PREFIX` | str | "vec_" | Prefix for vector storage tables | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:PgVector` |
| `ORI_CLI__PINECONE__API_KEY` | SecretStr | SecretStr(...) | Pinecone API key | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pinecone` |
| `ORI_CLI__PINECONE__ENVIRONMENT` | str | "" | Pinecone environment (e.g. 'us-west1-gcp') | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pinecone` |
| `ORI_CLI__PINECONE__INDEX_NAME` | str | "" | Name of the Pinecone index | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pinecone` |
| `ORI_CLI__PINECONE__NAMESPACE` | str | "" | Default namespace for the index | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pinecone` |
| `ORI_CLI__PINECONE__POOL_THREADS` | int | 4 | Number of threads for the connection pool | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pinecone` |
| `ORI_CLI__PINECONE__TIMEOUT` | float | (complex) | Request timeout in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Pinecone` |
| `ORI_CLI__PLAYGROUND__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Playgro` |
| `ORI_CLI__PLAYGROUND__PATH` | str | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Playgro` |
| `ORI_CLI__PLAYGROUND__TITLE` | str | "Oridecon GraphQL Playground" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Playgro` |
| `ORI_CLI__POOL__ACQUIRE_TIMEOUT` | Duration | Duration.seconds(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__POOL__IDLE_TIMEOUT` | Duration | Duration.minutes(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__POOL__MAX_LIFETIME` | Duration | Duration.hours(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__POOL__MAX_OVERFLOW` | int | 5 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__POOL__MAX_SIZE` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__POOL__MIN_SIZE` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__POOL__RECYCLE` | int | 3600 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__POOL__TIMEOUT` | float | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/sql/config.py:DatabasePoo` |
| `ORI_CLI__PORT` | int | 8080 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__POSTGRES` | PostgresEventStoreConfig  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventsCo` |
| `ORI_CLI__PROJECTION__BATCH_SIZE` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projecti` |
| `ORI_CLI__PROJECTION__CHECKPOINT_INTERVAL` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projecti` |
| `ORI_CLI__PROJECTION__ENABLE_PARALLEL_PROJECTIONS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projecti` |
| `ORI_CLI__PROJECTION__MAX_CATCH_UP_EVENTS` | int | 10000 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projecti` |
| `ORI_CLI__PROJECTION__REBUILD_BATCH_SIZE` | int | 1000 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Projecti` |
| `ORI_CLI__PROMETHEUS__ENABLE_DEFAULT_METRICS` | bool | True | Enable default process metrics | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prometh` |
| `ORI_CLI__PROMETHEUS__METRICS_TABLE` | str | "metrics_samples" | Table name for metrics samples | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prometh` |
| `ORI_CLI__PROMETHEUS__PATH` | str | "/metrics" | Metrics endpoint path | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prometh` |
| `ORI_CLI__PROMETHEUS__PORT` | int | (complex) | Metrics server port | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prometh` |
| `ORI_CLI__PROMETHEUS__PUSHGATEWAY_URL` | str  \| None | None | Pushgateway URL for push-based metrics | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prometh` |
| `ORI_CLI__PROMETHEUS__PUSH_INTERVAL` | float | 10.0 | Push interval for Pushgateway | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prometh` |
| `ORI_CLI__PROMETHEUS__STORE_IN_DB` | bool | False | Persist metrics observations to DB | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Prometh` |
| `ORI_CLI__PUSH_BACKENDS` | list[NamedPushConfig] | (required) | Named push notification backends for multi-backend support. When non-empty, the provider registers each backend under An | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:No` |
| `ORI_CLI__QDRANT__API_KEY` | SecretStr  \| None | None | Qdrant API key | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:QdrantCo` |
| `ORI_CLI__QDRANT__GRPC_PORT` | int | 6334 | gRPC port for Qdrant | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:QdrantCo` |
| `ORI_CLI__QDRANT__PREFER_GRPC` | bool | True | Whether to prefer gRPC over HTTP | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:QdrantCo` |
| `ORI_CLI__QDRANT__TIMEOUT` | float | (complex) | Request timeout in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:QdrantCo` |
| `ORI_CLI__QDRANT__URL` | str | "http://localhost:6333" | Qdrant server URL | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:QdrantCo` |
| `ORI_CLI__QUERY_BUS__ENABLE_LOGGING` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:QueryBus` |
| `ORI_CLI__QUERY_BUS__ENABLE_METRICS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:QueryBus` |
| `ORI_CLI__QUERY_BUS__TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:QueryBus` |
| `ORI_CLI__RABBITMQ__DURABLE` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RabbitMQ` |
| `ORI_CLI__RABBITMQ__EXCHANGE_NAME` | str | "events" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RabbitMQ` |
| `ORI_CLI__RABBITMQ__PREFETCH_COUNT` | int | 10 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RabbitMQ` |
| `ORI_CLI__RABBITMQ__QUEUE_PREFIX` | str | "events" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RabbitMQ` |
| `ORI_CLI__RABBITMQ__URL` | SecretStr | Ellipsis | AMQP connection URL | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RabbitMQ` |
| `ORI_CLI__RAG` | Any  \| None | None | RAG pipeline configuration (optional) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.rag` |
| `ORI_CLI__RATE_LIMIT` | RateLimitConfig | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__RATE_LIMIT__BURST` | int  \| None | None | Maximum burst size | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRateL` |
| `ORI_CLI__RATE_LIMIT__ENABLED` | bool | False | Whether rate limiting is enabled | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRateL` |
| `ORI_CLI__RATE_LIMIT__PER` | float | 1.0 | Time period in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRateL` |
| `ORI_CLI__RATE_LIMIT__RATE` | int | 100 | Number of tasks allowed per time period | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskRateL` |
| `ORI_CLI__REFERRER_POLICY` | str | "strict-origin-when-cross-origin" | Referrer-Policy header value | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/security/config.py:Se` |
| `ORI_CLI__REQUEST_TIMEOUT` | float | 30.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__RESOLUTION__HEADER_NAME` | str | DEFAULT_HEADER_NAME |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RESOLUTION__JWT_CLAIM_KEY` | str | DEFAULT_JWT_CLAIM_KEY |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RESOLUTION__PATH_PATTERN` | str  \| None | DEFAULT_PATH_PATTERN |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RESOLUTION__RESOLVERS` | list[str] | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RESOLUTION__STRICT_MEMBERSHIP` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RESOLUTION__SUBDOMAIN_PATTERN` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RESOLUTION__TRUSTED_RESOLVERS` | list[str] | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RESOLUTION__VALIDATOR_CACHE_TTL` | int | DEFAULT_VALIDATOR_CACHE_TTL |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tenancy/config.py:Resolut` |
| `ORI_CLI__RETENTION_POLICY` | RetentionPolicy | (required) | Retention rules | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditConf` |
| `ORI_CLI__RETRY` | RetryConfig | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Resi` |
| `ORI_CLI__RETRY` | RetryConfig | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskConfi` |
| `ORI_CLI__RETRY_DELAY` | float | (complex) | Delay between retries in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphConf` |
| `ORI_CLI__RETRY_DELAY` | float | (complex) | Delay between retries in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__RETRY_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryMid` |
| `ORI_CLI__RETRY_MIDDLEWARE__EXPONENTIAL_BASE` | float | 2.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryMid` |
| `ORI_CLI__RETRY_MIDDLEWARE__INITIAL_DELAY_SECONDS` | float | 0.1 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryMid` |
| `ORI_CLI__RETRY_MIDDLEWARE__MAX_DELAY_SECONDS` | float | 10.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryMid` |
| `ORI_CLI__RETRY_MIDDLEWARE__MAX_RETRIES` | int | 3 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:RetryMid` |
| `ORI_CLI__SAGA__CLEANUP_COMPLETED_AFTER_HOURS` | int | 24 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaConf` |
| `ORI_CLI__SAGA__DEFAULT_TIMEOUT_SECONDS` | float | 300.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaConf` |
| `ORI_CLI__SAGA__ENABLE_COMPENSATION` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaConf` |
| `ORI_CLI__SAGA__MAX_RETRIES_PER_STEP` | int | 3 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaConf` |
| `ORI_CLI__SAGA__PERSIST_STATE` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaConf` |
| `ORI_CLI__SAGA__RETRY_DELAY_SECONDS` | float | 1.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SagaConf` |
| `ORI_CLI__SCHEDULER__CHECK_INTERVAL` | float | (complex) | Interval between schedule checks (seconds) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskSched` |
| `ORI_CLI__SCHEDULER__ENABLED` | bool | True | Whether scheduling is enabled | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskSched` |
| `ORI_CLI__SCHEDULER__TIMEZONE` | str | (complex) | Timezone for cron expressions | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskSched` |
| `ORI_CLI__SCHEMA_BASELINE_PATH` | str  \| None | None | Path to a GraphQL SDL (.graphql) file containing the baseline schema. When set, GraphQLProvider.boot() compares the curr | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:GraphQL` |
| `ORI_CLI__SERVER_NAME` | str | "oridecon-mcp" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__SERVER_VERSION` | str | "1.0.0" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__SERVICE__ALLOWED_MIME_TYPES` | list[str] | (required) | Allowed MIME types for upload validation. Defaults to a safe set of common image types: ['image/jpeg', 'image/png', 'ima | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__SERVICE__CIRCUIT_BREAKER_ENABLED` | bool | (complex) | Enable circuit breaker | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__CIRCUIT_BREAKER_THRESHOLD` | int | (complex) | Circuit breaker threshold | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__DEFAULT_BACKEND` | str  \| None | None | Default backend name | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__DEFAULT_SERIALIZER` | str | (complex) | Default serializer | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__ENABLE_HEALTH_CHECKS` | bool | (complex) | Enable health checks | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__ENABLE_METRICS` | bool | (complex) | Enable metrics | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__ENABLE_PROTECTION` | bool | (complex) | Enable stampede protection | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__MAX_FILE_SIZE_MB` | int | (complex) | Maximum file size in MB | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/storage/config.py:Storage` |
| `ORI_CLI__SERVICE__PROTECTION_LOCK_TTL` | int | (complex) | Protection lock TTL | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__PROTECTION_MAX_WAIT` | float | (complex) | Max wait for locks | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SERVICE__PROTECTION_RETRY_INTERVAL` | float | (complex) | Lock retry interval | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheServ` |
| `ORI_CLI__SIMILARITY_THRESHOLD` | float | 0.7 | Minimum similarity score threshold | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__SLO__ALERT_CHANNELS` | list[str] | (required) | Alert channel names for SLO violation dispatch | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOConf` |
| `ORI_CLI__SLO__ENABLED` | bool | True | Enable periodic SLO evaluation worker | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOConf` |
| `ORI_CLI__SLO__EVALUATION_INTERVAL` | float | 60.0 | SLO evaluation interval in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOConf` |
| `ORI_CLI__SLO__SUPPRESSION_WINDOW_SECONDS` | int | 300 | Alert suppression window in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:SLOConf` |
| `ORI_CLI__SMS_BACKENDS` | list[NamedSMSConfig] | (required) | Named SMS backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[SMSCha | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:No` |
| `ORI_CLI__SNAPSHOTS__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapshot` |
| `ORI_CLI__SNAPSHOTS__EVENT_COUNT_THRESHOLD` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapshot` |
| `ORI_CLI__SNAPSHOTS__MAX_SNAPSHOTS_PER_AGGREGATE` | int | 5 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapshot` |
| `ORI_CLI__SNAPSHOTS__STRATEGY` | SnapshotStrategy | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapshot` |
| `ORI_CLI__SNAPSHOTS__TIME_THRESHOLD_SECONDS` | int | 3600 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Snapshot` |
| `ORI_CLI__SQLITE__DATABASE` | str | "./events.db" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SqliteCo` |
| `ORI_CLI__SQLITE__JOURNAL_MODE` | str | "WAL" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SqliteCo` |
| `ORI_CLI__SQLITE__PRAGMAS` | dict[str, str] | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SqliteCo` |
| `ORI_CLI__SQLITE__WAL_MODE` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:SqliteCo` |
| `ORI_CLI__STDIO_MODE` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/mcp/config.py:MCPConfi` |
| `ORI_CLI__STORE_BACKEND` | str | (complex) | Backend type — 'sql' or 'memory' | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditConf` |
| `ORI_CLI__STORE_RAW_PAYLOADS` | bool | False | Persist raw incoming feedback payloads for auditing | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/feedback/config.py:Fee` |
| `ORI_CLI__STREAMING__BATCH_SIZE` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Streamin` |
| `ORI_CLI__STREAMING__BUFFER_SIZE` | int | 1000 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Streamin` |
| `ORI_CLI__STREAMING__ENABLE_WEBSOCKET` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Streamin` |
| `ORI_CLI__STREAMING__MAX_SUBSCRIBERS` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Streamin` |
| `ORI_CLI__STREAMING__POLL_INTERVAL_MS` | int | 100 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Streamin` |
| `ORI_CLI__STREAMING__WEBSOCKET_PING_INTERVAL` | int | 30 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Streamin` |
| `ORI_CLI__SUBSCRIPTIONS__CONNECTION_TIMEOUT` | Duration  \| int | 60 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subscri` |
| `ORI_CLI__SUBSCRIPTIONS__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subscri` |
| `ORI_CLI__SUBSCRIPTIONS__KEEPALIVE_INTERVAL` | Duration  \| int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subscri` |
| `ORI_CLI__SUBSCRIPTIONS__PATH` | str | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subscri` |
| `ORI_CLI__SUBSCRIPTIONS__PROTOCOL` | SubscriptionProtocol | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Subscri` |
| `ORI_CLI__SUBSYSTEMS` | dict[str, dict[str, Any]] | (required) | Dynamic configuration for third-party AI subsystems discovered via entry points.  Keys are subsystem names; values are t | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.sub` |
| `ORI_CLI__SYNTHESIS_STRATEGY` | str | "hybrid" | Synthesis strategy (direct, extractive, abstractive, hybrid) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__TABLE_NAME` | str | (complex) | SQL table name for the unified audit store | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditConf` |
| `ORI_CLI__TENANCY__ENABLED` | bool | False | Enable tenant-aware graph resolution | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphTena` |
| `ORI_CLI__TENANCY__ENABLED` | bool | False | Enable tenant-aware collection resolution in RAG pipeline | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGTenan` |
| `ORI_CLI__TENANCY__ENABLED` | bool | False | Enable tenant-aware collection name resolution | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorTe` |
| `ORI_CLI__TENANCY__RESOLVER_KIND` | str | "templated" | Which ``TenantCollectionResolver`` to use. One of ``"templated"`` or ``"pinecone_namespace"``. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorTe` |
| `ORI_CLI__TENANCY__STRATEGY` | str | "node_property" | Which tenancy strategy to use. One of ``"node_property"`` or ``"graph_per_tenant"``. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphTena` |
| `ORI_CLI__TENANCY__TEMPLATE` | str | "{logical}_t_{tenant}" | Collection name template for ``GRAPH_PER_TENANT`` strategy. Supports ``{logical}`` and ``{tenant}`` placeholders. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graph/config.py:GraphTena` |
| `ORI_CLI__TIMEOUT` | TimeoutConfig | field(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Resi` |
| `ORI_CLI__TIMEOUT__DEFAULT_TIMEOUT` | float | (complex) | Default timeout | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskTimeo` |
| `ORI_CLI__TIMEOUT__ENFORCE_TIMEOUT` | bool | True | Enforce timeouts | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskTimeo` |
| `ORI_CLI__TIMEOUT__MAX_TIMEOUT` | float | (complex) | Maximum allowed timeout | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskTimeo` |
| `ORI_CLI__TOP_K` | int | 5 | Number of documents to retrieve | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__TRACE_MAX_ATTRIBUTE_LENGTH` | int | 0 | Cap on string attribute values written to trace spans, in characters. 0 disables the cap. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config.p` |
| `ORI_CLI__TRACE_REDACTION_ENABLED` | bool | False | Redact secret-shaped keys (e.g. token, password, api_key) from trace span attributes and audit metadata. Strongly recomm | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config.p` |
| `ORI_CLI__TRACING_ENABLED` | bool | True | Enable distributed tracing | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/observability/config.p` |
| `ORI_CLI__TRACING__ENABLED` | bool | True | Enable tracing | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__ENABLED` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Tracing` |
| `ORI_CLI__TRACING__MAX_ATTRIBUTES` | int | 128 | Max attributes per span | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__MAX_EVENTS` | int | 128 | Max events per span | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__MAX_LINKS` | int | 128 | Max links per span | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__MAX_SPANS` | int | (complex) | Max number of spans to keep in memory | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__MAX_TRACES_PER_SECOND` | int | 100 | Max traces to sample per second | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__PROPAGATION_FORMATS` | list[str] | (required) | Propagation format list | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__SAMPLE_RATE` | float | 1.0 | Sample rate (0.0 to 1.0) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__SAMPLE_RATE` | float | 1.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Tracing` |
| `ORI_CLI__TRACING__SERVICE_NAME` | str | (complex) | Service name for traces | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/monitor/config.py:Tracing` |
| `ORI_CLI__TRACING__SERVICE_NAME` | str | "oridecon-graphql" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Tracing` |
| `ORI_CLI__TRACING__TRACE_DATALOADERS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Tracing` |
| `ORI_CLI__TRACING__TRACE_RESOLVERS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/graphql/config.py:Tracing` |
| `ORI_CLI__TRANSACTION_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Transact` |
| `ORI_CLI__TRANSACTION_MIDDLEWARE__ISOLATION_LEVEL` | str | "READ_COMMITTED" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Transact` |
| `ORI_CLI__TRANSACTION_MIDDLEWARE__TIMEOUT_SECONDS` | float | 30.0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Transact` |
| `ORI_CLI__UPSERT_BATCH_SIZE` | int | (complex) | Number of vectors per upsert batch | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:VectorCo` |
| `ORI_CLI__USE_HYBRID_SEARCH` | bool | True | Enable hybrid search (semantic + keyword) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__VALIDATION_MIDDLEWARE__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Validati` |
| `ORI_CLI__VALIDATION_MIDDLEWARE__STRICT_MODE` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:Validati` |
| `ORI_CLI__VECTOR` | Any  \| None | None | Vector store configuration | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/config.py:AIConfig.vec` |
| `ORI_CLI__VECTOR_DIMENSION` | int | 1536 | Embedding vector dimension (1536 for OpenAI ada-002) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__VECTOR_STORE_TYPE` | str | "pgvector" | Vector store backend (pgvector, chroma, qdrant, mock) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/ai/rag/config.py:RAGConfi` |
| `ORI_CLI__VERIFICATION_BATCH_SIZE` | int | (complex) | Entries to verify per verification run | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditConf` |
| `ORI_CLI__VERIFICATION_SCHEDULE` | str | (complex) | Cron expression for scheduled verification | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/audit/config.py:AuditConf` |
| `ORI_CLI__VERSION` | str | (complex) | Config version | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/cache/config.py:CacheConf` |
| `ORI_CLI__VERSION_SKEW_ALERTS_ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/events/config.py:EventsCo` |
| `ORI_CLI__WEAVIATE__API_KEY` | SecretStr  \| None | None | Weaviate API key for authenticated clusters | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weaviate` |
| `ORI_CLI__WEAVIATE__GRPC_PORT` | int | 50051 | gRPC port for the Weaviate cluster | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weaviate` |
| `ORI_CLI__WEAVIATE__TIMEOUT` | float | (complex) | Request timeout in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weaviate` |
| `ORI_CLI__WEAVIATE__URL` | str | "http://localhost:8080" | Weaviate cluster URL (HTTP) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/config.py:Weaviate` |
| `ORI_CLI__WORKER__DEFAULT_TIMEOUT` | float | (complex) | Default timeout for tasks without an explicit timeout (seconds) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWorke` |
| `ORI_CLI__WORKER__ENFORCE_TIMEOUT` | bool | True | Whether to enforce timeouts on all tasks | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWorke` |
| `ORI_CLI__WORKER__MAX_CONCURRENT_TASKS` | int | (complex) | Maximum concurrent tasks per worker | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWorke` |
| `ORI_CLI__WORKER__MAX_TIMEOUT` | float | (complex) | Maximum allowed timeout for any task (seconds) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWorke` |
| `ORI_CLI__WORKER__POLL_INTERVAL` | float | (complex) | Interval between queue polls (seconds) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWorke` |
| `ORI_CLI__WORKER__SHUTDOWN_TIMEOUT` | float | (complex) | Timeout for graceful shutdown (seconds) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWorke` |
| `ORI_CLI__WORKER__WORKER_COUNT` | int | (complex) | Number of worker instances | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/tasks/config.py:TaskWorke` |
| `ORI_EVENTS__COMMAND_BUS__ENABLE_LOGGING` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:CommandBusConfig.command_bus.enable_logging` |
| `ORI_EVENTS__COMMAND_BUS__ENABLE_METRICS` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:CommandBusConfig.command_bus.enable_metrics` |
| `ORI_EVENTS__COMMAND_BUS__ENABLE_VALIDATION` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:CommandBusConfig.command_bus.enable_validatio` |
| `ORI_EVENTS__COMMAND_BUS__MAX_RETRIES` | int | 3 |  | `packages/oridecon-events/src/oridecon/events/config.py:CommandBusConfig.command_bus.max_retries` |
| `ORI_EVENTS__COMMAND_BUS__RETRY_DELAY_SECONDS` | float | 1.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:CommandBusConfig.command_bus.retry_delay_seco` |
| `ORI_EVENTS__COMMAND_BUS__TIMEOUT_SECONDS` | float | 30.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:CommandBusConfig.command_bus.timeout_seconds` |
| `ORI_EVENTS__DEBUG` | bool | False |  | `packages/oridecon-events/src/oridecon/events/config.py:EventsConfig.debug` |
| `ORI_EVENTS__ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:EventsConfig.enabled` |
| `ORI_EVENTS__ENV` | str  \| None | None | Environment (development/staging/production) | `packages/oridecon-events/src/oridecon/events/config.py:EventsConfig.env` |
| `ORI_EVENTS__EVENT_BUS__ALLOW_NO_HANDLERS` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.allow_no_handlers` |
| `ORI_EVENTS__EVENT_BUS__CONTINUE_ON_ERROR` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.continue_on_error` |
| `ORI_EVENTS__EVENT_BUS__ENABLE_DEAD_LETTER` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.enable_dead_letter` |
| `ORI_EVENTS__EVENT_BUS__HANDLER_TIMEOUT_SECONDS` | float | 30.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.handler_timeout_seco` |
| `ORI_EVENTS__EVENT_BUS__MAX_CONCURRENT_HANDLERS` | int | 10 |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.max_concurrent_handl` |
| `ORI_EVENTS__EVENT_BUS__MAX_HANDLER_RETRIES` | int | 3 |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.max_handler_retries` |
| `ORI_EVENTS__EVENT_BUS__MAX_QUEUE_PER_SUBSCRIBER` | int | 1000 | Maximum number of events queued per event type before backpressure is applied. 0 means unbounded (no backpressure). | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.max_queue_per_subscr` |
| `ORI_EVENTS__EVENT_BUS__PARALLEL_DISPATCH` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.parallel_dispatch` |
| `ORI_EVENTS__EVENT_BUS__RETRY_FAILED_HANDLERS` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:EventBusConfig.event_bus.retry_failed_handler` |
| `ORI_EVENTS__EVENT_STORE_BACKEND` | EventStoreBackend | (complex) |  | `packages/oridecon-events/src/oridecon/events/config.py:EventsConfig.event_store_backend` |
| `ORI_EVENTS__KAFKA__AUTO_OFFSET_RESET` | str | "earliest" |  | `packages/oridecon-events/src/oridecon/events/config.py:KafkaConfig.kafka.auto_offset_reset` |
| `ORI_EVENTS__KAFKA__BOOTSTRAP_SERVERS` | str | Ellipsis | Kafka bootstrap servers | `packages/oridecon-events/src/oridecon/events/config.py:KafkaConfig.kafka.bootstrap_servers` |
| `ORI_EVENTS__KAFKA__CONSUMER_GROUP` | str | "events-consumers" |  | `packages/oridecon-events/src/oridecon/events/config.py:KafkaConfig.kafka.consumer_group` |
| `ORI_EVENTS__KAFKA__ENABLE_AUTO_COMMIT` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:KafkaConfig.kafka.enable_auto_commit` |
| `ORI_EVENTS__KAFKA__TOPIC_PREFIX` | str | "events" |  | `packages/oridecon-events/src/oridecon/events/config.py:KafkaConfig.kafka.topic_prefix` |
| `ORI_EVENTS__LOGGING_MIDDLEWARE__ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:LoggingMiddlewareConfig.logging_middleware.en` |
| `ORI_EVENTS__LOGGING_MIDDLEWARE__INCLUDE_PAYLOAD` | bool | False |  | `packages/oridecon-events/src/oridecon/events/config.py:LoggingMiddlewareConfig.logging_middleware.in` |
| `ORI_EVENTS__LOGGING_MIDDLEWARE__LOG_LEVEL` | str | "INFO" |  | `packages/oridecon-events/src/oridecon/events/config.py:LoggingMiddlewareConfig.logging_middleware.lo` |
| `ORI_EVENTS__LOGGING_MIDDLEWARE__MAX_PAYLOAD_LENGTH` | int | 1000 |  | `packages/oridecon-events/src/oridecon/events/config.py:LoggingMiddlewareConfig.logging_middleware.ma` |
| `ORI_EVENTS__MEMORY__ENABLE_SNAPSHOTS` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:InMemoryEventStoreConfig.memory.enable_snapsh` |
| `ORI_EVENTS__MEMORY__MAX_EVENTS_PER_STREAM` | int | 10000 |  | `packages/oridecon-events/src/oridecon/events/config.py:InMemoryEventStoreConfig.memory.max_events_pe` |
| `ORI_EVENTS__METRICS_MIDDLEWARE__ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:MetricsMiddlewareConfig.metrics_middleware.en` |
| `ORI_EVENTS__METRICS_MIDDLEWARE__HISTOGRAM_BUCKETS` | list[float] | (required) |  | `packages/oridecon-events/src/oridecon/events/config.py:MetricsMiddlewareConfig.metrics_middleware.hi` |
| `ORI_EVENTS__METRICS_MIDDLEWARE__INCLUDE_HISTOGRAMS` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:MetricsMiddlewareConfig.metrics_middleware.in` |
| `ORI_EVENTS__METRICS_MIDDLEWARE__PREFIX` | str | "events" |  | `packages/oridecon-events/src/oridecon/events/config.py:MetricsMiddlewareConfig.metrics_middleware.pr` |
| `ORI_EVENTS__MONGODB__CONNECTION_STRING` | SecretStr | Ellipsis | MongoDB connection string | `packages/oridecon-events/src/oridecon/events/config.py:MongoDBEventStoreConfig.mongodb.connection_st` |
| `ORI_EVENTS__MONGODB__DATABASE_NAME` | str | "events" |  | `packages/oridecon-events/src/oridecon/events/config.py:MongoDBEventStoreConfig.mongodb.database_name` |
| `ORI_EVENTS__MONGODB__EVENTS_COLLECTION` | str | "domain_events" |  | `packages/oridecon-events/src/oridecon/events/config.py:MongoDBEventStoreConfig.mongodb.events_collec` |
| `ORI_EVENTS__MONGODB__MAX_POOL_SIZE` | int | 10 |  | `packages/oridecon-events/src/oridecon/events/config.py:MongoDBEventStoreConfig.mongodb.max_pool_size` |
| `ORI_EVENTS__MONGODB__SERVER_SELECTION_TIMEOUT` | int | 30000 |  | `packages/oridecon-events/src/oridecon/events/config.py:MongoDBEventStoreConfig.mongodb.server_select` |
| `ORI_EVENTS__MONGODB__SNAPSHOTS_COLLECTION` | str | "snapshots" |  | `packages/oridecon-events/src/oridecon/events/config.py:MongoDBEventStoreConfig.mongodb.snapshots_col` |
| `ORI_EVENTS__NAME` | str | "events" |  | `packages/oridecon-events/src/oridecon/events/config.py:EventsConfig.name` |
| `ORI_EVENTS__POSTGRES` | PostgresEventStoreConfig  \| None | None |  | `packages/oridecon-events/src/oridecon/events/config.py:EventsConfig.postgres` |
| `ORI_EVENTS__PROJECTION__BATCH_SIZE` | int | 100 |  | `packages/oridecon-events/src/oridecon/events/config.py:ProjectionConfig.projection.batch_size` |
| `ORI_EVENTS__PROJECTION__CHECKPOINT_INTERVAL` | int | 100 |  | `packages/oridecon-events/src/oridecon/events/config.py:ProjectionConfig.projection.checkpoint_interv` |
| `ORI_EVENTS__PROJECTION__ENABLE_PARALLEL_PROJECTIONS` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:ProjectionConfig.projection.enable_parallel_p` |
| `ORI_EVENTS__PROJECTION__MAX_CATCH_UP_EVENTS` | int | 10000 |  | `packages/oridecon-events/src/oridecon/events/config.py:ProjectionConfig.projection.max_catch_up_even` |
| `ORI_EVENTS__PROJECTION__REBUILD_BATCH_SIZE` | int | 1000 |  | `packages/oridecon-events/src/oridecon/events/config.py:ProjectionConfig.projection.rebuild_batch_siz` |
| `ORI_EVENTS__QUERY_BUS__ENABLE_LOGGING` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:QueryBusConfig.query_bus.enable_logging` |
| `ORI_EVENTS__QUERY_BUS__ENABLE_METRICS` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:QueryBusConfig.query_bus.enable_metrics` |
| `ORI_EVENTS__QUERY_BUS__TIMEOUT_SECONDS` | float | 30.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:QueryBusConfig.query_bus.timeout_seconds` |
| `ORI_EVENTS__RABBITMQ__DURABLE` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:RabbitMQConfig.rabbitmq.durable` |
| `ORI_EVENTS__RABBITMQ__EXCHANGE_NAME` | str | "events" |  | `packages/oridecon-events/src/oridecon/events/config.py:RabbitMQConfig.rabbitmq.exchange_name` |
| `ORI_EVENTS__RABBITMQ__PREFETCH_COUNT` | int | 10 |  | `packages/oridecon-events/src/oridecon/events/config.py:RabbitMQConfig.rabbitmq.prefetch_count` |
| `ORI_EVENTS__RABBITMQ__QUEUE_PREFIX` | str | "events" |  | `packages/oridecon-events/src/oridecon/events/config.py:RabbitMQConfig.rabbitmq.queue_prefix` |
| `ORI_EVENTS__RABBITMQ__URL` | SecretStr | Ellipsis | AMQP connection URL | `packages/oridecon-events/src/oridecon/events/config.py:RabbitMQConfig.rabbitmq.url` |
| `ORI_EVENTS__RETRY_MIDDLEWARE__ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:RetryMiddlewareConfig.retry_middleware.enable` |
| `ORI_EVENTS__RETRY_MIDDLEWARE__EXPONENTIAL_BASE` | float | 2.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:RetryMiddlewareConfig.retry_middleware.expone` |
| `ORI_EVENTS__RETRY_MIDDLEWARE__INITIAL_DELAY_SECONDS` | float | 0.1 |  | `packages/oridecon-events/src/oridecon/events/config.py:RetryMiddlewareConfig.retry_middleware.initia` |
| `ORI_EVENTS__RETRY_MIDDLEWARE__MAX_DELAY_SECONDS` | float | 10.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:RetryMiddlewareConfig.retry_middleware.max_de` |
| `ORI_EVENTS__RETRY_MIDDLEWARE__MAX_RETRIES` | int | 3 |  | `packages/oridecon-events/src/oridecon/events/config.py:RetryMiddlewareConfig.retry_middleware.max_re` |
| `ORI_EVENTS__SAGA__CLEANUP_COMPLETED_AFTER_HOURS` | int | 24 |  | `packages/oridecon-events/src/oridecon/events/config.py:SagaConfig.saga.cleanup_completed_after_hours` |
| `ORI_EVENTS__SAGA__DEFAULT_TIMEOUT_SECONDS` | float | 300.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:SagaConfig.saga.default_timeout_seconds` |
| `ORI_EVENTS__SAGA__ENABLE_COMPENSATION` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:SagaConfig.saga.enable_compensation` |
| `ORI_EVENTS__SAGA__MAX_RETRIES_PER_STEP` | int | 3 |  | `packages/oridecon-events/src/oridecon/events/config.py:SagaConfig.saga.max_retries_per_step` |
| `ORI_EVENTS__SAGA__PERSIST_STATE` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:SagaConfig.saga.persist_state` |
| `ORI_EVENTS__SAGA__RETRY_DELAY_SECONDS` | float | 1.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:SagaConfig.saga.retry_delay_seconds` |
| `ORI_EVENTS__SNAPSHOTS__ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:SnapshotConfig.snapshots.enabled` |
| `ORI_EVENTS__SNAPSHOTS__EVENT_COUNT_THRESHOLD` | int | 100 |  | `packages/oridecon-events/src/oridecon/events/config.py:SnapshotConfig.snapshots.event_count_threshol` |
| `ORI_EVENTS__SNAPSHOTS__MAX_SNAPSHOTS_PER_AGGREGATE` | int | 5 |  | `packages/oridecon-events/src/oridecon/events/config.py:SnapshotConfig.snapshots.max_snapshots_per_ag` |
| `ORI_EVENTS__SNAPSHOTS__STRATEGY` | SnapshotStrategy | (complex) |  | `packages/oridecon-events/src/oridecon/events/config.py:SnapshotConfig.snapshots.strategy` |
| `ORI_EVENTS__SNAPSHOTS__TIME_THRESHOLD_SECONDS` | int | 3600 |  | `packages/oridecon-events/src/oridecon/events/config.py:SnapshotConfig.snapshots.time_threshold_secon` |
| `ORI_EVENTS__SQLITE__DATABASE` | str | "./events.db" |  | `packages/oridecon-events/src/oridecon/events/config.py:SqliteConfig.sqlite.database` |
| `ORI_EVENTS__SQLITE__JOURNAL_MODE` | str | "WAL" |  | `packages/oridecon-events/src/oridecon/events/config.py:SqliteConfig.sqlite.journal_mode` |
| `ORI_EVENTS__SQLITE__PRAGMAS` | dict[str, str] | (required) |  | `packages/oridecon-events/src/oridecon/events/config.py:SqliteConfig.sqlite.pragmas` |
| `ORI_EVENTS__SQLITE__WAL_MODE` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:SqliteConfig.sqlite.wal_mode` |
| `ORI_EVENTS__STREAMING__BATCH_SIZE` | int | 100 |  | `packages/oridecon-events/src/oridecon/events/config.py:StreamingConfig.streaming.batch_size` |
| `ORI_EVENTS__STREAMING__BUFFER_SIZE` | int | 1000 |  | `packages/oridecon-events/src/oridecon/events/config.py:StreamingConfig.streaming.buffer_size` |
| `ORI_EVENTS__STREAMING__ENABLE_WEBSOCKET` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:StreamingConfig.streaming.enable_websocket` |
| `ORI_EVENTS__STREAMING__MAX_SUBSCRIBERS` | int | 100 |  | `packages/oridecon-events/src/oridecon/events/config.py:StreamingConfig.streaming.max_subscribers` |
| `ORI_EVENTS__STREAMING__POLL_INTERVAL_MS` | int | 100 |  | `packages/oridecon-events/src/oridecon/events/config.py:StreamingConfig.streaming.poll_interval_ms` |
| `ORI_EVENTS__STREAMING__WEBSOCKET_PING_INTERVAL` | int | 30 |  | `packages/oridecon-events/src/oridecon/events/config.py:StreamingConfig.streaming.websocket_ping_inte` |
| `ORI_EVENTS__TRANSACTION_MIDDLEWARE__ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:TransactionMiddlewareConfig.transaction_middl` |
| `ORI_EVENTS__TRANSACTION_MIDDLEWARE__ISOLATION_LEVEL` | str | "READ_COMMITTED" |  | `packages/oridecon-events/src/oridecon/events/config.py:TransactionMiddlewareConfig.transaction_middl` |
| `ORI_EVENTS__TRANSACTION_MIDDLEWARE__TIMEOUT_SECONDS` | float | 30.0 |  | `packages/oridecon-events/src/oridecon/events/config.py:TransactionMiddlewareConfig.transaction_middl` |
| `ORI_EVENTS__VALIDATION_MIDDLEWARE__ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:ValidationMiddlewareConfig.validation_middlew` |
| `ORI_EVENTS__VALIDATION_MIDDLEWARE__STRICT_MODE` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:ValidationMiddlewareConfig.validation_middlew` |
| `ORI_EVENTS__VERSION_SKEW_ALERTS_ENABLED` | bool | True |  | `packages/oridecon-events/src/oridecon/events/config.py:EventsConfig.version_skew_alerts_enabled` |
| `ORI_FEATURES__CACHE_TTL` | int | DEFAULT_CACHE_TTL | Seconds to cache flag evaluations (0 = disabled). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Feat` |
| `ORI_FEATURES__CACHE_TTL` | int | DEFAULT_CACHE_TTL | Seconds to cache flag evaluations (0 = disabled). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Featur` |
| `ORI_FEATURES__CACHE_TTL` | int | DEFAULT_CACHE_TTL | Seconds to cache flag evaluations (0 = disabled). | `packages/oridecon-features/src/oridecon/features/config.py:FeatureFlagsConfig.cache_ttl` |
| `ORI_FEATURES__DEFAULT_ENABLED` | bool | DEFAULT_ENABLED | Default value when a flag is not found in the provider. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Feat` |
| `ORI_FEATURES__DEFAULT_ENABLED` | bool | DEFAULT_ENABLED | Default value when a flag is not found in the provider. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Featur` |
| `ORI_FEATURES__DEFAULT_ENABLED` | bool | DEFAULT_ENABLED | Default value when a flag is not found in the provider. | `packages/oridecon-features/src/oridecon/features/config.py:FeatureFlagsConfig.default_enabled` |
| `ORI_FEATURES__ENABLED` | bool | True | Enable the feature flags subsystem | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Feat` |
| `ORI_FEATURES__ENABLED` | bool | True | Enable the feature flags subsystem | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Featur` |
| `ORI_FEATURES__ENABLED` | bool | True | Enable the feature flags subsystem | `packages/oridecon-features/src/oridecon/features/config.py:FeatureFlagsConfig.enabled` |
| `ORI_FEATURES__FLAG_ENV_PREFIX` | str | FLAG_ENV_PREFIX | Env var prefix used by EnvProvider when reading flag values. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Feat` |
| `ORI_FEATURES__FLAG_ENV_PREFIX` | str | FLAG_ENV_PREFIX | Env var prefix used by EnvProvider when reading flag values. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Featur` |
| `ORI_FEATURES__FLAG_ENV_PREFIX` | str | FLAG_ENV_PREFIX | Env var prefix used by EnvProvider when reading flag values. | `packages/oridecon-features/src/oridecon/features/config.py:FeatureFlagsConfig.flag_env_prefix` |
| `ORI_FEATURES__INITIAL_FLAGS` | dict[str, bool] | (required) | Seed flags for the in-memory provider (name -> enabled). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Feat` |
| `ORI_FEATURES__INITIAL_FLAGS` | dict[str, bool] | (required) | Seed flags for the in-memory provider (name -> enabled). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/features/config.py:Featur` |
| `ORI_FEATURES__INITIAL_FLAGS` | dict[str, bool] | (required) | Seed flags for the in-memory provider (name -> enabled). | `packages/oridecon-features/src/oridecon/features/config.py:FeatureFlagsConfig.initial_flags` |
| `ORI_GRAPHQL__ALIAS_LIMIT__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:AliasLimitConfig.alias_limit.enabled` |
| `ORI_GRAPHQL__ALIAS_LIMIT__MAX_ALIASES` | int | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:AliasLimitConfig.alias_limit.max_aliases` |
| `ORI_GRAPHQL__BATCH__ENABLED` | bool | False |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:BatchConfig.batch.enabled` |
| `ORI_GRAPHQL__BATCH__MAX_BATCH_SIZE` | int | 10 |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:BatchConfig.batch.max_batch_size` |
| `ORI_GRAPHQL__CACHE__DEFAULT_MAX_AGE` | Duration  \| int | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:CacheConfig.cache.default_max_age` |
| `ORI_GRAPHQL__CACHE__DEFAULT_SCOPE` | CacheScope | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:CacheConfig.cache.default_scope` |
| `ORI_GRAPHQL__CACHE__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:CacheConfig.cache.enabled` |
| `ORI_GRAPHQL__CACHE__VARY_HEADERS` | list[str] | (required) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:CacheConfig.cache.vary_headers` |
| `ORI_GRAPHQL__COMPLEXITY__DEFAULT_FIELD_COST` | float | 1.0 |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ComplexityConfig.complexity.default_field_c` |
| `ORI_GRAPHQL__COMPLEXITY__DEFAULT_LIST_COST` | float | 10.0 |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ComplexityConfig.complexity.default_list_co` |
| `ORI_GRAPHQL__COMPLEXITY__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ComplexityConfig.complexity.enabled` |
| `ORI_GRAPHQL__COMPLEXITY__MAX_COMPLEXITY` | int | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ComplexityConfig.complexity.max_complexity` |
| `ORI_GRAPHQL__DATALOADER__BATCH_DELAY_MS` | float | 2.0 | Delay in milliseconds before executing a DataLoaderProtocol batch. A small non-zero value (2ms) lets more keys accumulat | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DataLoaderConfig.dataloader.batch_delay_ms` |
| `ORI_GRAPHQL__DATALOADER__BATCH_ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DataLoaderConfig.dataloader.batch_enabled` |
| `ORI_GRAPHQL__DATALOADER__CACHE_ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DataLoaderConfig.dataloader.cache_enabled` |
| `ORI_GRAPHQL__DATALOADER__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DataLoaderConfig.dataloader.enabled` |
| `ORI_GRAPHQL__DATALOADER__MAX_BATCH_SIZE` | int | 100 |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DataLoaderConfig.dataloader.max_batch_size` |
| `ORI_GRAPHQL__DEBUG` | bool | False |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.debug` |
| `ORI_GRAPHQL__DEPTH_LIMIT__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DepthLimitConfig.depth_limit.enabled` |
| `ORI_GRAPHQL__DEPTH_LIMIT__IGNORE_INTROSPECTION` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DepthLimitConfig.depth_limit.ignore_introsp` |
| `ORI_GRAPHQL__DEPTH_LIMIT__MAX_DEPTH` | int | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:DepthLimitConfig.depth_limit.max_depth` |
| `ORI_GRAPHQL__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.enabled` |
| `ORI_GRAPHQL__ENABLE_IDENTITY_RESOLUTION` | bool | False |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.enable_identity_resolution` |
| `ORI_GRAPHQL__ENV` | str  \| None | None | Environment (development/staging/production) | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.env` |
| `ORI_GRAPHQL__ERRORS__DEBUG_MODE` | bool | False |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ErrorConfig.errors.debug_mode` |
| `ORI_GRAPHQL__ERRORS__INCLUDE_STACKTRACE` | bool | False |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ErrorConfig.errors.include_stacktrace` |
| `ORI_GRAPHQL__ERRORS__LOG_ERRORS` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ErrorConfig.errors.log_errors` |
| `ORI_GRAPHQL__ERRORS__MASK_ERRORS` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:ErrorConfig.errors.mask_errors` |
| `ORI_GRAPHQL__INTROSPECTION__ALLOWED_ENVIRONMENTS` | set[str] | (required) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:IntrospectionConfig.introspection.allowed_e` |
| `ORI_GRAPHQL__INTROSPECTION__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:IntrospectionConfig.introspection.enabled` |
| `ORI_GRAPHQL__METRICS__ENABLED` | bool | False |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:MetricsConfig.metrics.enabled` |
| `ORI_GRAPHQL__METRICS__HISTOGRAM_BUCKETS` | list[float] | (required) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:MetricsConfig.metrics.histogram_buckets` |
| `ORI_GRAPHQL__METRICS__INCLUDE_LABELS` | list[str] | (required) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:MetricsConfig.metrics.include_labels` |
| `ORI_GRAPHQL__METRICS__NAMESPACE` | str | "oridecon_graphql" |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:MetricsConfig.metrics.namespace` |
| `ORI_GRAPHQL__NAME` | str | "graphql" |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.name` |
| `ORI_GRAPHQL__PATH` | str | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.path` |
| `ORI_GRAPHQL__PERSISTED_QUERIES__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:PersistedQueryConfig.persisted_queries.enab` |
| `ORI_GRAPHQL__PERSISTED_QUERIES__STORE_TYPE` | str | "memory" |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:PersistedQueryConfig.persisted_queries.stor` |
| `ORI_GRAPHQL__PERSISTED_QUERIES__TTL_SECONDS` | Duration  \| int | 86400 |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:PersistedQueryConfig.persisted_queries.ttl_` |
| `ORI_GRAPHQL__PLAYGROUND__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:PlaygroundConfig.playground.enabled` |
| `ORI_GRAPHQL__PLAYGROUND__PATH` | str | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:PlaygroundConfig.playground.path` |
| `ORI_GRAPHQL__PLAYGROUND__TITLE` | str | "Oridecon GraphQL Playground" |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:PlaygroundConfig.playground.title` |
| `ORI_GRAPHQL__RATE_LIMIT` | RateLimitConfig | (required) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.rate_limit` |
| `ORI_GRAPHQL__SCHEMA_BASELINE_PATH` | str  \| None | None | Path to a GraphQL SDL (.graphql) file containing the baseline schema. When set, GraphQLProvider.boot() compares the curr | `packages/oridecon-graphql/src/oridecon/graphql/config.py:GraphQLConfig.schema_baseline_path` |
| `ORI_GRAPHQL__SUBSCRIPTIONS__CONNECTION_TIMEOUT` | Duration  \| int | 60 |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:SubscriptionConfig.subscriptions.connection` |
| `ORI_GRAPHQL__SUBSCRIPTIONS__ENABLED` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:SubscriptionConfig.subscriptions.enabled` |
| `ORI_GRAPHQL__SUBSCRIPTIONS__KEEPALIVE_INTERVAL` | Duration  \| int | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:SubscriptionConfig.subscriptions.keepalive_` |
| `ORI_GRAPHQL__SUBSCRIPTIONS__PATH` | str | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:SubscriptionConfig.subscriptions.path` |
| `ORI_GRAPHQL__SUBSCRIPTIONS__PROTOCOL` | SubscriptionProtocol | (complex) |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:SubscriptionConfig.subscriptions.protocol` |
| `ORI_GRAPHQL__TRACING__ENABLED` | bool | False |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:TracingConfig.tracing.enabled` |
| `ORI_GRAPHQL__TRACING__SAMPLE_RATE` | float | 1.0 |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:TracingConfig.tracing.sample_rate` |
| `ORI_GRAPHQL__TRACING__SERVICE_NAME` | str | "oridecon-graphql" |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:TracingConfig.tracing.service_name` |
| `ORI_GRAPHQL__TRACING__TRACE_DATALOADERS` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:TracingConfig.tracing.trace_dataloaders` |
| `ORI_GRAPHQL__TRACING__TRACE_RESOLVERS` | bool | True |  | `packages/oridecon-graphql/src/oridecon/graphql/config.py:TracingConfig.tracing.trace_resolvers` |
| `ORI_GRAPH__BACKEND` | str | (complex) | Graph store backend to use | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphConfig.backend` |
| `ORI_GRAPH__BULK_BATCH_SIZE` | int | (complex) | Batch size for bulk operations | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphConfig.bulk_batch_size` |
| `ORI_GRAPH__DEFAULT_QUERY_LIMIT` | int | (complex) | Default limit for query results | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphConfig.default_query_limit` |
| `ORI_GRAPH__DEFAULT_TRAVERSAL_MAX_DEPTH` | int | (complex) | Default maximum depth for traversals | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphConfig.default_traversal_max_depth` |
| `ORI_GRAPH__ENABLED` | bool | True | Enable the graph store subsystem | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphConfig.enabled` |
| `ORI_GRAPH__MAX_RETRIES` | int | (complex) | Maximum number of retries for operations | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphConfig.max_retries` |
| `ORI_GRAPH__MEMORY__MAX_EDGES` | int | (complex) | Maximum number of edges in memory | `packages/oridecon-graph/src/oridecon/graph/config.py:MemoryConfig.memory.max_edges` |
| `ORI_GRAPH__MEMORY__MAX_NODES` | int | (complex) | Maximum number of nodes in memory | `packages/oridecon-graph/src/oridecon/graph/config.py:MemoryConfig.memory.max_nodes` |
| `ORI_GRAPH__NEO4J__CONNECTION_TIMEOUT` | float | (complex) | Connection timeout in seconds | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.connection_timeout` |
| `ORI_GRAPH__NEO4J__DATABASE` | str | (complex) | Target database name | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.database` |
| `ORI_GRAPH__NEO4J__ENCRYPTED` | bool | False | Whether to use SSL/TLS encryption | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.encrypted` |
| `ORI_GRAPH__NEO4J__FETCH_SIZE` | int | (complex) | Default fetch size for results | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.fetch_size` |
| `ORI_GRAPH__NEO4J__MAX_CONNECTION_POOL_SIZE` | int | (complex) | Maximum number of connections in the pool | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.max_connection_pool_size` |
| `ORI_GRAPH__NEO4J__MAX_TRANSACTION_RETRY_TIME` | float | 30.0 | Maximum time for transaction retries | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.max_transaction_retry_time` |
| `ORI_GRAPH__NEO4J__PASSWORD` | SecretStr | (required) | Neo4j password | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.password` |
| `ORI_GRAPH__NEO4J__TRUST` | str | "TRUST_SYSTEM_CA_SIGNED_CERTIFICATES" | Trust strategy for SSL | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.trust` |
| `ORI_GRAPH__NEO4J__URI` | str | "bolt://localhost:7687" | Neo4j BOLT URI | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.uri` |
| `ORI_GRAPH__NEO4J__USERNAME` | str | "neo4j" | Neo4j username | `packages/oridecon-graph/src/oridecon/graph/config.py:Neo4jConfig.neo4j.username` |
| `ORI_GRAPH__RETRY_DELAY` | float | (complex) | Delay between retries in seconds | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphConfig.retry_delay` |
| `ORI_GRAPH__TENANCY__ENABLED` | bool | False | Enable tenant-aware graph resolution | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphTenancyConfig.tenancy.enabled` |
| `ORI_GRAPH__TENANCY__STRATEGY` | str | "node_property" | Which tenancy strategy to use. One of ``"node_property"`` or ``"graph_per_tenant"``. | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphTenancyConfig.tenancy.strategy` |
| `ORI_GRAPH__TENANCY__TEMPLATE` | str | "{logical}_t_{tenant}" | Collection name template for ``GRAPH_PER_TENANT`` strategy. Supports ``{logical}`` and ``{tenant}`` placeholders. | `packages/oridecon-graph/src/oridecon/graph/config.py:GraphTenancyConfig.tenancy.template` |
| `ORI_MONITOR__DEBUG` | bool | False | Enable debug mode | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MonitorConfig.debug` |
| `ORI_MONITOR__ENABLED` | bool | True | Enable monitoring | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MonitorConfig.enabled` |
| `ORI_MONITOR__ENV` | str  \| None | None | Environment (development/staging/production) | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MonitorConfig.env` |
| `ORI_MONITOR__ENVIRONMENT` | Environment | (complex) | Deployment environment | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MonitorConfig.environment` |
| `ORI_MONITOR__ERROR_TRACKING__DSN` | str  \| None | None | Sentry DSN; error tracking is a no-op when unset | `packages/oridecon-monitor/src/oridecon/monitor/config.py:ErrorTrackingConfig.error_tracking.dsn` |
| `ORI_MONITOR__ERROR_TRACKING__ENVIRONMENT` | str  \| None | None | Environment tag for captured events | `packages/oridecon-monitor/src/oridecon/monitor/config.py:ErrorTrackingConfig.error_tracking.environm` |
| `ORI_MONITOR__ERROR_TRACKING__SEND_DEFAULT_PII` | bool | False | Send default PII fields to the error tracker | `packages/oridecon-monitor/src/oridecon/monitor/config.py:ErrorTrackingConfig.error_tracking.send_def` |
| `ORI_MONITOR__ERROR_TRACKING__TRACES_SAMPLE_RATE` | float | 1.0 | Traces sample rate (0.0 to 1.0) | `packages/oridecon-monitor/src/oridecon/monitor/config.py:ErrorTrackingConfig.error_tracking.traces_s` |
| `ORI_MONITOR__HEALTH__CHECKS` | list[str] | (required) | List of health check names to run | `packages/oridecon-monitor/src/oridecon/monitor/config.py:HealthCheckConfig.health.checks` |
| `ORI_MONITOR__HEALTH__ENABLED` | bool | True | Enable health checks | `packages/oridecon-monitor/src/oridecon/monitor/config.py:HealthCheckConfig.health.enabled` |
| `ORI_MONITOR__HEALTH__INCLUDE_DETAILS` | bool | True | Include detailed health info in response | `packages/oridecon-monitor/src/oridecon/monitor/config.py:HealthCheckConfig.health.include_details` |
| `ORI_MONITOR__HEALTH__INTERVAL` | int | (complex) | Health check interval in seconds | `packages/oridecon-monitor/src/oridecon/monitor/config.py:HealthCheckConfig.health.interval` |
| `ORI_MONITOR__HEALTH__PATH` | str | "/health" | Health endpoint path | `packages/oridecon-monitor/src/oridecon/monitor/config.py:HealthCheckConfig.health.path` |
| `ORI_MONITOR__HEALTH__TIMEOUT` | float | 5.0 | Health check timeout in seconds | `packages/oridecon-monitor/src/oridecon/monitor/config.py:HealthCheckConfig.health.timeout` |
| `ORI_MONITOR__METRICS__COLLECTION_INTERVAL` | float | 60.0 | Metrics collection interval in seconds | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MetricsConfig.metrics.collection_interval` |
| `ORI_MONITOR__METRICS__DEFAULT_LABELS` | dict[str, str] | (required) | Default labels for all metrics | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MetricsConfig.metrics.default_labels` |
| `ORI_MONITOR__METRICS__ENABLED` | bool | True | Enable metrics collection | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MetricsConfig.metrics.enabled` |
| `ORI_MONITOR__METRICS__HISTOGRAM_BUCKETS` | list[float] | (required) | Default histogram bucket boundaries | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MetricsConfig.metrics.histogram_buckets` |
| `ORI_MONITOR__METRICS__PREFIX` | str | (complex) | MetricProtocol name prefix | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MetricsConfig.metrics.prefix` |
| `ORI_MONITOR__NAME` | str | (complex) | Provider name | `packages/oridecon-monitor/src/oridecon/monitor/config.py:MonitorConfig.name` |
| `ORI_MONITOR__OPENTELEMETRY__BATCH_SIZE` | int | 512 | Export batch size | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.batch_siz` |
| `ORI_MONITOR__OPENTELEMETRY__COMPRESSION` | str | "none" | Compression type (none, gzip) | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.compressi` |
| `ORI_MONITOR__OPENTELEMETRY__ENDPOINT` | str  \| None | None | OTLP endpoint URL | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.endpoint` |
| `ORI_MONITOR__OPENTELEMETRY__EXPORT_INTERVAL` | float | 5.0 | Export interval seconds | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.export_in` |
| `ORI_MONITOR__OPENTELEMETRY__HEADERS` | dict[str, str] | (required) | OTLP request headers | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.headers` |
| `ORI_MONITOR__OPENTELEMETRY__INSECURE` | bool | False | Use insecure connection | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.insecure` |
| `ORI_MONITOR__OPENTELEMETRY__METRICS_EXPORTERS` | list[OTelExporterConfig] | (required) | List of metrics exporters to build. | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.metrics_e` |
| `ORI_MONITOR__OPENTELEMETRY__TIMEOUT` | float | 30.0 | Export timeout seconds | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.timeout` |
| `ORI_MONITOR__OPENTELEMETRY__TRACING_EXPORTERS` | list[OTelExporterConfig] | (required) | List of tracing exporters to build. | `packages/oridecon-monitor/src/oridecon/monitor/config.py:OpenTelemetryConfig.opentelemetry.tracing_e` |
| `ORI_MONITOR__PROMETHEUS__ENABLE_DEFAULT_METRICS` | bool | True | Enable default process metrics | `packages/oridecon-monitor/src/oridecon/monitor/config.py:PrometheusConfig.prometheus.enable_default_` |
| `ORI_MONITOR__PROMETHEUS__METRICS_TABLE` | str | "metrics_samples" | Table name for metrics samples | `packages/oridecon-monitor/src/oridecon/monitor/config.py:PrometheusConfig.prometheus.metrics_table` |
| `ORI_MONITOR__PROMETHEUS__PATH` | str | "/metrics" | Metrics endpoint path | `packages/oridecon-monitor/src/oridecon/monitor/config.py:PrometheusConfig.prometheus.path` |
| `ORI_MONITOR__PROMETHEUS__PORT` | int | (complex) | Metrics server port | `packages/oridecon-monitor/src/oridecon/monitor/config.py:PrometheusConfig.prometheus.port` |
| `ORI_MONITOR__PROMETHEUS__PUSHGATEWAY_URL` | str  \| None | None | Pushgateway URL for push-based metrics | `packages/oridecon-monitor/src/oridecon/monitor/config.py:PrometheusConfig.prometheus.pushgateway_url` |
| `ORI_MONITOR__PROMETHEUS__PUSH_INTERVAL` | float | 10.0 | Push interval for Pushgateway | `packages/oridecon-monitor/src/oridecon/monitor/config.py:PrometheusConfig.prometheus.push_interval` |
| `ORI_MONITOR__PROMETHEUS__STORE_IN_DB` | bool | False | Persist metrics observations to DB | `packages/oridecon-monitor/src/oridecon/monitor/config.py:PrometheusConfig.prometheus.store_in_db` |
| `ORI_MONITOR__SLO__ALERT_CHANNELS` | list[str] | (required) | Alert channel names for SLO violation dispatch | `packages/oridecon-monitor/src/oridecon/monitor/config.py:SLOConfig.slo.alert_channels` |
| `ORI_MONITOR__SLO__ENABLED` | bool | True | Enable periodic SLO evaluation worker | `packages/oridecon-monitor/src/oridecon/monitor/config.py:SLOConfig.slo.enabled` |
| `ORI_MONITOR__SLO__EVALUATION_INTERVAL` | float | 60.0 | SLO evaluation interval in seconds | `packages/oridecon-monitor/src/oridecon/monitor/config.py:SLOConfig.slo.evaluation_interval` |
| `ORI_MONITOR__SLO__SUPPRESSION_WINDOW_SECONDS` | int | 300 | Alert suppression window in seconds | `packages/oridecon-monitor/src/oridecon/monitor/config.py:SLOConfig.slo.suppression_window_seconds` |
| `ORI_MONITOR__TRACING__ENABLED` | bool | True | Enable tracing | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.enabled` |
| `ORI_MONITOR__TRACING__MAX_ATTRIBUTES` | int | 128 | Max attributes per span | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.max_attributes` |
| `ORI_MONITOR__TRACING__MAX_EVENTS` | int | 128 | Max events per span | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.max_events` |
| `ORI_MONITOR__TRACING__MAX_LINKS` | int | 128 | Max links per span | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.max_links` |
| `ORI_MONITOR__TRACING__MAX_SPANS` | int | (complex) | Max number of spans to keep in memory | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.max_spans` |
| `ORI_MONITOR__TRACING__MAX_TRACES_PER_SECOND` | int | 100 | Max traces to sample per second | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.max_traces_per_second` |
| `ORI_MONITOR__TRACING__PROPAGATION_FORMATS` | list[str] | (required) | Propagation format list | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.propagation_formats` |
| `ORI_MONITOR__TRACING__SAMPLE_RATE` | float | 1.0 | Sample rate (0.0 to 1.0) | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.sample_rate` |
| `ORI_MONITOR__TRACING__SERVICE_NAME` | str | (complex) | Service name for traces | `packages/oridecon-monitor/src/oridecon/monitor/config.py:TracingConfig.tracing.service_name` |
| `ORI_NOSQL__BACKENDS` | list[NamedNoSQLConfig] | (required) | Named NoSQL backends for multi-store support. When non-empty, the provider registers each backend under Annotated[Docume | `packages/oridecon-nosql/src/oridecon/nosql/config.py:NoSQLConfig.backends` |
| `ORI_NOSQL__DRIVER` | str | "mongodb" | NoSQL driver name | `packages/oridecon-nosql/src/oridecon/nosql/config.py:NoSQLConfig.driver` |
| `ORI_NOSQL__ENABLED` | bool | True | Enable NoSQL support | `packages/oridecon-nosql/src/oridecon/nosql/config.py:NoSQLConfig.enabled` |
| `ORI_NOSQL__FIRESTORE__CREDENTIALS_JSON` | str  \| None | None | Path to a service account JSON key file, or the raw JSON string. When ``None``, Application Default Credentials (ADC) ar | `packages/oridecon-nosql/src/oridecon/nosql/config.py:FirestoreConfig.firestore.credentials_json` |
| `ORI_NOSQL__FIRESTORE__DATABASE_ID` | str | "(default)" | Firestore database ID (use '(default)' for the default database) | `packages/oridecon-nosql/src/oridecon/nosql/config.py:FirestoreConfig.firestore.database_id` |
| `ORI_NOSQL__FIRESTORE__PROJECT_ID` | str | Ellipsis | Google Cloud project ID | `packages/oridecon-nosql/src/oridecon/nosql/config.py:FirestoreConfig.firestore.project_id` |
| `ORI_NOSQL__MONGODB__AUTH_SOURCE` | str | "admin" | Authentication database | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.auth_source` |
| `ORI_NOSQL__MONGODB__CONNECT_TIMEOUT_MS` | int | 10000 | Connection timeout (ms) | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.connect_timeout_ms` |
| `ORI_NOSQL__MONGODB__DATABASE` | str | "oridecon" | Database name | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.database` |
| `ORI_NOSQL__MONGODB__MAX_POOL_SIZE` | int | 100 | Maximum connection pool size | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.max_pool_size` |
| `ORI_NOSQL__MONGODB__MIN_POOL_SIZE` | int | 10 | Minimum connection pool size | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.min_pool_size` |
| `ORI_NOSQL__MONGODB__READ_PREFERENCE` | str | "primaryPreferred" | Read preference mode | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.read_preference` |
| `ORI_NOSQL__MONGODB__RETRY_READS` | bool | True | Enable read retries | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.retry_reads` |
| `ORI_NOSQL__MONGODB__RETRY_WRITES` | bool | True | Enable write retries | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.retry_writes` |
| `ORI_NOSQL__MONGODB__SERVER_SELECTION_TIMEOUT_MS` | int | 5000 | Server selection timeout (ms) | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.server_selection_timeout_` |
| `ORI_NOSQL__MONGODB__SOCKET_TIMEOUT_MS` | int | 30000 | Socket timeout (ms) | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.socket_timeout_ms` |
| `ORI_NOSQL__MONGODB__URI` | str | "mongodb://localhost:27017" | MongoDB connection URI | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.uri` |
| `ORI_NOSQL__MONGODB__WRITE_CONCERN_W` | str  \| int | "majority" | Write concern level | `packages/oridecon-nosql/src/oridecon/nosql/config.py:MongoDBConfig.mongodb.write_concern_w` |
| `ORI_NOTIFICATION__INBOX__MARK_READ_ON_FETCH` | bool | False | Automatically mark messages as read when fetched. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_NOTIFICATION__INBOX__MARK_READ_ON_FETCH` | bool | False | Automatically mark messages as read when fetched. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:In` |
| `ORI_NOTIFICATION__INBOX__MARK_READ_ON_FETCH` | bool | False | Automatically mark messages as read when fetched. | `packages/oridecon-notification/src/oridecon/notification/config.py:InboxConfig.mark_read_on_fetch` |
| `ORI_NOTIFICATION__INBOX__MAX_PAGE_SIZE` | int | 50 | Maximum messages returned per page. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_NOTIFICATION__INBOX__MAX_PAGE_SIZE` | int | 50 | Maximum messages returned per page. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:In` |
| `ORI_NOTIFICATION__INBOX__MAX_PAGE_SIZE` | int | 50 | Maximum messages returned per page. | `packages/oridecon-notification/src/oridecon/notification/config.py:InboxConfig.max_page_size` |
| `ORI_NOTIFICATION__INBOX__RETENTION_DAYS` | int | 30 | Days to retain inbox messages before pruning. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_NOTIFICATION__INBOX__RETENTION_DAYS` | int | 30 | Days to retain inbox messages before pruning. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:In` |
| `ORI_NOTIFICATION__INBOX__RETENTION_DAYS` | int | 30 | Days to retain inbox messages before pruning. | `packages/oridecon-notification/src/oridecon/notification/config.py:InboxConfig.retention_days` |
| `ORI_NOTIFICATION__INBOX__STORE_BACKEND` | str | "database" | Storage backend. One of 'database' or 'memory'. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_NOTIFICATION__INBOX__STORE_BACKEND` | str | "database" | Storage backend. One of 'database' or 'memory'. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:In` |
| `ORI_NOTIFICATION__INBOX__STORE_BACKEND` | str | "database" | Storage backend. One of 'database' or 'memory'. | `packages/oridecon-notification/src/oridecon/notification/config.py:InboxConfig.store_backend` |
| `ORI_NOTIFICATION__MAILER__BACKENDS` | list[NamedMailerConfig] | (required) | Named mailer backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[Mai | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_NOTIFICATION__MAILER__BACKENDS` | list[NamedMailerConfig] | (required) | Named mailer backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[Mai | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:Ma` |
| `ORI_NOTIFICATION__MAILER__BACKENDS` | list[NamedMailerConfig] | (required) | Named mailer backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[Mai | `packages/oridecon-notification/src/oridecon/notification/config.py:MailerConfig.backends` |
| `ORI_NOTIFICATION__MAILER__CONSOLE_FALLBACK` | bool | True | When no backends are configured, bind a ConsoleMailer as the default MailerProtocol so emails are logged to the applicat | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:` |
| `ORI_NOTIFICATION__MAILER__CONSOLE_FALLBACK` | bool | True | When no backends are configured, bind a ConsoleMailer as the default MailerProtocol so emails are logged to the applicat | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/notification/config.py:Ma` |
| `ORI_NOTIFICATION__MAILER__CONSOLE_FALLBACK` | bool | True | When no backends are configured, bind a ConsoleMailer as the default MailerProtocol so emails are logged to the applicat | `packages/oridecon-notification/src/oridecon/notification/config.py:MailerConfig.console_fallback` |
| `ORI_NOTIFICATION__PUSH_BACKENDS` | list[NamedPushConfig] | (required) | Named push notification backends for multi-backend support. When non-empty, the provider registers each backend under An | `packages/oridecon-notification/src/oridecon/notification/config.py:NotificationConfig.push_backends` |
| `ORI_NOTIFICATION__SMS_BACKENDS` | list[NamedSMSConfig] | (required) | Named SMS backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[SMSCha | `packages/oridecon-notification/src/oridecon/notification/config.py:NotificationConfig.sms_backends` |
| `ORI_RESILIENCE__BULKHEAD__MAX_CONCURRENT` | int | 10 | Max concurrent requests | `packages/oridecon-resilience/src/oridecon/resilience/config.py:BulkheadConfig.bulkhead.max_concurren` |
| `ORI_RESILIENCE__BULKHEAD__NAME` | str | "" | Bulkhead name | `packages/oridecon-resilience/src/oridecon/resilience/config.py:BulkheadConfig.bulkhead.name` |
| `ORI_RESILIENCE__BULKHEAD__QUEUE_SIZE` | int | 100 | Max queue size | `packages/oridecon-resilience/src/oridecon/resilience/config.py:BulkheadConfig.bulkhead.queue_size` |
| `ORI_RESILIENCE__BULKHEAD__TIMEOUT` | float | 30.0 | Execution timeout | `packages/oridecon-resilience/src/oridecon/resilience/config.py:BulkheadConfig.bulkhead.timeout` |
| `ORI_RESILIENCE__CIRCUIT_BREAKER` | CircuitBreakerConfig | field(...) |  | `packages/oridecon-resilience/src/oridecon/resilience/config.py:ResilienceConfig.circuit_breaker` |
| `ORI_RESILIENCE__IDEMPOTENCY__AUTO_CLEANUP` | bool | True | Start background cleanup task on init. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Id` |
| `ORI_RESILIENCE__IDEMPOTENCY__AUTO_CLEANUP` | bool | True | Start background cleanup task on init. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Idem` |
| `ORI_RESILIENCE__IDEMPOTENCY__AUTO_CLEANUP` | bool | True | Start background cleanup task on init. | `packages/oridecon-resilience/src/oridecon/resilience/config.py:IdempotencyConfig.auto_cleanup` |
| `ORI_RESILIENCE__IDEMPOTENCY__CLEANUP_INTERVAL` | float | 300.0 | Seconds between background cleanup sweeps. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Id` |
| `ORI_RESILIENCE__IDEMPOTENCY__CLEANUP_INTERVAL` | float | 300.0 | Seconds between background cleanup sweeps. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Idem` |
| `ORI_RESILIENCE__IDEMPOTENCY__CLEANUP_INTERVAL` | float | 300.0 | Seconds between background cleanup sweeps. | `packages/oridecon-resilience/src/oridecon/resilience/config.py:IdempotencyConfig.cleanup_interval` |
| `ORI_RESILIENCE__IDEMPOTENCY__KEY_PREFIX` | str | "idempotency:" | Prefix for all keys in backing stores. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Id` |
| `ORI_RESILIENCE__IDEMPOTENCY__KEY_PREFIX` | str | "idempotency:" | Prefix for all keys in backing stores. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Idem` |
| `ORI_RESILIENCE__IDEMPOTENCY__KEY_PREFIX` | str | "idempotency:" | Prefix for all keys in backing stores. | `packages/oridecon-resilience/src/oridecon/resilience/config.py:IdempotencyConfig.key_prefix` |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_ENTRIES` | int | 10000 | Maximum in-memory entries before FIFO eviction. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Id` |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_ENTRIES` | int | 10000 | Maximum in-memory entries before FIFO eviction. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Idem` |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_ENTRIES` | int | 10000 | Maximum in-memory entries before FIFO eviction. | `packages/oridecon-resilience/src/oridecon/resilience/config.py:IdempotencyConfig.max_entries` |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_KEY_LENGTH` | int | 512 | Maximum allowed idempotency key length. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Id` |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_KEY_LENGTH` | int | 512 | Maximum allowed idempotency key length. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Idem` |
| `ORI_RESILIENCE__IDEMPOTENCY__MAX_KEY_LENGTH` | int | 512 | Maximum allowed idempotency key length. | `packages/oridecon-resilience/src/oridecon/resilience/config.py:IdempotencyConfig.max_key_length` |
| `ORI_RESILIENCE__IDEMPOTENCY__TTL` | int | 3600 | TTL for cached results in seconds. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Id` |
| `ORI_RESILIENCE__IDEMPOTENCY__TTL` | int | 3600 | TTL for cached results in seconds. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/resilience/config.py:Idem` |
| `ORI_RESILIENCE__IDEMPOTENCY__TTL` | int | 3600 | TTL for cached results in seconds. | `packages/oridecon-resilience/src/oridecon/resilience/config.py:IdempotencyConfig.ttl` |
| `ORI_RESILIENCE__RETRY` | RetryConfig | field(...) |  | `packages/oridecon-resilience/src/oridecon/resilience/config.py:ResilienceConfig.retry` |
| `ORI_RESILIENCE__TIMEOUT` | TimeoutConfig | field(...) |  | `packages/oridecon-resilience/src/oridecon/resilience/config.py:ResilienceConfig.timeout` |
| `ORI_SEARCH__BACKENDS` | list[NamedSearchConfig] | (required) | Named search backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[Sea | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__BACKENDS` | list[NamedSearchConfig] | (required) | Named search backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[Sea | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchCo` |
| `ORI_SEARCH__BACKENDS` | list[NamedSearchConfig] | (required) | Named search backends for multi-backend support. When non-empty, the provider registers each backend under Annotated[Sea | `packages/oridecon-search/src/oridecon/search/config.py:SearchConfig.backends` |
| `ORI_SEARCH__DATABASE` | str  \| None | None | Named database to use for DB-backed backends (postgres/mysql). References a named database registered via Annotated[Data | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__DATABASE` | str  \| None | None | Named database to use for DB-backed backends (postgres/mysql). References a named database registered via Annotated[Data | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchCo` |
| `ORI_SEARCH__DATABASE` | str  \| None | None | Named database to use for DB-backed backends (postgres/mysql). References a named database registered via Annotated[Data | `packages/oridecon-search/src/oridecon/search/config.py:SearchConfig.database` |
| `ORI_SEARCH__ELASTICSEARCH__API_KEY` | SecretStr  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__API_KEY` | SecretStr  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__API_KEY` | SecretStr  \| None | None |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.api_key` |
| `ORI_SEARCH__ELASTICSEARCH__HOSTS` | list[str] | (required) | Elasticsearch hosts | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__HOSTS` | list[str] | (required) | Elasticsearch hosts | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__HOSTS` | list[str] | (required) | Elasticsearch hosts | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.hosts` |
| `ORI_SEARCH__ELASTICSEARCH__INDEX_PREFIX` | str | "oridecon_search_" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__INDEX_PREFIX` | str | "oridecon_search_" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__INDEX_PREFIX` | str | "oridecon_search_" |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.index_prefi` |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_REPLICAS` | int | 0 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_REPLICAS` | int | 0 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_REPLICAS` | int | 0 |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.number_of_r` |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_SHARDS` | int | 1 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_SHARDS` | int | 1 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__NUMBER_OF_SHARDS` | int | 1 |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.number_of_s` |
| `ORI_SEARCH__ELASTICSEARCH__PASSWORD` | SecretStr  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__PASSWORD` | SecretStr  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__PASSWORD` | SecretStr  \| None | None |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.password` |
| `ORI_SEARCH__ELASTICSEARCH__USERNAME` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__USERNAME` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__USERNAME` | str  \| None | None |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.username` |
| `ORI_SEARCH__ELASTICSEARCH__USE_SSL` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__USE_SSL` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__USE_SSL` | bool | False |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.use_ssl` |
| `ORI_SEARCH__ELASTICSEARCH__VERIFY_CERTS` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elasti` |
| `ORI_SEARCH__ELASTICSEARCH__VERIFY_CERTS` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Elastics` |
| `ORI_SEARCH__ELASTICSEARCH__VERIFY_CERTS` | bool | True |  | `packages/oridecon-search/src/oridecon/search/config.py:ElasticsearchConfig.elasticsearch.verify_cert` |
| `ORI_SEARCH__ENABLED` | bool | True | Enable the search subsystem | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__ENABLED` | bool | True | Enable the search subsystem | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchCo` |
| `ORI_SEARCH__ENABLED` | bool | True | Enable the search subsystem | `packages/oridecon-search/src/oridecon/search/config.py:SearchConfig.enabled` |
| `ORI_SEARCH__MEILISEARCH__API_KEY` | SecretStr  \| None | None | MeiliSearch API key | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__API_KEY` | SecretStr  \| None | None | MeiliSearch API key | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__API_KEY` | SecretStr  \| None | None | MeiliSearch API key | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.api_key` |
| `ORI_SEARCH__MEILISEARCH__DISPLAYED_ATTRIBUTES` | list[str] | (required) | Fields to return in results | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__DISPLAYED_ATTRIBUTES` | list[str] | (required) | Fields to return in results | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__DISPLAYED_ATTRIBUTES` | list[str] | (required) | Fields to return in results | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.displayed_attri` |
| `ORI_SEARCH__MEILISEARCH__FILTERABLE_ATTRIBUTES` | list[str] | (required) | Attributes that can be filtered | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__FILTERABLE_ATTRIBUTES` | list[str] | (required) | Attributes that can be filtered | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__FILTERABLE_ATTRIBUTES` | list[str] | (required) | Attributes that can be filtered | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.filterable_attr` |
| `ORI_SEARCH__MEILISEARCH__MAX_CONNECTIONS` | int | 10 | Maximum number of connections | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__MAX_CONNECTIONS` | int | 10 | Maximum number of connections | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__MAX_CONNECTIONS` | int | 10 | Maximum number of connections | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.max_connections` |
| `ORI_SEARCH__MEILISEARCH__MIN_WORD_SIZE_FOR_TYPOS` | dict[str, int] | (required) | Minimum word size for typo tolerance | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__MIN_WORD_SIZE_FOR_TYPOS` | dict[str, int] | (required) | Minimum word size for typo tolerance | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__MIN_WORD_SIZE_FOR_TYPOS` | dict[str, int] | (required) | Minimum word size for typo tolerance | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.min_word_size_f` |
| `ORI_SEARCH__MEILISEARCH__RANKING_RULES` | list[str] | (required) | Ranking rules in order | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__RANKING_RULES` | list[str] | (required) | Ranking rules in order | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__RANKING_RULES` | list[str] | (required) | Ranking rules in order | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.ranking_rules` |
| `ORI_SEARCH__MEILISEARCH__SEARCHABLE_ATTRIBUTES` | list[str] | (required) | Fields to search in | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__SEARCHABLE_ATTRIBUTES` | list[str] | (required) | Fields to search in | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__SEARCHABLE_ATTRIBUTES` | list[str] | (required) | Fields to search in | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.searchable_attr` |
| `ORI_SEARCH__MEILISEARCH__SORTABLE_ATTRIBUTES` | list[str] | (required) | Attributes that can be sorted | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__SORTABLE_ATTRIBUTES` | list[str] | (required) | Attributes that can be sorted | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__SORTABLE_ATTRIBUTES` | list[str] | (required) | Attributes that can be sorted | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.sortable_attrib` |
| `ORI_SEARCH__MEILISEARCH__TIMEOUT` | int | 30 | Request timeout in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__TIMEOUT` | int | 30 | Request timeout in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__TIMEOUT` | int | 30 | Request timeout in seconds | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.timeout` |
| `ORI_SEARCH__MEILISEARCH__TYPO_TOLERANCE_ENABLED` | bool | True | Enable typo tolerance | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__TYPO_TOLERANCE_ENABLED` | bool | True | Enable typo tolerance | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__TYPO_TOLERANCE_ENABLED` | bool | True | Enable typo tolerance | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.typo_tolerance_` |
| `ORI_SEARCH__MEILISEARCH__URL` | str | "http://localhost:7700" | MeiliSearch server URL | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliS` |
| `ORI_SEARCH__MEILISEARCH__URL` | str | "http://localhost:7700" | MeiliSearch server URL | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MeiliSea` |
| `ORI_SEARCH__MEILISEARCH__URL` | str | "http://localhost:7700" | MeiliSearch server URL | `packages/oridecon-search/src/oridecon/search/config.py:MeiliSearchConfig.meilisearch.url` |
| `ORI_SEARCH__MONGO__CONNECTION_STRING` | SecretStr | SecretStr(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MongoS` |
| `ORI_SEARCH__MONGO__CONNECTION_STRING` | SecretStr | SecretStr(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MongoSea` |
| `ORI_SEARCH__MONGO__CONNECTION_STRING` | SecretStr | SecretStr(...) |  | `packages/oridecon-search/src/oridecon/search/config.py:MongoSearchConfig.mongo.connection_string` |
| `ORI_SEARCH__MONGO__DATABASE_NAME` | str | "search" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MongoS` |
| `ORI_SEARCH__MONGO__DATABASE_NAME` | str | "search" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MongoSea` |
| `ORI_SEARCH__MONGO__DATABASE_NAME` | str | "search" |  | `packages/oridecon-search/src/oridecon/search/config.py:MongoSearchConfig.mongo.database_name` |
| `ORI_SEARCH__MONGO__USE_ATLAS_SEARCH` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MongoS` |
| `ORI_SEARCH__MONGO__USE_ATLAS_SEARCH` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MongoSea` |
| `ORI_SEARCH__MONGO__USE_ATLAS_SEARCH` | bool | False |  | `packages/oridecon-search/src/oridecon/search/config.py:MongoSearchConfig.mongo.use_atlas_search` |
| `ORI_SEARCH__MYSQL__CONNECTION_STRING` | SecretStr | SecretStr(...) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MySQLS` |
| `ORI_SEARCH__MYSQL__CONNECTION_STRING` | SecretStr | SecretStr(...) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MySQLSea` |
| `ORI_SEARCH__MYSQL__CONNECTION_STRING` | SecretStr | SecretStr(...) |  | `packages/oridecon-search/src/oridecon/search/config.py:MySQLSearchConfig.mysql.connection_string` |
| `ORI_SEARCH__MYSQL__FULLTEXT_MODE` | str | "natural_language" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MySQLS` |
| `ORI_SEARCH__MYSQL__FULLTEXT_MODE` | str | "natural_language" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MySQLSea` |
| `ORI_SEARCH__MYSQL__FULLTEXT_MODE` | str | "natural_language" |  | `packages/oridecon-search/src/oridecon/search/config.py:MySQLSearchConfig.mysql.fulltext_mode` |
| `ORI_SEARCH__MYSQL__MIN_WORD_LENGTH` | int | 3 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MySQLS` |
| `ORI_SEARCH__MYSQL__MIN_WORD_LENGTH` | int | 3 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:MySQLSea` |
| `ORI_SEARCH__MYSQL__MIN_WORD_LENGTH` | int | 3 |  | `packages/oridecon-search/src/oridecon/search/config.py:MySQLSearchConfig.mysql.min_word_length` |
| `ORI_SEARCH__OPENSEARCH__HOSTS` | list[str] | (required) | OpenSearch hosts | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSe` |
| `ORI_SEARCH__OPENSEARCH__HOSTS` | list[str] | (required) | OpenSearch hosts | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSear` |
| `ORI_SEARCH__OPENSEARCH__HOSTS` | list[str] | (required) | OpenSearch hosts | `packages/oridecon-search/src/oridecon/search/config.py:OpenSearchConfig.opensearch.hosts` |
| `ORI_SEARCH__OPENSEARCH__INDEX_PREFIX` | str | "oridecon_search_" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSe` |
| `ORI_SEARCH__OPENSEARCH__INDEX_PREFIX` | str | "oridecon_search_" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSear` |
| `ORI_SEARCH__OPENSEARCH__INDEX_PREFIX` | str | "oridecon_search_" |  | `packages/oridecon-search/src/oridecon/search/config.py:OpenSearchConfig.opensearch.index_prefix` |
| `ORI_SEARCH__OPENSEARCH__PASSWORD` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSe` |
| `ORI_SEARCH__OPENSEARCH__PASSWORD` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSear` |
| `ORI_SEARCH__OPENSEARCH__PASSWORD` | str  \| None | None |  | `packages/oridecon-search/src/oridecon/search/config.py:OpenSearchConfig.opensearch.password` |
| `ORI_SEARCH__OPENSEARCH__TIMEOUT` | int | 30 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSe` |
| `ORI_SEARCH__OPENSEARCH__TIMEOUT` | int | 30 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSear` |
| `ORI_SEARCH__OPENSEARCH__TIMEOUT` | int | 30 |  | `packages/oridecon-search/src/oridecon/search/config.py:OpenSearchConfig.opensearch.timeout` |
| `ORI_SEARCH__OPENSEARCH__USERNAME` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSe` |
| `ORI_SEARCH__OPENSEARCH__USERNAME` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSear` |
| `ORI_SEARCH__OPENSEARCH__USERNAME` | str  \| None | None |  | `packages/oridecon-search/src/oridecon/search/config.py:OpenSearchConfig.opensearch.username` |
| `ORI_SEARCH__OPENSEARCH__USE_SSL` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSe` |
| `ORI_SEARCH__OPENSEARCH__USE_SSL` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSear` |
| `ORI_SEARCH__OPENSEARCH__USE_SSL` | bool | False |  | `packages/oridecon-search/src/oridecon/search/config.py:OpenSearchConfig.opensearch.use_ssl` |
| `ORI_SEARCH__OPENSEARCH__VERIFY_SSL` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSe` |
| `ORI_SEARCH__OPENSEARCH__VERIFY_SSL` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:OpenSear` |
| `ORI_SEARCH__OPENSEARCH__VERIFY_SSL` | bool | True |  | `packages/oridecon-search/src/oridecon/search/config.py:OpenSearchConfig.opensearch.verify_ssl` |
| `ORI_SEARCH__OPERATIONS__BULK_CHUNK_SIZE` | int | 500 | Bulk request chunk size | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__OPERATIONS__BULK_CHUNK_SIZE` | int | 500 | Bulk request chunk size | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchOp` |
| `ORI_SEARCH__OPERATIONS__BULK_CHUNK_SIZE` | int | 500 | Bulk request chunk size | `packages/oridecon-search/src/oridecon/search/config.py:SearchOperationsConfig.operations.bulk_chunk_` |
| `ORI_SEARCH__OPERATIONS__MAX_RETRIES` | int | 3 | Max retry attempts | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__OPERATIONS__MAX_RETRIES` | int | 3 | Max retry attempts | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchOp` |
| `ORI_SEARCH__OPERATIONS__MAX_RETRIES` | int | 3 | Max retry attempts | `packages/oridecon-search/src/oridecon/search/config.py:SearchOperationsConfig.operations.max_retries` |
| `ORI_SEARCH__OPERATIONS__REQUEST_TIMEOUT` | float | 30.0 | Request timeout seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__OPERATIONS__REQUEST_TIMEOUT` | float | 30.0 | Request timeout seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchOp` |
| `ORI_SEARCH__OPERATIONS__REQUEST_TIMEOUT` | float | 30.0 | Request timeout seconds | `packages/oridecon-search/src/oridecon/search/config.py:SearchOperationsConfig.operations.request_tim` |
| `ORI_SEARCH__OPERATIONS__RETRY_BACKOFF` | float | 0.5 | Retry backoff multiplier | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__OPERATIONS__RETRY_BACKOFF` | float | 0.5 | Retry backoff multiplier | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchOp` |
| `ORI_SEARCH__OPERATIONS__RETRY_BACKOFF` | float | 0.5 | Retry backoff multiplier | `packages/oridecon-search/src/oridecon/search/config.py:SearchOperationsConfig.operations.retry_backo` |
| `ORI_SEARCH__POSTGRES__AUTO_CREATE_TABLES` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgr` |
| `ORI_SEARCH__POSTGRES__AUTO_CREATE_TABLES` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgres` |
| `ORI_SEARCH__POSTGRES__AUTO_CREATE_TABLES` | bool | True |  | `packages/oridecon-search/src/oridecon/search/config.py:PostgresSearchConfig.postgres.auto_create_tab` |
| `ORI_SEARCH__POSTGRES__CONNECTION_STRING` | SecretStr | SecretStr(...) | PostgreSQL connection string | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgr` |
| `ORI_SEARCH__POSTGRES__CONNECTION_STRING` | SecretStr | SecretStr(...) | PostgreSQL connection string | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgres` |
| `ORI_SEARCH__POSTGRES__CONNECTION_STRING` | SecretStr | SecretStr(...) | PostgreSQL connection string | `packages/oridecon-search/src/oridecon/search/config.py:PostgresSearchConfig.postgres.connection_stri` |
| `ORI_SEARCH__POSTGRES__ENABLE_TRIGRAM` | bool | True | Enable pg_trgm fuzzy matching | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgr` |
| `ORI_SEARCH__POSTGRES__ENABLE_TRIGRAM` | bool | True | Enable pg_trgm fuzzy matching | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgres` |
| `ORI_SEARCH__POSTGRES__ENABLE_TRIGRAM` | bool | True | Enable pg_trgm fuzzy matching | `packages/oridecon-search/src/oridecon/search/config.py:PostgresSearchConfig.postgres.enable_trigram` |
| `ORI_SEARCH__POSTGRES__TEXT_SEARCH_CONFIG` | str | "english" | PostgreSQL text search config | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgr` |
| `ORI_SEARCH__POSTGRES__TEXT_SEARCH_CONFIG` | str | "english" | PostgreSQL text search config | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Postgres` |
| `ORI_SEARCH__POSTGRES__TEXT_SEARCH_CONFIG` | str | "english" | PostgreSQL text search config | `packages/oridecon-search/src/oridecon/search/config.py:PostgresSearchConfig.postgres.text_search_con` |
| `ORI_SEARCH__QUERY__DEFAULT_LIMIT` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryC` |
| `ORI_SEARCH__QUERY__DEFAULT_LIMIT` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryCon` |
| `ORI_SEARCH__QUERY__DEFAULT_LIMIT` | int | (complex) |  | `packages/oridecon-search/src/oridecon/search/config.py:QueryConfig.query.default_limit` |
| `ORI_SEARCH__QUERY__ENABLE_AGGREGATIONS` | bool | False |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryC` |
| `ORI_SEARCH__QUERY__ENABLE_AGGREGATIONS` | bool | False |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryCon` |
| `ORI_SEARCH__QUERY__ENABLE_AGGREGATIONS` | bool | False |  | `packages/oridecon-search/src/oridecon/search/config.py:QueryConfig.query.enable_aggregations` |
| `ORI_SEARCH__QUERY__ENABLE_FACETING` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryC` |
| `ORI_SEARCH__QUERY__ENABLE_FACETING` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryCon` |
| `ORI_SEARCH__QUERY__ENABLE_FACETING` | bool | True |  | `packages/oridecon-search/src/oridecon/search/config.py:QueryConfig.query.enable_faceting` |
| `ORI_SEARCH__QUERY__ENABLE_HIGHLIGHTING` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryC` |
| `ORI_SEARCH__QUERY__ENABLE_HIGHLIGHTING` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryCon` |
| `ORI_SEARCH__QUERY__ENABLE_HIGHLIGHTING` | bool | True |  | `packages/oridecon-search/src/oridecon/search/config.py:QueryConfig.query.enable_highlighting` |
| `ORI_SEARCH__QUERY__FUZZY_THRESHOLD` | float | 0.8 |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryC` |
| `ORI_SEARCH__QUERY__FUZZY_THRESHOLD` | float | 0.8 |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryCon` |
| `ORI_SEARCH__QUERY__FUZZY_THRESHOLD` | float | 0.8 |  | `packages/oridecon-search/src/oridecon/search/config.py:QueryConfig.query.fuzzy_threshold` |
| `ORI_SEARCH__QUERY__MAX_LIMIT` | int | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryC` |
| `ORI_SEARCH__QUERY__MAX_LIMIT` | int | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryCon` |
| `ORI_SEARCH__QUERY__MAX_LIMIT` | int | (complex) |  | `packages/oridecon-search/src/oridecon/search/config.py:QueryConfig.query.max_limit` |
| `ORI_SEARCH__QUERY__STRATEGY` | str | "fuzzy" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryC` |
| `ORI_SEARCH__QUERY__STRATEGY` | str | "fuzzy" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:QueryCon` |
| `ORI_SEARCH__QUERY__STRATEGY` | str | "fuzzy" |  | `packages/oridecon-search/src/oridecon/search/config.py:QueryConfig.query.strategy` |
| `ORI_SEARCH__SQLITE__AUTO_CREATE_TABLES` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SQLite` |
| `ORI_SEARCH__SQLITE__AUTO_CREATE_TABLES` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SQLiteSe` |
| `ORI_SEARCH__SQLITE__AUTO_CREATE_TABLES` | bool | True |  | `packages/oridecon-search/src/oridecon/search/config.py:SQLiteSearchConfig.sqlite.auto_create_tables` |
| `ORI_SEARCH__SQLITE__DB_PATH` | str | ":memory:" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SQLite` |
| `ORI_SEARCH__SQLITE__DB_PATH` | str | ":memory:" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SQLiteSe` |
| `ORI_SEARCH__SQLITE__DB_PATH` | str | ":memory:" |  | `packages/oridecon-search/src/oridecon/search/config.py:SQLiteSearchConfig.sqlite.db_path` |
| `ORI_SEARCH__SQLITE__TOKENIZER` | str | "porter unicode61" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SQLite` |
| `ORI_SEARCH__SQLITE__TOKENIZER` | str | "porter unicode61" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SQLiteSe` |
| `ORI_SEARCH__SQLITE__TOKENIZER` | str | "porter unicode61" |  | `packages/oridecon-search/src/oridecon/search/config.py:SQLiteSearchConfig.sqlite.tokenizer` |
| `ORI_SEARCH__TIMEOUT` | float | 30.0 | Default request timeout seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Search` |
| `ORI_SEARCH__TIMEOUT` | float | 30.0 | Default request timeout seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:SearchCo` |
| `ORI_SEARCH__TIMEOUT` | float | 30.0 | Default request timeout seconds | `packages/oridecon-search/src/oridecon/search/config.py:SearchConfig.timeout` |
| `ORI_SEARCH__TYPESENSE__API_KEY` | SecretStr  \| None | None | Typesense API key | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typese` |
| `ORI_SEARCH__TYPESENSE__API_KEY` | SecretStr  \| None | None | Typesense API key | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typesens` |
| `ORI_SEARCH__TYPESENSE__API_KEY` | SecretStr  \| None | None | Typesense API key | `packages/oridecon-search/src/oridecon/search/config.py:TypesenseConfig.typesense.api_key` |
| `ORI_SEARCH__TYPESENSE__CONNECTION_TIMEOUT` | int | 30 | Connection timeout | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typese` |
| `ORI_SEARCH__TYPESENSE__CONNECTION_TIMEOUT` | int | 30 | Connection timeout | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typesens` |
| `ORI_SEARCH__TYPESENSE__CONNECTION_TIMEOUT` | int | 30 | Connection timeout | `packages/oridecon-search/src/oridecon/search/config.py:TypesenseConfig.typesense.connection_timeout` |
| `ORI_SEARCH__TYPESENSE__HEALTH_CHECK_INTERVAL` | int | 60 | Health check interval | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typese` |
| `ORI_SEARCH__TYPESENSE__HEALTH_CHECK_INTERVAL` | int | 60 | Health check interval | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typesens` |
| `ORI_SEARCH__TYPESENSE__HEALTH_CHECK_INTERVAL` | int | 60 | Health check interval | `packages/oridecon-search/src/oridecon/search/config.py:TypesenseConfig.typesense.health_check_interv` |
| `ORI_SEARCH__TYPESENSE__NODES` | list[dict[str, str]] | (required) | Typesense node connections | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typese` |
| `ORI_SEARCH__TYPESENSE__NODES` | list[dict[str, str]] | (required) | Typesense node connections | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/search/config.py:Typesens` |
| `ORI_SEARCH__TYPESENSE__NODES` | list[dict[str, str]] | (required) | Typesense node connections | `packages/oridecon-search/src/oridecon/search/config.py:TypesenseConfig.typesense.nodes` |
| `ORI_SQL__AUDIT_HMAC_KEY` | str  \| None | None | HMAC key for audit checksum signing. Plain text or base64. | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseConfig.audit_hmac_key` |
| `ORI_SQL__BACKENDS` | list[NamedDatabaseConfig] | (required) | Multi-database backends list. When non-empty, drives multi-DB mode. The entry with primary=True (or the first entry) als | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseConfig.backends` |
| `ORI_SQL__BACKEND__URL` | SecretStr | Ellipsis | Database connection URL (may contain credentials) | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseBackendConfig.backend.url` |
| `ORI_SQL__ENABLED` | bool | True |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseConfig.enabled` |
| `ORI_SQL__MIGRATIONS__LOCK_TIMEOUT` | Duration | Duration.seconds(...) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseMigrationConfig.migrations.lock_timeout` |
| `ORI_SQL__NAME` | str | "database" |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseConfig.name` |
| `ORI_SQL__OPERATIONS__ECHO` | bool | False |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseOperationConfig.operations.echo` |
| `ORI_SQL__OPERATIONS__STATEMENT_TIMEOUT` | Duration | Duration.seconds(...) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseOperationConfig.operations.statement_timeou` |
| `ORI_SQL__OUTBOX__BATCH_MAX_AGE` | Duration | Duration.seconds(...) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseOutboxConfig.outbox.batch_max_age` |
| `ORI_SQL__OUTBOX__ENABLED` | bool | True |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseOutboxConfig.outbox.enabled` |
| `ORI_SQL__OUTBOX__POLL_INTERVAL` | Duration | Duration.seconds(...) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabaseOutboxConfig.outbox.poll_interval` |
| `ORI_SQL__POOL__ACQUIRE_TIMEOUT` | Duration | Duration.seconds(...) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.acquire_timeout` |
| `ORI_SQL__POOL__IDLE_TIMEOUT` | Duration | Duration.minutes(...) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.idle_timeout` |
| `ORI_SQL__POOL__MAX_LIFETIME` | Duration | Duration.hours(...) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.max_lifetime` |
| `ORI_SQL__POOL__MAX_OVERFLOW` | int | 5 |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.max_overflow` |
| `ORI_SQL__POOL__MAX_SIZE` | int | (complex) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.max_size` |
| `ORI_SQL__POOL__MIN_SIZE` | int | (complex) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.min_size` |
| `ORI_SQL__POOL__RECYCLE` | int | 3600 |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.recycle` |
| `ORI_SQL__POOL__TIMEOUT` | float | (complex) |  | `packages/oridecon-sql/src/oridecon/sql/config.py:DatabasePoolConfig.pool.timeout` |
| `ORI_STORAGE__BACKENDS` | list[NamedStorageConfig] | (required) | Named storage backends for multi-store support. When non-empty, the provider registers each backend under Annotated[Blob | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageConfig.backends` |
| `ORI_STORAGE__DEFAULT_DRIVER` | Literal['local', 's3', 'gcs', 'azure', 'memory', 'r2'] | (complex) | Default storage driver to use | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageConfig.default_driver` |
| `ORI_STORAGE__DRIVERS` | dict[str, StorageLocalConfig  \| StorageS3Config  \| StorageGCSConfig  \| Storag | (required) | Driver-specific configurations | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageConfig.drivers` |
| `ORI_STORAGE__ENABLED` | bool | True |  | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageConfig.enabled` |
| `ORI_STORAGE__ENV` | str  \| None | None | Environment (development/staging/production) | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageConfig.env` |
| `ORI_STORAGE__HEALTH_CHECK_TIMEOUT` | float | 5.0 | Timeout in seconds for the startup health check in StorageProvider.boot() | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageConfig.health_check_timeout` |
| `ORI_STORAGE__NAME` | str | "storage" |  | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageConfig.name` |
| `ORI_STORAGE__SERVICE__ALLOWED_MIME_TYPES` | list[str] | (required) | Allowed MIME types for upload validation. Defaults to a safe set of common image types: ['image/jpeg', 'image/png', 'ima | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageOperationConfig.service.allowed_mime` |
| `ORI_STORAGE__SERVICE__MAX_FILE_SIZE_MB` | int | (complex) | Maximum file size in MB | `packages/oridecon-storage/src/oridecon/storage/config.py:StorageOperationConfig.service.max_file_siz` |
| `ORI_TASKS__BACKENDS` | list[NamedTaskConfig] | (required) | Named task queue backends for multi-queue support. When non-empty, the provider registers each backend under Annotated[T | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskConfig.backends` |
| `ORI_TASKS__BACKEND__AMQP_URL` | SecretStr | SecretStr(...) | AMQP connection URL (may contain credentials). | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskBackendConfig.backend.amqp_url` |
| `ORI_TASKS__BACKEND__POSTGRES_DSN` | SecretStr  \| None | None | Postgres DSN (required when type="postgres"; may contain credentials). | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskBackendConfig.backend.postgres_dsn` |
| `ORI_TASKS__BACKEND__QUEUE_NAME` | str | (complex) | Name of the task queue | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskBackendConfig.backend.queue_name` |
| `ORI_TASKS__BACKEND__REDIS_URL` | SecretStr | SecretStr(...) | Redis connection URL (may contain credentials). | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskBackendConfig.backend.redis_url` |
| `ORI_TASKS__BACKEND__TYPE` | str | (complex) | Queue backend type | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskBackendConfig.backend.type` |
| `ORI_TASKS__ENABLED` | bool | True | Whether tasks module is enabled | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskConfig.enabled` |
| `ORI_TASKS__ENV` | str  \| None | None | Environment (development/staging/production) | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskConfig.env` |
| `ORI_TASKS__EXTRA` | dict[str, Any] | (required) |  | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskConfig.extra` |
| `ORI_TASKS__NAME` | str | "tasks" | Configuration name | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskConfig.name` |
| `ORI_TASKS__RATE_LIMIT__BURST` | int  \| None | None | Maximum burst size | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskRateLimitConfig.rate_limit.burst` |
| `ORI_TASKS__RATE_LIMIT__ENABLED` | bool | False | Whether rate limiting is enabled | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskRateLimitConfig.rate_limit.enabled` |
| `ORI_TASKS__RATE_LIMIT__PER` | float | 1.0 | Time period in seconds | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskRateLimitConfig.rate_limit.per` |
| `ORI_TASKS__RATE_LIMIT__RATE` | int | 100 | Number of tasks allowed per time period | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskRateLimitConfig.rate_limit.rate` |
| `ORI_TASKS__RETRY` | RetryConfig | (required) |  | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskConfig.retry` |
| `ORI_TASKS__SCHEDULER__CHECK_INTERVAL` | float | (complex) | Interval between schedule checks (seconds) | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskSchedulerConfig.scheduler.check_interval` |
| `ORI_TASKS__SCHEDULER__ENABLED` | bool | True | Whether scheduling is enabled | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskSchedulerConfig.scheduler.enabled` |
| `ORI_TASKS__SCHEDULER__TIMEZONE` | str | (complex) | Timezone for cron expressions | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskSchedulerConfig.scheduler.timezone` |
| `ORI_TASKS__TIMEOUT__DEFAULT_TIMEOUT` | float | (complex) | Default timeout | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskTimeoutConfig.timeout.default_timeout` |
| `ORI_TASKS__TIMEOUT__ENFORCE_TIMEOUT` | bool | True | Enforce timeouts | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskTimeoutConfig.timeout.enforce_timeout` |
| `ORI_TASKS__TIMEOUT__MAX_TIMEOUT` | float | (complex) | Maximum allowed timeout | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskTimeoutConfig.timeout.max_timeout` |
| `ORI_TASKS__WORKER__DEFAULT_TIMEOUT` | float | (complex) | Default timeout for tasks without an explicit timeout (seconds) | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskWorkerConfig.worker.default_timeout` |
| `ORI_TASKS__WORKER__ENFORCE_TIMEOUT` | bool | True | Whether to enforce timeouts on all tasks | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskWorkerConfig.worker.enforce_timeout` |
| `ORI_TASKS__WORKER__MAX_CONCURRENT_TASKS` | int | (complex) | Maximum concurrent tasks per worker | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskWorkerConfig.worker.max_concurrent_tasks` |
| `ORI_TASKS__WORKER__MAX_TIMEOUT` | float | (complex) | Maximum allowed timeout for any task (seconds) | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskWorkerConfig.worker.max_timeout` |
| `ORI_TASKS__WORKER__POLL_INTERVAL` | float | (complex) | Interval between queue polls (seconds) | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskWorkerConfig.worker.poll_interval` |
| `ORI_TASKS__WORKER__SHUTDOWN_TIMEOUT` | float | (complex) | Timeout for graceful shutdown (seconds) | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskWorkerConfig.worker.shutdown_timeout` |
| `ORI_TASKS__WORKER__WORKER_COUNT` | int | (complex) | Number of worker instances | `packages/oridecon-tasks/src/oridecon/tasks/config.py:TaskWorkerConfig.worker.worker_count` |
| `ORI_TENANCY__INTEGRATION__CACHE_KEY_PREFIX` | bool | True |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:IntegrationConfig.integration.cache_key_pre` |
| `ORI_TENANCY__INTEGRATION__SQL_CONTEXT_BRIDGE` | bool | True |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:IntegrationConfig.integration.sql_context_b` |
| `ORI_TENANCY__LIFECYCLE__AUTO_PROVISION_ISOLATION` | bool | True |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:LifecycleConfig.lifecycle.auto_provision_is` |
| `ORI_TENANCY__LIFECYCLE__ISOLATION_STRATEGY` | str | "row_level" |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:LifecycleConfig.lifecycle.isolation_strateg` |
| `ORI_TENANCY__OVERRIDES__CACHE_TTL` | int | DEFAULT_CONFIG_CACHE_TTL |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ConfigOverridesConfig.overrides.cache_ttl` |
| `ORI_TENANCY__RESOLUTION__HEADER_NAME` | str | DEFAULT_HEADER_NAME |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.header_name` |
| `ORI_TENANCY__RESOLUTION__JWT_CLAIM_KEY` | str | DEFAULT_JWT_CLAIM_KEY |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.jwt_claim_key` |
| `ORI_TENANCY__RESOLUTION__PATH_PATTERN` | str  \| None | DEFAULT_PATH_PATTERN |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.path_pattern` |
| `ORI_TENANCY__RESOLUTION__RESOLVERS` | list[str] | field(...) |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.resolvers` |
| `ORI_TENANCY__RESOLUTION__STRICT_MEMBERSHIP` | bool | True |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.strict_membersh` |
| `ORI_TENANCY__RESOLUTION__SUBDOMAIN_PATTERN` | str  \| None | None |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.subdomain_patte` |
| `ORI_TENANCY__RESOLUTION__TRUSTED_RESOLVERS` | list[str] | field(...) |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.trusted_resolve` |
| `ORI_TENANCY__RESOLUTION__VALIDATOR_CACHE_TTL` | int | DEFAULT_VALIDATOR_CACHE_TTL |  | `packages/oridecon-tenancy/src/oridecon/tenancy/config.py:ResolutionConfig.resolution.validator_cache` |
| `ORI_TESTING__CLEANUP_TEMP_FILES` | bool | True | Clean up temporary files after tests | `packages/oridecon-testing/src/oridecon/testing/config.py:TestingConfig.cleanup_temp_files` |
| `ORI_TESTING__DB_REUSE` | bool | True | Reuse test databases between tests | `packages/oridecon-testing/src/oridecon/testing/config.py:TestingConfig.db_reuse` |
| `ORI_TESTING__ENABLED` | bool | True |  | `packages/oridecon-testing/src/oridecon/testing/config.py:TestingConfig.enabled` |
| `ORI_TESTING__MOCK_EXTERNAL_SERVICES` | bool | True | Mock external service calls | `packages/oridecon-testing/src/oridecon/testing/config.py:TestingConfig.mock_external_services` |
| `ORI_UI__AUTO_ESCAPE` | bool | True | HTML-escape user strings by default. | `experimental/apps/oridecon-ui/src/oridecon/ui/config.py:UIConfig.auto_escape` |
| `ORI_UI__DEBUG_COMPONENTS` | bool | False | Render data-component debug attributes. | `experimental/apps/oridecon-ui/src/oridecon/ui/config.py:UIConfig.debug_components` |
| `ORI_UI__DEFAULT_THEME` | str | "default" | Default CSS theme name. | `experimental/apps/oridecon-ui/src/oridecon/ui/config.py:UIConfig.default_theme` |
| `ORI_UI__ENABLE_REALTIME` | bool | False | Enable realtime update features. | `experimental/apps/oridecon-ui/src/oridecon/ui/config.py:UIConfig.enable_realtime` |
| `ORI_UI__ENABLE_SSE` | bool | False | Enable Server-Sent Events support. | `experimental/apps/oridecon-ui/src/oridecon/ui/config.py:UIConfig.enable_sse` |
| `ORI_UI__HTMX_VERSION` | str | "2.0.4" | HTMX CDN version. | `experimental/apps/oridecon-ui/src/oridecon/ui/config.py:UIConfig.htmx_version` |
| `ORI_UI__THEME` | str | "light" | Active UI theme. | `experimental/apps/oridecon-ui/src/oridecon/ui/config.py:UIConfig.theme` |
| `ORI_VECTOR__BACKEND` | str | (complex) | Vector store backend to use | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.backend` |
| `ORI_VECTOR__BACKENDS` | list[NamedVectorConfig] | (required) | Named vector store backends for multi-store support. When non-empty, the provider registers each backend under Annotated | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.backends` |
| `ORI_VECTOR__CACHE_TTL` | int | 86400 | Cache TTL in seconds (default: 24 hours) | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.cache_ttl` |
| `ORI_VECTOR__COLLECTION_NAME` | str | "default" | Default collection name for AI-layer operations | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.collection_name` |
| `ORI_VECTOR__DEFAULT_DIMENSION` | int | 1536 | Default vector dimension | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.default_dimension` |
| `ORI_VECTOR__DEFAULT_DISTANCE_METRIC` | DistanceMetric | (complex) | Default distance metric for new collections | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.default_distance_metric` |
| `ORI_VECTOR__DEFAULT_INDEX_TYPE` | IndexType | (complex) | Default index type for new collections | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.default_index_type` |
| `ORI_VECTOR__EMBEDDING_MODEL` | str | "text-embedding-3-small" | Embedding model name for AI-layer embedding generation | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.embedding_model` |
| `ORI_VECTOR__EMBEDDING__API_BASE` | str | "http://fastembed" | Base URL of the embedding API. The client appends '/embeddings' to this URL. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config` |
| `ORI_VECTOR__EMBEDDING__API_BASE` | str | "http://fastembed" | Base URL of the embedding API. The client appends '/embeddings' to this URL. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config.p` |
| `ORI_VECTOR__EMBEDDING__API_BASE` | str | "http://fastembed" | Base URL of the embedding API. The client appends '/embeddings' to this URL. | `packages/oridecon-vector/src/oridecon/vector/embedding/config.py:EmbeddingClientConfig.api_base` |
| `ORI_VECTOR__EMBEDDING__API_KEY` | str  \| None | None | API key sent as Bearer token (required for OpenAI and most cloud providers). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config` |
| `ORI_VECTOR__EMBEDDING__API_KEY` | str  \| None | None | API key sent as Bearer token (required for OpenAI and most cloud providers). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config.p` |
| `ORI_VECTOR__EMBEDDING__API_KEY` | str  \| None | None | API key sent as Bearer token (required for OpenAI and most cloud providers). | `packages/oridecon-vector/src/oridecon/vector/embedding/config.py:EmbeddingClientConfig.api_key` |
| `ORI_VECTOR__EMBEDDING__BATCH_SIZE` | int | 64 | Maximum number of texts per embedding API request. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config` |
| `ORI_VECTOR__EMBEDDING__BATCH_SIZE` | int | 64 | Maximum number of texts per embedding API request. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config.p` |
| `ORI_VECTOR__EMBEDDING__BATCH_SIZE` | int | 64 | Maximum number of texts per embedding API request. | `packages/oridecon-vector/src/oridecon/vector/embedding/config.py:EmbeddingClientConfig.batch_size` |
| `ORI_VECTOR__EMBEDDING__DIMENSION` | int | 768 | Expected output vector dimension. Must match the model (768 for nomic-embed-text-v1.5, 1536 for text-embedding-ada-002). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config` |
| `ORI_VECTOR__EMBEDDING__DIMENSION` | int | 768 | Expected output vector dimension. Must match the model (768 for nomic-embed-text-v1.5, 1536 for text-embedding-ada-002). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config.p` |
| `ORI_VECTOR__EMBEDDING__DIMENSION` | int | 768 | Expected output vector dimension. Must match the model (768 for nomic-embed-text-v1.5, 1536 for text-embedding-ada-002). | `packages/oridecon-vector/src/oridecon/vector/embedding/config.py:EmbeddingClientConfig.dimension` |
| `ORI_VECTOR__EMBEDDING__FORMAT` | Literal['openai', 'fastembed', 'cohere'] | "openai" | API payload format. 'openai' uses {'input': [...]}, 'fastembed' uses {'texts': [...]}, 'cohere' uses {'texts': [...]}. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config` |
| `ORI_VECTOR__EMBEDDING__FORMAT` | Literal['openai', 'fastembed', 'cohere'] | "openai" | API payload format. 'openai' uses {'input': [...]}, 'fastembed' uses {'texts': [...]}, 'cohere' uses {'texts': [...]}. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config.p` |
| `ORI_VECTOR__EMBEDDING__FORMAT` | Literal['openai', 'fastembed', 'cohere'] | "openai" | API payload format. 'openai' uses {'input': [...]}, 'fastembed' uses {'texts': [...]}, 'cohere' uses {'texts': [...]}. | `packages/oridecon-vector/src/oridecon/vector/embedding/config.py:EmbeddingClientConfig.format` |
| `ORI_VECTOR__EMBEDDING__MODEL` | str | "nomic-ai/nomic-embed-text-v1.5" | Embedding model identifier passed to the API. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config` |
| `ORI_VECTOR__EMBEDDING__MODEL` | str | "nomic-ai/nomic-embed-text-v1.5" | Embedding model identifier passed to the API. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config.p` |
| `ORI_VECTOR__EMBEDDING__MODEL` | str | "nomic-ai/nomic-embed-text-v1.5" | Embedding model identifier passed to the API. | `packages/oridecon-vector/src/oridecon/vector/embedding/config.py:EmbeddingClientConfig.model` |
| `ORI_VECTOR__EMBEDDING__TIMEOUT` | float | 30.0 | HTTP request timeout in seconds. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config` |
| `ORI_VECTOR__EMBEDDING__TIMEOUT` | float | 30.0 | HTTP request timeout in seconds. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/vector/embedding/config.p` |
| `ORI_VECTOR__EMBEDDING__TIMEOUT` | float | 30.0 | HTTP request timeout in seconds. | `packages/oridecon-vector/src/oridecon/vector/embedding/config.py:EmbeddingClientConfig.timeout` |
| `ORI_VECTOR__ENABLED` | bool | True | Enable the vector store subsystem | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.enabled` |
| `ORI_VECTOR__ENABLE_CACHE` | bool | False | Enable embedding caching (requires a CacheBackend binding) | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.enable_cache` |
| `ORI_VECTOR__MAX_RETRIES` | int | (complex) | Maximum number of retries for operations | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.max_retries` |
| `ORI_VECTOR__MEMORY__MAX_COLLECTIONS` | int | 100 | Maximum number of collections in memory | `packages/oridecon-vector/src/oridecon/vector/config.py:MemoryConfig.memory.max_collections` |
| `ORI_VECTOR__MEMORY__MAX_VECTORS_PER_COLLECTION` | int | 100000 | Maximum number of vectors per collection | `packages/oridecon-vector/src/oridecon/vector/config.py:MemoryConfig.memory.max_vectors_per_collectio` |
| `ORI_VECTOR__PGVECTOR__CREATE_EXTENSION` | bool | True | Whether to create pgvector extension if missing | `packages/oridecon-vector/src/oridecon/vector/config.py:PgVectorConfig.pgvector.create_extension` |
| `ORI_VECTOR__PGVECTOR__DATABASE` | str | "primary" | Name of the database backend from db.backends to use for pgvector. Matches a 'name:' entry in the db.backends list. Defa | `packages/oridecon-vector/src/oridecon/vector/config.py:PgVectorConfig.pgvector.database` |
| `ORI_VECTOR__PGVECTOR__DEFAULT_EF_SEARCH` | int | (complex) | Default ef_search for HNSW index | `packages/oridecon-vector/src/oridecon/vector/config.py:PgVectorConfig.pgvector.default_ef_search` |
| `ORI_VECTOR__PGVECTOR__DEFAULT_LISTS` | int | (complex) | Default number of lists for IVFFlat index | `packages/oridecon-vector/src/oridecon/vector/config.py:PgVectorConfig.pgvector.default_lists` |
| `ORI_VECTOR__PGVECTOR__DEFAULT_PROBES` | int | (complex) | Default number of probes for IVFFlat index | `packages/oridecon-vector/src/oridecon/vector/config.py:PgVectorConfig.pgvector.default_probes` |
| `ORI_VECTOR__PGVECTOR__SCHEMA` | str | "public" | Database schema for vector tables | `packages/oridecon-vector/src/oridecon/vector/config.py:PgVectorConfig.pgvector.schema` |
| `ORI_VECTOR__PGVECTOR__TABLE_PREFIX` | str | "vec_" | Prefix for vector storage tables | `packages/oridecon-vector/src/oridecon/vector/config.py:PgVectorConfig.pgvector.table_prefix` |
| `ORI_VECTOR__PINECONE__API_KEY` | SecretStr | SecretStr(...) | Pinecone API key | `packages/oridecon-vector/src/oridecon/vector/config.py:PineconeConfig.pinecone.api_key` |
| `ORI_VECTOR__PINECONE__ENVIRONMENT` | str | "" | Pinecone environment (e.g. 'us-west1-gcp') | `packages/oridecon-vector/src/oridecon/vector/config.py:PineconeConfig.pinecone.environment` |
| `ORI_VECTOR__PINECONE__INDEX_NAME` | str | "" | Name of the Pinecone index | `packages/oridecon-vector/src/oridecon/vector/config.py:PineconeConfig.pinecone.index_name` |
| `ORI_VECTOR__PINECONE__NAMESPACE` | str | "" | Default namespace for the index | `packages/oridecon-vector/src/oridecon/vector/config.py:PineconeConfig.pinecone.namespace` |
| `ORI_VECTOR__PINECONE__POOL_THREADS` | int | 4 | Number of threads for the connection pool | `packages/oridecon-vector/src/oridecon/vector/config.py:PineconeConfig.pinecone.pool_threads` |
| `ORI_VECTOR__PINECONE__TIMEOUT` | float | (complex) | Request timeout in seconds | `packages/oridecon-vector/src/oridecon/vector/config.py:PineconeConfig.pinecone.timeout` |
| `ORI_VECTOR__QDRANT__API_KEY` | SecretStr  \| None | None | Qdrant API key | `packages/oridecon-vector/src/oridecon/vector/config.py:QdrantConfig.qdrant.api_key` |
| `ORI_VECTOR__QDRANT__GRPC_PORT` | int | 6334 | gRPC port for Qdrant | `packages/oridecon-vector/src/oridecon/vector/config.py:QdrantConfig.qdrant.grpc_port` |
| `ORI_VECTOR__QDRANT__PREFER_GRPC` | bool | True | Whether to prefer gRPC over HTTP | `packages/oridecon-vector/src/oridecon/vector/config.py:QdrantConfig.qdrant.prefer_grpc` |
| `ORI_VECTOR__QDRANT__TIMEOUT` | float | (complex) | Request timeout in seconds | `packages/oridecon-vector/src/oridecon/vector/config.py:QdrantConfig.qdrant.timeout` |
| `ORI_VECTOR__QDRANT__URL` | str | "http://localhost:6333" | Qdrant server URL | `packages/oridecon-vector/src/oridecon/vector/config.py:QdrantConfig.qdrant.url` |
| `ORI_VECTOR__RETRY_DELAY` | float | (complex) | Delay between retries in seconds | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.retry_delay` |
| `ORI_VECTOR__TENANCY__ENABLED` | bool | False | Enable tenant-aware collection name resolution | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorTenancyConfig.tenancy.enabled` |
| `ORI_VECTOR__TENANCY__RESOLVER_KIND` | str | "templated" | Which ``TenantCollectionResolver`` to use. One of ``"templated"`` or ``"pinecone_namespace"``. | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorTenancyConfig.tenancy.resolver_kind` |
| `ORI_VECTOR__UPSERT_BATCH_SIZE` | int | (complex) | Number of vectors per upsert batch | `packages/oridecon-vector/src/oridecon/vector/config.py:VectorConfig.upsert_batch_size` |
| `ORI_VECTOR__WEAVIATE__API_KEY` | SecretStr  \| None | None | Weaviate API key for authenticated clusters | `packages/oridecon-vector/src/oridecon/vector/config.py:WeaviateConfig.weaviate.api_key` |
| `ORI_VECTOR__WEAVIATE__GRPC_PORT` | int | 50051 | gRPC port for the Weaviate cluster | `packages/oridecon-vector/src/oridecon/vector/config.py:WeaviateConfig.weaviate.grpc_port` |
| `ORI_VECTOR__WEAVIATE__TIMEOUT` | float | (complex) | Request timeout in seconds | `packages/oridecon-vector/src/oridecon/vector/config.py:WeaviateConfig.weaviate.timeout` |
| `ORI_VECTOR__WEAVIATE__URL` | str | "http://localhost:8080" | Weaviate cluster URL (HTTP) | `packages/oridecon-vector/src/oridecon/vector/config.py:WeaviateConfig.weaviate.url` |
| `ORI_WEB__ALLOWED_HOSTS` | list[str] | (required) | Hostnames permitted to reach the application. Empty by default; must be configured before production deployment. | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityConfig.allowed_hosts` |
| `ORI_WEB__API_DOCS__ENABLED` | bool | True | Enable API documentation endpoints (/docs, /redoc) and auto-configure CSP for their CDN assets | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:APIDocsCo` |
| `ORI_WEB__API_DOCS__ENABLED` | bool | True | Enable API documentation endpoints (/docs, /redoc) and auto-configure CSP for their CDN assets | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:APIDocsConf` |
| `ORI_WEB__API_DOCS__ENABLED` | bool | True | Enable API documentation endpoints (/docs, /redoc) and auto-configure CSP for their CDN assets | `packages/oridecon-web/src/oridecon/web/config.py:APIDocsConfig.api_docs.enabled` |
| `ORI_WEB__API_DOCS__PROVIDER` | str | "both" | Documentation provider: 'swagger', 'redoc', or 'both' | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:APIDocsCo` |
| `ORI_WEB__API_DOCS__PROVIDER` | str | "both" | Documentation provider: 'swagger', 'redoc', or 'both' | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:APIDocsConf` |
| `ORI_WEB__API_DOCS__PROVIDER` | str | "both" | Documentation provider: 'swagger', 'redoc', or 'both' | `packages/oridecon-web/src/oridecon/web/config.py:APIDocsConfig.api_docs.provider` |
| `ORI_WEB__AUTH_EXCLUDE_PATHS` | list[str] | (required) | Paths to exclude from authentication | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__AUTH_EXCLUDE_PATHS` | list[str] | (required) | Paths to exclude from authentication | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.a` |
| `ORI_WEB__AUTH_EXCLUDE_PATHS` | list[str] | (required) | Paths to exclude from authentication | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.auth_exclude_paths` |
| `ORI_WEB__COMPRESSION_ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__COMPRESSION_ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.c` |
| `ORI_WEB__COMPRESSION_ENABLED` | bool | True |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.compression_enabled` |
| `ORI_WEB__CORS` | CORSConfig | (required) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__CORS` | CORSConfig | (required) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.c` |
| `ORI_WEB__CORS` | CORSConfig | (required) |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.cors` |
| `ORI_WEB__CORS__ALLOWED_ORIGINS` | list[str] | (required) | Allowed origins (use ['*'] to allow all) | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.allowed_origins` |
| `ORI_WEB__CORS__ALLOW_CREDENTIALS` | bool | False |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.allow_credentials` |
| `ORI_WEB__CORS__ALLOW_HEADERS` | list[str] | (required) |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.allow_headers` |
| `ORI_WEB__CORS__ALLOW_METHODS` | list[str] | (required) |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.allow_methods` |
| `ORI_WEB__CORS__ALLOW_ORIGIN_REGEX` | str  \| None | None | Regex pattern for allowed origins (matched when not in allowed_origins) | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.allow_origin_regex` |
| `ORI_WEB__CORS__DEBUG_PERMISSIVE` | bool | False | When True and debug mode is active, allow any origin via wildcard (explicit opt-in replacement for the old implicit debu | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.debug_permissive` |
| `ORI_WEB__CORS__ENABLED` | bool | True | Enable CORS | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.enabled` |
| `ORI_WEB__CORS__EXPOSE_HEADERS` | list[str] | (required) |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.expose_headers` |
| `ORI_WEB__CORS__MAX_AGE` | int | 600 |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CORSConfig.cors.max_age` |
| `ORI_WEB__CROSS_ORIGIN__EMBEDDER_POLICY` | str | "require-corp" | Cross-Origin-Embedder-Policy header value | `packages/oridecon-web/src/oridecon/web/security/config.py:CrossOriginConfig.cross_origin.embedder_po` |
| `ORI_WEB__CROSS_ORIGIN__ENABLED` | bool | False | Emit cross-origin isolation headers | `packages/oridecon-web/src/oridecon/web/security/config.py:CrossOriginConfig.cross_origin.enabled` |
| `ORI_WEB__CROSS_ORIGIN__OPENER_POLICY` | str | "same-origin" | Cross-Origin-Opener-Policy header value | `packages/oridecon-web/src/oridecon/web/security/config.py:CrossOriginConfig.cross_origin.opener_poli` |
| `ORI_WEB__CROSS_ORIGIN__RESOURCE_POLICY` | str | "same-origin" | Cross-Origin-Resource-Policy header value | `packages/oridecon-web/src/oridecon/web/security/config.py:CrossOriginConfig.cross_origin.resource_po` |
| `ORI_WEB__CSP__DIRECTIVES` | dict[str, Any] | (required) | CSP directives mapping directive name to source expression(s) | `packages/oridecon-web/src/oridecon/web/security/config.py:CSPConfig.csp.directives` |
| `ORI_WEB__CSP__ENABLED` | bool | True | Emit the Content-Security-Policy header | `packages/oridecon-web/src/oridecon/web/security/config.py:CSPConfig.csp.enabled` |
| `ORI_WEB__CSRF__COOKIE_DOMAIN` | str  \| None | None |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.cookie_domain` |
| `ORI_WEB__CSRF__COOKIE_HTTPONLY` | bool | True |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.cookie_httponly` |
| `ORI_WEB__CSRF__COOKIE_NAME` | str | "csrf_token" |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.cookie_name` |
| `ORI_WEB__CSRF__COOKIE_PATH` | str | "/" |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.cookie_path` |
| `ORI_WEB__CSRF__COOKIE_SAMESITE` | str | "Lax" |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.cookie_samesite` |
| `ORI_WEB__CSRF__COOKIE_SECURE` | bool | True |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.cookie_secure` |
| `ORI_WEB__CSRF__ENABLED` | bool | False |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.enabled` |
| `ORI_WEB__CSRF__EXCLUDED_PATHS` | list[str] | (required) | URL path prefixes exempt from CSRF validation for cookie-less requests; cookie-bearing requests on these paths are still | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.excluded_paths` |
| `ORI_WEB__CSRF__EXCLUDE_AUTH_SCHEMES` | list[str] | (required) | Authorization header schemes that bypass CSRF validation (explicit opt-in). | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.exclude_auth_schemes` |
| `ORI_WEB__CSRF__EXCLUDE_CONTENT_TYPES` | list[str] | (required) | Content-Type values that bypass CSRF validation (explicit opt-in — JSON requests are validated by default so cookie-auth | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.exclude_content_types` |
| `ORI_WEB__CSRF__HEADER_NAME` | str | "X-CSRF-Token" |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.header_name` |
| `ORI_WEB__CSRF__SECRET_KEY` | str  \| None | None | HMAC secret used to sign and verify CSRF tokens (populated via ORI_WEB__SECURITY__CSRF__SECRET_KEY) | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.secret_key` |
| `ORI_WEB__CSRF__TOKEN_LENGTH` | int | 32 |  | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.token_length` |
| `ORI_WEB__CSRF__TOKEN_TTL` | int | 3600 | TTL in seconds for synchronizer-mode tokens stored in cache. | `packages/oridecon-web/src/oridecon/web/security/config.py:CSRFConfig.csrf.token_ttl` |
| `ORI_WEB__CUSTOM_HEADERS` | dict[str, str] | (required) | Additional HTTP response headers emitted verbatim | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityConfig.custom_headers` |
| `ORI_WEB__DEBUG_ROUTES` | bool | False | Enable debug routes | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__DEBUG_ROUTES` | bool | False | Enable debug routes | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.d` |
| `ORI_WEB__DEBUG_ROUTES` | bool | False | Enable debug routes | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.debug_routes` |
| `ORI_WEB__DEBUG_ROUTES_TOKEN` | SecretStr  \| None | None | Token required to access debug routes (sent as X-Debug-Token header). | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__DEBUG_ROUTES_TOKEN` | SecretStr  \| None | None | Token required to access debug routes (sent as X-Debug-Token header). | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.d` |
| `ORI_WEB__DEBUG_ROUTES_TOKEN` | SecretStr  \| None | None | Token required to access debug routes (sent as X-Debug-Token header). | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.debug_routes_token` |
| `ORI_WEB__ENABLED` | bool | True | Enable the security subsystem | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityConfig.enabled` |
| `ORI_WEB__ENABLED` | bool | True |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__ENABLED` | bool | True |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.e` |
| `ORI_WEB__ENABLED` | bool | True |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.enabled` |
| `ORI_WEB__ENABLE_AUTH` | bool | False | Enable built-in authentication middleware. Requires authenticators to be registered in the container. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__ENABLE_AUTH` | bool | False | Enable built-in authentication middleware. Requires authenticators to be registered in the container. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.e` |
| `ORI_WEB__ENABLE_AUTH` | bool | False | Enable built-in authentication middleware. Requires authenticators to be registered in the container. | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.enable_auth` |
| `ORI_WEB__ENABLE_CORS` | bool | True |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityConfig.enable_cors` |
| `ORI_WEB__ENABLE_CSRF` | bool | True |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityConfig.enable_csrf` |
| `ORI_WEB__ENABLE_DEBUG_ROUTES_ENV_GATE` | bool | False | Require explicit opt-in for debug route registration. | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__ENABLE_DEBUG_ROUTES_ENV_GATE` | bool | False | Require explicit opt-in for debug route registration. | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.e` |
| `ORI_WEB__ENABLE_DEBUG_ROUTES_ENV_GATE` | bool | False | Require explicit opt-in for debug route registration. | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.enable_debug_routes_env_gate` |
| `ORI_WEB__ENABLE_IDENTITY_RESOLUTION` | bool | False | Automatically resolve OAuth external IDs to internal UUIDs in authenticated requests | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__ENABLE_IDENTITY_RESOLUTION` | bool | False | Automatically resolve OAuth external IDs to internal UUIDs in authenticated requests | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.e` |
| `ORI_WEB__ENABLE_IDENTITY_RESOLUTION` | bool | False | Automatically resolve OAuth external IDs to internal UUIDs in authenticated requests | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.enable_identity_resolution` |
| `ORI_WEB__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__ENV` | str  \| None | None | Environment (development/staging/production) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.e` |
| `ORI_WEB__ENV` | str  \| None | None | Environment (development/staging/production) | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.env` |
| `ORI_WEB__HEADERS__CONTENT_TYPE_NOSNIFF` | bool | True |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.content_type` |
| `ORI_WEB__HEADERS__CSP` | str  \| None | None |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.csp` |
| `ORI_WEB__HEADERS__FRAME_OPTIONS` | str | "DENY" |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.frame_option` |
| `ORI_WEB__HEADERS__HSTS_INCLUDE_SUBDOMAINS` | bool | True |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.hsts_include` |
| `ORI_WEB__HEADERS__HSTS_MAX_AGE` | int | 31536000 |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.hsts_max_age` |
| `ORI_WEB__HEADERS__PERMISSIONS_POLICY` | str  \| None | None |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.permissions_` |
| `ORI_WEB__HEADERS__REFERRER_POLICY` | str | "strict-origin-when-cross-origin" |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.referrer_pol` |
| `ORI_WEB__HEADERS__XSS_PROTECTION` | str | "1; mode=block" |  | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityHeadersConfig.headers.xss_protecti` |
| `ORI_WEB__HSTS__ENABLED` | bool | False | Emit the Strict-Transport-Security header | `packages/oridecon-web/src/oridecon/web/security/config.py:HSTSConfig.hsts.enabled` |
| `ORI_WEB__HSTS__INCLUDE_SUBDOMAINS` | bool | True | Apply HSTS to all subdomains | `packages/oridecon-web/src/oridecon/web/security/config.py:HSTSConfig.hsts.include_subdomains` |
| `ORI_WEB__HSTS__MAX_AGE` | int | 31536000 | HSTS max-age in seconds (default 1 year) | `packages/oridecon-web/src/oridecon/web/security/config.py:HSTSConfig.hsts.max_age` |
| `ORI_WEB__HSTS__PRELOAD` | bool | False | Include site in HSTS preload list | `packages/oridecon-web/src/oridecon/web/security/config.py:HSTSConfig.hsts.preload` |
| `ORI_WEB__MAX_BODY_SIZE` | int  \| None | (complex) | Maximum allowed request body size in bytes. Requests with a Content-Length header exceeding this limit receive a 413 res | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__MAX_BODY_SIZE` | int  \| None | (complex) | Maximum allowed request body size in bytes. Requests with a Content-Length header exceeding this limit receive a 413 res | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.m` |
| `ORI_WEB__MAX_BODY_SIZE` | int  \| None | (complex) | Maximum allowed request body size in bytes. Requests with a Content-Length header exceeding this limit receive a 413 res | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.max_body_size` |
| `ORI_WEB__NAME` | str | "web" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__NAME` | str | "web" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.n` |
| `ORI_WEB__NAME` | str | "web" |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.name` |
| `ORI_WEB__OPENAPI_TITLE` | str | "API" | OpenAPI Title | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__OPENAPI_TITLE` | str | "API" | OpenAPI Title | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.o` |
| `ORI_WEB__OPENAPI_TITLE` | str | "API" | OpenAPI Title | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.openapi_title` |
| `ORI_WEB__OPENAPI_URL` | str  \| None | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__OPENAPI_URL` | str  \| None | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.o` |
| `ORI_WEB__OPENAPI_URL` | str  \| None | (complex) |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.openapi_url` |
| `ORI_WEB__OPENAPI_VERSION` | str | "1.0.0" | OpenAPI Version | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__OPENAPI_VERSION` | str | "1.0.0" | OpenAPI Version | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.o` |
| `ORI_WEB__OPENAPI_VERSION` | str | "1.0.0" | OpenAPI Version | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.openapi_version` |
| `ORI_WEB__PERMISSIONS_POLICY` | dict[str, str] | (required) | Permissions-Policy directive map | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityConfig.permissions_policy` |
| `ORI_WEB__RATE_LIMIT__DEFAULT_LIMIT` | int | (complex) | Max requests per window | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimit` |
| `ORI_WEB__RATE_LIMIT__DEFAULT_LIMIT` | int | (complex) | Max requests per window | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimitCo` |
| `ORI_WEB__RATE_LIMIT__DEFAULT_LIMIT` | int | (complex) | Max requests per window | `packages/oridecon-web/src/oridecon/web/config.py:RateLimitConfig.rate_limit.default_limit` |
| `ORI_WEB__RATE_LIMIT__DEFAULT_WINDOW` | int | (complex) | Window size in seconds | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimit` |
| `ORI_WEB__RATE_LIMIT__DEFAULT_WINDOW` | int | (complex) | Window size in seconds | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimitCo` |
| `ORI_WEB__RATE_LIMIT__DEFAULT_WINDOW` | int | (complex) | Window size in seconds | `packages/oridecon-web/src/oridecon/web/config.py:RateLimitConfig.rate_limit.default_window` |
| `ORI_WEB__RATE_LIMIT__ENABLED` | bool | True | Enable rate limiting. When true, RateLimitMiddleware enforces the matched per-path rule or the default_limit/default_win | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimit` |
| `ORI_WEB__RATE_LIMIT__ENABLED` | bool | True | Enable rate limiting. When true, RateLimitMiddleware enforces the matched per-path rule or the default_limit/default_win | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimitCo` |
| `ORI_WEB__RATE_LIMIT__ENABLED` | bool | True | Enable rate limiting. When true, RateLimitMiddleware enforces the matched per-path rule or the default_limit/default_win | `packages/oridecon-web/src/oridecon/web/config.py:RateLimitConfig.rate_limit.enabled` |
| `ORI_WEB__RATE_LIMIT__RULES` | dict[str, RateLimitRuleConfig] | (required) | Per-path rate limit rules; longest-prefix match wins | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimit` |
| `ORI_WEB__RATE_LIMIT__RULES` | dict[str, RateLimitRuleConfig] | (required) | Per-path rate limit rules; longest-prefix match wins | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimitCo` |
| `ORI_WEB__RATE_LIMIT__RULES` | dict[str, RateLimitRuleConfig] | (required) | Per-path rate limit rules; longest-prefix match wins | `packages/oridecon-web/src/oridecon/web/config.py:RateLimitConfig.rate_limit.rules` |
| `ORI_WEB__RATE_LIMIT__STORAGE_BACKEND` | str | "memory" | Storage backend (memory/redis) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimit` |
| `ORI_WEB__RATE_LIMIT__STORAGE_BACKEND` | str | "memory" | Storage backend (memory/redis) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimitCo` |
| `ORI_WEB__RATE_LIMIT__STORAGE_BACKEND` | str | "memory" | Storage backend (memory/redis) | `packages/oridecon-web/src/oridecon/web/config.py:RateLimitConfig.rate_limit.storage_backend` |
| `ORI_WEB__RATE_LIMIT__WHITELIST_IPS` | list[str] | (required) | Exempt IP addresses | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimit` |
| `ORI_WEB__RATE_LIMIT__WHITELIST_IPS` | list[str] | (required) | Exempt IP addresses | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RateLimitCo` |
| `ORI_WEB__RATE_LIMIT__WHITELIST_IPS` | list[str] | (required) | Exempt IP addresses | `packages/oridecon-web/src/oridecon/web/config.py:RateLimitConfig.rate_limit.whitelist_ips` |
| `ORI_WEB__REDOC_JS_URL` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__REDOC_JS_URL` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.r` |
| `ORI_WEB__REDOC_JS_URL` | str  \| None | None |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.redoc_js_url` |
| `ORI_WEB__REDOC_URL` | str  \| None | "/redoc" |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__REDOC_URL` | str  \| None | "/redoc" |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.r` |
| `ORI_WEB__REDOC_URL` | str  \| None | "/redoc" |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.redoc_url` |
| `ORI_WEB__REFERRER_POLICY` | str | "strict-origin-when-cross-origin" | Referrer-Policy header value | `packages/oridecon-web/src/oridecon/web/security/config.py:SecurityConfig.referrer_policy` |
| `ORI_WEB__ROLE_GUARD__RULES` | list[RoleGuardRuleConfig] | (required) | Role guard rules in declaration order | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RoleGuard` |
| `ORI_WEB__ROLE_GUARD__RULES` | list[RoleGuardRuleConfig] | (required) | Role guard rules in declaration order | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:RoleGuardCo` |
| `ORI_WEB__ROLE_GUARD__RULES` | list[RoleGuardRuleConfig] | (required) | Role guard rules in declaration order | `packages/oridecon-web/src/oridecon/web/config.py:RoleGuardConfig.role_guard.rules` |
| `ORI_WEB__SECURITY` | SecurityConfig | (required) | Security configuration (HSTS, CSP, cross-origin, CSRF, headers) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__SECURITY` | SecurityConfig | (required) | Security configuration (HSTS, CSP, cross-origin, CSRF, headers) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.s` |
| `ORI_WEB__SECURITY` | SecurityConfig | (required) | Security configuration (HSTS, CSP, cross-origin, CSRF, headers) | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.security` |
| `ORI_WEB__SERVER__DEBUG` | bool | False | Enable debug mode | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerCon` |
| `ORI_WEB__SERVER__DEBUG` | bool | False | Enable debug mode | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerConfi` |
| `ORI_WEB__SERVER__DEBUG` | bool | False | Enable debug mode | `packages/oridecon-web/src/oridecon/web/config.py:ServerConfig.server.debug` |
| `ORI_WEB__SERVER__HOST` | str | (complex) | Bind host | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerCon` |
| `ORI_WEB__SERVER__HOST` | str | (complex) | Bind host | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerConfi` |
| `ORI_WEB__SERVER__HOST` | str | (complex) | Bind host | `packages/oridecon-web/src/oridecon/web/config.py:ServerConfig.server.host` |
| `ORI_WEB__SERVER__PORT` | int | (complex) | Bind port | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerCon` |
| `ORI_WEB__SERVER__PORT` | int | (complex) | Bind port | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerConfi` |
| `ORI_WEB__SERVER__PORT` | int | (complex) | Bind port | `packages/oridecon-web/src/oridecon/web/config.py:ServerConfig.server.port` |
| `ORI_WEB__SERVER__RELOAD` | bool | (complex) | Enable auto-reload | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerCon` |
| `ORI_WEB__SERVER__RELOAD` | bool | (complex) | Enable auto-reload | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerConfi` |
| `ORI_WEB__SERVER__RELOAD` | bool | (complex) | Enable auto-reload | `packages/oridecon-web/src/oridecon/web/config.py:ServerConfig.server.reload` |
| `ORI_WEB__SERVER__WORKERS` | int | (complex) | Number of workers | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerCon` |
| `ORI_WEB__SERVER__WORKERS` | int | (complex) | Number of workers | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:ServerConfi` |
| `ORI_WEB__SERVER__WORKERS` | int | (complex) | Number of workers | `packages/oridecon-web/src/oridecon/web/config.py:ServerConfig.server.workers` |
| `ORI_WEB__STATIC__DIRECTORY` | str | "static" | Directory to serve | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFil` |
| `ORI_WEB__STATIC__DIRECTORY` | str | "static" | Directory to serve | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFileC` |
| `ORI_WEB__STATIC__DIRECTORY` | str | "static" | Directory to serve | `packages/oridecon-web/src/oridecon/web/config.py:StaticFileConfig.static.directory` |
| `ORI_WEB__STATIC__ENABLED` | bool | False | Enable static file serving | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFil` |
| `ORI_WEB__STATIC__ENABLED` | bool | False | Enable static file serving | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFileC` |
| `ORI_WEB__STATIC__ENABLED` | bool | False | Enable static file serving | `packages/oridecon-web/src/oridecon/web/config.py:StaticFileConfig.static.enabled` |
| `ORI_WEB__STATIC__HTML` | bool | False | Serve HTML files (SPA mode) | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFil` |
| `ORI_WEB__STATIC__HTML` | bool | False | Serve HTML files (SPA mode) | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFileC` |
| `ORI_WEB__STATIC__HTML` | bool | False | Serve HTML files (SPA mode) | `packages/oridecon-web/src/oridecon/web/config.py:StaticFileConfig.static.html` |
| `ORI_WEB__STATIC__PREFIX` | str | "/static" | URL prefix for static files | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFil` |
| `ORI_WEB__STATIC__PREFIX` | str | "/static" | URL prefix for static files | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:StaticFileC` |
| `ORI_WEB__STATIC__PREFIX` | str | "/static" | URL prefix for static files | `packages/oridecon-web/src/oridecon/web/config.py:StaticFileConfig.static.prefix` |
| `ORI_WEB__SWAGGER_CSS_URL` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__SWAGGER_CSS_URL` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.s` |
| `ORI_WEB__SWAGGER_CSS_URL` | str  \| None | None |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.swagger_css_url` |
| `ORI_WEB__SWAGGER_JS_URL` | str  \| None | None |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__SWAGGER_JS_URL` | str  \| None | None |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.s` |
| `ORI_WEB__SWAGGER_JS_URL` | str  \| None | None |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.swagger_js_url` |
| `ORI_WEB__SWAGGER_UI_URL` | str  \| None | (complex) |  | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__SWAGGER_UI_URL` | str  \| None | (complex) |  | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.s` |
| `ORI_WEB__SWAGGER_UI_URL` | str  \| None | (complex) |  | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.swagger_ui_url` |
| `ORI_WEB__TEMPLATE_DIRECTORY` | str | "templates" | Directory for Jinja2 templates | `experimental/apps/oridecon-admin/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig` |
| `ORI_WEB__TEMPLATE_DIRECTORY` | str | "templates" | Directory for Jinja2 templates | `experimental/apps/oridecon-cli/.venv/lib/python3.13/site-packages/oridecon/web/config.py:WebConfig.t` |
| `ORI_WEB__TEMPLATE_DIRECTORY` | str | "templates" | Directory for Jinja2 templates | `packages/oridecon-web/src/oridecon/web/config.py:WebConfig.template_directory` |

## Non-Config ENV Sources

| Env Var | Source | Rationale |
|---------|--------|-----------|
| `ORI_DEBUG` | `core/oridecon/src/oridecon/logging/debug.py` | Early-boot logging toggle before typed config is available. |
| `ORI_QUIET` | `core/oridecon/src/oridecon/app/base.py` | Controls startup banner suppression during process bootstrap. |
| `ORI_CONFIG` | `experimental/apps/oridecon-cli/src/oridecon/cli/lib/config_loader.py` | CLI override for explicit configuration file path. |

---

*This document is auto-generated. Do not edit manually.*
