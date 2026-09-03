"""The tier check must be a path rule, not a name list.

Spec Task 15: a package under core/ or packages/ may not depend on one under
experimental/. Optional dependencies are exempt (oridecon[all] is opt-in).
"""

from __future__ import annotations

from pathlib import Path

from dev.checks.tier_boundary import violations


def _root_with_members(tmp_path: Path) -> Path:
    (tmp_path / "pyproject.toml").write_text(
        '[tool.uv.workspace]\nmembers = ["*/*", "*/*/*"]\n'
    )
    return tmp_path


def test_core_may_not_depend_on_experimental(tmp_path: Path) -> None:
    tmp_path = _root_with_members(tmp_path)
    pkg = tmp_path / "core" / "oridecon-x"
    pkg.mkdir(parents=True)
    (pkg / "pyproject.toml").write_text(
        '[project]\nname = "oridecon-x"\ndependencies = ["oridecon-admin"]\n'
    )
    target = tmp_path / "experimental" / "apps" / "oridecon-admin"
    target.mkdir(parents=True)
    (target / "pyproject.toml").write_text(
        '[project]\nname = "oridecon-admin"\ndependencies = []\n'
    )
    assert violations(tmp_path) == [("core/oridecon-x", "oridecon-admin")]


def test_optional_dependencies_are_exempt(tmp_path: Path) -> None:
    """`oridecon[all]` deliberately fans out to experimental packages."""
    tmp_path = _root_with_members(tmp_path)
    pkg = tmp_path / "core" / "oridecon"
    pkg.mkdir(parents=True)
    (pkg / "pyproject.toml").write_text(
        '[project]\nname = "oridecon"\ndependencies = []\n'
        '[project.optional-dependencies]\nall = ["oridecon-admin"]\n'
    )
    assert violations(tmp_path) == []


def test_package_does_not_report_itself(tmp_path: Path) -> None:
    tmp_path = _root_with_members(tmp_path)
    pkg = tmp_path / "experimental" / "apps" / "oridecon-ui"
    pkg.mkdir(parents=True)
    (pkg / "pyproject.toml").write_text(
        '[project]\nname = "oridecon-ui"\ndependencies = []\n'
    )
    assert violations(tmp_path) == []