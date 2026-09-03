from __future__ import annotations

from dev.audit.generators import env_vars as env_vars_audit


def test_env_audit_includes_non_config_sources_appendix() -> None:
    env_var_def = env_vars_audit.EnvVarDef
    generate_markdown = env_vars_audit.generate_markdown

    sample_packages = {
        "oridecon-web": [
            env_var_def(
                package="oridecon-web",
                env_var="ORI_WEB__HOST",
                type_annotation="str",
                default_value='"127.0.0.1"',
                description="Host binding for web server",
                source_file="oridecon-web/src/oridecon/web/config.py",
                source_class="WebConfig",
                source_field_path="host",
            )
        ]
    }

    markdown = generate_markdown(sample_packages)

    assert "## Non-Config ENV Sources" in markdown
    assert "`ORI_DEBUG`" in markdown
    assert "oridecon/src/oridecon/logging/debug.py" in markdown
