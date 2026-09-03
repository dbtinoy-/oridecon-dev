"""Static atom re-exports for the ``oridecon.ui`` public surface.

Type-checker only: the top-level package resolves names lazily via
``__getattr__`` at runtime, so these imports never execute eagerly.
"""

# File-level suppression: this module is an intentional lazy-re-export
# manifest — imports live under TYPE_CHECKING on purpose.
# ruff: noqa: TC004

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.ui.atoms.badge import Badge
    from oridecon.ui.atoms.button import Button, SubmitButton
    from oridecon.ui.atoms.divider import Divider
    from oridecon.ui.atoms.editors import MarkdownEditor, RichEditor
    from oridecon.ui.atoms.fieldset import Fieldset
    from oridecon.ui.atoms.file_upload import FileUpload
    from oridecon.ui.atoms.icon import Icon
    from oridecon.ui.atoms.inputs import (
        AbstractInput,
        AvatarUpload,
        BelongsTo,
        Checkbox,
        CheckboxList,
        ColorPicker,
        DateInput,
        EmailInput,
        Hidden,
        Input,
        KeyValueField,
        LazySelect,
        MorphTo,
        MultiFileUpload,
        MultiSelect,
        NativeMultiSelect,
        NumberInput,
        PasswordInput,
        Radio,
        Rating,
        Select,
        Slider,
        TagsInput,
        TextArea,
        TextInput,
        TimePicker,
        Toggle,
    )
    from oridecon.ui.atoms.label import Label
    from oridecon.ui.atoms.layout import Aside, Col, Container, Grid, Row
    from oridecon.ui.atoms.link import Link
    from oridecon.ui.atoms.progress_bar import ProgressBar
    from oridecon.ui.atoms.skeleton import Skeleton
    from oridecon.ui.atoms.spinner import Spinner
    from oridecon.ui.atoms.switch import Switch
    from oridecon.ui.atoms.tooltip import Tooltip

    __all__ = (
        "Badge",
        "Button",
        "SubmitButton",
        "Divider",
        "MarkdownEditor",
        "RichEditor",
        "Fieldset",
        "FileUpload",
        "Icon",
        "AbstractInput",
        "AvatarUpload",
        "BelongsTo",
        "Checkbox",
        "CheckboxList",
        "ColorPicker",
        "DateInput",
        "EmailInput",
        "Hidden",
        "Input",
        "KeyValueField",
        "LazySelect",
        "MorphTo",
        "MultiFileUpload",
        "MultiSelect",
        "NativeMultiSelect",
        "NumberInput",
        "PasswordInput",
        "Radio",
        "Rating",
        "Select",
        "Slider",
        "TagsInput",
        "TextArea",
        "TextInput",
        "TimePicker",
        "Toggle",
        "Label",
        "Aside",
        "Col",
        "Container",
        "Grid",
        "Row",
        "Link",
        "ProgressBar",
        "Skeleton",
        "Spinner",
        "Switch",
        "Tooltip",
    )
