"""FieldSchema molecule component - wrapper for form inputs with label and error."""

from __future__ import annotations

from copy import copy
from typing import Any

from oridecon.ui.core.base import Component, el


class FormField(Component):
    """Form field wrapper with label, input, error message, and help text."""

    """Form field wrapper with label, input, error message, and help text."""

    def __init__(
        self,
        input_component: Component,
        label: str | None = None,
        error: str | None = None,
        help_text: str | None = None,
        hint: str | None = None,
        required: bool = False,
        hidden: bool = False,
        visible_condition: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(
            input_component=input_component,
            label=label,
            error=error,
            help_text=help_text,
            hint=hint,
            required=required,
            hidden=hidden,
            visible_condition=visible_condition,
            **props,
        )
        self.input_component = input_component
        self.label = label
        self.error = error
        self.help_text = help_text
        self.hint = hint
        self.required = required
        self.hidden = hidden
        self.visible_condition = visible_condition

    def render(self) -> Any:
        # Decorate a shallow clone so rendering a FormField never mutates a
        # reusable input component supplied by its caller.
        input_component = copy(self.input_component)
        input_component.props = dict(self.input_component.props)

        # Build container attributes
        container_attrs: dict[str, Any] = {"class": "mb-6"}
        input_id = (
            getattr(input_component, "id", None)
            or getattr(input_component, "input_id", None)
            or getattr(input_component, "name", None)
            or "field"
        )

        described_by: list[str] = []
        existing_description = input_component.props.pop(
            "aria_describedby",
            input_component.props.get("aria-describedby"),
        )
        if existing_description:
            described_by.extend(str(existing_description).split())
        if self.help_text:
            described_by.append(f"{input_id}-help")
        if self.error:
            described_by.append(f"{input_id}-error")
            input_component.props["aria-invalid"] = "true"
        if described_by:
            input_component.props["aria-describedby"] = " ".join(
                dict.fromkeys(described_by)
            )

        required_if = self.props.get("required_if")
        if required_if:
            input_component.props["x-bind:required"] = required_if
            input_component.props["x-bind:aria-required"] = f"Boolean({required_if})"
        elif self.required:
            input_component.props["aria-required"] = "true"
            if hasattr(input_component, "required"):
                input_component.required = True

        # Handle hidden state
        if self.hidden:
            container_attrs["style"] = "display: none"

        # Handle conditional visibility (Alpine.js)
        if self.visible_condition:
            container_attrs["x-show"] = self.visible_condition
            container_attrs["x-cloak"] = True

        elements = []

        # Header (Label + Hint)
        if self.label or self.hint:
            header_parts = []

            if self.label:
                label_text = self.label

                # Dynamic requirement asterisk
                if required_if:
                    header_parts.append(
                        el(
                            "label",
                            label_text,
                            el(
                                "span",
                                "*",
                                class_="text-destructive ml-1",
                                aria_hidden="true",
                                **{"x-show": required_if},
                            ),
                            for_=input_id,
                            class_="block text-sm font-medium text-foreground",
                        ),
                    )
                elif self.required:
                    header_parts.append(
                        el(
                            "label",
                            label_text,
                            el(
                                "span",
                                "*",
                                class_="text-destructive ml-1",
                                aria_hidden="true",
                            ),
                            for_=input_id,
                            class_="block text-sm font-medium text-foreground",
                        ),
                    )
                else:
                    header_parts.append(
                        el(
                            "label",
                            label_text,
                            for_=input_id,
                            class_="block text-sm font-medium text-foreground",
                        ),
                    )

            if self.hint:
                header_parts.append(
                    el(
                        "span",
                        self.hint,
                        class_="text-xs text-muted-foreground italic",
                        title=self.hint,
                    ),
                )

            elements.append(
                el(
                    "div",
                    *header_parts,
                    class_="flex items-center justify-between mb-2",
                ),
            )

        # Keep the input structured so the normal renderer owns failures and
        # escaping. Broken form controls must not be replaced by a generic box
        # that makes the form appear usable.
        elements.append(input_component)

        # Error message
        if self.error:
            error_id = f"{input_id}-error"
            elements.append(
                el(
                    "p",
                    self.error,
                    id=error_id,
                    role="alert",
                    class_="mt-2 text-sm text-destructive font-medium",
                ),
            )

        # Help remains available when validation errors are shown; the control
        # references both descriptions in deterministic order.
        if self.help_text:
            elements.append(
                el(
                    "p",
                    self.help_text,
                    id=f"{input_id}-help",
                    class_="mt-2 text-sm text-muted-foreground",
                ),
            )

        return el("div", *elements, **container_attrs)


FieldSchema = FormField
