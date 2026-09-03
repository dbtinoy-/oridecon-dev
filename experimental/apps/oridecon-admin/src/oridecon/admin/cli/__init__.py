"""Admin package CLI contributor and generators.

CLI is tooling, not a runtime API. Use the `oridecon-admin` console script.
"""

from __future__ import annotations

import os
import warnings

if not __name__.endswith(".__main__") and "_ORI_ADMIN_CLI_OK" not in os.environ:
    warnings.warn(
        "oridecon.admin.cli is tooling, not a runtime API. "
        "Use the `oridecon-admin` console script instead.",
        ImportWarning,
        stacklevel=2,
    )

from oridecon.admin.cli.contributor import AdminCliContributor
from oridecon.admin.cli.generators.admin_action import AdminActionGenerator
from oridecon.admin.cli.generators.admin_resource import AdminResourceGenerator

__all__ = ["AdminActionGenerator", "AdminCliContributor", "AdminResourceGenerator"]
