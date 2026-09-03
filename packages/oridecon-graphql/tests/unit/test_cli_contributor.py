from __future__ import annotations

from oridecon.contracts.cli.types import GeneratorDefinition
from oridecon.graphql.cli.contributor import GraphQLCliContributor


class TestGraphQLCliContributor:
    def test_contributor_id(self) -> None:
        contributor = GraphQLCliContributor()
        assert contributor.contributor_id == "graphql"

    def test_get_generators(self) -> None:
        contributor = GraphQLCliContributor()
        generators = contributor.get_generators()
        assert len(generators) == 1
        gen = generators[0]
        assert isinstance(gen, GeneratorDefinition)
        assert gen.name == "dataloader"
        assert gen.title == "Generate Dataloader"
        assert gen.contributor == "graphql"
        assert gen.default_output_dir == "src/schema/dataloaders"
        assert (
            gen.generator_path
            == "oridecon.graphql.cli.generators.dataloader:DataLoaderGenerator"
        )
