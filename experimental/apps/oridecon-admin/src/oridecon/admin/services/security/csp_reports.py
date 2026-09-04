"""CSP violation report ingestion (CSP v2 groundwork, docs/09-01-2026/30).

Browsers post violation reports for the ``Content-Security-Policy-Report-Only``
candidate policy emitted by :mod:`oridecon.admin.middleware.security_headers`.
This module normalizes both wire formats (legacy ``application/csp-report``
and the modern Reporting API ``application/reports+json``), dedupes them into
a capped in-memory store, and exposes a superuser-only JSON summary so
operators can drive the strict policy's violations to zero before enforcing
it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from starlette.responses import JSONResponse, PlainTextResponse, Response

from oridecon.logging import get_logger
from oridecon.serialization import loads

if TYPE_CHECKING:
    from starlette.requests import Request

logger = get_logger(__name__)

#: Maximum accepted report body size (bytes). Reports are tiny; anything
#: larger is hostile or broken.
MAX_REPORT_BODY_BYTES = 32 * 1024

#: Maximum distinct violation signatures retained (oldest evicted).
MAX_SIGNATURES = 200

#: Violation class labels returned by :func:`classify_csp_violation`.
KNOWN_ALPINE_EVAL = "known-alpine-eval"
KNOWN_INLINE_SCRIPT = "known-inline-script"
KNOWN_INLINE_STYLE = "known-inline-style"
UNEXPECTED = "unexpected"

_SCRIPT_DIRECTIVES = frozenset({"script-src", "script-src-elem"})
_STYLE_DIRECTIVES = frozenset({"style-src", "style-src-elem", "style-src-attr"})

#: Blocked-uri value browsers report for inline content.
_INLINE_URI = "inline"

_ALPINE_ASSET = "alpine.min.js"


def classify_csp_violation(report: dict[str, Any]) -> str:
    """Classify a normalized violation against the known CSP-v2 blockers.

    The report-only candidate (``STRICT_CSP``) deliberately omits
    ``'unsafe-inline'``/``'unsafe-eval'`` (docs/09-01-2026/14 §3, 30), so the
    stock admin is expected to produce exactly three classes:

    - ``known-alpine-eval`` — the vendored standard Alpine build compiles
      directive expressions via the ``Function`` constructor;
    - ``known-inline-script`` — shell/component inline ``<script>`` blocks;
    - ``known-inline-style`` — inline ``<style>`` blocks and ``style=``
      attributes (sticky offsets, dynamic widths).

    Anything else is ``unexpected`` and should be investigated before the
    report-only candidate is ever flipped to enforced.

    Args:
        report: A normalized violation dict (see ``_normalize``).

    Returns:
        One of the four class labels above.
    """
    directive = str(report.get("directive", ""))
    blocked_uri = str(report.get("blocked_uri", ""))
    source_file = str(report.get("source_file", ""))

    if directive in _SCRIPT_DIRECTIVES and _ALPINE_ASSET in source_file:
        return KNOWN_ALPINE_EVAL
    if directive in _SCRIPT_DIRECTIVES and blocked_uri == _INLINE_URI:
        return KNOWN_INLINE_SCRIPT
    if directive in _STYLE_DIRECTIVES and blocked_uri == _INLINE_URI:
        return KNOWN_INLINE_STYLE
    return UNEXPECTED

#: Content types accepted by the ingest endpoint. ``application/json`` is
#: included for tooling/manual testing; browsers use the first two.
_ACCEPTED_CONTENT_TYPES = (
    "application/csp-report",
    "application/reports+json",
    "application/json",
)


def _pick(data: dict[str, Any], *keys: str) -> str:
    """Return the first non-empty value among kebab/camel key variants."""
    for key in keys:
        value = data.get(key)
        if value:
            return str(value)
    return ""


def _normalize(raw: dict[str, Any]) -> dict[str, str] | None:
    """Normalize one raw report body to canonical string fields."""
    if not isinstance(raw, dict):
        return None
    directive = _pick(
        raw,
        "effective-directive",
        "effectiveDirective",
        "violated-directive",
        "violatedDirective",
    )
    if not directive:
        return None
    return {
        "directive": directive,
        "blocked_uri": _pick(raw, "blocked-uri", "blockedURL", "blockedURI"),
        "document_uri": _pick(raw, "document-uri", "documentURL", "documentURI"),
        "source_file": _pick(raw, "source-file", "sourceFile"),
        "line": _pick(raw, "line-number", "lineNumber"),
    }


def parse_csp_reports(body: bytes, content_type: str) -> list[dict[str, str]]:
    """Parse a report request body into normalized violation dicts.

    Handles the legacy single-report envelope ``{"csp-report": {...}}``,
    Reporting API arrays ``[{"type": "csp-violation", "body": {...}}, ...]``,
    and bare report objects. Malformed input yields an empty list — this
    endpoint must never raise on attacker-controlled bytes.
    """
    del content_type  # both formats are sniffed from the JSON shape
    try:
        payload = loads(body)
    except (ValueError, UnicodeDecodeError):
        return []

    candidates: list[Any] = []
    if isinstance(payload, dict):
        if isinstance(payload.get("csp-report"), dict):
            candidates.append(payload["csp-report"])
        else:
            candidates.append(payload)
    elif isinstance(payload, list):
        for item in payload:
            if not isinstance(item, dict):
                continue
            if item.get("type") not in (None, "csp-violation"):
                continue
            body_obj = item.get("body")
            candidates.append(body_obj if isinstance(body_obj, dict) else item)

    out: list[dict[str, str]] = []
    for candidate in candidates:
        normalized = _normalize(candidate)
        if normalized is not None:
            out.append(normalized)
    return out


@dataclass
class CspViolation:
    """A deduped violation signature with occurrence bookkeeping."""

    directive: str
    blocked_uri: str
    document_uri: str
    source_file: str
    line: str
    classification: str = UNEXPECTED
    count: int = 1
    first_seen: str = field(
        default_factory=lambda: datetime.now(UTC).isoformat(timespec="seconds")
    )
    last_seen: str = field(
        default_factory=lambda: datetime.now(UTC).isoformat(timespec="seconds")
    )

    def as_dict(self) -> dict[str, Any]:
        return {
            "directive": self.directive,
            "blocked_uri": self.blocked_uri,
            "document_uri": self.document_uri,
            "source_file": self.source_file,
            "line": self.line,
            "classification": self.classification,
            "count": self.count,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
        }

    @property
    def is_known(self) -> bool:
        """Return True when this violation matches a documented blocker."""
        return self.classification != UNEXPECTED


class CspReportStore:
    """In-memory, signature-deduped violation store.

    Diagnostics, not audit data: contents reset on restart, and the store
    caps at :data:`MAX_SIGNATURES` distinct signatures (oldest evicted).
    A persistent backend can replace this behind the same interface later.
    """

    def __init__(self, max_signatures: int = MAX_SIGNATURES) -> None:
        self._max = max(1, max_signatures)
        self._by_signature: dict[tuple[str, str, str], CspViolation] = {}
        self.total_received = 0

    def add(self, report: dict[str, str]) -> tuple[CspViolation, bool]:
        """Record one normalized report; returns (violation, is_new)."""
        self.total_received += 1
        signature = (
            report.get("directive", ""),
            report.get("blocked_uri", ""),
            report.get("source_file", ""),
        )
        existing = self._by_signature.get(signature)
        if existing is not None:
            existing.count += 1
            existing.last_seen = datetime.now(UTC).isoformat(timespec="seconds")
            return existing, False
        violation = CspViolation(
            directive=report.get("directive", ""),
            blocked_uri=report.get("blocked_uri", ""),
            document_uri=report.get("document_uri", ""),
            source_file=report.get("source_file", ""),
            line=report.get("line", ""),
            classification=classify_csp_violation(report),
        )
        if len(self._by_signature) >= self._max:
            oldest = next(iter(self._by_signature))
            del self._by_signature[oldest]
        self._by_signature[signature] = violation
        return violation, True

    def list_violations(self) -> list[CspViolation]:
        """Return violations, most frequent first."""
        return sorted(
            self._by_signature.values(), key=lambda v: v.count, reverse=True
        )

    @property
    def known_count(self) -> int:
        """Number of distinct signatures matching a documented blocker."""
        return sum(1 for v in self._by_signature.values() if v.is_known)

    @property
    def unexpected_count(self) -> int:
        """Number of distinct signatures not matching a documented blocker."""
        return sum(1 for v in self._by_signature.values() if not v.is_known)


class CspReportEndpoint:
    """HTTP handlers for report ingestion and the operator summary."""

    def __init__(self, store: CspReportStore) -> None:
        self._store = store

    async def ingest(self, request: Request) -> Response:
        """Accept browser violation reports; always terse, never an oracle."""
        content_type = (request.headers.get("content-type") or "").lower()
        if not content_type.startswith(_ACCEPTED_CONTENT_TYPES):
            return Response(status_code=204)

        body = await request.body()
        if len(body) > MAX_REPORT_BODY_BYTES:
            return PlainTextResponse("Report too large", status_code=413)

        for report in parse_csp_reports(body, content_type):
            _violation, is_new = self._store.add(report)
            if is_new:
                logger.warning(
                    "admin.csp_violation",
                    directive=report.get("directive", ""),
                    blocked_uri=report.get("blocked_uri", ""),
                    document_uri=report.get("document_uri", ""),
                    source_file=report.get("source_file", ""),
                )
        return Response(status_code=204)

    async def list_reports(self, request: Request) -> Response:
        """Superuser-only JSON summary of collected violations."""
        user = getattr(request.state, "user", None)
        if user is None:
            return PlainTextResponse("Authentication required", status_code=401)
        if getattr(user, "is_superuser", False) is not True:
            return PlainTextResponse("Forbidden", status_code=403)
        violations = self._store.list_violations()
        return JSONResponse(
            {
                "total_received": self._store.total_received,
                "summary": {
                    "distinct": len(violations),
                    "known_blockers": self._store.known_count,
                    "unexpected": self._store.unexpected_count,
                },
                "violations": [v.as_dict() for v in violations],
            }
        )


__all__ = [
    "KNOWN_ALPINE_EVAL",
    "KNOWN_INLINE_SCRIPT",
    "KNOWN_INLINE_STYLE",
    "MAX_REPORT_BODY_BYTES",
    "MAX_SIGNATURES",
    "UNEXPECTED",
    "CspReportEndpoint",
    "CspReportStore",
    "CspViolation",
    "classify_csp_violation",
    "parse_csp_reports",
]
