"""Widget configuration popup rendering for the admin dashboard."""

from __future__ import annotations

from typing import Any

from oridecon.admin.dashboard.widget_types import ConfigField
from oridecon.ui import el, get_render_scope


def render_widget_config_popup(
    widget_name: str,
    title: str,
    fields: list[ConfigField],
    current_values: dict[str, Any],
    enabled: bool = True,
    admin_prefix: str = "/admin",
) -> str:
    """Render HTML for a widget config dialog."""
    scope = get_render_scope().child("widget-config")
    form_id = scope.id("form", key=widget_name)
    rows: list[Any] = [
        el(
            "label",
            el(
                "input",
                type_="checkbox",
                name="enabled",
                checked="checked" if enabled else None,
            ),
            " Show on dashboard",
            class_="flex items-center gap-2 text-sm mb-4",
        )
    ]

    for f in fields:
        if isinstance(f, dict):
            f = ConfigField(**f)
        value = current_values.get(f.name, f.default)
        field_id = scope.id("field", key=f"{widget_name}-{f.name}")
        rows.append(
            el(
                "div",
                el(
                    "label",
                    f.label,
                    for_=field_id,
                    class_="block text-sm font-medium mb-1",
                ),
                _render_field_input(f, value, input_id=field_id),
                class_="mb-3",
            ),
        )

    from oridecon.admin.ui.organisms.admin_slide_over import (
        render_slide_over_fragment,
    )

    config_endpoint = (
        (admin_prefix or "/admin").rstrip("/") or "/admin"
    ) + "/core/widgets/config"
    form = el(
        "form",
        *rows,
        el("input", type_="hidden", name="widget_name", value=widget_name),
        id=form_id,
        **{
            "hx-post": config_endpoint,
            "hx-swap": "none",
            "hx-on:htmx:after-request": "if(event.detail.successful){window.location.reload();}",
        },
        class_="space-y-3",
    )

    return render_slide_over_fragment(
        title=f"Configure: {title}",
        subtitle="Update this widget's settings.",
        content=form,
        size="md",
        footer=[
            el(
                "button",
                "Cancel",
                type_="button",
                **{"x-on:click": "open = false"},
                class_="inline-flex items-center rounded-lg px-4 py-2 text-sm font-medium text-foreground bg-card border border-border hover:bg-muted transition-colors",
            ),
            el(
                "button",
                "Save",
                type_="submit",
                form=form_id,
                class_="inline-flex items-center rounded-lg px-4 py-2 text-sm font-medium text-white bg-primary hover:bg-primary/90 transition-colors",
            ),
        ],
    )


def _render_field_input(
    field: ConfigField,
    current: Any,
    widget_name: str | None = None,
    *,
    input_id: str | None = None,
) -> Any:
    """Build a structured widget setting input."""
    prefix = f"param__{widget_name}__" if widget_name else "param_"
    common = {"id": input_id, "name": f"{prefix}{field.name}"}
    if field.type == "select" and field.options:
        return el(
            "select",
            *[
                el(
                    "option",
                    label,
                    value=str(value),
                    selected="selected" if value == current else None,
                )
                for value, label in field.options
            ],
            class_="w-full border rounded px-2 py-1 text-sm",
            **common,
        )
    if field.type == "number":
        return el(
            "input",
            type_="number",
            value=str(current) if current is not None else "",
            class_="w-full border rounded px-2 py-1 text-sm",
            **common,
        )
    if field.type == "boolean":
        return el(
            "input",
            type_="checkbox",
            checked="checked" if current else None,
            **common,
        )
    return el(
        "input",
        type_="text",
        value=str(current) if current is not None else "",
        class_="w-full border rounded px-2 py-1 text-sm",
        **common,
    )


__all__ = ["render_widget_config_popup"]
