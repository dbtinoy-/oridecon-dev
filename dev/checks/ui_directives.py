"""Reject Alpine directives that Python would render with dead syntax.

Alpine directive arguments are colon-delimited. Keyword spellings such as
``x_bind_value=...`` become ``x-bind-value`` and remain inert in the browser.
This AST check covers both the shared UI and admin source trees without
matching explanatory comments or docstrings. Runtime validation in
``Element.__html__`` provides the corresponding rendered-output boundary.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
import re
import sys

_INVALID_KEYWORD_PREFIXES = ("x_on_", "x_bind_", "x_transition_")
_COLON_FAMILIES = ("x-on", "x-bind", "x-transition")
_ARGUMENT = re.compile(r"^[a-z][a-z0-9:_-]*$")
_MODIFIER = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


@dataclass(frozen=True, order=True)
class DirectiveFinding:
    path: Path
    line: int
    name: str

    def format(self, root: Path) -> str:
        return f"{self.path.relative_to(root).as_posix()}:{self.line}: {self.name}"


def _invalid_keyword(name: str) -> bool:
    return name in {"x_on", "x_bind"} or name.startswith(_INVALID_KEYWORD_PREFIXES)


def _invalid_raw_name(name: str) -> bool:
    if not name.startswith("x-"):
        return False
    if name != name.lower() or "--" in name:
        return True

    for family in _COLON_FAMILIES:
        if name.startswith(f"{family}-"):
            return True
        if name.startswith(f"{family}:"):
            argument, *modifiers = name[len(family) + 1 :].split(".")
            return (
                not _ARGUMENT.fullmatch(argument)
                or any(not _MODIFIER.fullmatch(item) for item in modifiers)
                or len(set(modifiers)) != len(modifiers)
            )

    if name in {"x-on", "x-bind"} or name.startswith(("x-on.", "x-bind.")):
        return True
    if name.startswith("x-transition."):
        modifiers = name.removeprefix("x-transition.").split(".")
        return any(not _MODIFIER.fullmatch(item) for item in modifiers) or len(
            set(modifiers)
        ) != len(modifiers)
    return False


def scan_file(path: Path) -> list[DirectiveFinding]:
    """Return malformed Alpine keyword and literal dict-key attributes."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    findings: list[DirectiveFinding] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            findings.extend(
                DirectiveFinding(path, keyword.lineno, keyword.arg)
                for keyword in node.keywords
                if keyword.arg and _invalid_keyword(keyword.arg)
            )
        elif isinstance(node, ast.Dict):
            findings.extend(
                DirectiveFinding(path, key.lineno, key.value)
                for key in node.keys
                if isinstance(key, ast.Constant)
                and isinstance(key.value, str)
                and _invalid_raw_name(key.value)
            )
    return findings


def source_roots(root: Path) -> tuple[Path, ...]:
    return (
        root / "experimental/apps/oridecon-admin/src/oridecon/admin",
        root / "experimental/apps/oridecon-ui/src/oridecon/ui",
    )


def scan_sources(root: Path) -> list[DirectiveFinding]:
    """Scan all Python files in the product UI source roots."""
    return sorted(
        finding
        for source_root in source_roots(root)
        if source_root.exists()
        for path in source_root.rglob("*.py")
        for finding in scan_file(path)
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ui_directives")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    root = args.root.resolve()

    findings = scan_sources(root)
    for finding in findings:
        print(finding.format(root), file=sys.stderr)
    if findings:
        print(
            "use oridecon.ui.attributes.alpine or a canonical colon-delimited key",
            file=sys.stderr,
        )
        return 1

    print("UI directive syntax passed (admin + oridecon-ui)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
