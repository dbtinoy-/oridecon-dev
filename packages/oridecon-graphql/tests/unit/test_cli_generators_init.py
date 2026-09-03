from __future__ import annotations

from oridecon.graphql.cli.generators import DataLoaderGenerator


class TestGeneratorsInit:
    def test_exports_dataloader_generator(self) -> None:
        assert DataLoaderGenerator is not None
