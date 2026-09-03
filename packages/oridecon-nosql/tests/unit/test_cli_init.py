from __future__ import annotations

from oridecon.nosql.cli import DocumentRepositoryGenerator, NoSqlCliContributor


class TestCliInit:
    def test_exports_document_repository_generator(self) -> None:
        assert DocumentRepositoryGenerator is not None

    def test_exports_nosql_cli_contributor(self) -> None:
        assert NoSqlCliContributor is not None
