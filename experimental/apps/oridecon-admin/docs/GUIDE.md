# Guide

Welcome to `oridecon-admin` — a Python-first admin framework for the Oridecon ecosystem.

## Overview

`oridecon-admin` provides auto-generated CRUD interfaces, dashboards, bulk
actions, RBAC, and extension points — all with zero frontend code. It is
built on `oridecon-ui` for responsive HTMX-driven components and integrates
with the broader Oridecon framework for identity, tenancy, caching, search,
and background tasks.

## When to use it

- You need an admin panel for your domain models — Resource CRUD with
  fields, actions, relations, permissions, and search.
- You are writing a plugin that should contribute resources, pages, widgets,
  or navigation to an existing admin installation.
- You need a contributor system where third-party packages can add admin
  capabilities without modifying the host application.

## Core Concepts

- **Resource** — Declarative class that models an admin entity. Configures
  fields, actions, relations, permissions, and data source.
- **SchemaField** — Single source of truth for form input, table column, and
  filter widget rendering.
- **Action** — Stateful work unit: row-level (`RowAction`), selection-level
  (`BulkAction`), or header-level (`HeaderAction`).
- **Page** — Unit of routing. Built-in: List, Create, Edit, View.
- **Cluster** — Navigation grouping for resources and custom pages.
- **RelationManager** — Inline related-record editor on ViewPage.
- **Contributor** — Extension point via `BaseAdminContributor` for plugins
  to contribute resources, pages, widgets, navigation, routes, settings.

## Typical Usage

```python
from oridecon.admin import AdminModule
from oridecon.admin.resources.base import Resource
from oridecon.admin.schema import TextField, EmailField, DateField

class UserResource(Resource):
    model = User
    name = "users"
    cluster = "users"
    fields = [
        TextField("name", required=True, sortable=True),
        EmailField("email", required=True),
        DateField("created_at", sortable=True),
    ]

module = AdminModule.configure(resources=[UserResource])
```

## Common Patterns

### Pattern: Custom actions

```python
from oridecon.admin.actions.base import RowAction
from oridecon.admin.actions.types import ActionColor, ActionContext
from oridecon.result import Ok

class PublishAction(RowAction):
    def __init__(self):
        super().__init__(name="publish", label="Publish", icon="send", color=ActionColor.SUCCESS)

    async def execute(self, record, ctx: ActionContext):
        await publish_service.publish(record.id)
        return Ok({"message": f"Published #{record.id}"})
```

### Pattern: Custom page

```python
from oridecon.admin.pages.base import Page
from oridecon.admin.pages.types import PageResponse

class DashboardPage(Page):
    title = "Dashboard"
    path = "/admin/dashboard"

    async def view(self, request):
        return PageResponse(title=self.title, content="<div>Hello</div>")
```

### Pattern: Plugin contributor

```python
from oridecon.contracts.admin import BaseAdminContributor

class MyContributor(BaseAdminContributor):
    name = "my_plugin"
    display_name = "My Plugin"
    package_source = "my_plugin"

    def get_resources(self):
        return [MyResource]
```

## Integration

`oridecon-admin` integrates with:

- **oridecon-auth** — identity, sessions, OAuth, RBAC
- **oridecon-cache** — resource cacheability (`Resource.cacheable = True`)
- **oridecon-tasks** — background task execution for bulk actions
- **oridecon-search** — resource search indexing
- **oridecon-tenancy** — multi-tenant resource scoping
- **oridecon-monitor** — metrics and health checks

## Best Practices

- ✅ Use `fields` (not legacy `columns`/`filters`/`form_class`)
- ✅ Define a `cluster` for every Resource
- ✅ Use `SchemaField` validators for form validation
- ✅ Return `Result[Outcome, ActionError]` from action `execute()`
- ✅ Set `search_fields` on listable Resources
- ✅ Namespace contributed names with a `package_source` prefix
- ❌ Do not use `Result.unwrap()` without an `is_ok()` check
- ❌ Do not wrap infrastructure exceptions in Result — raise them
- ❌ Do not use `if/elif` chains for dispatch — use registries

## Next Steps

- [Quickstart](./QUICKSTART.md)
- [How-Tos](./HOWTOS.md)
- [Configuration](./CONFIGURATION.md)
- [Architecture](./ARCHITECTURE.md)
- [Resources](./RESOURCES.md)
- [Extension Developer Guide](./EXTENSION_DEVELOPER_GUIDE.md)
- [Contributor Reference](./CONTRIBUTOR_REFERENCE.md)
- [Framework Composition](./FRAMEWORK_COMPOSITION.md)
- [Troubleshooting](./TROUBLESHOOTING.md)
