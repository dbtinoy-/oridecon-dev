"""Component registry for oridecon-ui.

Maps component names to their source paths and dependencies,
mirroring ShadCN's registry concept for Python components.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ComponentEntry:
    """Metadata for a registrable UI component."""

    name: str
    description: str
    source_path: str
    dependencies: list[str] = field(default_factory=list)
    requires: list[str] = field(default_factory=list)


COMPONENT_REGISTRY: dict[str, ComponentEntry] = {
    "button": ComponentEntry(
        name="button",
        description="Button component with semantic color variants",
        source_path="oridecon/ui/atoms/button.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
    "badge": ComponentEntry(
        name="badge",
        description="Badge/chip with semantic color variants",
        source_path="oridecon/ui/atoms/badge.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
    "card": ComponentEntry(
        name="card",
        description="Card container with header, content, footer",
        source_path="oridecon/ui/molecules/card.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
    "input": ComponentEntry(
        name="input",
        description="Text input with label, error, and help text",
        source_path="oridecon/ui/atoms/inputs/text.py",
        dependencies=[
            "oridecon/ui/core/base.py",
            "oridecon/ui/atoms/inputs/base.py",
        ],
    ),
    "modal": ComponentEntry(
        name="modal",
        description="Modal dialog with backdrop and transitions",
        source_path="oridecon/ui/molecules/modal.py",
        dependencies=[
            "oridecon/ui/core/base.py",
            "oridecon/ui/atoms/button.py",
        ],
    ),
    "select": ComponentEntry(
        name="select",
        description="Dropdown select input",
        source_path="oridecon/ui/atoms/inputs/selection/select.py",
        dependencies=[
            "oridecon/ui/core/base.py",
            "oridecon/ui/atoms/inputs/base.py",
        ],
    ),
    "tabs": ComponentEntry(
        name="tabs",
        description="Tabbed interface",
        source_path="oridecon/ui/molecules/tabs.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
    "toast": ComponentEntry(
        name="toast",
        description="Toast notification",
        source_path="oridecon/ui/molecules/toast.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
    "tooltip": ComponentEntry(
        name="tooltip",
        description="CSS-only tooltip",
        source_path="oridecon/ui/atoms/tooltip.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
    "skeleton": ComponentEntry(
        name="skeleton",
        description="Loading skeleton placeholder",
        source_path="oridecon/ui/atoms/skeleton.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
    "form": ComponentEntry(
        name="form",
        description="Form with HTMX and validation",
        source_path="oridecon/ui/organisms/forms.py",
        dependencies=[
            "oridecon/ui/core/base.py",
            "oridecon/ui/atoms/button.py",
            "oridecon/ui/molecules/form_field.py",
        ],
    ),
    "pagination": ComponentEntry(
        name="pagination",
        description="Page navigation with next/previous",
        source_path="oridecon/ui/molecules/pagination.py",
        dependencies=["oridecon/ui/core/base.py"],
    ),
}
