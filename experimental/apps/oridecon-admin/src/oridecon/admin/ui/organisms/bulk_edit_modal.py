"""
Bulk Edit Slide-Over Component.

Provides UI for bulk editing multiple records with field updates.
Now rendered as a slide-over panel consistent with the unified overlay system.
"""

from __future__ import annotations

from typing import Any

from htpy import div, form, label, option, p, select

from oridecon.admin.actions.bulk_manager import BulkEditField
from oridecon.admin.ui.organisms.admin_slide_over import render_slide_over_fragment
from oridecon.ui import Button, Zones, el, get_render_scope, js_string


def bulk_edit_modal(
    selected_count: int,
    fields: list[BulkEditField],
    action_url: str,
    preview_items: list[str] | None = None,
    *,
    hx_target: str | None = None,
    modal_key: str | None = None,
) -> str:
    """
    Render a bulk-edit slide-over panel.

    Args:
        selected_count: Number of selected records
        fields: List of editable fields
        action_url: URL to submit the form to
        preview_items: Optional list of item labels for preview

    Returns:
        HTML string for the SlideOver zone (``#slide-over-container``)
    """
    identity_key = modal_key or action_url or "default"
    scope = get_render_scope().child("bulk-edit")
    form_id = scope.id("form", key=identity_key)
    field_nodes = [
        _render_field_node(
            field,
            field_id=scope.id(
                "field",
                key=f"{identity_key}-{index}-{field.name}",
            ),
        )
        for index, field in enumerate(fields)
    ]

    preview_block: Any = ""
    if preview_items:
        preview_block = el(
            "div",
            {
                "class": "mb-5 rounded-xl bg-primary-50 dark:bg-primary-950/30 "
                "border border-primary-200 dark:border-primary-800/50 p-4",
            },
            el(
                "p",
                {
                    "class": "text-sm font-semibold text-primary-800 dark:text-primary-200 mb-2"
                },
                "Selected records:",
            ),
            el(
                "div",
                {"class": "space-y-1"},
                *[
                    el(
                        "p",
                        {
                            "class": "text-sm text-primary-700 dark:text-primary-300 truncate"
                        },
                        f"• {item}",
                    )
                    for item in preview_items[:5]
                ],
                *(
                    [
                        el(
                            "p",
                            {"class": "text-xs text-primary-500 mt-1"},
                            f"…and {len(preview_items) - 5} more",
                        )
                    ]
                    if len(preview_items) > 5
                    else []
                ),
            ),
        )

    body = el(
        "div",
        {"class": "space-y-5"},
        preview_block,
        el(
            "form",
            el("div", *field_nodes, class_="space-y-4"),
            id=form_id,
            hx_post=action_url,
            hx_target=hx_target or Zones.DATA.selector,
            hx_swap="outerHTML",
        ),
    )

    cancel_btn = el(
        "button",
        {
            "type": "button",
            "x-on:click": "open = false",
            "class": (
                "inline-flex items-center rounded-lg px-4 py-2 text-sm font-medium "
                "text-foreground bg-card "
                "border border-border "
                "hover:bg-muted dark:hover:bg-muted transition-colors"
            ),
        },
        "Cancel",
    )
    submit_btn = el(
        "button",
        {
            "type": "submit",
            "form": form_id,
            "x-on:click": "open = false",
            "class": (
                "inline-flex items-center rounded-lg px-4 py-2 text-sm font-medium "
                "text-white bg-primary-600 hover:bg-primary-700 "
                "focus:outline-none focus:ring-2 focus:ring-primary-500 "
                "transition-colors shadow-sm"
            ),
        },
        "Update Records",
    )

    return render_slide_over_fragment(
        title=f"Bulk Edit {selected_count} Record{'s' if selected_count != 1 else ''}",
        content=body,
        subtitle="Changes will be applied to all selected records.",
        footer=[cancel_btn, submit_btn],
        size="xl",
    )


def _render_field_node(field: BulkEditField, *, field_id: str) -> Any:
    """Build one escaped, structured field for the bulk-edit form."""
    input_class = (
        "mt-1 block w-full rounded-lg border border-border "
        "bg-card text-foreground px-3 py-2 text-sm "
        "focus:outline-none focus:ring-2 focus:ring-primary-500 transition-colors"
    )
    label_node = el(
        "label",
        field.label,
        (
            el("span", "*", class_="text-destructive ml-0.5", aria_hidden=True)
            if field.required
            else ""
        ),
        for_=field_id,
        class_="block text-sm font-medium text-foreground mb-1",
    )

    common = {
        "id": field_id,
        "name": field.name,
        "required": field.required,
        "class_": input_class,
    }
    if field.field_type == "select" and field.options:
        input_node = el(
            "select",
            el("option", "-- No change --", value=""),
            *[
                el("option", option_label, value=str(value))
                for value, option_label in field.options
            ],
            **common,
        )
    elif field.field_type == "textarea":
        input_node = el("textarea", rows="3", **common)
    elif field.field_type == "checkbox":
        common["class_"] = (
            "mt-1 h-4 w-4 rounded border-border text-primary-600 focus:ring-primary-500"
        )
        input_node = el("input", type="checkbox", value="true", **common)
    else:
        input_node = el("input", type=field.field_type, **common)

    help_node = (
        el("p", field.help_text, class_="mt-1 text-xs text-muted-foreground")
        if field.help_text
        else ""
    )
    return el("div", label_node, input_node, help_node, class_="space-y-1")


def bulk_assign_modal(
    selected_count: int,
    field_label: str,
    options: list[tuple[Any, str]],
    action_url: str,
    field_name: str = "value",
    allow_null: bool = False,
    confirm_message: str | None = None,
    *,
    hx_target: str | None = None,
    modal_key: str | None = None,
) -> Any:
    """
    Render a modal for bulk assign operations (status, owner, etc.).

    Args:
        selected_count: Number of selected records
        field_label: Label for the field being assigned
        options: List of (value, label) tuples
        action_url: URL to submit the form to
        field_name: Name attribute for the select field
        allow_null: Whether to show "Unassign" option
        confirm_message: Optional custom confirmation message

    Returns:
        htpy component for the modal
    """
    identity_key = modal_key or f"{action_url}-{field_name}"
    scope = get_render_scope().child("bulk-assign")
    modal_id = scope.id("modal", key=identity_key)
    form_id = scope.id("form", key=identity_key)
    value_id = scope.id("value", key=identity_key)
    close_script = (
        f"document.getElementById({js_string(modal_id)}).classList.add('hidden')"
    )

    return div(
        class_="fixed inset-0 bg-muted bg-opacity-50 hidden",
        id=modal_id,
    )[
        div(class_="flex items-center justify-center min-h-screen px-4")[
            div(
                class_="bg-card rounded-lg shadow-xl max-w-lg w-full",
            )[
                # Header
                div(class_="px-6 py-4 border-b border-border")[
                    div(class_="flex items-center justify-between")[
                        p(class_="text-lg font-semibold text-foreground")[
                            f"Bulk Assign {field_label}"
                        ],
                        Button(
                            "✕",
                            type="button",
                            variant="ghost",
                            onclick=close_script,
                            aria_label="Close bulk assignment",
                        ),
                    ],
                ],
                # Body
                div(class_="px-6 py-4")[
                    (
                        div(
                            class_="mb-4 p-3 bg-warning/10 rounded-lg",
                        )[
                            p(class_="text-sm text-warning")[
                                confirm_message
                                or f"This will update {selected_count} record(s)."
                            ]
                        ]
                    ),
                    form(
                        id=form_id,
                        hx_post=action_url,
                        hx_target=hx_target or Zones.DATA.selector,
                        hx_swap="outerHTML",
                    )[
                        label(
                            for_=value_id,
                            class_="block text-sm font-medium text-foreground mb-2",
                        )[f"Select {field_label}"],
                        select(
                            id=value_id,
                            name=field_name,
                            required=not allow_null,
                            class_="block w-full rounded-md border-border dark:bg-muted dark:text-foreground shadow-sm focus:border-ring focus:ring-ring",
                        )[
                            (
                                option(value="", selected=True)["-- Unassign --"]
                                if allow_null
                                else None
                            ),
                            [
                                option(value=str(val))[label_text]
                                for val, label_text in options
                            ],
                        ],
                    ],
                ],
                # Footer
                div(
                    class_="px-6 py-4 border-t border-border flex justify-end space-x-3",
                )[
                    Button(
                        "Cancel",
                        type="button",
                        variant="secondary",
                        onclick=close_script,
                    ),
                    Button(
                        "Assign",
                        type="submit",
                        form=form_id,
                        onclick=close_script,
                    ),
                ],
            ]
        ]
    ]


def bulk_confirm_dialog(
    action_name: str,
    selected_count: int,
    preview_items: list[str] | None = None,
    is_danger: bool = False,
    action_url: str = "",
    *,
    hx_target: str | None = None,
    dialog_key: str | None = None,
) -> Any:
    """
    Render a confirmation dialog for bulk actions.

    Args:
        action_name: Name of the action (e.g., "delete", "archive")
        selected_count: Number of selected records
        preview_items: Optional preview of affected items
        is_danger: Whether this is a dangerous action (red styling)
        action_url: URL to submit the action to

    Returns:
        htpy component for the confirmation dialog
    """
    identity_key = dialog_key or f"{action_url}-{action_name}"
    dialog_id = (
        get_render_scope()
        .child("bulk-confirm")
        .id(
            "dialog",
            key=identity_key,
        )
    )
    close_script = (
        f"document.getElementById({js_string(dialog_id)}).classList.add('hidden')"
    )

    return div(
        class_="fixed inset-0 bg-muted bg-opacity-50 hidden",
        id=dialog_id,
    )[
        div(class_="flex items-center justify-center min-h-screen px-4")[
            div(
                class_="bg-card rounded-lg shadow-xl max-w-md w-full",
            )[
                # Header
                div(class_="px-6 py-4")[
                    p(class_="text-lg font-semibold text-foreground")[
                        f"Confirm {action_name.title()}"
                    ],
                    p(class_="mt-2 text-sm text-muted-foreground")[
                        f"Are you sure you want to {action_name} {selected_count} record(s)?"
                    ],
                ],
                # Preview
                (
                    div(class_="px-6 py-2")[
                        div(
                            class_="max-h-40 overflow-y-auto border border-border rounded p-3 bg-muted dark:bg-background",
                        )[
                            [
                                p(
                                    class_="text-sm text-foreground truncate",
                                )[f"• {item}"]
                                for item in (preview_items or [])[:10]
                            ],
                            (
                                p(
                                    class_="text-sm text-muted-foreground mt-2",
                                )[f"...and {len(preview_items) - 10} more"]
                                if preview_items and len(preview_items) > 10
                                else None
                            ),
                        ]
                    ]
                    if preview_items
                    else None
                ),
                # Footer
                div(
                    class_="px-6 py-4 border-t border-border flex justify-end space-x-3",
                )[
                    Button(
                        "Cancel",
                        type="button",
                        variant="secondary",
                        onclick=close_script,
                    ),
                    Button(
                        action_name.title(),
                        type="button",
                        variant="destructive" if is_danger else "default",
                        hx_post=action_url,
                        hx_target=hx_target or Zones.DATA.selector,
                        hx_swap="outerHTML",
                        onclick=close_script,
                    ),
                ],
            ]
        ]
    ]


def bulk_progress_indicator(
    action_name: str,
    progress_url: str,
    *,
    progress_key: str | None = None,
) -> Any:
    """
    Render a progress indicator for slow bulk actions.

    Polls the progress_url to update the progress bar.

    Args:
        action_name: Name of the action being performed
        progress_url: URL to poll for progress updates

    Returns:
        htpy component for the progress indicator
    """
    identity_key = progress_key or f"{progress_url}-{action_name}"
    scope = get_render_scope().child("bulk-progress")
    root_id = scope.id("root", key=identity_key)
    bar_id = scope.id("bar", key=identity_key)
    status_id = scope.id("status", key=identity_key)
    errors_id = scope.id("errors", key=identity_key)

    return div(
        class_="fixed inset-0 bg-muted bg-opacity-50 flex items-center justify-center",
        id=root_id,
    )[
        div(
            class_="bg-card rounded-lg shadow-xl max-w-md w-full p-6",
        )[
            p(class_="text-lg font-semibold text-foreground mb-4")[
                f"{action_name.title()} in Progress..."
            ],
            # Progress bar
            div(class_="w-full bg-muted rounded-full h-2.5 mb-2")[
                div(
                    id=bar_id,
                    class_="bg-primary h-2.5 rounded-full transition-all duration-300",
                    style="width: 0%",
                )
            ],
            # Status text
            div(
                id=status_id,
                class_="text-sm text-muted-foreground text-center",
                hx_get=progress_url,
                hx_trigger="every 500ms",
                hx_swap="innerHTML",
            )["Starting..."],
            # Errors
            div(
                id=errors_id,
                class_="mt-4 text-sm text-destructive",
            ),
        ]
    ]
