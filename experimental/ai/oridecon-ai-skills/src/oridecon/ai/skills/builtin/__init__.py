"""Built-in skill implementations for the Oridecon skills package."""

from __future__ import annotations

from oridecon.ai.skills.builtin.code_execution import CodeExecutionSkill
from oridecon.ai.skills.builtin.database_query import DatabaseQuerySkill
from oridecon.ai.skills.builtin.datetime_skill import DatetimeSkill
from oridecon.ai.skills.builtin.file_operations import FileReadSkill, FileWriteSkill
from oridecon.ai.skills.builtin.http_request import HTTPRequestSkill
from oridecon.ai.skills.builtin.math_skill import MathSkill
from oridecon.ai.skills.builtin.text_processing import (
    TextSummarizeSkill,
    TextTranslateSkill,
)
from oridecon.ai.skills.builtin.web_search import WebSearchSkill

DateTimeSkill = DatetimeSkill
HttpRequestSkill = HTTPRequestSkill

__all__ = [
    "CodeExecutionSkill",
    "DatabaseQuerySkill",
    "DateTimeSkill",
    "DatetimeSkill",
    "FileReadSkill",
    "FileWriteSkill",
    "HTTPRequestSkill",
    "HttpRequestSkill",
    "MathSkill",
    "TextSummarizeSkill",
    "TextTranslateSkill",
    "WebSearchSkill",
]
