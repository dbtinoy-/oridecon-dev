"""Pivot data field for editable pivot columns in relation managers."""

from __future__ import annotations

from dataclasses import dataclass
import html as _html
from typing import Any

from oridecon.admin.schema.base import SchemaField
from oridecon.admin.schema.exceptions import FieldError
from oridecon.result import Ok, Result
from oridecon.serialization import dumps_str
from oridecon.ui import Element, get_render_scope


@dataclass(frozen=True, kw_only=True)
class PivotColumn:
    """Configuration for a single pivot column."""

    name: str
    label: str
    field_type: str = "text"
    required: bool = False
    default: str = ""


class PivotDataField(SchemaField):
    """Editable pivot columns displayed inline in a relation manager.

    Renders form fields for each pivot column.
    """

    def __init__(
        self,
        name: str,
        *,
        pivot_columns: list[PivotColumn] | None = None,
        related_id: str = "",
        **kwargs: Any,
    ) -> None:
        super().__init__(name=name, **kwargs)
        self._pivot_columns = pivot_columns or []
        self._related_id = related_id

    @property
    def pivot_columns(self) -> list[PivotColumn]:
        return self._pivot_columns

    def render_form(
        self, value: dict[str, Any] | None, *, errors: list[str] | None = None
    ) -> Element:
        data = value or {}
        scope = get_render_scope().child("pivot-data")
        field_key = f"{self.name}-{self._related_id}" if self._related_id else self.name
        group_id = scope.id("group", key=field_key)
        error_id = scope.id("error", key=field_key) if errors else None

        children: list[Element] = []
        for column in self.pivot_columns:
            current = data.get(column.name, column.default)
            input_id = scope.id("input", key=f"{field_key}-{column.name}")
            children.append(
                Element(
                    "div",
                    Element(
                        "label",
                        column.label,
                        for_=input_id,
                        class_="text-xs font-medium text-muted-foreground w-24",
                    ),
                    self._build_pivot_input(
                        column,
                        current,
                        input_id=input_id,
                        error_id=error_id,
                    ),
                    class_="flex items-center gap-2 mb-2",
                )
            )

        error_node = (
            Element("p", errors[0], id=error_id, class_="text-sm text-destructive")
            if errors
            else None
        )
        return Element(
            "div",
            *children,
            error_node,
            id=group_id,
            role="group",
            aria_label=self.label or self.name.replace("_", " ").title(),
            class_="pivot-data-fields",
        )

    def _build_pivot_input(
        self,
        column: PivotColumn,
        value: Any,
        *,
        input_id: str,
        error_id: str | None,
    ) -> Element:
        common: dict[str, Any] = {
            "id": input_id,
            "name": f"pivot_{column.name}",
            "required": column.required,
            "aria_invalid": "true" if error_id else None,
            "aria_describedby": error_id,
        }
        if column.field_type == "checkbox":
            return Element(
                "input",
                type="checkbox",
                checked=bool(value),
                class_="rounded border-border text-primary-600",
                **common,
            )
        if column.field_type == "select":
            text = str(value)
            return Element(
                "select",
                Element("option", text, value=text, selected=True),
                class_="px-2 py-1 text-sm border rounded",
                **common,
            )
        return Element(
            "input",
            type=str(column.field_type),
            value=str(value),
            class_="px-2 py-1 text-sm border rounded w-full",
            **common,
        )

    def render_column(self, record: Any, value: dict[str, Any] | None) -> Element:
        if value is None:
            return Element("span", "\u2014", class_="text-muted")
        parts = ", ".join(f"{k}={v}" for k, v in value.items())
        return Element("span", parts, class_="text-sm text-muted-foreground")

    def from_form(self, raw: str | None) -> Result[dict[str, Any] | None, FieldError]:
        if raw is None:
            return Ok(None)
        if isinstance(raw, dict):
            return Ok(dict(raw))
        return Ok({})

    def to_form(self, value: dict[str, Any] | None) -> str:
        return ""


class PivotTable:
    """Table organism showing related records with inline pivot editing.

    Renders a table where each row has the related record label,
    editable pivot columns, and detach action.
    """

    def __init__(
        self,
        pivot_columns: list[PivotColumn],
        rows: list[dict[str, Any]] | None = None,
    ):
        self.pivot_columns = pivot_columns
        self.rows = rows or []

    def render(
        self,
        resource_name: str = "",
        parent_id: str = "",
        admin_prefix: str = "/admin",
        csrf_token: str | None = None,
    ) -> str:
        """Render pivot controls using the configured admin mount prefix."""
        rel_name = "pivot"
        prefix = admin_prefix.rstrip("/") or "/admin"
        safe_resource = _html.escape(str(resource_name), quote=True)
        safe_parent = _html.escape(str(parent_id), quote=True)
        csrf_attr = ""
        if csrf_token:
            csrf_attr = (
                ' hx-headers="'
                + _html.escape(
                    dumps_str({"X-CSRF-Token": str(csrf_token)}),
                    quote=True,
                )
                + '"'
            )

        header_cols = "".join(
            f'<th class="px-4 py-2 text-left text-xs font-medium text-muted-foreground uppercase">'
            f"{_html.escape(str(c.label))}</th>"
            for c in self.pivot_columns
        )

        rows_html = ""
        for row in self.rows:
            related_id = _html.escape(str(row.get("id", "")), quote=True)
            label = _html.escape(str(row.get("label", row.get("id", ""))))

            pivot_cells = ""
            pivot_values = row.get("pivot") or {}
            for col in self.pivot_columns:
                value = pivot_values.get(col.name, col.default)
                safe_name = _html.escape(str(col.name), quote=True)
                safe_value = _html.escape(str(value), quote=True)
                pivot_url = (
                    f"{prefix}/{safe_resource}/{safe_parent}/relations/{rel_name}/"
                    f"pivot/{related_id}"
                )
                pivot_cells += f"""<td class="px-4 py-2">
                    <input type="text" class="px-2 py-1 text-sm border rounded w-full"
                           value="{safe_value}" name="pivot_{safe_name}"
                           hx-post="{pivot_url}"
                           hx-trigger="change" hx-swap="none"{csrf_attr} />
                </td>"""

            detach_url = f"{prefix}/{safe_resource}/{safe_parent}/relations/{rel_name}/{related_id}"
            rows_html += f"""<tr>
                <td class="px-4 py-2 text-sm font-medium text-foreground">{label}</td>
                {pivot_cells}
                <td class="px-4 py-2 text-sm">
                    <button type="button" class="text-destructive hover:text-destructive/90 text-sm"
                            hx-delete="{detach_url}"
                            hx-confirm="Detach this record?"
                            hx-target="closest tr" hx-swap="outerHTML"{csrf_attr}>Detach</button>
                </td>
            </tr>"""

        return f"""<table class="min-w-full divide-y divide-border">
            <thead class="bg-muted dark:bg-card">
                <tr>
                    <th class="px-4 py-2 text-left text-xs font-medium text-muted-foreground uppercase">Record</th>
                    {header_cols}
                    <th class="px-4 py-2 text-left text-xs font-medium text-muted-foreground uppercase">Actions</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-border">{rows_html}</tbody>
        </table>"""
