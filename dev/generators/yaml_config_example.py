#!/usr/bin/env python3
"""Generate application.example.yaml from docs/reference/REF_ENV_VARS.md.

Usage:
    uv run python dev/generators/yaml_config_example.py
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

_ROOT = Path(__file__).resolve().parents[2]

if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from dev.generators.env_example import _resolve_default, parse

ROOT = _ROOT
CATALOG = ROOT / "docs/reference/REF_ENV_VARS.md"
OUT = ROOT / "application.full.example.yaml"

PKG_HEADER = re.compile(r"^### `([^`]+)` \((\d+) vars\)$")

# Packages where env_prefix does NOT match the first env segment.
# Key = first lowercase segment after stripping ORI_, Value = YAML section key.
_PACKAGE_TO_YAML_SECTION: dict[str, str] = {
    "sql": "db",
}

# Package metadata: keyed by catalog pkg_name (e.g. "oridecon-sql").
# Value = (display_name, env_prefix_override_or_None)
_SECTION_META: dict[str, tuple[str, str | None]] = {
    "oridecon": ("Core Framework", None),
    "oridecon-sql": ("SQL Database", "ORI_SQL__"),
    "oridecon-cache": ("Cache", "ORI_CACHE__"),
    "oridecon-web": ("Web", "ORI_WEB__"),
    "oridecon-auth": ("Auth", "ORI_AUTH__"),
    "oridecon-events": ("Events", "ORI_EVENTS__"),
    "oridecon-graphql": ("GraphQL", "ORI_GRAPHQL__"),
    "oridecon-monitor": ("Monitor", "ORI_MONITOR__"),
    "oridecon-search": ("Search", "ORI_SEARCH__"),
    "oridecon-storage": ("Storage", "ORI_STORAGE__"),
    "oridecon-vector": ("Vector", "ORI_VECTOR__"),
    "oridecon-nosql": ("NoSQL", "ORI_NOSQL__"),
    "oridecon-graph": ("Graph", "ORI_GRAPH__"),
    "oridecon-tasks": ("Tasks", "ORI_TASKS__"),
    "oridecon-features": ("Features", "ORI_FEATURES__"),
    "oridecon-resilience": ("Resilience", "ORI_RESILIENCE__"),
    "oridecon-admin": ("Admin", "ORI_ADMIN__"),
    "oridecon-ai": ("AI", "ORI_AI__"),
    "oridecon-ai-rag": ("AI RAG", "ORI_AI_RAG__"),
    "oridecon-ai-memory": ("AI Memory", "ORI_AI_MEMORY__"),
    "oridecon-ai-session": ("AI Session", "ORI_AI_SESSION__"),
    "oridecon-ai-agents": ("AI Agents", "ORI_AI_AGENTS__"),
    "oridecon-ai-governance": ("AI Governance", "ORI_AI_GOVERNANCE__"),
    "oridecon-ai-guard": ("AI Guard", "ORI_AI_GUARD__"),
    "oridecon-ai-feedback": ("AI Feedback", "ORI_AI_FEEDBACK__"),
    "oridecon-ai-prompt": ("AI Prompt", "ORI_AI_PROMPT__"),
    "oridecon-ai-skills": ("AI Skills", "ORI_AI_SKILLS__"),
    "oridecon-ai-workers": ("AI Workers", "ORI_AI_WORKERS__"),
    "oridecon-ai-mcp": ("AI MCP", "ORI_AI_MCP__"),
    "oridecon-ai-observability": ("AI Observability", "ORI_AI_OBSERVABILITY__"),
    "oridecon-ai-evaluation": ("AI Evaluation", "ORI_AI_EVALUATION__"),
    "oridecon-ai-llm": ("AI LLM", "ORI_AI_LLM__"),
    "oridecon-audit": ("Audit", "ORI_AUDIT__"),
    "oridecon-http": ("HTTP Client", "ORI_HTTP__"),
    "oridecon-secrets": ("Secrets", "ORI_SECRETS_"),
    "oridecon-tenancy": ("Tenancy", "ORI_TENANCY__"),
    "oridecon-webhook": ("Webhook", "ORI_WEBHOOK__"),
    "oridecon-multimedia": ("Multimedia", None),
    "oridecon-ui": ("UI", "ORI_UI__"),
    "oridecon-cli": ("CLI", None),
    "oridecon-notification": ("Notification", "ORI_NOTIFICATION__"),
    "oridecon-testing": ("Testing", "ORI_TESTING__"),
    "oridecon-middleware": ("Middleware", "ORI_MIDDLEWARE__"),
    "oridecon-security": ("Security", "ORI_SECURITY__"),
    "oridecon-idempotency": ("Idempotency", "ORI_IDEMPOTENCY__"),
    "oridecon-mapping": ("Mapping", "ORI_MAPPING__"),
    "oridecon-workflow": ("Workflow", "ORI_WORKFLOW__"),
}

# Manual sections for vars not in the catalog (core config, etc.)
_MANUAL_SECTIONS: dict[str, str] = {
    "oridecon": """\
# ── Core Framework (oridecon) ──────────────────────────────────────────────────
# config_section: root (folded by OrideconConfig._fold_oridecon_env_section)
# Core config fields live at the root level of the YAML.
app_name: "oridecon-app"
debug: false
env: development
logging:
  level: info
  format: json
modules: []
discovery:
  auto_discover: true
  package_patterns:
    - "oridecon_*"
health:
  enabled: true
  path: /health
  detailed: false""",
}

# Packages where vars are direct env access (not config-derived) — emit as comments only.
_COMMENT_ONLY_SECTIONS = {"oridecon-testing"}

_SECRET_SUFFIXES = (
    "SECRET",
    "SECRET_KEY",
    "API_KEY",
    "PASSWORD",
    "TOKEN",
    "HMAC_KEY",
    "CREDENTIALS",
    "PRIVATE_KEY",
)


def _is_secret(env_var: str) -> bool:
    """Check if an env var name suggests it holds a secret."""
    return env_var.endswith(_SECRET_SUFFIXES) or "SECRET" in env_var or "API_KEY" in env_var


def _coerce_yaml_value(raw: str, _typ: str) -> str | int | float | bool | None:
    """Convert a string default to the appropriate Python/YAML type."""
    if raw in ("", "—", "(complex)", "None"):
        return None
    if raw.lower() in ("true", "false"):
        return raw.lower() == "true"
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        pass
    return raw


def _derive_env_prefix(env_var: str) -> str:
    """Derive the env_prefix from the first env var of a section."""
    if not env_var.startswith("ORI_"):
        return "ORI_"
    parts = env_var[4:].split("__")
    return "ORI_" + parts[0] + "__"


def env_var_to_yaml_path(env_var: str) -> list[str] | None:
    """Convert an env var name to a YAML key path.

    Args:
        env_var: Full env var name, e.g. ``ORI_AUTH__TOKEN__ALGORITHM``.

    Returns:
        List of YAML key segments, or None if the var should be skipped.
    """
    if not env_var.startswith("ORI_"):
        return None
    rest = env_var[4:]  # AUTH__TOKEN__ALGORITHM
    segments = rest.lower().split("__")
    first = segments[0]
    yaml_section = _PACKAGE_TO_YAML_SECTION.get(first, first)
    if not yaml_section:
        return None
    return [yaml_section, *segments[1:]]


def _group_by_nesting(rows: list[tuple[str, str, str, str]]) -> dict:
    """Group catalog rows into a nested dict keyed by YAML path segments."""
    tree: dict = {}
    for env_var, typ, default, desc in rows:
        path = env_var_to_yaml_path(env_var)
        if not path or len(path) < 2:
            continue
        node = tree
        for seg in path[1:-1]:
            node = node.setdefault(seg, {})
        value = _resolve_default(default)
        if _is_secret(env_var):
            value = "${" + env_var + "}"
        elif not value:
            value = None
        else:
            value = _coerce_yaml_value(value, typ)
        node[path[-1]] = {"_value": value, "_desc": desc}
    return tree


def _format_yaml_value(value: object) -> str:
    """Format a Python value for YAML output."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        if value.startswith("${"):
            return f'"{value}"'
        if value.lower() in ("true", "false", "null", "yes", "no"):
            return f'"{value}"'
        return f'"{value}"'
    return str(value)


def _emit_section(lines: list[str], tree: dict, indent: int) -> None:
    """Recursively emit a YAML section with proper indentation."""
    prefix = " " * indent
    for key in sorted(tree.keys()):
        node = tree[key]
        if isinstance(node, dict) and "_value" in node:
            value = node["_value"]
            desc = node["_desc"]
            val_str = _format_yaml_value(value)
            comment = f"  # {desc}" if desc else ""
            lines.append(f"{prefix}{key}: {val_str}{comment}")
        elif isinstance(node, dict):
            lines.append(f"{prefix}{key}:")
            _emit_section(lines, node, indent + 2)
        else:
            lines.append(f"{prefix}{key}: {_format_yaml_value(node)}")


def _emit_header() -> list[str]:
    return [
        "# ==============================================================================",
        "# application.example.yaml",
        "# Oridecon Framework — complete configuration reference.",
        "#",
        "# All values shown are exact defaults taken from each package's config class.",
        "# Secrets:  prefer environment variables or a vault over plaintext.",
        '#           Syntax: "${ENV_VAR_NAME}" lets the loader substitute at runtime.',
        "# Env-var overrides use double-underscore nesting, e.g.:",
        "#   ORI_WEB__SERVER__PORT=9000  →  web.server.port = 9000",
        "# ==============================================================================",
    ]


def generate() -> None:
    """Write application.example.yaml from the env var catalog."""
    sections = parse(CATALOG)

    pkg_vars = dict(sections)

    lines = _emit_header()

    # Emit manual sections first (core config, etc.)
    for pkg_name in sorted(_MANUAL_SECTIONS.keys()):
        if pkg_name in pkg_vars:
            lines.append("")
            lines.append(_MANUAL_SECTIONS[pkg_name])

    # Emit catalog-derived sections
    for pkg_name in sorted(pkg_vars.keys()):
        if pkg_name in _MANUAL_SECTIONS:
            continue  # already emitted
        rows = pkg_vars[pkg_name]
        if not rows:
            continue
        first_var = rows[0][0]
        path = env_var_to_yaml_path(first_var)
        if not path:
            continue
        yaml_section = path[0]
        display_name, prefix_override = _SECTION_META.get(
            pkg_name, (pkg_name.replace("oridecon-", "").replace("-", " ").title(), None)
        )
        env_prefix = prefix_override or _derive_env_prefix(first_var)

        lines.append("")
        sep_len = max(1, 70 - len(display_name) - len(pkg_name))
        lines.append(f"# ── {display_name} ({pkg_name}) ──" + "─" * sep_len)
        lines.append(f"# env_prefix: {env_prefix}")

        if pkg_name in _COMMENT_ONLY_SECTIONS:
            # Direct env vars — list as comments, not config fields
            for env_var, _typ, default, _desc in rows:
                val = _resolve_default(default) or "—"
                lines.append(f"# {env_var}={val}")
        else:
            lines.append(f"{yaml_section}:")
            nested = _group_by_nesting(rows)
            _emit_section(lines, nested, indent=2)

    OUT.write_text("\n".join(lines) + "\n")
    print(f"wrote {OUT} ({len(lines)} lines)")


if __name__ == "__main__":
    generate()
