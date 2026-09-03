"""
Input components for admin UI.

All inputs inherit from AbstractInput for consistent styling.
"""

from __future__ import annotations

from oridecon.ui.atoms.inputs.base import AbstractInput
from oridecon.ui.atoms.inputs.date import DateInput
from oridecon.ui.atoms.inputs.file import (
    AvatarUpload,
    FileUpload,
    MultiFileUpload,
)
from oridecon.ui.atoms.inputs.numeric import NumberInput, Slider
from oridecon.ui.atoms.inputs.selection import (
    BelongsTo,
    CheckboxList,
    LazySelect,
    MorphTo,
    MultiSelect,
    NativeMultiSelect,
    Radio,
    Select,
)
from oridecon.ui.atoms.inputs.special import (
    ColorPicker,
    Hidden,
    KeyValueField,
    Rating,
    TagsInput,
    TimePicker,
)
from oridecon.ui.atoms.inputs.text import (
    EmailInput,
    Input,
    PasswordInput,
    TextArea,
    TextInput,
)
from oridecon.ui.atoms.inputs.toggle import Checkbox, Toggle

__all__ = [
    # Base
    "AbstractInput",
    "AvatarUpload",
    "BelongsTo",
    "Checkbox",
    "CheckboxList",
    # Special
    "ColorPicker",
    # Date/Time
    "DateInput",
    "EmailInput",
    # File
    "FileUpload",
    "Hidden",
    "Input",
    "KeyValueField",
    "LazySelect",
    "MorphTo",
    "MultiFileUpload",
    "MultiSelect",
    "NativeMultiSelect",
    # Numeric
    "NumberInput",
    "PasswordInput",
    "Radio",
    "Rating",
    # Selection
    "Select",
    "Slider",
    "TagsInput",
    "TextArea",
    # Text
    "TextInput",
    "TimePicker",
    # Toggle
    "Toggle",
]
