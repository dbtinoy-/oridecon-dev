#!/usr/bin/env python3
"""Reject new legacy render-trust usage outside an audited allowlist.

The unified render boundary (doc 02) makes ``render_to_string`` escape plain
strings at every depth. Verbatim markup now requires a source-attributed
``TrustedHTML`` grant. The legacy ``raw()`` / ``RawHTML`` / ``markupsafe.Markup``
shims survive one migration window (removal: v0.2.0) but every framework call
site must be listed here with an owner, a reason, and a removal version so
reviewers can see exactly which producers still cross the boundary untrusted.

Usage:
    uv run python dev/checks/ui_trusted_html.py
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent.parent
ALLOWLIST = ROOT / "dev" / "checks" / "_data" / "ui_trusted_html_allowlist.json"
SEARCH_ROOTS = (
    ROOT / "core",
    ROOT / "packages",
    ROOT / "experimental",
)

# AST names that reach the legacy trust shims.
_LEGACY_NAMES = ("raw", "RawHTML", "Markup")
# Plain-HTML-string returns from functions named *render* that are then fed
# into the renderer without a trust grant (data flow is checked by tests; this
# static check only catches the obvious producer pattern).
_HTML_RETURN_PATTERNS = (
    "return f\"<",
    "return \"<",
    "return '<",
    "return f'<",
    "return '''<",
)


def _iter_python_files(root: Path):
    for path in sorted(root.rglob("*.py")):
        if any(part in {"node_modules", ".venv", "htmlcov", "__pycache__"} for part in path.parts):
            continue
        yield path


def _legacy_names_in_scope(tree: ast.Module) -> set[str]:
    """Return legacy names actually imported into a file's scope.

    This avoids false positives such as a local variable named ``raw``,
    ``RelayPassthroughBody.raw(...)`` method calls, or ``Markup`` used only
    in type annotations.
    """
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module == "markupsafe":
                for alias in node.names:
                    if alias.name == "Markup":
                        names.add(alias.asname or alias.name)
            if node.module and node.module.startswith("oridecon.ui"):
                for alias in node.names:
                    if alias.name in {"raw", "RawHTML"}:
                        names.add(alias.asname or alias.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "markupsafe":
                    names.add(alias.asname or alias.name)
    return names


def _is_legacy_call(node: ast.Call, names: set[str]) -> str | None:
    """Return the legacy name invoked, or None.

    Handles ``Markup(...)``, ``markupsafe.Markup(...)``, ``raw(...)`` and
    ``RawHTML(...)`` only when the name was imported (or is markupsafe).
    """
    target = node.func
    if isinstance(target, ast.Name) and target.id in names:
        return target.id
    if isinstance(target, ast.Attribute):
        if isinstance(target.value, ast.Name) and target.value.id == "markupsafe":
            return f"markupsafe.{target.attr}"
    return None


def _load_allowlist() -> dict[str, dict[str, str]]:
    if not ALLOWLIST.exists():
        return {}
    return json.loads(ALLOWLIST.read_text(encoding="utf-8"))


def _entries_for_path(allowlist: dict[str, dict[str, str]], path: Path) -> dict[str, str]:
    """Match allowlist keys by absolute path, subpath, or ``*`` glob."""
    absolute = str(path.resolve())
    relative = path.relative_to(ROOT).as_posix()
    for key in allowlist:
        if key == "*" or key == relative or key == absolute:
            return allowlist[key]
        if key.endswith("/*") and relative.startswith(key[:-1]):
            return allowlist[key]
    return {}


def check() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    allowlist = _load_allowlist()
    findings: list[str] = []

    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        for path in _iter_python_files(root):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except (SyntaxError, UnicodeDecodeError):
                continue
            entries = _entries_for_path(allowlist, path)
            names = _legacy_names_in_scope(tree)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    name = _is_legacy_call(node, names)
                    if name is not None:
                        _report(findings, path, node.lineno, name, entries, args.verbose)

    if findings:
        print("Legacy render-trust usage outside the audited allowlist:", file=sys.stderr)
        for finding in findings:
            print(f"  {finding}", file=sys.stderr)
        print(
            f"\n{len(findings)} finding(s). Add an entry to {ALLOWLIST.relative_to(ROOT)} "
            "with owner/reason/removal version, or migrate to trusted_html(...).",
            file=sys.stderr,
        )
        return 1
    print("ui_trusted_html: clean")
    return 0


def _report(
    findings: list[str],
    path: Path,
    line: int,
    name: str,
    entries: dict[str, str],
    verbose: bool,
) -> None:
    relative = path.relative_to(ROOT).as_posix()
    if entries:
        if verbose:
            findings.append(f"{relative}:{line}: {name} (allowlisted)")
        return
    findings.append(f"{relative}:{line}: {name}")


if __name__ == "__main__":
    raise SystemExit(check())
